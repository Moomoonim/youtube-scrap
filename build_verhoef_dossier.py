"""
Verhoef 단계별 **사례 상세 카드**(dossier) 생성기.

`classify_verhoef.py`가 단계를 배정했다면, 이 스크립트는 배정된 사례 하나하나를
**연구 노트 수준으로 펼친다**. 사례집(`docs/VERHOEF_CASES.md`)이 단계별 개관이라면,
이 문서는 사례 카드다.

각 카드에 담는 것:
  · 식별   — 회사(채널)·계층·HQ·업로드일·발화 위치(vendor/media)·언어·분량
  · 단계   — 배정 단계, S1/S2/S3/S4c 원점수, 단계 혼합
  · 판정근거 — **실제로 매칭된 단계 마커**와 횟수 (왜 이 단계로 갔는지 감사 가능)
  · 주장   — "무엇을 했다"고 말하는 문장 최대 5개(행동 동사 필수, 수치 우선)
  · 수치   — 문장에서 뽑은 성과 수치 스니펫
  · 관계   — 문장에 등장한 다른 기업(고객·파트너 사례 포착)
  · 전략요소 — Verhoef Table 1의 네 축 중 해당하는 것
  · 출처   — 영상 링크 + 원본 스크립트 경로

출력:
  docs/VERHOEF_DOSSIER_S3.md   디지털 전환(BM 재구성) 사례
  docs/VERHOEF_DOSSIER_S2.md   디지털화(프로세스 최적화) 사례
  docs/VERHOEF_DOSSIER_S1.md   전산화 사례
  docs/VERHOEF_DOSSIER_S4c.md  알고리즘 전환 후보(논문 밖 보조축)

직접 실행: python build_verhoef_dossier.py   (classify_verhoef.py 를 먼저 돌릴 것)
"""

import collections
import csv
import os
import re

from classify import parse_transcript
from classify_verhoef import STAGES, ELEMENTS, STAGE_LABEL, MIN_STAGE_HITS
from extract_cases import ACTION_RE, METRIC_RE, AI_RE, NOISE_RE, split_sentences, find_mentions

csv.field_size_limit(10 ** 9)

STAGE_RE = dict(STAGES)

MAX_CLAIMS = 5
MAX_SENT_LEN = 320

# 보조 축 한글 이름 (Table 1)
ELEMENT_KO = {
    "res_asset": "디지털 자산·데이터 자산",
    "res_agility": "디지털 민첩성·애자일",
    "res_networking": "네트워킹 역량(파트너·생태계)",
    "res_bigdata": "빅데이터 분석 역량",
    "org_hierarchy": "표준 위계·사일로",
    "org_separate_unit": "분리된 전담 조직(CDO·CoE)",
    "org_embedded": "내재화된 유연 조직(전사 확산)",
    "growth_penetration": "시장침투(기존 고객 확대)",
    "growth_cocreation": "공동창출(사용자·개발자 생태계)",
    "growth_diversification": "다각화(신시장·M&A)",
    "kpi_traditional": "전통 KPI(ROI·이익·원가)",
    "kpi_digital": "디지털 KPI(활성 사용자·전환율·NPS)",
}
ELEMENT_GROUP = [
    ("디지털 자원", ["res_asset", "res_agility", "res_networking", "res_bigdata"]),
    ("조직구조", ["org_hierarchy", "org_separate_unit", "org_embedded"]),
    ("성장전략", ["growth_penetration", "growth_cocreation", "growth_diversification"]),
    ("지표", ["kpi_traditional", "kpi_digital"]),
]

SUBJECT_KO = {"channel": "공급자(공식 채널)", "keyword": "미디어·검색분"}
STANCE_KO = {"washing": "워싱(과장)", "anti_washing": "안티워싱(검증)", "neutral": "중립"}


def norm(s):
    """마커 표기를 통일해 집계한다(공백·대소문자)."""
    return re.sub(r"\s+", " ", s).strip().lower()


def matched_markers(pattern, text, top=8):
    """실제 매칭된 문자열을 세어 '왜 이 단계인지'를 감사 가능하게 만든다."""
    c = collections.Counter(norm(m.group(0)) for m in pattern.finditer(text))
    return c.most_common(top)


def claims(text, stage_key, top=MAX_CLAIMS):
    """'무엇을 했다'는 문장을 단계 마커 우선으로 골라 점수순 반환."""
    pat = STAGE_RE[stage_key]
    scored = []
    for sent in split_sentences(text):
        if NOISE_RE.search(sent) or not ACTION_RE.search(sent):
            continue
        on_stage = bool(pat.search(sent))
        has_metric = bool(METRIC_RE.search(sent))
        if not (on_stage or has_metric):
            continue
        score = (2 if on_stage else 0) + (2 if has_metric else 0) + (1 if AI_RE.search(sent) else 0)
        if score < 2:
            continue
        if len(sent) > MAX_SENT_LEN:
            sent = sent[:MAX_SENT_LEN] + "…"
        scored.append((score, on_stage, has_metric, sent))
    scored.sort(key=lambda x: (-x[0], -len(x[3])))
    seen, out = set(), []
    for score, on_stage, has_metric, sent in scored:
        key = sent[:60]
        if key in seen:
            continue
        seen.add(key)
        out.append((score, on_stage, has_metric, sent))
        if len(out) >= top:
            break
    return out


def metrics_in(sentences):
    found = []
    for _s, _o, _m, sent in sentences:
        for m in METRIC_RE.finditer(sent):
            v = m.group(0).strip()
            if v not in found:
                found.append(v)
    return found[:10]


def card(idx, row, stage_key):
    """사례 카드 한 장(마크다운)."""
    path = row["file"]
    if not os.path.exists(path):
        return ""
    meta, text = parse_transcript(path)
    cl = claims(text, stage_key)
    if not cl:
        return ""

    channel = row["channel"]
    ident = " · ".join(x for x in [row["layer"], row["hq_country"]] if x)
    lines = []
    lines.append(f"### {idx}. {channel} — {row['title']}\n")
    lines.append(f"- **식별**: {ident or '-'} · 업로드 {row['date'] or row['month']} · "
                 f"{SUBJECT_KO.get(row['source'], row['source'])} · 자막 {row['lang']} · "
                 f"{int(row['words']):,}단어 · 톤 {STANCE_KO.get(row['stance'], row['stance'])}")
    lines.append(f"- **단계**: {STAGE_LABEL[stage_key]} "
                 f"(원점수 S1 {row['s1_digitization']} / S2 {row['s2_digitalization']} / "
                 f"S3 {row['s3_transformation']} / S4c {row['s4c_algorithmic']} · 혼합 {row['stage_mix']})")

    mk = matched_markers(STAGE_RE[stage_key], text)
    lines.append("- **판정 근거(매칭 마커)**: " +
                 (", ".join(f"`{k}`×{v}" for k, v in mk) if mk else "-"))
    # 한 단어가 점수를 독식하면 단계 배정이 그 단어의 인공물일 수 있다 — 정직하게 표시한다.
    total = sum(v for _k, v in mk)
    if mk and total >= 3 and mk[0][1] / total >= 0.7:
        lines.append(f"  - ⚠️ **단일 마커 지배**: 점수의 {100*mk[0][1]/total:.0f}%가 "
                     f"`{mk[0][0]}` 하나에서 나왔다. 맥락 확인 없이 단계 사례로 쓰지 말 것.")

    els = []
    for gname, keys in ELEMENT_GROUP:
        on = [ELEMENT_KO[k] for k in keys if row.get(k) == "1"]
        if on:
            els.append(f"{gname}: " + " / ".join(on))
    lines.append("- **Table 1 전략요소**: " + (" · ".join(els) if els else "해당 없음"))

    mets = metrics_in(cl)
    lines.append("- **성과 수치(발췌)**: " + (", ".join(f"`{m}`" for m in mets) if mets else "없음 — 수치 없는 주장"))

    mentions = []
    for _s, _o, _m, sent in cl:
        for name in find_mentions(sent, channel):
            if name not in mentions:
                mentions.append(name)
    lines.append("- **언급된 다른 기업**: " + (", ".join(mentions[:8]) if mentions else "-"))

    lines.append(f"- **출처**: [영상]({meta['url']}) · [스크립트](../{path})\n")
    lines.append("**무엇을 했다고 말하는가 (스크립트 발췌)**\n")
    for j, (_score, on_stage, has_metric, sent) in enumerate(cl, 1):
        flag = []
        if on_stage:
            flag.append("단계마커")
        if has_metric:
            flag.append("수치")
        lines.append(f"{j}. {sent}  \n   <sub>({' · '.join(flag) or '행동'})</sub>")
    lines.append("")
    return "\n".join(lines)


HEAD = """# Verhoef {label} — 사례 상세 카드

> `build_verhoef_dossier.py` 자동 생성 · 이론틀: Verhoef et al.(2021), *JBR* 122, 889–901.
> 개관·통계는 [`VERHOEF_CASES.md`](VERHOEF_CASES.md), 전량 기계판독본은
> `analysis/verhoef_stages.csv`.

**{label}** 정의 — {defn}

수록 {n:,}건 / {c:,}개 회사·채널. 카드 순서는 **단계 신호 강도 → 근거 강도** 순.

각 카드의 읽는 법:
- **판정 근거(매칭 마커)** — 이 영상을 해당 단계로 배정한 실제 어휘와 횟수. 태깅을 감사할 수 있다.
- **무엇을 했다고 말하는가** — 행동 동사가 든 문장만 발췌. `단계마커`는 그 문장에 단계 어휘가
  함께 있다는 뜻이고, `수치`는 성과 숫자가 붙어 있다는 뜻이다.
- ⚠️ 자동자막 기반 1차 발췌다. **발화 주체(벤더 홍보 vs 도입 기업 증언)와 맥락은
  원본 스크립트로 확인한 뒤 인용할 것.**

---

"""

DEFN = {
    "s1_digitization": "아날로그 정보의 디지털 변환. 가치창출 활동 자체는 바꾸지 않는다. 목표는 비용 절감.",
    "s2_digitalization": "디지털 기술로 **기존 비즈니스 프로세스**를 변경·최적화. 비용 절감과 고객경험 개선을 동시에 지향.",
    "s3_transformation": "전사적 차원에서 **새로운 비즈니스 모델**과 가치창출·전유 로직을 도입. 사업 논리 자체가 재구성된다.",
    "s4c_algorithmic": "논문 밖 보조축. 의사결정의 알고리즘화·자율 에이전트·AI 인력화 — 3단계로 담기지 않는 잔여를 표시한다.",
}
FILE = {
    "s1_digitization": "VERHOEF_DOSSIER_S1.md",
    "s2_digitalization": "VERHOEF_DOSSIER_S2.md",
    "s3_transformation": "VERHOEF_DOSSIER_S3.md",
    "s4c_algorithmic": "VERHOEF_DOSSIER_S4c.md",
}


def build(rows, stage_key):
    if stage_key == "s4c_algorithmic":
        sub = [r for r in rows if int(r["s4c_algorithmic"]) >= MIN_STAGE_HITS]
        sub.sort(key=lambda r: (-int(r["s4c_algorithmic"]), -int(r["evidence_strength"])))
    else:
        sub = [r for r in rows if r["verhoef_stage"] == stage_key]
        sub.sort(key=lambda r: (-int(r[stage_key]), -int(r["evidence_strength"])))

    cards, companies = [], []
    for r in sub:
        c = card(len(cards) + 1, r, stage_key)
        if c:
            cards.append(c)
            companies.append(r["channel"])

    path = os.path.join("docs", FILE[stage_key])
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(HEAD.format(label=STAGE_LABEL[stage_key], defn=DEFN[stage_key],
                             n=len(cards), c=len(set(companies))))
        # 회사별 색인
        cnt = collections.Counter(companies)
        fp.write("## 회사·채널 색인\n\n")
        fp.write(" · ".join(f"{k}({v})" for k, v in cnt.most_common()) + "\n\n---\n\n")
        fp.write("## 사례 카드\n\n")
        fp.write("\n".join(cards))
    return path, len(cards), len(set(companies))


def main():
    src = os.path.join("analysis", "verhoef_stages.csv")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8-sig"))
            if r["relevance"] == "ax_core"]
    for key in ("s3_transformation", "s2_digitalization", "s1_digitization", "s4c_algorithmic"):
        path, n, c = build(rows, key)
        print(f"[dossier] {STAGE_LABEL[key]}: 카드 {n:,}장 / {c:,}개 회사 → {path}")


if __name__ == "__main__":
    main()
