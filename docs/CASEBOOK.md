# AX Transformation 사례집 (CASEBOOK)

> 코퍼스 **8,155건**(공식 채널 90 + 키워드) 중 실질 AX 담론(ax_core 2,338건)을 가진 회사군을 **13개 클러스터 사례집**으로 정리.
> 각 권 구성: **①핵심 기술 스택 → ②파트너·고객사별 AI 전환 사례(AX/DX 판정 포함) → ③핵심 인사이트** — 각 클러스터 담당 에이전트가 원문 트랜스크립트를 클러스터당 8~20편 정독해 작성(총 ~200편), 수치는 발화 그대로·출처 영상 병기.
> ⚠️ **읽기 전 필수**: 모든 수치·주장은 **발표자(대부분 자사) 발화 기준**이며 독립 검증이 아니다. 자막 자동번역 훼손(도메인명사→"음악", 제품명 오기)이 상존하므로 인용 전 원 영상 확인. 워싱 위험은 각 권 신뢰경계에 표기.

---

## AX / DX 판정 기준 (코퍼스 합의 정의)

| 판정 | 기준 | 시금석 질문 |
|---|---|---|
| **DX** | 아날로그→디지털, **정해진 패턴의 자동화**. 규칙은 사람이 확정, 시스템은 실행만 | "규칙을 사람이 다 정해놓았는가?" |
| **AX** | **자율화** — AI가 판단·의사결정·실행. 도구 도입이 아니라 워크플로 재설계 | "AI가 스스로 판단/분기하는가? 사람 역할이 재정의됐는가?" |
| **DX→AX** | DX 기반 위에 자율 판단을 얹는 이행 | "DX 먼저, 그 위에 AX" 경로가 실제로 보이는가? |
| **DX(AX 표방)** | 실질은 규칙 자동화인데 "AI 에이전트"로 마케팅(워싱 의심) | 결정론 플레이북에 AI 라벨만 달았는가? |

코퍼스 합의 명제: **"DX가 먼저 돼야 AX 가능"**(삼성SDS·SK하이닉스·INSEAD), **"AX는 DX보다 돈이 더 든다"**. 2026년 AX의 실체는 사실상 **에이전틱 AI**(모델+하네스+운영)로 수렴.

---

## 목차

1. NVIDIA · AI 인프라(칩·전력) — AI Transformation 사례집
2. AWS · 에이전트 플랫폼(Bedrock·Strands·AgentCore) — AI Transformation 사례집
3. Google · Gemini/ADK/A2A 생태계 — AI Transformation 사례집
4. Microsoft · GitHub(코파일럿과 원가 거버넌스) — AI Transformation 사례집
5. OpenAI · Anthropic(파운데이션 모델의 위임 담론) — AI Transformation 사례집
6. Palantir · ServiceNow · Oracle(데이터·거버넌스 계층) — AI Transformation 사례집
7. Databricks · Snowflake · 벡터DB · W&B(데이터/ML 인프라) — AI Transformation 사례집
8. SAP · Salesforce · IT서비스 · 컨설팅(엔터프라이즈 앱) — AI Transformation 사례집
9. 한국 AX(삼성SDS·SK·LG·NAVER·Upstage·무신사) — AI Transformation 사례집
10. 중국·아시아(Huawei·Alibaba·소버린 국가전략) — AI Transformation 사례집
11. 자율주행·물리 AI(Tesla·현대차·Zoox·Wayve·Waymo·로보틱스) — AI Transformation 사례집
12. 통신·주권·국가 클러스터 (Orange·Telefónica·Nokia·Telenor·Swisscom·Scale AI) — AI Transformation 사례집
13. 생성 미디어 · 개발도구 · 수요기업 클러스터 — AI Transformation 사례집

---

## 마스터 색인 — 전 사례 AX/DX 분류

13권 전체에서 추출한 **135개 사례**의 판정 분포: **AX** 41 · **DX→AX** 40 · **DX** 37 · **DX(AX 표방)** 17 († = 판정 근거 약함)


### AX — 41건

| 사례 | 클러스터 | 판정 근거 | 대표 수치 |
|---|---|---|---|
| ServiceNow L1 티켓 자율 해결 | NVIDIA · AI 인프라 | 에이전트가 접수→해결 전 과정 자율 수행 | 티켓 90% 자율 해결 |
| Cadence 칩 검증 슈퍼 에이전트 | NVIDIA · AI 인프라 | 서브에이전트 분업·시뮬레이션 자율 실행 | 형식검증 1개월→10시간 |
| CrowdStrike SOC 트리아지 | NVIDIA · AI 인프라 | AI가 오탐 판단·분기, 분석가 역할 재정의(수치 미제시 †) | — |
| Palantir FDE 코드 작성 | NVIDIA · AI 인프라 | 에이전트가 최적화 코드 자율 작성(정성적 †) | — |
| AWS Q Developer 모델 주도 전환 | AWS 에이전트 플랫폼 | 수작업 오케스트레이션 폐기, 모델이 계획·분기 | 투입 수개월→수주 |
| OpenAI 모델 AgentCore 물류 에이전트 데모 | AWS 에이전트 플랫폼 | 에이전트 자율 판단·실행 구조, 단 데모 실증† | — |
| AT&T 판매 에이전트 | Google 생태계 | 오케스트레이터가 스킬 기준 판단·분기, 판매원 역할 대체 | Day7 타채널 원클릭 구매 |
| PayPal 자율 SRE 에이전트 | Google 생태계 | 감지·분류·완화 자율 수행, 단계적 권한 확대 | 코딩 시간 50~60% 단축 |
| (자사) Google 플랫폼 지표 | Google 생태계 | 전환 사례 아닌 AX 인프라 규모 지표(†) | 월 480조 토큰 |
| EY Frontier Firm 컨설팅 전환 | Microsoft · GitHub | 빌러블 아워 해체·역할 재정의(선언 중심 †) | AI 준비 투자 10억 달러+ |
| Home Assistant 버그 트리아지 자동화 | Microsoft · GitHub | AI가 판별·분기 후 수정 PR 자율 생성 | — |
| Shopify — 트리아지 에이전트 재설계 | OpenAI · Anthropic | 워크플로 재설계·에이전트 위임 명시† | 대규모 팀→에이전트 하나 |
| Verso — Codex 중심 회사 구축 | OpenAI · Anthropic | /goal 위임 예시, 언급뿐 검증 불가† | — |
| AIG — 언더라이팅 재구상 | OpenAI · Anthropic | 심사 판단을 AI가 수행·재설계 | 정확도 75%→90%, 주→일 |
| HG Capital — 포트폴리오 전환 이식 | OpenAI · Anthropic | 에이전틱 엔지니어·인력 구조 재정의 | 1,000 인스턴스, 스쿼드 9→2 |
| DocuSign·Honeywell ITSM 전문가 | Palantir · ServiceNow · Oracle | 역할 단위 자율 해결 주장, 자사 발화† | — |
| Oracle 북미 영업 에이전틱 앱 | Palantir · ServiceNow · Oracle | signal→context→action 자율 실행 | 400명→1만 명 확대 |
| Mem0 메모리 계층 | Databricks · 벡터DB · W&B | 자율 기억 추출·갱신·망각 루프(†) | 사용자 100만 |
| Salesforce × Indeed 서비스 에이전트 | SAP · Salesforce · 컨설팅 | 에이전트 티켓 자율 해결·역할 재정의 | 해결률 4%→25%, CSAT 1.8→4.0 |
| Salesforce × LIV Golf 팬 에이전트 | SAP · Salesforce · 컨설팅 | 자율 응대, 결정론 선실행 비중 큼(†) | 지연 -60%, 정확도 94% |
| Salesforce × Falabella·JPW | SAP · Salesforce · 컨설팅 | 자가응답 자율 해결, 구조 미공개(†) | 자가응답 60%, 해결 +40% |
| 삼성전자 콜센터·시장조사 에이전트 | 한국 AX | 인터뷰어·응답자 모두 에이전트, 역할 대체 | 실제 인터뷰와 80~95% 일치 |
| LG 계열 제조·R&D(스케줄링) | 한국 AX | 100% AI 스케줄 공장, AI가 운영 의사결정 | 연 $54M 절감·한계이익 4%↑ |
| 무신사×OpenAI AI 네이티브 전환 | 한국 AX | 에이전트 개발 수행+채용·평가 재정의 | SaaS 구독비 약 4.5억 절감 |
| 톈진항 스마트항만 PortGPT | 중국·아시아 | 이상탐지→근본원인→해법 추천, L4 자율운행 | IGV 92대 3년+ 자율운행 |
| 중국 자동차사 에이전트 하네스 | 중국·아시아 | 에이전트 운영이나 자율성 상세 미공개(†) | 400+ 인스턴스 |
| SoftBank×OpenAI 사이버 자기실험 | 중국·아시아 | 에이전트가 발굴→재현·검증→패치→회귀테스트 | 취약점 10,500건 |
| 미쓰이스미토모카드 X-Ghost 콜센터 | 중국·아시아 | 본질 이해·고위험 인간 이관 분기, 70%는 구상(†) | 업무 약 70% AI 구상 |
| 현대차 × DeepMind 휴머노이드 두뇌 | 자율주행·물리 AI | 학습형 로봇 자율 작업 지향(미실현†) | 2028년 연 3만 대 로봇 생산 |
| Nissan × Wayve 양산 ADAS | 자율주행·물리 AI | E2E 모델이 주행 판단, 무개입 시연 | 신규 국가·차량 적응 4개월 |
| Wayve × Ford/Qualcomm 플랫폼 | 자율주행·물리 AI | 맵·규칙 없이 신경망이 주행 결정 | 런던 60~75분 무개입 주행 |
| Zoox × Amazon/AWS 컴퓨트·자본 | 자율주행·물리 AI | 무인 로보택시 운행+모델이 검증 대체 | 로보택시 100대+ 운행 |
| Boston Dynamics 제조 고객 | 자율주행·물리 AI | 학습 로봇 자율 작업 지향, 미해결 자인† | 목표 신뢰도 99.7% 미달성 |
| H Company×Orange 컴퓨터유즈 에이전트 | 통신·주권·국가 | 에이전트가 화면 보고 자율 조작, 간호사 역할 재정의 | 응급실 대기시간 단축(비재무 ROI) |
| Dataiku×Orange 에이전틱 데이터 플랫폼 | 통신·주권·국가 | 에이전트가 조달·법무 워크플로 자체 재설계 | 수 주→수 시간 |
| ElevenLabs·Hasbro 광고 국제화 | 생성미디어·도구·수요기업 | 번역·더빙·송출 일체를 AI가 수행, 4인 팀으로 워크플로 재설계 | ROAS 7.16·$3.78M |
| Deutsche Telekom 음성 CX | 생성미디어·도구·수요기업 | 에이전트가 L1 자율 해결, 인간은 QC·저니 설계로 재정의 | 연 8,000억 통화(분) |
| BCG·Naturgy·Konecta 에이전트 | 생성미디어·도구·수요기업 | 에이전트 자율 통화 처리+사업부 재편(사람 역할 재정의) | 통화 35만 건+ |
| FaZe Apex×Replit 창업 | 생성미디어·도구·수요기업 | 에이전트가 빌드·자가테스트·디버깅 자율 수행 | 100k ARR |
| Replit 내부 자가검증 | 생성미디어·도구·수요기업 | 자율 판단(자가검증)의 실재와 분포 이탈 실패까지 실증 | — |
| IQVIA Vigilance | 생성미디어·도구·수요기업 | 신뢰도 점수로 자동/수동 분기, 인간은 예외 큐만 | 임상개발 116→52개월 |

### DX→AX — 40건

| 사례 | 클러스터 | 판정 근거 | 대표 수치 |
|---|---|---|---|
| Mercedes 등 Alpamayo AV | NVIDIA · AI 인프라 | L2+ 보조에서 추론형 L4 자율 판단으로 이행 | 2028년 말 L4 목표 |
| NVIDIA 자체 도그푸딩 | NVIDIA · AI 인프라 | ChipNeMo 코파일럿 기반 위 자율 워크스페이스 확장 | 월 4조 토큰 |
| Leidos 전사 생성형 AI 전략(CAIO) | AWS 에이전트 플랫폼 | 클라우드/IaC DX 기반 위 AI 보조, 자율성 약함† | 프로덕션 승인율 27% |
| Orca Security 보안경고 복구 지침 생성 | AWS 에이전트 플랫폼 | AI가 복구안 판단·생성하나 실행은 사람 원클릭† | 정량 수치 미공개 |
| Home Depot AIOps 인시던트 대응 | Google 생태계 | 텔레메트리 통합(DX)+AI RCA, 전 과정 인간 검증 | 20분 이상→약 2분 |
| MediaMarktSaturn 스킬 플랫폼 | Google 생태계 | 스킬 전산화(DX)+Cloud Assist 자율 조사(†) | 온보딩 수주→수시간 |
| Carrefour BigQuery 데이터 에이전트 | Google 생태계 | 정형 파이프라인 위 에이전트 분석, 배포 전(†) | 결제→수초 내 알림 |
| Moonshot Kimi K2.7 Copilot 편입 | Microsoft · GitHub | 공급은 DX, 자율 구현 시연은 AX 요소 † | 캐시 히트율 95% 주장 |
| Anthropic 모델·Auto 라우팅 | Microsoft · GitHub | AI가 복잡도 판단해 모델 분기(캐시 제약) | API 입력 $10/출력 $50 |
| Wolters Kluwer 세무 워크로드 | Microsoft · GitHub | AKS 자동확장(DX)+무개입 신고서 작성(AX) | — |
| Virgin Atlantic — 대시보드 자체 구축 | OpenAI · Anthropic | 비개발자 역할 재정의, 산출물은 DX† | 몇 주→몇 시간 |
| 무신사 — SaaS 내재화·채용 전환 | OpenAI · Anthropic | SaaS 내재화(DX)+역할·채용 재정의 | 연 4.5억 SaaS→3명·2개월 내재화 |
| NBIM — Snowflake·MCP 통합 | OpenAI · Anthropic | 데이터 파이프라인 위 AI 판단 접속 | 생산성 20%↑=연 213,000시간 |
| Bridgewater — 애널리스트 어시스턴트 | OpenAI · Anthropic | 보조 수준, 자율 실행 근거 없음† | — |
| DE Shaw/NYL — 전사 배포 | OpenAI · Anthropic | 보급 단계, 자율화 실체 미확인† | — |
| AbbVie — Gaia·Genesis 문서화 | OpenAI · Anthropic | 정형 문서 자동화+AI 생성 요소† | 문서 시간 40~60% 절감 |
| Deloitte 등 — COBOL·에이전트 배포 | OpenAI · Anthropic | 마이그레이션(DX)을 에이전트 수행† | — |
| Motorola CPQ·에이전틱 제안서 | Palantir · ServiceNow · Oracle | CPQ 정렬(DX) 위 견적·RFP 자동 생성 | RFP 응답 약 50% 단축 |
| Whitespace 국방 의사결정 AI | Palantir · ServiceNow · Oracle | 표적 웹 참여하나 데모 단계† | 데모 약 6주 구축 |
| Adobe·Atlassian·NAB LakeWatch 이전 | Databricks · 벡터DB · W&B | SIEM 이전 위 에이전트 자율 조사 | 페타바이트급 분석 |
| Thrivent·HSBC 차선책 추천 | Databricks · 벡터DB · W&B | AI 판단·사람 실행, 재설계 약함(†) | 신규 예금 +10% |
| TripAdvisor·Dust 등 Qdrant | Databricks · 벡터DB · W&B | 플래너·에이전트, 자율성 미공개(†) | 레스토랑 5만 곳 |
| SAP × Fonterra S4전환+AI앱 | SAP · Salesforce · 컨설팅 | ERP 전환 위 추천·비정형 판단 앱 | 2개 공장 가동→22개 확대 |
| SAP × ZF 데이터+품질 에이전트 | SAP · Salesforce · 컨설팅 | BW 이관 위 4-에이전트 근본원인 판단 | 160개 공장·29개국 |
| SAP × 제로 고객 Agent-led 전환 | SAP · Salesforce · 컨설팅 | 신뢰도 분기 설계, 단 착수 전(†) | 노력 35~50% 절감 목표 |
| TCS × TDC NET 레거시 현대화 | SAP · Salesforce · 컨설팅 | AI 로직 해석, 규칙은 인간 템플릿(†) | 수년→몇 달 |
| Infosys × Sandvik 보증처리 AI | SAP · Salesforce · 컨설팅 | 프로세스 재구상 지향, POC 단계(†) | 대부분 POC |
| 우리은행×SDS 전행 175개 에이전트 | 한국 AX | 에이전트 전면 설계이나 구축 전, 자율성 미실증† | 에이전트 175개 설계(최소 300개+ 진단) |
| 국민연금·LSEG×LG Master Score | 한국 AX | AI가 신호 판단 생성, 실행은 사람† | 전문가 선호도 25%↑ |
| İşbank 지점망·자율 네트워크 | 중국·아시아 | 실증은 배포 자동화, L4 자율은 선언 단계 | 지점 구축 1시간(10배) |
| Web3 거래소 AIDBS 거버넌스 | 중국·아시아 | 메타데이터 통합(DX) 위 DAS 에이전트 자동 장애처리 | 진단 30초·정확도 92% |
| 현대차 × NVIDIA 자율주행·로봇·공장 | 자율주행·물리 AI | 디지털트윈·표준은 DX, 자율주행은 로드맵 | 2028년경 양산 로드맵 |
| 현대차 × Waymo 로보택시 파운드리 | 자율주행·물리 AI | 양산은 DX, 자율판단은 Waymo Driver | 아이오닉5 수만 대 공급 계획 |
| 현대차 국내 투자 데이터 플라이휠 | 자율주행·물리 AI | 인프라 DX 위 재학습 순환으로 자율화 | 총 51조 원 |
| Institut Curie×Orange 의료 XAI | 통신·주권·국가 | 딥러닝이 판단하나 최종 결정은 의사(애매†) | 연 7,000명 신규 환자 |
| Elisa×Nokia×NVIDIA AI-RAN 상용화 | 통신·주권·국가 | 인프라 PoC 위 자율 네트워크는 로드맵(애매†) | 2027년 말 상용 SW 목표 |
| Scale AI×산업 190개 프로젝트 | 통신·주권·국가 | 배치 최적화에 AI 판단, 다수는 파이프라인형(애매†) | 총 $7.5억, 배율 4.7x |
| Zapier×Anthropic 자동화 | 생성미디어·도구·수요기업 | 규칙 워크플로 기반 위 에이전트化, 70.17%로 자율화 미완 | 70.17%(600과제) |
| Pringles/Kellanova×Siemens 공정 | 생성미디어·도구·수요기업 | 디지털트윈(DX) 위 규칙기반→목표기반 제어 이행 | 증산 2~10%·에너지 7%↓ 목표 |
| Unilever R&D·마케팅 | 생성미디어·도구·수요기업 | 데이터 정비·디지털화가 본체, AI 시나리오는 인간 의사결정 보조(†) | 혁신주기 2~3년→9~12개월 |

### DX — 37건

| 사례 | 클러스터 | 판정 근거 | 대표 수치 |
|---|---|---|---|
| Instacart Caper Cart 추천 | NVIDIA · AI 인프라 | ML 추천 고도화, 워크플로 재설계 근거 부족 † | 매장 매출 +1%p |
| BYD·Geely·닛산·현대 Hyperion | NVIDIA · AI 인프라 | 공통 플랫폼·데이터 표준화, 자율 요소 미확인 | 톱10 중 4개 OEM 채택 |
| Red Hat·Canonical·MS OpenShell | NVIDIA · AI 인프라 | 에이전트용 OS 런타임 통합, 발표 단계 | — |
| (비교) AMD Helios 랙 | NVIDIA · AI 인프라 | 하드웨어 공급, '에이전트' 단위는 마케팅 지표 | 동시성 34배 처리량 |
| (비교) Vertiv 전력·냉각 | NVIDIA · AI 인프라 | 물리 인프라, AI 판단 요소 없음 | 랙 140kW→1MW+ |
| (비교) SK하이닉스 AI 메모리 | NVIDIA · AI 인프라 | 부품 공급·전시 서사 수준 | — |
| BBVA 클라우드 거버넌스 | Google 생태계 | 대시보드·경계 정비, 에이전트는 예고 단계 | 1,000+ GCP 프로젝트 |
| NVIDIA 인프라 공동설계 | Microsoft · GitHub | 인프라 최적화, AI 자율 판단 없음 | 토큰 비용 약 30배 절감 |
| NHS 의료 데이터 플랫폼 FDP | Palantir · ServiceNow · Oracle | 사일로 통합·단일 화면, 판단은 사람 | 작업 4분→30초 |
| Hadean 국방 C2 시뮬레이션 | Palantir · ServiceNow · Oracle | Foundry 위 플랫폼 구축, 자율 판단 근거 없음† | MOD 3개월 조달 주기 |
| 익명 조달 고객군 인보이스·RFQ | Palantir · ServiceNow · Oracle | 정형 대사·자동화, 자율 분기 근거 없음† | 대상 지출 연 1~10% 절감 |
| FedEx 디지털 트윈·Control Tower | Palantir · ServiceNow · Oracle | 트윈·AI 자산 관리는 거버넌스 인프라† | 일 2PB 데이터 |
| CNA 보험 리스크 평가 자동화 | Palantir · ServiceNow · Oracle | 평가 처리량 확대, 판단 자율성 불명† | 연 50개 시스템→확대 |
| Ricoh 영업 AI | Palantir · ServiceNow · Oracle | 데이터 품질 정비 병행 초기 단계 | — |
| Red Bull Racing 레이스 전략 | Palantir · ServiceNow · Oracle | 시뮬레이션 컴퓨팅, 인간 판단 유지 | — |
| Panther Labs 인수 | Databricks · 벡터DB · W&B | 인수 이벤트, 자율 판단 실체 없음(†) | LakeWatch 출시 2개월차 |
| Anthropic 파트너십·키노트 | Databricks · 벡터DB · W&B | 담론·파트너십, 배포 사례 아님(†) | — |
| DEFRA 이탄지 지도화 | Databricks · 벡터DB · W&B | 정해진 인식 작업 자동화(†) | 1주→1일 미만 |
| Canva·Nestlé·TR·DraftKings | Databricks · 벡터DB · W&B | 분석·예측 앱, 판단은 사람(†) | 월 2.65억 사용자 |
| Expel 경보 중복 방지 | Databricks · 벡터DB · W&B | 유사도 검색 보조 파이프라인 | — |
| Morningstar Intelligence Engine | Databricks · 벡터DB · W&B | RAG·text-to-SQL 정형 파이프라인(†) | — |
| Sanofi·GSK·CoreWeave W&B | Databricks · 벡터DB · W&B | 교육·보조 앱, 자율 실행 증거 없음(†) | 대화 900만+건 |
| Infosys × Swedbank 미팅 요약 | SAP · Salesforce · 컨설팅 | 요약 자동화뿐, 자율 판단 미확인(†) | ~60개 저축은행 확산 |
| 삼성 관계사 ChatGPT Enterprise | 한국 AX | 도구 보급·거버넌스 정비, 재설계 근거 없음† | 고객사 20여 개 |
| SK디스커버리 현업 AX(JSA·번역·챗봇) | 한국 AX | 생성 AI 보조 도구, 자율 분기 없음† | 문의응대 건당 30분↓ |
| 한국은행×NAVER 금융 LLM | 한국 AX | 프라이빗 클라우드 인프라 구축 단계 | — |
| 플리토×Upstage Document Parse | 한국 AX | 정형 문서 추출 파이프라인 | 인식률 10%p 우위 |
| Ant Group 코어 아키텍처 재구축 | 중국·아시아 | AI-native는 촉구 담론, 자율 판단 실증 없음 | 12년 5회 전면 재구축 |
| Telecom Argentina 멀티클라우드 | 중국·아시아 | 클라우드 이전, AI는 계획 단계 | — |
| Keyrus×RCBC 데이터 역량화 | 중국·아시아 | 데이터 통합·분석 부여, 자율 판단 없음 | — |
| 베트남 통신 3사 국가 AX 분업 | 중국·아시아 | 전략·전망 단계, 자율화 실증 없음(†) | 2030 GDP +$790억 전망 |
| 텔코 얼라이언스 12사 스타트업 공동투자 | 통신·주권·국가 | 투자·확산 채널 구축, AI 자율 판단 아님(애매†) | 70개 시장·3.6억~15억+ 고객 접근 |
| Bleu·Cloud Avenue 주권 인프라 | 통신·주권·국가 | 클라우드 인프라 구축, 자율 판단 요소 없음 | 헬스데이터 호스팅 인증 보유 |
| T-Mobile 등×Nokia AI-for-RAN 검증 | 통신·주권·국가 | 정해진 최적화 알고리즘 PoC, 자율 분기 근거 없음(애매†) | 스펙트럼 효율 20%+ 검증 |
| Telefónica CMD 2025 EU 주권 프레임 | 통신·주권·국가 | 투자자 담론, 전환 실행 사례 아님(애매†) | 사이버방어 기회 €100억~220억(2035) |
| GE HealthCare 초음파 AI | 생성미디어·도구·수요기업 | 'GPS' 증강 한정, 판단은 인간 유지 — 보수 판정(†) | — |
| LinkedIn 노동시장 데이터 | 생성미디어·도구·수요기업 | 정형 데이터 분석·리포트, AI 자율 판단 없음 | AI 신규 일자리 130만 |

### DX(AX 표방) — 17건

| 사례 | 클러스터 | 판정 근거 | 대표 수치 |
|---|---|---|---|
| GitHub 생산성 서사 | NVIDIA · AI 인프라 | 검증 불가 외삽 서사, 전환 실체 없음 † | 커밋 5억→14억(외삽) |
| (비교) Arm AGI CPU | NVIDIA · AI 인프라 | 칩 공급인데 AGI·에이전트 담론 차용 † | GW당 코어 3,000만 |
| Visa MCP 쇼핑 컨시어지 데모 | AWS 에이전트 플랫폼 | AX형 라우팅이나 mock 모드, 자율 실행 증거 부재† | 모의(mock) 모드 |
| Ulta/Flex/HCL 공장 데이터 에이전트 | Google 생태계 | 실체는 데이터 통합, 자율 판단 근거 미제시(†) | 100+ 공장 30개국 |
| Blue Tulip/Affectiva 담론 파트너 | Microsoft · GitHub | 담론 중심, 에이전트 자율화 실증 없음 † | Fortune 500 절반 사용 주장 |
| BNY — CEO 'Eliza' 간증 | OpenAI · Anthropic | 실명 간증만, 자율화 실체 부재† | — |
| Commonwealth Bank — 전략 선언 | OpenAI · Anthropic | 선언만, 실행 근거 전무† | — |
| Accenture × JPM·DBS·BNY 보고서 | SAP · Salesforce · 컨설팅 | 디지털 직원 수사 vs 이메일 보조 실체(†) | 주 3시간 절감(재인용) |
| Infosys Davos 패널 담론 | SAP · Salesforce · 컨설팅 | 구현 없는 담론·공포 수사(†) | — |
| 대동×NAVER 농업 에이전트 | 한국 AX | 에이전트 표방이나 준비 단계·실질 미확인† | — |
| BMW 차내 Qwen 에이전트 | 중국·아시아 | 대표 지표가 웨이크업 정확도=음성비서 수준(†) | 웨이크업 정확도 99% |
| SoftBank 전사 에이전트 운동 | 중국·아시아 | KPI가 제작 개수, 자율 성과 미검증(†) | 2.5개월 250만+ 에이전트 |
| Tesla × SpaceX·xAI TERAFAB | 자율주행·물리 AI | 비전 서사, 자율화 실체 미검증† | — |
| Siemens × AWS·MS 산업 AI 팩토리 | 자율주행·물리 AI | 디지털트윈 DX+AI 수사, 실증 부재† | — |
| 오렌지 아프리카·중동 포용 AX | 통신·주권·국가 | AX 명명이나 실질은 인프라·교육 구축(애매†) | 3년 capex €50억 |
| Netflix·할리우드×Runway 대담 | 생성미디어·도구·수요기업 | 정량 0, 유명인 권위 서사만 — 워싱 위험 최고(†) | — |
| Philips 의료 워크플로 | 생성미디어·도구·수요기업 | 선언 중심·방법론 미제시, 자율화 근거 부재(†) | MRI 시간 절반~1/3(무방법론) |

---

# NVIDIA · AI 인프라(칩·전력) — AI Transformation 사례집
> **대표 세션/이벤트**: GTC 2026(Automotive/Healthcare Special Address, Nemotron Days, "Long-Running AI Agents"), COMPUTEX 2026 키노트("Extreme Co-Design: Building the AI Factory"), "Introducing NVIDIA Dynamo", "How NVIDIA Blackwell and NVIDIA Dynamo Scale AI Agents", AI Factory Insider Ep.1–2, AI Podcast Ep.299/302 | **관련 채널**: NVIDIA, NVIDIA_Developer (비교: AMD, Arm, SK_hynix, Vertiv) | **코퍼스 근거**: 실질 정독 18편(본채널 14 + 비교 4)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Dynamo | 분산 추론 프레임워크(오픈소스) | LLM의 prefill(연산 바운드)·decode(메모리대역 바운드)를 분리 배치하고, radix tree로 워커별 KV캐시 적중률을 계산해 라우팅. NIXL로 KV캐시 저지연 전송, Planner가 SLA 기반 prefill/decode 자동 재배분 | 단일 노드 분리만으로 GPU당 처리량 +30%, 멀티노드 구성 시 2배. 실측 10만 건 R1 요청으로 검증. DeepSeek식 배치(prefill 32 GPU/decode 320 H800)를 오픈소스로 재현 가능화 |
| Blackwell GB200 NVL72 | 랙스케일 GPU 시스템 | 72 GPU를 단일 NVLink 도메인(1,800GB/s vs 이더넷 100GB/s)으로 묶어 MoE 전문가를 GPU별 분산 서빙 | Hopper 대비 토큰 생산 최대 50배·백만 토큰당 비용 35배 절감(시간당 단가 약 2배 비쌈에도). AA AgentPerf(Artificial Analysis) 기준 GPU당 동시 코딩 에이전트 40배(57개 vs 약 1.5개, 20tok/s/user SLO) |
| Nemotron 3 (Ultra/Super/Nano) | 오픈 모델 패밀리 | 약 0.5조/120B/소형 파라미터 3종. 가중치·데이터셋·학습기법 전부 공개, build.nvidia.com 무료 엔드포인트 | Ultra는 "타 선도 오픈모델 대비 5배 빠르고 B200/B300에서 30% 저렴"(자사 주장). 온프레미스 데이터 주권 수요 흡수 |
| NeMo 커스터마이징 스택(Customizer·TAO 스킬·RLP) | 미세조정·후훈련 | LoRA로 도구호출(tool calling) 특화 미세조정(xLAM 데이터셋, 도구 10개→수백 개 확장 대응), TAO 7 스킬을 Codex 등 코딩 에이전트에 로드해 자연어 프롬프트만으로 파인튜닝 파이프라인 자동 생성. RLP는 사전학습 단계에 "생각 후 다음 토큰 예측" RL 도입 | Cosmos 3 후훈련 데모: 정확도 54.41%→87.14%(+32.7%p)를 에이전트가 자율 수행. "전문 AI 연구자 없이 도메인 적응" 서사 |
| OpenShell | 에이전트 보안 런타임(Apache 2) | 에이전트별 샌드박스로 파일·네트워크·추론 엔드포인트·프로세스 생성 범위를 정책 제어. API 키를 샌드박스 밖 게이트웨이에 두고 요청 시점 주입 | 장시간 자율 에이전트의 전제조건(승인 피로 제거). Canonical·Microsoft Windows·Red Hat이 OS에 통합·상용 지원 |
| Cosmos / Alpamayo(자막 오기: "알파 메이/마요네즈") | 물리AI·AV 파운데이션 모델 | 실주행 2,000만 시간으로 학습한 Cosmos에서 파생된 10B 파라미터 AV 추론 모델. 주행 판단을 자연어로 설명·대화 | AV 최초 추론 모델 주장, HF 로보틱스 다운로드 2위·16만 회. 7,000시간·25개국 데이터셋 오픈소스화 |
| Hyperion 10 + HALOS + AGX Thor(자막 오기 "SOAR") | AV 참조 하드웨어·안전 OS | 카메라 14/레이더 9/라이다 1 통합 센서 아키텍처, ASIL-D OS·안전 중재자(E2E모델↔클래식 스택 전환). Thor는 FP4로 Orin 대비 20배 | OEM 간 데이터 공유 표준화. NeuRec 신경 재구성으로 일 200만 건 폐쇄루프 시뮬레이션, 1년간 약 3,500회(일 10버전) 모델 반복 |
| DSX | AI 팩토리 "운영체제"·기가와트 참조설계 | 학습 부하의 급격한 전력 스파이크를 저장장치·커패시터로 평탄화, 전력회사와 수요 조율 | 와트당 GPU 40% 추가 배치→토큰 40% 증가(자사 주장). 데이터센터를 "비용센터→토큰 수익원"으로 재정의 |
| AI Factory ERA/검증된 설계 | 엔터프라이즈 참조 아키텍처 | 하드웨어(ERA)+K8s 위 에이전트·추론·관측성 스택을 파트너 ISV와 사전 통합 검증 | NVIDIA 자체 운영: 월 4조 토큰(가용성 99.9%), 일 2억 추론 요청, 내부 수요 월 40% 증가 |
| 토크노믹스 지표 체계 | 담론/측정 프레임 | 비용 지표를 GPU시간당 비용·달러당 FLOPS(입력 지표)에서 토큰당 비용=GPU비용÷토큰생산량, 메가와트당 토큰(출력 지표)으로 전환. PUE 통상 1.15–1.2, 최악 2 | "추론 모델은 출력 토큰의 100배를 내부 생성" → 분모를 바꿔 세대교체 격차(35배)를 정당화하는 핵심 문법 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| ServiceNow | IT 서비스 자율화 | "Project Arc" 자율 워크포스: 전문 에이전트(접수→심층조사→해결→기록)가 L1 티켓을 끝까지 처리. Apriel+Nemotron+클라우드 프론티어 모델, AI-Q 블루프린트 기반 | "티켓의 90%를 자율 에이전트가 해결"(How ServiceNow's AI Agents Resolve 90% of Tickets) — 자사·파트너 공동 발화 기준 | AX (에이전트가 티켓을 끝까지 자율 해결, L1 역할 재정의) |
| Cadence | 칩 설계 검증 에이전트 | ChipStack "슈퍼 에이전트"가 RTL 생성·테스트벤치·회귀·디버깅을 서브에이전트로 분업, Xcelium 시뮬레이션·Jasper 형식검증 자동 실행. Nemotron 구동·OpenShell 보안 | 형식검증 "1개월 이상→10시간"(Long-Running AI Agents), "검증 주기 40배 이상 단축"(Cadence Cuts Chip Verification). Vera Rubin 세대당 프로세서 7종 공동설계에 적용 | AX (서브에이전트 분업·계획 수립 후 자율 실행) |
| CrowdStrike | 보안 운영(SOC) | 알림 자동 트리아지 에이전트로 오탐 선별, 분석가는 심층 건에 집중 | 정성적 언급만(Long-Running AI Agents) — 수치 미제시 | AX† (AI가 오탐 판단·분기, 사람 역할 재정의 — 단 수치 미제시) |
| Palantir | 플랫폼 통합 | Nemotron을 "AI 전진배치 엔지니어(FDE)"로 탑재, 온톨로지 위에서 공급망·물류 최적화 코드 작성 | 정성적 언급(Long-Running AI Agents) | AX† (에이전트가 최적화 코드 자율 작성 — 정성적 발화뿐, 자율 범위 불명) |
| Instacart | 리테일 엣지 AI | Caper Cart: Jetson 엣지 센서퓨전 물리AI + 클라우드 추천(10년간 온라인 주문 16억 건 학습) | 카트 경유 지출 "두 자릿수 %" 증가, 신규 추천 알고리즘으로 매장 매출 절대 +1%p, "잊으신 물건?" 기능 단독 약 1%(NVIDIA AI Podcast Ep.302) | DX† (ML 추천·센서퓨전 고도화이나 워크플로 재설계·자율 판단 근거 부족) |
| Mercedes-Benz (+JLR·Lucid) | 자율주행 | Alpamayo 추론 모델 프로토타입 SF 실주행 시연. 2020년 파트너십→2025년 중국 제외 전 세계 차량 적용 원년, L2+ 순차 확대 | 2028년 말 승용 L4 목표. Uber와 L4 협력(도시 수 등 세부 수치는 자막 훼손 가능) | DX→AX (현행 L2+는 보조, 추론 모델 기반 L4 자율 판단으로 이행 중) |
| BYD·Geely·닛산·현대 | Hyperion 생태계 | 글로벌 톱10 중 4개 OEM이 공통 센서·컴퓨트 플랫폼 채택(GTC Automotive Special Address) | 데이터 공유 표준화 효과 주장 | DX (플랫폼·데이터 표준화 = 인프라 정비, 자율 판단 요소 미확인) |
| Red Hat·Canonical·Microsoft | 에이전트 인프라 | OpenShell의 OS 통합, Red Hat AI Factory(Nemotron 온프레미스+기밀 컴퓨팅 프리뷰, Google Gemini의 GDC 반입 협력) | 상용 지원 발표 단계 | DX (에이전트를 위한 런타임·OS 통합 = 기반 인프라, 발표 단계) |
| NVIDIA(자체 도그푸딩) | 사내 AI 팩토리 | ChipNeMo(3년 이상 운영, 하드웨어 엔지니어 약 5,000명 매일 사용), 보안 에이전트 워크스페이스(VDI 샌드박스) | 월 4조 토큰·일 2억 요청·수요 월 40%↑, 워크스페이스 3개월 만에 15배 성장(AI Factory Insider Ep.2) | DX→AX (코파일럿형 ChipNeMo 기반 위에 자율 에이전트 워크스페이스 확장 중) |
| 생태계 지표(GitHub 인용) | 생산성 서사 | "작년 커밋 5억(전문 개발자 3,000만)→올 상반기 14억 = 생산성 3배 → 인건비 3조 달러×3 = 6조 달러 경제산출" | NVIDIA 발화의 추정치(Long-Running AI Agents) — 검증 불가 외삽 | DX(AX 표방)† (전환 사례가 아닌 검증 불가 외삽 서사) |
| (비교) AMD | 개방형 랙 대항 | Helios 랙(MI455X): 저동시성 4배, 최고 동시성서 전세대 대비 34배 처리량. Venice CPU "에이전트 샌드박스 와트당 에이전트 2배+, Arm 칩 대비 2.8배" | "open ecosystem" 3대 전략으로 NVIDIA 수직통합에 대항(Advancing AI 2026) | DX (하드웨어 인프라 공급 — '에이전트' 단위는 마케팅 지표) |
| (비교) Arm | 전력·CPU 담론 | "기가와트당 CPU 코어 3,000만 개", 에이전트 폭발이 CPU 수요 견인. 최초 자체 실리콘 'AGI CPU' 판매 개시, Meta가 앵커 파트너("동일 전력 봉투에 3,000만→1.2억 코어") | IP 라이선스→칩 판매로 사업모델 전환(Arm Everywhere Keynote) | DX(AX 표방)† ('AGI CPU' 명명 등 담론 차용, 실질은 칩 공급 인프라) |
| (비교) Vertiv | 전력·냉각 물리 | 랙 밀도 140kW(현재)→200/240kW→600kW→1MW+ 로드맵, 커넥터·버스바·구리의 물리 한계→800VDC 전환 | NVIDIA GTC 세션 공동 등판, OneCore로 Vera Rubin DSX 대응(The physics driving the shift to 800 VDC) | DX (전력·냉각 물리 인프라, AI 판단 요소 없음) |
| (비교) SK하이닉스 | AI 메모리 | GTC 2026 부스 'NVIDIA 협업존'에서 HBM·SOCAMM2(자막 "Soc 2")·eSSD 전시. "GPU 성능은 데이터 끊김 없는 공급이 전제" | 전시·서사 수준(하이포커스 ON GTC 2026) | DX (메모리 부품 공급·전시 서사 수준) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 분모 바꾸기의 진화 계보 | GPU시간당 비용→토큰당 비용→MW당 토큰→"동시 에이전트 수"(AA AgentPerf)로 지표가 이동. AMD는 "agents per watt", Arm은 "cores per gigawatt"로 같은 문법을 자사 유리하게 변주 | AX 비용구조 연구의 측정 단위 자체가 벤더 경쟁의 산물. 35배·40배류 수치는 항상 "어느 분모에서인가"를 물어야 함 |
| 에이전트=인력 환산의 정점 | "커밋 3배=인건비 3조 달러×3=6조 달러", 티켓 90% 자율 해결, GPU당 동시 에이전트 57개 — 노동을 인프라 구매 단위로 환산 | 칩 판매 논리가 곧 노동 대체 담론. ServiceNow "L1 대체"와 결합해 '에이전트=인력' 프레임의 공급측 원천 |
| 전력이 최상위 제약 | PUE·800VDC·DSX 전력 평탄화(와트당 GPU 40%↑)·45°C 폐쇄 액랭·랙 140kW→1MW. "토큰의 원자재는 전기" | AX 원가의 물리적 하한선은 전력망. 균등화발전비용(LCOE)식 사고가 토큰 원가론으로 이식됨 — 비용구조 연구의 1차 정량 앵커 |
| 자기 실증(첫 고객=자사) 전략 | 사내 월 4조 토큰, ChipNeMo 5,000명, Cadence와의 자사 칩 검증, Alpamayo "일 200만 시뮬레이션" — "우리가 먼저 써봤다"가 판매 논리 | 워싱 방지 장치인 동시에 순환 구조(자사 수요로 자사 칩 정당화). 내부 수치는 외부 감사 불가 |
| 거버넌스 계층의 락인 | OpenShell·NeMo Guardrails·"검증된 설계"는 오픈소스(Apache 2)지만 OS 3사 통합·참조 아키텍처로 스택 전체가 NVIDIA로 수렴 | "AX의 진짜 락인은 모델이 아니라 런타임·거버넌스 계층" 명제의 하드웨어판. AMD의 open-vs-lock-in은 이에 대한 직접 대항 담론 |
| HITL 제거의 재포장 | "승인 버튼 피로(네/아니오 반복)"를 샌드박스 보안으로 해소 → 자율 실행이 기본값化 | 인간 개입 축소가 '보안 강화'의 언어로 정당화되는 전형 사례. HITL 프레임 연구에 핵심 |

**AX/DX 스펙트럼**: 이 클러스터의 실질 AX는 ServiceNow·Cadence 등 장시간 자율 에이전트 사례에 집중되고, 자체 도그푸딩·Mercedes AV는 DX 기반 위에 자율 판단을 얹는 DX→AX 이행 단계다. 비교군(AMD·Arm·Vertiv·SK하이닉스)과 생태계 지표는 인프라 공급·담론(DX)이면서 "agents per watt", "AGI CPU" 같은 에이전트 어휘를 차용해 워싱 위험이 상존한다.

※ **신뢰 경계**: 본 클러스터 수치는 전량 자사(NVIDIA) 또는 파트너 공동 마케팅 발화 기준이며 독립 검증은 AA AgentPerf(제3자 벤치마크) 정도가 유일. 한국어 자동자막 훼손이 심각함 — 도메인명사→"[음악]" 치환, Nemotron→"Neumotron/니모트론", Thor→"SOAR/급등", Alpamayo→"알파 메이/마요네즈", Claude/Claw→"발톱/집게발", kW→W 오기(Vertiv) 등. 의심 수치(Uber L4 도시 수 등)는 표기함. 이전 분석노트의 "Adobe Firefly 파트너"는 원문 재확인 결과 Dynamo Q&A의 'Firefly 파일시스템'(스토리지) 언급으로 판명되어 제외. GitHub 커밋→6조 달러 환산은 NVIDIA의 외삽이며 근거 미제시. SK하이닉스·Vertiv 영상은 전시·홍보 성격이 짙어 워싱 위험 중간, ServiceNow 90% 수치는 데모 내레이션 기반으로 모수·기간 미공개.

---

# AWS · 에이전트 플랫폼(Bedrock·Strands·AgentCore) — AI Transformation 사례집
> **대표 세션/이벤트**: "Model Driven Agents – Strands Agents"(오픈소스 공개 발표), "Multi-Agent Patterns" 3부작(Agents as Tools/Graph Workflows/Agent Swarms), "Evaluating Agents", "Improve Agent Reliability with Strands Steering", "We Need to Talk About AI Agent Architectures", "Deploy Production-Ready Agents in 22 Minutes with AgentCore Runtime", "How Much Does Your AI Agent Actually Cost?", AWS Executive Insights 팟캐스트 "Leading AI Transformation: A Chief AI Officer's Perspective"(Leidos CAIO), IBM "MCP vs ADK" | **관련 채널**: AWS_Developers, Amazon Web Services(※코퍼스에 AWS_Events 폴더 부재 — 키워드 수집분 1편으로 대체), IBM_Technology | **코퍼스 근거**: 실질 정독 16편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Strands Agents SDK | 오픈소스 프레임워크(Apache 2) | "모델 주도(model-driven)" 에이전트: 목표+도구만 주면 모델이 계획·오케스트레이션. `@tool` 데코레이터 한 줄로 함수→도구화, MCP 연결, Bedrock/Ollama/OpenAI 등 모델 중립 | Q Developer 팀 자사 사용에서 신규 에이전트 프로덕션 투입 기간 "수개월→수주"로 단축(발화 그대로) |
| Strands 멀티에이전트 3패턴 | 아키텍처 패턴 | ①agents-as-tools: 허브앤스포크, 하위 에이전트별 격리 컨텍스트로 "시끄러운 도구"(웹검색) 노이즈 차단 ②graph: 노드=에이전트·엣지=의존성으로 실행순서 보장, 병렬 팬아웃·조건분기·피드백 루프 ③swarm: 자율 핸드오프로 경로가 런타임에 창발(프로덕션 장애 분류 예시) | 판단 기준 명문화: "화이트보드에 그릴 수 있으면 graph, 관리자-전문가 관계면 tools, 함께 답을 찾아야 하면 swarm". 그래프는 max 노드실행·재방문 시 리셋, 스웜은 max handoffs/iterations·타임아웃·반복 핸드오프 감지로 "에이전트 둘이 핑퐁하며 토큰 소각" 방지 |
| Strands Steering | 신뢰성 계층 | 에이전트 루프 훅에서 진행/가이드/중단 3판정. 결정론적 tool-steering(이벤트 원장으로 환불 전 필수단계 순서 강제)+LLM-judge 스티어링(톤·정책 위반 응답을 고객 도달 전 폐기·재생성) | "모델은 몇 턴 전 정적 프롬프트보다 시의적 수정 피드백에 훨씬 안정적으로 반응" — 프롬프트 순종 한계를 검증층으로 보완, 매개변수 환각 차단 |
| Strands Evals SDK | 평가 | 대화 시뮬레이터+LLM 심판(루브릭)+궤적(trajectory) 평가기(올바른 절차 수행 검증)+순수 파이썬 결정론 평가기+테스트케이스 자동 생성기. CI/CD에 연결해 점수 미달 시 배포 자동 실패 | "프로덕션 에이전트에서 가장 중요한 투자". 데모 고객서비스 에이전트 합격률 66%(환불 83점, 주문추적 0.5, 계정 0점) — 실패를 정직하게 노출 |
| Strands 컨텍스트 관리(`context_manager=auto`) | 컨텍스트 엔지니어링 | 대용량 도구 결과 외부 오프로딩+미리보기 치환, 슬라이딩 윈도우/요약 압축(저가 모델로 요약 가능), 사용량 85% 도달 시 사전 압축 | 자사 코드 분석 벤치마크: **비용 55% 감소, 정확도 68%→98%**(자사 발화 기준) — 토큰 절반으로 더 나은 결과 |
| Amazon Bedrock | 모델 서빙 | Converse API로 Claude·Mistral·Nova 등 FM 호출, Knowledge Bases(문서 업로드→자동 인덱싱 RAG), Guardrails | 모델 교체·저가 라우팅의 기반. "간단 쿼리는 Nova Micro로 라우팅" — Sonnet 대비 격차가 커 대규모에서 상당한 절감 |
| AgentCore Runtime | 관리형 서버리스 런타임 | import·인스턴스·데코레이터 "3줄 코드"로 배포. 세션당 격리 microVM(자체 컴퓨트·파일시스템), 기본 15분~최대 8시간 세션, 프레임워크·모델 불문(LangGraph·CrewAI·OpenAI 모델 포함), VPC 연결로 프라이빗 RDS 접근 | 배포·확장·세션격리·인증 추상화, 250MB 미만 직접 코드 배포는 업데이트 ~10초 — "노트북→인터넷" 시간 수분화 |
| AgentCore Memory | 관리형 메모리 | 단기: 대화 이벤트 영속화(재시작 후 복원). 장기: 전략(사용자 선호 등) 기반 사실 자동 추출→의미검색으로 컨텍스트 주입(개인화 특화 RAG) | 세션 경계를 넘는 연속성·개인화, actor ID 스코핑으로 사용자 간 데이터 격리 |
| AgentCore Gateway·Identity·Observability | 운영 하위서비스 | 요금계산기 항목으로 Runtime·Gateway·Identity·Memory 구분. 관찰: CloudWatch 자동 로그, OpenTelemetry 스팬(에이전트 호출→모델→도구 중첩 추적), OTLP로 Datadog·LangFuse 연동 | 사이클 수·도구별 지연·토큰 사용을 요청 단위로 계측 — "도구호출 급증=무한루프, 한 사이클 장기화=느린 모델" 진단 문법 제공 |
| AgentCore Managed Harness | 신규 관리형 하네스 | 에이전트 루프 자체를 구성 파일+시스템 프롬프트로 대체(정의→배포→호출 3단계), 세션별 microVM·기본 메모리 활성·영구 스토리지 | 컴퓨트·샌드박스·스토리지·인증·관찰의 조립 노동 소거 — 하네스의 상품화 |
| 비용 계측 도구 | FinOps | AWS Pricing Calculator(월 세션수·IO대기·vCPU 입력→견적), Cost Explorer(모델·API별 일 단위 분해), AWS Pricing MCP 서버(Kiro IDE에서 견적 자동화) | 데모 견적: 런타임 월 ~$1 + Bedrock(Sonnet 4.5) 월 ~$259 — "에이전트 비용은 창발적"이라는 명제의 도구화 |
| IBM 프레임: MCP vs ADK | 개념 구분(교육) | MCP(Anthropic 개방 표준)=연결 계층: 도구·리소스·프롬프트를 JSON-RPC로 표준 노출, 모델 불문 재사용. ADK(Google)=구축·오케스트레이션 프레임워크: 에이전트·러너·상태/메모리, LLM 에이전트 vs 결정론 워크플로 에이전트 | "경쟁이 아니라 상호보완" — ADK가 무엇을 할지, MCP가 세상과 어떻게 통신할지. 계층 명명 자체가 시장 교육 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| Leidos(론 케인, 신임 CAIO) | AWS 클라우드+생성형 AI 전사 전략 | CAIO 직책을 본인이 직접 설계·신설. AI 액셀러레이터 조직 기반 허브앤스포크(중앙 COE 독점 거부), IT 헬프데스크 생성형 AI 챗봇을 정부 고객으로 확대, 코딩 어시스턴트는 IaC·컴플라이언스 자동화에 집중 | 생성형 AI 솔루션 중 **27%만 승인돼 프로덕션 투입**. 운영 규모: 1천만+ 사용자 전자의무기록, FAA 관제 SW, 미 국방부 대상 세계 3위 IT 네트워크. "개발자 효율 30~40%↑가 30~40% 감원을 뜻하진 않는다" (Leading AI Transformation: A Chief AI Officer's Perspective) | DX→AX† (클라우드·IaC 자동화라는 DX 기반 위 생성형 AI 보조 — 자율 판단·워크플로 재설계 근거는 약함) |
| Orca Security(Shai Alon, AI혁신 디렉터) | Amazon Bedrock+Knowledge Bases | 클라우드 보안 경고→원클릭 복구 지침 생성(CLI/콘솔/IaC 형식 선택), 채팅으로 후속 교정. 연구원 큐레이션 문서를 Knowledge Bases에 업로드해 LLM 보강 | 최초 OpenAI 사용→정확도 요구로 **Bedrock 전환**(수집 코드 불필요가 전환 사유). "티켓 발행 대신 즉시 조치" — 정량 수치 미공개 (Orca Security: GenAI-powered Cloud Security Remediation) | DX→AX† (AI가 복구안을 판단·생성해 티켓 워크플로를 재설계했으나 실행은 사람의 원클릭 — 자율 실행 미달) |
| AWS Q Developer(자사 도그푸딩) | Strands 개발 원류 | 초기 모델 시절 수작업 오케스트레이션 지침의 불안정성을 겪고 "모델 주도"로 전환, 내부 수개월 사용 후 오픈소스화 | 에이전트 프로덕션 투입 "수개월→수주" (Model Driven Agents – Strands Agents) | AX (사람이 정한 오케스트레이션 규칙을 버리고 모델이 계획·분기 — 시금석 정면 충족) |
| OpenAI(모델 제공사) | AgentCore Runtime 데모 | 물류 지원 에이전트를 Strands+OpenAI 모델로 구축, Secrets Manager로 키 관리, NAT 게이트웨이 경유 호출 | AgentCore의 "모델·프레임워크 중립" 실증 — 경쟁사 모델도 자사 런타임 위에 (Deploy Production-Ready Agents in 22 Minutes) | AX† (에이전트가 판단·도구 실행하는 구조이나 프로덕션 아닌 데모 실증) |
| Visa(결제 MCP 서버) | 쇼핑 컨시어지 데모 | 관리자 에이전트가 쇼핑/장바구니/구매 에이전트로 라우팅, 결제는 Visa MCP 서버 연동 구조 | 데모는 **모의(mock) 모드** — 실거래 아님, 실계약 여부 미확인 (How Much Does Your AI Agent Actually Cost?) | DX(AX 표방)† (멀티에이전트 라우팅 구조는 AX형이나 mock 모드·실계약 미확인 — 실질 자율 실행 증거 부재) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| "사람 소거"형 AX 담론 | 16편 전체에서 인력 대체·헤드카운트 수사가 사실상 부재. 동일한 업무 알고리즘화를 토큰·컨텍스트·평가·격리라는 순수 원가/신뢰성 엔지니어링 언어로만 번역 | Zapier·Google(사람 전면화)과의 대조축 — 청중(개발자 vs 경영진)이 담론 표면을 결정. "에이전트=인력" 프레임의 부재 자체가 데이터 |
| 평가(eval)가 새 전장 | 궤적 평가+LLM 심판+CI 게이팅을 "가장 중요한 투자"로 선언, 단 "평가 자체가 토큰을 상당히 소모"도 인정. 합격률 66% 실패 노출은 드문 반워싱 제스처 | 벤치마크·루브릭 정의권=「어느 에이전트가 좋은가」의 정의권. 온톨로지 land-grab의 성능판정 버전(분모스왑 평가층) |
| 컨텍스트 관리=원가 지렛대 | `context_manager=auto` 한 줄로 비용 55%↓·정확도 68→98% — 비용과 품질이 상충 아닌 동행으로 제시 | AX 비용구조 연구의 직접 데이터포인트. 단 자사 벤치마크·검증 불가 — "분모(토큰) 최적화"가 플랫폼 셀링포인트로 상품화 |
| 프로덕션 반패턴: 에이전트≠백엔드 | "에이전트는 시스템이 아니라 시스템 내부의 한 기능, 더 큰 시스템은 대부분 결정론적". 클라이언트-에이전트 직결 시 에이전트가 '기본 위치'가 되는 문제, 동일 토큰 재사용 시 게이트웨이 우회 취약점까지 실연 | 분산시스템 20년 교훈으로의 회귀 — 에이전트 만능론에 대한 벤더 내부의 구조적 견제. HITL 이전에 '결정론적 외곽'이 선행 |
| 폭주 비용의 제도화된 공포 | "$2,000 날리고 CEO가 질문 쏟아지는" 훅, 스웜 무한 핑퐁 토큰 소각 경고, 도구호출 20회 캡·25초 타임아웃·Nova Micro 저가 라우팅·요청당 토큰 계측 | '에이전트 FinOps'가 독립 장르로 성립(계산기·Cost Explorer·가격 MCP까지 도구화) — 창발적 비용이 AX 도입의 핵심 마찰이라는 방증 |
| 운영계층 거버넌스 락인 | "프레임워크·모델 중립"(OpenAI·LangGraph도 환영)을 내세우되 Runtime·Memory·Gateway·Observability·Harness로 실행·기억·연결·계측 전 계층을 관리형으로 포섭 | 모델이 아닌 하네스·운영이 락인 지점. IBM은 MCP/ADK 계층 구분 교육으로 같은 지형을 명명하며 진입 |
| 수요측 분모 전환(Leidos) | "효율 30~40%↑≠감원. 절감된 노동시간의 투자처는 기업 몫" — 성공지표를 컴플라이언스 체크마크·배포속도·파이프라인 기여로 재정의. 제안서를 AI가 쓰고 AI가 읽는 미래엔 "텍스트 인코딩·디코딩이 근본 가치를 더하지 못한다" | 분모스왑의 수요측(CAIO) 발화 — 인건비 환산을 회피하고 시간→체크마크로 지표 이동. 27% 프로덕션율은 "도입≠성과" 명제의 자사 인정 |

**AX/DX 스펙트럼**: 이 클러스터는 플랫폼(Strands·AgentCore) 자체는 AX 인프라를 팔지만, 고객 사례는 DX→AX 이행 구간(Leidos·Orca)에 몰려 있고 순수 AX 실증은 자사 도그푸딩(Q Developer)뿐이다. Visa·OpenAI 건은 mock/데모 수준이라 "에이전트" 명명이 실거래 자율성보다 앞서는 워싱 위험이 있으나, 실패율·비용을 스스로 노출하는 채널 성격상 전반적 워싱 강도는 낮다.

※ **신뢰 경계**: 수치 전부 벤더 자사 발화(55%↓·68→98%는 Strands 자체 벤치마크, 외부 검증 없음; Leidos 27%는 자사 CAIO 발화). 자막 자동번역 훼손 다수 확인 — 도메인명사→"음악" 치환(비용 영상), agent→"부동산 중개인"류 치환, "Anthropic Games"(→Anthropic), "CLOM/CLA"(→Claude), "법학전문대학원"(→LLM), "인류 모델"(→Anthropic 모델) 등: 인용 시 원어 재확인 필수. 워싱 위험은 낮은 편(실패율·비용 리스크를 스스로 노출하는 엔지니어링 채널)이나, AWS_Developers는 자사 플랫폼 셀링이 전제이며 고객 성과 수치는 Leidos·Orca 모두 정량 ROI 미공개. AWS_Events 채널은 코퍼스에 부재해 Amazon Web Services 채널 1편(CAIO 팟캐스트)으로 대체함.

---

# Google · Gemini/ADK/A2A 생태계 — AI Transformation 사례집
> **대표 세션/이벤트**: Google I/O 2026 키노트(Sundar Pichai 오프닝, Google Antigravity 세션), Google Cloud Next '26 세션("Agent context engineering for production", "Building enterprise-grade AI agents"), "Prototype to Production with ADK" 워크숍, "AI Agent Clinic"·"A2A & Agent Registry" 시리즈 | **관련 채널**: Google_Cloud_Tech, Google_Developers, Google, Google_DeepMind | **코퍼스 근거**: 실질 정독 12편(전문 10 + 표적 발췌 2)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| ADK (Agent Development Kit) | 에이전트 프레임워크 | LLM 에이전트(비결정적 추론)와 워크플로 에이전트(순차=조립라인, 루프=최대반복+escalate 탈출)를 조합해 멀티에이전트 파이프라인 구성. "결정적 작업은 도구, 추론·오케스트레이션은 에이전트" 분리 원칙 | PayPal: 자체 오케스트레이션 대비 코딩 시간 50~60% 단축(세션·메모리·병렬실행 내장 덕) |
| A2A 프로토콜 | 에이전트 간 통신 표준 | 에이전트 카드(agent_card.json)로 스킬·연결법 공개, "AI 에이전트의 HTTP". LangGraph·CrewAI 등 프레임워크 무관, 동기/폴링/SSE 지원 | 느슨한 결합으로 에이전트 단위 수정·재배포 가능 → 모놀리스 재작성 비용 제거 |
| Agent Registry | 발견·거버넌스 계층 | 에이전트·MCP 서버·엔드포인트를 단일 등록소에 등재, 레지스트리의 MCP 서버가 프롬프트→적합 에이전트를 동적 매핑. 에이전트 정책(비공개 프리뷰)으로 통신 허용 범위 통제 | 명시 목표 3종: 재사용성·연결 표준화·**거버넌스와 감사**(비용·위험 모니터링, 로깅) |
| Memory Bank (Vertex AI/Agent Platform) | 장기 기억 관리 | 대화에서 LLM이 의미 추출→기존 기억과 통합(consolidation), 스키마 기반 memory profiles, 사용자/세션/부서 단위 scope, 파생 이력 추적·롤백, 10분 비활성 시 추출 트리거 | 세션·채널을 넘는 컨텍스트 지속 → "매번 0에서 시작하지 않는" 에이전트. AT&T 판매 에이전트의 핵심 기반 |
| 컨텍스트 엔지니어링(스킬·컴팩션) | 방법론/신규 직능 | context rot(토큰 증가 시 성능 저하) 대응: 스킬의 progressive disclosure(레벨1 메타데이터만 상시 로드), 세션 컴팩션, 도구 스키마 다이어트 | 단일 에이전트 정확도 95%도 3단 연쇄 시 약 86%로 하락("10%p 하락=프로덕션 부적합") — 오류 복리를 근거로 신규 필수 역량 규정 |
| Google Antigravity 2.0 | 에이전트 우선 개발 플랫폼 | 에이전트 하네스(서브에이전트·후크·비동기 작업 관리)+데스크톱 앱·CLI·SDK·음성. 계측 코드 삽입, 헤드리스 브라우저로 자가 검증 | OS 구축 데모: 93개 서브에이전트 병렬·12시간+·모델 요청 1.5만+·토큰 26억 처리, API 비용 $1,000 미만. Gemini 3.5 Flash 기본 4배→하네스 결합 시 12배 속도. "수백만 명 사용 중"(자사 발화) |
| Gemini Enterprise Agent Platform / Agent Engine | 관리형 런타임 | 세션 서비스·Memory Bank·평가·실행경로 관찰가능성 내장, 코드 수정 없는 모델 스왑. 배포 선택지: Agent Engine(관리형)/Cloud Run(scale-to-zero)/GKE | PayPal: "실행 경로 가시성이 금융사 프로덕션 전환의 확신 근거" |
| OpenTelemetry + Cloud Trace | 관측/계측 | 스팬 단위로 함수별 소요시간·토큰 수 추적, 병목 식별 | "80% speedup" 실연: 1분36초→최장 16~23초(TTS 병렬화). Home Depot AI ops의 상관분석 기반 |
| Cloud Hub / App Hub | 애플리케이션 거버넌스 | 프로젝트 단위 리소스를 '애플리케이션' 경계로 묶어 집계 대시보드 제공 | BBVA 1,000+ GCP 프로젝트 운영 부담 축소, 차기 단계로 에이전트 레이어 예고 |
| Gemini Cloud Assist + 에이전트 스킬 | 운영 자동화 | 터미널에서 로그 탐색·조사·해결 지식을 스킬로 자동 공유 | MediaMarkt: Gemini CLI로 스킬 130개 구축, 신규 개발자 온보딩 수주→수시간 수준(발화 기준) |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| AT&T | 판매 에이전트(컨텍스트 엔지니어링) | ADK+Gemini로 오케스트레이터+전문가 에이전트(제품군 아닌 스킬 기준 분할), 로직/표시 계층 분리로 채널 무관 단일 컨텍스트. DLP 암복호화, MCP 도구 필터링, Vertex 세션+Memory Bank | 인간 판매원 tenure 12개월 미만 vs "장기근속" AI 논리. Day1 웹→Day3 IVR→Day7 타채널 원클릭 구매(백그라운드 카트 생성). 현재 단일 채널·단일 유스케이스로 프로덕션 가동 ("Agent context engineering for production") | **AX** — 오케스트레이터가 스킬 기준으로 판단·분기하고 판매원 역할 자체를 대체 |
| Home Depot | AIOps/신뢰성 엔지니어링 | Managed Service for Prometheus+OpenTelemetry(일관 라벨)로 컨텍스트 통합, Gemini로 RCA·요약 | 인시던트 대응 "20분 이상→약 2분"(자체 산정 발화). 목표는 자동 PR 생성이나 "아직 전 과정 인간 검증 필요" ("20 minutes to 2 minutes: How Home Depot automated incident responses") | **DX→AX** — 텔레메트리 통합(DX) 위에 AI RCA를 얹었으나 판단·실행은 아직 전량 인간 검증 |
| PayPal | 자율 SRE 에이전트 | 감지·분류·완화·보고 에이전트 생태계(관리자·RCA·보고·변경분석·서비스), MCP 서버로 사내 데이터 통합 | ADK+Gemini Enterprise로 코딩 시간 50~60% 단축. 읽기전용→차단/허용목록→샌드박스 단계적 권한. "에이전트=재입사한 인턴, 감독 필요" ("Building an MCP-powered autonomous incident response ecosystem") | **AX** — 감지→분류→완화를 에이전트가 자율 수행, 권한 확대 로드맵으로 감독 축소 설계 |
| MediaMarktSaturn | 개발자 플랫폼/스킬 | Gemini CLI 기반 스킬 130개, Application Design Center에 Terraform 블루프린트 저장, Cloud Assist로 새벽 장애 조사 | "shift-left 아닌 shift-down"(플랫폼으로 권한 이양) 명제. 팀 이동·온보딩 수주→수시간/수분(발화 기준) ("Agile developers: shifting down with agentic skills") | **DX→AX**† — 스킬·블루프린트는 지식 전산화(DX), Cloud Assist 장애 조사만 자율 판단 요소 |
| BBVA | 클라우드 거버넌스 | 15년+ 구글 관계, App Engine 시절부터 내부 개발 플랫폼 구축, Cloud Hub/App Hub로 애플리케이션 경계 정의 | 25개국 8,100만 고객, 1,000+ GCP 프로젝트. 차기: "콘솔을 안 봐도 되는" 에이전트 레이어 ("How BBVA manages 1,000+ GCP projects") | **DX** — 리소스 경계·대시보드 정비가 실체, 에이전트 레이어는 아직 예고 단계 |
| Carrefour | 데이터 에이전트 | BigQuery 툴셋+BigQuery 에이전트 분석. 에이전트 ID가 아닌 **최종 사용자 자격증명**(OAuth, 코드 3~4줄)으로 실행해 데이터 접근 통제. 계산대 결제→Kafka→수초 내 모바일 알림 | 전사 사용자 배포 직전 단계 발화, 주간 세션 수를 에이전트 분석으로 계측 ("Agent development and AgentOps with BigQuery, ADK, and MCP") | **DX→AX**† — 결제→Kafka→알림은 정형 파이프라인(DX), 에이전트 데이터 분석이 자율 요소나 프로덕션 전 |
| Ulta Beauty / Flex / HCL Tech | 엔터프라이즈 패널 | "AI는 성과가 아니라 enabler, outcome-first" (Ulta), 공장 데이터 통합 에이전트(Flex, 100+ 공장 30개국, HCLTech 구현) | HCLTech×Omdia 조사 인용: "주요 AI 이니셔티브 43%가 실패 예상 — 분석가 아닌 실행 당사자 응답" ("Building enterprise-grade AI agents") | **DX(AX 표방)**† — 실체는 공장 데이터 통합(정형 파이프라인), 자율 판단 근거 미제시인데 '에이전트'로 명명 |
| (자사) Google | 플랫폼 규모 지표 | I/O 2026: 월 처리 토큰 2년 전 9.7조→작년 I/O 480조(자막 훼손 가능), API 분당 약 190억 토큰, 최근 12개월 1조+ 토큰 처리 고객 375곳+, Gemini 앱 MAU 4억→9억 | "토큰 맥싱이란 비판도 일리 있다"고 자인하면서 토큰을 채택 지표로 고수 (Sundar Pichai Opening Remarks) | **AX**† — 전환 사례가 아닌 AX 인프라 규모 지표, 판정 대상으로는 부적합에 가까움 |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 분모 스왑의 실시간 실연 | "80% speedup" 편: 1시간 내 문제 해결 챌린지가 UI 버그 미해결로 타이머 0에 실패하자, 즉석에서 "계측 도입·80% 단축·Cloud Run 배포 — 사실상 3:1 승리"로 성공 지표를 재정의 | AX 담론의 성과 서사가 목표 실패 순간 분모(평가 기준)를 바꿔 생존하는 메커니즘의 가장 선명한 단일 표본. 벤더 발표 수치 해석 시 '원래 목표' 복원 필수 |
| 오류 복리 → 컨텍스트 락인 | 95%³≈86% 논리로 context rot를 신규 리스크로 규정한 뒤, 해법을 자사 관리형 제품(Memory Bank·세션 서비스·Agent Engine)으로 유도 | 문제 정의와 해법 판매의 수직 통합. '기억'이 플랫폼에 축적될수록 전환 비용 상승 — 메모리가 새로운 데이터 중력 |
| 에이전트=인력 프레임 | PayPal "재입사한 인턴", AT&T "인간 판매원 tenure 12개월 미만 vs AI는 장기근속·전 카탈로그 숙지" | 에이전트 도입 논리가 기능 자동화가 아니라 이직·온보딩·교육이라는 **인력 비용 구조** 직접 대체로 이동. K1(인건비 종속변수) 프레임과 직결 |
| 거버넌스 지점 점거 | Agent Registry의 3대 명시 가치에 거버넌스·감사 포함, 에이전트 정책·Carrefour식 최종사용자 자격증명 실행 | 멀티에이전트 시대 통제 평면(레지스트리·정책·감사로그)을 선점하는 쪽이 락인 획득 — 프로토콜(A2A)은 열고 등록소는 자사화하는 이중 전략 |
| HITL의 단계적 후퇴 설계 | Home Depot "아직 인간 검증 필요, 자동 PR은 목표", PayPal 읽기전용→허용목록→변이 에이전트 순 권한 확대 | 감독 축소가 로드맵으로 명문화됨. '현재 HITL'은 상태가 아니라 이행기 — 연구 시 시점 명기 필요 |
| shift-down 신조어 | MediaMarkt: shift-left를 넘어 복잡성 자체를 플랫폼·에이전트로 내려보내는 "shift down" | 탈숙련화(deskilling)의 긍정 재명명. 온보딩 단축 수치가 곧 개인 숙련의 조직 자산화(스킬 파일)를 의미 |

**AX/DX 스펙트럼**: AT&T·PayPal 두 건만 에이전트가 판단·실행까지 맡는 확실한 AX이고, 나머지는 텔레메트리·스킬·파이프라인 등 DX 기반 위에 AI 판단을 얹어가는 DX→AX 이행 구간에 몰려 있다(HITL 후퇴가 로드맵으로 명문화된 것이 이행의 증거). 전 소스가 자사·공동 마케팅 채널이라 Flex/HCL처럼 정형 데이터 통합을 '에이전트'로 부르는 워싱 위험이 상존한다.

※ **신뢰 경계**: 전 소스가 구글 자사 채널이며 고객 수치(20분→2분, 50~60%, 130 스킬, 온보딩 단축)는 모두 고객 자사 발화·공동 마케팅 세션 기준으로 제3자 감사 없음("we've done the math" 수준). Google_Cloud_Tech는 제품 마케팅 성격이 강해 워싱 위험 상단. 자막 자동번역 훼손 실측: Antigravity→"반중력", agent→"상담원/중개인", dog walker agent가 한 영상 안에서 "의료 종사자/문서 작업자/주식 중개인/경매 대리인"으로 제각각 치환됨 — 고유명사·수치 인용 시 원문 대조 필수. 키노트 토큰 지표(9.7조→480조 등)는 자막 숫자 훼손 가능성 표기.

---

# Microsoft · GitHub(코파일럿과 원가 거버넌스) — AI Transformation 사례집
> **대표 세션/이벤트**: Microsoft Build 2026(Satya Nadella×Jensen Huang "unmetered intelligence" 대담), GitHub Octoverse 2025(Tim Rogers), WorkLab 팟캐스트(Molly Wood 진행), The Shift Podcast(Microsoft Azure), GitHub Checkout·The Download 시리즈, GitHub Universe 2026(10월 예고) | **관련 채널**: Microsoft, Microsoft_Azure, Microsoft_Developer, GitHub | **코퍼스 근거**: 실질 정독 19편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Copilot AI 크레딧·비용 센터 | 과금 거버넌스 | 엔터프라이즈 팀→비용 센터 매핑(IdP 그룹 자동 동기화), 크레딧 풀에서 비용 센터별 지출 한도+1인당 예산(예시 월 $50) 부과, 개별 재정의 요청 가능, "잔여가 가장 적은 예산이 우선" 규칙 | AI 사용량을 부서 단위 원가로 계량 — 토큰이 재무 관리 객체(FinOps)로 편입 |
| 모델별 크레딧 단가표(Kimi K2.7 Code) | 과금 | 입력 100만 토큰=95크레딧, 출력 100만 토큰=400크레딧, 1크레딧≈1센트, 캐시 히트율 95%(자막은 "현금 적중률"로 오역). Copilot 최초 오픈웨이트 모델, 미국 내 MS AI Foundry 인프라 호스팅, 기본 비활성(관리자가 켜야 함) | 모델 선택이 곧 단가 선택이 되는 구조. 오픈웨이트조차 자사 인프라·거버넌스 안에서만 제공(락인) |
| Copilot Auto 모델 라우팅 | 오케스트레이션 | 작업 복잡도·추론/도구/디버깅 요구로 모델 순위화+지연·용량·오류 실시간 재랭킹. **라우팅은 세션 시작 시와 컨텍스트 압축 후에만** — 매 요청 분류 시 "캐시가 삭제돼 오히려 비용 증가"라고 명시. 쉬운 작업→Claude Haiku 4.5, 리팩토링→Sonnet 4.6 시연 | Auto 사용 모델 전량 10% 크레딧 할인. "최적 모델 일관 사용이 단일 모델보다 비용↓·성능↑"(일부 작업은 작은 모델만 해결) |
| Agentic Workflows | 자동화+가드레일 | 마크다운(영어 문서+frontmatter)을 컴파일러가 GitHub Actions 워크플로로 변환. `safe-outputs`로 산출 제한(예: PR 1개만 생성), 도구·접근 도메인 화이트리스트를 **"에이전트 루프 외부에서 강제"**("에이전트와 인터넷 사이 방화벽" 비유) | 프롬프트 준수가 아닌 실행계층 강제로 안전 확보. 의존성 업그레이드·이슈 트리아지·CI 닥터 등 유지보수 노동 자동화 |
| Copilot 코드 리뷰 medium depth | 품질 | 복잡 로직·보안 민감 코드·서비스 간 변경 PR을 상위 추론 모델로 라우팅, 조직 관리자가 기본 리뷰 수준 설정 | 심층 리뷰는 "더 많은 AI 크레딧 소모" 명시(깊이=가격). 일반 문제 해결률 70%+ 주장 |
| Copilot Cloud Agent | 클라우드 에이전트 | PR 즉시 생성 폐지→비공개 협업 후 개발자가 PR 시점 결정, 머지 컨플릭트 자동 해결, 자체 개발환경에서 빌드·테스트·린트 후 푸시, CI 실행 전 인간 승인 기본값(옵트아웃 가능) | "자동 병합 없음" — 속도보다 개발자 통제 우선. 다중 에이전트 병렬화로 충돌 자체가 늘었음을 자인 |
| Copilot SDK·BYOK | 플랫폼 개방 | SDK 5개 언어(프로덕션 동일 런타임), 구독자는 프리미엄 요청 할당량 차감. BYOK로 GitHub 라우팅 우회, Ollama/vLLM/Foundry Local 등 로컬 실행·완전 오프라인 모드 지원(권장 컨텍스트 120k 토큰+) | 과금 경로의 이원화: GitHub 크레딧 경제 안 또는 자기 인프라 비용으로 탈출 — 단 하네스는 GitHub 것 |
| Azure AI Foundry 모델 관리 | 인프라 | "차량(플릿) 관리" 프레임. 처리량 **6단계 티어를 사용 추이 감지 후 선제·자동 상향**. 데이터 상주 3단(글로벌>데이터존>지역 — 지역이 최고가·최저 처리량). 성능 3티어: priority(SLA 지연 보장·할증)/standard/batch(약 24시간·대폭 할인) | "높은 데서 시작해 필요할 때만 내려가라" — 의사결정 자체를 추상화해 소비 마찰 제거 |
| Foundry 프로비저닝+스필오버 | 인프라 | 시간당 과금 프로비저닝(처리량·지연 SLA 보장)과 종량제 priority를 결합 — **할당 용량 소진·수요 변동 시 다른 배포로 전환**해 속도 제한 없이 유지 | "전 세계에 수요 충족할 GPU·CPU가 없다"는 공급 제약을 티어·할인·스필오버라는 가격 상품으로 변환 |
| Dataverse 플러그인+비즈니스 스킬 | 엔터프라이즈 데이터 | 최상위 `DV-overview` 스킬이 요청을 6개 하위 스킬(연결·모델링 등)로 **라우팅**, MCP 서버·PAC CLI·Python SDK 중 최적 도구 선택. 결정론적 Python 스크립트를 산출해 소스 관리에 커밋 가능, 고객이 자체 skill 파일로 사내 표준 주입 | "SaaS 종말론은 과장, 기록 시스템→에이전트 시스템"으로 기존 자산 방어. 개발자·분석가·관리자 3페르소나 통합(민주화=탈숙련 경로) |
| Azure Copilot(에이전틱 운영)·SRE 에이전트 | 운영 | 사용자 권한만 상속(권한 초과 불가), 실행 전 일시정지·인간 승인, 추론 과정·증거 전량 기록, BYO 스토리지에 감사로그 보관(보존기간 설정) | 사후 대응→선제 운영 전환, "인지 부담 감소·고된 작업 제거" — 단 온콜은 유지된다고 자인 |
| RTX Spark·"unmetered intelligence" | 엣지 | 1페타플롭(NVFP4)·128GB 통합 메모리로 수천억(약 2,000억) 파라미터 모델을 데스크톱 로컬 실행, PC가 자율 에이전트 실행 주체로 | 토큰 미터링 없는 엣지 지능 — 클라우드 크레딧 계량과 정반대 서사를 동일 진영이 병행 판매 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| NVIDIA | 인프라 공동설계 | Fairwater 데이터센터를 Grace Blackwell 전용 설계(완전 수랭·폐쇄 루프), Vera Rubin은 "에이전트 실행용" CPU/시스템, Fabric·SQL·Spark GPU 가속 | 토큰 생성 비용 Hopper 대비 약 30배 절감, GitHub 커밋 수 최근 수개월 3배("parabolic"), "토큰은 이제 수익성이 있다"(Jensen Huang, Build 2026) | DX — 인프라 최적화, AI의 자율 판단 없음 |
| EY | 컨설팅 AX(Frontier Firm) | EY.ai 조직 신설, 전 직원 AI 커리큘럼, Client Zero 프로그램, 빌러블 아워(노력 기반 과금) 해체 선언, Harvard D^3 Frontier Firm 이니셔티브 참여 | 인력 40만 명, 작년 AI 준비에 자본 10억 달러+ 투자. 직원 85% "에이전틱 AI 기대" vs 86% "혼자 독학". "내년 입사자는 1일차부터 (에이전트) 관리자"(Dan Diasio, WorkLab) | AX† — 과금·역할 재정의 선언은 AX, 실행 증거는 미검증 |
| Moonshot AI(Kimi) | 모델 공급 | Kimi K2.7 Code를 Copilot 라인업에 오픈웨이트 최초 편입, MS·GitHub가 미국 Foundry 인프라에서 직접 호스팅·관리 | 라인업 최저가·최속(첫 토큰 시간)급, 캐시 히트율 95% 주장. 요구사항 문서에 8개 확인 질문 후 자율 구현 시연(자사 내부 테스트 기준) | DX→AX† — 공급 자체는 DX, 자율 구현 시연은 AX 요소(자사 시연 한정) |
| Anthropic | 모델 공급 | Auto 라우팅의 실연 모델(Haiku 4.5/Sonnet 4.6), Claude 신모델을 Copilot에 동시 탑재. 안전 분류기용 프롬프트·출력 30일 보존 조건 명시 | 신형 최상위 모델 API 가격 입력 $10/출력 $50(100만 토큰당, 기존 Opus급의 2배) — 단 모델명 표기 자막 훼손 심각(가격 수치도 자막 훼손 가능). GitHub 자체 벤치마크 "더 적은 도구 호출·토큰으로 동일 작업" (The Download) | DX→AX — Auto 라우팅이 작업 복잡도를 판단해 모델 분기(단 캐시 제약으로 판단 빈도 제한) |
| Home Assistant(관리자 Frank) | Agentic Workflows 초기 테스터 | 버그 리포트 스택트레이스가 자사 코드에서 끝나는지 판별→자사 버그면 수정 PR 자동 생성하는 워크플로 구축 | GitHub "가장 바쁜 오픈소스 프로젝트 중 하나"의 트리아지 노동 자동화 사례(정량 수치 없음) (GitHub Checkout) | AX — AI가 스스로 판별·분기 후 PR 생성까지 실행 |
| Wolters Kluwer | Azure 규제 워크로드 | 세무·회계 순환 피크(1/15·3/15·4/15)를 AKS 자동 확장으로 흡수, CCH Access Scan(무개입 세금신고서 작성)을 Azure AI Content Understanding+Azure OpenAI로 구현 | "전문가 워크플로에 내장(embedded), 덧붙임(bolted-on) 아님" — 정량 성과 미공개 (Microsoft Azure 채널) | DX→AX — 클라우드 자동확장(DX) 위에 무개입 AI 신고서 작성(AX) 결합 |
| Blue Tulip Ventures/Affectiva(Rana El Kaliouby) | 담론 파트너(WorkLab 게스트) | 감정 AI 상용화 경험 기반 "인간 중심 AI" 투자론, 자사 펀드에 AI 비서 에이전트("Blue") 훈련 | Affectiva 시절 "Fortune 500 절반이 사용" 주장. 핵심 발화: "코딩·협업 플랫폼은 60~70%까지 가지만 나머지 30%가 진짜 노동", **"망가진 워크플로에 AI를 얹으면 실패한다"** | DX(AX 표방)† — 담론 중심, 에이전트("Blue")의 자율화 실증 없음 |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 크레딧=사내 통화, AX의 회계화 | 토큰을 "1크레딧≈1센트"로 환산해 비용 센터·1인당 월 한도·재정의 요청까지 갖춘 예산 체계로 내림. 코드 리뷰 "깊이"조차 크레딧 단가로 차등화 | AX 거버넌스가 기술 문제에서 **재무 관리 언어**로 이동. "에이전트=인력" 프레임(EY "1일차 관리자")과 결합하면 에이전트 인건비 회계가 성립 — 거버넌스 락인의 신형태 |
| 캐시가 아키텍처를 결정 | Auto가 매 요청 라우팅을 포기한 이유는 품질이 아니라 **모델 전환 시 캐시 파기→비용 증가**. 라우팅 빈도 자체가 원가 최적화 산물 | 프롬프트 캐시 경제가 시스템 설계의 1차 제약이 된 실증. "작은 모델만 푸는 작업 존재"는 프론티어 단일모델 신화에 대한 자사발 반례 |
| 가드레일은 루프 밖에 | safe-outputs·도구 화이트리스트는 에이전트 루프 외부(컴파일러·실행계층)에서 강제, Cloud Agent는 CI 승인 기본값·자동 병합 없음, Azure Copilot은 사용자 권한 상속+HITL | HITL 담론의 기술적 구현 표준화. "속도는 신뢰할 때만 의미" — 통제권 서사가 엔터프라이즈 세일즈의 전제조건임을 보여줌 |
| 희소성의 상품화 | "전 세계 GPU가 수요에 부족"(Foundry 책임자 직접 발언)을 6단계 티어·priority 할증·batch 24시간 할인·프로비저닝+스필오버로 가격표화. 지역 데이터 상주=최고가 | 공급 제약이 가격 차별화 상품이 되고, 데이터 주권은 **프리미엄 옵션**으로 판매됨 — 소버린 담론의 원가 번역 |
| 계량 vs 비계량의 양면 전략 | 클라우드에선 크레딧 미터링을 정교화하면서, 엣지에선 "unmetered intelligence"(RTX Spark 로컬 2,000억 파라미터)와 BYOK/오프라인 모드를 동시 판매 | "분모 바꾸기"의 플랫폼판: 어느 쪽이든 하네스(Copilot SDK·Windows·Foundry)는 자사 소유 — 과금 방식은 바뀌어도 종속 지점은 유지 |
| 반워싱 담론의 내재화 | 자사 채널에서 "망가진 워크플로에 AI 얹으면 실패"(El Kaliouby), "AI는 바닥은 올리지만 천장은 못 올린다·산출물 동질화(matcha 일화)"(EY), "온콜은 안 사라진다"(Azure) 등 자기절제 발화 배치 | 실패담·한계 인정이 오히려 도입 정당화 장치("그러니 워크플로 재설계=우리 컨설팅/플랫폼 필요")로 기능 — 반워싱 수사의 세일즈 편입 사례 |

**AX/DX 스펙트럼**: 이 클러스터는 DX→AX 이행대에 몰려 있다 — 인프라·과금 정비(DX)를 깔고 그 위에 Auto 라우팅·Agentic Workflows·무개입 문서처리 같은 자율 판단(AX)을 얹는 구조이며, 순수 AX 실증은 Home Assistant 트리아지 정도다. 수치가 전부 자사 발화이고 EY·Affectiva처럼 선언·담론이 실증을 앞서는 행은 워싱 위험을 †로 표시했다.

※ **신뢰 경계**: 본 클러스터 수치는 전부 자사(Microsoft/GitHub) 채널 발화이며 고객 사례도 자사 편집 콘텐츠(Wolters Kluwer 등은 정량 성과 부재). 커밋 3배·해결률 70%·캐시 95% 등은 독립 검증 불가. 한국어 자동자막 오염이 특히 심함: Auto→"자동차", agent→"상담원", Copilot→"부조종사", cache hit→"현금 적중률", 도메인명사→"음악"(Wolters Kluwer 편은 "세무 산업"이 "음악 산업"으로 치환), 모델명 오기(Kimi→Kimmy, 신형 Claude 모델명·가격 관련 표기 훼손 — 해당 수치는 자막 훼손 가능 표기). WorkLab 2편과 Build 대담은 영어 자막이라 인용 신뢰도가 상대적으로 높음. GitHub The Download의 타사 소식(Anthropic 보안 프로젝트 등)은 전언 보도로 별도 취급 필요.

---

# OpenAI · Anthropic(파운데이션 모델의 위임 담론) — AI Transformation 사례집
> **대표 세션/이벤트**: Claude for Financial Services Keynote(2025.7, NY) · MCP 리눅스재단 기증 발표(2025.12) · Project Glasswing 공개(2026.4) · OpenAI Codex 릴리스 데모·Build Week(2026.7) · ChatGPT Work 레퍼런스 고객 시리즈(2026.7) · 오픈AI×무신사 비공개 행사(2026.7, 키워드 수집분) | **관련 채널**: OpenAI, Anthropic(+제3자 후기 1편) | **코퍼스 근거**: 실질 정독 15편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Codex + GPT-5.6 "Soul"/Ultra(자막 표기) | OpenAI 코딩 에이전트 | 자연어 목표(/goal)만 주면 서브에이전트 자동 분배·브라우저/시뮬레이터 직접 조작·PR 병합까지 수행. Sites로 호스팅·인증·DB 내장 배포 | 주간 사용자 300만→400만(2주, 무신사 행사 발화)·자사 영상은 "매주 600만+"(자막상 'Coda', 훼손 가능). 2개월간 150+ 업데이트 |
| ChatGPT Work | OpenAI 기업 제품 | 사내 데이터·에이전트·Codex를 단일 업무 공간으로 통합 | 간증 포맷: "1인이 4~5인 팀의 일"(주당 수백 건 콘텐츠), "몇 주→몇 시간" — 정량 검증치 부재 |
| 위임(delegation)·/goal 담론 | OpenAI 방법론 | "프롬프트를 멈추고 목표를 줘라. 모델은 high agency라 수단은 알아서 정한다"(Katia Gil Guzman, OpenAI France) | AI를 도구가 아닌 '위임 가능한 노동력'으로 재정의 — 도입 문제를 경영진 의지·채용 재설계로 이동 |
| Claude Code SDK | Anthropic 하네스 | 에이전트 루프·도구호출·파일시스템·MCP·프롬프트 캐싱을 기본 내장. "코딩 요소를 빼면 범용 에이전트 하네스"(공식 발화) | 개발자가 루프를 재발명하지 않고 상위 추상화에서 시작 — 에이전트 구축 진입장벽 제거 |
| MCP | 개방 프로토콜 | 모델↔외부 SW 연결 표준("USB-C"). 리눅스재단 산하 Agentic AI Foundation에 상표까지 기증(Google·MS·Amazon·Bloomberg·Block·Cloudflare 참여) | "락인 없음" 신호로 사실상 표준 장악. 컨텍스트 블로트는 tool search·programmatic tool calling으로 대응 |
| Skills | Anthropic 재사용 자산 | 지침+템플릿·스크립트·이미지 등 '자원'을 통째로 주입("매트릭스 쿵푸" 비유) | 반복 업무를 조직 자산화 — "Claude가 갑자기 뱅커가 된다" |
| workflows→agents→멀티에이전트 | Anthropic 아키텍처론 | 고정 체인(워크플로)→루프형 에이전트→'workflows of agents'→오케스트레이터가 서브에이전트 병렬 위임. Claude를 "더 나은 매니저"로 훈련 | 품질 우선 작업에서 에이전트가 워크플로를 압도, 컨텍스트 보호·병렬화로 속도 확보 |
| Claude for Financial Services | 도메인 수직화 | FactSet·S&P(Kensho)·Daloopa·Morningstar·PitchBook·Box 등 통합 조회→DCF·comps·투자메모 자동 생성 | 데모 기준 3~5시간 분석→30분 미만. Fundamental Labs 'Shortcut'은 재무모델링 월드컵 7레벨 중 5개 통과·정확도 83% |
| Glasswing 모델 | Anthropic 보안 이니셔티브 | 코딩 훈련의 부산물로 취약점 탐지·연쇄 익스플로잇 조합 능력 확보(모델명 자막상 "Claude 3 Opus Preview" — 훼손 가능). 비공개 운용 | OpenBSD 27년 묵은 원격 다운 버그·리눅스 권한상승 다수 발견→관리자 통보·패치. "몇 주간 찾은 버그가 평생 찾은 것보다 많다"(파트너 발화) |
| 해석가능성(Interpretability) | Anthropic 안전 연구 | 모델 내부 회로를 "AI 신경과학/생물학"으로 역공학 | "수십억 달러 관리엔 good enough로 부족"(키노트) — 안전 담론을 금융 영업 언어로 번역 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| BNY | ChatGPT/사내 플랫폼 | CEO Robin Vince가 사내 AI 플랫폼 "Eliza"로 하루 시작, "낙관을 행동으로" 톤 세팅 | 수치 전무 — CEO 실명 간증만(How BNY CEO Robin Vince Turns AI Optimism Into Action) | DX(AX 표방)† — 실명 간증뿐, 자율 판단·워크플로 재설계 근거 없음 |
| Shopify | ChatGPT Work·Codex | "가장 큰 변화는 위임에 익숙해지는 것" — 트리아지 워크플로를 에이전트로 재설계 | "대규모 팀→에이전트(자막 '상담원') 하나"(How Shopify Uses ChatGPT Work…) — 정량치 없음 | AX† — 워크플로 재설계·에이전트 위임 명시, 단 정량 근거 부재 |
| Virgin Atlantic | ChatGPT Work·Codex | 고객경험팀이 멀티소스 대시보드·리포트 자체 구축 | "몇 주 작업→몇 시간"(제목·발화), 수치 없음(How Virgin Atlantic Uses ChatGPT Work…) | DX→AX† — 산출물은 대시보드(DX)나 비개발자가 AI로 직접 구축(역할 재정의) |
| Verso(프랑스) | Codex | "Codex를 중심으로 회사를 구축" | 사례 언급만(Stop Prompting. Start Giving AI Goals.) | AX† — /goal 위임 담론의 예시이나 언급뿐, 실체 검증 불가 |
| 무신사 | Codex 엔터프라이즈 | CTO 전준일: 에반젤리스트 발굴→슬랙 '허브' 공유→부서 임베딩→탑다운 푸시. 채용도 AI 활용 문제해결 테스트로 전환(66명) | 연 4.5억 원 SaaS를 비개발 매니저 기획+개발자 3명·2개월에 내재화. Claude 엔터프라이즈 토큰 비용 ~5배 발언. "2026년 말 실리콘밸리 코드 80% AI 작성" 주장(제3자 후기 영상 — 전언·자막 훼손 가능) | DX→AX — SaaS 내재화(DX) 위에 AI 개발·채용/역할 재정의(AX 요소) |
| NBIM(노르웨이 국부펀드) | Claude 엔터프라이즈·MCP | $2조 운용·직원 700명. Snowflake 데이터에 Claude 연결, 약 9,000개 포트폴리오 기업 MCP 통합 자체 구축 | "생산성 20%↑ = 연 213,000시간 회수"(CEO Nicolai Tangen 인용, Financial Services Keynote) | DX→AX — 데이터 파이프라인(DX) 기반 위 MCP로 AI 판단 접속 |
| AIG | Claude 언더라이팅 | 인수심사 프로세스 재구상 | 소요기간 5배 이상 압축(주→일), 정확도 75%→90%(키노트 발화) | AX — 심사 판단 자체를 AI가 수행, 프로세스 재설계·정확도 지표 |
| Bridgewater | Claude | 2023년부터 투자 애널리스트 어시스턴트 구동 | 정량치 없음(키노트) | DX→AX† — 어시스턴트(보조) 수준, 자율 실행 근거 없음 |
| HG Capital | Claude 포트폴리오 전개 | 50개 B2B SaaS 포트폴리오사·12만 FTE에 중앙 AI팀(전문가 20명+계약자 150명)이 전환 이식 | SW엔지니어링 생산성 평균 30%↑, 개발 스쿼드 9명→2명, 한 회사는 에이전틱 SW엔지니어 1,000 인스턴스로 캐파 +50%. "비용 절감이 아니라 재투자" 명시(키노트 패널) | AX — 에이전틱 엔지니어 1,000 인스턴스·스쿼드 9→2, 인력 구조 재정의 |
| DE Shaw / New York Life | Claude 전사 배포 | 바텀업 확산(사용강도 로그노멀 분석·라이트닝 라운드) / "포트폴리오식" 전사 전략 | NYL: Fortune 69·보험계약 $1조 규모 언급, 성과 수치는 없음(키노트 패널) | DX→AX† — 전사 보급 단계, 자율화 실체는 미확인 |
| Commonwealth Bank | Claude | CTO가 "글로벌 AI 전략의 기반"으로 규정 | 수치 없음(키노트) | DX(AX 표방)† — 전략 선언만, 실행·자율화 근거 전무 |
| AbbVie | Claude 신약개발·문서화 | 임상문서 자동화 'Gaia'(NDA·PSUR), 영업 콜플래닝 'Genesis' | 문서 작성 시간 40~60% 절감(How AbbVie accelerates drug discovery…) | DX→AX† — 정형 규제문서 자동화(DX 성격) + AI 생성·콜플래닝 판단 요소 |
| Deloitte·KPMG·PwC·Slalom 등 | 컨설팅 생태계 | 에이전트 대규모 배포·레거시 COBOL 마이그레이션·규제 대응 | 역할 언급만 — 수치 없음(키노트) | DX→AX† — COBOL 마이그레이션(DX)을 에이전트로 수행하는 이행형, 검증 불가 |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 위임 = 에이전트의 인력화 | Shopify "팀→에이전트 하나", /goal 담론, 무신사 "개발비 0 수렴→유일 병목은 인간 상상력·PM" | '에이전트=헤드카운트' 프레임의 진원지. 탈숙련(deskilling)·유휴인력 문제(무신사 CTO의 "고과 정렬→도태→한직" 진술)와 동전의 양면 — K1 인건비 종속변수 직결 |
| 하네스·프로토콜 선점 | Claude Code SDK="범용 하네스", MCP는 상표까지 기증해 표준화 | '락인 없음'을 신호하는 개방 자체가 생태계 점거 전략 — 거버넌스 락인의 세련된 형태. 경쟁사(Google)도 Claude Code를 흡수 구동 |
| 레퍼런스 간증의 이중 구조 | OpenAI: 실명 CEO(BNY·Shopify·Virgin)+수치 부재. Anthropic: 자사 키노트에서만 수치(NBIM 20%·AIG 75→90%) 공개 | "권위 있는 실명+검증 불가 수치"가 워싱 방어 장치로 기능 — 제3자 감사 없는 벤더 발화라는 점은 동일 |
| 토큰 경제 = 새 원가 경쟁 | 무신사: Claude 토큰 ~5배 비용, 월급보다 비싼 헤비유저 발생. OpenAI는 "GPU 풍부·토큰 저렴" 서사로 대응 | AX 원가의 분모가 인건비→토큰비로 이동. '가성비 토큰'이 벤더 선택 기준으로 부상 |
| 안전이 영업 언어가 되다 | Glasswing(방어자 우위·모델 비공개·美 정부 협의), 해석가능성 연구를 "수십억 관리엔 필수 신뢰"로 번역 | Anthropic의 안전 코뮤니케이션은 규제산업(금융·제약) 진입 자산이자 차별화 — 안전=비용이 아닌 안전=매출 프레임 |
| HITL의 조직화 | 탑다운("AI 매니악" CEO 톤 세팅)+바텀업(에반젤리스트·해커톤·6개월 재방문 룰), HG "비용 절감 아닌 재투자" 화법 | 도입 실패를 기술이 아닌 경영진 의지 문제로 귀속 — 해고 서사를 회피하는 '재배치·재투자' 수사가 표준화 |

**AX/DX 스펙트럼**: 벤더 자사 담론 클러스터답게 AX 확정(AIG·HG)보다 DX→AX 이행·판정 유보(†)가 다수이며, 정량 근거 없는 실명 간증형(BNY·Commonwealth)은 AX 워싱 위험이 가장 크다. "위임/goal" 담론 자체가 AX 서사를 앞세우지만, 사례 실체는 대시보드 구축·문서 자동화·마이그레이션 등 DX 기반 위의 이행 단계에 몰려 있다.

※ **신뢰 경계**: 본 클러스터의 수치는 전량 벤더 자사 발화 또는 자사 주최 행사 발화(NBIM·AIG·HG 수치 포함)로 제3자 검증 없음. 무신사 건은 참석 인플루언서의 전언이라 이중 간접 인용. 자막 자동번역 오염 심각 — BNY "음악 분야 AI 리더십팀"(원문 소실), agent→"상담원", Codex→"Coda", 도메인명사→"음악" 치환 다수. "GPT-5.6 Soul", "Claude 3 Opus Preview"(2026.4 영상) 등 모델명과 Codex 사용자 수(300만→400만 vs 600만+)는 자막 훼손 가능성을 전제로 인용할 것. "실리콘밸리 코드 80%(2026말)·100%(2027말)" 류 예측은 발화자 주장이며 근거 미제시.

---

# Palantir · ServiceNow · Oracle(데이터·거버넌스 계층) — AI Transformation 사례집
> **대표 세션/이벤트**: Palantir AIPCon 6~8·Paragon 2025·"Chad &" 아키텍트 시리즈·UK Stories(NHS/Hadean) | ServiceNow Knowledge 2026 오프닝·Day 2 키노트·Michael Park Whiteboard Masterclass/2.0·Zurich 릴리스 | Oracle at Gartner CSO·Defence Tech Summit 2026(브뤼셀) Oracle TV·AI Changes Everything 팟캐스트 | **관련 채널**: Palantir, ServiceNow, Oracle | **코퍼스 근거**: 실질 정독 17편(전문 완독 9·표적 심층발췌 8)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| 온톨로지 프리미티브 도구화 (Palantir AIP Logic) | 에이전트 기반층 | 온톨로지의 Object Query Tool(맥락 조회)·Action Tool(인간과 동일한 실행 액션)·Function Tool(예: 재고 재배치 시나리오 모델)을 LLM에 도구로 그대로 서빙. "AI용 추가 설정 없이" 인간·에이전트가 같은 프리미티브 공유 | 자동화를 "다이얼"로 조절, 주문 수백~수천 건/분 병렬 처리, "무한히 확장 가능한 AI 노동(AI labor)" 선언(AIPCon 6) |
| AIP Evals + Feedback Workbench | 평가·거버넌스 | 썸업/다운→온톨로지 정의 라벨→비정형 피드백→테스트케이스 승격(4단계 상태머신)→LLM-as-judge 채점→에이전트가 실패 분석·프롬프트 수정안 생성→모델×프롬프트 그리드서치 "실험" | 시연에서 GPT-4.1+구조화 체크리스트 프롬프트로 정확도 0%→50%; "이것 없으면 장난감(toy)", 규제산업 감사 대응 = "우리가 이기는 이유" |
| Foundry 기반 NHS FDP | 데이터 주권층 | 트러스트별 분리 인스턴스+일관된 임상데이터모델(CDM)+목적 기반 액세스 제어(purpose-based access control)로 극장(수술실)·인력·환자 시스템 연결 | 7~8개 시스템 로그인→단일 화면; 데이터가 주권 조직을 떠나지 않는 설계 자체가 공공 조달 통과 장치 |
| Workflow Data Fabric (ServiceNow) | 데이터층 | 제로카피(Snowflake·Databricks, Oracle·GCP 예정)+비정형 인덱싱+RaptorDB 컬럼스토어로 이동 없는 읽기·쓰기 연결 | 쿼리 성능 5~10배(자사), "타사처럼 데이터를 다 가져오라 하지 않는다"는 반(反)이동 원가 담론 |
| Context Graph/컨텍스트 엔진 | 맥락층 | "그래프들의 그래프": 지식·행동·접근·자산·의사결정 그래프를 CMDB 위에 통합, 시맨틱 레이어로 에이전트에게 "데이터를 어디서 가져올지" 내비게이션 제공 | 연 1,000억 워크플로 실행 이력이 그래프를 강화 — 사용할수록 깊어지는 락인 구조 |
| Action Fabric | 실행층 | 외부 AI(Gemini, Azure AI 등)가 REST/MCP/A2A로 ServiceNow 런타임(워크플로·승인·SLA·감사추적·컴플라이언스)을 호출 | "어디서 만들든 실행은 우리 거버넌스 통과" — 타사 모델까지 자사 계층에 종속 |
| AI Control Tower | 거버넌스층 | IRM+SPM을 결합해 전사 AI 자산(타사 LLM 포함)을 데이터 모델에 등록·발견·위험관리·성과측정; Microsoft Agent 365 통합 | FedEx급 고객이 "타 조직 95%가 못하는 AI 투자가치 측정" 수행(자사 발화) |
| 머신·에이전트 아이덴티티 (Veza 인수; 자막 'Vissa/Vera') | 신원·보안층 | 인간·비인간·AI 에이전트의 액세스 그래프(약 1,200억 권한 — Day2 발화; 오프닝 키노트는 300억+, 편차)로 작업 시점 최소권한 부여 | "모든 LLM·코파일럿·에이전트는 신원과 권한이 필요" — 에이전트를 인력처럼 IAM 관리 |
| AI 전문가(AI Experts)·오케스트레이터·Auto | 노동 대체층 | 역할 단위 자율 인력(ITSM 등), Moveworks 통합 대화형 관문 "Auto", 슈퍼에이전트가 계획 수립·순차 실행 | 자사 헬프데스크 "사람보다 99% 빠른 해결"; DocuSign·Honeywell 대부분 요청 자동 차단(자사 발화) |
| Oracle 에이전틱 영업 앱 | 응용층 | signal(로이터 뉴스·제안서 열람·ERP 갱신일 등 신호 수신)→context(영업전략과 결합해 맥락화)→action(견적·지역계획·프레젠테이션 생성)+전 과정 거버넌스·출처 기록 | "그게 없으면 강화된 ChatGPT일 뿐" — 거버넌스를 차별화 본체로 규정 |
| Oracle 주권 클라우드·디펜스 에코시스템 | 인프라·지정학층 | 에어갭 환경과 동일한 OCI 스택, Raven 엣지 디바이스, 중소 방산기업-대형 고객 중개 생태계 | "인간은 기술처럼 확장되지 않는다"; 주권을 서방 가치체계 수호로 정의(Rand Waldron) |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| NHS (Palantir) | 의료 데이터 플랫폼 | FDP로 사일로 시스템 통합, 수술실 일정 제품 약 3주 만에 구축·현장 테스트 | 작업 4분→30초, 환자 평균 약 40일(최대 2~3개월) 조기 진료, 트러스트당 월 120건+·누적 8만 건+ 추가 시술 (Palantir and the NHS \| UK Stories) | DX |
| Hadean (Palantir) | 국방 C2·시뮬레이션 | Foundry 위에 Domini AI(차세대 지휘통제) 구축, 시뮬레이션이 실운영 체계와 "같은 언어" 사용 | MOD 3개월 조달 주기 약속의 수혜 사례; 영국 직원 비중 1/6+, 영국=유럽 방위 본부 합의 (Palantir and Hadean \| UK Stories) | DX† |
| 익명 조달 고객군 (Palantir) | 조달 자동화 | 인보이스-계약 대사, RFQ 자동화 | 대상 지출의 연 1~10% 절감, 일부 고객 "3년 30%" 주장; 건설사 RFQ 발행 시간 절반 (Chad & Agathe \| Procurement) | DX† |
| FedEx (ServiceNow) | 공급망·AI 거버넌스 | 2020년~ 디지털 트윈, AI Control Tower로 전 벤더 AI 자산 관리, 공동 공급망 솔루션 출시 | 연 약 2조 달러 상거래·일 2PB 데이터·화주 300만·소비자 2.25억(자사 발화); "공급망 비효율 1.8조 달러" 시장 프레임 (Knowledge 2026 오프닝) | DX† |
| DocuSign·Honeywell (ServiceNow) | ITSM AI 전문가 | 역할 단위 자율 에이전트 도입 | "대부분의 요청 차단, 몇 초 만에 해결"(수치 미제시, 자사 발화) (Knowledge 2026 오프닝) | AX† |
| CNA 보험 (ServiceNow) | 리스크 평가 | 900+ 앱 포트폴리오의 위험 평가 자동화 | 연 50개 시스템 평가→그 이상으로 확대 (How CNA unified risk…) | DX† |
| Motorola Solutions (Oracle) | CPQ·에이전틱 제안서 | ①프로세스 정렬 ②Customer Data Hub(2021) 단일 고객 뷰 ③인사이트→행동(견적 옵션 자동 생성) 3단계 | CPQ 도입률 8년간 33%→99%(주문 99% CPQ 경유), 에이전틱 제안서 센터로 RFP 응답 약 50% 단축 (Oracle at Gartner CSO) | DX→AX |
| Ricoh (Oracle) | 영업 AI | 서비스기업 전환 중 플랫폼 내장 AI 배포+데이터 품질 기반 정비 병행 | 초기 단계; "정렬 안 된 시스템에 AI 얹으면 신뢰 못 얻는다" 증언 (Gartner CSO) | DX |
| Oracle 북미 영업(자사) | 에이전틱 영업 앱 | 영업 담당자 전면 배포 | 400명 파일럿→신 회계연도 1만 명 확대 예정 (Gartner CSO) | AX |
| Whitespace (Oracle) | 국방 의사결정 AI | 영국 육군 Asgard 디지털 표적 웹 참여, 에코시스템(Esri·Janes·Mattermost 등)과 엔드투엔드 데모 약 6주 구축 | Prince of Wales 항공모함 Raven 엣지에 초단기 AI 배치; "데이터는 왔다 사라진다, 결국 결정" (Whitespace on Sovereign AI) | DX→AX† |
| Oracle Red Bull Racing | 레이스 전략 | OCI로 몬테카를로 시뮬레이션 컴퓨팅 한계 완화, 레이스 중 시뮬레이션 확대→학습 기반 접근으로 진화 중 | 구체 수치 미제시; 고압 상황 인간 판단 유지 강조 (AI Changes Everything: Red Bull) | DX |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 진짜 락인=거버넌스 계층 | 3사 모두 모델을 커머디티로 격하("models are commodity here" — Palantir Evals 회; ServiceNow "어떤 LLM이든 가져오라"; Oracle "강화된 ChatGPT" 비판)하고, 온톨로지/컨텍스트그래프+권한그래프/거버넌스 기록을 대체 불가 자산으로 배치 | AX 락인의 본진은 모델이 아니라 컨텍스트·거버넌스 계층 — "온톨로지 land-grab" 명제의 최강 근거 클러스터 |
| 평가(Evals)가 새 운영비 | 피드백→라벨→테스트케이스→LLM-judge→프롬프트 실험의 상시 루프가 "프로토타입→프로덕션" 전환의 실체. 0%→50%라는 수치 자체가 '반복 개선이 기본값'임을 증언 | 에이전트 도입 원가에 평가·회귀 인프라 상시 비용이 가산됨 — 비용구조 연구에서 은폐되기 쉬운 항목 |
| 에이전트=인력 프레임의 완성형 | Palantir "신입사원 훈련" 은유·"무한 확장 AI 노동"; ServiceNow AI 전문가(역할 전체 수행)+에이전트 신원·최소권한(IAM); 거버넌스가 곧 인사관리로 번역됨 | "에이전트=인력" 담론이 채용(온보딩)-권한(IAM)-평가(Evals)-감사(Control Tower)의 완결된 노무관리 어휘를 획득 |
| 분모 바꾸기의 플랫폼 버전 | ServiceNow는 고객가치 대신 "one platform→higher operating cash flow margin", 연 1,000억 워크플로·7조 액션·Fortune 500의 90% 규모를 정당화 근거로 제시 | 전환 성과의 분모가 '업무 성과'에서 '플랫폼 통과량·마진'으로 이동 — 워싱 판별 지표로 활용 가능 |
| 주권·조달=거버넌스 락인의 국가 버전 | NHS 목적기반 접근제어, MOD 3개월 조달, Oracle "정치보다 깊은 가치체계" — 규제 통과 설계 자체가 판매 장치 | 공공 AX에서 락인은 기술이 아니라 조달·주권 요건 충족 능력으로 발생; 서방 블록 담론과 결합 |
| HITL의 제품화 | Palantir "AI가 평범한 일, 인간은 비범한 일"+유저 액션 플래그; Oracle "신뢰하되 검증, AI를 유일한 답으로 받아들이는 게 걱정" | 인간 개입 지점이 윤리 장치가 아니라 거버넌스 계층의 유료 기능으로 재포장되는 경향 |

**AX/DX 스펙트럼**: 이 클러스터는 데이터 통합·거버넌스 인프라 구축이 본체라 대다수가 DX(NHS·FDP, Data Fabric, Control Tower)에 몰려 있고, AX는 에이전틱 영업 앱(Oracle 자사)과 Motorola의 DX→AX 이행처럼 정렬된 DX 기반 위에서만 등장한다. ServiceNow의 "자율 AI 전문가" 주장(DocuSign·Honeywell)은 수치 미제시 자사 발화로 워싱 위험이 가장 크다.

※ **신뢰 경계**: 본 클러스터 수치는 전량 벤더 자사 채널·자사 무대 발화(고객 등판 포함)로 제3자 검증 없음. ServiceNow는 규모 과시·인수 통합 서사가 강해 워싱 위험 최고 채널(연 1,000억 워크플로 등은 자사 집계). 자막 자동번역 오류 다수: Veza→"Vissa/Vera/Visa", Hadean→"하디안/Haydn/Hayden", FDP→"FTP", theatre(수술실)→"극장", AI Control Tower 홍보영상의 "[음악]" 삽입·"음악적 가치" 치환. Veza 권한 수는 300억(오프닝)/1,200억(Day 2)로 발화 간 편차(자막 훼손 가능). Oracle "AI Changes Everything"은 팟캐스트 형식으로 외부 게스트 견해 포함(80% 파일럿 실패율 등은 게스트 발화이며 오라클 공식 입장 아님). Palantir 재고·관세 데모(Onyx Inc., $88K 절감 등)는 가상 기업 시연 수치임.

---

# Databricks · Snowflake · 벡터DB · W&B(데이터/ML 인프라) — AI Transformation 사례집
> **대표 세션/이벤트**: Data + AI Summit 2026 Keynote(Day 1·Ali Ghodsi 킥오프), DAIWT Paris 2025 Keynote, RSA Conference(LakeWatch 발표), Snowflake Summit 2026(Opening·Platform Keynote, Sridhar Ramaswamy×Daniela Amodei), Snowflake Build London, Qdrant Vector Space Day 2025·Vector Space Meetup 2026, Weaviate Podcast 시리즈, W&B Fully Connected 2025(London·Tokyo), Pinecone 웨비나/RAG Brag | **관련 채널**: Databricks, Snowflake, Pinecone, Qdrant, Weaviate, Weights & Biases | **코퍼스 근거**: 실질 정독 18편 + 표적 발췌 정독 5편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Agent Bricks(Knowledge Assistant·AI/BI Genie·Multi-Agent Supervisor) | Databricks 에이전트 플랫폼 | PDF 등 비정형→Knowledge Assistant, 정형 데이터→Genie, 슈퍼바이저가 질의를 라우팅해 통합 답변. 폴더 지정만으로 10~15분 내 에이전트 생성 | 기업 78%가 2개+ LLM 패밀리 사용하는 파편화를 단일 거버넌스로 흡수. "에이전트가 조용히 성능 저하"되는 문제를 MLflow 평가로 상쇄 |
| Unity Catalog | 거버넌스 계층 | 테이블·파일·모델·MCP·에이전트·평가까지 단일 권한/감사 체계. 별도 권한 시스템 불필요(기존 권한 강제) | 자사 보고서: AI 거버넌스 투자 1년 새 7배 증가, 거버넌스 도입 기업이 **약 12배** 더 많은 프로젝트를 프로덕션 배포(연사 스스로 "상관관계" 단서) |
| LakeWatch | 에이전틱 보안 레이크하우스 | 보안 로그를 개방형 포맷으로 수집→OCSF 자동 정규화→Genie가 웹 리서치+자사 스키마 검증으로 탐지룰 작성·백그라운드 사건 조사 | 탐지룰 작성 **1주(때론 수주)→수 분**. 경보 주 7천 건(2020)→3만+ 건, 인력으로는 400명+ 필요 → "조사 역량이 SOC 인원수에 더 이상 묶이지 않는 최초의 순간" |
| CustomerLake | 에이전틱 CDP | Profile Agent가 신원 확인을 **룰→LLM→인간 검토** 3단 판정(매 실행 학습 반영), Campaign Agent가 "무한 캠페인"(상시 1:1 개인화) 실행, 역ETL로 채널 활성화 | 캠페인 기획 수주~수개월→상시 자율 루프. 데모 기준 420만 통합 프로필. "세계 최초" 신카테고리 네이밍은 워싱 신호로 병기 |
| Genie One + Genie Ontology(OntoRank) | 컨텍스트 계층 | 파이프라인·쿼리·대시보드에서 지식을 추출, PageRank류 알고리즘으로 권위 스니펫 선별→에이전트 루프에 주입 | 자사 벤치마크: 범용 코딩 에이전트 정답률 ~50%(수 분 소요) 대비 **정확도 +30%p·실행시간 절반** |
| Snowflake Intelligence · Cortex Code("Coco") · Horizon | 에이전틱 제어면 | 자연어 업무 비서+코딩 에이전트, Horizon Catalog(거버넌스)·AI Guardrails(프롬프트 인젝션·탈옥·제로데이 탐지)·Horizon Context(신호 수집형 컨텍스트) | "에이전트 기업의 관제센터" 포지셔닝 — 데이터·모델·앱 위 제어층을 쥐는 락인 전략 |
| Pinecone 캐스케이딩 검색 | 검색 파이프라인 | 밀집+학습형 희소 병렬 검색→리랭커 병합. 학습형 희소는 BM25 대비 DL트랙 최대 23%·BEIR 평균 8%↑ | 희소 단독 대비 **최대 45%(평균 24~25%) 정밀도 향상**(제목 표기는 48%). 리랭킹이 LLM 입력 토큰 절감=비용 방어 논리 |
| Qdrant + Qdrant Edge | 벡터 검색 엔진 | 클라우드와 동일 스토리지·인덱스 포맷을 로컬 기기에서 직접 접근(클러스터 우회) | 사내 비공식 테스트: 온디바이스 0.1ms vs 클라우드 왕복 52ms(**440배**, 네트워크 지연 제거). GitHub 스타 2.6만+, 커뮤니티 6만+ |
| Mem0(Qdrant 기반) | 에이전트 메모리 계층 | 관찰→추출→검색→실행→갱신 5단 루프. 학습을 가중치가 아닌 하네스에 저장: 검사·되돌리기·범위지정·이식 가능해야 | **망각 설계**(강화·수정·감쇠·삭제 권한·질문)가 핵심 — "모두 기억하면 충돌·무관 답변". 모델 교체 시대의 학습 이식성 주장 |
| Weaviate late chunking | 임베딩 기법 | 전체 문서를 장문맥 모델로 먼저 임베딩→토큰 임베딩을 사후 청킹(Jina AI 고안) | 청킹 문맥손실 해소하면서 ColBERT식 late interaction(2.5TB vs 5GB, 500배 저장)의 비용 회피 — 저장비용은 일반 청킹과 동일 |
| W&B Weave(+Models) | LLMOps/평가·가드레일 | 에이전트 트레이싱(수천 LLM 호출 스택), 평가·플레이그라운드, 기본 제공 환각 가드레일 | 채용 에이전트 데모: 가드레일 1차 실패→자가 재시도→2차 실패 시 인간 전문가 호출(HITL 3단 캐스케이드). Models는 P90/P99 두 자릿수 개선 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| Adobe·Atlassian·NAB | Databricks LakeWatch | 레거시 SIEM 한계(30일 초과 데이터 폐기, LLM 로그·코드·Jira 수집 불가)→보안 레이크하우스 이전 | Adobe: 레거시로 불가능했던 **페타바이트급** 분석 후 "이전엔 못 찾던 위협" 탐지(Defending against a tidal wave of AI attacks) | DX→AX — SIEM 이전(DX) 위에 에이전트 탐지룰 작성·자율 조사(AX)를 얹는 이행 |
| Panther Labs | Databricks 인수 | LakeWatch 강화용 보안기업 인수, CEO가 서밋 등판 | 인수 발표 시점 LakeWatch 출시 2개월차(동일 영상) | DX† — 기업 인수 이벤트로, AI의 자율 판단 실체가 문서상 없음 |
| Anthropic | Databricks·Snowflake 양쪽 파트너 | Dario Amodei×Ali Ghodsi 대담(독점 데이터 위 Claude), Daniela Amodei가 Snowflake Summit 2026 오프닝 키노트 | "신뢰가 성장의 가속제"(Snowflake Opening Keynote). LakeWatch 발표에서는 해커가 Claude로 멕시코 정부 공격, 인사기록 2억 건 탈취한 Anthropic 리포트 인용 | DX† — 키노트 담론·파트너십으로, 배포된 전환 사례 자체가 아님 |
| DEFRA·Natural England(영국) | Databricks 지리공간 AI | 잉글랜드 전역 이탄지 지도화 자동화 | West Pennines 규모 수작업 디지타이징 **1주→1일 미만**, 연간 수주~수개월 절감(How DEFRA… Peatland, 영어자막) | DX† — 정해진 인식 작업(디지타이징)의 자동화, 자율 판단·분기 근거 없음 |
| Thrivent·HSBC | Databricks 금융 웨비나 | Thrivent: 차선책(next-best-action) 추천을 자문 도구에 내장. HSBC: 글로벌 결제 데이터 활용 | 신규 예금 +10%, 다상품 가구 +20%(Unscripted: How Banks & Insurers…; 업계 일반 수치와 자사 성과 경계 모호, 자막 훼손 가능) | DX→AX† — AI가 차선책을 판단하나 실행은 자문가, 워크플로 재설계 근거 약함 |
| Canva·Nestlé·Thomson Reuters·DraftKings | Snowflake | Canva: Cortex 기반 제품 의사결정, Nestlé: 공급망 예측 전사앱, TR: "수임인(fiduciary)급" 신뢰 기준, DraftKings: 30개 주 규제 준수 데이터 관리 | Canva 월 2.65억 사용자·분석 수주→준실시간, Nestlé 185개국 2,000+브랜드·사용자 5만+·글로벌 기능 150개(Summit 2026 Opening/Platform Keynote) | DX† — 분석 가속·예측 앱·규제 데이터 관리로, 판단은 여전히 사람 몫 |
| Expel | Pinecone 보안 활용 | 보안 경보 중복 조사 방지 — 유사 경보 벡터 검색 | 탐지·대응 엔지니어링팀 실사용 사례(Preventing Déjà Vu, 2021) | DX — 유사도 검색으로 사람의 조사를 보조, 규칙적 파이프라인 |
| TripAdvisor·HubSpot·Deutsche Telekom·Dust | Qdrant | TripAdvisor AI 휴가 플래너(레스토랑 5만 곳 데이터), 프랑스 에이전트 플랫폼 Dust 등 | TripAdvisor 클러스터가 "우리가 아는 최대 규모"(Vector Space Day 2025 키노트, 자사 발화) | DX→AX† — 플래너·에이전트 플랫폼(계획 수립)이나 자율성 상세는 미공개 |
| Morningstar | Weaviate | Intelligence Engine — 사내·고객용 노코드/로우코드 GenAI 앱 플랫폼(리서치·애널리스트 노트 RAG, text-to-SQL) | FAISS PoC→Weaviate 프로덕션 전환, "Morningstar Mo" 투자 콘퍼런스 공개(Weaviate Podcast #111) | DX† — RAG·text-to-SQL은 정형 검색·생성 파이프라인, 자율 분기 근거 없음 |
| Sanofi·GSK·CoreWeave | Weights & Biases | Sanofi: 전사 AI 교육+자체 앱, GSK: 프로덕션 협업 언급, CoreWeave: 인수 후 기가와트급 DC 연계 | Sanofi 직원 ~10만 명 AI 교육·1만 명 심화, 사내 앱 직원 80% 사용·대화 900만+건·1인당 일 ~2시간 절감(Fully Connected London, 자막 훼손 가능) | DX† — 교육·업무 보조 앱 확산으로, 워크플로 재설계·자율 실행 증거 없음 |
| Mem0 | Qdrant 기반 스타트업 | 오픈소스 메모리 계층의 내부 벡터DB로 Qdrant 채택 | 창업자가 사용자 100만 GPT스토어 운영 경험 언급(Vector Space Day) | AX† — 에이전트가 스스로 기억을 추출·갱신·망각하는 자율 루프(단, 행 자체는 인프라 채택) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 거버넌스=배포 승수, 그리고 락인 | Databricks "거버넌스 기업이 12배 더 배포"(연사 스스로 상관관계 인정), Snowflake Horizon, Genie Ontology 모두 데이터+권한+컨텍스트 계층을 선점 | AX의 실질 락인은 모델이 아니라 **컨텍스트/거버넌스 계층** — '거버넌스=제동장치' 통념을 '처리량 승수'로 뒤집는 화법 자체가 인프라 판매 논리 |
| 에이전트=인력 환산 화법 | LakeWatch "경보 감당엔 400명 팀 필요"→"조사 역량이 SOC 인원에 묶이지 않는 최초의 순간", Sanofi "일 2시간 절감" | 도입 정당화가 기능이 아니라 **인건비 분모**로 계산됨 — 비용구조 연구의 종속변수(담론→원가 언어 번역 지점) |
| HITL 3단 판정의 표준화 | CustomerLake 신원확인(룰→LLM→인간), W&B Weave(가드레일→자가재시도→전문가), LakeWatch(에이전트 조사→분석가 검증) | 인간은 '경계 사례의 최종심'으로 재배치 — 자동화율을 높이는 안전판인 동시에, 인간 역할이 판정 노동으로 좁아지는 디스킬링 경로 |
| 유사성≠관련성 — 검색의 자기비판 2막 | Arize Laurie Voss "벡터 검색은 관련 문서가 아니라 유사 문서를 반환"(Qdrant 행사), Pinecone 캐스케이딩(+45%), Weaviate late chunking, Qdrant MMR | 벡터DB 진영이 1막(임베딩 판매)의 한계를 스스로 고발하며 2막(리랭킹·평가·컨텍스트 엔지니어링)을 판매 — '평가를 정의하는 자가 성능을 규정'하는 eval 전장과 합류 |
| 롱컨텍스트 대항 비용 담론 | Pinecone "토큰 과금이라 컨텍스트가 크면 비용·지연 증가+lost in the middle", Qdrant Edge 440배(네트워크 지연 제거) | 인프라 벤더는 **분모를 토큰·지연시간으로 치환**해 자기 계층의 존재를 방어 — '분모 바꾸기' 프레임의 인프라판 |
| 학습의 저장 위치 이동 | Mem0: 학습은 가중치가 아닌 하네스에(검사·가역·범위·이식 가능), 망각을 설계 대상으로 격상 | 모델 교체 가능성이 커질수록 가치가 메모리/컨텍스트 계층으로 이동 — 반락인을 표방하며 새 계층 락인을 만드는 이중 구조 |

**AX/DX 스펙트럼**: 이 클러스터의 고객 사례는 대부분 DX(검색·분석·RAG 파이프라인, 업무 보조 앱)에 몰려 있고, 진짜 AX 요소(LakeWatch 자율 조사, CustomerLake 자율 캠페인, Mem0 자율 메모리 루프)는 고객 검증 사례가 아니라 **벤더 자사 제품·데모 층위**에 집중되어 있다. 따라서 이 클러스터는 전형적 DX→AX 이행 국면이며, "세계 최초 에이전틱 CDP"류 신카테고리 네이밍과 자사 발화 수치는 AX 워싱 위험 신호로 함께 읽어야 한다.

※ **신뢰 경계**: 본 클러스터 수치의 대부분은 자사 컨퍼런스 키노트·웨비나의 **자사(또는 초청 고객) 발화**로, 제3자 검증 없음. Databricks "12배"는 연사가 상관관계임을 자인했고, "세계 최초 에이전틱 CDP" 등 신카테고리 네이밍은 워싱 위험 신호. Thrivent +10/20%는 업계 일반 수치와 자사 성과의 경계가 자막상 불명확. 한국어 자동번역 자막의 오염이 심각함 — agent→"상담원/부동산 중개업/요원", lakehouse→"호숫가 별장/창고", governance→"통치", Postgres→"은혜 이후", BEIR→"맥주", vibe coding→"와이프 코딩", LLM→"법률 석사", Pinecone→"솔방울", Sanofian→"샌디에이고 주민", 도메인 명사의 "[음악]" 치환 등이 확인되었으며, 위 수치 중 (자막 훼손 가능) 표기 항목은 원발화 대조가 불가능해 보수적으로 해석해야 한다. LakeWatch·DEFRA·Morningstar·W&B Weave 데모는 영어 자막 원문으로 확인되어 상대적으로 신뢰도가 높다.

---

# SAP · Salesforce · IT서비스 · 컨설팅(엔터프라이즈 앱) — AI Transformation 사례집
> **대표 세션/이벤트**: SAP Sapphire Madrid 2026(Global Keynote "The Beginning of Better", "Rise into the Future" 웨비나, BTP Unlocked 팟캐스트) | Salesforce Agentforce Demo Day·TDX 2026·Dreamforce 2025 | Infosys at Davos 2026 "AI Your Enterprise"(The Boardroom Mandate) | Accenture Top Banking Trends 2026(HBR 공동 브리핑) | McKinsey Podcast | BCG "So What" 팟캐스트, Kore.ai×BCG 런던 서밋 | **관련 채널**: SAP, Salesforce, Infosys, TCS, Accenture, McKinsey & Company, Boston Consulting Group | **코퍼스 근거**: 실질 정독 15편(+수치 검증용 발췌 3편)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| SAP Agent-led 마이그레이션 툴체인(7종 어시스턴트) | ERP 전환 자동화 | ECC→S/4HANA 전환의 시스템분석·데이터관리·커스텀코드·구성·테스트·롤아웃·프로젝트관리를 에이전트가 백그라운드 "스웜"으로 병렬 수행. Joule 채팅에서 시작해 동적 생성 "마이그레이션 콕핏"으로 진행 관리 | 전체 마이그레이션 노력 **35~50% 절감** 목표. 테스트케이스 1건 30~60분×1~2만 건 → **몇 분**, 데이터 정리 수개월→수주. 2026년 6월 첫 에이전트, 연말 완성 로드맵 |
| SAP 신뢰도 점수 분기 | HITL 거버넌스 | 커스텀 코드 수정 제안에 신뢰도 점수 부여 — 고신뢰=자동 적용, 중·저신뢰=개발자 검토로 라우팅 | 인간 개입을 예외 처리로 축소하면서 "완전한 통제" 서사 유지 — HITL의 계량화·상품화 |
| SAP Joule / Joule Studio + Business AI Platform | 참여·빌드 레이어 | Joule=전 앱 공통 대화 레이어, Joule Studio=의도(intent)→PRD→코드·워크플로 생성. SAP Knowledge Graph·Signavio(병목 탐지)·LeanIX 기반, 관리형 런타임에 거버넌스 내장 배포. VS Code·GitHub 연동 | "자율 기업(Autonomous Enterprise)" 운영모델 전환 선언. "지능은 프롬프트가 아니라 기록 시스템에 있다"며 SaaS 사망론 반박 — 50만 고객 데이터가 해자 |
| SAP Business Data Cloud(BDC) | 데이터 기반 | 레거시 BW를 흡수해 데이터를 "AI-ready"로 정비 | ZF 전 BW 시스템 이관 완료 — 에이전트 전 단계의 데이터 락인 |
| Salesforce Agentforce(topic/action 구조) | 에이전트 플랫폼 | 발화(utterance)→토픽→액션 3계층 템플릿으로 에이전트 구성, Agent Studio 로우코드 + 내부 추론 추적 노출 | 비개발자 구축 가능("AI로 AI를 만든다"), 토픽ID·액션 단위 디버깅 |
| Agentforce Testing Center | 평가·CI | AI가 토픽·데이터 기반 테스트케이스 자동 생성(최대 100개), CSV/XML로 Git 저장 → CI/CD 게이트 | 자사 영업 에이전트에 **180개 테스트**를 배포마다 전수 실행, **1건이라도 실패 시 프로덕션 파이프라인 차단** — eval의 배포 관문화 |
| Salesforce Agent Script | 하이브리드 추론 | LLM 창의성+결정론적 분기 결합, LLM 호출 전 로직 선실행 | Indeed 오류패턴(75%) 교정, LIV Golf 지연 **-60%**·정확도 94%. 음성 에이전트 GA |
| Agentforce Vibes | 코딩 에이전트 | 자연어 프롬프트→Apex 클래스·Flow·배포파일 자동 생성 | 에이전트 개발 자체의 탈숙련화 |
| TCS AI 지원 마이그레이션(HITL 템플릿) | 레거시 현대화 | 고객·TCS 엔지니어가 공동 개발한 템플릿을 AI에 입력, 반복 정제+인간 품질검사로 레거시 코드의 비즈니스 로직 해석·보존 | TDC NET "수년→몇 달". "GenAI가 다 해주진 않는다" — 반(反)과장 포지셔닝 |
| Infosys 고객 미팅 AI(스웨드뱅크 공동구축) | 도메인 앱 | 고객 미팅 녹음→요약 자동화 | 스웨드뱅크+약 60개 저축은행·4개 시장 확산 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| SAP × Fonterra(뉴질랜드 낙농협동조합) | Rise/S4 전환+AI | 클린코어 전환 중 현금앱·정비주문 추천·운송계획 3개 AI 앱 가동, Joule로 비정형 데이터→서비스 접수표 생성(월 수천 건 서비스 청구서) | 2개 공장 가동, 22개 공장 확대 계획. "기술이 아니라 변화관리가 과제"(WalkMe 활용) (AI Transformation with Fonterra) | DX→AX — ERP 전환(DX) 위에 추천·비정형 판단 앱 가동 |
| SAP × ZF Group | 데이터+품질 AI | 15만 명·29개국·160개 공장, 인수합병발 복잡 ECC. 전 BW→BDC 이관, 8D 품질 프로세스에 4-에이전트(유사사례 검색→근본원인→해결안) | SAP "전방배치 엔지니어링" 1호 고객 (AI Value at Scale with ZF Group) | DX→AX — BW 이관(DX)+근본원인 판단 에이전트 체인(AX) |
| SAP × "제로 고객"(익명 대기업) | Agent-led 전환 | 마이그레이션 노력 1/3~50% 절감을 명시 목표로 조기 착수 대기 | ECC 유지보수 2027 종료·2030 연장 종료가 수요 동인 (Agent-led Transformation) | DX→AX† — 신뢰도 분기 설계는 AX적이나 착수 전 목표치 단계 |
| TCS × TDC NET(덴마크 통신) | 레거시 해체·이관 | 40년 이상 된 국가 기간망 시스템을 HITL AI로 현대화, 비즈니스 로직 보존 | "수년 예상 작업을 몇 달에" — 금전·일정 가치 명시(정량 미공개) (TCS helps TDC NET modernise) | DX→AX† — 마이그레이션(DX)에 AI 로직 해석, 단 규칙은 인간 템플릿 |
| Infosys × Swedbank | 전행 AI 확산 | CIO Lotta Lovén: 탑다운 전략 사례(KYC·신용처리·고객서비스 재구상)+바텀업 풀뿌리 병행, 전 직원 역량교육 | 미팅 요약 시스템을 ~60개 저축은행·4개 시장으로 확산 (How Swedbank Is Scaling AI) | DX† — 확산 실체는 미팅 요약 자동화, 자율 판단·분기 미확인 |
| Infosys × Sandvik | 광업·기계가공 AI | CDO Sofia Sirvell: 보증처리 전과정 AI, S&OP, 기술문서 지능형 안내. 3-직무 측정틀 — 개인생산성=채택률, 프로세스 재구상=크로나/유로 순익, 제품 내 AI=고객 생산성 | 대부분 POC, 일부 스케일링. "최대 장벽은 기술이 아니라 변화 여정" (The Biggest Barrier to AI) | DX→AX† — 프로세스 재구상 지향이나 대부분 POC 단계 |
| Salesforce × Indeed | 서비스 에이전트 | Sr. TPM Oliver Bowden: 분당 31명 채용 지표에 에이전트 정렬. Agent Script로 "계정 상태에서 멈추는" 75% 오류 교정, 커서+플레이북(md)·MCP(Jira) 운영 | 해결률(deflection) 4%→평균 25%(6배), CSAT 1.8→4.0 (How @Indeed is Building Agents / Demo Day) | AX — 에이전트가 티켓 자율 해결, 워크플로 재설계 |
| Salesforce × LIV Golf | 팬 에이전트 | Agent Script+변수 프리로드로 지연 단축, QA팀 전 버전 테스트 | 지연 -60%, 정확도 94% (Agentforce Demo Day) | AX† — 에이전트 자율 응대, 단 결정론 선실행 비중 큼 |
| Salesforce × Falabella·JPW | 커머스·제조 | WhatsApp 문의 자가응답, 사건 해결 가속 | Falabella 60% 자가응답, JPW 해결속도 +40% (Agentforce Demo Day) | AX† — 자가응답률은 자율 해결 근거, 판단 구조 상세 미공개 |
| Accenture 보고서 × JP Morgan·DBS·BNY | 은행 AI 스케일링 | "과학박람회 프로젝트" 탈피·전사 확장 촉구. BNY는 AI 디지털 직원에 신원 부여, 이메일 도구 1.1만→12만 명 확대 | JP Morgan $2B·DBS $1B 효익 발표 인용, 이메일 도구 주 3시간 절감(자막 훼손 가능) (Top Banking Trends 2026) | DX(AX 표방)† — "디지털 직원" 수사 대비 실체는 이메일 보조 도구, 수치도 재인용 |
| Infosys Davos 패널(Anthropic·Danske Bank) | 담론 컨비닝 | AI 투자 수조 달러 vs 업계 연매출 ~500억 달러 격차 논쟁 | "임원 75%, 5년 내 AI 확장 실패 시 폐업 전망" 인용 (The Boardroom Mandate) | DX(AX 표방)† — 구현 사례 아닌 담론·공포 수사, 판정 대상 실체 부재 |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 만료 시한이 만든 AX 수요 | SAP는 ECC 유지보수 종료(2027/연장 2030)를 명시적 동인으로 에이전트 마이그레이션을 판매 — "고객은 이미 여정에 있다" | AX가 자발적 혁신이 아니라 **유지보수 절벽+락인 갱신**으로 강제되는 경로. 전환 비용 35~50% 절감 약속은 곧 SI·컨설팅 인건비 재편 선언 |
| HITL의 제품화·계량화 | SAP 신뢰도 점수 분기, Salesforce 180테스트 CI 차단, TCS 인간 품질검사, Accenture "소비자 ~80%가 AI 결정 전 승인 원함" | 거버넌스가 신뢰 수사에서 **관문 기능(gate)**으로 상품화 — 평가·테스트 정의권을 쥔 플랫폼이 배포권을 쥐는 거버넌스 락인. "eval이 새 전장" 프레임과 합치 |
| "도입≠수익" 컨설팅 공통 문법 | McKinsey State of AI "88% 사용 vs 의미 있는 수익 39%", Krivkovich "80% 투자 vs 80%+ 미체감", BCG(Nick Clarke, Kore.ai 서밋) "**효율 15% 미만이면 P&L 반영 불가**" | 실패 통계가 컨설팅 수요 창출 장치로 기능(책임전가 알고리즘). 15% 임계는 분모 바꾸기 담론에 계량 눈금을 제공 — ROI 서사 검증의 기준선 |
| 레거시=비용구조의 본체 | Accenture: 은행 기술비용이 매출보다 200~300% 빠르게 성장(15년간 4배), **기술 시간 70%가 레거시 유지**, 오픈소스로 50~90% 절감. TCS·SAP도 레거시 현대화를 AX 관문으로 판매 | AX 담론의 실제 원가 접점은 모델비용이 아니라 레거시 유지비 — "저비용 결정의 높은 대가" 프레임이 현대화 CAPEX를 정당화 |
| 에이전트=인력 분모 전환 | Accenture "10배 은행"(2만 명 은행→20만 '직원'), "한계비용 0의 추가 인력". McKinsey "임원 직무 70% 재편, 2~3년 내 전원 새 직무기술서, Human above the loop"(AAA 중재 사례) | 인력 수 분모에 에이전트를 산입하는 재정의 — 감원 서사를 "확장 서사"로 뒤집는 수사 장치. 노동 측정 지표 연구의 핵심 관찰점 |
| 대리화자(proxy speaker) 전략 | Infosys는 자사 발화 대신 고객 임원(Swedbank CIO, Sandvik CDO, Air Liquide·Adecco)과 Davos 패널(Anthropic·Danske CEO)로 말하게 함. Salesforce는 자사 이벤트에서 고객 수치 증언(Indeed·LIV Golf) | 권위 이전형 마케팅 — 수치는 고객 입에서 나오므로 검증 책임이 분산됨. 워싱 판별 시 발화 주체·수치 출처 분리 태깅 필요 |

**AX/DX 스펙트럼**: 이 클러스터는 DX→AX 이행 지대에 집중된다 — SAP·TCS는 레거시 마이그레이션(DX)이라는 기존 사업 위에 에이전트 판단(신뢰도 분기·로직 해석)을 얹는 전형적 이행 사례이고, 순수 AX는 Salesforce 고객사(Indeed 등 자율 해결 에이전트)에 몰려 있다. 반면 Accenture "디지털 직원"·Davos 담론처럼 실체(이메일 보조·수치 재인용) 대비 자율성 수사가 과대한 워싱 위험 구간이 컨설팅 축에 뚜렷하다.

※ **신뢰 경계**: 본 클러스터 수치는 전량 벤더 자사 채널 발화(고객 증언 포함)로 제3자 검증 없음. SAP 35~50%는 "목표치", Salesforce 성과는 자사 행사 내 고객 인터뷰, Accenture JP Morgan/DBS 수치는 타사 발표 재인용. 자막 오역 위험 높음 — Joule→"Jewel/주얼", Agentforce→"Agent Force 게임", deflection rate→"감염 확산 방지율", LIV Golf→"Live Golf", Danske→"Danska", TCS "음악 IT 생태계"(도메인명사→음악 치환), BNY 이메일 사례가 "BP"로 표기되는 등 고유명사·수치 인용 시 원어 확인 필수. 워싱 위험: Accenture(배수 수사 "10배 은행", 스포츠 스폰서십 AI buzzword 전력) > Salesforce(자사 이벤트 증언 구조) > McKinsey·BCG(실패 통계=수임 장치) >> TCS·SAP 기술 웨비나(상대적으로 구체·절제, 단 목표치와 실적 혼재 주의).

---

# 한국 AX(삼성SDS·SK·LG·NAVER·Upstage·무신사) — AI Transformation 사례집
> **대표 세션/이벤트**: [AX Summit] 키노트 "AI Native 기업으로의 전환 방안과 사례"(삼성SDS AX센터 신계영 부사장) · [AI&CLOUD2026] 세션1(IT조선) · "ChatGPT Enterprise 도입전략" 웨비나(삼성SDS×OpenAI 한지은) · LG AI Talk Concert 2025(임우형·이홍락·최정규+FriendliAI·FuriosaAI·LSEG) · OpenAI×무신사 비공개 행사(전준일 CTO) · MWC26 SKT 기자간담회 · 티타임즈TV 황재선 SK 부사장(『AX 100배의 법칙』) · 정부 독자 AI 파운데이션 모델 프로젝트 | **관련 채널**: 삼성SDS AX, IT조선, 티타임즈TV, AI겸임교수 이종범, LG_AI_Research, SK텔레콤, NAVER_Cloud, Upstage, 전인구경제연구소, 카툰경제학 (+담당 채널 중 SK_hynix·kakao_tech는 AX 실질 콘텐츠 희박) | **코퍼스 근거**: 실질 정독 14편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| FabriX(삼성SDS) | 에이전트 플랫폼 | 사내 데이터·업무시스템을 연결해 노코드~프로코드로 에이전트 생성, AI 스토어(마켓플레이스) 등록·재사용, 멀티에이전트 오케스트레이션 | 삼성전자 "작년 기준 에이전트 1만여 개 동작"; 우리은행 전사 플랫폼; 금융·공공 중심 확산 |
| Brity Automation·Brightics AI(삼성SDS) | 자동화·데이터 | RPA/BPA+컴퓨터 유즈 에이전트 실행, 비정형·정형 데이터를 "AI 레디 데이터"로 전처리·파싱 | 프로세스 리디자인→데이터 우선순위→권한 연계까지 E2E; T2A(Text-to-Analytics) 멀티에이전트가 Spider 2.0 벤치마크 글로벌 1위(2025.11, 자사 주장) |
| 에이전트 가드·MCP 가드(삼성SDS) | 거버넌스 | 에이전트별 권한·비인가 소스 접근·도구 동작을 감시, 토큰 사용량 미터링→KPI 대비 | "에이전트도 사람처럼 HR식 역량평가·재배치" — 에이전트=인력 관점의 통제 체계 |
| EXAONE 4.0/4.0 VL/Path 2.0(LG) | 파운데이션 모델 | 32B+1.2B 온디바이스, 문서·차트 이해(ChartQA 세계 1위 주장), 병리영상→유전자 변이 예측 | 유전자검사 2주→1분; 누적 다운로드 510만·파생모델 200+ |
| ChatEXAONE·Data Foundry(LG) | 업무 에이전트·데이터 | 딥리서치(20p+ 보고서 자동생성), 도메인 파인튜닝용 데이터 자동 생성·평가 | LG 임직원 5만+·사무직 65% 사용; 전문가 60명·3개월·2,200건(절반 폐기)→1명·34시간·11,000건 |
| EXAONE 온프레미스 패키지+FuriosaAI NPU·FriendliAI API(LG) | 인프라 | 망분리 내부망 구동, MCP/A2A 지원; NPU 8카드 4PFLOPS·3kW | NPU 에너지효율 GPU 대비 2.3배; API 가격 "ChatGPT의 1/10"; 데이터 컴플라이언스 에이전트 NEXUS: 정확도 26%↑·45배 빠름·비용 1/1,000 |
| A.X 독자 파운데이션 모델(SKT 컨소시엄) | 소버린 모델 | 5천억 파라미터(국내 최대 목표), GPU 1천장+ 학습, 라이너·셀렉트스타·크래프톤·포티투닷·리벨리온 NPU 풀스택 | 정부 독자 AI 파운데이션 프로젝트 2단계 진출; MWC26에서 1조 파라미터급·1GW급 AIDC 벨트·"1인 1 AI" 선언 |
| HyperCLOVA X·Neurocloud·CLOVA Studio(NAVER) | 소버린 클라우드 | 고객 내부망 프라이빗 클라우드에 초거대 모델+관리형 서비스 설치, RAG·에이전트 개발 | "보편 AI와 공존하는 소버린 AI" 하이브리드 전략; 한국은행·공공 등 규제산업 진입 |
| Document Parse·Solar(Upstage) | 문서 AI | 저해상도 문서를 어절 단위로 추출, 표·레이아웃 보존 | 인식률 10%p 차이=검수 원가(플리토 사례); 보험 언더라이팅 등 도메인 특화 확장 |
| Codex 엔터프라이즈(무신사 도입) | 코딩 에이전트 | 코너케이스 우선 추론, TDD·사전 문서화 강제 | 사내 발화 기준 Claude Code 엔터프라이즈 토큰 대비 약 5배 저렴한 효율(자막 훼손 가능); "월급보다 토큰을 더 쓰는 헤비유저" 통제 이슈 해소 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| 우리은행×삼성SDS | 전행 AX | CEO가 "금융회사지만 AX 회사" 선언, 1년 컨설팅으로 5대 업무·27개 핵심업무에 175개 에이전트 설계 | SDS 진단 결과 실제 최소 300개+ 에이전트 필요, FabriX 기반 내년 하반기까지 구축 ([AX Summit] 키노트) | DX→AX† (에이전트 전면 설계이나 아직 구축 전 — 자율 판단 실증 미확인) |
| 삼성전자(SDS 수행) | 콜센터·시장조사 | 상담 보조 AI(요약 자동입력)→서비스 사이트 챗봇 에이전트 전환→보이스봇 시도; 인터뷰어·응답자 모두 에이전트인 시장조사 | 연 100억 이상 외부 조사비 업무를 대체, 실제 글로벌 인터뷰와 80~95% 일치 ([AI&CLOUD2026]) | AX (에이전트가 인터뷰 수행·응답 판단, 사람 역할 대체·재정의) |
| 삼성 관계사×OpenAI(SDS 국내 최초 리셀) | ChatGPT Enterprise | 기밀=FabriX/비기밀=외부 모델 이원화, 거버넌스는 FabriX 일원화 | 1월 사업 개시 후 고객사 20여 개, 6월부터 삼성 관계사 전면 사용 결정 ([AX Summit]) | DX† (도구 보급·거버넌스 정비 단계, 워크플로 재설계 근거 없음) |
| LG 계열(LG AI연구원) | 제조·R&D | 소수 결함이미지 학습 비전검사, 석유화학 원료 스케줄링 에이전트, 고객상담 STT·요약 | 검사 정확도 20%↑·연 $54M 절감; 100% AI 스케줄 공장 운영·한계이익 4%↑; 상담 만족도·생산성 20%↑ (Talk Concert 2025) | AX (100% AI 스케줄 공장 — AI가 운영 의사결정 수행) |
| 국민연금공단·LSEG×LG | 파인튜닝·금융 | Data Foundry로 기관 문서 기반 모델 튜닝; 뉴스 5,000건/일 반영 Master Score(4주 수익률 1~100 신호) | 전문가 선호도 25%↑; LQAI ETF NYSE 상장·S&P500 상회 주장(자사 발화) | DX→AX† (AI가 투자신호 판단을 생성하나 실행·최종결정은 사람) |
| SK디스커버리·SK바이오사이언스(황재선) | 현업 AX | 중대재해 대응 작업위험성평가서(JSA) 생성 AI, 레이아웃 보존 문서번역, HR 규정 챗봇 | 번역문 읽기 속도 약 50%↑; 문의응대 건당 30분↓; 콜센터 챗봇 연 1.5억 절감 사례 제시(티타임즈TV) | DX† (생성 AI 보조 도구 중심 — 정해진 업무의 자동화, 자율 분기 없음) |
| 한국은행×NAVER Cloud | 금융 특화 LLM | 내부망 전용 프라이빗 클라우드+Neurocloud로 금융·경제 특화 LLM, 통합데이터플랫폼 BIDAS 연계 자연어 분석 | 구축 진행 중, 요약·번역·질의응답 제공 예정(자사 채널) | DX (인프라·플랫폼 구축 단계, 요약·번역 등 보조 기능) |
| 대동×NAVER Cloud | 농업 에이전트 | AI콜 기반 영농일지·재배 컨설팅·유통 에이전트 | 구축 준비 단계(자사 채널, 수치 없음) | DX(AX 표방)† (에이전트 표방이나 준비 단계·수치 부재로 실질 미확인) |
| 플리토×Upstage | 데이터 전처리 | 번역 데이터 기업의 원천문서 추출을 Document Parse로 대체 | 타사 대비 저해상도 인식률 10%p 우위=신문 1장당 오류 300어절→1만 장이면 300만 어절 검수 인건비 차이(고객사례 영상) | DX (정형 문서 추출 파이프라인 — 전형적 디지털화·자동화) |
| 무신사×OpenAI | AI 네이티브 전환 | 에반젤리스트 발굴→슬랙 허브 공유→부서 임베디드 배치→탑다운 푸시 4단계; 연 4.5억 원 SaaS를 비개발자 매니저 기획+개발자 3명 바이브코딩으로 2개월 내재화 | 구독비용 약 4.5억 절감; 개발자 66명 신규채용을 "AI 활용 문제해결" 평가로 선발; "2026년 말 실리콘밸리 코드 80%가 AI 작성" 전망(전준일 CTO 발언, 3자 후기 경유) | AX (코딩 에이전트가 개발 수행, 채용·평가 등 사람 역할 재정의) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 토큰=ROI 회계단위 | 삼성SDS: AX 투자를 토큰 비용으로 전량 치환, KPI를 Tech(정확도)→Process(성인화·TAT)→Business(수율) 3층으로 계측. 중요 업무에 토큰을 "배정"하는 예산 개념 | 담론의 '분모 바꾸기'가 실무 회계로 제도화되는 지점. 토큰 미터링+에이전트 가드가 플랫폼(FabriX) 락인의 실체 |
| 에이전트=인력 | SDS는 에이전트를 HR처럼 역량평가·재배치·거버넌스; 조직 측은 CAIO 선임·AX센터 결집·AI 크루 107명·임원 2박3일 합숙교육 | "에이전트 채용·관리"라는 인력 프레임이 조직도(CAIO)와 평가제도로 물화. AX의 본체는 기술이 아니라 조직 재설계 |
| AX 100배 산식과 CEO 70% | 황재선: 개발자 40~50배·통상 10배 생산성×기업가치 10배="100배"; 성공의 70%는 CEO 스폰서십, 나머지는 현업 오너십+AI팀+AI 챔피언 | 배수 서사는 자기증식적(측정은 재무+비재무 병행 권고). 5단계 로드맵(체험→공식도입→ML→에이전트→신규 BM)은 한국 대기업 AX의 표준 문법 |
| 결핍이 혁신·한국형 노동마찰 | 무신사: 인력이 부족한 팀일수록 AI를 잘 씀; 정규직 해고 경직성 하에서 "성과평가 기준을 AI 활용으로 재설정"→도태 인력은 사실상 한직화. 3자 채널은 희망퇴직·"월 3만원 AI vs 월 700만원 인건비" 대비, 한은 보고서 인용(청년 일자리 감소 21.1만 중 98.6%가 AI 고노출 업종) | 미국식 해고 대신 평가제도·희망퇴직이 노동조정 통로 — HITL 논의가 한국에선 고용법제와 접합. 유휴인력 흡수("하고 싶은 일 100 중 5→50")는 낙관 서사로 병존 |
| 소버린 하이브리드 | NAVER "보편 AI와 공존하는 소버린 AI", SKT 5천억→1조 파라미터+15GW AIDC(3자), LG 온프레미스+국산 NPU(FuriosaAI·리벨리온) | 망분리·국가핵심기술 규제가 온프레미스·NPU 수요를 창출 — 규제가 곧 시장인 한국형 거버넌스 락인. 정부 독자 파운데이션 프로젝트(SKT·업스테이지·LG·모티프)가 공적 보증 역할 |
| 도메인 특화=원가 | Upstage: 인식률 10%p가 검수 인건비·프로젝트 원가로 직결(플리토); Amwins "범용 LLM은 작은 꼬리로 큰 개 흔들기" | 모델 성능 %가 곧 비용구조라는 번역이 도메인 특화 진영의 판매 논리. 정확도→원가 환산 공식은 AX 비용연구의 핵심 표본 |

**AX/DX 스펙트럼**: 이 클러스터는 실증된 AX(삼성전자 시장조사 에이전트, LG 100% AI 스케줄 공장, 무신사 코딩 에이전트+평가제 재설계)와 인프라·문서처리 중심 DX(한국은행·플리토·SK 현업 도구)가 양극으로 갈리고, 우리은행·국민연금처럼 설계·신호생성 단계의 DX→AX 이행 사례가 중간을 채운다. 성과 수치가 거의 전부 자사 발화이고 "에이전트" 명명이 준비 단계 사례(대동)까지 확장되는 만큼, 워싱 위험은 자율 판단·분기의 실증 여부로 걸러야 한다.

※ **신뢰 경계**: 성과 수치는 거의 전부 자사 발화(삼성SDS·LG·SKT·NAVER·Upstage 자사 채널 또는 자사 주최 행사)이며 외부 검증 없음. 무신사 사례는 인플루언서 3자 후기 경유(수치 재확인 불가), 카툰경제학·전인구경제연구소는 선정적·투자 프레임의 3자 채널로 워싱·과장 위험 높음. 자막 자동전사 오류 다수 확인: 황재선→"황제선", SKT CEO 성명 표기 불안정("정재원/정재현"), 리벨리온 NPU→"MPU", 무신사 CTO→"전준희", Codex 사용자 400만 등 급증 수치와 토큰 5배 비교는 (자막 훼손 가능). 담당 채널 중 SK_hynix는 HR·교양 중심, kakao_tech는 2021 인프라 세션 위주로 AX 담론 실질이 얕아 본 사례집은 키워드 수집분과 자사 이벤트 채널에 의존함.

---

# 중국·아시아(Huawei·Alibaba·소버린 국가전략) — AI Transformation 사례집
> **대표 세션/이벤트**: HiFS(Huawei Intelligent Finance Summit) 2026 상하이 · HUAWEI CONNECT 상하이 · Huawei Cloud Summit(동관 캠퍼스 인터뷰) · MWC 바르셀로나 2026 · Alibaba Cloud ClawTalks EP1–6(웨비나) · Hannover Messe 2026(Dr. Ye Huang 강연) · SB OAI Japan 법인 특별 이벤트(2026.6 도쿄, 손정의×Mark Chen, 130개사 200명) | **관련 채널**: Huawei(126편), Alibaba_Cloud(121편), SoftBank(97편), NTT_DATA(26편) + 키워드(Vietnam AX) | **코퍼스 근거**: 실질 정독 15편(+NTT_DATA 전수 키워드 검증)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Huawei Atlas 950 슈퍼포드 | AI 컴퓨트 | 캐비닛당 64개 MPU, 통합버스로 최대 8,192 MPU 확장·통합 메모리로 수천 노드를 단일 컴퓨터처럼 구동 | 금융권 "밀리초 시장" 대응용 자급 컴퓨트(NVIDIA 비언급 = 제재 우회 자급 스택) |
| Huawei 금융 탄력 아키텍처(자막 "ROS 2.0") | 금융 인프라 | 액티브-액티브 멀티사이트 재해복구, 4-zero(무중단·무대기·비접촉 운영·제로트러스트) | 가용성 99.999% — "신뢰는 선택이 아니라 인프라 문제"로 AX 신뢰담론을 스펙화 |
| Huawei ModelArts + Ascend NPU + CodeArts/DataArts | AI 플랫폼 3층 | NPU 컴퓨트→멀티모델(상용+오픈소스) 오케스트레이션 MaaS→에이전트/코딩/데이터 에이전트 | 톈진항에서 방대한 실시간 데이터 이상탐지·근본원인·해법 추천 — "수동 모니터링·전문지식 의존 제거" |
| Pangu CV 기반 PortGPT + OptVerse AI Solver | 산업 AI | 항만 영상 다중 인식 단일모델 + 수천만 변수·제약 최적화(크레인·출항 계획) | 계획 수 시간→수 분, 원격 1인 다(多)크레인 제어, IGV 92대 L4 자율주행 3년+ 무사고 "세계 최초 무탄소 스마트 터미널" |
| Huawei 자율주행 네트워크·Easy Branch | 네트워크 운영 | 네트워크 디지털맵 가시화, 배포 전 시뮬레이션, 지점 개설 자동화. 금융 L4 자율 네트워크 원년 선언 | 지점 1개 구축 1시간(효율 10배↑), 중국 은행 연 3만 건 망변경 리스크 흡수, 2,000+ 금융기관 공급 |
| Alibaba AIDBS(AI-native Database Service) | 데이터+에이전트 | 데이터/메타/DAS/데이터브리지 4개 에이전트 + 에이전트 마켓 + 50여 소스 멀티클라우드 메타데이터 통합(AWS Aurora·MongoDB까지 포섭) | 장애 진단보고서 30초 생성·정확도 92%(전문가 85%, 기본 LLM 대비 +33%). "2027년 자사 DB 인스턴스 50%+를 AI 에이전트가 직접 사용" 선언 |
| Alibaba QoderWork(자막 "코다 워크") + Quick BI | 데스크톱 에이전트 | 격리 VM에서 로컬 파일·브라우저·오피스를 직접 조작, SOP를 '스킬'로 변환·마켓 공유, MS365/Teams 커넥터 | 리서치 1~2일→11분, 주간 매출보고 1.5일→5분, 브랜드 웹사이트 1주(팀)→22분(자사 데모 기준). OpenAI 2025 리포트 "조직당 추론 토큰 320배" 인용해 수요 정당화 |
| Alibaba Qwen 3.6/모델 스튜디오·링쥔 클러스터 | 파운데이션 모델 | 100만 토큰 컨텍스트·에이전틱 코딩, 오픈소스 300+ 모델, 10만+ GPU 클러스터 | 일 사용 1.4조 토큰(자막 훼손 가능), 누적 10억 다운로드=글로벌 오픈소스 20%·파생모델 20만 개 — 오픈소스로 서방 시장 침투 |
| SB OAI Japan "Daybreak"(GPT-5.5 Cyber+Codex Security) | AI 보안 | 취약점 발굴→에이전트가 사용자 모방 재현·검증→패치 생성→회귀테스트→감사로그, "Patching as a Service" | SoftBank 자체 700개 시스템에서 취약점 10,500건 발견(¼ 즉시 패치), 반복 스캔 22→11→7→5건. 일본 중요인프라 3,000개사에 무상 제공, 인력 50→1,000명 확충 계획 |
| Gen-AX "X-Ghost" | 콜센터 에이전트 | GPT Realtime 기반 speech-to-speech(텍스트 변환 생략), 프롬프트 실드·가드레일, 고위험 건 인간 이관, 노코드 빌더 | 금융·철도·제조·소매 10개사+ 선행 도입. "대체 아닌 지원" 선언과 "업무 70% AI 담당" 구상의 동거 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| Ant Group(알리페이) | 코어 아키텍처(크리스 스키너 사례연구, HiFS 발화) | 2003년 창립 후 12년 만에 5번째 아키텍처 — 3~4년마다 전면 재구축 | "유럽·미국 은행은 50년간 안 한 일"·AI 기반 플랫폼 위 전면 재설계 촉구("Banks Need AI-Native Foundations") | DX† (AI-native는 촉구 담론, 자율 판단 실증 없음) |
| 톈진항만그룹 | 스마트항만 1.0~3.0(2021~) | PortGPT·OptVerse·ModelArts·디지털트윈·TCA 관제 | 계획 수 시간→수 분, IGV 92대 3년+ 자율운행, 최소인력·자율 운영("Decoding Tianjin Port") | AX |
| İşbank(터키) | 지점망·자율 네트워크 | 2,800개 지점 Easy Branch·ST1 프로젝트(2024~), 제로트러스트 | 지점 구축 며칠~몇 주→몇 시간·1시간 구축 10배 효율, 거래 95% 디지털("Transforming a Vast Network") | DX→AX† (실증은 배포 자동화, L4 자율은 '원년 선언' 단계) |
| Telecom Argentina(Personal) | 하이브리드 멀티클라우드·AI 네이티브 통신 | 코어 IT 무중단 이전("비행 중 엔진 교체"), 고객 개인화+망 장애 예측 | 워크로드별 배치 프로세스 수립 단계, 수치 미공개("Why Telecom Argentina is Betting…") | DX |
| Keyrus × RCBC(필리핀 5대 은행) | 데이터·분석 전사 역량화 | 전 직원·관리자에 AI/분석 부여 결정(1년 전), single source of truth 기반 360도 고객뷰 | 정량 성과 미공개 — "지성은 진실성(데이터 품질) 위에"("Why Data Alone…") | DX |
| 글로벌 Web3 거래소(익명) | Alibaba AIDBS 멀티클라우드 거버넌스 | 타 클라우드 DB 600+ 인스턴스·Aurora 100개까지 단일 거버넌스, DAS 에이전트 자동 장애처리 | 진단보고 30초·정확도 92% vs 전문가 85%(ClawTalks EP6) | DX→AX |
| 중국 대형 자동차 제조사(익명) | 에이전트 하네스 운영(자막 "오픈 클라우드"=OpenClaw 추정) | 400+ 인스턴스를 로컬/글로벌 메모리·관측성으로 관리 | 수치 미공개(ClawTalks EP6) | AX† (에이전트 운영이나 자율성 상세·성과 미공개) |
| BMW(중국 시장) | Qwen 기반 차내 AI | "카 지니어스"·"트래블 컴패니언" 에이전트 | 웨이크업 정확도 99%·연산 출력 20배(자막 훼손 가능)(Hannover Messe 강연) | DX(AX 표방)† (대표 지표가 웨이크업 정확도 = 음성비서 수준) |
| SoftBank(고객 0호) ×OpenAI | 사이버 AX 자기실험 | 1,800개 시스템 중 700개 진단, GPT-5.5 Cyber로 발굴→패치 | 취약점 10,500건·월 5만 건 공격 방어 중 진단(수치 자막 혼재), 그룹사 1곳 공격으로 6개월 영업중단 경험(SB OAI Japan 이벤트) | AX |
| 미쓰이스미토모카드·JCB(추정, 자막 "잘 카드") | X-Ghost 콜센터 | 질문의 본질 이해→사내 데이터 대조 최적응답, IVR 진화 | "최종 업무 약 70% AI 담당" 구상 명시(X-Ghost 해설) | AX† (고위험 인간 이관 분기 설계, 단 70%는 구상 단계) |
| SoftBank 전사(2025.2 OpenAI 제휴 후) | 전 직원 에이전트 제작 운동 | 1인 100개 목표 의무화, e러닝·세미나 병행 | 2.5개월 250만+ 에이전트, 약 90% "이해 깊어짐", AI 자격 2,000명+ — "양이 곧 훈련" | DX(AX 표방)† (KPI가 제작 개수, 자율 수행 성과 미검증) |
| 베트남 통신 3사(국가전략) | 국가 AX 분업(제3자 채널 분석) | Viettel=자체 칩~LLM 풀스택(NVIDIA·Intel·ASUS 제휴) / VNPT=정부·대기업 B2G / MobiFone=소비자·SMB 플랫폼 | 2030년 GDP +$790억(≈+12%) 전망, AI 전문가 7,000명·스타트업 500개 목표(태국은 3만 명 목표와 대비) | DX† (전략·전망 단계, 자율화 실증 없음) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 중국의 '주권 탈색' 신뢰담론 | Huawei는 지정학·주권 언어를 완전히 소거하고 "글로벌 선호 파트너·99.999%·회복력·비용절감"으로 대체. 고객 사례도 터키·아르헨티나·필리핀·아프리카 등 글로벌 사우스에 집중 | 서방(Oracle 동맹주권)·EU(기술주권)와 대조되는 **주권회피형 신뢰담론** — state 담론 축이 블록 대 블록으로 분화. 제재국 벤더의 '국가판 자동차 침묵' 전략 |
| 재건축 주기 = 분모 바꾸기의 아키텍처판 | Ant 12년 5회 vs 서방 은행 50년 0회 프레임으로 '레거시 유지'를 리스크로, '주기적 전면 재구축'을 경쟁력 지표로 재정의 | TCS·Accenture의 "레거시 현대화=AX 관문" 서사와 동형. 기술부채 상각 주기를 KPI로 바꾸는 분모 스왑 |
| 에이전트=인력 회계의 극단화 | Alibaba "디지털 실리콘 전문가팀"·"AI Workforce"·DB 사용자의 50%가 에이전트(2027), 토큰 할당량·예산관리 내장. SoftBank는 전 직원 1인 100개 에이전트 의무화 | 에이전트를 헤드카운트·예산 단위로 세는 담론의 미·중·일 수렴 + FinOps가 인사관리 문법을 흡수. 단 성과지표는 '제작 개수'(양)로 치환 — 도입≠성과 리스크 내재 |
| 일본형 AX = 외생 충격·안보 프레임 | 손정의 "흑선(黑船)" 비유로 AI를 페리 내항급 위기로 서사화, 사이버 방어를 "필수 비용"으로 규정, 3,000개 중요인프라에 무상 제공 | 비용편익이 아닌 **국가안보 서사로 도입을 정당화**. 동시에 방어 스택 전체를 OpenAI 프론티어 모델에 위탁 — 중국 자급 스택(Ascend·Pangu·Qwen)과 정반대의 '위임형 소버린' |
| 소버린의 세 갈래 (자급/위임/분업) | 중국=풀스택 자급, 일본=미국 모델 합작 위임(SB OAI), 베트남=통신3사 국가분업+글로벌 칩 제휴 하이브리드 | 소버린 AI가 단일 노선이 아니라 지정학 위치별 포트폴리오임을 보여주는 비교축. 한국(하이브리드)·EU 연구의 대조군 |
| HITL·책임의 최종 심급은 인간/기관 | 손정의 "패치 실행은 의사의 수술 결정처럼 인간 몫", Skinner "봇이 범죄 봇에 송금하면 은행 책임", X-Ghost 가드레일·인간 이관 설계 | 아시아 클러스터도 HITL 수렴 — 단 책임귀속을 '중개 기관'에 두는 규제 예응 담론(에어캐나다 판례 프레임과 연결) |
| 채널≠담론 (부재의 신호) | NTT_DATA 26편 전부 채용 홍보(AI 언급 2편) — 일본 대형 SIer의 AX 침묵. SoftBank는 소비자 CM 채널 안에 최상급 이벤트 원문이 공존 | 담론 밀도는 기업 전략 단위로 갈림. 'AX를 말하지 않는 기업'이 대조군으로서 워싱 판별 기준선 제공 |

**AX/DX 스펙트럼**: 스펙트럼 전체가 넓게 퍼진 클러스터 — 실증된 AX는 톈진항(자율운항·근본원인 추론)과 SB OAI 사이버(발굴→검증→패치 자율 파이프라인)에 집중되고, 은행·통신 인프라 사례(Ant·İşbank·Telecom Argentina)는 DX 재구축 위에 자율성을 '선언'하는 DX→AX 이행 단계다. 워싱 위험은 성과지표가 자율 판단이 아닌 양적 지표(웨이크업 정확도, 에이전트 제작 개수)로 치환된 BMW 차내 AI와 SoftBank 전사 운동에서 가장 높다.

※ **신뢰 경계**: 본 클러스터 수치는 사실상 전부 자사(벤더) 발화 — Alibaba 92%/320배, Huawei 10배/99.999%, SoftBank 10,500건 모두 외부 검증 없음. Vietnam 편은 벤더가 아닌 제3자 분석 채널(Vietnam Off The Record)의 투자 브리핑으로 전망치 출처 미상. 자막 자동번역 훼손 심각: 도메인명사→"음악" 치환(HiFS "음악 은행"), Qoder→"코다", OpenClaw→"오픈 클라우드", Ascend→"essence", ASEAN→"아지온", SoftBank 공격 건수 월 5만/6만/60만 혼재 — 의심 수치는 (자막 훼손 가능) 표기했으며 인용 시 원어 재확인 필요. 워싱 위험: Huawei 단문 홍보물·HiFS 하이라이트(수치 없는 신뢰 수사), Alibaba 브랜드 스펙터클 영상군은 높음, ClawTalks·SB OAI 이벤트는 구체 수치·실패 노출(반복 스캔 잔존 취약점 자인)로 상대적으로 낮음.

---

# 자율주행·물리 AI(Tesla·현대차·Zoox·Wayve·Waymo·로보틱스) — AI Transformation 사례집
> **대표 세션/이벤트**: Tesla TERAFAB 발표(2026.4)·Tesla Q3 2023 실적콜·"How Tesla Vision Helps Deploy Airbags Earlier", 현대차그룹 샌프란시스코 AI 서밋 발표(2026.7, 정의선 "우리는 이제 자동차 회사가 아니다"), Zoox "Inside The Ride: Scaling Zoox"·"Blueprints for the Future"·10주년 대담, Wayve "Ride The Wayve"(CEO Alex Kendall×VP of AI Vijay)·CVPR24 E2EAI 워크숍·시리즈D $1.5B 발표·닛산 CEO 요코하마 데모, Waymo SXSW 2024 키노트, Boston Dynamics "Why Humanoids Are the Future of Manufacturing" 웨비나, Siemens CES 2026 키노트 | **관련 채널**: Tesla, Zoox, Wayve, Waymo, Boston_Dynamics, Figure, Nissan, Volvo_Cars, BMW, Mercedes-Benz, Siemens + 키워드(차플레이 '현대차 51조') | **코퍼스 근거**: 실질 정독 12편 + 발췌 검증 다수(Figure는 자막 공동화로 분석 불가)

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Tesla FSD v12 | E2E 자율주행 | "광자 수 입력→제어 출력" 엔드투엔드 신경망. FSD 베타 누적 5억 마일 이상 주행(Q3 2023 시점) | 규칙코딩 제거("하드코딩 불가"의 역전). 훈련 컴퓨트가 "자율성의 근본 제한요소"로 선언 — 비용 중심이 인건비→GPU로 이동 |
| Tesla Vision 에어백 | 안전 AI | 주변 카메라로 충돌 시점·심각도를 사전 식별→에어백 컨트롤러에 전달, 가속도계 판단을 보완 | 전개 결정 최대 70ms 조기화. 기존 차량에 OTA 소프트웨어 업데이트로 배포 — 안전기능이 하드웨어 아닌 소프트웨어 원가로 전환 |
| Tesla TERAFAB | 자체 칩 파운드리(비전) | 리소그래피 마스크 제작→칩 제조→테스트→재설계를 한 건물에서 반복하는 재귀 루프. 엣지/추론(Optimus·차량)용과 우주용 칩 2종 | "기존 전 세계 팹 합계는 필요량의 2%"→연간 테라와트급 컴퓨트 목표. 휴머노이드 연 10억~100억 대 전망(자사 비전 서사, 검증 불가) |
| Zoox purpose-built 로보택시 | 전용 하드웨어 | 핸들·페달 없는 양방향 대칭 차체, 4모서리 센서포드(각 270° 중첩 시야), 마이크 8개로 긴급차량 삼각측량, 조향랙·모터·배터리·브레이크 전 계통 2벌, 133kWh 배터리 | 전용 펌웨어 축별 독립 제어로 궤적추적 오차 5mm~1cm — 개조차(최선 5~10cm) 대비 약 10배. 대용량 배터리로 충전 왕복·배터리 교체 비용 구조 회피 |
| Zoox 하이브리드 AI 스택 | 온보드+오프라인 분리 | 차량엔 명시적 3D 표현·충돌검사 유지 + VLA 'Scene IQ'가 백그라운드에서 플래너에 힌트 제공. 오프라인엔 32B~1,000억 파라미터 파운데이션/월드모델로 시나리오 생성·트리아지 | "센서→운전 전권 이양(E2E)은 거부" 명시. 수백 명이 하던 시뮬레이션 시나리오 수작업 검토를 대형모델이 대체, 지오펜스 4배 확장·정차빈도 수만 마일당 1회 달성 |
| Zoox 안전공학(SDMA) | 검증 체계 | STPA·FMEA+정량 리스크 합산 모델로 잔여 리스크 총량을 수치화해 엔지니어링 우선순위 결정, 안전케이스 문서화 | "목표 미달 시 출시 안 함"을 문화로 제도화. 2023.2 공공도로 첫 주행→SF·라스베이거스 스트립 등 100대 이상 운행, 시간당 3대 생산 체제 |
| Wayve 파운데이션 드라이빙 모델 | E2E 범용 드라이버 | 카메라 5대+NVIDIA GPU 1개, HD맵·라이다 없이 센서 입력+내비 프롬프트→주행 궤적 출력. 영국·미국·독일·일본을 단일 모델로 주행 | 90일간 90개 이상 도시 주행, 그중 절반은 자사 차량 데이터 전무(3자 데이터 학습), 미국 적응에 "몇백 시간". 신규 국가·신규 차량 일반화 4~6개월 — 도시당 재개발 비용 제거 |
| Wayve GAIA·LINGO | 월드모델/VLA | GAIA: 생성형 월드모델로 시뮬레이션-현실 격차 축소·적대적 검증. LINGO-2: 주행하며 자기 결정을 언어로 설명 | 평가·검증도 엔드투엔드 학습으로 확장(수십~수백 페타바이트 학습 데이터). 시리즈D $1.5B로 양산 ADAS~L4 전 스펙트럼 배포 |
| Waymo Driver | 개조형 L4 | 자동차 제조 포기 선언("차는 안 만든다")→완성차 구매 후 드라이버 탑재 | 피닉스 225제곱마일(맨해튼 10배) 24/7 상용 운행(2020.10~), SF 50제곱마일·대기자 20만 명(2024.3 시점) |
| Boston Dynamics Atlas 행동엔진 | 휴머노이드 LBM | 사전훈련(상식·손재주)+원격조작 시연 기반 사후훈련(현장교육)으로 계층형 파이프라인 대체 | 목표: 인간 작업자 수준 신뢰도 99.7% — "아직 해법 없음"을 공개 인정. 하드 자동화가 경제성 없는 고변동 조립공정이 표적 |
| 현대차그룹 피지컬 AI 스택 | 표준연합형 | NVIDIA Thor(1,000TOPS급) 칩+Hyperion 센서 표준+옴니버스 디지털트윈, 로봇 레퍼런스 플랫폼 무료 개방 | 51조 원 국내 투자. 가상 커미셔닝으로 라인 정지(일 수십억 손실) 회피. 표준 개방→생태계 데이터 회수 구조(키워드 채널 해석) |
| Siemens 산업 AI | 산업 스택 | 디지털트윈+엣지 GPU+산업 데이터로 공장·그리드 운영 AI화. "산업 현장에서 환각은 용납 불가" 선언 | 전 세계 제조설비 3대 중 1대에 자사 컨트롤러, AI 전문가 1,500명+. 범용기술 확산주기 "증기 60년→전기 30→컴퓨터 15→AI 7년" 프레임(자사 키노트) |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| 현대차 × NVIDIA | 자율주행·로봇·공장 | Thor 칩·Hyperion 센서 아키텍처를 차세대 플랫폼에 결합, 로봇 레퍼런스 플랫폼 공동 구축, 옴니버스 기반 공장 디지털트윈 | 젠슨 황 "자율주행 제네시스 공동 개발" 발언, 2028년경 양산 로드맵(차플레이 '현대차 51조') | DX→AX† (디지털트윈·표준 인프라는 DX, 자율주행 양산은 로드맵 단계) |
| 현대차 × Waymo | 로보택시 파운드리 | 조향·제동·전력 이중화 등 항공기 수준 안전사양 적용 아이오닉5를 조지아 메타플랜트에서 양산·공급 — "자율주행의 TSMC" 전략 | 아이오닉5 로보택시 "수만 대" 공급 계획(호세 무뇨스 발언 인용, 동 영상) | DX→AX† (현대 역할은 하드웨어 양산, 자율판단은 Waymo Driver 몫) |
| 현대차 × Google DeepMind | 휴머노이드 두뇌 | Boston Dynamics Atlas(신체)+DeepMind(지능) 결합, 전동식 아틀라스를 메타플랜트 아메리카에 우선 투입 | 2028년까지 조지아 연 3만 대 로봇 생산체제. 단, BD 전 CTO 등 핵심인력 딥마인드 이직 — 하청화 리스크 병기(동 영상) | AX† (학습형 휴머노이드의 자율 작업 지향, 다만 2028 목표로 미실현) |
| 현대차 국내 투자 | 데이터 플라이휠 | 새만금 AI밸리 9조(NVIDIA GPU 5만 장 데이터센터 포함)+영남권 공장 AI 팩토리 전환 42조 | 총 51조 원(세부 금액 일부 자막 훼손 가능). "학습(새만금)→탑재(영남)→수집(도로)→재학습" 순환 설계 | DX→AX (인프라 구축은 DX, 재학습 플라이휠로 자율화 지향) |
| Nissan × Wayve | 양산 ADAS | 차세대 ProPilot에 Wayve AI 통합, CEO Ivan Espinosa가 요코하마 데모 탑승 — "닛산을 일본 지능형 차 선두로" | 신규 국가+신규 차량 적응 4개월(통합 수개월+도로학습 수개월), 태풍 폭우 속 무개입 주행 시연(Wayve 채널) | AX (E2E 모델이 주행 판단 수행, 무개입 시연) |
| Wayve × Ford/Qualcomm | 차량·칩 플랫폼 | 시승차는 Ford 차량 기반 2세대 플랫폼. Qualcomm과 양산형 E2E AI 협력(영상 제목 수준 확인) | 카메라 5대+GPU 1개 구성으로 런던 도심 60~75분 무개입 주행 시리즈 공개 | AX (규칙·맵 없이 신경망이 주행 결정) |
| Zoox × Amazon/AWS | 컴퓨트·자본 | 모회사 아마존 지원 하 AWS로 대규모 파운데이션 모델 학습 인프라 운용 | 로보택시 100대+→"내년 수천 대", 신공장 시간당 3대(20분당 1대) 생산. SF 지오펜스가 시내 호출수요 절반 이상 커버, 승하차 지점 5,000곳+ | AX (무인 로보택시 상용 운행 + 대형모델이 수백 명 몫 검증 대체) |
| Tesla × SpaceX·xAI | 칩·우주 컴퓨트 | TERAFAB 3사 공동 추진, 스타십으로 연 1천만 톤 궤도 수송 전제 | "삼성·TSMC·마이크론 칩은 전부 사겠다, 그래도 부족" — 공급망 병목을 수직통합 근거로 제시(자사 발화) | DX(AX 표방)† (컴퓨트 인프라 비전 서사, 자율화 실체 미검증) |
| Boston Dynamics 제조 고객 | 휴머노이드 도입 | 조립라인 대상 아님 — 부품 시퀀싱 등 "하드 자동화가 경제성 없는" 고변동 작업부터 단계 진입, 시연 기반 현장교육 | 자동차 공장 일 1,000대·트림 5종·색상 20종의 변동성을 범용성 근거로 제시. 동적균형 로봇 안전 인증제도 부재 공개 인정 | AX† (학습 로봇이 고변동 작업 판단 지향, 99.7% 신뢰도 미해결 자인) |
| Siemens × AWS·Microsoft | 산업 AI 팩토리 | 중앙 AI 팩토리(하이퍼스케일러)+엣지 GPU 이원 구조로 산업 AI 확산 | CES 2026 키노트 기준(자사 발화, washing 성향 — 개별 고객 수치는 별도 산업 클러스터에서 검증 필요) | DX(AX 표방)† (디지털트윈 기반 DX에 AI 수사, 자율 판단 실증 부재) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 자동차 침묵 4분법 | 같은 산업 안에서 AI 화법이 4단 스펙트럼: 침묵(Nissan·Volvo 자사채널) → 서사적 침묵(Mercedes: AI 무명화+헤리티지로 공백 대체) → 완곡(BMW) → 정체성화(Tesla "AI·에너지·로봇 기업", 현대 "자동차 회사 아니다"). 단 Nissan은 자사채널 침묵하되 Wayve 채널에서 CEO가 적극 발화하는 비대칭 | AX 담론은 산업 단위가 아닌 기업 전략 단위 변수. "말하지 않는 방식"도 전략이며, 파트너 채널 대변은 리스크 외주화(실패해도 자사 브랜드 비손상)로 읽힘 |
| "물리 AI는 절대 틀리면 안 됨" | 디지털 AI의 오류 허용 경제와 단절: Zoox 정량 리스크 합산·전 계통 2벌 이중화, 현대·Waymo 조향/제동/전력 이중화("항공기 수준"), BD 99.7% 신뢰도 미해결 공시, Siemens "환각 불용" | 물리 AI의 원가 본체는 모델이 아니라 검증·이중화·안전케이스. HITL이 '검토자'가 아니라 시스템 설계(리던던시)로 내재화 — AX 비용구조 연구의 별도 축 |
| 아키텍처 3파전 | E2E 전면화(Wayve·Tesla v12: 맵·규칙 제거로 확장 한계비용↓) vs 하이브리드(Zoox: 오프라인 1,000억 파라미터/온보드 경량+명시적 안전장치 분리 — "직감 주행은 안전크리티컬에 부적합") vs 표준연합(현대·NVIDIA: 애플형 수직통합 대 안드로이드형 개방) | 아키텍처 선택=비용구조 선택. E2E는 데이터·컴퓨트로, 하이브리드는 검증 파이프라인으로, 표준연합은 생태계 보조금으로 비용이 이동 |
| 분모 바꾸기(밸류에이션 재정의) | Tesla: 자동차(연 1억 대 시장)→휴머노이드(연 10억~100억 대)·연산(테라와트)·카르다셰프 문명으로 분모 교체. 현대: 완성차 멀티플→"피지컬 AI 솔루션 회사" 재평가 요구. Zoox: 차 판매(일회 이익)→가동률 판매(하루 4%만 쓰이는 차의 96% 유휴 회수) | AX 담론의 극단형 = 시장 자체의 재정의. 수치 대부분이 자사 전망치이므로 '비전 서사'와 '검증된 전환'의 구분이 연구의 핵심 변별 |
| 거버넌스 락인·데이터 플라이휠 | 현대·NVIDIA 로봇 표준 무료 개방→대학·스타트업 데이터가 표준 소유자에 회수(안드로이드 유비). 현대는 동시에 새만금 자체 데이터센터로 내재화 병행 — "빌리면서 배수진" | 표준 개방=사회공헌 수사 뒤의 락인 전략. 소프트웨어 외주 시 "하드웨어 하청화" 리스크를 당사국 담론이 스스로 명시(BD 인력 유출 사례) |
| 에이전트=인력, 첫 적용처는 차 밖 | Zoox: AI 에이전트가 이슈 티켓 근본원인 분석(코드·재시뮬레이션·Slack 종합), 오프라인 대형모델이 수백 명 몫 시나리오 검토 대체. Wayve도 평가·검증을 E2E 학습으로 대체 | 자율주행사의 실질 AX 1호는 도로가 아닌 자사 개발·QA 파이프라인 — "에이전트=인력" 프레임이 물리 AI 기업 내부에서 먼저 실현 |
| 반워싱 검증자 포지션 | BD "모든 휴머노이드는 아직 1단계(하드웨어 신뢰성)", "고객은 옳고 우리가 틀렸다(another bitter lesson)", 인증제도 부재 인정. Zoox도 "완벽한 성공 아직 아님" 반복 | 하드웨어를 실제로 파는 쪽일수록 겸손한 공시(검증자의 법칙). 키노트형 채널(Tesla TERAFAB, Siemens CES)과의 수사 낙차 자체가 워싱 판별 지표 |

**AX/DX 스펙트럼**: 이 클러스터는 주행·작업을 AI가 직접 판단하는 순수 AX(Wayve·Zoox 계열)와, 디지털트윈·칩·양산 인프라라는 DX 기반 위에 자율화를 얹는 DX→AX 이행(현대차 계열)으로 양분되며, 휴머노이드(DeepMind·BD)는 AX 지향이나 신뢰도 미해결로 미실현 단계다. 키노트형 비전 서사(Tesla TERAFAB, Siemens)는 자율 판단의 실증 없이 AX 수사를 쓰는 워싱 위험군으로 별도 표기했다.

※ **신뢰 경계**: 본 사례집의 수치는 거의 전부 자사(또는 해설 채널) 발화 기준이며 제3자 검증 없음. **자막 오역 위험 실증**: Wayve $1.5B 영상에서 "autonomy→자율주행 음악 시스템", "robotaxi→로봇 세금 징수" 치환 확인, "제로샷 일반화"가 "일반화 능력이 전혀 없는 것으로"로 반전 오역 추정(15% 미학습 도시 관련), Zoox→"주크스/스즈키" 오기, Zoox 영상 내 "GPT-5.5 5조 파라미터"는 전언·미검증, 현대차 51조 세부 금액("3조 8,억" 등) 자막 훼손 가능. **워싱 위험 채널**: Tesla TERAFAB·Optimus 10억 대는 검증 불가 비전 서사, Siemens 키노트는 catalog상 washing 판정 다수, Waymo 셀럽 시리즈는 정량근거 빈약. Figure 채널은 자막 공동화(2~12단어)로 분석 제외. Zoox 과거 수집분 중 동명 게임 유튜버 오수집 이력 있어 D3 재수집분만 사용.

---

# 통신·주권·국가 클러스터 (Orange·Telefónica·Nokia·Telenor·Swisscom·Scale AI) — AI Transformation 사례집
> **대표 세션/이벤트**: VivaTech 2026(Orange Tech10·Agentic AI 텔코 패널·헬스AI 신뢰 패널·포용 핀테크 패널), MWC 2026(Zerbib 인터뷰, Telefónica "El futuro del SOC es AI-native"), Orange OpenTech 2025, Telefónica Capital Markets Day 2025, Nokia AI-RAN 플랫폼 발표·Elisa/NVIDIA 웨비나, Scale AI ALL IN 2024/2025, Telenor Telco Tech Talks | **관련 채널**: Orange, Telefónica, Nokia, Telenor, Swisscom, Scale_AI | **코퍼스 근거**: 실질 정독 15편 + 발췌 검증 2편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| Orange Dino 2 → Live Intelligence | 사내 GenAI→B2B 플랫폼 | 직원 프롬프트·문서를 받아 맞춤 "어시스턴트" 생성, OpenAI·Anthropic·Google·Mistral 멀티모델을 EU 내 데이터 상주·비학습 계약으로 제공 | 목표 1만→실사용 10만+명(직원 80%), 어시스턴트 2만+개, 섀도우AI 억제 후 B2B 상품화 |
| Orange 계층별 주권 참조아키텍처 | 거버넌스 | GPU·서버·LLM·오케스트레이션을 제어점으로 분해, **데이터+하네스(에이전트 오케스트레이션)만 자국 통제**, 나머지는 오픈소스·유럽 생태계로 대체 | "주권은 흑백 아님·주권에는 비용"을 명시한 등급제 주권 상품화(Zerbib) |
| Orange 4C→5C 신뢰 프레임 | 담론/방법론 | Control·Choice·Competence·Critical scale(Berger) + 헬스 5번째 C=**Comprehension**(설명가능성, Curie 연구소 딥러닝 블랙박스 해명) | 신뢰를 운영 전략으로 전환, 프랑스 영상의학 클리닉 1/3에 Orange SW 공급 |
| Orange Money / Max It | 핀테크 인프라 | 모바일 지갑·슈퍼앱(KYC까지 모바일), 결제 API를 외부 핀테크에 개방 | 월 활성 5,000만+, 월 이체 200억 유로(자막상 달러/유로 혼용), **세네갈 GDP 11%**(생태계 기여 연구), Max It 2,000만→3년내 7,500만 목표 |
| Telefónica AI-native SOC | 보안 운영 | IT·OT 융합 관제를 공동설계, AI 에이전트가 반복·저부가·결정론적 업무를 자동화하고 인력은 회복력 업무로 재배치 | 인적 오류 감소·글로벌 확장성(자사 발화, 정량 없음) |
| Telefónica Tech | B2B 디지털 | 주권형 IoT 클라우드·인더스트리4.0·사이버 서비스 "제품 공장" | 사이버 매출 2배 목표, capex/매출 12.5%→2030년 ~11%, AI로 OPEX·CAPEX 최적화(CMD 2025) |
| Nokia AI-RAN (AnyRAN + NVIDIA ARC-Pro) | 무선 인프라 | 커스텀 칩→**머천트 실리콘**(Dell·Supermicro·Quanta GPU서버 포함) 3개 하드웨어 트랙, AI 알고리즘(딥리시버·MU-MIMO 페어링·채널추정)으로 스펙트럼 효율 개선 | 기존 플랫폼서 20%+ 검증, 2028년 2배 목표. **하드웨어 가격은 전세대 수준 = 같은 투자로 용량 2배 = cost-per-delivered-bit 절반, "no GPU premium"** |
| Nokia AI-그리드/분산추론 | 엣지 컴퓨트 | 기지국을 RAN+AI 추론 겸용 자산화 | NVIDIA 추산: 2030년 컴퓨트 수요 60%가 추론, 25개 통신사가 이미 AI 인프라 구축 중 |
| Scale AI 운영지표 레이어 | 측정 방법론 | AI 모델 지표와 사업 KPI 사이에 "운영 지표"(재고↓·리드타임↓ 등) 중간층 삽입해 귀속(attribution) 문제 해소 | 190개 프로젝트 상향식 도출, 효율·정확도·생산성·수익관리 4범주, "중앙값<평균=KPI 과대계상" 자체 공개 |
| Scale AI 특허 10단계 판별 도구 | IP 전략 | 탐지가능성→가치제안 정렬→목표 명확성→시점(Goldilocks)으로 특허/영업비밀 분기 | Todd Bailey: "내가 읽은 AI 특허의 **96%는 무효(비효과)**, 아이디어 90%는 1단계 탈락" |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| H Company × Orange | 컴퓨터유즈 에이전트 | 마우스·키보드·화면 조작 에이전트를 Orange 플랫폼·마켓플레이스에 통합 | 병원 도입 시 간호사 전산 수작업 감소→**응급실 대기시간 단축**(비재무 ROI 사례) ("Agentic AI, Trust & Scale") | **AX** — 컴퓨터유즈 에이전트가 화면을 보고 스스로 판단·조작, 간호사 역할 재정의 |
| Dataiku × Orange | 에이전틱 데이터 플랫폼 | 재무 데이터소스 결합 자동화, 조달·법무 프로세스 재설계 | 수 주 걸리던 작업→수 시간. 반면 타사 "마법지팡이" 실패담: 데이터레이크의 10년 전 프로모션 점수를 고객에 발송 ("Impact of Agentic AI") | **AX** — 에이전트가 데이터 결합을 수행하고 조달·법무 워크플로 자체를 재설계 (실패담이 자율 실행의 리스크를 방증) |
| 텔코 얼라이언스 12사 (Orange·Telefónica·KPN·STC 등) | 스타트업 공동 발굴·투자 | 12개 통신사가 에이전틱 AI 스타트업을 공동 심사·확산 | 3.6억~15억+ 고객·70개 시장 접근 제공 (동 패널) | **DX**† — 투자·확산 채널 구축이지 AI 자율 판단 사례 아님(대상이 에이전틱일 뿐) |
| Institut Curie × Orange Business | 의료 XAI | 암 원발부위 탐지 딥러닝의 설명가능성 확보→의사가 환자에 결정 근거 설명 | 연 7,000명 신규 환자 대상 질환 ("La confiance…IA en santé") | **DX→AX**† — 딥러닝이 원발부위를 판단하나 최종 결정·설명 주체는 의사(HITL 유지) |
| Bleu(MS Azure 주권클라우드)·Cloud Avenue·EU AI 기가팩토리 | 주권 인프라 | Orange가 주권 클라우드 합작+자체 프라이빗 클라우드+기가팩토리 컨소시엄 참여 | 헬스데이터 호스팅 인증 보유 (동 패널) | **DX** — 클라우드·인프라 구축, AI 자율 판단 요소 없음 |
| Elisa × Nokia × NVIDIA | AI-RAN 상용화 | 핀란드 PoC(ARC-Pro+AnyRAN)→자율 네트워크 로드맵 | 2026 하반기 실증, **2027년 말 상용 SW** 목표. 업링크에서 AI 트래픽 초기 흔적 관찰 ("Accelerating AI-RAN") | **DX→AX**† — 현재는 인프라 PoC(DX), "자율 네트워크"는 로드맵 단계의 목표 |
| T-Mobile US·SoftBank·Indosat × Nokia | AI-for-RAN 검증 | 채널추정·링크적응·CA 알고리즘 구조화 PoC | 스펙트럼 효율 20%+ 검증, 네트워크상 일 100조 토큰·연 1.3조 AI 상호작용 주장 (AI-RAN 플랫폼 발표) | **DX**† — AI 알고리즘이 정해진 최적화 문제를 푸는 구조화 PoC, 워크플로 재설계·자율 분기 근거 없음 |
| Scale AI(캐나다 연방 클러스터) × 산업 190개 프로젝트 | 국가 매칭펀딩 | 농업 작황·크레인 배치·AlayaCare(자막 표기 "allayia") 홈케어 인력 배치 등 AI 도입 공동 자금 | 2018년~ 총 **$7.5억**(자체 $2.8억, **배율 4.7x**), SME에 자금 2/3, 기대효과 $70억, StatCan: AI 사용 기업 1년새 2배 ("6 years of Scale AI") | **DX→AX**† — 포트폴리오 혼재: 배치·예측 최적화에 AI 판단 요소 있으나 다수는 데이터 파이프라인형 도입 |
| Telefónica CMD 2025 (EU 주권 프레임) | 투자자 담론 | Draghi 보고서 인용: 격차 해소에 2030년까지 €7,500억 투자 필요, 통신사 사이버방어 기회 €100억~220억(2035) | 2025년 런던·브뤼셀·베를린·더블린 공항 사이버공격 언급, 5G SA 가용성 중국 77% vs 유럽 2%(자막 훼손 가능) | **DX**† — 투자자 담론·시장 기회 계량이지 전환 실행 사례 아님 |
| 오렌지 아프리카·중동 | 포용 AX | 월로프어·스와힐리어·링갈라어 LLM, 디지털센터 50곳, 세계은행 여성 단말 보조금 | 3년 capex €50억, 2030년까지 300만 명 AI·데이터·사이버 교육, 오렌지벤처스 약 $5,000만 투자, 코트디부아르 은행계좌 <200만 vs 모바일머니 지갑 2,500만+ ("Social Inclusion and Fintech") | **DX(AX 표방)**† — "포용 AX"로 명명되나 실질은 인프라·교육·현지어 LLM 구축(디지털 접근성 확충) |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| **state 축 = 제3의 담론 주체** | 벤더(공급)·고객(수요) 이분법 밖에서 국가·클러스터가 AX를 조직: Scale AI는 "지분 없는 another pair of eyes"로 정부가 촉매자 역을 자임, EU는 Draghi 보고서·기가팩토리로 주권 투자를 정당화 | AX 담론 지형에 vendor/customer/state 3주체 모델 필요. state 내부도 블록(EU 기술주권 vs 캐나다 생산성 펀딩)으로 분화 |
| **주권의 계층화·상품화** | Orange는 주권을 흑백이 아닌 제어점 스택으로 분해(데이터+하네스만 통제)하고 "주권에는 비용이 따른다"고 고객에 등급별 판매. Telefónica는 주권을 사이버방어 시장 기회(€100~220억)로 계량 | 거버넌스 락인의 유럽형 변종: 주권 자체가 SKU가 되어 컨텍스트·오케스트레이션 계층 장악 경쟁과 직결 |
| **분모 바꾸기의 인프라판 vs 반(反)분모스왑** | Nokia "같은 하드웨어 가격, 비트당 비용 절반, no GPU premium"은 GPU 비용을 분모 재정의로 은폐하는 인프라판 분모스왑. 반대로 Scale AI는 "새 ERP·인프라 기다리지 말고 가진 데이터로 지금 측정"+운영지표 중간층으로 기존 지표 고수 | 분모스왑 진영과 측정주의 반스왑 진영의 대립 축 확보. KPI "중앙값<평균" 공개는 워싱 판별 도구 |
| **95% 실패 의례의 도메인 이식** | "마법지팡이 효과"(Orange/Dataiku 텔코판), 특허 96% 무효(Scale AI IP판), Zerbib의 5G 자기비판("원격수술 약속은 실현 안 됐고 5G로 수익화 못 했다") | 실패율 수사가 도메인을 갈아타며 반복=책임전가·전문가 관문화의 범용 문법. 단 자기비판형(Zerbib)은 신뢰 화폐로 기능하는 안티워싱 변종 |
| **에이전트=인력, HITL의 재정의** | Dataiku "미래엔 CHRO처럼 에이전트를 관리하는 조율자 필요", Telefónica SOC 인력 재배치, Zerbib "AI가 코드리뷰까지 하면서 통제점 자체가 이동—초기 규칙 설계+지속 감사로 HITL 재구성", 인간 조작↓·감독↑(Alliance 패널) | HITL이 '검수자'에서 '규칙 설계자·에이전트 인사관리자'로 승격되는 담론 전환점. 토큰 수요 기하급수(중국의 토큰 시장 규제 실험 언급)와 결합 시 비용구조 변수 |
| **같은 산업, 정반대 담론 온도(B2B 열광 vs B2C 위험)** | Nokia·Orange·Telefónica는 B2B 전환 열광, Swisscom은 최대 분량 콘텐츠가 "Kids & KI" 학부모 교육—AI를 성장동력이 아닌 관리할 위험으로 서사화. Telenor는 CEO 대담(BT CDO: 터치리스 운영, CRM 폐지 검토, 레거시 지출 매년 축소, "빠르게 실패하고 축하하라")로 조직·레거시 담론 특화 | 청중(투자자/기업/소비자)이 담론 표면을 결정. ROI·KPI 부재 채널(Swisscom 광고, Telefónica 브랜드 클립 다수)은 워싱 여부 판정 불가 지대 |

**AX/DX 스펙트럼**: 이 클러스터는 진성 AX가 Orange의 에이전트 사례 2건(H Company·Dataiku)에 집중되고, 나머지는 인프라·펀딩·담론 중심의 DX 또는 로드맵 단계의 DX→AX에 몰려 있다. "자율 네트워크"(Nokia AI-RAN)와 "포용 AX"(Orange 아프리카)처럼 AX 명명이 실질(최적화 PoC·디지털 접근성 구축)을 앞서가는 워싱 위험이 상존하며, 특히 자사 발화만 있는 사례는 판정 자체가 보수적일 수밖에 없다.

※ **신뢰 경계**: 전 채널이 자사 발화(키노트·CMD·자사 웨비나) 기준—Nokia 스펙트럼 효율 2배·Telefónica 사이버 기회액·Orange 직원 80% 등은 외부 검증 없음. Scale AI 수치($7.5억·4.7x·$70억)는 정부 클러스터 자기보고이나 "기대효과" 명시·KPI 과대계상 자인 등 상대적 절제. 자막 오역 위험 높음: 도메인명사→"음악" 치환(Nokia·Telefónica·Orange 전반), 인명 훼손(Ruza→"러시아", ARC-Pro→"Octopro", Telenor→"터미널", AlayaCare→"allayia", Julaya 추정→"주미아"), Orange Money 이체액 달러/유로 혼용, Telefónica 5G SA 수치 훼손 가능. Telefónica 채널은 CMD·SOC 2편 외 대부분 브랜드·사회공헌 콘텐츠, Swisscom은 소비자 교육·광고 중심—두 채널 모두 기업 AX 실증 부재로 워싱/실체 판별 자체가 제한됨.

---

# 생성 미디어 · 개발도구 · 수요기업 클러스터 — AI Transformation 사례집
> **대표 세션/이벤트**: ElevenLabs Summit(Warsaw·London 2026), Runway AI Festival 2026 · AI Film Festival(NY/LA), Zapier AI Benchmark 웨비나 · Build-Along Workshop, Siemens 하노버메세/CES 2026 연계 대담(Pringles·NVIDIA·Why Latin America), Unilever BNP Paribas CEO Conference 2026 · Deutsche Bank Global Consumer Conference 2026 · Q2/H1 2026 실적발표, LinkedIn 2026 Labor Market Report | **관련 채널**: ElevenLabs, Runway, Stability AI, Replit, Zapier, Siemens, Schneider Electric, Unilever, GE HealthCare, IQVIA, Philips, LinkedIn | **코퍼스 근거**: 실질 정독 18편 + 표적 발췌검색 10여 편

## 1. 핵심 기술 스택
| 기술/제품 | 구분 | 핵심 기능 | AI 전환 임팩트 |
|---|---|---|---|
| ElevenLabs Ads Engine·ElevenCreative 더빙 | 생성 광고 | 영어 광고(영상·정지이미지) 입력→Gemini 번역+용어사전(AI→KI)·글자수 제약·성우 더빙·화면비 변환→Google/Meta 직접 송출 | 4인 팀·신규채용 0으로 7개 언어 확장(본문상 9개 언어), ROAS 7.16, 증분 전환가치 $3.78M(자사 발화, lift test 진행 중) |
| ElevenAgents(음성 에이전트) | 대화형 CX | 고객 통화 입력→언어 전환·라우터 원격진단 툴콜·업셀·이메일 요약 발송 | DT 수백만 고객 대상 L1 자동화; "디지털 채널은 상호작용의 11%뿐, 가치는 음성에" |
| Runway Gen-4/4.5·Aleph·Workflows | 생성 영상 | 텍스트/이미지/기존 푸티지 입력→영상 생성·VFX·캐릭터 일관성 | 정량 성과 부재. "민주화·게이트키퍼 제거" 서사 중심(워싱 경계) |
| Stability AI Brand Studio | 브랜드 생성 | 브랜드 가드레일+소량 캠페인 이미지 입력→커스텀 파인튜닝 모델+프리셋 워크플로 출력 | 프롬프트 엔지니어링 노동 제거, 지역화 8~12주→2주 목표(가상 브랜드 롤플레이 기반) |
| Replit Agent 3 | 바이브 코딩 | 자연어 입력→앱 빌드+Playwright 자가 테스트(최대 6시간 실행, 200분+ 자체 디버깅) | 비개발자 창업 가능("엔지니어 배경 없는 창업자가 유리") |
| Zapier MCP·Agents·Automation Bench | 오케스트레이션 | AI 모델에 9,000개 앱·55,000개 액션 연결(구영상 8,000/30,000), 자체 벤치마크로 모델 선택 | 600개 실automation 과제에서 최고 모델(Anthropic) 성공률 70.17% — "완전 자동화는 아직 미완" 신호 |
| Siemens 디지털트윈+AI 공정제어(Senseye 포함) | 산업 AI | 공정·에너지 센서데이터 입력→실시간 공정 최적화·예측 유지보수; 규칙기반→목표기반("이것을 하라"만 지시) | Pringles 라인당 생산량 2~10%↑·에너지 7%↓ 목표(Kutno 검증→확산) |
| IQVIA Vigilance Platform | 제약 안전성 | 부작용 보고서 입력→OCR/GenAI 추출·자동 코딩·신뢰도 점수→고신뢰는 자동 처리, 인간은 예외만 검토 | 수작업 몇 시간→몇 분(자사 데모) |
| GE HealthCare 초음파 AI 가이드·CardioLab AI.i | 의료 AI | 초음파 영상 입력→해부구조 하이라이트·워크플로 자동화 | "자율주행차가 아니라 GPS" — 증강·HITL 프레임 명시 |
| Schneider Electric grid-to-chip | AI 인프라 | 그리드→칩 전력 아키텍처 설계 | 랙 밀도 5~15kW→30/100kW→1MW+ — AI를 전력수요 유발자로 규정하고 자사 기회화 |

## 2. 파트너·고객사별 AI 전환 사례
| 파트너/고객 | 협력 영역 | AI 전환 내용 | 현황/성과(수치) | AX/DX |
|---|---|---|---|---|
| ElevenLabs 자사(Tim Davis, 퍼포먼스마케팅 총괄)·Hasbro 캠페인 | 광고 국제화 | 스프레드시트+Gemini 수작업→자체 Ads Engine으로 번역·더빙 일체화, "생존 징후 테스트" 후 확장 | Google Ads Impact Award, 4인·ROAS 7.16·$3.78M(「ElevenLabs Built an AI Ad Tool That Drove $3.78M」) | AX |
| Deutsche Telekom(Jonathan Abramson CPDO) | 음성 CX 대량 배포 | 지식이 매뉴얼·주간메일·부족지식에 산재→SOP 15,000개를 Gherkin 형식으로 기계가독화; 4C(정확·침착·툴실행·지속개선); 3개월 초과 프로젝트는 착수 금지 | 독일 연 8,000억 통화(음성 분) 접점, L1 자동화→인간은 품질관리·저니 설계로(「How Deutsche Telekom Is Deploying AI Voice Agents」) | AX |
| BCG·Naturgy·Konecta | 에이전트 프로덕션 | BCG "기술 10%–인프라 20%–사람·프로세스 70%" 프레임, 도입기업 80%가 사업부 재편 진행 | 통화 35만 건+ 처리, "최고 상담원 수준"(「How BCG, Naturgy, and Konecta Are Deploying AI Agents」) | AX |
| Netflix(Girish Balakrishnan)·Bento Box(Joel Kuwahara)·Ron Howard·Roger Avary | 생성 영상×할리우드 | 축제 대담으로 권위 확보. Avary는 AI 제작사 설립 "연 52편·티켓 5달러" 야망(미실현); Howard는 "디지털이 비용 줄일 줄 알았지만 관객 기대치 상승으로 되레 비쌌다" 자인 | 전 세션 정량 성과 0 — 유명인 권위=워싱 위험(Runway AI Festival 2026) | DX(AX 표방)† |
| FaZe Apex(Yusuf)×Replit | 크리에이터 창업 | TryNearBy(로컬비즈니스 발견 플랫폼, 로컬광고 시장 연 $1,500억) 비개발자 단독 구축 | 100k ARR 도달 — "예전엔 4~5년 걸리던 성과"(「FaZe Apex: Between Builders」) | AX |
| Replit 내부(리드 AI 엔지니어) | 자가검증 | Agent 3 self-verification으로 내부 코드품질 Agent 2 대비 대폭 개선→출시 후 구버전 코드 만나자 "이건 쓰레기"라며 폭주(맥락 이탈) | 자가검증의 분포 이탈 실패 사례 공개(「Inside Replit Agent」) | AX |
| Zapier×Anthropic·Eric Ries | 자동화 인프라·메타비판 | Claude 스킬/커넥터, AI의 실제 4직무(커뮤니케이터·사무·분석가·조정자) 규명; Ries는 "LLM 정신병·슬롭 팩토리·근육 위축(탈숙련)" 경고 | Automation Bench 70.17%(600과제); 비용절감 CEO에 "책임을 안 묻는다" 비판(「Eric Ries on Vibe Coding」) | DX→AX |
| Pringles/Kellanova×Siemens | 공정 AI | 디지털트윈·AI 공정제어·에너지관리·예측보전 4종 선정, 마일스톤 대신 "사망 기준(death criteria)": 3개월 내 긍정 평가 없으면 중단 | 라인당 2~10% 증산, 에너지 7% 절감 목표; 라틴아메리카 제조 AI 도입 18%·산업 SME 5%(기업의 99%가 SME) | DX→AX |
| Unilever(Fernando Fernandez CEO) | R&D·마케팅 P&L 직결 | R&D 활동 80% 육체노동→80% 디지털(특허 15,000·실험/소비자 데이터 2,500만 건→수초 내 1만 시나리오); LLM 검색·증명·전환을 "대형브랜드 해자"로 규정, 50개 브랜드·20개 시장 LLM 순위 일일 추적 | 혁신주기 2~3년→9~12개월(Deutsche Bank 콘퍼런스); 크리에이터 1만→30만(2년), 영상 수명 4일; 월드컵 크리에이터 5만 명·오디언스 6억(Q2/H1 2026) | DX→AX† |
| GE HealthCare(마취과 KOL) | 초음파 AI | AI 가이드를 GPS로 한정, 맹신 금지 교육 | 정량은 KOL 강연에만, 단문 제품데모는 무근거(포맷별 양극화) | DX† |
| IQVIA | 제약 R&D·안전성 | Vigilance 예외기반 자동화; 일본 임상개발 기간 데이터로 효율화 서사 | 임상개발 116개월(2004)→52개월(2019); 대형제약 15사 R&D 지출 $190B(IQVIA Institute 브리프) | AX |
| Philips(임원 대담) | 의료 워크플로 | "제품 중심→생산성 중심 회사" 선언, 임상의 신뢰 3주체(병원·의사·환자) 구조화 | MRI 검사 시간 절반~1/3 단축 발화(방법론 미제시) | DX(AX 표방)† |
| LinkedIn(자사 데이터) | 노동시장 반증 | 13억 회원 데이터로 "채용 둔화의 원인은 AI가 아니라 금리", AI 노출도–채용변화 무상관, 신입도 동일 곡선 | AI 신규 일자리 130만("뉴칼라"); Fortune 100은 인력 비례 증가 없이 인당 매출 성장(2026 Labor Market Report) | DX |

## 3. 핵심 인사이트
| 주제 | 핵심 내용 | 시사점 |
|---|---|---|
| 정량성의 역설 | 인력·비용 절감을 직접 파는 벤더(ElevenLabs)는 ROAS 소수점 둘째 자리까지 제시하나 자사 검증이고, 권위를 파는 벤더(Runway)는 수치가 0. 실체 있는 수요기업(Unilever·Siemens)은 범위값(2~10%)·기간값으로 말함 | 정량 정밀도는 실증 강도가 아니라 '판매 대상'의 함수 — 수치의 자릿수 자체를 워싱 판별 변수로 코딩 가능 |
| 도입 원가구조의 노출 | Stability What-To-Expect는 파인튜닝 vs 프롬프트, 지역화 8~12주→2주, IT·조달·인뎀니피케이션·파일럿 성공기준까지 세일즈 원가구조를 통째로 공개 — 단 실고객 아닌 가상 브랜드 롤플레이 | AX 도입비용의 실제 구성(데이터 준비·조달 마찰·커스터마이징)이 모델 성능보다 큰 변수임을 벤더 스스로 인정한 문서 |
| 에이전트=인력, 인간=예외처리자 | DT(L1 대체→인간은 QC·저니 설계), Zapier(4직무 명명), IQVIA(예외기반 검토) — HITL이 '상시 감독'에서 '예외 큐 처리'로 축소되는 동형 패턴 | "대체 아닌 증강" 수사와 달리 실무 설계는 인간 개입 지점을 체계적으로 감축 — 인건비 종속변수(K1)와 직결 |
| 준비 노동이 진짜 병목 | DT SOP 15,000건 Gherkin화("우리의 해자는 학습 루프"), Unilever 데이터 2,500만 건 정비 — LLM이 아니라 암묵지 형식화가 최대 투자 | 분모 바꾸기의 이면: 모델 비용은 하락해도 조직 지식의 기계가독화 비용이 AX 원가의 본체 |
| 자가검증의 취약성 | Replit Agent 3는 내부 분포에선 품질 향상, 실고객의 구버전 코드 위에선 오작동 — 벤더가 실패를 자진 공개한 드문 사례 | eval·벤치마크 전장 명제의 미시 근거; Zapier 70.17%와 함께 "에이전트 신뢰성 미완"의 공급자 측 자백 |
| 수요기업의 P&L 번역 vs 반-워싱 대조군 | Unilever는 AI를 혁신주기·콘텐츠 단가·LLM 검색 해자라는 손익 언어로 CEO가 직접 번역(최상급 담론-재무 연결); Siemens는 death criteria로, LinkedIn은 "AI 아닌 금리"로 과열 서사를 스스로 기각 | AX 담론의 신뢰도는 '벤더의 배수 수사'가 아니라 '수요기업이 자기 P&L에 어느 항목으로 기입하는가'로 검증해야 함 |

**AX/DX 스펙트럼**: 이 클러스터는 에이전트가 자율 판단·실행하는 순수 AX(음성 CX의 DT·BCG·Konecta, 코딩의 Replit, 예외기반 자동화의 IQVIA)와, 디지털트윈·데이터 정비·규칙 자동화 기반 위에 목표기반 제어나 신뢰도 분기를 얹는 DX→AX 이행형(Siemens·Zapier·Unilever)으로 양분된다. 정량 성과 없이 권위·선언에 의존하는 Runway 할리우드 대담과 Philips는 DX(AX 표방) 워싱 위험이 크고, GE HealthCare("GPS")·LinkedIn은 자율화가 아닌 증강·분석에 머문다.

※ **신뢰 경계**: ElevenLabs 전 사례·IQVIA 데모·Philips 수치는 자사 발화 기준(ElevenLabs $3.78M은 lift test 진행 중 자인). Runway는 유명인 권위 의존·수치 부재로 워싱 위험 최고, Stability 사례는 가상 브랜드 롤플레이임. 자막 자동번역 오염 심각 — 본 클러스터 원문에서 "음악"이 산업/업무 명사를 치환(LinkedIn "음악 산업 채용"=전 산업, ElevenLabs 인터뷰 다수), DT 8,000억 통화·Replit 200분 등 전언 수치는 (자막 훼손 가능) 유보 필요. 수치 인용 시 영어 원자막 파일(DT·Stability·Replit 일부) 우선.

---
