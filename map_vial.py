"""
Vial(2019) DT 프레임워크 매퍼 — 코퍼스에서 '프레임워크에 맞는 사례'를 전량 탐색한다.

근거 문헌:
  Vial, G. (2019). Understanding digital transformation: A review and a research
  agenda. The Journal of Strategic Information Systems, 28(2), 118-144.

Vial의 귀납적 과정 모형 8개 구성요소(building blocks)를 그대로 코딩 축으로 삼아,
수집된 유튜브 스크립트 전량을 태깅한다.

  B1 tech        디지털 기술의 활용 (SMACIT + AI/LLM/에이전트)
  B2 disruption  파괴 — (a)소비자 행동·기대 (b)경쟁구도 (c)데이터 가용성
  B3 strategy    전략적 대응 — 디지털 비즈니스 전략 / DT 전략
  B4 value       가치창출 경로 변화 — 가치제안·가치네트워크·디지털채널·민첩성/양손잡이
  B5 structure   구조적 변화 — 조직구조·문화·리더십·직무/역량
  B6 barrier     장벽 — 관성·저항
  B7 positive    긍정 성과 — 운영효율·조직성과·사회적 편익
  B8 negative    부정 성과 — 보안·프라이버시

추가로 이 프로젝트(AX 연구)의 이론적 교량 3축을 함께 태깅한다:
  X1 bridge_means    '수단' 속성에 AI를 대입 — DX의 후속/심화로서의 AX 발화
  X2 bridge_ethics   Avenue 2 (윤리·거버넌스를 전략 변수로)
  X3 bridge_dyncap   Avenue 1 (동적역량: 감지-포착-재구성, 플랫폼·생태계, CDO/CAIO 미시기반)

출력:
  analysis/vial_cases.csv        — 구성요소 태깅 결과 전량(기계 판독용)
  analysis/vial_evidence.csv     — 구성요소별 근거 문장 발췌(코딩 감사용)
  docs/VIAL_CASES.md             — 사람이 읽는 사례 목록(티어·구성요소별)

직접 실행: python map_vial.py
※ classify_v2.py 와 같은 순수 규칙 기반(정규식) — 재현·감사 가능하고 가볍다.
"""

import collections
import csv
import glob
import os
import re

import config
from classify import parse_transcript, doc_month
from classify_v2 import classify_relevance, classify_stance


def rx(*pats):
    return [re.compile(p, re.IGNORECASE) for p in pats]


# ──────────────────────────────────────────────────────────────
# B1. 디지털 기술의 활용 (use of digital technologies)
#   Vial: SMACIT(소셜·모바일·애널리틱스·클라우드·IoT). 2019년 이후 맥락에서
#   LLM·에이전트를 '수단' 속성에 대입 → AX 확장 지점.
# ──────────────────────────────────────────────────────────────
B_TECH = rx(
    r"\bLLM\b", r"거대\s*언어\s*모델", r"large\s+language\s+model",
    r"생성형\s*AI", r"generative\s+AI", r"\bGenAI\b", r"\bGPT\b", r"ChatGPT",
    r"파운데이션\s*모델", r"foundation\s+model",
    r"AI\s*에이전트", r"AI\s+agent", r"\bagentic\b", r"에이전트\s*오케스트레이션",
    r"머신\s*러닝", r"machine\s+learning", r"딥\s*러닝", r"deep\s+learning",
    r"클라우드", r"\bcloud\b", r"\bSaaS\b", r"\bAPI\b",
    r"애널리틱스", r"analytics", r"빅데이터", r"big\s+data", r"데이터\s*(플랫폼|레이크|웨어하우스)",
    r"\bIoT\b", r"사물\s*인터넷", r"디지털\s*트윈", r"digital\s+twin",
    r"모바일\s*(앱|퍼스트)", r"소셜\s*미디어", r"social\s+media",
    r"자동화\s*(도구|플랫폼)", r"\bRPA\b", r"\bRAG\b", r"파인\s*튜닝", r"fine[-\s]?tun",
)

# ──────────────────────────────────────────────────────────────
# B2. 파괴(disruptions) — 3개 하위 차원
# ──────────────────────────────────────────────────────────────
B_DIS_CONSUMER = rx(
    r"고객\s*(기대|행동|경험|여정|요구)", r"소비자\s*(기대|행동|요구)",
    r"customer\s+(expectation|behavio|experience|journey|demand)",
    r"consumer\s+(expectation|behavio|demand)",
    r"사용자\s*경험", r"user\s+experience", r"\bUX\b",
    r"고객(이|들이)\s*(원|바라|요구)", r"customers?\s+(now\s+)?(expect|want|demand)",
    r"개인화", r"personaliz", r"고객\s*접점", r"touchpoint",
)
B_DIS_COMPETITION = rx(
    r"경쟁\s*(구도|환경|사|자|우위|심화)", r"competitive\s+(landscape|environment|advantage|pressure)",
    r"신규\s*(진입|진입자)", r"new\s+entrant", r"스타트업(이|에게)?\s*(위협|추격|잠식)",
    r"산업\s*(경계|구조)(가|의)?\s*(무너|붕괴|재편|변화)", r"blur(ring|red)?\s+(industry\s+)?boundar",
    r"파괴적\s*혁신", r"disrupt(ion|ive|ing|ed|s)?\b", r"디스럽", r"게임의\s*룰",
    r"플랫폼\s*(경쟁|기업|비즈니스)", r"platform\s+(competition|business|player)",
    r"승자\s*독식", r"winner[-\s]?takes?[-\s]?all", r"시장\s*(재편|판도)",
)
B_DIS_DATA = rx(
    r"데이터(가|의)?\s*(폭증|급증|넘쳐|쏟아|가용|활용\s*가능)",
    r"data\s+(availability|explosion|deluge|abundance)",
    r"데이터\s*(자산|확보|접근|개방)", r"proprietary\s+data", r"독점\s*데이터",
    r"비정형\s*데이터", r"unstructured\s+data", r"실시간\s*데이터", r"real[-\s]?time\s+data",
    r"데이터(를)?\s*(수집|축적)", r"데이터\s*(양|볼륨)", r"페타바이트|petabyte|zettabyte",
)

# ──────────────────────────────────────────────────────────────
# B3. 전략적 대응 (digital business strategy / DT strategy)
# ──────────────────────────────────────────────────────────────
B_STRATEGY = rx(
    r"디지털\s*(비즈니스)?\s*전략", r"digital\s+(business\s+)?strategy",
    r"AI\s*전략", r"\bAI\s+strategy\b", r"전환\s*전략", r"transformation\s+strategy",
    r"로드맵", r"roadmap", r"전사\s*(전략|차원|적용|도입)", r"enterprise[-\s]?wide",
    r"경영\s*(전략|진|계획)", r"비즈니스\s*모델(을|의)?\s*(전환|재설계|혁신|변화)",
    r"business\s+model\s+(change|innovation|transformation)",
    r"투자\s*(계획|우선순위|결정)", r"strategic\s+(priority|priorities|response|bet)",
    r"transformation\s+office", r"전환\s*(조직|추진단|TF)", r"중장기\s*계획",
    r"CEO(가|는|의)\s*(직접|주도|의지)", r"C[-\s]?(suite|level)", r"이사회", r"board\s+level",
)

# ──────────────────────────────────────────────────────────────
# B4. 가치창출 경로의 변화 (changes in value creation paths)
# ──────────────────────────────────────────────────────────────
B_VAL_PROPOSITION = rx(
    r"가치\s*제안", r"value\s+proposition", r"신규\s*(사업|서비스|수익원|제품)",
    r"new\s+(business|revenue)\s+(model|stream|line)", r"수익\s*모델", r"monetiz",
    r"제품(을|의)?\s*(재정의|고도화|지능화)", r"서비스화|servitization|as[-\s]a[-\s]service",
    r"구독\s*(모델|경제)", r"subscription\s+model", r"outcome[-\s]?based\s+pricing",
    r"AI\s*(기반|탑재|내장)\s*(제품|서비스|기능)", r"AI[-\s]?powered\s+(product|service|feature)",
    r"새로운\s*(가치|제품|서비스|경험)(를|을)?\s*(제공|만들|창출)",
    r"(제품|서비스)에\s*AI(를)?\s*(넣|탑재|적용|결합)", r"embed(ding)?\s+AI\s+into",
    r"기존\s*(제품|사업)(을|의)\s*(대체|잠식|전환)", r"프리미엄\s*(요금|가격)|premium\s+tier",
    r"가격\s*(정책|체계)(을|를)?\s*(바꾸|재설계)", r"pricing\s+model\s+(chang|shift)",
)
B_VAL_NETWORK = rx(
    r"가치\s*(사슬|네트워크)", r"value\s+(chain|network)", r"생태계", r"ecosystem",
    r"파트너(십|사)", r"partnership", r"공급망", r"supply\s+chain",
    r"협력사|협업\s*체계|얼라이언스|alliance|공동\s*(개발|창출)|co[-\s]?creat",
    r"아웃소싱|outsourc|벤더|vendor\s+(management|selection)",
)
B_VAL_CHANNEL = rx(
    r"디지털\s*채널", r"digital\s+channel", r"옴니\s*채널", r"omni[-\s]?channel",
    r"이커머스", r"e[-\s]?commerce", r"온라인\s*(판매|채널|전환)", r"D2C|다이렉트\s*채널",
    r"모바일\s*앱(을|으로)?\s*(통해|출시)", r"셀프\s*서비스", r"self[-\s]?service",
    r"챗봇(을|으로)?\s*(고객|상담|응대)", r"콜센터|컨택센터|contact\s+center|call\s+center",
)
B_VAL_AGILITY = rx(
    r"민첩(성|하게)", r"agility|agile\b", r"애자일", r"양손잡이|ambidext",
    r"빠른\s*(실험|시도|반복|출시)", r"rapid\s+(experiment|iterat|prototyp)",
    r"실험\s*(문화|조직)", r"experimentation", r"파일럿(을|에서)?\s*(빠르게|확산|스케일)",
    r"스케일업|scal(e|ing)\s+(up|out|across)", r"시간\s*단축|time[-\s]?to[-\s]?market",
    r"탐색과\s*활용|exploration\s+and\s+exploitation",
)

# ──────────────────────────────────────────────────────────────
# B5. 구조적 변화 (structural changes)
# ──────────────────────────────────────────────────────────────
B_STR_STRUCTURE = rx(
    r"조직\s*(구조|개편|설계|재편)", r"organizational\s+structure", r"reorganiz",
    r"전담\s*(조직|팀|부서)", r"dedicated\s+team", r"\bCoE\b|센터\s*오브\s*엑설런스|center\s+of\s+excellence",
    r"사일로", r"silo", r"부서\s*간\s*(협업|장벽)", r"cross[-\s]?functional",
    r"보고\s*체계|reporting\s+line", r"플랫폼\s*조직|중앙\s*(집중|플랫폼)",
)
B_STR_CULTURE = rx(
    r"조직\s*문화", r"organizational\s+culture", r"기업\s*문화", r"corporate\s+culture",
    r"문화(를|가)\s*(바꾸|바뀌|변화)", r"culture\s+change", r"마인드셋", r"mindset",
    r"실패(를)?\s*용인|psychological\s+safety|심리적\s*안전",
    r"데이터\s*(기반|중심)\s*(문화|의사결정)", r"data[-\s]?driven\s+culture",
    r"학습\s*(조직|문화)", r"learning\s+(organization|culture)",
)
B_STR_LEADERSHIP = rx(
    r"리더십", r"leadership", r"\bCDO\b|최고\s*디지털\s*책임자|chief\s+digital\s+officer",
    r"\bCAIO\b|최고\s*AI\s*책임자|chief\s+AI\s+officer", r"\bCIO\b|\bCTO\b|\bCDAO\b",
    r"경영진(의|이)\s*(의지|지원|역할|주도)", r"executive\s+(sponsor|buy[-\s]?in|commitment)",
    r"톱다운|top[-\s]?down\s+(mandate|push)", r"리더(가|의)\s*(바뀌|역할|책임)",
)
B_STR_ROLES = rx(
    r"직무(가|의|를)?\s*(변화|재설계|재편|사라)", r"job\s+(redesign|role|change)",
    r"역량\s*(강화|재교육|개발)", r"reskill|upskill|재교육|리스킬|업스킬",
    r"인재\s*(확보|영입|전쟁|육성)", r"talent\s+(war|acquisition|development)",
    r"채용|hiring|headcount|인력\s*(재배치|감축|구조조정)|layoff|정리해고",
    r"AI\s*(리터러시|교육)", r"AI\s+literacy", r"새로운\s*(직무|역할|직군)|new\s+role",
    r"데이터\s*(과학자|엔지니어)|data\s+(scientist|engineer)|프롬프트\s*엔지니어",
)

# ──────────────────────────────────────────────────────────────
# B6. 장벽 (organizational barriers) — 관성·저항
# ──────────────────────────────────────────────────────────────
B_BARRIER = rx(
    r"관성", r"inertia", r"저항", r"resistance|resist(ing)?\s+change",
    r"기존\s*(방식|관행)(을|에)\s*(고수|집착)", r"legacy\s+(system|mindset|process)",
    r"레거시", r"기술\s*부채", r"technical\s+debt",
    r"변화(를|에)\s*(거부|꺼|두려)", r"현업(의)?\s*(반발|불신|거부)",
    r"내부\s*(반발|정치|갈등)", r"internal\s+politics", r"not\s+invented\s+here",
    r"도입(이|에)\s*(실패|지연|막)", r"파일럿(에서)?\s*(멈|정체)", r"pilot\s+purgatory",
    r"규정(이|의)?\s*(발목|제약)", r"승인(이|을)\s*(오래|지연)", r"의사결정(이)?\s*(느|지연)",
    r"예산(이)?\s*(부족|없)", r"데이터(가)?\s*(흩어|파편|사일로|더럽|없)",
    r"skills?\s+gap|역량\s*(격차|부족)|인재\s*부족|talent\s+shortage",
)

# ──────────────────────────────────────────────────────────────
# B7. 긍정적 성과 (positive impacts)
# ──────────────────────────────────────────────────────────────
B_POS_OPERATIONAL = rx(
    r"운영\s*(효율|효율화|개선|최적화)", r"operational\s+efficien",
    r"생산성(이|을)?\s*(향상|증가|개선|\d)", r"productivity\s+(gain|improv|increas|boost)",
    r"비용(을|이)?\s*(절감|감소|줄)", r"cost\s+(saving|reduc|cut)",
    r"시간(을|이)?\s*(단축|절약|줄)", r"time\s+(saving|reduc)", r"\d+\s*%\s*(단축|절감|감소|향상|증가)",
    r"처리(량|속도)(이|가)?\s*(증가|향상)", r"throughput", r"불량(률)?\s*(감소|개선)",
    r"자동화(로|를\s*통해)\s*(절감|단축|효율)", r"\bROI\b|투자\s*수익",
)
B_POS_ORGPERF = rx(
    r"매출(이|을)?\s*(증가|성장|늘|\d)", r"revenue\s+(growth|increas|up)",
    r"이익(이|을)?\s*(증가|개선)", r"margin\s+(improv|expan)", r"수익성",
    r"시장\s*(점유율|지위)(이|가|를)?\s*(확대|상승)", r"market\s+share",
    r"경쟁\s*우위(를)?\s*(확보|강화)", r"competitive\s+advantage",
    r"고객\s*(만족|유지|이탈)(도|율)?", r"customer\s+(satisfaction|retention|churn)",
    r"기업\s*가치|valuation|주가(가)?\s*(상승|반영)",
)
B_POS_SOCIETY = rx(
    # 사회적 편익은 '조직 성과 밖의 수혜'를 말할 때만 인정 — 단어 하나로는 판정하지 않는다.
    r"사회적\s*(가치|편익|기여|임팩트)", r"societal\s+(benefit|impact|value|good)",
    r"공익|public\s+(good|benefit)", r"공공\s*(서비스|부문)(의)?\s*(개선|혁신|효율)",
    r"의료\s*(접근성|격차)", r"환자(의)?\s*(치료\s*결과|생존|안전)(이|을)?\s*(개선|향상)",
    r"patient\s+outcomes?\s+(improv|better)", r"신약\s*개발\s*(기간|비용)(을|이)\s*(단축|절감)",
    r"교육\s*격차(를)?\s*(줄|해소)", r"교육\s*기회(를)?\s*(확대|제공)",
    r"탄소\s*(배출|발자국)(을|이)\s*(감축|줄)", r"carbon\s+(emission|footprint)\s+(reduc|cut)",
    r"에너지\s*(소비|사용)(을|이)\s*(절감|감축)", r"기후\s*(변화)?\s*(대응|문제\s*해결)",
    r"장애인|접근성(을)?\s*(개선|높)|accessibility\s+for", r"디지털\s*(격차|포용)",
    r"재난|안전\s*사고(를)?\s*(예방|감소)", r"일자리(를)?\s*(창출|늘)",
)

# ──────────────────────────────────────────────────────────────
# B8. 부정적 성과 (negative impacts) — 보안·프라이버시(+확장: 편향·일자리)
# ──────────────────────────────────────────────────────────────
B_NEGATIVE = rx(
    # 'security' 단어 하나가 아니라 위험·사고·우려 문맥일 때만 부정 성과로 본다.
    r"보안\s*(위협|사고|우려|리스크|취약|문제|이슈|침해)", r"보안(을|이)\s*(뚫|취약)",
    r"security\s+(risk|breach|incident|concern|vulnerab|threat|issue)",
    r"해킹|hack(ed|ing|er)|사이버\s*(공격|위협)|cyber[-\s]?(attack|threat)",
    r"데이터\s*(유출|침해)", r"data\s+(breach|leak|exfiltrat)", r"정보(가)?\s*(유출|샜)",
    r"프라이버시|privacy|개인정보\s*(보호|유출|처리)",
    r"기밀\s*(정보|유출)|confidentiality", r"규제\s*(위반|리스크)|compliance\s+risk",
    r"편향|\bbias(ed)?\b|차별(?!화)|discriminat", r"할루시네이션|hallucinat",
    r"오작동|오류(가|를)?\s*(발생|많|낸)", r"부정확|inaccura|틀린\s*답",
    r"일자리(가|를)?\s*(사라|줄|위협|대체|잃)", r"job\s+(loss|displacement|cut)",
    r"저작권|copyright\s+(issue|infringe)|딥페이크|deepfake|오남용|misuse|악용",
    r"감시|surveillance", r"프롬프트\s*인젝션|prompt\s+injection|섀도우\s*AI|shadow\s+AI",
    r"신뢰(를)?\s*(잃|훼손)|reputational\s+(risk|damage)",
)

# ──────────────────────────────────────────────────────────────
# AX 연계 교량 3축
# ──────────────────────────────────────────────────────────────
X_MEANS = rx(  # DX → AX 계승/확장을 명시하는 발화 ('수단' 속성에 AI를 대입하는 지점)
    r"\bDX\b.{0,80}\bAX\b", r"\bAX\b.{0,80}\bDX\b",
    r"디지털\s*전환.{0,60}(AI|인공지능)\s*전환", r"(AI|인공지능)\s*전환.{0,60}디지털\s*전환",
    r"digital\s+transformation.{0,80}AI\s+transformation",
    r"AI\s+transformation.{0,80}digital\s+transformation",
    r"디지털\s*전환(의|을)?\s*(다음|연장|심화|후속|넘어|이어)",
    r"next\s+(phase|wave|step|chapter|era)\s+of\s+digital",
    r"beyond\s+digital\s+transformation",
    r"클라우드\s*전환.{0,60}(AI|인공지능)", r"DT\s*(의)?\s*(연장|확장|다음)",
    r"(디지털화|디지타이제이션).{0,60}(AI|지능화)", r"지능화(로|의)\s*(전환|단계|진화)",
)
# 명시 문구가 없어도 DX 어휘와 AX 어휘가 함께 등장하면 '정의 확장' 후보로 본다.
X_MEANS_DX = rx(
    r"\bDX\b", r"디지털\s*전환", r"디지털\s*트랜스포메이션", r"digital\s+transformation",
    r"디지털화|digitali[sz]ation|digiti[sz]ation", r"클라우드\s*(전환|마이그레이션)",
    r"레거시\s*(시스템|전환)|legacy\s+system|\bERP\b|시스템\s*현대화|modernizat",
)
X_MEANS_AX = rx(
    r"\bAX\b", r"(AI|인공지능)\s*전환", r"AI\s+transformation",
    r"(AI|인공지능)\s*(도입|적용)|AI\s+adoption", r"생성형\s*AI|generative\s+AI",
    r"AI\s*에이전트|AI\s+agent|agentic",
)
X_ETHICS = rx(  # Avenue 2 — 윤리를 전략 변수로
    r"\bAI\s*윤리\b|AI\s+ethics|윤리(적)?\s*(문제|기준|원칙|가이드)",
    r"책임\s*있는\s*AI|responsible\s+AI|신뢰할\s*수\s*있는\s*AI|trustworthy\s+AI",
    r"거버넌스|governance", r"규제|regulat|\bEU\s*AI\s*Act\b|AI\s*기본법",
    r"감사(를|가)?\s*(가능|추적)|audit(able|ability|ing)?\b|추적성|traceab",
    r"설명\s*가능(성)?|explainab|투명성|transparency",
    r"가드레일|guardrail|정책\s*(수립|준수)|compliance",
    r"이해관계자|stakeholder", r"human[-\s]?in[-\s]?the[-\s]?loop|사람(의)?\s*(검토|승인|개입)",
)
X_DYNCAP = rx(  # Avenue 1 — 동적역량(감지-포착-재구성), 플랫폼·생태계, CDO 미시기반
    r"동적\s*역량|dynamic\s+capabilit", r"감지|sens(e|ing)\b", r"포착|seiz(e|ing)",
    r"재구성|reconfigur|재배치|재설계", r"조직\s*역량(을|의)\s*(구축|재편|축적)",
    r"역량\s*(내재화|축적|체화)|capability\s+building|in[-\s]?house\s+capabilit",
    r"플랫폼\s*(전략|역량|생태계)|platform\s+(strategy|capability|ecosystem)",
    r"\bCDO\b|\bCAIO\b|최고\s*(디지털|AI)\s*책임자|transformation\s+(lead|office)",
    r"전략\s*실행|strategy\s+as\s+practice|현장(에서)?\s*(실행|적용)",
    r"학습\s*(곡선|루프)|feedback\s+loop|피드백\s*루프|지속(적)?\s*(개선|학습)",
)

CONSTRUCTS = [
    # (키, 블록, 라벨, 패턴)
    ("tech",            "B1", "디지털·AI 기술의 활용",       B_TECH),
    ("dis_consumer",    "B2", "파괴: 소비자 행동·기대",      B_DIS_CONSUMER),
    ("dis_competition", "B2", "파괴: 경쟁구도",              B_DIS_COMPETITION),
    ("dis_data",        "B2", "파괴: 데이터 가용성",         B_DIS_DATA),
    ("strategy",        "B3", "전략적 대응",                 B_STRATEGY),
    ("val_proposition", "B4", "가치제안 변화",               B_VAL_PROPOSITION),
    ("val_network",     "B4", "가치네트워크·생태계",         B_VAL_NETWORK),
    ("val_channel",     "B4", "디지털 채널",                 B_VAL_CHANNEL),
    ("val_agility",     "B4", "민첩성·양손잡이",             B_VAL_AGILITY),
    ("str_structure",   "B5", "조직구조 변화",               B_STR_STRUCTURE),
    ("str_culture",     "B5", "조직문화 변화",               B_STR_CULTURE),
    ("str_leadership",  "B5", "리더십·CDO/CAIO",             B_STR_LEADERSHIP),
    ("str_roles",       "B5", "직무·역량 변화",              B_STR_ROLES),
    ("barrier",         "B6", "장벽: 관성·저항",             B_BARRIER),
    ("pos_operational", "B7", "성과: 운영효율",              B_POS_OPERATIONAL),
    ("pos_orgperf",     "B7", "성과: 조직성과",              B_POS_ORGPERF),
    ("pos_society",     "B7", "성과: 사회적 편익",           B_POS_SOCIETY),
    ("negative",        "B8", "부정 성과: 보안·프라이버시",  B_NEGATIVE),
]

BRIDGES = [
    ("bridge_means",  "X1", "정의 확장(DX→AX 계승)", X_MEANS),
    ("bridge_ethics", "X2", "Avenue 2 윤리·거버넌스", X_ETHICS),
    ("bridge_dyncap", "X3", "Avenue 1 동적역량",      X_DYNCAP),
]

BLOCK_LABEL = {
    "B1": "B1 디지털 기술의 활용",
    "B2": "B2 파괴(disruption)",
    "B3": "B3 전략적 대응",
    "B4": "B4 가치창출 경로 변화",
    "B5": "B5 구조적 변화",
    "B6": "B6 장벽",
    "B7": "B7 긍정적 성과",
    "B8": "B8 부정적 성과",
}

# 구성요소 '존재' 판정 기준: 최소 등장 횟수 (희소 어휘 오탐 억제)
MIN_HITS = 2
# 사례로 채택할 최소 조건
MIN_BLOCKS_CASE = 4          # 8개 블록 중 최소 몇 개를 다뤄야 '사례'로 볼지
MIN_WORDS = 200              # 너무 짧은 자막은 사례로 보지 않음
EVIDENCE_MAX_LEN = 220


def count(patterns, text):
    return sum(len(p.findall(text)) for p in patterns)


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|(?<=다\.)\s*|(?<=요\.)\s*|(?<=죠\.)\s*", text)
    return [p.strip() for p in parts if p and len(p.strip()) >= 15]


def first_evidence(patterns, sentences):
    """구성요소를 대표하는 근거 문장 1개를 고른다(패턴 적중 수가 가장 많은 문장)."""
    best, best_n = "", 0
    for sent in sentences:
        n = sum(1 for p in patterns if p.search(sent))
        if n > best_n:
            best, best_n = sent, n
            if n >= 3:
                break
    if len(best) > EVIDENCE_MAX_LEN:
        best = best[:EVIDENCE_MAX_LEN] + "…"
    return best


def tier_of(n_blocks, has_impact, has_strategy):
    """Vial 과정 모형의 사슬 충족도로 티어를 매긴다.

    A: 기술→파괴/전략→가치·구조→성과 사슬이 온전(블록 7개 이상 + 전략 + 성과)
    B: 블록 6개 이상 (사슬 대부분)
    C: 블록 4~5개 (부분 사례)
    """
    if n_blocks >= 7 and has_impact and has_strategy:
        return "A"
    if n_blocks >= 6:
        return "B"
    if n_blocks >= MIN_BLOCKS_CASE:
        return "C"
    return ""


def analyze(path):
    meta, text = parse_transcript(path)
    words = len(text.split())
    rel = classify_relevance(text, words)
    sentences = split_sentences(text)

    counts, present, evid = {}, {}, {}
    for key, _blk, _label, pats in CONSTRUCTS + BRIDGES:
        c = count(pats, text)
        counts[key] = c
        present[key] = 1 if c >= MIN_HITS else 0
        if present[key]:
            evid[key] = first_evidence(pats, sentences)

    # X1(정의 확장)은 복합 규칙: 명시 문구 1회 이상, 또는 DX 어휘·AX 어휘 동시 등장.
    dx_n, ax_n = count(X_MEANS_DX, text), count(X_MEANS_AX, text)
    explicit = counts["bridge_means"]
    counts["bridge_means"] = explicit * 3 + min(dx_n, ax_n)
    present["bridge_means"] = 1 if (explicit >= 1 or (dx_n >= 2 and ax_n >= 2)) else 0
    if present["bridge_means"] and "bridge_means" not in evid:
        evid["bridge_means"] = first_evidence(X_MEANS + X_MEANS_DX, sentences)

    blocks = set()
    for key, blk, _label, _pats in CONSTRUCTS:
        if present[key]:
            blocks.add(blk)
    n_blocks = len(blocks)
    has_impact = ("B7" in blocks) or ("B8" in blocks)
    has_strategy = "B3" in blocks

    tier = tier_of(n_blocks, has_impact, has_strategy) if words >= MIN_WORDS else ""

    source = "channel" if f"{os.sep}channels{os.sep}" in path else "keyword"
    row = {
        "file": path.replace(os.sep, "/"),
        "title": meta["title"],
        "channel": meta["channel"] or "(미상)",
        "url": meta["url"],
        "upload_date": meta.get("upload_date", ""),
        "month": doc_month(path, meta),
        "lang": meta["lang"],
        "source": source,
        "words": words,
        "relevance": rel,
        "stance": classify_stance(text) if rel in ("ax_core", "ax_adjacent") else "neutral",
        "vial_blocks": n_blocks,
        "vial_block_list": "·".join(sorted(blocks)),
        "tier": tier,
    }
    for key, _blk, _label, _pats in CONSTRUCTS + BRIDGES:
        row[key] = present[key]
        row[f"{key}_n"] = counts[key]
    row["bridge_means_explicit"] = explicit   # DX→AX 계승을 명시한 발화 횟수
    return row, evid


def main():
    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows, evidence_rows = [], []
    for path in files:
        row, evid = analyze(path)
        rows.append(row)
        if row["tier"]:
            for key, blk, label, _pats in CONSTRUCTS + BRIDGES:
                if key in evid and evid[key]:
                    evidence_rows.append({
                        "file": row["file"], "channel": row["channel"], "title": row["title"],
                        "block": blk, "construct": key, "construct_label": label,
                        "hits": row[f"{key}_n"], "evidence": evid[key], "url": row["url"],
                    })

    os.makedirs("analysis", exist_ok=True)
    with open("analysis/vial_cases.csv", "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open("analysis/vial_evidence.csv", "w", encoding="utf-8-sig", newline="") as fp:
        fields = ["file", "channel", "title", "block", "construct", "construct_label",
                  "hits", "evidence", "url"]
        w = csv.DictWriter(fp, fieldnames=fields)
        w.writeheader()
        w.writerows(evidence_rows)

    write_md(rows, evidence_rows)

    cases = [r for r in rows if r["tier"]]
    print(f"[map_vial] 전체 {len(rows)}건 → 사례 {len(cases)}건 "
          f"(A {sum(1 for r in cases if r['tier']=='A')} / "
          f"B {sum(1 for r in cases if r['tier']=='B')} / "
          f"C {sum(1 for r in cases if r['tier']=='C')})")
    for key, _blk, label, _pats in CONSTRUCTS + BRIDGES:
        n = sum(r[key] for r in rows)
        nc = sum(r[key] for r in cases)
        print(f"  {label:28s} 전체 {n:5d} / 사례 {nc:5d}")


def _fmt_row(r):
    return (f"| [{r['title'][:60]}]({r['url']}) | {r['channel'][:24]} | {r['month']} | "
            f"{r['vial_blocks']} | {r['vial_block_list']} | {r['relevance']}/{r['stance']} |")


def write_md(rows, evidence_rows):
    os.makedirs("docs", exist_ok=True)
    cases = sorted([r for r in rows if r["tier"]],
                   key=lambda r: (-r["vial_blocks"], r["channel"], r["title"]))
    core_cases = [r for r in cases if r["relevance"] == "ax_core"]
    ev_by_file = collections.defaultdict(list)
    for e in evidence_rows:
        ev_by_file[e["file"]].append(e)

    out = []
    out.append("# Vial(2019) DT 프레임워크 대응 사례 목록\n")
    out.append("> 자동 생성: `python map_vial.py` · 근거 문헌: Vial, G. (2019). "
               "Understanding digital transformation: A review and a research agenda. "
               "*JSIS, 28*(2), 118–144.\n")
    out.append(f"> 코퍼스 {len(rows):,}건 전량을 8개 구성요소(B1–B8) + AX 교량 3축(X1–X3)으로 "
               f"규칙 기반 태깅 → **사례 {len(cases):,}건**(그 중 연구 주표본 ax_core "
               f"{len(core_cases):,}건).\n")
    out.append("> 기계 판독본: `analysis/vial_cases.csv`(태깅 전량) · "
               "`analysis/vial_evidence.csv`(구성요소별 근거 문장).\n")

    out.append("\n---\n\n## 1. 코딩 규칙\n")
    out.append("| 축 | 구성요소 | 판정 |\n|---|---|---|")
    for key, blk, label, _p in CONSTRUCTS:
        out.append(f"| {blk} | {label} | 사전 적중 ≥{MIN_HITS}회 |")
    for key, blk, label, _p in BRIDGES:
        rule = ("명시 문구 1회 이상, 또는 DX 어휘 ≥2 & AX 어휘 ≥2 동시 등장(복합 규칙)"
                if key == "bridge_means" else f"사전 적중 ≥{MIN_HITS}회")
        out.append(f"| {blk} | {label} | {rule} |")
    out.append("")
    out.append(f"- **사례(case) 채택**: 본문 {MIN_WORDS}단어 이상 & 8개 블록 중 "
               f"{MIN_BLOCKS_CASE}개 이상 충족.\n"
               "- **티어**: A = 블록 7개 이상 + 전략(B3) + 성과(B7/B8) → Vial 과정 사슬이 온전한 사례 · "
               "B = 블록 6개 · C = 블록 4~5개(부분 사례).\n"
               "- 규칙 기반이라 문맥·반어를 완벽히 잡지 못한다(코드북 v2와 동일한 한계). "
               "티어 A/B는 수기 검증 대상 후보 목록으로 쓰는 것이 정직하다.\n")

    # 2. 분포
    out.append("\n---\n\n## 2. 구성요소별 출현 분포\n")
    out.append("| 축 | 구성요소 | 전체 코퍼스 | 사례 내 | 사례 내 비율 |\n|---|---|---:|---:|---:|")
    n_case = max(len(cases), 1)
    for key, blk, label, _p in CONSTRUCTS + BRIDGES:
        n_all = sum(r[key] for r in rows)
        n_c = sum(r[key] for r in cases)
        out.append(f"| {blk} | {label} | {n_all:,} | {n_c:,} | {100*n_c/n_case:.0f}% |")

    out.append("\n### 티어 분포\n")
    tc = collections.Counter(r["tier"] for r in cases)
    out.append("| 티어 | 건수 | ax_core |\n|---|---:|---:|")
    for t in ("A", "B", "C"):
        out.append(f"| {t} | {tc.get(t,0):,} | "
                   f"{sum(1 for r in cases if r['tier']==t and r['relevance']=='ax_core'):,} |")

    out.append("\n### 채널(기업)별 사례 수 상위 40\n")
    ch = collections.Counter(r["channel"] for r in cases)
    out.append("| 채널 | 사례 | A | ax_core |\n|---|---:|---:|---:|")
    for name, n in ch.most_common(40):
        a = sum(1 for r in cases if r["channel"] == name and r["tier"] == "A")
        c = sum(1 for r in cases if r["channel"] == name and r["relevance"] == "ax_core")
        out.append(f"| {name[:34]} | {n} | {a} | {c} |")

    # 3. 티어 A 전량 (근거 포함)
    tier_a = [r for r in cases if r["tier"] == "A"]
    out.append(f"\n---\n\n## 3. 티어 A — 과정 사슬이 온전한 사례 ({len(tier_a):,}건, 전량)\n")
    out.append("> 기술 활용 → 파괴/전략 → 가치·구조 변화 → 성과까지 한 영상 안에서 이어지는 사례. "
               "Vial의 Fig. 1 과정 모형을 그대로 대입해 읽을 수 있다.\n")
    for r in sorted(tier_a, key=lambda r: (r["channel"], -r["vial_blocks"])):
        out.append(f"\n### {r['title'][:90]}\n")
        out.append(f"- 채널: **{r['channel']}** · {r['month']} · {r['lang']} · "
                   f"{r['words']:,}단어 · {r['relevance']}/{r['stance']}")
        out.append(f"- 블록 {r['vial_blocks']}/8: {r['vial_block_list']}")
        br = [lbl for k, _b, lbl, _p in BRIDGES if r[k]]
        out.append(f"- AX 교량: {' · '.join(br) if br else '—'}")
        out.append(f"- 링크: {r['url']} · 원문: `{r['file']}`")
        ev = ev_by_file.get(r["file"], [])
        if ev:
            out.append("\n| 구성요소 | 근거 문장(발췌) |\n|---|---|")
            for e in ev:
                if e["construct"].startswith("bridge_"):
                    continue
                txt = e["evidence"].replace("|", "/").replace("\n", " ")
                out.append(f"| {e['block']} {e['construct_label']} | {txt} |")

    # 4. 티어 B 전량 (목록)
    tier_b = [r for r in cases if r["tier"] == "B"]
    out.append(f"\n---\n\n## 4. 티어 B — 사슬 대부분 충족 ({len(tier_b):,}건, 전량)\n")
    out.append("| 제목 | 채널 | 월 | 블록수 | 블록 | 관련성/톤 |\n|---|---|---|---:|---|---|")
    for r in sorted(tier_b, key=lambda r: (r["channel"], r["month"])):
        out.append(_fmt_row(r))

    # 5. 구성요소별 대표 사례
    out.append("\n---\n\n## 5. 구성요소별 대표 사례 (적중 상위 15)\n")
    out.append("> 특정 구성요소를 집중적으로 다루는 사례. 개별 구성요소 심층 코딩의 출발점.\n")
    for key, blk, label, _p in CONSTRUCTS:
        sub = sorted([r for r in cases if r[key]], key=lambda r: -r[f"{key}_n"])[:15]
        out.append(f"\n### {blk} · {label} (사례 {sum(1 for r in cases if r[key]):,}건)\n")
        out.append("| 제목 | 채널 | 월 | 적중 | 블록수 |\n|---|---|---|---:|---:|")
        for r in sub:
            out.append(f"| [{r['title'][:58]}]({r['url']}) | {r['channel'][:22]} | "
                       f"{r['month']} | {r[f'{key}_n']} | {r['vial_blocks']} |")

    # 6. AX 교량축
    out.append("\n---\n\n## 6. AX 연계 교량축 사례\n")
    for key, blk, label, _p in BRIDGES:
        sub = sorted([r for r in cases if r[key]], key=lambda r: -r[f"{key}_n"])
        out.append(f"\n### {blk} · {label} (사례 {len(sub):,}건 · 상위 30)\n")
        out.append("| 제목 | 채널 | 월 | 적중 | 블록수 | 관련성 |\n|---|---|---|---:|---:|---|")
        for r in sub[:30]:
            out.append(f"| [{r['title'][:56]}]({r['url']}) | {r['channel'][:22]} | {r['month']} | "
                       f"{r[f'{key}_n']} | {r['vial_blocks']} | {r['relevance']} |")

    # 6-b. X1 명시 발화 전량 — 티어와 무관하게(사례 기준 미달이어도) 이론적으로 가장 값진 지점
    explicit = sorted([r for r in rows if int(r["bridge_means_explicit"]) > 0],
                      key=lambda r: -int(r["bridge_means_explicit"]))
    out.append(f"\n### X1-a · DX→AX 계승을 **명시한** 발화 전량 ({len(explicit):,}건, 티어 무관)\n")
    out.append("> \"디지털 전환 다음은 AI 전환\"처럼 두 전환을 한 문장 안에서 잇는 발화. "
               "Vial의 정의에서 '수단(means)' 속성에 AI를 대입하는 이론적 지점이라, "
               "블록 수가 적어 사례 기준(4블록)에 못 미쳐도 별도로 전량 남긴다.\n")
    out.append("| 제목 | 채널 | 월 | 명시 횟수 | 티어 | 블록수 | 관련성 |\n|---|---|---|---:|---|---:|---|")
    for r in explicit:
        out.append(f"| [{r['title'][:56]}]({r['url']}) | {r['channel'][:22]} | {r['month']} | "
                   f"{r['bridge_means_explicit']} | {r['tier'] or '—'} | {r['vial_blocks']} | "
                   f"{r['relevance']} |")

    # 7. 티어 C 전량 (압축 목록)
    tier_c = [r for r in cases if r["tier"] == "C"]
    out.append(f"\n---\n\n## 7. 티어 C — 부분 사례 ({len(tier_c):,}건, 전량)\n")
    out.append("> 블록 4~5개만 충족. 단일 구성요소 분석·보조 표본용.\n")
    out.append("<details><summary>목록 펼치기</summary>\n")
    out.append("\n| 제목 | 채널 | 월 | 블록수 | 블록 | 관련성/톤 |\n|---|---|---|---:|---|---|")
    for r in sorted(tier_c, key=lambda r: (r["channel"], r["month"])):
        out.append(_fmt_row(r))
    out.append("\n</details>\n")

    with open("docs/VIAL_CASES.md", "w", encoding="utf-8") as fp:
        fp.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
