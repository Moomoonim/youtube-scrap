"""
AI readiness framework(Holmström 2022) 적용 가능 케이스 스캐너.

Holmström, J. (2022). From AI to digital transformation: The AI readiness framework.
Business Horizons, 65(3), 329-339. https://doi.org/10.1016/j.bushor.2021.03.006

원 프레임워크는 4차원(technologies · activities · boundaries · goals) × 2시점
(current · future) = 8셀 스코어카드를 조직 구성원이 0~4점으로 self-report 하는
워크숍 도구다(논문의 보험사 사례: 기술 4/2 · 활동 2/3 · 경계 1/2 · 목표 0/1).
이 스캐너는 그 8셀을 **코딩 규칙**으로 옮겨, 코퍼스에서 "8셀을 채울 근거가 실제로
있는 케이스"를 찾는다.

  - 자기보고를 흉내내지 않는다. 우리가 가진 것은 공개 발화이므로 외부 코더가
    2차 자료로 프레임워크를 채우는(secondary application) 용도다. 산출 점수는
    `prov_*`(provisional) = **근거 밀도 대리지표**이며 self-report 점수가 아니다.
  - 프레임워크의 평가 단위는 **AI를 도입하는 조직**이다. 따라서 벤더의 제품
    키노트(공급측 발화)는 케이스로 쓰지 않고 분리해 집계한다. 이 판정이
    `case_role` 이다(§ 아래 4번).

판정 로직
  1) relevance == ax_core (classify_v2 재사용) 만 후보 모집단.
  2) 문장 단위로 4차원 마커를 매칭하고, 같은 문장의 시제 마커로 current/future 배정.
     (시제 마커가 없으면 unspec 으로 따로 집계 — 셀 충족에는 쓰지 않는다)
  3) 4차원을 모두 커버한 건만 케이스 후보. 채워진 셀 수로 티어: A=8 · B=6~7 · C=4~5.
  4) case_role — 프레임워크 적용 가능성의 핵심 축:
       adopter_self          : 도입 조직이 자기 전환을 말함 (1급 케이스)
       vendor_customer_story : 벤더가 특정 고객사 사례를 말함 → 초점=그 고객사 (2급)
       vendor_selfpromo      : 벤더 제품·플랫폼 발화 (프레임워크 부적합 — 분리 집계)
       expert_commentary     : 초점 조직 없는 컨설턴트·미디어 일반론 (부적합)
  5) 회사별로 근거를 합산(pooled)한 통합 스코어카드도 만든다 — 사례 단위는 기업이고,
     한 기업의 여러 영상을 합치면 8셀이 채워지는 경우가 많다.

출력
  analysis/ai_readiness_cases.csv    — 영상별 8셀 근거 수 · 티어 · 역할 · 발췌 (기계판독)
  analysis/ai_readiness_firms.csv    — 기업별 합산 스코어카드(수요측 근거만)
  docs/AI_READINESS_CASES.md         — 사람이 읽는 케이스 목록(발췌 근거 포함)

직접 실행: python readiness_scan.py
"""

import collections
import csv
import glob
import os
import re

import config
from classify import doc_month, parse_transcript, score_text
from classify_v2 import classify_relevance, classify_stance
from extract_cases import split_sentences


def rx(*p):
    return [re.compile(x, re.I) for x in p]


# ─────────────────────────────────────────────────────────────────
# 1. 프레임워크 4차원 사전
#    원문 4차원 정의를 코퍼스 어휘(한/영 혼용, 자동자막)로 옮긴 것.
# ─────────────────────────────────────────────────────────────────

DIMENSIONS = {
    # (a) technologies — 보유·도입한 AI 기술 포트폴리오
    "tech": rx(
        r"\bLLM\b|거대\s*언어\s*모델|large\s+language\s+model",
        r"\bGPT\b|ChatGPT|Claude|Gemini|Llama|Qwen|EXAONE|HyperCLOVA|Solar\b",
        r"생성형\s*AI|generative\s+AI|\bGenAI\b|파운데이션\s*모델|foundation\s+model",
        r"(AI\s*)?에이전트|\bagent(ic|s)?\b|코파일럿|copilot|챗봇|chatbot",
        r"\bRAG\b|검색\s*증강|벡터\s*(DB|검색)|vector\s+(db|database|search)|임베딩|embedding",
        r"머신\s*러닝|machine\s+learning|딥\s*러닝|deep\s+learning|파인\s*튜닝|fine[-\s]?tun",
        r"플랫폼(을|에|으로)?\s*(구축|도입|개발)|인프라|infrastructure",
        r"\bGPU\b|\bNPU\b|데이터\s*(센터|레이크|플랫폼)|data\s+(center|lake|platform)",
        r"사내\s*(GPT|AI|챗봇)|자체\s*(모델|LLM|AI)|온프레미스|on[-\s]?prem|프라이빗\s*클라우드",
        r"\bAPI\b|\bMCP\b|\bSaaS\b|시스템(을|에)?\s*(구축|연동|도입)|솔루션(을|를)?\s*(도입|구축)",
    ),
    # (b) activities — AI가 지원하는 핵심 활동·업무·프로세스
    "act": rx(
        r"업무(를|의|에|가)?\s*(자동화|재설계|프로세스|방식|효율)|업무\s*(프로세스|흐름)",
        r"워크플로|workflow|프로세스(를|의|가)?\s*(개선|재설계|자동화)|process\s+(redesign|automation)",
        r"현업|실무|일하는\s*방식|way\s+of\s+work|day[-\s]?to[-\s]?day",
        r"(고객|상담|콜)\s*(서비스|센터|응대)|customer\s+(service|support)|contact\s+center|상담(원|사)",
        r"제조|생산\s*(라인|공정)|공정|manufactur|품질\s*검사|수율|불량|설비\s*(예지|보전)",
        r"영업|마케팅|sales|marketing|물류|공급망|supply\s+chain|재고|조달|purchas",
        r"연구\s*개발|\bR&D\b|신약|설계|design\s+review|코드\s*(리뷰|생성)|개발\s*생산성",
        r"인사|\bHR\b|채용|recruit|교육\s*(과정|프로그램)|onboarding|평가\s*(제도|프로세스)",
        r"재무|회계|정산|결산|법무|계약서|심사|여신|보험\s*(심사|청구)|claims?\b",
        r"문서(를|의)?\s*(작성|처리|요약)|보고서(를|의)?\s*(작성|자동)|리포트\s*작성|document\s+processing",
        r"업무에\s*(적용|활용|도입)|일상\s*업무|task(s)?\b|직원(들)?(이|은|의)\s*(사용|활용)",
    ),
    # (c) boundaries — 조직 경계의 변화(외부 협력·생태계·내부 조직 재편)
    "bnd": rx(
        r"파트너(십|사)?|partner(ship)?|협력(사|업체|관계)|제휴|alliance|얼라이언스",
        r"생태계|ecosystem|컨소시엄|consortium|공동\s*(개발|연구|투자|사업)|joint\s+(venture|development)",
        r"합작|\bJV\b|인수|\bM&A\b|acquisition|acquire|지분\s*투자|출자|자회사|계열사|법인\s*설립",
        r"아웃소싱|outsourc|인소싱|insourc|내부화|위탁|외주|벤더|vendor|공급업체|supplier",
        # 한국어 구어는 어절이 끼어들므로("외부 전문 기관", "서울대 전문가들과 협업")
        # 인접 매칭 대신 2~3어절 간격을 허용한다
        r"(외부|사외|타사)(의)?\s*(?:\S+\s+){0,2}(기관|전문가|파트너|업체|인력|자원|조직)",
        r"(대학교?|교수|연구진|연구소|카이스트|서울대|포스텍)(?:\S*\s+){0,3}"
        r"(협업|협력|공동|자문|참여|함께)",
        r"산학|academia|(협력|공동)\s*(개발|연구|운영|프로젝트|과제)|외부와(의)?\s*협력",
        r"(외주|용역|위탁)\s*(개발|운영|계약)",
        r"고객사(와|와의)?\s*(공동|협업)|co[-\s]?(develop|creat|innovat)|공동\s*창출",
        r"플랫폼(을|를)?\s*(개방|공개)|\bAPI\b(을|를)?\s*(개방|공개)|오픈\s*소스|open[-\s]?source(d|ing)?",
        r"(전담|전문)\s*조직(을|이)?\s*(신설|구성|만들)|\bCoE\b|center\s+of\s+excellence",
        r"(AX|AI)\s*(센터|본부|조직|추진단|TF|태스크\s*포스)|transformation\s+office|조직\s*(개편|재편)",
        r"채널\s*파트너|리셀러|reseller|시스템\s*통합|하청|협력\s*업체",
        r"사업\s*(영역|범위)(을|를)?\s*(확장|확대)|신사업|new\s+business\s+(line|model)|영역\s*확장",
    ),
    # (d) goals — 조직 목표·전략·의도
    "goal": rx(
        r"목표(는|가|를|로|입니다)|목표\s*로\s*(한|하고)|goal(s)?\b|objective",
        r"전략(은|이|을|적)|strategy|strategic|비전|vision|미션|mission|지향",
        r"로드맵|roadmap|중장기|장기\s*계획|3개년|\d{4}년\s*까지|by\s+20\d\d",
        r"\bKPI\b|\bOKR\b|성과\s*지표|목표\s*(치|수치)|target(s)?\b|ambition",
        r"경영\s*(목표|방침|전략)|사업\s*(구조|모델)(을|를)?\s*(전환|재편)|business\s+model",
        r"우선\s*순위|prioriti[sz]|어디에\s*집중|집중(하기로|할)|focus\s+on",
        r"성장(을|의)?\s*(목표|동력)|매출\s*목표|수익성|profitab|시장\s*(점유율|1위|리더)",
        r"경쟁력(을|이)|competitive\s+(advantage|edge)|차별화|differentiat",
        r"전사(적)?\s*(목표|전략|방향)|company[-\s]?wide|경영진(이|의)\s*(방향|의지)|CEO(가|의)\s*(메시지|의지)",
    ),
}

# ─── 시제(현재/미래) 마커 ────────────────────────────────────────
FUTURE = rx(
    r"앞으로|향후|장차|이제부터",
    r"계획(이|입니다|하고|중)|예정(이|입니다)|추진(할|하겠|예정)|준비\s*(중|하고)",
    r"로드맵|중장기|내년|다음\s*(해|단계|분기)|올해\s*말|\d{4}년\s*까지|by\s+20\d\d",
    r"할\s*(것|계획|예정|생각)|하겠(다|습니다)|되어야|해야\s*(한다|합니다|된다)|나가야",
    r"목표(는|로)\s*(하|삼)|지향(한|하)|만들어\s*(갈|나갈)|바꿔\s*(갈|나갈)",
    r"\bwill\b|\bplan(s|ning)?\s+to\b|\bgoing\s+to\b|\bintend|\baim(s|ing)?\s+to\b",
    r"\bnext\s+(year|phase|step)|\bfuture\b|\broadmap\b|\bwe\s+want\s+to\b|\bshould\b",
)
CURRENT = rx(
    r"현재|지금|이미|올해|작년|지난해|최근(에|에는)?",
    r"(도입|구축|적용|배포|출시|시작|운영)(했|하였|해\s*왔|중이|하고\s*있)",
    r"쓰고\s*있|사용하고\s*있|활용하고\s*있|운영\s*중|시행\s*중|진행\s*중",
    r"성과(가|를)\s*(나|났|냈|있)|효과(가|를)\s*(봤|있|났)|절감(했|됐|되었)",
    r"\bcurrently\b|\btoday\b|\balready\b|\bwe\s+have\b|\bwe'?ve\b",
    r"\b(deployed|rolled\s+out|launched|built|implemented|adopted)\b|\bin\s+production\b",
)

# ─── 'value-adding' 마커 — 원 설문의 공통 프레이즈(가치 기여 여부) ──
VALUE = rx(
    r"가치|value[-\s]?(add|creat)|성과|효과|임팩트|impact|기여",
    r"비용\s*(절감|감소)|절감|savings?|\bROI\b|수익|매출|revenue|이익|마진|margin",
    r"생산성|productivity|효율(성|화)?|efficien|시간(을)?\s*(단축|절약)|단축",
    r"품질(이|을)\s*(개선|향상)|정확도(가|를)\s*(개선|향상|올)|만족도|\bNPS\b|전환율",
)
METRIC = re.compile(
    r"\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*퍼센트|\d+(?:\.\d+)?\s*배|\d+x\b|"
    r"\d+\s*(?:시간|분|일|주|개월|년)|\$\s*\d+|\d+\s*(?:억|조|만)\s*(?:원|달러)?|\d+(?:,\d{3})+",
    re.I,
)

# ─── AI 연결성 게이트 ───────────────────────────────────────────
# 원 설문의 모든 문항은 "AI가 가치를 더하는가"를 묻는다. 따라서 근거 문장은
# AI와 연결돼 있어야 한다. 이 게이트가 없으면 IR 실적발표·일반 경영 담론의
# 전략·목표·프로세스 어휘가 4차원에 그대로 걸려 케이스를 오염시킨다(실측).
AI_LINK = re.compile(
    r"\bAI\b|인공지능|\bAX\b|\bLLM\b|\bGPT\b|ChatGPT|Claude|Gemini|생성형|generative|\bGenAI\b|"
    r"머신\s*러닝|machine\s+learning|딥\s*러닝|deep\s+learning|에이전트|\bagent(ic|s)?\b|"
    r"코파일럿|copilot|챗봇|chatbot|파운데이션\s*모델|foundation\s+model|알고리즘|algorithm|"
    r"자동화\s*(에이전트|봇)|\bRAG\b|파인\s*튜닝|fine[-\s]?tun|프롬프트|prompt",
    re.I,
)
MIN_AI_LINKED_SENTS = 5        # AI 연결 문장이 이보다 적으면 케이스로 보지 않는다

# 강의·자격증 콘텐츠(케이스가 아니라 교육 상품)
TRAINING = rx(
    r"자격증|시험\s*(대비|합격|문제)|\bexam\b|certification|수강|커리큘럼|curriculum",
    r"강의(를|는|에서)|full\s+course|\bmodule\s*\d|챕터\s*\d|교재",
)

# ─────────────────────────────────────────────────────────────────
# 2. 수요측(도입 조직) vs 공급측(벤더) 발화 판별
#    프레임워크의 평가 단위는 'AI를 도입하는 조직'이므로 이 축이 케이스 적합성을 가른다.
# ─────────────────────────────────────────────────────────────────

DEMAND = rx(                                   # 조직 내부 전환 발화
    r"사내|전사(적)?|임직원|우리\s*(직원|회사|조직|팀|은행|그룹)|저희\s*(직원|회사|조직|팀|부서)",
    r"현업(\s*부서)?|현장(에서|의|에)|내부\s*(업무|시스템|프로세스|데이터)|자사\s*(업무|시스템)",
    r"\bour\s+(employees|workforce|teams?|people|staff|organization|company)\b",
    r"\binternal\s+(teams?|tools?|processes|systems)\b|\bour\s+own\s+(workflows?|processes|data)\b",
    r"변화\s*관리|change\s+management|리터러시|literacy|사내\s*교육|임직원\s*교육",
    r"저항|정착|확산(을|이|하)|adoption\s+rate|사용률|활용률|내재화",
    r"경영진|임원(진|들)?|\bCDO\b|\bCAIO\b|\bCIO\b|추진\s*(조직|단)|전담\s*조직|\bTF\b",
    r"파일럿|\bPoC\b|\bPOC\b|시범\s*(운영|적용)|도입\s*(과정|초기|후|배경)|현업\s*적용",
    r"업무(에|를)\s*(적용|활용)|일하는\s*방식(을|이)\s*(바꾸|변화|달라)",
)
SUPPLY = rx(                                   # 제품 판매·발표 발화
    r"출시(했|합니다|하는|됩니다)|launch(ing|ed|es)?\b|announc(e|ing|ed)\b|발표(합니다|해|했)",
    r"generally\s+available|\bGA\b|public\s+preview|베타|beta|얼리\s*액세스|early\s+access",
    r"가격|pricing|요금(제)?|무료\s*(체험|플랜)|free\s+(tier|trial)|구독(료|제)|\bSKU\b",
    r"저희\s*(제품|솔루션|플랫폼)|our\s+(product|platform|customers|solution)|우리\s*(제품|솔루션)",
    r"\bSDK\b|documentation|문서(를)?\s*보시|개발자(분)?(들)?(께|에게)|developers\s+can|샘플\s*코드",
    r"데모|demo\b|시연|부스|booth|이번\s*(세션|발표)에서(는)?\s*.{0,20}(소개|보여)",
    r"고객(사|분)들(께|에게|은)\s*.{0,12}(제공|드리|사용|쓰)|customers\s+can\s+now",
    r"파트너\s*(프로그램|사\s*모집)|리셀러|reseller\s+program",
)
# 사례 프레이밍(3자 사례 소개 포함)
CASE_FRAME = rx(r"사례|case\s+study|케이스|고객사|customer\s+story|적용\s*사례|도입\s*사례|성공\s*사례")
# 잡음 문장(홍보·구독 유도)
NOISE = re.compile(r"베스트셀러|출간|저자|구독|좋아요|알림\s*설정|채널\s*(구독|가입)|강의를\s*(듣|신청)|수강\s*신청")

# ─────────────────────────────────────────────────────────────────
# 3. 초점 조직(focal firm) 사전 — 정규 명칭 하나에 한/영 별칭을 묶는다.
#    ⚠️ 한글 회사명을 단순 부분일치로 세면 '애플' 이 '애플리케이션' 에 걸린다(실측 17회).
#       kr() 로 앞뒤 경계(조사만 허용)를 강제해 이 오탐을 막는다.
# ─────────────────────────────────────────────────────────────────

_PART = r"이|가|은|는|을|를|의|에|와|과|도|만|랑|께|에서|에선|으로|로|부터|까지|처럼|보다"


def kr(*names):
    """한글 회사명: 앞은 한글 아님, 뒤는 조사/비한글만 허용 (복합어 오탐 차단)."""
    return "|".join(rf"(?<![가-힣]){n}(?![가-힣])|(?<![가-힣]){n}(?=(?:{_PART}))" for n in names)


def en(*names):
    return "|".join(rf"\b{n}\b" for n in names)


def firm(*parts):
    return re.compile("|".join(parts), re.I)


FIRMS = {
    # ── 한국 수요기업(도입 조직) ──
    # '하닉스'는 자동자막 오인식 빈발형(원문 확인 필요) — 별칭으로 흡수한다
    "SK하이닉스": firm(kr("SK\\s*하이닉스", "하이닉스", "하닉스"), en("SK\\s*hynix")),
    "SK(지주·그룹)": re.compile(r"\bSK(?!\s*(?:하이닉스|하닉스|텔레콤|브로드밴드|이노베이션|hynix|Telecom))\b", re.I),
    "SK텔레콤": firm(kr("SK\\s*텔레콤", "SKT"), en("SK\\s*Telecom")),
    "SK그룹": firm(kr("SK\\s*그룹"), en("SK\\s*Group")),
    "삼성전자": firm(kr("삼성전자"), en("Samsung\\s+Electronics")),
    "삼성SDS": firm(kr("삼성\\s*SDS"), en("Samsung\\s+SDS")),
    "LG전자": firm(kr("LG전자"), en("LG\\s+Electronics")),
    "LG CNS": firm(kr("LG\\s*CNS"), en("LG\\s+CNS")),
    "LG AI연구원": firm(kr("LG\\s*AI\\s*연구원"), en("LG\\s+AI\\s+Research")),
    "현대자동차": firm(kr("현대차", "현대자동차"), en("Hyundai\\s+Motor")),
    "기아": firm(kr("기아차", "기아자동차")),
    "포스코": firm(kr("포스코"), en("POSCO")),
    "네이버": firm(kr("네이버"), en("NAVER")),
    "카카오": firm(kr("카카오"), en("Kakao")),
    "쿠팡": firm(kr("쿠팡"), en("Coupang")),
    "무신사": firm(kr("무신사", "무진사")),
    "토스": firm(kr("토스", "비바리퍼블리카"), en("Toss")),
    "KT": firm(en("KT")),
    "신한은행": firm(kr("신한은행", "신한금융")),
    "KB국민은행": firm(kr("국민은행", "KB국민", "KB금융")),
    "우리은행": firm(kr("우리은행", "우리금융")),
    "하나은행": firm(kr("하나은행", "하나금융")),
    "롯데": firm(kr("롯데")),
    "CJ": firm(kr("CJ제일제당", "CJ대한통운", "CJ올리브")),
    "한화": firm(kr("한화")),
    "두산": firm(kr("두산")),
    "아모레퍼시픽": firm(kr("아모레퍼시픽", "아모레")),
    "대한항공": firm(kr("대한항공")),
    "업스테이지": firm(kr("업스테이지"), en("Upstage")),
    # ── 글로벌 수요기업(도입 조직) ──
    "Unilever": firm(kr("유니레버"), en("Unilever")),
    "L'Oréal": firm(kr("로레알"), en("L'?Or[eé]al")),
    "Nestlé": firm(kr("네슬레"), en("Nestl[eé]")),
    "IKEA": firm(kr("이케아"), en("IKEA")),
    "Walmart": firm(kr("월마트"), en("Walmart")),
    "Carrefour": firm(kr("까르푸"), en("Carrefour")),
    "Target": firm(en("Target\\s+Corporation")),
    "Home Depot": firm(en("Home\\s*Depot")),
    "Starbucks": firm(kr("스타벅스"), en("Starbucks")),
    "Nike": firm(kr("나이키"), en("Nike")),
    "Reckitt": firm(kr("레킷"), en("Reckitt")),
    "JPMorgan": firm(kr("JP\\s*모건"), en("JPMorgan", "JP\\s*Morgan")),
    "Goldman Sachs": firm(kr("골드만\\s*삭스"), en("Goldman\\s+Sachs")),
    "Morgan Stanley": firm(kr("모건\\s*스탠리"), en("Morgan\\s+Stanley")),
    "BNY": firm(en("BNY", "Bank\\s+of\\s+New\\s+York")),
    "BBVA": firm(en("BBVA")),
    "Swedbank": firm(en("Swedbank")),
    "Klarna": firm(kr("클라르나"), en("Klarna")),
    "Moody's": firm(en("Moody'?s")),
    "DBS": firm(en("DBS\\s+Bank", "DBS")),
    "HSBC": firm(en("HSBC")),
    "Standard Chartered": firm(en("Standard\\s+Chartered")),
    "Allianz": firm(en("Allianz")),
    "AXA": firm(en("AXA")),
    "Moderna": firm(kr("모더나"), en("Moderna")),
    "Eli Lilly": firm(kr("일라이\\s*릴리"), en("Eli\\s+Lilly")),
    "Novo Nordisk": firm(kr("노보\\s*노디스크"), en("Novo\\s+Nordisk")),
    "Pfizer": firm(kr("화이자"), en("Pfizer")),
    "Roche": firm(en("Roche")),
    "Novartis": firm(en("Novartis")),
    "Johnson & Johnson": firm(kr("존슨앤존슨"), en("Johnson\\s*&\\s*Johnson")),
    "Mayo Clinic": firm(kr("메이요"), en("Mayo\\s+Clinic")),
    "Philips": firm(kr("필립스"), en("Philips")),
    "GE HealthCare": firm(en("GE\\s+HealthCare")),
    "IQVIA": firm(en("IQVIA")),
    "Toyota": firm(kr("도요타", "토요타"), en("Toyota")),
    "BMW": firm(en("BMW")),
    "Mercedes-Benz": firm(kr("벤츠"), en("Mercedes[-\\s]?Benz")),
    "Volvo": firm(kr("볼보"), en("Volvo")),
    "Nissan": firm(kr("닛산"), en("Nissan")),
    "General Motors": firm(en("General\\s+Motors", "\\bGM\\b")),
    "Ford": firm(en("Ford\\s+Motor", "Ford")),
    "BYD": firm(en("BYD")),
    "Hero MotoCorp": firm(en("Hero\\s+Moto(Corp)?")),
    "Siemens": firm(kr("지멘스"), en("Siemens")),
    "Schneider Electric": firm(en("Schneider\\s+Electric")),
    "Rockwell Automation": firm(en("Rockwell")),
    "Sandvik": firm(en("Sandvik")),
    "Caterpillar": firm(kr("캐터필러"), en("Caterpillar")),
    "Boeing": firm(kr("보잉"), en("Boeing")),
    "Foxconn": firm(en("Foxconn")),
    "Orange": firm(en("Orange\\s+(Business|Group)?")),
    "Telefónica": firm(en("Telef[oó]nica")),
    "Vodafone": firm(en("Vodafone")),
    "Swisscom": firm(en("Swisscom")),
    "Telenor": firm(en("Telenor")),
    "AT&T": firm(en("AT&T")),
    "Verizon": firm(en("Verizon")),
    "T-Mobile": firm(en("T-Mobile")),
    "Nokia": firm(kr("노키아"), en("Nokia")),
    "Ericsson": firm(kr("에릭슨"), en("Ericsson")),
    "SoftBank": firm(kr("소프트뱅크"), en("SoftBank")),
    "NTT DATA": firm(en("NTT\\s+DATA")),
    "Uber": firm(en("Uber")),
    "Shopify": firm(en("Shopify")),
    "Instacart": firm(en("Instacart")),
    "MediaMarkt": firm(en("MediaMarkt")),
    "Netflix": firm(kr("넷플릭스"), en("Netflix")),
    "Chegg": firm(en("Chegg")),
    "Indeed": firm(en("Indeed\\s+(com|Inc)?")),
    "PayPal": firm(en("PayPal")),
    "Intuit": firm(en("Intuit")),
    "LinkedIn": firm(en("LinkedIn")),
    # ── 벤더·공급측(초점 조직이 되면 대개 vendor_selfpromo) ──
    "NVIDIA": firm(kr("엔비디아"), en("NVIDIA")),
    "OpenAI": firm(kr("오픈AI", "오픈에이아이"), en("OpenAI")),
    "Anthropic": firm(kr("앤트로픽"), en("Anthropic")),
    "Google": firm(kr("구글"), en("Google", "Alphabet")),
    "Google DeepMind": firm(en("DeepMind")),
    "Microsoft": firm(kr("마이크로소프트", "MS"), en("Microsoft")),
    "Meta": firm(kr("메타"), en("Meta\\s+(Platforms|AI)?")),
    "Apple": firm(kr("애플"), en("Apple")),
    "Amazon": firm(kr("아마존"), en("Amazon")),
    "AWS": firm(en("AWS", "Amazon\\s+Web\\s+Services")),
    "IBM": firm(en("IBM")),
    "Oracle": firm(kr("오라클"), en("Oracle")),
    "Salesforce": firm(kr("세일즈포스"), en("Salesforce")),
    "SAP": firm(en("SAP")),
    "ServiceNow": firm(en("ServiceNow")),
    "Palantir": firm(kr("팔란티어"), en("Palantir")),
    "Databricks": firm(en("Databricks")),
    "Snowflake": firm(en("Snowflake")),
    "Adobe": firm(kr("어도비"), en("Adobe")),
    "Intel": firm(kr("인텔"), en("Intel")),
    "AMD": firm(en("AMD")),
    "Arm": firm(en("Arm\\s+(Holdings|Ltd)?")),
    "TSMC": firm(en("TSMC")),
    "Qualcomm": firm(kr("퀄컴"), en("Qualcomm")),
    "Broadcom": firm(en("Broadcom")),
    "Huawei": firm(kr("화웨이"), en("Huawei")),
    "Alibaba": firm(kr("알리바바"), en("Alibaba")),
    "Tencent": firm(kr("텐센트"), en("Tencent")),
    "Baidu": firm(kr("바이두"), en("Baidu")),
    "DeepSeek": firm(kr("딥시크"), en("DeepSeek")),
    "Mistral AI": firm(en("Mistral")),
    "Cohere": firm(en("Cohere")),
    "Hugging Face": firm(en("Hugging\\s*Face")),
    "GitHub": firm(kr("깃허브"), en("GitHub")),
    "Cursor": firm(en("Cursor")),
    "Replit": firm(en("Replit")),
    "Zapier": firm(en("Zapier")),
    "Slack": firm(en("Slack")),
    "Pinecone": firm(en("Pinecone")),
    "Weaviate": firm(en("Weaviate")),
    "Qdrant": firm(en("Qdrant")),
    "ElevenLabs": firm(en("ElevenLabs")),
    "Tesla": firm(kr("테슬라"), en("Tesla")),
    "Waymo": firm(en("Waymo")),
    "Figure": firm(en("Figure\\s+AI")),
    "Boston Dynamics": firm(en("Boston\\s+Dynamics")),
    "Anduril": firm(en("Anduril")),
    # ── 컨설팅(케이스의 화자로 자주 등장) ──
    "McKinsey": firm(kr("맥킨지"), en("McKinsey")),
    "BCG": firm(en("BCG", "Boston\\s+Consulting")),
    "Accenture": firm(kr("액센츄어", "액센추어"), en("Accenture")),
    "Deloitte": firm(kr("딜로이트"), en("Deloitte")),
    "PwC": firm(en("PwC")),
    "KPMG": firm(en("KPMG")),
    "EY": firm(en("Ernst\\s*&\\s*Young")),
    "Infosys": firm(en("Infosys")),
    "TCS": firm(en("Tata\\s+Consultancy")),
    "Capgemini": firm(en("Capgemini")),
    "Genpact": firm(en("Genpact")),
    "Gartner": firm(kr("가트너"), en("Gartner")),
}

# 채널명 → 정규 기업명 (같은 기업이 채널 여러 개로 쪼개지는 것 방지)
CHANNEL_ALIAS = {
    "Apple Developer": "Apple", "NVIDIA Developer": "NVIDIA", "AWS Events": "AWS",
    "AWS Developers": "AWS", "Google Cloud Tech": "Google", "Google Developers": "Google",
    "Microsoft Azure": "Microsoft", "Microsoft Developer": "Microsoft",
    "Meta Developers": "Meta", "IBM Technology": "IBM", "Samsung Semiconductor": "삼성전자",
    "SK hynix": "SK하이닉스", "NAVER Cloud": "네이버", "kakao tech": "카카오",
    "LG AI Research": "LG AI연구원", "SK텔레콤": "SK텔레콤", "McKinsey & Company": "McKinsey",
    "Boston Consulting Group": "BCG", "Google DeepMind": "Google DeepMind",
    "Volvo Cars": "Volvo", "Mercedes-Benz": "Mercedes-Benz", "Weights & Biases": "Weights & Biases",
    "Alibaba Cloud": "Alibaba", "Amazon Web Services": "AWS", "Unilever": "Unilever",
}

# 공급측 기본값 채널(스택 벤더) — 자기 채널 발화는 기본적으로 제품 담론으로 본다
VENDOR_CANON = {
    "NVIDIA", "OpenAI", "Anthropic", "Google", "Google DeepMind", "Microsoft", "Meta", "Apple",
    "Amazon", "AWS", "IBM", "Oracle", "Salesforce", "SAP", "ServiceNow", "Palantir", "Databricks",
    "Snowflake", "Adobe", "Intel", "AMD", "Arm", "TSMC", "Qualcomm", "Broadcom", "Huawei",
    "Alibaba", "Tencent", "Baidu", "DeepSeek", "Mistral AI", "Cohere", "Hugging Face", "GitHub",
    "Cursor", "Replit", "Zapier", "Slack", "Pinecone", "Weaviate", "Qdrant", "ElevenLabs",
    "Weights & Biases", "McKinsey", "BCG", "Accenture", "Deloitte", "PwC", "KPMG", "EY",
    "Infosys", "TCS", "Capgemini", "Genpact", "Gartner", "Scale AI", "LG CNS", "삼성SDS",
}

MIN_MENTION_FOR_FOCAL = 4      # 본문만으로 초점 기업을 인정할 최소 언급 수
MIN_MENTION_FOR_STORY = 5      # 벤더 채널에서 '고객 사례'로 볼 최소 고객사 언급 수
MAX_QUOTE = 260
DIM_LABEL = {"tech": "Technologies", "act": "Activities", "bnd": "Boundaries", "goal": "Goals"}
DIM_KO = {"tech": "기술", "act": "활동", "bnd": "경계", "goal": "목표"}
ROLE_KO = {
    "adopter_self": "도입 조직 자기발화",
    "third_party_case": "제3자가 보도·강연한 도입 사례",
    "vendor_customer_story": "벤더가 소개한 고객 사례",
    "vendor_selfpromo": "벤더 제품 발화",
    "expert_commentary": "전문가·미디어 일반론",
}
# 가치 언어가 이만큼도 없으면 'value-adding' 척도를 매길 수 없다 → 케이스에서 제외
MIN_VALUE_EVIDENCE = 2


def hits(patterns, text):
    return sum(1 for p in patterns if p.search(text))


def counts(patterns, text):
    return sum(len(p.findall(text)) for p in patterns)


def tense_of(sent):
    """시제 배정: future 우선(계획 발화가 더 특정적), 없으면 current, 둘 다 없으면 unspec."""
    if hits(FUTURE, sent):
        return "fut"
    if hits(CURRENT, sent):
        return "cur"
    return "unspec"


def scan_text(text):
    """본문을 8셀(4차원×2시제)로 코딩하고 셀별 근거 문장을 모은다.

    AI 연결성 게이트: 근거로 인정하는 문장은 그 문장 또는 바로 앞/뒤 문장에
    AI 어휘가 있는 것만이다(자동자막은 문장 경계가 흔들려 ±1문장까지 허용).
    """
    cells = {f"{d}_{t}": 0 for d in DIMENSIONS for t in ("cur", "fut", "unspec")}
    quotes = {f"{d}_{t}": [] for d in DIMENSIONS for t in ("cur", "fut")}
    value_sents = metric_sents = 0

    sents = split_sentences(text)
    ai_flags = [bool(AI_LINK.search(s)) for s in sents]
    ai_linked = sum(ai_flags)

    # 담화 시제 전파: 한국어 구어는 시제를 한 번 밝히고 이어 말하므로 문장마다
    # 마커가 없다. 마커 없는 문장은 앞 2문장 → 뒤 1문장의 시제를 물려받는다.
    # (전파를 안 하면 근거 대부분이 unspec 으로 빠져 8셀이 채워지지 않는다 — 실측)
    own = [tense_of(s) for s in sents]
    eff = list(own)
    for i, t in enumerate(own):
        if t != "unspec":
            continue
        for j in range(i - 1, max(-1, i - 3), -1):
            if own[j] != "unspec":
                eff[i] = own[j]
                break
        if eff[i] == "unspec" and i + 1 < len(own) and own[i + 1] != "unspec":
            eff[i] = own[i + 1]

    for i, sent in enumerate(sents):
        if NOISE.search(sent):
            continue
        if not (ai_flags[i] or (i and ai_flags[i - 1])
                or (i + 1 < len(sents) and ai_flags[i + 1])):
            continue                      # AI와 무관한 일반 경영 발화는 근거로 쓰지 않는다
        s = sent if len(sent) <= MAX_QUOTE else sent[:MAX_QUOTE] + "…"
        matched = [d for d, pats in DIMENSIONS.items() if hits(pats, sent)]
        if not matched:
            continue
        t = eff[i]
        has_value = bool(hits(VALUE, sent))
        has_metric = bool(METRIC.search(sent))
        value_sents += has_value
        metric_sents += has_metric
        for d in matched:
            cells[f"{d}_{t}"] += 1
            if t != "unspec":
                # 발췌 우선순위: 가치언어+수치 > 가치언어 > 그 외, 동점이면 차원 특이성 높은 문장
                pri = (2 if has_value else 0) + (1 if has_metric else 0)
                quotes[f"{d}_{t}"].append((pri, len(matched), s))

    best = {}
    for key, lst in quotes.items():
        lst.sort(key=lambda x: (-x[0], x[1]))
        best[key] = lst[0][2] if lst else ""
    return cells, best, value_sents, metric_sents, ai_linked


def prov_score(n):
    """근거 문장 수 → 잠정 0~4 대리지표 (self-report 점수가 아님)."""
    return 0 if n <= 0 else 1 if n == 1 else 2 if n == 2 else 3 if n <= 4 else 4


def canon_channel(channel):
    if channel in CHANNEL_ALIAS:
        return CHANNEL_ALIAS[channel]
    # 채널명이 정규 기업명과 그대로 일치하면 그것으로
    for name in FIRMS:
        if channel.lower() == name.lower():
            return name
    return channel


def detect_firms(text):
    """본문에 등장한 정규 기업명과 언급 횟수."""
    c = collections.Counter()
    for name, pat in FIRMS.items():
        n = len(pat.findall(text))
        if n:
            c[name] = n
    return c


def focal_from_body(mentioned, exclude=""):
    """본문 언급만으로 초점 기업 추정 — 1위가 2위를 압도할 때만 인정한다.
    (압도 규칙이 없으면 여러 기업을 나열하는 일반 강연에서 엉뚱한 기업이 초점이 된다)"""
    ranked = [(n, c) for n, c in mentioned.most_common() if n != exclude]
    if not ranked:
        return "", 0
    top, top_n = ranked[0]
    second_n = ranked[1][1] if len(ranked) > 1 else 0
    if top_n >= MIN_MENTION_FOR_FOCAL and (top_n >= 2 * second_n or top_n >= 10):
        return top, top_n
    return "", top_n


def classify_case(text, title, channel, source):
    """초점 조직 + case_role 판정. (초점, 화자, 역할, 수요/공급 카운트, 언급목록)"""
    mentioned = detect_firms(text)
    # 제목에 기업명이 있으면 그 기업이 사례의 초점이다(가장 강한 신호).
    # 본문 언급이 0이어도 인정한다 — 자막이 사명을 다르게 표기하는 일이 흔하다.
    in_title = list(detect_firms(title))
    speaker = canon_channel(channel) if source == "channel" else ""
    demand = counts(DEMAND, text)
    supply = counts(SUPPLY, text)
    case_frame = hits(CASE_FRAME, text)

    # 화자 자신을 제외한 초점 후보
    top_other, top_other_n = focal_from_body(mentioned, exclude=speaker)
    title_focal = max(in_title, key=lambda n: mentioned.get(n, 0)) if in_title else ""
    if title_focal and title_focal != speaker:
        top_other, top_other_n = title_focal, max(mentioned[title_focal], MIN_MENTION_FOR_STORY)

    if hits(TRAINING, text) >= 2:              # 강의·자격증 상품은 케이스가 아니다
        return "", speaker, "expert_commentary", demand, supply, mentioned

    if source == "channel" and speaker:
        speaker_n = mentioned.get(speaker, 0)
        if speaker in VENDOR_CANON:
            # 벤더 채널이 특정 고객사를 사례로 다루는가
            if (top_other_n >= MIN_MENTION_FOR_STORY and case_frame
                    and top_other not in VENDOR_CANON and demand >= 3):
                return top_other, speaker, "vendor_customer_story", demand, supply, mentioned
            # 벤더가 자기 조직의 내부 전환을 말하는 경우도 있다(수요측 발화).
            # 단, 게스트 인터뷰·팟캐스트에서 남의 회사 전환을 다루는 형식이 흔하므로
            # 채널사가 본문에서 최다 언급 기업일 때만 자기발화로 인정한다.
            if demand >= 12 and demand > supply * 1.5 and speaker_n >= top_other_n:
                return speaker, speaker, "adopter_self", demand, supply, mentioned
            return speaker, speaker, "vendor_selfpromo", demand, supply, mentioned
        # 비벤더(수요기업·미디어) 채널 — 남의 회사가 초점이면 제3자 사례다
        if top_other and top_other_n > speaker_n and demand >= 3:
            role = "vendor_customer_story" if top_other in VENDOR_CANON else "third_party_case"
            return top_other, speaker, role, demand, supply, mentioned
        if demand >= 3:
            return speaker, speaker, "adopter_self", demand, supply, mentioned
        return speaker, speaker, "expert_commentary", demand, supply, mentioned

    # 키워드 수집분(제3자 미디어·강연) — 제목 우선, 없으면 본문 우세 기업.
    # 화자가 그 기업 소속이 아니므로 자기보고가 아니라 '제3자 사례'다.
    if top_other and top_other_n >= MIN_MENTION_FOR_FOCAL:
        if top_other in VENDOR_CANON:
            # 벤더가 초점으로 잡혔다면 실제 사례 주체는 언급된 고객사다
            non_vendor = collections.Counter(
                {n: c for n, c in mentioned.items() if n not in VENDOR_CANON})
            cust, _ = focal_from_body(non_vendor)
            if case_frame and cust:
                return cust, top_other, "vendor_customer_story", demand, supply, mentioned
            return top_other, top_other, "vendor_selfpromo", demand, supply, mentioned
        if demand >= 4 or case_frame:
            return top_other, "", "third_party_case", demand, supply, mentioned
        return top_other, "", "expert_commentary", demand, supply, mentioned
    return "", "", "expert_commentary", demand, supply, mentioned


def tier_of(filled, dims_covered):
    if dims_covered < 4:
        return ""
    return "A" if filled == 8 else "B" if filled >= 6 else "C" if filled >= 4 else ""


ROLE_WEIGHT = {"adopter_self": 25, "third_party_case": 20, "vendor_customer_story": 15,
               "expert_commentary": 0, "vendor_selfpromo": -20}


def collect():
    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows, skipped = [], collections.Counter()
    for path in files:
        meta, text = parse_transcript(path)
        _h, _d, words = score_text(text)
        rel = classify_relevance(text, words)
        if rel != "ax_core":
            skipped[rel] += 1
            continue

        cells, quotes, value_sents, metric_sents, ai_linked = scan_text(text)
        if ai_linked < MIN_AI_LINKED_SENTS:
            skipped["ai_thin"] += 1        # AI가 곁가지인 발화(IR 실적발표 등)
            continue
        filled = sum(1 for d in DIMENSIONS for t in ("cur", "fut") if cells[f"{d}_{t}"] > 0)
        dims_covered = sum(
            1 for d in DIMENSIONS
            if cells[f"{d}_cur"] + cells[f"{d}_fut"] + cells[f"{d}_unspec"] > 0
        )
        tier = tier_of(filled, dims_covered)
        if not tier:
            skipped["framework_incomplete"] += 1
            continue

        source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
        channel = meta["channel"] or "(미상)"
        focal, speaker, role, demand, supply, mentioned = classify_case(
            text, meta["title"], channel, source)

        row = {
            "tier": tier,
            "case_role": role,
            "focal_firm": focal or "(초점 조직 불명)",
            "speaker": speaker or channel,
            "date": meta.get("upload_date") or doc_month(path, meta),
            "month": doc_month(path, meta),
            "channel": channel,
            "title": meta["title"],
            "source": source,
            "lang": meta["lang"],
            "words": words,
            "stance": classify_stance(text),
            "cells_filled": filled,
            "demand_hits": demand,
            "supply_hits": supply,
            "value_sents": value_sents,
            "metric_sents": metric_sents,
            "ai_linked_sents": ai_linked,
            "mentions": "; ".join(f"{n}({c})" for n, c in mentioned.most_common(5)),
            "url": meta["url"],
            "file": path.replace(os.sep, "/"),
        }
        for d in DIMENSIONS:
            for t in ("cur", "fut"):
                row[f"n_{d}_{t}"] = cells[f"{d}_{t}"]
                row[f"prov_{d}_{t}"] = prov_score(cells[f"{d}_{t}"])
                row[f"q_{d}_{t}"] = quotes[f"{d}_{t}"]
            row[f"n_{d}_unspec"] = cells[f"{d}_unspec"]
        # 케이스 적합도: 역할(수요측 우선) > 셀 충족 > 가치언어 > 수치
        row["usable"] = ""      # 아래에서 채운다
        row["fit"] = (
            ROLE_WEIGHT[role]
            + filled * 6
            + min(value_sents, 15)
            + min(metric_sents, 10)
            + min(demand // 3, 8)
        )
        rows.append(row)

    for r in rows:
        r["usable"] = "Y" if is_usable(r) else "N"
    rows.sort(key=lambda r: (-r["fit"], r["focal_firm"]))
    return rows, skipped, len(files)


USABLE_ROLES = ("adopter_self", "third_party_case", "vendor_customer_story")


def is_usable(row):
    """프레임워크 스코어카드를 실제로 채울 수 있는 케이스인가."""
    return (row["case_role"] in USABLE_ROLES
            and row["focal_firm"] != "(초점 조직 불명)"
            and row["value_sents"] + row["metric_sents"] >= MIN_VALUE_EVIDENCE)


def pool_by_firm(rows):
    """기업별 근거 합산 — 사례 단위는 기업. 수요측 근거(1·2급 역할)만 합산한다."""
    firms = collections.defaultdict(lambda: {
        "videos": 0, "value": 0, "metric": 0, "demand": 0, "months": set(),
        "titles": [], "cells": collections.Counter(), "roles": collections.Counter(),
        "langs": collections.Counter(),
    })
    for r in rows:
        if r["usable"] != "Y":
            continue
        f = firms[r["focal_firm"]]
        f["videos"] += 1
        f["value"] += r["value_sents"]
        f["metric"] += r["metric_sents"]
        f["demand"] += r["demand_hits"]
        f["months"].add(r["month"])
        f["titles"].append((r["fit"], r["title"], r["url"], r["file"], r["tier"]))
        f["roles"][r["case_role"]] += 1
        f["langs"][r["lang"]] += 1
        for d in DIMENSIONS:
            for t in ("cur", "fut"):
                f["cells"][f"{d}_{t}"] += r[f"n_{d}_{t}"]

    out = []
    for name, f in firms.items():
        filled = sum(1 for d in DIMENSIONS for t in ("cur", "fut") if f["cells"][f"{d}_{t}"] > 0)
        f["titles"].sort(key=lambda x: -x[0])
        row = {
            "focal_firm": name,
            "videos": f["videos"],
            "cells_filled": filled,
            "months": len(f["months"]),
            "span": f"{min(f['months'])}~{max(f['months'])}" if f["months"] else "",
            "value_sents": f["value"],
            "metric_sents": f["metric"],
            "demand_hits": f["demand"],
            "dominant_role": f["roles"].most_common(1)[0][0],
            "roles": " · ".join(f"{ROLE_KO[k]}{v}" for k, v in f["roles"].most_common()),
            "best_tier": min(t[4] for t in f["titles"]),
            "lang": "/".join(f"{k}{v}" for k, v in f["langs"].most_common()),
            "top_video": f["titles"][0][1],
            "top_url": f["titles"][0][2],
            "top_file": f["titles"][0][3],
        }
        for d in DIMENSIONS:
            for t in ("cur", "fut"):
                row[f"n_{d}_{t}"] = f["cells"][f"{d}_{t}"]
        row["fit"] = (filled * 10 + min(f["value"], 40) + min(f["metric"], 25)
                      + min(f["videos"], 12) + (10 if f["roles"]["adopter_self"] else 0))
        out.append(row)
    out.sort(key=lambda r: (-r["cells_filled"], -r["fit"]))
    return out


def write_csv(path, rows):
    if not rows:
        return
    with open(path, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def bar(score):
    return "■" * score + "·" * (4 - score)


def scorecard(row, prefix="prov_"):
    return " · ".join(
        f"{DIM_KO[d]} {row[f'{prefix}{d}_cur']}/{row[f'{prefix}{d}_fut']}" for d in DIMENSIONS
    )


def clip(s, n):
    s = s.replace("|", "／").strip()
    return s if len(s) <= n else s[:n] + "…"


def write_md(rows, firms, skipped, total_files):
    usable = [r for r in rows if r["usable"] == "Y"]
    tiers = collections.Counter(r["tier"] for r in usable)
    roles = collections.Counter(r["case_role"] for r in rows)
    L = []
    A = L.append

    A("# AI readiness framework 적용 가능 케이스 (코퍼스 전량 스캔)")
    A("")
    A("> Holmström, J. (2022). From AI to digital transformation: The AI readiness framework.")
    A("> *Business Horizons, 65*(3), 329–339. https://doi.org/10.1016/j.bushor.2021.03.006")
    A(">")
    A("> 4차원(**technologies · activities · boundaries · goals**) × 2시점(**current · future**)")
    A("> = 8셀 스코어카드, 0~4점(0 none · 1 low · 2 moderate · 3 high · 4 excellent) **자기보고**.")
    A("> 논문의 보험사 사례: 기술 4/2 · 활동 2/3 · 경계 1/2 · 목표 0/1 (현재/미래).")
    A("")
    A(f"생성: `python readiness_scan.py` — 스캔 {total_files:,}건 → ax_core 후보 중 "
      f"4차원 모두 커버 **{len(rows):,}건**, 그중 프레임워크에 쓸 수 있는 "
      f"**{len(usable):,}건**(A {tiers['A']} · B {tiers['B']} · C {tiers['C']}), "
      f"초점 기업 **{len(firms):,}곳**.")
    A("")
    A("## 1. 판정 규칙 — 무엇을 '적합한 케이스'로 봤나")
    A("")
    A("| 요건 | 규칙 |")
    A("|---|---|")
    A("| 담론 관련성 | `classify_v2` 의 `relevance == ax_core` (전환·조직·비용 프레이밍) |")
    A("| 4차원 커버 | technologies · activities · boundaries · goals 각각 근거 문장 ≥ 1 |")
    A("| 시점 분해 | 같은 문장의 시제 마커로 current / future 배정 (미배정분은 셀 충족에 미사용) |")
    A("| 티어 | **A** = 8셀 모두 · **B** = 6~7셀 · **C** = 4~5셀 |")
    A("| **평가 단위** | 프레임워크는 *AI를 도입하는 조직*을 재는 도구다 → `case_role` 로 발화 위치를 가른다 |")
    A(f"| AI 연결성 | 근거 문장은 자신 또는 ±1문장에 AI 어휘가 있어야 인정. AI 연결 문장 "
      f"{MIN_AI_LINKED_SENTS}개 미만이면 케이스 아님(IR 실적발표 배제) |")
    A(f"| 가치 언어 | 원 설문의 공통 프레이즈가 'value-adding' 이므로 가치·수치 문장 "
      f"{MIN_VALUE_EVIDENCE}개 이상을 요구 |")
    A("| 시제 전파 | 한국어 구어는 시제를 한 번만 밝히므로, 마커 없는 문장은 앞 2·뒤 1문장의 시제를 물려받는다 |")
    A("")
    A("| case_role | 뜻 | 프레임워크 적합성 | 건수 |")
    A("|---|---|---|---|")
    for k in ("adopter_self", "third_party_case", "vendor_customer_story",
              "expert_commentary", "vendor_selfpromo"):
        fitness = {"adopter_self": "**1급** — 조직이 자기 전환을 진술",
                   "third_party_case": "**2급** — 초점 조직은 명확, 진술은 제3자(교차검증 필요)",
                   "vendor_customer_story": "**3급** — 초점=고객사, 벤더 홍보 필터 필요",
                   "expert_commentary": "부적합 — 초점 조직 없음(설문 문항 설계에는 유용)",
                   "vendor_selfpromo": "부적합 — 공급측 제품 담론"}[k]
        A(f"| `{k}` | {ROLE_KO[k]} | {fitness} | {roles[k]:,} |")
    A("")
    A("`prov_*` 점수(0~4)는 **근거 문장 밀도 대리지표**다(1문장=1 · 2=2 · 3~4=3 · 5+=4). "
      "원 논문의 self-report 점수와 같은 것이 아니며 케이스 정렬 기준으로만 쓴다.")
    A("")

    # ── 차원별 충족률 ──
    A("## 2. 차원별 근거 충족률 — 논문의 '하락 패턴'이 재현되는가")
    A("")
    A("논문의 보험사는 기술 → 활동 → 경계 → 목표 순으로 점수가 체계적으로 하락했다. "
      "우리 코퍼스(사용 가능 케이스 기준)도 같은 순서로 얇아진다.")
    A("")
    A("| 차원 | 현재 근거 있는 케이스 | 미래 근거 있는 케이스 | 평균 근거 문장(현재/미래) |")
    A("|---|---|---|---|")
    n = max(len(usable), 1)
    for d in DIMENSIONS:
        cur = sum(1 for r in usable if r[f"n_{d}_cur"] > 0)
        fut = sum(1 for r in usable if r[f"n_{d}_fut"] > 0)
        acur = sum(r[f"n_{d}_cur"] for r in usable) / n
        afut = sum(r[f"n_{d}_fut"] for r in usable) / n
        A(f"| {DIM_LABEL[d]}({DIM_KO[d]}) | {cur:,} ({100*cur/n:.0f}%) | "
          f"{fut:,} ({100*fut/n:.0f}%) | {acur:.1f} / {afut:.1f} |")
    A("")
    A("읽는 법: **경계·목표 차원의 현재 근거가 가장 얇다**는 것이 이 코퍼스의 구조적 사실이다. "
      "논문의 진단(기업은 기술을 말하고 목표를 말하지 않는다)과 같은 방향이며, "
      "특별호 투고 시 '공개 담론에서도 경계·목표가 비어 있다'는 근거로 쓸 수 있다.")
    A("")

    # ── 기업 단위 통합 스코어카드 ──
    A("## 3. 기업 단위 통합 스코어카드 (여러 영상 합산 · 상위 45)")
    A("")
    A("사례 연구 단위는 기업이다. 아래는 **수요측 근거(1·2급 역할)만** 합산한 것으로, "
      "숫자는 근거 문장 수(0~4 점수가 아니다). `영상` = 이 기업이 초점인 케이스 수.")
    A("")
    A("| # | 기업 | 영상 | 셀 | 기술 현/미 | 활동 현/미 | 경계 현/미 | 목표 현/미 | 가치·수치 | 기간 | 대표 역할 |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, f in enumerate(firms[:45], 1):
        A(f"| {i} | **{f['focal_firm']}** | {f['videos']} | {f['cells_filled']}/8 | "
          + " | ".join(f"{f[f'n_{d}_cur']}/{f[f'n_{d}_fut']}" for d in DIMENSIONS)
          + f" | {f['value_sents']}·{f['metric_sents']} | {f['span']} | {ROLE_KO[f['dominant_role']]} |")
    A("")

    # ── 역할별 케이스 목록 ──
    for role, heading, limit in (
        ("adopter_self", "4. 1급 케이스 — 도입 조직이 자기 전환을 말한 영상", 70),
        ("third_party_case", "5. 2급 케이스 — 제3자(미디어·강연)가 다룬 도입 사례", 60),
        ("vendor_customer_story", "6. 3급 케이스 — 벤더가 소개한 고객사 사례", 40),
    ):
        sub = [r for r in usable if r["case_role"] == role]
        A(f"## {heading} ({len(sub):,}건 중 상위 {min(limit, len(sub))})")
        A("")
        A("| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |")
        A("|---|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(sub[:limit], 1):
            A(f"| {i} | {r['focal_firm']} | {r['tier']}{r['cells_filled']} | {scorecard(r)} | "
              f"{r['value_sents']}·{r['metric_sents']} | {r['date']} | {clip(r['channel'], 22)} | "
              f"{clip(r['title'], 54)} | [▶]({r['url']}) |")
        A("")

    # ── 상세 카드 ──
    border = [r for r in rows if r["case_role"] in USABLE_ROLES and r["usable"] != "Y"]
    A(f"## 7. 경계선 후보 ({len(border):,}건) — 역할은 케이스인데 게이트에 걸린 것")
    A("")
    A(f"초점 조직이 불명이거나 가치·수치 문장이 {MIN_VALUE_EVIDENCE}개 미만인 건들이다. "
      "초점 조직을 손으로 지정하거나 같은 기업의 다른 영상과 합치면 살아난다.")
    A("")
    A("| # | 초점 조직 | 역할 | 티어 | 가치·수치 | 제목 | 링크 |")
    A("|---|---|---|---|---|---|---|")
    for i, r in enumerate(border[:40], 1):
        A(f"| {i} | {r['focal_firm']} | {ROLE_KO[r['case_role']]} | {r['tier']}{r['cells_filled']} | "
          f"{r['value_sents']}·{r['metric_sents']} | {clip(r['title'], 52)} | [▶]({r['url']}) |")
    A("")
    A("## 8. 상세 — 셀별 근거 발췌 (상위 20)")
    A("")
    A("발췌는 자동자막 원문이라 오탈자·오인식이 있다(예: '애플리케이션'→'애플'). "
      "**인용 전 원문 파일 확인 필수.**")
    A("")
    for i, r in enumerate(usable[:20], 1):
        A(f"### {i}. {r['focal_firm']} — {clip(r['title'], 90)}")
        A("")
        A(f"- 티어 {r['tier']} ({r['cells_filled']}/8셀) · 역할 `{r['case_role']}` "
          f"· 톤 `{r['stance']}` · 수요/공급 신호 {r['demand_hits']}/{r['supply_hits']} "
          f"· {r['date']} · 채널 {r['channel']} · [영상]({r['url']})")
        A(f"- 파일: `{r['file']}`")
        A("")
        A("| 차원 | 현재 | 미래 |")
        A("|---|---|---|")
        for d in DIMENSIONS:
            A(f"| {DIM_LABEL[d]} | {bar(r[f'prov_{d}_cur'])} {r[f'prov_{d}_cur']} "
              f"| {bar(r[f'prov_{d}_fut'])} {r[f'prov_{d}_fut']} |")
        A("")
        for d in DIMENSIONS:
            for t, ko in (("cur", "현재"), ("fut", "미래")):
                q = r[f"q_{d}_{t}"]
                if q:
                    A(f"- **{DIM_KO[d]}·{ko}**: “{q}”")
        A("")

    # ── 제외된 것들 ──
    excluded = [r for r in rows if r["usable"] != "Y"]
    A(f"## 9. 프레임워크에 쓰지 않은 것 ({len(excluded):,}건)")
    A("")
    A("| 이유 | 건수 | 그래도 쓸 곳 |")
    A("|---|---|---|")
    A(f"| `vendor_selfpromo` — 공급측 제품 담론 | {roles['vendor_selfpromo']:,} | "
      "기술 차원의 '무엇이 시장에 있나' 레퍼런스, AI 워싱 측정 |")
    A(f"| `expert_commentary` — 초점 조직 없는 일반론 | {roles['expert_commentary']:,} | "
      "설문 문항 워딩 설계, 담론 지형 분석 |")
    A(f"| `framework_incomplete` — 4차원 미충족 | {skipped['framework_incomplete']:,} | — |")
    A(f"| `ai_thin` — AI 연결 문장 {MIN_AI_LINKED_SENTS}개 미만(IR 실적발표 등) | "
      f"{skipped['ai_thin']:,} | — |")
    novalue = sum(1 for r in rows if r["case_role"] in USABLE_ROLES and r["usable"] != "Y")
    A(f"| 가치언어 게이트 미달(가치·수치 문장 < {MIN_VALUE_EVIDENCE}) 또는 초점 불명 | "
      f"{novalue:,} | 기술 도입 사실 확인용 |")
    A(f"| `ax_adjacent` / `off_topic` / `noise` | "
      f"{skipped['ax_adjacent']:,} / {skipped['off_topic']:,} / {skipped['noise']:,} | — |")
    A("")

    # ── 한계 ──
    A("## 10. 한계 (정직한 고지)")
    A("")
    A("1. **자기보고가 아니다.** 원 프레임워크는 조직 구성원 self-report + 퍼실리테이션 "
      "워크숍이다. 여기 점수는 공개 발화의 근거 밀도이며 조직의 실제 준비도가 아니다. "
      "논문으로 쓰려면 이 목록을 **케이스 선별·인터뷰 대상 선정**에 쓰고 점수는 "
      "워크숍/설문으로 다시 받아야 한다.")
    A("2. **규칙 기반**이라 반어·부정·가정법을 놓친다(\"목표가 없었다\"도 목표 차원에 잡힌다). "
      "시제 배정은 문장 내 마커에 의존하므로 자동자막의 문장 경계 오류에 취약하다.")
    A("3. **경계(boundaries) 차원 과대집계 위험** — 파트너십·조직개편 어휘는 벤더 발화에 흔하다. "
      "1급 케이스라도 경계 발췌는 눈으로 확인할 것.")
    A("4. **초점 조직 귀속은 언급 빈도 기반 추정**이다. 한 영상이 여러 기업을 다루면 "
      "최다 언급 기업이 초점이 된다 — `mentions` 열로 반드시 교차 확인.")
    A("5. **공개 담론 표본 편향**: 성공 서사가 과표집되고 실패·중단은 과소표집된다. "
      "논문의 보험사처럼 '목표 0점'인 조직은 유튜브에 나오지 않는다.")
    A("6. 수기 코딩 검증(표본 100~200건, Cohen's κ) 전에는 방법론적 방어가 불가하다.")
    A("")
    A("## 11. 재현")
    A("")
    A("```bash")
    A("python classify_v2.py      # relevance 게이트 갱신")
    A("python readiness_scan.py   # 본 문서 + CSV 2종 재생성")
    A("```")
    A("")
    A("- `analysis/ai_readiness_cases.csv` — 영상별 8셀 근거 수·잠정점수·역할·발췌·링크")
    A("- `analysis/ai_readiness_firms.csv` — 기업별 합산 스코어카드")

    os.makedirs("docs", exist_ok=True)
    with open(os.path.join("docs", "AI_READINESS_CASES.md"), "w", encoding="utf-8") as fp:
        fp.write("\n".join(L) + "\n")


def main():
    os.makedirs("analysis", exist_ok=True)
    rows, skipped, total = collect()
    firms = pool_by_firm(rows)
    write_csv(os.path.join("analysis", "ai_readiness_cases.csv"), rows)
    write_csv(os.path.join("analysis", "ai_readiness_firms.csv"), firms)
    write_md(rows, firms, skipped, total)

    usable = [r for r in rows if r["usable"] == "Y"]
    roles = collections.Counter(r["case_role"] for r in rows)
    tiers = collections.Counter(r["tier"] for r in usable)
    print(f"[readiness_scan] 스캔 {total:,}건 → 4차원 커버 {len(rows):,}건 / "
          f"사용가능 {len(usable):,}건 (A {tiers['A']} · B {tiers['B']} · C {tiers['C']}), "
          f"초점 기업 {len(firms):,}곳")
    print("  역할:", dict(roles))
    print("  제외:", dict(skipped))
    print("  차원별 충족률(현재/미래, 사용가능 기준):")
    n = max(len(usable), 1)
    for d in DIMENSIONS:
        cur = sum(1 for r in usable if r[f"n_{d}_cur"] > 0)
        fut = sum(1 for r in usable if r[f"n_{d}_fut"] > 0)
        print(f"    {DIM_LABEL[d]:<13} {100*cur/n:>3.0f}% / {100*fut/n:>3.0f}%")
    print("  → docs/AI_READINESS_CASES.md · analysis/ai_readiness_cases.csv · ai_readiness_firms.csv")


if __name__ == "__main__":
    main()
