# 수집 콘텐츠 검토 보고서 (v6.1, 2026-07-26)

> **3,865건 전체 코퍼스** 기준 분석. 심층 정독 ~1,000건(키워드 120여 + 채널 대부분), 대규모 백필 잔여분은 인벤토리 상태.
> 자동분류: **AX 1,030 / DX 72 / AT 7 / 미분류 2,756** (채널 190개, 한국어 다수). 연도: 2020~22 얇음(36/69/44) → 2023:152 / 2024:289 / 2025:633 / 2026:2,642(68%).
> 다음 회귀분석·코딩 작업 전에 읽을 것. **누적 신규·심층 채널**: OpenAI·AMD·Orange·Scale AI·Huawei·Oracle·Vertiv·Telefónica·Google Cloud Tech·Zapier·AWS Developers·Hugging Face 등.
> **v6 증분(1,603→3,865, +2,262)**: 대규모 백필 + 신규 채널 **Huawei·Oracle·Vertiv·Telefónica·Figure·DuckDuckGo** + 한국어 AX 키워드 37편.
> **⚠️ v6.1 정정(중요)**: v6가 "회의론/역풍 클러스터"를 새 **횡단면 구조**로 제시했으나, 마커 검증 결과 **과잉주장으로 강등**. 순수 환멸 마커는 벤더/기업 채널에서 2023 이후 ~2.6%로 **평평**하고, 회의론은 대부분 **최근 한국어 키워드(비평 장르, 전량 2026-07 수집)**에 몰려 **"시점"과 "장르"가 교락**됨 → 시계열 트렌드인지 수집 아티팩트인지 **분리 불가**. §0-C 참조.
> **여전히 유효한 지도 확장**: (a) **state 축이 지정학 블록으로 분화**, (b) **분모스왑에 "15% P&L 임계"**, (c) **한국 노동마찰의 비균질성**, (d) **전력 비용축 정량 앵커**(Vertiv). 아래 §0·§4 참조.

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
| **연구** | Hugging Face(Sara Hooker) | 모델 크기(scaling law) | 적응 비용(adaptation) | 신생 랩 포지셔닝 |
| **평가** | AWS·Zapier·Google | 데모 성공 | 자사 벤치마크·eval 통과율 | "어느 에이전트가 좋은가"의 정의권 |
| 비즈니스(v5) | AMD | 토큰/watt(NVIDIA) | **agents per watt·dollar·rack + "concurrency(동시성)"** | CPU(EPYC)를 GPU 서사에 재삽입 |
| 신뢰(v5) | Orange | ROI | **4C→5C**(Control·Choice·Competence·Critical scale + **Comprehension/설명가능성**) | 텔코 주권·신뢰 상품화 |

→ **지표를 쥔 자가 ROI 서사를 쥔다.** 이것이 의사결정의 알고리즘화의 메타층위: 기업 안에서 AI가 결정하기 이전에, 'AI 가치를 어떻게 계산할지'라는 판단 기준 자체가 이해당사자에 의해 재작성된다. v4에서 이 명제가 **연구층·평가층까지 관통**함이 확인됐고, v5에서 분모 전투가 벤더별로 **증식**(AMD concurrency, Orange 5C)했다. 🔑 **v6 계량 눈금**: Kore.ai/BCG(Nick Clarke)가 분모스왑에 손익 컷오프를 제시 — **"생산성 향상 <15%면 P&L에 반영 불가"**(성숙조직 15~18%·하위 7~12%·규모 실현 25%). 지표 재정의가 '실제 손익으로 인정되는가'의 임계선을 획득. 또한 삼성SDS는 ROI 측정 단위를 **토큰 미터링**으로 삼아 거버넌스·KPI·비용을 하나로 재봉합(운영 계층의 분모 확정).

🔑 **분모스왑 실시간 포착**(Google Cloud Tech "How to speed up 80%"편) = 이 인사이트의 가장 선명한 단일 실연. 1시간 내 UI 버그 수정이라는 원래 목표는 **실패**(타이머 0)했으나, 발표자는 즉시 "사실 우리가 이겼다 — 계측→80% 단축→Cloud Run 배포, 축구로 치면 3:1 승리"로 성공 지표를 재정의한다. 목표 미달을 카메라 앞에서 실시간으로 승리 서사로 갈아끼우는 장면.

🔑 **NEW: 분모스왑 "반박" 진영 등장**(v5) — **Scale AI(캐나다 정부 클러스터)**는 정반대를 민다: "새 ERP·인프라를 기다리지 말고 **가진 데이터로 지금 기존 지표(시간·오류·처리량·가동률)로 측정하라**". 분모를 바꾸지 말라는 counter-move. 분모스왑이 이제 **스왑 진영 vs 반스왑(즉시측정) 진영**의 대립 구도를 형성 → K1에서 "지표 재정의 vs 기존지표 고수"를 벤더 유형별로 코딩 가능.

### B. 그 외 반복 구조
1. **"95% 실패" 개막 의식 — 이제 도메인 이식성 확인**(v5) — MIT "95% 실패", 맥킨지 "88% 도입 vs 39% 수익화", Google Emergent "코딩앱 95% 상용화 실패", **중소기업 "90% 실패"(한국 AX강의)·Scale AI "내가 읽은 AI 특허의 96%는 무효"·Orange "magic wand(마법 지팡이) 환상"** — 같은 문법이 컨설팅→코딩→중소기업→특허→텔코로 **도메인을 갈아타며 반복**. 문법: [파국적 실패율 인용]→["기술이 아니라 사람·프로세스·데이터 탓"]→[내 프레임만 예외]. = **책임 전가 알고리즘**(범용성 재확인).
2. **"AI는 기술 문제가 아니라 사람 문제" — 그러나 반증 축 등장**(v5) — 범용 명제로 확정돼 왔으나(Upstage·Palantir·BCG·McKinsey·Zapier Amit·Google Home Depot·Sandvik·중소기업강의 "성공의 80%는 사람"), 🔑 **무신사 CTO는 반대를 진술**: "결핍이 혁신" — **인력이 부족한 팀이 오히려 AX를 더 빨리 채택**한다(리소스가 있으면 안 씀). "사람 문제" 명제를 confirm이 아니라 **challenge**하는 첫 소스. K1에서 인력밀도×AX채택속도의 부(-)의 상관 가설로 전환 가능.
3. **공급/수요 담론의 분열 + "화자 대리(proxy)" 세탁**(v4.1) — 공급측("OpenClaw 모멘트, 추론 15배 폭발", Hugging Face 모델·데이터 제조)과 수요측("95%가 성과 없음", Qdrant/AX강의 도입·비용·규정)이 양립 불가. 이 간극이 버블 질문의 실체이자 검증가능한 특이점. 🔑 **혼합 변종**: Infosys의 on-topic 자료는 컨설팅사가 *직접* 말하지 않고 고객사 임원(Sandvik 디지털책임자·Swedbank CIO)을 화자로 세워 **공급측 담론을 수요측 증언으로 세탁**한다. "누가 말하는가"를 K1 태깅 시 벤더 자신 vs 대리 고객으로 구분 필요(OpenAI 레퍼런스 고객 포맷과 동형).
4. **온톨로지/컨텍스트 계층 = 격전지, 이제 "문서 하네스"까지 확장** — Palantir(온톨로지)·ServiceNow(context graph)·Databricks(Unity Catalog)·Pinecone/Weaviate/Qdrant(벡터)·**LlamaIndex("기업가치 90%가 비정형 문서에 묻힘"→PDF 파싱 관문화)·Vultr("데이터 중력·주권"→벡터DB 위치 관문화)·Google(OTel·App Hub)** 모두 "데이터+거버넌스 계층을 쥔 자가 에이전트 시대 지배"라 주장. AX의 진짜 락인은 모델이 아니라 컨텍스트/거버넌스 계층.
5. **정량성의 역설** — AI를 전면에 내세운 채널일수록 검증가능 정량 성과가 부재. 가장 단단한 숫자는 AX가 아니라 인접 상품(칩·영상장비)을 파는 채널, 또는 자사 실무를 공개하는 소규모 채널(AX 강의)에서 나옴.
6. **배수(multiple) 수사학** — 컨설턴트·벤더는 분모 없는 배수("4.4배", "16.5배", "10배 은행", "6배 전환")로 말함. 반증 불가하면서 인상적.
7. **"에이전트=인력(AI Workforce)" 프레임의 국제적 수렴** — Alibaba("디지털 실리콘 전문가팀"), SK AX("AI workforce"), TCS, ServiceNow("L1 대체"), **OpenAI("팀→상담원 하나"·"위임 가능한 노동력"), Google(PayPal "에이전트=재입사한 인턴"), Zapier(Lovable "BDR 조직 대신 AI 에이전트"), AX강의("AI 직원 고용")**. 노동을 '인력 단위'로 세는 담론이 미·중·한 공통.
8. **자동차 산업 AI 태도 4분화**(v4 확장) — 침묵(Nissan·Volvo) → **서사적 침묵(Mercedes: AI를 "에어밸런스"처럼 이름조차 안 붙이고, 그 공백을 140주년 헤리티지·자선·소재지속가능성으로 능동적으로 메움)** → 완곡 내재화(BMW: ADAS를 "AI"로 안 팜) → 정체성화(Tesla: AI/에너지/로봇 기업으로 자기재정의). "AI를 말하지 않는 방식"에도 전략적 스펙트럼 존재.
9. **소버린 AI의 하이브리드 실용주의** — NAVER·LG: 자국 모델(HyperCLOVA/EXAONE)+데이터주권(뉴로클라우드)을 내세우면서도 미국 Claude를 제어 UI로 병용. "소버린 vs 종속" 이분법이 아니라 계층별 선택.
10. **NEW: "신뢰성·평가(eval)가 새 전장"** — AWS(Steering/Evaluating Agents/Swarm 안전), Zapier(Automation Bench), Google(Arize/OTel). 에이전트 신뢰성이 미검증인 상태에서 "평가·벤치마크를 정의하는 자"가 "어느 에이전트가 좋은가"를 규정 → 온톨로지 land-grab의 **성능 판정 버전**. 분모스왑 평가층(§0-A)과 짝.
11. **축: "사람 소거 vs 사람 전면화"** — 동일한 알고리즘화 하부구조를 두고 **AWS**는 토큰·컨텍스트·평가라는 순수 원가/신뢰성 엔지니어링 언어로 번역(사람 부재), **Zapier/Google/AX강의**는 헤드카운트·판단·deskilling을 전면화. 같은 기질(substrate), 반대 표면언어. 벤더의 청중(개발자 vs 경영진)이 담론 표면을 결정 → 분석 시 "청중 통제" 필요.
12. **NEW: "국가/정책(state) 담론 = 공급·수요 외 제3축"**(v5) — 지금까지 담론 주체는 공급측(벤더)과 수요측(고객 기업)뿐이었으나, v5에서 **정부/클러스터/국가전략**이 독립 주체로 등장: **Scale AI(캐나다 연방 Global Innovation Cluster — "Build/Buy/Believe in Canada", 지분 없는 촉매자)·소버린AI Korea(SKT A.X, SK 15GW)·Vietnam(통신 3사 국가분업: Viettel 풀스택/VNPT B2G/MobiFone 소비자)·Orange(텔코 주권 Alliance 12사)**. 벤더 셀링도 고객 도입도 아닌 **국가 자본배분·주권·무역수지** 프레임 → K1에서 "담론 주체=벤더/고객/국가"의 3분 코딩 필요.
13. **소버린 AI 실용주의의 확장**(v5) — v3의 NAVER/LG 하이브리드가 **텔코(Orange: 데이터+harness만 쥐고 나머지는 오픈소스·Mistral 병용)**와 **국가(Vietnam·Canada)**로 확장.
14. **NEW: state 축이 지정학 블록으로 분화**(v6) — 국가/주권 담론이 단일이 아니라 **블록 대 블록**으로 갈림: 🔑 **중국(Huawei)=주권 "탈색"**(China-state를 지우고 "글로벌 파트너"·신뢰·공급망·비용을 전면화 — 국가판 자동차 침묵) / **서방·NATO(Oracle)=동맹 주권**("정치보다 깊은 가치체계·회복력·자율성") / **EU(Orange·Telefónica)=유럽 기술주권** / **한국(NAVER·SKT·삼성SDS)=하이브리드**. → K1 태깅 시 state 발화를 블록별로 코딩.

### C. (v6, ⚠️v6.1 강등) 회의론/역풍 담론 — 존재하나 "구조/시계열" 판정 보류
v6 초안은 이를 "새 횡단면 구조(부머 vs 회의론자 결정화)"로 적었으나, **마커 기반 검증 결과 그 지위는 과잉주장으로 판명**됐다(아래 검증). 회의론 콘텐츠 자체는 실재하나, **시계열 트렌드인지 장르/수집 아티팩트인지 현 데이터로 분리 불가**하다.

**검증(마커 기반, 거친 프록시):**
| 소스 | 넓은 마커(실패·취소·낭비 포함) | 순수 환멸(버블·철회·재고용·과대광고) |
|---|---|---|
| channel 2020→2026 | 5.6% → 20.1% (상승) | 0.0% → **2.6% (2023 이후 평평)** |
| keyword 2026-07 | 42.3% | **16.3%** |

→ **판정**: (1) 채널의 "넓은 마커" 상승(6→20%)은 거의 전부 **"95% 실패 의례" 언어**(실패·취소)이며, 이는 **부머가 오프닝으로 쓰는 도구**라 회의론이 아니다. (2) "순수 환멸"만 보면 벤더/기업 채널은 **2023년 이후 ~2.6%로 평평** → "시간이 지나 환멸기로 전환"이라는 깔끔한 시계열은 **채널에서 확인 안 됨**. (3) 아래 회의론 사례들은 대부분 **최근 한국어 키워드 영상(16.3%)**에 몰려 있는데, 키워드 수집분은 **비평·논평 장르**(원래 비판적)이자 **전량 2026-07 수집** → **"시점"과 "장르"가 완전 교락**되어 분리 불가. **결론: 회의론은 "장르+수집시점에 교락된 신호"이지, 검증된 시계열 트렌드도 깨끗한 횡단면 구조도 아니다.**

**개별 회의론 사례(신뢰도 가중 필수 — 존재 자체는 유효)**:
| 회의 유형 | 핵심 주장 | 출처 | 신뢰도 |
|---|---|---|---|
| **weakest-link 성장론** | SW 100% 자동화=GDP +0.5%, 소득 2배엔 94% 자동화 필요, 가속은 진짜지만 **75년 시차** | 채드 존스(월가아재) | 고(학술) |
| **워싱 폭로** | Builder.ai "AI"가 실은 인도 개발자 700명 | Kore.ai/BCG | 고 |
| **인지적 빚(deskilling)** | AI 의존이 "cognitive debt" 누적, MS 프론티어팀 의도적 AI 미사용 | 99%주식/MS | 중 |
| **unit-economics 반론** | 에이전트 API 비용>인건비, MS 클로드코드 철회·Tesla $200/주 제한 등 | 피셔인베스트 | ⚠️저(투자선동·광고물) |

→ **연구 함의(수정)**: 회의론 톤을 버블 대리지표로 태깅하려면 **반드시 (source 장르 × 수집 코호트)를 고정**한 뒤에만 시점 비교가 유효하다. 원시 회의론 빈도의 연도별 상승은 **95% 의례 + 장르 구성 변화 아티팩트**일 수 있으므로 그대로 쓰면 안 된다.

---

## 1. 코퍼스 지도 — AI/AX 담론 밀도 순

| 밀도 | 채널 | 성격 |
|---|---|---|
| ★★★ | NVIDIA·NVIDIA Developer, **AMD**, Arm, Siemens, Nokia, Wayve, Zoox, Tesla | "AI 팩토리"·"물리적 AI"·에이전트·자율주행·칩. 수치·비용구조 언어 풍부. AMD는 NVIDIA에 "open vs lock-in"·concurrency 분모로 대항 |
| ★★★ | LG AI Research, Upstage, Palantir, ServiceNow, SAP, IBM, Salesforce, Databricks, Alibaba Cloud, **Google Cloud Tech**, **AWS Developers**, W&B·Qdrant·Pinecone·Weaviate·Snowflake | AI가 곧 제품. 도입방법론·평가·거버넌스·온톨로지·에이전트 하네스 |
| ★★★ | **OpenAI** | 위임(delegation)·에이전트·레퍼런스 고객(BNY·Shopify·Virgin) 포맷 |
| ★★☆ | Meta(Boz), Boston Dynamics, Microsoft Azure, Google Developers·DeepMind, Meta Developers, SK하이닉스, GE HealthCare, Accenture, TCS, **Zapier**, ElevenLabs, Runway, Apple Developer, GitHub, Replit, NAVER Cloud, Unilever(IR), **Stability AI** | AX를 자사 제품/비전·투자자 서사·GTM에 접합 |
| ★★☆ | **Hugging Face** | ⚠️ 예외 — 엔터프라이즈 비용 담론이 아니라 **연구/OSS 공급측**(모델·데이터·로보틱스 제조). "채널명≠담론성격"의 최신 사례 |
| ★★★ | **Oracle**, **Huawei** | v6 신규 — 엔터프라이즈 data-layer land-grab + **state 축 지정학 블록**(Oracle=서방 동맹주권·최정교 anti-washing "데이터≠결정"; Huawei=중국 탈주권·신뢰담론) |
| ★★☆ | **Orange·Telefónica(텔코 주권)**, **Scale AI(캐나다 정부 클러스터)**, **Vertiv(데이터센터 전력)** | 텔코 주권 실용주의(4C→5C, EU 기술주권) / 국가·정책 담론(state) / **전력 비용축 정량 앵커** |
| ★☆☆ | SK텔레콤, Telenor, Amazon, Waymo, Mayo Clinic, LinkedIn, Schneider, Microsoft(PR), **Infosys(고객증언만)**, **IQVIA(제약 data-layer 약함)**, **DuckDuckGo(⚠️off-axis: "useful/private/optional AI" 소비자 반슬롭 anti-washing 극점)** | AI가 마케팅 소재 / 소비자 절제 담론 |
| ☆ | Swisscom, Reckitt, Nissan, Volvo, BMW, **Mercedes-Benz**, NTT DATA, Suno, Luma, Philips, Perplexity, Cohere(학술), Anthropic(모델PR), IKEA, L'Oréal, Chegg, SoftBank, **Nike**, **Figure(휴머노이드지만 자막 공동화)**, kakao_tech(2021) | AI 담론 희박 — 그 자체가 신호. **노이즈 확정(AI 멘션 0/자막 부재)**: L'Oréal·Chegg·SoftBank·Nike·Figure = 순수 대조군 |

키워드 수집분(120여 건, `transcripts/2026-*/`)은 한국어 AX 강의·컨설팅·정책·언론이 주력이며 연구 주제에 최고 밀도. 최고가치: "데이브의 개발 생활"(의사결정 알고리즘화 실연)·**오픈AI×무신사**(한국 노동마찰 진술)·**삼성SDS 신계영 AX센터**(AX-office 제도화 최강 실증)·**월가아재 채드 존스**(회의론 학술 앵커).

⚠️ **"채널명 ≠ 담론 성격"**: Cohere·Hugging Face(학술/OSS)·Microsoft·Anthropic(브랜드/모델PR)·BMW/Mercedes/IKEA/L'Oréal(광고·리테일·제조)·**Chegg(edtech이 ChatGPT에 파괴됐음에도 채널은 순수 생물학 학습영상 — 최고의 아이러니 대조군)**·**Scale AI(미국 데이터라벨링사 아니라 캐나다 정부 클러스터)**·Zoox/TCS(오수집) — 채널명으로 성격·소속·국적을 예단하면 안 됨. 🔑 **명제가 "채널 내부" 수준으로 확장**(v4.1) — Infosys 한 채널이 순수 AX담론(Sandvik·Swedbank 고객증언)과 순수 채용PR노이즈("Power Programmer" 시리즈)로 갈린다. 채널 필터가 아니라 **영상 단위 라벨링** 필수.

---

## 2. 주요 발화자·패널

**한국 AX 담론**: 김건우(『AI 전환 절대공식』 저자)·김유신 상무(티타임즈)·신계영 부사장(삼성SDS AX센터)·장진석(BCG)·윤병동(서울대·원프레딕트)·이세돌×이홍락(LG AI)·Galina Fendvich(Upstage US)·이상욱 교수(한양대 철학, 탈숙련)·서연석(NAVER Cloud)·"데이브"(AX 실무강의). **v5**: **전준일(무신사 CTO, ex-구글/요기요 — 한국형 노동 마찰 유일 직접 진술)**·김덕진(IT융합연구소장 — MCP 정책 자동화)·전인구(소버린AI)

**글로벌**: 젠슨 황·Kevin Deierling(NVIDIA), Will Abbey(Arm), Rainer Brehm·Rev Lebaredian(Siemens/NVIDIA), Alex Kendall(Wayve), Akshay(Palantir 수석아키텍트), Michael Park(ServiceNow), 일론 머스크(Tesla TERAFAB), 페르난도 페르난데스(Unilever CEO), Amjad Masad(Replit CEO), Rana El Kaliouby(MS/Affectiva), 페이(Alibaba DB BU), Boz+게스트 Shyam Sankar(Palantir CTO)·Ed Catmull·Dylan Field, Aaron Levie(Box), Peter Arduini(GE)

**v4 신규**: **Sara Hooker**(Adaption Labs 공동창립·前 Cohere For AI — "스케일링의 느린 죽음→적응"), **Eric Ries**(Lean Startup — 코퍼스 최강 메타비판자), **Amit Bendov**(Gong CEO), **Ryan Meadows**(Lovable CRO), **Guy Yalif**(Webflow CPO), **Wade Foster**(Zapier CEO), **로빈 빈스(BNY CEO, 사내 플랫폼 "Eliza")**, Shopify·Virgin Atlantic·Peter Steinberger(OpenAI France), Home Depot(Ashish·Chuma)·MediaMarkt·PayPal(Mir)·BBVA(Gerardo Monzelli)·Anthropic Lydia(Google 플랫폼 출연). **v4.1**: Sofia Sirvell(Sandvik 디지털책임자 — "사람 문제" 트로프), Lotta Lovén(Swedbank CIO). **v5**: Bruno Zerbib(Orange CTIO)·Jérôme Berger(Orange 전략·4C)·Gautier Cloix(H Company CEO)·Mark Voscher(Scale AI 투자디렉터)·Todd Bailey(Scale AI IP VP — "AI 특허 96% 무효")

**v6 신규**: **황재선(SK 디스커버리 CDO — "AX 100배"·한국 노동마찰)**·**Nellie Wartoft(Tigerhall CEO — AX-office/FTE avoidance)**·**Nick Clarke(BCG — "15% P&L 임계")**·**Aaron Levie×Martin Casado×Steven Sinofsky(a16z — agent=인간 신입·"95% 실패=멍청한 통계" 반박)**·**채드 존스(스탠퍼드, 월가아재 인용 — weakest-link 75년시차)**·**노정석(EP105 — 평가전장=학술 peer-review 붕괴)**·Chris Skinner·Rand Waldron(Oracle Sovereign Cloud)·Paul Jenkinson(Oracle Whitespace — "decision superiority")·정의선(현대차)·류재철(LG전자)

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
2. **전력/인프라 — v6 정량 앵커 확보** — Nokia("cost per delivered bit", "no GPU premium"), Siemens("물리산업 100조$"), Schneider("AI=전력수요 유발자"), LG("AI 비용의 본질=에너지"), Arm("power is not free"), Tesla TERAFAB(1테라와트), Google(Ironwood TPU 포드당 9216칩), **🔑 Vertiv(랙 140kW→200/240→600kW→1MW, 350~400kW에서 구리·버스바 물리한계, GPU 72→576개/랙, 800V DC(±400V) 전환, KPI="tokens per watt per second", 250MW 원샷 배포)** — 전력 담론이 랙밀도·전압·와트당토큰의 **하드넘버**로 구체화. AMD·Vertiv의 "수직통합 vs 멀티벤더"는 인프라판 open-vs-lock-in
3. **인건비 대체** — ElevenLabs(4인 ROAS 7.16), Databricks("400명 팀 필요"), Upstage("인건비 80%↓"), Palantir(증강 vs 대체), Alibaba("에이전트=인력"), **OpenAI(Shopify "팀→상담원 하나")**, **AX강의(7명→4명·VOC 직접처리 95%↓·주 16시간 확보)**
4. **토큰/크레딧 원가 거버넌스** — GitHub(Kimi K2.7 과금표: 100만 토큰당 95크레딧 입력/400 출력, 캐시히트 95%, Copilot "비용 센터"·월 $50 한도), **AWS(context_manager=auto로 "토큰 55%↓·정확도 68→98%"; 요약엔 저렴한 모델)**, **Zapier(월 10만 회 실행 토큰비용 모델링, 모델 간 4배 원가차)** — AX가 실제 기업 예산·FinOps로 번역되는 지점
5. **도입 실패·변경관리 비용** — Google/Microsoft("망가진 워크플로에 AI 얹으면 실패", "마지막 30%가 어렵다"), Zapier(Lovable "소프트웨어보다 변경관리·배포가 핵심"), AX강의("전직원 ChatGPT 결제+외부강사 3개월 뒤 변화 0 = 정상적 실패, 돈만 더 씀"). AX의 숨은 원가 = 도구비가 아니라 조직 재설계·변경관리
6. **🔑 한국형 노동 마찰(정규직 경직성) — v6에서 비균질성 확인** — **무신사 CTO 전준일·황재선(SK)**: AX가 고과를 AI 정렬로 바꾸면 도태자가 생기나 한국 정규직 경직성 때문에 **해고가 아니라 "한직 재배치·유휴인력·직무전환"으로 굴절**(vs 미국 MS 6천명·IBM 유연해고). 인건비가 장부에 남은 채 **생산성 손실로 이연**. 🔑 **단 반례**: 삼성SDS는 "특정 부서 사람 아예 빼보자"를 **KPI 측정 도구로 명시** — 한국도 균일하지 않음. + "**FTE avoidance ≠ layoff**"(Tigerhall·Levie: '해고'가 아니라 '채용 회피'라는 완충 수사). → K1 조절변수를 "국가"가 아니라 "기업/리더별 스펙트럼"으로.
7. **국가 자본배분/무역수지**(v5, state 축) — Scale AI(캐나다: 190프로젝트 기대효과 $70억), 소버린AI Korea("돈이 국내 순환"·SK 15GW), Vietnam(2030 GDP +$790억). AX 비용이 기업 P&L을 넘어 **국가 자본흐름·주권**으로 확장.
8. **🔑 NEW: AX 전담조직(Transformation Office) 신설 비용**(v6) — 담론이 조직 형태로 제도화: **삼성SDS AX센터·CAIO·AI크루 107명, SK AI팀+AI챔피언, 모더나 AI챔피언 100명·GPTs 750개, Tigerhall data flywheel**. → K1에서 "AX 전담조직/CAIO 신설" 이벤트를 자본지출·인건비 재편의 **선행지표**로 활용 가능.

**AX를 직접 P&L/원가로 환산하는 최고 자료**(K1 종속변수 후보): **Unilever 투자자 3편**(CEO가 R&D 혁신주기 2~3년→9~12개월·마진구조 직결), **무신사(SaaS 내재화 4.5억원 절감·2개월·개발자 3명 + 한국형 노동 마찰 진술)**, Upstage 플리토("인식률 10%=검수 시간=비용"), GitHub(크레딧=센트), AX강의(노하우 장표를 인건비 200만원+로 환산), Nokia("cost per delivered bit")

---

## 5. 반-워싱 vs 워싱 진영 (뚜렷한 분화)

**반-워싱(실체/절제)**: TCS·Google Samat("AI라는 단어 안 썼다")·LinkedIn·Nasdaq("MIT 5%만 프로덕션")·Swisscom·Siemens·Upstage·IBM·Boston Dynamics·Zoox("vibe driving은 안전 시스템에 부적합")·GitHub·McKinsey·**Google Cloud Tech("코드생성만 과의존=버그·기술부채↑")·AWS("합격률 66%뿐")·FineWeb(자사 실패 공개)·LlamaIndex·**v5**: **Orange("과대광고 아닌 진짜 AI, magic wand 사는 게 아니라 인간중심 도구상자")·Scale AI(프로젝트별 달러영향 측정·"파일럿 말고 제한범위 실사용"·"AI 특허 96% 무효" 폭로)·AMD("AI and Trust at Scale"·OSU "AI 글 불신→구술시험 전환")**

v6 추가 반-워싱: **Oracle(코퍼스 최정교 — "맥락 없으면 강화된 ChatGPT일 뿐", signal→context→action, "misaligned 시스템+AI=신뢰 못할 산출물")·Vertiv(사전검증·복잡성↓)·a16z Levie("95% 실패=멍청한 통계"·토큰카운팅=가짜 생산성)·더리치(감속기 미보유 리스크 명시 고지)·Kore.ai(Builder.ai "AI가 실은 인도 700명" 폭로).

**🔑 메타-비판·회의론(담론 알고리즘 자체를 해부 — §0-C 클러스터와 연결)**: **Eric Ries(Zapier)** — "슬롭 팩토리·LLM 정신병·deskilling·Dunning-Kruger 공장". **이상욱 교수** — 탈숙련. **v6: 채드 존스**(weakest-link 75년시차)·**노정석**(peer-review·RLVR 붕괴, AI리뷰 적발)·**unit-economics 반론**(에이전트 비용>인건비). 검증자의 법칙(Nasdaq·Boston Dynamics 계열)이 v6에서 **조직적 회의론 진영**으로 결정화.

**워싱(배수·신조어·무자막·비전)**: Accenture("10배 은행")·SK AX(사례 제로)·Databricks("세계 최초 에이전틱 CDP")·ServiceNow(규모 과시)·Runway(유명인 권위)·Nissan/Volvo/BMW/**Mercedes(서사적 침묵)**·Tesla TERAFAB(카르다셰프·우주 AI)·AppsTek·SAP "Autonomous Enterprise"·OpenAI 간증 4편("권위 있는 실명+수치 부재"의 전형)·AX강의(안티워싱 톤→유료 소모임 전환)·**v5: IQVIA("AI 기반·확장가능·규정준수" 벤더 셀링 문구 위주, 안티워싱 장치 약함)·시니어 AX가이드(무비판 낙관 홍보)·소버린AI/Vietnam(투자유치·정책 워싱 성격)**

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
| **무신사(코덱스 도입)** | SaaS 내재화 **4.5억원 절감**·2개월·개발자 3명, 코덱스 주간사용 300만→400만(2주) | 오픈AI×무신사(CTO 전준일) |
| **실리콘밸리 코드** | 2026말 **80%**, 2027말 **100%** AI 작성(전망) | 〃 |
| **앤트로픽 LLM지출 점유** | **12%(2023)→40%(2025)**, 오픈AI 27% | 오그랲/비디오머그 |
| **AMD Helios** | MI455X 72개, FP4 **2.9 exaFLOPS**, HBM4 31TB; AT&T 256GPU **94.2% 효율** | AMD |
| **Scale AI(캐나다)** | 2018~ 200+프로젝트 누적 **$750M**(배율 4.7x), 190프로젝트 기대효과 **$70억**, 자금 ⅔ SME | Mark Voscher |
| **AI 특허 무효율** | 읽은 AI 특허의 **96%가 무효** | Scale AI(Todd Bailey) |
| **임상개발 기간** | **116개월(2004)→52개월(2019)**, 다지역임상 30%→65% | IQVIA Japan |
| **Orange Money** | 월 활성 5천만·연 이체 **200억€**, 세네갈=GDP **11%** | Orange(fintech 포용) |
| **베트남 국가 AX** | 2030 GDP **+$790억**(12%), AI인재 7000(태국 3만) | Vietnam AX |
| **denominator 임계** | 생산성 향상 **<15%면 P&L 반영 불가**(성숙 15~18%·하위 7~12%) | Kore.ai/BCG(Nick Clarke) |
| **weakest-link** | SW 100% 자동화=GDP **+0.5%**, 소득 2배엔 **94% 자동화** 필요, 가속 진짜지만 **75년 시차** | 채드 존스(월가아재) |
| **Tigerhall** | 도입률 90일 **91%**, 변화활성화 19~32주→**3~5일**·27 FTE주→**1시간**·팀 5→3명 | Nellie Wartoft |
| **모더나** | 직원 **80%** 사용·40%가 GPTs 제작·총 **750개**, AI챔피언 **100명** | Matt Song |
| **MIT 역삼각형** | 도입 **88%→**성과 인지 **60→20→5%** | Matt Song |
| **Vertiv 랙밀도** | 랙 **140kW→1MW+**, 350~400kW 구리 물리한계, GPU 72→576개/랙, 800V DC | Vertiv |
| **삼성전자 에이전트** | 천~만 단위 가동, VOC **주 30만건** | 삼성SDS 신계영 |
| **Builder.ai** | "AI"가 실은 인도 개발자 **700명**(붕괴) | Kore.ai |
| Klarna | AI 퍼스트 → 실패 후 재고용 | 김건우 |

---

## 7. 🔴 데이터 품질 이슈 및 조치 내역

1. **채널 오수집 2건 발견·수정 완료(2026-07-21)** — 동명이인 채널 리스크:
   - **TCS**: `@TCS`(스위스 자동차클럽 Touring Club Schweiz) → `@TCSGlobal`(진짜 Tata Consultancy) 교정. 오수집분 7건 `Touring_Club_Schweiz/`로 격리.
   - **Zoox**: `@zoox`(동명 게임 유튜버) → `@ZooxYouTube`(아마존 로보택시) 교정. 오수집분 2건 격리. **→ 수정 후 진짜 Zoox 로보택시 콘텐츠 정상 수집 확인됨.**
   - → **약어·짧은 이름 채널 재검증 필요**(config.py "추정" 표시 핸들 전반).
2. **노이즈 채널** — Swisscom·Nissan/Volvo/BMW/Mercedes(AI 침묵/광고)·NTT DATA(채용)·LinkedIn·Cohere(학술)·Hugging Face(연구/OSS)·Microsoft(PR)·Suno/Luma/Philips·**v6: L'Oréal·Chegg·SoftBank·Nike·Figure(자막 공동화)**: AX 비용 분석에서 별도 분류 권장.
3. **자막 자동번역 오류 체계적 — v4에서 더 심각·구조적임 확인**. 특히 **의미 반전형 오역**:
   - `agents`→**"부동산 중개인"**(Google Architecture편 "향후 2~3년 부동산 중개인들이…"), `agents`→"요원/상담원", `mutating agents`→**"병원체·변이원"**(PayPal편)
   - `agentic harness`→**"억제력/능동적 억제력"**, `Antigravity`→"반중력 장치", `Claude/Claude Code`→**"오픈 클로(Open Claw)/클라우드 코드/인공 클라우드 모델"**, `Anthropic`→"Enthropic"
   - `cache`→**"현금/현금화"**, `staleness`→"스테인리스", `LLM`→**"법학 석사"**, `Gong`→"징", `Strands`→"가닥들", `LeRobot`→"레오봇/르루프"
   - 한국어 AX강의: `ChatGPT`→"채피 결제", `장면`→"장미안", `통으로`→"통어", `유휴인력`→"유효인력"
   - **v5 비영어 심화**: 프랑스어(Orange) 한국어 기계번역 반쯤 해독불능 — `Alliance`→"알리안자", `Gautier Cloix`→"구찌 코이스", `agentic AI`→"에이전트 QAI"; 일본어(SoftBank)·스페인어(L'Oréal) 채널은 자막 자체가 부실; `Scale AI`→"Skidi/Skaii", `AtCoder`→"에코더", `sovereignty`→"간결한 주권"
   - **🔴 v6 "음악" 치환이 체계적 리스크로 확정**: 도메인 명사(finance/telecom/electronic/AI/자산)가 **"음악"으로 대규모 치환** — Huawei("음악 은행"), Telefónica("음악 부문 자산 매각"·재무수치 신뢰도 저하), Vertiv("250MW 음악 프로젝트"), 삼성SDS. 중국어/스페인어/한국어 auto-caption 전반. + `딥시크`→"집시크", `환각`→"환강", `Vertiv`→"Verdiff", `Frozen v2`→"프로젠".
   - **결론: 영어 원본 자막은 신뢰도 높으나, 비영어(한·불·일·서·중)→한 자동번역 인용 시 원문 확인 필수. 특히 `agent`류 핵심어·고유명사·`음악` 치환된 도메인 명사가 완전히 뒤집힘. 수치 인용 전 원 영상 교차검증 필수.**
4. **빈/저품질 자막** — "[음악] 우." 뿐인 파일(BD 티저, LG 티저, **Figure 휴머노이드 7편 전량 2~12단어** 등). 단어 수 임계값(예: 50단어) 필터링 권장.
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
13. **🔑 오픈AI×무신사 코덱스 도입 사례**(v5) — 한국형 노동 마찰(유휴인력/한직)의 유일 직접 진술 + "결핍이 혁신" 반증 축 + 코덱스 vs 클로드 엔터프라이즈 가성비 현장 데이터
14. **Scale AI(캐나다) + 소버린AI Korea + Vietnam AX**(v5) — 국가/정책(state) 담론 축의 대표 텍스트(자본배분·주권·무역수지)
15. **Orange 4C/5C + Berger·Zerbib**(v5) — 텔코 주권 실용주의 + 신뢰 상품화 프레임
16. **🔑 회의론 클러스터 텍스트**(v6) — 채드 존스 weakest-link(75년 시차, 학술 앵커) + unit-economics 반론(에이전트 비용>인건비) + Builder.ai 폭로 = AX-boom 대항진영(§0-C)
17. **삼성SDS 신계영 AX센터 + SK 황재선**(v6) — AX-office 제도화(CAIO·AI크루) + 한국 노동마찰 진술 + "토큰=ROI 단위"
18. **Oracle(Gartner강연·Whitespace) + Huawei(Keyrus)**(v6) — "데이터≠결정"·decision superiority = 의사결정 알고리즘화 프레임 직결 + state 축 블록(서방·중국)
19. **Vertiv**(v6) — 전력 비용축 정량 앵커(랙밀도·전압·tokens/watt)

---

## 9. K1 병합으로 가는 측정변수 (operationalize)

1. **공급/수요 낙관 발산 지수** — 채널 유형 × 월 × AX 톤. 발산 폭 = AI 워싱/버블 대리지표.
2. **정량성 결핍 점수** — [AX 키워드 밀도] ÷ [provenance 있는 수치 등장 빈도].
3. **분모 교체 이벤트 탐지** — "토큰→에이전트", "usage→outcome", "job→skill", **"scaling→adaptation", "데모→벤치마크 통과율"** 재프레이밍 발화 태깅 → 산업×시점별 K1 자본지출/원가구조 변화와 이벤트 스터디.
4. **청중-표면 코드(사람 소거 vs 전면화)** — 동일 알고리즘화를 원가/신뢰성 언어로 번역하는가(사람 소거, 개발자 청중) vs 헤드카운트/deskilling으로 번역하는가(사람 전면화, 경영진 청중). 벤더의 청중 유형과 K1 인건비/자본 구조 변화 매칭.
5. **NEW: 담론 주체 3분 코드(vendor / customer / state)**(v5) — 발화 주체를 공급측 벤더·수요측 고객·국가/클러스터로 코딩. state 축(Scale AI·소버린·Vietnam·Orange)은 K1의 산업 자본지출을 넘어 **국가 자본흐름·주권** 변수와 매칭.
6. **NEW: 한국형 노동 마찰 지표**(v5) — AX 원가절감이 "headcount 감축"으로 실현되는가(미국식) vs "유휴인력·한직 재배치"로 이연되는가(한국식 정규직 경직성). K1 인건비 종속변수에서 **국가별 노동제도 조절변수**로 투입. 무신사 진술이 앵커.
7. **스왑 vs 반스왑 코드**(v5) — 지표를 재정의하는가(분모스왑) vs 기존 지표로 즉시 측정하라 주장하는가(Scale AI형 반스왑). + **v6 계량화**: "생산성 향상 <15%=P&L 미반영"(Kore.ai) 임계선을 담론이 인용하는지 태깅.
8. **회의론 톤 지수**(v6, ⚠️v6.1 조건부) — 회의론 발화를 버블 대리지표로 쓰되, **§0-C 검증에서 드러난 교락 때문에 (source 장르 × 수집 코호트)를 고정한 뒤에만 시점 비교 유효**. 원시 연도별 상승은 "95% 의례 언어 + 장르 구성 변화" 아티팩트일 수 있음(순수 환멸 마커는 채널에서 2023 이후 평평 ~2.6%). 출처 신뢰도 가중 필수(채드 존스=고, 투자선동=저).
9. **NEW: state 축 블록 코드**(v6) — state 발화를 중국(탈주권)·서방/NATO·EU·한국(하이브리드) 블록으로 세분 → K1의 국가 자본흐름·규제와 매칭.
10. **NEW: AX 전담조직 신설 이벤트**(v6) — CAIO·AX센터·AI챔피언 네트워크 신설을 자본지출/인건비 재편의 선행지표로.

⚠️ **신뢰도 경계**: 위 인사이트는 **횡단면 구조**에 근거해 유효하나, **시계열 주장(발산의 시간적 전개)은 백필이 고르게 찰 때까지 보류**. v6 표본은 채널 190개·3,865건으로 커져 **2023~2025 횡단면은 사용 가능**해졌으나(2023:152/2024:289/2025:633), 2026이 68%(2,642건)로 여전히 지배하고 2020~2022는 얇음(36/69/44). 월별 볼륨 시계열은 "채널 백필 순서" 아티팩트임에 유의(볼륨보다 share·횡단면이 신뢰 가능).
