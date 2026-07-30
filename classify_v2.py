"""
분류기 v2 — 다차원 담론 코딩 (규칙 기반, 재현 가능)

기존 classify.py 의 한계(진단 2026-07-29):
  - DX/AX/AT 3분 어휘 매칭이라 사실상 'AI 어휘 밀도'만 잼.
  - Cohere(학술)에 AX가 74개 붙고, 한국 비즈니스 AX 담론("AI 전환·도입")은
    약어를 안 써 미분류(72%)로 빠짐 → 라벨이 관련성·의미를 반영 못 함.

v2 설계 — 하나의 라벨 대신 연구틀에 맞춘 여러 축을 동시에 코딩한다:
  1) relevance  : ax_core / ax_adjacent / off_topic / noise
     (전환·조직·비용 프레이밍 vs 단순 AI기술 vs 무관 vs 저품질)
  2) stance     : washing / anti_washing / neutral        (톤)
  3) subject_hint: vendor / media_commentary               (발화 주체, 거친 추정)
     + is_investor_finance / is_academic / is_consulting    (보조 플래그)
  4) 구성개념 신호(불리언) — CONTENT_REVIEW·INTERVIEW_GUIDE 의 분석축을 직접 태깅:
     sig_denominator(분모 바꾸기) · sig_agent_workforce(에이전트=인력) ·
     sig_cost(비용 언어) · sig_sovereignty(주권/국가) · sig_failure_ritual(95% 실패) ·
     sig_deskilling(탈숙련) · sig_governance(거버넌스) · sig_eval(평가/벤치마크)

출력: analysis/classified_v2.csv  (회귀분석에 바로 쓸 수 있는 다차원 코드)
직접 실행: python classify_v2.py
※ 임베딩 없이 순수 규칙 기반이라 어디서나(클라우드 러너 포함) 가볍게 돈다.
"""

import csv
import glob
import os
import re

import config
from classify import parse_transcript, doc_month, score_text  # 메타·본문·DX/AX/AT 재사용


def rx(*pats):
    return [re.compile(p, re.IGNORECASE) for p in pats]


# ── relevance 신호 사전 ──────────────────────────────────────────
# (a) 전환/조직 프레이밍 — "기업·조직이 AI로 일하는 방식을 바꾼다"는 담론
TRANSFORM = rx(
    r"\bAX\b", r"AI\s*전환", r"인공지능\s*전환", r"AI\s+transformation",
    r"디지털\s*전환", r"digital\s+transformation",
    r"AI\s*도입", r"AI\s+adoption", r"adopt(ing)?\s+AI", r"도입\s*사례",
    r"enterprise\s+AI", r"전사(적)?", r"업무\s*(자동화|재설계)", r"워크플로",
    r"workflow", r"조직\s*(문화|변화|개편)", r"change\s+management", r"변화\s*관리",
    r"생산성", r"productivity", r"의사\s*결정", r"decision[-\s]?making",
    r"거버넌스", r"governance", r"에이전트\s*(도입|운영|오케스트레이션)",
    r"agentic\s+(enterprise|workforce|organization)", r"AI\s*(전략|조직|인재|거버넌스)",
    r"AI\s+(strategy|adoption|workforce|governance)", r"혁신", r"transformation\s+office",
)
# (b) AI 기술 어휘 — 있으면 AI 콘텐츠지만, 전환 프레이밍이 없으면 튜토리얼/연구/제품데모
AI_TECH = rx(
    r"\bLLM\b", r"\bGPT\b", r"ChatGPT", r"생성형\s*AI", r"generative\s+AI", r"\bGenAI\b",
    r"머신\s*러닝", r"machine\s+learning", r"딥\s*러닝", r"deep\s+learning",
    r"파운데이션\s*모델", r"foundation\s+model", r"neural|transformer|embedding",
    r"에이전트", r"\bagent(ic|s)?\b", r"코파일럿|copilot|챗봇|chatbot",
    r"파인\s*튜닝|fine[-\s]?tun|\bRAG\b|프롬프트|prompt", r"모델|model",
    r"인공지능|artificial\s+intelligence|\bAI\b",
)
# (c) 비용/재무 프레이밍 — 전환을 P&L·원가로 번역
COST = rx(
    r"비용|원가|인건비|cost|예산|budget|CAPEX|OPEX|FinOps|\bROI\b|투자\s*수익",
    r"절감|savings?|효율화|마진|margin|매출|revenue|손익|\bP&L\b|토큰\s*(비용|과금)|크레딧",
)

# ── stance(톤) 사전 ─────────────────────────────────────────────
WASHING = rx(
    r"혁명|revolution", r"게임\s*체인저|game[-\s]?chang", r"10\s*배|100\s*배|\b10x\b|\b100x\b",
    r"세계\s*최초|world['’]?s\s+first", r"완전\s*자동|fully\s+autonomous",
    r"마법|magic", r"unprecedented|seamless|effortless|revolutioniz",
    r"미래(를|가)\s*바(꾼|뀐)|the\s+future\s+of", r"판(을|도).*(뒤집|바꾼)",
)
ANTI_WASHING = rx(
    r"과대\s*광고|과장|hype", r"실사용|실제\s*사용|in\s+production", r"검증|verif|validat",
    r"한계|limitation|리스크|risk", r"신중|cautious", r"human[-\s]?in[-\s]?the[-\s]?loop",
    r"감독\s*필요|사람이\s*검토|사람\s*개입", r"대체(하지|가)\s*(못|않|아니)|doesn'?t\s+replace",
    r"파일럿|pilot", r"실패(율|했|한)|fail(ed|ure)?", r"근거|evidence", r"버블|거품|bubble|환멸",
)

# ── 구성개념(분석축) 신호 ───────────────────────────────────────
SIG = {
    "denominator": rx(
        r"지표|metric|측정\s*(단위|기준)|KPI", r"성과(를|의)?\s*(어떻게|무엇으로)?\s*(측정|잰|재)",
        r"토큰.{0,6}(에이전트|agent)", r"usage.{0,4}outcome", r"outcome[-\s]?based",
        r"새(로운)?\s*지표|재정의|reframe|redefine", r"분모",
    ),
    "agent_workforce": rx(
        r"AI\s*직원|AI\s+employee|AI\s*workforce|디지털\s*워커|digital\s+worker",
        r"에이전트.{0,4}(인력|노동)|위임\s*가능한\s*노동", r"replace.{0,10}headcount",
        r"인력\s*(감축|재배치|축소)|유휴\s*인력|재배치|headcount|FTE",
    ),
    "cost": COST,
    "sovereignty": rx(
        r"주권|sovereign|소버린", r"데이터\s*주권|data\s+sovereignty",
        r"국가(대표)?\s*AI|national\s+AI|K-?AI", r"정부|government|클러스터\s*(펀딩|투자)",
        r"자국\s*(모델|칩)|무역\s*수지",
    ),
    "failure_ritual": rx(
        r"9[05]\s*%.{0,12}(실패|fail)", r"8[05]\s*%.{0,12}(실패|fail)",
        r"대부분.{0,6}실패|most\s+.{0,10}fail", r"프로젝트\s*.{0,6}실패",
        r"88\s*%.{0,20}39\s*%", r"MIT.{0,20}(실패|5\s*%)",
    ),
    "deskilling": rx(
        r"탈숙련|deskill", r"숙련(자|공)?.{0,8}(사라|없어|줄)", r"주니어.{0,10}(안\s*뽑|줄|채용)",
        r"cognitive\s+debt|인지적\s*빚|근육\s*위축", r"파이프라인.{0,8}(끊|붕괴)",
    ),
    "governance": rx(
        r"거버넌스|governance|가드레일|guardrail|규제|regulat|compliance|규정\s*준수",
        r"감사|audit|통제\s*(권|타워)|control\s+tower",
    ),
    "eval": rx(
        r"벤치마크|benchmark", r"평가|evaluat|eval\b", r"정확도|accuracy",
        r"신뢰(성|도)|reliab", r"할루시네이션|hallucinat",
    ),
}

# ── subject 보조 플래그 ─────────────────────────────────────────
INVESTOR = rx(r"투자|investor|어닝|earnings|주가|시가총액|밸류에이션|valuation|실적|IR\b|나스닥|증권")
ACADEMIC = rx(r"교수|professor|연구(진|팀|자)|paper|논문|arxiv|대학|university|이론|theory")
CONSULTING = rx(r"맥킨지|mckinsey|\bBCG\b|액센츄어|accenture|딜로이트|deloitte|컨설팅|consult|가트너|gartner")
MEDIA = rx(r"\bKBS\b|\bSBS\b|\bYTN\b|\bMBC\b|뉴스|news|기자|앵커|경제\s*(콘서트|뉴스)|비디오머그|티타임즈")


def count(patterns, text):
    return sum(len(p.findall(text)) for p in patterns)


def any_hit(patterns, text):
    return 1 if any(p.search(text) for p in patterns) else 0


def classify_relevance(text, words):
    if words < 50:
        return "noise"
    t = count(TRANSFORM, text)
    a = count(AI_TECH, text)
    c = count(COST, text)
    if t >= 2 or (t >= 1 and c >= 1):
        return "ax_core"           # 전환·조직·비용으로 프레이밍된 진짜 AX 담론
    if a >= 2:
        return "ax_adjacent"       # AI 콘텐츠지만 전환 프레이밍 아님(튜토리얼·연구·데모)
    if a == 0 and t == 0:
        return "off_topic"         # AI/AX 신호 없음(광고·무관)
    return "ax_adjacent"


def classify_stance(text):
    w = count(WASHING, text)
    aw = count(ANTI_WASHING, text)
    if aw > w and aw >= 2:
        return "anti_washing"
    if w > aw and w >= 2:
        return "washing"
    return "neutral"


def main():
    out_dir = "analysis"
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        hits, _density, words = score_text(text)
        source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
        rel = classify_relevance(text, words)
        row = {
            "file": path.replace(os.sep, "/"),
            "title": meta["title"], "channel": meta["channel"], "source": source,
            "lang": meta["lang"], "month": doc_month(path, meta), "words": words,
            "relevance": rel,
            "stance": classify_stance(text) if rel in ("ax_core", "ax_adjacent") else "neutral",
            "subject_hint": "vendor" if source == "channel" else "media_commentary",
            "is_investor_finance": any_hit(INVESTOR, text),
            "is_academic": any_hit(ACADEMIC, text),
            "is_consulting": any_hit(CONSULTING, text),
            "is_media": any_hit(MEDIA, text),
        }
        for name, pats in SIG.items():
            row[f"sig_{name}"] = any_hit(pats, text)
        row["AX_hits"] = hits["AX"]; row["DX_hits"] = hits["DX"]; row["AT_hits"] = hits["AT"]
        rows.append(row)

    with open(os.path.join(out_dir, "classified_v2.csv"), "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()) if rows else ["file"])
        w.writeheader()
        w.writerows(rows)

    # ── 요약 출력 ──
    import collections
    total = len(rows)
    rel = collections.Counter(r["relevance"] for r in rows)
    core = [r for r in rows if r["relevance"] == "ax_core"]
    print(f"[classify_v2] 총 {total}건 → analysis/classified_v2.csv")
    print("  relevance:", dict(rel))
    st = collections.Counter(r["stance"] for r in core)
    print(f"  ax_core({len(core)}건) stance:", dict(st))
    print("  구성개념 신호 출현율(전체 대비):")
    for name in SIG:
        n = sum(r[f"sig_{name}"] for r in rows)
        print(f"    sig_{name}: {n}건 ({100*n/total:.0f}%)")
    # relevance × source 교차
    print("  relevance × source:")
    for s in ("channel", "keyword"):
        sub = [r for r in rows if r["source"] == s]
        c = collections.Counter(r["relevance"] for r in sub)
        print(f"    {s}({len(sub)}): {dict(c)}")


if __name__ == "__main__":
    main()
