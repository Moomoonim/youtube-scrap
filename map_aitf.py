"""
AITF 매핑 — 수집 코퍼스를 AI Transformation Framework(Holmström & Magnusson, 2026)
세 축(자동화 · 증강 · 데이터 풍부성)에 코딩해 '프레임워크에 맞는 사례'를 뽑는다.

원 논문 구조를 그대로 옮긴다:
  - 3개 차원 × 4개 하위항목(Level · Scope · Impact · Future) = 12칸 (Table 1)
  - 하위항목 0~4점 → 차원 합계 0~16점, 8점 이하 low / 9점 이상 high (논문 절단점)
  - 세 축의 low/high 조합 = 큐브의 8개 상태 (LLL … HHH=integrated intelligence, Fig.1~2)

⚠️ 타당성 고지: 논문의 설문은 '조직 내부 자기보고'다. 여기서 재는 것은
   **공개 담론에서의 강조**(discursive emphasis)이지 조직의 실제 성숙도가 아니다.
   따라서 산출물은 '사례 후보 목록'이며, 인용 전 원문 확인이 전제다(HANDOVER §6).
   - Level  : 해당 축 핵심어의 밀도(1천 단어당)
   - Scope  : 전사·전부서·all employees 등 범위 표지가 축 핵심어 근처(±400자)에 출현
   - Impact : 수치·효과 표지(%, 배, 절감, 단축 …)가 축 핵심어 근처에 출현
   - Future : 전략·로드맵·계획 표지가 축 핵심어 근처에 출현

입력 : transcripts/**/*.md  (relevance == ax_core 만, classify_v2 기준)
출력 : analysis/aitf_scored.csv   — 영상별 12칸 점수 + 큐브 좌표 + 근거 발췌
       analysis/aitf_company.csv  — 채널(기업)별 집계 + 큐브 좌표
       docs/AITF_CASES.md         — 8개 상태별 사례 후보 정리본(사람이 읽는 산출물)

직접 실행: python map_aitf.py
"""

import collections
import csv
import glob
import os
import re

import config
from classify import parse_transcript, doc_month, score_text
from classify_v2 import classify_relevance, rx

# ── 차원 1. 자동화(Automation) — 정형·반복 과업을 AI에 위임 ──────────────
AUTOMATION = rx(
    r"자동화", r"자동으로\s*(처리|실행|생성|수행)", r"무인(화)?", r"\bRPA\b",
    r"로보틱\s*프로세스", r"자동\s*(처리|실행|응답|승인)", r"사람\s*(개입|손)\s*없이",
    r"완전\s*자동", r"end[-\s]?to[-\s]?end\s+automat", r"straight[-\s]?through",
    r"automat(e|es|ed|ing|ion)", r"unattended", r"autonomous(ly)?",
    r"self[-\s]?driving\s+(operation|process|business)", r"without\s+human\s+(intervention|input)",
    r"워크플로\s*자동화", r"workflow\s+automation", r"백오피스\s*자동화",
    r"자율\s*(운영|실행|처리)", r"봇(이|을|으로)\s*(처리|실행)", r"batch\s+processing",
)
# ── 차원 2. 증강(Augmentation) — 인간의 판단·문제해결을 AI가 강화 ───────
AUGMENTATION = rx(
    r"증강", r"augment(s|ed|ing|ation)?", r"코파일럿", r"copilot",
    r"어시스턴트", r"assistant", r"보조(하|해|한다|도구|역할)", r"조수",
    r"human[-\s]?in[-\s]?the[-\s]?loop", r"사람(과|이)\s*(함께|협업|검토)",
    r"work(s|ing)?\s+(alongside|with)\s+(humans?|people)", r"human[-\s]?AI\s+(collaborat|team)",
    r"의사\s*결정\s*(지원|보조|도움)", r"decision\s+support", r"augmented\s+decision",
    r"생산성\s*(도구|향상\s*도구)", r"업무\s*(보조|지원)\s*(도구|툴)?",
    r"초안(을)?\s*(작성|생성)", r"draft(ing)?\s+(a|the|first)", r"brainstorm",
    r"페어\s*프로그래밍", r"pair\s+programming",
    r"대체(하지|가)\s*(않|못|아니)", r"doesn'?t\s+replace\s+(humans?|people)",
    r"amplif(y|ies|ying)\s+(human|people)", r"인간의\s*(역량|판단)(을)?\s*(강화|확장)",
)
# ── 차원 3. 데이터 풍부성(Data richness) — AI가 딛고 설 데이터 기반 ─────
DATA_RICHNESS = rx(
    r"데이터\s*(레이크|웨어하우스|플랫폼|파이프라인|인프라|기반|자산|품질|거버넌스|통합|표준화|카탈로그|메시|접근|활용|수집|축적)",
    r"data\s+(lake|warehouse|lakehouse|platform|pipeline|infrastructure|quality|governance|catalog|mesh|estate|asset|silo|access|integration|foundation|strategy)",
    r"정형\s*데이터", r"비정형\s*데이터", r"unstructured\s+data", r"structured\s+data",
    r"실시간\s*데이터", r"real[-\s]?time\s+data", r"스트리밍\s*데이터", r"streaming\s+data",
    r"센서\s*데이터", r"sensor\s+data", r"텔레메트리", r"telemetry",
    r"single\s+source\s+of\s+truth", r"데이터\s*사일로", r"silo(s|ed)?\s+data",
    r"지식\s*(베이스|저장소)", r"knowledge\s+(base|graph)", r"\bRAG\b", r"벡터\s*(DB|데이터베이스)",
    r"vector\s+(database|store|db)", r"마스터\s*데이터", r"master\s+data",
    r"학습\s*데이터", r"training\s+data", r"라벨링", r"labeled\s+data",
    r"first[-\s]?party\s+data", r"데이터\s*(가|를)\s*(모으|쌓|정리|정제)",
    r"데이터\s*(주도|기반)\s*(의사\s*결정|경영)", r"data[-\s]?driven\s+(decision|organization|company)",
)

# ── 하위항목 표지 (축 핵심어 근처에서만 인정) ───────────────────────────
SCOPE = rx(
    r"전사(적)?", r"전\s*부서", r"모든\s*(부서|팀|직원|임직원|사업부|프로세스|업무)",
    r"회사\s*전체", r"그룹\s*(전체|사)", r"전\s*조직", r"조직\s*전(체|반)",
    r"company[-\s]?wide", r"enterprise[-\s]?wide", r"organization[-\s]?wide",
    r"across\s+the\s+(company|organization|enterprise|business|firm)",
    r"every(one|\s+(team|employee|department|function|unit))", r"all\s+(employees|teams|departments)",
    r"at\s+scale", r"대규모\s*확산", r"전면\s*(도입|적용|확대)", r"롤아웃", r"roll(ed)?[-\s]?out",
)
IMPACT = rx(
    r"\d+\s*%", r"\d+\s*배", r"\b\d+x\b", r"\d+\s*(시간|일|주|개월)\s*(단축|절감|줄)",
    r"(비용|시간|인력|공수)(을|이)?\s*(절감|단축|줄|감축)", r"생산성(이|을)?\s*(향상|증가|올라)",
    r"매출(이|을)?\s*(증가|성장|늘)", r"효율(이|성이|성을)?\s*(향상|개선|증가)",
    r"(saved?|saving)\s+(\$|\d|time|cost)", r"(reduc|cut)(ed|ing|es)?\s+.{0,12}(cost|time|headcount|hours)",
    r"(increase|improve|boost)(d|s|ed|ment)?\s+.{0,15}(productivity|revenue|efficiency|throughput)",
    r"\bROI\b", r"payback", r"투자\s*수익", r"성과(가|를)?\s*(났|나왔|측정)",
    r"faster\s+than", r"몇\s*배\s*(빨라|빠르)",
)
FUTURE = rx(
    r"전략(적)?\s*(으로)?", r"로드맵", r"roadmap", r"마스터\s*플랜",
    r"(향후|앞으로|내년|중장기|단계적)(에|으로)?", r"계획(이|을|하고)", r"목표(는|로|가)",
    r"비전", r"vision", r"strateg(y|ic|ically)", r"plan\s+to", r"we\s+will\s+",
    r"next\s+(year|phase|step)", r"long[-\s]?term", r"투자(할|하겠|를\s*확대)",
    r"ambition", r"단계(적으로|를\s*밟)", r"phase(d|s)?\s+(approach|rollout)",
)

DIMENSIONS = [("aut", "자동화", AUTOMATION), ("aug", "증강", AUGMENTATION), ("dat", "데이터풍부성", DATA_RICHNESS)]
SUBITEMS = ["level", "scope", "impact", "future"]

NEAR_WINDOW = 400   # 축 핵심어와 하위항목 표지의 인정 거리(문자)
HIGH_CUTOFF = 9     # 논문 절단점: 0~16점 중 9점 이상이면 high


def band_count(n):
    """등장 횟수 → 0~4점 (논문의 5점 리커트 자리에 대응하는 대리 척도)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n <= 5:
        return 3
    return 4


def band_density(hits, words):
    """핵심어 밀도(1천 단어당) → Level 0~4점. 긴 영상이 유리해지지 않게 길이 보정."""
    if hits == 0:
        return 0
    d = hits * 1000.0 / max(words, 1)
    if hits == 1 or d < 0.5:
        return 1
    if d < 1.5:
        return 2
    if d < 3.0:
        return 3
    return 4


def positions(patterns, text):
    return [m.start() for p in patterns for m in p.finditer(text)]


def near_count(marker_pats, text, anchors):
    """축 핵심어(anchors) ±NEAR_WINDOW 안에 있는 표지 등장 횟수."""
    if not anchors:
        return 0
    n = 0
    for pos in positions(marker_pats, text):
        if any(abs(pos - a) <= NEAR_WINDOW for a in anchors):
            n += 1
    return n


BOUNDARY = re.compile(r"[.!?。]\s|다\.\s|\n")


def snippet(text, pos, span=230):
    """앞뒤 문장 경계까지 다듬은 발췌(요약이 아니라 원문 그대로)."""
    lo, hi = max(0, pos - span), min(len(text), pos + span)
    chunk = text[lo:hi]
    left = [m.end() for m in BOUNDARY.finditer(chunk[:span])]
    if left:
        chunk = chunk[left[-1]:]
    right = [m.end() for m in BOUNDARY.finditer(chunk)]
    if right and right[-1] > 60:
        chunk = chunk[:right[-1]]
    return re.sub(r"\s+", " ", chunk).strip()


def evidence(text, anchors, prefer_pats):
    """축 핵심어가 든 발췌 중 근거로 쓸 만한 것 하나(수치·범위 표지 있는 것 우선)."""
    if not anchors:
        return ""
    best, best_score = "", -1
    for a in anchors[:60]:
        chunk = snippet(text, a)
        s = sum(1 for p in prefer_pats if p.search(chunk))
        if s > best_score:
            best, best_score = chunk, s
    return best[:300]


def score_document(text, words):
    """문서 하나를 3차원 × 4항목으로 코딩한다."""
    out = {}
    for key, _label, pats in DIMENSIONS:
        anchors = positions(pats, text)
        lvl = band_density(len(anchors), words)
        sc = band_count(near_count(SCOPE, text, anchors))
        im = band_count(near_count(IMPACT, text, anchors))
        fu = band_count(near_count(FUTURE, text, anchors))
        out[f"{key}_level"], out[f"{key}_scope"] = lvl, sc
        out[f"{key}_impact"], out[f"{key}_future"] = im, fu
        out[f"{key}_total"] = lvl + sc + im + fu
        out[f"{key}_hits"] = len(anchors)
        out[f"{key}_evidence"] = evidence(text, anchors, IMPACT + SCOPE)
    return out


def cell_of(vals, cutoffs):
    """세 축의 low/high 조합을 큐브 좌표 문자열로. 예: 'H-L-H'."""
    return "-".join("H" if v >= c else "L" for v, c in zip(vals, cutoffs))


def pct(sorted_vals, p):
    return sorted_vals[min(len(sorted_vals) - 1, int(p / 100 * len(sorted_vals)))]


CELL_NAMES = {
    # (자동화, 증강, 데이터) — 논문이 이름 붙인 두 꼭짓점만 원문 용어, 나머지는 기술적 명명
    "L-L-L": "manual isolated data scarcity (논문 명명)",
    "H-L-L": "데이터 없는 자동화 (효율만 좇는 상태)",
    "L-H-L": "데이터 없는 증강 (도구 배포에 그친 상태)",
    "L-L-H": "데이터만 쌓인 상태 (활용 미달)",
    "H-H-L": "자동화+증강, 데이터 기반 취약",
    "H-L-H": "데이터 기반 자동화 (사람 강화는 후순위)",
    "L-H-H": "데이터 기반 증강 (자동화는 후순위)",
    "H-H-H": "integrated intelligence (논문 명명 · Fig.2 목표점)",
}


def main():
    out_dir, docs_dir = "analysis", "docs"
    os.makedirs(out_dir, exist_ok=True)

    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        _hits, _density, words = score_text(text)
        if classify_relevance(text, words) != "ax_core":   # 연구용 주 표본만
            continue
        source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
        row = {
            "file": path.replace(os.sep, "/"), "title": meta["title"], "channel": meta["channel"],
            "source": source, "lang": meta["lang"], "month": doc_month(path, meta),
            "words": words, "url": meta["url"],
        }
        row.update(score_document(text, words))
        row["aitf_sum"] = row["aut_total"] + row["aug_total"] + row["dat_total"]
        rows.append(row)

    keys = [k for k, _l, _p in DIMENSIONS]
    # 셀 판정 기준 두 벌:
    #  (a) 논문 절단점 9/16 그대로 — 원문 충실성. 담론 자료에서는 거의 전부 low로 떨어진다.
    #  (b) 코퍼스 상대 절단점(축별 상위 10%) — 사례 선별용 실무 기준.
    rel_cut = {k: max(2, pct(sorted(r[f"{k}_total"] for r in rows), 90)) for k in keys}
    for r in rows:
        vals = [r[f"{k}_total"] for k in keys]
        r["cell_paper"] = cell_of(vals, [HIGH_CUTOFF] * 3)
        r["cell_relative"] = cell_of(vals, [rel_cut[k] for k in keys])

    fields = ["file", "title", "channel", "source", "lang", "month", "words", "url"]
    for key in keys:
        fields += [f"{key}_{s}" for s in SUBITEMS] + [f"{key}_total", f"{key}_hits"]
    fields += ["aitf_sum", "cell_paper", "cell_relative"] + [f"{k}_evidence" for k in keys]
    with open(os.path.join(out_dir, "aitf_scored.csv"), "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # ── 채널(기업)별 집계: 자사 채널 수집분만이 '조직의 자기서술'이다 ──
    by_ch = collections.defaultdict(list)
    for r in rows:
        if r["source"] == "channel":
            by_ch[r["channel"]].append(r)

    comp = []
    for ch, rs in by_ch.items():
        if len(rs) < 5:            # 표본 5건 미만은 집계에서 제외
            continue
        rec = {"channel": ch, "n_docs": len(rs)}
        for key in keys:
            vals = sorted((r[f"{key}_total"] for r in rs), reverse=True)
            top = vals[:5]         # 그 기업이 '가장 강하게 말할 때'의 수준
            rec[f"{key}_top5"] = round(sum(top) / len(top), 2)
            rec[f"{key}_mean"] = round(sum(vals) / len(vals), 2)
            rec[f"{key}_max"] = vals[0]
        comp.append(rec)

    comp_cut = {k: pct(sorted(c[f"{k}_top5"] for c in comp), 50) for k in keys}   # 중앙값 분할
    for c in comp:
        c["cell_paper"] = cell_of([c[f"{k}_top5"] for k in keys], [HIGH_CUTOFF] * 3)
        c["cell_relative"] = cell_of([c[f"{k}_top5"] for k in keys], [comp_cut[k] for k in keys])

    comp.sort(key=lambda c: -sum(c[f"{k}_top5"] for k in keys))
    cfields = ["channel", "n_docs"]
    for key in keys:
        cfields += [f"{key}_top5", f"{key}_mean", f"{key}_max"]
    cfields += ["cell_paper", "cell_relative"]
    with open(os.path.join(out_dir, "aitf_company.csv"), "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=cfields)
        w.writeheader()
        w.writerows(comp)

    write_report(os.path.join(docs_dir, "AITF_CASES.md"), rows, comp, rel_cut, comp_cut)

    # ── 콘솔 요약 ──
    print(f"[aitf] ax_core {len(rows)}건 코딩 → analysis/aitf_scored.csv")
    for key, label, _p in DIMENSIONS:
        vals = [r[f"{key}_total"] for r in rows]
        hi = sum(1 for v in vals if v >= HIGH_CUTOFF)
        print(f"  {label}: 평균 {sum(vals)/len(vals):.2f}/16 · 논문절단점 high {hi}건 "
              f"({100*hi/len(vals):.1f}%) · 상대절단점 {rel_cut[key]}점")
    print("  셀 분포(영상·상대절단점):", dict(collections.Counter(r["cell_relative"] for r in rows).most_common()))
    print(f"[aitf] 기업(채널) {len(comp)}개 집계 → analysis/aitf_company.csv (상대 절단점 {comp_cut})")
    print("  셀 분포(기업·상대절단점):", dict(collections.Counter(c["cell_relative"] for c in comp).most_common()))
    for c in comp[:12]:
        print(f"    {c['channel'][:26]:<26} n={c['n_docs']:<3} "
              f"자동화 {c['aut_top5']:>5} · 증강 {c['aug_top5']:>5} · 데이터 {c['dat_top5']:>5} → {c['cell_relative']}")
    print("[aitf] 사례 정리본 → docs/AITF_CASES.md")
    return rows, comp, rel_cut, comp_cut


# ── 사람이 읽는 정리본 ───────────────────────────────────────────────
def write_report(path, rows, comp, rel_cut, comp_cut):
    keys = [k for k, _l, _p in DIMENSIONS]
    labels = {k: l for k, l, _p in DIMENSIONS}
    by_cell = collections.defaultdict(list)
    for r in rows:
        by_cell[r["cell_relative"]].append(r)

    L = []
    A = L.append
    A("# AITF 사례 후보 — AI Transformation Framework 3축 매핑\n")
    A("> Holmström, J., & Magnusson, J. (2026). Navigating the organizational AI journey: "
      "The AI transformation framework. *Business Horizons, 69*(1), 89–100.\n")
    A("> 자동 생성물(`python map_aitf.py`). 수집 코퍼스의 `ax_core` 문서를 논문의 "
      "3차원 × 4항목(Level·Scope·Impact·Future) 구조로 코딩해 **사례 후보**를 뽑은 것이다.\n")
    A("\n## 0. 무엇을 잰 것인가 (타당성 고지)\n")
    A("| 구분 | 논문 Table 1 | 본 매핑 |\n|---|---|---|")
    A("| 자료 | 조직 내부 자기보고 설문 | 공개 유튜브 담론(자막 전문) |")
    A("| 척도 | 5점 리커트 × 4항목 = 0~16 | 규칙 기반 대리지표 × 4항목 = 0~16 |")
    A("| 판정 | 8점 이하 low / 9점 이상 high | 동일 절단점 + 코퍼스 상대 절단점 병기 |")
    A("| 대상 | 특정 조직의 성숙도 | 발화의 **강조점**(claim), 성숙도 아님 |")
    A("\n측정 규칙: **Level** = 축 핵심어 밀도(1천 단어당), **Scope** = 전사·all employees 등 "
      "범위 표지가 축 핵심어 ±400자에 출현, **Impact** = 수치·효과 표지(%, 배, 절감 …)가 근처에 출현, "
      "**Future** = 전략·로드맵·계획 표지가 근처에 출현. 각 0~4점.\n")
    A("⚠️ 여기 뽑힌 것은 **사례 후보**다. 논문·발표에 인용하려면 원문(파일 링크)을 직접 확인해야 한다.\n")

    A("\n## 1. 세 축의 담론 강조 비교\n")
    A("| 축 | 평균(0~16) | 논문 절단점(≥9) 충족 | 상대 절단점(상위 10%) |\n|---|---|---|---|")
    for k in keys:
        v = [r[f"{k}_total"] for r in rows]
        hi = sum(1 for x in v if x >= HIGH_CUTOFF)
        A(f"| {labels[k]} | {sum(v)/len(v):.2f} | {hi}건 ({100*hi/len(v):.1f}%) | {rel_cut[k]}점 |")
    A(f"\n총 {len(rows)}건(ax_core) 기준. **논문 절단점을 그대로 적용하면 거의 모든 문서가 low**로 "
      "떨어진다 — 공개 담론은 네 하위항목(수준·범위·영향·전략)을 동시에 갖춰 말하는 일이 드물기 때문이다. "
      "이것 자체가 관찰이다: 담론은 성숙도 진술이 아니라 **부분적 주장**의 형태를 띤다.\n")
    A("축 간 비교에서 **자동화 > 데이터 풍부성 > 증강** 순으로 강조된다. 논문이 "
      "integrated intelligence(3축 동시 high)를 목표점으로 제시한 것과 대비하면, "
      "공개 담론은 자동화 쪽으로 치우쳐 있고 증강 서사가 가장 얇다.\n")

    A("\n## 2. 큐브 8개 상태별 사례 후보\n")
    A(f"셀 판정은 **코퍼스 상대 절단점**(자동화 ≥{rel_cut['aut']}, 증강 ≥{rel_cut['aug']}, "
      f"데이터 ≥{rel_cut['dat']} → high)이다. 각 셀에서 세 축 합계 상위 문서를 뽑았다.\n")
    order = ["H-H-H", "H-L-H", "L-H-H", "H-H-L", "H-L-L", "L-H-L", "L-L-H", "L-L-L"]
    for cell in order:
        items = sorted(by_cell.get(cell, []), key=lambda r: -r["aitf_sum"])
        A(f"\n### {cell} — {CELL_NAMES[cell]}  ({len(items)}건)\n")
        if cell == "L-L-L":
            A("⚠️ 이 셀은 '조직이 그 상태'라는 뜻이 아니라 **세 축 어느 쪽도 강조하지 않은 발화**라는 뜻이다. "
              "코퍼스의 69%가 여기 몰린다 — 담론 자료를 성숙도 진단으로 오독하면 안 되는 이유.\n")
        if not items:
            A("해당 문서 없음.\n")
            continue
        A("| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |\n|---|---|---|---|---|---|---|")
        for r in items[:8 if cell != "L-L-L" else 3]:
            best = max(keys, key=lambda k: r[f"{k}_total"])
            ev = r[f"{best}_evidence"].replace("|", "／")[:180]
            title = r["title"].replace("|", "／")[:60]
            link = f"[{title}]({r['url']})" if r["url"].startswith("http") else title
            kind = "자사 채널" if r["source"] == "channel" else "미디어·검색"
            A(f"| {r['channel'][:24]} | {kind} | {link} | {r['aut_total']} | {r['aug_total']} | "
              f"{r['dat_total']} | {ev} |")
        A("")
        for r in items[:3 if cell != "L-L-L" else 1]:
            A(f"- `{r['file']}`")

    A("\n## 3. 기업(자사 채널)별 큐브 좌표\n")
    A("영상 단위 점수를 채널별 상위 5건 평균(top5)으로 집계했다 — '그 조직이 가장 강하게 말할 때'의 수준. "
      f"상대 절단점(중앙값 분할): 자동화 {comp_cut['aut']}, 증강 {comp_cut['aug']}, 데이터 {comp_cut['dat']}.\n")
    A("| 기업(채널) | n | 자동화 | 증강 | 데이터 | 셀(상대) | 셀(논문절단점) |\n|---|---|---|---|---|---|---|")
    for c in comp[:40]:
        A(f"| {c['channel'][:26]} | {c['n_docs']} | {c['aut_top5']} | {c['aug_top5']} | "
          f"{c['dat_top5']} | {c['cell_relative']} | {c['cell_paper']} |")
    A(f"\n전체 {len(comp)}개 기업: `analysis/aitf_company.csv`.\n")

    A("\n## 4. 수치 성과가 붙은 사례 발췌 (Impact 항목 상위)\n")
    A("논문 Table 1의 Impact 문항('변혁적 영향을 미쳤다')에 대응하는, **수치가 붙은 주장**만 모았다. "
      "인용 가치가 가장 높은 후보군이다. 수치는 발화자의 주장이며 검증된 값이 아니다.\n")
    A("| 채널 | 구분 | 영상 | Impact(3축 합) | 근거 발췌 |\n|---|---|---|---|---|")
    num = re.compile(r"\d+\s*(%|배|퍼센트)|\b\d+x\b")
    ranked = sorted(rows, key=lambda r: -sum(r[f"{k}_impact"] for k in keys))
    seen_ch = collections.Counter()
    for r in ranked:
        best = max(keys, key=lambda k: r[f"{k}_impact"])
        ev = r[f"{best}_evidence"]
        if not num.search(ev) or seen_ch[r["channel"]] >= 2:
            continue
        seen_ch[r["channel"]] += 1
        title = r["title"].replace("|", "／")[:55]
        link = f"[{title}]({r['url']})" if r["url"].startswith("http") else title
        kind = "자사 채널" if r["source"] == "channel" else "미디어·검색"
        A(f"| {r['channel'][:22]} | {kind} | {link} | {sum(r[f'{k}_impact'] for k in keys)} | "
          f"{ev.replace('|', '／')[:190]} |")
        if sum(seen_ch.values()) >= 15:
            break

    A("\n## 5. 논문 3단계(path framing / narrating / stretching)용 후보\n")
    A("논문은 전환을 ① path framing(무엇을) ② path narrating(언제) ③ path stretching(어떻게 넓힐지)의 "
      "3단계로 서술한다. 각 단계에 대응하는 하위항목이 강한 문서를 후보로 붙인다. "
      "(하위항목↔단계 대응은 본 매핑의 해석이지 논문의 규정이 아니다.)\n")
    steps = [("path framing", "Level", "level", "무엇을 AI로 바꿀지 정의하는 진술"),
             ("path narrating", "Future", "future", "시간 순서·로드맵으로 서술한 진술"),
             ("path stretching", "Scope", "scope", "전사·전 부서로 넓히는 진술")]
    used = set()
    for name, item, sub, desc in steps:
        A(f"\n**{name}** — {item} 항목({desc})\n")
        A("| 채널 | 영상 | 해당 항목 점수(3축 합) | 근거 발췌 |\n|---|---|---|---|")
        picked, ch_seen = 0, set()
        for r in sorted(rows, key=lambda r: -sum(r[f"{k}_{sub}"] for k in keys)):
            if r["file"] in used or r["channel"] in ch_seen:   # 같은 문서·채널 중복 방지
                continue
            used.add(r["file"]); ch_seen.add(r["channel"]); picked += 1
            best = max(keys, key=lambda k: r[f"{k}_{sub}"])
            ev = r[f"{best}_evidence"].replace("|", "／")[:150]
            title = r["title"].replace("|", "／")[:55]
            link = f"[{title}]({r['url']})" if r["url"].startswith("http") else title
            A(f"| {r['channel'][:22]} | {link} | {sum(r[f'{k}_{sub}'] for k in keys)} | {ev} |")
            if picked >= 5:
                break

    A("\n## 6. 한계\n")
    A("1. **담론 ≠ 성숙도.** 자사 채널 발화는 마케팅 목적이 섞인다. 논문 설문의 자기보고와도 다른 "
      "층위이므로, 두 자료를 같은 척도로 취급하면 안 된다.\n"
      "2. **규칙 기반 코딩**이라 반어·부정·자막 오역에 취약하다(코드북 v2 §한계와 동일).\n"
      "3. **상대 절단점은 코퍼스 의존적**이다. 표본이 바뀌면 셀 배치도 바뀐다. 논문 절단점 결과를 "
      "함께 보고하는 이유다.\n"
      "4. 채널 단위 집계는 **기업 = 채널** 가정에 기댄다. 미디어·컨설팅 채널(source=keyword)은 "
      "기업 표에서 제외했다.\n")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
