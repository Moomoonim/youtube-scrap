#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""논문 인사이트 축별 코퍼스 사례 검색기.

Sun et al.(2024) "Uncovering the Interactions Between the Enterprise AI
Transformation, Supply Chain Concentration, and Corporate Risk-Taking Capacity"
(IEEE TEM 71:11315) 검토에서 도출한 8개 인사이트 축에 대응하는 발언을
transcripts/ 전체에서 찾아 근거 문장과 함께 뽑는다.

축은 AXES에 정의한다. 각 축은
  core    : 그 축의 주제어(필수, 문장 단위 매칭)
  context : 축을 성립시키는 보조어(문서 단위 필수 + 문장 단위 가점)
  boost   : 그 축의 '주장'을 만드는 어휘(문장 단위 가점 2점)
  gate    : 문장 채택 최소 점수(2=core+맥락, 3=boost 필수, 4=boost+맥락 동시)
로 구성되며, 문장이 core에 걸리고 문서에 context가 있으면 후보로 채택한다.
gate는 축마다 잡음 특성이 달라 개별 조정했다(예: F축의 '그래서'류 접속사,
D축의 의례적 '파트너십 감사' 발언을 배제하기 위해 4로 올림).
순수 규칙 기반이라 재현·감사 가능하다(CODEBOOK_v2와 동일 원칙).

사용:
    python paper_case_search.py                 # 전체 축
    python paper_case_search.py --axis A C      # 일부 축만
    python paper_case_search.py --top 40        # 축별 상위 N 문서

산출:
    analysis/paper_cases_sun2024.csv            # 기계 판독용(문장 단위)
    analysis/PAPER_CASES_SUN2024.md             # 사람이 읽는 축별 후보 목록
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPTS = os.path.join(ROOT, "transcripts")
ANALYSIS = os.path.join(ROOT, "analysis")
CATALOG = os.path.join(ANALYSIS, "catalog.csv")

# ---------------------------------------------------------------- 축 정의

AXES = {
    "A": {
        "title": "AX/DX 개념 경계 — AX를 DX와 구분하거나 'DX의 심화'로 규정하는 발언",
        "core": r"(디지털\s*(전환|트랜스포메이션)|디지털화|DX|digital\s+transformation|digitali[sz]ation)",
        "context": r"(AI\s*전환|AX|AI\s+transformation|인공지능\s*전환|전환의\s*다음|next\s+(phase|wave|era)|그\s*다음\s*단계)",
        "boost": r"(다르|차이|구분|넘어|이상|beyond|different\s+from|not\s+just|더\s*이상|단계|연장|심화|deeper|extension|evolution|진화)",
        "gate": 2,
    },
    "B": {
        "title": "측정 공백 — DX 지표로 안 잡히는 것(생성성·피드백 루프 속도·의사결정 위임)",
        "core": r"(어떻게\s*(측정|계량|평가)|측정\s*(방법|지표|기준|단위)|지표|KPI|메트릭|how\s+(do|would)\s+you\s+measure|metric|measurement|benchmark)",
        "context": r"(ROI|생산성|productivity|성과|value|가치|정량|정성|증명|prove)",
        "boost": r"(바꾸|재정의|redefine|new\s+metric|다른\s*지표|기존\s*지표|old\s+metric|측정할\s*수\s*없|hard\s+to\s+measure|정량화가?\s*(어렵|안)|잡히지\s*않)",
        "gate": 3,
    },
    "C": {
        "title": "공급망·협력구조 — AX가 조달/공급자 관계를 바꾸는가(집중 vs 분산)",
        "core": r"(공급망|공급\s*업체|공급사|협력사|하청|조달|구매팀?|벤더|supply\s+chain|supplier|procurement|vendor|sourcing|distributor|유통(망|사)?)",
        "context": r"(AI|인공지능|에이전트|agent|모델|자동화|automat)",
        "boost": r"(집중|분산|다변화|다각화|의존(도|성)|락인|lock[-\s]?in|single\s+vendor|multi[-\s]?vendor|multi[-\s]?model|교체|바꾸|switch|줄이|늘리|협상력|bargaining|negotiat)",
        "gate": 3,
    },
    "D": {
        "title": "제도·관계 맥락 — 신뢰·장기계약·관계기반 거래 대 알고리즘 매개 조정",
        "core": r"(신뢰|trust|장기\s*(계약|거래|관계)|관계\s*(기반|중심)|계약(서|을|이|은)?|contract|거래\s*관행|handshake|악수)",
        "context": r"(AI|에이전트|agent|알고리즘|algorithm|자동화|automat)",
        "boost": r"(대체|치환|replace|사람이?\s*(하던|맡던|했던)|중개|intermediar|기업\s*간|B2B|협상|negotiat|SLA|감사\s*(추적|가능)|audit|서명|sign(ed)?\s+off|검증|verif)",
        "gate": 4,
    },
    "E": {
        "title": "서사–수치 괴리 — 효과가 통계적으로만 존재하거나 실질 크기가 미미한 사례",
        "core": r"(파일럿|PoC|POC|실증|시범|pilot|proof\s+of\s+concept|파일롯)",
        "context": r"(전사|확대|scale|확산|배포|deploy|양산|production)",
        "boost": r"(멈추|중단|안\s*넘어가|넘지\s*못|stuck|stall|실패|fail|95\s*%|대부분|그친|머무|하지\s*못|없었|미미|작(다|았)|체감)",
        "gate": 3,
    },
    "F": {
        "title": "양방향 내생성 — 협력구조가 AX의 결과이자 원인(순환)인 발언",
        "core": r"(공급\s*(업체|사|망)|협력사|파트너사|벤더|고객사|supplier|vendor|partner\s+(company|ecosystem)|하청|외주|아웃소싱|outsourc)",
        "context": r"(AI|인공지능|에이전트|agent|자동화|automat|도입|전환)",
        "boost": r"(때문에|덕분에|그\s*결과|결과적으로|because|led\s+to|resulted\s+in|enabled|thanks\s+to|선순환|악순환|피드백\s*루프|feedback\s+loop|역으로|반대로|상호|서로|늘(렸|었|어났)|줄(였|었|어들)|바꾸|교체|다변화|의존)",
        "gate": 4,
    },
    "G": {
        "title": "거버넌스 수사 대 재무 검증 — 정렬·안전은 말하되 검증은 비용/ROI로만",
        "core": r"(거버넌스|governance|정렬|alignment|안전(성)?|safety|책임\s*있는|responsible\s+AI|윤리|ethic|가드레일|guardrail|규정\s*준수|compliance|RLHF|휴먼\s*인\s*더\s*루프|human[-\s]in[-\s]the[-\s]loop)",
        "context": r"(ROI|비용|cost|절감|saving|매출|revenue|생산성|productivity|예산|budget)",
        "boost": r"(정당화|justify|business\s+case|측정(할|하|해)|증명|입증|prove|이사회|board|CFO|경영진에게|보고(해|하|를)|예산\s*(승인|확보)|ROI(를|가)|투자\s*(대비|회수))",
        "gate": 3,
    },
    "H": {
        "title": "조직 조건부성 — 자원 여유·제도적 지위·생애주기에 따라 AX 유인이 갈림",
        "core": r"(대기업|중소(기업)?|스타트업|startup|enterprise|공기업|공공기관|국(영|유)|레거시|legacy|전통\s*(기업|산업)|SMB|SME|중견)",
        "context": r"(AI|인공지능|전환|도입|transformation|adopt)",
        "boost": r"(느리|빠르|더\s*쉽|더\s*어렵|유리|불리|여유|여력|절박|위기|생존|survival|urgen|잃을\s*게|risk[-\s]averse|보수적|conservative|규제|승인|의사결정\s*(속도|구조))",
        "gate": 3,
    },
    "I": {
        "title": "위험감수 역량 — AX와 실패 허용·실험·리스크 감수의 관계",
        "core": r"(리스크|위험\s*(감수|부담|을\s*지)|risk[-\s](taking|tolerance|appetite)|실패를?\s*(허용|용인|감수)|tolerate\s+failure|실험(을|하)|experiment|베팅|bet\s+on)",
        "context": r"(AI|인공지능|에이전트|agent|전환|transformation|도입)",
        "boost": r"(투자|investment|의사결정|decision|경영진|leadership|CEO|이사회|board|과감|공격적|aggressive|보수적|conservative|불확실|uncertain)",
        "gate": 3,
    },
}

SENT_SPLIT = re.compile(r"(?<=[.!?。])\s+|(?<=[다요죠음])\.\s+|\n+")
HEAD_LINK = re.compile(r"영상 링크:\s*(\S+)")
HEAD_CH = re.compile(r"채널:\s*(.+)")
HEAD_DATE = re.compile(r"업로드일:\s*(\S+)")


def load_catalog():
    """file -> catalog row (relevance/stance/layer 등 메타 보강용)."""
    meta = {}
    if not os.path.exists(CATALOG):
        return meta
    with open(CATALOG, encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            meta[row.get("file", "").replace("\\", "/")] = row
    return meta


def iter_transcripts():
    for dirpath, _dirs, files in os.walk(TRANSCRIPTS):
        for name in sorted(files):
            if not name.endswith(".md") or name == "README.md":
                continue
            yield os.path.join(dirpath, name)


def parse(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    head, _, body = raw.partition("## 스크립트")
    if not body:
        body = raw
    title = raw.lstrip().split("\n", 1)[0].lstrip("# ").strip()
    url = (HEAD_LINK.search(head) or [None, ""])[1] if HEAD_LINK.search(head) else ""
    ch = HEAD_CH.search(head)
    dt = HEAD_DATE.search(head)
    return {
        "title": title,
        "url": url,
        "channel": ch.group(1).strip() if ch else "",
        "date": dt.group(1).strip() if dt else "",
        "body": body,
    }


def compile_axes(keys):
    out = {}
    for key in keys:
        spec = AXES[key]
        out[key] = {
            "title": spec["title"],
            "core": re.compile(spec["core"], re.I),
            "context": re.compile(spec["context"], re.I),
            "boost": re.compile(spec["boost"], re.I),
            "gate": spec.get("gate", 2),
        }
    return out


def scan(axes, top_n):
    meta = load_catalog()
    hits = defaultdict(list)  # axis -> [record]
    scanned = 0

    for path in iter_transcripts():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        doc = parse(path)
        body = doc["body"]
        if len(body) < 400:
            continue
        scanned += 1
        row = meta.get(rel, {})
        if row.get("relevance") in ("noise", "off_topic"):
            continue

        sentences = None
        for key, ax in axes.items():
            if not ax["context"].search(body):
                continue
            if not ax["core"].search(body):
                continue
            if sentences is None:
                sentences = [s.strip() for s in SENT_SPLIT.split(body)]
            picked = []
            for sent in sentences:
                n = len(sent)
                if n < 25 or n > 600:
                    continue
                if not ax["core"].search(sent):
                    continue
                score = 1 + (2 if ax["boost"].search(sent) else 0)
                score += 1 if ax["context"].search(sent) else 0
                if score < ax["gate"]:  # 축별 채택 문턱(잡음 특성에 맞춰 조정)
                    continue
                picked.append((score, sent))
            if not picked:
                continue
            picked.sort(key=lambda x: (-x[0], -len(x[1])))
            doc_score = sum(s for s, _ in picked[:5]) + min(len(picked), 10) * 0.5
            hits[key].append(
                {
                    "axis": key,
                    "score": round(doc_score, 1),
                    "n_sent": len(picked),
                    "channel": doc["channel"] or row.get("channel", ""),
                    "date": doc["date"] or row.get("date", ""),
                    "title": doc["title"],
                    "relevance": row.get("relevance", ""),
                    "stance": row.get("stance", ""),
                    "layer": row.get("layer", ""),
                    "hq": row.get("hq_country", ""),
                    "url": doc["url"],
                    "file": rel,
                    "quotes": [s for _, s in picked[:4]],
                }
            )

    for key in hits:
        hits[key].sort(key=lambda r: -r["score"])
        hits[key] = hits[key][:top_n]
    return hits, scanned


def write_outputs(hits, axes):
    os.makedirs(ANALYSIS, exist_ok=True)
    csv_path = os.path.join(ANALYSIS, "paper_cases_sun2024.csv")
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(
            ["axis", "axis_title", "score", "n_sent", "date", "channel", "hq",
             "layer", "relevance", "stance", "title", "quote", "url", "file"]
        )
        for key in sorted(hits):
            for rec in hits[key]:
                for q in rec["quotes"]:
                    w.writerow(
                        [key, axes[key]["title"], rec["score"], rec["n_sent"],
                         rec["date"], rec["channel"], rec["hq"], rec["layer"],
                         rec["relevance"], rec["stance"], rec["title"], q,
                         rec["url"], rec["file"]]
                    )

    md_path = os.path.join(ANALYSIS, "PAPER_CASES_SUN2024.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("# Sun et al.(2024) 인사이트 축별 코퍼스 후보 사례\n\n")
        fh.write("> `paper_case_search.py` 자동 추출(규칙 기반 1차). "
                 "발언 주체·맥락 미검증이므로 인용 전 원문 확인 필수.\n\n")
        for key in sorted(hits):
            fh.write(f"## 축 {key} — {axes[key]['title']}\n\n")
            fh.write(f"후보 문서 {len(hits[key])}건\n\n")
            for rec in hits[key]:
                fh.write(
                    f"### [{rec['score']}] {rec['channel']} · {rec['date']} — {rec['title']}\n"
                )
                fh.write(
                    f"- {rec['relevance']}/{rec['stance']} · {rec['layer']} · {rec['hq']} · "
                    f"[영상]({rec['url']}) · `{rec['file']}`\n"
                )
                for q in rec["quotes"]:
                    fh.write(f"  - > {q}\n")
                fh.write("\n")
    return csv_path, md_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--axis", nargs="*", default=sorted(AXES), help="검색할 축 키")
    ap.add_argument("--top", type=int, default=30, help="축별 상위 문서 수")
    args = ap.parse_args()

    unknown = [k for k in args.axis if k not in AXES]
    if unknown:
        sys.exit(f"알 수 없는 축: {unknown}. 가능: {sorted(AXES)}")

    axes = compile_axes(args.axis)
    hits, scanned = scan(axes, args.top)
    csv_path, md_path = write_outputs(hits, axes)

    print(f"스캔 문서 {scanned}건")
    for key in sorted(hits):
        print(f"  축 {key}: 후보 {len(hits[key])}건 (상위 {args.top})")
    print(f"→ {csv_path}\n→ {md_path}")


if __name__ == "__main__":
    main()
