"""
사전 패턴의 '부분 문자열 오탐' 감사기 — 관성/일관성 사건의 재발 방지 장치.

배경: `map_vial.py` 의 B6(장벽) 패턴 `관성` 이 **일관성**(consistency)의 부분 문자열에
걸려, 장벽을 전혀 말하지 않는 IR 발표까지 B6 가 성립했다(코퍼스 B6 370→170건으로 교정).
한국어는 교착어라 '개선→개선할/개선하는' 같은 결합은 정상 매칭이지만,
**앞에 다른 글자가 붙어 낱말 자체가 달라지는 경우**(일관성·도대체·비장애인)는 오탐이다.

이 스크립트는 사전에서 '패턴 전체가 맨 한글 낱말'인 것만 골라,
코퍼스 표본에서 그 낱말을 부분 문자열로 포함하는 **다른 낱말**을 찾아 보고한다.
정규식 그룹 안쪽의 대안(예: `보안\\s*(위협|우려)` 의 '우려')은 앞말이 고정돼 있으므로 제외한다.

직접 실행: python audit_patterns.py [표본수]
"""

import collections
import glob
import random
import re
import sys

import map_vial as mv

SAMPLE_DEFAULT = 500
MIN_FREQ = 3


def top_level_branches(pattern):
    """정규식의 최상위 `|` 만 기준으로 대안을 쪼갠다(괄호 안쪽은 건드리지 않는다)."""
    depth, cur, out, i = 0, "", [], 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\":
            cur += pattern[i:i + 2]
            i += 2
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "|" and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
        i += 1
    out.append(cur)
    return [b.strip() for b in out if b.strip()]


def main():
    n_sample = int(sys.argv[1]) if len(sys.argv) > 1 else SAMPLE_DEFAULT

    bare = {}
    for _key, blk, label, pats in mv.CONSTRUCTS + mv.BRIDGES:
        for p in pats:
            for br in top_level_branches(p.pattern):
                if re.fullmatch(r"[가-힣]{2,4}", br):
                    bare.setdefault(br, set()).add(f"{blk} {label}")

    files = [f for f in sorted(glob.glob("transcripts/**/*.md", recursive=True))
             if not f.endswith("README.md")]
    random.seed(0)                      # 재현 가능한 표본
    sample = random.sample(files, min(n_sample, len(files)))
    freq = collections.Counter()
    for path in sample:
        with open(path, encoding="utf-8") as fp:
            freq.update(re.findall(r"[가-힣]{2,10}", fp.read()))

    print(f"[audit_patterns] 맨 한글 낱말 패턴 {len(bare)}개 · 표본 {len(sample)}건")
    flagged = 0
    for tok, blocks in sorted(bare.items()):
        # 앞에 글자가 붙어 낱말이 달라지는 경우만 위험으로 본다(뒤에 붙는 것은 조사·어미).
        risky = sorted([(w, n) for w, n in freq.items()
                        if tok in w and not w.startswith(tok) and n >= MIN_FREQ],
                       key=lambda x: -x[1])[:8]
        if risky:
            flagged += 1
            print(f"  ⚠️ [{tok}] ({', '.join(sorted(blocks))})")
            print(f"      앞말 결합: " + ", ".join(f"{w}({n})" for w, n in risky))
    if not flagged:
        print("  ⚠️ 없음 — 부분 문자열 오탐 위험 패턴 미검출")
    print("\n  판단은 사람이 한다: '개선→개선할' 같은 어미 결합은 정상이고,")
    print("  '관성→일관성', '대체→도대체'처럼 낱말이 달라지는 것만 부정 전방탐색으로 막는다.")


if __name__ == "__main__":
    main()
