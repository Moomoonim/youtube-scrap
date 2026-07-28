# AX 솔루션 지도 — 회사·솔루션·기능·핵심 (2026-07-27)

> 코퍼스(4,487건, 채널 199개) 정독에서 추출한 **행위자·제품·기능·핵심주장** 정리.
> ⚠️ **읽는 법**: 이 표는 제품 감사(audit)가 아니라 **담론에서 각 회사가 스스로 무엇이라 주장하는가**의 지도다. 수치·기능은 자사 발화 기준이며, 워싱 위험 표기(§ 워싱)를 함께 볼 것. 연구 목적은 "AX 담론 → 비용구조 변화"이므로, 각 행의 마지막 열(**핵심/비용함의**)이 K1 병합의 연결점이다.

---

## 1. AX 스택 계층 지도

AX 담론은 아래 9개 계층으로 정연하게 나뉜다. **락인(고착)이 일어나는 곳은 모델(L2)이 아니라 데이터/거버넌스 계층(L3)과 오케스트레이션(L4)**이라는 것이 코퍼스의 반복 명제다.

### L1. 실리콘 · 전력 · 데이터센터 인프라
| 회사 | 솔루션/제품 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **NVIDIA** | AI Factory, GB300·Rubin·Kaiver 랙 | GPU 오케스트레이션, "월 4조 토큰" | "비용센터→토큰 수익원"(분모: 토큰). GB300 MB72 랙 135~155kW |
| **AMD** | EPYC(Agentic AI), Instinct MI355/MI455X, Helios Rackscale | 개방형 랙스케일, "concurrency" | NVIDIA에 **"open vs lock-in"**·**agents per watt/dollar/rack**로 대항 |
| **Arm** | 컴퓨트 IP | 전력효율 | "power is not free" — 전력이 곧 원가 |
| **Vertiv** | 데이터센터 전력·냉각 | 800V DC, 액체냉각, SmartIT | 랙 140kW→1MW, 350~400kW 구리 물리한계, KPI="tokens/watt/sec" |
| **Schneider Electric** | 전력관리 | 에너지 인프라 | "AI=전력수요 유발자" |
| **SK hynix** | HBM(고대역폭메모리) | HBM3E/HBM4 | AI 메모리 병목 = 원가·공급망 핵심 |
| **Intel** | Xeon·Gaudi | CPU/가속기 | (배경 인프라) |
| **Huawei** | Ascend NPU, CloudMatrix, ModelArts | 자국 칩+멀티모델 | 중국 스택 자립 — 단 담론상 "주권" 지우고 신뢰·비용 전면화 |

### L2. 파운데이션 모델
| 회사 | 솔루션/제품 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **OpenAI** | ChatGPT Enterprise, Codex | 위임(delegation), 에이전트 | "팀→상담원 하나", 레퍼런스 고객 포맷(BNY·Shopify) |
| **Anthropic** | Claude, Claude Code, Project Glasswing | 자율 에이전트, 보안 | "며칠간 무개입 자율작동"(agent=자율노동력) |
| **Google/DeepMind** | Gemini, Gemini Enterprise, Gemma | 멀티모달, 에이전트 | "빌드는 쉽고 프로덕션이 어렵다→간극을 메움" |
| **Meta** | Llama | 오픈웨이트 | (오픈소스 배포) |
| **Alibaba** | Qwen, AIDBS(AI-native DB) | 에이전트=인력 | "2027년 DB 인스턴스 50%+가 에이전트 사용" |
| **LG AI Research** | EXAONE | 온디바이스·제조특화 | 누적 510만 다운로드, "AI 비용의 본질=에너지" |
| **NAVER Cloud** | HyperCLOVA X, 뉴로클라우드 | 소버린+설치형 | 자국모델+데이터주권, 미국 Claude 병용(하이브리드) |
| **Upstage** | Solar, Document Parse | 도메인특화·한국어 | "범용 LLM 못하는 정확도"·"인건비 80%↓" |
| **Cohere** | Command, Cohere Labs | 엔터프라이즈/연구 | ⚠️채널은 학술발표(비용담론 부재) |
| **Hugging Face** | FineWeb, Transformers.js, LeRobot | OSS·데이터·로보틱스 | 공급측 연구("스케일링→적응") |
| **xAI** | Grok | (프론티어 경쟁) | 가성비 경쟁 축 |

### L3. 데이터 · 컨텍스트 · 거버넌스 계층 (⭐ 진짜 락인)
| 회사 | 솔루션/제품 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **Palantir** | Foundry, AIP, **Ontology** | 온톨로지=인간·AI 공통언어 | "챗봇=요정, 의사결정에 내재된 시스템이 진짜"(증강 vs 대체) |
| **ServiceNow** | Now Assist, context graph, Action Fabric, AI Control Tower | 워크플로 데이터패브릭 | 타 플랫폼(Gemini/Bedrock)까지 거버넌스, "L1 대체" |
| **Databricks** | Unity Catalog, LakeWatch | 데이터 거버넌스 | "세계 최초 에이전틱 CDP"(⚠️워싱), "400명 팀 필요" |
| **Snowflake** | Cortex | 데이터 클라우드 | 데이터=결정 원천 |
| **Oracle** | Sovereign Cloud, Whitespace | signal→context→action | "맥락 없으면 강화된 ChatGPT일 뿐"(최정교 anti-washing) |
| **Pinecone·Weaviate·Qdrant** | 벡터 DB | 임베딩 검색·메모리 | 에이전트 기억=벡터 계층 선점 |
| **LlamaIndex** | LlamaParse | 문서 하네스 | "기업가치 90%가 비정형 문서에 묻힘" |
| **IQVIA** | Vigilance Platform | 제약 데이터+AI Assistant | 약물감시 "몇 시간→몇 분"(예외기반) |

### L4. 에이전트 오케스트레이션 · 개발 도구
| 회사 | 솔루션/제품 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **AWS** | Bedrock·**Strands**·AgentCore | 모델(두뇌)+하네스+운영 | context_manager로 "토큰 55%↓·정확도 68→98%", **평가(eval)가 전장** |
| **Google Cloud** | ADK, Antigravity, Agent Platform | SDLC 자동화, MCP | "80% speedup"(분모스왑 실시간 포착) |
| **GitHub** | Copilot | 코딩 에이전트, 크레딧 과금 | Kimi K2.7 100만토큰=95크레딧, "비용 센터"·월 $50 한도 |
| **Replit** | Agent, 병렬 에이전트 | 바이브 코딩 | "코드 희소→생성 저렴한 세상" |
| **Zapier** | MCP(9,000앱), Agents, Skills, Automation Bench | 앱 온톨로지+거버넌스 | "실험→인프라", 자체 벤치마크로 모델선택=비용×정확도 |
| **Microsoft** | Copilot, Azure AI Foundry | 엔터프라이즈 코파일럿 | "망가진 워크플로에 AI 얹으면 실패" |
| **Kore.ai** | 에이전트 플랫폼(BCG 협업) | 도입방법론 | **"생산성 <15%면 P&L 반영 불가"**(분모 임계) |

### L5. 엔터프라이즈 애플리케이션 · 수직 솔루션
| 회사 | 솔루션/제품 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **SAP** | Joule, Agent-led migration | 자율기업, 마이그레이션 | "노력 35~50%↓", ECC 2027/2030 만료가 강제 동인 |
| **Salesforce** | Agentforce | 영업/CS 에이전트 | 파이프라인·시간절약 환산액(⚠️대시보드 실사용률 20~30% 자인) |
| **삼성SDS** | Brity, FabriX, AX센터 | 에이전트 오케스트레이션+거버넌스 | 우리은행 175에이전트, "토큰=ROI 단위", CAIO·AI크루 107명 |
| **SK AX** | AI Workforce | 에이전트 인력 | ⚠️사례 제로(워싱) |
| **Tigerhall** | AX-office 플랫폼 | data flywheel | 도입률 90일 91%, "FTE avoidance ≠ layoff" |
| **ServiceNow/Workday류** | HR·ITSM 에이전트 | 업무 자동화 | 반복업무 대체 |

### L6. 생성 미디어
| 회사 | 솔루션 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **ElevenLabs** | 음성 생성 | 다국어 더빙 | "4인·신규채용0·7개국·ROAS 7.16" |
| **Runway** | 영상 생성(Aleph) | 편집·매트 | 유명인 권위(⚠️워싱), API |
| **Stability AI** | Brand Studio | 브랜드 이미지 | "프롬프트 노동 제거", 세일즈 비용구조 노출 |
| **Luma AI·Suno** | 영상·음악 | 생성 | (배경) |

### L7. 물리 AI · 로보틱스 · 자율주행
| 회사 | 솔루션 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **Tesla** | Optimus, FSD, TERAFAB, Autobidder | AI/에너지/로봇 | "자동차 회사 아님"(정체성화), 옵티머스 "연 10~100억 대" |
| **현대차** | 피지컬 AI(51조 투자) | 자율주행+로보틱스+스마트팩토리 | "이제 자동차 회사 아니다"(Tesla 극점 합류), "피지컬 AI는 절대 틀리면 안 됨" |
| **Boston Dynamics** | Atlas·Spot | 휴머노이드/4족 | "남들은 안 넘어지는 영상만 보여준다"(anti-washing) |
| **Figure** | 휴머노이드 | speech-to-speech | ⚠️자막 공동화(활용불가) |
| **Zoox** | 로보택시(purpose-built) | 핸들·페달 없는 재설계 | "vibe driving은 안전엔 부적합"(end-to-end 거부) |
| **Wayve** | 자율주행 SW(end-to-end) | 기존차에 학습 얹기 | "4~6개월 만에 새 나라 일반화" |
| **Waymo** | 로보택시 | 라이다+HD맵 | 안전·확장 |

### L8. 컨설팅 · 도입 방법론
| 회사 | 역할 | 핵심 프레임 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **McKinsey** | 전략 | State of AI | "88% 도입 vs 39% 수익화"(도입-성과 괴리) |
| **BCG** | 전략(장진석·Nick Clarke) | 기술비용 재배분 | "15% P&L 임계", 배수 수사("10배") |
| **Accenture** | 구현 | 스킬 아키텍처 | "기술비용 70%가 레거시 유지"·"직무→스킬" |
| **TCS·Infosys** | IT서비스 | 레거시 현대화 | "수년→몇 달"; Infosys는 고객(Sandvik·Swedbank) 대리화자 |
| **a16z(Levie 등)** | VC/논평 | 반-회의론 | "95% 실패=멍청한 통계", agent=인간 신입 |
| **Scale AI(캐나다)** | 정부 클러스터 | 국가 촉매 | "AI 특허 96% 무효", 분모스왑 반박 |

### L9. 통신 · 주권 · 국가 (state 축)
| 주체 | 솔루션/프레임 | 핵심 기능 | 핵심 주장 / 비용 함의 |
|---|---|---|---|
| **Orange(프랑스)** | 4C→5C, 텔코 Alliance | 데이터+harness 주권 | "magic wand 아닌 인간중심 도구상자", Orange Money |
| **Telefónica(스페인/EU)** | AI-native SOC | EU 기술주권 | "유럽 주권의 첫걸음" |
| **Nokia** | AI-native RAN | 네트워크 AI | "cost per delivered bit", "no GPU premium" |
| **소버린AI Korea** | SKT A.X-K2, SK 15GW | 국가대표 AI | "돈이 국내 순환", 손정의 "한국 약점=에너지" |
| **Vietnam** | 통신 3사 국가분업 | Viettel/VNPT/MobiFone | 2030 GDP +$790억 |

---

## 2. 반복되는 기능(capability) 축 — "무엇을 파는가"

계층을 가로질러 **8개 기능 유형**이 반복된다. AX 제품은 결국 이 조합이다.

1. **에이전트 오케스트레이션** — 다중 에이전트 조율(Swarm/Graph/Hub-spoke). 거의 모든 L4·L5.
2. **컨텍스트/메모리 관리** — RAG·벡터·세션·온톨로지. 원가(토큰)·정확도의 핵심 레버.
3. **거버넌스/평가(eval)** — 가드레일·감사·벤치마크. "어느 에이전트가 좋은가"의 정의권 = 새 전장.
4. **워크플로 재설계** — 업무를 단계로 쪼개 판단기준·KPI를 채움(=의사결정 알고리즘화의 실체).
5. **레거시 현대화/마이그레이션** — ECC·Oracle→클라우드. 강제 동인(라이선스 만료).
6. **원가 거버넌스(FinOps)** — 토큰·크레딧 미터링·한도. AX가 예산으로 번역되는 지점.
7. **도메인특화/데이터주권** — 한국어·규제·온프렘. 정확도·주권 트레이드오프.
8. **물리 구현(센서→액추에이터)** — 자율주행·로봇. "절대 틀리면 안 됨" 신뢰성 제약.

---

## 3. ⭐ 무엇이 핵심인가 — 계층을 관통하는 5개 본질

제품 다양성 아래에서 반복되는 **본질(essence)**은 다음 5가지이며, 이것이 곧 연구 프레임("의사결정의 알고리즘화")과 직결된다.

1. **"측정 단위를 쥔 자가 ROI를 쥔다"(분모 바꾸기)** — 토큰→에이전트, usage→outcome, scaling→adaptation, 데모→벤치마크. 그리고 Kore.ai의 "15% 임계"처럼 이제 계량 눈금까지. **AI가 결정하기 이전에, 'AI 가치를 어떻게 셀지'라는 판단 기준 자체가 이해당사자에 의해 재작성된다.**

2. **"진짜 락인은 모델이 아니라 컨텍스트/거버넌스 계층"** — Palantir 온톨로지·ServiceNow context graph·벡터DB·LlamaIndex 문서하네스. 모델은 교체 가능하나, 데이터+의사결정 규칙 계층을 쥔 자가 지배.

3. **"에이전트=인력(AI Workforce)"의 문자화** — Alibaba·OpenAI·삼성SDS·a16z(ACL·온보딩 부여). 노동을 '인력 단위'로 세는 담론이 미·중·한 공통. → 비용구조에서 인건비 대체/이연의 근원.

4. **"데이터≠결정"** — Oracle(signal→context→action)·Huawei(single source of truth). 데이터 축적이 아니라 **의사결정 우위(decision superiority)**가 목표. 프로젝트 핵심 프레임 직결.

5. **"AI를 말하는/안 말하는 방식 자체가 전략"** — 자동차 4분화(침묵~정체성화), state 축 블록화(중국 탈주권~서방 동맹주권), 사람 소거 vs 전면화(개발자 vs 경영진 청중). 담론 표면은 **청중·이해관계로 통제**되므로 액면 그대로 읽으면 안 됨.

---

## 4. 회사별 "한 줄 핵심 주장" 색인 (빠른 참조)

- **NVIDIA**: 토큰이 곧 매출이다. / **AMD**: 개방형이 락인을 이긴다. / **Vertiv**: 전력·냉각이 진짜 한계다.
- **OpenAI**: AI는 위임 가능한 노동력이다. / **Anthropic**: 에이전트는 며칠간 자율 작동한다. / **Google**: 프로덕션의 간극을 우리가 메운다.
- **Palantir**: 온톨로지가 인간과 AI의 다리다. / **ServiceNow**: 컨텍스트 그래프를 쥔 자가 지배한다. / **Oracle**: 맥락 없으면 강화된 챗봇일 뿐이다.
- **SAP**: 라이선스 만료가 도입을 강제한다. / **Upstage**: 도메인특화가 정확도를 만든다. / **삼성SDS**: AX는 E2E 프로세스 재설계다(토큰=ROI).
- **Accenture**: 기술비용을 재배분하라. / **McKinsey**: 도입과 수익화 사이에 골이 있다. / **Kore.ai**: 15% 못 넘으면 손익에 안 잡힌다.
- **Tesla·현대차**: 우리는 자동차 회사가 아니다. / **Zoox**: vibe driving은 안전에 부적합하다. / **Boston Dynamics**: 안 넘어지는 영상만 보여주지 마라.
- **Orange/Telefónica**: 주권은 흑백이 아니라 계층 선택이다. / **Scale AI(CA)**: 새 ERP 기다리지 말고 가진 데이터로 지금 측정하라. / **채드 존스**: 가속은 진짜지만 75년 걸린다.

---

## 5. ⚠️ 데이터 신뢰 경계
- 위 기능·수치는 **자사 발화 기준**. 워싱 위험(§CONTENT_REVIEW §5)과 함께 볼 것.
- 자막 오류로 제품·수치가 훼손된 경우 다수(§CONTENT_REVIEW §7). 인용 전 원 영상 교차검증.
- 채널명≠담론성격(Cohere=학술, Huawei=주권 탈색 등). 회사 성격을 채널명으로 예단 금지.
