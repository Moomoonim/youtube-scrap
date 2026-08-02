# LLM으로 에이전트를 구현하는 방법 — 키노트·GTC·컨퍼런스 발표 기술 상세 (2026-08-01)

> 코퍼스 7,967건 중 **키노트/컨퍼런스(GTC·re:Invent·Next·Sapphire·AIPCon 등) 508건 + 아키텍처/구현 강의 543건**에서 추출한 "어떻게 만드는가(how)"의 기술 지도. 약 90편의 실질 발표를 4개 트랙(NVIDIA/GTC, AWS+Google, 벡터DB·RAG·평가, 엔터프라이즈)으로 정독했다.
> `SOLUTIONS_MAP.md`가 "누가 무엇을 파는가"라면 이 문서는 **"발표에서 실제로 설명된 구현 아키텍처·기법·데모·수치"**다. 모든 내용은 발표자 발화 기준(자사 주장 포함)이며 출처(채널·발표·화자)를 병기한다.

---

## 0. 에이전트의 표준 해부학 — 업계가 수렴한 정의

발표들을 관통하는 공통 정의부터. 세부 어휘는 달라도 구조는 하나로 수렴한다:

**에이전트 = 모델(두뇌) + 하네스(몸: 도구·루프·메모리) + 운영(런타임·평가·거버넌스)**

- **NVIDIA "Agentic AI 101"(GTC)**: 에이전트를 "모델의 시스템(system of models)"으로 정의 — ①멀티모달 입력 ②단기→장기 기억 ③태스크별 모델 라우팅(음성이해·의도파악용 소형 오픈모델 + 프론티어 LLM 혼합으로 정확도·속도·비용 동시 최적화) ④에이전트 간 통신(하위 전문 에이전트 위임→종합) ⑤스킬/도구 ⑥컴퓨터 사용(UI/CLI/API) ⑦데이터 접근(정형=SQL, 비정형=RAG). "**데이터 언락이 에이전트 구축의 첫 단계**."
- **AWS(Strands 강좌)**: "모델이 두뇌, 하네스는 손·인프라·메모리." 도구 호출 순서를 하드코딩하지 않고 도구 설명+시스템 프롬프트로 **모델이 순서를 결정**하는 모델 주도(model-driven) 루프.
- **Anthropic("Building more effective AI agents")**: 진화 단계론 — 워크플로 → 에이전트 → **workflows of agents**(SQL 생성 같은 각 단계 자체가 자기교정 루프) → **멀티에이전트**(오케스트레이터가 서브에이전트에 병렬 위임, 서브에이전트는 메인 컨텍스트를 보호하는 "도구"로 노출). 원칙: "**무거운 스캐폴딩은 차기 모델의 지능을 가둔다** — 하네스는 갈수록 얇아진다."
- **SAP Joule Studio(Sapphire)**: "모델이 지능을, 스튜디오가 나머지(프로세스·아키텍처·도메인지식)를 제공" — 하네스 개념의 엔터프라이즈 번역.

---

## 1. 멀티에이전트 오케스트레이션 패턴 — 언제 무엇을 쓰는가

### AWS Strands의 3대 패턴 (Multi-Agent Patterns 시리즈)
| 패턴 | 구조 | 언제 쓰나 | 핵심 디테일 |
|---|---|---|---|
| **Agents-as-Tools** | 오케스트레이터가 하위 에이전트를 도구로 호출 | 작업이 독립적, 적응성 최우선 | 각 하위 에이전트가 **격리된 컨텍스트 창**을 가짐 → 웹검색 같은 "시끄러운 도구"의 노이즈를 메인 컨텍스트에서 차단(컨텍스트 엔지니어링 수단). `@tool` 데코레이터로 함수 래핑, 호출마다 새 인스턴스=깨끗한 컨텍스트 |
| **Graph Workflows** | GraphBuilder로 노드(에이전트)+엣지(의존성) 명시 | 실행 순서·의존성 보장 필요 시 | 4정형: 순차 파이프라인 / 병렬 팬아웃+집계 / 조건부 분기 / 피드백 루프(작성자↔검토자). 모델에 노출 않는 공유 데이터는 invocation state(공유 딕셔너리) |
| **Agent Swarms** | 에이전트들이 자율 핸드오프 | 구조를 미리 그릴 수 없을 때(예: 장애 분류 — 로그→메트릭→배포 검토로 경로가 발견됨) | **안전장치 필수**: max handoffs·max iterations·타임아웃·반복 핸드오프 감지 — 미설정 시 **토큰 무한 소각** |

### Google ADK: LLM 에이전트 vs 워크플로 에이전트
- 3분류: **LLM 에이전트**(추론·도구선택) / **워크플로 에이전트**(sequential·parallel·loop — 결정론적) / 커스텀. 판별 규칙: "**플로차트로 그릴 수 있으면 워크플로 에이전트를 써라**."
- 프로덕션 파이프라인 예(코드리뷰 에이전트): SequentialAgent(분석기→스타일검사기→테스트실행기→합성기) + LoopAgent(수정기→테스트→검증기, max_iterations=3, `escalate=True`로 탈출). **"결정론적 작업은 도구(AST 파싱·pycodestyle), 추론·오케스트레이션만 에이전트"**가 신뢰성의 초석. 워커는 Flash, 비판·합성은 Pro — 모델 차등 배치.

### 에이전트 간 상호운용: A2A + Agent Registry (Google)
- **A2A = "AI 에이전트를 위한 HTTP"**: 프레임워크(ADK·LangGraph·CrewAI) 무관 상호운용. **에이전트 카드**(`/agent_card.json`: 스킬·능력·URL)가 명함 역할. 동기 폴링/SSE 스트리밍/푸시 3가지 통신 모드.
- **Agent Registry**: 수백 개 에이전트·MCP 서버의 파편화 해결 — 재사용·연결 표준화·거버넌스(IAM·로깅·통신 허용목록). 레지스트리 자체가 MCP 서버 → 오케스트레이터가 **프롬프트+태그로 에이전트를 동적 발견**, URL 하드코딩 없이 원격 A2A 호출.

### 프로덕션 반패턴 (AWS "We Need to Talk About AI Agent Architectures")
- 프런트엔드→에이전트 런타임 직결 = "에이전트가 곧 백엔드"가 되는 반패턴. **"에이전트는 시스템이 아니라 시스템 안의 한 기능."** WAF(속도제한)+API Gateway+Lambda를 앞단에, 결정론적 조회(대화목록=DynamoDB)는 에이전트 밖으로.
- 보안: API GW와 에이전트 런타임에 같은 OAuth 토큰을 쓰면 게이트웨이 우회 가능 → **계층별 인증 분리**(사용자→GW는 OAuth, GW→에이전트는 IAM).

---

## 2. 컨텍스트 엔지니어링·메모리 — 에이전트의 "작업 기억" 설계

### Context rot와 오류 복리 (Google Next "Agent context engineering for production")
- 컨텍스트가 커질수록 성능 저하 = **context rot**. 4대 실패: 포이즈닝 / 과소(환각) / 과다(주의 분산·지연·비용) / 도구 정의 모호.
- 🔑 **95% 정확도 에이전트도 3단계 연쇄 시 ~86%** — 장기 작업에서 오류가 복리로 누적. 이것이 멀티에이전트 분리·컨텍스트 격리의 수학적 근거.
- 기법: ①**스킬 = progressive disclosure**(평소엔 제목+설명 메타데이터만, 호출 시 전체 로드 — 도구 스키마 상시 주입보다 토큰 효율 우수) ②세션 컴팩션(오래된 턴 요약·폐기) ③**Memory Bank**: 추출 LLM이 대화에서 의미 추출→기존 메모리와 **consolidation**(중복 병합)→비동기 처리(10분 비활성 시 트리거, hot path 오프로드). Pydantic 스키마로 **Memory Profiles** 정의(버전 추적·롤백). 주입은 just-in-time(도구로 검색) vs always-on(시스템 프롬프트) 2종.

### Strands의 컨텍스트 관리 4전략
외부화(파일·DB) / 도구로 동적 선택 / 압축 / 에이전트 간 격리. SlidingWindow(도구 호출-결과 쌍을 보존하며 지능적 트리밍) vs Summarizing(요약 비율 설정, **요약은 더 싼 모델로 위임**) — "요약은 손실 압축"임을 경고. 세션 저장은 File→S3→AgentCoreMemory로 구현체만 교체.

### Letta/MemGPT의 "컨텍스트 컴파일" (Weaviate 팟캐스트)
- 200k 컨텍스트를 다 쓰면 성능·지연·비용 모두 악화 → **실용 예산 ~3만 토큰** 권장.
- 구조화된 컨텍스트 창 = 메시지 버퍼 + 코어 메모리(human/persona 섹션) + 삭제된 메시지의 재귀 요약 + 외부 데이터 통계. 🔑 **LLM이 자기 메모리를 도구 호출(core_memory_replace/append)로 직접 편집** — 검색도 자동 RAG가 아니라 LLM의 명시적 결정.

### Mem0의 "망각을 1급 설계요소로" (Qdrant Vector Space Day)
- 메모리 루프 5단계: 관찰→추출(전부 추출하지 말 것)→검색→실행→업데이트. 강화(반복→선호 승격)·중요도 감쇠·일회성 사건 망각을 설계에 포함.
- **가중치 vs 메모리의 분업 기준**: 가중치=안정적·일반적(기술·도메인·추론 패턴), 메모리(RAG)=빠른 업데이트·검사 가능성·가역성·사용자 스코프·모델 간 이식성.

---

## 3. 검색/RAG 계층 — "모든 문제를 검색 문제로"

### Pinecone 캐스케이딩 검색
학습형 sparse(BM25 대비 TREC DL +23%) + dense를 **병렬 쿼리** → 병합 → **reranker**(cross-encoder — 쿼리·문서를 동시에 봐서 코사인 유사도보다 정확)로 상위 10~20개만 LLM에. 파이프라인 전체 정밀도 **최대 +45~48%, 평균 +24~25%**. "lost in the middle" 대응: 관련 문서를 컨텍스트 앞/뒤에 배치.

### 하이브리드·청킹·임베딩 선택
- **Qdrant 법률 AI**: dense(1024d)+BM25 sparse 한 컬렉션, RRF(순위 융합)가 기본 병합.
- **Weaviate late chunking**: 전체 문서를 롱컨텍스트 모델로 먼저 토큰 임베딩한 뒤 청킹 → 대명사-엔티티 연결 보존. ColBERT는 동일 코퍼스 2.5TB vs 일반 청킹 5GB(500배)인데 late chunking은 naive와 동일 저장.
- **임베딩 선택**(Weaviate): 구형 NDCG 0.595 vs 최신 0.908; 1천만 문서에 메모리 250GB vs 25GB. MTEB로 3~5개 후보 압축 후 자체 벤치(문서 20+쿼리 5)로 검증.
- **문서 파싱**(LlamaIndex): "PDF는 인쇄용이지 읽기용이 아니다" — PyPDF(읽기순서 붕괴)·OCR(표 상실)·VLM 스크린샷(과신)·에이전트 루프(정확하나 수십만 페이지엔 비쌈)를 각각 비판, 레이아웃 감지+다중 신호 하이브리드 권장.
- **벡터+그래프**(Cognee): 순수 벡터 검색은 60~70% 정확도(HotpotQA) — 그래프(Neo4j)+온톨로지 시맨틱 레이어로 보강.

### 멀티테넌시 (Pinecone)
index 아래 **namespace가 격리 단위**(쿼리는 정확히 1개 namespace, 한도 100/1만/5만+). 테넌트 삭제=namespace 삭제 한 번. 크로스테넌트는 ID prefix+메타데이터 필터.

---

## 4. 평가·신뢰성·가드레일 — "평가가 프로토타입→프로덕션의 관문"

### AWS Strands Evals + Steering
- 단일 턴 평가는 오류 — 실패는 **컨텍스트 누적·요약 오압축 후에** 발생. LLM-as-judge + **trajectory evaluation**(조회→검증→환불 순서 준수 검증) + 결정론적 평가기(JSON 스키마 — 빠르고 저렴) 병용. **experiment generator**가 도구·워크플로를 검사해 테스트 케이스 자동 생성. **CI/CD 게이팅**: 점수 미달 시 배포 자동 실패.
- **Steering**: "프롬프트 지시는 컨텍스트가 길어지면 효력 상실" → 런타임 개입. `steer_before_tool` 결정론적 핸들러(환불 전 필수 단계·금액 검증 = **모델 루프 안의 결정론적 검증 계층**) + LLM 조향 핸들러(별도 심판 에이전트). 판정 3종: proceed / guide(교정 피드백을 루프에 주입, 도구 호출 취소 후 재시도) / interrupt.

### Palantir AIP Evals — 피드백의 산업화
thumbs up/down+코멘트 → Feedback Workbench 4단계 상태머신(미분류→라벨→테스트케이스→학습예제) → 클릭 한 번에 eval 케이스화 → LLM-as-judge → **실패 eval을 다른 에이전트가 근본원인 분석해 프롬프트 수정안 제안** → Experiments(모델×프롬프트 그리드서치; 데모에서 0%→50% 개선). 감사자·규제환경 대응이 셀링 포인트.

### Salesforce Testing Center — 테스트 중심 ALM
에이전트=topic+action 구조. AI로 테스트케이스 최대 100개 자동 생성(독성·완전성·일관성 포함), off-topic 발화로 범위 이탈 검사. 영업 에이전트에 180개 테스트, **배포마다 전부 실행·실패 시 CI/CD 차단**(테스트를 XML로 Git 커밋). Indeed 사례: 에이전트가 75% 케이스에서 멈추는 문제를 **Agent Script로 결정론성 주입**해 해결.

### 관측(Observability)
- **Arize(Qdrant 행사)**: "쿼리 5개 돌려보고 배포"하는 vibe shipping 비판. 🔑 **유사성≠관련성**. LLM-judge로 청크별 관련성 라벨 → hit rate(0=임베딩/청킹 문제)·precision@k(낮음=컨텍스트가 쓰레기)·recall@k("조용한 살인자")·NDCG/MRR(순서 문제=reranker 필요). **검색 평가가 생성 평가보다 먼저.**
- **W&B Weave**: `@weave.op` 한 줄로 전체 트레이스·토큰·비용·지연 캡처, flame view로 병목 특정. 내장 환각 scorer를 **가드레일**로: 환각 시 1회 자기 재시도→재발 시 human-in-the-loop.
- **NVIDIA NeMo Relay**: OTel 트레이스에서 반복 도구호출 패턴 학습→Anthropic 캐싱 힌트 제공(30% 토큰비용 절감 사례)→Dynamo에 KV캐시 힌트.
- **평가 설정의 함정**(W&B Swallow): 같은 벤치마크도 채팅 템플릿·few-shot 설정에 따라 점수가 크게 요동 — 프레임워크를 개발 전에 고정하고 공개 점수와 대조 검증.

---

## 5. 추론 인프라 — 에이전트 시대의 서빙 아키텍처 (GTC 트랙)

### NVIDIA Dynamo (GTC 2025 발표, 아키텍처 밀도 최고)
- **Prefill-decode 분리**: prefill(연산집약)과 decode(메모리대역폭집약)를 별도 GPU군에 배치 — TTFT는 prefill 워커 수로, ITL은 decode 워커 수로 독립 최적화. 단일노드 분리만으로 GPU당 처리량 +30%, 2노드부터 초선형 스케일링.
- **KV-cache-aware 라우팅**: radix tree로 각 워커의 캐시 적중률+부하를 함께 스코어링 → TTFT 3배, 평균 지연 2배 개선(R1 요청 10만건 실측).
- **NIXL**: Rust 기반 zero-copy GPU간 KV 전송(RDMA/IB/이더넷), 중앙 컨트롤러 없는 P2P 노드 추가. 4단 메모리 계층(HBM→시스템메모리→SSD→오브젝트) KV 오프로드로 80유저·멀티턴 조건 1.6배 가속.

### "동시 에이전트 수"라는 새 지표 (Blackwell+Dynamo 발표)
전통 벤치마크(토큰/초)는 Q&A용 — 에이전트는 목표→계획→도구호출→재평가의 **trajectory 루프**를 돌므로 다른 지표가 필요: **"응답성을 유지하며 동시에 몇 개의 에이전트를 지속시키는가."** GB200 NVL72는 Hopper 대비 GPU당 **40배** 동시 코딩 에이전트(20 tok/s/user SLO에서 GPU당 57개 vs 1.5개). MoE 전문가를 72-GPU NVLink 단일 도메인(1,800GB/s)에 분산해 병목 해소. → 🔑 연구 프레임 연결: **분모 바꾸기의 인프라 실연**(토큰/초 → 동시 에이전트 수).

### 모델 라우팅 (GitHub Copilot Auto)
- 라우팅은 매 요청이 아니라 **세션 시작 시+컨텍스트 압축 후에만** — 매번 라우팅하면 프롬프트 캐시가 파기돼 비용 증가.
- 2단 구조: 동적 모델 선택 엔진(지연·용량·오류 실시간 재랭킹) + 작업 기반 라우터(추론/도구 오케스트레이션/디버깅 분류). 발견: **"작업별 최적 모델 혼용이 단일 최상위 모델보다 성능 우위."**

### 하드웨어 연구 전망 (Bill Dally, NVIDIA Research)
디코딩 지연의 **89%가 통신, 연산은 11%** → SRAM 인접 PE·정적 스케줄링(온칩 50ns)·칩간 대역폭 희생(400→200Gbps)으로 지연 최적화 — 목표 사용자당 초당 1.6만 토큰. 다이 위 DRAM 적층으로 비트당 에너지 10배 절감 전망.

---

## 6. 파인튜닝·RL — 에이전트를 "훈련"시키는 방법

- **NeMo 도구호출 파인튜닝**(실습 튜토리얼): XLAM 데이터셋→**LoRA SFT**(Llama-3.2-1B, 2에폭)→Evaluator→Guardrails 4단계. 결과: 함수명 정확도 **0.92**, 함수명+인자 0.72로 급상승. "AI 데이터 플라이휠"(사용 데이터→모델 개선) 명시.
- **RLP(RL Pretraining, NVIDIA Research)**: 사전학습 단계에 RL 삽입 — 다음 토큰 예측 전 "생각"을 생성시키고 정보이득을 보상으로. Qwen3 31→36%, 2.5억 토큰만으로 +35%(Nemotron 12B). Jeff Dean도 동의: "사전학습→SFT→RLHF 2단 구조는 인위적 구분, 장기적으로 행동-관찰이 사전학습에 통합될 것."
- **기업 RL의 실전 난제**(Applied Compute·Periodic Labs 패널, 前 OpenAI): 기업 데이터를 "환경+데이터포인트"로 변환. 수학·코딩과 달리 기업 현장은 **"무엇을 보상으로 삼을지"가 최대 난제**(전문가끼리 의견이 갈림) — 지연예산 내 완료율 같은 대리지표 사용. 실패 사례: 보상 해킹, 환경 모킹 실패, API rate limit로 학습 붕괴.
- **KernelLLM**(Stanford/Meta GPU MODE): LLM에게 GPU 커널을 짜게 하는 에이전트 — 프론티어 모델도 KernelBench 250문제 중 20% 미만만 PyTorch보다 빠른 정답. 원인=데이터 희소(인터넷 전체에 Triton 코드 2천개). 해법=KernelBook(Torch→Triton 쌍 5만개)+합성데이터(수율 12.5%→75%)+경쟁 리더보드(KernelBot)로 **데이터 플라이휠** 구축. 8B 모델이 671B DeepSeek-R1에 근접.

---

## 7. 엔터프라이즈 결합 — 시맨틱 계층에 LLM을 끼우는 법

> 공통 패턴: **모든 벤더가 LLM을 교체 가능 부품으로 취급하고, 차별화를 시맨틱 계층(온톨로지·그래프·카탈로그)에 둔다.** LLM은 그 계층을 "도구로 호출"하고 그 계층에 "그라운딩"된다.

### ServiceNow: Workflow Data Fabric → Context Graph → Action Fabric (Michael Park, Whiteboard)
① **데이터 계층**: 단일 물리 데이터 모델 + Integration Hub(200+ 시스템 연동) + Zero Copy(Snowflake/Databricks 원격 SQL, 데이터 이동 없음) + RaptorDB(행→컬럼 전환, 쿼리 5~10배 — 에이전트 상시 접근 대비) + **Knowledge Graph**(에이전트가 "어디서 데이터를 가져올지" 아는 내비게이션 맵). ② 운영 이력(연 1,000억 워크플로·7조 액션)이 **Context Graph**로. ③ 단일목적 에이전트 수백 개 + **AI Agent Orchestrator**(의도 파악→계획 수립→**계획을 사용자에게 제시·승인 후** 실행). **Action Fabric**에 A2A·MCP가 위치 — 외부(Gemini·Bedrock·Teams)에서 ServiceNow 런타임 호출. **AI Control Tower**: 'AI 자산'을 데이터 모델에 등록하면 타사 LLM 포함 전체 스택에 거버넌스 적용. Zurich 릴리스: **Machine Identity Console**(에이전트용 서비스 계정+위험점수), Build Agent(배포 실패 시 자가치유).

### Palantir: 온톨로지 프리미티브 = 인간·에이전트 공용 인터페이스 (AIPCon 6)
"온톨로지의 모든 프리미티브(객체·링크·액션·함수)를 인간과 AI가 동일하게 사용." AIP Logic에서 LLM 블록 체이닝 + 온톨로지 요소를 LLM에 **도구로 서빙**: Object Query Tool(객체 조회=컨텍스트 검색), **Action Tool(인간용 액션을 추가 설정 없이 LLM에 부여)**, Function Tool(ML 모델 호출). 결과는 MRP·생산스케줄 등 **시스템 오브 액션에 라이트백**. "자동화는 튜닝 다이얼" — 트리거 기준·자율/수동·재시도를 세밀 제어. 오퍼레이터는 에이전트의 액션 로그(접근 데이터·사용 도구·판단 근거) 열람 후 승인, 피드백은 온톨로지에 저장돼 **부족지식(tribal knowledge)의 거버넌스형 피드백 루프**가 됨.

### SAP: 신뢰도 점수 분기 + 에이전트 주도 마이그레이션 (Sapphire)
7개 어시스턴트(시스템분석~프로젝트관리)가 ERP 전환을 수행. 🔑 **HITL 설계의 정석: 수정안마다 신뢰도 점수 — 고신뢰=자동 적용, 중·저신뢰=개발자 검토 대기.** Joule Studio 의도기반 개발: 프롬프트→LeanIX를 MCP 서버로 랜드스케이프 파악→Knowledge Graph로 검증→Signavio로 병목 분석→PRD 자동 생성→**A2A 네이티브 에이전트+n8n 워크플로+확장앱 3층 생성**. 관세충격 데모: "에이전트는 추론, 워크플로는 응대" — 에이전트가 마진 영향 계산 후 워크플로가 4개 팀에 팬아웃. 3~5일 걸리던 조달 영향평가를 분 단위로.

### Databricks: Unity Catalog 거버넌스 위의 Agent Bricks
Unity Catalog가 모델·MCP·에이전트·평가·테이블을 **단일 거버넌스**로. Agent Bricks: Knowledge Assistant(PDF 폴더→15분 내 인용 포함 RAG), Genie(테이블 그라운딩 대화형 분석, 라인별 실행 근거 노출), **Multi-Agent Supervisor**(정형=Genie/비정형=KA 라우팅·합성). CustomerLake의 Profile Agent: 룰 기반 ID 매칭→**룰로 판단 불가 시 LLM 판정→경계 케이스만 인간 검토**, 실행마다 룰·LLM에 학습 반영(420만 프로필 데모). 수치(State of AI Agents, 2만+ 고객): 기업 78%가 2개+ LLM 패밀리 사용, **거버넌스 도입 기업이 12배 많은 프로젝트를 프로덕션 배포**.

### GitHub Agentic Workflows: 루프 밖 가드레일
마크다운+프런트매터를 Actions 워크플로로 컴파일. `safe-outputs`(PR 1개 제한)·도구/도메인 화이트리스트를 **에이전트 루프 밖에서 강제**(방화벽 개념) — 루프 안 프롬프트 지시보다 강한 보증.

---

## 8. 보안·샌드박싱 — 장기 자율 에이전트의 통제

- **NVIDIA OpenShell**(GTC "Securing Long-Running AI Agents"): 오픈소스 샌드박스+정책엔진+egress 통제+**시크릿 게이트웨이**(키를 샌드박스 밖에 두고 요청 시점에만 주입). Canonical·Microsoft·Red Hat이 OS 레벨 통합. 실사용 데모: PM이 에이전트에 전용 이메일·Slack 채널 부여, GitHub 읽기전용+웹서치 미허용(유출 방지)으로 운영.
- **AIQ Deep Research 아키텍처**: Nemotron Nano 의도 라우터 → 오케스트레이터+플래너(프론티어 모델) → 전문화 서브 리서처 5~6개(각기 다른 "성격": 증거수집·비판·반론·예측) → 신서사이저. 추론비용 50% 절감.
- **ServiceNow Machine Identity Console**: 에이전트용 서비스 계정 목록화+위험점수+미사용 계정 정리 — "에이전트의 신원 관리"가 새 보안 카테고리로.

---

## 9. 실전 배치 사례 모음 (발표에서 시연·공개된 것)

| 사례 | 스택 | 결과/수치 | 출처 |
|---|---|---|---|
| **AT&T 판매 에이전트** | ADK+Gemini, 오케스트레이터→스킬 기반 전문가 라우팅, **로직/표시 계층 분리**(웹·앱·IVR 채널 무관), Vertex Session+Memory Bank, DLP 암복호화 | 3일 뒤 다른 채널 재방문 시 기억, 7일차 백그라운드 장바구니 사전 생성. 프로덕션 가동 | Google Next |
| **ServiceNow 사내 IT 지원** | 케이스→Deep Research→트리아지→해결 에이전트 체인, 프론티어+Nemotron 혼합 | **티켓 90% 자율 해결** | NVIDIA GTC |
| **Cadence 칩 설계 검증** | Chip Stack AI, RTL 형식검증 에이전트 | **1개월→10시간** | NVIDIA Nemotron Days |
| **Carrefour Phoenix-Darwin** | Google Chat+Cloud Run ADK, RAG+BigQuery 도구셋(커스텀 파이썬 수백 줄 제거), OAuth 3-legged | 주 ~200세션 운영 | Google Cloud |
| **Playback IQ(축구 브리핑)** | Antigravity로 OTel 계측→Trace에서 TTS 직렬 병목 발견→16세그먼트 병렬화 | **96초→16~23초(80%↓)** | Google Cloud |
| **Indeed 채용 에이전트** | Agentforce, Agent Script로 결정론성 주입, Cursor+플레이북(MD)로 드리프트 방지 | 75% 미진행 문제 해소 | Salesforce |
| **LakeWatch(보안)** | Genie가 OCSF 정규화·탐지룰 자동 작성(웹리서치+스키마 샘플링 병렬→SQL→30일 오탐 검증) | 탐지룰 "1주→수 분", 알림 7천→3만 대응 | Databricks |
| **Adobe Firefly 학습 인프라** | FSDP+TP, 커스텀 데이터로더, EFA 전환, 자동 체크포인트 롤백 | GPU 유휴 66%→가동 80% | NVIDIA GTC |
| **NVIDIA 사내 개인비서** | Nemotron 3 Super(120B, 활성 12B MoE)를 DGX Spark 로컬 구동 | 로컬 프라이버시 데모 | GTC Agentic AI 101 |
| **홈어시스턴트 이슈 자동수정** | GitHub Agentic Workflows, 스택트레이스 분석→자사 버그면 수정 PR 자동 생성 | 자동 PR | GitHub |

---

## 10. 연구 프레임과의 연결 (담론 분석 관점)

1. **분모 바꾸기의 기술적 실체**: NVIDIA가 벤치마크 지표를 "토큰/초→**동시 에이전트 수**"로 재정의(Blackwell+Dynamo)하고, Bill Dally가 "연산→통신(89%)"으로 병목을 재정의 — 인프라 벤더가 성과지표 설계자·참가자·마케팅 주체를 겸함. 평가 전장(§4)도 동일: 벤더가 벤치마크를 만들고 1위를 발표.
2. **거버넌스 락인의 구현 형태**: ServiceNow Control Tower("AI 자산" 등록)·Databricks Unity Catalog(거버넌스 도입=12배 배포라는 셀링)·NVIDIA OpenShell(OS 벤더 통합) — "보안·거버넌스"를 명분으로 자사 스택 중심 표준을 앵커링.
3. **에이전트=인력의 기술 번역**: "DGX 스테이션=팀원 한 명 더"(NVIDIA), 에이전트 전용 이메일·Slack 계정 부여(OpenShell 데모), Machine Identity(에이전트 신원 관리) — 노동 은유가 실제 시스템 설계(계정·신원·온보딩)로 구현되는 중.
4. **HITL의 4가지 구현 수렴**: 신뢰도 분기(SAP) / 계획 승인(ServiceNow·Databricks) / 예외만 인간(Palantir·LakeWatch) / 경계 케이스 인간 판정(CustomerLake) — "협력의 경계"(INTERVIEW_GUIDE §8 cooperation 렌즈)가 코드 레벨에서 어떻게 그어지는지의 실증.
5. **공통 3층 수렴**: 모델 주도 루프(Strands/ADK) ② 결정론적 제어 계층(그래프·훅·스티어링·Agent Script·safe-outputs) ③ 관리형 운영 계층(AgentCore/Agent Engine/Registry) — AWS는 하네스 내부 제어를, Google은 생태계 표준(A2A·Registry)을, 엔터프라이즈는 시맨틱 계층을 각자의 해자로.

## ⚠️ 신뢰 경계
발표자 발화 기준(자사 벤치마크·데모 포함) — 제3자 검증 아님. 수치는 특정 조건의 자사 실측. 자막 오역 위험 상존(원본 확인 권장).
