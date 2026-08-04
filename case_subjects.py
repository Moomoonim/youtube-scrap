# -*- coding: utf-8 -*-
"""케이스 서사 블록의 '주체 조직'을 식별해 집계 (v4).

v3의 한계: 채널 보유 조직에는 문서 전체가 귀속되므로, 벤더 채널의 고객 사례 블록이
벤더 자신의 서사로 잘못 집계된다.

v4는 관점을 뒤집는다.
  1) 코퍼스 전체를 훑어 '케이스 서사 블록'을 먼저 찾는다.
  2) 각 블록 안에서 주체 조직을 식별한다(블록 내 조직명 등장 + 주체 표지).
  3) 조직별로 블록 수·소스 수·시점 폭을 집계한다.
출력: analysis/case_subjects.csv, analysis/case_blocks.csv
"""
import re, os, csv, glob, json, collections

ROOT = "/home/user/youtube-scrap"

# ---------- 코퍼스 ----------
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
                     body=body, month=(up[:7] if up else (mm.group(1)[:7] if mm else "")),
                     owner=(rel.split("/")[2].replace("_", " ") if rel.startswith("transcripts/channels/") else ""))
print(f"[1] 문서 {len(DOCS)}건")

# ---------- 블록 게이트 ----------
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
AITOPIC = re.compile(r"AI\b|인공지능|에이전트|\bagent|머신러닝|machine learning|LLM|자동화|automat|"
                     r"알고리즘|algorithm|생성형|generative|GPT|코파일럿|copilot|챗봇|chatbot|RAG", re.I)
BLK, STEP = 2000, 1000

# ---------- 조직 사전 ----------
CHANNELS = sorted({d["owner"] for d in DOCS.values() if d["owner"]})
KO_KNOWN = """삼성SDS 삼성전자 삼성물산 삼성바이오로직스 삼성증권 삼성생명 SK텔레콤 SK하이닉스 SK이노베이션
LG전자 LG화학 LG에너지솔루션 LGCNS LG유플러스 현대자동차 현대차 기아 현대모비스 포스코 네이버 카카오
쿠팡 토스 배달의민족 우아한형제들 무신사 당근마켓 야놀자 크래프톤 넥슨 엔씨소프트 하이브 롯데 신세계
이마트 한화 두산 효성 코웨이 셀트리온 유한양행 우리은행 신한은행 하나은행 국민은행 기업은행 농협
카카오뱅크 케이뱅크 토스뱅크 미래에셋 한국투자증권 KT 한국전력 대한항공 아시아나 리바이스 유니레버
세일즈포스 딜로이트 액센츄어 맥킨지 우아한 스타벅스 나이키 아마존 구글 마이크로소프트 메타 애플""".split()
STOP_ORG = set("""The This That There Here What When Where And But For With You Your We Our They Their It Its
AI ML LLM API SDK GPU CPU CEO CTO CIO CFO COO HR IT RPA ROI KPI SaaS MCP RAG NLP IoT GenAI Gen
Data Cloud Digital Enterprise Business Platform Solution Solutions Service Services Product Products
Team Teams Group Company Center Institute University Agent Agents Model Models System Systems Process
Human Humans People Customer Customers Partner Partners Market Industry Technology Software Network
Security January February March April May June July August September October November December
Q1 Q2 Q3 Q4 GPT ChatGPT Claude Gemini Llama Copilot Yes No OK Okay Thanks Thank Hello Welcome Please
Let Look Right Great Good Best Very Most One Two Three First Second Next Last New Now Today
Because However Therefore Also Then Just Even Still Already Actually Really Well So Um Uh Yeah
United States America China Japan Korea Europe Germany France India Asia Africa
Excel Word PowerPoint Slack Teams Zoom Google Docs Sheets Drive Gmail Outlook GitHub Git Python
North South East West Global Local Real Full Open Free Live Live""".split())

def orgs_in(block):
    found = collections.Counter()
    for m in re.finditer(r"\b([A-Z][A-Za-z0-9&\.\'\-]{1,}(?:\s+[A-Z][A-Za-z0-9&\.\'\-]{1,}){0,2})\b", block):
        s = m.group(1).strip(" .-'")
        toks = s.split()
        if len(s) < 3: continue
        if any(t in STOP_ORG for t in toks): continue
        found[s] += 1
    for k in KO_KNOWN:
        n = block.count(k)
        if n: found[k] += n
    for c in CHANNELS:
        n = block.count(c)
        if n: found[c] += n
    return found

# ---------- 블록 수집 ----------
blocks = []
for rel, d in DOCS.items():
    b = d["body"]
    for i in range(0, max(1, len(b) - BLK + 1), STEP):
        w = b[i:i+BLK]
        if not ((DEPLOY.search(w) or BEFORE.search(w)) and AFTER.search(w)
                and len(NUM.findall(w)) >= 1
                and (PROC.search(w) or AUTO.search(w) or AUG.search(w))
                and AITOPIC.search(w)):
            continue
        blocks.append(dict(rel=rel, pos=i, w=w,
                           nums=len(NUM.findall(w)), before=bool(BEFORE.search(w)),
                           fail=bool(FAIL.search(w)), actor=bool(ACTOR.search(w)),
                           auto=bool(AUTO.search(w)), aug=bool(AUG.search(w))))
print(f"[2] 케이스 서사 블록 {len(blocks)}개 ({len({b['rel'] for b in blocks})}개 문서)")

# ---------- 주체 귀속 ----------
agg = collections.defaultdict(lambda: dict(blocks=0, srcs=set(), months=set(), nums=0,
                                           before=0, fail=0, actor=0, dual=0, owners=collections.Counter(),
                                           examples=[]))
for b in blocks:
    d = DOCS[b["rel"]]
    cands = orgs_in(b["w"])
    if not cands: continue
    top = [o for o, n in cands.most_common(3) if n >= 2] or [cands.most_common(1)[0][0]]
    for o in top:
        a = agg[o]
        a["blocks"] += 1; a["srcs"].add(b["rel"]); a["nums"] += b["nums"]
        if d["month"]: a["months"].add(d["month"])
        a["before"] += b["before"]; a["fail"] += b["fail"]; a["actor"] += b["actor"]
        a["dual"] += (b["auto"] and b["aug"])
        a["owners"][d["owner"] or f"KW:{d['coll']}"] += 1
        if len(a["examples"]) < 3: a["examples"].append(f"{b['rel']}@{b['pos']}")

rows = []
for o, a in agg.items():
    if a["blocks"] < 2: continue
    own_ch = any(re.sub(r"\W","",k.lower()) == re.sub(r"\W","",o.lower()) for k in a["owners"])
    self_blocks = sum(v for k, v in a["owners"].items() if re.sub(r"\W","",k.lower()) == re.sub(r"\W","",o.lower()))
    ext_blocks = a["blocks"] - self_blocks
    verdict = ("CORE" if a["blocks"] >= 5 and len(a["srcs"]) >= 3 and a["nums"] >= 10
               else "PART" if a["blocks"] >= 3 and len(a["srcs"]) >= 2
               else "THIN")
    rows.append(dict(org=o, verdict=verdict, blocks=a["blocks"], self_blocks=self_blocks,
                     ext_blocks=ext_blocks, srcs=len(a["srcs"]), months=len(a["months"]),
                     nums=a["nums"], w_before=a["before"], w_fail=a["fail"], w_actor=a["actor"],
                     dual=a["dual"], own_channel=int(own_ch),
                     channels=";".join(f"{k}:{v}" for k, v in a["owners"].most_common(4)),
                     examples="|".join(a["examples"])))
rows.sort(key=lambda r: (-r["blocks"], -r["srcs"]))
out = os.path.join(ROOT, "analysis", "case_subjects.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(f"[3] 주체 조직 {len(rows)}개 → {out}")
print("   판정:", dict(collections.Counter(r["verdict"] for r in rows)))
print(f"\n{'조직':26}{'판정':>6}{'블록':>5}{'자사':>5}{'타사':>5}{'소스':>5}{'월':>4}{'수치':>6}"
      f"{'before':>7}{'실패':>5}{'행위자':>7}{'양축':>5} 주요채널")
for r in rows[:60]:
    print(f"{r['org'][:26]:26}{r['verdict']:>6}{r['blocks']:>5}{r['self_blocks']:>5}{r['ext_blocks']:>5}"
          f"{r['srcs']:>5}{r['months']:>4}{r['nums']:>6}{r['w_before']:>7}{r['w_fail']:>5}"
          f"{r['w_actor']:>7}{r['dual']:>5}  {r['channels'][:52]}")
# 블록 원문 저장 (검증용)
with open(os.path.join(ROOT, "analysis", "case_blocks.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["file","pos","nums","before","fail","actor","auto","aug","text"])
    for b in blocks: w.writerow([b["rel"], b["pos"], b["nums"], b["before"], b["fail"], b["actor"], b["auto"], b["aug"], b["w"]])
print("   블록 원문 → analysis/case_blocks.csv")
