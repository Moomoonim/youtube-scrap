# -*- coding: utf-8 -*-
"""케이스 스터디 성립 가능성 스캔 (v3).

핵심 지표를 '분량'에서 '**케이스 서사 블록**'으로 바꾼다.

케이스 서사 블록 = 조직 언급 주변 2,000자 창 안에서
    (도입/구축/운영 근거  또는  before 상태)
  + (after/결과 진술)
  + (정량 수치 1개 이상)
  + (프로세스 또는 자동화/증강 신호)
가 동시에 성립하는 구간. 즉 "무엇을 어떻게 바꿔서 어떤 결과가 났다"가 한 자리에 있는 대목.

케이스 스터디 적격 판정:
  CORE  블록 3개 이상 & 소스 2건 이상 & 정량 5개 이상  → 단독 케이스 가능
  PART  블록 1~2개                                    → 보조 사례/삽화 수준
  THIN  블록 0개                                      → 언급만, 케이스 불가
출력: analysis/case_feasibility.csv
"""
import re, os, csv, glob, json, collections

ROOT = "/home/user/youtube-scrap"
OUT = os.path.join(ROOT, "analysis", "case_feasibility.csv")

# ---------- 1. 코퍼스 ----------
DOCS = {}
for f in glob.glob(os.path.join(ROOT, "transcripts", "**", "*.md"), recursive=True):
    if f.endswith("README.md"): continue
    rel = os.path.relpath(f, ROOT)
    raw = open(f, encoding="utf-8", errors="ignore").read()
    head, _, body = raw.partition("## 스크립트")
    g = lambda p: (re.search(p, head).group(1).strip() if re.search(p, head) else "")
    body = re.sub(r"&nbsp;|&amp;", " ", body); body = re.sub(r"\s+", " ", body)
    if len(body) < 600: continue
    up = g(r"- 업로드일:\s*(.+)")
    mm = re.match(r"transcripts/(\d{4}-\d{2}-\d{2})/", rel)
    DOCS[rel] = dict(title=g(r"^#\s+(.+)$"), ch=g(r"- 채널:\s*(.+)"), up=up,
                     coll=(mm.group(1) if mm else ""), url=g(r"- 영상 링크:\s*(\S+)"),
                     body=body, month=(up[:7] if up else (mm.group(1)[:7] if mm else "")))
print(f"[1] 문서 {len(DOCS)}건")

# ---------- 2. 조직 후보 ----------
KO_NOISE = set("""사용 활용 실제 모범 이러한 이런 그런 저런 다양 여러 모든 일부 대부분 최근 기존 향후 현재
전체 자체 각각 서로 우리 저희 여러분 고객 회사 기업 조직 사람 직원 부서 현장 시장 정부 국가 산업 분야
기술 제품 서비스 시스템 플랫폼 데이터 클라우드 업무 프로세스 워크플로 에이전트 모델 자동화 증강 도입
구축 운영 관리 개선 혁신 전환 성공 실패 문제 해결 결과 효과 가치 비용 시간 규모 수준 방식 방법 경우
오늘 지금 내일 어제 이제 다음 이번 저번 작년 올해 내년 사례 예시 질문 답변 설명 소개 발표 강연 세션
그것 이것 저것 무엇 어떤 누구 얼마 정말 진짜 굉장 매우 아주 조금 많이 잘못 처음 마지막 음악 박수 웃음
비즈니스 프로덕션 마케팅 세일즈 커스텀 아키텍처 인프라 파트너 솔루션 서비스형
버전 기능 개발 설계 분석 예측 판단 결정 승인 검토 학습 훈련 배포 통합 연결 확장 최적 표준 기준 정책
""".split())
BAD_EN = re.compile(r"^(?:the|this|that|our|your|their|my|it|we|they|there|here|and|but|for|with|"
    r"ai|ml|llm|api|sdk|gpu|cpu|it|hr|erp|crm|rpa|roi|kpi|saas|paas|mcp|rag|nlp|ocr|iot|cli|sql|"
    r"ceo|cto|cio|cfo|coo|cdo|ciso|vp|gen ?ai|agentic|copilot|chatgpt|gpt|claude|gemini|llama|"
    r"data|cloud|digital|enterprise|business|platform|solution|solutions|service|services|product|"
    r"products|team|teams|group|company|corporation|inc|ltd|llc|center|centre|institute|university|"
    r"agent|agents|model|models|system|systems|process|work|human|humans|people|person|customer|"
    r"customers|partner|partners|market|industry|technology|software|hardware|network|security|"
    r"january|february|march|april|may|june|july|august|september|october|november|december)$", re.I)

def clean_org(s):
    s = s.strip(" .,·-–—:'\"()[]").strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(에서는|에서|에게|으로|이라는|라는|이라고|라고|이며|의|은|는|을|를|도|과|와|측)$", "", s).strip()
    if not (2 <= len(s) <= 34): return None
    if BAD_EN.match(s): return None
    if s in KO_NOISE: return None
    if re.fullmatch(r"[가-힣]{2,4}", s) and s in KO_NOISE: return None
    # 순한글 2~3자 일반명사 제거 (조직명은 보통 4자 이상 또는 고유 접미사 보유)
    if re.fullmatch(r"[가-힣]{2,3}", s): return None
    if re.fullmatch(r"[\d\W_]+", s): return None
    # 조직명 형태 게이트: (a) 라틴 고유명사(모든 어절 대문자 시작) (b) 한글 조직 접미사 보유
    #                    (c) 공백 없는 한글 3~10자 (음차 상호 허용)
    latin = bool(re.fullmatch(r"[A-Z][A-Za-z0-9&\.\'\-]*(?:\s+[A-Z0-9][A-Za-z0-9&\.\'\-]*){0,3}", s))
    ko_suf = bool(re.search(r"(전자|은행|카드|증권|생명|화재|보험|텔레콤|통신|중공업|건설|제철|화학|바이오|"
                            r"제약|물산|상사|백화점|홈쇼핑|항공|해운|모빌리티|에너지|전력|가스|공사|공단|"
                            r"의료원|병원|대학교|연구원|연구소|그룹|지주|금융|캐피탈|자산운용|디스플레이|"
                            r"반도체|케미칼|엔지니어링|네트웍스|시스템즈|테크|랩스|클라우드)$", s))
    ko_solo = bool(re.fullmatch(r"[가-힣]{3,10}", s))
    if not (latin or ko_suf or ko_solo): return None
    return s

ROLE_KO = r"(?:CIO|CTO|CEO|CFO|COO|CDO|CISO|부사장|전무|상무|사장|대표|본부장|센터장|팀장|실장|디렉터|매니저|리드|책임|수석|담당자?)"
ROLE_EN = r"(?:CIO|CTO|CEO|CFO|COO|CDO|CISO|VP|SVP|EVP|Head of [A-Za-z ]{2,24}|Director|Manager|Lead|Principal|Partner|Chief [A-Za-z]+ Officer)"
PATS = [
    re.compile(r"([가-힣A-Za-z0-9&\.\- ]{2,26})\s*(?:의|에서)\s*" + ROLE_KO),
    re.compile(r"(?:저는|제가)\s*([가-힣A-Za-z0-9&\.\- ]{2,26})\s*(?:의|에서|에)\s*(?:근무|재직|일하|있습니다|소속)"),
    re.compile(ROLE_EN + r"\s+(?:of|at)\s+([A-Z][A-Za-z0-9&\.\'\- ]{2,30})"),
    re.compile(r"I'?m\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?,?\s+(?:the\s+)?(?:" + ROLE_EN + r"|[a-z ]{3,24})\s+at\s+([A-Z][A-Za-z0-9&\.\'\- ]{2,30})"),
    re.compile(r"고객사(?:인|중|의)?\s*([가-힣A-Za-z0-9&\.\- ]{2,26})"),
    re.compile(r"([가-힣A-Za-z0-9&\.\- ]{3,26})\s*(?:의)?\s*사례(?:를|는|입니다|이며)?"),
    re.compile(r"([A-Z][A-Za-z0-9&\.\'\- ]{2,30})'s\s+(?:journey|story|transformation|experience|case)"),
    re.compile(r"([가-힣A-Za-z0-9&\.\- ]{3,26})(?:에서는|에서)\s*(?:이미|현재|작년|올해)?\s*(?:AI|에이전트|자동화|시스템)"),
    re.compile(r"(?:at|for)\s+([A-Z][A-Za-z0-9&\.\'\- ]{2,30}),?\s+(?:we|they|the team)\s+(?:have|has|had|built|deployed|automated|use)"),
]
CHANNEL_DOCS = collections.defaultdict(set)
for rel in DOCS:
    if rel.startswith("transcripts/channels/"):
        CHANNEL_DOCS[rel.split("/")[2].replace("_", " ")].add(rel)

hit_docs = collections.defaultdict(set)
for rel, d in DOCS.items():
    for p in PATS:
        for m in p.finditer(d["body"]):
            o = clean_org(m.group(1))
            if o: hit_docs[o].add(rel)

CAND = {o for o in hit_docs if len(hit_docs[o]) >= 2} | set(CHANNEL_DOCS)
def key(s): return re.sub(r"[^a-z0-9가-힣]", "", s.lower())
merged = collections.defaultdict(set)
for o in CAND: merged[key(o)].add(o)
CAND2 = {}
for k, vs in merged.items():
    canon = max(vs, key=lambda v: (len(hit_docs.get(v, set())) + len(CHANNEL_DOCS.get(v, set())), -len(v)))
    CAND2[canon] = vs
print(f"[2] 채점 대상 조직 {len(CAND2)}개")

# ---------- 3. 케이스 서사 블록 ----------
BEFORE = re.compile(r"기존에는|예전에는|과거에는|이전에는|원래는|종전에는|수동으로|수작업|엑셀로|종이로|"
                    r"before (?:we|the|this|that)|used to|previously|manual(?:ly)?|by hand|spreadsheet", re.I)
AFTER  = re.compile(r"이제는|현재는|지금은|그 결과|덕분에|단축되었|줄었|늘었|개선되었|가능해졌|절감(?:했|되)|"
                    r"now we|today we|as a result|after (?:we|the|implementing)|we (?:reduced|saved|cut|improved)", re.I)
NUM    = re.compile(r"\d+\s*(?:%|퍼센트|배|명|시간|분|건|일|주|개월|년|억|만|billion|million|x\b|percent|"
                    r"hours|minutes|days|weeks|months|people|FTE|tickets|cases)", re.I)
PROC   = re.compile(r"프로세스|워크플로|업무 흐름|파이프라인|process|workflow|pipeline|end[- ]to[- ]end|"
                    r"앞단|뒷단|upstream|downstream|승인|approval|검토|review|이관|escalat", re.I)
DEPLOY = re.compile(r"도입(?:했|하고|한|해)|구축(?:했|하고|한)|적용(?:했|하고|한)|운영(?:중|하고|한다|되고|합니)|"
                    r"we (?:deployed|rolled out|built|launched|implemented|operate|run)|in production|"
                    r"실제로 (?:쓰|사용|운영|적용)|정식 (?:서비스|출시)|go[- ]live", re.I)
AUTO   = re.compile(r"자동화|무인|사람 없이|사람을 대체|자율|automat|autonomous|without (?:a )?human|zero[- ]touch", re.I)
AUG    = re.compile(r"휴먼 인|사람이 (?:검토|확인|승인|개입)|사람의 개입|최종 (?:판단|승인|책임)|검수|증강|코파일럿|"
                    r"human[- ]in[- ]the[- ]loop|augment|co[- ]?pilot|human (?:review|oversight|approval|judgment)", re.I)
FAIL   = re.compile(r"실패|failed|didn'?t work|잘 안 ?[됐되]|중단(?:했|됐)|폐기|롤백|roll ?back|교훈|lessons? learned|"
                    r"어려웠|시행착오", re.I)
ACTOR  = re.compile(r"(?:CIO|CTO|CEO|CFO|COO|CDO|VP|Head of|Director|부사장|전무|상무|팀장|본부장|센터장|"
                    r"매니저|manager|engineer|엔지니어|분석가|analyst|기술자|technician)", re.I)
AITOPIC = re.compile(r"AI\b|인공지능|에이전트|\bagent|머신러닝|machine learning|딥러닝|deep learning|LLM|"
                     r"거대언어|모델을|모델이|모델로|\bmodel\b|자동화|automat|알고리즘|algorithm|생성형|generative|"
                     r"GPT|코파일럿|copilot|챗봇|chatbot|프롬프트|prompt|RAG|파운데이션|foundation model", re.I)
BLK = 2000; STEP = 1000

def blocks_in(seg):
    """세그먼트 안의 케이스 서사 블록 수와 품질"""
    out = []
    for i in range(0, max(1, len(seg) - BLK + 1), STEP):
        w = seg[i:i+BLK]
        has_start = bool(DEPLOY.search(w)) or bool(BEFORE.search(w))
        has_after = bool(AFTER.search(w))
        nn = len(NUM.findall(w))
        has_mech = bool(PROC.search(w)) or bool(AUTO.search(w)) or bool(AUG.search(w))
        has_ai = bool(AITOPIC.search(w))
        if has_start and has_after and nn >= 1 and has_mech and has_ai:
            out.append(dict(nums=nn, before=bool(BEFORE.search(w)), fail=bool(FAIL.search(w)),
                            actor=bool(ACTOR.search(w)), aug=bool(AUG.search(w)), auto=bool(AUTO.search(w))))
    return out

W = 1200
def analyze(canon, variants):
    own = set();
    for ch, docs in CHANNEL_DOCS.items():
        if key(ch) in {key(v) for v in variants}: own |= docs
    third = set()
    for v in variants: third |= hit_docs.get(v, set())
    third -= own
    if not (own or third): return None
    rxs = [re.compile(re.escape(v).replace(r"\ ", r"\s*"), re.I) for v in variants]
    blocks = []; months = set(); per_doc = []; nar = 0; c = collections.Counter()
    for rel in sorted(own | third):
        d = DOCS[rel]
        if rel in own:
            seg = d["body"]
        else:
            segs = []
            for rx in rxs:
                for m in rx.finditer(d["body"]):
                    segs.append(d["body"][max(0, m.start()-W): m.end()+W])
                    if len(segs) >= 10: break
            if not segs: continue
            seg = " ".join(segs)
        nar += len(seg)
        bl = blocks_in(seg)
        if bl:
            blocks += bl
            per_doc.append((rel, len(bl), sum(b["nums"] for b in bl)))
            if d["month"]: months.add(d["month"])
        c["auto"] += len(AUTO.findall(seg)); c["aug"] += len(AUG.findall(seg))
        c["fail"] += len(FAIL.findall(seg)); c["nums"] += len(NUM.findall(seg))
    nb = len(blocks); src = len(per_doc)
    if nb >= 3 and src >= 2 and c["nums"] >= 5: verdict = "CORE"
    elif nb >= 1:                                verdict = "PART"
    else:                                        verdict = "THIN"
    return dict(org=canon, verdict=verdict, blocks=nb, block_srcs=src,
                own_src=len(own), third_src=len(third), months=len(months),
                nar_kb=round(nar/1024, 1), nums=c["nums"],
                blk_with_before=sum(1 for b in blocks if b["before"]),
                blk_with_fail=sum(1 for b in blocks if b["fail"]),
                blk_with_actor=sum(1 for b in blocks if b["actor"]),
                blk_dual=sum(1 for b in blocks if b["auto"] and b["aug"]),
                auto=c["auto"], aug=c["aug"], fail=c["fail"],
                variants="|".join(sorted(variants)),
                top_docs="|".join(r for r, _, _ in sorted(per_doc, key=lambda x: -x[1])[:5]))

rows = [r for r in (analyze(c, v) for c, v in CAND2.items()) if r]
rows.sort(key=lambda r: (-r["blocks"], -r["block_srcs"], -r["nums"]))
with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
vc = collections.Counter(r["verdict"] for r in rows)
print(f"[3] {len(rows)}개 채점 → {OUT}")
print("   판정 분포:", dict(vc))
print(f"\n{'조직':28}{'판정':>6}{'블록':>5}{'블록소스':>7}{'자기':>5}{'3자':>4}{'월':>4}"
      f"{'서사KB':>8}{'수치':>6}{'before':>7}{'실패':>5}{'행위자':>7}{'양축':>5}")
for r in rows[:90]:
    print(f"{r['org'][:28]:28}{r['verdict']:>6}{r['blocks']:>5}{r['block_srcs']:>7}{r['own_src']:>5}"
          f"{r['third_src']:>4}{r['months']:>4}{r['nar_kb']:>8}{r['nums']:>6}"
          f"{r['blk_with_before']:>7}{r['blk_with_fail']:>5}{r['blk_with_actor']:>7}{r['blk_dual']:>5}")
json.dump(rows, open("/tmp/claude-0/-home-user-youtube-scrap/976172e8-99ab-50e9-bed4-da98f885dd8b/scratchpad/feas.json","w"), ensure_ascii=False)
