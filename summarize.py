"""
수집된 영상들을 메타데이터(채널/출처/언어/월/분류라벨) 기준으로 정리하고,
영상별 요약(발췌)을 생성한다.

요약 방식: 현재는 **발췌 요약(extractive lead)** — 스크립트 앞부분에서
의미 있는 분량을 잘라낸 것이다. 별도 LLM 비용 없이 대량(하루 수백 건)
처리가 가능하도록 이렇게 설계했다. 문장 단위 추상 요약(abstractive)이
필요해지면 ANTHROPIC_API_KEY 등을 워크플로우 비밀값으로 추가하고 이
스크립트의 summarize_text() 만 교체하면 된다.

입력: transcripts/ 아래 모든 영상 .md 파일 (+ analysis/classified.csv 있으면 병합)
출력:
    analysis/summaries.csv        — 영상별 메타데이터 + 요약 (기계 판독용)
    analysis/SUMMARY_BY_CHANNEL.md — 채널/출처별로 묶은 사람이 읽는 목록
    analysis/SUMMARY_BY_MONTH.md   — 월×분류라벨로 묶은 사람이 읽는 목록

직접 실행: python summarize.py
"""

import csv
import glob
import os
import re
from collections import defaultdict

import config
from classify import doc_month, parse_transcript

# 요약(발췌) 길이 상한 (단어 수 기준)
SUMMARY_WORDS = 70


def summarize_text(text):
    """스크립트 본문에서 발췌 요약을 만든다.

    문장 부호(. ! ? 다. 요.) 경계를 우선 찾고, 없으면 단어 수 기준으로 자른다.
    """
    text = text.strip()
    if not text:
        return ""

    # 문장 경계 후보를 찾아 SUMMARY_WORDS 단어 근처에서 가장 가까운 경계 사용
    boundaries = [m.end() for m in re.finditer(r"[\.!?]|다\.|요\.|습니다|입니다", text)]
    words = text.split()
    target_char = len(" ".join(words[:SUMMARY_WORDS]))

    if boundaries:
        best = min(boundaries, key=lambda b: abs(b - target_char))
        # 목표 지점에서 너무 멀리 떨어진 경계는 버리고 단어 수 컷으로 대체
        if abs(best - target_char) <= target_char * 0.6 + 40:
            excerpt = text[:best].strip()
            if excerpt:
                return excerpt

    excerpt = " ".join(words[:SUMMARY_WORDS]).strip()
    if len(words) > SUMMARY_WORDS:
        excerpt += " …"
    return excerpt


def load_classification():
    """classify.py 결과가 있으면 파일 경로 → 지배 라벨 매핑을 돌려준다."""
    path = os.path.join("analysis", "classified.csv")
    mapping = {}
    if not os.path.exists(path):
        return mapping
    with open(path, "r", encoding="utf-8-sig", newline="") as fp:
        for row in csv.DictReader(fp):
            mapping[row["file"]] = row.get("dominant", "unclassified")
    return mapping


def collect_rows():
    files = sorted(
        glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True)
    )
    files = [f for f in files if os.path.basename(f) != "README.md"]

    labels = load_classification()

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        rel = path.replace(os.sep, "/")
        source = "channel" if "/channels/" in rel else "keyword"
        rows.append({
            "file": rel,
            "title": meta["title"],
            "channel": meta["channel"] or "(미상)",
            "source": source,
            "lang": meta["lang"],
            "upload_date": meta["upload_date"],
            "month": doc_month(path, meta),
            "url": meta["url"],
            "label": labels.get(rel, "unclassified"),
            "summary": summarize_text(text),
        })
    return rows


def write_csv(rows):
    os.makedirs("analysis", exist_ok=True)
    fieldnames = [
        "file", "title", "channel", "source", "lang",
        "upload_date", "month", "label", "url", "summary",
    ]
    with open(os.path.join("analysis", "summaries.csv"), "w",
              encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_by_channel(rows):
    """채널(또는 키워드 검색분)별로 묶어 최신순으로 정렬한 목록."""
    groups = defaultdict(list)
    for r in rows:
        groups[r["channel"]].append(r)

    path = os.path.join("analysis", "SUMMARY_BY_CHANNEL.md")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("# 채널/출처별 수집 요약\n\n")
        fp.write(f"총 {len(rows)}건 · {len(groups)}개 채널/출처\n\n")
        for channel in sorted(groups, key=lambda c: -len(groups[c])):
            items = sorted(groups[channel], key=lambda r: r["upload_date"] or r["month"], reverse=True)
            fp.write(f"## {channel} ({len(items)}건)\n\n")
            for r in items:
                date = r["upload_date"] or r["month"]
                fp.write(f"- **[{r['title']}]({r['url']})** — {date} · {r['lang']} · `{r['label']}`\n")
                fp.write(f"  {r['summary']}\n\n")


def write_by_month(rows):
    """월 × 분류라벨로 묶은 목록 — K1 자료와 병합할 시계열 담론 지수의 사람용 버전."""
    groups = defaultdict(lambda: defaultdict(list))
    for r in rows:
        groups[r["month"]][r["label"]].append(r)

    path = os.path.join("analysis", "SUMMARY_BY_MONTH.md")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("# 월 × 분류(DX/AX/AT)별 수집 요약\n\n")
        for month in sorted(groups, reverse=True):
            month_total = sum(len(v) for v in groups[month].values())
            fp.write(f"## {month} (총 {month_total}건)\n\n")
            for label in ["AX", "DX", "AT", "unclassified"]:
                items = groups[month].get(label, [])
                if not items:
                    continue
                fp.write(f"### {label} ({len(items)}건)\n\n")
                for r in items:
                    fp.write(f"- **[{r['title']}]({r['url']})** · {r['channel']} ({r['source']})\n")
                    fp.write(f"  {r['summary']}\n\n")


def main():
    rows = collect_rows()
    if not rows:
        print("[summarize] 수집된 영상이 없습니다.")
        return
    write_csv(rows)
    write_by_channel(rows)
    write_by_month(rows)
    print(f"[summarize] {len(rows)}건 요약 정리 완료 → analysis/summaries.csv, "
          f"SUMMARY_BY_CHANNEL.md, SUMMARY_BY_MONTH.md")


if __name__ == "__main__":
    main()
