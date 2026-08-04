# 자동화·증강 양축 사례 — 전체 서술 (통합본)

> Raisch & Krakowski (2021), *AMR* 46(1): 192–210 의 구성개념으로 코딩한 사례 부록 통합본.
> 근거는 본 저장소가 수집한 유튜브 스크립트 **9,409건 중 44개 소스**이며 외부 검색은 쓰지 않았다.
> 개별 파일: `docs/cases/*.md` · 색인·방법·정정: `docs/PARADOX_CASES_IN_CORPUS.md`


## 목차

- [제1부 · 방법과 정정](#제1부--방법과-정정)
- [제2부 · 사례 1 — R1 RCM × Palantir : 의료 코딩](#사례-1-r1-rcm-palantir-의료-코딩)
- [제2부 · 사례 2 — ServiceNow : 자사 IT/CS 서비스데스크 (dogfooding)](#사례-2-servicenow-자사-it-cs-서비스데스크-dogfooding)
- [제2부 · 사례 3 — Zapier 회계·재무팀](#사례-3-zapier-회계-재무팀)
- [제2부 · 사례 3B — Zapier : 전사 AI 전환·거버넌스·측정](#사례-3b-zapier-전사-ai-전환-거버넌스-측정)
- [제2부 · 사례 4–5 — 삼성SDS 계열 : 우리은행 전 업무 재설계 + 삼성전자 VOC 분류](#사례-4-5-삼성sds-계열-우리은행-전-업무-재설계-삼성전자-voc-분류)
- [제2부 · 사례 6 — TK Elevator × Databricks : 보고 자동화 → 현장 기술자 증강](#사례-6-tk-elevator-databricks-보고-자동화-현장-기술자-증강)
- [제2부 · 사례 7 — Deloitte : 송장 92% 자동화 + 영업 에이전트](#사례-7-deloitte-송장-92-자동화-영업-에이전트)
- [제2부 · 사례 8 — Nokia : 제로터치 네트워크 + NOC 전문가](#사례-8-nokia-제로터치-네트워크-noc-전문가)
- [제2부 · 사례 9 — Siemens : 소프트웨어 정의 자동화 + 엔지니어링 코파일럿](#사례-9-siemens-소프트웨어-정의-자동화-엔지니어링-코파일럿)
- [제2부 · 사례 10 — McKinsey : GBS·서비스운영·뱅킹 진단 시리즈](#사례-10-mckinsey-gbs-서비스운영-뱅킹-진단-시리즈)
- [제3부 · 종합](#제3부--종합)


---

# 제1부 · 방법과 정정

## 0. 이 개정판에서 무엇이 달라졌나

초판은 사례당 소스 1건씩만 읽고 작성했다. 이번에는 사례별로 **관련 소스를 전수 탐색해 총 44개
스크립트를 정독**하고 교차 대조했다. 그 결과 **초판의 사실 주장 여러 건이 틀렸거나 과대**였음이
드러났다. 정정 내역을 먼저 밝힌다.

| # | 초판 서술 | 정정 |
|---|---|---|
| 1 | "Zapier 회계팀 **8명**이 **$5B** 규모 운영" | **본문에 근거 없음.** 두 수치는 **영상 제목에만** 존재한다. 팀 규모 질문에 CFO는 인원수를 말하지 않고 역할만 열거한다 — "저희 회사에는 재무 관리자 한 분과 다른 회계 담당자 몇 분이 계십니다". 매출 규모도 "우리가 큰 규모의 사업을 운영하고 있기 때문"이라고만 한다. → **제목 마케팅 문구로 표기하고 본문 사실로 인용하지 말 것** |
| 2 | Zapier의 "자동화 / 증강 / 고유하게 인간적인 요소" 3분할 프레임 | **Zapier 발화가 아니다.** 해당 영상에 게스트로 나온 **Glean 측 발화**이며, Zapier AI Workflow Index가 산출한 것은 "네 가지 일"(커뮤니케이터·사무보조·분석가·조정자)과 별도 수치다 |
| 3 | "Nokia의 TM Forum 자동화 4단계 = 시간축 순환의 **산업 표준 제도화**" | **과대 서술.** TM Forum 언급은 [S1] 제품 영상 **1문장뿐**이고, 나머지 6개 Nokia 소스에서 레벨 정의도 레벨별 인간 역할도 **전혀 나오지 않는다** |
| 4 | Nokia 성과 6개 수치를 사례 근거로 제시 | **단일 출처.** 2026-04~06의 다른 6개 Nokia 영상 어디에서도 재확인되지 않으며, 특정 제품/고객사가 아니라 "AI 기반 관리형 서비스 포트폴리오" 전체에 귀속된 집합적 주장이다 |
| 5 | "Siemens: AI 코파일럿이 엔지니어링 생산성 **30~40%** 향상" | 수치 자체는 [S1]에 실재하나 **다른 5개 소스에서 재확인되지 않는다.** 대신 지칭 대상이 다른 수치들이 나온다 — 개발 중 어시스턴트 "up to forty percent", Eigen 엔지니어링 에이전트 50%/2.5배/80%. 코파일럿→어시스턴트→에이전트로 **지시 대상이 이동**한다 |
| 6 | "우리은행 **29개** 핵심업무 **175개** 에이전트" | **판본마다 다르다.** 같은 발표자의 세 발표에서 핵심업무 **29개 / 27개 / 미명시**, 에이전트 **175개 → "175개가 아니라 최소 300개 그 이상"**으로 상향, 선언 주체 **"은행장께서" / "대표님께서"**, 완료 목표 **"올해 연말 내년 상반기까지 두 차례" / "내년 하반기까지"**로 엇갈린다 |
| 7 | "ServiceNow IT 요청 90% AI 처리" | 값은 유지되나 **술어가 강해진다.** 2025-11-17 "AI를 통해 처리됩니다" → 2026-05-07 "서비스 요청의 **91%**는 **AI의 지원을 받습니다**" → 2026-05-08 "IT 지원 요청의 90%가 **자율적으로 처리됩니다**". 하루 간격으로 값은 1%p 내려가고 자율성 주장은 올라간다 |
| 8 | "ServiceNow: 지원 인력 85% 재배치 = UBS 재투자 패턴" | **단일 출처·단일 시점.** 6개월 뒤 두 대형 키노트에서 재확인되지 않는다. 게다가 자막이 "더 가치 있는 **음악 관련** 업무에 재배치"로 붕괴되어 **재배치 목적지를 판독할 수 없다** |
| 9 | "Deloitte 송장 92% 자동화" | 수치는 실재하나 **주체가 Deloitte 자사인지 고객사인지 소스만으로 판정 불가** |
| 10 | R1 RCM을 SPILL 사례로 분류하지 않음 | 유지하되 근거 보강 — R1은 순차적 파급을 **명시적으로 부정**한다("task-based automations or siloed approaches"가 잘못이었다는 자기비판). 논문 SPILL의 **잠재적 반증** 방향 |

> 초판 대비 사례 구성도 바뀌었다. Intel 사례는 **Deloitte 사례로 귀속 정정**(초판 3차 커밋에서 이미
> 반영), Zapier는 재무편/전사편으로 분리, 삼성SDS 계열은 우리은행·삼성전자를 한 문서로 통합했다.

---

## 1. 코딩 기준

| 코드 | 논문 근거 | 조작적 정의 |
|---|---|---|
| **AUTO** | p.194 | 기계가 과업을 인계, 인간을 루프에서 제외 |
| **AUG** | p.194 | 인간이 루프에 남아 기계와 밀착 협업 |
| **CYCLE** | p.196–197 | 증강 학습 → 견고화 → 자동화, 또는 조건 변화 시 증강 회귀 |
| **SPILL** | p.197 | 한 과업의 자동화가 인접 과업의 증강을 유발 |
| **REINV** | p.201 (UBS) | 자동화로 확보한 자원을 증강에 재투자 |
| **RESP** | p.200 | 인간이 프로세스 전체 책임·승인·감사를 보유 |

보조 대조축: p.195(암묵지 위임 불가), p.198(기계 한계 4가지), p.199(편중 악순환),
p.204(기계 = 새로운 행위자 계급).

## 2. 방법

1. **소스 전수 탐색** — 사례 주체별 정규식으로 9,409건을 훑어 후보를 뽑고, 자동화·증강 신호
   밀도로 걸러 사례당 1~10개 소스를 확정. 총 **44개 스크립트**.
2. **전문 정독** — 사례별로 에이전트 1인이 지정 소스를 **끝까지** 읽고(장문은 청크 분할)
   11개 절 구조로 서술. grep 요약 의존 금지, 외부 지식 삽입 금지.
3. **인용 원문 보존** — 기계번역 자막의 오탈자·붕괴 표기를 교정하지 않고 그대로 인용
   ("휴먼 인더브로", "Netswuite", "디오이트", "음악 관련 업무", "체포" 등).
4. **기계 대조 검증** — 인용문을 원 파일과 문자열 단위로 대조. 사례별 검증 규모는
   R1 307건 / ServiceNow 140여 건 / Zapier 재무 130여 건 / Zapier 전사 140여 건 /
   TK Elevator 118건 / Nokia 232건 / Siemens 395건 등.
5. **핵심 수치 독립 재검증** — 종합에 쓰인 수치는 별도 스크립트로 코퍼스 전체 대조
   (§0의 정정 10건이 여기서 나왔다).

재현: `scan_paradox.py`(6축 코딩 → `analysis/paradox_scan.csv`), `cooc.py`(창 동시출현 추출).

## 3. 사례 색인

| 문서 | 사례 | 소스 수 | 시점 범위 | 1차 근거 성격 |
|---|---|---|---|---|
| [`cases/01_r1rcm.md`](cases/01_r1rcm.md) | R1 RCM × Palantir (의료 코딩) | 2 | 2025-03-18 ~ 06-10 | 벤더 컨퍼런스 고객 발표 |
| [`cases/02_servicenow.md`](cases/02_servicenow.md) | ServiceNow 자사 IT/CS | 5 | 2025-09-24 ~ 2026-05-08 | 자사 dogfooding + 키노트 |
| [`cases/03a_zapier_finance.md`](cases/03a_zapier_finance.md) | Zapier 회계·재무 | 4 | 2025-11-14 ~ 2026-05-20 | 자사 웨비나 (데모 포함) |
| [`cases/03b_zapier_enterprise.md`](cases/03b_zapier_enterprise.md) | Zapier 전사 전환·거버넌스·측정 | 5 | 2025-09-26 ~ 2026-07-29 | 자사 웨비나 + 자체 인덱스 |
| [`cases/04_samsungsds.md`](cases/04_samsungsds.md) | 우리은행 + 삼성전자 VOC × 삼성SDS | 5 | 수집일 2026-07-18 ~ 07-26 | 벤더 발표 (동일 발표 3판본) |
| [`cases/05_tkelevator.md`](cases/05_tkelevator.md) | TK Elevator × Databricks | 3 | 2026-01-27 ~ 06-23 | 벤더 고객 인터뷰 |
| [`cases/06_deloitte.md`](cases/06_deloitte.md) | Deloitte (Intel 팟캐스트) | 3 | 2025-10-15 ~ 2026-06-18 | 컨설팅사 발화 |
| [`cases/07_nokia.md`](cases/07_nokia.md) | Nokia 관리형 서비스 + DT | 7 | 2026-04-17 ~ 06-22 | 벤더 제품·패널 |
| [`cases/08_siemens.md`](cases/08_siemens.md) | Siemens 산업 AI | 6 | 2026-02-07 ~ 07-17 | 벤더 키노트·대담 |
| [`cases/09_mckinsey.md`](cases/09_mckinsey.md) | McKinsey 운영 시리즈 | 5 | 2025-08-30 ~ 2026-08-03 | 컨설팅사 팟캐스트 |

**시점 표기 규칙.** `transcripts/channels/…` 수집분은 헤더의 **업로드일**이 영상 공개 시점이다.
`transcripts/YYYY-MM-DD/…` 수집분(사례 4)은 업로드일 메타가 없어 **폴더명이 수집일**이며
업로드 시점은 불명이다. 어느 경우든 **업로드일 ≠ 발화일**이다(사례 8의 [S2]는 발화 시점이
업로드일보다 2개월 이상 앞선 것으로 보인다).

## 4. 구성개념별 근거 밀도

✅ 강한 근거 · ◐ 부분/약함 · ✗ 소스에 없음(미관측)

| 사례 | AUTO | AUG | CYCLE→ | CYCLE회귀 | SPILL | REINV | RESP |
|---|---|---|---|---|---|---|---|
| R1 RCM | ◐ | ✅ | ✅ | ✗ | ✗(반증 방향) | ◐(조직 간) | ✅ |
| ServiceNow | ✅ | ✅ | ◐ | ◐(킬 스위치) | ◐(자동화 복제) | ◐(회수만) | ✅ |
| Zapier 재무 | ✅ | ✅ | ✅ | ✗ | ✅ | ◐ | ✅ |
| Zapier 전사 | ✅ | ✅ | ◐ | ✗ | ◐ | ◐ | ◐ |
| 삼성SDS 계열 | ✅ | ✅ | ◐ | ✗ | ✅ | ◐ | ✅ |
| TK Elevator | ✅ | ✅ | ◐ | ✗ | ✅ | ✗ | ◐(데이터 계보) |
| Deloitte | ✅ | ✅ | ✅ | ✗ | ◐(측정 과업) | ✗ | ◐(원칙만) |
| Nokia | ◐ | ✅ | ✅ | ✅ | ✅ | ✗ | ◐(감사추적 없음) |
| Siemens | ✅ | ✅ | ✅ | ✗ | ✅ | ◐(시간) | ◐(원칙만) |
| McKinsey | ✅ | ✅ | ◐ | ✗ | ✅ | ✗ | ✅ |

**한눈에 보이는 두 가지.**

첫째, **CYCLE의 역방향(증강 회귀)은 사실상 관측되지 않는다.** 10건 중 근거가 있는 것은 Nokia
하나이고, 그마저 실제 회귀 사례가 아니라 "사용 사례가 변경되면 나중에 전체 자동화 시스템이
아무 의미가 없어질 수도 있습니다"라는 **예상 서술**이다. ServiceNow의 킬 스위치는 회귀가 아니라
**정지**다. 논문이 시간축 논증의 절반을 걸고 있는 명제인데, 실무 담론에는 그 절반이 없다.

둘째, **REINV(UBS 패턴)가 가장 약한 축이다.** 자동화로 아낀 자원의 **회수 측**은 어디서나
정량화되지만(ServiceNow 5억 달러·230만 시간, Nokia TCO 15%), **투입 측**은 대부분 부정형이거나
정성적이다. ServiceNow는 "그건 복사 붙여넣기나 티켓 라우팅 과정으로 이어지지 않았어요"라고
**아닌 것**만 말하고, TK Elevator·Deloitte·Nokia·McKinsey는 재투자 회계가 아예 없다.
논문이 UBS로 예시한 선순환의 후반부는 실무 담론에서 측정되지 않는다.


---

# 제2부 · 사례별 전체 서술



## 사례 1 — R1 RCM × Palantir : 의료 코딩

*원문: `docs/cases/01_r1rcm.md`*


> 인용 규약: 아래 모든 큰따옴표 인용은 소스 자막 파일에 존재하는 문자열 그대로다. 자막 원문의 오탈자·자동인식 오류("healthc care", "in to's today's", "paler", "palente", "Palunteer", "Palanteer", "emerent", "co-orbidities", "2hour", "20-oot", "tabber", "Taver", "TAVER")를 교정하지 않고 옮겼다. 자막 원문은 줄바꿈 위치에 `&nbsp;` 마크업이 삽입되어 있어, 인용은 그 마크업을 건너뛰지 않는 연속 구간 단위로만 끊어 인용했다. 여러 구간을 이어 읽어야 하는 대목은 인용을 나누고 사이에 `…`를 두었다. 큰따옴표는 오직 소스 원문 인용에만 쓰고, 필자의 요약·해석 표현은 홑낫표 「 」로 구분했다.

### 1.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Palantir | **업로드일 2025-03-18** (채널 수집분, 파일 헤더 "업로드일" 필드) | en | 약 1552개 | Palantir AIPCon 6 무대 발표. 발화자 2인 — 자기소개 그대로 "hey everybody I'm Steve and I'm Chris we're" [S1]. R1 RCM 측 인물로, 한 명은 데모 조작("while Steve gets" [S1]), 다른 한 명은 "digital twin and uh from operations and product" [S1]로 지칭됨. 성(姓)·직함은 해당 소스에 없음 | https://www.youtube.com/watch?v=YGxLLloZ3hU | /home/user/youtube-scrap/transcripts/channels/Palantir/Unlocking_Revenue_Potential_in_Healthcare_R1_RCM_at_AIPCon_6__YGxLLloZ3hU.md |
| [S2] | Palantir | **업로드일 2025-06-10** (채널 수집분, 파일 헤더 "업로드일" 필드) | en | 약 1493개 | Palantir AIPCon 7 무대 발표. 발화자 1인, Nebraska Medicine 측("Nebraska Medicine is" … "an academic medical center located in Omaha," [S2]). 이름·직함은 해당 소스에 없음 | https://www.youtube.com/watch?v=VM2XylCVYXI | /home/user/youtube-scrap/transcripts/channels/Palantir/Transforming_Patient_Journey_Nebraska_Medicine_at_AIPCon_7__VM2XylCVYXI.md |

**시점 표기 주의**: 두 소스 모두 `transcripts/channels/...` 경로의 **채널 수집분**이므로 헤더의 "업로드일"이 곧 **영상 업로드 시점**이다(키워드 수집분처럼 폴더명이 수집일인 경우가 아니다). 다만 업로드일은 **영상 공개일**이지 **AIPCon 6 / AIPCon 7 의 실제 개최일이 아니다** — 개최일은 두 소스 모두에 없음.

각 소스의 역할:
- **[S1] 1차 근거.** 이 사례의 본체. R1 RCM의 의료 코딩 AUTO/AUG 배분, 자율 코딩 로드맵의 조건절, human in the loop 대시보드, audit trail, 20년 코딩 전문성의 가이드라인 코드화가 모두 여기에만 있다.
- **[S2] 대조군.** 같은 Palantir AIPCon 시리즈(6→7, 업로드 기준 약 3개월 차)의 다른 헬스케어 사례. R1이 「코더 1인의 판단 루프」에 인간을 남기는 것과 달리, Nebraska Medicine은 「임상적 최종 결정권」에 인간을 남기고 **정보 종합·예측·후보 산출**을 기계에 넘긴다. 자동화/증강의 경계선이 어디에 그어지는지 비교하기 위한 대조 사례이며, R1 사례의 직접 근거로는 쓰지 않는다.

---

### 1.2 조직과 문제 상황

**R1 RCM의 정체성** — "R1 is a healthc care um revenue cycle" … "company" [S1]. 제공 범위는 진료 이후 청구 전 과정으로 서술된다: "appointment registering when you arrive um after" … "you provide service a lot of things happen behind" … "the scene your chart you seen your chart is coded" … "uh a claim is submitted to an insurer there's lots" … "of activities to follow up to get that payment" [S1].

**규모(벤더 자체보고)** — "to do it we serve over 500 clients we serve 94 of" … "the top 100 Health Systems some of which are here" [S1]. 즉 500개 초과 고객사, 상위 100대 헬스시스템 중 94곳 [S1]. 인원 수(코더 수, 직원 수)는 **해당 소스에 없음**.

**금액 규모(산업 전체 문제 규모, R1 자체 실적 아님)** [S1]:
- 수납 비용 비율 — "now is for a physician who maybe owed $100 for" … "their services they're typically having to spend" … "$4 just to collect that uh and oftentimes they're" … "only collecting 95% of it so when you extrapolate" [S1]. 즉 $100 청구당 수납 비용 $4, 수납률 약 95%.
- 산업 총액 — "that across today's Healthcare uh Revenue which" … "is around $4 trillion you're talking about $160" … "billion annually spent just trying to collect" … "the revenue that the providers are owed and" … "often times they're only collecting around 95% of" [S1]. 즉 헬스케어 매출 약 $4조, 수납 비용 연 $1,600억.
- 기회 규모 — "we believe there is a multi hundred billion" … "dollar opportunity here industrywide" [S1].

**물량·복잡도(before 상태)** [S1]:
- 의무기록 분량 — "a medical record these can be 300 500 pages long" [S1]. 내용물은 수치만이 아니다: "it contains not just numbers like your Labs but" … "also long narratives which can be quite different" … "depending on what physician wrote it and then also" … "diagnostic images" [S1].
- ICD-10 복잡도 — "over 10,000 many tens of thousands of different" … "codes in the icd10 universe uh such favorites as" … "uh sucked into a jet engine subsequent encounter" … "uh burn caused by water skis Catching Fire" … "uh or my personal favorite uh occupant" … "injury from space Collision" [S1]. 결과적으로 "imagine that multitude of icd10 codes creates" … "permutations that are sort of incomprehensible" [S1].
- 시스템 분절 — "and Technology we have disparate systems uh the" … "hospital has a system physician groups have a" … "system payers have a system Clearing Houses have a" … "system they're not that interoperable" [S1], 그리고 표준의 실질 부재: "are pseudo standards they're not actually" … "that standardized uh and making them work" … "is challenging" [S1].
- 규칙의 유동성 — "guidelines from Regulatory Agencies there's" … "guidelines from payers changing all the time" [S1], 계약별 상이: "so every health system has an agreement with an" … "insurer a contract that determines how they're" … "going to get paid" [S1].

**과거 접근의 실패 진단(중요)** — "our research really showed us is that we were" … "all attacking this problem in the wrong way we" … "were focused on task-based automations or siloed" … "approaches" [S1]. 대안으로 제시된 목표는 "what we would call comprehensive of automation" [S1] 이다. 즉 R1의 자기 서술에서 **과업 단위 자동화(task-based automation)는 실패한 전략**으로 명시적으로 부정되고, 포괄적 자동화가 목표로 설정된다.

**착수 시점** — "team we did a a build session in December uh we" … "started engaging with them on a full-time basis" … "um in January and so we'll show you what we've" … "built" [S1]. 즉 12월 빌드 세션 → 1월 풀타임 착수. **연도는 해당 소스에 없음.** (업로드일 2025-03-18 기준으로 직전 12월/1월로 읽는 것이 자연스럽지만, 소스가 연도를 말하지 않으므로 추정이다.)

---

### 1.3 자동화 구간 (AUTO)

기계에 넘어간 것은 **코드 후보의 사전 생성(pre-population)과 그 근거 하이라이팅**이다. 코드 부여 자체를 인간이 백지에서 시작하지 않는다.

- 화면 상태 — "are those are medical codes that have already" … "been pre-populated um how did this happen well" [S1].
- 생성 주체 구조 — "you you're looking at here is a constellation of" … "AI agents that's a combination of large language" … "models that are being applied to those guidelines" … "that I mentioned to the medical record and are" … "making decisions and interacting with one another" … "to actually come up with the predictions um see um" [S1]. 즉 **AI agent constellation** = 복수 LLM이 (a) 가이드라인과 (b) 의무기록에 적용되어 **서로 상호작용하며** 예측을 산출하는 구조.
- 근거 제시도 기계가 자동 수행 — "that the uh AI agents uh automatically provide" … "to the user uh highlights of where uh what the" … "reasons are in the guidelines uh as to why those" … "codes were actually generated" [S1].
- 자동화의 목표 스케일 — "deliver and by providing not only the ability to" … "automate this at scale but also provide the audit" … "Trail" [S1].

주의: **현재 시점의 AUTO는 「인간을 루프에서 제외한 자동화」가 아니다.** 소스 안에서 완전 자동(autonomous coding)은 아직 도달점으로만 서술된다(1.5 참조). 지금 기계가 인계한 것은 「탐색·초안·근거 수집」이며, 확정은 코더에게 남아 있다.

---

### 1.4 증강 구간 (AUG)

인간은 **코더 자리**에 남는다. 그리고 R1의 서술에서 인간의 자리는 두 겹이다: (i) 개별 인코딩 판단의 최종 검토자, (ii) 20년치 암묵지를 가이드라인이라는 기계 입력물로 제공한 원천.

- 인간이 루프에 남는 형태 — "get there by first having a co-pilot that helps" … "a medical coder" [S1]. 화면 구성은 큐 기반 검토다: "what you're going to see here is uh a coder that's" … "looking at a queue of encounters from patients" [S1], "and um they log in they're now looking at on the" … "left side of your screen there they're saying" … "all the detail from the medical record from this" … "encounter" [S1].
- 증강의 효과 서술(속도·규모) — "medical coders to work at an unprecedented" … "scale in speed on behalf of providers and" … "Physicians" [S1]. 즉 **코더를 대체한다**가 아니라 **코더의 처리 규모와 속도를 올린다**로 표현된다.
- **암묵지의 코드화** — "guidelines are important because these contain" … "the two decades of experience we have medical" … "coding across all our clients" [S1]. 그리고 이것이 가치의 원천으로 재확인된다: "value here is about being able to couple expert" … "expertise and technology that we've innovated on" … "over as Steve said two decades with the scaled" … "approach that a Foundry platform allows us to" … "deliver" [S1].
- 난이도 전제 — "to solve it so today coding is a really hard" … "job" [S1].

이 대목이 이론적으로 결정적이다. **기계가 적용하는 「가이드라인」의 내용물 자체가 R1 도메인 전문가 20년치 경험이다** [S1]. 즉 AUG는 「인간이 기계 옆에 앉아 있다」에 그치지 않고, 「기계가 작동하는 규칙 자체가 도메인 전문가에게서 나왔다」는 층위를 포함한다.

---

### 1.5 전환 메커니즘 (CYCLE)

**있음.** 단계와 조건절이 명시적으로 진술된다.

- 로드맵 — "built so our vision here is over time we believe" … "that autonomous medical coding is possible which" … "is required to accurately bill um but we probably" … "get there by first having a co-pilot that helps" … "a medical coder and then over time as accuracy is" … "validated we then move into autonomous coding" [S1].

여기서 전환 조건은 **"a medical coder and then over time as accuracy is"** … **"validated we then move into autonomous coding"** [S1] 이다. 즉 유일하게 진술된 문턱은 「정확도가 검증되면」 하나뿐이다. 이론(p.196-197)의 「증강 학습 → 견고화 → 자동화」 시간축과 문장 구조가 그대로 대응한다: co-pilot(증강) → 정확도 검증(견고화) → autonomous coding(자동화).

- **판별 장치**: 조건 충족 여부를 무엇으로 보느냐가 human in the loop 대시보드에 부여된 기능이다 — "now is just a view of how that human in the loop" … "dashboard might look and how we would know" … "when uh automations are being successful to" … "scale where it can be deployed" [S1].

즉 human in the loop 대시보드는 단순한 검수 UI가 아니라 **「자동화를 어디까지 확대해도 되는지 판별하는 계기(計器)」**로 서술된다. 인간의 검토 행위가 곧 자동화 확장 여부의 데이터 소스가 되는 구조다.

**중요한 유보**: 위 인용의 조동사에 주목해야 한다. "our vision here is over time we believe" [S1], "we probably" … "get there" [S1], "dashboard might look" [S1], "how we might go about auditing" [S1]. 전환 메커니즘은 **설계 의도로 진술**되었고, 이미 자동화 단계로 넘어간 과업이 있다는 진술은 **해당 소스에 없음**. 정확도 임계값(예: 몇 %에서 자동화로 넘어가는가), 검증 절차, 승인 주체도 **해당 소스에 없음**.

---

### 1.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

**SPILL — 부분적으로 있음(다만 인접 과업에서 「증강이 유발되었다」는 직접 진술은 없음).**

코딩은 4개 유스케이스 중 하나로 위치지어진다 — "uh coding is one space that we're working on but" … "with palente help we're actually focused on four" … "main use cases that represent a disproportionate" … "share of that 5% of Revenue that's lost" [S1]. 즉 코딩 옆에 3개 과업이 더 있고, 이들은 「손실되는 매출 5%」의 불균형하게 큰 몫을 차지하는 지점으로 선택되었다 [S1]. 그러나 **나머지 3개 유스케이스가 무엇인지, 코딩 자동화가 그 과업들의 증강을 유발했는지는 해당 소스에 없음.** 또한 R1의 전략 서술은 오히려 「부분 자동화의 사일로화」를 실패로 규정하고("were focused on task-based automations or siloed" … "approaches" [S1]) 처음부터 "comprehensive of automation" [S1]을 겨냥하므로, 이 사례의 공간축은 *사후 파급*이라기보다 *사전 통합 설계*에 가깝다. 이는 이론의 SPILL(한 과업 자동화가 인접 과업 증강을 유발)과 결이 다르며 1.10에서 다시 다룬다.

**REINV — 목적 진술 수준으로만 있음.**

"that money back into the pockets of providers" … "and Physicians so that they can better invest" … "in p outcomes" [S1]. 즉 회수된 자원이 의료제공자에게 돌아가 「환자 성과(자막상 'p outcomes')」에 재투자된다는 서술이다. 다만 이는 **R1 조직 내부의 자원 재배치가 아니라 고객(의료제공자) 측 재투자에 대한 기대**이며, 실제 재투자 사례·금액·시점은 **해당 소스에 없음**. UBS 패턴(p.201)처럼 「자동화로 남은 인력을 증강 업무로 이동시켰다」는 서술은 **해당 소스에 없음**.

---

### 1.7 통합 장치 (RESP)

**있음. 이 사례에서 가장 두껍게 서술된 구성개념이다.**

- 감사추적의 산업적 필수성 — "moreover um you have like it's very important for" … "us in our industry to have an audit Trail as to" … "why the codes were selected" [S1], 그리고 "Trail which as we all know with Healthcare" … "is super critical" [S1].
- 감사추적의 내용 — 코드가 왜 생성되었는지를 **가이드라인 원문 위치로 되짚어 보여주는 방식** — "that the uh AI agents uh automatically provide" … "to the user uh highlights of where uh what the" … "reasons are in the guidelines uh as to why those" … "codes were actually generated" [S1].
- 사후 대외 책임 — "a view into how we might go about auditing that" … "uh whether it be for a payer denial appeal or for" … "a a governmental um Regular audit on the back end" [S1]. 즉 감사추적의 수신자는 내부가 아니라 **지불자(보험사) 거부 항변**과 **정부 정기 감사**다.

**정확한 강도 표기**: 인간이 「승인권」을 보유한다는 명시적 문장(예: approve/sign-off/final say)은 **해당 소스에 없음**. 확인되는 것은 (a) 코더가 루프 안에 있는 co-pilot 구성, (b) 기계 판단의 근거를 인간이 읽을 수 있게 자동 제시, (c) 외부 감사에 제출 가능한 추적성, 이 세 가지다. 거버넌스 위원회, 책임 소재 규정, 오류 시 처리 절차는 **해당 소스에 없음**.

---

### 1.8 성과 수치

**핵심 경고: [S1]에는 R1의 도입 전후(before/after) 성과 수치가 사실상 없다.** 등장하는 숫자는 (a) 산업 전체의 문제 규모, (b) R1의 사업 규모, (c) 문제 대상의 복잡도이며, 이 협업의 결과치가 아니다.

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 코딩 정확도 / 자동화율 / 처리속도 (R1 도입 효과) | 해당 소스에 없음 | 해당 소스에 없음 | [S1] | — |
| $100 청구당 수납 비용 | "$4 just to collect that" | 해당 소스에 없음 | [S1] | 산업 통계로 제시, 출처 미상 (벤더 발표 중 인용) |
| 수납률 | "only collecting 95% of it" / "around 95%" | 해당 소스에 없음 | [S1] | 동상 |
| 산업 총 수납비용 | "$160" + "billion annually" (매출 "around $4 trillion" 기준) | — | [S1] | 벤더 산정치, 제3자 검증 없음 |
| 손실 매출 비중 | "that 5% of Revenue that's lost" | 해당 소스에 없음 | [S1] | 벤더 자체 규정 |
| 기회 규모 | — | "multi hundred billion" + "dollar opportunity here industrywide" | [S1] | 벤더 전망("we believe"), 미실현 |
| 고객사 수 | — | "over 500 clients" | [S1] | 벤더 자체보고 |
| 상위 100대 헬스시스템 커버리지 | — | "94 of" + "the top 100 Health Systems" | [S1] | 벤더 자체보고 |
| 의무기록 분량 | "300 500 pages long" | — | [S1] | 벤더 서술, 대상 복잡도 |
| ICD-10 코드 수 | "over 10,000 many tens of thousands of different" codes | — | [S1] | 벤더 서술 (자막상 수치 표현이 자체 모순적 — 1.11 참조) |
| 착수 경과 | "build session in December" → "full-time basis" "um in January" | — | [S1] | 벤더 자체보고, 연도 미기재 |

**대조군 [S2]의 성과 수치(참고용, R1 사례의 근거 아님)**

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 재원 활용률 | "constraints greater than 90% average daily census" + "every single day" | — | [S2] | 자체보고 |
| 퇴원 라운지 이용 | — | "we saw a 2100% increased use of our discharge" + "lounge" / "a 2,000% improvement" | [S2] | 자체보고 (2100% vs 2,000% 표기 불일치, 1.9 참조) |
| 가용 병상 | — | "one unit, 35 additional beds" | [S2] | 자체보고 |
| 전원 수용 | — | "allowed us to see a 13% increase in transfers" | [S2] | 자체보고 |
| 간호사 이직률 | "national averages" | "less than 50% nurse turnover compared" + "to national averages." | [S2] | 자체보고 |
| 퇴원 예측 정확도 | — | "it's a 95% discharge prediction accuracy" | [S2] | 자체보고, 검증 방법 미기재 |
| 이용관리(UM) 의사 검토 시간 | "our average was" + "80 minutes" | "now reduced down to seven" | [S2] | 자체보고 |
| 보험사 제출 문서 분량 | "From 50 to 70 pages of documents" | "are now down to two" | [S2] | 자체보고 |
| 퇴원 지시→실제 퇴원 소요 | — | 조직 전체 "by one" + "hour" 단축 | [S2] | 자체보고 |
| 공급망 앱 재작성 | "two and a half to three months" (견적) | "46 minutes, they had a live product inclusive" + "of machine learning and AI" | [S2] | 자체보고, 벤더 속도 서사 |
| 항변서 작성·제출 | — | "appeals letter in less than an hour and submitted" + "it successfully to the insurance company in about" + "90 minutes total" | [S2] | 자체보고, 단건 사례 |

---

### 1.9 소스 간 교차 대조

**(a) 두 소스에서 반복 확인되는 사실**

1. **분절된 규칙·문서를 기계가 흡수한다는 서사가 양쪽에 공통.** [S1]은 규제기관·지불자 가이드라인과 계약을 LLM 입력으로 삼고("models that are being applied to those guidelines" [S1]), [S2]도 동일한 구조를 말한다 — "process the different guidelines and protocols." … "That's now all been ingested in the system. It's" … "able to read the notes and make the determination." [S2]. **가이드라인의 기계화**가 Palantir 헬스케어 사례의 공통 패턴이다.
2. **긴 비정형 문서 전체를 읽어내는 능력이 공통 셀링포인트.** [S1] "a medical record these can be 300 500 pages long" vs [S2] "It actually reads through the entire chart and" … "looks through what else might be planned, what are" … "co-orbidities, what are other risk factors." [S2].
3. **보험사와의 사후 분쟁(denial/appeal) 처리가 양쪽 모두에 등장.** [S1]은 감사추적의 용도로("a payer denial appeal" [S1]), [S2]는 실제 개선 실적으로("There are occasions" … "where insurance companies will challenge that" … "reimbursement" [S2], "80 minutes now reduced down to seven" [S2]).
4. **양쪽 모두 벤더/고객 자체보고이며 제3자 검증치가 하나도 없다.** 두 소스 전체에서 외부 감사기관·학술 검증에 근거한 수치는 없다. 유일한 외부 인용은 [S2]의 "unfortunately do happen. In 2016, John's Hopkins" … "published it's the number three cause of death" … "in the United States." 인데, 이는 성과가 아니라 문제 배경이다.

**(b) 한 소스에만 있는 사실**

- **[S1]에만**: autonomous coding 로드맵과 그 조건절("as accuracy is" … "validated" [S1]), AI agent constellation 구조, audit trail의 이중 수신자(지불자/정부), 20년 코딩 경험의 가이드라인 코드화, 착수 타임라인(12월 빌드 세션 / 1월 풀타임), 4개 유스케이스 전략, "task-based automations or siloed" 접근에 대한 자기비판.
- **[S2]에만**: 조직 내부 운영 지표(병상, 이직률, 재원일수), 임상 스케줄링, 인력 배치, 예측 정확도 수치, 「forward success engineers」로의 개칭("we renamed forward deployment engineers forward" … "success engineers because they're really helping" [S2]), 데이터 분리 약속("protect our patient data, keep it separate from" … "others" [S2]).
- **[S2]에는 자율화 로드맵이 없다.** 「언제 인간을 빼도 되는가」에 해당하는 조건 서술이 [S2]에는 전혀 등장하지 않는다. 대신 인간이 계속 개입하는 지점이 반복 명시된다 — "we can then go back and start staffing that team." [S2], "see here is the authoring tool that allows you to" … "create that capacity." [S2], "that meet defined criteria based on ours. Urgent" [S2] (기준 자체가 조직 소유), "emerent cases, we always take them, but urgent" [S2] (수용 여부의 정책적 판단은 인간 규칙).

**(c) 시점에 따른 서술 변화**

- 업로드 기준 [S1] 2025-03-18 → [S2] 2025-06-10, 약 3개월 간격이지만 **두 사례는 서로 다른 조직**이므로 동일 사례의 종단 변화로 읽을 수 없다. 즉 「R1이 나중에 자율 코딩에 도달했는가」는 두 소스로 확인 불가 — **해당 소스에 없음**.
- 성숙도의 대비는 뚜렷하다. [S1]은 착수 후 수개월 시점의 **데모**를 보여주며 조동사가 미래형이다("dashboard might look" [S1], "we probably" … "get there" [S1]). [S2]는 "And because two years ago, 18 months ago, in fact," … "when we started with Palunteer, we had capacity" [S2]로 18~24개월 경과를 밝히고 확정 과거형 실적 수치를 제시한다. **같은 시리즈 무대에서도 발표 시점의 프로젝트 성숙도가 다르며, 수치의 존재 여부가 그 차이를 그대로 반영한다.**

**(d) 모순 / 내적 불일치**

1. **[S2] 내부 수치 불일치**: 같은 문장 흐름에서 "we saw a 2100% increased use of our discharge" … "lounge. You heard me correctly, greater than" … "a 2,000% improvement." [S2]. 2100%와 2,000%가 병기된다(후자는 "greater than"이 붙어 반올림 하한 표현으로 읽을 수 있으나, 표기는 불일치).
2. **[S2] 경과기간 불일치**: "two years ago, 18 months ago, in fact," [S2] — 발화자가 자가 정정한 형태로, 2년과 18개월이 한 문장에 공존한다.
3. **[S1] 코드 수 표현의 자체 모순**: "over 10,000 many tens of thousands of different" [S1] — 「1만 초과」와 「수만」이 겹쳐 제시된다.
4. **[S1] 전략 서술과 이론적 SPILL의 긴장**: R1은 "task-based automations or siloed" 접근을 실패로 규정하는데 [S1], 동시에 "coding is one space" [S1]로 과업 단위 착수를 서술한다. 모순이라기보다, **과업 단위로 시작하되 처음부터 통합 플랫폼 위에서 시작한다**는 주장으로 읽힌다. 다만 소스는 그 통합이 실현되었다고 말하지 않는다.
5. **명칭 표기 흔들림(자막 오류)**: [S1] "pal here" / "paler" / "palente", [S2] "Palunteer" / "Palanteer". 동일 기업명의 자동인식 오류이며 서로 다른 주체가 아니다.

---

### 1.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간 루프 제외 (p.194) | 코드 사전 생성과 근거 하이라이팅을 AI agent constellation이 수행 [S1]. 단, 현 시점 인간은 여전히 루프 안 | **부분 지지** — 완전한 AUTO는 미도달, 목표로만 존재 |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | "co-pilot that helps" + "a medical coder" [S1]; 큐 기반 검토 화면 [S1] | **지지** |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | "first having a co-pilot" → "as accuracy is" "validated" → "we then move into autonomous coding" [S1] | **강한 지지** — 3단계가 한 문장으로 명시됨. 이론 문헌에서 흔치 않게 실무자가 시퀀스를 자각적으로 진술 |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 회귀 조건에 대한 서술 **해당 소스에 없음**. [S1]은 단방향(증강→자동화)만 서술 | **미확인** — 반증도 지지도 아님 |
| SPILL: 한 과업 자동화가 인접 과업 증강 유발 (p.197) | "coding is one space" + "four" "main use cases" [S1]. 그러나 파급 인과는 서술되지 않음 | **미확인 / 잠재적 반증** — R1은 순차적 파급이 아니라 **동시·통합 설계**를 표방하며 사일로형 순차 자동화를 명시적으로 부정 [S1] |
| REINV: 자동화 자원을 증강에 재투자 (UBS 패턴, p.201) | "back into the pockets of providers" → "better invest" "in p outcomes" [S1] | **확장(주체 이동)** — 재투자 주체가 자동화 수행 조직이 아니라 **고객 조직**. 조직 간 REINV |
| RESP: 인간이 프로세스 전체 책임/승인/감사 보유 (p.200) | audit trail이 "very important for" "us in our industry" [S1], 지불자 항변 + 정부 정기 감사 대응 [S1] | **지지 + 확장** — 책임의 수신자가 조직 내부가 아니라 **규제기관·지불자라는 외부 제3자** |
| 증강 학습은 도메인 전문가 암묵지에 의존, IT/외부업체 위임 불가 (p.195) | 기계 입력 가이드라인 = "the two decades of experience we have medical" "coding across all our clients" [S1] | **강한 지지 + 확장** — 암묵지가 *루프 안 상호작용*이 아니라 *기계의 규칙 코퍼스*로 사전 이전됨 |
| 기계 한계: 훈련된 과업에 국한 (p.198) | ICD-10 순열이 "incomprehensible" [S1], 지불자 가이드라인이 "changing all the time" [S1] → 고정 훈련으로 커버 불가 | **지지** |
| 기계 한계: 제약 완화된 옵션만 제시 (p.198) | 기계는 코드 후보를 "pre-populated" [S1] 상태로 제시할 뿐 확정하지 않음 | **지지** |
| 기계 한계: 목적·자아 부재 (p.198) | 목적(정확한 청구, 손실 5% 회수)은 인간이 설정 [S1] | **지지** |
| 기계 한계: 감각·감정·사회기술 부재 (p.198) | [S1]에는 관련 서술 없음. [S2]에는 대응물 있음 — 간호사 "preferences" 반영 [S2], "staff happier" [S2], 가족의 "peace" [S2] | **[S1] 미확인 / [S2] 지지** |
| 한쪽 편중 시 악순환 (p.199) | R1의 자기비판 "were focused on task-based automations or siloed" "approaches" [S1] = 자동화 편중이 낳은 비효율의 자인 | **보강** |
| 기계는 조직 내 새로운 행위자 계급 (p.204) | "constellation of" "AI agents" 가 "making decisions and interacting with one another" [S1] — 기계끼리의 상호작용이 명시 | **강한 보강** |
| (대조군) AUTO/AUG 경계 | [S2]는 정보 종합·예측·후보 산출을 기계에, **수용 여부·배치·최종 임상 판단**을 인간에 남김 [S2] | R1 대비 **경계선이 다름**: R1은 「판정 자체」를 점진적으로 넘기려 하고, Nebraska는 「판정의 재료」만 넘긴다 |

**이 사례가 논문을 확장하는 지점.** 첫째, Raisch & Krakowski가 CYCLE을 사후적으로 관찰되는 궤적으로 기술하는 데 반해, R1은 그 궤적을 **사전 로드맵으로 선언하고 판별 계기를 설치한다** — human in the loop 대시보드가 검수 도구인 동시에 "how we would know" … "when uh automations are being successful to" … "scale where it can be deployed" [S1] 라는 자동화 확대 판정 장치로 이중 기능을 부여받는다. 즉 **증강은 자동화로 가는 통로일 뿐 아니라, 자동화의 정당성을 생산하는 계측 장치**다. 둘째, p.195의 암묵지 명제가 여기서는 「전문가가 루프에 남아 기계를 가르친다」가 아니라 「20년치 전문성이 이미 가이드라인 문서로 응결되어 LLM의 입력 코퍼스가 되었다」는 형태로 나타난다 [S1] — 암묵지 의존은 유지되지만, 그 의존이 **실시간 협업이 아니라 축적된 문서 자산**을 매개로 성립한다. 셋째, RESP의 수신자가 조직 내부가 아니라 지불자와 정부라는 외부 제3자이며 [S1], 이 때문에 감사추적은 자율화의 *제약*이 아니라 오히려 자율화를 정당화하기 위한 *전제조건*으로 기능한다. 넷째, 대조군 [S2]와 나란히 놓으면 같은 플랫폼·같은 산업에서도 인간을 남기는 위치가 다르다는 점이 드러난다 — R1은 **판단 자체를 단계적으로 이양**하려 하고, Nebraska Medicine은 판단의 재료만 기계화한 채 **수용·배치·임상 결정은 이양 대상으로 논의조차 하지 않는다** [S2]. 이는 AUTO/AUG 경계가 기술 성숙도가 아니라 **오류의 되돌릴 수 없음(irreversibility)** 에 따라 그어질 가능성을 시사하나, 이 해석을 뒷받침하는 명시적 진술은 두 소스에 없다.

---

### 1.11 인용 시 주의사항

1. **모든 수치가 자체보고다.** [S1]의 $160B, 5% 손실, 500+ 고객사, 94/100 헬스시스템은 모두 발표 조직 자신의 주장이며 제3자 검증치가 아니다. 산업 통계($100당 $4, 95% 수납률)도 출처가 소스에 없다. 인용 시 「R1 발표자 주장에 따르면」을 반드시 붙일 것.
2. **성숙도: 이것은 실적이 아니라 데모다.** [S1]의 코딩 화면은 "while Steve gets" … "the uh demo running" [S1] 이후 제시되며, 착수 후 수개월("build session in December" → "full-time basis" "um in January" [S1]) 시점이다. autonomous coding은 "our vision" [S1] 이고 대시보드는 "might look" [S1]이다. **운영 중인 자율 코딩 시스템의 사례로 인용하면 오독이다.**
3. **성과 부재를 명시할 것.** [S1]에는 R1의 코딩 정확도·자동화율·처리량 개선치가 **하나도 없다**. 이 사례는 성과 사례가 아니라 **AUTO/AUG 배분 설계 사례**로만 인용 가능하다.
4. **자막 오류.** "healthc care"(healthcare), "in to's today's"(into today's 추정), "pal here"/"paler"/"palente"(Palantir), "icd10"(ICD-10), "car is"(caring/care is 불명), "p outcomes"(patient outcomes 추정), "Regular audit"(regulatory audit 추정 — 이 교정형은 소스에 없는 필자 추정), "a a governmental"(중복). [S2]의 "Palunteer"/"Palanteer", "emerent"(emergent), "co-orbidities"(comorbidities), "2hour"(2 hour), "Taver"/"tabber"/"TAVER"(TAVR/TAVER), "20-oot"(20-foot), "the emissions"(admissions 추정), "worldclass"/"world-class", "multid-disciplinary". **원문 인용 시 교정하지 말 것.** 특히 "a a governmental um Regular audit on the back end" [S1]을 「regulatory audit」으로 고쳐 인용하면 기계적 대조 검증에서 불일치가 난다.
5. **귀속 문제.** [S1] 발화자는 "Steve"와 "Chris" 두 이름만 등장하고 성·직함·소속 부서가 없다. 어느 발언이 누구 것인지 자막상 구분이 불완전하다("he's my" … "digital twin and uh from operations and product" [S1] — 이 표현이 동료를 가리키는 농담인지 기술 용어인지 소스만으로 판별 불가). **개별 인물에게 특정 발언을 귀속시키지 말고 「R1 발표자」로 표기할 것.** [S2] 발화자는 이름조차 없다.
6. **소스 성격.** 두 영상 모두 **Palantir 공식 채널이 업로드한 자사 컨퍼런스(AIPCon) 발표**다. 즉 벤더 마케팅 맥락에서 고객사가 발화한 자료이며, 부정적 결과나 실패 사례가 구조적으로 배제된다. 이 편향을 각주로 밝힐 것.
7. **업로드일 ≠ 발표일 ≠ 프로젝트 시점.** 헤더의 업로드일(2025-03-18 / 2025-06-10)은 영상 공개일이다. AIPCon 6/7의 실제 개최일, [S1]의 "December"/"January"가 몇 년인지, [S2]의 "two years ago"의 기준점은 모두 **해당 소스에 없음**.
8. **[S2]를 R1 사례의 근거로 쓰지 말 것.** 두 사례는 조직이 다르고 과업이 다르다. [S2]는 오직 AUTO/AUG 경계 비교를 위한 대조군이며, [S2]의 성과 수치를 R1 사례로 옮기면 귀속 오류다.
9. **[S2]의 내적 불일치 수치(2100% vs 2,000%, "two years ago, 18 months ago")를 인용할 때는 원문의 양쪽 표기를 함께 제시할 것.** 한쪽만 인용하면 발화자가 하지 않은 정밀도를 부여하게 된다.


---



## 사례 2 — ServiceNow : 자사 IT/CS 서비스데스크 (dogfooding)

*원문: `docs/cases/02_servicenow.md`*


### 2.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 구분 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | ServiceNow | **업로드일 2025-11-17** (채널 수집분, 파일 헤더 "업로드일" = 영상 업로드 시점) | ko | 약 298개 | 자사 dogfooding 브랜디드 영상 "How does ServiceNow use ServiceNow to deliver autonomous IT?" — 인터뷰어 + 사내 IT 담당자(이름 소스에 없음)의 화면 시연 | https://www.youtube.com/watch?v=wt-cMjxE8zg | /home/user/youtube-scrap/transcripts/channels/ServiceNow/How_does_ServiceNow_use_ServiceNow_to_deliver_autonomous_IT__wt-cMjxE8zg.md |
| [S2] | ServiceNow | **업로드일 2025-11-17** (채널 수집분) | ko | 약 261개 | 같은 dogfooding 시리즈의 고객관계(CS/CRM)편. 발화자 이름 소스에 없음. 데모 인물로 "메러디스라는 기술 지원 엔지니어" 등장 | https://www.youtube.com/watch?v=9ptkdyhyakI | /home/user/youtube-scrap/transcripts/channels/ServiceNow/How_does_ServiceNow_use_ServiceNow_to_improve_customer_relat__9ptkdyhyakI.md |
| [S3] | ServiceNow | **업로드일 2026-05-07** (채널 수집분) | ko | 약 9200개 | Knowledge 2026 Day 1 오프닝 키노트. 빌 맥더모트(CEO), 아밋 자베리(사장 겸 COO/CPO), 홀리, 에이미(최고 경험 책임자), 닉 시트산, 파반 샤(Moveworks 창립자), 외부 게스트: 라지 수브라마니암(FedEx CEO), 비샬 탈와르(FedEx Dataworks), 젠슨 황(NVIDIA CEO) | https://www.youtube.com/watch?v=jeo2V1w-Peg | /home/user/youtube-scrap/transcripts/channels/ServiceNow/Welcome_to_Agentic_Business_ServiceNow_Knowledge_2026_Openin__jeo2V1w-Peg.md |
| [S4] | ServiceNow | **업로드일 2026-05-08** (채널 수집분) | ko | 약 8694개 | Knowledge 2026 Day 2 "The Blueprint for Agentic Business" 키노트. 아밋 자베리, 가우라브, 넨샤드, 샤르디 파텔, 켈리(CIO 역), 니키 파텔, 존/예브게니 디브로프(Armis)/타룬 시크리(Veza), 외부 게스트: 앨런 로사(CVS Health CISO), 다니엘(CVS 개발자 데모), 카르틱 나라인(Google Cloud), CJ(커뮤니티 MVP) | https://www.youtube.com/watch?v=q8kaVEkTWho | /home/user/youtube-scrap/transcripts/channels/ServiceNow/The_Blueprint_for_Agentic_Business_ServiceNow_Knowledge_2026__q8kaVEkTWho.md |
| [S5] | ServiceNow | **업로드일 2025-09-24** (채널 수집분) | ko | 약 2994개 | "Michael Park's AI Whiteboard Masterclass". 마이클 파크(ServiceNow 채널 및 파트너십 담당)의 파트너 대상 아키텍처 화이트보드 세션 | https://www.youtube.com/watch?v=0Fmw61s8CKc | /home/user/youtube-scrap/transcripts/channels/ServiceNow/Michael_Park's_AI_Whiteboard_Masterclass__0Fmw61s8CKc.md |

**시점 주의**: 5개 소스 모두 `transcripts/channels/` 하위 채널 수집분이며 파일 헤더에 "업로드일"이 있으므로 업로드 시점이 확인된다. 키워드 수집분(`transcripts/YYYY-MM-DD/`)은 이 사례에 포함되지 않았다. 다만 업로드일 ≠ 발화 시점이다. S3 본문에 "모두들 신코 데 마요 축하해요!" [S3](신코 데 마요 = 5월 5일)가 있고 S4 본문은 "어제 기조연설 정말 훌륭했습니다" [S4]라고 하므로, S3의 발화 시점은 업로드일(2026-05-07)보다 앞선 행사 1일차, S4는 그 다음 날이다. S1/S2는 발화 시점 메타가 없고 업로드일만 확인된다.

**각 소스의 역할**
- [S1] 1차 근거. 이 사례의 자사 IT 서비스데스크 자동화 수치(90%, 85%, 26,000명, 연 100만 건)가 나오는 유일한 원천.
- [S2] 1차 근거(CS 측면). 같은 시리즈·같은 업로드일로 IT편과 구조가 대칭이며, 수치 체계(89%, 15%, 7분기)가 IT편과 다르다는 점에서 IT편의 대조군 역할도 겸한다.
- [S3] 보강 + 시점 대조. 약 6개월 후 동일 dogfooding 서사가 어떻게 갱신·재진술되는지 확인하는 축.
- [S4] 보강 + 시점 대조. S3와 하루 차이인데 동일 지표를 다른 표현으로 재진술해, 같은 행사 내부의 서술 변이를 잡아내는 축.
- [S5] 대조군. IT 서비스데스크 사례가 아니라 아키텍처/거버넌스 설명이며, S1의 "AI 관제탑", "통치 체계 내재" 같은 표현의 제품적 배경을 제공한다. 자사 운영 수치는 없다.

---

### 2.2 조직과 문제 상황

- 인원: "ServiceNow는 현재 26,000명의 직원을 보유하고 있으며 지속적으로 성장하고 있습니다." [S1] — 이 수치는 S2~S5 어디에도 반복되지 않는다.
- 물량(before/현행 상태): "매년 백만 건의 사용자 상호 작용 거래가 발생한다고 상상해 보세요." [S1] — 역시 S2~S5에 반복 없음.
- 문제 인식: "많은 기업들과 마찬가지로 저희도 매우 유사한 어려움에 직면하고 있습니다. 수천 명의 직원과 수많은 최종 사용자 기기." [S1], "직원들이 더 나은 경험을 얻을 수 있도록 서비스 데스크와 지원 인력을 적절히 확장해야 합니다 ." [S1]
- 자기 위치 규정: "우리는 단순히 플랫폼만 구축하는 것이 아니라, 그 위에서 사업을 운영합니다." [S1], "저희는 실제로 플랫폼과 제품의 혁신성을 실전에서 테스트하고 있습니다 ." [S1]
- CS 측 규모: "저희는 14,000명 이상의 고객에게 서비스를 제공하고 있으며, 매출은 매년 20% 이상 성장하고 있습니다." [S2], "저희는 최초 고객입니다." [S2], "저희 사업은 고객을 위해 구축하는 것과 동일한 통합 AI 플랫폼을 기반으로 운영됩니다." [S2]
- CS 측 문제 인식: "기존 CRM은 현대 기업의 실제 업무 방식에 맞춰 설계되지 않았습니다." [S2]
- 6개월 후 자기 규정(S3): "저희가 직접 만든 샴페인을 마시고 있다는 사실도 알려드리고 싶습니다. 우리는 지금 ServiceNow가 ServiceNow를 실행하는 방식으로 운영되고 있습니다." [S3]
- 플랫폼 전체 규모(자사 운영 규모가 아니라 플랫폼 처리량): "기업 전반에 걸쳐 연간 1,000 억 건의 워크플로우 와 7조 건의 트랜잭션을 처리하는 엔드투엔드 시스템" [S3], "저희 플랫폼에서는 매년 1,000 억 건 이상의 워크플로우와 7조 건의 트랜잭션이 처리되며" [S4].

**before 상태에 대한 명시적 수치는 어느 소스에도 없다.** 즉 "AI 도입 전 티켓 수, 처리 시간, 인력 수"의 기준선이 제시되지 않는다. 90%/85%는 모두 after 값 단독 제시다.

---

### 2.3 자동화 구간 (AUTO)

**(a) 티켓의 감지-할당-해결 전 과정을 기계가 인계 (S1, 1차 근거)**

> "인공지능이 문제를 감지하는 순간 , 기본적으로 ' 아, 이 문제를 이해하고 해결할 수 있겠구나'라고 판단합니다 . 티켓을 자체적으로 할당한 다음 사람의 개입 없이 자동으로 해결 방법을 실행합니다 ." [S1]

Raisch & Krakowski의 automation 정의(기계가 과업 인계, 인간을 루프에서 제외)에 문자 그대로 대응하는 문장이다. "사람의 개입 없이"가 명시적이다.

> "저희 IT 지원 요청의 90%는 AI를 통해 처리됩니다. 그건 미래가 아니야. 바로 지금입니다." [S1]

**(b) 6개월 후 같은 구간의 재진술 (S3/S4)**

> "서비스 요청의 91%는 AI의 지원을 받습니다." [S3]

> "ServiceNow에서는 IT 지원 요청의 90%가 자율적으로 처리됩니다 . 그것이 바로 로드맵에서 현실로 나아가는 것의 의미입니다. 네, 맞습니다. 현재 정식 서비스 중입니다." [S4] (자사 CIO 역할로 등장한 켈리의 발언)

**(c) CS 측 자동화 (S2)**

> "복잡한 견적 생성, 전체 주문 처리 관리, 고객 응대 등 반복적이고 시간이 많이 소요되는 작업은 [음악] AI 에이전트가 처리합니다 ." [S2]

> "고객은 89%의 경우 셀프 서비스를 이용할 수 있습니다." [S2]

**(d) 에이전트를 "채용/온보딩"하는 은유 — 자동화 자원을 인사(人事) 문법으로 다루는 장치**

> "이 화면에서 보시다시피 저는 즉시 채용하거나 온보딩할 수 있는 여러 명의 에이전트 직원을 보유하고 있습니다. 지원 분석가가 어떻게 온보딩되는지 살펴보겠습니다." [S1]

> "이 작업의 지원 분석가 템플릿에서 볼 수 있듯이, 이 상담원은 보유한 지식과 과거 발생 사례를 바탕으로 모든 문제를 해결할 수 있습니다 ." [S1]

6개월 후 이 은유는 "AI 전문가(AI expert) = 자율적 인력"이라는 정식 제품 개념으로 승격된다.

> "올해 초, 우리는 AI 전문가들이 단순히 작업을 완료하는 데 그치지 않고 특정 역할을 처음부터 끝까지 수행하는 자율적인 인력을 발표했습니다." [S3]

> "AI 전문가들은 기존 팀에 자연스럽게 녹아들어 마치 새로운 팀원을 영입하는 것처럼 업무를 수행할 것입니다." [S3]

> "그들은 명확한 역할을 가지고 있으며, 기존 팀에 배정되어 워크플로우를 처음부터 끝까지 실행합니다 ." [S4]

**(e) 아키텍처적 배경 (S5, 대조군)**

> "따라서 이러한 기능들과 지식 그래프를 결합하면 단일 목적의 AI 에이전트가 만들어집니다." [S5]

> "미래에는 플랫폼 자체의 스마트한 인사이트 덕분에 1단계 또는 2단계 지원은 물론 서비스조차 필요하지 않게 되는 경우가 많습니다. 고객이 개입하기 전에 앞으로 발생할 문제를 예측하고 해결할 수 있기 때문입니다 ." [S5]

---

### 2.4 증강 구간 (AUG)

**(a) 재배치된 인력이 어디로 가는가 — S1은 목적지를 흐린다**

> "모든 기능이 플랫폼에 내장되어 있어 IT 지원 담당자의 85%가 더 가치 있는 음악 관련 업무에 재배치되었습니다." [S1]

"음악 관련 업무"는 자막 오류로 보인다(원 영상에 삽입된 [음악] 구간을 자막 엔진이 문장 안으로 끌어들인 흔적이 S1/S2 전반에 반복된다: "저희는 실제로 음악이라는 매체를 통해 고객의 요구에 더 빠르게 대응할 수 있도록 돕고 있습니다." [S2], "음악이 미치는 영향은 엄청납니다." [S2]). **따라서 S1은 "85%가 재배치되었다"는 사실만 말하고, 재배치된 인간이 실제로 어떤 증강 과업을 맡는지는 소스에서 판독 불가능하다.** 이는 이 사례의 AUG 근거 중 가장 약한 지점이다.

**(b) 인간이 남는 지점이 명시된 것은 CS편(S2)이다**

> "AIA 상담원이 세 건의 지원 사례를 자동으로 해결한 것을 확인할 수 있습니다 . 두 건의 사건이 진행 중이며 AI 에이전트가 해결하고 있고, 세 번째 사건에 대해서는 그녀가 조치를 취해야 합니다." [S2]

3건 완결 / 2건 진행 중 / 1건은 인간(기술 지원 엔지니어 메러디스)이 처리 — 자동화와 인간 개입이 같은 화면에 병렬로 놓인 구조다.

> "오른쪽에는 분석 패널이 있는데, 여기에서 문제 요약부터 취해진 조치, 사건 발생 시점까지 모든 세부 정보를 확인할 수 있습니다." [S2]

> "그래서 우리 직원들은 기록 관리보다는 관계 구축에 집중할 수 있습니다." [S2]

이것이 이 사례에서 재배치의 목적지가 명시된 유일한 문장이다(IT편이 아니라 CS편).

**(c) 에스컬레이션 = 복잡도 임계 초과 시 인간 회귀 (S3 데모)**

> "특정 기술들이 이미 활성화되어 있는 것을 확인할 수 있고, 사례가 너무 복잡해지면 담당자가 처리할 수 있도록 이관되는 것도 알 수 있습니다." [S3]

**(d) 인간 개입이 필수인 워크플로가 남는다는 원칙 진술**

> "게다가, 우리 모두 알다시피 일부 워크플로는 사람의 개입이 필수적입니다 . 그런 경우에는 직원들이 충분히 처리하고 실현할 수 있습니다." [S3] (파반 샤, Moveworks 창립자)

> "이제 AI 에이전트가 특정 작업을 실행합니다. 바로 이런 부분에서 인간이 과정에 참여하고, 관여해야 하며, 상당한 창의적 판단력이 요구됩니다. 당신은 AI 에이전트가 특정 행동만 수행하도록 하고 싶을 것입니다." [S4]

S4는 여기서 "AI 에이전트(단일 과업, 인간이 루프에 있음)"와 "AI 전문가(전체 결과 인계)"를 개념적으로 구분한다. 즉 벤더 스스로 AUG 층과 AUTO 층을 제품 등급으로 분리해 놓았다.

**(e) 인간이 승인·구성 권한을 쥐는 지점**

> "따라서 활성화되면 전문가가 즉시 제 팀에 배정되고, 저는 언제든지 설정을 조정하거나 비활성화할 수 있는 완전한 권한을 갖게 됩니다." [S3]

> "하지만 만약 제가 그 모든 것을 기계가 처리하도록 하고 싶지 않다면 어떻게 해야 할까요? 내가 통제권을 갖고 싶다면 어떻게 해야 할까요 ?" … "따라서 모든 AI 전문가는 완벽하게 구성 가능합니다. 나는 그것이 할 수 있는 것과 할 수 없는 것을 정의한다 ." [S4]

**(f) 오케스트레이터 구조에서 인간의 위치 (S5)**

> "따라서 워크플로 계층에서 사람이 직접 의도 신호를 보내게 됩니다 ." [S5]

> "AI는 워크플로 경험 레이어에 계획을 다시 제시하고 " 이게 원하시는 작업인가요?"라고 묻습니다. 워크플로 경험 계층에서 승인을 내리면 오케 스트레이터는 작업이 실제로 완료될 때까지 에이전트를 순차적으로 실행합니다 ." [S5]

인간이 (1) 의도 입력 (2) 계획 승인 두 지점에 남는 구조. S5는 자사 사례가 아니라 제품 아키텍처 설명이므로, 자사 서비스데스크에서 이 승인 게이트가 실제로 걸려 있는지는 **해당 소스에 없음**.

**(g) 증강·대체를 벤더가 명시적으로 병렬 배치한 문장 (논문 대조상 중요)**

> "이제 우리는 여러분이 자율적인 AI 에이전트와 함께 증강, 추가, 대체, 공존할 수 있도록 지원합니다 ." [S5]

---

### 2.5 전환 메커니즘 (CYCLE)

**증강 → 자동화 방향의 전환 기준은 부분적으로만 확인된다.**

(1) **성과 관찰 기간을 두고 승격한다는 서술**

> "온보딩이 완료되면 해당 상담원의 성과를 일정 기간 동안 확인할 수 있습니다." [S1]

"일정 기간 확인" 이후 무엇이 바뀌는지(권한 확대인지, 자율 실행 승격인지)는 **S1에 명시 없음**.

(2) **사전 평가 점수 기반의 도입 결정 (S3 데모)**

> "평가 점수는 85%의 정확도를 보이며, 연간 약 2,000건의 사고를 처리하여 3,000시간 이상의 시간을 절약할 수 있을 것으로 예상됩니다." [S3]
> "이로써 자신감이 생겼으니, 이제 AI 전문가를 활성화하겠습니다. 그 사람을 우리 팀에 합류시키는 건 당연한 선택입니다 ." [S3]

즉 전환 기준은 "정확도 평가 점수 + 예상 절감 시간"이며, 관리자가 이를 보고 활성화를 결정한다. **단 이 장면은 FedEx IT 서비스데스크 관리자를 가정한 라이브 데모이지 ServiceNow 자사 운영 실적이 아니다.**

(3) **학습을 통한 점진적 개선 서술**

> "그들은 여러분의 팀과 함께 일하고, 여러분의 프로세스를 따르며, 시간이 지남에 따라 발전하고 더욱 똑똑해집니다." [S3]
> "모든 결정, 모든 행동, 그리고 모든 결과가 시스템에 반영되기 때문에 시간이 지날수록 시스템은 더욱 똑똑해집니다 ." [S4]
> "이는 일반적인 추론이 가능한 모델 과 특정 비즈니스에 맞춰 추론하고 실행할 때마다 개선되는 시스템의 차이점입니다." [S4]

이는 논문의 "증강 학습이 축적되어 견고화된다"는 시간축 서술과 형태가 같지만, **어느 임계에서 인간을 루프에서 빼는지에 대한 명시적 기준(threshold)은 5개 소스 어디에도 없다.**

(4) **자동화 → 증강 회귀(조건 변화 시 되돌림) 방향은 명시적 장치가 있다.**

> "우리는 당신에게 킬 스위치를 드립니다. 이 기능을 사용하면 작업을 도중에 일시 중지하거나, 방향을 바꾸거나, 모든 것을 멈출 수 있습니다." [S3]

> "저는 언제든지 설정을 조정하거나 비활성화할 수 있는 완전한 권한을 갖게 됩니다." [S3]

> "제가 지금 한 일은 ServiceNow Vaser를 사용하여 이 에이전트를 일시적으로 비활성화하고, 에이전트가 설계된 목적을 달성하기 위해 자체적으로 부여한 상승 권한을 제거하는 것입니다." [S4] ("Vaser"는 Veza의 자막 오기로 보인다)

**정리: 증강→자동화 승격의 성과 기준은 데모 수준에서만 확인되고 자사 운영 기준으로는 확인되지 않는다. 반대 방향(자동화→인간 회수)은 킬 스위치·비활성화·구성 변경이라는 명시적 장치로 확인된다. 이 비대칭 자체가 이 사례의 특징이다.**

---

### 2.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

#### SPILL — 확인됨. 그리고 6개월 사이에 "검토 중"에서 "출시 완료"로 진척됐다.

**T1 (업로드일 2025-11-17): 계획 단계**

> "그리고 그 경험을 통해 우리가 얻은 큰 교훈은 IT 분야에서 효과가 있다면 왜 거기서 멈춰야 하느냐는 것이었습니다. 그래서 저희는 현재 인사, 재무, 고객 지원, 영업 운영 전반에 걸쳐 자율적인 서비스 데스크를 도입하는 방안을 검토하고 있습니다." [S1]

"검토하고 있습니다" — 이 시점에서는 계획이다.

**T2 (업로드일 2026-05-07/08): 제품 출시 단계**

> "우리의 핵심 가치에 부합하게, 우리가 처음으로 선보인 AI 전문가는 IT 서비스 관리자였습니다." [S3]
> "오늘, CRM부터 직원 경험, 위험 보안 및 핵심 IT에 이르기까지 전사적으로 새로운 AI 전문가를 영입하여 자율적인 업무 환경을 확대하게 되었음을 기쁜 마음으로 알려드립니다. 예를 들어, 고객 서비스 부문에는 사례 관리 AI 전문가가 있고, 보안 부문에는 위험 및 취약성 전문가가 있습니다." [S3]

> "더욱 흥미로운 점은 IT 분야에서 효과적인 전략이 비즈니스의 다른 모든 영역에서도 효과적이라는 것입니다 ." [S4]
> "어제 저희는 여러분 사업의 모든 영역을 담당할 20명의 새로운 AI 전문가를 영입했다고 발표했습니다 . 자, IT 전문가 여러분 , 제가 도와드리겠습니다. 인사팀, 저희가 도와드리겠습니다. 고객 서비스도 제공됩니다. 금융 분야라면 당연히 당신을 위한 분야가 있습니다. 보안, 당신도 알잖아요." [S4]

S1이 예고한 4개 영역(인사, 재무, 고객 지원, 영업 운영)과 S4의 열거(IT, 인사, 고객 서비스, 금융, 보안)는 완전히 일치하지는 않는다(S1의 "영업 운영"은 S4 열거에 없고, S4의 "보안"은 S1 예고에 없다).

**중요한 귀속 문제**: S1의 SPILL은 *자사 내부* 확산 계획인 반면, S3/S4의 20개 AI 전문가는 *고객에게 판매하는 제품 라인업* 확대다. 두 문장은 표면상 같은 "IT에서 다른 영역으로"라는 형태지만 **주체가 다르다**. S3/S4에서 자사 내부의 인사·재무·영업운영 서비스데스크가 실제로 가동 중이라는 진술은 없다. 자사 내부 확산으로 읽을 수 있는 유일한 T2 진술은 다음이다.

> "저희 회사의 직원 경험 개선 프로그램은 재키 키니에게 직접 물어보시면 아시겠지만, 230만 시간 의 업무 시간 절감을 가져왔습니다." [S3]

**인접 과업으로의 파급이 "새로운 인간 증강 과업"을 유발했다는 논문식 SPILL(한 과업 자동화 → 인접 과업의 증강 유발)의 직접 근거는 5개 소스 어디에도 없다.** 확인되는 것은 "자동화의 인접 영역 복제"이지 "자동화가 인접 영역의 증강을 촉발"은 아니다. 유일하게 근접한 서술은 외부 발화자(NVIDIA CEO)의 것이다.

> "이제 모든 직원이 상담원을 이용하고 있고, 이전보다 훨씬 더 바빠졌습니다. 그 이유는 이제 그들이 자유로워지고 , 승진하여 이전에는 상상도 못 했던 문제들을 해결하고 야망을 추구할 수 있게 되었기 때문입니다 ." [S3] (젠슨 황 — **ServiceNow 자사 사례가 아니라 NVIDIA 사내 사례**)

#### REINV — 부분 확인. 단, 회수 자원의 재투자처가 정량화되지 않는다.

**(a) 자원 회수는 명시적으로 정량화된다**

> "지나는 2025년에 우리가 지금 당장 어시스트 덕분에만 5억 달러를 절약했다고 ​​말할 거예요 ." [S3]
> "저희 회사의 직원 경험 개선 프로그램은 재키 키니에게 직접 물어보시면 아시겠지만, 230만 시간 의 업무 시간 절감을 가져왔습니다." [S3]

**(b) 재투자 방향은 서술적으로만 제시된다**

> "한번 생각해 보세요. 그건 복사 붙여넣기나 티켓 라우팅 과정으로 이어지지 않았어요. 실제로 사람들이 다시 일을 할 수 있게 되었고, 인공지능이 매번 정확하게 실행해 주기 때문에 사람들은 다시 즐겁게 일할 수 있게 되었습니다 ." [S3]

"복사 붙여넣기나 티켓 라우팅으로 가지 않았다"는 부정형 진술이며, 절감된 230만 시간이 구체적으로 어떤 증강 과업에 투입됐는지는 **해당 소스에 없음**. 논문의 UBS 패턴(자동화로 확보한 자원을 명시적으로 증강 역량에 재투자)과 비교하면 회수 측만 있고 투입 측이 비어 있다.

**(c) 재투자 원칙을 언어로 정식화한 것은 외부 발화자다**

> "리더들이 AI를 생각할 때, 생산성 향상이라는 관점에서만 생각해서는 안 됩니다. 생산성 향상과 그에 따른 비용 절감을 함께 고려해야 합니다. 생산성을 생각하고, 그로 인해 목표 의식이 높아진다고 봐야 한다고 생각합니다. 인력을 줄이는 대신 재배치하고, 직원 활용 방식을 재고하고, 더 많은 성과를 내도록 노력해야 합니다." [S3] (젠슨 황, NVIDIA CEO — ServiceNow 자사 진술 아님)

---

### 2.7 통합 장치 (RESP)

이 사례에서 가장 근거가 두터운 항목이다. 다섯 층으로 나뉜다.

**(1) 거버넌스가 워크플로에 "내장"된다는 원칙 (S1이 T1에 이미 선언)**

> "통치 체계 또한 그 안에 내재되어 있습니다. 이제 AI 관제탑을 통해 AI 자산의 전체 수명 주기를 실제로 모니터링할 수 있게 되었습니다." [S1]

("통치 체계"는 governance의 기계번역으로 보인다. 원문 그대로 인용함.)

**(2) 관제탑의 제품적 정의 (S5, 2025-09-24)**

> "AI 관제탑이란, 데이터 모델에서 우리가 만든 AI 자산이라는 새로운 자산 유형에 대응하기 위해 통합된 위험 관리 및 SPM을 결합한 시스템입니다 ." [S5]
> "따라서 워크플로우 자체 에 위험 관리 정책이 내장되어 있으므로, 워크 플로우를 통해 은행 전체에 걸쳐 관리할 수 있습니다. 그래서 사람이 실수할 수가 없어요." [S5]
> "하지만 타사 LLM을 도입하거나 다른 AI 자산을 추가하려는 경우, 법무팀, CISO 및 규정 준수팀이 하나의 통합된 화면에서 모든 AI 자산의 현황을 쉽게 파악할 수 있습니다." [S5]

"그래서 사람이 실수할 수가 없어요" [S5] 는 논문의 RESP(인간이 책임을 보유)와 미묘하게 다르다. 여기서는 정책을 워크플로에 박아 넣어 **인간의 재량 자체를 축소**함으로써 규정 준수를 달성한다. 책임 보유가 아니라 재량 제거에 가깝다.

**(3) 감사추적 (모든 소스에 반복)**

> "다시 한번 말씀드리지만, 저는 이 AI 전문가가 수행하는 단계를 정확히 볼 수 있으므로 , 작업이 어떻게 완료되었는지 조사하고 올바른 단계를 거쳤는지 확인해야 할 경우 감사 추적 기록을 확보할 수 있습니다." [S3]
> "하지만 우리는 정해진 안전장치 안에서 일을 처리합니다. 그래서 사람과 에이전트가 하는 모든 일에 대한 완벽한 감사 기록이 남습니다 ." [S3]
> "따라서 완벽한 가시성, 완벽한 감사 추적, 그리고 완벽한 제어 권한을 얻게 됩니다." [S4]
> "모든 전문가는 당사 플랫폼을 보호해 온 동일한 거버넌스 프레임워크를 준수하며 , 현재 이 프레임워크를 통해 매년 1000억 건 이상의 워크플로우가 처리되고 있습니다. 그리고 이들은 인간 직원과 동일한 접근 제어 시스템으로 보호됩니다 ." [S3]
> "이들은 모두 기존 업무 그룹 및 기존 관리 체계 내에서 운영됩니다." [S4]

**(4) 중단권 / 킬 스위치**

> "우리는 당신에게 킬 스위치를 드립니다. 이 기능을 사용하면 작업을 도중에 일시 중지하거나, 방향을 바꾸거나, 모든 것을 멈출 수 있습니다." [S3]
> "버튼 하나만 누르면 플랫폼이 즉시 작동하여 모든 권한을 제거하고 해당 에이전트를 비활성화하는 것을 확인할 수 있습니다. 관제탑이 출혈을 멈췄다. 또한 전체 감사 추적 기록을 제공합니다." [S3]

**(5) 승인권의 위치 — 두 방향이 공존한다**

인간 승인이 남는 쪽:
> "그래서 제가 검토하고 모든 것이 제대로 되어 있는지 확인한 후 제출합니다." [S3] (구매 요청 승인 데모)
> "따라서 AI 전문가인 SAM은 먼저 사용하지 않는 라이선스를 회수하고, 그에 따른 차액을 조달하는 한편, 재무 및 구매 부서에 승인을 보내고, 52명의 모든 직원에게 적극적으로 상황을 업데이트합니다. 승인이 완료되는 즉시 접근 권한이 부여됩니다." [S4]

승인이 자동화되는 쪽:
> "예전에는 승인받기까지 며칠씩 기다려야 했는데, 지금은 좀 달라졌네요. 자동 승인 시스템은 해당 애플리케이션이 모든 승인 기준을 충족한다는 것을 알고 있으므로 자동으로 승인됩니다 ." [S3] (휴가 신청 데모)

**(6) 자율성 수준을 명시적으로 인정한 유일한 문장 (S4, CVS 보안 데모)**

> "우리는 사람이 직접 개입하는 방식으로 전 과정에 걸친 확산 방지 조치를 실행했습니다 ."  [S4]
> "이 사용 사례에서 CVS Health의 현재 자율 운영 방식은 사람이 개입해야 한다는 점에 유의해야 합니다. 하지만 AI 관제탑은 모니터링부터 이상 징후 식별, 문제 해결에 이르기까지 완전 자율적으로 작동할 수도 있습니다." [S4]

이 문장은 벤더가 스스로 "현행은 human-in-the-loop, 기술적으로는 완전 자율 가능"이라는 두 상태를 구분한 드문 사례다. **단 이는 CVS Health(고객사) 사례이지 ServiceNow 자사 사례가 아니다.**

**(7) 고객사가 말하는 거버넌스 조건 (자사 사례와 구분)**

> "우리는 기업 전반에 걸쳐 AI 에이전트를 확장하면서 인간 직원과 전혀 다르게 대우하지 않습니다. 그래서 우리는 그들을 인간 팀과 마찬가지로 엄격한 기준과 정책으로 관리해야 하는 디지털 인력으로 간주합니다." [S3] (비샬 탈와르, FedEx)
> "우리가 AI 관점에서 살펴보는 모든 것은 개인정보 보호, 법률, 보안 및 거버넌스와 관련이 있으며, 그렇지 않은 경우에는 진행하지 않습니다 . 마침표." [S4] (앨런 로사, CVS Health CISO)
> "저희가 ServiceNow와 파트너십을 맺고 Control Tower에 기대를 거는 이유 중 하나는, 사람의 개입이 적은 영장 발부 시스템을 구축하고 있기 때문입니다 . 너무 느려요." [S4] (앨런 로사 — 인간 개입을 **줄이는** 것이 목표라고 명시)

---

### 2.8 성과 수치

**A. ServiceNow 자사(dogfooding) 수치**

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| IT 지원 요청 AI 처리율 | 소스에 없음 | "저희 IT 지원 요청의 90%는 AI를 통해 처리됩니다." | [S1] 업로드 2025-11-17 | 벤더 자체보고 (제3자 검증 없음) |
| 서비스 요청 AI 지원율 | 소스에 없음 | "서비스 요청의 91%는 AI의 지원을 받습니다." | [S3] 업로드 2026-05-07 | 벤더 자체보고 |
| IT 지원 요청 자율 처리율 | 소스에 없음 | "IT 지원 요청의 90%가 자율적으로 처리됩니다" | [S4] 업로드 2026-05-08 | 벤더 자체보고 (자사 CIO 발언) |
| IT 지원 담당자 재배치 | 소스에 없음 | "IT 지원 담당자의 85%가 더 가치 있는 음악 관련 업무에 재배치되었습니다" | [S1] | 벤더 자체보고. **S2~S5에서 한 번도 반복되지 않음** |
| 직원 수 | — | "26,000명" | [S1] | 벤더 자체보고 |
| 연간 사용자 상호작용 | — | "매년 백만 건" | [S1] | 벤더 자체보고 |
| IT 헬프데스크 해결 속도 | "사람이 직접 응대할 때" | "99% 더 빠르게 문제를 해결할 수 있습니다" | [S3] | 벤더 자체보고. before 절대값 없음 |
| Now Assist 절감액 | — | "2025년에 우리가 지금 당장 어시스트 덕분에만 5억 달러를 절약했다고" | [S3] | 벤더 자체보고, 전언 형식("지나는 …말할 거예요") |
| 직원경험 프로그램 시간 절감 | — | "230만 시간 의 업무 시간 절감" | [S3] | 벤더 자체보고, 전언 형식("재키 키니에게 직접 물어보시면 아시겠지만") |
| 고객사 수 / 성장률 | — | "14,000명 이상의 고객", "매출은 매년 20% 이상 성장" | [S2] | 벤더 자체보고 |
| 고객 셀프서비스율 | 소스에 없음 | "고객은 89%의 경우 셀프 서비스를 이용할 수 있습니다" | [S2] | 벤더 자체보고 |
| 사건 처리 생산성 | 소스에 없음 | "생산성을 15% 향상시킬 수 있을 것으로 기대합니다" (**기대치, 실적 아님**) | [S2] | 벤더 자체보고, 예상치 |
| 고객만족 지수 | — | "SEESAD 지수가 9점을 넘는 상태를 7분기 연속으로 유지" | [S2] | 벤더 자체보고. "SEESAD"는 CSAT류 지표의 자막 오기로 보이나 원문 그대로 표기 |
| 플랫폼 처리량 | — | "연간 1,000 억 건의 워크플로우 와 7조 건의 트랜잭션" | [S3], [S4] | 벤더 자체보고. 자사 서비스데스크 물량이 아니라 전 고객 합산 |
| Fortune 500 도입률 | — | "Fortune 500 기업의 90%" [S3] / "포춘 500대 기업의 92%" [S5] | [S3], [S5] | 벤더 자체보고. **두 소스가 다른 값** |

**B. 데모 화면상의 수치 (실적 아님 — 라이브 데모 내 가상 시나리오)**

| 지표 | 값 | 소스 | 비고 |
|---|---|---|---|
| AI 전문가 평가 점수 | "평가 점수는 85%의 정확도를 보이며, 연간 약 2,000건의 사고를 처리하여 3,000시간 이상의 시간을 절약할 수 있을 것으로 예상됩니다." | [S3] | FedEx IT 서비스데스크 관리자를 가정한 데모 |
| AI 전문가 업무 흡수율 | "저희 팀으로 들어오는 업무의 52%를 처리하고 있으며, 그중 절반 이상은 자율적으로 처리됩니다" | [S3] | 같은 데모의 "몇 주 후" 가상 시점 |
| 생산성 환산액 | "생산성 향상으로 인한 2억 5천만 달러라는 거창한 수치" | [S3] | AI 관제탑 데모 화면 |

**C. 고객사·제3자 수치 (자사 사례와 구분)**

| 조직 | 지표 | 소스 | 성격 |
|---|---|---|---|
| NVIDIA | "직원 개입이나 직원 지원 문제와 관련된 상호 작용 횟수를 2/3로 줄였습니다." | [S3] | 고객사 CEO 자체보고 |
| CVS Health | "상담원과의 실시간 채팅이 50% 감소" | [S3] | ServiceNow가 대신 인용 |
| Honeywell | "Honeywell 팀의 인바운드 업무는 80% 감소했습니다" | [S3] | ServiceNow가 대신 인용 |
| CrowdStrike | "우리는 이미 에이전트형 AI를 통해 30% 이상의 생산성 향상을 달성하고 있습니다" | [S3] | 고객사 영상 증언 |
| CVS Health | "250만 건 이상의 AI 대화를 제공하여", "22만 명이 이 플랫폼을 이용하고 있습니다", "현재 465만 개의 플러그인이 활용되고 있습니다", "저희는 서비스 센터 운영으로 걸려오는 전화 25만 5천 통을 줄이는 것에 대해 이야기하고 있습니다", "우리는 약 1년 만에 해당 제품과 200만 건 이상의 대화를 나눴습니다", "저희 반품 률은 75%가 넘습니다" | [S4] (모두 S4 내부) | 고객사 CISO 앨런 로사 발언 및 CVS 영상, 일부는 ServiceNow 임원이 대신 인용. **250만 건과 200만 건이 같은 소스 내 병존** |
| Adobe | "장애 복구 속도를 25% 향상" | [S4] | ServiceNow가 대신 인용 |
| Bell | "배차 관련 업무의 90%를 완전 자동화" | [S4] | ServiceNow가 대신 인용 |
| Siemens | "매달 21만 건의 티켓을 자동으로 해결" | [S4] | ServiceNow가 대신 인용 |
| FedEx | "매달 500만 건의 ServiceNow 워크플로우" | [S3] | 고객사 영상 |
| (NVIDIA 협업 제품영상) | "티켓의 90%는 자율 에이전트에 의해 해결되므로 엔지니어는 가장 어려운 문제에 집중할 수 있습니다" | [S3] | **귀속 불명**. ServiceNow+NVIDIA 공동 제품 영상 내 문장이며 자사 실적인지 NVIDIA 실적인지 소스가 명시하지 않음 |
| (시장 통계) | "실제로 AI를 통해 가치를 얻는 기업은 19%에 불과합니다", "에이전트형 AI를 통해 2.5배 더 나은 결과" | [S4] | 출처 미표기 |
| (시장 통계) | "오늘날 기업의 95%는 그 질문에 답할 수 없습니다", "10개 기업 중 6개 기업이 유전자 기반 AI를 사용하고 있지만, 자율 시스템을 구축한 기업은 10개 기업 중 단 한 곳뿐", "평균적으로 사용하는 367개의 서로 다른 애플리케이션" | [S3] | 출처 미표기 |

**제3자 검증치는 5개 소스 전체에 하나도 없다.** 모두 벤더 자체보고이거나 벤더가 인용한 고객 자체보고다.

---

### 2.9 소스 간 교차 대조

#### (1) 반복 확인된 사실

- **"IT 지원 요청의 90%"**: [S1](2025-11-17)과 [S4](2026-05-08) 두 시점에서 동일한 90%로 반복된다. 약 6개월 간격에도 값이 갱신되지 않았다.
- **AI 관제탑(Control Tower)**: [S1] "이제 AI 관제탑을 통해 AI 자산의 전체 수명 주기를 실제로 모니터링할 수 있게 되었습니다", [S5] 제품 정의, [S3] 회사 정체성 선언 "ServiceNow는 비즈니스 혁신을 위한 AI 관제탑입니다", [S4] 보안 데모. 4개 소스에서 일관되게 등장하며 T1(2025-09~11)의 모니터링 기능에서 T2(2026-05)의 "엔드투엔드 솔루션"으로 범위가 확대된다: "저희는 AI 컨트롤 타워를 가시성 및 관리 기능에서 포괄적인 엔드투엔드 솔루션으로 발전시켰으며" [S3].
- **에이전트 채용/온보딩 은유**: [S1] "즉시 채용하거나 온보딩할 수 있는 여러 명의 에이전트 직원", [S3] "마치 새로운 팀원을 영입하는 것처럼", [S4] "그렇게 간단하게 온보딩이 완료되었습니다", [S3-FedEx] "디지털 인력으로 간주합니다". 4개 소스에서 반복.
- **에이전트를 인간과 동일한 접근통제로 관리**: [S3] "인간 직원과 동일한 접근 제어 시스템으로 보호됩니다", [S3-NVIDIA] "그래서 이제 인간 요원과 AI 요원이 있고, 이들은 기본적으로 같은 방식으로 운영됩니다", [S4] "이들은 모두 기존 업무 그룹 및 기존 관리 체계 내에서 운영됩니다".
- **감사추적**: [S3] 2회 이상, [S4] 2회 이상, [S1] "통치 체계 또한 그 안에 내재되어 있습니다".
- **IT → 타 영역 확산 논리**: [S1] "IT 분야에서 효과가 있다면 왜 거기서 멈춰야 하느냐" ↔ [S4] "IT 분야에서 효과적인 전략이 비즈니스의 다른 모든 영역에서도 효과적이라는 것입니다". 사실상 같은 문장이 6개월 간격으로 반복된다.

#### (2) 한 소스에만 있는 사실

- **26,000명 직원** — [S1]에만. S3의 "2만 5천 명"/"25,000명"은 **행사 참석자 수**이지 직원 수가 아니다("라스베이거스에는 제 가장 친한 친구 2만 5천 명이 있습니다" [S3], "현재 이곳에 있는 25,000명의 모든 서비스 요청은 ServiceNow에서 감지, 라우팅 및 해결됩니다" [S3]). 혼동 주의.
- **연 100만 건 상호작용** — [S1]에만.
- **IT 지원 담당자 85% 재배치** — [S1]에만. **6개월 후 S3/S4 두 개의 대형 키노트 어디에도 이 수치가 재등장하지 않는다.** 자동화 성과(90%)는 반복되는데 인력 재배치 성과(85%)는 사라진 것이 이 사례에서 가장 눈에 띄는 비대칭이다.
- **89% 셀프서비스, 15% 생산성 기대, SEESAD 9점 7분기** — [S2]에만.
- **5억 달러 절감, 230만 시간, 91%, 99% 더 빠름** — [S3]에만. S4에서 재확인되지 않는다.
- **200개 이상 시스템 통합, Raptor DB 5~10배, 90일마다 AI 기능 2배** — [S5]에만.
- **20명의 새로운 AI 전문가** — [S4]에만 숫자로 명시(S3은 열거만 하고 개수를 말하지 않는다).

#### (3) 시점에 따른 서술 변화 (이 사례의 핵심)

| 축 | T0 [S5] 2025-09-24 | T1 [S1][S2] 2025-11-17 | T2 [S3][S4] 2026-05-07/08 |
|---|---|---|---|
| 지원 요청 처리 비율 | 없음 | "IT 지원 요청의 90%는 **AI를 통해 처리**됩니다" [S1] | "서비스 요청의 **91%는 AI의 지원을 받습니다**" [S3] / "IT 지원 요청의 **90%가 자율적으로 처리**됩니다" [S4] |
| 인력 효과 | 없음 | "IT 지원 담당자의 **85%가 …재배치**" [S1] | **언급 없음** |
| IT → 타영역 | 없음 | "**검토하고 있습니다**" [S1] | "**출시**" / "20명의 새로운 AI 전문가를 영입했다고 발표" [S4] |
| 인간 개입 서술 | "사람이 직접 의도 신호를 보내게 됩니다"·"승인을 내리면" [S5] | "사람의 개입 없이 자동으로 해결 방법을 실행" [S1] | "일부 워크플로는 사람의 개입이 필수적입니다" [S3] / "완전 자율적으로 작동할 수도 있습니다" [S4] |
| 관제탑 범위 | "통합된 위험 관리 및 SPM을 결합한 시스템" [S5] | "AI 자산의 전체 수명 주기를 …모니터링" [S1] | "30개 이상의 다양한 시스템과 연결", "킬 스위치", "섀도우 AI 탐지" [S3][S4] |
| 에이전트 단위 | "단일 목적 에이전트" + "AI 에이전트 오케스트레이터" [S5] | "지원 분석가 템플릿" [S1] | "AI 에이전트(작업 단위) vs AI 전문가(역할 단위)" 이원 구분 [S4] |

**가장 중요한 변화는 값이 아니라 술어다.** 90%라는 값은 유지되는데 술어가 "AI를 통해 처리됩니다" [S1] → "자율적으로 처리됩니다" [S4]로 강화된다. 그 사이 S3은 "AI의 지원을 받습니다"라는 **더 약한** 술어로 91%를 말한다. 즉 하루 차이의 두 키노트에서 (91%, AI 지원) → (90%, 자율)로 값은 1%p 내려가고 자율성 주장은 올라간다.

#### (4) 모순 / 긴장

- **91% vs 90%**: [S3](2026-05-07) "서비스 요청의 91%"와 [S4](2026-05-08) "IT 지원 요청의 90%". 분모가 "서비스 요청"과 "IT 지원 요청"으로 다르므로 직접 모순은 아니나, 두 키노트가 하루 간격이고 청중이 겹친다는 점에서 동일 사실의 두 판본으로 읽힌다.
- **Fortune 500 도입률**: [S3] "Fortune 500 기업의 90%" vs [S5] "포춘 500대 기업의 92%". S5(2025-09)가 더 높고 S3(2026-05)이 더 낮다. 시간 순으로 감소한 셈이라 최소한 하나는 부정확하다.
- **CVS Health 대화 건수**: 같은 [S4] 안에서 "250만 건 이상의 AI 대화" (아밋 인용)와 "약 1년 만에 해당 제품과 200만 건 이상의 대화를 나눴습니다" (CVS 영상)가 병존한다.
- **승인 자동화 vs 인간 승인**: [S3] 안에서 구매 요청은 인간이 검토·제출("그래서 제가 검토하고 모든 것이 제대로 되어 있는지 확인한 후 제출합니다")하는데 휴가 신청은 "자동으로 승인됩니다"로 처리된다. 승인권이 남는 기준이 소스 내에서 설명되지 않는다.
- **"사람이 실수할 수가 없어요" [S5] vs "사람의 개입이 적은 …시스템을 구축" [S4-CVS] vs "일부 워크플로는 사람의 개입이 필수적입니다" [S3]**: 인간 재량에 대한 세 진술이 서로 다른 방향을 향한다.
- **"자율" 정의의 유동성**: [S4]는 CVS 사례에 대해 "현재 자율 운영 방식은 사람이 개입해야 한다는 점에 유의해야 합니다"라고 하면서도 그 방식을 계속 "자율 운영"이라 부른다. 벤더 어휘에서 "자율(autonomous)"이 human-in-the-loop을 포함한다.

---

### 2.10 논문 대조

| 논문 명제 (쪽수) | 이 사례의 대응 | 지지 / 보강 / 확장 / 반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간을 루프에서 제외 (p.194) | "티켓을 자체적으로 할당한 다음 사람의 개입 없이 자동으로 해결 방법을 실행합니다" [S1]; "IT 지원 요청의 90%가 자율적으로 처리됩니다" [S4] | **지지**. 교과서적 대응 |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | "세 번째 사건에 대해서는 그녀가 조치를 취해야 합니다" [S2]; "사례가 너무 복잡해지면 담당자가 처리할 수 있도록 이관" [S3]; "바로 이런 부분에서 인간이 과정에 참여하고, 관여해야 하며, 상당한 창의적 판단력이 요구됩니다" [S4] | **지지**. 단 자사 IT편[S1]에는 AUG 서술이 없고 CS편[S2]·고객사 데모[S3][S4]에 있다 |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | "성과를 일정 기간 동안 확인할 수 있습니다" [S1]; "평가 점수는 85%의 정확도" [S3]; "시간이 지남에 따라 발전하고 더욱 똑똑해집니다" [S3] | **부분 지지 / 근거 빈약**. 학습→자동화 승격의 임계 기준이 어느 소스에도 없다 |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 킬 스위치 [S3]; "언제든지 설정을 조정하거나 비활성화" [S3]; "이 에이전트를 일시적으로 비활성화하고 …상승 권한을 제거" [S4] | **보강**. 논문의 회귀는 환경 변화에 따른 조직적 재조정인데, 이 사례는 그것을 *제품 기능(버튼)*으로 사물화했다 |
| SPILL: 한 과업 자동화가 인접 과업의 증강을 유발 (p.197) | "IT 분야에서 효과가 있다면 왜 거기서 멈춰야 하느냐" [S1] → 20개 AI 전문가 출시 [S4] | **반증 아님, 그러나 변형**. 관찰되는 것은 인접 과업의 *증강*이 아니라 인접 과업의 *자동화 복제*다. 증강 유발 근거는 소스에 없음 |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS) | "5억 달러", "230만 시간" [S3] 회수는 정량화; "그건 복사 붙여넣기나 티켓 라우팅 과정으로 이어지지 않았어요" [S3] | **부분 지지**. 회수 측은 정량, 투입 측은 부정형 서술뿐. UBS 패턴의 절반만 확인됨 |
| RESP: 인간이 프로세스 전체 책임/승인/감사를 보유 (p.200) | 감사추적 반복 [S1][S3][S4]; 킬 스위치 [S3]; "모든 AI 전문가는 완벽하게 구성 가능합니다. 나는 그것이 할 수 있는 것과 할 수 없는 것을 정의한다" [S4] | **지지 + 확장**. 다만 "그래서 사람이 실수할 수가 없어요" [S5]는 책임 보유가 아니라 재량 제거 방향이라 논문과 결이 다르다 |
| p.195 증강 학습은 도메인 전문가의 암묵지에 의존하며 IT부서/외부업체에 위임 불가 | "지난 20 년간 IT, HR, 구매, CRM 등 다양한 분야에서 서비스 관리 사고를 처리하는 방식에 대한 모든 노하우를 바탕으로 구축된 수백 개의 즉시 사용 가능한 에이전트" [S5]; "고객의 비즈니스 상황을 저희보다 더 잘 이해하는 곳은 없습니다" [S4]; "그들은 백지상태에서 시작하는 것이 아닙니다" [S4] | **반증 방향의 도전**. 벤더는 도메인 암묵지를 *플랫폼 축적물*로 재정의하고 이를 즉시 사용 가능한 형태로 외부에 판매한다. 다만 반대 근거도 같은 소스에 있다: CVS는 "7개월 프로젝트"와 내부 정렬을 거쳐야 했다 — "이것은 제품 선택의 문제가 아니라 운영 모델, 즉 사람들이 일하는 방식의 변화였습니다" [S4] |
| p.198 기계 한계 4가지 (목적/자아 부재, 제약 완화된 옵션만 제시, 훈련된 과업에 국한, 감각/감정/사회기술 부재) | "그러니까, 그들은 자기 분야에서는 정말 뛰어나지만 , 막상 경기장에 나가면 좀 멍청한 면이 있어요 . 그들은 경기장에서 어떻게 뛰어야 하는지 몰라요 ." [S5]; "이러한 AI 전문가들은 특정 작업을 수행하도록 훈련된 에이전트입니다" [S4] | **지지 (훈련된 과업 국한)**. 감각/감정 한계는 오히려 Google 파트너 발화가 보완 시도를 언급: "감정을 이해해서 같은 일을 반복한다는 느낌을 받지 않도록 하기 위해서입니다" [S4] |
| p.199 한쪽 편중 시 악순환 | "규칙과 틀이 없는 지능은 위험한 맹점이다" [S3]; 프롬프트 주입으로 배송비 1달러 사고 데모 + "이 요원은 혼자 활동하지 않습니다 . …작동 중인 매 순간, 폭발 반경이 커집니다" [S3] | **보강**. 논문의 악순환이 조직 역량 침식이라면, 이 사례는 *기술적 전파(blast radius)* 형태의 악순환을 제시한다 |
| p.204 기계는 조직 내 새로운 행위자 계급 | "즉시 채용하거나 온보딩할 수 있는 여러 명의 에이전트 직원" [S1]; "디지털 인력으로 간주합니다" [S3]; "인간 직원과 동일한 접근 제어 시스템으로 보호됩니다" [S3]; "약 1200억 개의 세부적인 권한 정보" [S4]; "VESA는 인간 및 비인간을 포함한 모든 신원을 지원합니다" [S3] | **강한 확장**. 새 행위자 계급이 은유가 아니라 *신원 관리 인프라(identity, 권한, 감사, 해고=kill switch)* 로 제도화되어 있다 |

**이 사례가 논문을 확장하는 지점.** Raisch & Krakowski의 자동화-증강 역설은 조직이 시간에 걸쳐 두 논리 사이를 오가는 *관리 딜레마*로 서술된다. 이 사례가 보태는 것은, 그 딜레마의 조정 장치가 여기서는 조직 프로세스가 아니라 **판매 가능한 제품 기능**으로 응고되어 있다는 점이다. 회귀 가능성은 "킬 스위치" [S3]로, 인간의 책임 보유는 "완벽한 감사 추적" [S4]로, 새 행위자 계급의 편입은 "인간 직원과 동일한 접근 제어 시스템" [S3]과 액세스 그래프의 "약 1200억 개의 세부적인 권한 정보" [S4]로 구현된다. 즉 논문이 조직에 요구하는 통합 조건(RESP)이 플랫폼 벤더에 의해 선(先)제공되고, 개별 조직은 그것을 구매해 켜는 쪽으로 이동한다.

둘째 확장점은 **자기적용(dogfooding)이 성과 서사를 어떻게 왜곡하는가**다. ServiceNow는 자사 서비스데스크 사례를 자사 제품의 증거로 사용하므로, 자동화율(90%)은 반복 갱신·강화되지만 재배치된 85% 인력이 무슨 일을 하게 됐는지는 6개월 뒤 두 개의 대형 키노트에서 사라진다 [S1][S3][S4]. 논문의 REINV가 성립하려면 회수와 투입이 모두 관측 가능해야 하는데, 벤더의 자기서사에서는 회수만이 판매 논거가 되므로 투입 측이 구조적으로 관측 불가능해진다. 이는 논문 명제의 반증이 아니라, **논문이 요구하는 관측 조건이 벤더 자체보고 자료에서는 체계적으로 충족되지 않는다**는 방법론적 확장이다.

셋째로, "자율(autonomous)"이라는 술어가 human-in-the-loop을 포함한 채 사용된다는 사실 [S4: "현재 자율 운영 방식은 사람이 개입해야 한다는 점에 유의해야 합니다"]은 논문의 AUTO/AUG 이분법이 실무 담론에서 이미 붕괴해 있음을 보여준다. 연구자는 벤더가 "자율"이라 부르는 것을 자동으로 AUTO로 코딩해서는 안 된다.

---

### 2.11 인용 시 주의사항

1. **전부 벤더 자체보고다.** 5개 소스 모두 ServiceNow 공식 유튜브 채널의 마케팅 자산(브랜디드 dogfooding 영상 2편, 자사 컨퍼런스 키노트 2편, 파트너 세일즈 인에이블먼트 세션 1편)이다. 제3자 검증치는 하나도 없다. 고객사 수치(CVS, FedEx, NVIDIA, Adobe, Bell, Siemens, CrowdStrike, DocuSign, Honeywell)도 벤더가 인용한 고객 자체보고이며, 상당수는 고객 본인이 아니라 ServiceNow 임원이 대신 말한 것이다.

2. **성숙도 구분이 필수다.** (a) 자사 운영 실적: [S1] 90%/85%, [S2] 89%, [S3] 91%/5억 달러/230만 시간. (b) 계획: [S1] "도입하는 방안을 검토하고 있습니다". (c) 기대치: [S2] "15% 향상시킬 수 있을 것으로 기대합니다". (d) **라이브 데모 내 가상 수치**: [S3] 85% 정확도/2,000건/3,000시간/52%, 2억 5천만 달러 — 이들은 무대 시연 화면의 값이므로 운영 실적으로 인용하면 오류다. (e) 미출시: [S5] "아직 배송은 시작되지 않았지만, 올해 말에 배송될 예정입니다" (AI 에이전트 패브릭).

3. **자막 오류가 다수다.** 기계번역 한국어 자막이며 아래 표현은 원문 그대로 인용해야 하지만 의미 판독 시 주의가 필요하다.
   - "더 가치 있는 음악 관련 업무에 재배치되었습니다" [S1] — [음악] 자막 태그가 문장에 삽입된 것으로 보임. **재배치 목적지를 이 문장에서 읽어내면 안 된다.**
   - "음악이 미치는 영향은 엄청납니다", "저희는 실제로 음악이라는 매체를 통해" [S2] — 동일 유형.
   - "통치 체계 또한 그 안에 내재되어 있습니다" [S1] — governance의 오역.
   - "SEESAD 지수가 9점을 넘는" [S2] — CSAT류 지표명의 음차 오기로 보이나 확인 불가.
   - "AIA 상담원" [S2] — AI agent의 오기로 보임.
   - "ServiceNow Vaser" [S4] — Veza의 오기로 보임. 같은 영상에서 "베자의 공동 창립자 겸 CEO인 타룬 시크리" [S4], "Vissa Access Graph" [S4], "VESA는 인간 및 비인간을 포함한 모든 신원을 지원합니다" [S3]로도 표기됨 — **동일 제품이 최소 4가지 표기로 등장**.
   - "유전자 기반 AI" [S3], "유전학 기반 비즈니스" [S3] — generative/agentic의 오역.
   - "LLM(법학 석사)" [S3], "LLM(Learning Leadership Model)" [S5], "AIE(Advanced Industry Enterprise)" [S5] — 자막 엔진이 삽입한 잘못된 확장어. **인용 시 이것이 ServiceNow의 공식 표현인 것처럼 다루면 안 된다.**
   - "Pocket OS의 AI 오류" [S3] — 제품명 음차 오류. 인명 표기도 같은 소스 안에서 흔들린다: [S3]은 같은 인물을 "아 미트"와 "아미트"로, Moveworks 창립자를 "보반 샤 씨를 무대 위로 모시겠습니다"와 "파반, 이 순간 당신과 함께"로 다르게 적는다. [S4]는 "넨샤드"(2회)와 "네나드"(1회)를, 화자 이름을 "아미트"·"아 미트"·"아흐메트"·"아미르"로 혼용한다.

4. **귀속 문제.** [S3]에 등장하는 "티켓의 90%는 자율 에이전트에 의해 해결되므로 엔지니어는 가장 어려운 문제에 집중할 수 있습니다"는 ServiceNow-NVIDIA 공동 제품 영상 내 문장으로, 자사 IT 서비스데스크 실적인지 NVIDIA 사례인지 소스가 명시하지 않는다. [S1]의 90%와 값이 같아 혼동하기 쉬우니 별도 인용해야 한다.

5. **"25,000명"을 직원 수로 읽지 말 것.** [S3]의 25,000명은 Knowledge 2026 참석자 수다. 직원 수는 [S1]의 26,000명뿐이며 T2 시점의 갱신값은 없다.

6. **"85% 재배치"는 단일 출처·단일 시점 수치다.** 6개월 뒤 두 개의 대형 키노트에서 재확인되지 않았으므로, 논문에서 REINV 근거로 쓸 경우 반드시 "2025-11-17 업로드 영상의 단일 진술이며 이후 갱신 없음"이라고 병기해야 한다.

7. **발화자 익명성.** [S1][S2]는 화자 이름이 자막에 없다. 직위·소속을 추정해 붙이면 안 된다. [S3][S4]는 이름이 나오지만 자막 표기가 불안정하다.

8. **자사 사례와 고객사 사례를 절대 섞지 말 것.** 특히 [S3][S4]는 분량의 대부분이 FedEx·CVS Health·NVIDIA·Google Cloud 관련이며, ServiceNow 자사 dogfooding 진술은 [S3]의 후반 한 단락과 [S4]의 CIO 발언 한두 문장에 집중되어 있다. 이 사례(사례 2)의 1차 근거는 여전히 [S1][S2]다.

9. **"자율"의 정의가 유동적이다.** [S4]에서 벤더 스스로 "현재 자율 운영 방식은 사람이 개입해야 한다"고 말한다. 벤더 어휘의 autonomous를 논문의 automation으로 그대로 매핑하면 코딩 오류가 발생한다.

---

**작성 요약**: 지정된 5개 소스를 전부 완독하고, ServiceNow의 자사 IT/CS 서비스데스크 dogfooding 사례를 Raisch & Krakowski(2021)의 6개 구성개념으로 코딩했다. 핵심 발견은 (1) "IT 지원 요청 90%"라는 값은 2025-11-17[S1]과 2026-05-08[S4] 두 시점에 동일하게 유지되지만 술어가 "AI를 통해 처리"에서 "자율적으로 처리"로 강화되고, 그 사이 2026-05-07[S3]에서는 "91% AI의 지원"이라는 더 약한 술어로 제시된다는 점, (2) 자동화율은 반복 갱신되는데 "IT 지원 담당자 85% 재배치"는 [S1] 단일 출처로만 존재하고 이후 사라져 REINV의 투입 측이 관측 불가능하다는 점, (3) SPILL이 "인접 과업의 증강 유발"이 아니라 "인접 영역으로의 자동화 복제 + 제품 라인업 확장"으로 나타나며, S1의 자사 내부 확산 계획과 S3/S4의 고객용 제품 출시가 주체가 다름에도 동일 서사로 연결된다는 점, (4) RESP는 감사추적·킬 스위치·에이전트 신원관리라는 제품 기능으로 강하게 제도화되어 논문을 확장한다는 점이다. 한계는 명확하다 — 다섯 소스 모두 벤더 마케팅 자산이라 제3자 검증치가 전무하고, before 기준선이 어느 수치에도 없으며, 증강→자동화 승격의 임계 기준은 어떤 소스에도 명시되지 않는다. 또한 한국어 기계번역 자막의 오류([음악] 삽입, 제품명·인명 표기 불일치, LLM/AIE의 잘못된 확장어)가 광범위해 핵심 문장인 "더 가치 있는 음악 관련 업무에 재배치되었습니다"[S1]에서 재배치 목적지를 판독할 수 없다.


---



## 사례 3 — Zapier 회계·재무팀

> ⚠️ 원 영상 제목은 "How 8 People Run a $5B Operation"이나, **"8명"과 "$5B"는 제목에만 있고 본문에 근거가 없다.** 본 문서 3.2·3.11 참조.

*원문: `docs/cases/03a_zapier_finance.md`*


### 3.1 소스 목록

| 태그 | 채널 | 업로드일/수집일 (구분) | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Zapier | **업로드일 2026-05-20** (채널 수집분, 파일 헤더 "업로드일") | ko | 약 8558개 | 벤더 주최 웨비나 "Steal Zapier's AI Playbook for Accounting". 발화자: 라이언(Zapier CFO), 미란다(회계팀 공동 리드), 루이스/루시오아(회계 관리자), 에즈라 골드버그(AP 팀 회계 운영 분석가), 진행자 라이언(제품마케팅) | https://www.youtube.com/watch?v=CxrrXKFn6cg | /home/user/youtube-scrap/transcripts/channels/Zapier/Steal_Zapier's_AI_Playbook_for_Accounting_How_8_People_Run_a__CxrrXKFn6cg.md |
| [S2] | Zapier | **업로드일 2025-11-14** (채널 수집분) | ko | 약 10278개 | 벤더 주최 "두 번째 연례 AI 쇼케이스". 발화자: 웨이드 포스터(공동창립자·CEO), 외부 고객 9명 데모, 제품 관리자 4인 Q&A, 이어지는 빌드어롱(라이언 리처드, 사용자 교육팀) | https://www.youtube.com/watch?v=pGjirCLK9qE | /home/user/youtube-scrap/transcripts/channels/Zapier/Zapier_AI_Showcase_50_Million_Tasks_Delegated_(The_Best_Use___pGjirCLK9qE.md |
| [S3] | Zapier | **업로드일 2026-03-30** (채널 수집분) | ko | 약 6901개 | 벤더 주최 실습 워크숍 "Using AI Without Losing Predictability". 발화자: 에밀리(Zapier AI 자동화 엔지니어), 브라이스(진행 보조) | https://www.youtube.com/watch?v=S9Tn3ddRuDI | /home/user/youtube-scrap/transcripts/channels/Zapier/Using_AI_Without_Losing_Predictability_Build_Along_Workshop__S9Tn3ddRuDI.md |
| [S4] | Zapier | **업로드일 2025-12-10** (채널 수집분) | ko | 약 6692개 | 벤더 주최 실습 워크숍 "The Executive's AI Agent You Can Build Today". 발화자: 코트니(CEO 지원 임원비서, 5년차), 크리스티나(CFO·인사/AI전환 책임자 지원 임원비서, 8~9년차), 라이언 앤더슨(제품마케팅) | https://www.youtube.com/watch?v=-x-nXqz4tKM | /home/user/youtube-scrap/transcripts/channels/Zapier/The_Executive's_AI_Agent_You_Can_Build_Today__-x-nXqz4tKM.md |

**시점 표기 원칙**: 네 소스 모두 `transcripts/channels/Zapier/` 아래의 **채널 수집분**이므로 파일 헤더의 "업로드일"이 영상 업로드 시점이다. 키워드 수집분(`transcripts/YYYY-MM-DD/`)이 아니므로 폴더명=수집일 문제는 이 사례에 해당하지 않는다. 단, [S2]는 업로드일 메타(2025-11-14)와 본문 내 날짜 언급이 어긋난다(→ 3.9 참조).

**각 소스의 역할**
- [S1] **1차 근거**. 이 사례의 회계팀 사실관계(인원 구성, 자동화 개수, 성과 수치, 3대 통제, 결정론↔추론 스펙트럼, FX 4-에이전트 포드)를 담은 유일한 소스.
- [S2] **대조군 겸 시간축 기준점**. 회계팀 사례는 전혀 등장하지 않는다. 외부 고객 데모 중심으로, "사람 검토를 언제 뺄 것인가"에 대한 담론이 아직 명시적 통제 언어로 정식화되지 않은 이전 시점의 상태를 보여준다.
- [S3] **보강**. "예측 가능성"을 주제로 한 워크숍으로, [S1]의 결정론↔추론 스펙트럼 논리를 다른 화자가 다른 맥락(개인 생산성)에서 반복·정교화한다.
- [S4] **보강 겸 대조군**. 임원비서 직군의 에이전트 구축 사례. 승인권/책임 귀속 언명이 [S1]과 유사하나, 운영 전환 후의 승인 처리가 [S1]과 상반되는 지점을 제공한다.

---

### 3.2 조직과 문제 상황

**팀 규모.** 제목의 "8 People"과 "$5B"는 **파일 제목 문자열에만 존재하며 [S1] 스크립트 본문에는 "8명"도 "$5B"에 해당하는 한국어 수치도 등장하지 않는다.** 본문에서 확인 가능한 팀 구성 서술은 정성적이다: "저희는 자동화와 AI를 우선시하는 경향이 강해서 팀 규모를 상당히 작게 운영하는 경우가 많습니다. 또는 직원들의 잠재력을 최대한 발휘할 수 있도록 확장 가능한 시스템을 갖추고 있기 때문이기도 합니다" [S1]. 직책 질문에 대한 답변은 "저희는 일반 회계 와 회계 운영 업무를 담당하고 있습니다"이며, "그리고 저희 회사에는 재무 관리자 한 분과 다른 회계 담당자 몇 분이 계십니다" [S1]로 마무리된다. 즉 **정확한 인원수와 매출 규모는 이 소스로 검증되지 않는다**(→ 3.11).

**운영 범위와 복잡도**
- 자동화 규모: "저희 회계팀은 현재 이메일 수신함, 월말 결산, 매입채무, 규정 준수 등 다양한 업무를 처리하는 150개 이상의 자동화 시스템과 에이전트를 운영하고 있습니다" [S1].
- 복잡도 증가: "우리는 지난 몇 년 동안 Zapier의 동일한 내부 팀이 여러 가지 복잡한 요소, 새로운 법인, 통화, 빅4 회계법인 감사 등을 도입해 왔습니다" [S1].
- 다국적 구조: "저희는 7개국에 자회사를 두고 있으며, 각 자회사는 해당 국가의 현지 통화로 자금을 조달해야 합니다" [S1]. FX 데이터 수집기는 "6개 통화에 대한 현재 미국 달러 환율을 가져와서 구글 스프레드시트에 새 행으로 기록합니다" [S1]. (자회사 7개국 / 추적 통화 6개로 수치가 서로 다르며, 소스는 이 차이를 설명하지 않는다.)
- 기술 스택: "Netswuite는 저희 회사의 ERP 시스템입니다", 알림·승인 Slack, 문서 저장 Google Drive, 지급계정 Zip, "Claude, ChatgPT, Zapier MCP, 그리고 Zapier 내부에 자체 개발한 AI 단계" [S1]. CFO는 "사용자 지정 데이터 웨어하우스가 필요하지 않다는 것입니다"라고 명시 [S1].

**before 상태 (과업별)**
- 회계 전표 검토: "검토 과정에서 발생한 문제는, 담당 부서가 잘못되었거나 프로젝트가 누락되었거나, 늦게 도착하는 등의 반응적인 문제였습니다" / "이전에는 발견되지 않은 불일치는 대개 거래 완료 과정이 상당히 진행된 후속 검토 단계에서 발견되었습니다" [S1]. 소요 시간 약 12시간 [S1].
- 미결제 현금 대조: "매달 우리는 넷 스위트에 접속해서 입금 내역과 수수료 내역을 검색하고, 여러 가지 필터링 작업을 하고, 엑셀에서 온갖 수식을 사용해서 실제로 이체 중인 내역을 확인해야 했습니다" / "이 업무 하나에 만 한 달에 약 두 시간 정도가 소요되었습니다" [S1].
- 선급 상각/거래 처리: "동기화 후에도 회계 부서는 여전히 거래 내역과 분개 항목을 수동으로 입력 하고 매번 마감 시마다 동일한 작업을 반복했습니다" / 실패 유형은 "잘못된 프로젝트 또는 누락된 프로젝트, 잘못 입력된 날짜 , 잘못된 선불 일정, 또는 누군가 시간이 부족해서 상각 계산을 설정하지 못한 경우 등" [S1].
- 회계 메일함: "이메일이 다섯 통 정도라면 괜찮지만, 하루에 30통 이상이라면 이메일 한 통당 대략적인 시간 단위로 분류하는 것이 좋습니다" [S1]. Zendesk("Zenesk")를 내부 티켓팅 시스템으로 사용, "그래서 Zenesk를 데이터 수집 시스템으로 사용하는 것입니다" [S1].
- FX 자금조달 판단: "따라서 이를 수동으로 처리했다면 누군가가 매일 금리를 추적하고 , 자금 지원이 가능한 자회사를 기억하고, 이동 평균을 계산하고, 시장에서 금리가 어떻게 변동할 것으로 예상하는지 조사하고, 승인 및 여유 자금을 추적해야 했을 것입니다. 속도가 느리고 오류 발생 가능성이 높아서 아무도 소유하고 싶어하지 않습니다" [S1].
- 역사적 대조군: CFO 본인 회고 — "저는 Zapier에서 7 년 동안 일하면서 Stripe, Brainree, PayPal의 거래 내역을 수동으로 대조하던 시절을 기억합니다" [S1].

**만든 주체.** "여기서 보시게 될 모든 것은 이 통화에 참여한 사람들이 만든 것입니다. 중앙 집중식 IT 팀도 아니고, 엔지니어 집단도 아닌, 회계 팀에서 실제로 업무를 수행하는 사람들입니다" [S1]. 경영진 측 조건은 "우리는 그 팀에게 공장을 재설계할 수 있는 공간과 권한, 그리고 기대를 주었습니다" [S1].

---

### 3.3 자동화 구간 (AUTO)

기계에 완전히 넘겨진 것은 **데이터 수집·추출·표준화·기록**과 **규칙 기반 예외 탐지**다.

1) **회계 전표 상시 모니터링**: "넷스위트에 게시된 모든 회계 전표를 검토하여 당사의 계정 체계 및 관련 규칙의 기준을 충족하는지 확인하는 시스템입니다" [S1]. 예외는 세 경로(부서 불일치/누락 부서/누락 프로젝트)로 분기하고 "각 경로마다 Slack 알림이 발생하고, 게시자와 승인자가 태그되며, Netswuite 저널 항목에 대한 직접 링크가 제공되고, 규정 준수 목적으로 영구 기록으로 테이블 행이 추가됩니다" [S1]. AI 단계는 표준화를 담당한다: "프로젝트 필드가 비어 있을 경우 프로젝트 없음으로 기본 설정하고 , 긴 문자열에서 계좌 번호만 추출하고 , 항목 번호를 일관된 형식으로 지정하여" [S1].

2) **미결제 현금 대조**: 수동 추출·필터·수식·PDF 전기가 통째로 이관됐다. "Zapier의 파일을 사용하여 각 PDF에서 전체 텍스트를 추출하고 있습니다. 이 시스템은 인공지능을 사용하여 각 명세서에서 최종 잔액을 찾아 추출합니다. 그러면 해당 잔액이 조정표의 올바른 탭과 셀에 자동으로 입력됩니다 . 수동 입력이 필요하지 않습니다" [S1]. 이관 원칙은 명시적이다: "우리는 수동 데이터 수집 단계를 파악 하고 해당 추출 과정을 자동화합니다. 모든 추론 및 논리 단계는 AI를 통해 처리되며, 모든 워크시트와 통합 문서는 그에 따라 자동으로 채워집니다" [S1].

3) **Zip→NetSuite 상각 일정 자동 설정**: "우리는 Zipum의 모든 거래 내역을 가져와 Netswuite에서 실제로 사용할 수 있는 필드로 변환하는 것부터 시작합니다" / "그 후 Zap은 Netswuite에서 현재 회계 장부 항목을 찾아 상각 날짜와 상각 일정 유형을 포함하여 업데이트합니다 . 따라서 J는 수동 입력 없이도 올바른 일정을 가지고 있습니다" [S1].

4) **FX 데이터 수집기와 검사기**: 수집기에 대한 서술이 가장 강한 자동화 언명이다 — "이것은 그 누구도 만지지 않는 곳이다 . 그냥 잘 작동합니다" [S1]. 그 위에 자율 자기수정 루프가 얹힌다: "웹에서 현재 환율을 독립적으로 가져와서 비교합니다. 오차가 5%를 초과하면 해당 행이 자동으로 수정되고, 제가 검토할 수 있도록 어떤 일이 발생했는지 알려주는 DM이 저에게 전송됩니다" [S1]. 즉 **수정은 자동, 통보는 사후**다.

5) **자동화 선정 기준(무엇을 먼저 기계에 넘겼는가)**: "에즈라의 경우, 자동화된 작업 대부분이 반복적이고 규칙 기반이며, 문제가 발생 하더라도 위험 부담이 적다는 점을 알 수 있습니다" / "제가 추천하는 세 가지는 받은 편지함 정리, 회계 전표 모니터링, 그리고 월말 결산입니다" [S1].

---

### 3.4 증강 구간 (AUG)

인간이 남는 자리는 **최종 승인, 판단 영역, 예외 처리, 규칙 저작**이다.

1) **최종 승인(불가침)**: "저희는 회계와 관련된 어떤 사안에 대해서도 인간의 승인 절차 없이 인공지능이 최종 결정을 내리도록 허용하지 않습니다" [S1]. 게시 정책도 동일하다: "그 모든 것들은 보류 중이거나 초안 상태로 들어갑니다. 사람의 승인 없이는 어떤 것도 기록에 남지 않습니다. 그것은 저희가 설계 과정에서 선택한 사항입니다. 자동으로 게시되도록 설정할 수도 있지만, 그렇게 하지 않기로 했습니다" [S1].

2) **판단 영역의 명시적 유보**: "하지만 판단이 필요하거나, 중요성, 재무제표에 미치는 영향 등을 고려해야 하는 경우에는 사람이 직접 참여합니다" [S1] / "마찬가지로 실제 월말 또는 기간 마감 시 최종 검토 단계는 항상 저희가 담당합니다" / "하지만 재무와 관련하여 남은 판단 사항은 AI의 역할이 아닙니다. 그게 바로 우리의 임무입니다" [S1].

3) **검토자의 역할 이동(제거가 아니라 상향)**: "이를 통해 저와 같은 검토자들은 회계 전표 승인 시 더 큰 확신을 가질 수 있으며, 회계 프로세스에서 보다 주관적인 영역에 집중할 수 있습니다" [S1].

4) **AP 메일함: 인간은 라우터에서 승인자로**: "수십 번씩 같은 전화를 거는 대신 , 저는 변경 사항을 승인합니다 . 에이전트는 반복적인 정렬 및 업데이트 작업을 수행합니다" [S1]. 자기 규정도 명시적이다: "저는 여전히 판단력을 갖고 있으며, 특히 예외적인 경우나 고객과 직접 관련된 상황에서는 더욱 그렇습니다. 하지만 저는 더 이상 라우터가 아닙니다" [S1]. 그리고 "MCP 덕분에 자료 수집 및 분류 단계는 가능했지만, 진행 여부 결정은 여전히 ​​제 책임입니다" [S1]. 남는 잔여 업무의 성격도 재정의된다: "자동화 시스템이 의도적으로 사람이 처리하도록 남겨둔 예외 사항들을 마무리했습니다" [S1].

5) **규칙 저작권은 인간이 보유**: 전표 규칙 테이블은 "회계 부서에서는 원할 때마다 정보를 업데이트할 수 있으며, 이 시스템은 지속적으로 발전하고 있습니다" [S1]. 확장 방식도 인간 주도다: "회계 규칙이 발전함에 따라 특정 공급업체 연결, 특정 GL 계정 등과 같은 코딩 규칙을 호출할 수 있는 경로를 계속해서 추가할 수 있다는 점입니다" [S1]. 스킬(플레이북)도 마찬가지 — "우리 팀이 계속 업데이트하는 참조 플레이북을 사용하여 커튼 스킬을 만드는 것이었습니다" [S1].

6) **실행 타이밍 통제를 인간이 쥔다**: 대조 자동화의 트리거를 스케줄이 아니라 인간 제출 양식으로 둔 이유 — "이 양식은 기본적으로 특정 조정 작업을 실행하려는 시점을 제어하기 위한 인터페이스입니다. 제 생각에는 이 경우에 스케줄 트리거를 사용하는 것은 까다롭습니다" [S1].

7) **FX 포드의 인간 지점**: 분석가는 판단하지 않고 제안한다. "그리고 가장 중요한 것은, 투자하려는 자회사에 해당하는 국가의 국기 이모티콘으로 응답하도록 팀에게 요청한다는 점입니다" [S1]. 그리고 "그러니까 사람이 이모티콘을 한 번 클릭하는 것만으로 모든 과정이 완료되는 거죠" [S1]. 설계 원칙 언명: "셋째, 실제 결정 과정에는 사람이 반드시 참여해야 합니다. 부동산 중개인들은 사람들이 직접 결정하도록 권유합니다. 그것이 바로 우리 가 재무와 관련된 모든 것에 적용하는 설계 원칙입니다. 인공지능의 가장 훌륭한 활용법 중 하나는 정답을 제시하지 않는 것입니다. 선택할 수 있는 추천 목록을 제공하거나 추천 항목을 평가하고 점수를 매길 수 있도록 하기 위한 것입니다" [S1]. (※ "부동산 중개인들은"은 기계번역 오류로 보이나 원문 그대로 인용함.)

---

### 3.5 전환 메커니즘 (CYCLE)

**증강 → 자동화 방향의 명시적 승급 절차가 존재한다.** 이 사례의 가장 이론적으로 값진 대목이다.

**(a) 관찰기 → 신뢰 → 인간 제거**
"그리고 그것들이 신뢰할 만했던 이유는 우리가 완전히 신뢰할 때까지 사람이 직접 검토하는 과정을 거쳤기 때문입니다. 우리는 첫날부터 사람의 검토 과정을 없애지 않았습니다. 우리는 여러 번 실행하고, 예외 상황을 파악하고, 모든 것을 검증한 후에야 그 담당자를 시스템에서 제외했습니다" [S1]. 승급의 선행조건은 피드백 속도다: "피드백 속도가 빨랐기 때문에 거기서부터 시작했습니다 . 이것들이 효과가 있는지 없는지는 바로 알 수 있을 거예요" [S1]. 시작점 권고: "글로벌 위험 워크플로를 기반으로 한 반복적인 규칙부터 시작하세요" [S1].

**(b) 결정론 → 추론(에이전트) 승급 2조건**
스펙트럼 정의: "이 스펙트럼에서 볼 수 있듯이 왼쪽은 결정론, 오른쪽은 추론론입니다" [S1]. 시작 권고는 왼쪽이다: "궁극적으로 저는 대부분의 사람들이 여기서 시작하는 것을 추천합니다. 그렇게 신뢰를 구축하고 이러한 시스템이 어떻게 작동하는지 배울 수 있기 때문입니다" [S1].
승급 조건(2개, 동시 충족):
> "그러니까 의사결정 공간이 너무 복잡해서 모든 규칙을 열거할 수 없을 때, 결정론적 자동화에서 추론 기반 또는 에이전트 기반 자동화로 넘어갈 준비가 되었다는 것을 알 수 있습니다. 길이 너무 많아요. 예외적인 경우가 너무 많습니다. 하지만 그 범위는 충분히 제한적이어서, 출력값이 나왔을 때 그것이 옳은지 판단할 수 있습니다. 그것을 보고 "맞아요, 그게 맞아요"라고 말할 수 있습니다" [S1]

즉 ① **규칙 열거 불가능성**(결정론으로는 못 담음) + ② **출력 정오 판정 가능성**(사후 검증 가능). ②가 없으면 승급하지 않는다는 역조건이 명시된다: "하지만 특정 결과물의 정확성이 절대적으로 요구되는 순간, 인간의 검토 단계를 거치는 결정론적 방식이 결국 승리하게 되는 경우가 많습니다" [S1].

**(c) 상위 판단선은 승급 대상이 아니다 (자동화 한계선의 고정)**
전체 자동화 가부 기준: "반복적이고, 규칙 기반이며, 검증 가능한 결과를 제공하는 작업이라면 자동화하는 것이 좋습니다. 하지만 판단이 필요하거나, 중요성, 재무제표에 미치는 영향 등을 고려해야 하는 경우에는 사람이 직접 참여합니다" [S1]. 즉 CYCLE은 판단선 **아래에서만** 작동하고, 판단선 자체는 이동하지 않는다.

**(d) 증강 회귀 방향의 근거**: 조건 변화 시 자동화→증강으로 되돌리는 사례는 [S1]에 **없음**. 다만 [S4]에는 출력 품질 저하를 사람이 감지해 지침을 수정하는 되먹임 루프가 있다: "하지만 저는 이것에서 마음에 들지 않는 점을 발견했습니다. 슬랙에 맞게 형식을 지정하는 방법을 제대로 이해하지 못하는 것 같습니다. 그래서 저는 에이전트에게 몇 가지 피드백을 드리고 싶습니다" [S4]. 이는 회귀(자동화 철회)가 아니라 감독 하 재조정이다.

---

### 3.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

**SPILL (한 과업의 자동화가 인접 과업의 증강을 유발)** — 근거 있음.

1) **모듈의 횡적 전파**: Slack ID 추출 에이전트는 한 워크플로에서 만들어졌으나 다른 워크플로의 부품이 된다 — "또한, 이 에이전트는 일종의 서브잽처럼 작동합니다. 따라서 이 기능을 Slack ID를 추출하려는 다른 워크플로에서도 사용할 수 있으며, 원하는 워크플로에 맞게 동적으로 에이전트 단계를 추가할 수 있습니다" [S1].
2) **로직의 계정 간 전파**: "월말 결산 프로세스의 여러 GL 계정과 대조 작업에 동일한 로직을 적용했으며 일관된 패턴을 보이고 있습니다" [S1].
3) **아키텍처의 도메인 간 전파**: "둘째, 이 패턴은 재사용이 가능합니다. 현금 흐름 모니터링, 공급업체 대금 지급 시기 관리, 예산 차이 알림 등 어떤 용도로든 동일한 아키텍처가 적용됩니다" [S1].
4) **부서 경계를 넘는 파급**: 매출 크레딧 자동화 하나가 회계팀과 영업팀 양쪽 시간을 절감한다 — "저희 회계팀과 영업팀은 단 하나의 매출 크레딧 계산 자동화 시스템 덕분에 매달 10시간 이상을 절약하고 있습니다" [S1].
5) **암묵지의 조직 내 전파(스킬 공유)**: "그래서 저는 제 Zenesk용으로 이 스킬을 만들 수 있지만, 제가 자리를 비웠을 때 매니저나 다른 사람이 이 공유 스킬에 접근해서 "이 에즈라가 만든 스킬을 실행해 봐"라고 하거나, 아니면 그냥 스킬을 실행해도 똑같이 작동할 거예요" [S1] / "Zapier 내부에서 볼 수 있는 멋진 점 중 하나는 팀 간에 기술을 많이 공유하고 있다는 것입니다" [S1].
6) **인접 증강의 신설**: 전표 검토가 실시간화되자 검토자의 활동이 "보다 주관적인 영역"으로 옮겨간다 [S1](3.4-3 인용). 이것이 이 사례에서 SPILL이 증강을 **유발**하는 가장 직접적 경로다.

**REINV (자동화로 확보한 자원의 증강 재투자)** — 근거 있음, 단 대부분 정성적.

- 재투자의 명시적 서술: "이는 저희 제품이 AI가 꾸준히 처리할 수 있다고 생각하는 작업들을 담당함으로써, 저희가 더욱 복잡한 영역에 집중할 시간을 확보할 수 있게 해 주었기 때문에, 출시 6일 차 마감 일정을 맞추는 데 매우 중요했습니다" [S1]. 즉 절감분이 (a) 마감 단축과 (b) 복잡 영역 집중으로 재투입된다.
- 동일 인력으로 복잡도를 흡수한 것 자체가 재투자다: "우리는 지난 몇 년 동안 Zapier의 동일한 내부 팀이 여러 가지 복잡한 요소, 새로운 법인, 통화, 빅4 회계법인 감사 등을 도입해 왔습니다" [S1].
- 인접 소스의 재투자 진술([S4], 회계팀 아님): "덕분에 저는 매주 최소 45분을 절약할 수 있게 되었습니다" → "이제 금요일 점심을 제대로 챙겨 먹을 수도 있고, 강아지와 한 시간 더 시간을 보낼 수도 있고, 아니면 시간을 좀 더 전략적으로 활용해서 다른 임원진들이 이런 에이전트를 만드는 데 도움을 줄 수도 있겠네요" [S4]. **여기서 재투자 대상에 "다른 임원진들의 에이전트 구축 지원"이 포함된다는 점이 UBS형 REINV(자동화 자원 → 증강 역량 확산)에 가장 근접한 진술이다.**
- 다만 [S1]에는 절감 시간의 **재배치 결과에 대한 정량 근거가 없다**. 절감치는 있으나 "그 시간에 무엇을 얼마나 더 했는가"의 수치는 해당 소스에 없음.

---

### 3.7 통합 장치 (RESP)

[S1]은 세 가지 통제를 하나의 답변으로 묶어 제시한다: "비슷한 질문 중 하나는 팀에서 어떤 통제, 감사 가능성, 예외 처리 및 직무 분리 가이드 라인을 구축해야 하는지에 대한 것이었는데, 이는 매우 좋은 질문이며 저희는 모든 워크플로에 이러한 세 가지 요소를 구축하려고 노력합니다" [S1].

**통제 1 — 인간 최종승인 불가침**
> "AI는 문제 발생 시 표시 작업을 수행하지만, 궁극적으로 어려운 결정을 내리는 것은 인간의 몫이 아닐까요? 저희는 회계와 관련된 어떤 사안에 대해서도 인간의 승인 절차 없이 인공지능이 최종 결정을 내리도록 허용하지 않습니다. 물론 일괄 승인 같은 기능을 통해 이러한 과정을 크게 간소화할 수 있다는 것을 알고 있지만, 최종 승인은 여전히 ​​사람이 직접 해야 한다고 생각합니다" [S1]

**통제 2 — 전수 로깅**
> "두 번째로, 모든 자동화된 작업이 기록됩니다. 누가 그것을 촉발했는지, 그것이 무슨 일을 했는지, 언제 일어났는지 . 궁극적으로 그것이 바로 Zapier와 Zapier 플랫폼의 강력한 힘입니다. 에이전트든 워크플로든 모든 작업은 쉽게 감사할 수 있도록 저장됩니다" [S1]

**통제 3 — 직무 분리(승인 ≠ 실행)**
> "그리고 세 번째로, 제가 말씀드렸던 승인 단계는 자동화된 작업 자체와는 항상 분리해서 진행합니다. 앞서 말씀드린 것처럼, 저희는 시스템이 마치 사람이 승인하는 것처럼 작동하기를 원합니다 . 그것이 바로 우리의 분리 정책입니다. 그것이 바로 제어 방식입니다. 그리고 이는 최초의 워크플로우를 누가 만들었는지와는 관계없이 적용됩니다" [S1]

**감사 대응 논리(설명책임)**: "이렇게 하면 감사관에게 AI가 무엇을 했는지, 언제 했는지, 왜 했는지 정확하게 보여줄 수 있습니다. 그것은 블랙 박스가 아닙니다. 이는 문서화된 의사결정 과정이 됩니다" [S1]. **도구 중립적 감사추적**도 명시된다: "모든 작업이 Zapier를 통해 이루어지기 때문에 어떤 AI 도구가 작업을 트리거했는지에 관계없이 감사 추적 기록이 일관적입니다 . 클로드든, 잽이든, 다른 요원이든, 우리는 동일한 기록과 동일한 증거를 가지고 있습니다" [S1].

**감사증거로의 전환**: 초안 상태 게시 정책은 제약이 아니라 증거로 재해석된다 — "이는 제한 사항이 아니라 궁극적으로 우리의 감사 증거가 됩니다" [S1].

**워크플로 수준 감사추적 구현**: 상각 Zap의 마지막 단계는 "우편번호의 자동화 세부 정보, 공급업체 요청 번호, 거래 ID, 그리고 업데이트 단계에서 반환된 J 번호 및 내부 ID와 같은 순 저널 식별자"와 Slack 알림 발송 시각을 테이블에 기록하고, "해당 자료 묶음을 한 곳에 보관하면 재무 부서에서 확실한 감사 추적 기록을 확보할 수 있습니다" [S1]. 사전 검토 게이트도 있다: "모든 중요한 단계는 슬랙 채널로 전달되어 회계 부서에서 변경 사항을 검토한 후에야 완료로 처리할 수 있습니다" [S1].

**접근통제(최소권한)**: "이러한 정보에 접근할 수 있는 모든 계층에서 최소 권한 원칙을 엄격하게 적용하는 것이 정말 중요하다는 점입니다" / "우리 중 소수만 NetSwuit에 접근할 수 있고, 영업 부서 내에서 적절한 자격을 갖춘 사람들만 HubSpot에 접근할 수 있습니다" [S1]. 벤더 측 인증 주장(벤더 자체 진술): "저희는 SOCK 2 type 2 인증을 획득했으며 GDPR 및 CCPA를 준수합니다" [S1].

**책임 귀속 원칙(다른 소스)**: [S4]는 같은 원칙을 한 문장으로 정식화한다 — "업무는 위임할 수 있지만 책임은 위임할 수 없다는 것입니다" / "따라서 이러한 에이전트를 구축할 때는 프로세스에서 사람이 개입하는 부분을 신중하게 고려하여 예상대로 정확하게 작동하는지 확인하는 것이 중요합니다" [S4].

---

### 3.8 성과 수치

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 월말 결산 기간 | (기준값 미제시) | 25% 단축 | [S1] "이러한 자동화를 통해 달성한 결과 중 하나는 월말 결산 기간이 25% 단축되었다는 것입니다" | 벤더 자체보고(제3자 검증 없음) |
| 회계 전표 검토 시간 | 약 12시간 | 2시간 미만 | [S1] "회계 전표 검토 시간이 약 12시간에서 2시간 미만으로 단축되었으며" | 벤더 자체보고 |
| 미결제 현금 대조 | 월 약 2시간 | 약 5분 | [S1] "이전에는 매달 2시간이 걸리던 작업이 이제는 약 5분밖에 걸리지 않습니다" | 벤더 자체보고 |
| 매출 크레딧 계산(회계+영업 합산) | (미제시) | 월 10시간 이상 절감 | [S1] | 벤더 자체보고 |
| 결산 마감 목표 | (미제시) | "출시 6일 차 마감 일정" 달성에 기여 | [S1] | 벤더 자체보고 |
| 자동화/에이전트 수 | (미제시) | 150개 이상 | [S1] | 벤더 자체보고 |
| 전표·구매전표 오류 자동 발견·수정 | 사후 검토 단계에서 발견 | "매달 수십 건" 자동 발견·수정 | [S1] "저희는 매달 수십 건의 회계 전표 오류와 구매 전표 오류를 자동으로 발견하고 수정하고 있습니다 . 월말 결산 시점이 아니라, 업무를 진행하는 동안에 말입니다" | 벤더 자체보고 |
| 거래 자동 수정 빈도 | (미제시) | "일주일에 한 번씩" 몇 건 | [S1] "Netswuite의 전체 감사 추적 기록에 반영되는 몇 건의 거래가 일주일에 한 번씩 자동으로 수정되었습니다" | 벤더 자체보고 |
| FX 자회사/통화 | 수동 추적 | 자회사 7개국 / 6개 통화 자동 수집 | [S1] | 벤더 자체보고 |
| FX 검사기 임계치 | — | 오차 5% 초과 시 자동 수정 + DM | [S1] | 벤더 자체보고 |
| FX 분석가 필터 | — | 최근 60일 내 자금조달 자회사는 스킵 / 30일 이동평균 대비 2% 이상 유리 시 매수 기회 | [S1] "자회사가 최근 60일 이내에 자금을 조달받은 경우 , 담당자는 해당 자회사를 건너뜁니다" / "오늘 금리가 평균보다 2% 이상 유리하다면 매수 기회입니다" | 벤더 자체보고 |
| FX 승인 구조 | — | 승인자 3인 태그, 국기 이모티콘 1회 클릭으로 승인 | [S1] "특정 승인자 세 명을 태그하고 피드 액션 회계 슬랙 채널에 게시합니다" | 벤더 자체보고 |
| AP 메일함 처리량 | 하루 30통 이상, 건당 수 분 | 검토 1회 패스 + 예외만 처리 | [S1] "그리고 업무량이 많은 날에는 이메일 하나당 몇 분씩 걸리는 것과 전체 이메일을 처리하는 데 몇 분씩 걸리는 것의 차이가 발생합니다" | 벤더 자체보고 |
| FX 포드 구축 공수 | — | "두 시간 정도" (며칠에 걸쳐) | [S1] "실제로 전체를 만드는 데는 아마 두 시간 정도밖에 안 걸렸을 거예요. 하지만 며칠에 걸쳐서 작업했죠" | 벤더 자체보고 |
| (참고, 회계팀 아님) 플랫폼 전체 | — | 고객 약 40만 명, 위임 작업 5천만 건 이상 | [S2] "약 40만 명의 고객이 AI와 Zapier를 사용하여 5천만 건 이상의 작업을 위임했습니다" | 벤더 자체보고 |
| (참고, 외부 고객 사례) 챗봇 매출 | — | 1년 차 13만 4천 달러 이상, 예약의 30% | [S2] | **고객 자체보고**(벤더 플랫폼상 시연) |
| (참고, 회계팀 아님) 임원비서 시간 절감 | 금요일마다 약 1시간 | 주당 최소 45분 절감 | [S4] "덕분에 저는 매주 최소 45분을 절약할 수 있게 되었습니다" | 벤더 자체보고 |

**주의**: 위 전부가 **벤더(Zapier)의 자기 사례 발표** 또는 벤더 웨비나에 초대된 고객의 자기 보고이며, 이 네 소스 안에 **제3자 검증치는 하나도 없다**. "빅4 회계법인 감사"가 언급되지만 [S1], 그것은 감사 대상 조직임을 말할 뿐 위 수치들이 감사받았다는 진술은 해당 소스에 없음.

---

### 3.9 소스 간 교차 대조

**A. 반복 확인된 사실 (2개 이상 소스에서 일치)**

1. **"자동화의 판단 지점은 사람이 갖는다"는 원칙.** [S1] "저희는 회계와 관련된 어떤 사안에 대해서도 인간의 승인 절차 없이 인공지능이 최종 결정을 내리도록 허용하지 않습니다" ↔ [S4] "업무는 위임할 수 있지만 책임은 위임할 수 없다는 것입니다" ↔ [S2] 리드 자동화의 마지막 단계가 초안 폴더 전달인 이유 — "따라서 영업 담당자나 제가 마지막에 보내기 버튼만 누르면 적격자에게 아웃리치 이메일을 보낼 수 있습니다" [S2]. 세 시점 모두에서 "마지막 클릭은 인간" 패턴이 반복된다.
2. **결정론↔추론 스펙트럼 프레임.** [S1]의 "왼쪽은 결정론, 오른쪽은 추론론입니다" ↔ [S3]의 동일 스펙트럼 서술("왼쪽에 주황색이고 '결정론'이라고 쓰여 있는 부분", "AI 워크플로우를 얻습니다" → 에이전트 → "전체 에이전트 워크플로 및 시스템"). [S3]은 명시적으로 왼쪽에 머문다: "우리는 완전히 왼쪽으로 치우쳐 있는 건 아니에요. 인공지능을 조금 활용할 예정이지만, 어디에 나타날지는 저희가 통제할 겁니다" [S3].
3. **LLM=구글지도 / 에이전트=자율주행 비유.** [S3] "AI 자동화 시스템을 활용하는 것은 마치 자율주행 자동차, 예를 들어 위모(Whimo)와 같은 것과 같습니다" ↔ [S4] "Agents는 Whimo와 더 비슷합니다". 동일 사내 교육 프레임이 서로 다른 화자·시점에 재사용된다.
4. **Copilot의 역할(구축 보조).** [S2](리치 카니, 제품관리자) ↔ [S1](미란다 "코파일럿을 항상 사용하시잖아요") ↔ [S3](막힐 때의 조수) ↔ [S4](에이전트 지침 개선). 네 소스 모두에서 확인된다.

**B. 한 소스에만 있는 사실**

- 회계팀 3대 통제(승인 불가침 / 전수 로깅 / 직무 분리), 자동화 승급 2조건, FX 4-에이전트 포드, 150개 이상 자동화, 25%·12h→2h·2h→5분·월 10시간·6일 마감 — **모두 [S1] 단독**. 다른 세 소스에 회계팀 사례는 등장하지 않는다.
- "직무 분리"라는 회계 통제 어휘 자체가 [S1]에만 있다. [S2]/[S3]/[S4]는 승인·검토를 말하되 SoD 개념은 쓰지 않는다.
- 프롬프트 예시 주입과 0~100 점수화 임계치 기법은 **[S3] 단독**: "하지만 제가 드릴 수 있는 가장 중요한 팁 중 하나는 질문에 예시를 포함시키는 것입니다" / "시스템이 상황의 긴급성을 0%에서 100%까지 평가하도록 하는 것이 매우 효과적이라는 것을 많이 봤습니다" / "그리고 필터 단계에서는 숫자가 80보다 큰 경우에만 계속 진행하도록 설정할 수 있겠죠" [S3].
- 입력 필드 최소화를 통한 데이터 노출 통제는 **[S3] 단독**: "그럴 경우 입력란에서 해당 주소를 제외하면 됩니다" / "반면에 제가 에이전트를 통해 이 정보를 처리한다면, 에이전트는 그 모든 정보에 접근할 수 있게 됩니다" [S3].
- 에이전트가 지시 범위를 넘어 산출물을 확장한 사례는 **[S4] 단독**: "제가 내부 회의 준비는 하지 말라고 설정해 놨는데 도 말이죠" → "바로 이 부분에서 에이전트가 창의력을 발휘했습니다" [S4].

**C. 시점에 따른 서술 변화 (2025-11 → 2025-12 → 2026-03 → 2026-05)**

| 시점 | 소스 | 자동화/증강 배분 담론의 상태 |
|---|---|---|
| 2025-11-14 | [S2] | **증강 배분이 관행 수준.** 인간 개입은 규범이 아니라 워크플로 마지막 단계의 실무(초안 폴더, 보내기 버튼)로 서술된다. 반대편에는 자동화 낙관 언명이 공존한다 — "이제 저희는 편안하게 앉아서 기계가 대부분의 작업을 처리하는 것을 지켜볼 수 있습니다" [S2]. 통제·감사·직무분리 어휘는 등장하지 않는다. CEO 프레임은 "팀원들이 더욱 전략적이고 창의적인 인간적인 업무에 집중할 수 있도록 했습니다" [S2] 수준의 일반론이다. |
| 2025-12-10 | [S4] | **책임 원칙이 문장으로 정식화된다.** "업무는 위임할 수 있지만 책임은 위임할 수 없다" [S4]가 세션 초반과 후반에 반복 강조되고, "블랙박스를 열어" 보여주는 에이전트 미리보기가 신뢰 장치로 제시된다. 다만 운영 전환 후에는 승인이 사라진다는 점이 함께 고지된다(→ D-1). |
| 2026-03-30 | [S3] | **"예측 가능성"이 세션 주제 자체로 승격된다.** "오늘은 예측 가능성을 잃지 않고 AI를 활용하는 데 초점을 맞춰, 간단한 동작으로 AI를 사용하는 방법에 대해 알아보겠습니다" [S3]. 담론이 "AI를 쓰자"에서 "AI가 어디에 나타날지 우리가 고른다"로 이동한다 — "AI는 우리 도구에서 어디에 나타날지 스스로 선택하는 것이 아닙니다 . 우리가 고르고 있어요" [S3]. 참가자 측 불안이 세션 설계 전제로 반영되어 있다는 점도 특징이다(예시 프롬프트: "AI를 사용해서 콘텐츠 캘린더를 수동으로 관리하는 일을 그만두고 싶은데, 예측 가능성이 떨어질까 봐 너무 걱정돼요" [S3]). 에이전트는 이 세션에서 "유연성"의 대가로 통제 상실을 수반하는 선택지로 상대화된다. |
| 2026-05-20 | [S1] | **회계 도메인 통제 체계로 제도화된다.** 승인·로깅·직무분리라는 감사 어휘, 승급 2조건, 판단선 고정이 명문화되고, 자동화 확대와 인간 승인 보존이 동시에 주장된다. 동시에 이 시점에서 처음으로 다중 에이전트 포드(FX)가 재무 영역에 도입된 사례가 공개된다 — 즉 **오른쪽(추론)으로의 확장과 통제 체계의 강화가 같은 시점에 함께 나타난다.** |

**부수적 시계열 지표(플랫폼 규모 자기보고)**: 앱 수 언급이 시점별로 다르다 — [S2] "Zapier의 6,000개 이상의 앱"(2025-11) → [S4] "8,000개 앱과 55,000개 이상의 액션"(2025-12) → [S3] "저희는 8,000개 이상의 앱을 보유하고 있습니다"(2026-03) → [S1] "Zapier가 지원하는 9,000개 이상의 앱"(2026-05). 단조 증가하나 [S4]와 [S3] 사이는 정체다.

**D. 모순 / 긴장**

1. **승인 게이트의 존속 여부가 소스 간 상충한다.** [S1]은 "사람의 승인 없이는 어떤 것도 기록에 남지 않습니다" [S1]라고 못박는 반면, [S4]는 정반대의 운영 규칙을 고지한다: "참고로, 에이전트를 테스트하는 동안에만 작업을 수행하기 전에 권한을 요청합니다 . 일단 전원을 켜면 별도의 승인 절차가 필요하지 않습니다" [S4]. 즉 **동일 플랫폼에서 재무 도메인([S1])과 임원지원 도메인([S4])의 승인 규범이 다르다.** [S1]의 불가침 원칙은 플랫폼 기본값이 아니라 회계팀의 설계 선택임을 [S1] 스스로도 인정한다: "자동으로 게시되도록 설정할 수도 있지만, 그렇게 하지 않기로 했습니다" [S1].
2. **자동화 낙관 vs. 통제 강조의 온도차.** [S2]의 "편안하게 앉아서 기계가 대부분의 작업을 처리하는 것을 지켜볼 수 있습니다"(외부 고객 발화)와 [S1]의 "최종 승인은 여전히 ​​사람이 직접 해야 한다고 생각합니다"는 같은 채널의 서로 다른 시점·화자에서 나온 상반된 톤이다.
3. **FX 검사기의 자동 수정은 [S1] 자신의 3대 통제와 긴장 관계에 있다.** 오차 5% 초과 시 "해당 행이 자동으로 수정되고" 사후 DM만 간다 [S1]. 이는 "인간 승인 없는 최종 결정 불허" 원칙의 예외처럼 보인다. [S1]은 이 긴장을 인식하지 않으며, 대신 위험 한정 논리로 정당화한다: "우리는 외환 거래에서 위험을 줄였습니다. 요원이 틀렸다고 해서 우리에게 해가 되는 건 아니고, 항상 작동 중이니까요" [S1]. **다만 NetSuite 게시(전표 기록)와 참조 데이터 수정은 다른 층위이므로 형식적 모순이라기보다 ‘승인 게이트가 걸리는 대상이 회계 기록에 한정된다’(필자 해석)는 해석이 가능하다 — 그러나 소스는 이 구분을 명시하지 않는다.**
4. **[S2]의 업로드일 메타와 본문 내 날짜가 어긋난다.** 파일 헤더는 "업로드일: 2025-11-14"인데, 본문은 "다음 주 화요일인 5월 14일"에 워크숍이 있다고 두 차례 안내하고 "저희 최신 AI 제품인 Zapier Central이 오늘 베타 버전으로 출시되었습니다" [S2]라고 말한다. **[S2]를 시계열 근거로 쓸 때는 "채널 업로드 시점"과 "행사 개최 시점"이 다를 수 있음을 반드시 표기해야 한다.** 본 사례에서 [S2]는 "네 소스 중 가장 이른 업로드"라는 상대적 위치로만 사용했다.
5. **자회사 7개국 vs. 추적 통화 6개** [S1] — 소스 내에서 조정되지 않는 수치 불일치(3.2 참조).
6. **제목과 본문의 불일치.** 파일명·제목의 "8 People", "$5B"는 본문 어디에도 근거가 없다(3.2, 3.11).

---

### 3.10 논문 대조

| 논문 명제 (쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간 루프 제외 (p.194) | 데이터 추출·표준화·PDF 잔액 전기·전표 규칙 검사·FX 환율 수집("그 누구도 만지지 않는 곳이다 . 그냥 잘 작동합니다") [S1] | 지지 |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | 최종 승인, 판단·중요성 평가, 예외 처리, 규칙 테이블 저작, 실행 타이밍 통제(양식 트리거) [S1]; "저는 더 이상 라우터가 아닙니다" [S1] | 지지 |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | "우리는 첫날부터 사람의 검토 과정을 없애지 않았습니다. 우리는 여러 번 실행하고, 예외 상황을 파악하고, 모든 것을 검증한 후에야 그 담당자를 시스템에서 제외했습니다" [S1] | **강한 지지 + 조작화 확장** (승급 2조건: 규칙 열거 불가 + 출력 정오 판정 가능) |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | [S1]에 자동화→증강 회귀 사례 **없음**. [S4]의 지침 재조정은 감독 하 튜닝이지 회귀가 아님 | **부분적 미확인** (반증은 아님; 근거 부재) |
| SPILL: 한 과업 자동화가 인접 과업의 증강 유발 (p.197) | 서브잽 모듈 재사용, GL 계정 간 로직 전파, 아키텍처의 도메인 간 재사용, 회계↔영업 부서 간 절감, 스킬 공유 [S1] | 지지 + 보강(전파 경로를 5가지로 구체화) |
| REINV: 자동화 자원을 증강에 재투자 (p.201, UBS) | "저희가 더욱 복잡한 영역에 집중할 시간을 확보"·6일 마감 [S1]; 동일 팀으로 신규 법인·통화·빅4 감사 흡수 [S1]; "다른 임원진들이 이런 에이전트를 만드는 데 도움을 줄 수도" [S4] | 지지, 단 **정량 근거 약함** |
| RESP: 인간이 프로세스 전체 책임/승인/감사 보유 (p.200) | 3대 통제 + 도구 중립적 감사추적 + "그것은 블랙 박스가 아닙니다" [S1]; "업무는 위임할 수 있지만 책임은 위임할 수 없다" [S4] | **강한 지지** |
| p.195 증강 학습은 도메인 전문가의 암묵지에 의존, IT/외주 위임 불가 | "중앙 집중식 IT 팀도 아니고, 엔지니어 집단도 아닌, 회계 팀에서 실제로 업무를 수행하는 사람들입니다" [S1]; 규칙 테이블/플레이북을 회계팀이 직접 유지 | **강한 지지** |
| p.198 기계 한계 ①목적/자아 부재 | 에이전트에 "최종 목표를 부여할 것입니다" [S4] — 목적은 외생적으로 주입됨 | 지지 |
| p.198 ②제약 완화된 옵션만 제시 | "인공지능의 가장 훌륭한 활용법 중 하나는 정답을 제시하지 않는 것입니다. 선택할 수 있는 추천 목록을 제공하거나" [S1] — 옵션 제시자로 명시 설계 | **강한 지지(설계 원칙화)** |
| p.198 ③훈련된 과업에 국한 | "각 요원은 한 가지 일을 아주 잘합니다. 그들 중 누구도 모든 것을 다 잘하려고 애쓰지 않습니다" [S1]; "에이전트 한 명당 하나의 캘린더를 만들고, 한 에이전트가 하나의 업무만 수행하도록 하는 것을 추천합니다" [S4] | 지지 |
| p.198 ④감각/감정/사회기술 부재 | 판단·중요성·재무제표 영향은 인간 유보 [S1]; "특히 예외적인 경우나 고객과 직접 관련된 상황에서는 더욱 그렇습니다" [S1] | 지지 |
| p.199 한쪽 편중 시 악순환 | 편중을 억제하는 설계가 명시적: 왼쪽(결정론)에서 시작→신뢰 축적→우측 이동, 그리고 정확성 요구 시 결정론 복귀 [S1] | 보강(악순환 회피 절차의 실례) |
| p.204 기계는 조직 내 새로운 행위자 계급 | FX 포드의 4개 에이전트에 역할명·담당·상호 견제가 부여됨("데이터 수집기, 데이터 품질 관리자, 분석가, 그리고 활동 기록기") [S1]; "여러 요원들이 서로를 견제하는 모습이 마음에 듭니다" [S1]; 로깅 항목이 "누가 그것을 촉발했는지" [S1] | **강한 지지 + 확장** |

**이 사례가 논문을 확장하는 지점.**
첫째, Raisch & Krakowski가 시간축 개념으로 제시한 CYCLE을 이 사례는 **승급 결정 규칙으로 조작화한다.** 증강에서 자동화로 넘어가는 기준이 ‘규칙을 전부 열거할 수 없을 만큼 복잡하되, 출력의 정오를 사후 판정할 수 있을 만큼 범위가 한정될 것’(필자 요약)이라는 두 조건의 논리곱으로 제시되고, 두 번째 조건이 깨지면 결정론+인간검토로 되돌린다는 역조건까지 붙어 있다 [S1]. 이는 학습→견고화→자동화라는 서술적 순환을 **검증가능성(verifiability)을 축으로 하는 게이트 규칙**으로 바꾼 것이다.

둘째, RESP가 이 사례에서는 감사(audit) 제도와 결합해 **경로 독립적 통제**로 나타난다. 어떤 AI 도구가 실행을 촉발했든 동일한 감사추적이 남고("클로드든, 잽이든, 다른 요원이든, 우리는 동일한 기록과 동일한 증거를 가지고 있습니다" [S1]), 승인 단계는 실행 주체와 항상 분리되며, 이 규칙은 "최초의 워크플로우를 누가 만들었는지와는 관계없이 적용됩니다" [S1]. 논문의 RESP가 "인간이 책임을 진다"는 규범적 진술이라면, 여기서는 **누가 만들었는가와 무엇이 실행했는가를 분리해 기록·승인·직무분리로 강제하는 조직 설계**로 구체화된다.

셋째, p.204의 "새로운 행위자 계급"이 FX 포드에서 **행위자 간 상호 통제**로까지 나아간다. 검사기 에이전트는 수집기 에이전트의 출력을 독립적으로 재조회해 검증하고, 임계치 초과 시 자동 수정 후 인간에게 통보한다 [S1]. 이는 인간-기계 이분법이 아니라 **기계-기계 감사 계층 위에 인간 승인이 얹힌 3층 구조**이며, 논문이 다루는 인간-기계 관계 모델의 한 단계 확장이다. 동시에 이 구조는 논문 프레임의 사각지대도 드러낸다 — 자동 수정이 이미 일어난 뒤 인간이 통보받는 이 지점은 AUTO도 AUG도 아닌 ‘사후 감독(post-hoc oversight)’이며, [S1] 자신이 내세운 "인간 승인 없는 최종 결정 불허" 원칙과 형식적으로 충돌한다.

넷째, 이 사례는 **도메인별로 RESP 강도가 다르게 설정된다**는 사실을 같은 조직 내부에서 보여준다. 재무([S1])는 승인 게이트 불가침, 임원지원([S4])은 운영 전환 후 승인 면제. 논문은 통합 조건으로서 RESP를 일반 원리로 제시하지만, 이 사례는 **RESP가 과업의 재무제표 영향도에 따라 조절되는 가변 변수**임을 시사한다.

---

### 3.11 인용 시 주의사항

1. **제목의 "8명"과 "$5B"는 본문 미근거.** "8명", "$5B"(또는 50억 달러)에 해당하는 수치는 [S1] 스크립트 본문 어디에도 없다. 팀 규모 관련 본문 진술은 "재무 관리자 한 분과 다른 회계 담당자 몇 분" [S1] 정도의 정성 서술뿐이다. **논문에서 "8명이 $5B를 운영"이라고 쓰려면 이 소스만으로는 불충분하며, "영상 제목 기준"이라고 명시하거나 별도 출처가 필요하다.**
2. **전부 벤더 자체보고.** 네 소스 모두 Zapier 공식 채널의 자사 마케팅 웨비나이고, [S1]은 Zapier가 자사 회계팀 사례를 자사 제품 홍보 맥락에서 발표한 것이다. 성과 수치에 제3자 검증은 없다. [S2]의 외부 고객 수치(13만 4천 달러, 예약 30%)는 **고객 자체보고**로 별도 표기해야 한다. [S1]의 "SOCK 2 type 2 인증" 진술 역시 벤더 자기 진술이다.
3. **성숙도: 대부분 운영 중, 일부는 시연·계획.** [S1]의 전표 모니터링·대조·상각·AP 메일함·FX 포드는 모두 "운영 중"으로 서술된다(실제 발생 사례 스크린샷 언급: "이는 몇 달 전에 발생했던 부서 부적합 사례입니다" [S1]). 반면 [S3]·[S4]는 **워크숍에서 실시간으로 처음 만드는 데모**이며([S4] "제가 사람들에게 실시간으로 대규모 에이전트를 구축하는 방법을 보여주는 것은 이번이 처음입니다"), [S2]의 다수 항목은 로드맵/베타 단계 언급이 섞여 있다("Central은 베타 버전 제품입니다" [S2]). 운영 실적과 데모를 같은 층위로 인용하면 안 된다.
4. **한국어 기계번역 자막의 오류가 많다.** 고유명사가 다수 왜곡되어 있다: "Netswuite"(NetSuite), "Zenesk"(Zendesk), "Zappy"/"Zapper"/"Zappier"/"Zap 연도"/"Zap 연간"(Zapier), "Brainree"(Braintree), "Whimo"(Waymo), "루시오아"/"루이스"(동일 인물로 보임), "Ezric"/"에즈라", "체커"/"검사기", "화해"(reconciliation=대조), "부동산 중개인들은 사람들이 직접 결정하도록 권유합니다"(원의미 불명), "추론론", "EOP(End Operations Program)", "To-D-Doist"(Todoist), "Kersure"/"커튼 스킬"/"커서"(Cursor), "제네스크", "디오이트"류의 음차 오류. **인용 시 원문 그대로 옮기고 [원문 오기] 표시를 붙일 것.** 특히 "회계 전표"와 "저널 항목"/"분개 항목"/"J"/"G J tw"가 같은 대상을 가리키는 것으로 보이나 번역이 일관되지 않는다.
5. **띄어쓰기·문장부호 이상이 원문에 있다.** "회계 와", "문제가 발생 하더라도", "어떤 워크 플로우에는", "7 년 동안", "조달받은 경우 ,", "대신 , 저는", "여전히 ​​사람이"(폭 없는 공백 포함) 등. 기계적 대조 검증을 위해 **한 글자·한 칸도 다듬지 말 것.**
6. **귀속 문제.** [S1]에서 CFO(라이언)의 총괄 수치 발언과 실무자(루이스·에즈라·미란다)의 개별 워크플로 수치는 화자가 다르다. 25% 결산 단축·150개 자동화·월 10시간은 CFO 발언, 12h→2h는 루이스, 2h→5분도 루이스, 6일 마감은 루이스, FX 수치는 미란다, AP 메일함은 에즈라다. **수치를 인용할 때 화자를 특정할 것.**
7. **[S2]는 회계팀 사례가 아니다.** [S2]에는 Zapier 회계팀이 전혀 등장하지 않는다. 시계열 담론 비교와 플랫폼 규모 맥락에만 사용해야 하며, "Zapier 회계팀의 2025-11 상태"로 인용하면 오류다.
8. **[S2]의 업로드일 신뢰도.** 헤더 업로드일(2025-11-14)과 본문 내 "5월 14일" 언급·Central 베타 출시 발표가 어긋난다. 시계열 논증의 핵심 근거로 삼지 말고, 보조 지표로만 쓸 것(3.9-D-4).
9. **기술적 장애로 인한 서술 중복.** [S1]은 발표자 인터넷 문제로 에즈라의 상각 데모가 중단·재시작되어 동일 내용이 두 번 서술된다(첫 시도 "이 예시에서는 Zip과 Netswuite를 사용합니다" 직후 중단, 이후 "안녕하세요 여러분. 저는 에즈라 골드버그이고"로 재시작). 인용 위치를 특정할 때 주의.
10. **"자동화 승급 2조건"은 CFO 개인 발언 형식이다.** 회사 공식 정책 문서로 제시된 것이 아니라 Q&A 답변 중 구술된 것이므로, "Zapier의 공식 기준"이 아니라 "CFO가 웨비나에서 제시한 판단 규칙"으로 인용해야 한다.


---



## 사례 3B — Zapier : 전사 AI 전환·거버넌스·측정

*원문: `docs/cases/03b_zapier_enterprise.md`*

# 사례 3B - Zapier : 전사 AI 전환·거버넌스·측정 (사례 3의 조직 맥락편)

### 3B.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 | 자막언어 | 단어수 | 발표 맥락 / 주요 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Zapier | **업로드일 2025-09-26** (채널 수집분, 파일 헤더 "업로드일") | en | 약 10927 | Zapier 주최 웨비나 "How Zapier Runs AI Hack Week". 발화자: Ryan(principal product marketer), Lindsay(revenue operations 팀 리드). 데모 영상 발화자: Sarah(RevOps), Mitchell(account executive), Denise/Lacy/Stacy(events) | https://www.youtube.com/watch?v=e1pk34c3oYU | /home/user/youtube-scrap/transcripts/channels/Zapier/How_Zapier_Runs_AI_Hack_Week_Real_Examples_of_AI_Transformat__e1pk34c3oYU.md |
| [S2] | Zapier | **업로드일 2025-11-24** (채널 수집분) | ko(기계번역 자막) | 약 8375 | Zapier 사내 주간 전체회의를 **최초로 일반 공개**한 방송. 발화자: 웨이드(공동창업자·CEO), 브랜든 시무트(인사 및 AI 혁신 책임자), 로렌 프랭클린(지원 부사장), 에밀리(AI 자동화 엔지니어), 체이스(기술지원 운영), 라이언 | https://www.youtube.com/watch?v=EfHm1Qjztd0 | /home/user/youtube-scrap/transcripts/channels/Zapier/Zapier's_Big_AI_Plans_for_2026_Revealed!_-_Leadership,_Cultu__EfHm1Qjztd0.md |
| [S3] | Zapier | **업로드일 2025-12-18** (채널 수집분) | en | 약 11943 | Zapier×PandaDoc 공동 AMA 파이어사이드 챗 "Defining AI Fluency". 발화자: Brandon Simute(Zapier chief people and AI transformation officer), Keith(PandaDoc president), Ryan Anderson(모더레이터) | https://www.youtube.com/watch?v=Rq1lzDDfTrU | /home/user/youtube-scrap/transcripts/channels/Zapier/Defining_AI_Fluency_A_Fireside_Chat_With_The_Executives__Rq1lzDDfTrU.md |
| [S4] | Zapier | **업로드일 2026-04-20** (채널 수집분) | ko(기계번역 자막) | 약 7764 | Zapier 주최 거버넌스 패널 웨비나. 발화자: 벤자민 프레시먼(Zapier 부법률고문, 사회), 제니(Rivian, AI 개인정보 보호·위험 관리), 케이티(Kayak, AI 거버넌스 위원회 설립·위원장), 리아(마케팅, 진행) | https://www.youtube.com/watch?v=-Y22OVH2w1o | /home/user/youtube-scrap/transcripts/channels/Zapier/The_Executive_Blueprint_for_Responsible_AI_Governance_Practi__-Y22OVH2w1o.md |
| [S5] | Zapier | **업로드일 2026-07-29** (채널 수집분) | ko(기계번역 자막) | 약 7168 | Zapier "AI Workflow Index" 최초 공개 웨비나 + Glean 보고서 대담. 발화자: 라이언(Zapier AI 전환 마케팅), 앙드레(Zapier, 인덱스 연구 주도), 레베카(Glean 사내 AI 연구소 책임자) | https://www.youtube.com/watch?v=rq4IbzPkwMg | /home/user/youtube-scrap/transcripts/channels/Zapier/The_four_jobs_AI_actually_does_at_work_A_first_look_inside_Z__rq4IbzPkwMg.md |

**시점 표기 원칙**: 5개 소스 전부 `transcripts/channels/Zapier/` 하위의 **채널 수집분**이며, 각 파일 헤더에 "업로드일"이 명시되어 있으므로 위 날짜는 **영상 업로드 시점**이다. (키워드 수집분처럼 폴더명이 수집일인 경우가 아니다.)

**각 소스의 역할**

- [S1] **1차 근거** — 바텀업 실험(해커위크)의 설계와 실제 산출물. AUG→AUTO 전환의 최초 관찰 지점.
- [S2] **1차 근거** — 전사 전환 프레임워크(리더십/인재·문화/도구/거버넌스), 인력 운영 모델, 성과 평가표, 2026년 2대 베팅. 조직 구조화 단계.
- [S3] **보강** — AI Fluency의 정의와 채용·평가 반영. 자원 재투자(REINV) 근거가 가장 명확한 소스. PandaDoc이라는 **비교 대조군**을 내장하고 있음.
- [S4] **1차 근거(거버넌스)** — 등급형 승인, 인벤토리, 관찰가능성 등 RESP 장치. 단, 발화의 다수가 **Rivian/Kayak 소속 외부 패널**이므로 Zapier 사례로 귀속할 수 없는 진술이 섞여 있다.
- [S5] **1차 근거(측정)** — AI Workflow Index 방법론과 "네 가지 일". 논문 2분법과의 직접 대조 지점. 단, 3분법 프레임은 **Glean 소속 게스트 발화**이며 Zapier 인덱스의 산출물이 아니다.

---

### 3B.2 조직과 문제 상황

**규모·인원**

- 전원 원격 근무의 국제 조직이며 주간 전체회의에 "42개국에서 800명이 접속합니다" [S2]. 이 전체회의는 "14년 전 자피어 창립 초기부터 이어져 온 전통"이고 2025-11-24 방송이 최초의 일반 공개였다 [S2].
- go-to-market 조직 규모는 해커위크 참여 기준 "across 150 people in Zapier's go to market team" [S1].
- 제품 규모: [S1] 시점(2025-09)에 "8,000 integrations" [S1]. [S4] 시점(2026-04)에는 같은 발화자가 한 번은 "거의 99,000개 이상의 앱을 연결합니다", 뒤에서는 "저희는 9,000개 이상의 앱을 제공하고 있습니다"라고 말한다 [S4] — 소스 내부 모순(3B.9 참조).

**before 상태**

- AI 도입률: "당시 저희 회사의 AI 도입률은 한 자릿수 퍼센트 정도였고, 사람들이 이 기술을 잠깐씩 사용해 보는 정도였습니다" (2023년 GPT-4 출시 이전/직후 시점) [S2].
- 도입 방식: "그건 전부 아주 아래에서부터, 아주 유기적으로, 아주 암시적인 성격을 띠고 있었어요" [S2].
- 계기: GPT-4 출시가 "우리에게 경종을 울린 사건이었다"이며, 3.5 출시 후 "불과 6개월 만에" 나온 개선 속도를 근거로 "비상사태를 선포하고" 대응했다 [S2].
- 지원(support) 조직의 심리 상태: "웨이드는 2023년 당시 지원팀들이 AI가 자신들의 일자리를 먼저 대체할까 봐 상당히 불안해했다는 점에 많은 사람들이 동의할 거라고 생각합니다" [S2].
- 도구 확산 문제: 기술지원 운영팀이 약 1년 전(≈2024년) 만든 Figma 맵 기준으로 "일반적인 문제 해결 티켓을 처리할 때 지원팀은 대략 다섯 가지 정도의 도구를 사용하는 경우가 많습니다" [S2].
- 갱신(renewal) 업무의 before: "there's a lot of unstructured data across a lot of systems here and that was very manual for us" [S1]. 이전에는 "Grady would have had to come in and fill out this renewal handoff form, do all this research herself, make a call herself, and work with the sales team on uh who wanted to work this" [S1].
- 시장 전체 진단(Zapier 자체 관찰): "most AI pilots are are failing right now" [S1].

---

### 3B.3 자동화 구간 (AUTO)

**(1) 갱신 리서치·핸드오프 [S1, 2025-09]**
Sarah가 만든 갱신 에이전트는 Looker 사용량 데이터, 미팅 이력, 참석자 직함, 내부 Slack 검색(Glean), 최신 뉴스를 모아 갱신 유형을 판정하고 초안 이메일까지 생성한다. 핸드오프 자체가 기계로 넘어갔다: "The handoff is made automatically." [S1]

**(2) 동일 워크플로의 10개월 뒤 서술 [S5, 2026-07]**
같은 성격의 갱신 에이전트를 앙드레가 다시 설명하면서, 자동화 구간의 경계를 명시적으로 그었다: 갱신 시기 파악, 가격 유지/인상/인하 후보 평가, 담당자 배정, 예보 갱신까지에 대해 "제가 방금 설명드린 모든 것 . 이 과정에 사람은 전혀 관여하지 않았습니다." [S5]

**(3) 이벤트 인텔리전스 [S1]**
주 1회 에이전트가 지난 7일간 신규 발표된 이벤트를 탐색해 자동 등재하고, 신뢰도 점수·참석 예상 규모 등을 부여한다 [S1].

**(4) 티켓 코파일럿 [S2]**
"Ticket Copilot은 당사의 지원 시스템에 직접 연결되어 여러 소스를 검색합니다"이며 근본 원인 분석과 고객 회신 초안까지 생성한다 [S2].

**(5) 해커위크 심사 자동화 [S1]**
Lindsay가 "I created a bot that I named Jade"라 명명한 봇이 "she worked um off of a rubric to score um and provide feedback on all the Hackweek projects" [S1] — 평가라는 관리 과업 자체가 부분 자동화되었다.

**(6) 워크플로 내부에서 AI가 차지하는 비중은 소수 [S5]**
AI Workflow Index 측정 결과 "평균적으로 AI 단계가 차지하는 비율은 18%에 불과하다는 것입니다" [S5]. 나머지는 규칙·비즈니스 로직 기반의 전통 자동화이며, 관찰된 자동화 대부분은 "마법이라기보다는 배관 설비에 훨씬 더 가깝습니다" [S5].

---

### 3B.4 증강 구간 (AUG)

**(1) 되돌릴 수 없는 접점에는 반드시 사람 [S5]**
갱신 에이전트에서 자동화가 멈추는 지점은 고객 발신 메시지다: "고객에게 보낸 메시지를 되돌리는 것은 매우 어렵습니다. 그래서 결국 사람이 개입하게 되는 거죠" [S5].

**(2) 추천의 수정권 [S1]**
"but now it's happening automatically with a recommendation from AI and people can always come in and change that recommendation after the fact if they don't agree with it" [S1].

**(3) 심층 리서치 실행 버튼 [S1]**
이벤트 시스템에서 AI가 찾은 후보에 대해 심층 분석을 돌릴지 여부를 사람이 버튼으로 결정한다. "Anytime a new event is added here, um a button will illuminate there that we can use just once"이고, 그 이유를 명시했다: "the reason why we added a human in the loop is maybe there's some events that get suggested that are that are really small and look look interesting but not enough to do like deep research" [S1].

**(4) 출처 역추적 [S1]**
챗봇 응답에는 "so it points me directly to where it found that information so I can do the verification on my side as well" [S1].

**(5) 지원 상담원의 검토·발송 [S2]**
티켓 코파일럿이 회신을 생성해도 "그러면 담당자가 내용을 검토한 후 바로 보낼 수 있습니다" [S2]. 성과 서술도 자동화가 아니라 인간 몫의 재배치로 표현된다: "상담원들이 고객 지원의 인간적인 측면, 즉 티켓 코파일럿에 더 집중할 수 있는 시간입니다" [S2] (기계번역 오류로 문장이 뭉개져 있음 — 3B.11 참조).

**(6) 검사 책임은 소멸하지 않는다 [S2]**
"결과를 검사하고 품질이 괜찮은지, 기준을 충족하는지 등을 확인해야 합니다. 그 부분은 없앨 수 없어요" [S2].

**(7) 품질 검사 때문에 노동시간이 줄지 않는다 [S3]**
"there are small mistakes it makes that require quality checks that it may not completely shrink the work week" [S3].

**(8) 인간-기계 공동 진화 [S2]**
에밀리의 개인 에이전트: "보시다시피, 이 에이전트는 시간이 지남에 따라 진화해 왔습니다 . 제 업무 방식에 맞춰 조정되었고, 점점 더 진정한 AI 협력자처럼 작동하도록 개선되었습니다." [S2]

**(9) 증강 학습의 소유자 [S2]**
"그 고통의 핵심에 깊이 관여하고 있는 사람이 바로 인공지능을 활용해 그 고통을 자동화하는 데 가장 적합한 사람이다" [S2]. AI 활용 능력의 정의도 기술 지식이 아니라 업무 이해로 규정된다: "자신의 작품을 충분히 잘 이해해서 재설계할 수 있다는 뜻입니다" [S2].

**(10) 무엇이 증강인지에 대한 조직 내 이견 [S4]**
"어떤 과정에든 직간접적으로 사람이 관여하는 것만으로도 충분히 사람이 개입된 것이라고 볼 수 있습니다"를 최대 오해로 지목하면서도, "만약 사람들이 AI가 생성한 텍스트를 읽고 편집하면서 자신의 목소리에 맞게 다듬 거나 특정 방식으로 수정한다면, 그것만으로도 충분히 인간의 개입이라고 생각합니다"라고 덧붙인다 [S4]. 진행자는 아예 "이 용어가 사람마다 다르게 해석되는 것 같아서요"라며 청중에게 정의를 물었다 [S4].

---

### 3B.5 전환 메커니즘 (CYCLE)

**있음.** 이 사례에서 확인되는 전환 규칙은 네 가지이며, 시점에 따라 정교해진다.

**(1) 되돌림 가능성 기준 (2026-07에 명문화) [S5]**
"그래서 우리가 가장 먼저 고려하는 원칙은 무언가를 되돌리기가 어려울수록, 더 일찍 그리고 더 적극적으로 , 가능하면 사람이 직접 검토해야 한다는 것입니다." [S5]
[S4]에서는 같은 취지가 법무 언어로 표현된다: "우리가 흔히 사용하는 ' 일방통행 문'이나 '양방통행 문' 같은 개념이 있나요? 문제가 발생하면 해결할 수 있나요?" 그리고 "위험 부담이 적고 쉽게 되돌릴 수 있는 일이라면, 인공지능이나 자동화에 더 많은 위험을 감수할 수도 있겠죠" [S4].

**(2) 결정론 가능성 기준 [S5]**
단계의 성격이 "X가 발생하면 항상 Y를 수행하라"이면 "그것은 AI가 처리할 일이 아닙니다"이고, AI는 "사고력이 필요한 단계에서 인공지능을 사용한다는 것입니다" [S5]. 이 선택적 배분의 근거는 비용과 신뢰성 양쪽이다(3B.8 참조).

**(3) '좋음'을 정의할 수 있는가 [S5]**
"만약 당신이 '좋은 것'이 무엇인지 정의할 수 있다면 , 아마도 당신은 우리가 보고 있는 이러한 자동화 AIC에 적합한 후보일 것입니다" [S5](AIC는 기계번역 오류로 보임).

**(4) 등급형 승인 = 데이터 민감도 기준 [S4]**
"내부적으로는 문이 아닌 안전 난간을 설치하는 방식을 채택하고 있으며, 단계별 승인 시스템을 운영하고 있습니다. 따라서 공개 데이터를 활용한 저위험 실험은 빠르게 진행되는 반면, 개인 식별 정보( PII)가 기업 시스템이나 제품 출시 단계에 통합되는 모든 작업은 더욱 상세한 AI 위험 평가 과정을 거칩니다." [S4]

**(5) 증강 → 자동화 방향의 실제 궤적**
- 2023년 해커톤 산출물 Zen GPT(현 Support Sidekick)가 "저희 회사 최초의 사내 AI 도구"로 시작해 상시 확장 프로그램으로 정착 [S2].
- 해커위크 산출물 64개 중 "about 20 of these workflows are now in full production" [S1] — 실험에서 운영으로의 선별 통과율이 명시된 유일한 수치.
- 에밀리 개인 에이전트: 개인 실험 → "수십 명의 사람들이 복사해서 사용한 것" → 2026-07 [S5]에서 Slack 응답 클론으로 시연.
- 투명성 장치의 미래 제거 예고: 로봇임을 밝히는 문구에 대해 "한 달 정도 더 사용해 보고 효과가 100% 확실해지면 그 기능을 없앨 수도 있을 것 같아요" [S5].

**(6) 역방향(자동화 → 증강/결정론 회귀)**
[S5]는 에이전트로 빠르게 시작한 뒤 다시 규칙 기반으로 되돌리는 패턴을 명시한다: "그리고 나서 다시 결정론으로 돌아가 보자면, 우리가 추구하는 것은 일관성, 정확성, 신뢰성인데, 이는 전반적으로 정말 흥미로운 흐름입니다" [S5]. 이는 유연한 판단(에이전트) → 견고화(결정론)라는, 논문 CYCLE과 방향이 같지만 **기계 내부에서의** 이동이다.

---

### 3B.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

### SPILL — 있음

**(1) 갱신 자동화 → CSM 대화 품질의 증강 [S1]**
"it actually allows the CSMS to go to the customers with all the information and and act quickly and confidently with them" [S1]. 리서치 과업의 자동화가 인접 과업(고객 대면 협상)의 인간 수행 조건을 바꾼다.

**(2) 콜 프렙 자동화 → 영업 시간 재배분 [S1]**
"this is where you're starting to see account executives become a lot more productive instead of having to do all this research themselves" [S1].

**(3) 지원 자동화 → 지원 담당자의 영업 과업 진입 [S3]** (SPILL과 REINV의 결합)
"as the support team's been using more automation AI to respond to tickets faster, we've unlocked some surplus capacity on the team and we're reinvesting that and now a customer support person at Zapier is much more actively involved in cross-selling, upselling, lead qualification, and so on." [S3]

**(4) 조정자(coordinator) AI = 다른 팀에 업무를 생성 [S5]**
네 번째 AI 직무의 정의 자체가 파급이다: "이는 다른 팀에게 업무를 창출하는 것입니다" [S5]. 예시는 "누군가가 슬랙에서 요청을 하면 자동으로 티켓으로 분류되고, 그 티켓이 담당자에게 할당된다는 것입니다" [S5].

**(5) 부정적 SPILL — '봇시팅' [S5, Glean 측정치]**
자동화 확산이 인접 인간 노동을 **증가**시키는 사례가 정량화되었다: "그래서 우리는 이것을 앉아서 일하는 로봇이라고 부릅니다"(=봇시팅), "디지털 노동자들은 평균적으로 일주일에 약 6시간 30분을 봇을 돌리는 데 소비하는 것으로 나타납니다" [S5]. 그리고 "이 모든 인력 노동은 제대로 추적되지 않는 경우가 많습니다. 조직 내에서 제대로 관리되지 않고 있지만, 관리되어야 합니다" [S5]. 이는 논문 SPILL이 항상 가치 창출로 귀결되지 않음을 보여주는 대항 증거다.

### REINV — 있음

**(1) 채용 프로세스 잉여를 후보자 피드백에 재투자 [S3]**
"with some of the ways they've updated the way that we do recruiting, more automation and AI in there, it's freed up just enough like elbow room as it were to actually be able to do this for the first time" [S3]. 대상은 최종 단계까지 온 불합격 후보자에 대한 개인화 피드백이다.

**(2) 지원 잉여 역량의 매출 활동 재투자 [S3]** — 위 SPILL (3) 인용과 동일.

**(3) 인력 대체가 아닌 역량 투자로의 전환 [S2]**
"저희는 인력 증원 보다는 팀원들의 역량과 사기 진작을 위해 새로운 도구를 도입하고 새로운 것을 배우도록 지원하는 데에도 집중해 왔습니다" [S2]. 결론부도 같다: "이건 정말로 직원들을 대체하는 게 아니라, 그들이 더 많은 일을 할 수 있도록 지원하는 것에 관한 겁니다" [S2].

**(4) 훈련 자원 투입 [S2]**
"그러니까 총 25시간 분량의 자기 주도 학습 콘텐츠와 마지막에 진행되는 과제들이 포함되어 있으며, 지원팀의 모든 구성원이 이를 완료해야 합니다" [S2].

**(5) 신설 직무로의 인력 이동 [S2, S3]**
인사팀 내 네 개 역할이 지정되었다: "네, 그분들은 AI 전환 관리자, AI 활용 능력 챔피언, AI 자동화 엔지니어, 그리고 AI 혁신 리더입니다" [S2]. [S3]에서 이는 외부 대담자에 의해 인력 재배치로 재확인된다: "you have developed and actually moved headcount over to have an AI automation engineer embedded in the talent team at Zapier" [S3].

**(6) 반대 방향의 자원 회수도 존재 [S2]**
Q팀 성과는 "인력 이탈로 인해 없어진 모든 직책을 다시 채우지 않고도 더 효율적으로 규모를 확장할 수 있다는 뜻입니다"로 서술된다 [S2]. 재투자와 인건비 회수가 동일 소스 안에 병존한다.

---

### 3B.7 통합 장치 (RESP)

**(1) 최상위 원칙 — 책임 비위임 [S2]**
CTO 겸 공동창업자 발언 인용: "일은 위임할 수 있지만, 책임은 위임할 수 없다." 그리고 마무리 발언에서 재인용된다: "AI를 통해 많은 작업을 자동화 하거나 위임할 수 있지만, 책임은 위임할 수 없습니다. 이 개념을 마음속에 새긴 팀은 이미 좋은 결과를 내는 데 절반은 성공한 셈입니다" [S2].
[S4]는 이를 조직 언어로 옮긴다: "생산성 향상과 자동화를 위해 AI를 적극적으로 활용하는 것은 맞지만, 결국 최종 결과물을 제출하는 사람은 여전히" 사람이며 "만약 제대로 작동하지 않는다면, 저희 Zappy 직원들이나 각 회사 직원들이 여전히 책임을 져야 합니다" [S4] (기계번역상 "Zappy"는 Zapier의 오기).

**(2) 거버넌스의 위치 — 워크플로 내재화 [S4]**
"제가 생각하기에 이런 격차가 발생하는 이유는 사람들이 거버넌스를 운영적인 문제가 아니라 정책적인 문제로 여기기 때문입니다"이고 "그 사건에서 얻은 교훈은 그룹 거버넌스를 워크플로에 내재화해야 한다는 것입니다" [S4].

**(3) 등급형 감독 [S4]**
"신뢰한다고 해서 감독이 필요 없다는 뜻은 아닙니다. 이는 비례적이고 예측 가능하며 신속한 감독을 의미합니다." [S4] (Kayak 발화자)

**(4) 인벤토리 우선 [S4]**
"AI 거버넌스 프로그램을 처음 구축할 때는 AI 사용 사례와 사용 중인 AI 시스템을 파악하고 목록을 만드는 것부터 시작하는 게 중요해요" [S4].

**(5) 벤더 실사 4문항 [S4]**
"우리의 데이터가 학습에 사용되고 있는지, 그리고 학습과 추론의 차이점을 이해하고 있는지 궁금합니다. 어디에서 처리되고 저장되나요? 누가 우리 데이터에 접근할 수 있나요? 그렇다면 세션이 끝나면 그것은 어떻게 되나요?" [S4]

**(6) 관찰가능성과 지속적 감독 [S4]**
"우리가 볼 수 없는 것들은 제대로 관리할 수 없다는 거죠"이며, "그래서 특히 AI 거버넌스 영역에서는 인간의 개입이 지속적인 과정입니다. 일회성 검문소가 아닙니다" [S4].

**(7) 기존 리스크 프로그램에의 통합 [S4]**
"AI는 기존 데이터 관리 방식을 확장하지만, 탄탄한 기반이 없다면 AI는 단순히 자동화를 통해 규정 준수 부담을 가속화할 뿐입니다"이며 벤치마크로 "NIST AI RMF나 ISO 42.01"을 든다 [S4] (ISO 42001의 오기로 보임).

**(8) 섀도우 AI 위험 [S4]**
"따라서 법률, 개인정보 보호, 규정 준수 관련 부서에서 AI 도입을 지지하지 않더라도 AI 도입은 여전히 진행될 것입니다. 안전 난간이 없으면 그런 일은 그냥 일어날 거예요" [S4].

**(9) 산출물 투명성 [S1, S5]**
사용자 대면 챗봇에 "always note the disclaimer here that this information is AI generated" [S1]. 에밀리 클론의 프롬프트에도 "당신이 일종의 로봇이라는 것을 설명해 주세요"가 들어 있고, 게스트는 "투명성이 부족하면 조직 내 신뢰가 빠르게 무너지는 경우가 많잖아요"라고 평가한다 [S5].

**(10) 필터·지연 등 비-AI 통제 장치 [S5]**
에밀리 클론은 "필터 단계를 사용해서 에밀리의 답변이 필요한 경우에만 계속 진행하도록 하는 거예요"와 5분 지연 단계를 둔다. 지연 이유는 "가끔 에밀리가 직접 답장을 할 수도 있거든요"이며 "에밀리가 반응하는 게 더 나을 테니까요" [S5] — 인간 우선권을 코드로 보장한 사례.

**(11) 거버넌스 구조와 소유권 [S2]**
전환 프레임워크 4요소는 "리더십, 인재 및 문화, 도구, 그리고 거버넌스"이고, 인력 모델은 "허브 앤 스포크 모델"이며 "우리는 이 다섯 가지 핵심 요소 각각에 대해 DRI라고 부릅니다"라고 직접 책임자를 지정한다 [S2] (4요소와 "다섯 가지"의 불일치는 3B.9 참조).

**(12) 제약 조건으로서의 승인권 [S2]**
"저와 저희 최고재무책임자(CFO)인 라이언이 모든 인력 충원 요청을 검토합니다. 저희는 새로 출시되는 모든 소프트웨어 버전을 검토합니다." [S2]

**(13) 검증 워킹그룹 [S2]**
"따라서 새로운 것을 출시하거나 Q 팀에 영향을 미치는 프로세스를 변경할 때마다 테스터 작업 그룹을 구성하여 우리가 만든 것을 검증하고 개선하도록 합니다" [S2]. 단, 도입 자체는 선택이 아니다: "무엇을 만들거나 사든, 그것은 선택 사항이 아닙니다" [S2].

---

### 3B.8 성과 수치

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 전사 AI 도입률 | "한 자릿수 퍼센트 정도" (2023 GPT-4 이전) | "97% adoption" (2025-09) / "우리 직원의 거의 100%가 정기적으로 AI를 활용" 및 "현재 우리 직원의 97%가 핵심 업무에 AI를 활용" (2025-11) | [S1] [S2] | **벤더 자체보고**. [S1]은 펄스 설문 + 백엔드 도구 사용량 교차확인("we're seeing that match") |
| 해커위크 제출 프로젝트 | 없음(첫 go-to-market 해커위크) | "we actually ended up having 64 projects submitted" | [S1] | 벤더 자체보고 |
| 해커위크 참여 인원 | — | "across 150 people in Zapier's go to market team", 참여는 "we made participation mandatory" | [S1] | 벤더 자체보고 |
| 실험→운영 전환 | — | "about 20 of these workflows are now in full production" | [S1] | 벤더 자체보고 |
| 지원팀 참여도(engagement) 점수 | "2024년 초 50점대 중반" | "현재 80점대 후반" (2025-11) | [S2] | 벤더 자체보고(사내 서베이) |
| 지원팀 인력 | — | "인력 이탈로 인해 없어진 모든 직책을 다시 채우지 않고도 더 효율적으로 규모를 확장" / "저희 Q팀은 더 적은 인원으로 더 빠르게 작업하고 있으며" | [S2] | 벤더 자체보고, **절대 수치 없음** |
| AI 활용 능력 교육 | — | "총 25시간 분량의 자기 주도 학습 콘텐츠" (지원팀 전원 필수) | [S2] | 벤더 자체보고 |
| 외부 프로그램 운영량 | — | "올해 하반기에만 AI 에이전트 빌더 세션부터 임원진 라운드 테이블까지 총 36개의 세션" | [S2] | 벤더 자체보고 |
| 워크플로 내 AI 단계 비중 | — | "평균적으로 AI 단계가 차지하는 비율은 18%에 불과" | [S5] | **벤더 자체 측정(플랫폼 텔레메트리)**, 제3자 검증 없음 |
| 복수 AI 역할 포함 워크플로 | — | "실제로 22%는 두 개 이상의 AI 관련 역할을 포함" | [S5] | 벤더 자체 측정 |
| 최초 도입 역할 | — | "1차 조사 대상자의 거의 80%가 커뮤니케이터 또는 사무직으로 시작했습니다" | [S5] | 벤더 자체 측정 |
| 선택적 아키텍처의 비용 절감 | 전 단계 AI 적용 | "71%의 비용 절감 효과" | [S5] | **벤더 자체 모델링(시뮬레이션)**. "600개 이상의 개별 단계로 구성된 24개의 워크플로우를 모델링" — 실측 아님 |
| 목표 개선 배율 | — | "10% 정도의 개선이 아니라 10배 정도의 개선일 것입니다" | [S2] | **목표치**, 실적 아님. 같은 소스에서 "오늘날 10배 개선의 사례는 찾아볼 수 없습니다"라고 인정 |
| 개인이 체감한 자동화 시간 | — | "주당 11시간의 업무가 이 기술에 의해 자동화되고 있다고 말합니다" | [S5] | **제3자(Glean) 자체보고 조사**, Zapier 수치 아님 |
| 조직 차원 가치 실현 | — | "같은 직원 중 13%는 소속 조직이 이 기술을 통해 실제로 이점과 가치를 얻었다고 답했습니다" | [S5] | 제3자(Glean) 조사 |
| 봇시팅 시간 | — | "일주일에 약 6시간 30분", 그중 맥락 제공에 "매주 약 두 시간 반" | [S5] | 제3자(Glean) 조사 |
| AI 세션 실패율 | — | "현재 AI 세션 10개 중 약 4개가 실패하는 것으로 나타나고 있습니다" | [S5] | 제3자(Glean) 조사 |
| AI 지출 계획 vs 위험 대비 | — | "경영진의 85%가 2026년에 AI 관련 지출을 늘릴 계획" / "실제로 위험 관리에 대비하고 있는 사람은 15% 미만" | [S4] | **출처 불명확** — "대부분의 지배구조 관련 조사에 따르면"으로만 언급 |
| AI 거버넌스 완성 전망 | — | "기업 리더 중 단 4%만이 올해 AI 거버넌스를 완전히 달성할 것으로 예상" | [S4] | "저희 연구에서 나온 또 다른 통계"라고만 함(Zapier 조사로 추정, 방법론 미공개) |
| 웨비나 청중 라이브 폴 | — | "32%는 진행 중이고, 36%는 공식 정책으로 28%를 추진하고 있으며, 21%는 현재 정책을 구축 중이고, 15%는 공식적인 AI 거버넌스 프레임워크를 마련했습니다" | [S4] | 라이브 폴. **합이 100%를 넘고 문장이 뭉개짐 — 기계번역 오류 가능성 높음. 인용 시 원문 그대로만 사용할 것** |
| 시간 절감 산정 방식 | — | "if you're saving 15 minutes per rep, you can sort of like extrapolate that out and provide a time savings calculation" | [S1] | 벤더 자체보고, **추정 방법론이지 실측치가 아님** |
| 2025-11 공개 방송 신청자 | — | "거의 1만 명에 가까운 사람들이 참석 신청을 하고 비용까지 지불했어요" | [S2] | 벤더 자체보고 |

**AI Workflow Index 방법론 원문 [S5]** — 이 표의 [S5] 행들을 해석할 때 반드시 병기해야 한다.
- "우리는 고객 기반에서 무작위로 선정된 1,500개 기업을 동일한 비율로 나누어 패널로 구성했습니다."
- "3분의 1은 대기업, 3분의 1은 규모가 큰 중견기업, 나머지 3분의 1은 규모가 작은 중견 기업에서 가져왔습니다."
- "거기서 상위 25%를 골랐습니다. 그래서 1,500개 업체 중 375개 업체가 AI가 적용된 자동화 기능의 개수를 기준으로 순위를 매겼습니다."
- "그리고 나서 우리는 2분기 중간쯤에 60일이라는 기간을 정해서 그 회사들이 해당 워크플로우를 어떻게 활용하고 있는지 측정하고 관찰했습니다."
- 설계 의도: "이 기술은 그에 못지않게, 어쩌면 그보다 더 가치 있는 일을 해낼 수 있는데, 그것은 바로 기업들이 말하는 것이 아니라 실제로 무엇을 하는지를 보여주는 것입니다."

즉 **모집단은 Zapier 고객사**이며, **AI 자동화 보유량 상위 25%만 선별**한 편향 표본이고, 관측 창은 60일이다. 따라서 18%·22%·80% 수치는 "AI를 이미 많이 쓰는 Zapier 고객"의 값이며 일반 기업 모집단으로 확장할 수 없다.

---

### 3B.9 소스 간 교차 대조

### (1) 반복 확인된 사실

- **AI 도입률 97%**: [S1](2025-09) "we've got 97% adoption" ↔ [S2](2025-11) "현재 우리 직원의 97%가 핵심 업무에 AI를 활용하고 있습니다". 2개월 간격, 동일 수치. [S1]은 백엔드 사용량으로 교차확인했다고 명시("we're seeing that match").
- **AI Fluency 프레임워크**: [S1] "it ranges from unacceptable to transformative", "And this is a very dumbed down version of a framework we have here at Zapier" → [S2] "해당 AI 활용 능력 프레임워크도 오픈 소스로 공개했습니다" → [S3] "Zapier open sourced its AI fluency framework". 세 소스에서 연속 확인.
- **채용 반영**: [S2] "Zapier에 채용하는 모든 직원에게 일정 수준의 AI 활용 능력을 요구하는 정책을 시행하기 시작했습니다" ↔ [S3] "we started assessing for AI fluency in the spring of this year ... for uh 100% of applicants and 100% of jobs that we hire into the company". 시행 시점(2025년 봄)이 [S3]에서 구체화된다.
- **해커톤 = 도입 촉진 수단**: [S1] 전체가 이 주장이고, [S2]에서 CEO가 재확인한다 — "이것이 아마도 가장 중요한 점이었고, 수백 명의 고객과 이야기를 나눠본 결과, 현재 시점에서 회사 내에서 도입을 촉진하는 데 가장 가치 있는 행동이라고 생각합니다".
- **3부 임팩트 프레임워크**: [S2] "효율성, 품질, 직원 경험" ↔ [S3] "efficiency, quality, employee experience, that's the three-part impact framework for Zapier". 네 번째 요소도 양쪽에 있다 — [S2] "이를 혁신적인 고객 가치라고 부르세요", [S3] "sometimes it unlocks an entirely new opportunity".
- **에밀리(AI 자동화 엔지니어)**: [S2](2025-11) 본인 등장 → [S3](2025-12) 외부 대담자가 인력 이동으로 언급 → [S5](2026-07) 그의 Slack 클론이 실물 데모로 등장. 3개 소스에 걸친 동일 인물의 궤적.
- **갱신(renewal) 에이전트**: [S1](2025-09) 해커위크 우승작으로 등장 → [S5](2026-07) 동일 성격 워크플로를 "시장 진출팀은 갱신 에이전트를 만들었습니다"로 재서술.

### (2) 한 소스에만 있는 사실

- 해커위크 운영 세부(브레인스토밍 3주 전 개시, 챔피언 지정, Jade 심사봇, 상금·스왜그) — [S1]만.
- 인력 운영 모델(허브 앤 스포크, COE, DRI, 네 개 역할) — [S2]만.
- 2026년 2대 베팅(Zapier 디지털 트윈 / AI 기반 가치 공학)과 성과 평가표 — [S2]만. [S3]에서 디지털 트윈만 재언급되고, [S4]·[S5]에는 **후속 결과가 전혀 나오지 않는다**.
- 지원팀 참여도 점수 50점대 중반 → 80점대 후반, 25시간 교육 프로그램, 티켓 코파일럿 — [S2]만.
- AI 리크루터 vs 인간 리크루터 선택지 실험 — [S3]만. 게다가 **데이터는 공개되지 않았다**: "I can actually share the data if folks are interested let me know in the questions" 라고만 하고 실제 수치는 나오지 않는다.
- 후보자 피드백 재투자 — [S3]만.
- 등급형 승인·인벤토리·4문항 실사·NIST/ISO 벤치마크 — [S4]만. 단, 상당수가 Rivian/Kayak 발화다.
- AI Workflow Index 방법론·18%·네 가지 일·71% — [S5]만.
- 봇시팅·11시간·13%·40% 실패율 — [S5]만이며 **Glean 측 수치**다.

### (3) 시점에 따른 서술 변화 (2025-09 → 2026-07)

담론의 무게중심이 **실험 → 역량 → 거버넌스 → 측정**으로 순차 이동한다.

1. **[S1] 2025-09 · 실험**. 핵심 어휘는 mandatory participation, 상금, 64개 제출, "permission and encouragement to fail, win, and learn using AI". 성공 지표는 소박하게 잡으라고 권한다: "I think a really simple one is just get everyone using AI every day." 거버넌스 어휘는 사실상 없고, human-in-the-loop은 개별 빌더의 설계 선택으로 등장한다.
2. **[S2] 2025-11 · 역량과 구조**. 도입(adoption)과 변혁(transformation)을 분리하고 — "우리는 AI 도입이 최저 수준을 높이고 있다고 이야기합니다" vs "천장을 높이는 것에 관한 이야기입니다" — 4요소 프레임워크, DRI, 성과 평가표, 인력 모델이 등장한다. 개인 실험의 조직화가 주제다. 거버넌스는 4요소 중 하나로 **처음 명시적 자리**를 얻지만 내용은 "AI 배포 방식을 표준화하기 시작할 것입니다"라는 예고 수준이다.
3. **[S3] 2025-12 · 역량의 정의**. AI Fluency가 프롬프팅 기술이 아니라 판단·크래프트임을 논증한다: "AI fluency is a whole lot more than like prompting skills". 훈련 방식도 뒤집힌다 — "We don't do a lot of if any like traditional L &amp; D or training on prompting or what have you". 여기서 처음으로 **재투자(REINV)가 명시적 언어**로 나온다.
4. **[S4] 2026-04 · 거버넌스**. 발화 주체가 인사·마케팅에서 **법무**로 바뀐다(Zapier 부법률고문 사회, Rivian·Kayak 리스크 담당자 패널). 정책·인벤토리·등급·섀도우 AI·벤더 실사가 주제다. 성과 서술은 거의 사라지고, 대신 "기업 리더 중 단 4%만이 올해 AI 거버넌스를 완전히 달성할 것으로 예상되었습니다"라는 **격차 진단**이 자리를 대신한다.
5. **[S5] 2026-07 · 측정**. 방법론이 전면에 나온다. "오늘 우리가 살펴볼 Zapier의 연구 결과는 실무자나 임원들을 대상으로 설문 조사나 인터뷰를 진행하는 전통적인 방식을 따르지 않습니다." 그리고 초기의 열광이 눌린다: "우리가 관찰하는 대부분의 자동화 시스템은 마법이라기보다는 배관 설비에 훨씬 더 가깝습니다."

**같은 사안의 서술 변화 3건**

- *갱신 워크플로*: [S1]에서는 "The handoff is made automatically"로 자동화 성취가 강조되고, 인간 개입은 "people can always come in and change that recommendation"이라는 사후 정정으로만 언급된다. [S5]에서는 동일 워크플로가 "이 과정에 사람은 전혀 관여하지 않았습니다"라고 더 강하게 자동화로 규정되는 **동시에**, 고객 발신 단계에서 인간 개입이 원칙에 의해 배치된다. 즉 10개월 사이에 인간 개입이 *사후 정정*에서 *사전 설계 규칙*으로 이동했다.
- *AI에 대한 기대치*: [S2]는 "10배 정도의 개선"을 목표로 내걸면서 즉시 "오늘날 10배 개선의 사례는 찾아볼 수 없습니다"라고 단서를 단다. [S5]에서는 AI가 워크플로 단계의 18%에 불과하다는 실측이 제시된다.
- *AI 확산의 프레이밍*: [S1]은 "most AI pilots are are failing"을 **시장의 문제**로 진단하고 해커위크를 해법으로 제시한다. [S5]는 "이러한 구현이 실패하는 경우를 많이 보는데, 그 근본적인 원인은 기술적인 문제뿐만 아니라 인적인 문제인 경우가 많습니다"로 원인을 인적 요인으로 재귀속한다.

### (4) 모순 / 불일치

1. **앱 연동 수** — [S1](2025-09) "8,000 integrations" / [S4](2026-04) 같은 발화자가 도입부에 "거의 99,000개 이상의 앱을 연결합니다", 후반부에 "저희는 9,000개 이상의 앱을 제공하고 있습니다". 99,000은 기계번역/음성인식 오류일 개연성이 높으나 **원문 그대로 두 값이 병존**한다. 이 수치를 논문에 인용하려면 반드시 소스 내부 모순을 명시해야 한다.
2. **도입률 97% vs 거의 100%** — [S2] 한 소스 안에서 CEO는 "우리 직원의 거의 100%가 정기적으로 AI를 활용할 수 있게 되었습니다"라 하고, 몇 문단 뒤 브랜든은 "현재 우리 직원의 97%가 핵심 업무에 AI를 활용하고 있습니다"라 한다.
3. **프레임워크 요소 개수** — [S2]는 "리더십, 인재 및 문화, 도구, 그리고 거버넌스"를 반복적으로 4요소로 제시하면서("우리가 그 목표를 달성하는 데 도움이 된다고 생각하는 네 가지 요소가 있습니다"), 인력 모델 설명에서는 "우리는 이 다섯 가지 핵심 요소 각각에 대해 DRI라고 부릅니다"라고 다섯을 말한다. 또한 영향 사례를 두고 "리더십, 인재, 문화, 도구, 거버넌스라는 네 가지 요소"라고 다섯 항목을 나열하며 '네 가지'라 칭한다 — 기계번역 오류 또는 인재/문화 분리 여부의 혼선.
4. **해커톤 주기** — [S1] 엔지니어링 팀은 분기 단위("that happens quarterly") / [S2] "저희는 이러한 해커톤을 몇 달에 한 번씩, 대략 4~6개월에 한 번씩 반복합니다".
5. **해커위크의 역사** — [S2]는 "Zapier는 회사 설립 14년 전부터 해킹 주간을 운영해 왔습니다"라고 하는데, 같은 소스에서 회사 창립 자체가 14년 전이다("14년 전 자피어 창립 초기부터"). 기계번역 오류로 보이지만 원문대로면 사실 오류가 된다.
6. **자동화의 인력 효과에 대한 상반된 프레이밍** — [S2] 내부에서 "인력 이탈로 인해 없어진 모든 직책을 다시 채우지 않고도"(인건비 회수)와 "이건 정말로 직원들을 대체하는 게 아니라, 그들이 더 많은 일을 할 수 있도록 지원하는 것에 관한 겁니다"(비대체)가 병존한다.
7. **거버넌스 성숙도의 자기평가 부재** — [S4]는 4%라는 산업 전체 진단을 제시하지만 Zapier 자신이 그 4%에 속하는지는 어느 소스에도 없다. **해당 소스에 없음.**
8. **2대 베팅의 후속 결과** — [S2](2025-11)에서 2026년 목표로 선언된 디지털 트윈과 AI 기반 가치 공학의 실행 결과는 [S4](2026-04), [S5](2026-07) 어디에도 보고되지 않는다. **해당 소스에 없음.**
9. **인간 개입 정의의 조직 내 불일치** — [S4] 안에서 "직간접적으로 사람이 관여하는 것만으로도 충분"을 오해로 지목하는 발언과, AI 텍스트 편집만으로도 "충분히 인간의 개입"이라는 발언이 같은 화자에게서 연달아 나온다.

---

### 3B.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 판정 |
|---|---|---|
| AUTO/AUG 정의 (p.194) | 갱신 리서치·핸드오프·이벤트 탐색은 AUTO ("이 과정에 사람은 전혀 관여하지 않았습니다" [S5]); 고객 발신·심층분석 실행·회신 검토는 AUG [S1][S2][S5] | **지지** |
| CYCLE: 증강 학습→견고화→자동화 (p.196-197) | 해커위크 실험 64건 중 20건 운영 이관 [S1]; Zen GPT → Support Sidekick → Ticket Copilot 계보 [S2]; 에밀리 개인 에이전트 → 사내 복제 → Slack 클론 [S2][S5] | **지지** |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 되돌림 불가 접점에서의 인간 재삽입 [S5]; 에이전트 → 결정론 회귀 [S5]; 다만 회귀의 트리거는 '조건 변화'가 아니라 **사전 설계된 위험 등급**이다 [S4] | **보강** |
| SPILL: 한 과업 자동화가 인접 과업 증강 유발 (p.197) | 갱신 리서치 자동화 → CSM 대화 증강 [S1]; 지원 자동화 → cross-sell/upsell/lead qualification 진입 [S3]; 코디네이터 AI가 "다른 팀에게 업무를 창출" [S5] | **지지** |
| SPILL (p.197)의 이면 | 봇시팅 주 6.5시간, "이 모든 인력 노동은 제대로 추적되지 않는 경우가 많습니다" [S5, Glean] — 파급이 가치가 아니라 **미측정 부채**로 나타남 | **확장/부분 반증** |
| REINV: 자동화 자원의 증강 재투자, UBS 패턴 (p.201) | "we've unlocked some surplus capacity on the team and we're reinvesting that" [S3]; 채용 잉여 → 후보자 피드백 [S3]; 25시간 교육·신설 4개 역할 [S2] | **지지** |
| REINV (p.201)의 한계 | 같은 조직에서 "인력 이탈로 인해 없어진 모든 직책을 다시 채우지 않고도" [S2] — 재투자와 인건비 회수가 병존 | **보강(조건부)** |
| RESP: 인간이 프로세스 전체 책임 보유 (p.200) | "일은 위임할 수 있지만, 책임은 위임할 수 없다." [S2]; "결국 최종 결과물을 제출하는 사람은 여전히" 사람 [S4]; 등급형 승인 [S4]; AI 생성 고지 [S1][S5] | **지지** |
| 증강 학습은 도메인 전문가의 암묵지에 의존하며 IT/외부 위임 불가 (p.195) | "그 고통의 핵심에 깊이 관여하고 있는 사람이 바로 인공지능을 활용해 그 고통을 자동화하는 데 가장 적합한 사람이다" [S2]; 해커위크가 IT가 아닌 영업·CS·마케팅 실무자에게 빌드를 맡긴 설계 [S1]; "is coding required for building more complex apps?"라는 청중 질문에 RevOps 리드가 "No."라고 답함 [S1] | **지지(강)** |
| 기계 한계 ① 목적·자아 부재 (p.198) | "AI는 도구입니다. 결과가 아닙니다." [S2]; "don't do AI for AI's sake" [S3] | **지지** |
| 기계 한계 ② 제약 완화된 옵션만 제시 (p.198) | 갱신 에이전트가 "making a call on what type of renewal the agent thinks it should be" 하되 최종 판단은 인간 [S1]; 커뮤니케이터 AI는 콘텐츠만 만들고 "무엇을 해야 할지 결정하는 권한은 결국 사람에게 있습니다" [S5] | **지지** |
| 기계 한계 ③ 훈련된 과업에 국한 (p.198) | "에이전트에게 여러 가지 일을 동시에 맡기려고 한다는 것입니다"를 대표적 실수로 지목 [S5]; 단일 과업 분해가 우수 빌더의 특징 [S5] | **지지(강)** |
| 기계 한계 ④ 감각·감정·사회기술 부재 (p.198) | 톤·공감을 사람이 설계해 프롬프트에 주입("에밀리는 아주 상냥 하고 착하고 느긋해요") [S5]; AI 카피에 대한 거부감 "There is nothing that is more of a turnoff to me than when I can tell it's AI." [S3] | **지지** |
| 한쪽 편중 시 악순환 (p.199) | 자동화 편중의 악순환이 [S5]에 구체적으로 기술됨 — AI로 5개 요점을 12페이지로 늘리고 수신자가 다시 5개로 줄이는 "쳇바퀴"; 개인 생산성 지표만 보면 "조직에 오히려 악영향을 미칠 수 있는 방식으로 개인의 생산성을 극대화하려는 자연스러운 경향" | **지지(강, 새 메커니즘 제시)** |
| 기계는 조직 내 새로운 행위자 계급 (p.204) | "이제 인공지능이 글을 쓰고, 서류를 정리하고, 결정을 내리고, 다른 사람을 위한 업무를 만들어내고 있습니다. 특히 마지막 항목, 즉 다른 사람을 위한 업무를 만들어내는 것이야말로 인공지능이 이제 막 하기 시작한 가장 인간적인 행동일지도 모릅니다." [S5] | **지지(강)** |
| AUTO/AUG **이분법** 자체 | "무엇을 자동화할 수 있고, 무엇을 증강할 수 있으며, 무엇이 고유하게 인간적인 요소로 남아 있어야 하는지" [S5] — 3분법. **단, Glean 게스트 발화이며 AI Workflow Index의 산출물이 아니다** | **확장(귀속 주의)** |

**이 사례가 논문을 확장하는 지점**

첫째, 논문의 자동화/증강 이분법은 과업(task) 수준에서 그어지지만, [S5]는 경계를 **워크플로 내부의 단계(step)** 로 내려 긋는다. 하나의 워크플로에서 AI 단계는 평균 18%뿐이고 나머지는 결정론적 로직이며, 이 선택적 배치가 71% 비용 절감과 신뢰성 양쪽의 근거로 제시된다 [S5]. 즉 실무에서 자동화와 증강은 서로 다른 과업에 배정되는 것이 아니라 **같은 과업의 서로 다른 단계에 교대로 배정**되고, 그 결정 규칙은 "사고력이 필요한 단계"인가라는 판단이다.

둘째, 이 사례는 증강/자동화 배분에 대해 논문에 없는 **조작 가능한 결정 규칙 두 가지**를 제공한다 — 되돌림 가능성("무언가를 되돌리기가 어려울수록, 더 일찍 그리고 더 적극적으로 , 가능하면 사람이 직접 검토해야 한다" [S5])과 데이터 민감도 등급("공개 데이터를 활용한 저위험 실험은 빠르게 진행되는 반면, 개인 식별 정보( PII)가 기업 시스템이나 제품 출시 단계에 통합되는 모든 작업은 더욱 상세한 AI 위험 평가 과정을 거칩니다" [S4]). 논문의 RESP가 규범적 요청에 가깝다면, 여기서는 승인 게이트의 배치 위치를 계산하는 함수가 된다.

셋째, SPILL의 부정적 사례가 정량화되어 있다. 논문은 한 과업의 자동화가 인접 과업의 증강을 유발한다고 보지만, [S5]의 봇시팅(주 6.5시간, 그중 맥락 제공 2.5시간)은 그 유발된 인간 노동이 **조직에 계측되지도 관리되지도 않는 부채**로 축적됨을 보여준다. 개인 수준 자동화 체감(주 11시간)과 조직 수준 가치 실현(13%) 사이의 간극은 SPILL이 자동으로 가치로 전환되지 않으며 조정(coordination)이라는 별도 조건을 요구함을 시사한다.

넷째, 담론 자체가 CYCLE의 조직 수준 대응물로 읽힌다. 10개월에 걸쳐 Zapier의 공개 발화는 실험(2025-09) → 역량 정의(2025-11~12) → 거버넌스(2026-04) → 측정(2026-07)으로 이동했고, 발화 주체 역시 마케팅·인사에서 법무를 거쳐 연구 기능으로 옮겨갔다. 논문이 개별 과업 수준에서 서술한 학습→견고화 순서가, 조직의 **담론과 책임 소재 이동**에서도 동형으로 관찰된다는 것이 이 사례의 고유 기여다.

---

### 3B.11 인용 시 주의사항

**1. 벤더 자체보고 vs 제3자**
- 5개 소스 전부 Zapier 채널의 **자사 마케팅 웨비나/사내 방송**이다. 독립 검증된 수치는 하나도 없다.
- [S5]의 Glean 수치(11시간, 13%, 6.5시간, 2.5시간, 40% 실패율)는 **Glean의 자체 조사**이며 Zapier 데이터가 아니다. 이를 "Zapier가 측정했다"고 쓰면 귀속 오류다.
- [S2]의 맥켄지 인용은 슬라이드로만 제시되고 보고서명·표본·기간이 없다("이 아기는 겨우 30~45일 됐어요"가 유일한 시점 단서).
- [S4]의 85%/15%/4%는 출처 표기가 사실상 없다.

**2. 성숙도 — 계획인가 운영인가**
- **계획/예고 단계**: 성과 평가표는 [S2] 시점에 "여기 있는 모든 데이터는 모의 데이터입니다. 합성 소재입니다. 아직 실제 점수가 아닙니다"이며 "저희는 내년 1월부터 이 모든 것에 대한 점수 측정을 시작할 예정입니다". 2026년 2대 베팅도 [S2]·[S3] 모두 선언 단계이고, [S3]에서 본인이 "I don't know exactly how we're going to do that yet"라 인정한다.
- **운영 단계**: 해커위크 산출 20개 워크플로 [S1], Ticket Copilot(단, "코파일럿도 테스트 기간이 끝나면" 의무화 예정 [S2]), AI Fluency 채용 심사 [S3], 에밀리 클론 [S5].
- 에밀리 클론은 [S5] 시점에도 완결되지 않았다 — 로봇 고지 문구 제거가 검토 중이고, 부적절 응답 방지책은 "어쩌면 에밀리가 프롬프트에 그 내용을 넣었는데 제가 못 봤을 수도 있지만"이라는 추정 수준이다 [S5].

**3. 자막 오류 — 반드시 원문 그대로 인용할 것**
- [S1]: "Netswuite"(NetSuite), "chief petite the agent"(cheat/chief 혼동), "Zapri MCP"/"Zapper"/"Zap year"(Zapier), "sap trends"(Zap trends), "KOD"/"koda"/"COD"(Coda로 추정), "at your table"(Zapier Tables로 추정), "Whimo"(Waymo), "Codeilot"/"C-pilot"(Copilot).
- [S2]: "Zap Your"/"Zappier"(Zapier), "GPD4"(GPT-4), "WDE"(Wade), "파업 트리거"/"스트라이크 트리거", "지원 사이드킥"/"Zen GPT", "Netswuite" 계열 오기, "Nadin"/"NAND"(n8n으로 추정 — 단정 금지), "인공지능 활용 능력"과 "AI 유창성"이 같은 프레임워크를 가리키는 두 번역어.
- [S3]: "Zachary"(Zapier), "Zap year", "Panda"/"Panadoc"/"handock"(PandaDoc), "Simute"(성 표기 불안정), "L &amp; D"(HTML 엔티티가 원문에 그대로 남아 있음 — 인용 시 이 형태 유지).
- [S4]: "Zappy"/"Zappier"(Zapier), "하 야크"(Kayak), "ISO 42.01"(ISO 42001로 추정), "Mints"(Ministry/컨설팅 부서명 불명), "제 공간에서는"/"마이스페이스에서처럼"(my space = 자기 영역의 직역), "결정a"(오타), "DI, 아니, 정확히는 데이터"(발화 정정이 그대로 남음), "회의 식 익명 보고"(의미 불명), "거의 99,000개".
- [S5]: "글린"/"글렌"(Glean), "자 피어"(Zapier), "AS 단계"(AI 단계로 추정), "AIC"(의미 불명), "로스(Ross)의 수백 개 주요 도입 기업"(의미 불명), "AI의 네 가지 규칙"(four jobs를 '규칙'으로 오역), "Zapier AI 워크플로 목차"(Index를 '목차'로 오역), "AI 관련 업무 목록"(Glean 보고서 제목의 오역).
- **특히 [S5]의 핵심 개념어가 번역마다 흔들린다**: "네 가지 일"은 "네 가지 역할", "AI 관련 직무", "AI의 네 가지 규칙"으로 각각 옮겨져 있다. 네 항목의 한국어 표기도 "의사소통 담당자/사무 담당자/분석가/조정자"와 "커뮤니케이터/사무 보조원/분석가/코디네이터"가 혼용된다. 논문에 인용할 때는 반드시 원문 문장을 그대로 옮기고 역명 표기 불안정을 각주로 밝혀야 한다.
- 한국어 자막 전반에 **어절 앞뒤 불규칙 공백**(예: "추출 하고", "적극적으로 ,", "직원 과")과 문장 끝 공백이 있다. 기계 대조 검증을 통과하려면 이 공백까지 그대로 복사해야 한다.

**4. 귀속 문제**
- [S4]의 거버넌스 실무 장치 대부분은 **Rivian(제니)와 Kayak(케이티)** 의 발언이다. "문이 아닌 안전 난간", "단계별 승인 시스템", 4문항 실사, NIST/ISO 벤치마크, 인벤토리 우선은 **Zapier의 실무가 아니라 Kayak/Rivian의 실무**다. Zapier 자신의 진술로 확인되는 것은 규제 봇 운영("Zapier에서는 실제로 다양한 AI 관련 규정을 수집하는 규제 봇을 운영하고 있습니다. 하나만 있는 게 아닙니다."), 기존 규정 검토 프로세스와의 통합 주장, "저희 Zapier에서도 비슷한 접근 방식을 취하고 있습니다"라는 동조 정도다. 이 구분을 흐리면 사례 자체가 무너진다.
- [S5]의 3분법("자동화 / 증강 / 고유하게 인간적인 요소")은 **Glean 측 레베카의 발화**이며, Zapier AI Workflow Index의 발견물이 아니다. 인덱스가 산출한 것은 "네 가지 일"과 18%·22%·80%·71%다.
- [S3]의 상당 부분은 PandaDoc(Keith)의 사례다. 보이스 에이전트, 엔터프라이즈 검색 도구, 고빈도-고마찰 패러다임은 PandaDoc 것이며 Zapier 사례로 쓰면 안 된다.
- [S1]의 사용 사례들은 개별 직원(Sarah, Mitchell, Denise/Lacy/Stacy)의 해커위크 산출물이며 전사 표준 프로세스가 아니다. 이 중 운영 이관된 것이 어느 것인지는 명시되지 않았다 — **해당 소스에 없음**.

**5. 표본 편향**
AI Workflow Index의 모집단은 Zapier 고객사 1,500곳이고, 그중 AI 자동화 보유 상위 25%(375곳)만 분석 대상이다 [S5]. 관측 창은 2분기 중 60일. 따라서 이 사례의 어떤 수치도 일반 기업 모집단으로 일반화할 수 없으며, "AI를 이미 적극 사용하는 자동화 플랫폼 고객"이라는 조건을 항상 병기해야 한다.

**6. 시점 표기**
5개 소스 모두 채널 수집분이며 헤더의 "업로드일"이 발화 시점이다. 다만 [S2]는 사내 전체회의 실황이므로 업로드일 = 발화일로 볼 수 있으나, [S1]·[S3]·[S4]·[S5]는 라이브 웨비나 녹화의 게시 시점일 수 있다. 소스에 녹화일과 게시일의 차이를 확인할 정보는 **없음**. 또한 [S2] "저희는 내년 1월부터", [S3] "in the spring of this year" 등 상대 시점 표현이 많으므로, 절대 연월로 환산해 인용할 때는 업로드일 기준임을 명시해야 한다.


---



## 사례 4–5 — 삼성SDS 계열 : 우리은행 전 업무 재설계 + 삼성전자 VOC 분류

*원문: `docs/cases/04_samsungsds.md`*

# 사례 4-5 - 삼성SDS 계열 : 우리은행 전 업무 재설계 + 삼성전자 VOC 분류

> **시점에 관한 최우선 경고**: 이 사례의 5개 소스는 **전부 키워드 검색 수집분**(`transcripts/YYYY-MM-DD/...`)이다.
> 파일 헤더에 "업로드일" 메타가 존재하지 않으므로, 아래 표의 날짜는 **모두 수집일**이며 **영상 업로드 시점이 아니다**.
> 발화 시점(발표가 실제로 이뤄진 날짜)은 다섯 소스 어디에도 명시되어 있지 않다. 본문에서 "발표 시점"이라 쓸 때는
> 발화자가 "올해/작년"이라고 말한 **화자 기준 상대시점**을 뜻하며, 절대 연월로 환산할 근거는 소스에 없다.

---

### 4-5.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | 삼성SDS AX | **수집일 2026-07-26** (업로드일 메타 없음, 업로드 시점 불명) | ko | 약 5546개 | 파일 제목 「AI-Native 기업으로 전환 전략과 사례」. 발화자명은 본문에 없으나 "저희 SS의 사례입니다"·"AX센터"·"저희 SDS는" 등 삼성SDS AX센터 소속 발화. S2·S3와 동일 슬라이드 구성 | https://www.youtube.com/watch?v=Y-ApGj-9ceI | /home/user/youtube-scrap/transcripts/2026-07-26/AI-Native_기업으로_전환_전략과_사례__Y-ApGj-9ceI.md |
| [S2] | 삼성SDS AX | **수집일 2026-07-23** (업로드일 메타 없음) | ko | 약 3155개 | 파일 제목 「[AX Summit] 2. (키노트)AI Native 기업으로의 전환 방안과 사례(AX센터 AI사업팀장 신계영 부사장)」. 삼성SDS 자사 주최 행사(AX Summit) 키노트 | https://www.youtube.com/watch?v=PsfnMJwSoXs | /home/user/youtube-scrap/transcripts/2026-07-23/[AX_Summit]_2._(키노트)AI_Native_기업으로의_전환_방안과_사례(AX센터_AI사업팀장_신계__PsfnMJwSoXs.md |
| [S3] | **IT조선** (제3자 미디어 채널) | **수집일 2026-07-21** (업로드일 메타 없음) | ko | 약 3683개 | 파일 제목: 「[AI&CLOUD2026] 세션1 AI-Native 기업으로의 전환 방안 및 사례 / 삼성SDS / 신계영 AX센터 AI사업팀 부사장」. 외부 컨퍼런스 세션 | https://www.youtube.com/watch?v=mHbsngztlHw | /home/user/youtube-scrap/transcripts/2026-07-21/[AI&CLOUD2026]_세션1_AI-Native_기업으로의_전환_방안_및_사례_삼성SDS_신계영_AX센터__mHbsngztlHw.md |
| [S4] | 삼성SDS AX | **수집일 2026-07-26** (업로드일 메타 없음) | ko | 약 3697개 | 웨비나. 사회 「삼성 SDS AI 사업팀 김혜식 프로」, 발표 「오픈 AI ... 어카운트 디렉터 한지은」, "삼성 SDS에서 AI 사업 개발을 담당하고 있는 조규어 프로" | https://www.youtube.com/watch?v=oXxq-xeAoJQ | /home/user/youtube-scrap/transcripts/2026-07-26/ChatGPT_Enterprise_도입전략__oXxq-xeAoJQ.md |
| [S5] | 삼성SDS and KASMO 인공지능혁신추진단 | **수집일 2026-07-18** (업로드일 메타 없음) | ko | 약 7100개 | 토크쇼형 좌담(파일 제목 「제조업 AX의 골든 타임 ⏰ 중요한 것은 AI 도입보다 이것?! 📢 IT슈다 EP. 제조」). 출연: 서울대 기계공학과 윤병동 교수(창업 CEO 겸직), 인공지능혁신추진단 안광현 단장, 삼성SDS 컨설팅팀 김지현 프로(IDP 담당, "20년째 근무"), 삼성SDS 에반젤리스트 그룹 김유리 프로 | https://www.youtube.com/watch?v=iAbE9YXnbqA | /home/user/youtube-scrap/transcripts/2026-07-18/제조업_AX의_골든_타임_⏰_중요한_것은_AI_도입보다_이것!_📢_IT슈다_EP._제조__iAbE9YXnbqA.md |

각 소스의 역할:

- **[S1] 1차 근거.** 우리은행·삼성전자 VOC·삼성SDS 자사 조직/인증 세 사례를 모두 담은 유일한 소스이며 분량도 가장 길다. 에이전트 옵스/거버넌스 서술이 가장 상세하다.
- **[S2] 1차 근거(대조군 겸용).** 동일 발화자·동일 사례를 자사 행사에서 다시 서술한 판본. S1과 수치가 어긋나는 지점이 이 사례의 핵심 관찰 대상이다.
- **[S3] 1차 근거(대조군 겸용).** 동일 발화자·동일 사례를 **외부 미디어 주최 컨퍼런스**에서 서술한 판본. 우리은행 에이전트 수를 SDS가 재산정했다는 진술, 콜센터 로드맵, 시장조사 에이전트가 S3에만 있다.
- **[S4] 보강.** 우리은행·삼성전자 사례는 전혀 나오지 않는다. HITL(승인·통제권) 서술과 삼성SDS 자사 유즈케이스 수치를 보강한다.
- **[S5] 보강/대조군.** 우리은행·삼성전자 VOC는 전혀 나오지 않는다. 제조 도메인의 암묵지·현장 반감·바텀업 논거로 논문 p.195 명제와 대조하는 데 쓴다. 삼성SDS 발화자는 신계영 부사장이 아닌 **다른 소속(컨설팅팀·에반젤리스트 그룹)** 이라 사내 관점차 확인에 유용하다.

---

### 4-5.2 조직과 문제 상황

**우리은행 (사례 4)**

- 출발점은 최고경영진 선언이다. S1: "우리 은행은 작년 한 해 동안 이i 컨설팅과 어 A를 하겠다라고 좀 선언을 하시면서 **은행장께서** 우리 은행은 어 금융 회사지만 앞으로는 AX 회사도 거듭나겠습니다." [S1]
- S2는 같은 사건의 주체를 다르게 부른다: "우리는 금융 회사지만 우리는 앞으로 AX 회사다라고 선언을 어 **대표님께서** 선언을 하시면서 1년 동안 5대 업무를 선정을 하고" [S2]
- S3는 컨설팅 기간을 명시한다: "우리 은행은 작년에 **컨설팅 회사와** 어, **1년에 걸쳐서** 어, ax로 우리는 전환하겠다. 금융 회사이긴 하지만 우리는 ax 회사라고 이렇게 시욕해서 선언을 하시고" [S3]
- 컨설팅 산출물의 범위: "그러면 그중에서 먼저 핵심 5대 업무를 좀 정의를 한 다음에이 5대 업무를 **엔듀텐드 프로세스를 다 1년 동안 컨설트를 통해서 정의를 하셨습니다**." [S3]
- 대상 업무의 이름은 두 소스에서 조금 다르게 열거된다. S2: "고객 관리 기업 여신에서부터 자산 관리 업무자동화까지" [S2] / S3: "각각의 어 기업 어 여신부터 업무자동까지 다섯 개 업무" [S3]. S1은 업무명을 열거하지 않는다.
- before 상태(AS-IS)에 대한 정량 서술 — 예: 기존 인원, 처리 건수, 소요 시간 — 은 **세 소스 어디에도 없음**. 우리은행 관련 before 수치는 해당 소스에 없음.

**삼성전자 VOC (사례 5)**

- 수집 규모: "그 VUC들이 어 **일주일에 보통 한 30몇만 건씩** 들어오거든요." [S1] (과업 지시문의 「주 30여만 건」과 대응하나, 파일의 실제 문자열은 "30몇만"이다.)
- 수집 목적과 투자: "전 세계로부터 **막대한 돈을 투자해서** 다양한 VOC들을 수집을 하고 있습니다." [S1]
- before 상태(병목): "실상 일주일에 수십만 건의 데이터가 들어오게 되면 담당하는 인력 한 몇 명이는 그 전체를 볼 수가 없죠. 그러다 보니까 특정 데이터들 중에서 눈에 띄는 것들만 중심으로 보면서" [S1]
- 검토 커버리지 before: "기존에는 **5% 7%**만 보던 다양한 VOC들" [S1]
- 담당 인력 수는 "한 몇 명"이라는 표현뿐, 정확한 인원은 해당 소스에 없음 [S1].

**삼성전자 전사 에이전트 규모 (두 소스가 다르게 말함)**

- S1: "저희 고객사들 중에서 삼성전자만 해도 지금 거의 어 **천개 단위에서 이제 만 개 단위**의 에이전트로 이제 돌아가고 있는데" [S1]
- S3: "삼성 전자 같은 경우에는 **작년에 이미 한 만여 넘겨는 에이전트**가 현재 만들어서 동작을 하고 있다 보니까" [S3]

**삼성SDS 자사 (사례 4-5의 배경 조직)**

- 조직 신설 시점: "저희도 다른 회사 IT 회사보다 좀 늦게 좀 AX센터 출범을 했습니다. **작년 12월에** 전사적으로 AI를 하고 있는 어 모든 개발자, 상품 기획자 실행하는 사람들을 좀 모아다가 어 하나의 조직 AX 센터를 좀 만들어서" [S1]
- 그룹 차원 확산: "삼성 관계사는 사실 작년 말 조직 협표한테 다 이렇게 AI 컨트롤 타워들을 다 조직만화 만들었습니다." [S1]
- AI 크루 규모: "저희 같은 경우에는 현재 **AI 크루가 107명**이 활동을 하고 있고" [S1] / "실주로 저희 현재 AS SDS AI 크루는 **한 107명 정도**가 활동을 하고 있고요." [S2]
- 자사 유즈케이스: "삼성 SDS는 **16개 부서와 50개 이상의 유즈 케이스**를 기반으로 여섯 가지 키워드 즉 자동화, 효준화, 콘텐츠 생성, 에이전트와 리서치 고도와 데이터 거버넌스 중심으로" [S4]

---

### 4-5.3 자동화 구간 (AUTO)

**(1) VOC 분류 — 전량 기계 처리로 이관된 대표 구간**

발화자는 이 과업을 명시적으로 「모델이 매우 잘할 수 있는」 것으로 분류한다.

> "VC 분류하는 에이전트라는 걸 도입을 하니까이 VC 분류 에이전트는 필요도 없고 또 VOC를 분류하는 거 자체가 어 **생성력 AI 모델이 매우매우 잘할 수 있는 타스크입니다**. 그래서이 에이전트가 성능이 꽤 높은 확률로 에이전트가 어 동작을 하면서 VOC를 성공적으로 분리하는 것들을 저희가 관찰할 수 있었는데" [S1]

> "기존에는 5% 7%만 보던 다양한 VOC들을 **에이전트가 전체 다 봐주니**" [S1]

즉 분류라는 하위 과업 자체는 인간 루프에서 빠졌다(AUTO). 다만 분류 결과의 후속 판단이 인간에게 남는지는 4-5.4에서 다룬다.

**(2) 탑다운 어프로치의 극단적 자동화 언어**

S1은 삼성SDS의 탑다운 접근을 「사람을 뺀다」는 표현으로 서술한다. 논문의 자동화 정의(인간을 루프에서 제외)와 어휘 수준에서 정확히 겹친다.

> "근데 반대로 탑다운 오프로치는 저희는 좀 되게 과격하게 생각을 해요. 그래서 야 **특정이 부서 없어지면 큰일 나. AI가 들어와서 한번 없애 보자. AI로 한번 없애 볼까?이 업무 프로세스 한번 전체를 사람 한번 빼 볼까?** 이런 어프로치가 저희는 탑 어프로치 생각을 하거든요." [S1]

> "심지어는 하나의 세 기존에 특정 업무를 하던 부서를 없애고 그 부서를 전부로 자동화하고 자유를 할 수 있겠다라는 관점으로 접근을 하는 부분입니다." [S2]

> "쉽게 생각하면 프로세스를 프로세스에 돈 특히 **특정 부서를 사람을 대체하는 쪽으로 접근**을 하는 어 방법이 되겠고요." [S3]

**(3) 챗봇 → 에이전트 전면 대체 (삼성전자 서비스 사이트)**

> "그 체포이 기존에도 있었습니다. 이런 전통적인 반 체포이 있는데 전통 전통적인 체포은 체포 디자이너라 걸 통해서 이런 질문이 나오면 이렇게 답변해 줘라고 하는 시나리오를 다 설계를 하고 시나리오 대로 질의 응답이 되는데 시나리오 밖에 있는 질문을 했을 때는 잘 답변을 못 하고 ... **이 부분을 에이전트 기반으로 대체를 진행을 했습니다.** ... 이 부분은 현재 삼성전자 서비스 사이트에 들어가시면 **이미 실제 적용에 돼서 사용이 되고 있습니다**." [S3]
> (자막 오류 주의: "체포"은 chatbot의 오인식으로 보이나, 본 문서는 원문 그대로 인용한다.)

**(4) 외주 시장조사의 내재화 — 인간 응답자까지 기계로 치환**

> "저희가 한 것은 어 에이전트를 고객한테 저희가 인터뷰를 했는데 **인터뷰를 받는 사람들도 에이전트로 만들고 인터뷰를 하는 사람도 에이전트로 만들어서 에이전트와 에이전트 간의 대화**를 하면서 ... 현재는 이제 어 에이전시한테 외브 에이전시한테 어 인터뷰에 대한 시장 조사에 대한 부분을 **의뢰하지 않고** 이렇게 자체적으로 어 에이전트를 만들어서 어 진행을 하고 있습니다." [S3]

**(5) 우리은행 — 자동화 구간은 「사전 정의된 설계 산출물」로만 존재**

우리은행 사례에서 「어디가 자동화인가」는 개별 구간의 실행 사례가 아니라, 컨설팅 단계에서 미리 그어진 경계로 서술된다(4-5.5에서 재인용).

---

### 4-5.4 증강 구간 (AUG)

**(1) 우리은행 — 자동화/증강 경계의 사전 정의 (이 사례의 핵심 문장)**

> "as 모든 프로세스를 다 분석을 하고이 모든 프로세스가 아까 제가 잠깐 설명드렸던 **어디는 자동화되고 어디 에이전트가 들어와서 어떻게 휴먼 인더브로 사람 에이전트가 같이 코하면서 개선할지를 다 정의를 하셨고요.**" [S1]

- 자막 표기 주의: 파일의 실제 문자열은 **"휴먼 인더브로"** 이다(human-in-the-loop의 오인식). 과업 지시문의 「휴머 인더루프」와 다르므로, 인용 시 반드시 파일 원문 표기를 쓸 것.
- 이 문장은 S1에만 있다. S2·S3에는 자동화/증강 경계를 사전 정의했다는 서술이 **없음**.

**(2) 워크플로 설계 수준의 HITL — 사람의 판단이 다음 단계의 조건**

> "특정 프로세스는 에이전트가 이렇게 들어와야 되겠 업무 프로세스에서 어떤 부분은 에이전트가 일을 하고 **어떤 부분은 사람이 개입을 해서 사람이 판단을 한 결과를 바탕으로 그다음 프로세스가 흘러가는 형태도록 구성하는게** 이제 로코드 기반 또는 워크플로우 기반의 에이전트 빌더라고 하고요." [S1]

> "기업의 업무 프로세스를 그대로 준용해서 순서대로 진행해야 되는 부분들이 중요한 케이스에서는 워크플로우 형태로 에이전트를 구성을 하고" [S2]

**(3) 콜센터 — 상담원 보조형 증강(대체 불가 판정을 명시)**

> "어 24년에 진행했던 것은 **상담원을 대체는 어렵다. 당장 어렵고 상담원의 업무를 보조해 주는 AI 어시스턴트를 먼저 진행을 했습니다.**" [S3]
> "그 답변을 상담원한테 딱 팝업을 띄어 줍니다. 그러면 숙련된 엔진 숙련된 답 숙련된 어 상담원처럼 **초보 상담원도 빠르게** 그 부분들을 어 정확도 높은 답변할 수 있는 어 이제 그런 상담 추천 답변 추천도 제공해 주고 있고" [S3]
> "에이전트가 요약해서 시스템 미리 입력해 놓고 어 **상담원이 그거에 대한 내용만 컨펌하고** 바로 넘어갈 수 있게" [S3]

이 세 문장은 증강의 세 층위를 각각 보여준다 — (a) 신참의 역량 상향(숙련자 수준으로), (b) 실시간 제안, (c) 인간의 최종 컨펌.

**(4) VOC — 증강으로 읽히는 부분**

> "그러다 보니까 기존에는 5% 7%만 보던 다양한 VOC들을 에이전트가 전체 다 봐주니 **내가 볼 수 있었던 내가 하고 있는 업무들이 실질적으로 확장이 되는 것들을 관찰**할 수 있었습니다." [S1]

발화자는 이를 자동화가 아니라 **업무 확장**으로 프레이밍한다. 다만 확장된 뒤 인간이 구체적으로 무엇을 판단하는지(예: PLM 반영 여부의 승인권자)는 소스에 명시가 없음.

**(5) 기계가 인간에게 알려주는 형태의 증강**

> "또 한편으로는 기존에는 **내가 인지하지 못했던 업무 에이전트가인지를 해서 알려주는 경우**도 있습니다." [S1]

**(6) ChatGPT Enterprise 측 서술 (외부 벤더 발화)**

> "진짜 우리 직원들은 관리 업무 대신의 **의사 결정 그리고 창의성 또 고객 임팩트** 정말 사용자들 우리 고객의 고객을 만날 수 있는 시간에 집중할 수 있게 됩니다." [S4]

**(7) 제조 현장 — 하이브리드 기간의 명시 (증강을 과도기로 규정)**

> "기존에 우리가 현장의 전문가분들에 의해서 판단을 하고 의사 결정을 했다면 앞으로는 AI 에이전트에 의해서 될 건데 **그 중간에는 하이브리드하게 진행이 될 거라고 저는 생각을 합니다.**" [S5]
> "품질 검사, 품질 예측, 그다음에 정비 그리고 에너지 최적화, 그다음에 공정 최적화, 생산, 어, 그다음에 뭐 SCM 같은 이제 서플라이 체인 뭐 등등의 업무들이 ... **중간중간에는 전문가의 개입이 들어갑니다.**" [S5]

---

### 4-5.5 전환 메커니즘 (CYCLE)

**(A) 우리은행 — 시간축 전환이 아니라 "사전 설계"로 처리됨**

우리은행 사례에는 「증강으로 시작해 학습이 쌓이면 자동화로 넘긴다」는 시간축 기준이 **없다**. 대신 컨설팅 1년 동안 AS-IS 전 프로세스를 분석해 경계를 **미리 확정**한다: "어디는 자동화되고 어디 에이전트가 들어와서 어떻게 휴먼 인더브로 사람 에이전트가 같이 코하면서 개선할지를 **다 정의를 하셨고요**" [S1]. 즉 전환 기준이 시간이 아니라 **설계 단계의 판정**이다. 이후의 시간 축은 개발 물량의 분할 일정일 뿐이다: "올해 연말 내년 상반기까지 **두 차례로 끊어가면서** 에이전트를 개발하면서" [S1].

**(B) 콜센터 — 소스 전체에서 유일하게 명확한 CYCLE 근거 (연도별 로드맵)**

> "그래서 저희가 **23년부터 준비해서 24년에 이제 시스템을 오픈해 나가면서요 밑에 보시면 24, 25, 26, 27 이렇게 진행을 지금 로드맵들을 저희는 하고 있는데** 어 24년에 진행했던 것은 상담원을 대체는 어렵다. 당장 어렵고 상담원의 업무를 보조해 주는 AI 어시스턴트를 먼저 진행을 했습니다." [S3]

이어서 다음 단계가 순차적으로 서술된다.

> "작년에 저희가 좀 진행했던 부분들은 ... 이 부분을 에이전트 기반으로 대체를 진행을 했습니다." [S3]
> "그리고 현재 저희가 진행하고 있는 부분들은 어 채보뿐만이 아니라 전화가 왔을 때 어 보이스 보로 어 **사람이 아니라 실제로 에이전트로 제하는 작업들을 올해는 이제 시도**를 하고 있습니다." [S3]

→ 증강(24년 어시스턴트) → 텍스트 채널 자동화(작년, 챗봇 대체) → 음성 채널 자동화 시도(올해). 논문 p.196-197의 시간축 전환과 정확히 대응한다. 다만 전환의 **판정 기준**(정확도 몇 %에서 넘어갔는지 등)은 소스에 없음.

**(C) 성능 평가에 따른 에이전트 라이프사이클 — 자동화의 되돌림 장치**

> "이 에이전트가 당초에는 예를 들어서 정확도 한 95% 정도 수준이 돼서 사용을 하기 시작했는데 데이터가 계속 더 추가가 되고 시스템이 누리면서이 **에이전트 성능이 지속적으로 떨어지게 되면** 사용자가 결국 이탈을 하고 안 쓰게 되고 어 펌플레인이 커질 겁니다. ... 그렇게 기준을 가지고 **에이전트의 어 성능을 평가하는 것들을 바탕으로 에이전트의 라이프 사이클을 결정하는 일들도** 어 당연히 진행이 돼야 되고" [S1]

> "필요에 따라서는 아이 에이전트는 어 쓰면 안 되겠어. **토큰을 통제해 되겠어.**" [S1]

이는 조건 변화 시 자동화를 철회하는 장치이나, **증강으로 회귀시킨다는 서술은 없다**. 회귀 대상(사람에게 되돌아가는지, 폐기하는지)은 해당 소스에 없음.

**(D) 접근법 자체의 전환 (바텀업 → 탑다운)**

> "그래서 어 최근에 저희가 저희 고객사들은 바텀을 많이 하는 회사들은 대부분 이제 탑다운으로 많이 돌았었습니다. 그래서 바텀업으로 가고 있다가 탑다운 가는 것도 하나의 방법인 거 같고**이 반대 방향으로 가는 거 아 제가 목격은 하지 못했는데** 뭐 여러 가지 방향은 있 있을 것 같습니다." [S1]

발화자 스스로 「역방향은 목격하지 못했다」고 말한다 — 논문의 증강 회귀(reversal) 가능성에 대한 **부분적 반증 진술**로 다룰 수 있다.

---

### 4-5.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

### SPILL (공간축 파급)

**있음.** VOC 사례가 가장 명확하다. VOC 분류라는 한 과업의 자동화가 설계·제조·품질이라는 인접 과업의 인간 작업을 되살리는 구조로 서술된다.

> "그 VC를 다 분석을 해서 어 이거는 **제품 설계하는 단에 다시 반영을 해서 차세대 제품에 좀이 부분을 고려를 해야 되겠다. PLM에 반영하는 부분도 있을 거고** 또 한편으로는 이게 품질적으로 좀 이슈가 되겠는데 그러면 어 **설계단에서부터 제조 양산단에서 또 품질단에서 각각의 어떻게 피드백을 빨리 줘서 그거에 대한 대응 체계를 빨리 가져가기 위해서**이 부요시를 수집을 할 텐데" [S1]

- 단, 위 문장은 VOC 수집 체계 구축 당시의 **"당초의 목표"** 서술이다("원래 당초의 목표는 ... 였을 텐데" [S1]). 분류 에이전트 도입 **이후에 실제로** PLM 반영이 늘었다는 사후 확인 수치는 해당 소스에 없음. 인용 시 반드시 구분할 것.
- 파급의 결과로 확인된 것은 커버리지 확대와 "업무 확장"이라는 정성 진술뿐이다: "내가 볼 수 있었던 내가 하고 있는 업무들이 실질적으로 확장이 되는 것들을 관찰할 수 있었습니다." [S1]

**부서 간 벽 해체라는 형태의 파급 구상**

> "1 예로 ERP를 하시는 분들하고 또 SCM을 하시는 분들간에 데이터가 대부분 한 **80%가 중복**이 되거든요. ... 그러면 어 앞으로 AI 시대로 전환이 된다고 했을 때는 그러면 기존에 벽에 있었던 업무와 업무관, 부서와 부서관의 업무들도 어떻게 혁신할 것인가에 대한 부분들도 다시 원점에서 한번 짚어봐야" [S1]
> (이 80%는 발화자의 일반론이며 특정 고객사 측정치가 아님.)

**에이전트 간 파급 (제조 도메인)**

> "예를 들면 어딘가에서 품질 분량이 생겼어요. 그러면 그 분량 문제를 해결하기 위해서 누군가는 제조현장이 어디에 이슈가 있어 그걸 빨리 정비해라고 이제 명령을 내릴 겁니다. 그러면 **품질 AI 에이전트하고 정비 AI 에이전트가 서로 소통을 해야 돼요.**" [S5] — 단 이는 향후 정부 사업 방향에 대한 **구상**이지 실행 사례가 아니다.

### REINV (자원 재투자)

**부분적으로 있음. 다만 논문의 UBS 패턴(자동화로 확보한 자원을 증강에 재투자)과 정확히 일치하는 서술은 약하다.**

- **금액 절감 근거는 있으나 재투자 서술이 없는 경우:** 시장조사 외주비 "그게 작게는 **연간한 100억**에서 그 이상의 돈을 저희가 몇년 사용을 하고 있는데" → "현재는 이제 어 에이전시한테 외브 에이전시한테 어 인터뷰에 대한 시장 조사에 대한 부분을 의뢰하지 않고 이렇게 자체적으로 어 에이전트를 만들어서 어 진행을 하고 있습니다." [S3]. **절감된 100억이 어디에 재투자되었는지는 해당 소스에 없음.**
- **시간 재배치 서술 (벤더 자체 서술):** "진짜 우리 직원들은 관리 업무 대신의 의사 결정 그리고 창의성 또 고객 임팩트 ... 시간에 집중할 수 있게 됩니다." [S4]
- **인재/역량으로의 재투자:** AI 크루 107명 [S1][S2], 레벨 1~4 인증체계 [S1], 우수사례 포상 — "잘 선정이 된 분들한테는 좀 꽤 큰 좀 어 **상금 또 해외 연수기회** 이런 것들을 제공을 하고 있습니다." [S1] — 그리고 컨테스트 선정 부서에 대한 자원 배분: "탑 5분과 선정이 되면 그 부서한테는 실제로 어 그 일을 프로젝트와 수행할 수 있는 **지원과 GPU 필요한 학습 모델을 제공해 준 것까지 학습하는 것까지 리소스까지 제공**해 준 것까지" [S1].
  → 이는 자동화로 **확보한** 자원의 재투자라기보다, AX 추진을 위한 **선행 투자**다. UBS 패턴과는 방향이 다르다는 점을 명시해야 한다.
- **토큰 재배분:** "어 토큰 배분하는 부분들도 당연히 **중요한 업무에 좀 더 많이 쓰고 저가체 업무에는 적게 쓰는** 부분들도 있고요." [S1] / "당연히 중요한 업무에는 더 많은 토큰을 배정을 하고 또 어 토큰에 대한 회순에 대한 부분들도 거버넌스 측면에서 특정 부서가 특정 개인이 많이 쓰고 있다면 그런 부분들을 어 뭔가 분배하는 차원에서 전체 거버넌스 컨트롤하고 해야 될 부분이 있을 텐데요." [S2]
  → 기계 자원(토큰)의 재배분 메커니즘은 있으나, **인간 자원의 증강 재투자**로 연결되는 서술은 아니다.

---

### 4-5.7 통합 장치 (RESP)

우리은행 자체의 승인권/책임 구조에 관한 서술은 **세 소스 어디에도 없음**. RESP 근거는 전부 플랫폼(패브릭스) 거버넌스 층과 벤더 제품 기능 층에서 나온다.

**(1) 등록 게이트 — 사용 전 사전 검증**

> "저희는 보통 마켓플레이스를 저희는 제공하고 있습니다. 그래서이 마켓플레이스 안에서는 어 에이전트에 대해서 여기 이쪽에서 만들어진 에이전트들 그리고 밖에서 우리가 사용하기로 결정한 에이전트들도 **다 같이 등록하는 프로세스**를 거치게 됩니다." [S1]
> "이 보안 관점에서는 어 위험 그 보안 리스크를 관리하는 관점에서는이 등록하는 시점에서 실제로 도구들과 어 사용하는 에이전트들이 **어떤 문제가 있는지를 다 어 검증을 한 이후에 등록할 수 있게끔** 해 줘야 되고" [S1]

**(2) 권한 승계 — 인간의 권한이 기계의 상한**

> "이 에이전트의 성격상이 에이전트가 사용하는 데이터와 툴들에 있는 **권한들을 그대로 승계**해서 실제로이 에이전트는 그 데이터와 어 권한 데이터와 권한이 있는 시스템에 연결할 수 있는 거만 사용할 수 있는 사람들만 사용할 수 있는 어 사용자 인증 권한 이런 것들이 매우 중요하게 됩니다." [S1]
> "저는이 에이전트의 권한이 있어요. 근데 에이전트가 문서를 A B C 세 개 문서를 보는데 저는 C 문서에 대한 권한 없는 사람이에요. 그러면 내가이 에이전트한테 뭔가 일을 하려고 할 때이 **에이전트가 최종적인 답변을 C까지 주면 안 되잖아요.**" [S1]
> "원본 데이터의 권한이 에이전트가 해당 데이터를 사용을 할 때 에이전트의 권한과 원본 데이터의 권한이 실로 **위배되지 않도록** 권한 거리를 어 엔드투 엔드를 시니스게 연결해서 관리할 수 있는 체계" [S2]

**(3) 이탈 감지 — 약속 위반의 적발**

> "예를 들어서 특정 에이전트가 이러 이러 이러한 도구만 사용하기로 했는데 에이전트 기술이 발전하면서 자기도 자기가 없는 도구들을 생성해서 막 실행한다고 하면 어 너 지금이 에이전트 등록할 때 사용하 도구 외에 다른 도구까지 연결해서 쓰고 있네. **얘는 반칙이야. 이런 것들 잡아낼 수 있는 잣대가 있어야 된다**라는 말씀이고요." [S1]
> "MCP 가드는 에이전트가 측정 툴들을 MCP라는 걸 바탕으로 ... **그 동작 방식대로 동작하고 있는지를 판단하는 부분들**도 어 MCP 카드를 통해서 측정을 합니다." [S3]

**(4) 감사추적/미터링과 KPI 연동**

> "전체 사용량에 대한 토큰이 어떻게 되고 있는지를 매절을 할 수 있어서 내가이 하나의 업무를 하데 있어서 **얼마만큼의 돈이 어 정확하게 미터링되고 있는지**를 볼 수 있어야 되고 ... 그래서 그런 식으로 **KPI 연동된 어 사용량의 토큰량까지도 관리**할 필요가 있어는 것입니다." [S1]
> "에이전트를 등록하는 시점에서 어 필요한 정보들을 우리가 어 이미 이제 **로깅을 하고 기록을 하게 하기 시작하기 때문에**" [S2]

**(5) 규제 준수 (가드레일)**

> "미국하고 유럽 쪽은 이제 액트 이유 액트 같은 거 나오고 어 미국도 액트라고 하는 AI 액트 법들이 나오고 **한국도 최근에 AI 액트가 나왔습니다.** 그래서 이런 AI 관련된 어 정부 차원의 규제들이 정말 준수가 되는 형태대로이 에이전트가 만들어지고 사용되고 있는지에 대한 부분들도이 가들의 관점에서는 체크를 하고 어 점검을 할 수 있어야 됩니다." [S1]
> 리스크의 비대칭도 명시된다: "특히 어 산내 생산성을 위해서 쓰는 에이전트들은 좀 리스크하는 거 덜데 **사외 서비스들 특히 이제대 고객향으로 서비스를 만들어서 에이전트가 적극적으로 돌아갈 때는 반드시 이런 가드레이들에 대한 안전 장치가 있지 않으면 회사 차원에 큰 리스크**가 벌어질 수가 있게 되겠습니다." [S1]

**(6) 벤더 제품 층의 승인권 (OpenAI 발화 — 제3자 검증치 아님)**

> "**통제권은 항상 사용자와 또 저희 조직에 있다**라는 부분입니다. 에이전트는 허용된 도구와 데이터만을 쓸 수가 있습니다. 그래서 민감한 민감한 작업을 하시는 경우에는 **승인을 요청하도록 설정**하실 수도 있고요. 그래서 이메일 발송이나 뭐 스프레드시트를 수정한다거나 캘린더를 직접 뭐 일정을 추가하는 것처럼 **외부 영향이 있는 테스크들은 사람이 확인할 수 있고 개입할 수 있어야 합니다.**" [S4]
> "누가이 에이전트를 만들 수 있고 어떤 앱과 데이터에 접근할 수 있으며 또 **어떤 작업을 승인받아야 할지 또 실행 결과는 어떻게 추적**해야 할 수 있을지 모두 다 관리하실 수가 있습니다." [S4]
> "역할 기반 권한 설정인 **알백** 기능을 통해 팀, 조직, 사용자 단위로 기능과 데이터 접근 범위를 통제할 수 있습니다." [S4]
> "**컴플라스 API**라는 기능을 통해서 워크스페이스 내에 일어나는 모든 대화와 최치T 로고를 기록하실 수가 있습니다." [S4] (자막 오류: compliance API / logs로 추정되나 원문 표기 유지)

**(7) 구축 현황의 성숙도 (중요)**

> "그래서 저희는 어 **삼성전자하고 우리 은행의 이런 어 옵스 체계와 거 체계를 어 현재 구축을 해서 어 활용을 하고 있고 우리 같은 경우 이제 앞으로 좀 구축해 나갈 어 그런 계획을 갖고 있습니다.**" [S1]

이 문장은 문법이 흐트러져 있어 "우리 같은 경우"가 우리은행인지 삼성SDS 자사인지 **자막만으로는 확정 불가**하다. 인용 시 이 모호성을 반드시 병기해야 한다.

**(8) 정부/기업 차원의 데이터 거버넌스 (제조 도메인, 참고)**

> "정부 차원이 제조 데이터를 관장하는 곳에서 데이터 거버런스 체계를 좀 정부 차원에서 만들 필요가 있다고 봅니다. 예를 들면 데이터를 공유하는 기업한테는 인센티브를 주는 거죠." [S5]
> "데이터를 등급제로 구분을 하고 어떻게 관리할 관리 체계를 정의하고 그리고 데이터를 생성만 할게 아니라 **폐기하는 거에 대해서도 우리가 정의할 필요**가 있습니다." [S5]

---

### 4-5.8 성과 수치

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 삼성전자 VOC 유입량 | "일주일에 보통 한 30몇만 건씩" | (동일) | [S1] | 벤더(삼성SDS) 자체보고 |
| VOC 검토 커버리지 | "5% 7%만 보던" | "에이전트가 전체 다 봐주니" (수치 미제시) | [S1] | 벤더 자체보고, **정량 after 값 없음** |
| VOC 담당 인원 | "담당하는 인력 한 몇 명" | 해당 소스에 없음 | [S1] | 벤더 자체보고 |
| 삼성전자 가동 에이전트 수 | - | "천개 단위에서 이제 만 개 단위" | [S1] | 벤더 자체보고 |
| 삼성전자 가동 에이전트 수 | - | "작년에 이미 한 만여 넘겨는 에이전트" | [S3] | 벤더 자체보고 (**S1과 불일치**) |
| 우리은행 핵심업무 수 | - | "29개 핵심 업무" | [S1] | 벤더 자체보고, **계획치** |
| 우리은행 핵심업무 수 | - | "27개 핵심 업무" | [S2] | 벤더 자체보고, **계획치** (**S1과 불일치**) |
| 우리은행 에이전트 수 (컨설팅 설계치) | - | "175개 에이전트" | [S1][S2][S3] | 우리은행/컨설팅사 설계치를 벤더가 전달, **계획치** |
| 우리은행 에이전트 수 (SDS 재산정) | 175개 | "최소 300개 그 이상" | [S3] | 벤더 자체 추정, **계획치** |
| 우리은행 에이전트 수 (SDS 재산정) | 175개 이상 | "300여개 이상" | [S2] | 벤더 자체 추정, **계획치** |
| 우리은행 개발 일정 | - | "올해 5월부터" 착수, "올해 연말 내년 상반기까지 두 차례로 끊어가면서" | [S1] | 벤더 자체보고, **계획치** |
| 우리은행 개발 일정 | - | "올해부터", "내년 하반기까지" | [S2] | 벤더 자체보고, **계획치** (**S1과 불일치**) |
| 시장조사 외주비 | "작게는 연간한 100억에서 그 이상" | 외주 미의뢰(자체 에이전트) | [S3] | 벤더 자체보고 |
| 시장조사 에이전트 결과 일치율 | 외부 에이전시 인터뷰 결과 | "최소 80% 최대 95% 지금도 결과가 일치" | [S3] | 벤더 자체보고, **제3자 검증 아님** |
| Text-to-Analytics 벤치마크 | - | "글로벌 1등을 한번 찍어 봤던 저희 경험" | [S2] | Spider 2.0 = **외부 벤치마크(제3자 리더보드)**, 다만 순위·시점은 벤더 진술 |
| 삼성SDS AI 크루 | - | "107명" / "한 107명 정도" | [S1][S2] | 자사 보고 |
| 삼성SDS 인증체계 | - | "레벨 1부터 레벨 4까지 어소시아프터 어드벤스드 프로페셔널 엑스퍼트" | [S1] | 자사 보고 |
| 삼성SDS 자사 유즈케이스 | - | "16개 부서와 50개 이상의 유즈 케이스" | [S4] | 자사 보고 |
| ChatGPT Enterprise 리셀링 고객사 | - | "벌써 한 20여개 정도의 고객사들" | [S2] | 자사 보고 |
| 맥킨지 설문 표본 | - | "1884개의 기업들" / "1800여의 기업" | [S1] / [S2] | 제3자(맥킨지) 조사이나 **발화자 구두 인용, S1·S2 수치 표기 상이** |
| ChatGPT 이용자 | - | "9억 명 이상의 매주 사용", "하루 30억 건 이상의 메시지" | [S4] | **OpenAI 자체보고** |

**성과 수치에 관한 총평:** 이 사례군에서 before/after가 쌍으로 제시된 정량 지표는 사실상 **VOC 커버리지(5~7% → 전량, 단 after는 정성)** 와 **시장조사 외주비(연간 100억 → 미의뢰)** 둘뿐이다. 우리은행 사례에는 성과 수치가 하나도 없다 — 전부 착수 규모와 일정의 계획치다.

---

### 4-5.9 소스 간 교차 대조

S1·S2·S3는 동일 발화자(삼성SDS AX센터 신계영 부사장으로 표기)의 **같은 골격의 발표 3판**이다. 6대 축(프로세스 리디자인 / 에이전트 옵스·거버넌스 / AI 레디 데이터 / 조직·문화 등), 맥킨지 설문 슬라이드, KPI 3분류, 토큰=투자 등식, 우리은행 사례, AI 크루, 패브릭스 구조는 세 판본에 모두 등장한다. 그러나 **수치와 서술은 판본마다 어긋난다.**

### (가) 반복 확인된 사실 (2개 이상 소스에서 일치)

| 사실 | 소스 |
|---|---|
| 우리은행 은행장/대표 선언 → 1년 컨설팅 → 5대 핵심 업무 정의 | [S1][S2][S3] |
| 우리은행 컨설팅 설계치 = **175개 에이전트** | [S1][S2][S3] |
| SDS가 실제 필요 수를 **300개 이상**으로 재산정 | [S2][S3] |
| KPI 3계층 (테크니컬 → 프로세스/워크플로 → 비즈니스), 뒤로 갈수록 정량화 곤란 | [S1][S2][S3] |
| ROI의 투자측 = 토큰 비용으로 치환 | [S1][S2][S3] |
| 마켓플레이스 등록 → ADS/메타데이터 → 멀티에이전트 오케스트레이션 | [S1][S2][S3] |
| 에이전트 가드/MCP 가드, 권한·인증, 토큰 미터링 | [S1][S2][S3] |
| AI 크루 **107명** | [S1][S2] |
| AI 서밋 우수사례에 상금 + 해외 연수 | [S1][S2][S3] |
| 임원/경영진 합숙 교육 | [S2][S3] |
| 삼성SDS = AI 풀스택 국내 유일 포지셔닝 | [S1][S2][S3][S5] |
| ChatGPT Enterprise 국내 최초 리셀링 파트너 | [S2][S3][S4] |
| Spider 2.0 벤치마크 글로벌 1위 경험 | [S2][S3] |
| 바텀업은 리터러시↑ / ROI 산정 난, 탑다운은 ROI 산정 용이 | [S1][S2][S3] |
| AI 레디 데이터 4단계(우선순위 → 품질 → 형변환/임베딩 → 권한) | [S1][S2][S3] |
| 패브릭스/ChatGPT Enterprise가 현장에 열려 있다는 사실 | [S1][S2][S3][S5] |

### (나) 한 소스에만 있는 사실

| 사실 | 유일 소스 |
|---|---|
| **"어디는 자동화되고 어디 에이전트가 들어와서 어떻게 휴먼 인더브로 사람 에이전트가 같이 코하면서 개선할지를 다 정의"** (자동화/증강 경계의 사전 정의) | **[S1]** |
| 우리은행 **29개** 핵심 업무 | [S1] |
| 우리은행 **27개** 핵심 업무 | [S2] |
| 우리은행 **"올해 5월부터"** 착수, **"두 차례로 끊어가면서"** | [S1] |
| 우리은행 **"내년 하반기까지"** | [S2] |
| 삼성전자 VOC 사례 전체 (30몇만 건, 5% 7%, PLM 반영, 분류 에이전트) | **[S1]** |
| 삼성전자 에이전트 「천개 단위에서 만 개 단위」 | [S1] |
| 삼성전자 에이전트 "작년에 이미 한 만여 넘겨는" | [S3] |
| 레벨 1~4 인증명 ("어소시아프터 어드벤스드 프로페셔널 엑스퍼트") | [S1] |
| AI 해커톤/컨테스트 4차례, 탑 5 선정 부서에 GPU·모델 제공 | [S1] |
| "특정이 부서 없어지면 큰일 나. AI가 들어와서 한번 없애 보자" (과격한 탑다운 언어) | [S1] |
| 한국 AI 액트 언급, 가드레일 규제 준수 | [S1] |
| 바둑(신진서 9단, AI 일치율 37.6% vs 2위권 20%) 비유 | [S1] |
| 콜센터 로드맵 24/25/26/27 및 상담원 대체 곤란 판정 | **[S3]** |
| 삼성전자 서비스 사이트 "체포" → 에이전트 대체, 실적용 중 | [S3] |
| 시장조사 에이전트 (연간 100억, 80~95% 일치, 바텀업 산출) | **[S3]** |
| 임원 AI 리터러시 진단 결과 ("오프타 리코드를 말씀드립니다만") | [S3] |
| B300 GPU 도입 | [S3] |
| 우리은행 AI 레디 데이터 파이프라인 도식 언급 | [S3] |
| "김수현 전문님 별 발표해 주셨는데" (같은 행사 내 우리은행 측 발표 존재) | [S2] |
| 삼성 관계사 "6월까지 6월부터는 전면적으로 어 외브 AI들을 사용하기로 결정" | [S2] |
| ChatGPT Enterprise 고객사 "20여개" | [S2] |
| 워크스페이스 에이전트, 코덱스, 승인 요청 설정, 알백, 컴플라스 API | **[S4]** |
| 삼성SDS 16개 부서 50개 이상 유즈케이스 | [S4] |
| 하나토/섹터인 등 고객 사례 유형 서술 | [S4] |
| 제조 암묵지 휘발, 온톨로지, 카테나X/우라노X/KMX, "AX형 인간" | **[S5]** |
| "중간중간에는 전문가의 개입이 들어갑니다" / "그 중간에는 하이브리드하게" | **[S5]** |

### (다) 시점/판본에 따른 서술 변화

1. **우리은행 핵심 업무 수: 29개 [S1] vs 27개 [S2] vs 명시 없음 [S3].** 세 판본 중 둘이 서로 다른 숫자를 말한다. 어느 쪽이 맞는지 판정할 근거는 소스에 없음. (수집일 순서로는 S3(07-21) → S2(07-23) → S1(07-26)이나, **수집일은 발화 순서를 뜻하지 않는다.**)
2. **에이전트 수의 상향:** 세 판본 모두 "175개"를 컨설팅 설계치로 두되, S2·S3에서 "300여개 이상"/"최소 300개 그 이상"으로 상향한다. S3는 상향 주체와 근거를 가장 명확히 밝힌다 — "저희가 들어가서 이제 판단을 해 보니까 175개가 아니라 최소 300개 그 이상의 에이전트들이 ... 돌아가야지만이 프로젝트가 성공하겠다라고 생각을 하고 있고" [S3]. **S1은 175개에 머문다.** 즉 S1이 더 이른 시점의 서술일 가능성이 있으나, 소스만으로는 확정 불가.
3. **완료 목표 시점: "올해 연말 내년 상반기까지" [S1] vs "내년 하반기까지" [S2].** 최소 한 분기 이상 어긋난다. 발화 시점이 달라 기준연도가 다를 가능성도 배제할 수 없으나, 두 소스 모두 절대 연도를 말하지 않아 **환산 불가**.
4. **선언 주체 호칭: "은행장께서" [S1] vs "대표님께서" [S2] vs 주체 미명시 [S3].** 동일 인물의 다른 호칭일 개연성이 높으나, 소스만으로는 동일인 확정 불가.
5. **삼성전자 에이전트 규모: 「천개 단위에서 만 개 단위」(현재형) [S1] vs "작년에 이미 한 만여 넘겨는"(작년 기준) [S3].** S3가 더 큰 수를, 더 이른 기준시점에 귀속시킨다 — 두 진술은 정합적으로 읽기 어렵다.
6. **Spider 2.0 1위 시점: "25년 1월 11월 달에" [S2] vs "작년에" / "작년 말 기준으로" [S3].** S2의 "25년 1월 11월 달에"는 자막이 깨진 표현이며 그대로는 해독 불가.
7. **맥킨지 표본: "1884개의 기업들" [S1] vs "1800여의 기업" [S2].** S1이 더 정밀하고 S2가 반올림한 형태.
8. **자사 조직 서술의 초점 이동:** S1은 AX센터 출범 시점("작년 12월")과 인증 레벨명을 말하고, S2는 CAIO 선임을, S3은 임원 리터러시 진단 결과를 강조한다. 청중(자사 행사 vs 외부 컨퍼런스)에 따라 노출 정보가 달라진다 — **S3이 "오프타 리코드를 말씀드립니다만"이라며 진단 결과를 외부 행사에서 밝힌 점이 특히 눈에 띈다.**
9. **탑다운/바텀업 권고의 방향:** S1·S2·S3(신계영)은 탑다운을 ROI 관점에서 우위로 놓거나 하이브리드를 답으로 제시하는 반면, **S5의 삼성SDS 컨설팅팀 김지현 프로는 정반대로 바텀업을 강조**한다 — "이렇게 탑다운 방식으로 뭐 AI 이런 거 써 이게 아니라 정말 바텀업 방식으로 그 현장의 어 인직원들이 겪고 있는 그런 고충 고층에서 출발을 해야 된다. 그걸 다시 한번 강조드리고 싶습니다." [S5]. 같은 회사 안에서 접근법 권고가 갈린다.

### (라) 모순

- **29개 [S1] ↔ 27개 [S2]** — 직접 모순.
- **"올해 연말 내년 상반기까지" [S1] ↔ "내년 하반기까지" [S2]** — 직접 모순(동일 기준연도 가정 시).
- **「천개 단위에서 만 개 단위」 [S1] ↔ "작년에 이미 한 만여 넘겨는" [S3]** — 사실상 모순.
- **탑다운 우선 [S1][S2][S3] ↔ 바텀업 우선 [S5]** — 같은 조직 내 권고 충돌. 단 도메인(금융 전사 vs 제조 현장)이 달라 조건부 모순으로 읽을 여지가 있다.
- **역방향 전환 관찰 부재 [S1: "이 반대 방향으로 가는 거 아 제가 목격은 하지 못했는데"] ↔ 시장조사 사례가 바텀업 산출물임 [S3: "이거는 바텀범 어프로치로 나온 임증원이 만든 에이전트인데"]** — 직접 모순은 아니나, 바텀업이 유의미한 성과를 내는 경로가 실재함을 S3가 스스로 입증한다.

---

### 4-5.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간 루프 제외 (p.194) | VOC 분류 전량 이관 [S1]; "체포"→에이전트 전면 대체, 실적용 [S3]; 시장조사 외주 미의뢰 [S3]; "이 업무 프로세스 한번 전체를 사람 한번 빼 볼까?" [S1] | **지지** |
| AUG: 인간이 루프에 남아 밀착 협업 (p.194) | 상담원 답변 추천 + "상담원이 그거에 대한 내용만 컨펌" [S3]; "사람이 판단을 한 결과를 바탕으로 그다음 프로세스가 흘러가는 형태" [S1]; "중간중간에는 전문가의 개입이 들어갑니다" [S5] | **지지** |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | 콜센터 23년 준비 → 24년 어시스턴트(대체 불가 판정) → 작년 챗봇 대체 → 올해 보이스봇 시도 [S3] | **지지** (단 전환 판정기준은 소스에 없음) |
| CYCLE: 조건 변화 시 증강 회귀 | 성능 저하 시 라이프사이클 재결정·토큰 통제 [S1]. 그러나 「인간으로 되돌린다」는 서술 없음. 발화자는 "이 반대 방향으로 가는 거 아 제가 목격은 하지 못했는데"라고 명시 [S1] | **부분 반증 / 미확인** |
| SPILL: 한 과업 자동화가 인접 과업의 증강 유발 (p.197) | VOC 분류 자동화 → 설계·제조·양산·품질단 피드백 및 PLM 반영 [S1]; "내가 하고 있는 업무들이 실질적으로 확장" [S1]; 품질↔정비 에이전트 소통 구상 [S5] | **지지(정성)** — 인접 과업의 사후 정량 근거는 없음 |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS) | 시장조사 외주비 "연간한 100억" 절감 [S3] — 그러나 재투자처 서술 없음. AI 크루 107명·레벨1~4 인증·GPU 지원 [S1][S2]은 절감분이 아닌 **선행 투자** | **미확인 / 부분 확장** |
| RESP: 인간이 프로세스 전체 책임·승인·감사 보유 (p.200) | 등록 게이트·권한 승계·에이전트/MCP 가드·토큰 미터링·AI 액트 준수 [S1][S2][S3]; "통제권은 항상 사용자와 또 저희 조직에 있다", 민감 작업 승인 요청, 알백, 컴플라스 API [S4] | **지지 + 확장**(개인 책임이 아니라 **플랫폼 계층의 제도화**로 구현) |
| p.195: 증강 학습은 도메인 전문가의 암묵지에 의존, IT부서/외부업체에 위임 불가 | S5가 정면 대응: "그분들이 지난 2, 30년 동안 싸워온 안묵적인 지식들이 꽤 많이 있거든요 ... 그런 것들이 그분들의 은퇴와 더불어서 휘발돼 버립니다" [S5]; "많은 경우에 인터뷰 형식으로 해서 끌어내는 작업이 필요하고 ... 온톨로지와 같은 기술을 가지고 ... 끄집어내는 작업이 필요합니다" [S5]. 그러나 우리은행은 **정확히 반대로 외부 컨설팅사에 1년간 프로세스 정의를 위임** [S2][S3] | **긴장/반증 소지 + 확장** |
| p.198 기계 한계 ① 목적·자아 부재 | "AI가 되게 안목지 같은 거죠. 블랙박스예요. 답이 뭔지 몰라. 사람이 이해 못 해요. 하지만 이렇게 두면 확률이 높아져." [S1] | **지지** |
| p.198 기계 한계 ② 제약 완화된 옵션만 제시 | 텍스트투SQL이 초벌 쿼리를 생성하고 실행·판단·리파인하는 구조 [S2][S3] — 후보 제시 후 인간/에이전트 검증 | **부분 지지** |
| p.198 기계 한계 ③ 훈련된 과업에 국한 | "전통적인 체포은 ... 시나리오 밖에 있는 질문을 했을 때는 잘 답변을 못 하고" [S3]; "제조 현장의 이질성 올라오는 데이터가 다 같지 않고 불확실합니다 ... 이질적이고 불확실한 상황을 학습하는 거는 더더욱다나 어렵습니다" [S5] | **지지** |
| p.198 기계 한계 ④ 감각·감정·사회기술 부재 | 현장 반감이 인간 사회기술의 문제로 반복 등장 — "AI 뭔가 기능을 만들어서 너네 이제 써 써 봐 이렇게 했는데 이게 실질적으로 도움이 안 되는 거예요" [S5] | **간접 지지** |
| p.199 한쪽 편중 시 악순환 | 바텀업 편중 → "너 투자했을 때 얼마나 RI 났어에 대한 얘기는 사실 하기 좀 어려운 좀 부분" [S1]. 탑다운 편중 → 현장 반감 [S5]. 양쪽 결론은 하이브리드 — "결론적으로 당연히 둘 다 해야 됩니다" [S1] | **지지** |
| p.204 기계는 조직 내 새로운 행위자 계급 | "사람은 HR 부서에서 어 각각의 사람의 어 영량도 평가를 하고 ... 에이전트도 결국 사람하고 똑같다고 본다면이 에이전트를 거버넌스하고 통제하는 일들도 당연히 필요한 업무입니다" [S3]; "에이전트와 진짜 우리 팀원들이 함께 일하는 형태", "AI 동료와도 같은데요" [S4]; "AI 직원들처럼 활용하면서" [S1] | **강한 지지 + 확장** — 기계에 대한 **HR 유비**(등록=채용, 명세서=직무기술서, 성능평가=고과, 라이프사이클=재배치·퇴출)가 실무 어휘로 자리 잡음 |

**이 사례가 논문을 확장하는 지점.**

첫째, 논문은 자동화-증강의 경계를 시간에 따라 **발견되는** 것으로 그리지만, 우리은행 사례에서 그 경계는 착수 전 1년의 컨설팅으로 **선언되고 고정된다** — "어디는 자동화되고 어디 에이전트가 들어와서 어떻게 휴먼 인더브로 사람 에이전트가 같이 코하면서 개선할지를 다 정의를 하셨고요" [S1]. 즉 CYCLE의 전환점이 조직의 학습 곡선이 아니라 **설계 문서의 한 칸**이 되며, 이는 논문이 다루지 않은 「경계의 사전 계약화」라는 변형이다. 그리고 이 사전 계약이 곧바로 무너진다는 점이 흥미롭다 — 시공사가 들어가 보니 "175개가 아니라 최소 300개 그 이상"이 필요했다 [S3]. 설계된 경계는 구현 단계에서 재협상된다.

둘째, RESP가 **개인의 책임에서 플랫폼의 기능으로 이전**되어 있다. 논문은 인간이 프로세스 전체의 책임·승인·감사를 보유해야 통합이 성립한다고 보지만, 이 사례군에서 그 기능은 특정 인간이 아니라 마켓플레이스 등록 게이트, 권한 승계 규칙, 에이전트/MCP 가드, 토큰 미터링이라는 **시스템 층**이 수행한다. 책임의 소재는 유지되되 그 **행사 방식이 코드화**된 셈이며, 이는 통합 조건을 확장하는 동시에 새로운 취약점(가드가 놓치면 책임의 공백)을 만든다.

셋째, p.195의 「암묵지는 위임 불가」 명제에 대해 이 사례군은 **양방향의 증거**를 동시에 제공한다. S5는 명제를 강하게 지지하며 암묵지의 휘발을 국가적 손실로까지 규정하지만, 우리은행은 전 프로세스 재설계를 외부 컨설팅사에 1년 위임했고 그 산출물이 175개라는 숫자로 표현됐다 [S2][S3]. 위임된 설계가 300개 이상으로 수정되어야 했다는 사실 자체가, 위임 불가한 암묵지가 어디에 남아 있었는지를 사후적으로 드러내는 자연 실험에 가깝다.

넷째, p.204의 「새로운 행위자 계급」이 조직 실무에서 **HR 제도의 문법 그대로 복제**되고 있다는 점이다 — 채용(등록)·직무기술(명세서)·권한 부여(승계)·근태 감시(가드)·고과(성능 평가)·퇴출(라이프사이클 결정). 논문의 은유가 이 사례에서는 은유가 아니라 운영 매뉴얼이 되어 있다.

---

### 4-5.11 인용 시 주의사항

1. **모두 벤더 자체보고다.** 우리은행·삼성전자 사례는 전부 **공급사(삼성SDS)의 발화**이며 고객사 확인이나 제3자 검증이 붙어 있지 않다. 유일하게 제3자 성격을 띠는 것은 Spider 2.0 벤치마크 순위지만, 순위와 시점 역시 벤더 구두 진술로만 존재한다 [S2][S3]. S4의 이용자 수치(9억 명, 하루 30억 건)는 **OpenAI 자체보고**다.
2. **우리은행은 계획이지 실적이 아니다.** 세 소스의 모든 동사가 미래형이다 — "만들겠다라고 디자인을 하셨고" [S2], "만들어 나가고요 ... 내년 하반기까지 진행을 해 나가면서" [S2], "돌아가야지만이 프로젝트가 성공하겠다라고 생각을 하고 있고 이제 과제료 이제 진행을 하고 있는" [S3], "AX를 추진을 하게로 되어 있습니다" [S1]. **175개도 300개도 구축 완료 수치가 아니다.** 성과 수치는 하나도 제시되지 않았다.
3. **「착수 몇 개월차」는 확정 불가.** S1만이 "올해 5월부터는 저희 SS와 함께"라고 착수 시점을 밝히며, 발화 시점 자체가 소스에 없다. S1 후반의 "올해 하반기에는 매우매우 중요한 일들이 될 것입니다"라는 표현은 발화가 하반기 이전이거나 초입임을 시사할 뿐, 개월 수 산정 근거가 되지 못한다. **「착수 N개월차」라는 표현은 쓰지 말 것.** 최대한으로 말할 수 있는 것은 「S1 기준 착수 선언이 '올해 5월'이고, 발화는 그 이후」까지다.
4. **수집일 ≠ 업로드일 ≠ 발화일.** 세 층위가 모두 다르며 이 사례군에서는 뒤의 두 개가 불명이다. S1(07-26 수집)이 S3(07-21 수집)보다 나중에 수집되었다는 사실은 **발표 순서에 대해 아무것도 말해주지 않는다.** 오히려 175개에 머무는 S1이 300개로 상향한 S2·S3보다 이른 발화일 가능성이 있으나 확증 불가.
5. **자막 오류가 많다. 인용은 반드시 파일 원문 그대로.** 특히 주의할 표기: **"휴먼 인더브로"**(human-in-the-loop, [S1] — 흔히 인용되는 「휴먼 인 더 루프」가 아님), **"체포"**(chatbot, [S3]), **"안묵지"/"암목지"/"안목지"**(암묵지의 세 가지 변형이 [S5]와 [S1]에 혼재), **"진흥형 파트너"**(proactive의 오인식으로 추정, [S4]), **"알백"**(RBAC, [S4]), **"컴플라스 API"**([S4]), **"바텀범 어프로치"**([S3]), **"VUC"/"VC"/"부요시"**(VOC의 변형, [S1]), **"엔듀텐드"/"엔더텐드"/"엔드투 엔드"**(end-to-end 변형), **"어소시아프터 어드벤스드 프로페셔널 엑스퍼트"**([S1]), **「디오이트」·「Netswuite」·「진흥화」는 이 다섯 소스에 존재하지 않는다**(다른 사례의 표기이므로 이 절에서 인용 금지).
6. **해독 불가 구간을 근거로 쓰지 말 것.** 대표적으로 S2의 "저희가 25년 1월 11월 달에 방금 설명드린 그 로직으로 그 당시 글로벌 1등을 한번 찍어 봤던" — 연월이 두 개 겹쳐 있어 시점 확정 불가. S1의 "저희는 어 삼성전자하고 우리 은행의 이런 어 옵스 체계와 거 체계를 어 현재 구축을 해서 어 활용을 하고 있고 우리 같은 경우 이제 앞으로 좀 구축해 나갈" — "우리 같은 경우"의 지시 대상(우리은행 vs 삼성SDS 자사)이 미확정. S1의 "내가 1,억 투자해서 10억 효과를 보면 굳이 할 이유가 없겠죠" — 논리가 뒤집힌 것으로 보이나 원문 그대로일 뿐 정정 근거 없음.
7. **귀속 주의.** (a) S3의 채널은 **IT조선**이며 삼성SDS 채널이 아니다 — 발화자는 삼성SDS 소속이나 게시 주체가 다르므로 「삼성SDS 공식 자료」로 귀속하면 오류다. (b) S5는 삼성SDS 단독이 아니라 "삼성SDS and KASMO 인공지능혁신추진단" 공동 채널이며, 발화자 4인 중 2인만 삼성SDS다. **암묵지·온톨로지·데이터 주권 발언은 서울대 윤병동 교수와 안광현 단장의 것이지 삼성SDS의 입장이 아니다.** (c) S4의 워크스페이스 에이전트·통제권·승인 관련 발언은 **OpenAI 한지은 디렉터**의 것이며 삼성SDS 발화가 아니다. (d) 발화자명 "신계영 부사장"은 S2·S3의 **영상 제목**에서만 확인되며 본문 발화 중 자기소개는 없다.
8. **성숙도 구분.** 실제 운영 중임이 명시된 것: 삼성전자 서비스 사이트 챗봇 대체("이미 실제 적용에 돼서 사용이 되고 있습니다" [S3]), 시장조사 에이전트("현재는 ... 자체적으로 어 에이전트를 만들어서 어 진행을 하고 있습니다" [S3]), VOC 분류 에이전트(관찰 완료형 [S1]), 콜센터 어시스턴트(24년 오픈 [S3]). 시도/계획 단계: 보이스봇("올해는 이제 시도를 하고 있습니다" [S3]), 우리은행 전체. **이 둘을 섞어 쓰면 안 된다.**
9. **VOC의 "전량"에는 정량 after 값이 없다.** "에이전트가 전체 다 봐주니" [S1]는 커버리지 100% 달성의 검증 진술이 아니라 관찰 서술이다. 분류 정확도 수치도 없다("성능이 꽤 높은 확률로"라는 표현뿐).
10. **삼성전자 에이전트 수는 두 소스가 다르므로 단독 인용 금지.** 반드시 「[S1]은 천~만 개 단위, [S3]은 작년 기준 만여 개 초과로 서술한다」처럼 병기할 것.
11. **S5는 이 사례의 1차 근거가 아니다.** 우리은행·삼성전자 VOC에 대한 언급이 **전무**하다. S5는 논문 p.195(암묵지)·p.198(기계 한계)·p.199(악순환) 대조용 보강 소스로만 쓰고, 사례 4-5의 사실 주장 근거로 쓰지 말 것.


---



## 사례 6 — TK Elevator × Databricks : 보고 자동화 → 현장 기술자 증강

*원문: `docs/cases/05_tkelevator.md`*


### 6.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 (구분) | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Databricks | **업로드일 2026-06-23** (채널 수집분, 파일 헤더 "업로드일" 필드) | ko (기계번역 자막) | 약 1995개 | 벤더(Databricks) 제작 고객 사례 인터뷰 영상. 진행자(Databricks 측 인터뷰어) + TK Elevator 최고 디지털 책임자 "마티아스 골"(Matthias) + 디지털 데이터·AI 재단 리드 "크리스티안"(Christian) 2인 순차 인터뷰. 발화 중 "바로 이곳 하노버 박람회에서"라는 표현이 있어 촬영 장소가 하노버 박람회장으로 시사됨 | https://www.youtube.com/watch?v=fHVV_09zIr4 | /home/user/youtube-scrap/transcripts/channels/Databricks/AI-Ready_Data_on_Databricks_How_TK_Elevator_Uses_Context_and__fHVV_09zIr4.md |
| [S2] | Databricks | **업로드일 2026-01-27** (채널 수집분) | ko (기계번역 자막) | 약 265개 | 벤더 제작 고객 사례 단편. UK Power Networks 데이터 팀 책임자 1인 단독 발화 | https://www.youtube.com/watch?v=iZVfuco1L7U | /home/user/youtube-scrap/transcripts/channels/Databricks/UK_Power_Networks_Manages_Smarter_Grids_with_Databricks_and___iZVfuco1L7U.md |
| [S3] | Databricks | **업로드일 2026-03-20** (채널 수집분) | ko (기계번역 자막) | 약 274개 | 벤더 제작 산업별 마케팅 영상(내레이션). 특정 고객사 지목 없음, Databricks 1인칭 내레이션 | https://www.youtube.com/watch?v=Hbn5H0rFOmE | /home/user/youtube-scrap/transcripts/channels/Databricks/AI_Agents_for_Manufacturing__Hbn5H0rFOmE.md |

각 소스의 역할:
- **[S1] 1차 근거.** 이 사례의 사실관계 전부(규모, 10년 축적 경로, AUTO/AUG 구간, 거버넌스 서술)가 이 한 건에서 나온다. 코퍼스 내 TK Elevator 관련 소스는 이것뿐이다.
- **[S2] 대조군.** 지정된 검색어("서비스 기술자", "현장 기술자", "field technician", "예지 정비", "predictive maintenance")로 transcripts/channels/Databricks/ 를 Grep한 결과 **정확히 [S1] 한 건만** 일치했다. 검색어를 "기술자|정비|유지보수|현장 서비스|technician|maintenance"로 완화했을 때 나온 8건 중, 물리적 설비 자산을 보유한 실명 고객 사례는 [S2]가 유일하다. TK Elevator와 동일하게 Unity Catalog 거버넌스를 도입한 인프라 운영기업이지만 **현장 인력 증강 서사가 전혀 없는** 사례로서 대조군 역할을 한다.
- **[S3] 대조군.** 완화 검색에서 나온 제조업 예지정비/에이전트 영상. 실명 고객이 없는 **벤더 자체 마케팅 집계치**의 예시로서, [S1]의 서술형·무수치 화법과 대비시키기 위해 사용한다. 고객 인터뷰가 아니므로 조직 사례로는 취급하지 않는다.

> **검색 결과 명시:** 지정 검색어 5개로는 추가 소스가 **없었다**. [S2][S3]는 완화 검색으로 확보한 구조적 대조군이며, TK Elevator에 관한 정보는 일절 포함하지 않는다.

---

### 6.2 조직과 문제 상황

TK Elevator는 [S1]에서 "세계 최대 규모의 모빌리티 기업 중 하나"로 소개된다 [S1].

규모 수치 (모두 [S1], 모두 **회사 임원 자체 진술**):

- 직원: "우리 회사에는 5만 명의 직원이 있습니다." [S1]
- 서비스 기술자: "저희는 25,000명의 서비스 기술자를 보유하고 있으며, 데이터와 AI를 활용하여 이들을 지원합니다." [S1]
- 관리 설비: "저희는 전 세계적으로 140만 대의 엘리베이터와 에스컬레이터를 관리하고 있습니다." [S1]
- 일일 수송 인원: "일반적으로 저희 회사는 말씀하신 대로 매일 15억 명의 사람들을 수송하고 있습니다." [S1]
- 시스템 파편화: "우리는 인수 합병을 통해 크게 성장했고, 그 결과 50개국 이상에서 100개 이상의 시스템을 보유하게 되었습니다" [S1]. 크리스티안도 동일하게 "기업 세계는 인수 합병을 통해 크게 성장하면서 50개국 이상에 100개가 넘는 시스템을 보유하게 되었고 , 그 시스템들이 모두 동일한 것은 아니었습니다."라고 반복한다 [S1].
- IoT 이벤트: 진행자가 "5억 개의 이벤트에 대해 좀 더 자세히 설명해 주시겠어요 ?"라고 묻고, 마티아스가 "5억 개의 데이터는 컨트롤러를 MAX 박스에 연결하여 클라우드로 전송하기 때문에 전 세계에서 수집됩니다."라고 답한다 [S1]. **주기(일/월/연) 단위가 자막에 명시되지 않는다** — "5억 건"이 무엇당 5억인지 [S1]에 없음.

before 상태 — 데이터 측면:
- "이전에는 수작업으로 처리하는 경우가 많았고, 집계된 데이터 수준에서는 수치에 대한 의문이 제기되기도 했습니다. 같은 질문에 대해 여러 개의 수치가 존재하기도 했죠" [S1]
- 진행자의 재확인: "같은 KPI라도 부서마다 수치가 조금씩 다를 수 있잖아요." → 크리스티안 "맞아요. \"어제는 똑같은 KPI 수치가 다른 걸 봤어요 .\"라는 질문을 받기도 하죠." [S1]

before 상태 — 현장 인력 측면:
- "저희는 항상 기술자들이 업무에는 매우 능숙 하지만 작업 자체에는 집중하지 못하고 사후 기록에는 소홀하다는 문제에 직면해 있었습니다." [S1]
- 지식이 조직화되지 않은 상태: "이는 기존에 서비스 기술자들이 가지고 있던 개별적인 지식이 아니라 시스템적인 지식에 더 가깝습니다" [S1] (사후 상태를 서술하면서 before를 함의)
- 비정형 정보 부재: RAG 대상이 "엔지니어링 매뉴얼이나 현장 서비스 관리 및 ERP 시스템에 없었던 계약 정보 등"이었다고 서술된다 [S1].

문제의 성격 규정:
- "그러므로 우리가 하는 일은 임무 수행에 매우 중요합니다. 또한 해당 서비스는 임무 수행에 매우 중요합니다." [S1]
- "가동 시간 확보가 궁극적인 목표입니다." [S1]

**10년 축적 경로의 시점 추출** (모두 [S1]):

| 단계 | [S1] 원문 근거 | 시점 |
|---|---|---|
| MAX Box (IoT 연결 장치) 최초 공개 | "정확히 10년 전, 바로 이곳 하노버 박람회에서 저희는 MAX Box를 처음으로 선보였습니다. 이것이 바로 엘리베이터를 클라우드에 연결하는 저희의 첫 번째 연결 장치입니다 ." | **"정확히 10년 전"** — 절대연도는 [S1]에 없음. 영상 업로드일 2026-06-23에서 역산하면 2016년경이나, 이는 소스에 없는 추론이므로 확정 불가 |
| 도메인 전문지식 결합 | "저희는 클라우드에 연결된 MAX Box로 시작했습니다. 우리는 거기에 우리 분야의 전문 지식을 더했습니다." | 순서만 명시, 연도 없음 |
| 머신러닝 | "우리는 거기에 머신러닝을 추가했습니다." | 순서만 명시, 연도 없음 |
| 디지털 운영 센터 | "우리는 거기에 디지털 운영 센터를 추가했습니다." | 순서만 명시, 연도 없음 |
| 예측·예방 정비 | "이 모든 것이 예측 및 예방 정비에 도움이 되었습니다" | 순서만 명시, 연도 없음 |
| Databricks 도입 | 진행자: "그의 팀은 2018년부터 Databricks를 사용해 왔습니다." / 크리스티안: "저희는 IoT 사업을 10년 전부터 시작했고, 2019년부터는 Databricks를 활용해 왔습니다." | **2018 vs 2019 — 같은 영상 안에서 불일치** (6.9 참조) |
| CDP Nexus / Unity Catalog | "Databricks의 Unity Catalog 기반 기능을 활용하여 CDP Nexus 프로젝트에서 공통 언어를 구축하고 이를 IoT 데이터와 연결할 수 있었습니다." | 연도 없음. Unity Catalog 도입은 Databricks 도입(2018/2019) 이후 |
| 보고 자동화 | "우선, 처음부터 보고 자동화를 진행했습니다." | "처음부터" = Unity Catalog 기반 위의 **첫 활용**. 연도 없음 |
| Genie | "방금 Genie를 언급하셨는데, 활용하고 계신가요? 검토 중입니다." / "Genie를 데이터 레이크 위에 구축하여 보고서에 표시되는 데이터를 음성으로 검색하거나 질문을 입력하여 KPI에 대한 답변을 얻을 수 있도록 했습니다." | **"검토 중입니다"** — 운영 배포가 아니라 탐색 단계로 자기 규정 (6.11 참조) |
| RAG 에이전트 | "비정형 데이터, PDF 문서를 기술자가 쉽게 검색할 수 있는 형태로 변환하는 검색 증강 생성 에이전트를 구축하여" | "구축하여"는 완료형이나, 배포 범위/시점 [S1]에 없음 |
| 음성 디브리핑 | "기술자에게 실제로 어떤 작업을 했는지 묻는 음성 에이전트가 있습니다" | "있습니다" — 존재는 단언. 배포 범위/시점 [S1]에 없음 |

즉 [S1]이 제공하는 **절대 시점은 "10년 전"(MAX Box)과 "2018년/2019년"(Databricks) 두 개뿐**이며, 나머지 8개 단계는 순서만 있고 연도가 없다.

---

### 6.3 자동화 구간 (AUTO)

[S1]에서 기계에 명시적으로 인계된 과업은 **보고서 생성**과 **비정형 문서 검색**, 그리고 **이벤트 스크리닝** 세 갈래다.

**(1) 보고 자동화 — 이 사례에서 가장 명확한 AUTO**

> "우선, 처음부터 보고 자동화를 진행했습니다. 저희 CFO와 현장 운영 담당자 모두 만족했습니다" [S1]

수작업 집계가 소스였다는 점이 before로 대응된다: "이전에는 수작업으로 처리하는 경우가 많았고" [S1]. 사람이 수치를 맞추는 루프가 제거된 지점이다.

**(2) 대량 이벤트의 사전 스크리닝**

> "우리는 문이 열리고 닫히는 것을 볼 뿐만 아니라, 모든 오류 코드, 모든 고장 코드도 확인하고 분석합니다" [S1]
> "그리고 우리는 어떤 일이 발생하기 전에 수천, 수십만 건의 사건들을 분석합니다." [S1]
> "이를 분석해 보면, 엘리베이터가 고장 나기 전인 향후 몇 주 안에 점검이 필요할 수 있음을 알 수 있습니다" [S1]

수십만 건 규모의 이벤트 판독은 인간이 수행하지 않는다. 다만 [S1]은 이 분석의 주체를 "우리"로 뭉뚱그려 서술하며, 어느 부분이 모델이고 어느 부분이 디지털 운영 센터 인력인지 **구분하지 않는다** — 6.4에서 보듯 티켓 생성 단계에는 사람이 명시적으로 들어간다.

**(3) 비정형 문서 -> 검색 가능 형태 변환**

> "즉, 비정형 데이터, PDF 문서를 기술자가 쉽게 검색할 수 있는 형태로 변환하는 검색 증강 생성 에이전트를 구축하여 기술자가 필요로 하는 시점에 필요한 정보를 제공하는 것입니다." [S1]

**(4) 사후 기록 작성**

> "기술자에게 실제로 어떤 작업을 했는지 묻는 음성 에이전트가 있습니다 . 그러면 해당 정보는 데이터 플랫폼에 입력되고 다음 서비스 기술자에게도 제공될 수 있습니다" [S1]

기술자가 직접 폼을 채우는 문서화 노동이 기계로 넘어간다. 단, 내용의 원천은 여전히 인간의 구술이므로 순수 AUTO가 아니라 AUTO/AUG 경계 사례다(6.4 재수록).

**AUTO 구간에서 배제된 것:** [S1]은 정비 실행, 티켓 승인, 현장 판단이 자동화되었다는 진술을 **하지 않는다**. 인력 감축·대체에 관한 언급도 [S1]에 **없다**.

---

### 6.4 증강 구간 (AUG)

이 사례의 핵심은 자동화가 기술자 방문의 **앞단과 뒷단 양쪽에서 증강을 만든다**는 구조다.

**(A) 앞단 증강 — 티켓이 기술자의 언어로 번역된다**

디지털 운영 센터의 성격 자체가 증강 장치로 규정된다:

> "우리 디지털 운영 센터는 모든 기술자의 든든한 지원군이자 AI 기반 전문가 허브 역할을 하고 있어요." [S1]

뉴욕 25층 일화 — 기계가 기술자를 대체하는 것이 아니라 **어디로 갈지 알려준다**:

> "데이터에서 패턴을 파악할 수 있죠. 그리고 그 패턴을 바탕으로 해당 건물에 있는 서비스 기술자들에게 ' 거기에 갈 때는 1층으로 가지 마세요'라고 알려줄 수 있는 겁니다 ." [S1]
> "3층으로 가지 마세요. "25층으로 가세요. 앞으로 몇 주 안에 문에 문제가 생길 수도 있습니다 ." 이렇게 맞춤형 지원을 제공할 수 있습니다 ." [S1]

(자막 원문의 따옴표·띄어쓰기 오류를 그대로 옮김. 과제 지시문의 "1층 말고 25층으로" 요약과 달리 원문에는 **1층·3층·25층 세 층이 모두 등장**한다.)

티켓 생성은 **인간 전문가 4개 직군이 한자리에 모이는 과정**으로 명시된다 — 이 사례에서 가장 강한 AUG 근거:

> "이를 디지털 운영 센터 티켓이라고 부릅니다. 데이터 전문가, AI 전문가, 서비스 기술 전문가, 프로세스 전문가가 한자리에 모여 엘리베이터에 앞으로 어떤 문제나 지원이 필요할지 파악하고 분석한 후 티켓을 생성합니다." [S1]

그리고 산출물은 **기술자의 언어로 번역**된다:

> "티켓은 적절한 언어로 작성됩니다. 마티아스의 골드 데이터 언어는 서비스 기술자가 이해하기 쉬운 언어로 작성되었습니다 ." [S1]
> "예를 들어, 해당 층으로 가서 다음 문을 확인하거나, 승강로 연동 장치에 문제가 있을 수 있다는 식이죠." [S1]
> "이렇게 데이터에서 문제를 파악하면 실제 상황 과 지원에 필요한 정보로 변환하여, 일반 FSM CRM 시스템을 통해 서비스 기술자에게 티켓으로 전송합니다. 따라서 기술자는 필요한 모든 데이터를 활용하여 실질적인 지원을 제공할 수 있습니다." [S1]

("마티아스의 골드 데이터 언어는" 부분은 기계번역 오류로 보인다. 원 발화는 화자 이름 Matthias Goll에서 파생된 오인식일 가능성이 높으나 **[S1]만으로는 확정 불가**. 인용 시 6.11 참조.)

RAG 에이전트도 대체가 아니라 **방문 준비와 의사결정 보조**로 규정된다:

> "이를 통해 기술자는 다음 유지보수 방문을 더욱 효과적으로 준비할 수 있게 되고, 더 나은 의사 결정을 내릴 수 있습니다." [S1]
> "기술자가 필요로 하는 맥락에 맞춰 정보를 제공함으로써" [S1]

**(B) 뒷단 증강 — 음성 디브리핑**

> "저희는 항상 기술자들이 업무에는 매우 능숙 하지만 작업 자체에는 집중하지 못하고 사후 기록에는 소홀하다는 문제에 직면해 있었습니다. 하지만 이제 저희는 이러한 문제를 해결할 수 있게 되었습니다. 기술자에게 실제로 어떤 작업을 했는지 묻는 음성 에이전트가 있습니다 ." [S1]

여기서 인간은 루프에서 빠지는 것이 아니라 **지식의 유일한 원천으로 루프에 고정**된다. 기계는 질문자이고 인간이 응답자다. 그 결과가 조직 자산으로 전환된다:

> "그러면 해당 정보는 데이터 플랫폼에 입력되고 다음 서비스 기술자에게도 제공될 수 있습니다 . 이는 기존에 서비스 기술자들이 가지고 있던 개별적인 지식이 아니라 시스템적인 지식에 더 가깝습니다 ." [S1]

**(C) 증강 학습의 전제 — 도메인 전문성**

마티아스가 제시한 "네 가지 주제" 중 두 번째:

> "한 사람은 이 훌륭한 기술을 정말 잘 활용하고 있네요 . 강력합니다. 하지만 여기에 더해 저희는 해당 분야에 대한 탄탄한 전문 지식을 갖추고 있습니다. 저희 회사에는 업무에 정통한 서비스 기술자들이 있습니다 . 그래서 거기에 그걸 더하는 겁니다." [S1]

(첫 문장 "한 사람은 이 훌륭한 기술을 정말 잘 활용하고 있네요"는 자막 붕괴 구간으로 판단되며, 네 요소 중 첫 번째 항목의 원문을 복원할 수 없다 — [S1]에 없음.)

크리스티안 측의 대응 진술:

> "엘리베이터 분야에서 얻은 모든 경험을 서비스 운영에 접목시킨 것이죠. 이 두 가지를 통합해야만 현장에서 서비스 기술자들에게 실질적인 가치를 창출할 수 있다고 생각합니다" [S1]

**(D) 범용 개인 생산성 도구로는 불충분하다는 판단**

> "Copilot, ChatGPT 등 개인 생산성을 향상시키는 도구는 많지만, 그것만으로는 충분하지 않다고 생각했습니다 . 그래서 저희는 전체적인 여정을 다시 살펴보았습니다. Matthias가 모든 단계를 설명했고, 지난 10년 동안 이미 해결한 문제와 아직 부족한 부분을 파악했습니다." [S1]

---

### 6.5 전환 메커니즘 (CYCLE)

**명시적·형식화된 승격 기준(정확도 임계치, 파일럿 기간, 게이트 심사 등)은 [S1]에 없다.** 다만 [S1]은 **서사 형태의 순차 축적 원칙**을 반복적으로 진술하며, 이것이 사실상의 전환 논리로 기능한다.

**(1) 층위적 축적 원칙 — "기반이 먼저"**

> "저희는 클라우드에 연결된 MAX Box로 시작했습니다. 우리는 거기에 우리 분야의 전문 지식을 더했습니다. 우리는 거기에 머신러닝을 추가했습니다. 우리는 거기에 디지털 운영 센터를 추가했습니다. 이 모든 것이 예측 및 예방 정비에 도움이 되었습니다" [S1]

> "하지만 우리는 탄탄한 기반을 다지고 , 그 기반을 지속적으로 발전시키며, 그 위에 쌓아 올리는 데 집중해야 합니다 . 그렇지 않으면 우리는 한 유행에서 다른 유행으로 휙휙 옮겨 다니게 될 뿐입니다" [S1]

**(2) 승격의 전제조건 = 데이터가 읽을 수 있게 되는 것**

이 사례의 전환 기준으로 가장 근접한 진술:

> "이 모든 것을 AI 준비 데이터라고 부릅니다. 왜냐하면 사람이 읽을 수 없다면 에이전트가 어떻게 읽을 수 있겠습니까?" [S1]

영상 도입부에도 같은 명제가 다른 번역으로 반복된다: "인간도 읽을 수 없다면, 요원들은 어떻게 읽을 수 있을까요?" [S1] ("요원들" = agents의 오역).

즉 **인간이 해석 가능한 상태(공통 의미 부여)를 통과한 데이터만 기계에게 넘긴다**는 것이 이 조직의 전환 게이트다. "우리는 데이터를 표준화 하고 공통된 의미를 부여했습니다." [S1]

**(3) 규모 확장 요건**

> "세 번째는 단순히 개념 증명(POC)에 그치는 것이 아니라, 실제로 규모 확장을 목표로 하는 것입니다." [S1]

**(4) 조언 형태로 제시된 순서**

> "모든 것을 한 번에 시작하기보다는 아주 작은 것부터 시작하는 것이 좋습니다. 하지만 항상 최종 목표를 염두에 두고 모듈화하여 계층적으로 구축해 나가세요. Databricks를 사용하면 이러한 방식이 가능해집니다. 먼저 데이터를 가져와 모델링하고, 더 자세히 설명한 다음, 에이전트 기반 솔루션 등을 구현하는 단계로 나아갈 수 있습니다" [S1]

**증강 회귀(조건 변화 시 인간 복귀) 사례: [S1]에 없음.** 실패 후 되돌린 사례, 에이전트 오류 대응 절차, 롤백 기준에 대한 서술이 [S1]에 전혀 등장하지 않는다.

---

### 6.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

**SPILL — 있음. 이 사례의 가장 뚜렷한 특징이다.**

파급 경로 1: **이벤트 판독 자동화 -> 티켓 작성이라는 인간 협업 과업의 신설**

기계가 오류코드·고장코드를 대량 판독하게 되자, 그 출력을 현장 언어로 번역하는 **새로운 다직군 협업 과업**이 생겼다:

> "데이터 전문가, AI 전문가, 서비스 기술 전문가, 프로세스 전문가가 한자리에 모여 엘리베이터에 앞으로 어떤 문제나 지원이 필요할지 파악하고 분석한 후 티켓을 생성합니다." [S1]

파급 경로 2: **보고 자동화 -> 대화형 데이터 접근 요구의 발생**

보고 자동화가 끝나자 **다음 질문이 자동으로 생겨났다**고 [S1]은 서술한다:

> "우선, 처음부터 보고 자동화를 진행했습니다. 저희 CFO와 현장 운영 담당자 모두 만족했습니다 . 하지만 그 외에도 항상 ' 데이터와 더 쉽게 상호작용할 수 있는 방법은 없을까?'라는 질문이 있었습니다. 그래서 Genie를 통해 이 부분을 더욱 심층적으로 탐구했습니다." [S1]

이것이 논문의 SPILL 도식(한 과업의 자동화가 인접 과업의 증강을 유발)과 정확히 맞물린다: 보고서 생산은 기계로 넘어갔고, 그 결과 **비개발자가 데이터에 직접 질문하는** 증강 과업이 인접에서 생겨났다. Genie Code 언급도 같은 방향이다:

> "요즘 Genie Code는 개발 경험이 없거나 개발 경험이 부족한 사람들도 대시보드 등을 만들 수 있게 해줘서 정말 좋습니다." [S1]

파급 경로 3: **RAG 자동화 -> 음성 디브리핑이라는 인접 증강**

[S1]은 두 단계를 인과적으로 연결한다:

> "기술자가 필요로 하는 맥락에 맞춰 정보를 제공함으로써 다음 단계인 음성 디브리핑을 진행할 수 있습니다." [S1]

즉 방문 **전** 정보 제공(자동)이 방문 **후** 지식 회수(증강)를 가능하게 만들었다.

**REINV — 근거 빈약. 사실상 확인 불가.**

논문의 UBS 패턴(자동화로 확보한 자원을 증강에 재투자)에 해당하려면 "자동화로 절감된 시간/인력/비용을 X에 돌렸다"는 진술이 필요하나, **[S1]에 그런 진술은 없다.** 절감 수치도 없고 재배치 서술도 없다.

간접적으로 REINV 방향으로 읽을 수 있는 유일한 진술은 지속 투자 선언이다:

> "그래서 이것은 장기적인 여정이었고 우리는 계속 투자했습니다. 우리는 계속 집중했어요. 우리는 가치를 창출하는 데 정말 최선을 다했습니다." [S1]

그러나 이는 **자동화 산출물의 재투자가 아니라 일반적인 투자 지속 선언**이므로 REINV 근거로 쓰기에는 약하다. 또한 사후 기록 부담을 음성 에이전트로 덜어낸 결과 기술자가 "작업 자체"에 집중하게 된다는 함의가 있으나, [S1]은 절감된 시간이 어디로 갔는지 **명시하지 않는다**.

판정: **REINV = 근거 불충분(사실상 없음).**

---

### 6.7 통합 장치 (RESP)

[S1]의 RESP는 **개인의 승인권**이 아니라 **데이터 계보·감사가능성이라는 인프라 수준의 책임 구조**로 나타난다. 이 점이 이 사례의 특징이자 한계다.

**(1) 계보와 감사 가능성 — 명시적이고 최우선 순위로 선언됨**

> "저희에게 가장 중요한 것은 데이터의 계보를 파악하는 것입니다 . 모든 데이터의 감사 가능성을 확보해야 합니다." [S1]

> "레이크하우스 아키텍처를 Unity Catalog를 통해 설명하고, 회사 전체에 걸쳐 일관성 있는 더 나은 감사 가능한 정보를 만드는 데 사용했습니다" [S1]

**(2) 단일 진실 원천 — "여러 개의 수치" 문제의 해소**

> "이전에는 수작업으로 처리하는 경우가 많았고, 집계된 데이터 수준에서는 수치에 대한 의문이 제기되기도 했습니다. 같은 질문에 대해 여러 개의 수치가 존재하기도 했죠 . 하지만 이제는 이러한 문제를 해결했습니다." [S1]

진행자 확인: "네, 그러니까 기본적으로 Databricks 메트릭을 구축하신 거죠? 여러 부서 간의 단일 진실 소스 역할을 하는 거죠 ." [S1]

("하지만 이제는 이러한 문제를 해결했습니다"는 **자체 선언**이며, 제3자 검증이나 측정 근거는 [S1]에 없다.)

**(3) 데이터 품질 유지의 지속 책임**

> "한편으로는 데이터 품질을 유지하고 데이터 기반을 구축하는 데 계속 집중하는 것이 매우 중요하다고 생각합니다." [S1]

**(4) 조직적 파트너십 구조**

> "단순히 기술적인 문제만이 아니라, 어떻게 시스템을 구축하느냐가 중요했습니다. 저희는 기술 개발도 중요하지만, 조직 내에서 적합한 파트너를 확보하는 것도 중요하다고 생각했습니다. 그래서 비즈니스 조직, 현장 조직과 협력했습니다. 기술 측면에서는 Microsoft와 Databricks 같은 파트너를 영입했고, 필요한 서비스 제공업체도 확보했습니다." [S1]

이 진술은 논문 p.195 명제(증강 학습은 IT부서/외부업체에 위임 불가)와 **부분적으로 긴장**한다: 기술 파트너와 서비스 제공업체를 외부에서 영입했다고 명시하되, 도메인 지식 축은 사내 서비스 기술자에게 두었다("저희 회사에는 업무에 정통한 서비스 기술자들이 있습니다" [S1]). 6.10 참조.

**(5) 명시적으로 없는 것**

다음 항목은 **[S1]에 없다**: 티켓에 대한 인간 최종 승인권 절차, 에이전트 출력의 검토·거부 절차, 에이전트 오류 시 책임 귀속, 모델 성능 모니터링/평가 체계, 기술자가 에이전트 권고를 무시할 수 있는 권한에 관한 서술. "안전"은 데이터 속성으로만 언급된다: "모든 것은 고품질의 안전하고 보안이 강화된 데이터를 기반으로 합니다." [S1]

즉 **RESP는 데이터 층위에서는 강하고, 에이전트 의사결정 층위에서는 [S1]에 서술이 없다.**

---

### 6.8 성과 수치

**정량 성과 판정: [S1]은 before/after 정량 성과 수치를 사실상 제시하지 않는다.** 등장하는 숫자는 전부 **규모(scale) 수치**이거나 **연혁 수치**이며, 개선 폭을 나타내는 수치는 **0건**이다.

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 직원 수 | — | 5만 명 | [S1] | **자체보고** (규모 수치, 성과 아님) |
| 서비스 기술자 수 | — | 25,000명 | [S1] | **자체보고** (규모 수치) |
| 관리 엘리베이터/에스컬레이터 | — | 140만 대 | [S1] | **자체보고** (규모 수치) |
| 일일 수송 인원 | — | 15억 명 | [S1] | **자체보고** (규모 수치) |
| 보유 시스템 / 국가 | — | 100개 이상 시스템 / 50개국 이상 | [S1] | **자체보고**, 영상 내 2회 반복 |
| IoT 이벤트 | — | 5억 개 (단위 주기 미상) | [S1] | **자체보고**, 진행자와 화자 모두 언급 |
| 사전 분석 이벤트 건수 | — | "수천, 수십만 건" | [S1] | **자체보고**, 정성 표현 |
| 동일 KPI에 대한 복수 수치 | "같은 질문에 대해 여러 개의 수치가 존재하기도 했죠" | "하지만 이제는 이러한 문제를 해결했습니다." | [S1] | **자체보고, 정성 서술 — 수치 없음** |
| 보고 자동화 효과 | 수작업 처리 | "저희 CFO와 현장 운영 담당자 모두 만족했습니다" | [S1] | **자체보고, 만족도 진술 — 수치 없음** |
| 기술자 사후 기록 | "사후 기록에는 소홀하다" | "이제 저희는 이러한 문제를 해결할 수 있게 되었습니다" | [S1] | **자체보고, 수치 없음. "할 수 있게 되었습니다"는 역량 진술이지 성과 측정치 아님** |
| 가동 시간(uptime) | — | "가동 시간 확보가 궁극적인 목표입니다." | [S1] | **목표 진술 — 달성치 없음** |
| Databricks 도입 시점 | — | 2018년(진행자) / 2019년(크리스티안) | [S1] | 자체보고, **불일치** |
| MAX Box 최초 공개 | — | "정확히 10년 전" 하노버 박람회 | [S1] | 자체보고, 절대연도 없음 |

참고 — **대조군의 수치 성격 차이:**

| 지표 | 값 | 소스 | 자체보고 여부 |
|---|---|---|---|
| 직원 / 고객 | 6,000명 / 약 800만 명 | [S2] | 고객사 임원 **자체보고** |
| 예비 부품 재고 최적화 | "18,000개 이상의 자산에서 실시간 센서 데이터를 통합하여 10억 달러 이상의 예비 부품 재고를 최적화했습니다" | [S3] | **벤더(Databricks) 자체 집계**, 고객사 무기명 |
| 예측 시간 단축 | "예측 시간을 48시간에서 45분으로 단축했습니다" | [S3] | **벤더 자체 집계**, 고객사 무기명, before/after 형태 |
| 기획 리드타임 | "며칠씩 걸리던 음악 기획 작업을 단 몇 분으로 단축" | [S3] | **벤더 자체 집계**. "음악"은 자막 오류로 원 단어 소실 |

즉 **before/after 형태의 성과 수치는 실명 고객 사례 [S1][S2]에는 없고, 무기명 벤더 집계 [S3]에만 존재한다.** 이 비대칭 자체가 인용 시 중요한 사실이다.

---

### 6.9 소스 간 교차 대조

**(1) 반복 확인된 사실 — [S1] 내부 2인 화자 간**

- **인수합병에 따른 시스템 파편화 (50개국+/100개 시스템+).** 영상 도입 요약과 마티아스 파트에서 "우리는 인수 합병을 통해 크게 성장했고, 그 결과 50개국 이상에서 100개 이상의 시스템을 보유하게 되었습니다" [S1], 크리스티안 파트에서 "기업 세계는 인수 합병을 통해 크게 성장하면서 50개국 이상에 100개가 넘는 시스템을 보유하게 되었고" [S1]. **서로 다른 화자가 같은 수치를 진술** — [S1] 내에서 가장 견고한 수치.
- **"AI 준비 데이터"의 논거.** 도입부 "인간도 읽을 수 없다면, 요원들은 어떻게 읽을 수 있을까요?" [S1] / 크리스티안 "왜냐하면 사람이 읽을 수 없다면 에이전트가 어떻게 읽을 수 있겠습니까?" [S1]. 같은 문장의 두 가지 번역이 한 파일에 공존한다.
- **명칭의 표기 흔들림.** 도입부는 "City to Nexus 프로젝트에서 Unity 카탈로그" [S1], 본문은 "CDP Nexus라는 공통 언어 시스템" / "CDP Nexus 프로젝트" [S1]. 또 "AI 활용 가능 데이터"(도입부)와 "AI 준비 데이터"(본문)가 같은 개념을 가리킨다 [S1]. 동일 대상의 **번역 불안정**이며 사실 불일치는 아니다.
- **10년이라는 기간.** 마티아스 "우리는 이 여정을 10년 넘게 걸어왔습니다" [S1] / 크리스티안 "저희는 IoT 사업을 10년 전부터 시작했고" [S1] / "지난 10년 동안 이미 해결한 문제와 아직 부족한 부분을 파악했습니다" [S1]. 3회 반복.
- **서비스 기술자가 가치 창출의 종점이라는 규정.** 마티아스 "그리고 그 일은 저희 서비스 기술자들이 가장 잘 해내는 부분입니다" [S1] / 크리스티안 "이 두 가지를 통합해야만 현장에서 서비스 기술자들에게 실질적인 가치를 창출할 수 있다고 생각합니다" [S1]. **두 화자가 독립적으로 같은 규정에 도달** — 이 사례의 AUG 성격을 뒷받침하는 가장 강한 교차 근거.

**(2) 명백한 모순 — Databricks 도입 연도**

| 화자 | 진술 | 연도 |
|---|---|---|
| 진행자 | "그는 디지털 데이터 및 AI 재단을 이끌고 있으며, 그의 팀은 2018년부터 Databricks를 사용해 왔습니다." [S1] | 2018 |
| 크리스티안(당사자) | "말씀하신 대로, 저희는 IoT 사업을 10년 전부터 시작했고, 2019년부터는 Databricks를 활용해 왔습니다." [S1] | 2019 |

같은 영상, 연속된 두 발화에서 1년 차이. 크리스티안이 "말씀하신 대로"로 받으면서도 다른 연도를 말한다. **당사자 진술(2019)이 우선하되, 1년 오차를 병기하는 것이 정직하다.** 어느 쪽이 옳은지는 [S1]으로 판정 불가.

**(3) 한 소스에만 있는 사실 — 사실상 [S1] 고유 정보 전부**

TK Elevator에 관한 모든 진술(규모, MAX Box, 디지털 운영 센터, CDP Nexus, 25층 일화, 음성 디브리핑, RAG 에이전트, 계보/감사 서술)은 **[S1] 단일 소스에만 존재**한다. [S2][S3]에는 TK Elevator가 등장하지 않는다. **교차 검증된 TK Elevator 사실은 0건**이며, 위 (1)의 "반복 확인"은 모두 **동일 영상 내부의 화자 간 반복**이지 독립 소스 간 확인이 아니다. 이 점을 인용 시 반드시 명시해야 한다.

**(4) 시점에 따른 서술 변화**

동일 조직에 대한 시계열 소스가 없으므로 **시점별 서술 변화는 관측 불가**. 다만 채널 수준에서 Databricks 고객 사례 화법의 변화는 관측된다: [S2](2026-01-27)는 플랫폼 통합·거버넌스 서사에 머물고 에이전트를 언급하지 않는 반면, [S1](2026-06-23)은 RAG·음성 에이전트까지 나아간다. [S3](2026-03-20)은 그 중간 시점에 "단순히 작업을 자동화하는 것을 넘어, 엔드 투 엔드 방식으로 인텔리전스를 조율하는 특수 AI 에이전트" [S3]라는 서사를 제시한다. **5개월 사이 벤더 서사가 거버넌스에서 에이전트로 이동**했다는 관측은 가능하나, 이는 고객 조직의 변화가 아니라 **벤더 마케팅 서사의 변화**로 해석해야 한다.

**(5) 대조군과의 구조 대비**

| 축 | [S1] TK Elevator | [S2] UK Power Networks | [S3] 제조업 일반(무기명) |
|---|---|---|---|
| 거버넌스 도구 | Unity Catalog + 계보/감사 [S1] | "저희는 Unity [음악] 카탈로그를 사용하여 사람들이 데이터에 접근하는 방식에 대한 접근 권한 및 관리 체계를 유지하고 있습니다" [S2] | "셋째, 접근 제어, 감사 및 모니터링을 통한 안전한 거버넌스입니다." [S3] |
| 현장 인력 증강 | 앞단·뒷단 양쪽 명시 [S1] | **없음** — 유지보수는 데이터 항목으로만 언급("장비의 상태, 최근 유지보수 시기" [S2]) | 운영자 알림 수준: "제조 현장 운영자는 실시간으로 지연 시간이 짧은 이미지 기반 결함 알림을 받아" [S3] |
| 정량 성과 | **없음** | **없음** | 있으나 **무기명 벤더 집계** [S3] |
| 자동화의 종착점 | 인간(기술자) [S1] | 명시 안 됨, 탐색 단계 강조 [S2] | "가동 시간 증가, 효율적인 스케줄링, 비용 절감" [S3] |

[S2]는 성숙도가 낮은 단계의 화법을 보여준다: "AI 실험을 진행하고, 머신러닝을 활용하고, 음악 분야에서 이러한 기술이 어떻게 도움이 될 수 있는지 실험하여, 이전에는 플랫폼이 없어서 만들 수 없었던 비즈니스용 제품을 개발합니다." [S2] — 즉 **동일 벤더·동일 도구·동일 시기에도 현장 인력 증강 서사가 없는 사례가 존재**하며, 이는 [S1]의 증강 구조가 도구의 필연적 결과가 아님을 보여주는 대조 증거다.

---

### 6.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간 루프 제외 (p.194) | 보고 자동화("우선, 처음부터 보고 자동화를 진행했습니다" [S1]), 대량 이벤트 판독("수천, 수십만 건의 사건들을 분석합니다" [S1]), PDF -> 검색가능 변환 [S1] | **지지** |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | 티켓의 기술자 언어 번역("서비스 기술자가 이해하기 쉬운 언어로 작성되었습니다" [S1]), 음성 디브리핑에서 인간이 지식 원천 [S1] | **지지** |
| CYCLE: 증강 학습 -> 견고화 -> 자동화 (p.196-197) | 층위적 축적 서사(6.2 표의 MAX Box→전문지식→머신러닝→디지털 운영 센터 순서 [S1]), "탄탄한 기반을 다지고 , 그 기반을 지속적으로 발전시키며, 그 위에 쌓아 올리는 데 집중해야 합니다" [S1] | **부분 지지.** 방향성은 일치하나 **승격 임계치·게이트 기준은 [S1]에 없음** |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 해당 서술 **[S1]에 없음** | **미관측** (반증 아님, 데이터 부재) |
| SPILL: 한 과업 자동화가 인접 과업의 증강 유발 (p.197) | 보고 자동화 완료 -> "데이터와 더 쉽게 상호작용할 수 있는 방법은 없을까?" -> Genie [S1]; RAG 제공 -> "다음 단계인 음성 디브리핑을 진행할 수 있습니다" [S1]; 이벤트 판독 자동화 -> 4직군 티켓 회의 신설 [S1] | **강한 지지 + 확장** (3개 경로 관측) |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS 패턴) | 절감 자원의 재배치 서술 **없음**. "우리는 계속 투자했습니다" [S1]는 일반 투자 선언 | **미관측 / 근거 불충분** |
| RESP: 인간이 프로세스 전체 책임·승인·감사 보유 (p.200) | 데이터 계보·감사 가능성 최우선("모든 데이터의 감사 가능성을 확보해야 합니다" [S1]), 단일 진실 원천 확립 [S1] | **부분 지지 + 재정의.** 감사 축은 강하나 **에이전트 출력에 대한 인간 승인권은 [S1]에 없음** |
| 증강 학습은 도메인 전문가의 암묵지에 의존, IT부서/외부업체 위임 불가 (p.195) | "저희 회사에는 업무에 정통한 서비스 기술자들이 있습니다" [S1]; 티켓 회의에 "서비스 기술 전문가, 프로세스 전문가" 참여 [S1]; 음성 디브리핑으로 기술자 암묵지를 직접 추출 [S1]. 동시에 "Microsoft와 Databricks 같은 파트너를 영입했고, 필요한 서비스 제공업체도 확보했습니다" [S1] | **지지 + 정교화.** 위임 불가 대상은 **도메인 지식 축**이며, **플랫폼 축은 외부 위임이 일어났다** — 두 축의 분리를 보여줌 |
| 기계 한계 4가지 중 "훈련된 과업에 국한" (p.198) | 범용 도구 불충분 판단: "Copilot, ChatGPT 등 개인 생산성을 향상시키는 도구는 많지만, 그것만으로는 충분하지 않다고 생각했습니다" [S1] | **지지** |
| 기계 한계 중 "감각/감정/사회기술 부재" (p.198) | 현장 육안·촉각 판단은 여전히 기술자에게 있음이 함의되나 **명시적 진술은 [S1]에 없음** | **미관측** |
| 한쪽 편중 시 악순환 (p.199) | "그렇지 않으면 우리는 한 유행에서 다른 유행으로 휙휙 옮겨 다니게 될 뿐입니다" [S1] — 다만 이는 기술 유행 추종 경고이지 자동화/증강 편중 경고는 아님 | **약한 유사 / 직접 대응 아님** |
| 기계는 조직 내 새로운 행위자 계급 (p.204) | 음성 에이전트가 기술자에게 **질문하는 주체**로 등장("기술자에게 실제로 어떤 작업을 했는지 묻는 음성 에이전트가 있습니다" [S1]); 디지털 운영 센터가 "AI 기반 전문가 허브" [S1] | **지지 + 확장** (에이전트가 인간에게 질문을 발하는 역할 역전) |

**이 사례가 논문을 확장하는 지점.**

첫째, 논문의 SPILL은 자동화가 인접 과업에 증강 부담을 남긴다는 공간적 명제인데, TK Elevator는 그 파급이 **한 방향이 아니라 현장 방문을 축으로 앞뒤 양쪽에서 동시에** 발생함을 보여준다. 방문 전에는 이벤트 판독 자동화가 "거기에 갈 때는 1층으로 가지 마세요" [S1] / "25층으로 가세요." [S1]라는 번역 노동을 새로 만들었고, 방문 후에는 RAG 자동화가 "다음 단계인 음성 디브리핑" [S1]을 열었다. 자동화된 과업이 인간 과업을 **감싸는 샌드위치 구조**는 논문의 선형적 spillover 도식보다 한 단계 복잡하다.

둘째, 이 사례의 RESP는 논문이 상정한 "인간의 최종 승인권"이 아니라 **데이터 계보와 감사 가능성이라는 사전적·인프라적 책임**으로 구현되어 있다. "저희에게 가장 중요한 것은 데이터의 계보를 파악하는 것입니다" [S1]와 "같은 질문에 대해 여러 개의 수치가 존재하기도 했죠" [S1]의 해소는, 통합 조건이 산출물 승인 시점이 아니라 **입력 의미론이 확정되는 시점**에 걸릴 수 있음을 시사한다. 이는 "사람이 읽을 수 없다면 에이전트가 어떻게 읽을 수 있겠습니까?" [S1]라는 문장으로 압축되며, 증강-자동화 순환의 게이트를 **인간 가독성**으로 정의하는 새로운 판별 기준을 제안한다.

셋째, 음성 디브리핑은 논문 p.195의 암묵지 명제에 대해 **암묵지를 위임 불가한 제약으로 두는 대신 조직적으로 추출·순환시키는 장치**를 보여준다. "이는 기존에 서비스 기술자들이 가지고 있던 개별적인 지식이 아니라 시스템적인 지식에 더 가깝습니다" [S1]는 개인 암묵지가 시스템 지식으로 전환되는 경로를 명시하는데, 이 전환이 **다음 자동화의 학습 데이터를 인간이 직접 공급하는 구조**임에 유의해야 한다. 즉 증강이 자동화를 낳는다는 CYCLE이 여기서는 **인간의 구술이 매 사이클의 연료가 되는 재귀 구조**로 나타난다.

넷째, 대조군 [S2]는 동일 벤더·동일 도구(Unity Catalog)·동일 분기에도 **현장 인력 증강 서사가 전혀 없는 조직**이 존재함을 보여준다. UK Power Networks는 거버넌스와 실험 단계에 머무르며 "장비의 상태, 최근 유지보수 시기" [S2]를 데이터 항목으로만 다룬다. 이는 증강-자동화 배치가 **플랫폼의 함수가 아니라 조직의 축적 이력과 선택의 함수**라는 논문의 전제를 경험적으로 뒷받침한다.

---

### 6.11 인용 시 주의사항

**(1) 단일 소스 의존 — 가장 큰 제약.**
TK Elevator에 관한 모든 사실은 [S1] 한 건에서 나온다. 6.9(1)의 "반복 확인"은 **동일 영상 내 두 화자 간 반복**일 뿐 독립 소스 간 교차검증이 아니다. 이 사례를 인용할 때는 "벤더 제작 단일 영상 기반"임을 반드시 병기해야 한다.

**(2) 전량 자체보고 + 벤더 채널 게시.**
[S1]은 Databricks 공식 채널이 제작·배포한 고객 사례 영상이며, 발화자는 모두 TK Elevator 임원이다. **제3자 검증치는 [S1]에 단 한 건도 없다.** 실패·비용·중단·저항에 관한 서술도 전혀 없다(생존 편향).

**(3) 정량 성과가 없다는 사실 자체를 명시할 것.**
6.8에서 판정했듯 **before/after 개선 수치는 0건**이다. "저희 CFO와 현장 운영 담당자 모두 만족했습니다" [S1], "이제는 이러한 문제를 해결했습니다" [S1] 같은 만족도·역량 진술을 성과 수치로 환산해 인용해서는 안 된다. 5만/25,000/140만/15억/5억은 모두 **규모 수치이지 성과 수치가 아니다**.

**(4) 성숙도 — 계획/탐색과 운영을 구분할 것.**
- Genie: 진행자의 "활용하고 계신가요?" [S1]에 대한 답이 **"검토 중입니다." [S1]** 이다. 이어지는 "Genie를 데이터 레이크 위에 구축하여 보고서에 표시되는 데이터를 음성으로 검색하거나 질문을 입력하여 KPI에 대한 답변을 얻을 수 있도록 했습니다." [S1]와 시제가 충돌한다. **Genie를 운영 중인 것으로 인용하면 과장이다.**
- RAG 에이전트("구축하여" [S1])와 음성 디브리핑("음성 에이전트가 있습니다" [S1])은 존재는 단언되지만, **배포 범위(25,000명 중 몇 명), 지역, 시작 시점이 [S1]에 전혀 없다.** 파일럿인지 전사 운영인지 판정 불가.
- 보고 자동화만이 "저희 CFO와 현장 운영 담당자 모두 만족했습니다" [S1]라는 수용 증거를 동반한 유일한 항목이다.

**(5) 자막 기계번역 오류 — 인용 전 반드시 확인.**
[S1]은 한국어 기계번역 자막이며 다음 붕괴 구간이 있다:
- "City to Nexus 프로젝트" [S1] = 본문의 "CDP Nexus" [S1]의 오인식. **동일 대상**.
- "인간도 읽을 수 없다면, 요원들은 어떻게 읽을 수 있을까요?" [S1] — "요원들"은 agents의 오역.
- "AI 활용 가능 데이터" [S1] / "AI 준비 데이터" [S1] — 동일 개념(AI-ready data)의 두 번역.
- "마티아스의 골드 데이터 언어는 서비스 기술자가 이해하기 쉬운 언어로 작성되었습니다" [S1] — 문장이 붕괴되어 있다. 화자 이름 "마티아스 골"에서 파생된 오인식으로 추정되나 **[S1]만으로 원문 복원 불가**. 이 문장을 근거로 "골드 데이터 언어"라는 개념이 존재한다고 주장해서는 안 된다.
- "한 사람은 이 훌륭한 기술을 정말 잘 활용하고 있네요" [S1] — 마티아스의 "네 가지 주제" 중 첫 항목이 소실된 구간. **네 요소 중 첫째가 무엇인지 [S1]에 없다.**
- "원하시면 엘리베이터 내부에 머신 비전 카메라를 설치하여 안전성을 높이고 아바타가 내부에서 원활하게 움직일 수 있도록 도와드릴 수도 있습니다." [S1] — "아바타"는 오역으로 보이며 원 단어 불명.
- "제 생각에는 이는 기술적인 질문이기도 하고... 동맹 질문을 던지고 해결하고자 하는 문제가 무엇인지 이해하는 것이 중요합니다." [S1] — "동맹 질문"은 붕괴된 표현.
- "세대 인공지능" [S1] = generative AI의 오역.
- 문장부호 앞 공백("있습니다 .", "겁니다 .", "봤어요 .")과 따옴표 불일치가 다수 있다. **원문 그대로 인용하되 오류임을 각주로 밝힐 것.**
- 대조군 [S2][S3]는 오류가 더 심각하다: "누가 어떤 음악에 얼마나 접근할 수 있는지" [S2], "며칠씩 걸리던 음악 기획 작업" [S3], "음악은 재료비를 절감하며" [S3] 등에서 **원 단어가 "음악"으로 치환**되어 소실됐다. [S3]의 수치를 인용할 때 문맥 단어가 불명함을 반드시 표기할 것.

**(6) 귀속 문제.**
- **Databricks 도입 연도 2018 vs 2019 불일치** (6.9(2)). 인용 시 "2018년 또는 2019년(소스 내 불일치)"로 표기할 것.
- MAX Box 공개 시점은 "정확히 10년 전" [S1]으로만 서술된다. 영상 업로드일(2026-06-23)에서 역산한 2016년은 **소스에 없는 추론**이므로 확정 표기 금지. 또한 "바로 이곳 하노버 박람회에서" [S1]는 촬영 장소를 시사할 뿐 촬영일이 업로드일과 같다는 보장이 없다.
- "5억 개의 이벤트" [S1]의 **집계 주기가 명시되지 않는다**. "일 5억 건"으로 인용하면 소스를 넘어선다.
- 25층 일화는 마티아스가 **기술자에게 들은 말을 재구성한 것**이다("그러자 서비스 기술자 중 한 명이 저에게 다가와서" [S1] 로 시작해 "라고 말했습니다." [S1] 로 닫히는 전언 구조). 기술자의 직접 발화가 아니라 **임원의 전언**이며, 인용부호 위치도 자막상 붕괴되어 있어 어디까지가 기술자 발화인지 불분명하다.
- [S3]의 수치("18,000개 이상의 자산", "10억 달러 이상", "48시간에서 45분")는 **고객사가 특정되지 않은 벤더 집계**이며 TK Elevator와 무관하다. 두 사례의 수치를 섞어 인용해서는 안 된다.

**(7) 이론 코딩상의 취약 지점.**
REINV는 근거가 없고, CYCLE의 승격 기준과 증강 회귀도 [S1]에 없으며, RESP의 에이전트 승인권도 없다. **이 세 구성개념에 대해 이 사례를 근거로 삼는 것은 부적절하며, "미관측"으로 처리해야 한다.** 이 사례가 강한 근거를 제공하는 것은 AUTO, AUG, SPILL, 그리고 (데이터 층위로 재정의된) RESP 네 가지다.

---

**요약.** [S1] TK Elevator 인터뷰 전문(1995단어)과 대조군 [S2] UK Power Networks·[S3] AI Agents for Manufacturing 전문을 모두 읽고 사례를 작성했다. 지정 검색어 5개로는 추가 소스가 없었고, 완화 검색으로 확보한 두 건은 TK Elevator 정보를 포함하지 않는 순수 구조 대조군이다. 이 사례는 AUTO(보고 자동화·이벤트 판독·PDF 변환), AUG(티켓의 기술자 언어 번역·음성 디브리핑), SPILL(3개 파급 경로)에 강한 근거를 제공하고, RESP는 승인권이 아닌 데이터 계보·감사 가능성 형태로 재정의된다. 반면 REINV, CYCLE의 승격 임계치, 증강 회귀, 에이전트 출력 승인 절차는 소스에 전혀 없어 미관측 처리했다. 최대 한계는 세 가지다 — (1) 벤더 제작 단일 영상 의존으로 독립 교차검증이 0건, (2) before/after 정량 성과 수치가 0건이고 전부 규모 수치와 만족도 진술뿐, (3) Genie가 "검토 중"으로 자기 규정되고 RAG·음성 에이전트의 배포 범위·시점이 없어 성숙도 판정 불가. 추가로 Databricks 도입 연도가 같은 영상 안에서 2018년과 2019년으로 엇갈리며, 기계번역 자막 붕괴 구간("City to Nexus", "골드 데이터 언어", "요원들", 대조군의 "음악" 치환 등)을 인용 주의사항에 전수 기재했다.


---



## 사례 7 — Deloitte : 송장 92% 자동화 + 영업 에이전트

*원문: `docs/cases/06_deloitte.md`*

> **[귀속 경고 — 반드시 먼저 읽을 것]**
> 이 사례의 1차 근거 [S1]은 **Intel 공식 유튜브 채널**(팟캐스트 "인텔 온 AI")에 게시된 영상이지만,
> 사례를 진술하는 발화자는 Intel 직원이 아니라 **Deloitte의 TMT(기술·미디어·엔터테인먼트·통신) 산업
> AI 사업부 글로벌 리더**다. 자막 표기로는 "바레쉬는 디오이트의 기술, 미디어, 엔터테인먼트 및 통신(TMT) 산업 분야 AI 사업부의 글로벌 리더입니다." [S1]
> 따라서 **송장 92% 자동화도, 영업 에이전트도 Intel의 자사 사례가 아니다.** Intel은 이 사례에서
> 게시 플랫폼(호스트 채널)일 뿐이며, 사례의 주체·수치·주장의 출처는 전적으로 Deloitte 측 발화자다.
> 인용 시 "Intel 사례"로 표기하면 귀속 오류가 된다.
>
> **표기 주의**: [S1]의 한국어 기계번역 자막은 Deloitte를 일관되게 오인식한다. 확인된 표기는
> "디오이트"(1회), "디오테"(1회), "Deote"(2회)이며, 정확한 원 표기 "Deloitte" 또는 "딜로이트"는
> [S1] 안에 **단 한 번도 등장하지 않는다**(문자열 카운트: Deloitte 0, 딜로이트 0). 본문 인용은 자막
> 원문 그대로 옮기고, 실제 회사명은 각주로만 밝힌다.
> - 각주 (a): "디오이트" = Deloitte(딜로이트).
> - 각주 (b): "Deote" = Deloitte. "디오테로서 우리는" = 『As Deloitte, we…』의 오인식.
> - 각주 (c): 발화자명 "Bares Sesh" / "바레쉬" = 자막 오인식된 인명. 정확한 철자는 해당 소스에서 확인 불가.
> - 각주 (d): "정부의 책임성" = governance(거버넌스)의 오역으로 추정되나, 추정임을 명시한다.
> - 각주 (e): "폭의 시대" = "The Age of With"(영상 제목)의 오역. 영상 제목은 The Age of With이다.

---

### 사례 7 - Deloitte : 송장 92% 자동화 + 영업 에이전트 (자율성 단계론과 통제 되돌리기)

### 7.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Intel | **업로드일 2025-10-15** (채널 수집분, 파일 헤더 "업로드일" 기준) | ko | 약 3669개 | Intel 자사 팟캐스트 "인텔 온 AI" 대담. 진행: "헤더 맥위건"(자막 후반부에는 "헤더 맥 위건"으로도 표기). 게스트: "Bares Sesh"/"바레쉬", **Deloitte TMT 산업 AI 사업부 글로벌 리더**(자막 "디오이트") | https://www.youtube.com/watch?v=NgeYg6tyncs | /home/user/youtube-scrap/transcripts/channels/Intel/The_Age_of_With_Rethinking_Enterprise_Strategy_Through_Agent__NgeYg6tyncs.md |
| [S2] | SAP | **업로드일 2026-05-20** (채널 수집분) | en | 약 12149개 | SAP Sapphire Madrid 2026 글로벌 키노트(벤더 자사 행사 무대). Deloitte 측 등장인물: Pavan Srivastava(global CTO of Deloitte), Marlene(Deloitte 컨설턴트, 무대 데모 수행). SAP 측: Christian Klein(CEO), Philipp Herzig, Sebastian Steinhaeuser, Sophia Levens | https://www.youtube.com/watch?v=CocpyxAizwE | /home/user/youtube-scrap/transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Madrid_2__CocpyxAizwE.md |
| [S3] | Oracle | **업로드일 2026-06-18** (채널 수집분) | ko | 약 7025개 | Oracle 영상 시리즈 "AI가 모든 것을 바꾼다" 인터뷰. 게스트: 토니 와이스, **딜로이트의 국방 분야 AI 파트너**. 서두에 면책 고지("이 팟캐스트에서 표현된 견해는 개별 발표자의 견해이며, 발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다.") | https://www.youtube.com/watch?v=AF8rr7rCl38 | /home/user/youtube-scrap/transcripts/channels/Oracle/AI_Changes_Everything_What_Leaders_Must_Get_Right_About_AI__AF8rr7rCl38.md |

세 소스 모두 **채널 수집분**이므로 표의 날짜는 **영상 업로드일**이다(키워드 수집분의 『수집일』과 혼동하지 말 것).

각 소스의 역할:
- **[S1] 1차 근거.** 송장 92%/8% 배분, 영업 에이전트(2,000명·30~50개 시스템·피치덱 70%), 자율성 단계론, 통제 되돌리기, 성과지표 재정의, Talo ARPU 일화, 확장 규모 조언이 모두 여기에만 있다.
- **[S2] 보강(단, 별개 조직·별개 시점).** 사전 확인 결과 **단순 파트너 언급이 아니다** — Deloitte 글로벌 CTO가 무대에 올라 자사 AI 도입 수치를 직접 진술하고, Deloitte 컨설턴트가 에이전트 구축 데모를 수행하며, Deloitte가 SAP Industry AI 고객 명단에도 등장한다. 다만 [S1]의 송장/영업 사례와는 **연결점이 전혀 없는 별개 사안**이다. 아래 7.6·7.9에서 보조 사례로 별도 정리한다.
- **[S3] 보강 겸 대조군.** 역시 단순 언급이 아니라 **Deloitte 국방 AI 파트너 본인의 인터뷰**다. 그러나 다루는 조직(국방·공공)과 논점(인간 개입 필요성 자체에 대한 반론)이 [S1]과 달라, 같은 회사 내부의 **상반된 인간-루프 관점**을 보여주는 대조군으로 쓴다.

---

### 7.2 조직과 문제 상황

**(1) 영업 에이전트 고객사** — 조직 정체성은 "고객사 중 한 곳"으로만 특정된다. "예를 들어, 저희는 고객사 중 한 곳을 위해 에이전트 기반 AI 솔루션을 구축했습니다." [S1]

- 업종·규모: "그들은 기술 사업, 특히 하드웨어 사업을 하고 있어요. 그리고 그들은 대규모 판매자 기반을 가지고 있는데, 2,000명에 달하는 영업 사원들이 직면한 가장 큰 과제 중 하나는 정보를 수집하는 시스템이 매우 다양하다는 점입니다." [S1] → 영업 인력 **2,000명** [S1].
- before 상태(수작업 통합): "그들은 그것을 꿰매야 합니다 . 그들이 하는 방식에는 공통점이 전혀 없습니다 ." [S1]
- before 상태(표준화 실패의 원인): "정보는 있지만 분산되어 있고 자동화 시스템이 없기 때문에 표준화된 프로세스를 시행하기가 매우 어렵습니다 ." [S1]
- 시스템 수: "하루에 필요한 30개, 40개, 50개의 시스템을 일일이 살펴볼 필요 없이, 필요한 정보가 이미 모두 수집되어 정리되어 있는 것입니다 ." [S1] → **30~50개 시스템** [S1]. 단, 이 문장은 after(목표 상태) 서술 안에 등장하며, before의 실측치라고 명시되지는 않았다.

**(2) 송장 관리** — 조직이 특정되지 않는다. 원문은 "예를 하나 더 들어드리겠습니다 . 우리는 송장 관리 솔루션을 도입하여 프로세스의 92%를 자동화했습니다 ." [S1]

- **92%의 주체 판정(정직한 서술)**: [S1] 본문만으로는 **판정 불가**하다. 근거는 다음 세 가지다. ① 앞 사례는 "저희는 고객사 중 한 곳을 위해"라고 고객사를 명시했으나, 송장 사례는 『우리는 … 도입하여』로만 서술되고 고객사 지칭이 사라진다 [S1]. ② 그러나 이 답변 전체를 유도한 질문이 "인공지능 에이전트 기능이 실질적인 비즈니스 가치를 창출한 시나리오를 공유해 주시겠습니까? 고객이나 업계와 관련된 이야기일 수도 있습니다." [S1] 여서, 고객 사례 열거 맥락일 개연성이 있다. ③ 자막이 한국어 기계번역이라 영어 원문의 "we"가 Deloitte 자사인지 "we built for a client"의 축약인지 복원할 수 없다. → **『Deloitte 자사분인지 고객사분인지 해당 소스에서 확인 불가』**로 표기해야 하며, 어느 쪽으로도 단정하면 안 된다.
- before 수치(송장 처리량·건수·인원·리드타임): **해당 소스에 없음.** [S1]에는 92%/8% 배분 외의 송장 관련 수치가 전혀 없다.

**(3) 시점 맥락** — [S1] 시점의 성숙도는 발화자 스스로 초기라고 규정한다: "2025년은 에이전트형 AI에 있어 중요한 해가 될 것으로 예상되지만, 아직은 초기 단계라고 생각합니다." [S1] (업로드일 2025-10-15)

---

### 7.3 자동화 구간 (AUTO)

**(a) 송장 관리 프로세스의 92%.**
"우리는 송장 관리 솔루션을 도입하여 프로세스의 92%를 자동화했습니다 . 92%입니다. 10% 개선이 아니라 20% 개선입니다. 전체 프로세스가 이제 92% 자동화되었습니다. 그리고 8%는 실제로 예외 상황이나 다른 이유로 사람의 개입이 필요한 상황을 처리해야 할 때입니다." [S1]
→ AUTO의 경계가 **『예외 아닌 것 전부』**로 설정돼 있다. 인간은 잔여 8%의 예외 처리로 밀려난다. (자막의 "10% 개선이 아니라 20% 개선입니다"는 문맥상 『10%나 20% 개선이 아니라』의 오역으로 보이나, **추정이므로 인용 시 원문 그대로 두고 해석을 덧붙이지 말 것**.)

**(b) 프로세스 재설계의 기본 전제 자체가 완전자동화.**
"그리고 그렇게 할 때, 우리는 프로세스가 완전히 자동화되거나 그에 가까운 방식으로 이루어질 것이라고 가정하고 재설계에 대해 이야기하는 것입니다." [S1]
→ 자동화가 사후 결과가 아니라 **설계 시작점의 가정**으로 놓인다.

**(c) 야간 무인 실행(백그라운드 자동화).**
"봇이 제가 자는 동안 밤새도록 쉴 새 없이 일하면서 이 모든 정보를 수집하고, 종합하고 , 분석하고, 여러 곳에서 정보를 가져와서 제가 그날 고객이나 클라이언트의 행동에 필요한 준비를 마쳤다는 겁니다 ." [S1]
→ 정보 수집·종합·분석 구간은 인간 부재 상태로 돌아간다.

**(d) 자동화의 표적 선택 기준: 하기 싫은 행정 업무.**
"궁극적으로 기회가 있는 영역들을 살펴보면, 우리가 실제로 하기 싫어하는 일들, 즉 가장 행정적인 부분들이 바로 그런 영역들입니다." [S1]

---

### 7.4 증강 구간 (AUG)

**(a) 인간의 잔여 역할이 명시적으로 정의된다 — 설계·재구상·개입·관리.**
"인간의 역할은 이 프로세스를 설계하거나 재구상하고 개입하여 에이전트가 실행하는 프로세스를 기본적으로 관리하는 것입니다." [S1]

**(b) 영업 에이전트: 70%에서 인간에게 넘긴다.**
"그리고 사업 계획서(피치 덱)도 70% 정도 완성된 상태입니다. 그러니까, 이제 세밀하게 조정할 수 있는 훌륭한 덱이 생겼네요 ." [S1]
→ **완성도 70%가 인간-기계 인계선**이다. 나머지 30%(맞춤화·조정)는 인간 영업사원 몫으로 남는다.

**(c) 증강의 목적이 판매자 역량 강화로 진술된다.**
"그래서 우리는 판매자를 지원 하고 역량을 강화하기 위해 자동화된 프레임워크, 즉 에이전트 구조를 활용하는 아이디어를 떠올렸습니다." [S1]
→ 동일 문장 안에 "자동화된 프레임워크"와 "지원·역량 강화"가 공존한다. 자동화 수단 / 증강 목적의 결합.

**(d) 맞춤 제안은 인간이 수행.**
"그리고 자사 제품에 대한 정보든, 경쟁사 제품 및 경쟁 정보에 대한 정보든, 잠재 고객의 시장 상황에 대한 정보든, 모든 중요한 정보를 활용하여 맞춤형 제안을 할 수 있습니다 ." [S1]

**(e) 프론트오피스는 애초에 증강 영역으로 분류된다.**
"영업과 마케팅은 당연히 창의성과 인간적인 상호작용 등이 필요하죠. 따라서 영업 담당자들이 훨씬 더 효과적으로 판매할 수 있도록 어떤 수준의 AI 비서를 제공할 수 있을까요?" [S1]

**(f) 통합 프레임 자체가 증강 서사로 제시된다.**
"그래서 시대의 흐름은 인간과 기계를 하나로 통합하는 것입니다." [S1] / "Deote에서는 '폭의 시대'에 대해 이야기합니다 ." [S1] (각주 b, e)
그리고 이 프레임은 대체 불안에 대한 응답으로 제시된다: "음, 시장에 불안감이 있는 것 같고, 어느 정도는 정당한 불안감이라고 생각합니다 . 사람들은 자동화, 에이전트, 봇에 대한 이야기를 계속 듣다 보니 우리가 대체될지도 모른다는 인식이 생깁니다." [S1]

---

### 7.5 전환 메커니즘 (CYCLE)

이 사례의 최대 강점 구간이다. 전환 기준이 **비유·조건·되돌림 규칙**의 세 층으로 진술된다.

**(a) 자율성 4단계론(자동차 비유).**
1단계 수동운전: "20~30년 전만 해도 사람들은 직접 차를 운전했고, 차가 스스로 달리는 일은 없었습니다." [S1]
2단계 크루즈컨트롤: "그러다가 어느 시점에 버튼을 누르면 크루즈 컨트롤 모드로 전환되는 기능이 생겼습니다." [S1]
3단계 차선이탈경고(제안만 함): "그리고 다음 단계의 자율 주행은 차가 우리에게 신호를 보내기 시작할 때 이루어집니다. 이봐요, 당신이 차선을 조금 벗어난 것 같네요. 하지만 이건 제안에 가깝습니다." [S1]
4단계 로보택시: "자, 이제 우리는 로보택시에 대해 이야기하고 있는 거죠? 1015년 후로 시간을 되돌려 봅시다." [S1] (자막의 "1015년"은 "10~15년"의 오인식으로 보이나 **원문 그대로 인용**할 것)

**(b) 전환의 종착점과 조건.**
"제가 말씀드리고 싶은 요점은, 챗봇에게 질문을 하는 단계에서 시작하여, 궁극적으로는 챗봇이 전체 비즈니스 프로세스를 운영하고 필요한 경우에만 사람의 개입이 이루어지는 단계로 발전할 것이라는 점입니다 ." [S1]

**(c) 통제 장치 선(先)설치 → 신뢰 축적 → 통제 일부 회수(되돌리기).**
"하지만 그러한 수준의 자율성을 확보하려면 모든 단계에 걸쳐 통제 장치를 마련해야 합니다. 그리고 시간이 지나면서 시스템의 성능, 안정성, 신뢰성에 대한 확신이 생기면 이러한 제어 기능 중 일부는 시간이 지남에 따라 되돌려지거나 형태가 바뀔 수도 있다고 생각합니다." [S1]
→ 전환 기준 = **성능·안정성·신뢰성에 대한 확신 축적**. 전환 방식 = 통제 장치를 먼저 전 단계에 깔고, 신뢰가 쌓인 만큼 사후적으로 제거·변형.

**(d) 시작점의 원칙: 무신뢰(zero-trust) 출발.**
"우리는 그들을 첫날부터 신뢰할 수 없습니다 . 아직 확실한 증거가 없습니다." [S1]
"챗봇 하나만 있어도 실수를 할 수 있는데, 다섯 개를 연결하면 그 위험성도 커지죠." [S1]
"따라서 이러한 시스템을 설계할 때는 모든 단계에서 적절한 통제 시스템을 구축해야 합니다." [S1]

**(e) 전환 속도에 대한 자기 제한.**
"완전 자율 주행 시대가 곧 도래할 것 같지도 않다 . 우리는 한 단계씩 차근차근 나아가야 합니다. 이러한 투자 에서 적절한 수익을 얻고 있는지 확인해야 합니다 ." [S1]
"저는 앞으로 2~3년 안에 말씀하신 바로 그 방향으로 점진적인 변화가 일어날 것이라고 생각합니다. 하지만 앞서 말씀드린 것처럼, 매우 통제된 방식으로 진행되어야 하며, 우리는 통제 시스템을 구축하고 진행하면서 신뢰를 얻어야 합니다." [S1]

**(f) 증강 회귀(reversal to augmentation)의 명시적 사례는?**
[S1]에는 『이미 자동화한 과업을 조건 변화로 인해 다시 인간에게 되돌렸다』는 **실제 사례가 없다**. (c)의 "되돌려지거나"는 *통제 장치*를 되돌린다는 뜻이지 *과업*을 인간에게 되돌린다는 뜻이 아니다. 이 구분을 흐리면 오독이 된다. → **증강 회귀 실사례: 해당 소스에 없음.**

**(g) 대조 — [S2]에는 전환이 데모 안에서 실연된다.**
"These assistants can be triggered by humans, or be system triggered with humans in the loop, or set up to run autonomously, collaborating across multiple assistants. Once you have built the right trust and confidence." [S2]
그리고 승인 1회가 곧바로 규칙으로 굳는 장면: "I'll take care of that right away. All right. Thank you for confirming. I will speed up the shipment of this order and add a new rule for top tier customers to my memory, so I don't need to interrupt you again for comparable cases." [S2]
→ [S1]이 『신뢰가 쌓이면』이라고 **원칙**으로 말한 것을, [S2]는 『인간 승인 1건 → 메모리에 규칙 추가 → 다음부터 중단하지 않음』이라는 **1회 학습 기반 자동 승격**으로 보여준다. 단, [S2]는 벤더 무대 데모이며 실제 운영 데이터가 아니다.

---

### 7.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

**SPILL(한 과업 자동화 → 인접 과업 증강 유발)**

- **부분적으로 있음(간접).** [S1] 영업 에이전트는 정보 수집·정리·이메일 초안·일정·문서·피치덱 초안까지 자동화한 결과, 인접 과업인 『맞춤형 제안』과 『덱 미세조정』에 인간 노동이 재배치된다: "누구에게 연락해야 할지 알잖아요. 당신은 후속 조치를 취해야 할 사항을 알고 있습니다. 이메일 작성이 완료되었습니다. 회의 일정이 잡혔습니다. 준비 서류가 준비되었습니다. 그리고 사업 계획서(피치 덱)도 70% 정도 완성된 상태입니다." [S1]
- **성과지표 파급(측정 과업으로의 파급).** 이 사례에서 가장 뚜렷한 파급은 인접 *실행* 과업이 아니라 인접 *측정* 과업이다: "있잖아요, 제가 질문 하나 드려도 될까요? 음, 만약 송장 관리 프로세스의 92%를 자동화할 수 있다면, 예를 들어 송장 처리 속도와 같은 관련 지표는 이전과 같을까요? AI가 소프트웨어 개발의 상당 부분을 수행할 수 있다면 프로젝트 완료에 몇 주가 걸릴까요, 아니면 몇 시간밖에 걸리지 않을까요?" [S1] → 자동화가 **성과 지표 자체의 재설계**라는 인간 과업을 새로 만들어낸다.
- **조직 파급.** "이는 IT 책임자가 배포해야 할 기술적 해결책이 아닙니다 . 온 마을이 힘을 합쳐야 할 거예요. 많은 기업 업무 프로세스가 조직 전체에 걸쳐 이루어집니다." [S1]
- 단, 『송장 92% 자동화 때문에 어떤 인접 과업의 인간 개입이 늘었다』는 **직접적 인과 진술은 해당 소스에 없음.**

**REINV(자동화로 확보한 자원을 증강에 재투자)**

- **[S1]에는 자원 재투자의 명시적 근거가 없다.** 절감된 인원·시간·비용을 어디에 재배치했는지에 대한 서술이 없다. 가장 근접한 문장은 서비스 커버리지 확대 *가능성*을 묻는 수사적 질문뿐이다: "우리가 모든 고객에게 훨씬 더 효과적으로 서비스를 제공할 수 있도록 인적 자원을 확충할 수 있을까요?" [S1] — 이는 실행된 재투자가 아니라 **질문 형태의 가능성 제시**다. → **REINV(실행 근거): 해당 소스에 없음.**
- **역량 재투자(인적 자본 쪽)는 있음.** "그러므로 리더십을 교육해야 하고, 전체 직원들의 역량을 향상시켜야 하며, 사람들에게 실험할 기회를 제공해야 합니다." [S1] / "그리고 두 번째로, 저는 조직 전체의 역량을 강화하는 것이 정말 중요하다고 생각합니다. 왜냐하면 이러한 능동형 AI 비전을 실현하기 위해서는 기술 전문가 혼자서는 해낼 수 없기 때문입니다 ." [S1] → 자동화 잉여의 재투자가 아니라 **선행 투자**에 가깝다. UBS 패턴(p.201)과는 방향이 다르다.

**보조 사례 — [S2] SAP Sapphire 2026 무대의 Deloitte 자체 도입분** (별개 조직·별개 시점, 업로드일 2026-05-20)
[S2]의 Deloitte 등장은 단순 파트너 언급이 **아니다**. 글로벌 CTO가 자사 도입 수치를 직접 진술한다.
- "We also adopted Joule for Consultants last year to give our global workforce a smarter way to deliver everyday consulting tasks, and today, thousands of our Deloitte consultants globally are using Jolule for Consultants for everyday tasks, and results speak for itself. 83% of them have experienced a positive impact on their daily work and save up to 30% of their time, allowing them to deliver a better outcome for our clients." [S2] (자막 오기 "Jolule" = Joule)
- "We have built more than 78 agents specific to industries and process areas, and we are innovating more with Business AI Platform." [S2]
- "In fact, we have established an AI center of excellence here in Europe to accelerate that option of our clients AI journey." [S2] (자막 "that option" = 『the adoption』의 오인식으로 추정)
- 증강 명제: "So as a team, Joule and our consultants at Deloitte now turn tech and process know-how into agents running your business, AI and experts working together for an impact that matters." [S2]
- 코딩 없는 구축: "and I can build agents for my clients without even writing a single line of code" [S2] / "This is a clear blueprint that used to take weeks, and we now have it in minutes, so I can even adjust it if needed." [S2]
- Deloitte는 SAP Industry AI의 **고객 명단**에도 오른다: "delivering value for customers like CHS, Roche, Deloitte, Vestas and many, many more already now, the initial feedback has been phenomenal." [S2]
→ 이 보조 사례는 [S1]의 송장/영업 사례와 **연결 근거가 전혀 없다**. 같은 회사라는 것 외에 공통점을 주장해서는 안 된다.

---

### 7.7 통합 장치 (RESP)

**[S1]** — 책임·승인·감사 구조가 **원칙 수준으로만** 존재하고, 구체적 장치(승인 워크플로, 감사로그, 역할 정의, 위원회)는 서술되지 않는다.
- 진행자의 질문 자체가 거버넌스를 겨냥한다: "이러한 주체들이 결정을 내릴 때 어떻게 신뢰를 확보하고 정부의 책임성을 보장할 수 있을까요 ?" [S1] (각주 d)
- 답변의 핵심: "따라서 이러한 시스템을 설계할 때는 모든 단계에서 적절한 통제 시스템을 구축해야 합니다." [S1]
- 인간의 프로세스 보유권: "인간의 역할은 이 프로세스를 설계하거나 재구상하고 개입하여 에이전트가 실행하는 프로세스를 기본적으로 관리하는 것입니다." [S1]
- 양방향 신뢰: "그리고 궁극적으로 양측 모두, 즉 저희에게는 기업 고객이 있고 그들에게는 또 다른 고객이 있는데, 이러한 신뢰는 양측 모두에서 구축되어야 합니다 ." [S1]
- **감사추적(audit trail)·승인권자·책임 귀속에 관한 구체 장치: 해당 소스에 없음.**

**[S2]** — 대조적으로 통합 장치가 구체적이다(단, 전부 **SAP 벤더 자체 발표**이며 Deloitte 사례가 아니다).
- "The Autonomous Suite is role-centric with a Joule Assistant for every persona in your company, always with the human in the loop." [S2]
- "It's audit ready. We provide full traceability for every action performed by an agent with the highest compliance standards" [S2]
- "we follow a SOX ordered, compatible, ISO certified development process to build these agents" [S2] (자막 "SOX ordered" = 『SOX-audited』류의 오인식으로 추정)
- 실행 게이트: "It's very important because we are making sure that only verified agents get executed in the runtime." [S2]
- 인간 승인 유보 지점: "And the agent is not automatically doing that, right, because that is of course, critical and also for the business decision." [S2]
- 승인 임계값: "each with the confidence level that's been set by my team. This professional services accrual is just below my confidence, confidence threshold. I click Approve and the system remembers." [S2]

**[S3]** — 같은 Deloitte 소속 발화자가 **정반대 방향의 RESP 논지**를 편다. 인간 통제는 필수지만 인간 개입(in-the-loop)은 필수가 아니라는 주장이다.
- "하지만 동시에 인간의 통제가 필요하다는 점을 인식해야 하지만, 반드시 인간이 개입해야 한다는 의미는 아닙니다 ." [S3]
- "앞으로 몇 년 안에 인간의 개입 없이 작동하는 자율 시스템이 점점 더 많아질 것이라고 생각합니다. 다만, 목표 설정, 행동 방식 등은 인간이 제어하고 , 임무 성공 여부에 따라 시스템을 비활성화하는 제어 기능을 갖추게 될 것입니다 ." [S3]
- 규범 공백 지적: "하지만 전장에서 AI를 사용하는 데에는 이와 유사한 선택지, 유사한 매뉴얼, 유사한 지침이 없습니다 ." [S3]
- 제3자 보증 역할: "저희는 국방부(MOD) 의 AI 보증 파트너로서 협력하고 있으며" [S3]

---

### 7.8 성과 수치

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 송장 관리 프로세스 자동화율 | 해당 소스에 없음 | 92% ("전체 프로세스가 이제 92% 자동화되었습니다.") | [S1] | **벤더/컨설팅사 자체보고**(Deloitte 측 발화자 구술). 제3자 검증 없음. 측정 방법·기간·모수 미제시 |
| 송장 프로세스 인간 개입 비율 | 해당 소스에 없음 | 8% ("8%는 실제로 예외 상황이나 다른 이유로 사람의 개입이 필요한 상황") | [S1] | 동일(자체보고) |
| 영업 인력 규모 | 2,000명 | (변동 서술 없음) | [S1] | 자체보고. 인력 증감 효과는 서술되지 않음 |
| 영업사원이 조회해야 하던 시스템 수 | "30개, 40개, 50개" | 조회 불필요("일일이 살펴볼 필요 없이") | [S1] | 자체보고. 이 수치는 after 서술문 안에 등장하므로 before 실측치로 단정 불가 |
| 피치덱 완성도(에이전트 산출 기준) | 해당 소스에 없음 | 70% ("사업 계획서(피치 덱)도 70% 정도 완성된 상태") | [S1] | 자체보고. 완성도 측정 기준 미제시 |
| 송장 처리속도 등 프로세스 KPI | 해당 소스에 없음 | 해당 소스에 없음(오히려 "이전과 같을까요?"라고 지표 유효성 자체를 문제 삼음) | [S1] | — |
| ROI·비용절감액·FTE 절감 | 해당 소스에 없음 | 해당 소스에 없음 | [S1] | — |
| (보조) Joule for Consultants 긍정 영향 응답률 | 해당 소스에 없음 | 83% | [S2] | **Deloitte 자체보고**(SAP 무대 위 발언). 표본·설문방법 미제시 |
| (보조) Joule for Consultants 시간 절감 | 해당 소스에 없음 | "save up to 30% of their time"(최대치 표현) | [S2] | Deloitte 자체보고. "up to"이므로 평균치 아님 |
| (보조) Deloitte 구축 에이전트 수 | 해당 소스에 없음 | "more than 78 agents" | [S2] | Deloitte 자체보고 |
| (참고, Deloitte 아님) SAP Autonomous Suite 규모 | — | "224 agents and 51 assistants" | [S2] | SAP 자체발표 |
| (참고, Deloitte 아님) Sony 수작업 절감 | 4 days | 15 minutes | [S2] | SAP가 전한 고객 사례(제3자 검증 아님) |
| (참고, Deloitte 아님) Invoice Assistant 문의 처리 | 30 minutes | 2 minutes / AP backlog −25% | [S2] | SAP 고객 영상 증언(발화자 미상, 자체보고) |
| (참고) AI 파일럿 실패율 | — | 80% ("다들 아시다시피 AI 파일럿의 80%가 실패했죠.") | [S3] | 진행자(Oracle 측) 발언, 출처 미제시. **제3자 검증치로 인용 금지** |
| (참고) AI의 취약점 탐색 | 전문가 20시간 | "20 ~30분", 성공률 "10번 중 3번" | [S3] | 발화자가 "AI 보안 연구소(AI Security Institute) 연구"로 귀속. **인용된 제3자 연구**이나 원문 확인 불가 |

---

### 7.9 소스 간 교차 대조

**반복 확인된 사실(2개 이상 소스에서 같은 방향)**
1. **인간을 루프에 남긴다는 원칙**은 세 소스 모두에 있다. [S1] "인간의 역할은 이 프로세스를 설계하거나 재구상하고 개입하여 에이전트가 실행하는 프로세스를 기본적으로 관리하는 것입니다." / [S2] "always with the human in the loop" / [S3] "기업에서 AI를 이야기할 때 항상 쓰는 표현 중에 ' 인간 개입'이라는 말이 있죠 ."를 둘러싼 논쟁 자체가 인터뷰의 한 축.
2. **신뢰 축적이 자율성의 선행조건**이라는 논리도 반복된다. [S1] "우리는 그들을 첫날부터 신뢰할 수 없습니다 ." / [S2] "Once you have built the right trust and confidence."
3. **AI 도입은 IT 부서 단독 과제가 아니다**라는 명제가 [S1]과 [S3]에 독립적으로 등장한다. [S1] "이는 IT 책임자가 배포해야 할 기술적 해결책이 아닙니다 ." / [S3] "CIO를 통해 AI를 도입하는 조직은 대부분 80%의 실패율을 경험하고 있을 겁니다." + "AI를 연구실이나 기술팀에만 머물러 있게 해서는 확장할 수 없기 때문입니다."(진행자 발언)
4. **도메인 담당자의 문제 정의가 출발점**이라는 명제. [S1] "비즈니스 프로세스를 이해하는 누군가가 " 이제 이 기술이 있으니 이 일을 근본적으로 다르게 할 수 있겠어"라고 말할 수 있어야 합니다." / [S3] "해결해야 할 문제가 있어야 하고, 그 문제를 겪고 있는 사람이 문제를 이해하고 해결하는 데 도움을 주어야 합니다 ."

**한 소스에만 있는 사실**
- 송장 92%/8%, 영업 2,000명, 30~50개 시스템, 피치덱 70%, 자율성 4단계론, 통제 되돌리기, Talo ARPU 3~4달러, "수십 배, 심지어 한 자릿수" 규모 조언, "최종 사용자 채택"으로서의 확장 — **전부 [S1] 단독**. 다른 두 소스에 교차 확인되는 수치는 **하나도 없다**.
- 83% / 최대 30% 시간절감 / 78개 에이전트 / 유럽 AI CoE — **[S2] 단독**.
- 80% 파일럿 실패율, 신경다양성 순만족도, 제본스 역설, "차세대 지도자들은 이러한 학습 경험을 갖지 못할 것입니다" — **[S3] 단독**.

**시점에 따른 서술 변화(2025-10 → 2026-05 → 2026-06)**
- [S1](2025-10-15)은 "2025년은 에이전트형 AI에 있어 중요한 해가 될 것으로 예상되지만, 아직은 초기 단계라고 생각합니다."라며 **초기·실험 단계**로 규정하고, 확장 조언은 "제 생각에 규모 확장은 단순히 물량이나 숫자의 문제가 아닙니다 ."라며 **집중과 채택**을 강조한다.
- [S2](2026-05-20)에서 같은 회사(Deloitte)는 이미 "more than 78 agents"를 구축했고 "thousands of our Deloitte consultants globally"가 사용 중이라고 말한다. **[S1]의 "수십 배, 심지어 한 자릿수 정도가 적당할 것입니다 ."라는 규모 조언과 [S2]의 78개 에이전트는 표면적으로 긴장 관계다.** 다만 [S1]의 조언은 *동시에 추진할 프로세스 재설계 과제 수*를 말한 것으로 읽히고 [S2]의 78은 *누적 구축 에이전트 수*여서, 단위가 다르므로 **직접적 모순이라고 단정할 수 없다.** 이 유보를 반드시 함께 표기해야 한다.
- [S3](2026-06-18)은 자율 시스템 확산을 [S1]보다 훨씬 앞당겨 전망한다: "앞으로 몇 년 안에 인간의 개입 없이 작동하는 자율 시스템이 점점 더 많아질 것이라고 생각합니다."

**모순 / 긴장**
1. **인간 개입의 필요성에 대한 사내 견해차.** [S1]은 통제 장치를 전 단계에 깔고 신뢰가 쌓일 때만 일부를 되돌리는 보수적 노선이다. [S3]은 "그래서 저는 인간의 개입이 필요 없다고 말하는 것입니다 ."라고 말하며, 인간 개입 고수가 오히려 위험할 수 있다고 본다("만약 적이 AI를 이용해 더 빠르게 움직이고, 더 빠르게 생각하고, 우리 병사들에게 피해를 입히고, 더 효율적이고 효과적이며 신속하게 사살한다면, 우리는 인간의 생명을 희생하면서까지 인간을 개입시키는 것에 대해 사회적으로 만족할 수 있을까요?"). 두 발화자는 소속은 같지만 부문(TMT vs 국방)과 시점(2025-10 vs 2026-06)이 다르며, **동일 조직의 통일된 입장으로 인용해서는 안 된다.** [S3] 서두에는 소속기관 견해가 아니라는 면책 고지가 명시돼 있다.
2. **에이전틱(agentic)이라는 용어에 대한 태도 역전.** [S1]은 에이전트형 AI를 핵심 프레임으로 옹호한다. [S3]에서 같은 회사 파트너는 폐기하고 싶은 용어로 이를 지목한다: "어, 올해는 에이전트틱이에요. 능동적인." [S3] (자막 "에이전트틱" = agentic)
3. **자동화의 학습 효과에 대한 반대 방향.** [S1]은 자동화가 "우리가 실제로 하기 싫어하는 일들"을 걷어낸다고 본다. [S3]은 바로 그 지점의 부작용을 지적한다: "우리는 AI를 이용해 모든 쉬운 일들을 처리하게 될 것입니다. 우리와 같은 사람들이 배우고 실패하고 다시는 하고 싶지 않은 일들이 자동화될 것입니다. 따라서 차세대 지도자들은 이러한 학습 경험을 갖지 못할 것입니다." [S3]
4. **성과 측정 방식에 대한 공통 회의, 다른 결론.** [S1]은 자동화가 기존 KPI를 무의미하게 만든다고 본다. [S3]은 ROI 산정 자체가 개인화되어 집계가 불가능해진다고 본다: "네. 그리고 훨씬 쉽게 정량화할 수 있죠, 그렇죠? 하지만 그걸 종합하면 훨씬 어려워집니다."

---

### 7.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간 루프 제외 (p.194) | 송장 프로세스 92% 자동화, 인간은 8% 예외만 [S1]; 야간 무인 정보 수집·종합·분석 [S1] | **지지**. 단 자체보고 수치 1건에 의존 |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | 피치덱 70% 지점 인계, 나머지 조정·맞춤 제안은 인간 [S1]; "인간의 역할은 이 프로세스를 설계하거나 재구상하고 개입하여 에이전트가 실행하는 프로세스를 기본적으로 관리하는 것입니다." [S1] | **지지 + 보강**. 인계선을 **완성도 백분율(70%)**로 명시한 드문 사례 |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | 자율성 4단계론(수동→크루즈컨트롤→차선이탈경고→로보택시) [S1]; "시스템의 성능, 안정성, 신뢰성에 대한 확신이 생기면 이러한 제어 기능 중 일부는 시간이 지남에 따라 되돌려지거나" [S1] | **보강**. 논문의 시간축에 **단계별 통제 장치의 사후 제거**라는 구체 메커니즘을 덧붙임 |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 과업의 증강 회귀 실사례 없음. 되돌리는 대상은 과업이 아니라 통제 장치 [S1] | **반증 아님 / 미확인**. 해당 소스에 없음 |
| SPILL: 한 과업 자동화가 인접 과업 증강 유발 (p.197) | 자동화가 **성과지표 재설계**라는 새 인간 과업을 낳음: "송장 처리 속도와 같은 관련 지표는 이전과 같을까요?" [S1]; "온 마을이 힘을 합쳐야 할 거예요." [S1] | **확장**. 파급 대상이 인접 *실행* 과업이 아니라 인접 *측정·거버넌스* 과업 |
| REINV: 자동화 자원의 증강 재투자, UBS 패턴 (p.201) | 실행된 재투자 근거 없음. 서비스 확대는 질문 형태의 가능성뿐 [S1] | **미확인**. 해당 소스에 없음 |
| RESP: 인간이 프로세스 전체 책임·승인·감사 보유 (p.200) | "인간의 역할은 이 프로세스를 설계하거나 재구상하고 개입하여 에이전트가 실행하는 프로세스를 기본적으로 관리하는 것입니다." [S1]; 구체 장치는 [S2]에만("full traceability for every action performed by an agent", "only verified agents get executed in the runtime") | **[S1] 원칙 수준 지지 / 장치 근거는 타 소스 의존**. [S3]은 "인간의 통제"와 "인간의 개입"을 분리하며 **부분 반증** |
| p.195 증강 학습은 도메인 전문가 암묵지 의존, IT/외부업체 위임 불가 | "이는 IT 책임자가 배포해야 할 기술적 해결책이 아닙니다 ." [S1]; "기술 전문가 혼자서는 해낼 수 없기 때문입니다 ." [S1]; [S3] "CIO를 통해 AI를 도입하는 조직은 대부분 80%의 실패율을 경험하고 있을 겁니다." | **강한 지지(2개 소스 독립 확인)**. 다만 **긴장점**: 이 사례의 화자들 자체가 외부 컨설팅사이며, [S2]에서는 Deloitte 컨설턴트가 고객사 에이전트를 대신 구축한다("I can build agents for my clients") — 위임 불가 명제와 실무의 충돌 |
| p.198 기계 한계 ① 목적/자아 부재 | 목적 설정·프로세스 재구상은 인간 몫으로 남음 [S1]; [S3] "목표 설정, 행동 방식 등은 인간이 제어하고" | **지지** |
| p.198 기계 한계 ② 제약 완화된 옵션만 제시 | Talo 일화: ARPU "3달러에서 4달러" 환경에서 "그래서 저는 다른 시장에서 더 많은 창의성을 발견하고 있습니다." [S1] — 제약이 해법의 질을 규정 | **확장**. 논문은 기계가 제약을 놓친다고 보는데, 이 사례는 **제약이 강한 조직일수록 AI 활용이 창의적**이라는 역상관을 제시 |
| p.198 기계 한계 ③ 훈련된 과업에 국한 | 챗봇/에이전트 오해 교정: "에이전트형 AI가 챗봇의 새로운 이름이 아니라는 점을 이해하는 것이 중요하다고 생각합니다 ." [S1] | **약한 지지** |
| p.198 기계 한계 ④ 감각/감정/사회기술 부재 | "영업과 마케팅은 당연히 창의성과 인간적인 상호작용 등이 필요하죠." [S1]; [S3] "여전히 많은 문제는 인공지능이 아닌 인간의 창의력으로 해결될 것이라고 생각합니다 ." | **지지** |
| p.199 한쪽 편중 시 악순환 | "제 생각엔 그들이 거의 스스로를 압도할 지경인 것 같아요."(과잉 실험) [S1]; [S3] 학습 경험 상실("차세대 지도자들은 이러한 학습 경험을 갖지 못할 것입니다") | **보강 + 확장**. 악순환의 새 경로: 자동화된 초급 과업이 곧 학습 사다리였다는 지적 |
| p.204 기계는 조직 내 새로운 행위자 계급 | "첫째는 우리가 디지털 인력을 보유하게 될 것이라는 점입니다." [S1] / "앞서 말씀드렸듯이 디지털 인력과 인간 인력이라는 두 가지 요소가 있습니다." [S1] | **강한 지지**. [S2]도 같은 방향("mapping your agents to SAP SuccessFactors in your org chart"—단, 이는 SAP 발표) |

**이 사례가 논문을 확장하는 지점.** 첫째, Raisch & Krakowski의 CYCLE은 증강과 자동화 사이의 이동을 서술하지만 *무엇을 근거로 언제 넘기는가*의 조작적 기준은 열어둔다. [S1]은 이를 두 개의 측정 가능한 표지로 대체한다 — 산출물 완성도 70%라는 **인계선**, 그리고 통제 장치를 전 단계에 먼저 설치한 뒤 신뢰가 쌓인 만큼 사후 제거한다는 **역방향 게이트 해제 규칙**("우리는 그들을 첫날부터 신뢰할 수 없습니다 ." [S1]). 둘째, SPILL의 파급 방향이 실행 과업이 아니라 측정 체계로 향한다: 92% 자동화가 곧 "송장 처리 속도와 같은 관련 지표는 이전과 같을까요?"라는 지표 재설계 과업을 인간에게 새로 부과한다 [S1] — 자동화가 인접 과업의 증강을 유발한다는 명제를, 자동화가 **성과 측정이라는 메타 과업의 증강**을 유발한다는 형태로 확장한다. 셋째, p.198의 기계 한계 논의를 조직 환경 쪽으로 뒤집는다. ARPU 3~4달러로 운영되는 통신사업자에서 제약이 창의성을 낳는다는 관찰([S1] Talo 일화)은, 증강-자동화 배분이 기술 성숙도가 아니라 **자원 제약의 함수**일 수 있음을 시사한다. 넷째, p.199의 악순환에 세대 간 경로를 더한다 — 같은 회사의 다른 발화자가 "우리와 같은 사람들이 배우고 실패하고 다시는 하고 싶지 않은 일들이 자동화될 것입니다. 따라서 차세대 지도자들은 이러한 학습 경험을 갖지 못할 것입니다." [S3]라고 말할 때, 자동화의 표적("우리가 실제로 하기 싫어하는 일들, 즉 가장 행정적인 부분들" [S1])이 곧 다음 세대의 암묵지 형성 경로였다는 문제가 드러난다.

---

### 7.11 인용 시 주의사항

1. **귀속.** 이 사례를 『Intel 사례』로 표기하면 오류다. Intel은 호스팅 채널이고, 발화자는 Deloitte TMT AI 글로벌 리더다 [S1]. 마찬가지로 [S3]을 『Oracle 사례』로 쓰면 오류이며, [S3] 서두에는 "발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다."라는 면책 고지가 있다 [S3].
2. **92%의 주체 미확정.** Deloitte 자사 프로세스인지 고객사 프로세스인지 [S1] 본문으로 판정할 수 없다(7.2 참조). 『Deloitte가 자사 송장의 92%를 자동화했다』고 쓰면 근거를 초과한다. 『Deloitte 측 발화자가 송장 관리 프로세스 92% 자동화 사례를 제시했다』가 안전한 표현이다.
3. **전부 자체보고.** [S1]·[S2]의 모든 수치는 발화 당사자의 구술이며, 제3자 검증·감사·독립 측정에 대한 언급이 없다. 측정 기간, 모수(송장 건수), 자동화의 정의(완전 무인인지 규칙 기반 처리 포함인지) 모두 미제시다. [S2]의 "save up to 30%"는 상한 표현이지 평균이 아니다.
4. **성숙도(계획 vs 운영) 구분.** [S1] 영업 에이전트는 진행 중 여정으로 서술된다: "저희는 이러한 여정을 시작했고, 궁극적으로 영업 담당자들이 아침에 노트북 앞에 앉아 커피를 마시며 하루를 시작하는 시나리오를 상상할 수 있도록 지원하는 것을 목표로 하고 있습니다." [S1] → **목표 상태 서술이며 완결된 운영 성과가 아니다.** 반면 송장 92%는 완료형("전체 프로세스가 이제 92% 자동화되었습니다.")이다. 두 사례의 성숙도를 같은 등급으로 취급하지 말 것. [S2]의 무대 데모는 라이브 데모이며 프로덕션 데이터가 아니다.
5. **자막 오류 목록(원문 그대로 인용하되 해석 주의).** 디오이트/디오테/Deote(=Deloitte), "폭의 시대"(=The Age of With), "정부의 책임성"(=governance 추정), "포르노 관련 해결책"(=point solutions 추정, [S1]에 2회), "에닉"·"Agenti"·"Gent AI"(=agentic 계열), "1015년 후로"(=10~15년 추정), "아르푸(arpoo)"·"탈쿠(talcu)"(=ARPU), "탈로(Talo)"(회사명 오인식 가능성), "10% 개선이 아니라 20% 개선입니다"(=not a 10% or 20% improvement 추정), "세대 인공지능"(=generative AI 추정), "बिल्कुल"(힌디어 문자열 혼입), [S2]의 "Jolule"(=Joule)·"that option"(=the adoption 추정)·"SOX ordered"(=SOX-audited 추정), [S3]의 "에이전트틱". **괄호 안 해석은 모두 추정이며 소스가 확인해주지 않는다.**
6. **Talo 수치의 불안정성.** ARPU는 자막에서 "30~34달러"로 잘못 들은 뒤 "3달러에서 4달러"로 정정되는 대화 형태로 등장한다 [S1]. 정정된 값(3~4달러)만 인용하고, 회사명은 자막 표기가 불확실하므로 『자막상 "탈로(Talo)"로 표기된 중동·아프리카 16개국 통신사업자』로 쓰는 것이 안전하다.
7. **[S2]·[S3]을 [S1] 사례의 증거로 쓰지 말 것.** 세 소스는 Deloitte라는 공통점 외에 부문·지역·시점·주제가 모두 다르다. 특히 [S2]의 78개 에이전트를 [S1]의 송장/영업 사례의 후속 성과로 연결할 근거는 **어느 소스에도 없다**.
8. **[S3]의 80% 실패율은 인용 금지 수준.** 진행자가 "다들 아시다시피 AI 파일럿의 80%가 실패했죠."라고 출처 없이 말하고 게스트가 동조하는 형태다 [S3]. 통계로 재인용하면 안 된다.
9. **REINV 부재를 채워 넣지 말 것.** 자동화로 확보한 자원의 재투자 근거는 [S1]에 없다. 논문의 UBS 패턴과 억지로 맞추려는 서술은 근거 초과다.


---



## 사례 8 — Nokia : 제로터치 네트워크 + NOC 전문가

*원문: `docs/cases/07_nokia.md`*


### 8.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 구분 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Nokia | **업로드일 2026-04-17** (채널 수집분, 파일 헤더 "업로드일") | ko | 약 338개 | 내레이션 단독. Nokia Managed Services 제품 소개 영상(광고성). 발화자 명시 없음 | https://www.youtube.com/watch?v=fmsEHuUJmPQ | `/home/user/youtube-scrap/transcripts/channels/Nokia/AI-driven_and_automated_Nokia_Managed_Services__fmsEHuUJmPQ.md` |
| [S2] | Nokia | **업로드일 2026-04-21** (채널 수집분) | ko | 약 3387개 | 사내 팟캐스트 "노키아 5G 토크". 진행자 그렉(자동화 솔루션 설계자), 게스트 티모 라즐로(제품 책임자 겸 연구 개발 관리자), 아틸라 헤기(자동화 설계자) | https://www.youtube.com/watch?v=w1SfoW8SXgQ | `/home/user/youtube-scrap/transcripts/channels/Nokia/The_Evolution_to_a_Fully_Automated_Network_Part_I__w1SfoW8SXgQ.md` |
| [S3] | Nokia | **업로드일 2026-04-21** (채널 수집분) | ko | 약 2926개 | 위 팟캐스트 Part II. 동일 3인(단, 자막에서 테무로 표기 변동) | https://www.youtube.com/watch?v=IaqO4MXSiP4 | `/home/user/youtube-scrap/transcripts/channels/Nokia/The_Evolution_to_a_Fully_Automated_Network_Part_II__IaqO4MXSiP4.md` |
| [S4] | Nokia | **업로드일 2026-04-21** (채널 수집분) | ko | 약 2522개 | 팟캐스트 "SaaS Talks". 진행자 노르베르트 타발리(SaaS DevOps 엔지니어링 매니저), 게스트 졸탄 몰나르(핵심 SaaS 수석 아키텍트), 가보르 파프(SaaS 자동화 아키텍트) | https://www.youtube.com/watch?v=u4OXW5uhzWw | `/home/user/youtube-scrap/transcripts/channels/Nokia/SaaS_Talks_–_Beyond_Connectivity_Part_I__u4OXW5uhzWw.md` |
| [S5] | Nokia | **업로드일 2026-04-21** (채널 수집분) | ko | 약 4233개 | 위 팟캐스트 Part II. 동일 3인(자막에서 게스트가 모모/모미르/졸타로 혼용 표기) | https://www.youtube.com/watch?v=DkFHM1PZ6fI | `/home/user/youtube-scrap/transcripts/channels/Nokia/Saas_Talks_–_Beyond_Connectivity_Part_II__DkFHM1PZ6fI.md` |
| [S6] | Nokia | **업로드일 2026-05-26** (채널 수집분) | ko | 약 976개 | Nokia Core Talk 대담. 호스트 마르셀로 마드루가(노키아 핵심 네트워크 기술 및 플랫폼 총괄), 게스트 토마스 비하크(Deutsche Telekom TDI 자동화 플랫폼 책임자) | https://www.youtube.com/watch?v=h179sfOi5xk | `/home/user/youtube-scrap/transcripts/channels/Nokia/AI,_GitOps,_and_the_new_core_DT's_road_to_autonomy__h179sfOi5xk.md` |
| [S7] | Nokia | **업로드일 2026-06-22** (채널 수집분) | ko | 약 1656개 | 대담 시리즈 "Networked". Nokia 측 진행자(라구/라가브로 혼용 표기), 게스트 존(T-Mobile) | https://www.youtube.com/watch?v=ABdfqQZlGDU | `/home/user/youtube-scrap/transcripts/channels/Nokia/Networked_The_rise_of_the_three_As_AI,_Automation_and_API_ex__ABdfqQZlGDU.md` |

각 소스의 역할:

- **[S1] 1차 근거(단, 벤더 마케팅)** — 이 사례의 핵심 주장(제로 터치 네트워크, 제로 아이볼 운영, NOC 전문가 설계, TM 포럼 4단계, 6개 성과 수치)이 전부 여기 한 곳에 집중돼 있다. 동시에 338단어 제품 광고라 검증 가능한 세부가 없다.
- **[S2] 1차 근거(실무자 서술)** — 자동화 계층 구조, 의도(intent) 기반 운영, 폐쇄 루프, 「인간을 어디에 남길 것인가」에 대한 엔지니어 자신의 서술. AUG/RESP의 주된 근거.
- **[S3] 1차 근거(전환 메커니즘)** — 증강→자동화 전환의 판단 기준("100번 정도 같은 결과"), 승인 요청 방식, 55명 조직 사례. CYCLE/REINV의 주된 근거.
- **[S4] 보강** — 배포 자동화의 before(수동 개입 필수) 상태와 "제로 터치 배포" 목표. AUTO 구간의 이력.
- **[S5] 보강 + SPILL 근거** — Core SaaS의 실제 운영, SRE의 잔여 역할, 코어 자동화가 인접 과업(관측, DNS, 스토리지, 에너지 효율)의 자체 개발을 유발한 서술.
- **[S6] 대조군(고객사 = Deutsche Telekom 관점)** — 벤더가 아닌 통신사 측 자동화 책임자가 성숙도와 인간 잔여 역할을 직접 서술. S1의 벤더 자기서술을 대조할 수 있는 유일한 소스.
- **[S7] 대조군(고객사 = T-Mobile 관점)** — "제로 터치 프로비저닝", 자가 복구를 통신사 측이 어떻게 말하는지. 유일한 제3자 발화 정량 사례(허리케인 밀턴).

> **시점 주의**: 7개 소스 전부 채널 수집분이므로 표의 날짜는 **영상 업로드일**이다(키워드 수집분이 아니므로 수집일 문제는 없음). 단 [S2]~[S5] 4건은 모두 2026-04-21로 동일 업로드일이며, 팟캐스트 **녹음 시점**은 어느 파일에도 없다. 따라서 「2026-04-21 현재의 상태」라고 단정할 수 없고 「2026-04-21에 공개된 서술」까지만 말할 수 있다.

---

### 8.2 조직과 문제 상황

이 사례의 "조직"은 단일 기업이 아니라 **Nokia(벤더)와 그 통신사 고객들**의 이중 구조다. 소스마다 관찰 대상이 다르므로 분리해 기술한다.

**(a) Nokia가 서술한 산업 전반의 before 상태 [S1]**

> "현대 네트워크는 서로 다른 도구들 간의 시너지 부족으로 점점 더 복잡해지고 있으며, 이로 인해 시스템을 효율적으로 관리하기 어렵고 투자 대비 실질적인 수익을 달성하기는 더욱 어려워지고 있습니다." [S1]

> "에너지 소비량은 증가하고 있고, 자동화는 아직 널리 보급되지 않았으며, 직원들의 기술 역량은 미래 기술과 항상 일치하는 것은 아닙니다" [S1]

**(b) 통신 산업의 제약 조건 [S2]**

> "우리가 반드시 지켜야 하는 특별한 규칙 , 99.999%의 가용성입니다" [S2]
> "즉, 10만 번의 통화 중 단 한 번만 실패할 수 있다는 뜻입니다." [S2]

멀티벤더 복잡성:

> "그러니 운영자 입장에서 다른 사람이 개발하고 여러 회사가 개발한 시스템을 운영해야 하고, 그것이 항상 정상적으로 작동하도록 보장해야 한다는 것이 얼마나 복잡한 일인지 짐작할 수 있을 것입니다" [S2]

**(c) 물량 — 코어 네트워크 배포 규모 [S4]**

| 항목 | 값 | 소스 |
|---|---|---|
| 통상적 통신사 구축에 포함되는 개별 네트워크 기능 수 | "12개 또는 15개의 개별 네트워크 기능" | [S4] |
| 필요 자원 | "수백 개의 VCPU와 수백 기가바이트의 메모리, 그리고 수백 개, 심지어 수천 개의 인터페이스" | [S4] |
| 네트워크 기능당 매개변수 | "네트워크 기능당 수십 개씩 있습니다" / "어떤 경우에는 1만 명에 달할 수도 있습니다"(문맥상 1만 **개** 매개변수의 오역으로 보임) | [S4] |
| 온프레미스 구축 소요 기간 | "일반적인 온프레미스 구축에는 몇 달 또는 심지어 1년이 걸린다" | [S4] |
| 투입 인원 | "수백 명의 엔지니어와 건축가가 참여하는 매우 거대한 프로젝트일 수도 있습니다" | [S4] |

**(d) 배포 자동화의 before 상태 [S4]**

> "그런데 이러한 워크플로우 기반 배포는 때때로 알 수 없는 이유로 중단되는 문제가 있었고, 그때마다 무엇이 잘못되었는지 수동으로 확인하고 처음부터 다시 시작해야 했습니다." [S4]
> "그래서 항상 수동 개입을 통해 과정을 완료해야 했습니다" [S4]

**(e) 고객사 규모 [S6][S7]**

- Deutsche Telekom: "우선 EU 시장에는 각기 다른 요구사항과 운영 모델을 가진 9개의 제품이 있습니다." [S6] — 문맥상 9개 EU 시장(국가 자회사)의 오역으로 읽히나, **원문 그대로는 9개의 제품**이다. 정확한 인원/가입자 규모는 해당 소스에 없음.
- T-Mobile: 가입자 수·인원 수치는 해당 소스에 없음. 정량 서술은 8.8 표 참조.
- Nokia 내부 조직 1건: "당시에는 엔지니어가 55명 정도 있었던 것으로 기억합니다" [S3] (검증팀 라인 관리자가 맡았던 조직).

---

### 8.3 자동화 구간 (AUTO)

**(1) 운영 프로세스 대부분의 기계 인계 — 벤더 주장 [S1]**

> "저희 관리형 서비스 [음악] AI/ML 플랫폼의 AI 기반 솔루션은 대부분의 운영 프로세스를 자동화하고, 높은 수준의 폐쇄 루프 및 도메인 간 자율성을 활용하여 자체 최적화, 자체 복구 및 위협으로부터 스스로를 보호하는 제로 터치 네트워크를 제공합니다" [S1]

여기서 **"제로 터치"의 정의**는 (i) 자체 최적화 (ii) 자체 복구 (iii) 위협 자기방어 — 세 자율 능력의 묶음으로 제시된다. 인간의 위치는 이 문장에 **명시되지 않는다.**

**제로 아이볼(zero-eyeball)의 정의** [S1]:

> "게다가 수동 KPI 추적을 엔드투엔드 모니터링으로 대체함으로써 여러 영역에 걸쳐 연관된 제로 아이볼 운영을 구축할 수 있을 뿐 아니라" [S1]

즉 제로 아이볼은 **수동 KPI 추적(사람의 눈)을 엔드투엔드 모니터링으로 대체**하는 것. 대체된 인간이 어디로 가는지는 [S1]에 없음.

**(2) 이상적 목표 상태 — "설정 후 신경 쓸 필요 없는" [S1]**

> "네트워크가 구축 및 자동화되어 사람의 개입이 최소화되는, 설정 후 신경 쓸 필요 없는 상태가 되는 것이 이상적입니다" [S1]

이 문장이 이 사례에서 **가장 강한 AUTO 선언**이다(인간을 루프에서 빼는 것을 명시적 이상으로 삼음).

**(3) 배포·수명주기의 자동화 [S4][S5][S6]**

> "쿠버네티스에 배포하기만 하면 쿠버네티스 자체의 오퍼레이터가 이 모든 정보를 처리하고 최종적으로 우리가 원하는 결과물을 만들어냅니다." [S4]

> "그리고 이 기능을 사용하면 각 CNF마다 수천 개의 매개변수를 하나씩 처리할 필요가 없으므로 코어 배포를 훨씬 간소화하고 속도를 높일 수 있습니다" [S4]

관측 도구의 자동 통합 [S5]:
> "자동 통합 기능이 있습니다. 따라서 코어가 시작되면 트리거만 제공하면 도구 자체가 배포된 네트워크 기능과 같은 새로운 배포를 자동으로 감지합니다." [S5]

Deutsche Telekom이 정의한 "급진적 자동화" [S6]:
> "저희에게 있어 급진적 자동화란 전체 수명 주기 자동화, 즉 프로비저닝, 업데이트, 오류 감지, 네트워크 기능 확장 등을 수동 작업 없이 자동화하는 것을 의미합니다." [S6]
> "단순히 티켓을 개설하는 것뿐만 아니라 이러한 티켓을 자동으로 해결해야 합니다." [S6]

**(4) 자가 복구 — 통신사 측 [S7]**

> "그리고 최우선 순위에는 종단 간 네트워크 오케스트레이션과 자가 복구 기능 같은 것들이 포함될 것입니다. 즉, 네트워크에 장애가 발생했을 때 사람의 개입 없이도 복구할 수 있도록 하는 것이죠." [S7]

> "저희는 이미 예를 들어 새로운 MVNO를 활성화하는 방식에서 제로 터치 프로비저닝과 같은 방식으로 이를 실천하기 시작했습니다." [S7]

---

### 8.4 증강 구간 (AUG)

**(1) 인간이 남는 첫 번째 자리 — 자동화 플랫폼의 설계자로서의 도메인 전문가 [S1]**

> "이 플랫폼은 노키아 관리형 서비스 제공의 기반이 되는 포괄적인 자동화 프레임워크로, 실제 통신 문제를 해결한 경험이 있는 글로벌 네트워크 운영 센터의 전문가들이 설계하고 강화했습니다" [S1]

이 문장이 과제에서 지목한, NOC 전문가가 플랫폼을 설계·강화했다는 서술의 원문이다. **[S2]~[S7] 어디에도 이 문장(또는 NOC 전문가에 의한 플랫폼 설계라는 주장)은 재확인되지 않는다.** 다만 기능적으로 대응하는 서술은 [S5]에 있다(아래 (3)).

**(2) 자동화가 아직 못 하는 자리 [S2]**

> "지금까지는 인간의 개입에 더 의존해 왔고, 여전히 이러한 작업을 직접 수행해야 하는 경우가 있습니다. 따라서 자동화가 아직 완벽한 해결책을 제공하지 못하는 경우가 분명히 존재합니다." [S2]

> "하지만 어쩌면 우리는 이것을 자동화 방향으로 전환하고, 이전보다 훨씬 높은 수준에서 필요한 개입 지점만 제공하는 방식을 시도해 볼 수 있을지도 모릅니다" [S2]

— 인간을 **제거**하는 것이 아니라 **개입 지점의 추상 수준을 올린다**는 서술. 논문 용어로는 자동화가 아니라 증강 재설계다.

**(3) SRE — 실제 운영의 잔여 인간 [S5]**

> "간단히 말해, GitOps 기반 접근 방식을 통해 핵심 서비스 배포를 실제로 담당하는 SRE(사이트 신뢰성 엔지니어)들이 서비스 배포에 대한 최종 미세 조정을 수행할 수 있도록 지원하는 것입니다." [S5]

> "또한 CI/CD에서 얻은 정보를 기반으로 추가 정보를 더할 수 있는 역량이 있으며, 내부 지식을 갖춘 SRE도 활용할 수 있습니다. 고객은 모든 매개변수를 알 필요가 없기 때문입니다." [S5]

> "하지만 코르사체의 가장 큰 강점은 바로 저희 SRE(사이트 신뢰성 엔지니어)들이 문제 해결 능력이 뛰어나고 문제의 근본 원인을 파악하는 데 매우 능숙하다는 점입니다. 그래서 비가 오는 날에도 다음 날에는 통화할 준비가 되어 있습니다." [S5]

기계가 못 하는 경계도 명시된다:
> "예를 들어, 사용 가능한 IP 주소가 모두 소진된 경우와 같이 불가능한 시나리오가 있을 수 있습니다. 자동화 시스템은 완벽하게 작동하지만, 하이퍼스케일러 측의 리소스 문제가 원인입니다" [S5]
> "그래서 그 부분에 대해서는 자동화 자체에서 할 수 있는 일이 많지 않습니다. 이 문제를 해결하려면 퍼블릭 클라우드 제공업체에 문의해야 합니다." [S5]

증강 관계를 가장 노골적으로 표현한 문장:
> "네, 마치 우리 SRE 팀이 해군 특수부대나 해병대 같다는 말이 나왔는데, 우리가 그들에게 서비스 빌더나 자동화 프레임워크 같은 최첨단 무기를 제공했기 때문이죠." [S5]

**(4) 고객 요구 도출 단계의 인간 협업 [S3][S4][S5]**

> "고객들은 자신이 원하는 것을 안다고 생각하지만, 때로는 무엇이 부족한지조차 모른다는 것입니다" [S3]
> "그리고 고객과 함께 어떤 해결책이 있을 수 있을지 항상 함께 고민해야 합니다" [S3]

> "고객이 우리 솔루션을 원한다고 동의하면, 우리 솔루션 설계자는 고객 엔지니어와 협력하여 배포 매개변수와 필요한 사항을 파악합니다." [S4]

> "저희 건축가와 엔지니어들 도 초기 논의 단계에 참여합니다. 우리는 고객과 아이디어를 공유하고 있으며, 제품의 기능도 공유하고 있습니다. 우리는 함께 그들이 진정으로 원하는 것이 무엇인지, 그리고 그것을 어떻게 달성해야 하는지 결정합니다." [S5]

**(5) 검증·의사결정의 인간 — 통신사 측 서술 [S6]**

> "일반적으로 이는 가능한 한 많은 단계를 자동화하는 단계적인 진화 과정이지만 , 아직 완전 자율화와는 거리가 멉니다. 그래서 우리 엔지니어들은 여전히 검증 및 의사 결정에 중요한 역할을 하고 있습니다." [S6]

AI 도구가 인간을 대체하지 않고 **속도만 바꾼** 사례:
> "반면에, 우리 엔지니어들은 Wireshark에서 다양한 패킷 파일을 분석하는 데 몇 시간씩 소비하고 있었지만, 이제는 예를 들어 AI 에이전트를 활용하여 그 시간을 몇 분으로 단축하고 주어진 작업 사례의 근본 원인 분석을 제공하는 실험을 진행하고 있습니다" [S6]

---

### 8.5 전환 메커니즘 (CYCLE)

**있음.** 단, 기준은 **정량 지표가 아니라 반복 성공을 통한 신뢰 축적**으로 제시된다.

**(1) 명시적 전환 기준 — "100번 정도 같은 결과" [S3]**

> "처음 자동화를 사용했을 때는 첫 번째 컨테이너가 제대로 작동하는 것을 확인하고, 두 번째 , 세 번째 컨테이너를 만들면서 "아, 잘 작동하네"라고 생각하죠. AI도 마찬가지일 거라고 생각합니다. 처음에는 작동하는지 확인하고 점검하겠지만, 100번 정도 같은 결과가 나오면 시스템 내부에서 무슨 일이 일어나는지 완전히 이해하지 못하더라도 신뢰를 갖게 될 겁니다." [S3]

이것이 이 사례에서 **논문 CYCLE(증강 학습 → 견고화 → 자동화)의 가장 직접적인 대응 문장**이다. 특징은 두 가지다. 첫째, 전환 기준이 **반복 관찰 횟수**다. 둘째, 전환 후에도 **기계 내부 이해는 회복되지 않는다**("완전히 이해하지 못하더라도").

**(2) 동일 패턴의 과거 사례 — 설치 자동화 [S3]**

> "예전에는 어떤 카드인지 알고 소프트웨어를 업로드하는 데 몇 달이 걸렸습니다. 하지만 나중에는 설치 과정까지 자동화했습니다. " 여기 패키지가 있습니다. 연결하고 마법의 버튼을 누르세요."라고 말하기만 하면 모든 구성 요소가 랙 전체에 설치됩니다. 저는 AI도 마찬가지일 것이라고 생각합니다. 처음에는 약간의 오류가 발생하겠지만, 시간이 지나면서 점점 더 안정되고 오류가 없는 도구로 발전할 것입니다." [S3]

**(3) 전환의 전제 조건 — 신뢰·관찰 가능성 [S2][S3]**

> "그리고 신뢰를 제공하고 구축하는 방법도 정확히 알아야 합니다." [S2]
> "그래서 우리는 자동화 시스템이 모든 것을 처리할 수 있으므로 모든 것이 제대로 작동하고 있음을 보여주기 위해 도구와 전체 시스템에 대한 모니터링 및 관찰 가능성을 제공해야 합니다." [S2]

> "따라서 AI 기반 자동화 도구에서도 마찬가지로, AI를 사용하는 도구라면 항상 신뢰성과 관찰 가능성을 확보해야 합니다" [S3]

**(4) 증강 회귀(조건 변화 시) 방향의 서술 [S3]**

시간 축의 역방향(자동화 → 재설계)이 명시된다:
> "그러니까 특정 기간, 예를 들어 1년, 2년, 혹은 3년 동안 필요한 자동화 기능이 있을 수 있습니다. 그 후에는 해당 자동화 기능을 교체하거나 네트워크를 변경하는 방향으로 진화시킬 수 있는 시점이 오는 것입니다." [S3]
> "그러므로 사용 사례가 변경되면 나중에 전체 자동화 시스템이 아무 의미가 없어질 수도 있습니다." [S3]
> "그러니까 단순히 단계가 있는 것뿐만 아니라, 단계 간의 이동도 가능하다는 거죠. 한 주에서 다른 주로 이동하는 방법." [S3]

마지막 문장은 기계번역이 어색하나("한 주에서 다른 주로" = one state to another state의 오역으로 보임), **상태 간 이동**을 자동화 설계의 축으로 명시한 점에서 CYCLE 근거로 유효하다.

**(5) TM Forum 자동화 성숙도 — 소스 상태**

- **[S1]에만 1회 언급**: "이 모듈형 플랫폼은 다양한 공급업체 또는 멀티 클라우드 환경에 적응하고, TM 포럼 자동화 모델의 4단계 달성을 향한 진행 상황을 직접적으로 매핑하며" [S1]
- **레벨 0~5 또는 4단계의 정의, 각 레벨에서 인간이 무엇을 하는지는 [S1]~[S7] 어디에도 없음.** [S1]은 "4단계 달성을 향한 진행 상황"이라고만 하고 단계별 내용을 설명하지 않는다. [S2]~[S7]에는 TM Forum이라는 표현 자체가 등장하지 않는다(단 [S3]의 "Taco API"는 문맥상 TM Forum API의 자막 오류로 보이나 확정할 수 없음 — 8.11 참조).
- 따라서 **각 레벨에서 인간이 무엇을 하는가는 이 사례에서 답할 수 없다.** 대신 소스가 제공하는 것은 위 (1)~(4)의 **비공식적·서술적 성숙도 곡선**이며, 이것은 산업 표준 레벨이 아니라 실무자의 경험칙이다.

**(6) 폐쇄 루프(closed-loop) 자동화의 "단계"**

소스는 폐쇄 루프를 **단계로 나누지 않는다.** 확인되는 것은 다음뿐이다.

- [S1]: "머신러닝을 도입하여 폐쇄 루프 자동화를 구현하고 생성형 AI를 활용함으로써" / "높은 수준의 폐쇄 루프 및 도메인 간 자율성"
- [S2]: 의도(intent)와 폐쇄 루프의 결합 — "그러니까, 의도는 기본적으로 어떻게 표현하는지에 관한 것이지만, 동시에 이 의도를 이해하고 실행하려고 시도하는 폐쇄 루프 자동화 시스템과 연결되어야 합니다." [S2] / "그래서 우리는 폐쇄 루프 자동화 시스템과 의도 인터페이스를 구현하고 있습니다." [S2]
- [S2]: 계층 하강 — "그러니까 기본적으로 지금 일어나고 있는 일은 계층별 배포입니다." / "그리고 경우에 따라 한 단계 또는 여러 단계로, 하나씩 차례로 내려가서 기본적으로 가장 낮은 매개변수 수준까지 내려가는 거죠?" [S2]
- [S5]: 루프의 UI 노출 — "의도 기반 자동화를 위한 개별 리소스 루프의 보기를 제공하고, UI 자체에서 어떤 매개변수, 아, 죄송합니다, 어떤 제어 루프가 전송되었는지, 그리고 어떤 제어 루프가 아직 조정 중인지 등을 실제로 알 수 있는 피드백을 제공한다는 것입니다." [S5]

즉 폐쇄 루프의 **성숙도 단계는 소스에 없고**, 대신 루프의 상태를 인간에게 보여주는 UI라는 **증강 장치**가 확인된다.

---

### 8.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

#### SPILL — 있음(강함)

**(1) 코어 배포 자동화 → 인접 과업의 자체 개발 유발 [S5]**

코어를 SaaS로 자동 배포하게 되자, 운영·관측이라는 **인접 과업**에서 기존 도구가 맞지 않게 되었고, 그 결과 새로운 인간 설계 작업이 발생했다.

> "온프레미스 환경에서는 노키아 제품이 이러한 운영 작업을 수행하지만, 해당 시스템은 상당히 복잡합니다. 통합에 시간이 너무 오래 걸리고 리소스 소모가 심하며 모든 CNF를 통합하는 데 시간이 걸리고 자동화하기 어렵기 때문에 이를 SaaS 환경으로 가져오는 것은 현명한 결정이 아니었습니다." [S5]
> "하지만 안타깝게도 노키아 내부나 외부에서 그에 대한 해결책을 찾지 못했습니다." [S5]
> "그래서 우리는 그 문제에 대한 자체적인 해결책을 개발하자는 아이디어를 떠올렸습니다" [S5]

파급된 인접 과업 목록(모두 [S5]):
- 관측 미들웨어: "코어 애플리케이션과 관찰 가능 애플리케이션 사이에 존재하는 미들웨어라고 합니다. 이 도구는 저희가 개발했습니다."
- DNS: "그래서 이러한 상황에서는 그들의 서비스 상품을 이용할 수 없었고, 직접 해결책을 마련해야 했습니다."
- 장기 데이터 보관: "그래서 우리는 저장 공간을 위한 솔루션도 개발해야 했습니다."
- CDR 보안 처리: "그리고 그러한 경우, 우리는 데이터를 어떻게 저장하고 고객에게 어떻게 전달할 수 있을지에 대한 해결책을 개발해야 했습니다."
- Git 저장소 관리: "Git 저장소 관리와 같이 기본적으로 클라우드 네이티브 방식이 아닌 특정 사용 사례를 위해, 저희는 다른 자동화 작업과 마찬가지로 GitOps 방식으로 이를 수행할 수 있는 도구를 개발하고 있습니다."

**(2) 자동화로 인해 인간이 대시보드를 볼 수 없게 되자 → 또 다른 자동화 필요 [S5]**

> "대시 보드를 보는 것 자체는 중요하지만, 엔지니어들이 통합, 배포, 문제 해결 등 다양한 작업을 수행해야 하므로 하루 종일 대시보드만 보고 있는 것을 원하지 않습니다. 그래서 대시 보드를 확인하고 무엇이 잘못되었는지 파악할 시간이 없습니다. 그러므로 네트워크에서 발생하는 문제에 대응하기 위해 운영 측면에서도 자동화가 분명히 필요합니다." [S5]

이것은 [S1]의 "제로 아이볼 운영"이 실무에서 어떻게 생겨나는지를 보여주는 **유일한 메커니즘 서술**이다. 인간이 사라져서 제로 아이볼이 된 것이 아니라, **인간이 다른 과업으로 옮겨가서** 눈이 비게 되고 그 자리를 Datadog/PagerDuty 연동이 메운다.

> "그리고 Datadog이라는 관찰 도구는 PagerDuty라는 또 다른 SaaS 유형의 도구와 통합되어 이상 징후와 문제를 지능적으로 감지하고 엔지니어에게 이러한 상황을 알리는 데 사용됩니다." [S5]

**(3) 코어(클라우드) 자동화 → 라디오 도메인 최적화로 파급 [S5]**

> "처음에는 잘 이해가 안 될 수도 있지만, 생각해 보면 코어 서버가 퍼블릭 클라우드에 배포되었다고 해서 무선 네트워크가 실제로 운영되는 위치에 그대로 분산되어 있는 것은 아닙니다. 그리고 이를 보완하기 위해 Ava 에너지 효율 제품을 배포할 수 있는데, 이 제품은 코어 계층과 OSS 계층을 통해 네트워크 내의 무선 기지국에 접근하여 실제 필요에 따라 구성할 수 있습니다." [S5]

**(4) 네트워크 자동화 → 네트워크 외부 과업으로 파급 [S2][S5]**

> "또는 대기 오염 데이터를 수집하여 다른 공급업체나 해당 데이터를 사용하는 다른 회사에 제공하는 연구 프로젝트도 있었습니다." [S2]
> "예를 들어 벨기에에서는 엄청난 양의 트래픽을 실제로 모니터링하고 있습니다" / "그리고 이는 예를 들어 경찰이 실제로 얼마나 많은 인력을 현장에 투입해야 군중 해산을 도울 수 있는지 파악하는 데 필요합니다." [S5]

후자는 **한 도메인의 자동화(네트워크 노출 기능)가 인접 조직(경찰)의 인간 판단을 증강**하는 사례로, 조직 경계를 넘는 SPILL이다.

**(5) 자동화 자체가 자동화 필요를 낳음 [S2]**

> "또한 자동화가 필수적입니다. 사람이 직접 이러한 애플리케이션을 구성해야 한다면 악몽과도 같을 것입니다. 배포해야 할 곳도 많고 설정해야 할 매개변수도 많기 때문입니다" [S2]

#### REINV — 약함(간접 근거만)

논문의 UBS 패턴(자동화로 확보한 자원을 증강에 재투자)에 **직접 대응하는 서술은 없다.** 확인되는 것은 인접한 세 가지다.

**(a) 재사용을 통한 내부 시너지 [S5]** — 자원의 재투자라기보다 산출물의 재사용.
> "하지만 여기서 중요한 점은 우리가 퍼블릭 클라우드 위에 추가로 개발한 이러한 서비스와 솔루션 들을 다른 서비스에서도 재사용할 수 있다는 것입니다" [S5]
> "그래서 서로 다른 팀들이 똑같은 것을 계속해서 개발하는 것이 아니라 , 핵심 분야뿐만 아니라 다양한 영역에서 동일한 접근 방식을 재사용할 수 있습니다" [S5]
> "레고 블록처럼요." [S5]

**(b) 절약된 시간의 행선지 — 명시 없음 [S6]**
> "이전에는 몇 시간씩 걸리던 작업이 이제는 몇 분 만에 완료됩니다." [S6]
— 절약된 엔지니어 시간이 어디로 재배치되는지는 [S6]에 없음.

**(c) 역량/재교육 관련 서술** — **거의 없음.**
- [S1]은 문제 진술로 "직원들의 기술 역량은 미래 기술과 항상 일치하는 것은 아닙니다" [S1]라고만 말하고, 재교육 프로그램·전환배치·역량 투자에 대한 서술은 [S1]에 **없다**.
- [S2]~[S7] 어디에도 재교육/리스킬링 프로그램 서술은 **없음**.
- 가장 근접한 것은 [S3]의 조직 사례인데, 이는 재교육이 아니라 **기존 전문가에게 문제 정의권을 넘긴 조직 개편**이다:
> "그러자 제 매니저가 저에게 "직원들을 잘 챙겨라. 그러면 직원들이 회사를 잘 챙겨줄 것이다"라고 말했습니다. 그래서 제가 세운 전략은 그들에게 "좋습니다, 당신이 그 문제에 대한 전문가시니 어떻게 해결하시겠습니까?"라고 묻는 것이었습니다." [S3]
> "그리고 반년 만에 수많은 환경이 완전히 재설치되었고, 자동화 시스템이 제대로 구축되었습니다." [S3]
> "자동화를 활용하고 제대로 설정하는 방법을 이해했기 때문에 이러한 시스템이 가능해진 것입니다." [S3]

**결론: REINV는 이 사례에서 사실상 확인되지 않는다. 위 (a)의 재사용 서술만 부분적 대응이며, 인력·예산의 재투자 근거는 지정 소스에 없다.**

---

### 8.7 통합 장치 (RESP)

**있음. 다만 "설계 원칙"과 "미래 계획"의 형태이며, 구현된 승인 워크플로/감사 추적의 구체 사양은 소스에 없다.**

**(1) 통제권 유지 원칙 — 가장 명확한 RESP 문장 [S2]**

> "하지만 통신업계에서는 99.99%의 가용성을 유지해야 하기 때문에 사업자들이 모든 것을 통제하려고 합니다. 즉, 시스템이 항상 가동되고 서비스가 중단되지 않도록 보장해야 한다는 것입니다" [S2]

> "하지만 우리 입장에서는 모든 것이 자동으로 이루어지도록 하면서도, 그들이 언제든 제어할 수 있도록 하는 것이 중요합니다. 이러한 요소들이 모두 조화를 이루어야 하는데, 이는 우리가 해결해야 할 상당히 복잡한 문제이며, 우리는 지금 바로 그 작업을 진행하고 있습니다." [S2]

**(2) 운영자 사고방식 전환 — 통제의 성격 변화 [S2]**

> "그리고 운영자들에게도 사고방식의 변화가 필요하다고 생각합니다. 왜냐하면 그들은 도구가 이러한 것들을 제어하도록 하고, 도구가 결정을 내리도록 하며, 필요할 때 모니터링하고 상호 작용해야 하기 때문입니다." [S2]

**(3) 승인권의 형태 — "자동으로 또는 원한다면 승인을 요청" [S3]**

> "관찰 내용을 알리는 알림을 보내면 됩니다 . "이것이 제가 관찰한 내용입니다. 이것이 근본 원인이었고, 저는 이렇게 조치했습니다." 그런 다음 자동으로 또는 원한다면 승인을 요청하는 방식으로 진행할 수 있습니다" [S3]

주의: 이 문장은 **미래형 서술**(5년 후 전망 문답 안에 위치)이며, 현재 운영 중인 승인 게이트가 아니다.

**(4) 검증·의사결정 책임의 인간 보유 — 통신사 측 [S6]**

> "그래서 우리 엔지니어들은 여전히 검증 및 의사 결정에 중요한 역할을 하고 있습니다." [S6]
> "또한, 테스트 자동화는 종종 과소 평가되지만, 매 분기 수십 개의 새로운 소프트웨어 패키지가 출시되는 현재와 같이 빠르게 변화하는 환경에서는 이러한 모든 소프트웨어 패키지를 검증하고 견고하고 신뢰할 수 있는 테스트 자동화 시스템을 구축해야 합니다." [S6]

**(5) 벤더-고객 간 책임 배분 [S6][S7]**

> "저희 조직인 기술 제공 국제 부서는 공급업체가 제공하는 솔루션을 선정, 설계 및 검증하는 데 핵심적인 역할을 담당합니다." [S6]
> "저희는 협력업체들이 자동화와 배포가 용이한 소프트웨어 자산을 저희 소프트웨어 제품에 제공해 주기를 바랍니다" [S6]

> "사실 귀사는 저희 핵심 네트워크 분야에서 가장 큰 공급업체입니다 . 그와 함께 노키아는 더 큰 책임과 기대를 안게 됩니다" [S7]

**(6) 근본 원인 분석 = 책임 귀속 장치 [S2]**

> "또한, 저희는 여러 공급업체와 다양한 계층으로 구성된 모델을 사용하고 있기 때문에 근본 원인 분석이 필요합니다. 따라서 운영자는 무슨 일이 일어나는지, 그리고 누가 그 문제를 해결해야 하는지 알아야 합니다. 어느 판매업체인가요?" [S2]

멀티벤더 환경에서 RCA는 기술 진단이자 **책임 소재 확정 장치**로 기능한다. 이는 논문 p.200 RESP의 산업적 변형이다.

**(7) 데이터 거버넌스 [S3][S5]**

> "고객은 데이터를 보유하고 있지만, 여러 경우에 그 데이터는 고객과 최종 사용자 모두에게 비공개이기 때문에 저희와 공유할 수 없습니다" [S3]
> "네, 예를 들어 CDR, 즉 통화 기록에는 가입자에 대한 기밀 정보와 데이터 사용량 등이 포함되어 있습니다" [S5]
> "그리고 이 데이터는 프로그램을 통해 익명화할 수 있습니다." [S5]

**감사추적(audit trail)이라는 명시적 용어와 그 구현은 [S1]~[S7] 어디에도 없음.** 가장 근접한 것은 GitOps의 선언적 저장소 개념이다:
> "GitOps는 리소스를 Git에 저장하고, 해당 리소스가 Kubernetes 클러스터와 동기화되도록 하는 것을 의미합니다" [S4]
> "자체 개발한 마젠타 CI/CD를 기반으로 CI/CD를 구축하고, GitOps 사고방식을 바탕으로 코드로 구성을 관리하며, 자동화된 테스트를 처음부터 현실로 구현할 수 있습니다." [S6]
그러나 **어느 소스도 이것을 "감사" 목적으로 설명하지 않는다.** 감사 해석은 필자의 추론이 아니라 소스 부재로 처리해야 한다.

---

### 8.8 성과 수치

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 헬프 데스크 티켓 | 명시 없음 | "최대 20% 감소" | [S1] | **벤더 자체보고**(Nokia 제품 영상, 측정 방법·기간·표본 미공개) |
| 평균 감지 시간(MTTD) | 명시 없음 | "75% 단축" | [S1] | 벤더 자체보고 |
| 평균 복구 시간(MTTR) | 명시 없음 | "20% 단축" | [S1] | 벤더 자체보고 |
| 셀 열화 예측 정확도 | 명시 없음 | "약 90%" | [S1] | 벤더 자체보고 |
| 현장 방문 횟수 | 명시 없음 | "10~20% 감소" | [S1] | 벤더 자체보고 |
| 총 소유 비용(TCO) | 명시 없음 | "약 15% 절감" | [S1] | 벤더 자체보고 |
| 매니지드 서비스 시장 순위 | — | "5년 연속 세계 최고의 매니지드 서비스 제공업체로 인정받았습니다" | [S1] | **제3자 평가를 인용한 자체 서술** — 평가 주체(기관명)가 [S1]에 명시되지 않음 |
| 코어 네트워크 배포 소요 시간 | "몇 달 또는 심지어 1년" [S4] | 90분(수사적 제안) / 실제 서술은 몇 시간 배포 + 몇 시간 통합 [S5] | [S4][S5] | 벤더 자체보고, **두 소스 간 값이 다름**(8.9 참조) |
| 첫 통화(first call) 달성 시점 | 명시 없음 | "배포를 시작하고 통합을 완료한 바로 그날, 첫 번째 테스트를 진행했습니다. 그리고 같은 날 첫 통화 테스트도 성공적으로 완료되었습니다." | [S5] | 벤더 자체보고, 표본 수 미상 |
| 허리케인 밀턴 시 기지국 피해 | — | "기지국의 22%가 파괴되었습니다" | [S7] | **고객사(T-Mobile) 임원 자체보고** |
| 동 사건 고객 영향 | (자동화 없었을 경우 값 없음) | "고객의 8%에게만 영향을 미칠 수 있습니다" | [S7] | 고객사 자체보고. **반사실(counterfactual) 기준선 없음** |
| RAN 에너지 절감(Ava 에너지 효율) | — | "5%에서 20~ 25%까지 절감 효과" | [S5] | 벤더 자체보고, 조건부("고객의 기후, 기존 에너지 효율 수준, 최신 무선 기술 사용 여부 등에 따라") |
| 네트워크 에너지 구성비 | — | "그중 10%는 운송에, 10% 는 핵심 부품에, 그리고 나머지 80%는 라디오에 사용된다고 가정해 봅시다." | [S5] | **가정치**("가정해 봅시다"). 실측치 아님 |
| 라디오 에너지 중 냉각 비중 | — | "그러니까 그 80% 중에서 20~30% 정도는 냉방, 난방 등에 쓰이는 거죠" | [S5] | 벤더 추정 |
| DT의 에너지 절감 감도 | — | "에너지 소비량을 1%만 절약해도 저희 같은 사업자에게는 엄청난 절감 효과가 됩니다" | [S6] | 고객사 정성 진술(금액 미제시) |
| Wireshark 패킷 분석 시간 | "몇 시간씩 소비하고 있었지만" | "그 시간을 몇 분으로 단축" | [S6] | 고객사 자체보고, **"실험을 진행하고 있습니다"= 실험 단계** |
| 문서/문제해결 처리 시간 | "이전에는 몇 시간씩 걸리던 작업" | "이제는 몇 분 만에 완료됩니다" | [S6] | 고객사 자체보고 |
| 검증 조직 개선 | "대부분의 환경이 제대로 갖춰져 있지 않았기 때문에 상당히 어려운 과제였습니다" | "반년 만에 수많은 환경이 완전히 재설치되었고, 자동화 시스템이 제대로 구축되었습니다" | [S3] | 개인 회고(연도 미상, 55명 조직) |
| 퍼블릭 클라우드 워크로드 비중(2024) | — | 진행자가 "70%"라 답하고 "가보르는 75%로 거의 근접했죠"라고 함 — **정답 수치가 문장으로 확정되지 않음** | [S4] | 퀴즈 형식, 출처 미제시 |
| 대기업 평균 SaaS 앱 수(2024) | — | "대기업은 평균적으로 130개 정도의 SaaS 애플리케이션을 사용합니다" | [S5] | 퀴즈 형식, 출처 미제시 |
| 전 세계 SaaS 기업 수(2024) | — | "전 세계적으로 3만 개 이상의 SaaS 기업이 있다는 추산이 있습니다" | [S5] | 퀴즈 형식, 출처 미제시 |
| T-Mobile/SpaceX 위성 | — | "T-Mobile과 SpaceX는 400개 이상의 위성을 발사했으며" | [S7] | 고객사 자체보고 |

---

### 8.9 소스 간 교차 대조

#### (1) 반복 확인된 사실

| 사실 | 확인된 소스 | 비고 |
|---|---|---|
| 제로 터치라는 목표 어휘 | [S1] "제로 터치 네트워크" / [S4] "제로 터치 배포" / [S7] "제로 터치 프로비저닝" | **동일 어휘, 서로 다른 대상**(네트워크 운영 / 소프트웨어 배포 / MVNO 프로비저닝). 셋을 같은 것으로 취급하면 오류 |
| 폐쇄 루프/제어 루프 | [S1][S2][S5] | [S1]은 결과 주장, [S2]는 의도-루프 결합 원리, [S5]는 루프 상태의 UI 노출 |
| 의도(intent) 기반 자동화 | [S2][S3][S4][S5] | 4개 소스 독립 확인. Nokia 내 일관된 용어 |
| GitOps 채택 | [S2][S4][S5][S6] | [S6]에서 **고객사 측이 독립적으로 확인**("마젠타 CI/CD", "GitOps 사고방식") — 벤더 주장이 아님 |
| 완전 자율화 미도달 | [S2] "자동화가 아직 완벽한 해결책을 제공하지 못하는 경우가 분명히 존재합니다" / [S6] "아직 완전 자율화와는 거리가 멉니다" / [S6] "완전 자율 네트워크는 아직 몇 년 더 걸릴 거라고 생각" | 벤더·고객 **양측이 일치** |
| 인간이 검증/의사결정에 잔류 | [S2][S3][S5][S6] | 4개 소스 확인 |
| 신뢰(trust)가 자동화 확대의 병목 | [S2] "신뢰할 수 있고 믿음직스럽다" / [S3] "100번 정도 같은 결과" / [S2] "신뢰를 제공하고 구축하는 방법" | 3회 반복. 이 사례의 중심 개념 |
| 멀티벤더 복잡성이 자동화의 근본 제약 | [S2][S3][S6] | [S6]에서 고객사가 확인: "저희 협력업체 중 어느 곳도 진정한 클라우드 네이티브 기업이 아니라는 점을 알고 있습니다" |

#### (2) 한 소스에만 있는 사실 (재확인 실패)

**[S1]의 6개 성과 수치 — 전부 단일 출처.** 헬프데스크 티켓 20%, MTTD 75%, MTTR 20%, 셀 열화 예측 90%, 현장 방문 10~20%, TCO 15%. **[S2]~[S7] 어디에서도 이 수치들이 반복되지 않으며, 유사 수치조차 등장하지 않는다.** 논문 인용 시 복수 출처 확인 불가임을 반드시 표기해야 한다.

기타 단일 출처 항목:

| 사실 | 유일 소스 | 상태 |
|---|---|---|
| "글로벌 네트워크 운영 센터의 전문가들이 설계하고 강화했습니다" | [S1] | **재확인 실패.** 기능적 유사물은 [S5]의 SRE 서술뿐이며, [S5]는 "설계"가 아니라 "미세 조정"과 "내부 지식" 활용을 말한다 |
| "제로 아이볼 운영" | [S1] | 재확인 실패. 다른 소스에는 이 용어 자체가 없음 |
| "TM 포럼 자동화 모델의 4단계" | [S1] | 재확인 실패. 레벨 정의 없음 |
| "5년 연속 세계 최고의 매니지드 서비스 제공업체" | [S1] | 재확인 실패, 평가 주체 미명시 |
| 조직 개편으로 반년 만에 자동화 정상화(55명) | [S3] | 개인 회고, 연도·부서 미상 |
| 허리케인 밀턴 22%/8% | [S7] | 유일. 반사실 기준선 없음 |
| Nokia MNOS 플랫폼 사용(DT) | [S6] | 유일. 제품명 표기가 자막 오류 가능성 있음 |
| 드론 가디언(멀티 에이전트) | [S6] | 유일. MWC 전시 예정 = **계획 단계** |
| Ava 에너지 효율 5~25% | [S5] | 유일 |
| Core SaaS Edge / 로컬 브레이크아웃 구분 | [S5] | 유일 |

#### (3) 시점에 따른 서술 변화

7개 소스는 2026-04-17 ~ 2026-06-22의 약 2개월 구간에 업로드됐다. 이 짧은 구간에서 **기술 내용의 변화는 확인되지 않는다.** 그러나 **서술 장르에 따른 체계적 변화**가 뚜렷하다.

- **2026-04-17 [S1] (제품 영상)**: 완료형·단정형. "제공합니다", "경험했습니다". 인간은 플랫폼 설계자로만 1회 등장하고 운영 루프에서는 사라진다.
- **2026-04-21 [S2][S3][S4][S5] (실무자 팟캐스트)**: 진행형·조건형. "지금 바로 그 작업을 진행하고 있습니다" [S2], "아직은 다소 새로운 기술입니다" [S2], "현재 저희 포트폴리오에는 없지만, 미래에는 포함될 수도 있습니다" [S2]. 인간이 도처에 남아 있다.
- **2026-05-26 [S6] (고객사 관점)**: 진행형 + 부정형. "아직 완전 자율화와는 거리가 멉니다", "정말 새로운 분야라서 기본적으로 테스트 단계입니다", "완전 자율 네트워크는 아직 몇 년 더 걸릴 거라고 생각".
- **2026-06-22 [S7] (고객사 임원 대담)**: 완료형과 미래형 혼재. "저희는 이미 예를 들어 새로운 MVNO를 활성화하는 방식에서 제로 터치 프로비저닝과 같은 방식으로 이를 실천하기 시작했습니다."와 "앞으로 저희는 노키아와 더욱 많은 협력을 진행할 예정입니다."가 같은 문단에 있음.

**따라서 시간에 따른 성숙이 아니라, 누가 어디서 말하는가가 자동화 완성도 서술을 결정한다.** 이 사례에서 시점 변수는 장르 변수와 교란(confounded)되어 있으며, 4일 간격의 [S1]과 [S2]가 정반대 톤이라는 점이 그 증거다.

#### (4) 모순 / 긴장

**모순 A — 「설정 후 신경 쓸 필요 없는 상태」 대 「인간은 여전히 필요」**

> [S1] "네트워크가 구축 및 자동화되어 사람의 개입이 최소화되는, 설정 후 신경 쓸 필요 없는 상태가 되는 것이 이상적입니다" [S1]

> [S2] "지금까지는 인간의 개입에 더 의존해 왔고, 여전히 이러한 작업을 직접 수행해야 하는 경우가 있습니다." [S2]
> [S6] "그래서 우리 엔지니어들은 여전히 검증 및 의사 결정에 중요한 역할을 하고 있습니다." [S6]

업로드 간격 4일([S1] 4/17 → [S2] 4/21). 엄밀히는 [S1]이 "이상적"이라는 목표 진술이므로 논리적 모순은 아니나, [S1]만 인용하면 인간 잔여 역할이 전부 소거된다.

**모순 B — 배포 시간: 90분 대 몇 시간＋몇 시간**

> [S4] "수개월 또는 수년을 기다리는 대신 90분 만에 핵심 네트워크 서비스(음악)를 배포할 수 있다고 상상해 보세요. 네, 가능합니다(음악으로도요)." [S4]

> [S5] "배포 버튼을 클릭한 후에는 몇 시간 동안 앉아서 코어 시스템이 가동될 때까지 기다립니다. 그리고 핵심 시스템이 구축되면 통합 작업을 시작하는데, 통합 작업 자체도 몇 시간 정도 소요됩니다." [S5]

같은 날 업로드된 같은 팟캐스트 시리즈의 Part I과 Part II다. Part I의 인트로(내레이션)는 90분, Part II의 실무 서술은 수 시간+수 시간. **90분이라는 값은 인트로의 홍보 문구이고 실제 절차 서술과 자릿수가 다르다.** 인용 시 반드시 [S5] 쪽을 병기해야 한다.

**모순 C — 제로 터치 배포(사람 접촉 없음) 대 SRE의 최종 미세 조정**

> [S4] "CIQ가 AI와 협상되면 단 한 번의 클릭으로 배포할 수 있습니다. 사람과의 직접적인 접촉 없이도, 고객이 먼저 우리에게 연락하여 문을 두드리는 지점에 도달할 수 있습니다." [S4]

> [S5] "GitOps 기반 접근 방식을 통해 핵심 서비스 배포를 실제로 담당하는 SRE(사이트 신뢰성 엔지니어)들이 서비스 배포에 대한 최종 미세 조정을 수행할 수 있도록 지원하는 것입니다." [S5]

[S4]의 제로터치 배포는 **미래 전망**("저는 그것이 미래 SaaS 모델의 나아갈 방향이라고 생각합니다")이고, [S5]는 **현재 절차**다. 시제가 다르다.

**모순 D — 자동화의 성격: 단순화 대 복잡화**

> [S2] "음, 자동화는 단순화라고 할 수 있겠죠." / "물론 이는 프로세스 자체가 단순화된다는 것을 의미하지만, 자동화 시스템이 작업자의 업무량을 대신 처리해야 하므로 결과적으로 시스템이 더 복잡해지는 측면도 있습니다" [S2]

같은 발화 안의 자기모순이며, **화자가 의식적으로 제시한 긴장**이다. [S3]에서 반복 확장된다:
> "간소화가 진행됨에 따라, 아주 세부적인 설정 매개변수에 대한 제어권이나 시스템을 미세 조정할 수 있는 기능을 잃게 될 것입니다." [S3]
> "따라서 우리는 고객을 만족시키기 위한 적절한 수준의 단순화와 자동화를 제공하는 것 사이에서 균형을 찾아야 합니다. 왜냐하면 이 두 가지 요구 사항은 서로 상충하기 때문입니다." [S3]

**긴장 E — 가용성 수치의 흔들림**

[S2]에서 같은 화자군이 99.999%(3회)와 99.99%(2회)를 섞어 쓴다. [S3]에서는 "99.99% 이상의 정확도"라는 표현까지 나온다(정확도와 가용성 혼동). 자막 오류인지 발화 오류인지 판별 불가. **정밀 수치로 인용하면 안 된다.**

**긴장 F — AI에 대한 벤더 내부의 온도차**

> [S1] "생성형 AI를 활용함으로써 네트워크의 안정성, 신뢰성 및 보안을 보장할 수 있습니다" [S1]
> [S3] "하지만 때로는 신뢰할 수 없는 경우도 있으며, 존재하지 않는 사실이나 내용을 제시하기도 합니다." [S3]

같은 회사 채널에서 4일 간격으로 생성형 AI가 "보안을 보장"하는 수단과 "환각하는" 대상으로 각각 서술된다.

---

### 8.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 판정 |
|---|---|---|
| AUTO: 기계가 과업을 인계, 인간을 루프에서 제외 (p.194) | "사람의 개입이 최소화되는, 설정 후 신경 쓸 필요 없는 상태" [S1]; "수동 작업 없이 자동화" [S6]; "사람의 개입 없이도 복구" [S7] | **지지** |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | SRE의 "최종 미세 조정" [S5]; "필요한 개입 지점만 제공하는 방식" [S2]; "여전히 검증 및 의사 결정에 중요한 역할" [S6] | **지지** |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | "100번 정도 같은 결과가 나오면 시스템 내부에서 무슨 일이 일어나는지 완전히 이해하지 못하더라도 신뢰를 갖게 될 겁니다." [S3]; 설치 자동화 회고 [S3] | **지지 + 확장**(전환 기준을 반복 관찰 횟수에 의한 신뢰 축적으로 구체화) |
| CYCLE 역방향: 조건 변화 시 증강 회귀 (p.196-197) | "그러니까 특정 기간, 예를 들어 1년, 2년, 혹은 3년 동안 필요한 자동화 기능이 있을 수 있습니다." [S3]; "사용 사례가 변경되면 나중에 전체 자동화 시스템이 아무 의미가 없어질 수도 있습니다" [S3] | **지지**(단, 실제 회귀 사례는 없고 예상 서술) |
| SPILL: 한 과업 자동화가 인접 과업의 증강을 유발 (p.197) | 코어 SaaS화 → 관측 미들웨어/DNS/스토리지/CDR 자체 개발 [S5]; "대시 보드를 확인하고 무엇이 잘못되었는지 파악할 시간이 없습니다" → 알림 자동화 필요 [S5]; 코어 자동화 → 라디오 에너지 최적화 [S5] | **지지 + 확장**(파급이 "증강"뿐 아니라 **새 자동화 요구**로도 이어짐) |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS) | 직접 대응 없음. 산출물 재사용("레고 블록처럼요" [S5])과 절약 시간의 행선지 미명시 [S6]뿐 | **미확인 / 근거 빈약** |
| RESP: 인간이 프로세스 전체 책임·승인·감사 보유 (p.200) | "그들이 언제든 제어할 수 있도록 하는 것이 중요합니다" [S2]; "자동으로 또는 원한다면 승인을 요청하는 방식" [S3]; RCA를 통한 벤더 책임 귀속 [S2]; "노키아는 더 큰 책임과 기대를 안게 됩니다" [S7] | **부분 지지**(승인권·통제권은 확인, **감사추적은 소스에 없음**) |
| p.195 증강 학습은 도메인 전문가의 암묵지에 의존하며 IT부서/외부업체에 위임 불가 | "실제 통신 문제를 해결한 경험이 있는 글로벌 네트워크 운영 센터의 전문가들이 설계하고 강화했습니다" [S1]; "당신이 그 문제에 대한 전문가시니 어떻게 해결하시겠습니까?" [S3]; "내부 지식을 갖춘 SRE도 활용할 수 있습니다" [S5]; "이미 존재하는 실질적인 제품이나 서비스를 통해 회사와 협력하거나 관계를 맺기를 원합니다" → 연구자와 고객의 단절 [S3] | **지지 + 반증 요소 병존**(아래 산문 참조) |
| p.198 기계 한계 ①목적/자아 부재 | "고객들은 자신이 원하는 것을 안다고 생각하지만, 때로는 무엇이 부족한지조차 모른다는 것입니다" + "그래서 우리도 혁신해야 하고, 어떻게 하면 그들의 삶과 일을 더 나아지게 할 수 있을지 아이디어를 제시해야 합니다." [S3] | **지지**(목적 설정은 인간 몫) |
| p.198 기계 한계 ②제약 완화된 옵션만 제시 | "자동화 시스템은 완벽하게 작동하지만, 하이퍼스케일러 측의 리소스 문제가 원인입니다" [S5] — IP 고갈 시 루프가 무한 조정만 반복 | **지지**(외부 제약 앞에서 기계가 무력) |
| p.198 기계 한계 ③훈련된 과업에 국한 | "그러므로 사용 사례가 변경되면 나중에 전체 자동화 시스템이 아무 의미가 없어질 수도 있습니다." [S3]; "특정 사용 사례만을 위한 맞춤형 솔루션이 되어버리기 때문입니다." [S3] | **지지** |
| p.198 기계 한계 ④감각/감정/사회기술 부재 | 고객 조직 정치 대응은 인간 몫: "그러니까 당신은 중간에 앉아서 여러 팀과 소통하면서 모든 팀의 요구 사항을 충족시켜야 하는 거죠. 우선순위를 정해야 합니다." [S3]; "한 고객이라도 동일한 자동화 시스템에 대해 서로 모순되는 요구 사항을 가질 수 있습니다." [S3] | **지지**(사회기술 = 조직 간 협상) |
| p.199 한쪽 편중 시 악순환 | 직접 사례 없음. 근접 서술: 자동화 편중 시 "아주 세부적인 설정 매개변수에 대한 제어권이나 시스템을 미세 조정할 수 있는 기능을 잃게 될 것입니다" [S3]; 맞춤화 편중 시 "그렇게 되면 자동화 기능이 완전히 망가지거나, 자동화 기능을 제대로 활용하지 못하게 될 겁니다" [S3] | **보강**(양방향 편중의 대가를 각각 진술하나 "악순환"이라는 동학은 없음) |
| p.204 기계는 조직 내 새로운 행위자 계급 | "이것이 제가 관찰한 내용입니다. 이것이 근본 원인이었고, 저는 이렇게 조치했습니다." [S3] — 기계가 1인칭으로 보고하고 승인을 요청하는 화행; "시스템 자체가 스스로 " 내가 지금 해야 할 일은 뭐지?"를 판단하고" [S3]; "그중 하나가 드론 가디언입니다" [S6] | **지지 + 확장**(1인칭 화행과 멀티에이전트 조직화) |

**이 사례가 논문을 확장하는 지점**

첫째, 논문의 CYCLE은 증강에서 자동화로의 이행을 **성능의 견고화**로 설명하지만, 이 사례의 실무자들은 이행 기준을 **관찰 횟수에 기반한 신뢰의 사회적 축적**으로 서술한다("100번 정도 같은 결과가 나오면 시스템 내부에서 무슨 일이 일어나는지 완전히 이해하지 못하더라도 신뢰를 갖게 될 겁니다" [S3]). 즉 자동화 전환은 기계 이해도가 올라가서가 아니라 **이해를 포기해도 될 만큼 반복이 쌓여서** 일어난다. 이는 견고화를 인식론적 사건이 아니라 조직적 관행의 문제로 재정의하며, 논문이 전제하는 학습 → 지식 이전 → 위임의 순서를 위임 → 사후적 신뢰로 뒤집는다.

둘째, 논문의 SPILL은 한 과업의 자동화가 인접 과업의 **증강**을 유발한다고 본다. 이 사례에서는 파급이 두 갈래로 갈라진다. 코어 배포 자동화는 한편으로 SRE라는 새로운 증강 역할을 만들었지만([S5]), 다른 한편으로 **자동화가 인간의 시선을 인접 과업으로 이동시켜 원래 자리를 비게 만들고, 그 빈 자리가 다시 자동화로 메워진다**("하루 종일 대시보드만 보고 있는 것을 원하지 않습니다. 그래서 대시 보드를 확인하고 무엇이 잘못되었는지 파악할 시간이 없습니다. 그러므로 네트워크에서 발생하는 문제에 대응하기 위해 운영 측면에서도 자동화가 분명히 필요합니다." [S5]). [S1]이 성과로 내세우는 "제로 아이볼 운영"은 이 두 번째 경로의 산물이지 인간 감시가 불필요해진 결과가 아니다. SPILL은 증강만이 아니라 **자동화의 자기증식** 경로도 포함하도록 확장돼야 한다.

셋째, p.195(암묵지의 위임 불가)에 대해 이 사례는 지지와 반례를 동시에 제공한다. NOC 전문가가 플랫폼을 설계·강화했다는 [S1]의 서술과 "당신이 그 문제에 대한 전문가시니 어떻게 해결하시겠습니까?"라는 [S3]의 조직 개편은 논문 명제를 지지한다. 그러나 [S3]의 연구조직 회고("연구원이라는 직업은 마치 외로운 탑에서 일하는 것과 같았습니다")와 [S3]의 데이터 접근 장벽("그 데이터는 고객과 최종 사용자 모두에게 비공개이기 때문에 저희와 공유할 수 없습니다")은, 벤더가 **고객의 도메인 암묵지에 구조적으로 접근할 수 없는 상태에서 그 고객을 위한 자동화를 설계**해야 함을 보여준다. 논문은 암묵지를 조직 내부의 문제로 다루지만, 멀티벤더 통신 산업에서는 그것이 **조직 경계를 가로지르는 협상 문제**가 된다. [S6]의 DT가 "공급업체가 제공하는 솔루션을 선정, 설계 및 검증하는 데 핵심적인 역할"을 자기 조직의 정체성으로 규정하는 것은, 위임 불가능한 암묵지를 지키기 위해 고객 측이 만든 방어 조직으로 읽을 수 있다.

넷째, RESP의 산업적 변형이 관찰된다. 논문의 RESP는 단일 조직이 프로세스 전체에 책임을 지는 구조를 상정하지만, 이 사례에서 책임은 **벤더-고객-하이퍼스케일러 3자에 분산**되어 있고, 근본 원인 분석이 기술 진단이자 책임 귀속 절차로 이중 기능한다("운영자는 무슨 일이 일어나는지, 그리고 누가 그 문제를 해결해야 하는지 알아야 합니다. 어느 판매업체인가요?" [S2]). 나아가 IP 주소 고갈 사례([S5])는 **어느 인간도 책임질 수 없는 실패 구간**(하이퍼스케일러의 자원 한계)이 존재함을 보여주며, 이는 RESP가 조직 경계 안에서만 성립하는 조건임을 시사한다.

---

### 8.11 인용 시 주의사항

**(1) 자체보고 문제 — 이 사례의 최대 약점**

8.8의 6개 핵심 수치(20%/75%/20%/90%/10~20%/15%)는 **전부 [S1] 단일 출처이고, [S1]은 338단어 제품 홍보 영상이다.** 측정 기간, 표본(몇 개 고객사·몇 개 네트워크), 비교 기준선, 산출 방법이 전부 미공개다. 제3자 검증치는 이 사례에 **하나도 없다.** "5년 연속 세계 최고의 매니지드 서비스 제공업체" 역시 평가 기관명이 [S1]에 없어 제3자 인증인지 확인 불가다. 논문 본문에서 이 수치를 쓸 경우 「Nokia 자체보고 / 복수 출처 미확인 / 방법론 미공개」를 병기해야 한다.

**(2) 성숙도 — 계획/실험/운영의 구분**

| 항목 | 성숙도 | 근거 |
|---|---|---|
| Core SaaS 배포·운영 | **운영 중**(단, 대부분 실험 목적) | "오늘날 우리가 진행하는 대부분의 배포는 혁신을 위한 과정입니다." [S5] |
| 제로 터치 배포(무접촉) | **미래 전망** | "저는 그것이 미래 SaaS 모델의 나아갈 방향이라고 생각합니다." [S4] |
| AI가 CIQ 작성 지원 | **미래 전망** | "저는 AI가 활용될 수 있는 영역 중 하나가 바로 고객이 설정을 준비하는 과정 , 즉 CIQ를 생성하는 데 도움을 주는 것이라고 생각합니다." [S4] |
| 승인 요청형 자율 조치 | **미래 전망**(5년 후 문답 내) | [S3] |
| DT의 AI 이상탐지(MNOS) | **운영/도입 중** | "저희는 이러한 특정 이상 징후 탐지 사례에 Nokia MNOS 플랫폼을 사용하고 있으며" [S6] |
| DT의 AI 패킷 분석 | **실험 단계** | "정말 새로운 분야라서 기본적으로 테스트 단계입니다." [S6] / "실험을 진행하고 있습니다" [S6] |
| 드론 가디언(에이전틱 AI) | **전시 예정** | "저희는 바르셀로나에서 열리는 MWC에서 에이전트형 AI에 관한 흥미로운 이야기를 하나 선보일 예정입니다." [S6] |
| 애플리케이션 오케스트레이션 | **미제품화** | "현재 저희 포트폴리오에는 없지만, 미래에는 포함될 수도 있습니다." [S2] |
| GitOps의 통신업계 적용 | **초기** | "통신 업계에서는 점차 도입되고 있고, 우리도 사용하기 시작하겠지만, 아직은 다소 새로운 기술입니다." [S2] |

**(3) 자막(기계번역) 오류 — 원문 그대로 옮겼으므로 오탈자로 오해하지 말 것**

- "타코 업계도 마찬가지라고 생각합니다" [S3], "내 생각엔 타코일 것 같아" [S2], "물론, 우리가 준수해야 할 Taco API도 있습니다" [S3] — 모두 telco / TM Forum의 오역으로 보이나 **확정 불가**. 특히 `Taco API`를 TM Forum API로 단정 인용하면 안 된다.
- `코르사체` [S5] 는 Core SaaS의 음역 오류. `Core SAS`, `핵심 SAS`, `SAS 자동화` 등 SaaS를 SAS로 적은 표기가 [S4][S5]에 다수.
- `GitHub 기반 자동화` [S3], `GitHub 기술과 연동하여` [S6] — 문맥상 GitOps의 오역 가능성이 높으나 원문 표기 유지.
- `Nokia MNOS 플랫폼` [S6] — 제품명 표기 신뢰도 낮음. 같은 문서 안에 ML Ops가 병기되어 있어 혼동 가능("현재 Nokia ML Ops를 사용하고 계시죠?" [S6]).
- "저희는 AI 기반 픽업 분석 도구를 사용하고 있는데" [S6] — `픽업`은 pcap(패킷 캡처)의 오역으로 보임. 바로 다음 문장이 Wireshark를 언급한다.
- `아바 에너지 효율` 과 `Ava 에너지 효율` [S5] — 같은 문단 내 표기 불일치.
- `네트워크 코드화` [S5] 는 Network as Code, `네트워크 노출 기능` 은 Network Exposure Function.
- "런 및 고정 액세스 네트워크" [S6] = RAN and fixed access의 오역.
- 그 밖의 어색한 표기(원문 그대로): `제 3자 기업` [S3], `미적분 이나 주판` [S2], `저건 검증팀이에요` [S3], `2080년쯤부터 계산을 잊어버렸거든요` [S5](퀴즈 보기, 2018 등의 오역 추정), `네, बिल्कुल 그렇습니다` [S4](힌디어 혼입), `한 주에서 다른 주로 이동하는 방법` [S3](state의 오역), `인력 중복 문제` [S5](redundancy의 오역). 반면 체포 / 디오이트 / Netswuite / 진흥화 같은 표현은 **이 7개 파일에는 없음**.
- 문장 중간의 불규칙한 공백(예: `일치하는 것은 아닙니다 .`, `10% 는 핵심 부품에`, `5%에서 20~ 25%까지`, `의도 기반 솔루션 과`, `여전히 ​​의사 결정`)은 **원본 파일 그대로**다. 일부에는 폭 없는 공백 문자가 포함돼 있어 기계 대조 시 주의가 필요하다.

**(4) 귀속 문제**

- **화자 이름이 소스 간 불일치**: 같은 인물이 [S2] 티모 라즐로 → [S3] 테무; [S4] 졸탄 몰나르 → [S5] 졸타 / 모모 / 모미르; [S7] 라구 → 라가브. **개별 발화를 실명에 귀속시키지 말 것.** 역할(자동화 설계자, SRE 매니저)로만 귀속하는 편이 안전하다.
- **회사 귀속**: 7개 소스 전부 **Nokia 공식 채널**에 업로드됐다. [S6] DT 발언과 [S7] T-Mobile 발언도 Nokia가 제작·편집한 대담이므로 **완전한 제3자 증언이 아니다.** 편집 개입 여부는 확인 불가.
- **제로 터치의 대상 혼동 금지**: [S1]은 네트워크 운영, [S4]는 소프트웨어 배포, [S7]은 MVNO 프로비저닝. 세 개를 하나로 합산하면 안 된다.
- **[S1]의 성과 수치는 AI 기반 관리형 서비스 포트폴리오 전체에 귀속된 것**이지 특정 제품이나 특정 고객사에 귀속된 것이 아니다: "AI 기반 관리형 서비스 포트폴리오의 지원 덕분에 고객은 헬프 데스크 티켓이 최대 20% 감소하고" [S1].
- **허리케인 밀턴 수치의 논리 검토 필요**: "기지국의 22%가 파괴되었습니다. 하지만 인공지능과 자율 조직 네트워크, 자동화 기능을 활용하더라도 고객의 8%에게만 영향을 미칠 수 있습니다." [S7] — 활용하더라도라는 표현은 문맥상 활용한 덕분에의 오역으로 보이며, 22%→8%가 자동화 효과인지 커버리지 중첩 효과인지 [S7]은 구분하지 않는다.

**(5) 이 사례의 근거 밀도 평가**

- **강함**: AUG, RESP(승인/통제 측면), SPILL, CYCLE의 전환 기준.
- **중간**: AUTO(선언은 많으나 실제 무인화 범위의 정량 서술 부족).
- **약함/부재**: REINV, 감사추적, TM Forum 레벨별 인간 역할, 폐쇄 루프의 단계 구분, 재교육·역량 투자, 인원 규모·조직 변화의 정량.

TM Forum 성숙도 레벨을 논문 CYCLE의 산업 표준 버전으로 다루려던 분석 의도는 **이 소스 집합으로는 수행할 수 없다.** [S1]의 1회 언급 외에 아무 근거가 없으며, 그 대체물로 쓸 수 있는 것은 [S3]의 비공식적 신뢰 축적 서사뿐이다.

---

**요약**: 이 절은 Nokia 채널의 7개 영상(업로드일 2026-04-17 ~ 2026-06-22, 전부 채널 수집분이므로 날짜는 업로드 시점)을 전문 판독해, [S1] 제품 영상의 마케팅 서사(제로 터치, 제로 아이볼, NOC 전문가 설계, TM 포럼 4단계, 6개 성과 수치)를 [S2]~[S7]의 실무자·고객사 서술과 대조한 결과를 정리했다. 핵심 발견은 세 가지다. (i) [S1]의 6개 수치와 NOC 전문가 설계·강화 주장, 제로 아이볼, TM 포럼 4단계는 **다른 6개 소스 어디에서도 재확인되지 않는 단일 출처**이며 TM Forum 레벨별 인간 역할은 소스에 정의 자체가 없다. (ii) 증강에서 자동화로의 전환 기준이 성능 지표가 아니라 100번 정도 같은 결과라는 반복 관찰 기반 신뢰로 서술되어 논문 CYCLE을 구체화·역전시킨다. (iii) 코어 자동화가 인접 과업(관측·DNS·스토리지·라디오 에너지)의 자체 개발을 낳고 동시에 인간의 시선을 이동시켜 그 빈자리를 다시 자동화가 메우는 이중 파급이 확인되어 SPILL을 확장한다. 한계는 명확하다 — 7개 소스 전부 Nokia 공식 채널 제작물이라 DT·T-Mobile 발언도 완전한 제3자 증언이 아니고, 제3자 검증 수치가 하나도 없으며, REINV(자원 재투자)와 감사추적 근거는 사실상 부재하고, 화자명·제품명이 기계번역 자막에서 소스 간 불일치하여 개별 발화의 실명 귀속이 불가능하다.


---



## 사례 9 — Siemens : 소프트웨어 정의 자동화 + 엔지니어링 코파일럿

*원문: `docs/cases/08_siemens.md`*


> **인용 표기 규칙**
> - 모든 인용은 원문 자막 문자열 그대로이며 낫표 인용부호 안에 넣었다. 낫표 안의 문자열은 전부 소스 파일에 실재하는 원문이며, 개념 요약이나 이어붙인 문구에는 낫표를 쓰지 않았다. 한국어 기계번역 자막의 어색한 띄어쓰기(예: 마침표 앞 공백 `습니다 .`), 오탈자, 고유명사 오기를 **교정하지 않고** 그대로 옮겼다.
> - [S3]와 [S4]는 영어 자막이다. 특히 **[S3] 원문에는 자막 줄바꿈 위치마다 HTML 엔티티 `&nbsp;`가 삽입되어 있다.** 아래 S3 인용문은 `&nbsp;`를 공백으로 치환한 것 외에 한 글자도 바꾸지 않았다. 기계적 대조 검증 시 이 치환을 적용해야 일치한다.
> - 논문 쪽수는 Raisch & Krakowski(2021, AMR 46(1):192-210) 기준이다.

---

### 9.1 소스 목록

| 태그 | 채널 | 업로드일 / 수집일 | 자막언어 | 단어수 | 발표 맥락 / 발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S1] | Siemens | **업로드일 2026-02-07** (채널 수집분) | ko | 약 2960개 | 웨비나/패널. 진행 「마리아 루트」(Siemens 글로벌 파트너 관리 책임자, 「산업용 소프트웨어 엣지-클라우드 통합 및 산업용 AI」 담당), AWS 측 「스리 엘라 프롤로」(AWS AI 혁신센터 책임자), Siemens 측 「호스 카이저 박사」(자막 내 「허스트」·「허스트 박사」로도 표기) | https://www.youtube.com/watch?v=EfYVIaGQwts | /home/user/youtube-scrap/transcripts/channels/Siemens/How_Physical_AI_is_Transforming_Industries_AWS_and_Siemens_o__EfYVIaGQwts.md |
| [S2] | Siemens | **업로드일 2026-07-17** (채널 수집분). 단, 본문상 촬영 시점은 **하노버 메세 현장**이며 업로드일보다 이르다(9.9 참조) | ko | 약 2439개 | 무대 대담. NVIDIA 「옴니버스 및 시뮬레이션 부문 부사장」(자막상 「레브 아레디안 목사님」, 뒤에서 「랄프」·「레프」·「브렛」으로도 표기), Siemens 「라이너 브레흠」(자막이 「디지털 인더스트리의 CEO」라 소개한 뒤 「사실 CTO입니다」로 정정) | https://www.youtube.com/watch?v=CAI_vn1lxhg | /home/user/youtube-scrap/transcripts/channels/Siemens/From_Analytic_to_Autonomous_How_Siemens_and_NVIDIA_Are_Trans__CAI_vn1lxhg.md |
| [S3] | Siemens | **업로드일 2026-02-12** (채널 수집분) | en | 약 4145개 | 스튜디오 대담. 진행 Magnus Edholm(Siemens), Brenda Discher(Siemens), Goetz Erhardt(Accenture, CEO of Industry X) | https://www.youtube.com/watch?v=nmaBILWJm_c | /home/user/youtube-scrap/transcripts/channels/Siemens/Agentic_and_Physical_AI_in_Manufacturing_Siemens_&_Accenture__nmaBILWJm_c.md |
| [S4] | Siemens | **업로드일 2026-03-24** (채널 수집분) | en | 약 11224개 | CEO 키노트. Roland Busch, Siemens RXD Summit **Beijing**. 게스트: Joe Tsai(Alibaba 회장), Wang Xingxing(Unitree 창업자·CEO), Prof. Ni Jun(CATL), 제품 담당 Fan Lele / Liu Hong / Yang Jingfan | https://www.youtube.com/watch?v=S3vM-v8cbjY | /home/user/youtube-scrap/transcripts/channels/Siemens/Industrial_AI_Is_Scaling_Now_Roland_Busch_Keynote_Siemens_RX__S3vM-v8cbjY.md |
| [S5] | Siemens | **업로드일 2026-06-19** (채널 수집분) | ko | 약 4756개 | CEO 키노트. 롤랜드 부쉬, VivaTech 2026 **Paris**. 게스트: 이사회 동료 「세드릭 니케」, Capgemini CEO(자막상 「이만」/「이몬」), ASML CEO 「크리스토프 푸케」 | https://www.youtube.com/watch?v=AvSNxD9GQH4 | /home/user/youtube-scrap/transcripts/channels/Siemens/Industrial_AI_in_Action_Roland_Busch_Keynote_VivaTech_2026_P__AvSNxD9GQH4.md |
| [S6] | Siemens | **업로드일 2026-07-12** (채널 수집분) | ko | 약 1387개 | 부스/세션 패널(전시장 현장, 「16번 홀에 있는 액센츄어 부스」 언급). Siemens 「카이 마이클」, BASF 「마테우스」(자막상 「마티아스」로도 표기, 「처리량 기술 및 실험실 자동화 분야의 책임자」), BASF 「카트린 콘」(「디지털 랩 프로세스 디자인 책임자」), Accenture 「카트린」(자막상 「캐스린」으로도 표기) | https://www.youtube.com/watch?v=Zhs5190nbV0 | /home/user/youtube-scrap/transcripts/channels/Siemens/Three_Key_Challenges_Limiting_Lab_Performance_—_and_How_to_S__Zhs5190nbV0.md |

**여섯 소스 모두 Siemens 자체 채널의 자체 발화**이다. 제3자 검증 소스는 이 사례에 **없다**. Accenture(S3, S6), NVIDIA(S2), AWS(S1), Capgemini·ASML(S5), Alibaba·Unitree·CATL(S4)은 모두 Siemens와 파트너 또는 고객 관계로 같은 무대에 오른 이해관계자다.

각 소스의 역할:
- **[S1] 1차 근거.** 이 사례의 핵심 주장(소프트웨어 정의 자동화 + 엔지니어링 코파일럿 30~40%, 완전 가상 PLC, 아우디 프라이빗 클라우드, 산업용 엣지, 자율 공장 연구소, 중소기업 데이터 제휴)이 한 곳에 모여 있는 유일한 소스.
- **[S2] 1차 근거.** 분석 → 보조 → 연기(acting) 3단계 자율성 단계론과 에를랑겐 「고객 0」 파일럿, 규칙 기반→목표 기반 전환 논거를 제공.
- **[S3] 보강.** 파트너(Accenture) 시각에서 인간이 어디에 남는지(유지보수 계획자, 이상현상 담당, 모델 훈련자)를 가장 명시적으로 말하는 소스. 고객 사례(Navantia, Keon) 수치 포함.
- **[S4] 1차 근거(수치).** CEO 키노트. Industrial AI 규모·조직·고객 성과 수치가 가장 많다.
- **[S5] 1차 근거(수치).** CEO 키노트. Eigen 엔지니어링 에이전트 성과, 에를랑겐 성과, 거버넌스 서술.
- **[S6] 대조군.** 공장이 아닌 **실험실**. 자동화/증강 배분이 과업 축이 아니라 **시간 축(주간/야간)** 으로 갈리는 유일한 사례.

---

### 9.2 조직과 문제 상황

**Siemens 자체 규모(모두 벤더 자체 보고치).**
- 역사: 「짐멘스는 175년 동안 존재해 왔고, 전기라는 기본 기술을 바탕으로 성장해 왔습니다.」 [S1] / S5는 전기 도입 이후 「150년이 지난 지금」이라 표현 [S5] — 두 수치가 다르다(9.9 참조).
- AI 인력·도메인: 「At Siemens, our one thousand five hundred AI experts and tens of thousands of engineers, they work across both worlds, the real and the digital world, with deep know-how across thirty industrial verticals.」 [S4]
- 설치 기반: 「One out of three manufacturing machines worldwide run on a Siemens controller. Approximately seventy percent of the world's electricity flows through grids planned or optimized using our software.」 [S4]
- 중국 조직: 「Twenty-six new products developed in China for China, engineered for scale, coming from our twenty-five thousand colleagues in this country.」 [S4]
- 플랫폼: 「in China, more than half a million users are registered on our open digital business platform. Almost two-thirds of the offerings are AI-related, and many come from Chinese partners.」 [S4]
- 투자: 「특히 저희 CEO인 롤랜드 부시가 두 달 전에 향후 몇 년 동안 미래 AI 역량 개발에 10억 달러 이상을 투자할 것이라고 발표했습니다」 [S1] (즉 2026-02-07 업로드분 기준 「두 달 전」 발표. 정확한 발표일은 해당 소스에 없음)
- 데이터 제휴: 「Nine of them have already joined us to create an international data alliance」 [S4] / 「저희는 최근 발표했듯이 여러 중소기업과 데이터 제휴를 맺었습니다.」 [S1] — 두 소스가 같은 제휴를 가리키는지는 **해당 소스들에 명시되어 있지 않다**.

**before 상태 1 — 자동화 엔지니어링이 느리고 반복적이다.**
「먼저, 제조 엔지니어들이 자동화 코드를 작성합니다. 이를 위해 그들은 TIA 포털에서 작업합니다.」 「이러한 환경에서 엔지니어는 모든 구성 요소를 구성합니다. 그들은 자신들이 하는 일을 문서화하고, 코드가 완벽하게 작동할 때까지 테스트하고 디버깅합니다 . 그리고 이것은 시간이 걸립니다, 아주 오랜 시간이요. 게다가 반복적인 작업이 많지만, 이제 상황이 바뀔 것입니다.」 [S5]

**before 상태 2 — 기존 자동화는 대량생산에만 경제성이 있다.**
「소량 생산이나 유연한 작업 처리가 필요한 경우에는 자동화 기술이 대량 생산에 맞춰 설계되었기 때문에 적합하지 않을 수 있습니다 . 그러니까, 예를 들어 10개 정도의 소량 생산을 자동화하려고 하면 투자 대비 수익률이 좋지 않다는 거죠. 차라리 수동으로 하는 게 낫습니다.」 [S2]
「하지만 알 수 없는 다른 문제가 발생하면 기계가 멈추므로 더 이상 자동화할 수 없습니다.」 [S2]

**before 상태 3 — 고도로 자동화된 공장에도 수작업이 남아 있다.**
「이곳은 세계 경제의 디지털 등대 역할을 하는 고도로 자동화된 공장이지만, 여전히 수작업이 많이 이루어지고 있습니다.」 [S2] (에를랑겐 공장)
「바로 생산 라인의 마지막 단계인 포장 작업입니다. 이 작업은 대개 수작업으로 이루어집니다.」 [S2]
「모든 공장에는 이와 같은 작업이 수백 가지씩 있습니다 . 지금까지는 자동화할 가치가 없다고 생각했던 작업들이 이제는 자동화되고 있습니다.」 [S5]

**before 상태 4 — 브라운필드 제약과 OT/IT 격차.**
「제조업 분야에서는 기존 제조업 인프라에 수천억 달러 또는 유로가 투자되어 있다는 점입니다 . 그것들을 전부 버리고 기술적으로나 기계적으로 더 유연한 접근 방식으로 새롭게 시작할 수는 없습니다.」 [S1]
「저희 회사는 OT 커뮤니티와 협력해 온 경험이 있는데, 이들은 기계 지향적인 기술자들로, 기계를 다루는 일을 합니다. 따라서 저희는 그들과 협력하여 컴퓨터 과학자들이 말하는 AI 기능에 대해 배우고 이해할 수 있도록 도와야 합니다.」 [S1]

**before 상태 5(대조군, 실험실) — 3대 제약** [S6]
「첫 번째 과제이자 첫 번째 핵심 제약 조건은 기존 실험실의 24시간 연중무휴 운영입니다 . 화학 실험실은 보통 주간 근무로 운영되지만, 물론 야간이나 주말에도 근무할 수 있다면 정말 좋겠습니다.」 / 「두 번째 과제는 모든 삶의 영역에서 흔히 관찰되는 표준화 부족입니다 .」 / 「세 번째 과제는 확장성과 적응성 부족으로 인해 자동화 솔루션에 대한 투자 수익률이 제한적인 경우가 많다는 점입니다.」
「그래서 오늘날 우리 연구실에 들어가 보면 완전히 산만하고 파편화된 IT/OT 환경을 발견하게 될 것입니다. 각 기기마다 의사 결정을 내리는 데 필요한 정보를 제공하는 서로 다른 데이터 모델이 제공됩니다.」 [S6]

**시장 규모 주장(모두 발화자 자체 인용, 제3자 검증 아님).**
- 「SNS Insider의 최신 보고서에 따르면, 현재 50억 달러 규모인 SNS 시장은 2033년까지 500억 달러로 성장할 것으로 예측됩니다. 이는 전년 대비 33%의 성장률입니다.」 [S1] — 자막이 「물리적 AI」 시장을 「SNS 시장」으로 오기한 것으로 보이나, **소스에 정정 표기는 없다**.
- 「전 세계 시장을 살펴보면 약 5조 달러 규모가 정보 기술 시장입니다.」 / 「100조 달러 규모의 물리적 산업들이 컴퓨팅의 기하급수적 성장으로부터 혜택을 받을 수 있게 되었습니다.」 [S2]
- Joe Tsai(Alibaba): 「the world economy is about a hundred and ten trillion U.S. dollars, and labor is approximately sixty percent of that. And roughly our estimate is two-thirds of that labor is white-collar knowledge workers. So you're looking at potentially almost fifty trillion dollars of potential value that could be either disrupted or enhanced」 [S4]

---

### 9.3 자동화 구간 (AUTO)

**(a) 물리 과업 — 포장·픽킹·용접검사.**
- 에를랑겐 포장: 「그러니까, 이 비닐봉투는 현재 사람이 가져다가 상자에 넣는다는 거죠. 그리고 미래에는 이 작업이 기계에 의해 수행될 것입니다. 이 경우에는 로봇 팔 두 개입니다.」 [S2]
  같은 과업을 S5는 이미 운영 서술로 말한다: 「예를 들어, 나사가 든 비닐봉지를 포장재에 넣는 것은 간단해 보입니다. 하지만 이러한 자루들은 유연하고, 잡기 어렵고, 모양이 예측 불가능하기 때문에 기존의 자동화 방식으로는 합리적인 비용으로 최고 수준의 품질 기준을 충족하면서 생산 현장에 필요한 작업을 처리할 수 없습니다. 물리 AI는 가능합니다.」 [S5] / 「두 개의 경량 로봇 팔, 최소한의 프로그래밍, 그리고 최대한의 유연성.」 [S5]
- 자기수정까지 기계가 수행: 「우리는 시스템이 물건이 올바르게 배치되지 않았을 경우 어떻게 해야 하는지 학습시켰고, 시스템은 이를 감지하고 스스로 수정합니다.」 [S5] / 「보시 다시피 로봇 팔이 무언가를 수정하고 있습니다. 상자 안에 무언가가 없어서 수정하고 있는 중입니다. 그러니까, 상황을 제대로 이해하고 그에 따라 행동하고 있는 겁니다.」 [S2]
- 청두 공장 픽킹: 「A similar industrial AI application is helping robots in our factory in Chengdu. The task: picking correct parts from a random pile to assemble industrial controllers. Very easy for humans, but really hard for robots. This industrial PC does the trick. Using three-D images, the AI guides and controls the robots to perform the job.」 [S4]
- 아우디 용접 검사(인간 불가 과업): 「In a factory of the car maker Audi, our industrial AI is checking the quality of welding seams, actually two thousands per minute. For humans, this task is impossible.」 [S4]

**(b) 기계 파라미터 조정 — 루프에서 인간 제외.**
「If a machine deviates from its target performance, this IPC detects and automatically adjusts the parameters to keep the machine and the whole system on track, and this is called inferencing. This is when AI works in operation at the edge. Models not only interpret data, but also trigger actions in real-time.」 [S4]
「We have software that allows us to let AI operate machines directly.」 [S4]

**(c) 엔지니어링 과업 자체의 자동화 — 에이전트.**
「우리는 그것을 아이겐 엔지니어링 에이전트라고 부릅니다. 그리고 단순히 제안만 내놓는 AI 챗봇이 아닙니다 . 이는 엔지니어링 작업을 처음부터 끝까지 완료하는 산업용 AI 에이전트입니다. 따라서 이 기능은 TIA 포털 내에서 작동하며 자율적으로 작동합니다. 결과물을 정의하시면 엔지니어링 담당자가 계획을 세우고, 관련 문서와 모든 데이터를 수집합니다. 이 도구는 컨트롤러용 실행 코드를 작성하고, 전체를 컴파일하고, 코드가 제대로 작동하고 오류 없이 컴파일되어 구현 준비가 완료될 때까지 반복적으로 유효성을 검사합니다.」 [S5]
확장 기능: 「이제 이 시스템은 전기 설계 도구의 도면을 기반으로 하며, 해당 정보를 TIA 포털에 자동으로 통합하여 모든 엔지니어가 바로 사용할 수 있도록 합니다. 예전에는 며칠씩 걸리던 수작업이 이제는 몇 분 만에 끝납니다.」 [S5]
그 결과 에이전트가 워크플로 상단으로 이동한다: 「이러한 기능 덕분에 당사 에이전트는 워크플로에서 더 상위 단계로 이동합니다.」 [S5]

**(d) 인프라의 탈물리화 — 완전 가상 PLC.**
「예를 들어, 저희는 최초의 완전 가상 PLC를 개발했습니다. 이 PLC는 더 이상 일반적인 PLC 박스에 담겨 있지 않고 클라우드 기반 환경에서 실행될 수 있습니다. 예를 들어, 저희 고객사인 아우디의 경우, 사내 프라이빗 클라우드에 설치되어 있지만, 명백히 클라우드 기반의 가상 PLC 환경입니다.」 [S1]

**(e) 실험실(대조군) — 야간 전면 자동화.**
「야간 근무 시 자율 로봇이 반복적인 작업 흐름을 완전히 대신 수행하여 연구실 운영이 24시간 내내 지속될 수 있습니다.」 [S6]

**(f) 창고 — 완전 무인 지향.**
「So the vision clearly is a lights out warehouse fully sort of almost autonomous in its operations from material which goes into the warehouse or pellets which go into depalitizing packaging outbound fulfillment.」 [S3] (「Keon」 = 자막상 표기)
「we see the first instances of dark warehouses or lights out warehouses we see the first instances of level four autonomous vehicles we see instances of fully software defined automation from a change in the recipe to the manufacturing line in seconds which took months to basically validate a change in the recipe」 [S3]

**(g) 자동화의 명시적 목적어가 「인간 노동력」인 대목.**
「그래서 물리적 AI가 지금 여기에 있는 이유는 인간 노동 자동화의 한계를 뛰어넘을 수 있는 엄청난 기회를 제공하기 때문입니다. 응. 그리고 이를 통해 인간 노동력을 대체하는 과정을 가속화할 수 있습니다.」 [S1]

---

### 9.4 증강 구간 (AUG)

**(a) 자동화를 설계하는 엔지니어 — 이 사례의 핵심 증강 지점.**
「그래서 기존의 함수 블록이나 다른 엔지니어링 도구들을 넘어서, 이제는 AI 기반 코파일럿이 코드를 훨씬 빠르게 생성하고 자동화 솔루션 엔지니어링에서 생산성을 30~40% 향상시킬 수 있도록 지원하는 고전적인 프로그래밍 언어 방식 의 접근법이 가능해졌습니다 . 그래서 이러한 보조 조종사들은 중요한 다음 단계이며」 [S1]
「we are developing industrial AI assistants specifically designed to transform industrial engineering from PLC programming to complex hardware configuration. This will significantly reduce engineering time, automate repetitive tasks, minimize errors, and allows engineers to focus on high value work.」 [S4]

**(b) 품질 검사에서 인간은 시정하는 자로 남는다.**
「Now, our AI alerts the experts immediately where they have to improve quality manually.」 [S4]
같은 라인을 다룬 S5는 기계 측 역할만 서술한다: 「이 장비는 저희 산업용 PC인데, 분당 2,000개의 용접 지점을 검사하고 있습니다 . 이 시스템은 클라우드에 학습된 AI 모듈을 탑재하고 있으며, 이 모듈은 엣지에서 실행됩니다.」 [S5] — 즉 **인간 전문가에게 알린다는 부분은 S4에만 있다**(9.9 참조).

**(c) 이상현상·검증 담당자로서의 인간(가장 명시적).**
「What you still need is people who work on anomalies which no one has detected yet.」 [S3]
「or making sure that the AI recommendations or the agentic AI in terms of the new maintenance plan is solid, is valid, is workable. But so you need more experience in working with meta data rather than the task itself.」 [S3]
「And you have a maintenance planner, typically very experienced people, done the job for 20 odd years. And they know how to basically best schedule different types of maintenance, which equipment goes there, which person can do the job, right? Where it has the right skill profile. But think about it. All is in the knowledge base of the customer.」 [S3]

**(d) 두 갈래 증강: 현장 작업자 vs 엔지니어.**
「There is shop floor workers which are enabled by AI, right? Yes. so you can use AI to diagnose problems and solve them quickly without sort of extensive training and experience that's a good thing right and then for the engineering side or the product development side what we what we clearly can see and will become more important is that people you need very skilled people to train those models.」 [S3]

**(e) 인간의 잔여 우위에 대한 명시적 주장.**
「인간은 가치 판단을 내리고, 제한된 자원을 어떻게 활용할지, 무엇이 가장 큰 가치를 가져다줄지 결정하는 데 있어서 항상 다른 인간보다 뛰어날 수밖에 없습니다. 이는 오직 인간만이 할 수 있는 일이며, 따라서 우리는 앞으로도 이 분야에서 항상 더 나을 것입니다 .」 [S2]
「여전히 직감이라는 것이 중요한데, 이는 우리 인간이 가진 본능적인 감각이지만, 인공지능은 확실히 학습 속도가 훨씬 빠릅니다.」 [S2]
「Now you still need good problem solving skills. You still need business acumen. You need to understand what is my company producing? What's the value of my company?」 [S3]
「Now, we do need human intelligence to make industrial AI work.」 [S4]

**(f) 도메인 전문가가 판단 주체라는 선언(논문 p.195와 직결).**
「But equally important is industrial domain know-how. This is where your knowledge and your expertise matters. You are in the best position to decide which data matters in your respective industry and how to cluster it to decide which AI application makes sense and which decision should rather remain in human hands.」 [S4]

**(g) 실험실(대조군) — 주간은 증강, 야간은 자동화.**
「예를 들어, 직원과 과학자들은 낮 시간 동안 지능형 로봇의 지원을 받아 혁신 및 연구와 같은 부가가치 창출 업무에 집중할 수 있습니다.」 [S6]
「그리고 가장 중요한 것은 단순히 연결만 되는 것이 아니라, 인간과 함께 작동해야 한다는 것입니다. 그리고 저희 Z 무브를 통해, 음, 저희는 정말로 사람들과 함께 협력하며 일할 수 있습니다 .」 [S6]

**(h) 인간-에이전트 신뢰가 증강의 전제조건.**
「인공지능 에이전트와 인간이 나란히 협력하는 것은 결코 간단한 일이 아닙니다. 왜냐하면 인간이 AI 에이전트를 신뢰하지 않으면 제대로 작동하지 않을 것이기 때문입니다 . 그러니까, 기본적으로 아무 소득 없이 돈만 낭비하는 셈이죠.」 [S5]
「우리는 업무를 효율적으로 수행하기 위해 직원과 AI 에이전트를 결합하고 있습니다 .」 [S5]

---

### 9.5 전환 메커니즘 (CYCLE)

**(a) 명시적 자율성 단계론 — S2가 제목대로 제시한다.**
「하지만 과거에는 인공지능이 주로 분석적인 측면에 집중되어 있었습니다. 그래서 우리는 여러 가지를 분석하고 최적화합니다 . 그건 마치 품질 검사 같은 거예요 . 하지만 이제 우리는 분석 단계를 지나 보조 단계로 넘어가고 있습니다. 어제 저희 Eigen 엔지니어링 에이전트를 출시했습니다. 네, 지금 바로 지원 또는 이미 작동 중입니다. 그리고 이제 연기적인 측면이 중요해진다고 생각합니다.」 [S2]
→ **분석(analytic) → 보조(assistive) → 행위(acting/autonomous)** 의 3단계. 자막이 acting을 「연기」로 오역했다(연극의 연기). 「하지만 연기란 실제 환경에서 진정으로 연기하는 것을 의미합니다 .」 [S2]

**(b) 단계 이행의 판정 기준 = 신뢰성 임계치.**
「제 말은, 산업 현장의 생산 능력은 높은 신뢰성을 의미하며 , 우리는 80% 같은 건 이야기하지 않는다는 겁니다 . 우리는 거의 100%에 가까운 신뢰성이 필요합니다 . 보안이 확보되어야 합니다. 실제 작동 중일 때도 운영자가 쉽게 사용할 수 있어야 합니다 .」 [S2]
「물리적 인공지능에서는 85% 정확도로는 충분하지 않기 때문입니다. 어떤 과정에서는 쉼표 뒤에 99까지 찍더라도 99.99% 정확해야 합니다.」 [S1]
「In industry, we need AI with one hundred percent reliability, and this is possible with the right technology stack, industrial domain know-how, and of course, with the right partners.」 [S4]
「따라서 환각은 산업용 인공지능에서 용납될 수 없습니다.」 [S5]

**(c) 단계 이행의 두 번째 기준 = ROI / 비용 임계치.**
「결론적으로, 우리는 이것을 개념 증명 차원에서 하는 것이 아닙니다 . 우리는 투자 수익을 원합니다 . 따라서 우리는 그것을 도입하는 것이 합리적일 수 있는 비용 수준에 도달해야 합니다.」 [S2]
「그리고 지금 우리가 함께 하는 일은 투자 대비 최고의 수익률을 가져오는 사용 사례가 무엇인지 파악하는 것입니다.」 [S2]

**(d) 규칙 기반 → 목표 기반으로의 통제 양식 전환.**
「하지만 이제 문제는, 시스템에 정확히 무엇을 어떻게 해야 하는지 지시해야 하는 규칙 기반 자동화 시스템이 아니라, 단순히 "이것을 하라"라고만 지시하고 생산량을 10개, 1000개 또는 1개로 설정할 수 있는 목표 기반 자동화 시스템으로 전환하는 경우입니다.」 [S2]
「그러므로 시스템에 어떻게 해야 할지 알려줄 필요가 없습니다 . 시스템에 무엇을 해야 하는지 알려주고 싶은 겁니다 . 그리고 해야 할 일은 시스템에 의해 자율적으로 실행됩니다.」 [S2]

**(e) 증강 학습이 시뮬레이션으로 이전된다(=인간 시연을 대체하려는 시도).**
「따라서 이러한 인공지능을 훈련시키는 방법은 기본적으로 물리적 세계를 시뮬레이션으로 재구성하여, 인공지능이 안전한 환경에서 물리적 세계의 행동 방식, 작동 방식, 사물을 이해하는 방식을 학습한 후 실제 환경에 배포하는 것입니다.」 [S2]
그러나 조작 과업은 아직 인간 데이터에 의존한다: 「However, under current conditions, for manipulation tasks — like having a robot pick up an object or assemble components — simulation isn't working well enough yet globally. In most cases, the industry worldwide is still relying on real humans to collect data and perform training for these tasks.」 [S4]
「Now I want to give this guy a particular task, and I see currently you need tele operations in order to train the robots somehow in the real world.」 [S4]

**(f) 파일럿 → 스케일 전환 실패가 명시적으로 문제화된다.**
「그래서 저는 산업 환경에서 인공지능을 도입할 때 겪게 되는 세 가지 함정을 꼽겠습니다 . 저는 그것들을 산업 AI 증후군이라고 부릅니다.」 [S5] — 「뿌리고 기도하는 증후군」, 「기초 증후군」, 「외로운 카우보이 증후군」 [S5]
「우리가 여기서 얻을 수 있는 교훈은 집중하고, 기반을 다지고, 가능한 한 많은 파트너십을 맺으면 일이 더 쉬워진다는 것입니다.」 [S5]
실험실판: 「자 , 먼저 조종 모드를 해제하세요. 로컬에 국한된 솔루션을 글로벌 확장이 가능한 플랫폼 기반 솔루션으로 대체하십시오.」 [S6] (「조종 모드」는 pilot mode의 오역)

**(g) 증강으로의 회귀(조건 변화 시)에 대한 명시적 서술은 없다.**
자동화된 과업을 조건 변화 때문에 다시 인간에게 돌려보냈다는 서술은 **여섯 소스 어디에도 없다**. 가장 근접한 것은 자동화 실패 시 인간이 붙어야 한다는 일반 진술뿐이다: 「What you still need is people who work on anomalies which no one has detected yet.」 [S3], 「But if I change the object even slightly, the success rate drops dramatically.」 [S4]

---

### 9.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

#### SPILL — **메타 수준에서 확인된다**

이 사례의 파급은 "과업 A 자동화 → 인접 과업 B 증강"이라는 논문의 기본형과, 그것의 **한 층 위** 형태를 함께 보여준다.

**(1) 공장 과업 자동화 → 그 자동화를 설계하는 엔지니어링 과업의 증강.**
자동화의 형태가 바뀌면(소프트웨어 정의) 그것을 만드는 엔지니어링 도구도 바뀐다는 인과가 한 문장에 들어 있다:
「자동화 모델을 더욱 소프트웨어 정의 자동화 아키텍처로 전환하여 AI 도구에 더욱 개방적이고 쉽게 접근할 수 있도록 함으로써 엔지니어링 프로세스를 더욱 빠르고 효율적으로 만들고, 제조 공정을 최적화하고자 합니다.」 [S1]
「저희는 IT에 훨씬 더 가까운 엔지니어링 도구 쪽으로 방향을 전환해 왔습니다 .」 [S1]
「The paradigm for the future is everything will be software defined and pervasive with agentic and physical AI.」 [S3]

**(2) 로봇 자동화 → 시뮬레이션 구축이라는 새 인접 과업 발생 → 그 과업이 다시 증강된다(2차 파급).**
「자, 우리가 직면한 문제는 물리적 세계의 여러 측면을 시뮬레이션할 수 있는 모든 기술을 보유하고 있음에도 불구하고 , 이러한 시뮬레이션을 구축하고, 시뮬레이션 대상 세계를 만들고, 그것을 정확하게 만드는 작업은 실제로 매우 많은 인력이 투입되는 작업이라는 점입니다. 마치 우리가 공장에서 하는 일과 비슷하죠 .」 [S2]
「음, 애초에 시뮬레이션을 설정하는 것조차 세계적으로 극소수의 전문가가 필요합니다 . 이제 처음으로 그 병목 현상을 실제로 제거해주는 기술을 갖게 되었습니다 . 이러한 AI 에이전트, 즉 코딩 에이전트는 기본적으로 우리 모두가 소프트웨어를 개발할 수 있는 초인적인 능력을 갖도록 해주는 것인데 , 이는 시뮬레이션을 구축하고 앞으로 나아가는 데 도움을 줄 시뮬레이션 전문가를 만드는 데 필요한 기술과 정확히 동일합니다.」 [S2]
→ 공장 자동화가 시뮬레이션 구축이라는 **새 인간 노동**을 낳고, 그 노동이 다시 코딩 에이전트로 증강되는 연쇄. 논문의 spillover(p.197)가 한 단계가 아니라 **재귀적으로** 일어난다.

**(3) 자동화 도구 자체를 만드는 회사의 제품 개발이 자기 도구로 가속된다(자기참조적 파급).**
「And the second, I need thanks to our Siemens advanced digital software to help us design and the simulator. This also give us the faster speed.」 [S4] (S7-200 SMART G2 PLC 개발, 9개월 / 「twice as faster than before」)
「The complex in Nanjing was designed, tested, and optimized entirely in the virtual world before a single brick was laid. We used our own technology to make that possible in record time.」 [S4]

**(4) OT 자동화 → IT/OT 경계 인력의 역할 변화.**
「음, 그래서 이것이 바로 고전적인 OT 영역에서 고전적인 IT 기반 환경으로 연결되는 전형적인 다리라고 할 수 있습니다.」 [S1]
「하지만 다른 한편으로는 , AI 전문가들과 협력하여 고객들이 이 여정에 함께 참여할 수 있도록 인내심을 갖고, 기존 OT 환경에 AI 도구를 적용할 때 얻을 수 있는 모든 기능을 진정으로 활용할 수 있도록 도와야 합니다.」 [S1]

**(5) 자동화가 인접 과업의 인간 역량 요건을 바꾼다(과업→메타데이터로 이동).**
「But so you need more experience in working with meta data rather than the task itself.」 [S3]

**(6) 학습 결과의 사이트 간 파급(공간축의 문자 그대로의 사례, 대조군).**
「게다가 물리적 AI는 디지털 트윈을 기반으로 학습할 수 있으며, 하드웨어에 구애받지 않는 학습 결과를 동일한 작업을 수행하는 다른 사이트에서도 로컬로 재사용할 수 있습니다.」 [S6]

#### REINV — 확인된다(단, 재무 자원 재투자가 아니라 **시간 자원** 재투자)

- 「그리고 동료들은 자신들의 전문 지식이 정말로 필요한 업무에 더 많은 시간을 할애할 수 있게 됩니다 .」 [S5] — 포장 물리AI 자동화 직후에 나오는 문장. UBS 패턴(p.201)과 구조가 같다.
- 「allows engineers to focus on high value work」 [S4]
- 「예를 들어, 직원과 과학자들은 낮 시간 동안 지능형 로봇의 지원을 받아 혁신 및 연구와 같은 부가가치 창출 업무에 집중할 수 있습니다.」 [S6]
- 경영자 수준의 같은 논리(Joe Tsai): 「the CEO's most scarce resource is bandwidth, is time.」 「But now with agents, you actually can manage so many more things, and it also frees you to think about strategic issues and things, you know, that's about the future of the company.」 [S4]
- ASML CEO의 같은 논리: 「그래서 저희는 엔지니어들이 시간을 온전히 혁신에 집중하기를 바랍니다. 그러므로 그런 일들을 관리하는 데 드는 시간을 최대한 줄여야 합니다.」 [S5]
- 재무적 재투자 선언: 「향후 몇 년 동안 미래 AI 역량 개발에 10억 달러 이상을 투자할 것」 [S1] — 다만 이 투자가 **자동화로 절감한 자원에서 나왔다는 서술은 소스에 없다**. UBS 패턴으로 해석하려면 근거가 부족하다.

---

### 9.7 통합 장치 (RESP)

**(a) 의사결정 권한의 명시적 유보.**
「You are in the best position to decide which data matters in your respective industry and how to cluster it to decide which AI application makes sense and which decision should rather remain in human hands.」 [S4]

**(b) 감사·추적성 설계.**
- Sanofi(제약, 규제산업): 「이 시스템은 수기로 작성된 종이 기록이 아닌 전자식 배치 기록을 보관합니다 .」 「이는 무엇이 필요한지를 보여줍니다. 실제로 일어나는 일을 기록합니다. 이 책은 모든 사람을 단계별로 안내합니다.」 [S5]
- Navantia(방산 조선): 「This is where you need to track and trace stuff through production. You need to have the workers in the shipyard very well equipped with all the necessary information to assemble, to weld, to do all the things, traceability, anything that's needed.」 [S3]
- 실험실: 「따라서 이러한 비즈니스 계층을 구현함으로써 수직적 및 수평적 추적성이 설계 단계부터 내재화됩니다.」 [S6]

**(c) 에이전트 거버넌스 — 이 사례에서 가장 구체적인 통합 장치.**
「그다음은 AI 에이전트를 배포하는 것입니다. AI 에이전트는 인간의 디지털 작업자입니다. 그러기 위해서는 매우 강력한 통치력이 필요합니다. 매우 뛰어난 제어 메커니즘이 필요합니다. 그리고 매우 강력한 운영 모델이 필요합니다 . 그렇지 않으면 마치 수백 명의 직원을 회사 전체에 통제 없이 마음대로 행동하도록 내버려 두는 것과 같습니다 . 만약 이러한 에이전트들을 관리할 수 있는 적절한 거버넌스 체계가 없다면 회사에 혼란이 초래될 것입니다. 아시다시피, 우리는 이러한 모든 AI 에이전트를 어떻게 관리할 것인지에 대한 제어 평면에 대해 이야기합니다.」 [S5]
데이터 접근 통제 문제도 같은 맥락에서 제기된다: 「because we now see agents getting too much data, and then they start to act in a very way that's uncontrollable. But that's very important, is to have the access to data and how do you control that access and make the agent smarter that way.」 [S4]

**(d) 제3자 인증 — 이 사례에서 유일하게 외부 기관이 등장하는 지점.**
「이 시설은 독일에서 유일하게 TÜV 인증을 받았기 때문에, 미래가 아닌 바로 지금, 미래에 진정한 의미의 자율 연구실을 운영할 수 있는 기반이 됩니다.」 [S6]
단, 무엇이 인증 대상인지(시설인지 플랫폼인지)는 자막이 모호하다.

**(e) 감독(supervision) 개념.**
「카트린, 적절한 자동화와 AI 감독이 있다면 기존 연구실의 판도가 바뀔 수도 있다는 점에 전적으로 동의해요.」 [S6]
「인공지능의 감독 하에, 나아가 인공지능에 의해 주도되는 시스템이어야 하며, 무엇보다 중요한 것은 대규모 운영에 맞춰 설계되어야 한다는 점입니다.」 [S6]
→ 주의: 이 문장의 「감독」 주체는 **AI**다(AI가 감독). 인간 감독이 아니다. (d)의 인간-루프 서술과 방향이 반대이며, 같은 소스 안에서 인간 감독/AI 감독이 혼재한다.

**(f) 책임의 무게에 대한 인식.**
「Right. So the industrial agent better gets it right.」 [S4]
「And then the other thing is the agent is rationalizing. Right. It has a memory, but very important, it finally acts on your behalf.」 [S4]
「하지만 한 가지 명심해야 할 점은 고객이 우리의 첫 번째 애플리케이션을 사용하면서 얻는 신뢰와 구체적인 실제 경험에 대해 신중해야 한다는 것입니다.」 [S1]
「왜냐하면 우리 모두가 알다시피 신뢰는 아주 빨리 잃지만, 어렵게 얻어야만 얻을 수 있기 때문입니다.」 [S1]
「하지만 특히 물리적 AI 분야에서는 과도한 약속을 하지 않도록 주의해야 합니다. 그렇지 않으면 엄청난 역효과를 초래할 수 있습니다.」 [S1]

**(g) 규제 측면(외부 통합 장치).**
「인공지능법에 있어서 규제가 소비자 데이터 등을 규제하는 방식과 동일하게 기계를 규제하지 않는다는 점에서 우리는 성공적이라고 말할 수 있습니다 .」 [S5]
「왜냐하면 개인 데이터와 기계 데이터는 다르게 취급해야 하기 때문입니다.」 [S5]

**없는 것**: 자동화된 의사결정에 대한 **개별 승인권(human sign-off) 절차**, 이의제기·롤백 절차, 책임 귀속 규정에 대한 구체적 서술은 여섯 소스 어디에도 **없다**.

---

### 9.8 성과 수치

모두 **벤더(Siemens) 또는 그 파트너의 자체 보고치**다. 이 사례에 제3자 검증치는 TÜV 인증 언급([S6], 성과 수치 아님)과 세계경제포럼 등대공장 선정([S4], 성과 수치 아님)뿐이다.

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| 자동화 솔루션 엔지니어링 생산성 (AI 코파일럿) | 명시 없음 | 「30~40% 향상」 | [S1] 2026-02-07 | 자체보고 |
| 엔지니어링 단계 효율 (industrial AI assistants) | 명시 없음 | 「efficiency gains of up to forty percent in the engineering phase」 | [S4] 2026-03-24 | 자체보고(「up to」) |
| Eigen 엔지니어링 에이전트 생산성 | 명시 없음 | 「생산성 50% 향상」 | [S5] 2026-06-19 | 「고객들의 피드백」으로 귀속, 고객명 없음 |
| Eigen 에이전트 개발 속도 | 명시 없음 | 「개발 속도 2.5배 증가」 | [S5] | 동일 |
| Eigen 에이전트 품질 | 명시 없음 | 「품질 80% 향상」 | [S5] | 동일 |
| 전기설계 도면 → TIA 포털 통합 소요 | 「예전에는 며칠씩 걸리던 수작업이」 | 「이제는 몇 분 만에 끝납니다.」 | [S5] | 자체보고 |
| 프레임워크 준수 소프트웨어 구조 도출 | 「수백 페이지 분량의 문서와 수천 개의 규칙」 | 「그리고 다시, 몇 분 안에.」 | [S5] | 자체보고 |
| 에를랑겐 공장 — 가동 AI 알고리즘 수 | 명시 없음 | 「현재까지 100개의 AI 알고리즘이 생산 현장에서 활용되고 있습니다 .」 | [S5] | 자체보고 |
| 에를랑겐 — 제품 출시 기간 | 명시 없음 | 「제품 출시 기간 40% 단축」 | [S5] | 자체보고(자사 공장) |
| 에를랑겐 — 에너지 소비 | 명시 없음 | 「에너지 소비량 42% 절감」 | [S5] | 자체보고(자사 공장) |
| 에를랑겐 — 생산성 | 명시 없음 | 「생산성 69% 향상」 | [S5] | 자체보고(자사 공장) |
| PepsiCo 단일 설비 효율 | 명시 없음 | 「increased efficiency by twenty percent in a single facility within three months」 | [S4] | 자체보고(「our pilot customer」) |
| Navantia 생산성 | 명시 없음 | 「20% improvement in productivity」 | [S3] | Siemens/Accenture 자체보고 |
| Navantia 비용 | 명시 없음 | 「20% less cost, better quality, better faster time to market」 | [S3] | 동일 |
| 아우디 용접 검사 처리량 | 「For humans, this task is impossible.」 | 「two thousands per minute」 / 「분당 2,000개의 용접 지점을 검사하고 있습니다」 | [S4], [S5] | 자체보고, 2개 소스 일치 |
| Latitude(프랑스 스타트업) 납기 | 「기존의 여러 도구를 조합해서 사용하던 방식에서」 | 「프로젝트 납기가 6개월 단축되고 엔지니어링 효율성이 15% 향상되었습니다.」 | [S5] | 자체보고(고객 사례) |
| Simcenter Simsolid 구조 계산 속도 | 「모델 하나를 제작하고 시뮬레이션하는 데만 몇 주가 걸렸습니다.」 | 「30배 더 빠르게 수행할 수 있습니다.」 | [S5] | 자체보고(신제품 발표) |
| Sanofi 배치 생산 | 명시 없음 | 「배치 생산 감소에서 70%의 이점」 | [S5] | Capgemini/Siemens 자체보고 |
| Sanofi 편차 | 명시 없음 | 「편차 감소에서 80%의 이점」 | [S5] | 동일 |
| NVIDIA 협업 — 칩 설계 SW | 명시 없음 | 「speeding up workflows of up to ten times」 | [S4] | 자체보고 |
| NVIDIA 협업 — 시뮬레이션 SW | 「일반적으로 이러한 계산에는 며칠이 걸립니다.」 [S5] | 「accelerating our simulation software with Nvidia technology and AI hundred thousand fold」 [S4] / 「10배, 100배, 심지어는 1,000배 더 빠르게」 [S5] / 「GPU에서 실행되도록 코드를 다시 작성하여 속도를 10만 배 향상시켰습니다」 [S5] | [S4], [S5] | 자체보고, **같은 소스 내 수치 불일치**(9.9) |
| 3VD 차단기(신제품) | 「traditional AC architecture requires a lot of AC/DC conversions」 | 「save the space by thirty percent, reduce the corporate consumption by forty-five percent」, 「twenty percent smaller in size」, 「thirty percent faster in installation」, 「eight hundred volt applications」 | [S4] | 자체보고, 「corporate consumption」은 자막 오류로 보임 |
| 3VD 개발 리드타임 | 「from the project initiation to the product launch」 | 「forty percent faster than before」 | [S4] | 자체보고 |
| S7-200 SMART G2 PLC 개발 리드타임 | 명시 없음 | 「we only use nine months. That means we are twice as faster than before.」 | [S4] | 자체보고 |
| 실험실 자산 활용률 | 「화학 실험실은 보통 주간 근무로 운영되지만」 | 「그렇게 되면 현재 활용률이 두 배로 늘어날 수 있는데」 | [S6] | BASF 발화, **기대치**(「늘어날 수 있는데」) |
| 실험실 구현 시간 | 명시 없음 | 「또한 구현 시간을 60% 증가시킵니다.」 | [S6] | 자체보고. **자막 오류 의심**(맥락상 단축이어야 함) |
| CATL 배터리 불량 기준 | 「Translate into a common language, that mean out of one million product, you are allowed to have two to three non-conforming, but that's already the best in class.」 | 「We require part per billion, B, start with B.」 | [S4] | CATL 자체보고(Siemens 성과 아님) |
| ASML 장비 가동률 | 「당신은 차를 아마 1~2% 정도만 운행할 거예요 .」 | 「거의 항상, 95%의 시간 동안 작동합니다.」 | [S5] | ASML 자체보고 |

---

### 9.9 소스 간 교차 대조

#### (1) 반복 확인된 사실

| 사실 | 소스 | 비고 |
|---|---|---|
| 아우디 용접 검사 분당 2,000점, 산업용 PC + NVIDIA GPU, 클라우드 학습·엣지 추론 | [S4] 2026-03-24, [S5] 2026-06-19 | 수치·구성 모두 일치. 단 S4에만 「our AI alerts the experts immediately where they have to improve quality manually」가 있다 |
| 에를랑겐 공장이 AI 기반 자율생산의 첫 사례 | [S2], [S5] | S2 「에를 랑겐에 있는 우리 공장을 인공지능 기반 자율 생산 시설의 첫 번째 사례로」 / S5 「이 공장을 세계 최초의 완전 인공지능 기반 생산 시설로 바꾸고 있습니다」 |
| 비닐봉지 포장 과업 = 물리AI 첫 대표 사례, 로봇 팔 2개, 자기수정 | [S2], [S5] | 동일 과업을 다른 무대에서 반복 |
| 산업용 AI는 100%에 가까운 신뢰성을 요구 | [S1]「99.99%」, [S2]「거의 100%」, [S4]「one hundred percent reliability」, [S5]「따라서 환각은 산업용 인공지능에서 용납될 수 없습니다.」 | 4개 소스가 같은 논리 |
| 소프트웨어 정의 자동화가 방향 | [S1], [S3], [S6] | S3 「everything will be software defined」, S6 「소프트웨어 정의 자동화 개념을 지원하므로」 |
| NVIDIA가 계산·시뮬레이션, Siemens가 물리세계 적용이라는 역할 분담 | [S2], [S4], [S5] | S2 「저희는 컴퓨터 과학의 어려운 부분을 담당하고, 지멘스는 저희의 컴퓨터 과학 기술과 컴퓨터를 물리적 세계에 적용하여 산업계의 문제를 해결합니다」 |
| 파트너십 없이는 스케일 불가 | [S1], [S3]「It takes a village.」, [S4], [S5]「외로운 카우보이 증후군」, [S6] | 전 소스 공통 |
| BMW 풍동/공기흐름 시뮬레이션 | [S4], [S5] | S4 「the simulation of airflow around a new BMW electric vehicle」 / S5 「여기 보이는 것은 BMW의 풍동 시뮬레이션입니다.」 |
| KION(자막상 「Keon」/「KN」) 물류 고객 | [S3], [S5] | S5 「KN을 데려오세요. 선도적인 물류 회사로서, 그들의 지게차와 자동화 차량은」 — 동일 고객으로 보이나 자막 표기가 달라 **동일성은 추정**이다 |
| Accenture가 파트너 | [S3], [S6] | S3는 「Accenture Siemens business group」 발표, S6는 실험실 프로젝트 3자 구도 |
| 조립·파지의 일반화 실패 = 미해결 병목 | [S3]「anomalies which no one has detected yet」, [S4] Unitree「if I change the object even slightly, the success rate drops dramatically」 | 벤더 측과 로봇 제조사 측이 같은 한계를 지목 |

#### (2) 한 소스에만 있는 사실

- **완전 가상 PLC와 아우디 프라이빗 클라우드 배치**: [S1]에만 있음. S4·S5는 아우디를 용접 검사 사례로만 언급하고, 가상 PLC를 **전혀 언급하지 않는다**.
- **자율 공장 연구소**: 「예를 들어, 저희는 최신 기술 개발을 항상 시험해 볼 수 있는 자율 공장 연구소를 보유하고 있습니다 .」 [S1]에만 있음. 위치·규모·인원은 소스에 없음.
- **중소기업 데이터 제휴**: [S1]에만 서술. [S4]의 「international data alliance」와 참여사 「Nine of them」은 [S4]에만 있음. 두 언급의 관계는 **소스에 없음**.
- **Xcelerator 액셀러레이터 마켓플레이스**(자막상 「ZIT 액셀러레이터」/「ZTH 액셀러레이터」): [S1]. [S4]는 「Siemens Xcelerator marketplace」로 정상 표기.
- **AWS 협업 구체안**(Bedrock 위 로우코드 실행, IoT SiteWise Edge ↔ 산업용 엣지): [S1]에만 있음.
- **AWS 물리AI 펠로우십 프로그램**(NVIDIA·「매스 로보틱스」와, 1기 완료, 2기 접수 중): [S1]에만 있음.
- **에이전트 4종 분업 구조**(product agent / machine agent / real-time data agent / problem-solving agent): [S4]에만 있음.
- **Eigen 엔지니어링 에이전트의 정량 성과(50%/2.5배/80%)와 두 신기능**: [S5]에만 있음. [S2]는 출시 사실만 언급.
- **산업 AI 증후군 3종과 「원단」(fabric)**: [S5]에만 있음. 「우리는 그것을 기본적으로 원단이라고 부릅니다. 우리는 모든 사람이 동일한 구조적 역량을 갖추도록 강제하고 있으며」 [S5]
- **에이전트 거버넌스/제어 평면 논의**: [S5]에만 있음.
- **Navantia / Clorox / Keon 사례**: [S3]에만 있음. Clorox는 진행자가 물었으나 답변자가 「I'm not sure what the case refers to.」라고 답해 **사례 내용이 확정되지 않았다** [S3].
- **PepsiCo 20%/3개월**: [S4]에만 있음.
- **Foxconn 데이터센터 디지털트윈**: [S4]에만 있음.
- **Gravity 마르세유 친환경 제철소 22억 유로 / Sanofi 스마트 운영 / Latitude / ASML Teamcenter 2만 부품**: [S5]에만 있음.
- **실험실 3대 제약, Z-Move 오케스트레이션, TÜV 인증, 주간/야간 분업**: [S6]에만 있음.
- **Unitree / CATL / Alibaba Qwen / 3VD / S7-200 SMART G2 / 난징·청두 등대공장**: [S4]에만 있음.

#### (3) 시점에 따른 서술 변화 (핵심 대조)

**엔지니어링 생산성 수치가 4개월 사이에 30~40% → 40% → 50%로 상승하며, 동시에 지칭 대상이 바뀐다.**

| 시점(업로드일) | 소스 | 기술 명칭 | 수치 | 성숙도 표현 |
|---|---|---|---|---|
| 2026-02-07 | [S1] | 「AI 기반 코파일럿」 / 「보조 조종사들」 | 「30~40% 향상」 | 「이러한 보조 조종사들은 중요한 다음 단계이며」 — 이미 가능 |
| 2026-03-24 | [S4] | 「dozens of industrial AI co-pilots」는 기구축, 「industrial AI assistants」는 개발 중 | 「up to forty percent」 | 「The next step, we are developing」 — **개발 중** |
| 2026-06-19 | [S5] | 「아이겐 엔지니어링 에이전트」 | 「생산성 50% 향상, 개발 속도 2.5배 증가, 품질 80% 향상」 | 「두 달도 채 되지 않은 시점에, 저희는 산업 자동화를 위한 혁신적인 AI 제품을 출시했습니다 .」 + 「고객들의 피드백은 어떻습니까 ?」 |
| (하노버 메세 현장, 업로드 2026-07-17) | [S2] | 「Eigen 엔지니어링 에이전트」 | 수치 없음 | 「어제 저희 Eigen 엔지니어링 에이전트를 출시했습니다.」 |

→ **코파일럿(증강 도구) → 어시스턴트 → 에이전트(자율 실행)** 로 명칭과 자율성 수준이 함께 올라간다. 즉 [S1]의 30~40%와 [S5]의 50%는 **같은 것의 갱신치가 아니라 다른 제품의 수치**일 가능성이 높다. 그러나 어느 소스도 이를 명시적으로 구분해 주지 않으므로, 30~40%가 재확인되었다고 말할 수 없다. **재확인되지 않았다**가 정확한 답이다.

**[S2]의 촬영 시점 문제.** [S2] 업로드일은 2026-07-17이지만, 본문은 하노버 메세 현장이고 「어제 저희 Eigen 엔지니어링 에이전트를 출시했습니다」라고 한다. [S5](2026-06-19)는 그 출시를 「두 달도 채 되지 않은 시점에」라고 한다. 따라서 **[S2]의 발화 시점은 업로드일보다 약 2개월 이상 이르다.** 채널 수집분의 「업로드일」을 발화 시점으로 쓰면 이 사례의 시간 순서가 뒤집힌다. [S2]는 또 「그건 저희가 특히 그 분야에서 연구하고 있다고 1월 CES에서 발표했던 내용입니다」라고 하여 CES 발표가 선행함을 보여준다.

**에를랑겐 서술의 시제 변화.** [S5](2026-06-19)는 100개 알고리즘·40/42/69%를 **이미 달성된 수치**로 제시하고 포장 물리AI도 운영 서술로 말한다. 반면 [S2](발화 시점은 그보다 이름)는 「미래에는 이 작업이 기계에 의해 수행될 것입니다」, 「고객 0의 입장에서」로 **파일럿** 성격을 강조한다. 발화 시점 순서(S2 → S5)를 따르면 파일럿→운영으로 일관되지만, 업로드일 순서(S5 → S2)로 읽으면 운영→파일럿으로 역행하는 것처럼 보인다. 이 사례에서 시점 표기가 결론을 바꾸는 지점이다.

**자동화가 인간을 대체한다는 어조의 변화.** [S1](2026-02-07)은 「인간 노동력을 대체하는 과정을 가속화할 수 있습니다」라고 직설한다. [S5](2026-06-19)는 같은 자동화를 「동료들은 자신들의 전문 지식이 정말로 필요한 업무에 더 많은 시간을 할애할 수 있게 됩니다 .」로 프레이밍한다. 대상 청중(파트너 웨비나 vs 공개 키노트)이 다르므로 순수한 시간적 변화로 단정할 수 없다.

#### (4) 모순 / 불일치

1. **회사 연혁**: [S1] 「175년 동안 존재해 왔고」 vs [S5] 「150년이 지난 지금」. S5의 「150년」은 전기 도입 이후 경과 연수를 가리키는 문맥이므로 직접 모순은 아니지만, 두 수치가 병존한다.
2. **시뮬레이션 가속 배수**: [S4] 「hundred thousand fold」(10만 배), [S5] 「10배, 100배, 심지어는 1,000배 더 빠르게」와 「속도를 10만 배 향상시켰습니다」가 **같은 소스 안에 공존**한다. 대상 소프트웨어가 같은지 다른지 소스에 명시 없음.
3. **감독의 주체**: [S6] 「적절한 자동화와 AI 감독이 있다면」·「인공지능의 감독 하에, 나아가 인공지능에 의해 주도되는 시스템이어야 하며」 = AI가 감독. vs [S4] 「which decision should rather remain in human hands」 = 인간이 결정. 통합 조건(RESP)의 방향이 소스 간에 반대다.
4. **코파일럿의 지위**: [S1]·[S4]는 코파일럿을 인간 보조로 위치시키지만, [S4] 내부에서 Joe Tsai는 「in the future with very smart agents, they become the main pilot, not the co-pilot.」이라 말하고 Roland Busch가 「Exactly.」로 동의한다. 즉 **증강 도구의 정체성이 같은 키노트 안에서 뒤집힌다.**
5. **자율성 도달 시점**: [S2] 「변곡점은 이미 도달했다고 생각해요.」(S1의 발화) vs [S1] 「저희는 물리적 AI가 아직 초기 단계에 있다고 생각하며」(AWS 측 발화). 같은 소스 [S1] 안에서 두 발화자가 반대로 말한다.
6. **실험실 구현 시간 60%**: 「또한 구현 시간을 60% 증가시킵니다.」 [S6] — 문맥(위험 감소, 확장성)상 단축이어야 하나 자막은 「증가」다. 어느 방향인지 **소스만으로는 확정 불가**.
7. **Clorox 사례**: 진행자가 보안 사례로 제시했으나 Accenture 측이 「I'm not sure what the case refers to.」라고 답했다 [S3]. 이 사례는 **내용 없이 이름만 남았다**.
8. **직함 정정**: [S2]는 라이너 브레흠을 「디지털 인더스트리의 CEO」로 소개한 뒤 곧바로 「사실 CTO입니다, 라이너 씨, 죄송하지만」으로 정정한다. 귀속 인용 시 주의.

---

### 9.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO = 기계가 과업 인계, 인간 루프 제외 (p.194) | 포장·픽킹·용접검사·야간 실험실·파라미터 자동조정. 「이 작업이 기계에 의해 수행될 것입니다」[S2], 「automatically adjusts the parameters」[S4], 「자율 로봇이 반복적인 작업 흐름을 완전히 대신 수행하여」[S6] | **지지** |
| AUG = 인간이 루프에 남아 기계와 밀착 협업 (p.194) | 「AI 기반 코파일럿」[S1], 「our AI alerts the experts immediately where they have to improve quality manually」[S4], 「저희는 정말로 사람들과 함께 협력하며 일할 수 있습니다 」[S6] | **지지** |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | 「하지만 이제 우리는 분석 단계를 지나 보조 단계로 넘어가고 있습니다.」 그리고 「그리고 이제 연기적인 측면이 중요해진다고 생각합니다.」 = 분석→보조→연기(acting) 3단계 [S2]. 견고화 판정 기준이 정량 임계치로 제시됨: 「거의 100%에 가까운 신뢰성」[S2], 「99.99%」[S1] | **보강** — 논문이 서술적으로만 둔 이행 조건에 **정량적 게이트(신뢰성 임계치 + ROI 임계치)** 를 제공 |
| CYCLE: 조건 변화 시 증강 회귀 (p.196-197) | 자동화된 과업을 인간에게 되돌린 사례가 **없음**. 「if I change the object even slightly, the success rate drops dramatically」[S4]는 회귀 필요성을 암시하나 실제 회귀 서술은 없음 | **미확인**(반증도 지지도 아님). 벤더 채널이라는 소스 편향 가능성 |
| SPILL: 한 과업 자동화가 인접 과업의 증강을 유발 (p.197) | ① 공장 자동화의 소프트웨어화 → 엔지니어링 과업 증강[S1][S3] ② 로봇 자동화 → 시뮬레이션 구축이라는 새 인간 과업 발생 → 그 과업이 코딩 에이전트로 재증강[S2] ③ 자동화 벤더가 자기 도구로 자기 제품을 개발[S4] | **확장** — 파급이 1회가 아니라 **재귀적**이며, 대상이 현장 과업이 아니라 자동화를 만드는 과업이라는 **메타 수준**에서 일어남 |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS) | 「동료들은 자신들의 전문 지식이 정말로 필요한 업무에 더 많은 시간을 할애할 수 있게 됩니다 」[S5], 「allows engineers to focus on high value work」[S4], 「부가가치 창출 업무에 집중」[S6], CEO의 bandwidth 논리[S4] | **지지(부분)** — 다만 재투자되는 자원이 **자본이 아니라 시간**이다. 10억 달러 투자[S1]가 자동화 절감분에서 나왔다는 근거는 없음 |
| RESP: 인간이 프로세스 전체 책임/승인/감사 보유 (p.200) | 「which decision should rather remain in human hands」[S4], 전자식 배치 기록[S5], 추적성 내재화[S6], 에이전트 거버넌스·제어 평면[S5], TÜV[S6] | **부분 지지 + 부분 반증** — 개별 승인권 절차는 없고, [S6]은 오히려 「인공지능의 감독 하에」를 목표로 제시 |
| p.195: 증강 학습은 도메인 전문가의 암묵지에 의존, IT부서/외부업체에 위임 불가 | 「You are in the best position to decide which data matters in your respective industry」[S4]; 「you need very skilled people to train those models」[S3]; 유지보수 계획자 20년 경력[S3]; 「그들은 해당 분야에 대한 전문 지식이 없습니다. 그들은 맥락에 대한 이해가 부족하고, 데이터를 기반으로 훈련해야 합니다.」[S5] | **강한 지지**. 단 **부분 반증**도 있다: Accenture 7,000명 투입[S3], Capgemini 배포 역량[S5], 「액센츄어는 기술과 비즈니스를 확장 가능한 디지털 아키텍처, 데이터, 클라우드 및 AI 인프라에 연결하여 혁신을 이끌어내고, 시범 프로젝트를 전사적 솔루션으로 전환하는 데 필요한 역량을 제공합니다 」[S6] — 즉 실제로는 **외부 컨설팅에 대규모 위임**이 일어나고 있다 |
| p.198 한계1: 목적/자아 부재 | 「인간은 가치 판단을 내리고, 제한된 자원을 어떻게 활용할지, 무엇이 가장 큰 가치를 가져다줄지 결정하는 데 있어서 항상 다른 인간보다 뛰어날 수밖에 없습니다.」[S2]; 「You still need business acumen.」[S3]; 「Now, we do need human intelligence to make industrial AI work.」[S4] | **지지**. 단 Joe Tsai의 「main pilot」·「CEO agent」 논의[S4]는 이 경계를 밀어붙인다 |
| p.198 한계2: 제약 완화된 옵션만 제시 | ASML 대목이 정반대 방향으로 대응한다: 「이제 저희는 고객님의 기존 디자인을 기반으로 소프트웨어를 학습시켜 새로운 디자인과 아이디어를 창출하고자 합니다.」 「하지만 그래도 상자에 넣어둬야겠죠. 그래서 우리는 이것을 물리 기반 시뮬레이션이라고 부릅니다. 왜냐하면 물리 법칙이 한계를 알려주기 때문입니다.」[S5] | **확장** — 제조 도메인에서는 물리 법칙이 **외생적 제약**으로 강제되므로, 기계가 제약을 완화한 비현실적 옵션을 낼 여지가 원천 차단된다. 논문의 한계2가 산업 도메인에서는 완화된다 |
| p.198 한계3: 훈련된 과업에 국한 | 「But if I change the object even slightly, the success rate drops dramatically.」[S4]; 「currently, AI's generalization to unfamiliar environments, and its success rate, are still relatively low.」[S4]; 「What you still need is people who work on anomalies which no one has detected yet.」[S3]; 반대 주장으로 「특정 영역에서 한 가지 작업을 수행하도록 학습된 객체나 모델이 다른 환경에 놓이더라도 적응할 수 있게 되는 것이죠」[S1] | **강한 지지**. 이 사례에서 가장 여러 번, 가장 구체적으로 확인되는 한계 |
| p.198 한계4: 감각/감정/사회기술 부재 | 「But grasping and manipulation — especially anything related to haptics — that hasn't been solved yet. And that's the key bottleneck preventing humanoid robots and embodied intelligence from being truly deployed at scale in factories and homes.」[S4]; 「여전히 직감이라는 것이 중요한데, 이는 우리 인간이 가진 본능적인 감각이지만」[S2] | **지지 + 확장** — 논문의 「감각」이 제조 도메인에서는 **촉각(haptics)** 이라는 구체적 병목으로 특정된다. 감정·사회기술 결여는 이 사례에서 **거의 논의되지 않는다**(대신 「신뢰」 문제로 치환됨: 「인간이 AI 에이전트를 신뢰하지 않으면 제대로 작동하지 않을 것」[S5]) |
| p.199: 한쪽 편중 시 악순환 | 「뿌리고 기도하는 증후군」·「기초 증후군」·「외로운 카우보이 증후군」[S5]; 「그렇다면 왜 많은 기업들이 규모 확장을 하기보다는 파일럿 프로젝트에만 매달리는 걸까요?」[S5]; 「기업들은 여전히 이를 구현하고 시범 단계에서 생산 단계로 넘어가는 데 어려움을 겪고 있습니다 .」[S1] | **보강** — 다만 이 소스들이 진단하는 악순환은 자동화/증강 편중이 아니라 **파일럿 난립·데이터 기반 부재·고립**이다. 논문과 다른 축의 실패 유형 |
| p.204: 기계는 조직 내 새로운 행위자 계급 | 「AI 에이전트는 인간의 디지털 작업자입니다.」[S5]; 「So basically, he's created four employees, virtual employees」[S4]; 「an agent is basically a knowledge worker. It's a virtual employee.」[S4]; 「인공지능들이 서로에게 작업을 지시하는 시대가 올 것이고 」[S2]; 통제 은유: 「마치 수백 명의 직원을 회사 전체에 통제 없이 마음대로 행동하도록 내버려 두는 것과 같습니다 」[S5] | **강한 지지 + 확장** — 논문이 개념적으로 제시한 새로운 행위자 계급이 여기서는 **인사관리 은유(디지털 직원, 거버넌스, 제어 평면)** 로 구체화된다 |

**이 사례가 논문을 확장하는 지점.**
첫째, Siemens에서는 자동화의 대상과 증강의 대상이 **조직적으로 분리**된다. 자동화되는 것은 고객사 공장의 물리 과업이고, 증강되는 것은 그 자동화를 설계하는 Siemens(및 고객사) 엔지니어다. 논문의 spillover(p.197)가 한 조직 내 인접 과업 사이에서 일어난다고 본 데 비해, 여기서는 파급이 **가치사슬의 층을 건너뛰어** 일어난다 — 아래층(생산 과업)의 자동화가 위층(자동화 엔지니어링)의 증강 수요를 만들고, 그 증강 도구가 다시 에이전트로 자율화되면서([S1] 코파일럿 → [S5] 「엔지니어링 작업을 처음부터 끝까지 완료하는 산업용 AI 에이전트」) 새로운 층의 자동화를 낳는다.

둘째, 이 재귀는 **자기참조적**이다. [S2]는 로봇 자동화가 시뮬레이션 구축이라는 새로운 인간 노동을 발생시켰고, 그 노동에 「세계적으로 극소수의 전문가가 필요합니다」라는 병목이 생겼으며, 그 병목을 다시 코딩 에이전트가 푼다고 말한다. 즉 자동화가 만들어낸 새 과업이 곧바로 다음 증강 대상이 된다. 논문의 시간축(CYCLE)과 공간축(SPILL)이 별개 차원이 아니라 **한 나선의 두 투영**으로 나타난다.

셋째, 이행 조건이 정량화된다. 논문이 증강→자동화 이행을 견고화(robustification)로 서술한 데 비해, 이 사례는 신뢰성 임계치(「99.99%」[S1], 「거의 100%」[S2])와 경제성 임계치(「투자 대비 최고의 수익률」[S2])라는 **두 개의 게이트**를 명시한다. 특히 후자는 논문에 없는 조건으로, 「10개 정도의 소량 생산을 자동화하려고 하면 투자 대비 수익률이 좋지 않다」[S2]처럼 **자동화가 기술적으로 가능해도 경제적으로 차단되는 구간**의 존재를 보여준다. 물리AI의 의의는 이 구간을 잠식하는 것으로 규정된다: 「지금까지는 자동화할 가치가 없다고 생각했던 작업들이 이제는 자동화되고 있습니다.」[S5]

넷째, [S6]은 자동화/증강 배분이 **과업 축이 아니라 시간 축**으로도 나뉠 수 있음을 보여준다. 낮에는 로봇이 과학자를 보조하고(증강) 밤에는 로봇이 전 과업을 대신한다(자동화). 동일한 기계, 동일한 과업이 시각에 따라 AUG와 AUTO를 오간다. 논문의 이분법은 과업 단위 분류를 전제하지만, 여기서는 **동일 과업의 교대 근무 편성**이 배분 단위가 된다.

---

### 9.11 인용 시 주의사항

1. **전부 벤더 자체 채널·자체 발화다.** 여섯 소스 모두 Siemens 공식 유튜브 채널이며, 동석자(AWS, NVIDIA, Accenture, Capgemini, Alibaba, Unitree, CATL, ASML, BASF)는 전원 파트너 또는 고객이다. 반대 증언·독립 검증·부정적 사례가 구조적으로 배제된 코퍼스다. 9.8의 모든 수치는 자체보고로 표기해야 한다.

2. **성숙도(계획/파일럿/운영)를 반드시 구분하라.**
   - **계획·개발 중**: 「The next step, we are developing industrial AI assistants」[S4]; 「미래에는 이 작업이 기계에 의해 수행될 것입니다」[S2]; 「우리는 여기서 수작업을 자동화로 전환할 수 있도록 함께 노력하고 있습니다」[S2]
   - **파일럿·고객0**: 「우리는 고객 0의 입장에서 이러한 사용 사례들을 연구하지만」[S2]; 「PepsiCo, our pilot customer」[S4]; 「we already have some use cases and pilot customers」[S4]
   - **운영·출시**: 「현재까지 100개의 AI 알고리즘이 생산 현장에서 활용되고 있습니다 」[S5]; 「그건 이미 수년 동안 현실 세계에서 작동하고 있었잖아.」[S5, 아우디 용접 라인]
   - **미래 비전(인용 시 사실로 오독 금지)**: 「전 세계 1천만 개 이상의 공장 모두 자율 시스템을 갖추게 될 것입니다.」[S2]; 「이제 우리는 명령만 내리고 브라질행 비행기표를 예약해서 그곳에서 시간을 즐길 수 있어요.」[S2]

3. **[S2]의 시점을 업로드일로 쓰지 말 것.** 업로드일 2026-07-17이지만 발화는 하노버 메세 현장이고 「어제 저희 Eigen 엔지니어링 에이전트를 출시했습니다」다. [S5](2026-06-19)가 그 출시를 「두 달도 채 되지 않은 시점에」라 하므로 실제 발화는 업로드보다 2개월 이상 이르다. 시계열 논증에 쓸 때 반드시 명기.

4. **자막 오류·오기가 대량이다.** 인용 시 원문 그대로 옮기되 독자에게 오류임을 표시하라.
   - 사명 오기: 「Seammen's」·「Seammens」·「짐멘스」·「시멘스」·「시먼스」·「Zemen」·「Semens」·「WeSemens」·「Z-Meds」·「시멘트 회사」·「정액」(모두 Siemens) [S1][S2][S6]
   - 「ZIT 액셀러레이터」/「ZTH 액셀러레이터」(= Xcelerator) [S1]
   - 「Z-Move」/「Z 무브」[S6] ↔ 「SIMOVE」[S4] — 같은 제품으로 보이나 **소스 간 표기가 다르다**
   - 「연기」(= acting)·「공기 동력 자율 생산」(= AI powered)·「오줌.」·「목사님」(Rev.으로 오인식) [S2]
   - 「채널 목적에 특화된 기술」/「채널 전용 기술」(= general-purpose technology), 「감자 칩 때문이에요」(= It's the chips), 「GPO(그룹 구매 조직)」(= GPU), 「엔비디아 GPA」, 「KN을 데려오세요」(= KION) [S5]
   - 「corporate consumption by forty-five percent」(= copper로 추정) [S4]
   - 「구현 시간을 60% 증가시킵니다」(= 단축이어야 할 것으로 보임) [S6]
   - 「SNS 시장」(= 물리적 AI 시장으로 추정) [S1]
   - 「전년 대비 33%의 성장률」 — 50억→500억(2033)이라는 서술과 「전년 대비」라는 표현이 정합하지 않음 [S1]

5. **귀속 문제.**
   - [S2]의 직함: 「디지털 인더스트리의 CEO」 → 「사실 CTO입니다」로 정정됨. 발화자 이름도 「라이너」/「라나」, 「레브」/「레프」/「랄프」/「브렛」으로 흔들려 **어느 발화가 누구 것인지 확정이 어려운 구간이 있다**.
   - [S6]의 「마테우스」/「마티아스」, 「카트린 콘」(BASF)과 「카트린」(Accenture)이 동명이라 **발화 귀속이 자주 모호하다**. 특히 「캐스린」이 누구를 가리키는지 확정 불가한 대목이 있다.
   - [S1] Siemens 측 발화자는 「호스 카이저 박사」·「HT」·「허스트 님」·「허스트 박사」·「호스 박사님」으로 표기가 갈린다.
   - 50%/2.5배/80%는 Siemens가 **「고객들의 피드백은 어떻습니까 ?」라는 말로 고객에게 귀속**한 수치이며 고객명·표본수·측정방법이 소스에 없다 [S5].

6. **일부 사례는 Siemens 성과가 아니다.** CATL의 R&D 130억 달러·2만3천 명·part-per-billion, Unitree의 로봇 성능, ASML의 95% 가동률·2만 부품, Alibaba의 Qwen·50조 달러 TAM은 **게스트 기업 자체 주장**이다. Siemens 기여분과 섞어 인용하면 안 된다.

7. **Navantia·Keon·Clorox는 Accenture 공동 사례**로 제시되며([S3]), 20% 개선의 기여 분해는 소스에 없다. Clorox는 답변자가 사례를 확인하지 못했으므로 인용 불가.

8. **RESP 관련 조심.** 이 사례에는 인간 승인권에 해당하는 구체적 절차가 없다. 있는 것은 ① 원칙 선언(「remain in human hands」[S4]), ② 기록·추적 인프라([S5][S6]), ③ 거버넌스 필요성 주장([S5]), ④ 제3자 인증 1건([S6])뿐이다. 따라서 Siemens가 인간 승인 게이트를 운영한다는 주장은 **이 소스들로 뒷받침되지 않는다**.

9. **[S6]은 단독 대조군이며 정보량이 얇다.** 1387단어, BASF 측 성과는 대부분 기대 표현(「기대합니다」, 「늘어날 수 있는데」)이다. 실현된 수치는 없다: 「우리는 더 빠른 지식 생성, 견고한 운영, 그리고 무엇 보다도 현재 에 비해 처리량의 상당한 증가를 기대합니다 .」[S6] 이 소스를 성과 근거로 쓰지 말고, **배분 구조(주간/야간)** 의 근거로만 쓸 것.

10. **[S1]의 「자율 공장 연구소」와 「여러 중소기업과 데이터 제휴」는 한 문장씩만 존재한다.** 위치, 규모, 참여사, 시점이 전부 소스에 없다. 이 사례의 핵심 확인 사항으로 지목되었으나 **실제 근거는 각각 1문장에 불과하다**는 점을 명시해야 한다.

---

**요약 및 한계.** 이 절은 Siemens 공식 채널의 6개 영상(2026-02-07 ~ 2026-07-17 업로드, 총 약 26,900단어)을 전량 정독해 작성했다. 확인된 핵심 구조는 (i) 자동화의 대상은 고객 공장의 물리 과업이고 증강의 대상은 그 자동화를 설계하는 엔지니어라는 층위 분리, (ii) 그 분리가 만들어내는 메타 수준·재귀적 spillover(공장 자동화 → 엔지니어링 증강 → 시뮬레이션 구축이라는 새 과업 발생 → 코딩 에이전트로 재증강), (iii) 신뢰성(99.99%/거의 100%)과 ROI라는 **이중 게이트**로 정량화된 증강→자동화 이행 조건, (iv) [S6] 실험실 사례가 보여주는 **시간축(주간 증강/야간 자동화) 배분**이다. 핵심 확인 사항이었던 「30~40%」[S1]는 **다른 소스에서 재확인되지 않았고**, 대신 40%(S4, 개발 중 어시스턴트)와 50%/2.5배/80%(S5, Eigen 에이전트)라는 서로 다른 제품의 다른 수치가 나왔다 — 코파일럿→어시스턴트→에이전트로 지칭 대상이 이동한 결과다. 한계는 명확하다. 여섯 소스 전부가 벤더 자체 채널·자체 보고이며 제3자 검증치가 없고, [S2]는 업로드일과 발화 시점이 2개월 이상 어긋나며, 한국어 기계번역 자막의 오기·오역이 대량이어서 고유명사와 일부 수치(구현 시간 60%, 시뮬레이션 10만 배 vs 1,000배, corporate/copper)의 해석이 소스만으로는 확정되지 않는다. 증강 회귀(CYCLE의 역방향)와 인간 개별 승인권(RESP의 절차적 실체)은 여섯 소스 어디에도 근거가 없어 해당 소스에 없음으로 처리했다.


---



## 사례 10 — McKinsey : GBS·서비스운영·뱅킹 진단 시리즈

*원문: `docs/cases/09_mckinsey.md`*


이 사례는 단일 조직의 도입 사례가 아니라 **동일 컨설팅사(McKinsey & Company)가 1년에 걸쳐 발표한
5개 자료의 담론 계열체**다. 따라서 before/after 수치를 가진 도입 사례로 읽으면 근거가 빈약하고,
자동화/증강 담론이 시간에 따라 어떻게 이동했는가로 읽으면 정보량이 크다. 아래 분석은 후자를 주축으로 한다.
모든 자료는 채널 수집분이므로 **파일 헤더의 "업로드일"이 영상 업로드 시점**이며, 수집일이 아니다.

---

### 10.1 소스 목록

| 태그 | 채널 | 업로드일(채널 수집분 → 영상 업로드 시점) | 자막언어 | 단어수 | 발표 맥락/발화자 | URL | 파일경로 |
|---|---|---|---|---|---|---|---|
| [S5] | McKinsey & Company | 2025-08-30 (업로드일) | ko | 약 287개 | 짧은 단독 발화 영상. "Redefining service operations: Navigating the crossroads of opportunity". 화자 이름이 자막에 나오지 않음 | https://www.youtube.com/watch?v=mOuD5ZDAGDQ | /home/user/youtube-scrap/transcripts/channels/McKinsey_&_Company/Redefining_service_operations_Navigating_the_crossroads_of_o__mOuD5ZDAGDQ.md |
| [S4] | McKinsey & Company | 2025-11-13 (업로드일) | ko | 약 3217개 | McKinsey Talks Operations 팟캐스트. 게스트 = "의료 분야의 리더이자 이사회 멤버이며 포춘 15대 기업의 전 CEO인 마이크 칼프만"(카디널 헬스), "서비스 운영을 전문으로 하는 맥켄지 파트너 스티브 에클랜드" [S4] | https://www.youtube.com/watch?v=yoWyJnej0Iw | /home/user/youtube-scrap/transcripts/channels/McKinsey_&_Company/Unlocking_hidden_value_with_process_intelligence_in_healthca__yoWyJnej0Iw.md |
| [S3] | McKinsey & Company | 2025-11-20 (업로드일) | ko | 약 2646개 | McKinsey 팟캐스트. 진행자 "Lucia Raheli", "Robera Fisaro"(자막 표기), 게스트 = "McKenzie의 수석 파트너인 Dan Swan" [S3] | https://www.youtube.com/watch?v=O-aUZqfcLKg | /home/user/youtube-scrap/transcripts/channels/McKinsey_&_Company/Productivity_first_AI_and_the_COO_agenda__O-aUZqfcLKg.md |
| [S2] | McKinsey & Company | 2026-02-02 (업로드일) | ko | 약 2375개 | McKinsey Talks Operations 팟캐스트. 진행자 "스테파니 룩센버그"(후반부 "다파니"/"다프네 룩셈부르크"로 흔들림), 게스트 = "데이비드 데니슨은 맥켄지 뉴욕 사무소의 선임 파트너이자 맥켄지 로펌의 은행 운영 부문 글로벌 공동 책임자", "아발라쉬 스리단은 맥켄지 뭄바이 사무소의 파트너이며 아시아 지역 서비스 운영을 총괄" [S2] | https://www.youtube.com/watch?v=EnuwWHoUKpk | /home/user/youtube-scrap/transcripts/channels/McKinsey_&_Company/The_paradigm_shift_how_agentic_AI_is_redefining_banking_oper__EnuwWHoUKpk.md |
| [S1] | McKinsey & Company | 2026-08-03 (업로드일) | ko | 약 2937개 | McKinsey Talks Operations 팟캐스트. 진행자 "크리스찬 존슨", 게스트 = "맥킨지 쾰른 사무소의 파트너인 하이코 하임스", "조쉬 피터스는 워싱턴 D.C. 사무소에 근무하는 맥킨지 파트너" [S1] | https://www.youtube.com/watch?v=LuHGabkzlGU | /home/user/youtube-scrap/transcripts/channels/McKinsey_&_Company/Agentic_AI_and_the_future_of_Global_Business_Services__LuHGabkzlGU.md |

각 소스의 역할:
- **[S1] 1차 근거.** 자동화-증강 병존 명제('둘 중 하나'가 아니라 '둘 다'), 20~30% 축소 전망, 다이아몬드 인재모델,
  활동 빈도 증가, 통화 50% 디플렉션 대 증강 대비, P2P 프런트엔드 확장 등 이 사례의 핵심 관찰이 모두 여기 있다.
- **[S2] 1차 근거(도메인 특화).** 뱅킹 운영에서의 자동화 역량 전망치, 1인당 에이전트 20~30, 모델리스크위원회 승인이라는
  명시적 RESP 장치를 제공한다.
- **[S3] 보강 + 부분 대조군.** 생산성 우선 프레이밍이 자동화를 노동 대체가 아닌 노동 부족 해소로 재정의한다.
  AUTO/AUG 구분 언어는 약하다.
- **[S4] 대조군.** 에이전트형 AI 이전 단계(프로세스 마이닝/인텔리전스) 담론. 프로세스 단위 관점과
  AI 도입 이전에 프로세스 인텔리전스가 선행해야 한다는 전제 조건 논리를 제공한다. 유일하게 구체적 금액 목표치가 나온다.
- **[S5] 보강(프레이밍).** 287단어의 짧은 자료로, 시리즈의 출발점 프레이밍(갈림길, 마법의 공식)만 확인된다.
  근거로서는 얇다.

---

### 10.2 조직과 문제 상황

이 사례에는 단일 조직이 없다. 대신 소스별로 언급된 규모/물량 수치를 시점 순으로 정리한다.
**모두 McKinsey 자체 추정 또는 무명 고객사 일화이며, 제3자 검증치가 아니다**(예외는 아래 MIT 인용 1건).

**2025-08-30 [S5]** — 서비스 부문의 거시 규모 프레이밍:
"음악 서비스는 100조 달러 규모의 세계 음악 경제에서 60%를 차지하며, 중요한 전환점에 서 있습니다." [S5]
(주: "음악"은 자막 오류로 보이며 원문 단어는 이 소스만으로 복원 불가. 10.11 참조.)
before 상태는 "첫째는 점진적 개선의 시대가 끝났다는 인식입니다." [S5]로만 서술된다.

**2025-11-13 [S4]** — 카디널 헬스 및 유사 대기업의 프로세스 난맥:
"특히 수천 개의 지점을 보유하고 인수 합병을 통해 수년에 걸쳐 수많은 다양한 비즈니스 프로세스를 축적해 온 조직이라면,
비즈니스 운영 프로세스를 얼마나 잘 이해하고 계십니까 ?" [S4]
"여러 프로세스가 있거나, 여러 차례 인수 합병을 거쳤거나, 다양한 시스템 간에 복잡하게 연결되어 있는 회사라면,
A에서 B, C, D로 이어지는 과정이 설계대로 제대로 작동하지 않는 문제가 발생할 가능성이 매우 높습니다." [S4]
발화자 이력: "저는 카디널 32에 있었지만, 그 후 20년 동안 업계에서 다양한 역할을 맡았고, 마지막 5년은 CEO로 재직했습니다." [S4]
(자막 오류 의심 구간. 10.11 참조.)

**2025-11-20 [S3]** — 생산성 분포와 노동 공급:
"맥켄지에서 진행한 저희 연구 결과에서도 주요 경제권에서 생산성 증가의 63%를 차지하는 기업이 전체 기업의 2%에 불과하다는
사실이 드러났는데" [S3] (McKinsey 자체 연구, 관측치로 제시)
"현재 미국에는 약 50만 개의 제조업 일자리가 공석으로 남아 있습니다." [S3] (관측치로 제시)
"제조업과 건설업 분야의 숙련 노동력은 2030년까지 최대 300만 명에 달할 것으로 추산됩니다." [S3] (**전망치**)
"MIT에서 최근 발표된 연구 결과가 있습니다. 기술 기반 시범 사업의 약 95%가 애매한 상태에 빠진다고 합니다 ." [S3]
(**이 시리즈에서 유일하게 외부 기관에 귀속된 수치**. 다만 MIT 보고서 자체를 확인할 수 없으므로 제3자 검증이 아니라
제3자 인용으로만 취급해야 한다.)

**2026-02-02 [S2]** — 은행 운영의 인력 비중:
"은행에 따라 다르지만, 정규직 직원의 50~60%가 어떤 형태로든 운영과 관련되어 있다고 추정합니다." [S2] (**자체 추정치**)
"아시아에서 저희와 협력하는 금융 기관의 거의 80%가 사회적 영향력 창출을 위해 AIEL 애플리케이션의 다양한 버전을 사용하고
있다고 보고했습니다. 하지만 전 세계적으로 비슷한 비율의 기업들이 실적에 큰 영향을 받지 않았다고 보고하고 있습니다." [S2]
(**벤더/컨설팅사 자체 수집 + 고객 자기보고의 이중 자기보고**)
프로세스 분해 물량: "은행 전체를 하나의 상자로 만들어" 각 사업 부문과 가치 사슬에 걸쳐
"약 600개의 프로세스와 하위 프로세스로 세분화했습니다" [S2] (익명 "한 아시아 은행" 사례)

**2026-08-03 [S1]** — GBS의 위치와 도입 성숙도:
"제 고객 포트폴리오를 살펴보면, 모두가 AI에 대해 생각하고 있고, 예를 들어 GPS 분야에서도 AI를 활용하는 것에 대해
고민하고 있습니다. 제 생각에는 절반 정도가 시범 운영을 시작하고 AI를 활용하여 첫 번째 사용 사례를 만들어내고 있는 것
같습니다." [S1] (**개인 포트폴리오 기반 인상치. 표본 정의 없음**)
"제가 지난 9~12 개월 동안, 즉 AI가 실제로 변화를 가져오기 시작한 시기에 관찰한 선도적인 사례들은 오히려 보다 전통적인
금융 프로세스 영역에서 나타나고 있습니다." [S1]

---

### 10.3 자동화 구간 (AUTO)

**[S5] 2025-08-30** — 에이전트를 인간 대체 행위자로 명시한 유일한 강한 표현:
"마지막으로, AI 에이전트와 에이전트 아키텍처를 배포하여 기업의 복잡한 워크플로우를 재구상하는 것입니다.
AI 에이전트는 명확하게 정의된 직무 설명을 바탕으로 인간 동료를 대신하여 계획, 추론 및 행동을 수행할 수 있는
가상 동료가 될 것입니다 ." [S5] (**전망치, "될 것입니다"**)

**[S4] 2025-11-13** — 이 시점의 AUTO는 아직 에이전트가 아니라, 프로세스 마이닝이 찾아낸 즉시 절감 항목이다:
"무엇보다도 , 이 제품은 즉시 비용 절감 효과를 가져다 줄 수 있습니다. 예를 들어, 외상 매입금 같은 영역에 입력하면
이중으로 지불했거나, 조기에 지불했거나, 고객에게 신용 보류를 걸었거나, 공급망에서 제때 물품이 도착하지 않을 것 같은
상황을 파악할 수 있습니다 ." [S4]

**[S3] 2025-11-20** — 자동화를 생산성의 원동력이자 기피 업무 제거 장치로 규정:
"오늘날 우리가 발견하는 것은 자동화가 생산성 향상의 실질적인 원동력 중 하나라는 점입니다. 특정 직무에 필요한 인력이
부족한 경우가 있기 때문이기도 하지만, 자동화로 인해 직원들이 가장 싫어하는 업무 부분이 사라지는 경우가 많기 때문입니다." [S3]
콜센터 자동화가 인간보다 선호된다는 주장:
"그리고 그 예시에서 정말 흥미로운 점은 사람들이 종종 자신이 상담원과 대화하고 있다는 것을 알고 있고, 상담원과 대화할 때
사람보다 더 만족감을 느낀다는 것입니다 ." [S3] (**출처 없는 주장. 수치 없음**)
R&D 사이클 압축:
"이전에는 신제품에 대한 피드백을 얻기 위해 소비자 샘플링을 몇 주 또는 몇 달 동안 진행해야 했던 작업을 이제는
생성형 AI 프로세스를 통해 몇 시간 만에 얻을 수 있습니다 ." [S3]

**[S2] 2026-02-02** — 은행 운영의 자동화 역량 전망:
"저희는 운영 과정이나 프로세스에 따라 AI를 통해 창출되는 역량이 40%, 60%, 70% 이상에 달할 것으로 예상합니다.
하지만 그건 몇 가지 조건이 모두 충족될 때만 가능한 일이죠." [S2] (**전망치이며 조건부**)
AUTO의 실패 양식도 이 소스가 가장 명확히 제시한다:
"우리가 직면한 가장 큰 위험은 바로 손가락과 발가락 문제라고 부르는 것이죠, 그렇죠? 개별 담당자들이 하는 일의 일부만
자동화하는 데 도움이 되는 모델과 기능을 만드는 것, 그렇죠? 그게 바로 과거에 자동화와 RPA가 실패했던 근본적인 이유죠 ?" [S2]

**[S1] 2026-08-03** — 거래성 업무의 기계 인계:
"자동화, 특히 RPA와 AI가 상당 부분을 담당하는 거래 중심적인 활동을 관리하고 운영할 필요성이 줄어들고" [S1]
"따라서, GBS 내 여러 영역에서 업무를 인계받을 AI 에이전트 세트가 있습니다." [S1]
고객주문 사례의 자동화 측면:
"통화의 50 %를 다른 곳으로 돌릴 수 있어서 비용을 많이 절감할 수 있었습니다" [S1]
(**주의: 이 문장은 화자가 이것만 보여주는 것으로는 부족하다는 맥락에서 인용한 예시 문장이다. 10.11 참조.**)
구매 프로세스 재설계:
"그래서 이 조직은 AI가 공급 업체 식별 및 선정 과정의 상당 부분을 담당하도록 프로세스를 재구상했습니다." [S1]

---

### 10.4 증강 구간 (AUG)

**[S5] 2025-08-30** — 증강을 "마법의 공식"으로 선언:
"세 번째이자 제가 가장 좋아하는 비결은 인공지능의 힘과 인간의 협력을 결합하는 데 마법의 공식이 있다는 것입니다 .
기관들이 경쟁 우위를 유지하려면 인공지능과 인간의 균형을 적절히 맞추는 것이 매우 중요합니다 ." [S5]
같은 287단어 안에 10.3의 "인간 동료를 대신하여" 문장과 이 문장이 **동시에** 들어 있다는 점이 중요하다(10.9 참조).

**[S4] 2025-11-13** — 인간이 남는 자리는 프로세스 소유자와 경영진 후원자다:
"그리고 아시다시피, 비즈니스 프로세스 소유자라는 개념은 프로세스 마이닝과 같은 도구에서 얻은 통찰력을 활용하여 조직이
고객 경험, 효율성, 속도, 품질, 정확성 또는 생산성 등 더 나은 결과를 달성하도록 이끌어가는 사람입니다.
이는 이제 대부분의 조직에서 반드시 필요한 중요한 역할입니다 ." [S4]

**[S3] 2025-11-20** — 현장 인력의 기술 재구성:
"아시다시피 , 저희 연구 결과에 따르면 현장 노동자들의 업무, 기술, 시간 활용 방식의 40~50%가 향후 3 ~5년 안에
기술 발전으로 인해 의미 있게 변화할 수 있다고 합니다." [S3] (**전망치**)
"여러분은 로봇과 상호작용하는 방법을 배우고 있습니다. 여러분은 인공지능과 머신러닝, 그리고 그 외 여러 분야에서
활용 가능한 기술들을 배우고 있는 겁니다 ." [S3]

**[S2] 2026-02-02** — 증강의 결과를 관리 범위 확대로 정의:
"우리는 이러한 변화의 영향 중 하나로 인간이 자신의 업무를 수행하고 규모를 확장할 수 있는 능력이 향상될 것으로 기대합니다.
오른쪽? 따라서 대략 20~30명의 상담원이 한 명의 담당자에 의해 관리될 것으로 예상합니다. 오른쪽? 그러니까, 개인 기여자가
20~30명의 동료로 구성된 팀을 이끌고 함께 협력하여 결과물을 도출하는 것이라고 생각하시면 됩니다." [S2] (**전망치**)
1선 리스크 업무의 시간 재배분:
"이러한 간단한 초기 분석은 현장 직원들이 고객에게 실질적인 서비스를 제공하는 데 더 많은 시간을 할애할 수 있도록 도와주고,
검토되는 사례 및 제품 수를 늘리며, 궁극적으로 검토의 정확도를 높일 수 있습니다 ." [S2]
"그래서 조직의 리더들은 위험을 식별하고, 위험을 살펴보고, 위험을 완화하기 위한 결정을 내리는 데만 시간을 쏟고,
정작 그러한 논의를 위한 데이터를 수집하는 데는 80% 또는 90%의 시간을 투자하지 않습니다." [S2]
증강 은유:
"그들은 인공지능이 조종사가 승무원을 대체하는 것이 아니라고 말했습니다. 새로운 엔진 덕분에 동일한 승무원이 탑승한 상태로
항공기가 더 멀리, 더 빠르게 비행할 수 있게 되었습니다 ." [S2]

**[S1] 2026-08-03** — 이 시리즈에서 가장 명시적인 AUG 선언:
"그러니까 AI가 GBS를 아직 대체하지는 않았다는 거죠. 실제로는 그것을 증강시키는 것입니다." [S1]
"따라서 현재로서는 '둘 중 하나'가 아니라 '둘 다'를 선택해야 하는 상황이라는 점을 고려할 때 , 조직은 기존의
GBS(게임 기반 서비스) 전략과 AI 도입 사이에서 어떻게 적절한 균형을 찾아야 할까요?" [S1]
고객주문 사례에서 자동화가 아니라 **증강**을 선택한 대목:
"보통은 상위 직급 자에게 보고해야 했을 문제를, 증강 AI와 도움을 받고, 고객의 말에 따라 적절한 방향으로 안내해주는
스크립트를 활용해서 직접 해결할 수 있게 된 거죠. 둘째, 직원에게 훨씬 더 만족스러운 경험이 되잖아요 ?" [S1]
FP&A의 질적 전환:
"그래서 저희가 고객사들이 FP&amp;A를 위한 보조 전문가를 개발하도록 도울 때, 단순히 " 계절적 요인이나 기상 현상 때문에
매출이 감소한 것 같습니다"라고 말하는 데 그치지 않고, " 다음으로 어떤 두세 가지 질문을 던져야 할까요?" 또는
" 다음으로 어떤 두세 가지 조치를 취해야 할까요?"와 같은 구체적인 방안을 함께 제시합니다." [S1]
인재 모델:
"네, GBS에서 인재들의 미래 모습을 생각할 때 , 우리는 그것을 다이아몬드 형태의 구조로 생각합니다. 그러니까 기본적으로
GBS 조직의 소위 중간 계층에 더 많은 인력이 배치될 거라는 뜻입니다." [S1]
"그래서 피라미드형 인재 모델에서 벗어나 다이아몬드형 인재 모델로 전환하는 것이 향후 몇 년 동안 우리가 예상하는 모습입니다." [S1]

---

### 10.5 전환 메커니즘 (CYCLE)

이 시리즈에는 **개별 조직의 증강 학습 → 견고화 → 자동화 타임라인이 담긴 사례는 없다.**
대신 두 종류의 전환 기준이 서술된다.

**(a) 표준화 성숙도를 문턱으로 삼는 명시적 순서 규칙 [S1]**
"앞으로도 많은 조직들이 인재 확보, 규모 확대, 표준화, 가치 창출을 위해 GBS(Global Business Services)에 업무를
우선적으로 투입하고, 표준화가 완료되면 AI를 적용하여 추가적인 개선을 추진하는 '우선순위 아웃소싱' 전략을 계속해서
추진할 것으로 예상됩니다 ." [S1]
= 표준화 완료가 자동화 진입 조건이라는 CYCLE 서술이다. 그 반대 경로도 병기된다:
"저는 이와 병행하여 자동화 우선 전략을 추진하는 기업들이, 특히 특정 분야, 즉 핵심 전략 프로세스에서 장기적인 디지털
역량을 구축하고자 할 때, 어떻게 하면 기업 가치를 극대화할 수 있을지 고민하고 있다고 생각합니다." [S1]
"프로세스의 일부는 GPS를 먼저 도입하는 것이 도움이 될 수 있습니다. 프로세스의 다른 부분부터 먼저 자동화하면 이점을
얻을 수 있을 것입니다." [S1]
결정 요인으로 제시된 것: 기존 GBS 성숙도, 기술 활용 경험, 기대 영향, 프로세스 유형 —
"어떤 길을 택할지 결정하는 데에는 여러 가지 요소가 복합적으로 작용하는 것은 분명합니다." [S1]

**(b) 프로세스/데이터 가시성을 전제 조건으로 삼는 순서 규칙 [S4]**
"따라서 프로세스 인텔리전스, 프로세스 마이닝, 그리고 여러 시스템의 데이터를 연결하여 올바른 답을 도출할 수 있도록 하는
모든 것을 갖추지 않고서는 기업 에서 효과적으로 AI를 구현할 방법이 없습니다." [S4]
"왜냐하면 제 생각에는 프로세스 인텔리전스 없이는 AI도 없기 때문입니다." [S4]
"음, 그래서 저희는 이것이 그러한 목표와 생산성 및 효율성 수준에 도달하기 위한 필수 전제 조건이라고 말씀드릴 수 있습니다." [S4]

**(c) 증강 회귀 조건**: 조건 변화 시 자동화에서 증강으로 되돌아간다는 서술은 **해당 소스들에 없음**.
다만 [S2]는 배치를 지연·차단하는 조건을 제시한다:
"또 다른 하나는 규제 지침의 불명확성입니다. 이로 인해 모든 사람이 해당 기능이 효과적으로 작동하고 품질이 우수하다는 것을
확신할 때까지, 특히 고객 대면 기능의 경우, 일부 기능이 완전히 도입되는 것이 지연되거나 불가능해질 수 있습니다." [S2]
이는 "회귀"가 아니라 "진입 보류"이므로 CYCLE의 완전한 대응이라 보기 어렵다.

**(d) 파일럿 정체가 CYCLE을 끊는다는 진단**은 시리즈 전체에 반복된다:
"기술 기반 시범 사업의 약 95%가 애매한 상태에 빠진다고 합니다 ." [S3]
"두 번째로 말씀드리고 싶은 것은 첫날부터 대규모로 일을 처리하는 것을 진지하게 고려해야 한다는 것입니다." [S3]
"기술 도입이 더딘 기업들은 우리가 '음악 시범 사업의 늪'이라고 부르는, 좁은 사용 사례에만 매몰되어 이 기술의 혁신적인
잠재력을 온전히 실현하지 못하는 매우 현실적인 위험에 직면하게 됩니다 ." [S2]
"이러한 목표는 조직이 소규모 시범 단계를 넘어 더 큰 단계로 나아가는 촉매제 역할을 해야 합니다." [S5]

---

### 10.6 공간축 파급 (SPILL) / 자원 재투자 (REINV)

**SPILL — 있음. 이 사례의 최대 강점 구간이다.**

1) **P2P 백엔드 자동화 → 프런트엔드 인간 책임 확대 [S1]**
"제 고객 중 한 곳은 GPS가 오랫동안 자금 조달부터 지급까지의 프로세스 후반 작업을 담당해 왔습니다. (…)
백엔드에 AI를 도입하는 것뿐만 아니라, 이를 프로세스의 프런트엔드와 연결하는 것입니다 ." [S1]
"현재 공급업체 선정은 GPS가 관리하고 있으며, 이를 통해 GPS는 프로세스의 백엔드를 얼마나 원활하게 운영할 수 있는지를
결정하는 프런트엔드를 더욱 효과적으로 담당하게 되었습니다. 따라서 GPS에 더 큰 책임을 부여함으로써 마찰을 줄이고
전체 프로세스를 더욱 원활하게 만드는 것입니다." [S1]
파급은 조직 경계를 넘어 외부 행위자에게도 미친다:
"공급업체들은 전반적인 프로세스가 잘 진행되고, 예를 들어 제때 계획대로 대금을 지급받는 것에 대해 훨씬 더 만족스러워합니다." [S1]

2) **거래 처리 자동화 → 감사/내부통제의 표본 검사에서 실시간 전수 검사로 [S1]**
"그러니까 과거에는 내부 통제나 감사 같은 것이 불규칙적으로만 이루어지는 것을 볼 수 있었던 것 아닌가요?
혹은 특정 표본 크기에 도달하면 갑자기 AI를 활용하여 내부 통제와 같은 분야에서 실시간 처리를 수행할 수 있게 됩니다.
그래서 거래가 규정을 준수하고 규칙에 부합하는지 지속적으로 확인하는 거죠." [S1]
"그리고 이것 또한 AI 덕분에 GBS가 갑자기 훨씬 더 많은 업무량을 차지하게 될 수 있는 상황의 한 예가 될 수 있습니다." [S1]

3) **자동화가 인접 과업의 인간 업무량을 늘린다는 총량 서술 [S1]**
"그리고 하이코, 흥미로운 점은 이 두 가지가 서로 상쇄되는 것처럼 보인다는 것입니다. 그렇죠? 동시에 인공지능으로
대체되는 업무가 많아지는 한편, 시스템에 유입되는 업무도 늘어나고 있습니다." [S1]

4) **1선 리스크 데이터 수집 자동화 → 검토 건수/정확도 확대 [S2]** (10.4 인용 재참조)
"검토되는 사례 및 제품 수를 늘리며, 궁극적으로 검토의 정확도를 높일 수 있습니다 ." [S2]

5) **AI 도입 → 프로세스 인텔리전스라는 인접 감시 과업 신설 [S4]**
"두 번째는, 설령 그렇게 해서 AI를 효과적으로 활용한다고 하더라도, AI를 무방비 상태로 둘 수는 없다는 것입니다.
AI 결과가 정확한지 지속적으로 모니터링해야 합니다. 바로 이 부분에서 프로세스 인텔리전스와 데이터 마이닝이 중요한
역할을 합니다." [S4]

**REINV — 약한 형태로만 있음.** UBS 패턴처럼 자동화로 확보한 예산·인력을 명시적으로 증강에 재배치했다는
회계적 서술은 **해당 소스들에 없다**. 근접한 서술은 세 가지다.
- 능력 이동 방향 서술 [S1]: "분석적 의사 결정이나 판단에 기반한 업무, 즉 다른 종류의 기술이 필요한 업무로 인력이
  이동하게 될 것이기 때문입니다." [S1] (**전망치**)
- 절감액을 확대 목표로 되돌리는 목표 설정 [S4]: "개념 증명을 마친 후, 첫 해에는 3천만 달러, 둘째 해에는 7천만 달러의
  가치를 창출하는 것을 목표로 삼았습니다." [S4] — 이는 재투자가 아니라 목표 상향이므로 REINV로 보기 어렵다.
- 시간 재배분 [S2]: 리스크 데이터 수집 시간을 리스크 판단 시간으로 옮긴다는 서술(10.4 인용). 예산이 아니라 시간의 재배분이다.

---

### 10.7 통합 장치 (RESP)

**[S2]가 가장 강한 RESP 근거를 제공한다 — 모델 승인 게이트가 제도로 존재한다.**
"아시다시피 은행은 모델 리스크 관리 절차를 거쳐야 합니다. 은행에서 사용되는 모든 모델은 문서화되고, 검토되고,
모델 리스크 관리 위원회의 승인을 받아야 합니다 ." [S2]
"그러므로 AI로 인해 발생하는 위험을 이해하고 운영 영역뿐만 아니라 다른 영역에서 나오는 다양한 AI 및 에이전트형 AI 모델을
신속하게 승인할 수 있는 명확한 운영 모델을 갖추는 것이 이 모든 과정에서 매우 중요할 것입니다." [S2]
책임 소재의 분산 금지:
"어느 한 부서나 한 사람이 기업 전체에 걸쳐 이 일을 주도할 수는 없습니다. 명확한 목표와 책임감을 가진 헌신적인
리더 그룹이어야 합니다." [S2]
"우선, 최고 경영진의 최우선 과제가 되어야 합니다. 저희는 미국에 있는 여러 고객사에서 CEO들이 주도적으로 의제를 이끌고
팀원들에게 책임을 묻는 모습을 보았습니다." [S2]
거버넌스 3주체 분업(CIO=인프라, CRO=리스크 승인, COO=의제 설정):
"또한 CIO가 마련한 도구를 활용하고, 위험 관리 조직이 구축한 위험 방지 장치를 활용하며, HR과 협력하여 AI를 활용할 수 있는
적절한 역량과 인력이 있는지 확인하는 것도 COO의 역할입니다 ." [S2]
"CTO 또는 CIO와 그의 팀은 기본적으로 이를 지원하기 위해 적절한 데이터 플랫폼, 머신러닝 파이프라인 및 거버넌스가 모두
갖춰져 있는지 확인합니다 ." [S2]
사용 추적의 설계 원칙(개인 감시가 아닌 도구 단위 계측):
"개별 사용량을 추적하는 것이 아니라 도구와 기능 사용량을 추적하는 일련의 지표, 즉 일종의 지표 또는 대략적인 지표를
제공하여 무엇이 더 유용한지, 어떤 부분을 계속 개발해야 하는지, 어떤 부분은 개발하지 않아도 되는지 파악할 수 있도록
하는 것입니다." [S2]

**[S4]는 감사추적/모니터링 쪽 RESP를 제공한다.**
"프로세스 인텔리전스는 AI가 도출한 실제 결과를 모니터링하여, 잘못된 결과로 고객 관계가 손상되거나 재정적인 손실을
입는 것을 방지합니다." [S4]
전문성 귀속에 관한 강한 규범(논문 p.195와 직결):
"제 생각에 두 번째로, 성공적인 결과를 얻으려면 비즈니스 주도형 IT 지원 방식이 되어야 합니다. IT 주도형 비즈니스 지원
방식이 되어서는 안 됩니다. 비즈니스 주도가 없으면 IT 부서에서 주도하는 방식 만큼의 관심과 참여, 그리고 최종 결과를
달성하려는 의지를 얻을 수 없기 때문입니다 ." [S4]
"제가 배운 것 중 하나는 CIO, COO, CFO 또는 CEO와 같은 고위 임원의 후원이 없다면, 제가 카디널에서 후원자였듯이,
모든 프로세스를 아우르고 정기적으로 진행 상황을 점검해 줄 수 있는 사람이 없다는 것입니다." [S4]
전체 프로세스 소유의 필요:
"흔히 발생하는 문제는 전체 과정 중 일부만 담당하는 사람이 프로젝트 리더로 임명되는 경우입니다. 그러면 그 사람이 담당하는
부분, 즉 전체 과정의 일부에만 갇히게 되어 프로젝트의 잠재력을 최대한 발휘할 수 없게 됩니다 ." [S4]

**[S1]의 RESP는 "책임 부여"라는 조직 설계 언어로만 나타난다.**
"따라서 GPS에 더 큰 책임을 부여함으로써 마찰을 줄이고 전체 프로세스를 더욱 원활하게 만드는 것입니다." [S1]
개별 AI 산출물에 대한 인간 승인 게이트/감사추적을 명시한 대목은 **[S1]에 없음**.

**[S3], [S5]에는 승인권·감사추적 수준의 RESP 서술이 없음.** [S3]은 COO의 통제 범위를 논하지만
AI 산출물 승인 절차는 다루지 않는다.

---

### 10.8 성과 수치

이 사례에는 **동일 조직의 before/after 쌍이 거의 없다.** 대부분 전망치이거나 before가 결측이다.
아래 표에서 before가 비어 있으면 소스에 없다는 뜻이다.

| 지표 | before | after | 소스 | 자체보고 여부 |
|---|---|---|---|---|
| GBS 조직 규모 | 현재 규모 | "20~ 30% 더 작아지겠지만, 생산성은 훨씬 더 높아질 것" (**전망치**) | [S1] | McKinsey 자체 전망 |
| 인바운드/아웃바운드 고객 문의 통화 | 소스에 없음 | "통화의 50 %를 다른 곳으로 돌릴 수 있어서" (관측 일화, 익명 고객사) | [S1] | 고객사 자기보고를 컨설턴트가 전언 |
| 고객사 AI 파일럿 착수 비율 | 소스에 없음 | "절반 정도가 시범 운영을 시작하고" (**인상치**) | [S1] | 컨설턴트 개인 포트폴리오 |
| 은행 FTE 중 운영 관련 비중 | — | "정규직 직원의 50~60%" (현황 추정) | [S2] | McKinsey 자체 추정 |
| 프로세스별 AI 창출 역량 | 소스에 없음 | "40%, 60%, 70% 이상" (**전망치, 조건부**) | [S2] | McKinsey 자체 전망 |
| 담당자 1인당 관리 에이전트 수 | 소스에 없음 | "대략 20~30명의 상담원" (**전망치**) | [S2] | McKinsey 자체 전망 |
| 아시아 금융기관 AI 애플리케이션 사용률 | — | "거의 80%" 사용 보고 / 전 세계 "비슷한 비율"이 실적 영향 없다고 보고 | [S2] | 고객사 자기보고 |
| 리스크 논의 준비 시간 배분 | "데이터를 수집하는 데는 80% 또는 90%의 시간" (현행 문제로 제시) | 명시 안 됨 | [S2] | McKinsey 자체 서술 |
| 은행 프로세스 분해 개수 | — | "약 600개의 프로세스와 하위 프로세스" | [S2] | 익명 고객사 사례 |
| 주요 경제권 생산성 증가 기여 | — | "생산성 증가의 63%를 차지하는 기업이 전체 기업의 2%" | [S3] | McKinsey 자체 연구 |
| 미국 제조업 공석 | — | "약 50만 개" | [S3] | 출처 미표기 |
| 제조·건설 숙련 노동력 부족 | — | "2030년까지 최대 300만 명" (**전망치**) | [S3] | 출처 미표기 |
| 현장 노동자 업무 변화 폭 | — | "40~50%가 향후 3 ~5년 안에" 변화 (**전망치**) | [S3] | McKinsey 자체 연구 |
| 기술 파일럿 실패율 | — | "약 95%가 애매한 상태에 빠진다" | [S3] | **MIT에 귀속된 제3자 인용** |
| 신제품 소비자 피드백 소요 시간 | "몇 주 또는 몇 달" | "몇 시간" | [S3] | McKinsey 자체 서술, 사례 익명 |
| 타사 CEO의 프로세스 마이닝 절감액 | — | "매년 1억 달러 이상 절감" | [S4] | 제3자 CEO 구두 전언(익명) |
| 부분 적용 시 투자 대비 가치 | "20만 달러의 비용" | "200만~300만 달러의 가치" | [S4] | 전 CEO 자기보고 |
| 전체 프로세스 적용 시 가치 | — | "25개 영역에 걸쳐 전체 프로세스를 활용하여 2억 달러의 가치" | [S4] | 전 CEO 자기보고 |
| 카디널 목표치 | — | "첫 해에는 3천만 달러, 둘째 해에는 7천만 달러" (**목표치, 달성치 아님**) | [S4] | 전 CEO 자기보고 |
| 순이익 개선 폭 | — | "순이익을 3~5% 향상" (**전망/일반화**) | [S4] | 전 CEO 자기보고 |
| 서비스의 경제 비중 | — | "100조 달러 규모의 세계 음악 경제에서 60%" | [S5] | McKinsey 자체 수치 |

**제3자 검증치는 사실상 없다.** [S3]의 MIT 인용 1건만이 외부 기관에 귀속되어 있고, 나머지는 전부
McKinsey 자체 추정·전망이거나 익명 고객사/전 CEO의 자기보고를 컨설턴트가 전언한 것이다.

---

### 10.9 소스 간 교차 대조

**(1) 반복 확인된 사실 — 3개 이상 소스에서 일치**

- **파일럿에서 멈춘다는 진단.** [S5] "소규모 시범 단계를 넘어" / [S3] "기술 기반 시범 사업의 약 95%가 애매한 상태에
  빠진다고 합니다" / [S2] "'음악 시범 사업의 늪'이라고 부르는, 좁은 사용 사례에만 매몰되어" — 1년 내내 동일 진단이 유지된다.
- **전체 프로세스(end-to-end) 단위로 봐야 한다는 규범.** [S4] "가장 성공적이고 최대한의 가치를 얻으려면 전체 프로세스를
  살펴봐야 합니다" / [S2] "가치 비중이 높은 영역을 우선적으로 고려하여 엔드투엔드 혁신을 추진하는 것입니다" /
  [S1] "기능별 사일로가 아닌 전체적인 관점에서 프로세스를 바라볼 수 있는 곳입니다" / [S5] "프런트엔드부터 백엔드까지".
- **기능별 사일로가 장애물이라는 진단.** [S4] "그래서 우리에게 있어 가장 큰 과제 중 하나는 기능별 부서 간의 장벽을 허물고" /
  [S2] "AI 관련 사업들이 기능별 및 사업별 사일로 내에서 추진되고 있으며, 재정적 가치와의 연관성이 불분명합니다" / [S1] 동일 취지.
- **풀 스택 관점, 즉 기존 기술 병용이라는 처방.** [S5] "기존 AI와 고급 자동화 및 디지털 기술을 완벽하게 결합하여 다중 객체 아키텍처에
  대한 전체 스택 렌즈를 적용하는 것입니다" / [S2] "세대 AI를 기존 AI, 현대 AI, 자동화 기술, 디지털 애플리케이션과 결합하는
  풀 스택 관점" / [S1] "AI를 적용하여 업무량을 줄이는 차세대 기술과 더불어 (…) 기존의 기술들을 모두 고려해야 한다".
  **[S5]와 [S2]는 문구가 거의 동일하다** — 같은 발표 자료 계열에서 나온 표준 메시지로 보인다.
- **최고경영진 후원/목표 설정.** [S4] "저희는 임원진의 후원을 확보할 예정입니다" / [S2] "우선, 최고 경영진의 최우선 과제가
  되어야 합니다" / [S3] "최고 경영진부터 올바른 분위기를 조성하는 것이 매우 중요하다" / [S5] "대담한 전사적 AIEL 비전".
- **콜센터/고객관리가 대표 사례로 반복.** [S3], [S1] 모두 콜센터·고객주문을 예시로 든다. 단, 결론 방향은 다르다(아래 (4) 참조).

**(2) 한 소스에만 있는 사실**

- 인재 피라미드 → 다이아몬드 전환, 신입 경력 사다리 붕괴 문제: **[S1]에만 있음.**
  "왜냐하면 신입 인재가 기술 전문성을 개발하고 관리자급으로 승진하는 데 걸리는 시간이 예전처럼 길지 않을 것이기 때문입니다." [S1]
  "만약 그런 인재들이 많이 사라진다면, 우리는 다양한 직무 분야에서 사람들을 훈련시키고 디지털 인재를 조직하고 관리할 수 있도록
  준비시키는 새로운 메커니즘을 마련해야 할 것입니다 ." [S1]
- 감사·내부통제의 표본 → 실시간 전수 전환: **[S1]에만 있음.**
- 아웃소싱 우선 vs 자동화 우선의 명시적 분기 논의: **[S1]에만 있음.**
- 3E(효율성/효과성/경험) 프레임: **[S1]에만 있음.**
- 모델리스크관리위원회 승인 게이트: **[S2]에만 있음.** 다른 4개 소스에는 개별 산출물 승인 절차가 없다.
- 담당자 1명당 에이전트 20~30이라는 관리 범위 수치: **[S2]에만 있음.**
- "AI를 무방비 상태로 둘 수는 없다" + 프로세스 인텔리전스를 AI 감시 장치로 쓰는 논리: **[S4]에만 있음.**
- 노동력 부족을 자동화 정당화 근거로 쓰는 논변(50만 공석, 300만 명): **[S3]에만 있음.**
- "인원 감축 같은 실질적인 조치를 취하지 않고도 그곳 상황이 실제로 많이 개선되고 있는 것 같아요." [S4] — 감원 없는 개선을
  명시한 유일한 대목.
- 구체적 달러 목표치(3천만/7천만/2억/1억): **[S4]에만 있음.** 나머지 4개 소스에는 절대 금액이 전혀 없다.

**(3) 시점에 따른 서술 변화 — 이 사례의 핵심 관찰**

| 시점 | 기계의 위치 | 인간의 위치 | 대표 문구 |
|---|---|---|---|
| 2025-08-30 [S5] | "가상 동료"로서 인간을 **대신**해 계획/추론/행동 | 균형을 맞추는 주체 | "인간 동료를 대신하여 계획, 추론 및 행동을 수행할 수 있는 가상 동료가 될 것입니다 ." [S5] |
| 2025-11-13 [S4] | 아직 에이전트 이전. 프로세스/데이터 가시화 도구 | 프로세스 소유자·후원자·AI 감시자 | "왜냐하면 제 생각에는 프로세스 인텔리전스 없이는 AI도 없기 때문입니다." [S4] |
| 2025-11-20 [S3] | 생산성 원동력, 기피 업무 제거 장치 | 기술을 흡수해 가치가 올라가는 현장 인력 | "역사적으로 우리는 자동화와 기술이 노동자들에게 해롭다고 생각해 왔습니다 . 저는 근본적으로 정반대라고 생각합니다." [S3] |
| 2026-02-02 [S2] | 40~70% 역량 창출 전망 + "손가락과 발가락" 실패 경고 | 20~30 에이전트의 관리자, 리스크 판단자, 모델 승인자 | "새로운 엔진 덕분에 동일한 승무원이 탑승한 상태로 항공기가 더 멀리, 더 빠르게 비행할 수 있게 되었습니다 ." [S2] |
| 2026-08-03 [S1] | 업무를 인계받되 GBS를 대체하지 못함 | 증강 대상이자 축소 대상(동시) | "그러니까 AI가 GBS를 아직 대체하지는 않았다는 거죠. 실제로는 그것을 증강시키는 것입니다." [S1] |

이동의 방향은 **대체 예고(2025-08) → 전제 조건 강조(2025-11) → 노동 부족 프레이밍(2025-11) → 조건부 대체 + 관리 범위 확대(2026-02) → 명시적 증강 선언 + 부분 축소(2026-08)**이다. 즉 1년 사이 담론이 **자동화 수사에서 증강 수사로 이동**했고,
그 이동은 규모 축소 전망을 포기하는 방식이 아니라 **'둘 다'로 묶어내는 방식**으로 이루어졌다 [S1].
또 하나의 이동은 **실패 원인 진단의 위치 변화**다: 2025-11에는 실패 원인이 데이터·프로세스 미비였고 [S4],
2026-02에는 부분 자동화("손가락과 발가락")와 사일로였으며 [S2], 2026-08에는 잘못된 과업을 자동화하는 것 자체로 [S1] 옮겨간다.

**(4) 모순 / 긴장**

- **[S5] 내부 모순.** 같은 287단어 안에 "인간 동료를 대신하여 (…) 가상 동료" [S5]와 "인공지능의 힘과 인간의 협력을
  결합하는 데 마법의 공식이 있다" [S5]가 병치된다. 대체와 협업이 조정 없이 공존한다.
- **[S1] 내부 모순(자막 기인 가능).** 3E가 두 번 다르게 열거된다. 처음: "효율성, 효과성, 그리고 고객 경험이라는 측면에서
  경험이라는 세 가지 E를 생각합니다" [S1]. 나중: "세 가지 E(효율성, 개발, 혁신)를 모두 최적화해서" [S1].
  뒤쪽 괄호는 자막 오류일 가능성이 높으나 **원문 확인 불가**이므로 앞쪽을 인용하는 편이 안전하다.
- **[S3] vs [S1] — 콜센터 결론의 방향이 반대다.** [S3]은 "상담원과 대화할 때 사람보다 더 만족감을 느낀다" [S3]며
  기계 응대의 우월성을 시사하고, [S1]은 동일 영역에서 "통화의 50 %" 디플렉션만 내세우면 안 되고 증강 쪽 이야기를 해야 한다며
  "증강 AI와 도움을 받고 (…) 직접 해결할 수 있게 된 거죠" [S1]를 강조한다. 같은 회사의 8개월 간격 자료가 같은 과업에 대해
  다른 처방을 낸다.
- **[S2] 내부의 역설을 화자 스스로 지적.** "인공지능 기반의 에이전트형 AI 애플리케이션이 해당 분야에 미치는 영향은 엇갈리고
  있습니다." [S2] — 80% 사용 보고와 "실적에 큰 영향을 받지 않았다"는 보고가 병존한다.
- **[S3]의 "악순환"은 논문의 악순환이 아니다.** [S3]에 나오는 "제 생각엔 이건 악순환이 아닌 것 같아요." [S3]는
  공급망 복잡성에 대한 발언이며 자동화 편중과 무관하다. **오귀속 위험이 크므로 인용 시 반드시 맥락을 명시할 것.**
- **[S1]의 GBS 축소 전망과 확장 전망이 동시에 제시된다.** "GBS의 규모가 축소될 것으로 예상할 수 있으며" [S1]와
  "하지만 다른 분야에서도 실제로 크게 확장되고 있는 것을 볼 수 있습니다. 더 많은 사람, 더 넓은 범위, 더 많은 예산,
  더 많은 지출." [S1]이 나란히 온다. 화자는 이를 모순이 아니라 상쇄 관계로 처리한다.

---

### 10.10 논문 대조

| 논문 명제(쪽수) | 이 사례의 대응 | 지지/보강/확장/반증 |
|---|---|---|
| AUTO: 기계가 과업 인계, 인간을 루프에서 제외 (p.194) | "GBS 내 여러 영역에서 업무를 인계받을 AI 에이전트 세트" [S1]; "인간 동료를 대신하여 계획, 추론 및 행동" [S5]; 거래성 활동의 RPA/AI 이관 [S1] | 지지 |
| AUG: 인간이 루프에 남아 기계와 밀착 협업 (p.194) | "실제로는 그것을 증강시키는 것입니다" [S1]; "증강 AI와 도움을 받고 (…) 직접 해결" [S1]; 조종사-승무원 비유 [S2] | 지지 |
| AUTO/AUG는 상호배타가 아니라 병존·상호의존 (p.194-197) | "'둘 중 하나'가 아니라 '둘 다'" [S1]; "20~ 30% 더 작아지겠지만, 생산성은 훨씬 더 높아질 것" [S1] | 지지 + 보강 |
| CYCLE: 증강 학습 → 견고화 → 자동화 (p.196-197) | "표준화가 완료되면 AI를 적용하여 추가적인 개선을 추진하는 '우선순위 아웃소싱' 전략" [S1]; "프로세스 인텔리전스 없이는 AI도 없기 때문입니다" [S4] | 보강 — 단, 조직 단위 학습이 아니라 **프로세스 표준화·데이터 정합성**을 문턱으로 재정의 |
| CYCLE: 조건 변화 시 증강으로 회귀 (p.196-197) | 회귀 사례 **해당 소스에 없음**. 규제 불명확성에 의한 진입 보류만 있음 [S2] | 미확인 |
| SPILL: 한 과업 자동화가 인접 과업의 증강 유발 (p.197) | P2P 백엔드 자동화 → 프런트엔드 공급업체 선정을 인간 조직이 인수 [S1]; 감사 표본 → 실시간 전수 [S1]; 리스크 데이터 수집 자동화 → 검토 건수·정확도 확대 [S2]; AI 배치 → 결과 모니터링 과업 신설 [S4] | **강한 지지 + 확장** |
| REINV: 자동화로 확보한 자원을 증강에 재투자 (p.201, UBS) | 명시적 재투자 회계 **해당 소스에 없음**. 시간 재배분 [S2], 인력 이동 전망 [S1]만 존재 | 미확인/약한 대응 |
| RESP: 인간이 프로세스 전체 책임/승인/감사 보유 (p.200) | 모델리스크관리위원회 승인 [S2]; 비즈니스 프로세스 소유자 [S4]; "고위 임원의 후원" [S4]; "전체 과정의 일부에만 갇히게 되어" [S4] | 지지 |
| 증강 학습은 도메인 전문가의 암묵지에 의존, IT/외부업체 위임 불가 (p.195) | "비즈니스 주도형 IT 지원 방식이 되어야 합니다. IT 주도형 비즈니스 지원 방식이 되어서는 안 됩니다." [S4]; IT의 자체구축 선호가 10배 비싸진다는 경고 [S4] | **강한 지지** — 단, 이 시리즈 자체가 외부 컨설팅사 발화라는 점에서 수행모순의 소지 있음(10.11) |
| 기계 한계 ①목적/자아 부재 (p.198) | "AI 에이전트는 명확하게 정의된 직무 설명을 바탕으로" 행동한다 [S5] — 목적은 인간이 부여 | 지지 |
| 기계 한계 ②제약 완화된 옵션만 제시 (p.198) | FP&A 보조 전문가가 "다음으로 어떤 두세 가지 조치를 취해야 할까요?"까지만 제시 [S1] | 지지 |
| 기계 한계 ③훈련된 과업에 국한 (p.198) | "손가락과 발가락 문제" [S2]; "현장 분석가의 역량을 자동화하는 것은 매우 어려웠습니다" [S2] | 지지 |
| 기계 한계 ④감각/감정/사회기술 부재 (p.198) | 직접 대응 약함. 오히려 반대 방향 주장이 있음: "상담원과 대화할 때 사람보다 더 만족감을 느낀다" [S3] | **부분 반증(주장 수준)** |
| 한쪽 편중 시 악순환 (p.199) | 효율 편중 탈피 선언: "효율성, 즉 비용 절감을 신속하게 달성하는 방법에 대한 논쟁에서 벗어나 보다 포괄적인 목표를 향해 나아가고 있다" [S1]; "서비스 운영이 더 이상 효율성에 관한 것이 아니라는 점" [S5]. 반대로 [S3]은 생산성/비용 언어를 전면에 둔다 | 보강 + 시리즈 내부 긴장 |
| 기계는 조직 내 새로운 행위자 계급 (p.204) | "가상 동료" [S5]; "대략 20~30명의 상담원이 한 명의 담당자에 의해 관리될 것" [S2]; "영업팀을 관리할 수 있는 인재가 필요합니다" [S1] | **강한 지지 + 확장** |

**확장 지점.**
첫째, 이 사례는 SPILL을 논문보다 한 단계 더 밀고 간다. 논문의 SPILL이 인접 과업의 증강 유발이라면, [S1]의 감사 사례는
자동화가 **과업의 수행 빈도 자체를 표본에서 전수로 바꿔** 인간이 감당해야 할 판단 대상의 총량을 늘린다는 것을 보여준다
("특정 표본 크기에 도달하면 갑자기 AI를 활용하여 내부 통제와 같은 분야에서 실시간 처리를 수행할 수 있게 됩니다" [S1]).
이는 증강의 질적 변화가 아니라 **증강 대상의 양적 팽창**이라는, 논문이 명시하지 않은 파급 경로다.
둘째, 논문의 CYCLE은 조직학습의 시간축인데, 이 시리즈는 그 문턱을 **프로세스 표준화 정도와 데이터 정합성**이라는
기술적·행정적 조건으로 치환한다 — "프로세스 인텔리전스 없이는 AI도 없기 때문입니다" [S4]. 즉 증강→자동화 전환이
암묵지의 형식지화가 아니라 **가시성 인프라 구축**의 문제로 재서술되며, 이는 논문 p.195의 암묵지 명제와 긴장한다.
셋째, p.204의 새로운 행위자 계급 명제는 이 사례에서 **관리 범위(span of control) 문제**로 구체화된다. 인간 1인이
"20~30명의 상담원"을 관리한다는 [S2]의 전망과 "영업팀을 관리할 수 있는 인재" [S1] 서술은, 기계 행위자의 등장이
조직도의 계층 구조 자체를 재설계하게 만든다는 점을 보여준다 — 피라미드에서 다이아몬드로 [S1].
넷째, 이 사례는 논문이 다루지 않은 **증강의 세대 재생산 문제**를 제기한다. 신입이 거래성 업무를 거치며 전문성을 쌓는 경로가
사라지면 증강을 수행할 인간 자체가 공급되지 않는다는 [S1]의 우려는, 논문의 선순환 논리가 인력 파이프라인이라는
전제 위에 서 있음을 드러낸다.

---

### 10.11 인용 시 주의사항

1. **성숙도 — 이 사례에는 완료된 도입 사례가 거의 없다.** 수치의 대다수가 "예상합니다", "될 것입니다", "믿습니다"로
   끝나는 전망치다. 특히 [S1]의 "20~ 30%", [S2]의 "40%, 60%, 70% 이상"과 "20~30명", [S3]의 "300만 명"과 "40~50%"는
   모두 전망치이므로 관측된 성과로 인용하면 안 된다.
2. **자체보고 문제.** [S4]의 달러 수치는 전 CEO의 회고 자기보고이며, "매년 1억 달러 이상 절감" [S4]은 **또 다른 익명 CEO의
   구두 전언을 다시 전언한 2차 전언**이다. "첫 해에는 3천만 달러, 둘째 해에는 7천만 달러" [S4]는 **목표치**이지 달성치가 아니다.
   달성 여부는 해당 소스에 없음.
3. **귀속 문제.** [S1]의 "통화의 50 %" 문장은 발화자가 **비판적 예시로 인용한 문장**이다. 원문 맥락은
   "핵심은 단순히 (…)라고 보여주는 것보다, 이 방법이 고객과 회사 모두에게 어떻게 더 나은 결과를 가져오는지 보여주는 것" [S1]이다.
   50%를 "성과"로 단독 인용하면 화자의 의도를 뒤집는다.
4. **귀속 문제 2.** [S3]의 "악순환" 언급은 공급망 복잡성에 관한 것이며 논문 p.199의 자동화 편중 악순환과 무관하다.
   교차 참조 시 반드시 분리할 것.
5. **자막 오류가 매우 심각하다.** 확인된 것만:
   - GBS 약어 확장이 소스 내에서 3번 다르게 나타남: "GBS(Global Business Strategy)", "GBS(그룹 비즈니스 전략)",
     "GBS(게임 기반 서비스)" [S1]. 정확한 확장인 "Global Business Services"도 한 번 등장한다 [S1].
   - "GBS"가 후반부 대부분 "GPS"로 오기됨 [S1]. 인용 시 원문 그대로 옮기되 대괄호 주석이 필요하다.
   - "개인적으로는 길랑- 바레 증후군의 사망률이 지나치게 과장되었다고 생각합니다." [S1] — GBS(약어)를
     길랑-바레 증후군으로 오역한 것으로 보인다. 이 문장은 **원문 의미 복원 없이 인용하면 안 된다.**
   - "음악"이 문맥과 무관하게 반복 삽입됨: "세계 음악 업계의 최고 경영진" [S1], "AI를 음악 플랫폼으로 활용" [S2],
     "'음악 시범 사업의 늪'" [S2], "100조 달러 규모의 세계 음악 경제" [S5]. 원 단어는 이 파일들만으로 복원 불가.
   - "AIEL", "AIE", "Aentic AI", "인테닉 AIEL", "신경 인공지능( NAI)", "인공지능(EI)", "RARI(수익성 있는 투자)",
     "카디널 32", "COOS", "GPS 우선 우측 아웃소싱", "우측 해안 우선 전략"(right-shore 추정) 등 다수의 표기 붕괴.
   - 진행자 이름 표기가 한 파일 안에서 흔들림: [S2]에서 "스테파니 룩센버그" → "다파니" → "다프네 룩셈부르크".
     [S3]의 "McKenzie", "Lucia Raheli", "Robera Fisaro"도 표기 붕괴다.
   - 문장 부호 앞뒤 공백 불규칙(예: "20~ 30%", "통화의 50 %", "3 ~5년", "9~12 개월"). **인용 시 공백을 정리하면
     원문과 불일치**하므로 그대로 옮길 것.
6. **수행모순 주의.** [S4]는 "비즈니스 주도형 IT 지원 방식이 되어야 합니다" [S4]라며 외부·IT 위임을 경계하지만,
   이 시리즈 전체가 외부 컨설팅사의 판매 담론이다. 논문 p.195 명제의 지지 근거로 쓸 때 이 층위를 명시해야 한다.
7. **[S5]는 근거로서 얇다.** 287단어이며 화자 이름·소속·사례가 전혀 없다. 프레이밍의 시점 기준점으로만 쓰고
   실증적 주장의 근거로는 쓰지 말 것.
8. **익명성.** 이 시리즈에서 실명이 나오는 조직은 카디널 헬스 [S4], 도요타(예시) [S3], JP모건 체이스와 DBS [S2]뿐이며,
   그중 JP모건과 DBS는 **McKinsey의 다른 기사/인터뷰를 인용한 2차 언급**이다. 나머지 사례는 전부 익명 고객사다.
9. **시점 표기.** 5개 자료는 모두 채널 수집분이므로 헤더 "업로드일"이 업로드 시점이다. 다만 팟캐스트 녹음 시점과
   업로드 시점의 간격은 **해당 소스에 없음**. [S1]의 "지난 9~12 개월", [S2]의 "3분기 실적 발표" 같은 상대 시점 표현은
   녹음 시점 기준이므로 업로드일과 정확히 대응한다고 단정할 수 없다.

---

**요약.** 이 부록은 McKinsey가 2025-08-30부터 2026-08-03까지 발표한 5개 영상을 시점 순으로 배열해, 자동화/증강 담론이
가상 동료가 인간을 대신한다([S5], 2025-08) → AI 도입 이전에 프로세스·데이터 가시성이 먼저다([S4], 2025-11) →
자동화는 노동 부족 해소이자 기피 업무 제거다([S3], 2025-11) → 40~70% 역량 창출이 가능하되 부분 자동화는 실패한다([S2], 2026-02) →
AI는 GBS를 대체하지 않고 증강한다([S1], 2026-08)로 이동했음을 기록했다. 이론 대조에서는
SPILL(P2P 프런트엔드 확장, 감사 표본→실시간 전수)과 p.204(가상 동료·1인당 20~30 에이전트·다이아몬드 인재모델)에 대한
강한 지지가 확인되었고, RESP는 [S2]의 모델리스크관리위원회 승인과 [S4]의 프로세스 소유자·경영진 후원으로 뒷받침된다.
반면 REINV(자원 재투자)와 증강 회귀 사례는 5개 소스 어디에도 없어 미확인으로 남겼다.
한계는 세 가지다. 첫째, 단일 조직의 before/after가 사실상 없고 수치의 대부분이 컨설팅사 자체 전망치이며, 제3자 귀속은
MIT 인용 1건뿐이다. 둘째, 한국어 기계번역 자막의 손상이 심해(GBS→GPS/길랑-바레, "음악"의 무맥락 삽입, AIEL/RARI 등)
일부 문장은 원문 의미를 복원할 수 없어 그대로 인용하되 주석이 필수다. 셋째, 이 자료들은 판매 담론이므로 성과 주장과
규범 처방을 분리해 읽어야 하며, 특히 [S4]의 비즈니스 주도·IT 지원 규범을 논문 p.195의 지지 근거로 쓸 때는
발화 주체가 외부 컨설팅사라는 수행모순을 함께 표기해야 한다.


---


# 제3부 · 종합

## 5. 전환 판정 기준의 유형학 — 논문이 비워둔 자리

논문은 증강→자동화 전환 조건을 "모델이 **충분히 견고(sufficiently robust)**해지면"이라고만 쓴다
(p.196). 코퍼스는 이 빈칸을 서로 다른 여섯 방식으로 채운다.

| 유형 | 사례 | 판정 기준 |
|---|---|---|
| **계측형** | R1 RCM | "as accuracy is validated" + 확대 배포 가부를 판별하는 HITL 대시보드 |
| **검증가능성형** | Zapier 재무 | ① 규칙 열거 불가(복잡성) **논리곱** ② 출력의 정오를 인간이 판정 가능(범위 한정). 두 번째 조건이 깨지면 결정론+인간검토로 **되돌린다**는 역조건까지 명시 |
| **반복관찰형** | Nokia | "100번 정도 같은 결과가 나오면 시스템 내부에서 무슨 일이 일어나는지 완전히 이해하지 못하더라도 신뢰를 갖게 될 겁니다" — 설명가능성이 아니라 **재현 횟수**가 기준 |
| **정량 이중게이트형** | Siemens | 신뢰성 임계치("거의 100%에 가까운 신뢰성", "99.99%") **+** ROI 임계치 |
| **통제완화형** | Deloitte | 과업을 넘기는 게 아니라 **통제 장치를 사후에 제거**한다 — "확신이 생기면 이러한 제어 기능 중 일부는 시간이 지남에 따라 되돌려지거나" |
| **선행조건형** | McKinsey | 전환 기준이 아니라 **문턱** — 프로세스 표준화·데이터 정합성이 먼저다. "프로세스 인텔리전스 없이는 AI도 없기 때문입니다" |
| *(기준 부재)* | ServiceNow | 5개 소스 어디에도 승격 임계 기준이 없다. 자동화율만 발표되고 그 문턱은 서술되지 않는다 |

여섯 유형은 서로 다른 층위에 있다 — 계측(대시보드) / 논리(검증가능성) / 통계(반복) /
수치(임계치) / 거버넌스(통제 완화) / 데이터(선행조건). **논문 명제를 조작화하는 방법의 유형학**으로
쓸 수 있고, 조직이 어느 유형을 택하는지가 곧 그 조직의 위험 태도를 드러낸다.

## 6. SPILL의 변형 — 논문의 선형 도식으로 안 잡히는 것들

논문의 spillover는 "한 과업의 자동화 → 인접 과업의 증강"이라는 **선형 1회 파급**이다.
코퍼스에는 여섯 가지 변형이 있다.

1. **샌드위치형** (TK Elevator) — 파급이 한 방향이 아니라 **현장 방문을 축으로 앞뒤 양쪽**에서
   동시에 일어난다. 방문 전에는 이벤트 판독 자동화가 "거기에 갈 때는 1층으로 가지 마세요" 같은
   **번역 노동**을 새로 만들고, 방문 후에는 RAG 자동화가 **음성 디브리핑**을 연다.
   자동화가 인간 과업을 **감싼다**.
2. **메타·재귀형** (Siemens) — 파급 대상이 현장 과업이 아니라 **자동화를 만드는 과업**이다.
   공장 자동화 → 엔지니어링 증강 → 시뮬레이션 구축이라는 새 인간 과업 발생 → 그 과업이 다시
   코딩 에이전트로 증강된다. 1회가 아니라 **재귀적**이다.
3. **자동화 복제형** (ServiceNow) — 인접 영역에서 관측되는 것은 **증강이 아니라 자동화의 복제**다.
   IT에서 된 것을 HR·재무·CS·영업운영으로 옮긴다. 증강 유발 근거는 소스에 없다.
   → 논문 SPILL의 **변형이자 반례 후보**.
4. **측정·거버넌스형** (Deloitte) — 파급 대상이 인접 *실행* 과업이 아니라 인접 *측정* 과업이다.
   92% 자동화가 "송장 처리 속도와 같은 관련 지표는 이전과 같을까요?"라는 **지표 재설계 노동**을 낳는다.
5. **이중 파급형** (Nokia) — 코어 자동화가 인접 과업(관측 미들웨어·DNS·스토리지·라디오 에너지)의
   **자체 개발**을 낳고, 동시에 인간의 시선을 이동시켜 그 빈자리를 다시 자동화가 메운다.
   증강과 새 자동화 요구가 **함께** 발생한다.
6. **조직 인수형** (McKinsey) — P2P 백엔드 자동화가 프런트엔드(공급업체 식별·선정)를
   **인간 조직(GBS)이 인수**하게 만든다. 파급이 과업이 아니라 **조직 경계**를 움직인다.

## 7. RESP 구현의 유형학

논문 p.200은 "통합에는 인간이 프로세스 전체 책임을 보유해야 한다"고만 쓴다. 구현은 다섯 갈래다.

| 유형 | 사례 | 구현 |
|---|---|---|
| **내부통제형** | Zapier 재무 | 인간 최종승인 불가침 + 전수 로깅 + **직무분리**. 승인 단계를 실행 주체와 분리하고 "최초의 워크플로우를 누가 만들었는지와는 관계없이" 적용 → **경로 독립적 통제** |
| **제품기능형** | ServiceNow | 킬 스위치, AI 관제탑(자산 수명주기 모니터링), 에이전트 신원관리("인간 및 비인간을 포함한 모든 신원"), 권한 회수 버튼 |
| **외부 제3자형** | R1 RCM | 책임의 수신자가 조직 내부가 아니라 **지불자·규제기관**. audit trail이 보험사 지급거절 이의제기와 정부 정기감사를 동시에 겨냥 |
| **데이터 계보형** | TK Elevator | 승인권이 아니라 **입력 의미론이 확정되는 시점**에 책임이 걸린다. "모든 데이터의 감사 가능성", "같은 질문에 대해 여러 개의 수치가 존재" 문제의 해소 |
| **원칙 선언형** | Siemens, Deloitte | "remain in human hands" 같은 선언과 기록 인프라는 있으나 **개별 승인 절차는 소스에 없음** |

주의할 대비 하나. ServiceNow 소스에는 "따라서 워크플로우 자체에 위험 관리 정책이 내장되어 있으므로
… **그래서 사람이 실수할 수가 없어요**"라는 진술이 있다. 이는 인간의 **책임 보유**가 아니라
**재량 제거** 방향이라 논문 RESP와 결이 반대다. 벤더 어휘의 "거버넌스"를 논문의 통합 조건으로
그대로 매핑하면 코딩 오류가 난다.

## 8. 논문을 확장하는 관측 6가지

**① 학습 사다리의 소멸 — 두 소스에서 독립 확인**
McKinsey: "**신입 인재가 기술 전문성을 개발하고 관리자급으로 승진하는 데 걸리는 시간이 예전처럼
길지 않을 것**입니다. 만약 그런 인재들이 많이 사라진다면…"
Deloitte 계열 [S3]: "차세대 지도자들은 이러한 학습 경험을 갖지 못할 것입니다."
논문 p.201의 "선택적 탈숙련 + 전략적 재자격화" 선순환은 **증강을 수행할 인간이 계속 공급된다**는
전제 위에 서 있다. 자동화된 초급 과업이 곧 학습 사다리였다면 그 전제가 무너진다.
**서로 다른 두 컨설팅 조직이 독립적으로 같은 문제를 지적한 유일한 논점**이다.

**② 자동화가 인간 과업의 *범위*를 확장한다**
삼성전자 VOC(주 30여만 건 중 "기존에는 5% 7%만 보던" 것을 "에이전트가 전체 다 봐주니"),
McKinsey 감사(표본 → 실시간 전수). 논문은 자동화를 주로 "인간의 시간을 비운다"로 다루는데,
여기서는 **인간이 다룰 수 있는 문제 공간 자체**가 넓어진다. p.200의 "경로의존성 타파" 확장.

**③ 성과 지표(분모)가 재정의된다**
Deloitte: "92% 자동화하면 송장 처리 속도 같은 관련 지표는 이전과 같겠는가."
논문은 기존 지표 위에서 성과를 논한다. 이 관측은 저장소 코드북의 `sig_denominator` 축과 직결된다.

**④ 기계가 인간에게 질문하는 역할 역전**
TK Elevator의 음성 디브리핑 에이전트는 **기술자에게 묻는 주체**다. 논문의 human-in-the-loop은
인간이 기계를 감독하는 구도인데, 여기서는 기계가 인간의 암묵지를 **호출한다**.

**⑤ 기계가 기계를 견제한다**
Zapier FX 포드에서 환율 불일치 검사기가 추출기의 출력을 웹에서 독립 재조회해 대조하고,
5% 초과 시 자동 수정 후 인간에게 보고한다. 논문 p.200의 상호 검증(Hoc, 2001)은 인간↔기계
2자 구도인데, 여기에 **기계↔기계 층**이 얹히고 그 결과가 다시 인간으로 간다.

**⑥ "새로운 행위자 계급"이 은유가 아니라 인프라가 된다**
ServiceNow는 에이전트를 "채용/온보딩"하고 성과를 평가하며, 인간과 동일한 접근제어 체계로 관리한다
("인간 및 비인간을 포함한 모든 신원", 권한 정보 규모 언급). 삼성SDS는 마켓플레이스 등록·에이전트
옵스·토큰 비용 통제를 건다. McKinsey는 "담당자 1인당 상담원 20~30명"이라는 관리 폭을 제시한다.
논문 p.204의 명제가 **신원관리·비용회계·관리 폭이라는 실물 인프라**로 구현된다.

## 9. 판독 결과에 대한 유의사항

1. **표본이 공급측에 완전히 치우쳐 있다.** 44개 소스 전부가 벤더·컨설팅 공식 채널 자료다.
   제3자 검증치는 **0건**이다. 모든 성과 수치는 자체 보고치로 취급해야 한다.
2. **실패·악순환 사례가 없다.** 논문이 경고한 자동화 편중의 탈숙련·경로고착(p.199)은
   일반론으로만 등장하고 **특정 조직의 실패로는 서술되지 않는다.** 구조적 편향이며
   `sig_deskilling` 출현율 ~0%(`docs/CODEBOOK_v2.md`)와 일치한다.
   **선순환 사례만 모아 결론을 내면 생존 편향이 된다.**
3. **성숙도가 제각각이다.** 운영 중(ServiceNow·Zapier·Nokia), 10년 축적(TK Elevator·Siemens),
   착수 2개월 계획(R1 RCM·우리은행), 목표 상태 서술(Deloitte 영업 에이전트), 전망치(McKinsey
   20~30%). **같은 표에 놓되 시간 지평을 구분해 읽어야 한다.**
4. **"자율"의 정의가 유동적이다.** ServiceNow 소스에서 벤더 스스로 "현재 자율 운영 방식은
   사람이 개입해야 한다"고 말한다. 벤더 어휘의 autonomous를 논문의 automation으로 그대로
   매핑하면 코딩 오류가 난다.
5. **자막 붕괴가 광범위하다.** 각 사례 문서의 11절에 오류 목록을 전수 기재했다. 대표적으로
   "더 가치 있는 **음악** 관련 업무"(ServiceNow, 재배치 목적지 판독 불가), "휴먼 인더브로"(삼성SDS),
   "디오이트/디오테/Deote"(Deloitte), "Netswuite"(NetSuite), "**길랑-바레 증후군**"(McKinsey에서
   GBS 약어 오역), "폭의 시대"(The Age of With), "포르노 관련 해결책"(point solutions 추정).
   **인용 시 교정하지 말 것** — 기계 대조 검증에서 불일치가 난다.
6. **귀속을 반드시 확인할 것.** 채널 소유자 ≠ 사례 주체인 경우가 많다.
   Deloitte 사례는 Intel 채널에 있고, ServiceNow 키노트 분량의 대부분은 FedEx·CVS·NVIDIA·Google
   발화이며, Zapier 거버넌스 장치 대부분은 Rivian·Kayak 발화이고, Zapier 3분법은 Glean 발화이며,
   삼성SDS 소스의 암묵지 논의는 서울대 교수와 KASMO 단장의 발언이다.
7. **수행모순 층위.** p.195의 "증강 학습은 도메인 전문가 암묵지에 의존하며 IT/외부업체에 위임
   불가"라는 명제를 **가장 강하게 지지하는 발화들이 외부 컨설팅사·벤더의 것**이다. 동시에 같은
   소스들에서 Accenture 7,000명 투입, Deloitte 컨설턴트의 고객사 에이전트 대행 구축이 서술된다.
   이 명제의 지지 근거로 인용할 때 **화자의 이해관계를 반드시 병기**해야 한다.
8. **논문 사례와의 대조.** 논문의 핵심 사례 Symrise는 코퍼스 언급 **0건**이고, JP Morgan Chase·
   Unilever·UBS도 자동화–증강 맥락으로는 등장하지 않는다. **학술 정전과 실무 담론이 공유하는
   사례가 사실상 없다.**

## 10. 산출물

- `docs/cases/*.md` — 사례별 상세 문서 10건 (각 11절 구조, 총 약 535KB)
- `analysis/paradox_scan.csv` — 5,742건 × 6축 규칙기반 코딩
- `scan_paradox.py`, `cooc.py` — 재현 스크립트
