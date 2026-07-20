"""
수집된 스크립트를 DX / AX / AT 축으로 1차(사전 기반) 분류한다.

- 기준: docs/CODEBOOK.md (코드북 개정 시 아래 사전도 함께 갱신)
- 입력: transcripts/ 아래 모든 영상 .md 파일
- 출력:
    analysis/classified.csv       — 영상별 점수·지배 라벨
    analysis/monthly_summary.csv  — 월×라벨 집계 (시계열 분석용)

직접 실행: python classify.py
"""

import csv
import glob
import os
import re

import config

# ──────────────────────────────────────────────
# 키워드 사전 (한/영) — 코드북의 판별 신호를 구현
# 짧은 약어(AX/DX)는 대문자 단어 경계로만 매칭. 'AT'는 영어 전치사와
# 겹치므로 약어 단독 매칭은 하지 않는다.
# ──────────────────────────────────────────────

DX_PATTERNS = [
    r"\bDX\b", r"디지털\s*전환", r"디지털\s*트랜스포메이션",
    r"digital\s+transformation", r"digitali[sz]ation", r"digiti[sz]ation",
    r"클라우드\s*(전환|이전|도입|마이그레이션)", r"cloud\s+(migration|adoption|first)",
    r"레거시", r"legacy\s+system", r"\bERP\b", r"시스템\s*현대화",
    r"데이터\s*플랫폼", r"data\s+platform", r"data\s+lake", r"데이터\s*레이크",
    r"페이퍼리스", r"paperless", r"이커머스\s*전환", r"모바일\s*전환",
]

AX_PATTERNS = [
    r"\bAX\b", r"AI\s*전환", r"인공지능\s*전환", r"AI\s+transformation",
    r"AI\s*도입", r"AI\s+adoption", r"adopting\s+AI",
    r"생성형\s*AI", r"generative\s+AI", r"\bGenAI\b",
    r"\bLLM\b", r"거대\s*언어\s*모델", r"large\s+language\s+model",
    r"\bGPT\b", r"챗\s*GPT", r"ChatGPT",
    r"머신\s*러닝", r"machine\s+learning", r"딥\s*러닝", r"deep\s+learning",
    r"파운데이션\s*모델", r"foundation\s+model",
    r"AI\s*에이전트", r"AI\s+agent", r"agentic",
    r"코파일럿", r"copilot", r"챗봇", r"chatbot",
    r"파인\s*튜닝", r"fine[-\s]?tuning", r"\bRAG\b", r"프롬프트", r"prompt\s+engineering",
    r"AI\s*(인재|조직|거버넌스|전략)", r"AI\s+(talent|governance|strategy)",
]

AT_PATTERNS = [
    r"algorithmic\s+transformation", r"알고리즘\s*전환",
    r"algorithmic\s+management", r"알고리즘\s*(경영|관리)",
    r"algorithmic\s+(decision|pricing|trading|hiring)",
    r"알고리즘\s*(의사\s*결정|가격|매매|채용|평가)",
    r"automated\s+decision[-\s]?making", r"자동화된\s*의사\s*결정",
    r"알고리즘(이|에\s*의해|으로)\s*(결정|판단|배분|운영)",
    r"algorithm[-\s]driven", r"autonomous\s+(agent|operation|enterprise)",
    r"자율\s*(에이전트|운영)", r"self[-\s]driving\s+(operation|business|enterprise)",
    r"추천\s*알고리즘", r"recommendation\s+algorithm",
]

LABELS = {
    "DX": [re.compile(p, re.IGNORECASE if not p.startswith(r"\bDX") else 0) for p in DX_PATTERNS],
    "AX": [re.compile(p, re.IGNORECASE if not p.startswith(r"\bAX") else 0) for p in AX_PATTERNS],
    "AT": [re.compile(p, re.IGNORECASE) for p in AT_PATTERNS],
}

# 지배 라벨로 인정할 최소 등장 횟수 (코드북 규칙 2)
MIN_HITS = 2


def parse_transcript(path):
    """영상 .md 파일에서 메타데이터와 본문을 뽑는다."""
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    meta = {"title": "", "channel": "", "lang": "", "upload_date": "", "url": ""}
    title_m = re.match(r"#\s*(.+)", content)
    if title_m:
        meta["title"] = title_m.group(1).strip()
    for key, pattern in [
        ("channel", r"-\s*채널:\s*(.+)"),
        ("lang", r"-\s*자막 언어:\s*(.+)"),
        ("upload_date", r"-\s*업로드일:\s*(.+)"),
        ("url", r"-\s*영상 링크:\s*(.+)"),
    ]:
        m = re.search(pattern, content)
        if m:
            meta[key] = m.group(1).strip()

    body = content.split("## 스크립트", 1)
    text = body[1] if len(body) > 1 else content
    return meta, text


def doc_month(path, meta):
    """영상의 연-월을 정한다. 업로드일 우선, 없으면 수집 날짜 폴더."""
    ud = meta.get("upload_date", "")
    m = re.match(r"(\d{4})-(\d{2})", ud)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    m = re.search(r"(\d{4})-(\d{2})-\d{2}", path)  # transcripts/2026-07-18/...
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    return "unknown"


def score_text(text):
    """라벨별 키워드 등장 횟수와 1천 단어당 밀도를 계산한다."""
    words = max(len(text.split()), 1)
    hits = {}
    for label, patterns in LABELS.items():
        n = sum(len(p.findall(text)) for p in patterns)
        hits[label] = n
    density = {label: round(n * 1000 / words, 3) for label, n in hits.items()}
    return hits, density, words


def dominant_label(hits):
    """최소 횟수를 넘는 라벨 중 최다 라벨. 없으면 unclassified."""
    eligible = {k: v for k, v in hits.items() if v >= MIN_HITS}
    if not eligible:
        return "unclassified"
    return max(eligible, key=eligible.get)


def main():
    out_dir = "analysis"
    os.makedirs(out_dir, exist_ok=True)

    files = sorted(
        glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True)
    )
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        hits, density, words = score_text(text)
        source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
        rows.append({
            "file": path.replace(os.sep, "/"),
            "title": meta["title"],
            "channel": meta["channel"],
            "source": source,
            "lang": meta["lang"],
            "month": doc_month(path, meta),
            "words": words,
            "DX_hits": hits["DX"], "AX_hits": hits["AX"], "AT_hits": hits["AT"],
            "DX_per1k": density["DX"], "AX_per1k": density["AX"], "AT_per1k": density["AT"],
            "dominant": dominant_label(hits),
        })

    # 영상별 분류 결과
    with open(os.path.join(out_dir, "classified.csv"), "w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=list(rows[0].keys()) if rows else ["file"])
        writer.writeheader()
        writer.writerows(rows)

    # 월×라벨 집계 (시계열)
    months = {}
    for r in rows:
        m = months.setdefault(r["month"], {"total": 0, "DX": 0, "AX": 0, "AT": 0, "unclassified": 0})
        m["total"] += 1
        m[r["dominant"]] += 1

    with open(os.path.join(out_dir, "monthly_summary.csv"), "w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["month", "total", "DX", "AX", "AT", "unclassified", "AX_share", "DX_share", "AT_share"])
        for month in sorted(months):
            m = months[month]
            t = m["total"] or 1
            writer.writerow([
                month, m["total"], m["DX"], m["AX"], m["AT"], m["unclassified"],
                round(m["AX"] / t, 3), round(m["DX"] / t, 3), round(m["AT"] / t, 3),
            ])

    total = len(rows)
    counts = {}
    for r in rows:
        counts[r["dominant"]] = counts.get(r["dominant"], 0) + 1
    print(f"[classify] 총 {total}건 분류 완료 → analysis/classified.csv")
    for label in ["AX", "DX", "AT", "unclassified"]:
        print(f"[classify]   {label}: {counts.get(label, 0)}건")


if __name__ == "__main__":
    main()
