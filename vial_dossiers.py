"""
Vial(2019) 사례 상세 정리(dossier) 생성기 — map_vial.py 가 뽑은 사례를 건별로 펼친다.

map_vial.py 는 '어떤 영상이 Vial 프레임워크에 걸리는가'까지만 답한다.
이 스크립트는 그 사례 하나하나를 **사례집(case dossier) 형식**으로 상세화한다:

  ① 메타 (채널·스택계층·본사국가·이벤트·업로드일·언어·분량·관련성/톤)
  ② 개요 발췌 (summarize.py 의 문장경계 요약)
  ③ 사슬 판독 (B1→…→B7/B8 중 실제로 성립한 경로 + 빠진 블록)
  ④ 구성요소별 근거 문장 (블록마다 최대 3문장, 원문 발췌)
  ⑤ 수치 주장 (행동 동사 + 성과 수치가 함께 있는 문장)
  ⑥ AX 교량 3축(X1 정의확장 · X2 윤리 · X3 동적역량) 근거
  ⑦ 등장 요소 (기능 10범주 · 기술 스택 · 인물 · 언급 기업)

출력:
  docs/VIAL_CASES_A_B.md   — 티어 A(사슬 완성)·B(사슬 대부분) 전건 상세 정리
  docs/VIAL_CASES_C.md     — 티어 C(부분 사례) 전건 요약 정리
  analysis/vial_dossiers.csv — 정리 내용의 기계 판독본(1행=1사례)

직접 실행: python vial_dossiers.py   (map_vial.py 를 먼저 돌려 vial_cases.csv 가 있어야 함)
"""

import csv
import os
import re
import sys

from build_catalog import CAP, CH2HQ, CH2LAYER, COMPANIES, EVENTS, PEOPLE, TECH, detect
from classify import parse_transcript
from extract_cases import ACTION_RE, METRIC_RE
from map_vial import (BRIDGES, CONSTRUCTS, X_MEANS, X_MEANS_AX, X_MEANS_DX,
                      count, split_sentences)
from summarize import summarize_text

EVIDENCE_PER_CONSTRUCT = 3
MAX_SENT_LEN = 260
MAX_METRIC_CLAIMS = 6

BLOCK_ORDER = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"]
BLOCK_SHORT = {
    "B1": "기술 활용", "B2": "파괴", "B3": "전략 대응", "B4": "가치창출 경로",
    "B5": "구조 변화", "B6": "장벽", "B7": "긍정 성과", "B8": "부정 성과",
}
CONSTRUCT_LABEL = {k: (blk, label) for k, blk, label, _p in CONSTRUCTS + BRIDGES}
CONSTRUCT_PATS = {k: p for k, _b, _l, p in CONSTRUCTS + BRIDGES}


def clip(s, n=MAX_SENT_LEN):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + "…"


def top_evidence(patterns, sentences, k=EVIDENCE_PER_CONSTRUCT):
    """구성요소를 대표하는 문장 k개 — 서로 다른 패턴을 많이 맞힌 순."""
    scored = []
    for sent in sentences:
        n = sum(1 for p in patterns if p.search(sent))
        if n:
            scored.append((n, -abs(len(sent) - 160), sent))
    scored.sort(key=lambda x: (-x[0], -x[1]))
    out, seen = [], set()
    for _n, _d, sent in scored:
        key = sent[:40]
        if key in seen:
            continue
        seen.add(key)
        out.append(clip(sent))
        if len(out) >= k:
            break
    return out


def metric_claims(sentences, k=MAX_METRIC_CLAIMS):
    """'무엇을 했다 + 수치' 문장 — 사례의 성과 주장 후보."""
    out = []
    for sent in sentences:
        if not (ACTION_RE.search(sent) and METRIC_RE.search(sent)):
            continue
        if len(sent) < 25:
            continue
        out.append(clip(sent))
        if len(out) >= k:
            break
    return out


def chain_reading(blocks_present, row):
    """성립한 블록으로 Vial 과정 사슬을 한 줄 판독하고, 빠진 블록을 명시한다."""
    chain = " → ".join(f"{b} {BLOCK_SHORT[b]}" for b in BLOCK_ORDER if b in blocks_present)
    missing = [f"{b} {BLOCK_SHORT[b]}" for b in BLOCK_ORDER if b not in blocks_present]
    notes = []
    if "B3" in blocks_present and "B5" in blocks_present:
        notes.append("전략 선언이 조직 변화 언급까지 이어짐")
    if "B7" in blocks_present and "B6" in blocks_present:
        notes.append("성과와 장벽을 함께 말함(자기검증형 서술)")
    if "B8" in blocks_present and "B7" not in blocks_present:
        notes.append("리스크만 말하고 편익은 말하지 않음")
    if "B2" not in blocks_present:
        notes.append("외부 파괴(불확실성의 소재) 언급 없이 내부 도입 서사")
    if row["val_proposition"] == "1":
        notes.append("가치제안 재정의까지 건드림(드문 유형)")
    if row["pos_society"] == "1":
        notes.append("사회적 편익까지 언급(드문 유형)")
    return chain, missing, notes


def bridges_of(row):
    return [(k, CONSTRUCT_LABEL[k][1]) for k, _b, _l, _p in BRIDGES if row[k] == "1"]


def build(row):
    path = row["file"]
    meta, text = parse_transcript(path)
    sentences = split_sentences(text)

    blocks = set(row["vial_block_list"].split("·")) if row["vial_block_list"] else set()
    chain, missing, notes = chain_reading(blocks, row)

    evid = {}
    for key, blk, label, pats in CONSTRUCTS:
        if row[key] == "1":
            evid[key] = top_evidence(pats, sentences)
    bridge_evid = {}
    for key, blk, label, pats in BRIDGES:
        if row[key] == "1":
            pool = pats + (X_MEANS_DX + X_MEANS_AX if key == "bridge_means" else [])
            bridge_evid[key] = top_evidence(pool, sentences, k=2)

    dx_n, ax_n = count(X_MEANS_DX, text), count(X_MEANS_AX, text)

    return {
        "row": row, "meta": meta,
        "summary": clip(summarize_text(text), 400),
        "chain": chain, "missing": missing, "notes": notes,
        "evidence": evid, "bridge_evidence": bridge_evid,
        "claims": metric_claims(sentences),
        "layer": CH2LAYER.get(row["channel"], "(미분류)"),
        "hq": CH2HQ.get(row["channel"], "—"),
        "event": detect(EVENTS, text) or "—",
        "caps": detect(CAP, text) or "—",
        "techs": detect(TECH, text) or "—",
        "people": detect(PEOPLE, text) or "—",
        "companies": detect(COMPANIES, text) or "—",
        "dx_n": dx_n, "ax_n": ax_n,
    }


def render_full(d, idx):
    """티어 A·B — 전체 상세 정리."""
    r, o = d["row"], []
    o.append(f"\n### {idx}. {r['title']}\n")
    o.append(f"**{r['channel']}** · {d['layer']} · {d['hq']} · {r['month']} · {r['lang']} · "
             f"{int(r['words']):,}단어 · `{r['relevance']}`/`{r['stance']}` · "
             f"티어 **{r['tier']}**({r['vial_blocks']}/8블록)")
    if d["event"] != "—":
        o.append(f"· 이벤트: {d['event']}")
    o.append(f"\n[영상 보기]({r['url']}) · 원문 `{r['file']}`\n")

    o.append(f"**사슬 판독**: {d['chain']}")
    if d["missing"]:
        o.append(f"  · *빠진 블록*: {', '.join(d['missing'])}")
    for n in d["notes"]:
        o.append(f"  · *{n}*")
    o.append("")

    o.append(f"**개요(발췌)**: {d['summary']}\n")

    if d["claims"]:
        o.append("**수치를 동반한 주장**")
        for c in d["claims"]:
            o.append(f"- {c}")
        o.append("")

    o.append("**구성요소별 근거**\n")
    o.append("| 블록 | 구성요소 | 적중 | 근거 문장(원문 발췌) |")
    o.append("|---|---|---:|---|")
    for key, blk, label, _p in CONSTRUCTS:
        if key not in d["evidence"]:
            continue
        sents = "<br>".join("· " + s.replace("|", "/") for s in d["evidence"][key])
        o.append(f"| {blk} | {label} | {r[key + '_n']} | {sents} |")
    o.append("")

    br = bridges_of(r)
    if br:
        o.append("**AX 연계 교량**\n")
        for key, label in br:
            extra = ""
            if key == "bridge_means":
                extra = (f" (명시 발화 {r['bridge_means_explicit']}회 · "
                         f"DX 어휘 {d['dx_n']} / AX 어휘 {d['ax_n']})")
            o.append(f"- **{label}**{extra}")
            for s in d["bridge_evidence"].get(key, []):
                o.append(f"  - {s}")
        o.append("")

    o.append(f"**등장 요소** — 기능: {d['caps']} / 기술: {d['techs']} / "
             f"인물: {d['people']} / 언급 기업: {d['companies']}\n")
    o.append("---")
    return "\n".join(o)


def render_compact(d, idx):
    """티어 C — 요약 정리."""
    r, o = d["row"], []
    o.append(f"\n**{idx}. [{r['title']}]({r['url']})** — {r['channel']} · {d['layer']} · "
             f"{d['hq']} · {r['month']} · {r['lang']} · {r['vial_blocks']}/8블록 · "
             f"`{r['relevance']}`/`{r['stance']}`")
    o.append(f"- 사슬: {d['chain']}" + (f" · 빠짐: {', '.join(d['missing'])}" if d["missing"] else ""))
    o.append(f"- 개요: {clip(d['summary'], 220)}")
    strongest = sorted(
        [k for k in d["evidence"]], key=lambda k: -int(r[k + "_n"]))[:2]
    for key in strongest:
        blk, label = CONSTRUCT_LABEL[key]
        if d["evidence"][key]:
            o.append(f"- {blk} {label}: {d['evidence'][key][0]}")
    if d["claims"]:
        o.append(f"- 수치 주장: {d['claims'][0]}")
    br = ", ".join(label for _k, label in bridges_of(r))
    o.append(f"- 교량: {br or '—'} · 기술: {d['techs']}")
    o.append(f"- 원문: `{r['file']}`")
    return "\n".join(o)


def header(title, note, n):
    return (f"# {title}\n\n"
            f"> 자동 생성: `python vial_dossiers.py` · 근거 문헌: Vial, G. (2019). "
            f"Understanding digital transformation: A review and a research agenda. "
            f"*JSIS, 28*(2), 118–144.\n\n"
            f"> {note} **총 {n:,}건**. 사례 선정·티어 기준은 `docs/VIAL_CASES.md` §1 참조.\n\n"
            f"> 근거 문장은 자동 자막 원문 발췌라 오탈자·오역이 있을 수 있다(대리지표로만 사용).\n")


def main():
    src = "analysis/vial_cases.csv"
    if not os.path.exists(src):
        sys.exit("analysis/vial_cases.csv 가 없다. 먼저 `python map_vial.py` 를 실행할 것.")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8-sig")) if r["tier"]]
    ab = sorted([r for r in rows if r["tier"] in ("A", "B")],
                key=lambda r: (r["tier"], -int(r["vial_blocks"]), r["channel"]))
    c = sorted([r for r in rows if r["tier"] == "C"],
               key=lambda r: (r["channel"], r["month"]))

    os.makedirs("docs", exist_ok=True)
    dossier_rows = []

    # ── 티어 A·B 상세 ──
    parts = [header("Vial(2019) 프레임워크 사례 상세 — 티어 A·B",
                    "과정 사슬이 온전한(A) 또는 대부분 충족한(B) 사례를 건별로 펼친 정리본.",
                    len(ab))]
    cur_tier = None
    for i, r in enumerate(ab, 1):
        d = build(r)
        if r["tier"] != cur_tier:
            cur_tier = r["tier"]
            title = ("티어 A — 기술→파괴/전략→가치·구조→성과 사슬이 온전한 사례"
                     if cur_tier == "A" else "티어 B — 사슬 대부분(6블록) 충족 사례")
            parts.append(f"\n---\n\n## 티어 {cur_tier}: {title}\n")
        parts.append(render_full(d, i))
        dossier_rows.append(flatten(d))
    open("docs/VIAL_CASES_A_B.md", "w", encoding="utf-8").write("\n".join(parts) + "\n")

    # ── 티어 C 요약 ──
    parts = [header("Vial(2019) 프레임워크 사례 상세 — 티어 C(부분 사례)",
                    "8블록 중 4~5개만 성립한 부분 사례. 단일 구성요소 분석·보조 표본용.",
                    len(c))]
    cur_ch = None
    for i, r in enumerate(c, 1):
        d = build(r)
        if r["channel"] != cur_ch:
            cur_ch = r["channel"]
            parts.append(f"\n---\n\n## {cur_ch}\n")
        parts.append(render_compact(d, i))
        dossier_rows.append(flatten(d))
    open("docs/VIAL_CASES_C.md", "w", encoding="utf-8").write("\n".join(parts) + "\n")

    fields = list(dossier_rows[0].keys())
    with open("analysis/vial_dossiers.csv", "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields)
        w.writeheader()
        w.writerows(dossier_rows)

    print(f"[vial_dossiers] 티어 A·B {len(ab)}건 → docs/VIAL_CASES_A_B.md")
    print(f"                티어 C   {len(c)}건 → docs/VIAL_CASES_C.md")
    print(f"                기계 판독본 {len(dossier_rows)}행 → analysis/vial_dossiers.csv")


def flatten(d):
    r = d["row"]
    return {
        "tier": r["tier"], "blocks": r["vial_blocks"], "block_list": r["vial_block_list"],
        "channel": r["channel"], "layer": d["layer"], "hq": d["hq"], "month": r["month"],
        "title": r["title"], "lang": r["lang"], "words": r["words"],
        "relevance": r["relevance"], "stance": r["stance"], "event": d["event"],
        "chain": d["chain"], "missing_blocks": ", ".join(d["missing"]),
        "reading_notes": " / ".join(d["notes"]),
        "summary": d["summary"],
        "metric_claims": " || ".join(d["claims"]),
        "evidence": " || ".join(f"[{CONSTRUCT_LABEL[k][0]} {CONSTRUCT_LABEL[k][1]}] " + " ; ".join(v)
                                for k, v in d["evidence"].items()),
        "bridges": ", ".join(label for _k, label in bridges_of(r)),
        "capabilities": d["caps"], "technologies": d["techs"],
        "people": d["people"], "companies_mentioned": d["companies"],
        "url": r["url"], "file": r["file"],
    }


if __name__ == "__main__":
    main()
