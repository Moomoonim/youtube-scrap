"""
사례 본문(prose)을 사람이 읽는 문서로 조립한다.

입력: analysis/vial_prose.json  (사례별 headline·prose·quotes·verdict + 메타)
출력: docs/VIAL_CASES_PROSE.md  (티어 A → B 순, 사례별 본문 서술)
      analysis/vial_prose.csv   (기계 판독본)

직접 실행: python build_prose_doc.py
"""

import csv
import json
import os
import sys

VERDICT_MARK = {"adopt": "✅ 채택", "conditional": "⚠️ 조건부", "exclude": "❌ 제외 권고"}


def main():
    src = "analysis/vial_prose.json"
    if not os.path.exists(src):
        sys.exit(f"{src} 없음.")
    cases = json.load(open(src, encoding="utf-8"))
    cases.sort(key=lambda c: (c["tier"], -int(c["blocks"]), c["channel"]))

    out = []
    out.append("# Vial(2019) 프레임워크 사례 본문 — 티어 A·B 전건 서술\n")
    out.append("> 각 사례의 스크립트 원문을 읽고 쓴 **본문 서술**이다. "
               "표·불릿로 정리한 `docs/VIAL_CASES_A_B.md`(자동 발췌)와 달리, "
               "여기서는 사례 하나를 네 문단(자료의 성격 → 사례 내용 → Vial 블록 대응 → 연구 활용과 한계)으로 서술한다.\n")
    out.append(f"> 총 **{len(cases)}건** (티어 A {sum(1 for c in cases if c['tier']=='A')} · "
               f"B {sum(1 for c in cases if c['tier']=='B')}). "
               "근거 문헌: Vial, G. (2019). *JSIS, 28*(2), 118–144.\n")
    out.append("> 「」 안의 인용은 자막 원문 발췌이며, 전량을 `verify_prose_quotes.py` 로 원문 대조했다"
               "(결과: `analysis/vial_prose_quotecheck.csv`). 자동 자막·자동 번역이라 오탈자·오역이 그대로 있다.\n")

    cur = None
    for i, c in enumerate(cases, 1):
        if c["tier"] != cur:
            cur = c["tier"]
            title = ("티어 A — 기술→파괴/전략→가치·구조→성과 사슬이 온전한 사례"
                     if cur == "A" else "티어 B — 사슬 대부분(6블록)을 충족한 사례")
            out.append(f"\n---\n\n## 티어 {cur}: {title}\n")
        out.append(f"\n### {i}. {c['title']}\n")
        out.append(f"**{c['headline']}**\n")
        out.append(f"{c['channel']} · {c['month']} · {c['lang']} · {int(c['words']):,}단어 · "
                   f"`{c['relevance']}`/`{c['stance']}` · {c['blocks']}/8블록({c['block_list']}) · "
                   f"{VERDICT_MARK.get(c.get('verdict',''), c.get('verdict',''))}\n")
        out.append(f"{c['prose']}\n")
        out.append(f"*판정 근거: {c.get('verdict_reason','')}* · "
                   f"[영상]({c['url']}) · 원문 `{c['file']}`\n")

    os.makedirs("docs", exist_ok=True)
    open("docs/VIAL_CASES_PROSE.md", "w", encoding="utf-8").write("\n".join(out) + "\n")

    fields = ["n", "tier", "blocks", "block_list", "channel", "title", "month", "lang", "words",
              "relevance", "stance", "verdict", "verdict_reason", "headline", "prose",
              "quotes", "url", "file"]
    with open("analysis/vial_prose.csv", "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for c in cases:
            row = dict(c)
            row["quotes"] = " || ".join(c.get("quotes", []))
            w.writerow(row)

    print(f"[build_prose_doc] {len(cases)}건 → docs/VIAL_CASES_PROSE.md · analysis/vial_prose.csv")


if __name__ == "__main__":
    main()
