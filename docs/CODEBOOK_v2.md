# 코드북 v2 — 다차원 담론 코딩 (classify_v2.py)

> 2026-07-29. 기존 `classify.py`(DX/AX/AT 어휘 매칭)의 타당성 문제를 진단(미분류 72%,
> 어휘 밀도만 측정)한 뒤 재설계한 코딩 스킴. `classify_v2.py`가 이 문서를 구현한다.
> 출력: `analysis/classified_v2.csv`. **규칙 기반(순수 정규식)이라 재현·감사 가능** —
> 논문 방법론 절에 그대로 기술할 수 있고, 클라우드 파이프라인에서도 가볍게 돈다.

## 왜 재설계했나
- 옛 `dominant`(AX/DX/AT) 라벨은 **"AI 어휘 밀도"**를 잴 뿐 담론 관련성을 반영 못 함.
  - Cohere(학술 발표)에 AX 74건이 붙고, 한국 비즈니스 AX 담론("AI 전환·도입", 약어 미사용)은
    미분류로 빠짐(전체의 72%).
- v2는 **하나의 라벨 대신 연구틀에 맞춘 여러 축을 동시 코딩**한다.

## 코딩 축

### 1. `relevance` — 담론 관련성 게이트
| 값 | 정의 | 판정 규칙(정규식 카운트) |
|---|---|---|
| `noise` | 빈/저품질 자막 | 본문 < 50단어 |
| `ax_core` | **기업·조직이 AI로 일하는 방식·비용을 바꾸는** 전환 담론 | TRANSFORM≥2, 또는 TRANSFORM≥1 & COST≥1 |
| `ax_adjacent` | AI 콘텐츠이나 전환 프레이밍 아님(튜토리얼·연구·제품데모) | AI_TECH≥2 & 위 조건 미충족 |
| `off_topic` | AI/AX 신호 없음(광고·무관) | AI_TECH=0 & TRANSFORM=0 |

- **TRANSFORM**(전환/조직 프레이밍): AI 전환·도입·enterprise AI·워크플로·조직 변화·생산성·의사결정·거버넌스·에이전트 도입·transformation office 등.
- **AI_TECH**(AI 기술 어휘): LLM·GPT·모델·에이전트·머신러닝·RAG·프롬프트 등.
- **COST**(비용/재무): 비용·인건비·ROI·예산·절감·마진·토큰 과금 등.
- ⚠️ 연구용 주 표본은 **`ax_core`**. `ax_adjacent`는 공급측 기술 담론(별도 분석), `off_topic`/`noise`는 제외.

### 2. `stance` — 톤 (ax_core·ax_adjacent에만 부여)
| 값 | 규칙 | 마커 예 |
|---|---|---|
| `anti_washing` | ANTI≥2 & ANTI>WASH | 검증·한계·실사용·human-in-the-loop·파일럿·실패·버블 |
| `washing` | WASH≥2 & WASH>ANTI | 혁명·게임체인저·10배/100배·세계최초·마법·seamless |
| `neutral` | 그 외 | — |

### 3. `subject_hint` — 발화 주체 (거친 추정)
| 값 | 규칙 |
|---|---|
| `vendor` | 공식 채널 수집분(source=channel) |
| `media_commentary` | 키워드 검색분(source=keyword) |

보조 플래그(비배타, 0/1): `is_investor_finance`·`is_academic`·`is_consulting`·`is_media`.
→ 정밀 주체 분류(customer/critic/state)는 인터뷰·수기 코딩으로 보강 필요(자동은 여기까지가 정직한 한계).

### 4. 구성개념 신호 (0/1) — 분석틀 직접 태깅
CONTENT_REVIEW·INTERVIEW_GUIDE의 축을 회귀분석용 변수로 뽑아낸다.

| 변수 | 의미 | 전체 출현율(6,055 기준) |
|---|---|---|
| `sig_denominator` | 분모 바꾸기(지표·측정단위 재정의) | ~15% |
| `sig_agent_workforce` | 에이전트=인력(AI 직원·재배치·headcount) | ~9% |
| `sig_cost` | 비용/재무 언어 | ~31% |
| `sig_sovereignty` | 주권/국가(state 축) | ~8% |
| `sig_failure_ritual` | "95% 실패" 개막 의식 | ~1% (고정밀·저재현) |
| `sig_deskilling` | 탈숙련 | ~0% (희소 담론) |
| `sig_governance` | 거버넌스/규제/감사 | ~37% |
| `sig_eval` | 평가/벤치마크/신뢰성 | ~28% |

## 검증(2026-07-29, 6,055건)
- **관련성 분포**: ax_core 1,760 / ax_adjacent 2,152 / off_topic 1,505 / noise 638.
- **오분류 교정 확인**: Cohere 74 AX → 대부분 ax_adjacent로 이동; 한국 키워드 AX 담론(김유신·김건우 등)은 ax_core로 정상 포착(예전 미분류).
- **노이즈 교정**: IKEA(66 noise), Chegg(49 off_topic), Nike(대부분 off_topic/noise)로 정확히 배제.
- **ax_core 톤**: neutral 901 / anti_washing 741 / washing 118 → 안티워싱이 워싱의 6배(검증자 담론 우세).

## 한계 (정직한 고지)
1. **규칙 기반**이라 문맥·반어·부정을 완벽히 못 잡음(임베딩/LLM 분류가 이 환경에선 인프라상 비현실적이라 채택). 고정밀·저재현 설계(특히 failure_ritual·deskilling은 과소집계 가능).
2. **자막 오역**('음악' 치환 등)이 마커를 훼손할 수 있음 → 신호는 대리지표로만.
3. **subject 자동분류는 vendor/media 2분까지만** 신뢰. 그 이상은 수기 보강.
4. 여전히 **공개 담론**이라 실제 비용구조 아님 → K1·인터뷰 삼각검증 필수.

## 사용
```bash
python classify_v2.py          # analysis/classified_v2.csv 생성
```
회귀분석 주 표본 = `relevance == "ax_core"`. 종속/독립변수로 `stance`·`sig_*`·`is_*`·`month`·`source` 사용.
