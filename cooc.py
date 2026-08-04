# -*- coding: utf-8 -*-
"""좁은 창(window) 안에서 자동화 신호와 증강 신호가 동시에 나타나는 구절을 전수 추출.
   = '한 과업/프로세스에서 두 축을 함께 설계한' 진술만 남긴다."""
import re, os, glob, json
ROOT="/home/user/youtube-scrap"; W=700

AUTO = re.compile("|".join([
 r"완전\s*자동화", r"자동화", r"자동으로\s*처리", r"무인", r"사람\s*없이", r"사람을\s*대체",
 r"자율(적|성|형)", r"에이전트가\s*(직접|알아서|스스로)",
 r"fully automat", r"end[- ]to[- ]end", r"automat(e|ed|es|ing|ion)", r"autonomous",
 r"without (a )?human", r"straight[- ]through", r"zero[- ]touch", r"deflect",
]), re.I)
AUG = re.compile("|".join([
 r"휴먼\s*인\s*더\s*루프", r"휴먼\s*인더루프", r"사람이\s*검토", r"사람이\s*확인", r"사람이\s*승인",
 r"사람이\s*개입", r"사람의\s*개입", r"최종\s*판단", r"최종\s*편집", r"검수", r"증강",
 r"코파일럿", r"사람한테\s*(가|넘)", r"사람에게\s*(에스컬|이관|넘)",
 r"human[- ]in[- ]the[- ]loop", r"human (review|oversight|judgment|judgement|approval|expert)",
 r"augment", r"co[- ]?pilot", r"escalat\w+ to (a )?human", r"sign[- ]?off", r"approval step",
]), re.I)
# 패러독스 관리(분화·통합·순환·재투자) 신호가 같은 창에 있으면 가점
MGMT = re.compile("|".join([
 r"점진|단계적|처음에?는|나중에|성숙도|레벨|신뢰가?\s*쌓|검증(이)?\s*되면|권한을?\s*(확대|나누)",
 r"앞단|뒷단|다음\s*단계|프로세스\s*전체|워크플로우?\s*전체",
 r"확보(한|된)\s*시간|절감(한|된)\s*시간|재배치|고부가가치|더\s*가치\s*있는",
 r"최종\s*책임|책임\s*소재|거버넌스|감사\s*추적|권한\s*관리",
 r"gradual|progressiv|maturity|over time|once (proven|validated)|crawl,? walk",
 r"upstream|downstream|whole (workflow|process)|free[sd]? up|redeploy|reinvest",
 r"accountab|audit trail|governance|guardrail|separation of duties",
]), re.I)
NUM = re.compile(r"\d+\s*(%|퍼센트|배|명|시간|건|일|분|주|개월|x\b)|\d+\s*(percent|hours|people|tickets|cases|days)", re.I)

hits=[]
for path in glob.glob(os.path.join(ROOT,"transcripts","**","*.md"), recursive=True):
    rel=os.path.relpath(path, ROOT)
    if rel.endswith("README.md"): continue
    raw=open(path,encoding="utf-8",errors="ignore").read()
    body=re.sub(r"\s+"," ", raw.split("## 스크립트",1)[-1])
    if len(body)<1200: continue
    tm=re.search(r"^#\s+(.+)$", raw, re.M); ch=re.search(r"- 채널:\s*(.+)", raw)
    url=re.search(r"- 영상 링크:\s*(\S+)", raw); dt=re.search(r"- 업로드일:\s*(.+)", raw)
    windows=[]
    for m in AUG.finditer(body):
        s=max(0,m.start()-W); e=min(len(body), m.end()+W)
        seg=body[s:e]
        if not AUTO.search(seg): continue
        if windows and s < windows[-1][1]-W//2: continue
        windows.append((s,e))
        mg=len(MGMT.findall(seg)); nm=len(NUM.findall(seg))
        hits.append(dict(file=rel, title=(tm.group(1).strip() if tm else ""),
            channel=(ch.group(1).strip() if ch else ""), date=(dt.group(1).strip() if dt else ""),
            url=(url.group(1) if url else ""), mgmt=mg, nums=nm,
            seg=seg.strip()))
# 파일 단위 집계
from collections import defaultdict
agg=defaultdict(lambda: dict(n=0,mgmt=0,nums=0))
for h in hits:
    a=agg[h["file"]]; a["n"]+=1; a["mgmt"]+=h["mgmt"]; a["nums"]+=h["nums"]
    a.update(title=h["title"], channel=h["channel"], date=h["date"], url=h["url"])
rank=sorted(agg.items(), key=lambda kv: kv[1]["n"]*1.0 + kv[1]["mgmt"]*0.8 + kv[1]["nums"]*0.3, reverse=True)
json.dump(hits, open("/tmp/claude-0/-home-user-youtube-scrap/976172e8-99ab-50e9-bed4-da98f885dd8b/scratchpad/cooc.json","w"), ensure_ascii=False)
print("co-occurrence windows:", len(hits), "in files:", len(agg))
print()
for f,a in rank[:45]:
    print(f'w{a["n"]:>3} m{a["mgmt"]:>3} n{a["nums"]:>3} | {a["date"][:10]:10} | {a["channel"][:20]:20} | {a["title"][:62]}')
