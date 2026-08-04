"""
사례 본문(prose)에 실린 인용문이 실제 스크립트 원문에 있는지 기계 검증한다.

사례 본문은 사람이 읽는 서술이지만 근거는 자막 원문 발췌여야 한다.
LLM이 문장을 다듬거나 지어내면 인용의 지위를 잃으므로, 인용문 전량을
원문 대조해 **일치/불일치**를 표로 남긴다(코딩 감사 기록).

입력: analysis/vial_prose.json   (사례별 headline·prose·quotes·verdict)
출력: analysis/vial_prose_quotecheck.csv  (인용문 1행 = 1건, ok/공백정규화후ok/불일치)
      표준출력에 요약

직접 실행: python verify_prose_quotes.py
"""

import csv
import json
import os
import re
import sys
import unicodedata


def norm(s):
    """공백·유니코드 정규화 — 자막의 &nbsp;·중복 공백·전각 문자 차이를 흡수한다."""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace(" ", " ").replace("&nbsp;", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main():
    src = "analysis/vial_prose.json"
    if not os.path.exists(src):
        sys.exit(f"{src} 없음 — 본문 생성 결과를 먼저 저장할 것.")
    cases = json.load(open(src, encoding="utf-8"))

    bodies = {}
    rows = []
    for c in cases:
        path = c["file"]
        if path not in bodies:
            with open(path, encoding="utf-8") as fp:
                bodies[path] = norm(fp.read())
        body = bodies[path]
        for q in c.get("quotes", []):
            nq = norm(q)
            if not nq:
                continue
            if nq in body:
                status = "ok"
            elif norm(q.replace("…", "")) and norm(q.replace("…", "")) in body:
                status = "ok_ellipsis"
            else:
                # 앞뒤 잘림 허용: 12자 이상 연속 일치 구간이 있으면 부분 일치로 본다
                status = "mismatch"
                for i in range(0, max(len(nq) - 12, 0) + 1):
                    if nq[i:i + 12] in body:
                        status = "partial"
                        break
            rows.append({
                "n": c["n"], "tier": c.get("tier", ""), "channel": c.get("channel", ""),
                "title": c.get("title", ""), "status": status, "quote": q, "file": path,
            })

    os.makedirs("analysis", exist_ok=True)
    with open("analysis/vial_prose_quotecheck.csv", "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["n", "tier", "channel", "title", "status", "quote", "file"])
        w.writeheader()
        w.writerows(rows)

    import collections
    cnt = collections.Counter(r["status"] for r in rows)
    print(f"[verify_prose_quotes] 인용문 {len(rows)}건 검증 → analysis/vial_prose_quotecheck.csv")
    for k in ("ok", "ok_ellipsis", "partial", "mismatch"):
        if cnt.get(k):
            print(f"  {k}: {cnt[k]}건 ({100*cnt[k]/max(len(rows),1):.1f}%)")
    bad = [r for r in rows if r["status"] in ("mismatch", "partial")]
    if bad:
        print("\n  원문 대조 실패/부분일치 목록:")
        for r in bad:
            print(f"    [{r['status']}] #{r['n']} {r['channel'][:18]} | {r['quote'][:70]}")
    return 0 if not [r for r in rows if r["status"] == "mismatch"] else 1


if __name__ == "__main__":
    sys.exit(main())
