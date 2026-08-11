# CASEBOOK_THEORY — 문헌 기준 AX/DX 재판정 사례집

> 2026-08-11. `docs/CASEBOOK.md`의 135개 사례를 **코퍼스 합의 정의 대신 학술 문헌의 DT/AT 판별 기준으로 전량 재판정**한 이론판.
> 각 사례 행: 사례명 · **YouTube 출처(채널·영상)** · 재판정 · 범위 · 기존 판정 · **논문·페이지를 명시한 판정 근거**.
> ⚠️ 수치·주장은 발표자(대부분 자사) 발화 기준(독립 검증 아님). 원 논문 인용문은 연구자 제공 발췌 기준이며 원문 PDF 재대조는 하지 않았음.

---

## 1. 판정 기준 문헌

| 문헌 | 정의/구분 | 이 재판정에서의 역할 |
|---|---|---|
| **Vial (2019, p.4)** | DT = "a process that aims to improve an entity by triggering significant changes to its properties through combinations of information, computing, communication, and connectivity technologies" | **실체(=조직) 속성의 유의미한 변화**가 정량 증거로 있는가. 제품의 자율성이 아니라 조직의 변화가 기준 |
| **Verhoef et al. (2021, p.891)** | DT = "a company-wide change that leads to the development of new business models". 하위 단계: digitization(아날로그→디지털 변환) / digitalization(기존 프로세스의 기술적 개선) — 둘 다 DT가 아님 | **전사성 + 신규 비즈니스 모델** 관문, 그리고 D1/D2 사다리 |
| **Holmström (2022, p.331)** | DT = "The profound transformation of organizational activities, boundaries, and goals" | **활동·경계·목표 3요소 중 몇 개가 변형됐는지** 세는 체크리스트 |
| **Raisch & Krakowski (2021, p.192)** | automation(기계가 인간 과업 대체) vs augmentation(인간-기계 긴밀 협업) — 과업 수준 개념 | AI 자율성이 있어도 **단일 과업 수준에 머문 사례**의 분류 축 |
| **Neumann et al. (2024, p.120)** | 성숙도: assessing(실험 착수) / determined(실험 초과) / managed(전사 적용 프로세스) | 각 사례의 **범위(scope)** 열 + 선언·데모 단계를 전환으로 호명하는 워싱 판별 |
| **Wamba et al. (2020, p.864)** | 전환의 실질이 프로세스 수준 변혁효과(TE)로 격하되는 패턴 | 과업/프로세스 수준 판정의 보조 근거 |

**재판정 범주**: **D1**(digitization) · **D2**(digitalization) · **D3-auto/D3-aug**(과업수준 AI 자동화/증강 — AI가 판단하더라도 전환 요건 미달) · **AT**(① Vial 정량 증거 + ② Holmström 3요소 중 2개 이상 변형 또는 Verhoef 신규 BM) · **워싱**(전환 표방하나 실질 D2 이하 또는 선언·데모·간증뿐). 이행 실증이 있으면 "(이행 중)" 부기. †(근거 약함)는 보수 판정.

---

## 2. 재판정 결과 총괄

**분포**: D1 **2** · D2 **38** · D3-auto **30** · D3-aug **25** · **AT 7행(6개 조직)** · 워싱 **33** (총 135)

**기존 판정 → 재판정 교차표**:

| 기존 \ 재판정 | AT | D3-auto | D3-aug | D2 | D1 | 워싱 | 계 |
|---|---|---|---|---|---|---|---|
| AX (41) | 6 | 24 | 5 | — | — | 6 | 41 |
| DX→AX (40) | 1 | 6 | 19 | 9 | — | 5 | 40 |
| DX (37) | — | — | 1 | 29 | 2 | 5 | 37 |
| DX(AX 표방) (17) | — | — | — | — | — | 17 | 17 |
| **계 (135)** | **7** | **30** | **25** | **38** | **2** | **33** | 135 |

**AT 충족 7행 (6개 조직 — 무신사는 2개 클러스터에 중복 등재)**:

| 조직 | 범위 | 충족 근거 요약 | 출처 채널 |
|---|---|---|---|
| 톈진항 (PortGPT) | managed | IGV 92대 3년+ L4 운영(Vial 정량) + 활동·경계 변형 | Huawei |
| HG Capital | managed | 스쿼드 9→2·1,000 인스턴스 + 인력 구조 재정의 | Anthropic |
| 무신사 (×OpenAI) | managed | 연 4.5억 SaaS 내재화 + 활동·경계·목표 3요소 변형("채용 기준의 패러다임 전환") — 단 3자 후기 경유 | 3자 후기(키워드 수집) |
| 삼성전자 시장조사 (SDS 수행) | determined | 연 100억 외주 기능 내재화(경계 변형) + 실제 인터뷰 80~95% 일치 | IT조선(키워드 수집) |
| SoftBank×OpenAI (Daybreak) | determined | 취약점 10,500건 발굴→패치 자율 루프 + 보안 기능 재편 | SoftBank |
| ElevenLabs·Hasbro | determined | 4인 팀 워크플로 재설계 + 내부 도구의 Ads Engine 상품화(Verhoef 신규 BM) | ElevenLabs |

---

## 3. 핵심 발견

1. **기존 "AX" 41건 중 문헌 기준 AT 생존은 6건(15%)**. 강등 사유 1위는 "단일 과업/프로세스 수준"(29건 → D3) — AI의 자율 판단이 실재해도 Raisch·Krakowski(p.192)의 automation/augmentation, 즉 과업 수준 개념에 머물며, Verhoef(p.891)의 전사성·신규 BM과 Holmström(p.331)의 3요소 다중 변형에 도달하지 못함. AIG(정확도 75→90%)·LG(100% AI 스케줄 공장)·Deutsche Telekom(범위는 managed)처럼 정량 성과가 강한 사례도 예외가 아님.
2. **워싱이 17건 → 33건으로 배증**. 기존 "표방" 17건에 더해, 선언·간증·데모·로드맵뿐인 사례 16건(EY·BNY·Commonwealth·우리은행 175개 설계·SAP 제로 고객·현대차×DeepMind·베트남 3사 등)이 Neumann(p.120) assessing 단계의 전환 호명으로 추가 판정됨. **문헌이 지적한 "정의 없이 조작화로 직행"하는 개념 공백이 실무 담론에서 그대로 재현**된다는 실증.
3. **"제품 자율성 ≠ 조직 전환"**: 자율주행 클러스터의 기존 AX 5건(Wayve·Zoox 등) 전멸. Vial(p.4)의 entity는 조직이므로, 자율주행 기술이 아무리 자율적이어도 그 조직의 활동·경계·목표 변형(Holmström p.331) 없이는 AT가 아님. 창업 때부터 자율주행이 본업인 조직은 '변형' 자체가 성립 불가.
4. **AT 6개 조직의 공통 서명**: ① 정량 증거(Vial), ② 경계(boundary) 변형 — 외주 기능의 내재화(삼성전자·무신사) 또는 내부 기능의 상품화(ElevenLabs) — 가 6건 중 4건에서 결정적. 활동(activities)만으로는 AT에 못 가고 **경계·목표가 움직여야 전환**이라는 것이 이 코퍼스의 귀납적 결론.

---

## 4. 클러스터별 재판정 표 (13개 클러스터 · 135건)

### NVIDIA · AI 인프라 (14건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| ServiceNow L1 티켓 자율 해결 | NVIDIA · 「How ServiceNow's AI Agents Resolve 90% of Tickets Autonomously」 | D3-auto | assessing | AX | 에이전트가 접수→해결을 자율 수행하나 L1 티켓 처리라는 단일 프로세스 대체 — Raisch·Krakowski(p.192) automation. 90%는 데모 내레이션 기반·모수 미공개로 Vial(p.4) 정량 증거 미달, Verhoef(p.891) 전사성·신규 BM 부재, Holmström(p.331) 3요소 중 활동만 변형 → D3-auto |
| Cadence 칩 검증 슈퍼 에이전트 | NVIDIA · 「Cadence Cuts Chip Verification From Weeks to Hours With AI」; NVIDIA_Developer · 「Long-Running AI Agents」 | D3-auto | determined | AX | 형식검증 1개월→10시간은 검증이라는 단일 엔지니어링 프로세스의 변혁효과 — Wamba(p.864) TE 수준, Raisch·Krakowski(p.192) automation. Holmström(p.331) 활동만 변형, Verhoef(p.891) 신규 BM 없음. 실제 Vera Rubin 설계 적용으로 실험 단계는 초과(Neumann p.120 determined) → D3-auto |
| CrowdStrike SOC 트리아지 | NVIDIA_Developer · 「Long-Running AI Agents: The Next Breakthrough in Enterprise Work」 | D3-auto | assessing | AX† | AI가 오탐을 자율 판단하나 SOC 트리아지 단일 과업 — Raisch·Krakowski(p.192) automation. 수치 전무로 Vial(p.4) 정량 요건 미충족, 파트너 언급뿐이라 Neumann(p.120) assessing. † 보수 원칙 적용 → D3-auto |
| Palantir FDE 코드 작성 | NVIDIA_Developer · 「Long-Running AI Agents: The Next Breakthrough in Enterprise Work」 | D3-aug | assessing | AX† | 에이전트가 최적화 코드를 작성하나 온톨로지 위 코드 생성 단일 과업이고 자율 범위 불명·인간 검토 전제 — Raisch·Krakowski(p.192) augmentation. 정성 발화뿐으로 Vial(p.4) 정량 증거 부재, Holmström(p.331) 3요소 변형 미확인 → D3-aug |
| Instacart Caper Cart 추천 | NVIDIA · 「Inside Instacart's AI-Powered Smart Shopping Cart (AI Podcast Ep.302)」 | D2 | determined | DX† | ML 추천·센서퓨전은 기존 쇼핑 프로세스의 기술적 개선이며 AI는 보조 — Verhoef(p.891) digitalization. 매출 +1%p는 개선 지표일 뿐 Vial(p.4)의 실체 속성 변화 아님, 워크플로 재설계 부재 → D2 |
| Mercedes 등 Alpamayo AV | NVIDIA · 「NVIDIA GTC Automotive Special Address」·「This is NVIDIA Alpamayo: Thinking Out Loud」 | D3-aug | determined | DX→AX | 현행 실증은 L2+ 주행 보조 = 주행 단일 과업의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation. L4는 2028년 로드맵뿐이므로 프레임 규칙상 현재 실증 단계로 판정(도착점 미실증), Verhoef(p.891) 전사성 미충족 → D3-aug |
| NVIDIA 자체 도그푸딩 | NVIDIA · 「How NVIDIA Runs Its Own AI Factory (AI Factory Insider Ep.2)」 | D3-aug (이행 중) | managed | DX→AX | ChipNeMo는 5,000명 코파일럿 = Raisch·Krakowski(p.192) augmentation, 자율 워크스페이스로의 이행 경로·실증(3개월 15배) 명시. 월 4조 토큰은 사용량 지표라 Vial(p.4)의 성과 기반 속성 변화 증거 아님, Holmström(p.331) 활동만 변형·신규 BM 없음. 전사 운영 프로세스 정의(99.9% 가용성)로 Neumann(p.120) managed → D3-aug(이행 중) |
| BYD·Geely·닛산·현대 Hyperion | NVIDIA · 「NVIDIA GTC Automotive Special Address」 | D2 | assessing | DX | 공통 센서·컴퓨트 플랫폼·데이터 표준화는 기존 개발 프로세스의 기술적 정비 — Verhoef(p.891) digitalization. AI 자율 판단 요소 미확인, 채택 발표 단계 = Neumann(p.120) assessing → D2 |
| Red Hat·Canonical·MS OpenShell | NVIDIA_Developer · 「Long-Running AI Agents: The Next Breakthrough in Enterprise Work」 | D2 | assessing | DX | 에이전트용 런타임의 OS 통합은 기반 인프라 정비이며 발표 단계 — Verhoef(p.891) digitalization 수준, Vial(p.4) 실체 속성 변화 증거 없음. Neumann(p.120) assessing → D2 |
| GitHub 생산성 서사 | NVIDIA_Developer · 「Long-Running AI Agents: The Next Breakthrough in Enterprise Work」 | 워싱 | assessing | DX(AX 표방)† | 커밋 5억→14억→"6조 달러" 환산은 검증 불가 외삽 서사로 전환 실체 자체가 없음 — Vial(p.4) 정량 증거 요건 정면 위반, 선언·서사를 전환으로 호명(Neumann p.120 위반) → 워싱 |
| (비교) AMD Helios 랙 | AMD · 「Advancing AI 2026 Replay: Build What's Next with AMD」 | D2 | assessing | DX | 랙·CPU 하드웨어 공급으로 AI 판단 요소 없음 — Verhoef(p.891) digitalization(인프라 공급) 이하. "agents per watt"는 에이전트 어휘 차용 마케팅 지표로 워싱 위험 병기, Holmström(p.331) 3요소 변형 없음 → D2 |
| (비교) Arm AGI CPU | Arm · 「Arm Everywhere Keynote: Rene Haas, new Arm AGI CPU, Meta, OpenAI」 | 워싱 | assessing | DX(AX 표방)† | 실질은 칩 공급인데 'AGI CPU'·에이전트 담론을 차용 — 표방 대비 실질 D2 이하로 프레임상 워싱. IP→칩 판매 전환은 Verhoef(p.891) 신규 BM 요소가 있으나 AI 전환 실증이 아닌 사업 피벗 선언 단계(Neumann p.120 assessing) → 워싱 |
| (비교) Vertiv 전력·냉각 | Vertiv · 「The physics driving the shift to 800 VDC」 | D2 | assessing | DX | 전력·냉각 물리 인프라 로드맵으로 AI 판단 요소 전무 — Verhoef(p.891) digitalization(기존 데이터센터 인프라의 기술 개선) 수준, Holmström(p.331) 3요소 변형 없음 → D2 |
| (비교) SK하이닉스 AI 메모리 | SK_hynix · 「[하이포커스 ON GTC 2026] SK하이닉스가 말하는 AI 메모리 미래」 | D2 | assessing | DX | HBM·eSSD 부품 공급의 전시·홍보 서사 — Verhoef(p.891) digitalization 이하, Vial(p.4) 실체 속성 변화 증거 없음. 전시 단계 = Neumann(p.120) assessing → D2 |

**재판정 변동 요약**: 기존 AX 4건(ServiceNow·Cadence·CrowdStrike·Palantir)은 모두 티켓 해결·칩 검증·SOC 트리아지·코드 작성이라는 단일 과업/프로세스 수준에 머물러 Raisch·Krakowski(p.192)의 과업 수준 개념(D3)으로 전량 강등됐다 — Verhoef(p.891)의 전사성·신규 BM과 Holmström(p.331) 3요소 2개 이상 변형을 충족한 사례가 없어 이 클러스터에서 AT는 0건이다. GitHub 서사와 Arm은 검증 불가 외삽·담론 차용으로 워싱 확정, DX→AX 2건(Mercedes·NVIDIA 도그푸딩)은 도착점(L4·자율 워크스페이스)이 로드맵/이행 중이라 현재 실증 단계인 D3-aug로 내려 판정했다.

### AWS 에이전트 플랫폼 (5건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| AWS Q Developer 모델 주도 전환 | AWS_Developers · 「Model Driven Agents – Strands Agents (A New Open Source, Model-Driven Approach)」 | D3-auto | determined | AX | 수작업 오케스트레이션 규칙을 폐기하고 모델이 계획·분기 — Raisch·Krakowski(p.192) automation. 그러나 한 팀의 에이전트 구축 프로세스라는 단일 프로세스 개선("수개월→수주"도 자사 발화)으로 Verhoef(p.891) 전사성·신규 BM 미충족, Holmström(p.331) 활동만 변형. 내부 수개월 사용 후 오픈소스화로 실험 단계 초과(Neumann p.120 determined) → D3-auto |
| OpenAI 모델 AgentCore 물류 에이전트 데모 | AWS_Developers · 「Deploy Production-Ready Agents in 22 Minutes with AgentCore Runtime」 | 워싱 | assessing | AX† | 에이전트 자율 구조이나 프로덕션 아닌 시연용 데모뿐 — 프레임 정의상 "선언·데모뿐"은 워싱(Neumann p.120 assessing 단계를 전환으로 호명). Vial(p.4) 실체 속성 변화 증거 전무, † 보수 원칙 → 워싱 |
| Leidos 전사 생성형 AI 전략(CAIO) | Amazon Web Services · 「Leading AI Transformation: A Chief AI Officer's Perspective」(키워드 수집분) | D3-aug | managed | DX→AX† | 헬프데스크 챗봇·코딩 어시스턴트는 개별 과업의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation, 자율 실행 근거 약함. 27% 승인율은 다수 미성숙의 자인이나 전사 승인 프로세스가 정의돼 Neumann(p.120) managed. Verhoef(p.891) 신규 BM 부재, Holmström(p.331) 활동만 변형 → D3-aug |
| Orca Security 보안경고 복구 지침 생성 | AWS_Developers · 「Orca Security: GenAI-powered Cloud Security Remediation with Amazon Bedrock」 | D3-aug | determined | DX→AX† | AI가 복구안을 판단·생성하나 실행은 사람의 원클릭 = 복구 지침 생성 단일 과업의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation, Wamba(p.864) 프로세스 수준 TE. 정량 ROI 미공개로 Vial(p.4) 정량 요건 미충족 → D3-aug |
| Visa MCP 쇼핑 컨시어지 데모 | AWS_Developers · 「How Much Does Your AI Agent Actually Cost?」 | 워싱 | assessing | DX(AX 표방)† | 멀티에이전트 라우팅 구조는 AX형이나 모의(mock) 모드로 실거래·실계약 증거 부재 — 데모를 에이전트 전환으로 호명(Neumann p.120 위반), Vial(p.4) 실체 변화 없음 → 워싱 |

**재판정 변동 요약**: 유일한 순수 AX였던 Q Developer 도그푸딩조차 한 팀의 구축 프로세스 개선이라는 단일 프로세스 수준이어서 D3-auto로 강등됐고, AX†였던 OpenAI 데모는 프로덕션 실증이 전무한 시연이라 워싱으로 내려갔다. DX→AX 2건(Leidos·Orca)은 자율 실행 미달의 인간-AI 협업으로 D3-aug 확정 — 이 클러스터 역시 Verhoef(p.891) 기준을 충족하는 AT는 0건이다.

### Google 생태계 (8건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| AT&T 판매 에이전트 | Google_Cloud_Tech · 「Agent context engineering for production」 | D3-auto | determined | AX | 오케스트레이터가 스킬 기준 판단·분기하며 판매 과업을 대체 — Raisch·Krakowski(p.192) automation. 그러나 현재 단일 채널·단일 유스케이스로 Verhoef(p.891) 전사성·신규 BM 미충족, 성과 정량치 부재로 Vial(p.4) 요건 미달, Holmström(p.331) 활동·역할만 변형(3요소 2개 미만). 프로덕션 가동으로 Neumann(p.120) determined → D3-auto |
| Home Depot AIOps 인시던트 대응 | Google_Cloud_Tech · 「20 minutes to 2 minutes: How Home Depot automated incident responses」 | D3-aug | determined | DX→AX | AI가 RCA·요약을 제공하나 전 과정 인간 검증 = 인시던트 대응 단일 프로세스의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation. 20분→2분은 Wamba(p.864) 프로세스 수준 TE(자체 산정), 자동 PR은 로드맵뿐이라 현재 실증 단계로 판정 → D3-aug |
| PayPal 자율 SRE 에이전트 | Google_Cloud_Tech · 「Building an MCP-powered autonomous incident response ecosystem」 | D3-aug | determined | AX | 감지→분류→완화 에이전트 생태계이나 읽기전용→허용목록의 제한 권한과 "재입사한 인턴, 감독 필요" 발화 = 감독 하 협업 — Raisch·Krakowski(p.192) augmentation. 인시던트 대응 단일 운영 프로세스로 Verhoef(p.891) 전사성 미충족, 코딩 시간 50~60%는 개발 효율 지표로 Vial(p.4) 실체 속성 변화 증거 미달 → D3-aug |
| MediaMarktSaturn 스킬 플랫폼 | Google_Cloud_Tech · 「Agile developers: shifting down with agentic skills」 | D2 | determined | DX→AX† | 스킬 130개·Terraform 블루프린트는 운영 지식의 전산화·프로세스 개선 — Verhoef(p.891) digitalization. Cloud Assist 장애 조사만 AI 판단 요소이나 보조 수준·정량 근거 발화뿐, † 보수 원칙 → D2 |
| BBVA 클라우드 거버넌스 | Google_Cloud_Tech · 「How BBVA manages 1,000+ GCP projects」 | D2 | assessing | DX | 리소스 경계·대시보드 정비가 실체이고 AI 판단 요소 없음 — Verhoef(p.891) digitalization. 에이전트 레이어는 예고 단계로 Neumann(p.120) assessing(AI 전환 성숙도 기준) → D2 |
| Carrefour BigQuery 데이터 에이전트 | Google_Cloud_Tech · 「Agent development and AgentOps with BigQuery, ADK, and MCP」 | D2 | assessing | DX→AX† | 결제→Kafka→알림은 정형 파이프라인 = 기존 프로세스 기술 개선 — Verhoef(p.891) digitalization. 에이전트 분석은 전사 배포 직전(프로덕션 전)으로 Neumann(p.120) assessing 단계라 판정에 반영 불가, † 보수 원칙 → D2 |
| Ulta/Flex/HCL 공장 데이터 에이전트 | Google_Cloud_Tech · 「Building enterprise-grade AI agents: How enterprises scale」 | 워싱 | assessing | DX(AX 표방)† | 실체는 100+ 공장 데이터 통합(정형 파이프라인 = D2 수준)인데 '에이전트'로 명명 — 표방 대비 실질 D2 이하 + 자율 판단 근거 미제시로 프레임상 워싱(Neumann p.120 위반). 패널 발화뿐 Vial(p.4) 정량 증거 없음 → 워싱 |
| (자사) Google 플랫폼 지표 | Google · 「Sundar Pichai Opening Remarks I/O 2026 Keynote」 | 워싱 | assessing | AX† | 월 480조 토큰 등은 특정 실체의 전환이 아닌 플랫폼 채택 규모 지표 — Vial(p.4)의 "실체 속성 변화" 판정 대상 자체가 부재하며, 지표 서사를 전환으로 호명하는 구조(Neumann p.120 위반). † 보수 원칙 → 워싱(판정 대상 부적합 병기) |

**재판정 변동 요약**: 확실한 AX로 꼽혔던 AT&T·PayPal이 각각 단일 유스케이스 판매 과업(D3-auto)과 감독 하 인시던트 대응(D3-aug)으로 강등돼, 이 클러스터도 Verhoef(p.891)·Holmström(p.331) 기준의 AT는 0건이다. Google 자사 지표는 전환 사례가 아닌 규모 서사로, Ulta/Flex/HCL은 데이터 통합의 에이전트 명명으로 각각 워싱 판정했고, DX→AX† 2건(MediaMarkt·Carrefour)은 AI 요소가 보조/프로덕션 전이라 D2로 보수 판정했다.

---

**집계(27건)**: D1 0 · D2 9 · D3-auto 5 · D3-aug 7(이행 중 1 포함) · AT 0 · 워싱 6

---

### Microsoft · GitHub (7건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| NVIDIA 인프라 공동설계 | Microsoft · 「Jensen Huang & Satya Nadella on unmetered intelligence (Build 2026)」 | D2 | managed | DX | 데이터센터·시스템 최적화로 기존 공급 프로세스의 기술적 개선(토큰 비용 30배 절감)일 뿐 AI의 자율 판단 없음 — Verhoef(p.891) digitalization. Holmström(p.331) 3요소(활동·경계·목표) 중 변형 없음 → D2 |
| EY Frontier Firm 컨설팅 전환 | Microsoft · 「Is Agentic AI upending the corporate ladder? EY's Global Consulting Leader (WorkLab)」 | 워싱 | assessing | AX† | 빌러블 아워 해체는 Verhoef(p.891) 신규 BM 요건에 해당하나 본문 근거가 '해체 선언'·'내년 입사자는 1일차 관리자' 등 선언뿐이고 투자액(10억 달러)은 투입이지 Vial(p.4)이 요구하는 실체 속성의 정량 변화 증거가 아님. 직원 86% '혼자 독학'은 오히려 assessing 단계 증거 — Neumann(p.120) 위반의 전형 → 워싱 |
| Moonshot Kimi K2.7 Copilot 편입 | GitHub · 「Kimi K2.7 Code: The first open-weight model in GitHub Copilot」 | 워싱 | assessing | DX→AX† | 실체는 모델 라인업 추가(공급)이고 '자율 구현'은 자사 내부 테스트 시연 1건뿐 — 데모·시연만으로 전환 호명은 Neumann(p.120) assessing 단계 위반. 조직 실체(entity) 속성 변화 증거 전무 — Vial(p.4) 미충족 → 워싱 |
| Anthropic 모델·Auto 라우팅 | GitHub · 「How Copilot auto mode selects the best AI model (GitHub Checkout)」 | D3-auto | managed | DX→AX | AI가 작업 복잡도를 판단해 모델을 분기하나 '모델 선택'이라는 단일 과업의 자동화이며 캐시 제약으로 판단 빈도 자체가 제한 — Raisch·Krakowski(p.192) automation. Verhoef(p.891) 전사성·신규 BM 무관, 제품 기능 수준 TE — Wamba(p.864) → D3-auto |
| Home Assistant 버그 트리아지 자동화 | GitHub · 「How to use agentic workflows for your repos (GitHub Checkout)」 | D3-auto | assessing | AX | AI가 스택트레이스 귀속을 판별·분기해 수정 PR까지 자율 생성하나 버그 트리아지라는 단일 과업 대체 — Raisch·Krakowski(p.192) automation, 프로세스 수준 TE(Wamba p.864). Verhoef(p.891) 전사성·신규 BM 부재, Holmström(p.331) 3요소 중 활동만 변형, 정량 수치 없는 초기 테스터 → AX에서 D3-auto로 강등 |
| Wolters Kluwer 세무 워크로드 | Microsoft_Azure · 「Wolters Kluwer scales regulated workloads with AKS, enabling…」 | D3-auto | determined | DX→AX | AKS 자동확장은 D2(Verhoef p.891 digitalization)이고 CCH Access Scan 무개입 신고서 작성은 단일 문서 과업의 AI 자동화 — Raisch·Krakowski(p.192) automation. 정량 성과 미공개로 Vial(p.4) 실체 속성 변화 증거 미충족 → D3-auto |
| Blue Tulip Ventures/Affectiva 담론 파트너 | Microsoft · 「Why AI adoption fails (and how to fix it) (WorkLab)」 | 워싱 | assessing | DX(AX 표방)† | 투자론·경험담 담론이 본체이고 자사 에이전트 'Blue'의 자율 수행 실증 전무('Fortune 500 절반' 주장도 과거 타사 시절 자사 주장) — 선언·간증뿐인 사례의 전환 호명은 Neumann(p.120) 위반 → 워싱 |

**재판정 변동 요약**: 기존 유일 AX였던 Home Assistant는 실체가 트리아지 단일 과업 자동화여서 Raisch·Krakowski(p.192) 기준 D3-auto로 강등했고, DX→AX로 분류됐던 Auto 라우팅·Wolters Kluwer도 도착점이 과업 수준이라 같은 등급이다. EY는 빌러블 아워 해체가 Verhoef(p.891) 신규 BM 요건을 형식상 건드리지만 실증이 선언·투입액뿐이라 Moonshot 데모·Affectiva 담론과 함께 워싱으로 내렸다. 이 클러스터에 AT는 0건 — 인프라·과금 정비(D2) 위 과업 자동화(D3)와 선언(워싱)만 남는다.

### OpenAI · Anthropic (13건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| BNY — CEO 'Eliza' 간증 | OpenAI · 「How BNY CEO Robin Vince Turns AI Optimism Into Action」 | 워싱 | assessing | DX(AX 표방)† | CEO 실명 간증 외 수치·메커니즘 전무 — Vial(p.4) 실체 속성 변화 증거 0. 간증으로 전환을 호명하는 전형 — Neumann(p.120) 위반 → 워싱 |
| Shopify — 트리아지 에이전트 재설계 | OpenAI · 「How Shopify Uses ChatGPT Work to Build Faster with AI Agents」 | D3-auto | determined | AX† | '대규모 팀→에이전트 하나'로 위임 메커니즘은 구체적이나 대상이 트리아지 단일 워크플로 — Raisch·Krakowski(p.192) automation. 정량 부재로 Vial(p.4) 미충족, Verhoef(p.891) 전사성·신규 BM 부재 → AX에서 D3-auto로 강등(워싱 경계 사례) |
| Virgin Atlantic — 대시보드 자체 구축 | OpenAI · 「How Virgin Atlantic Uses ChatGPT Work to Turn Weeks of Work…」 | D3-aug | determined | DX→AX† | 비개발자가 AI와 협업해 대시보드를 직접 구축('몇 주→몇 시간') — Raisch·Krakowski(p.192) augmentation. 산출물은 기존 리포팅 프로세스 개선이고 CX 1개 팀 범위 — Verhoef(p.891) digitalization 수준, 전사성 부재 → D3-aug |
| Verso — Codex 중심 회사 구축 | OpenAI · 「Stop Prompting. Start Giving AI Goals. (Katia Gil Guzman)」 | 워싱 | assessing | AX† | /goal 위임 담론의 예시로 1회 언급뿐, 조직·성과 실체 검증 불가 — Vial(p.4) 증거 0, 선언·언급만으로 전환 호명 — Neumann(p.120) 위반 → 워싱 |
| 무신사 — SaaS 내재화·채용 전환 | 제3자 후기 영상 · 「오픈AI x 무신사 비공개 행사 후기…」(transcripts/2026-07-23, 채널 미상·전언) | AT (이행 중) | determined | DX→AX | 연 4.5억 SaaS를 3명·2개월에 내재화한 정량 속성 변화 — Vial(p.4) 충족. 활동(개발·업무 프로세스)+경계(외부 SaaS 의존→내재화)+목표(채용 기준·역할 재정의, 66명 AI 테스트 채용) — Holmström(p.331) 3요소 중 2개 이상 변형, 에반젤리스트→부서 임베딩→탑다운의 전사 확산 설계 → AT. 단 전언(이중 간접 인용) 기반이라 (이행 중)·determined로 한정 |
| NBIM — Snowflake·MCP 통합 | Anthropic · 「Claude for Financial Services Keynote」 | D3-aug | managed | DX→AX | 생산성 20%=연 213,000시간의 정량은 있으나(Vial p.4) 실질은 전 직원의 분석 업무 증강 — Raisch·Krakowski(p.192) augmentation. Holmström(p.331) 3요소 중 활동만 변형(1/3), 운용 BM 불변 — Verhoef(p.891) 신규 BM 미충족 → AT 불가, D3-aug |
| AIG — 언더라이팅 재구상 | Anthropic · 「Claude for Financial Services Keynote」 | D3-auto | determined | AX | 정확도 75%→90%·주→일의 정량은 Vial(p.4)을 충족하나 언더라이팅 단일 프로세스의 심사 판단 대체 — Raisch·Krakowski(p.192) automation, 프로세스 수준 TE(Wamba p.864). Holmström(p.331) 활동만 변형(1/3), 신규 BM 없음 → AX에서 D3-auto로 강등 |
| Bridgewater — 애널리스트 어시스턴트 | Anthropic · 「Claude for Financial Services Keynote」 | D3-aug | determined | DX→AX† | 2023년부터 상시 구동이나 '어시스턴트' 보조 형태 — Raisch·Krakowski(p.192) augmentation. 정량 전무로 Vial(p.4) 미충족 → D3-aug |
| DE Shaw / New York Life — 전사 배포 | Anthropic · 「Claude for Financial Services Keynote」 | D3-aug | determined | DX→AX† | 전사 '보급'은 도구 배포이지 변형이 아님 — Verhoef(p.891)의 digitalization/전사성 구분상 신규 BM·재설계 근거 없음, 성과 수치 0(Vial p.4 미충족). 자율 실행 근거 없어 augmentation 보급 수준 — Raisch·Krakowski(p.192) → D3-aug |
| HG Capital — 포트폴리오 전환 이식 | Anthropic · 「Claude for Financial Services Keynote」 | AT | managed | AX | 생산성 30%↑·스쿼드 9→2·에이전틱 엔지니어 1,000 인스턴스로 캐파 +50% — Vial(p.4) 정량 충족. 활동(개발 방식)+경계(인간/에이전트 인력 구조 재정의)의 Holmström(p.331) 2요소 변형, 중앙 AI팀(20+150)이 50개사·12만 FTE에 이식하는 정의된 프로세스 — Neumann(p.120) managed → AT 유지 |
| Commonwealth Bank — 전략 선언 | Anthropic · 「Claude for Financial Services Keynote」 | 워싱 | assessing | DX(AX 표방)† | CTO의 '글로벌 AI 전략 기반' 규정뿐 실행·수치 전무 — Vial(p.4) 증거 0, 선언을 전환으로 호명 — Neumann(p.120) 위반 → 워싱 |
| AbbVie — Gaia·Genesis 문서화 | Anthropic · 「How AbbVie accelerates drug discovery with Claude」 | D3-aug | determined | DX→AX† | 임상 규제문서 작성 40~60% 절감은 문서화·콜플래닝이라는 개별 과업의 AI 증강(규제문서 특성상 인간 검수 전제) — Raisch·Krakowski(p.192) augmentation, 프로세스 수준 TE(Wamba p.864). Verhoef(p.891) 전사성·신규 BM 부재 → D3-aug |
| Deloitte·KPMG·PwC 등 — COBOL·에이전트 배포 | Anthropic · 「Claude for Financial Services Keynote」 | 워싱 | assessing | DX→AX† | 키노트에서 파트너 '역할 언급'만 있고 수행 실체·수치 전무 — Vial(p.4) 증거 0. 실체 확인돼도 COBOL 마이그레이션은 단일 과업이나 현재는 언급 단계 — Neumann(p.120) assessing → 워싱 |

**재판정 변동 요약**: 기존 AX 4건 중 2건이 떨어졌다 — Shopify는 트리아지 단일 과업이라 D3-auto로, Verso는 언급뿐이라 워싱으로, AIG도 정량은 훌륭하나 언더라이팅 단일 프로세스여서 D3-auto로 강등했다. 반대로 HG Capital은 인력 구조 재정의(Holmström 2요소)+정량으로 AT를 유지했고, 무신사는 SaaS 경계 재편+채용 재정의+정량이 확인돼 DX→AX에서 AT(이행 중)로 승격했다(단 전언 기반). 실명 간증·선언형(BNY·Commonwealth·Deloitte)은 전부 워싱으로 수렴 — 이 클러스터의 '위임' 담론과 실증 사이 간극이 3개 클러스터 중 가장 크다.

### Palantir · ServiceNow · Oracle (11건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| NHS 의료 데이터 플랫폼 FDP | Palantir · 「Palantir and the NHS \| UK Stories」 | D2 | managed | DX | 사일로 통합·단일 화면으로 4분→30초·8만 건+ 추가 시술의 정량은 강하나 판단은 전부 사람 — 기존 프로세스의 기술적 개선인 Verhoef(p.891) digitalization. AI 자율 판단 요소 없어 D3 이상 불가 → D2 |
| Hadean 국방 C2 시뮬레이션 | Palantir · 「Palantir and Hadean \| UK Stories」 | D2 | assessing | DX† | Foundry 위 플랫폼 구축·조달 서사가 본체이고 자율 판단 근거 없음 — Verhoef(p.891) digitalization, 구축 단계 — Neumann(p.120) assessing. † 보수 판정 → D2 |
| 익명 조달 고객군 인보이스·RFQ | Palantir · 「Chad & Agathe: How Palantir Powers AI Automation Across Procurement」 | D2 | determined | DX† | 인보이스-계약 대사·RFQ 자동화는 규칙을 사람이 확정한 정형 자동화(자율 분기 근거 없음) — Verhoef(p.891) digitalization. 절감 1~10%는 프로세스 개선 수치 → D2 |
| FedEx 디지털 트윈·Control Tower | ServiceNow · 「Welcome to Agentic Business (Knowledge 2026 Opening Keynote)」 | D2 | managed | DX† | 디지털 트윈·AI 자산 등록/위험관리는 거버넌스 인프라이지 AI의 자율 판단이 아님 — Verhoef(p.891) digitalization. 전사 AI 자산 관리 프로세스 정의는 Neumann(p.120) managed이나 전환 실체는 D2 |
| DocuSign·Honeywell ITSM 전문가 | ServiceNow · 「Welcome to Agentic Business (Knowledge 2026 Opening Keynote)」 | 워싱 | assessing | AX† | '대부분 요청 자동 차단·몇 초 해결'은 수치 미제시 자사 발화(간증)뿐 — Vial(p.4) 증거 0, 검증 없는 전환 호명 — Neumann(p.120) 위반. 사실이어도 ITSM 단일 기능 automation(Raisch·Krakowski p.192)에 그침 → 워싱 |
| CNA 보험 리스크 평가 자동화 | ServiceNow · 「How CNA unified risk and scaled assessment from 50 to 900+ apps」 | D2 | determined | DX† | 평가 처리량 확대(연 50개→900+ 앱)는 기존 평가 프로세스의 기술적 확장이고 AI 판단의 자율성 불명 — Verhoef(p.891) digitalization. † 보수 판정 → D2 |
| Motorola CPQ·에이전틱 제안서 | Oracle · 「Oracle at Gartner CSO: Demand More from Enterprise AI」 | D3-auto | determined | DX→AX | CPQ 33%→99%는 8년의 D2(Verhoef p.891 digitalization) 기반이고, 도착점인 견적 옵션·RFP 자동 생성(응답 50% 단축)은 제안서 작성 단일 과업의 automation — Raisch·Krakowski(p.192). Holmström(p.331) 활동만 변형(1/3) → D3-auto |
| Ricoh 영업 AI | Oracle · 「Oracle at Gartner CSO: Demand More from Enterprise AI」 | D2 | assessing | DX | 데이터 품질 정비 병행의 초기 단계로 자사 증언도 '정렬 안 된 시스템에 AI 얹으면 실패' — 기존 프로세스 정비 수준(Verhoef p.891 digitalization), Neumann(p.120) assessing → D2 |
| Oracle 북미 영업 에이전틱 앱 | Oracle · 「Oracle at Gartner CSO: Demand More from Enterprise AI」 | D3-auto | determined | AX | signal→context→action으로 견적·계획·자료를 자율 생성하나 영업 지원 과업군의 automation — Raisch·Krakowski(p.192). 400명 파일럿→1만 명 '확대 예정'은 배포 규모이지 성과가 아니어서 Vial(p.4) 정량 속성 변화 미충족, Holmström(p.331) 활동만 변형 → AX에서 D3-auto로 강등 |
| Whitespace 국방 의사결정 AI | Oracle · 「Whitespace on Sovereign AI for Defense (Oracle TV, Defence Tech Summit)」 | 워싱 | assessing | DX→AX† | 엔드투엔드 '데모 6주 구축'·항모 초단기 배치 등 데모·시연 단계 — Neumann(p.120) assessing 단계의 전환 호명. 운영 성과·정량 전무로 Vial(p.4) 미충족 → 워싱 |
| Oracle Red Bull Racing 레이스 전략 | Oracle · 「AI Changes Everything: Inside Oracle Red Bull Racing's AI Edge」 | D2 | determined | DX | 몬테카를로 시뮬레이션 컴퓨팅 확대가 실체이고 고압 상황 인간 판단 유지 명시 — Verhoef(p.891) digitalization, AI 자율 판단 없음. '학습 기반 진화'는 방향 서사 → D2 |

**재판정 변동 요약**: 기존 DX 7건은 전부 D2로 1:1 이동했다(자율 판단 요소가 없어 D3 진입 불가). 기존 AX 2건이 모두 강등됐다 — Oracle 자사 영업 앱은 자율 실행 구조는 있으나 성과 정량이 없고 과업군 수준이라 D3-auto, DocuSign·Honeywell은 수치 미제시 자사 간증뿐이라 워싱이다. Whitespace도 데모 단계라 워싱으로 내려, 이 클러스터는 AT 0건 — '거버넌스 계층' 서사와 달리 실증된 전환은 한 건도 없다.

---

## 집계 (31건)

| 재판정 | 건수 | 사례 |
|---|---|---|
| D1 | 0 | — |
| D2 | 8 | NVIDIA 인프라, NHS, Hadean, 익명 조달, FedEx, CNA, Ricoh, Red Bull |
| D3-auto | 7 | Auto 라우팅, Home Assistant, Wolters Kluwer, Shopify, AIG, Motorola, Oracle 영업 |
| D3-aug | 5 | Virgin Atlantic, NBIM, Bridgewater, DE Shaw/NYL, AbbVie |
| AT | 2 | HG Capital, 무신사(이행 중) |
| 워싱 | 9 | EY, Moonshot Kimi, Blue Tulip/Affectiva, BNY, Verso, Commonwealth, Deloitte 등, DocuSign·Honeywell, Whitespace |

---

### Databricks · 벡터DB · W&B

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| Adobe·Atlassian·NAB LakeWatch 이전 | Databricks · 「Defending against a tidal wave of AI attacks with Lakewatch」 | D3-aug (이행 중) | determined | DX→AX | SIEM 이전은 Verhoef(p.891) digitalization, 그 위 에이전트 탐지룰 작성·백그라운드 조사는 분석가 검증이 남는 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation. SOC 단일 기능의 프로세스 수준 변혁효과(Wamba p.864 TE), Holmström(p.331) 3요소 중 활동만 변형 → AT 미충족 |
| Panther Labs 인수 | Databricks · 「Defending against a tidal wave of AI attacks with Lakewatch」(동일 영상) | 워싱 | assessing | DX† | 기업 인수 이벤트를 AX 서사에 편입한 것으로 전환 실체 자체가 없음 — Vial(p.4) 실체 속성 변화 증거 전무, LakeWatch 출시 2개월차의 assessing 단계 발표를 전환으로 호명(Neumann p.120 위반). † 보수 판정 |
| Anthropic 파트너십·키노트 | Databricks · 「Dario Amodei and Ali Ghodsi: Anthropic + Databricks, AI Agents…」 / Snowflake · 「Snowflake Summit 2026 Opening Keynote」 | 워싱 | assessing | DX† | 키노트 담론·파트너십 발표뿐 배포된 전환 사례가 아님 — 선언·간증만으로 Verhoef(p.891) digitalization조차 판정할 실체 부재, assessing 단계 담론의 전환 호명(Neumann p.120) |
| DEFRA·Natural England 이탄지 지도화 | Databricks · 「How DEFRA and Natural England Accelerate Peatland Restoration」 | D1 | determined | DX† | 수작업 디지타이징(아날로그 지도의 디지털 변환)을 AI가 가속한 것으로 산출물·과업 모두 digitization 그 자체 — Verhoef(p.891). 자율 판단·분기 근거가 없어 Raisch·Krakowski(p.192) automation 인정도 유보, † 보수 판정 |
| Thrivent·HSBC 차선책 추천 | Databricks · 「Unscripted: How Banks & Insurers Grow with Data, AI Agents…」 | D3-aug | determined | DX→AX† | AI가 차선책(next-best-action)을 판단·제시하고 실행·결정은 자문가 — Raisch·Krakowski(p.192) augmentation. 자문 단일 과업, Holmström(p.331) 활동만 변형, Verhoef(p.891) 전사성·신규 BM 부재(+10%는 업계 일반 수치와 경계 모호) → 이행 판정 철회, D3-aug |
| TripAdvisor·HubSpot·DT·Dust (Qdrant) | Qdrant · 「Qdrant Vector Space Day 2025 Opening Keynotes」 | D2 | determined | DX→AX† | 실증된 것은 벡터 검색 인프라 채택·검색 고도화 — Verhoef(p.891) digitalization. 플래너·에이전트의 자율 판단은 상세 미공개로 Raisch·Krakowski(p.192) 증강 판정 근거 부족, † 보수 판정으로 D2 |
| Morningstar Intelligence Engine | Weaviate · 「Morningstar Intelligence Engine with Aravind Kesiraju (Weaviate Podcast #111)」 | D2 | determined | DX† | RAG·text-to-SQL은 기존 리서치 검색·조회 프로세스의 기술적 개선으로 AI는 보조 역할 — Verhoef(p.891) digitalization. 자율 분기 없음, 프로세스 수준 효과(Wamba p.864)에도 판단 대체 요소 미확인 |
| Sanofi·GSK·CoreWeave (W&B) | Weights & Biases · 「Transformative & cross-functional AI adoption at Sanofi (FC London)」·「Fully Connected London 2025」 | D2 | managed | DX† | 전사 교육·업무 보조 앱 확산(직원 80% 사용)은 범위만 넓을 뿐 기존 업무의 기술적 보조 — Verhoef(p.891) digitalization, 신규 BM·프로세스 재설계 없음. Neumann(p.120) managed 범위와 전환 실질은 별개, 자율 실행 증거 없음 |
| Expel 경보 중복 방지 | Pinecone · 「Preventing Déjà Vu: Vector Similarity Search for Security Alerts」 | D2 | determined | DX | 유사 경보 벡터 검색으로 사람의 조사를 보조하는 규칙적 파이프라인 — Verhoef(p.891) digitalization. AI의 판단·실행 없음(Raisch·Krakowski p.192 어느 쪽도 미해당) |
| Canva·Nestlé·TR·DraftKings (Snowflake) | Snowflake · 「Snowflake Summit 2026 Opening Keynote」·「Platform Keynote」 | D2 | determined | DX† | 분석 가속·공급망 예측 앱·규제 데이터 관리로 최종 판단은 사람 — Verhoef(p.891) digitalization. Nestlé 185개국 전사앱도 예측 제공에 그쳐 Holmström(p.331) 3요소 변형 미확인, † 보수 판정 |
| Mem0 메모리 계층 | Qdrant · 「Mem0: Continual Learning Starts with Memory (Taranjeet Singh)」 | D3-auto | assessing | AX† | 기억 추출·갱신·망각 자율 루프는 실재하나 '에이전트 메모리 관리'라는 단일 기능이며, 전환의 실체(속성이 변한 도입 조직·정량 증거)가 없음 — Vial(p.4) 미충족. 벤더 제품 층위 발화 — Raisch·Krakowski(p.192) automation 수준으로 강등, † 보수 판정 |

**재판정 변동 요약**: 이 클러스터는 기존 판정이 전반적으로 하향 조정됐다 — 유일한 AX였던 Mem0는 도입 조직의 속성 변화 증거가 없는 벤더 제품 층위 발화라 Vial(p.4) 기준으로 D3-auto(assessing)로 강등됐고, DX→AX 3건(LakeWatch·Thrivent·Qdrant)은 자율 요소가 단일 과업 증강이거나 미공개여서 D3-aug/D2로 내려갔다. Panther 인수와 Anthropic 키노트는 판정할 전환 실체가 없는 이벤트·담론이라 워싱으로 재분류했으며, DEFRA는 과업 자체가 아날로그→디지털 변환이라 D1로 정밀화했다.

### SAP · Salesforce · 컨설팅

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| SAP × Fonterra S4전환+AI앱 | SAP · 「AI Transformation with Fonterra and SAP (Sapphire Madrid 2026)」 | D3-aug (이행 중) | determined | DX→AX | ERP 클린코어 전환은 Verhoef(p.891) digitalization; 현금앱·정비 추천·운송계획 3개 AI 앱과 Joule 접수표 생성은 개별 프로세스의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation. Holmström(p.331) 활동만 변형, 신규 BM 없음. 2→22개 공장 확대 실증 중이라 (이행 중) 부기 |
| SAP × ZF 데이터+품질 에이전트 | SAP · 「AI Value at Scale with ZF Group (Sapphire Madrid 2026)」 | D3-aug (이행 중) | determined | DX→AX | BW→BDC 이관은 digitalization(Verhoef p.891); 8D 품질 프로세스의 4-에이전트 근본원인 판단 체인은 품질 단일 프로세스의 변혁효과 — Wamba(p.864) TE 수준, 인간 8D 절차 내 협업(Raisch·Krakowski p.192 augmentation). Holmström(p.331) 활동만 변형 |
| SAP × "제로 고객" Agent-led 전환 | SAP · 「Agent-led Transformation: Fast-Track your ERP Migration」 | 워싱 | assessing | DX→AX† | 착수 전 목표치(35~50% 절감)뿐으로 실증 0 — 프레임 규칙상 도착점이 로드맵이면 현재 실증 단계로 판정하며, assessing 단계(Neumann p.120)를 'Agent-led 전환'으로 호명. Vial(p.4) 속성 변화 증거 전무 → 워싱 |
| TCS × TDC NET 레거시 현대화 | TCS · 「TCS helps TDC NET modernise with human-in-the-loop AI」 | D3-aug | determined | DX→AX† | AI가 레거시 비즈니스 로직을 해석하되 규칙은 고객·TCS 공동 템플릿, 인간 품질검사 유지 — Raisch·Krakowski(p.192) augmentation. 마이그레이션 단일 프로그램으로 레거시 현대화 자체는 Verhoef(p.891) digitalization, 전사성·신규 BM 무관 |
| Infosys × Sandvik 보증처리 AI | Infosys · 「The Biggest Barrier to AI? It's Not Technology (Sofia Sirvell)」 | D3-aug | assessing | DX→AX† | 보증처리·S&OP 등 과업 수준 증강 지향이나 "대부분 POC" — Neumann(p.120) assessing(실험 착수) 단계. Holmström(p.331) 3요소 변형은 지향일 뿐 미실증, † 보수 판정으로 D3-aug(assessing) |
| Infosys × Swedbank 미팅 요약 | Infosys · 「How Swedbank Is Scaling AI Across the Entire Bank (Lotta Lovén)」 | D2 | managed | DX† | 확산의 실체는 미팅 녹음→요약 자동화라는 기존 기록 프로세스의 기술 개선 — Verhoef(p.891) digitalization, 자율 판단·분기 미확인. 전행 전략·60개 저축은행 확산 프로세스는 Neumann(p.120) managed이나 전환 실질과 별개 |
| Salesforce × Indeed 서비스 에이전트 | Salesforce · 「How @Indeed is Building Agents without Opening a Browser」·「Welcome to Agentforce Demo Day!」 | D3-auto | managed | AX | 해결률 4%→25%·CSAT 1.8→4.0으로 Vial(p.4) 정량 증거는 충족하나, 고객서비스 티켓 해결이라는 단일 과업의 대체 — Raisch·Krakowski(p.192) automation. Holmström(p.331) 3요소 중 활동만 변형(목표는 기존 '분당 31명 채용'에 정렬), Verhoef(p.891) 신규 BM 부재 → AT 미충족, 강등 |
| Salesforce × LIV Golf 팬 에이전트 | Salesforce · 「@LIVGolf Elevates Fan Engagement with Agentforce」·「Agentforce Demo Day」 | D3-auto | determined | AX† | 팬 응대 단일 과업의 자동화이며 Agent Script의 결정론적 선실행 비중이 커 자율성 제한적 — Raisch·Krakowski(p.192) automation, Wamba(p.864) 프로세스 수준 TE. Verhoef(p.891) 전사성 없음, † 보수 판정 |
| Salesforce × Falabella·JPW | Salesforce · 「Welcome to Agentforce Demo Day!」·「What Agentblazers Learned about Agent Orchestration & Control」 | D3-auto | determined | AX† | WhatsApp 자가응답 60%·해결 +40%는 단일 채널 응대 과업의 automation(Raisch·Krakowski p.192). 판단 구조 미공개로 Vial(p.4) 속성 변화 증거가 자사 행사 수치뿐 — Holmström(p.331) 3요소 검증 불가, † 보수 강등 |
| Accenture × JP Morgan·DBS·BNY 보고서 | Accenture · 「Top Banking Trends 2026 - Unconstrained Banking」 | 워싱 | assessing | DX(AX 표방)† | 'AI 디지털 직원' 수사 대비 확인되는 실체는 이메일 보조 도구(주 3시간 절감, 재인용·자막 훼손) — 실질이 Verhoef(p.891) digitalization 이하인데 전환을 표방, 수치도 타사 발표 재인용으로 Vial(p.4) 검증 불가 → 워싱 |
| Infosys Davos 패널 (Anthropic·Danske) | Infosys · 「The Boardroom Mandate: Scaling AI for Business Impact (Davos 2026)」 | 워싱 | assessing | DX(AX 표방)† | 구현 사례 없는 담론·공포 수사("75% 폐업 전망")로 판정 대상 실체 부재 — 선언·간증뿐인 assessing 단계 담론의 전환 호명(Neumann p.120 위반) → 워싱 |

**재판정 변동 요약**: 기존 AX 3건(Indeed·LIV Golf·Falabella)이 전부 D3-auto로 강등됐다 — 정량 성과는 있으나 모두 고객 응대라는 단일 과업 자동화로 Holmström(p.331) 3요소 중 활동만 변형되고 Verhoef(p.891)의 전사성·신규 BM이 없기 때문이다. SAP·TCS의 DX→AX 이행 4건은 개별 프로세스 증강(D3-aug)으로 정리하되 Fonterra·ZF에만 (이행 중)을 남겼고, 착수 전 목표치뿐인 SAP 제로 고객은 Accenture·Davos 담론과 함께 워싱으로 내려갔다.

### 한국 AX

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| 우리은행×삼성SDS 전행 175개 에이전트 | 삼성SDS AX · 「[AX Summit] 2. (키노트) AI Native 기업으로의 전환 방안과 사례(신계영 부사장)」 | 워싱 | assessing | DX→AX† | "AX 회사" 선언+1년 컨설팅 설계만 있고 구축은 내년 하반기 목표로 실증 0 — assessing(설계·착수 전) 단계를 '전행 AX'로 호명(Neumann p.120 위반), Vial(p.4) 속성 변화 증거 전무. 구축 후 재평가 대상 |
| 삼성전자 콜센터·시장조사 에이전트 (SDS 수행) | IT조선 · 「[AI&CLOUD2026] 세션1 AI-Native 기업으로의 전환 방안 및 사례(삼성SDS 신계영)」 | AT | determined | AX | Vial(p.4) 정량 증거(연 100억 외부 조사비 업무 대체, 실제 인터뷰와 80~95% 일치) 충족; Holmström(p.331) 3요소 중 활동(에이전트가 인터뷰 수행·응답)+경계(외부 조사업체에 두던 기능의 내재화) 2개 변형 → AT 요건 ①② 충족. 단 시장조사 사업기능 범위·자사 발화 수치 |
| 삼성 관계사 ChatGPT Enterprise (SDS 리셀) | 삼성SDS AX · 「[AX Summit] 2. (키노트) AI Native 기업으로의 전환 방안과 사례」 | D2 | determined | DX† | 도구 보급·기밀/비기밀 이원화 거버넌스 정비로 기존 업무의 기술적 보조 — Verhoef(p.891) digitalization. 워크플로 재설계·자율 판단 근거 없음(Raisch·Krakowski p.192 미해당) |
| LG 계열 제조·R&D(스케줄링) | LG_AI_Research · 「LG AI Talk Concert 2025 - Shaping the Future of AI」 | D3-auto | determined | AX | 정량 증거는 Vial(p.4) 수준(연 $54M·한계이익 4%↑)이나, 트랜스크립트 원문은 "100% based on schedules proposed by AI" — 원료 스케줄링이라는 단일 운영 과업의 대체(Raisch·Krakowski p.192 automation). Holmström(p.331) 3요소 중 활동만 변형(공장의 경계·목표 불변), Verhoef(p.891) 신규 BM 부재 → AT 미충족, 강등. 비전검사·상담 STT도 각각 과업 수준 |
| 국민연금·LSEG×LG Master Score | LG_AI_Research · 「LG AI Talk Concert 2025 - Shaping the Future of AI」 | D3-aug | determined | DX→AX† | AI가 투자신호(Master Score)를 생성하고 실행·최종결정은 사람 — Raisch·Krakowski(p.192) augmentation. 신호 생성 단일 과업으로 Verhoef(p.891) 전사성 없음, ETF 성과는 자사 발화 † |
| SK디스커버리 현업 AX(JSA·번역·챗봇) | 티타임즈TV · 「현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)」 | D2 | determined | DX† | JSA 생성·레이아웃 보존 번역·HR 챗봇은 정해진 업무의 생성형 AI 보조 도구 — Verhoef(p.891) digitalization, 자율 분기 없음. 'AX 100배' 배수 서사와 실증(건당 30분↓)의 간극 주의 |
| 한국은행×NAVER Cloud 금융 LLM | NAVER_Cloud · 「한국은행, 하이퍼클로바X로 금융·경제 특화 생성형 AI 구축」 | D2 | assessing | DX | 내부망 프라이빗 클라우드 인프라 구축 진행 중, 제공 예정 기능도 요약·번역·질의응답 보조 — Verhoef(p.891) digitalization, Neumann(p.120) assessing 단계 |
| 대동×NAVER Cloud 농업 에이전트 | NAVER_Cloud · 「네이버클라우드 X 대동: 농업 특화 AI 에이전트로 만들어 나갈 농업 혁신」 | 워싱 | assessing | DX(AX 표방)† | '에이전트' 표방이나 구축 준비 단계·수치 전무 — assessing 단계 선언을 전환으로 호명(Neumann p.120 위반), Vial(p.4) 증거 0 → 워싱 |
| 플리토×Upstage Document Parse | Upstage · 「문서 처리 AI, 10%의 인식률 차이가 프로젝트 비용을 바꿉니다 (Upstage 고객사례)」 | D1 | determined | DX | 저해상도 원천문서→어절 단위 텍스트 추출은 아날로그/비정형 정보의 디지털 변환 그 자체 — Verhoef(p.891) digitization. 인식률 10%p가 검수 원가로 직결되는 변환 품질 문제이며 판단·분기 없음 |
| 무신사×OpenAI AI 네이티브 전환 | AI 겸임교수 이종범(3자 후기) · 「오픈AI x 무신사 비공개 행사 후기, 코덱스 기업 도입 사례와 AI 네이티브 워크플로우 인사이트 총정리」 | AT | managed | AX | Holmström(p.331) 3요소 모두 변형 — 활동(코딩 에이전트가 개발 수행·바이브코딩 내재화), 경계(연 4.5억 외부 SaaS를 3명·2개월 내재화 = make/buy 경계 재편), 목표(채용 66명을 'AI 활용 문제해결' 기준으로 선발, 성과평가 기준 재설정 — 트랜스크립트에 "채용 기준의 패러다임 전환" 명시). Verhoef(p.891) 지표 재정의 충족, 4단계 전사 확산 프로세스는 Neumann(p.120) managed. 단 수치가 3자 후기 경유로 Vial(p.4) 정량 증거의 검증력 약함 |

**재판정 변동 요약**: 최대 변동은 LG의 강등이다 — "100% AI 스케줄 공장"은 원문상 AI '제안' 스케줄 기반 운영으로, 정량 증거는 강하지만 스케줄링 단일 과업이라 Holmström(p.331) 3요소 중 활동만 변형돼 AT가 아닌 D3-auto다. 반면 삼성전자 시장조사(활동+경계 2요소)와 무신사(활동·경계·목표 3요소+평가지표 재정의)는 AT를 유지했고, 구축 전 선언뿐인 우리은행과 준비 단계의 대동은 assessing 단계의 전환 호명으로서 워싱으로 재분류됐다.

---

## 전체 분포 (32건)

| 재판정 | 건수 | 사례 |
|---|---|---|
| D1 | 2 | DEFRA, 플리토×Upstage |
| D2 | 9 | TripAdvisor·Qdrant, Morningstar, Sanofi·GSK, Expel, Canva·Nestlé 등, Swedbank, 삼성 관계사, SK디스커버리, 한국은행 |
| D3-auto | 5 | Mem0, Indeed, LIV Golf, Falabella·JPW, LG 스케줄링 |
| D3-aug | 7 | LakeWatch(이행 중), Thrivent·HSBC, Fonterra(이행 중), ZF(이행 중), TDC NET, Sandvik, 국민연금·LSEG |
| AT | 2 | 삼성전자 시장조사, 무신사×OpenAI |
| 워싱 | 7 | Panther, Anthropic 키노트, SAP 제로 고객, Accenture 은행 보고서, Infosys Davos, 우리은행, 대동 |

기존 대비: AX 7건 중 5건 강등(잔존 AT 2건), DX→AX 9건 전원 D3 이하로 정리, "표방" 3건+선언·이벤트 4건이 워싱으로 확정.

---

### 중국·아시아 (12건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| Ant Group 코어 아키텍처 재구축 | Huawei · 「Banks Need AI-Native Foundations, but Trust Still Matters」 | D2 | assessing | DX† | 12년 5회 전면 재구축은 기존 뱅킹 프로세스의 기술적 재구현 — Verhoef(p.891) digitalization. "AI-native"는 촉구 담론으로 자율 판단 실증 없음, Holmström(p.331) 3요소 변형 증거 부재 → D2. |
| 톈진항 스마트항만 PortGPT | Huawei · 「Decoding Tianjin Port – A World-Class Port!」 | AT | managed | AX | 계획 수 시간→수 분, IGV 92대 3년+ L4 자율운행, 최소인력 자율 운영 — Vial(p.4) 실체 속성의 정량적 변화 충족. 활동(자율 운영·근본원인 추론)+목표(무탄소 스마트 터미널 1.0→3.0) 변형 — Holmström(p.331) 2요소. 터미널 사업기능 전체에 프로세스 정의·수년 운영 — Neumann(p.120) managed → AT. 단 수치는 벤더 발화. |
| İşbank 지점망·자율 네트워크 | Huawei · 「Transforming a Vast Network, One Branch at a Time」 | D2 | assessing | DX→AX† | 실증된 것은 지점 구축 배포 자동화(1시간·10배)로 사람이 규칙을 확정한 프로세스 개선 — Verhoef(p.891) digitalization. L4 자율 네트워크는 '원년 선언' 단계 — Neumann(p.120) assessing을 전환으로 셈할 수 없어 보수 판정 → D2. |
| Telecom Argentina 멀티클라우드 | Huawei · 「Why Telecom Argentina is Betting on Hybrid Multicloud and AI」 | D2 | assessing | DX | 코어 IT 무중단 클라우드 이전은 기존 프로세스의 기술적 개선 — Verhoef(p.891) digitalization. AI(개인화·장애 예측)는 계획 단계·수치 미공개 — Neumann(p.120) assessing → D2. |
| Keyrus × RCBC 데이터 역량화 | Huawei · 「Why Data Alone Does Not Lead to Better Decisions」 | D2 | assessing | DX | 데이터 통합·360도 고객뷰·분석 부여는 프로세스 기술 개선이고 판단 주체는 사람 — Verhoef(p.891) digitalization. 정량 성과 미공개, Vial(p.4)의 속성 변화 증거 부재 → D2. |
| Web3 거래소 AIDBS 거버넌스 | Alibaba_Cloud · 「ClawTalks EP6: Your AI Workforce — Launch of Alibaba AIDBS」 | D3-auto | determined | DX→AX | DAS 에이전트가 장애를 자율 진단(30초·정확도 92%>전문가 85%)하나 DB 운영이라는 단일 프로세스 대체 — Raisch·Krakowski(p.192) automation, Wamba(p.864) TE 수준. Verhoef(p.891) 전사성·신규 BM 부재, Holmström(p.331) 3요소 중 활동만 → D3-auto. 600+ 인스턴스 운영으로 실험 단계는 초과 — determined. |
| 중국 자동차사 에이전트 하네스 | Alibaba_Cloud · 「ClawTalks EP6: Your AI Workforce — Launch of Alibaba AIDBS」 | D3-auto | determined | AX† | 400+ 인스턴스 운영은 과업 수준 에이전트 활용의 증거일 뿐, 자율성 상세·성과·조직 변형(Holmström p.331 3요소) 전부 미공개 — † 보수 원칙에 따라 Raisch·Krakowski(p.192) automation 수준으로 강등 → D3-auto. Vial(p.4) 정량 증거 없음. |
| BMW 차내 Qwen 에이전트 | Alibaba_Cloud · 「How the Next Era of Industrial AI is Transforming Manufacturing」(Hannover Messe, Dr. Ye Huang) | 워싱 | assessing | DX(AX 표방)† | '에이전트'를 표방하나 대표 지표가 웨이크업 정확도 99% = 음성비서 성능으로 실질은 D2 이하 제품 기능 — 워싱 정의 그대로 충족. 조직 전환 아닌 제품 사양이며 Vial(p.4)의 실체(조직) 속성 변화 증거 전무, Neumann(p.120) assessing 단계의 전환 호명. |
| SoftBank × OpenAI 사이버 자기실험(Daybreak) | SoftBank · 「Special Event Hosted by SoftBank Corp., SB OAI Japan GK…」(손정의×Mark Chen 법인 특별 이벤트) | AT | determined | AX | 발굴→재현·검증→패치 생성→회귀테스트 파이프라인으로 700개 시스템 취약점 10,500건·반복 스캔 22→5건 — Vial(p.4) 정량적 속성 변화. 보안기능 전체의 활동 변형+3,000개사 무상 'Patching as a Service'로 경계 확장(인력 50→1,000명 계획) — Holmström(p.331) 2요소, Verhoef(p.891) 신규 서비스 모델 → AT. 단 패치 실행은 인간 결정(HITL), 발표 직후라 determined. |
| 미쓰이스미토모카드 X-Ghost 콜센터 | SoftBank · 「コンタクトセンター向け自律思考型AIオペレーター「X-Ghost」が始動」 | D3-auto | assessing | AX† | speech-to-speech 에이전트가 응대를 자율 수행하고 고위험만 인간 이관 — 콜센터 응대라는 단일 과업 automation(Raisch·Krakowski p.192, Wamba p.864 TE 수준). "업무 70% AI 담당"은 구상 단계로 Neumann(p.120) assessing 보수 판정, Verhoef(p.891) 전사성 미충족 → D3-auto. |
| SoftBank 전사 에이전트 제작 운동 | SoftBank · 「わずか2カ月半で250万超のAIエージェントを作成」(ソフトバンクニュースPodcast) | 워싱 | assessing | DX(AX 표방)† | KPI가 제작 개수(2.5개월 250만 개)·"이해 깊어짐" 등 교육 지표로, 자율 수행 성과 미검증 — 실질은 도구 보급·e러닝(D2 이하). 성숙도 assessing 단계를 전사 전환으로 호명 — Neumann(p.120) 위반, 워싱 정의 충족. |
| 베트남 통신 3사 국가 AX 분업 | 키워드 수집(Vietnam Off The Record) · 「Vietnam's AI Transformation (AX) 2025: Telecom Giants & National Strategy」 | 워싱 | assessing | DX† | 2030 GDP +$790억 등 전망치와 분업 전략 선언뿐, 실행·자율화 실증 전무(제3자 분석 채널, 출처 미상 수치) — 로드맵·목표 연도만 있는 사례로 Neumann(p.120) assessing 보수 판정. 'AX' 호명 대비 실질 부재 → 워싱. |

**재판정 변동 요약**: 기존 AX 4건 중 톈진항·SoftBank 사이버만 AT로 살아남았고(정량 증거+Holmström 2요소), 중국 자동차사 하네스와 X-Ghost는 자율성 미공개·구상 단계라는 이유로 과업 수준 D3-auto로 강등됐다. DX→AX 2건은 도착점이 선언(İşbank→D2) 또는 단일 프로세스(AIDBS→D3-auto)에 그쳐 모두 하향됐으며, 'AX 표방' 2건(BMW·SoftBank 운동)에 실증 없는 국가전략 담론인 베트남까지 더해 워싱이 3건으로 늘었다.

### 자율주행·물리 AI (10건)

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| 현대차 × NVIDIA 자율주행·로봇·공장 | 키워드 수집(차플레이) · 「현대차 '피지컬 AI'에 51조 투자 발표, 엔비디아-구글-웨이모까지…」 | D2 | assessing | DX→AX† | 디지털트윈 가상 커미셔닝·센서 표준화는 기존 제조·개발 프로세스의 기술적 개선 — Verhoef(p.891) digitalization. 자율주행 양산은 2028년경 로드맵뿐 — Neumann(p.120) assessing 보수 판정, Vial(p.4) 속성 변화의 정량 증거 부재 → D2. |
| 현대차 × Waymo 로보택시 파운드리 | 키워드 수집(차플레이) · 「현대차 '피지컬 AI'에 51조 투자 발표…」(동 영상) | D2 | assessing | DX→AX† | 현대의 활동은 안전사양 강화 차량의 위탁 양산으로 기존 제조 활동의 연장이며, 자율 판단은 Waymo Driver(타사 제품) 몫 — Vial(p.4)의 실체=조직 기준에서 현대 조직 변형 증거 없음. '파운드리' 신규 BM(Holmström p.331 경계)은 "수만 대 공급 계획" 단계 — Neumann(p.120) assessing → D2. |
| 현대차 × Google DeepMind 휴머노이드 두뇌 | 키워드 수집(차플레이) · 「현대차 '피지컬 AI'에 51조 투자 발표…」(동 영상) | 워싱 | assessing | AX† | 실체는 파트너십 발표+2028년 연 3만 대 '목표'뿐으로 자율 작업의 실증 전무(핵심인력 유출 리스크 병기) — 로드맵·목표 연도만 있는 사례. assessing 단계를 AX로 호명 — Neumann(p.120) 위반, 실질 D2 이하 → 기존 AX에서 워싱으로 강등. |
| 현대차 국내 투자 데이터 플라이휠 | 키워드 수집(차플레이) · 「현대차 '피지컬 AI'에 51조 투자 발표…」(동 영상) | D2 | assessing | DX→AX | 51조는 데이터센터·공장 인프라 투자 = 기존 프로세스 기반의 기술적 구축 — Verhoef(p.891) digitalization. "학습→탑재→수집→재학습" 플라이휠은 설계 단계이고 "자동차 회사 아니다"는 목표 선언 1요소뿐(Holmström p.331) — Neumann(p.120) assessing → D2. |
| Nissan × Wayve 양산 ADAS | Wayve · 「Alex Kendall takes Ivan Espinosa, President & CEO Nissan Motor…」(요코하마 데모)·「Ride the Wayve: Through a Typhoon in Tokyo」 | D3-aug | assessing | AX | E2E 모델이 주행 판단을 수행하나 ADAS(차세대 ProPilot)는 운전자 감독하의 인간-AI 협업 — Raisch·Krakowski(p.192) augmentation. 닛산 조직 차원에선 제품 개발 활동의 개선일 뿐 Holmström(p.331) 3요소 중 목표 선언만, Verhoef(p.891) 신규 BM 없음 → D3-aug. 양산 전 데모·통합 단계 — assessing. |
| Wayve × Ford/Qualcomm 플랫폼 | Wayve · 「Qualcomm and Wayve Advance Production-Ready End-to-End AI」·「Ride The Wayve: 60/75 minutes Uninterrupted」 | D3-auto | determined | AX | 신경망이 맵·규칙 없이 주행 과업을 자율 수행(런던 60~75분 무개입)하나 이는 제품의 자율성 — Vial(p.4)의 실체는 조직이며, Wayve는 창업 시점부터 E2E 자율주행이 본업이라 활동·경계·목표(Holmström p.331)의 '변형' 증거가 없음. 주행 과업 automation — Raisch·Krakowski(p.192) → D3-auto. 반복 실증·양산 협력으로 determined. |
| Zoox × Amazon/AWS 컴퓨트·자본 | Zoox · 「Inside The Ride: Scaling Zoox Episode One」·「Blueprints for the Future: The System Design of the Zoox Robotaxi」 | D3-auto | managed | AX | 무인 로보택시 100대+ 상용 운행과 오프라인 대형모델의 시나리오 검토 대체(수백 명 몫, 지오펜스 4배)는 주행·검증이라는 과업/프로세스 수준 automation — Raisch·Krakowski(p.192), Wamba(p.864) TE. 가동률 판매 BM은 창업 모델이라 Verhoef(p.891) '신규' BM 아니며 Holmström(p.331) 3요소 중 활동만 변형 → D3-auto. SDMA 안전케이스·생산 체제로 프로세스 정의 — managed. |
| Tesla × SpaceX·xAI TERAFAB | Tesla · 「TERAFAB: The Largest Chip Manufacturing Facility Ever」 | 워싱 | assessing | DX(AX 표방)† | 테라와트 컴퓨트·휴머노이드 연 10억~100억 대 등 검증 불가 비전 서사뿐, 실행·정량 실증 전무 — Vial(p.4) 속성 변화 증거 0. 선언 단계를 전환 서사로 호명 — Neumann(p.120) assessing 위반, 워싱 정의 충족. |
| Boston Dynamics 제조 고객 | Boston_Dynamics · 「Why Humanoids Are the Future of Manufacturing」(웨비나) | D3-aug | assessing | AX† | 시연 기반 사후훈련(원격조작 교육)으로 인간-로봇 협업 학습 루프를 만드는 단계 — Raisch·Krakowski(p.192) augmentation. 목표 신뢰도 99.7% 미달을 자인하고 고변동 단일 과업(부품 시퀀싱)부터 진입 — Wamba(p.864) 과업 수준, Neumann(p.120) assessing. 조직 전환 아닌 파일럿 → D3-aug (정직한 공시로 워싱은 아님). |
| Siemens × AWS·Microsoft 산업 AI 팩토리 | Siemens · 「The Industrial AI Revolution: Siemens Keynote at CES 2026」 | 워싱 | assessing | DX(AX 표방)† | 중앙 AI 팩토리+엣지 이원 구조는 키노트 수사이며 자율 판단의 고객 실증 부재(케이스북 자체가 washing 성향 명기) — 실질은 디지털트윈 기반 D2 이하. assessing 단계의 전환 호명 — Neumann(p.120) 위반 → 워싱. |

**재판정 변동 요약**: 기존 AX 5건이 전부 강등된 것이 최대 변동 — Wayve·Zoox는 '제품이 자율적'일 뿐 조직(Vial p.4의 entity) 변형 증거가 없어 D3-auto로, Nissan·Boston Dynamics는 인간 감독하 협업·파일럿이라 D3-aug로, 현대×DeepMind는 2028 목표뿐이라 워싱으로 내려갔다. 현대차 계열 DX→AX 3건은 도착점이 모두 로드맵이어서 Neumann(p.120) assessing 원칙에 따라 D2로 수렴했고, 결과적으로 이 클러스터에는 AT가 한 건도 남지 않았다 — 물리 AI의 자율성은 아직 과업 수준 실증과 비전 서사 사이에 있다.

---

### 통신·주권·국가

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| H Company×Orange 컴퓨터유즈 에이전트 | Orange · 「Agentic AI, Trust & Scale — Jérôme Berger(Orange) & Gautier C…」 | **D3-auto** | determined | AX | 에이전트가 화면을 보고 자율 조작하나 병원 전산 수작업이라는 단일 과업 대체 — Raisch·Krakowski(p.192) automation. "응급실 대기시간 단축"은 정량 미제시로 Vial(p.4) 실체 속성 변화 입증 불가, Holmström(p.331) 3요소 중 활동만 변형, Verhoef(p.891) 전사성·신규 BM 부재 → D3-auto. |
| Dataiku×Orange 에이전틱 데이터 플랫폼 | Orange · 「The Impact of Agentic AI on Telco Transformation & Innovation」 | **D3-auto** | determined | AX | 에이전트가 재무 데이터 결합을 자율 수행(수 주→수 시간, Vial p.4 정량은 프로세스 수준)하나 조달·법무라는 특정 워크플로에 국한 — Wamba(p.864) 프로세스 수준 TE, Raisch·Krakowski(p.192) automation. Holmström(p.331) 3요소 중 활동만 변형 → D3-auto. |
| 텔코 얼라이언스 12사 스타트업 공동투자 | Orange · 「The Impact of Agentic AI on Telco Transformation & Innovation」(동 패널) | **워싱** | assessing | DX† | 에이전틱 AI를 표방하나 실질은 스타트업 심사·투자 채널 구축으로 자사 프로세스의 AI 변형이 전무 — Verhoef(p.891) 기준 digitalization에도 미달하는 선언 단계, Neumann(p.120) assessing(실험 착수 이전)을 전환 담론으로 호명 → 워싱. |
| Institut Curie×Orange 의료 XAI | Orange · 「La confiance, un facteur clé du déploiement de l'IA en santé」 | **D3-aug** | assessing | DX→AX† | 딥러닝이 암 원발부위를 판단하나 최종 결정·환자 설명 주체는 의사(HITL 유지) — Raisch·Krakowski(p.192) augmentation의 전형. 단일 진단 과업으로 Holmström(p.331) 3요소 중 활동 일부만 변형, Verhoef(p.891) 전사성 부재, † 보수 판정 → D3-aug. |
| Bleu·Cloud Avenue 주권 인프라 | Orange · 「La confiance, un facteur clé du déploiement de l'IA en santé」(동 패널) | **D2** | assessing | DX | 주권 클라우드·인프라 구축으로 AI 판단 요소 자체가 없음 — Verhoef(p.891) digitalization(기존 프로세스의 기술 기반 정비). Vial(p.4) 실체 속성 변화·Holmström(p.331) 3요소 변형 근거 없음 → D2. |
| Elisa×Nokia×NVIDIA AI-RAN 상용화 | Nokia · 「Nokia, Elisa & NVIDIA: Accelerating AI-RAN from concept to commercial」 | **D2** | assessing | DX→AX† | 현재 실증은 핀란드 인프라 PoC이고 "자율 네트워크"는 2027년 상용 SW 로드맵뿐 — 프레임 규칙상 현재 실증 단계로 판정: Verhoef(p.891) digitalization, Neumann(p.120) assessing. 도착점 자율화는 미실증이므로 (이행 중) 부기 불가 → D2. |
| T-Mobile·SoftBank·Indosat×Nokia AI-for-RAN 검증 | Nokia · 「Nokia and NVIDIA collaboration accelerates AI-RAN deployment」(AI-RAN 플랫폼 발표) | **D2** | assessing | DX† | 채널추정·링크적응 등 사람이 정의한 최적화 문제를 AI 알고리즘이 푸는 구조화 PoC(스펙트럼 효율 20%+)로 기존 무선 프로세스의 기술적 개선 — Verhoef(p.891) digitalization. 자율 분기·워크플로 재설계 근거 없어 Raisch·Krakowski(p.192) automation에도 미달 → D2. |
| Scale AI×산업 190개 프로젝트 | Scale AI · 「Scale AI @ ALL IN 2025: Back to the future of Canadian AI — 6 years of Scale AI」 | **D2** | determined | DX→AX† | 190개 포트폴리오 중 배치 최적화 일부에 AI 판단이 있으나 다수는 데이터 파이프라인형 도입이라고 자체 공개(중앙값<평균 자인) — 지배적 실질은 Verhoef(p.891) digitalization, 개별 과업형은 Wamba(p.864) TE 수준. 단일 실체의 전환이 아닌 펀딩 프로그램, † 보수 판정 → D2. |
| Telefónica CMD 2025 EU 주권 프레임 | Telefónica · 「Telefónica Capital Markets Day 2025 (ES)」 | **워싱** | assessing | DX† | "Transform & Grow"를 표방하나 실질은 투자자 담론·시장 기회 계량(€100억~220억)으로 전환 실행 실증이 없음 — Vial(p.4) 실체 속성 변화 증거 전무, Neumann(p.120) assessing 이전의 선언을 전환으로 호명 → 워싱. |
| 오렌지 아프리카·중동 포용 AX | Orange · 「Social Inclusion and Fintech: Balancing Innovation and Equity」 | **워싱** | assessing | DX(AX 표방)† | "포용 AX"로 명명되나 실질은 디지털센터·교육·현지어 LLM·모바일머니 인프라 구축 — Verhoef(p.891) digitization~digitalization 수준. AI 자율 판단 요소 없이 AX 명명이 실질을 앞서감(Neumann p.120 assessing 단계의 전환 호명) → 워싱. |

**재판정 변동 요약**: 기존 AX 2건(H Company·Dataiku)은 에이전트 자율성이 실재하나 단일 과업/워크플로 수준을 넘지 못해 Raisch·Krakowski(p.192)·Wamba(p.864) 기준 D3-auto로 전원 강등됐고, 이 클러스터에 AT는 0건이다. DX→AX로 분류됐던 3건(Curie·Elisa·Scale AI)은 도착점(자율 네트워크 등)이 로드맵뿐이어서 현재 실증 단계인 D3-aug/D2로 내려앉았다. 표방성이 강한 3건(텔코 얼라이언스·Telefónica CMD·오렌지 아프리카)은 Neumann(p.120) assessing 이전의 선언·채널·인프라를 전환으로 호명한 워싱으로 재판정됐다.

### 생성미디어·도구·수요기업

| 사례 | 출처(YouTube) | 재판정 | 범위(Neumann p.120) | 기존 | 판정 근거(논문·페이지 명시) |
|---|---|---|---|---|---|
| ElevenLabs·Hasbro 광고 국제화 | ElevenLabs · 「ElevenLabs Built an AI Ad Tool That Drove $3.78M — Then Launched It」 | **AT** | determined | AX | Vial(p.4) 정량 충족(ROAS 7.16·증분 $3.78M — 단 자사 발화, lift test 진행 중). Holmström(p.331) 3요소 중 2개 변형: 활동(스프레드시트 수작업→AI 일체형 파이프라인, 4인·신규채용 0)+경계(7~9개 언어 시장 확장, 내부 도구의 Ads Engine 외부 상품화). 상품화는 Verhoef(p.891) 신규 BM에 해당하며 마케팅 국제화 기능 전체 범위 → AT. |
| Deutsche Telekom 음성 CX | ElevenLabs · 「How Deutsche Telekom Is Deploying AI Voice Agents to Millions」 | **D3-auto** | managed | AX | L1 통화 자동화라는 단일 프로세스 대체(인간은 예외·QC로) — Raisch·Krakowski(p.192) automation, Wamba(p.864) TE 수준. Holmström(p.331) 3요소 중 활동만 변형(역할 재정의는 활동 변형의 일부), Verhoef(p.891) 신규 BM 없음, 해결률 등 성과 정량 미제시로 Vial(p.4) 미충족. SOP 15,000건 Gherkin화·4C·3개월 규칙은 Neumann(p.120) managed(적용 프로세스 정의)를 입증하나 범위 판정일 뿐 → D3-auto. |
| BCG·Naturgy·Konecta 에이전트 | ElevenLabs · 「How BCG, Naturgy, and Konecta Are Deploying AI Agents in Production」 | **D3-auto** | determined | AX | 에이전트가 통화 35만 건+를 자율 처리하나 콜센터 단일 프로세스 — Raisch·Krakowski(p.192) automation. "도입기업 80% 사업부 재편"은 BCG 일반론 발화로 Holmström(p.331) 경계 변형의 사례 증거가 아니며, Verhoef(p.891) 전사성·신규 BM 미충족 → D3-auto. |
| Netflix·할리우드×Runway 대담 | Runway · 「A Conversation with Girish Balakrishnan & Joel Kuwahara」·「A Conversation with Ron Howard」(Runway AI Festival 2026) | **워싱** | assessing | DX(AX 표방)† | 전 세션 정량 0, 유명인 권위 서사만(Avary 연 52편 야망은 미실현 자인) — Vial(p.4) 실체 속성 변화 증거 전무, Neumann(p.120) assessing에도 못 미치는 담론을 산업 전환 서사로 유통 → 워싱. |
| FaZe Apex×Replit 창업 | Replit · 「FaZe Apex: From content empire to startup founder (Between Builders)」 | **D3-aug** | determined | AX | 에이전트가 빌드·자가테스트·디버깅을 수행하나 창업자가 방향·검수를 담당하는 인간-AI 협업의 개발 과업 수준 — Raisch·Krakowski(p.192) augmentation. 기존 조직의 속성 변화가 아닌 1인 신규 프로덕트(100k ARR)로 Vial(p.4)의 실체 전환·Verhoef(p.891) 전사성 개념이 성립하지 않음 → D3-aug. |
| Replit 내부 자가검증 | Replit · 「Inside Replit Agent with a lead AI engineer」 | **D3-auto** | assessing | AX | 자가검증은 코드 품질이라는 단일 개발 과업 내 자율 판단이며 분포 이탈 시 실패를 자진 공개 — Raisch·Krakowski(p.192) automation의 과업 수준, Neumann(p.120) 실험(assessing) 단계. 조직 활동·경계·목표 변형(Holmström p.331) 해당 없음 → D3-auto. |
| Zapier×Anthropic 자동화 | Zapier · 「Zapier AI Benchmark: How to choose the right AI model」·「Eric Ries on Vibe Coding」 | **D3-auto** | determined | DX→AX | 규칙 워크플로 위에 에이전트를 얹었으나 최고 모델 성공률 70.17%(600과제)로 자율화 미완을 자체 공개 — Raisch·Krakowski(p.192) automation의 과업 수준, Wamba(p.864) TE. 기존 자동화 BM의 연장으로 Verhoef(p.891) 신규 BM 아님 → D3-auto. |
| Pringles/Kellanova×Siemens 공정 | Siemens · 「AI-Based Process Control at Scale: Pringles and Siemens on Digital…」 | **D3-auto (이행 중)** | determined | DX→AX | 디지털트윈(DX) 위에서 규칙기반→목표기반 제어로 AI가 공정 제어를 판단하는 이행이 Kutno 검증→확산으로 명시적 — Raisch·Krakowski(p.192) automation, 단 생산 공정 단일 프로세스이고 2~10% 증산·에너지 7%↓는 목표치라 Vial(p.4) 정량 미충족, Verhoef(p.891) 전사성 부재 → D3-auto(이행 중). |
| Unilever R&D·마케팅 | Unilever · 「Deutsche Bank Global Consumer Conference 2026」·Q2/H1 2026 실적발표 | **D3-aug (이행 중)** | managed | DX→AX† | 혁신주기 2~3년→9~12개월은 Vial(p.4) 정량이나, 본체는 데이터 2,500만 건 정비·R&D 디지털화(Verhoef p.891 digitalization)이고 AI 시나리오는 인간 의사결정 보조 — Raisch·Krakowski(p.192) augmentation. Holmström(p.331) 3요소 중 활동 변형은 확실하나 경계·목표 변형은 담론(LLM 해자) 수준, † 보수 판정 → D3-aug(이행 중). LLM 순위 일일 추적 등 프로세스 정의로 범위는 managed. |
| GE HealthCare 초음파 AI | GE HealthCare · 「AI in Regional Anesthesia: Smarter Ultrasound Guidance」 | **D3-aug** | determined | DX† | 벤더 스스로 "자율주행차가 아니라 GPS"로 한정, 해부구조 하이라이트로 인간 시술을 보조하고 판단 주체는 임상의 — Raisch·Krakowski(p.192) augmentation의 명시적 사례. 단일 진단·시술 과업으로 Holmström(p.331)·Verhoef(p.891) 전환 요건 해당 없음 → D3-aug. |
| IQVIA Vigilance | IQVIA · 「IQVIA Vigilance Platform with AI Assistant」 | **D3-auto** | determined | AX | 신뢰도 점수로 자동/수동을 분기하고 인간은 예외 큐만 검토하나 부작용 보고 처리라는 단일 프로세스 — Raisch·Krakowski(p.192) automation, Wamba(p.864) TE. "몇 시간→몇 분"은 자사 데모 기준이고 임상개발 116→52개월은 산업 통계로 인과 귀속 불가 → Vial(p.4) 실체 수준 정량 미충족, D3-auto. |
| Philips 의료 워크플로 | Philips · 「How Philips Is Turning AI Into Real Healthcare Impact (Jeff D…)」 | **워싱** | assessing | DX(AX 표방)† | "제품 중심→생산성 중심 회사" 선언 중심이며 MRI 시간 절반~1/3은 방법론 미제시 발화 — Vial(p.4) 검증 가능한 속성 변화 증거 부재, Neumann(p.120) assessing 단계 선언을 전환으로 호명 → 워싱. |
| LinkedIn 노동시장 데이터 | LinkedIn · 「2026 Labor Market Report: Building a Future of Work That Works」 | **D2** | assessing | DX | 13억 회원 정형 데이터의 분석·리포트 산출로 AI 자율 판단·워크플로 변형이 없음 — Verhoef(p.891) digitalization 수준의 데이터 활용. 자사 전환 시도 자체가 아니므로 Holmström(p.331) 3요소 변형 해당 없음 → D2. |

**재판정 변동 요약**: 기존 AX 6건 중 AT로 살아남은 것은 ElevenLabs·Hasbro 1건뿐으로, Holmström(p.331) 활동+경계 2요소 변형과 Verhoef(p.891) 신규 BM(Ads Engine 상품화)을 동시 충족한 유일 사례다. Deutsche Telekom·BCG-Konecta·IQVIA·Replit 등 나머지 AX는 자율성이 실재해도 L1 통화·예외 분기·코드 검증이라는 단일 프로세스 대체(Raisch·Krakowski p.192; Wamba p.864)에 그쳐 D3-auto로 강등됐고, FaZe Apex는 협업형이라 D3-aug다. DX→AX 이행형 중 Siemens·Unilever는 이행 경로가 실증돼 "(이행 중)"을 유지하되 과업 수준(D3)으로, Runway·Philips는 정량 0의 선언·권위 서사로 워싱 확정됐다.

---

**분포 집계(담당 23건)**: AT 1 · D3-auto 8 · D3-aug 4 · D2 5 · D1 0 · 워싱 5
