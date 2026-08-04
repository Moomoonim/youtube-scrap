# -*- coding: utf-8 -*-
"""Raisch & Krakowski(2021) 자동화-증강 패러독스 구성개념을 규칙기반으로 코딩해
   저장소 수집 스크랩(transcripts/**/*.md)에서 '양쪽 모두 최적화' 사례를 찾는다."""
import re, os, csv, json, glob

ROOT = "/home/user/youtube-scrap"

def L(*pats):
    return re.compile("|".join(pats), re.I)

# 1) AUTOMATION: 기계가 과업을 인계, 인간 out of the loop
AUTO = L(
 r"완전\s*자동화", r"전\s*자동", r"자동화", r"자동으로\s*처리", r"자동\s*실행", r"무인",
 r"사람\s*없이", r"사람이\s*개입하지\s*않", r"사람\s*손을\s*거치지", r"사람을\s*대체",
 r"인력\s*감축", r"인원\s*감축", r"헤드카운트", r"자율\s*실행", r"셀프\s*서비스",
 r"end[- ]to[- ]end automation", r"fully automat", r"full automation", r"automate[ds]?\b",
 r"automation", r"autonomous(ly)?", r"without (a )?human", r"human out of the loop",
 r"straight[- ]through", r"unattended", r"zero[- ]touch", r"hands[- ]off",
 r"replace (people|humans|workers|staff|headcount)", r"deflect(ion|ed)?\b",
)
# 2) AUGMENTATION: 인간-기계 밀착 협업, human in the loop
AUG = L(
 r"휴먼\s*인\s*더\s*루프", r"사람이\s*검토", r"사람이\s*확인", r"사람이\s*승인",
 r"최종\s*판단은?\s*사람", r"사람의\s*판단", r"전문가가\s*검", r"검수", r"감수",
 r"코파일럿", r"부조종사", r"증강", r"보조\s*도구", r"사람과\s*함께", r"협업",
 r"human[- ]in[- ]the[- ]loop", r"human in the loop", r"augment(ation|ed|ing|s)?\b",
 r"co[- ]?pilot", r"assist(ant|ive|s|ing)?\b", r"collaborat(e|ion|ing) with",
 r"human (review|oversight|judgment|judgement|approval|expert)",
 r"expert[- ]in[- ]the[- ]loop", r"centaur", r"side by side with",
)
# 3) 시간축 전환: 증강 -> 자동화 (또는 그 역)
CYCLE = L(
 r"처음에?는?\s*사람이", r"초반에?는?\s*사람", r"학습시키", r"길들", r"신뢰가?\s*쌓이",
 r"검증(이)?\s*되면", r"점진적으로\s*자동", r"단계적으로\s*자동", r"자동화로\s*넘어",
 r"자율성을?\s*높", r"권한을?\s*(확대|넓)", r"레벨\s*[1-5]", r"성숙도",
 r"start(ing|ed)? with (a )?human", r"over time,? (we )?automat", r"gradually automat",
 r"graduate[sd]? to", r"increase (the )?autonomy", r"earn(ed|s)? trust",
 r"once (it('s| is)? )?(validated|proven|reliable)", r"crawl,? walk,? run",
 r"training wheels", r"ramp(ed|ing)? up (the )?autonomy", r"progressively",
 r"maturity (model|curve|level)", r"autonomy (level|slider|dial)",
)
# 4) 공간축 spillover: 인접 과업으로 파급
SPILL = L(
 r"앞단", r"뒷단", r"인접", r"다음\s*단계", r"상류", r"하류", r"전\s*공정",
 r"워크플로우?\s*전체", r"프로세스\s*전체", r"파이프라인\s*전체",
 r"upstream", r"downstream", r"adjacent (task|step|process)", r"rest of the (workflow|process)",
 r"end of the (process|workflow)", r"across the (whole |entire )?(workflow|process|pipeline)",
 r"knock[- ]on", r"ripple",
)
# 5) UBS 패턴: 자동화로 확보한 자원을 증강에 재투자
REINVEST = L(
 r"확보(한|된)\s*시간", r"남는\s*시간", r"절감(한|된)\s*시간", r"아낀\s*시간",
 r"더\s*가치\s*있는", r"고부가가치", r"더\s*중요한\s*일", r"재배치", r"전환\s*배치",
 r"freed[- ]up", r"free[sd]? up (time|capacity|people|hours)", r"time saved",
 r"focus on (higher|more) [- ]?value", r"redeploy", r"spend more time on",
 r"reinvest", r"upskill", r"reskill", r"재교육", r"업스킬", r"리스킬",
)
# 6) 통합 조건: 인간이 프로세스 전체 책임 보유
RESP = L(
 r"최종\s*책임", r"책임은\s*사람", r"사람이\s*책임", r"책임\s*소재", r"승인\s*권한",
 r"의사결정\s*권한", r"거버넌스", r"감사\s*추적", r"어카운터빌리티",
 r"accountab(le|ility)", r"human (owns|remains responsible|is responsible)",
 r"sign[- ]off", r"final say", r"audit trail", r"governance", r"guardrail",
 r"escalat(e|ion|es|ed) to (a )?human", r"사람에게\s*(에스컬|넘김|이관)",
)
# 7) 구체성 게이트: 실제 조직의 실행 사례인가 (수치/도입/운영 언어)
CONCRETE = L(
 r"\d+\s*%", r"\d+\s*배", r"\d+\s*명", r"\d+\s*시간", r"\d+\s*건", r"\d+\s*일",
 r"\d+x\b", r"\d+\s*percent", r"\d+ hours", r"\d+ (people|agents|tickets|cases)",
 r"도입(했|하고|한|해)", r"운영(중|하고|한다)", r"적용(했|하고|한)", r"구축(했|하고|한)",
 r"we (deployed|rolled out|built|run|operate)", r"in production", r"실제로\s*(쓰|사용|운영)",
)

def score(txt):
    return {
        "auto": len(AUTO.findall(txt)),
        "aug": len(AUG.findall(txt)),
        "cycle": len(CYCLE.findall(txt)),
        "spill": len(SPILL.findall(txt)),
        "reinvest": len(REINVEST.findall(txt)),
        "resp": len(RESP.findall(txt)),
        "concrete": len(CONCRETE.findall(txt)),
    }

rows = []
for path in glob.glob(os.path.join(ROOT, "transcripts", "**", "*.md"), recursive=True):
    rel = os.path.relpath(path, ROOT)
    if rel.endswith("README.md"):
        continue
    try:
        raw = open(path, encoding="utf-8", errors="ignore").read()
    except Exception:
        continue
    body = raw.split("## 스크립트", 1)[-1]
    w = len(body.split())
    if w < 300:
        continue
    m = re.search(r"^#\s+(.+)$", raw, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    ch = re.search(r"- 채널:\s*(.+)", raw)
    dt = re.search(r"- 업로드일:\s*(.+)", raw)
    s = score(body)
    # 정규화(만 단어당) — 긴 영상 편향 보정
    k = 10000.0 / max(w, 1)
    bal = min(s["auto"], s["aug"])                    # 양축 동시 존재
    para = s["cycle"] + s["spill"] + s["reinvest"] + s["resp"]  # 패러독스 관리 신호
    rows.append(dict(file=rel, title=title,
                     channel=(ch.group(1).strip() if ch else ""),
                     date=(dt.group(1).strip() if dt else ""),
                     words=w, **s, bal=bal, para=para,
                     bal_n=round(bal * k, 2), para_n=round(para * k, 2)))

rows.sort(key=lambda r: (min(r["bal"], 40) * (r["para"] ** 0.5) * (1 + 0.15 * min(r["concrete"], 20))), reverse=True)
out = os.path.join(ROOT, "analysis", "paradox_scan.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    wri = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    wri.writeheader(); wri.writerows(rows)
print("scanned:", len(rows), "->", out)
print()
for r in rows[:40]:
    print(f'{r["bal"]:>3} {r["para"]:>3} c{r["concrete"]:>3} | {r["channel"][:22]:22} | {r["title"][:70]}')
