# 수집 콘텐츠 검토 보고서 (v3, 2026-07-21)

> **771건 전체 코퍼스** 기준 전수 정독 분석. 심층 정독 ~700건(키워드 65 + 채널 63개 대부분), 최신 자동수집 잔여분 일부는 인벤토리 상태.
> 자동분류: **AX 214 / DX 15 / AT 4 / 미분류 538**.
> 다음 회귀분석·코딩 작업 전에 읽을 것. v2(648) 대비 신규 채널 15개(Palantir·ServiceNow·Upstage·Siemens·Wayve·진짜 Zoox·Microsoft·SAP·GitHub·Replit·Cohere·Alibaba·NAVER Cloud·Tesla·BMW·Unilever 등)와 인사이트를 반영.

---

## 0. 핵심 인사이트 — 담론에서 작동하는 "알고리즘"

이 코퍼스에서 단순 채널 인벤토리를 넘는 **구조적으로 반복되는 조작(=담론의 알고리즘)**이 발견된다. 프로젝트 궁극 프레임(의사결정의 알고리즘화)과 직결된다.

### A. "분모 바꾸기(denominator swap)" — 최상위 발견
**기존 지표가 실망스러운 ROI를 보이면, 담론은 실망을 인정하는 대신 '무엇을 셀 것인가'(측정 단위)를 바꾼다. 그리고 그 조작을 하는 주체는 언제나 새 지표에서 이득을 보는 쪽이다.**

| 주체 | 낡았다고 규정한 지표 | 새로 미는 지표 | 이득 |
|---|---|---|---|
| NVIDIA·Arm | 토큰 수 | 동시 에이전트 수 / 와트당·달러당 산출 | 하드웨어 수요 정당화 |
| Apple·Nokia | 개발자 토큰비 / GPU 프리미엄 | "무료"(→PCC·온디바이스·구독으로 이전) / "no GPU premium" | 비용 비가시화 |
| 컨설팅(BCG·Accenture) | 사용량 | 비즈니스 성과 / 학습 속도 | 컨설팅 필요성 |
| Accenture | 직무(job) | 스킬 아키텍처 | 인재 재교육 상품 |
| Salesforce·Deloitte | (자인) 대시보드 실사용률 20~30% | 파이프라인·시간절약 환산액 | 도입 서사 유지 |

→ **지표를 쥔 자가 ROI 서사를 쥔다.** 이것이 의사결정의 알고리즘화의 메타층위: 기업 안에서 AI가 결정하기 이전에, 'AI 가치를 어떻게 계산할지'라는 판단 기준 자체가 이해당사자에 의해 재작성된다.

### B. 그 외 반복 구조
1. **"95% 실패" 개막 의식** — MIT "95% 실패", 맥킨지 "88% 도입 vs 39% 수익화", "AI 프로젝트 80% 실패" 3~4개 숫자가 한/영·컨설턴트·학계 불문 반복. 문법: [파국적 실패율 인용]→["기술이 아니라 사람·프로세스·데이터 탓"]→[내 프레임만 예외]. = **책임 전가 알고리즘**.
2. **"AI는 기술 문제가 아니라 사람 문제"** — 범용 명제로 확정(Upstage·Palantir·김건우·BCG·McKinsey). 책임전가 문법의 핵심.
3. **공급/수요 담론의 분열** — 공급측("OpenClaw 모멘트, 추론 15배 폭발")과 수요측("95%가 성과 없음")이 양립 불가. 이 간극이 버블 질문의 실체이자 검증가능한 특이점.
4. **온톨로지/컨텍스트 계층 = 새 격전지** — Palantir(온톨로지)·ServiceNow(context graph)·Databricks(Unity Catalog)·Pinecone/Weaviate(벡터)·Cognee(그래프 메모리) 모두 "데이터+거버넌스 계층을 쥔 자가 에이전트 시대 지배"라 주장. AX의 진짜 락인은 모델이 아니라 컨텍스트/거버넌스 계층.
5. **정량성의 역설** — AI를 전면에 내세운 채널일수록 검증가능 정량 성과가 부재. 가장 단단한 숫자는 AX가 아니라 인접 상품(칩·영상장비)을 파는 채널에서 나옴.
6. **배수(multiple) 수사학** — 컨설턴트는 분모 없는 배수("4.4배", "16.5배", "10배 은행")로 말함. 반증 불가하면서 인상적.
7. **"에이전트=인력(AI Workforce)" 프레임의 국제적 수렴** — Alibaba("디지털 실리콘 전문가팀"), SK AX("AI workforce"), TCS, ServiceNow("L1 대체"). 노동을 '인력 단위'로 세는 담론이 미·중·한 공통.
8. **자동차 산업 AI 태도 삼분화** — 침묵(Nissan·Volvo) → 완곡 내재화(BMW: ADAS를 "AI"로 안 팜) → 정체성화(Tesla: AI/에너지/로봇 기업으로 자기재정의). 같은 산업 안에서도 갈림 → 분석 단위는 '산업'이 아니라 '기업 전략'.
9. **소버린 AI의 하이브리드 실용주의** — NAVER·LG: 자국 모델(HyperCLOVA/EXAONE)+데이터주권(뉴로클라우드)을 내세우면서도 미국 Claude를 제어 UI로 병용. "소버린 vs 종속" 이분법이 아니라 계층별 선택(모델은 자국, 인터페이스/에이전트는 최선).

---

## 1. 코퍼스 지도 — AI/AX 담론 밀도 순

| 밀도 | 채널 | 성격 |
|---|---|---|
| ★★★ | NVIDIA·NVIDIA Developer, Arm, Siemens, Nokia, Wayve, Zoox, Tesla | "AI 팩토리"·"물리적 AI"·에이전트·자율주행. 수치·비용구조 언어 풍부 |
| ★★★ | LG AI Research, Upstage, Palantir, ServiceNow, SAP, IBM, Salesforce, Databricks, Alibaba Cloud, W&B·Qdrant·Pinecone·Weaviate·Snowflake | AI가 곧 제품. 도입방법론·평가·거버넌스·온톨로지 |
| ★★☆ | Meta(Boz), Boston Dynamics, Microsoft Azure, Google Developers·DeepMind, Meta Developers, SK하이닉스, GE HealthCare, Accenture, TCS, ElevenLabs, Runway, Apple Developer, GitHub, Replit, NAVER Cloud, Unilever(IR) | AX를 자사 제품/비전·투자자 서사에 접합 |
| ★☆☆ | SK텔레콤, Telenor, Amazon, Waymo, Mayo Clinic, LinkedIn, Schneider, Microsoft(Nation PR) | AI가 마케팅 소재(보안·안전·감성·노동시장·정당성) |
| ☆ | Swisscom, Reckitt, Nissan, Volvo, BMW, NTT DATA, Suno, Luma, Philips, Perplexity, Cohere(학술), kakao_tech(2021) | AI 담론 희박 — 그 자체가 신호(자동차 침묵, 학술, pre-AX 기준선 등) |

키워드 수집분(65건, `transcripts/2026-*/`)은 한국어 AX 강의·컨설팅·정책·언론 콘텐츠가 주력이며 연구 주제에 최고 밀도.

⚠️ **"채널명 ≠ 담론 성격"**: Cohere(엔터프라이즈 아닌 학술)·Microsoft(대부분 브랜드 PR)·BMW(광고)·Zoox/TCS(오수집) — 채널명으로 성격을 예단하면 안 됨. 코퍼스 분류는 채널이 아니라 **영상 단위**로 해야 함.

---

## 2. 주요 발화자·패널

**한국 AX 담론**: 김건우(『AI 전환 절대공식』 저자)·김유신 상무(티타임즈)·신계영 부사장(삼성SDS AX센터)·장진석(BCG)·윤병동(서울대·원프레딕트)·이세돌×이홍락(LG AI)·Galina Fendvich(Upstage US)

**글로벌**: 젠슨 황·Kevin Deierling(NVIDIA), Will Abbey(Arm), Rainer Brehm·Rev Lebaredian(Siemens/NVIDIA), Alex Kendall(Wayve), Akshay(Palantir 수석아키텍트), Michael Park(ServiceNow), 일론 머스크(Tesla TERAFAB), 페르난도 페르난데스(Unilever CEO), Amjad Masad(Replit CEO), Rana El Kaliouby(MS/Affectiva), 페이(Alibaba DB BU), 서연석(NAVER Cloud), Boz+게스트 Shyam Sankar(Palantir CTO)·Ed Catmull(픽사)·Dylan Field(Figma), Aaron Levie(Box), Ron Howard·Roger Avary(Runway), Peter Arduini(GE), Dave Fredrickson(아스트라제네카), Michael Abbott(Accenture 뱅킹)

---

## 3. AX·DX·AI 개념 정의 (코퍼스 합의)

| 개념 | 정의 |
|---|---|
| DX | 아날로그→디지털, 프로세스 **자동화**(정해진 패턴) |
| AX | **자율화**(AI가 판단·의사결정·실행). 도구 도입이 아니라 워크플로 재설계 |
| 관계 | "DX가 먼저 돼야 AX 가능"(삼성SDS·SK하이닉스·INSEAD). "AX는 DX보다 돈이 더 든다" |
| 실체 | 2026년 AX의 실체는 사실상 **에이전틱 AI**(오케스트레이션)로 수렴 |

⚠️ **용어 이중성**: 한국·기업 담론 = AI Transformation. 해외 UX 계열(Microsoft Developer, Brave Achievers) = **Agent Experience**(에이전트를 사용자로 보는 설계). 분류 라벨에 반드시 구분.

---

## 4. 비용구조 담론의 3대 축 (K1 병합 대비)

1. **레거시 현대화** — TCS TDC Net("수년→몇 달"), Accenture("기술비용 70%가 레거시 유지, 매출의 200~300% 속도로 증가"), ServiceNow(레거시 우회), **SAP("마이그레이션 노력 35~50% 절감", ECC 2027/2030 만료가 강제 동인)**
2. **전력/인프라** — Nokia("cost per delivered bit", "no GPU premium"), Siemens("물리산업 100조$"), Schneider("AI=전력수요 유발자"), LG("AI 비용의 본질=에너지"), Arm("power is not free"), **Tesla TERAFAB(1테라와트·우주 AI 연산 — 극한 스케일)**
3. **인건비 대체** — ElevenLabs(4인 7개국 ROAS 7.16), Databricks("400명 팀 필요"), Upstage("인건비 80%↓"), Nasdaq("right-sizing"), Palantir(증강 vs 대체), **Alibaba("에이전트=인력")**
4. **토큰/크레딧 원가 거버넌스(신규 축)** — **GitHub(Kimi K2.7 과금표: 100만 토큰당 95크레딧 입력/400 출력, 캐시히트율 95%, Copilot "비용 센터"·사용자당 월 $50 한도)** — AX가 실제 기업 예산·FinOps로 번역되는 지점을 가장 노골적으로 노출

**AX를 직접 P&L/원가로 환산하는 최고 자료**(K1 종속변수 후보): **Unilever 투자자 3편(CEO가 R&D 혁신주기 2~3년→9~12개월·콘텐츠 크리에이터 1만→30만·"LLM 검색=대형브랜드 해자"를 마진구조와 직결)**, Upstage 플리토("인식률 10%=검수 시간=비용"), GitHub(크레딧=센트), Nokia("cost per delivered bit"), Alibaba ClawTalks("에이전트 운영비 92% 정확도·30초")

---

## 5. 반-워싱 vs 워싱 진영 (뚜렷한 분화)

**반-워싱(실체/절제)**: TCS("GenAI가 다 해주진 않는다")·Google Samat("AI라는 단어 안 썼다")·LinkedIn("채용둔화는 금리 탓")·Nasdaq("MIT 5%만 프로덕션")·Swisscom("AI는 관리할 위험")·Siemens("80% 같은 건 말 안 한다")·Upstage(할루시네이션 억제 데모)·IBM(AI 5대 신화 반박)·Boston Dynamics("남들은 안 넘어지는 영상만 보여준다")·**Zoox(end-to-end 명시적 거부: "vibe driving은 안전 시스템에 부적합")·GitHub("속도는 신뢰할 때만 의미, 자동병합 없음")·McKinsey("80% 투자 vs 80%+ 미수익 역설")**

**워싱(배수·신조어·무자막·비전)**: Accenture("10배 은행")·SK AX(사례 제로)·Databricks("세계 최초 에이전틱 CDP")·ServiceNow(규모 과시 통계)·Runway(유명인 권위)·Nissan/Volvo/BMW(AI 침묵/완곡 속 "intelligence"/"superbrain" 수사)·**Tesla TERAFAB(카르다셰프·우주 AI — 검증불가 비전)·AppsTek("79% 실패·3배 성공률·90일 ROI" 출처 없는 리드젠)·SAP "Autonomous Enterprise"(브랜드 시)**

---

## 6. 대표 수치·사례 하이라이트

| 사례 | 수치 | 출처 |
|---|---|---|
| JP모건 | 32만 중 20만 LLM 사용 | 김건우 |
| 우리은행 | "AX 회사" 선언, 에이전트 175→300개 | 삼성SDS 신계영 |
| 삼성전자 | 에이전트 1만+, 시장조사 에이전트 연 100억 조사비 대체 | 〃 |
| NVIDIA 내부 | 월 4조 토큰, 일 2억 추론, 수요 월 40%↑ | AI Factory Insider |
| LG AI | EXAONE 누적 510만 다운로드, 제조 비전검사 연 $54M 절감 | Talk Concert |
| Siemens/Pringles | 라인당 생산량 2~10%↑·에너지 7%↓ | AI Process Control |
| Siemens(중남미) | 제조 AI 도입률 18%, 산업 SME는 5%(SME=기업 99%) | Why Latin America |
| Wayve | 4~6개월 만에 새 나라·새 차량 일반화, $1.5B 시리즈D | AI-500 로드쇼 |
| Upstage/플리토 | 저해상도 인식률 타사 대비 10%차=검수비용 | 문서처리 AI |
| ElevenLabs | 4인·신규채용0·7개국·ROAS 7.16·$3.78M | AI Ad Tool |
| Databricks | 보안 알림 주당 7천(2020)→3만+, 감당하려면 400명 팀 | LakeWatch |
| SAP | 마이그레이션 노력 35~50% 절감, 테스트케이스 30~60분→몇 분 | Agent-led |
| Alibaba | 문제해결 정확도 92%(전문가 85%)·30초, "2027년 DB 인스턴스 50%가 에이전트 사용" | ClawTalks EP6 |
| Unilever | R&D 혁신주기 2~3년→9~12개월, 콘텐츠 크리에이터 1만→30만 | 투자자 컨퍼런스 |
| GitHub | Kimi K2.7 100만 토큰당 95크레딧(입력)/400(출력), 캐시히트 95% | Kimi K2.7 |
| Klarna | AI 퍼스트 → 실패 후 재고용 | 김건우 |
| 에어캐나다 | 챗봇 오안내 배상 판례(2024) | 〃 |

---

## 7. 🔴 데이터 품질 이슈 및 조치 내역

1. **채널 오수집 2건 발견·수정 완료(2026-07-21)** — 동명이인 채널 리스크:
   - **TCS**: `@TCS`(스위스 자동차클럽 Touring Club Schweiz) → `@TCSGlobal`(진짜 Tata Consultancy) 교정. 오수집분 7건 `Touring_Club_Schweiz/`로 격리.
   - **Zoox**: `@zoox`(동명 게임 유튜버, "Until Dawn" 공략) → `@ZooxYouTube`(아마존 로보택시) 교정. 오수집분 2건 `_misfetched_Zoox_gaming/`으로 격리. **→ 수정 후 진짜 Zoox 로보택시 콘텐츠 정상 수집 확인됨.**
   - → **약어·짧은 이름 채널 재검증 필요**(config.py "추정" 표시 핸들 전반). 각 교정 후 다음 회차부터 진짜 채널 수집됨.
2. **노이즈 채널** — Swisscom 축구광고, Nissan/Volvo/BMW(AI 침묵/광고), NTT DATA(채용), LinkedIn GYB 카피광고, Cohere(학술), Microsoft(Nation PR), Suno/Luma/Philips: AX 분석에서 별도 분류 권장.
3. **자막 자동번역 오류 체계적** — "AI/humanities→music(음악)", "Pinecone→솔방울", "OpenTelemetry→호텔", "robotaxi→로봇 세금 징수", "Hadean→하디안" 등. **인용 전 원문 확인 필수**.
4. **빈/저품질 자막** — "[음악] 우." 뿐인 파일(BD 티저, LG 티저 5편 등). 단어 수 임계값(예: 50단어) 필터링 권장.
5. **AX 용어 이중성**(§3) — 분류 라벨 반영.
6. **pre-AX 기준선(t0) 확보** — kakao_tech if(kakao)2021 8편: AI가 담론 중심이 아니던 시점(플랫폼·구독·NFT). 시계열 원점.

---

## 8. 연구(AX 담론→비용구조) 최우선 자료

1. NVIDIA COMPUTEX 기조 — "비용센터→토큰 수익원"
2. Meta Boz×Shyam Sankar — "소프트웨어가 싸지면 프로세스가 비싸진다"
3. Siemens "Analytic to Autonomous" — 규칙기반 ROI 한계→목표기반
4. Upstage 플리토 — AX를 직접 원가로 환산("인식률 10%=비용")
5. 삼성SDS 신계영 — 한국 대기업 KPI 3층·에이전트 거버넌스
6. Accenture Top Banking Trends 2026 — "기술비용 재배분" 교과서
7. Nasdaq "Where the Gaps Exist" — 담론의 비판적 대조군(검증자의 법칙)
8. Nokia AI-native RAN — "cost per delivered bit", "no GPU premium"
9. Palantir "Future of AI and Work" — 노동가치 재정의 이론 텍스트
10. **Unilever 투자자 3편** — AX를 P&L(혁신비용·마케팅비용·마진)에 직접 연결한 최고 자료
11. **GitHub Copilot 과금/비용센터** — AX→기업 예산·FinOps 원가 거버넌스
12. 맥킨지 State of AI + BCG 장진석 — 도입-성과 괴리 정량 기준선

---

## 9. K1 병합으로 가는 측정변수 3개 (operationalize)

1. **공급/수요 낙관 발산 지수** — 채널 유형 × 월 × AX 톤. 발산 폭 = AI 워싱/버블 대리지표.
2. **정량성 결핍 점수** — [AX 키워드 밀도] ÷ [provenance 있는 수치 등장 빈도].
3. **분모 교체 이벤트 탐지** — "토큰→에이전트", "usage→outcome", "job→skill" 재프레이밍 발화 태깅 → 산업×시점별 K1 자본지출/원가구조 변화와 이벤트 스터디.

⚠️ **신뢰도 경계**: 위 인사이트는 **횡단면 구조**에 근거해 유효하나, **시계열 주장(발산의 시간적 전개)은 백필이 고르게 찰 때까지 보류**. 현 표본은 채널 118개 중 ~63개, 최근 영상 위주라 2020~2024 구간이 얇다. 월별 볼륨 시계열은 "채널 백필 순서" 아티팩트임에 유의(볼륨보다 share·횡단면이 신뢰 가능).
