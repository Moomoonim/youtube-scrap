"""
수집 콘텐츠 카탈로그 생성기.

각 영상을 연구용 메타데이터로 구조화한다:
  날짜 · 채널 · 관련 회사 · 기능(상세) · AX/DX 라벨 · 이벤트 · 인물 · 기술

출력:
  analysis/catalog.csv   — 전량 기계판독용(회귀분석·필터링)
  docs/CATALOG.md        — 사람이 읽는 카탈로그(계층·회사별 정리 + 통계)

직접 실행: python build_catalog.py
"""

import csv
import collections
import glob
import os
import re

import config
from classify import parse_transcript, doc_month, score_text
# 분류 v2의 관련성·톤 판정과 기능/신호 사전을 그대로 재사용해 일관성 유지
from classify_v2 import classify_relevance, classify_stance, SIG


def rx(*p):
    return [re.compile(x, re.I) for x in p]


# ── 기능(capability) 10범주 — CAPABILITY_STATS.md와 동일 사전 ──
CAP = {
    "에이전트 오케스트레이션": rx(r"에이전트|\bagent(ic|s)?\b", r"오케스트레이션|orchestrat",
                            r"multi[-\s]?agent|멀티\s*에이전트", r"\bA2A\b|\bMCP\b|swarm|handoff|tool[-\s]?use"),
    "검색·컨텍스트·메모리(RAG)": rx(r"\bRAG\b|검색\s*증강|retrieval",
                             r"벡터|vector\s*(db|database|search)|embedding|임베딩",
                             r"온톨로지|ontology|knowledge\s*graph|지식\s*그래프",
                             r"컨텍스트|context\s*(window|engineering)|메모리|memory"),
    "코딩·개발 자동화": rx(r"copilot|코파일럿", r"코드\s*(생성|작성)|code\s*(generation|gen)|coding\s*agent",
                     r"바이브\s*코딩|vibe\s*coding", r"\bSDLC\b|개발\s*자동화|IDE"),
    "대화·고객서비스": rx(r"챗봇|chatbot",
                    r"고객\s*(서비스|지원|상담)|customer\s*(service|support)|contact\s*center|콜센터|상담(원|사)?",
                    r"voice\s*agent|음성\s*(비서|에이전트)|가상\s*상담"),
    "문서·데이터 처리": rx(r"문서\s*(처리|파싱|추출)|document\s*(processing|parsing|extraction)|\bOCR\b|parse",
                     r"데이터\s*(파이프라인|처리|정제|통합)|data\s*(pipeline|integration|ingestion)|\bETL\b"),
    "생성 미디어": rx(r"이미지\s*생성|image\s*generation|text[-\s]?to[-\s]?image",
                 r"영상\s*(생성|편집)|video\s*(generation|editing)|text[-\s]?to[-\s]?video",
                 r"음성\s*(합성|생성)|voice\s*(synthesis|clon)|더빙|dubbing|text[-\s]?to[-\s]?speech"),
    "거버넌스·평가·보안": rx(r"거버넌스|governance|가드레일|guardrail", r"평가|evaluat|벤치마크|benchmark",
                      r"보안|security|compliance|규정\s*준수|감사|audit"),
    "자율주행·로보틱스·물리AI": rx(r"자율\s*주행|self[-\s]?driving|autonomous\s*(driving|vehicle)|로보택시|robotaxi",
                           r"로봇|robot(ics|s)?|휴머노이드|humanoid|액추에이터|actuator",
                           r"피지컬\s*AI|physical\s*AI|센서|sensor"),
    "인프라·칩·컴퓨트": rx(r"\bGPU\b|\bTPU\b|\bHBM\b|반도체|semiconductor|칩\b|chip",
                     r"데이터\s*센터|data\s*center|랙|rack|전력|power|cooling|냉각",
                     r"추론|inference|훈련|training\s*(cluster|run)|가속기|accelerator"),
    "예측·분석·최적화": rx(r"예측|forecast|prediction", r"최적화|optimiz",
                     r"분석|analytics|\bBI\b|대시보드|dashboard", r"추천|recommendation"),
}


# ── 채널 → 회사 · HQ 국가 · 스택 계층 ──────────────────────────
LAYER = {
    "인프라·칩·전력": ["NVIDIA", "NVIDIA Developer", "AMD", "Arm", "Intel", "SK hynix",
                      "Vertiv", "Schneider Electric", "Huawei", "Samsung Semiconductor",
                      "Cerebras", "SambaNova"],
    "파운데이션 모델": ["OpenAI", "Anthropic", "Google DeepMind", "Meta", "Alibaba Cloud",
                      "Cohere", "Hugging Face", "xAI", "LG AI Research", "NAVER Cloud",
                      "Upstage", "Mistral AI", "Google"],
    "데이터·컨텍스트·거버넌스": ["Palantir", "ServiceNow", "Databricks", "Snowflake", "Oracle",
                              "Pinecone", "Weaviate", "Qdrant", "IQVIA"],
    "에이전트·개발도구": ["AWS Developers", "AWS Events", "Google Cloud Tech", "Google Developers",
                        "GitHub", "Replit", "Zapier", "Microsoft", "Microsoft Azure",
                        "Microsoft Developer", "Weights & Biases", "Meta Developers",
                        "Apple Developer", "Apple", "IBM Technology"],
    "엔터프라이즈 앱": ["SAP", "Salesforce", "Infosys", "TCS", "Accenture", "Genpact",
                      "LinkedIn", "Intuit", "Slack", "Cursor"],
    "생성 미디어": ["ElevenLabs", "Runway", "Stability AI", "Luma AI", "Suno", "Synthesia"],
    "물리 AI·자율주행": ["Tesla", "Boston Dynamics", "Figure", "Zoox", "Wayve", "Waymo",
                       "Aurora", "Anduril", "General Motors", "BYD", "Nissan", "Volvo Cars",
                       "BMW", "Mercedes-Benz", "Siemens", "Rockwell Automation"],
    "컨설팅·전략": ["McKinsey & Company", "Boston Consulting Group", "Scale AI"],
    "통신·주권·국가": ["Orange", "Telefónica", "Nokia", "Telenor", "Swisscom", "SK텔레콤", "KT"],
    "수요기업·기타": ["L'Oréal", "IKEA", "Amazon", "Nike", "Unilever", "Reckitt", "Adobe",
                    "Netflix", "Chegg", "SoftBank", "NTT DATA", "Philips", "GE HealthCare",
                    "Mayo Clinic", "Eli Lilly", "Snap", "DuckDuckGo", "Perplexity",
                    "kakao tech", "Infosys"],
}
CH2LAYER = {ch: layer for layer, chs in LAYER.items() for ch in chs}

HQ = {
    "US": ["NVIDIA", "NVIDIA Developer", "AMD", "Intel", "Vertiv", "OpenAI", "Anthropic",
           "Meta", "Meta Developers", "Google", "Google Developers", "Google Cloud Tech",
           "Palantir", "ServiceNow", "Databricks", "Snowflake", "Oracle", "Pinecone",
           "AWS Developers", "AWS Events", "GitHub", "Replit", "Zapier", "Microsoft",
           "Microsoft Azure", "Microsoft Developer", "Weights & Biases", "Salesforce",
           "Tesla", "Boston Dynamics", "Figure", "Zoox", "Waymo", "Aurora", "Anduril",
           "McKinsey & Company", "Apple", "Apple Developer", "IBM Technology", "IQVIA",
           "ElevenLabs", "Runway", "Luma AI", "Suno", "Amazon", "Nike", "Adobe", "Netflix",
           "Chegg", "Mayo Clinic", "GE HealthCare", "Eli Lilly", "Snap", "DuckDuckGo",
           "Perplexity", "xAI", "LinkedIn", "Intuit", "Slack", "Cursor", "Cerebras",
           "SambaNova", "General Motors", "Hugging Face", "Scale AI", "Rockwell Automation"],
    "KR": ["SK hynix", "LG AI Research", "NAVER Cloud", "SK텔레콤", "Upstage", "kakao tech", "KT",
           "Samsung Semiconductor"],
    "CN": ["Huawei", "Alibaba Cloud", "BYD"],
    "DE": ["SAP", "Siemens", "BMW", "Mercedes-Benz", "Qdrant"],
    "FR": ["Schneider Electric", "Orange", "L'Oréal", "Mistral AI"],
    "UK": ["Arm", "Wayve", "Stability AI", "Google DeepMind", "Reckitt"],
    "JP": ["Nissan", "SoftBank", "NTT DATA"],
    "IN": ["Infosys", "TCS"],
    "CA": ["Cohere"],
    "NL": ["Philips", "Weaviate", "Unilever"],
    "SE": ["IKEA", "Volvo Cars"],
    "FI": ["Nokia"], "CH": ["Swisscom"], "ES": ["Telefónica"], "NO": ["Telenor"],
    "IE": ["Accenture"], "IL": [], "SG": [],
}
CH2HQ = {ch: k for k, chs in HQ.items() for ch in chs}

# ── 이벤트(키노트·컨퍼런스) ────────────────────────────────────
EVENTS = {
    "NVIDIA GTC": rx(r"\bGTC\b"),
    "AWS re:Invent": rx(r"re:?Invent"),
    "Google I/O": rx(r"Google\s+I/?O\b"),
    "Google Cloud Next": rx(r"Cloud\s+Next|\bNext\s*'?\d{2}"),
    "Microsoft Build/Ignite": rx(r"MS\s*Build|Microsoft\s+Build|\bIgnite\b"),
    "Apple WWDC": rx(r"\bWWDC\b"),
    "SAP Sapphire": rx(r"Sapphire"),
    "Salesforce Dreamforce": rx(r"Dreamforce"),
    "Palantir AIPCon": rx(r"AIPCon|AIP\s*Con"),
    "COMPUTEX": rx(r"COMPUTEX"),
    "CES": rx(r"\bCES\s*20\d\d|\bCES\b(?=.*(keynote|booth))"),
    "Databricks Summit": rx(r"Data\s*\+?\s*AI\s+Summit|Databricks\s+Summit"),
    "Meta Connect": rx(r"Meta\s+Connect"),
    "OpenAI DevDay": rx(r"DevDay|Dev\s+Day"),
    "기타 키노트/서밋": rx(r"keynote|기조\s*연설|summit|서밋|컨퍼런스|conference|webinar|웨비나"),
}

# ── 기술 스택 (제품·프레임워크·모델) ───────────────────────────
TECH = {
    "LLM 모델": rx(r"\bGPT-?[45]?\b|ChatGPT|Claude|Gemini|Llama|Qwen|Mistral|Nemotron|"
                 r"EXAONE|HyperCLOVA|DeepSeek|Grok|Solar\b|Command\s*R"),
    "에이전트 프레임워크": rx(r"\bADK\b|Strands|LangChain|LangGraph|CrewAI|AutoGen|LlamaIndex|"
                        r"Agent\s*Bricks|Agentforce|AgentCore|Bedrock\s+Agents"),
    "프로토콜·표준": rx(r"\bMCP\b|Model\s+Context\s+Protocol|\bA2A\b|Agent2Agent|OpenTelemetry|\bOTel\b"),
    "검색·RAG": rx(r"\bRAG\b|retrieval[-\s]augmented|벡터\s*(DB|검색)|vector\s+(db|database|search)|"
                 r"embedding|임베딩|rerank|하이브리드\s*검색|hybrid\s+search"),
    "파인튜닝·학습": rx(r"\bLoRA\b|fine[-\s]?tun|파인\s*튜닝|\bRLHF\b|\bRLVR\b|\bSFT\b|"
                    r"강화\s*학습|reinforcement\s+learning|distill|증류"),
    "추론 최적화": rx(r"\bvLLM\b|TensorRT|Dynamo|quantiz|양자화|\bKV\s*cache\b|"
                  r"speculative\s+decod|추측\s*디코딩|prefill|배치\s*추론"),
    "칩·하드웨어": rx(r"\bCUDA\b|Blackwell|Hopper|\bH100\b|\bGB200\b|\bTPU\b|\bHBM\d?\b|"
                  r"Ascend|Instinct|\bEPYC\b|Xeon|Jetson|\bNPU\b"),
    "코딩 에이전트": rx(r"Copilot|Codex|Claude\s+Code|Cursor|Antigravity|바이브\s*코딩|vibe\s*coding"),
    "거버넌스·평가 도구": rx(r"Unity\s+Catalog|Control\s+Tower|guardrail|가드레일|"
                        r"LLM[-\s]as[-\s]a?[-\s]?judge|Weave\b|MLflow|Arize|eval\s+harness"),
    "온톨로지·데이터계층": rx(r"온톨로지|ontology|knowledge\s+graph|지식\s*그래프|context\s+graph|"
                        r"data\s+fabric|semantic\s+layer|시맨틱\s*(계층|레이어)"),
}

# ── 인물 (코퍼스 분석에서 확인된 주요 발화자) ─────────────────
PEOPLE = {
    # 글로벌 경영/기술 리더
    "젠슨 황(Jensen Huang, NVIDIA CEO)": rx(r"젠슨\s*황|Jensen\s+Huang"),
    "일론 머스크(Tesla)": rx(r"일론\s*머스크|Elon\s+Musk"),
    "Jeff Dean(Google Chief Scientist)": rx(r"Jeff\s+Dean|제프\s*딘"),
    "Bill Dally(NVIDIA Chief Scientist)": rx(r"Bill\s+Dally"),
    "Aaron Levie(Box CEO)": rx(r"Aaron\s+Levie"),
    "Amjad Masad(Replit CEO)": rx(r"Amjad\s+Masad"),
    "Eric Ries(Lean Startup)": rx(r"Eric\s+Ries"),
    "Sara Hooker(Adaption Labs)": rx(r"Sara\s+Hooker"),
    "Amit Bendov(Gong CEO)": rx(r"Amit\s+Bendov"),
    "Wade Foster(Zapier CEO)": rx(r"Wade\s+Foster"),
    "Alex Kendall(Wayve CEO)": rx(r"Alex\s+Kendall"),
    "Shyam Sankar(Palantir CTO)": rx(r"Shyam\s+Sankar"),
    "Robin Vince(BNY CEO)": rx(r"Robin\s+Vince"),
    "Fernando Fernandez(Unilever CEO)": rx(r"Fernando\s+Fernandez|페르난도\s*페르난데스"),
    "Rand Waldron(Oracle)": rx(r"Rand\s+Waldron"),
    "Bruno Zerbib(Orange CTIO)": rx(r"Bruno\s+Zerbib"),
    "Nellie Wartoft(Tigerhall CEO)": rx(r"Nellie\s+Wartoft"),
    "Lotta Lovén(Swedbank CIO)": rx(r"Lotta\s+Lov"),
    # 한국 AX 담론
    "김건우(『AI 전환 절대공식』 저자)": rx(r"김건우"),
    "신계영(삼성SDS AX센터 부사장)": rx(r"신계영"),
    "황재선(SK CDO)": rx(r"황재선"),
    "전준일(무신사 CTO)": rx(r"전준일"),
    "이상욱(한양대 교수, 탈숙련)": rx(r"이상욱\s*교수|이상욱"),
    "김유신(티타임즈 상무)": rx(r"김유신"),
    "장진석(BCG)": rx(r"장진석"),
    "서연석(NAVER Cloud)": rx(r"서연석"),
    "김덕진(IT융합연구소장)": rx(r"김덕진"),
    "이세돌": rx(r"이세돌"),
    "이홍락(LG AI)": rx(r"이홍락"),
    "최태원(SK 회장)": rx(r"최태원"),
    "정의선(현대차 회장)": rx(r"정의선"),
    "손정의(SoftBank)": rx(r"손정의|Masayoshi\s+Son"),
}

# ── 언급된 주요 기업(고객사·파트너) ────────────────────────────
COMPANIES = {
    n: re.compile(p, re.I) for n, p in {
        "JPMorgan": r"JP\s?모건|JPMorgan", "우리은행": r"우리은행", "삼성전자": r"삼성전자",
        "Walmart": r"월마트|Walmart", "Home Depot": r"Home\s?Depot", "PayPal": r"PayPal",
        "BBVA": r"\bBBVA\b", "Swedbank": r"Swedbank", "AT&T": r"AT&T", "Verizon": r"Verizon",
        "Uber": r"\bUber\b", "Shopify": r"Shopify", "BNY": r"\bBNY\b|Bank of New York",
        "Klarna": r"Klarna", "Moderna": r"모더나|Moderna", "Adobe": r"어도비|Adobe",
        "Instacart": r"Instacart", "Carrefour": r"Carrefour|까르푸", "Indeed": r"\bIndeed\b",
        "Lovable": r"Lovable", "Cadence": r"Cadence", "CrowdStrike": r"CrowdStrike",
        "Mayo Clinic": r"메이요|Mayo\s+Clinic", "무신사": r"무신사", "현대차": r"현대차|현대자동차",
        "MediaMarkt": r"MediaMarkt", "Sandvik": r"Sandvik", "Builder.ai": r"Builder\.?ai",
        "Deloitte": r"딜로이트|Deloitte", "McKinsey": r"맥킨지|McKinsey", "BCG": r"\bBCG\b",
        "Accenture": r"액센츄어|Accenture", "Gartner": r"가트너|Gartner",
    }.items()
}


def detect(dic, text, joiner=" · "):
    """사전 dict(name -> [patterns]) 에서 매칭된 이름 목록."""
    hits = [n for n, pats in dic.items()
            if (any(p.search(text) for p in pats) if isinstance(pats, list) else pats.search(text))]
    return joiner.join(hits)


def main():
    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        hits, _d, words = score_text(text)
        source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
        ch = meta["channel"]
        rel = classify_relevance(text, words)
        title = meta["title"]
        blob = title + "\n" + text  # 이벤트는 제목에도 자주 등장

        # 기능(상세) — CAP 사전 전체
        funcs = [name for name, pats in CAP.items() if any(p.search(text) for p in pats)]
        # 구성개념 신호
        sigs = [n for n, pats in SIG.items() if any(p.search(text) for p in pats)]

        label = ("AX" if hits["AX"] >= 2 and hits["AX"] >= hits["DX"]
                 else "DX" if hits["DX"] >= 2
                 else "AT" if hits["AT"] >= 2 else "—")

        rows.append({
            "date": meta.get("upload_date", "") or "",
            "month": doc_month(path, meta),
            "channel": ch,
            "layer": CH2LAYER.get(ch, "(미분류)"),
            "hq_country": CH2HQ.get(ch, "KW" if source == "keyword" else "?"),
            "title": title,
            "source": source,
            "lang": meta["lang"],
            "words": words,
            "ax_dx_label": label,
            "relevance": rel,
            "stance": classify_stance(text) if rel.startswith("ax") else "neutral",
            "event": detect(EVENTS, blob),
            "functions": " · ".join(funcs),
            "technologies": detect(TECH, text),
            "people": detect(PEOPLE, text),
            "companies_mentioned": detect(COMPANIES, text),
            "signals": " · ".join(sigs),
            "file": path.replace(os.sep, "/"),
        })

    os.makedirs("analysis", exist_ok=True)
    with open("analysis/catalog.csv", "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ── 사람이 읽는 카탈로그 ──
    core = [r for r in rows if r["relevance"] == "ax_core"]
    out = []
    out.append("# 수집 콘텐츠 카탈로그 (Catalog)\n")
    out.append(f"> 총 **{len(rows):,}건** · 연구 주표본(ax_core) **{len(core):,}건** · "
               f"생성 자동화(`build_catalog.py`)\n")
    out.append("> 각 항목: 날짜 · 채널 · 계층 · 국가 · AX/DX · 이벤트 · 기능 · 기술 · 인물 · 언급기업\n")
    out.append("> 전량 기계판독본은 `analysis/catalog.csv` (필터링·회귀분석용).\n")
    out.append("\n---\n")

    # 요약 통계
    out.append("## 1. 카탈로그 요약\n")
    out.append("### 계층별 분포\n")
    out.append("| 스택 계층 | 전체 | ax_core |\n|---|---|---|")
    lay_all = collections.Counter(r["layer"] for r in rows)
    lay_core = collections.Counter(r["layer"] for r in core)
    for lay, n in lay_all.most_common():
        out.append(f"| {lay} | {n} | {lay_core.get(lay,0)} |")

    out.append("\n### 이벤트별 분포 (키노트·컨퍼런스)\n")
    out.append("| 이벤트 | 건수 |\n|---|---|")
    ev = collections.Counter()
    for r in rows:
        for e in filter(None, r["event"].split(" · ")):
            ev[e] += 1
    for e, n in ev.most_common():
        out.append(f"| {e} | {n} |")

    out.append("\n### 기술 스택 출현\n")
    out.append("| 기술 범주 | 건수 | 비율 |\n|---|---|---|")
    tc = collections.Counter()
    for r in rows:
        for t in filter(None, r["technologies"].split(" · ")):
            tc[t] += 1
    for t, n in tc.most_common():
        out.append(f"| {t} | {n} | {100*n/len(rows):.0f}% |")

    out.append("\n### 주요 인물 등장\n")
    out.append("| 인물 | 등장 영상 수 |\n|---|---|")
    pc = collections.Counter()
    for r in rows:
        for p in filter(None, r["people"].split(" · ")):
            pc[p] += 1
    for p, n in pc.most_common(25):
        out.append(f"| {p} | {n} |")

    out.append("\n### 언급된 고객사·사례 기업\n")
    out.append("| 기업 | 언급 영상 수 |\n|---|---|")
    cc = collections.Counter()
    for r in rows:
        for c in filter(None, r["companies_mentioned"].split(" · ")):
            cc[c] += 1
    for c, n in cc.most_common(25):
        out.append(f"| {c} | {n} |")

    # 계층 → 채널 → 대표 항목
    out.append("\n---\n\n## 2. 계층·채널별 카탈로그 (ax_core 중심)\n")
    out.append("각 채널에서 연구 관련성이 높은(ax_core) 항목을 단어수 순으로 최대 12건 표기.\n")
    by_layer = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in core:
        by_layer[r["layer"]][r["channel"]].append(r)

    for lay in [l for l, _ in lay_all.most_common()]:
        if lay not in by_layer:
            continue
        out.append(f"\n### ▍{lay}\n")
        for ch, items in sorted(by_layer[lay].items(), key=lambda kv: -len(kv[1])):
            items.sort(key=lambda r: -int(r["words"]))
            hq = items[0]["hq_country"]
            out.append(f"\n**{ch}** ({hq}) — ax_core {len(items)}건\n")
            out.append("| 날짜 | 제목 | AX/DX | 이벤트 | 기능 | 기술 | 인물/기업 |")
            out.append("|---|---|---|---|---|---|---|")
            for r in items[:12]:
                t = r["title"][:58].replace("|", "/")
                fn = (r["functions"][:52] or "—")
                tech = (r["technologies"][:44] or "—")
                who = " ".join(x for x in [r["people"][:28], r["companies_mentioned"][:28]] if x) or "—"
                out.append(f"| {r['month']} | {t} | {r['ax_dx_label']}/{r['stance'][:4]} | "
                           f"{r['event'][:22] or '—'} | {fn} | {tech} | {who} |")

    with open("docs/CATALOG.md", "w", encoding="utf-8") as fp:
        fp.write("\n".join(out))

    print(f"[catalog] {len(rows)}건 → analysis/catalog.csv, docs/CATALOG.md")
    print(f"  ax_core {len(core)} · 이벤트 태깅 {sum(1 for r in rows if r['event'])} "
          f"· 인물 태깅 {sum(1 for r in rows if r['people'])} "
          f"· 기술 태깅 {sum(1 for r in rows if r['technologies'])}")


if __name__ == "__main__":
    main()
