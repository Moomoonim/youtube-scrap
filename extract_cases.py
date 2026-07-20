"""
스크립트에서 'AX 사례 주장'을 추출해 회사별·날짜별 테이블로 정리한다.

목표: HBR 사례집 형식처럼 — 회사(채널) | 날짜 | 분류 | 무엇을 했다고 말하는지
(스크립트 발췌 = 근거) | 성과 수치 | 원본 링크 — 를 자동 생성.

추출 방식(1차, 규칙 기반):
- 문장 단위로 나눈 뒤, '행동 동사'(도입/구축/적용/deployed/launched...)와
  '성과 수치'(%·배·시간 단축 등)가 포함된 문장을 근거 후보로 선별
- 수치+행동이 함께 있는 문장을 우선 순위로, 영상당 최대 3문장 발췌
- LLM 없이 무료·대량 처리 가능. 정밀 추출(문맥 요해)은 추후 LLM 단계로
  업그레이드 가능 (extract_claims() 교체)

입력: transcripts/**.md (+ analysis/classified.csv 라벨)
출력:
    analysis/cases.csv               — 기계 판독용
    analysis/CASES_BY_COMPANY.md     — 회사별·날짜별 사례 테이블 (사람용)

직접 실행: python extract_cases.py
"""

import csv
import glob
import os
import re
from collections import defaultdict

import config
from classify import doc_month, parse_transcript
from summarize import load_classification

# ── 행동(무엇을 했다) 신호 ──────────────────────────────
ACTION_PATTERNS = [
    # 한국어
    r"도입", r"구축", r"적용", r"전환", r"출시", r"개발", r"자동화",
    r"절감", r"단축", r"향상", r"개선", r"증가", r"감소", r"확대",
    r"활용", r"통합", r"대체", r"학습시", r"배포",
    # 영어
    r"\bdeploy(?:ed|ing|s)?\b", r"\blaunch(?:ed|ing|es)?\b",
    r"\bbuilt\b", r"\bbuild(?:ing|s)?\b", r"\badopt(?:ed|ing|s|ion)?\b",
    r"\bimplement(?:ed|ing|s|ation)?\b", r"\bautomat(?:ed|ing|ion)\b",
    r"\breduc(?:ed|ing|es|tion)\b", r"\bimprov(?:ed|ing|es|ement)\b",
    r"\bincreas(?:ed|ing|es)\b", r"\bcut\b", r"\bsav(?:ed|ing|es)\b",
    r"\bintegrat(?:ed|ing|es|ion)\b", r"\btransform(?:ed|ing|s|ation)?\b",
    r"\brolled?\s+out\b", r"\bscal(?:ed|ing)\b",
]
ACTION_RE = re.compile("|".join(ACTION_PATTERNS), re.IGNORECASE)

# ── 성과 수치 신호 ──────────────────────────────────────
METRIC_PATTERNS = [
    r"\d+(?:\.\d+)?\s*%", r"\d+(?:\.\d+)?\s*퍼센트",
    r"\d+(?:\.\d+)?\s*배", r"\d+x\b", r"\d+\s*times\b",
    r"\d+\s*(?:시간|분|일|주|개월|년)\s*(?:단축|절감|절약)?",
    r"\d+\s*(?:hours?|minutes?|days?|weeks?|months?)\b",
    r"(?:수|몇)\s*(?:십|백|천|만|억)\s*(?:명|건|개|달러|원)",
    r"\$\s*\d+", r"\d+\s*(?:억|조|만)\s*(?:원|달러)?",
    r"\d+(?:,\d{3})+",
]
METRIC_RE = re.compile("|".join(METRIC_PATTERNS), re.IGNORECASE)

# AI 관련 문맥 (사례 문장에 AI 언급이 있으면 가산점)
AI_RE = re.compile(r"\bAI\b|인공지능|생성형|LLM|GPT|머신\s*러닝|딥\s*러닝|에이전트|agent|copilot|챗봇|chatbot|알고리즘|algorithm", re.IGNORECASE)

# 홍보·자기소개성 잡음 문장 제외
NOISE_RE = re.compile(r"베스트셀러|책을|발간|출간|저자|구독|좋아요|시청|채널|영상\s*끝까지|강연|강의를|인사드리")

MAX_CLAIMS_PER_VIDEO = 3
MIN_SENT_LEN = 20      # 너무 짧은 조각 제외
MAX_SENT_LEN = 400     # 자동자막 이어붙음 방지

# ── 언급 기업 감지 (벤더→고객 사례 포착용) ──────────────
# "NVIDIA가 Eli Lilly에 AI Factory를 구축해줬다"처럼, 영상 채널이 아닌
# 다른 회사가 문장에 등장하면 '협력/고객 사례'로 표시하고 그 회사를 기록한다.
MENTION_COMPANIES = [
    # 글로벌 테크·AI
    "NVIDIA", "OpenAI", "Anthropic", "Google", "DeepMind", "Microsoft",
    "Meta", "Apple", "Amazon", "AWS", "IBM", "Oracle", "Salesforce", "SAP",
    "Adobe", "Netflix", "LinkedIn", "GitHub", "Slack", "Zapier", "Intercom",
    "ServiceNow", "Databricks", "Snowflake", "Hugging Face", "Perplexity",
    "Intel", "AMD", "TSMC", "Qualcomm", "Broadcom", "Cursor", "Replit",
    # 소비재·리테일·제조
    "L'Oréal", "로레알", "IKEA", "이케아", "Nike", "나이키", "Unilever",
    "유니레버", "Reckitt", "레킷", "Walmart", "월마트", "Coca-Cola",
    "Caterpillar", "캐터필러", "Siemens", "지멘스", "Boeing", "Foxconn",
    "BMW", "Mercedes", "벤츠", "Tesla", "테슬라", "Toyota", "도요타",
    "Volvo", "볼보", "GM", "Ford", "BYD", "Waymo", "Cruise", "Nissan",
    # 금융·컨설팅
    "JPMorgan", "JP모건", "Goldman", "골드만", "McKinsey", "맥킨지",
    "BCG", "Deloitte", "딜로이트", "Accenture", "액센츄어", "액센추어",
    "PwC", "KPMG", "Genpact", "Intuit", "IQVIA", "Capgemini",
    # 헬스케어·제약
    "Eli Lilly", "일라이 릴리", "Novo Nordisk", "노보 노디스크",
    "Johnson & Johnson", "존슨앤존슨", "Pfizer", "화이자", "Philips",
    "필립스", "GE HealthCare", "Mayo Clinic", "메이요", "Abridge",
    "Verily", "Epic", "Moderna", "Roche", "Novartis",
    # 통신
    "T-Mobile", "Nokia", "노키아", "Ericsson", "에릭슨", "Orange",
    "Telefónica", "Swisscom", "Telenor", "SoftBank", "소프트뱅크",
    "Vodafone", "TCS", "Infosys", "Verizon", "AT&T",
    # 한국
    "삼성", "Samsung", "LG", "SK", "현대", "Hyundai", "네이버", "NAVER",
    "카카오", "Kakao", "KT", "롯데", "포스코", "POSCO", "한화", "두산",
    "CJ", "신한", "국민은행", "KB", "우리은행", "하나은행", "업스테이지",
    "Upstage", "쿠팡", "Coupang", "배민", "토스", "Toss",
    # 중국·기타
    "Alibaba", "알리바바", "Tencent", "텐센트", "Baidu", "바이두",
    "Huawei", "화웨이", "DeepSeek", "딥시크", "Palantir", "팔란티어",
    "Anduril", "Boston Dynamics", "Figure",
    # 한글 표기·띄어쓰기 변형
    "엔비디아", "마이크로소프트", "구글", "아마존", "애플", "오픈AI",
    "오픈에이아이", "앤트로픽", "세일즈포스", "어도비", "넷플릭스",
    "깃허브", "JP 모건", "골드만 삭스", "모건 스탠리", "스타벅스",
    "Starbucks", "Target", "지멘스", "보잉", "인텔", "퀄컴",
]
# 정규식 컴파일: 순수 영문 이름만 단어 경계 사용.
# 한글이 섞인 이름은 조사(에/은/이 등)가 붙으므로 부분 일치로 처리.
_mention_res = []
for name in MENTION_COMPANIES:
    if re.fullmatch(r"[A-Za-z0-9&'\-\. ]+", name):
        _mention_res.append((name, re.compile(r"\b" + re.escape(name) + r"\b")))
    else:
        _mention_res.append((name, re.compile(re.escape(name))))


def _same_company(channel, name):
    """채널명과 언급 기업명이 같은 회사인지 대략 판정."""
    c, n = channel.lower(), name.lower()
    return n in c or c in n


def find_mentions(sentence, channel):
    """문장에서 채널(화자) 이외의 회사 언급을 찾는다."""
    found = []
    for name, rx in _mention_res:
        if rx.search(sentence) and not _same_company(channel, name):
            if name not in found:
                found.append(name)
    return found[:5]


def split_sentences(text):
    """한/영 혼용 텍스트를 문장 단위로 대략 나눈다."""
    # 한국어 종결(다./요./까?/죠.) + 영문 종결(. ! ?) 기준
    parts = re.split(r"(?<=[.!?])\s+|(?<=다\.)\s*|(?<=요\.)\s*|(?<=죠\.)\s*", text)
    return [p.strip() for p in parts if p and len(p.strip()) >= MIN_SENT_LEN]


def extract_claims(text):
    """행동+수치 신호 기반으로 '사례 주장' 문장을 점수순으로 추출한다."""
    scored = []
    for sent in split_sentences(text):
        if len(sent) > MAX_SENT_LEN:
            sent = sent[:MAX_SENT_LEN] + "…"
        if NOISE_RE.search(sent):
            continue
        has_action = bool(ACTION_RE.search(sent))
        if not has_action:
            continue
        has_metric = bool(METRIC_RE.search(sent))
        has_ai = bool(AI_RE.search(sent))
        if not (has_metric or has_ai):
            continue  # 행동만으로는 부족 — 수치나 AI 문맥 필요
        score = 1 + (2 if has_metric else 0) + (1 if has_ai else 0)
        scored.append((score, has_metric, sent))
    scored.sort(key=lambda x: -x[0])
    return scored[:MAX_CLAIMS_PER_VIDEO]


def collect_cases():
    files = sorted(
        glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True)
    )
    files = [f for f in files if os.path.basename(f) != "README.md"]
    labels = load_classification()

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        rel = path.replace(os.sep, "/")
        claims = extract_claims(text)
        if not claims:
            continue
        source = "channel" if "/channels/" in rel else "keyword"
        date = meta.get("upload_date") or doc_month(path, meta)
        channel = meta["channel"] or "(미상)"
        for rank, (score, has_metric, sent) in enumerate(claims, 1):
            mentions = find_mentions(sent, channel)
            rows.append({
                "company": channel,
                "date": date,
                "source": source,
                "label": labels.get(rel, "unclassified"),
                "case_type": "협력/고객사 언급" if mentions else "자사/일반",
                "mentions": "; ".join(mentions),
                "title": meta["title"],
                "claim": sent,                      # 무엇을 했다고 말하는지 (발췌)
                "has_metric": "Y" if has_metric else "N",
                "score": score,
                "rank": rank,
                "url": meta["url"],
                "file": rel,                        # reference (script 파일)
            })
    return rows


def write_csv(rows):
    os.makedirs("analysis", exist_ok=True)
    fields = ["company", "date", "source", "label", "case_type", "mentions",
              "title", "claim", "has_metric", "score", "rank", "url", "file"]
    with open(os.path.join("analysis", "cases.csv"), "w",
              encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def write_md(rows):
    """회사별 → 날짜순 사례 테이블 (HBR 사례집 형식)."""
    groups = defaultdict(list)
    for r in rows:
        groups[r["company"]].append(r)

    path = os.path.join("analysis", "CASES_BY_COMPANY.md")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("# 회사별 AX 사례 추출 테이블\n\n")
        fp.write("영상 스크립트에서 '무엇을 했다/성과가 났다'고 말하는 문장을 "
                 "발췌한 것으로, 각 행의 근거는 원문 스크립트 파일(reference)과 "
                 "영상 링크로 확인할 수 있다.\n\n")
        fp.write("> ⚠️ 1차 규칙 기반 발췌 — 발언 주체·맥락 검증 전이므로 "
                 "인용 시 원문 확인 필수. (정밀 추출은 LLM 2차 단계에서)\n\n")
        for company in sorted(groups, key=lambda c: -len(groups[c])):
            items = sorted(groups[company], key=lambda r: (r["date"], r["rank"]))
            fp.write(f"## {company} ({len(items)}건)\n\n")
            fp.write("| 날짜 | 분류 | 유형 | 언급 기업 | 사례 주장 (스크립트 발췌) | 수치 | 근거 |\n")
            fp.write("|---|---|---|---|---|---|---|\n")
            for r in items:
                claim = r["claim"].replace("|", "／")
                fp.write(
                    f"| {r['date']} | {r['label']} | {r['case_type']} "
                    f"| {r['mentions'] or '-'} | {claim} | {r['has_metric']} "
                    f"| [영상]({r['url']}) · [script]({'../' + r['file']}) |\n"
                )
            fp.write("\n")


def main():
    rows = collect_cases()
    if not rows:
        print("[cases] 추출된 사례가 없습니다.")
        return
    write_csv(rows)
    write_md(rows)
    companies = len(set(r["company"] for r in rows))
    with_metric = sum(1 for r in rows if r["has_metric"] == "Y")
    partner = sum(1 for r in rows if r["case_type"] == "협력/고객사 언급")
    print(f"[cases] {companies}개 회사/채널에서 사례 문장 {len(rows)}건 추출 "
          f"(수치 포함 {with_metric}건, 협력/고객사 언급 {partner}건) "
          f"→ analysis/cases.csv, CASES_BY_COMPANY.md")


if __name__ == "__main__":
    main()
