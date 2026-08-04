## 사례 1 - R1 RCM x Palantir : 의료 코딩

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
