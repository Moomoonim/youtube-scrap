# 수집 콘텐츠 검토 보고서 (v4.1, 2026-07-22)

> **1,105건 전체 코퍼스** 기준 전수 정독 분석. 심층 정독 ~860건(키워드 76 + 채널 95여 개 대부분), 최신 자동수집 잔여분 일부는 인벤토리 상태.
> 자동분류: **AX 341 / DX 21 / AT 4 / 미분류 739** (채널 135개, 한국어 다수).
> 다음 회귀분석·코딩 작업 전에 읽을 것. v3(771) 대비 신규·심층 채널: **OpenAI·Stability AI·Mercedes-Benz·Google Cloud Tech·Zapier·AWS Developers·Hugging Face**(+ Apple·Siemens·Pinecone·SAP·ServiceNow 백필 심화)와 인사이트를 반영.
> **v4.1 증분(954→1,105, +151)**: 신규 채널 **Infosys·Anthropic·IKEA**. 결론은 **거의 전부 확증적**(기존 인사이트를 바꾸는 자료 없음). 두 가지 미세 뉘앙스만 추가 — (a) **화자 대리(proxy) 구조**, (b) **채널 내부 분열**(아래 §1·§0-3 참조).

---

## 0. 핵심 인사이트 — 담론에서 작동하는 "알고리즘"

이 코퍼스에서 단순 채널 인벤토리를 넘는 **구조적으로 반복되는 조작(=담론의 알고리즘)**이 발견된다. 프로젝트 궁극 프레임(의사결정의 알고리즘화)과 직결된다.

### A. "분모 바꾸기(denominator swap)" — 최상위 발견, 이제 3층 구조
**기존 지표가 실망스러운 ROI를 보이면, 담론은 실망을 인정하는 대신 '무엇을 셀 것인가'(측정 단위)를 바꾼다. 그리고 그 조작을 하는 주체는 언제나 새 지표에서 이득을 보는 쪽이다.**

| 층위 | 주체 | 낡았다고 규정한 지표 | 새로 미는 지표 | 이득 |
|---|---|---|---|---|
| 비즈니스 | NVIDIA·Arm | 토큰 수 | 동시 에이전트 수 / 와트당·달러당 산출 | 하드웨어 수요 정당화 |
| 비즈니스 | Apple·Nokia | 개발자 토큰비 / GPU 프리미엄 | "무료"(→PCC·온디바이스·구독으로 이전) / "no GPU premium" | 비용 비가시화 |
| 비즈니스 | 컨설팅(BCG·Accenture) | 사용량 | 비즈니스 성과 / 학습 속도 | 컨설팅 필요성 |
| 비즈니스 | Accenture | 직무(job) | 스킬 아키텍처 | 인재 재교육 상품 |
| 비즈니스 | Salesforce·Deloitte | (자인) 대시보드 실사용률 20~30% | 파이프라인·시간절약 환산액 | 도입 서사 유지 |
| 비즈니스 | Zapier(Guy Yalif) | 전환율 6% | "6배"(LLM 유입 vs SEO) | AX 마케팅 전환 서사 |
| **인프라/컨텍스트** | Palantir·ServiceNow·Databricks·Pinecone | 모델 성능 | 온톨로지·거버넌스·벡터 계층 | 데이터 락인 |
| **연구(신규)** | Hugging Face(Sara Hooker) | 모델 크기(scaling law) | 적응 비용(adaptation) | 신생 랩 포지셔닝 |
| **평가(신규)** | AWS·Zapier·Google | 데모 성공 | 자사 벤치마크·eval 통과율 | "어느 에이전트가 좋은가"의 정의권 |

→ **지표를 쥔 자가 ROI 서사를 쥔다.** 이것이 의사결정의 알고리즘화의 메타층위: 기업 안에서 AI가 결정하기 이전에, 'AI 가치를 어떻게 계산할지'라는 판단 기준 자체가 이해당사자에 의해 재작성된다. v4에서 이 명제가 **최상위 연구층(스케일링→적응)과 평가층(벤치마크 정의권)까지 관통**함이 확인됐다.

🔑 **분모스왑 실시간 포착**(Google Cloud Tech "How to speed up 80%"편) = 이 인사이트의 가장 선명한 단일 실연. 1시간 내 UI 버그 수정이라는 원래 목표는 **실패**(타이머 0)했으나, 발표자는 즉시 "사실 우리가 이겼다 — 계측→80% 단축→Cloud Run 배포, 축구로 치면 3:1 승리"로 성공 지표를 재정의한다. 목표 미달을 카메라 앞에서 실시간으로 승리 서사로 갈아끼우는 장면.

### B. 그 외 반복 구조
1. **"95% 실패" 개막 의식** — MIT "95% 실패", 맥킨지 "88% 도입 vs 39% 수익화", "AI 프로젝트 80% 실패", Google Emergent "코딩앱 95% 상용화 실패, 나는 되는 5%를 찾는다" — 한/영·컨설턴트·학계·벤더 불문 반복. 문법: [파국적 실패율 인용]→["기술이 아니라 사람·프로세스·데이터 탓"]→[내 프레임만 예외]. = **책임 전가 알고리즘**.
2. **"AI는 기술 문제가 아니라 사람 문제"** — 범용 명제로 확정(Upstage·Palantir·김건우·BCG·McKinsey·Zapier Amit·Google Home Depot). 책임전가 문법의 핵심.
3. **공급/수요 담론의 분열 + "화자 대리(proxy)" 세탁**(v4.1) — 공급측("OpenClaw 모멘트, 추론 15배 폭발", Hugging Face 모델·데이터 제조)과 수요측("95%가 성과 없음", Qdrant/AX강의 도입·비용·규정)이 양립 불가. 이 간극이 버블 질문의 실체이자 검증가능한 특이점. 🔑 **혼합 변종**: Infosys의 on-topic 자료는 컨설팅사가 *직접* 말하지 않고 고객사 임원(Sandvik 디지털책임자·Swedbank CIO)을 화자로 세워 **공급측 담론을 수요측 증언으로 세탁**한다. "누가 말하는가"를 K1 태깅 시 벤더 자신 vs 대리 고객으로 구분 필요(OpenAI 레퍼런스 고객 포맷과 동형).
4. **온톨로지/컨텍스트 계층 = 격전지, 이제 "문서 하네스"까지 확장** — Palantir(온톨로지)·ServiceNow(context graph)·Databricks(Unity Catalog)·Pinecone/Weaviate/Qdrant(벡터)·**LlamaIndex("기업가치 90%가 비정형 문서에 묻힘"→PDF 파싱 관문화)·Vultr("데이터 중력·주권"→벡터DB 위치 관문화)·Google(OTel·App Hub)** 모두 "데이터+거버넌스 계층을 쥔 자가 에이전트 시대 지배"라 주장. AX의 진짜 락인은 모델이 아니라 컨텍스트/거버넌스 계층.
5. **정량성의 역설** — AI를 전면에 내세운 채널일수록 검증가능 정량 성과가 부재. 가장 단단한 숫자는 AX가 아니라 인접 상품(칩·영상장비)을 파는 채널, 또는 자사 실무를 공개하는 소규모 채널(AX 강의)에서 나옴.
6. **배수(multiple) 수사학** — 컨설턴트·벤더는 분모 없는 배수("4.4배", "16.5배", "10배 은행", "6배 전환")로 말함. 반증 불가하면서 인상적.
7. **"에이전트=인력(AI Workforce)" 프레임의 국제적 수렴** — Alibaba("디지털 실리콘 전문가팀"), SK AX("AI workforce"), TCS, ServiceNow("L1 대체"), **OpenAI("팀→상담원 하나"·"위임 가능한 노동력"), Google(PayPal "에이전트=재입사한 인턴"), Zapier(Lovable "BDR 조직 대신 AI 에이전트"), AX강의("AI 직원 고용")**. 노동을 '인력 단위'로 세는 담론이 미·중·한 공통.
8. **자동차 산업 AI 태도 4분화**(v4 확장) — 침묵(Nissan·Volvo) → **서사적 침묵(Mercedes: AI를 "에어밸런스"처럼 이름조차 안 붙이고, 그 공백을 140주년 헤리티지·자선·소재지속가능성으로 능동적으로 메움)** → 완곡 내재화(BMW: ADAS를 "AI"로 안 팜) → 정체성화(Tesla: AI/에너지/로봇 기업으로 자기재정의). "AI를 말하지 않는 방식"에도 전략적 스펙트럼 존재.
9. **소버린 AI의 하이브리드 실용주의** — NAVER·LG: 자국 모델(HyperCLOVA/EXAONE)+데이터주권(뉴로클라우드)을 내세우면서도 미국 Claude를 제어 UI로 병용. "소버린 vs 종속" 이분법이 아니라 계층별 선택.
10. **NEW: "신뢰성·평가(eval)가 새 전장"** — AWS(Steering/Evaluating Agents/Swarm 안전), Zapier(Automation Bench), Google(Arize/OTel). 에이전트 신뢰성이 미검증인 상태에서 "평가·벤치마크를 정의하는 자"가 "어느 에이전트가 좋은가"를 규정 → 온톨로지 land-grab의 **성능 판정 버전**. 분모스왑 평가층(§0-A)과 짝.
11. **NEW 축: "사람 소거 vs 사람 전면화"** — 동일한 알고리즘화 하부구조를 두고 **AWS**는 토큰·컨텍스트·평가라는 순수 원가/신뢰성 엔지니어링 언어로 번역(사람 부재), **Zapier/Google/AX강의**는 헤드카운트·판단·deskilling을 전면화. 같은 기질(substrate), 반대 표면언어. 벤더의 청중(개발자 vs 경영진)이 담론 표면을 결정 → 분석 시 "청중 통제" 필요.

---

## 1. 코퍼스 지도 — AI/AX 담론 밀도 순

| 밀도 | 채널 | 성격 |
|---|---|---|
| ★★★ | NVIDIA·NVIDIA Developer, Arm, Siemens, Nokia, Wayve, Zoox, Tesla | "AI 팩토리"·"물리적 AI"·에이전트·자율주행. 수치·비용구조 언어 풍부 |
| ★★★ | LG AI Research, Upstage, Palantir, ServiceNow, SAP, IBM, Salesforce, Databricks, Alibaba Cloud, **Google Cloud Tech**, **AWS Developers**, W&B·Qdrant·Pinecone·Weaviate·Snowflake | AI가 곧 제품. 도입방법론·평가·거버넌스·온톨로지·에이전트 하네스 |
| ★★★ | **OpenAI** | 위임(delegation)·에이전트·레퍼런스 고객(BNY·Shopify·Virgin) 포맷 |
| ★★☆ | Meta(Boz), Boston Dynamics, Microsoft Azure, Google Developers·DeepMind, Meta Developers, SK하이닉스, GE HealthCare, Accenture, TCS, **Zapier**, ElevenLabs, Runway, Apple Developer, GitHub, Replit, NAVER Cloud, Unilever(IR), **Stability AI** | AX를 자사 제품/비전·투자자 서사·GTM에 접합 |
| ★★☆ | **Hugging Face** | ⚠️ 예외 — 엔터프라이즈 비용 담론이 아니라 **연구/OSS 공급측**(모델·데이터·로보틱스 제조). "채널명≠담론성격"의 최신 사례 |
| ★☆☆ | SK텔레콤, Telenor, Amazon, Waymo, Mayo Clinic, LinkedIn, Schneider, Microsoft(Nation PR), **Infosys(고객증언 2편만 실질)** | AI가 마케팅 소재(보안·안전·감성·노동시장·정당성) |
| ☆ | Swisscom, Reckitt, Nissan, Volvo, BMW, **Mercedes-Benz**, NTT DATA, Suno, Luma, Philips, Perplexity, Cohere(학술), **Anthropic(모델제작사 자체 안전/제품 코뮤)**, **IKEA(리테일·자막 사실상 공백)**, kakao_tech(2021) | AI 담론 희박 — 그 자체가 신호(자동차 침묵/서사적 침묵, 학술, 모델제작사 PR, pre-AX 기준선 등) |

키워드 수집분(76건, `transcripts/2026-*/`)은 한국어 AX 강의·컨설팅·정책·언론 콘텐츠가 주력이며 연구 주제에 최고 밀도. 특히 2026-07-22 "데이브의 개발 생활" AX 강의는 **의사결정 알고리즘화의 교과서적 실연**(아래 §6).

⚠️ **"채널명 ≠ 담론 성격"**: Cohere·Hugging Face(학술/OSS)·Microsoft·Anthropic(브랜드/모델PR)·BMW/Mercedes/IKEA(광고·헤리티지·리테일)·Zoox/TCS(오수집) — 채널명으로 성격을 예단하면 안 됨. 코퍼스 분류는 채널이 아니라 **영상 단위**로 해야 함. 🔑 **v4.1: 명제가 "채널 내부" 수준으로 확장** — Infosys 한 채널이 순수 AX담론(Sandvik·Swedbank 고객증언)과 순수 채용PR노이즈("Power Programmer" 시리즈·Carlos Alcaraz)로 갈린다. 채널 필터가 아니라 영상 단위 라벨링이 필수임을 재확인.

---

## 2. 주요 발화자·패널

**한국 AX 담론**: 김건우(『AI 전환 절대공식』 저자)·김유신 상무(티타임즈)·신계영 부사장(삼성SDS AX센터)·장진석(BCG)·윤병동(서울대·원프레딕트)·이세돌×이홍락(LG AI)·Galina Fendvich(Upstage US)·**이상욱 교수(한양대 철학, 탈숙련 담론)·서연석(NAVER Cloud)·"데이브"(AX 실무강의)**

**글로벌**: 젠슨 황·Kevin Deierling(NVIDIA), Will Abbey(Arm), Rainer Brehm·Rev Lebaredian(Siemens/NVIDIA), Alex Kendall(Wayve), Akshay(Palantir 수석아키텍트), Michael Park(ServiceNow), 일론 머스크(Tesla TERAFAB), 페르난도 페르난데스(Unilever CEO), Amjad Masad(Replit CEO), Rana El Kaliouby(MS/Affectiva), 페이(Alibaba DB BU), Boz+게스트 Shyam Sankar(Palantir CTO)·Ed Catmull·Dylan Field, Aaron Levie(Box), Peter Arduini(GE)

**v4 신규**: **Sara Hooker**(Adaption Labs 공동창립·前 Cohere For AI — "스케일링의 느린 죽음→적응"), **Eric Ries**(Lean Startup — 코퍼스 최강 메타비판자), **Amit Bendov**(Gong CEO), **Ryan Meadows**(Lovable CRO), **Guy Yalif**(Webflow CPO), **Wade Foster**(Zapier CEO), **로빈 빈스(BNY CEO, 사내 플랫폼 "Eliza")**, Shopify·Virgin Atlantic·Peter Steinberger(OpenAI France), Home Depot(Ashish·Chuma)·MediaMarkt·PayPal(Mir)·BBVA(Gerardo Monzelli)·Anthropic Lydia(Google 플랫폼 출연). **v4.1**: Sofia Sirvell(Sandvik 그룹 디지털책임자 — "사람 문제" 트로프), Lotta Lovén(Swedbank CIO — 미팅요약 60개 저축은행 확산)

---

## 3. AX·DX·AI 개념 정의 (코퍼스 합의)

| 개념 | 정의 |
|---|---|
| DX | 아날로그→디지털, 프로세스 **자동화**(정해진 패턴) |
| AX | **자율화**(AI가 판단·의사결정·실행). 도구 도입이 아니라 워크플로 재설계 |
| 관계 | "DX가 먼저 돼야 AX 가능"(삼성SDS·SK하이닉스·INSEAD). "AX는 DX보다 돈이 더 든다" |
| 실체 | 2026년 AX의 실체는 사실상 **에이전틱 AI**(오케스트레이션)로 수렴. 벤더 스택은 "모델(두뇌)+하네스(도구/루프)+운영(런타임·메모리·평가)" 3층 정형구로 표준화(AWS Bedrock/Strands/AgentCore, Google Gemini/ADK/Agent Platform) |

⚠️ **용어 이중성**: 한국·기업 담론 = AI Transformation. 해외 UX 계열(Microsoft Developer, Brave Achievers) = **Agent Experience**(에이전트를 사용자로 보는 설계). 분류 라벨에 반드시 구분.

---

## 4. 비용구조 담론의 축 (K1 병합 대비)

1. **레거시 현대화** — TCS TDC Net("수년→몇 달"), Accenture("기술비용 70%가 레거시 유지"), ServiceNow(레거시 우회), SAP("마이그레이션 노력 35~50% 절감", ECC 2027/2030 만료가 강제 동인), **Google(Oracle→BigQuery 복제, PayPal 코딩 50~60%↓)**
2. **전력/인프라** — Nokia("cost per delivered bit", "no GPU premium"), Siemens("물리산업 100조$"), Schneider("AI=전력수요 유발자"), LG("AI 비용의 본질=에너지"), Arm("power is not free"), Tesla TERAFAB(1테라와트), **Google(Ironwood TPU 포드당 9216칩·최대 100만; "비디오 모델은 아직 비싸다" vs "Gemini3 레슨원가 <3센트")**
3. **인건비 대체** — ElevenLabs(4인 ROAS 7.16), Databricks("400명 팀 필요"), Upstage("인건비 80%↓"), Palantir(증강 vs 대체), Alibaba("에이전트=인력"), **OpenAI(Shopify "팀→상담원 하나")**, **AX강의(7명→4명·VOC 직접처리 95%↓·주 16시간 확보)**
4. **토큰/크레딧 원가 거버넌스** — GitHub(Kimi K2.7 과금표: 100만 토큰당 95크레딧 입력/400 출력, 캐시히트 95%, Copilot "비용 센터"·월 $50 한도), **AWS(context_manager=auto로 "토큰 55%↓·정확도 68→98%"; 요약엔 저렴한 모델)**, **Zapier(월 10만 회 실행 토큰비용 모델링, 모델 간 4배 원가차)** — AX가 실제 기업 예산·FinOps로 번역되는 지점
5. **NEW: 도입 실패·변경관리 비용** — Google/Microsoft("망가진 워크플로에 AI 얹으면 실패", "마지막 30%가 어렵다"), Zapier(Lovable "소프트웨어보다 변경관리·배포가 핵심"), AX강의("전직원 ChatGPT 결제+외부강사 3개월 뒤 변화 0 = 정상적 실패, 돈만 더 씀"). AX의 숨은 원가 = 도구비가 아니라 조직 재설계·변경관리

**AX를 직접 P&L/원가로 환산하는 최고 자료**(K1 종속변수 후보): **Unilever 투자자 3편**(CEO가 R&D 혁신주기 2~3년→9~12개월·콘텐츠 크리에이터 1만→30만·"LLM 검색=대형브랜드 해자"를 마진구조와 직결), Upstage 플리토("인식률 10%=검수 시간=비용"), GitHub(크레딧=센트), **AX강의(노하우 장표를 인건비 200만원+로 환산)**, Nokia("cost per delivered bit")

---

## 5. 반-워싱 vs 워싱 진영 (뚜렷한 분화)

**반-워싱(실체/절제)**: TCS·Google Samat("AI라는 단어 안 썼다")·LinkedIn·Nasdaq("MIT 5%만 프로덕션")·Swisscom·Siemens·Upstage·IBM·Boston Dynamics·Zoox("vibe driving은 안전 시스템에 부적합")·GitHub·McKinsey·**Google Cloud Tech("코드생성만 과의존=버그·기술부채↑", "Claude는 검증 필요", "AI는 교사 대체 못함")·AWS(비결정성·환각 전제로 결정론적 검증층·평가·가드레일 강조, "합격률 66%뿐")·FineWeb(자사 중복제거 실패 공개)·LlamaIndex("최첨단이라 완벽하다는 뜻 아님")**

**🔑 메타-비판(담론 알고리즘 자체를 해부 — 코퍼스 최강)**: **Eric Ries(Zapier)** — "슬롭 팩토리·LLM 정신병·근육 위축(deskilling)·Dunning-Kruger 공장", "챗봇으로 직원 대체하는 CEO 한심, 비용절감엔 책임 안 물음", "에이전트 20명이 4천만 줄 코드 자랑—고객 서사는 부재". + **이상욱 교수** — 탈숙련("AI에 지시할 5·10년차 숙련자가 사라진다", "할루시네이션=버그 아닌 아키텍처적 특징"). 이 둘이 검증자의 법칙(Nasdaq·Boston Dynamics 계열)의 정점.

**워싱(배수·신조어·무자막·비전)**: Accenture("10배 은행")·SK AX(사례 제로)·Databricks("세계 최초 에이전틱 CDP")·ServiceNow(규모 과시)·Runway(유명인 권위)·Nissan/Volvo/BMW/**Mercedes(서사적 침묵)**·Tesla TERAFAB(카르다셰프·우주 AI)·AppsTek("79% 실패·3배 성공률" 출처 없는 리드젠)·SAP "Autonomous Enterprise"·**OpenAI 간증 4편(실명 대기업 CEO를 카메라에 세워 "실험 아닌 프로덕션" 신호 — 단 정량수치는 없음, "권위 있는 실명+수치 부재"의 전형)·AX강의(안티워싱 톤으로 신뢰 확보 후 유료 소모임 전환)**

---

## 6. 대표 수치·사례 하이라이트

| 사례 | 수치 | 출처 |
|---|---|---|
| JP모건 | 32만 중 20만 LLM 사용 | 김건우 |
| 우리은행 | "AX 회사" 선언, 에이전트 175→300개 | 삼성SDS 신계영 |
| 삼성전자 | 에이전트 1만+, 시장조사 에이전트 연 100억 조사비 대체 | 〃 |
| NVIDIA 내부 | 월 4조 토큰, 일 2억 추론, 수요 월 40%↑ | AI Factory Insider |
| LG AI | EXAONE 누적 510만 다운로드, 제조 비전검사 연 $54M 절감 | Talk Concert |
| Wayve | 4~6개월 만에 새 나라·새 차량 일반화, $1.5B 시리즈D | AI-500 로드쇼 |
| Upstage/플리토 | 저해상도 인식률 타사 대비 10%차=검수비용 | 문서처리 AI |
| ElevenLabs | 4인·신규채용0·7개국·ROAS 7.16·$3.78M | AI Ad Tool |
| SAP | 마이그레이션 노력 35~50% 절감 | Agent-led |
| Alibaba | 문제해결 정확도 92%(전문가 85%)·30초 | ClawTalks EP6 |
| Unilever | R&D 혁신주기 2~3년→9~12개월, 크리에이터 1만→30만 | 투자자 컨퍼런스 |
| GitHub | Kimi K2.7 100만 토큰당 95크레딧(입력)/400(출력), 캐시히트 95% | Kimi K2.7 |
| **Home Depot** | 장애대응 **20분→2분** | Google Cloud Tech |
| **Google 에이전트** | 응답속도 **80%↑**(1:36→16~23초), PayPal 코딩 **50~60%↓** | 〃 |
| **MediaMarkt** | 온보딩 수주→수시간, Gemini CLI로 스킬 **130개**("shift down") | 〃 |
| **BBVA** | GCP 프로젝트 **1,000+**, 고객 8,100만, 25개국 | 〃 |
| **Gemini 3 레슨원가** | 레슨 1개 전체 **3센트 미만** | Agent Factory |
| **Webflow** | 셀프서비스 가입 중 LLM 유입 **8%**, 전환율 SEO의 **6배**, 검색어 **23단어**(구글 4) | Zapier(Guy Yalif) |
| **Gong/B2B 영업** | 판매자 1천만·시장 6조$·시간 **75% 낭비**, 통화대기 5시간→30초로 기회 +60% | Zapier(Amit Bendov) |
| **Lovable** | ARR $400M(2월 한 달 +$100M), <200명, **인당 ≈$3M**, Fortune500 **50%**가 프로토타입에 사용 | Zapier(Ryan Meadows) |
| **AWS 컨텍스트 자동관리** | 토큰 **55%↓**, 정확도 **68→98%** | Context Engineering |
| **AWS 고객서비스 에이전트** | 평균 합격률 **66%**(환불 83·주문추적 0.5·계정 0) | Evaluating Agents |
| **FineWeb** | **15조** 토큰(FineWeb-EDU 1.3조), Common Crawl 96스냅샷 | Hugging Face |
| **AX강의(데이브)** | ROI 2배·월매출 +8%·**7명→4명**·VOC 직접처리 **95%↓**(주 16시간)·노하우 인건비환산 200만원+ | 데이브의 개발 생활 |
| Klarna | AI 퍼스트 → 실패 후 재고용 | 김건우 |

---

## 7. 🔴 데이터 품질 이슈 및 조치 내역

1. **채널 오수집 2건 발견·수정 완료(2026-07-21)** — 동명이인 채널 리스크:
   - **TCS**: `@TCS`(스위스 자동차클럽 Touring Club Schweiz) → `@TCSGlobal`(진짜 Tata Consultancy) 교정. 오수집분 7건 `Touring_Club_Schweiz/`로 격리.
   - **Zoox**: `@zoox`(동명 게임 유튜버) → `@ZooxYouTube`(아마존 로보택시) 교정. 오수집분 2건 격리. **→ 수정 후 진짜 Zoox 로보택시 콘텐츠 정상 수집 확인됨.**
   - → **약어·짧은 이름 채널 재검증 필요**(config.py "추정" 표시 핸들 전반).
2. **노이즈 채널** — Swisscom·Nissan/Volvo/BMW/Mercedes(AI 침묵/광고)·NTT DATA(채용)·LinkedIn·Cohere(학술)·**Hugging Face(연구/OSS — AX 비용 담론 아님)**·Microsoft(Nation PR)·Suno/Luma/Philips: AX 비용 분석에서 별도 분류 권장.
3. **자막 자동번역 오류 체계적 — v4에서 더 심각·구조적임 확인**. 특히 **의미 반전형 오역**:
   - `agents`→**"부동산 중개인"**(Google Architecture편 "향후 2~3년 부동산 중개인들이…"), `agents`→"요원/상담원", `mutating agents`→**"병원체·변이원"**(PayPal편)
   - `agentic harness`→**"억제력/능동적 억제력"**, `Antigravity`→"반중력 장치", `Claude/Claude Code`→**"오픈 클로(Open Claw)/클라우드 코드/인공 클라우드 모델"**, `Anthropic`→"Enthropic"
   - `cache`→**"현금/현금화"**, `staleness`→"스테인리스", `LLM`→**"법학 석사"**, `Gong`→"징", `Strands`→"가닥들", `LeRobot`→"레오봇/르루프"
   - 한국어 AX강의: `ChatGPT`→"채피 결제", `장면`→"장미안", `통으로`→"통어"
   - **결론: 영어 원본 자막은 신뢰도 높으나, 한→영/영→한 자동번역 인용 시 원문 확인 필수. 특히 `agent`류 핵심어가 완전히 다른 의미로 뒤집힘.**
4. **빈/저품질 자막** — "[음악] 우." 뿐인 파일(BD 티저, LG 티저 등), "work→음악" 대규모 오삽입. 단어 수 임계값(예: 50단어) 필터링 권장.
5. **중복 스크립트** — Stability "Change exactly"와 "Quick Guide"는 동일 스크립트. 파일해시·본문 유사도 중복제거 권장.
6. **pre-AX 기준선(t0) 확보** — kakao_tech if(kakao)2021 8편: AI가 담론 중심이 아니던 시점. 시계열 원점.
7. **AX 용어 이중성**(§3) — 분류 라벨 반영.

---

## 8. 연구(AX 담론→비용구조) 최우선 자료

1. **Unilever 투자자 3편** — AX를 P&L(혁신비용·마케팅비용·마진)에 직접 연결한 최고 자료
2. **AX강의 "데이브의 개발 생활"**(2026-07-22) — 의사결정 알고리즘화의 미시적 실연 + 인건비 직접 환산(7→4명, 노하우 200만원+)
3. **GitHub Copilot 과금/비용센터** + **AWS 토큰 원가 모델링** + **Zapier 실행량×원가** — AX→기업 예산·FinOps 원가 거버넌스
4. Upstage 플리토 — AX를 직접 원가로 환산("인식률 10%=비용")
5. 삼성SDS 신계영 — 한국 대기업 KPI 3층·에이전트 거버넌스
6. Accenture Top Banking Trends 2026 — "기술비용 재배분" 교과서
7. Nasdaq "Where the Gaps Exist" + **Eric Ries(Zapier)** + **이상욱 교수** — 담론의 비판적 대조군·메타비판(검증자의 법칙)
8. Nokia AI-native RAN — "cost per delivered bit"
9. Palantir "Future of AI and Work" + **OpenAI 위임(delegation) 담론** — 노동가치 재정의 이론 텍스트(위임↔탈숙련의 동전 양면)
10. **Google Cloud Tech "80% speedup"** — 분모스왑 실시간 포착 사례
11. **Sara Hooker(Hugging Face) "scaling→adaptation"** — 분모스왑의 연구층위 텍스트
12. 맥킨지 State of AI + BCG 장진석 — 도입-성과 괴리 정량 기준선

---

## 9. K1 병합으로 가는 측정변수 (operationalize)

1. **공급/수요 낙관 발산 지수** — 채널 유형 × 월 × AX 톤. 발산 폭 = AI 워싱/버블 대리지표.
2. **정량성 결핍 점수** — [AX 키워드 밀도] ÷ [provenance 있는 수치 등장 빈도].
3. **분모 교체 이벤트 탐지** — "토큰→에이전트", "usage→outcome", "job→skill", **"scaling→adaptation", "데모→벤치마크 통과율"** 재프레이밍 발화 태깅 → 산업×시점별 K1 자본지출/원가구조 변화와 이벤트 스터디.
4. **NEW: 청중-표면 코드(사람 소거 vs 전면화)** — 동일 알고리즘화를 원가/신뢰성 언어로 번역하는가(사람 소거, 개발자 청중) vs 헤드카운트/deskilling으로 번역하는가(사람 전면화, 경영진 청중). 벤더의 청중 유형과 K1 인건비/자본 구조 변화 매칭.

⚠️ **신뢰도 경계**: 위 인사이트는 **횡단면 구조**에 근거해 유효하나, **시계열 주장(발산의 시간적 전개)은 백필이 고르게 찰 때까지 보류**. 현 표본은 채널 131개, 최근 영상 위주라 2020~2024 구간이 얇다. 월별 볼륨 시계열은 "채널 백필 순서" 아티팩트임에 유의(볼륨보다 share·횡단면이 신뢰 가능).
