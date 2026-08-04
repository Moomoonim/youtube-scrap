# AI readiness framework 적용 가능 케이스 (코퍼스 전량 스캔)

> Holmström, J. (2022). From AI to digital transformation: The AI readiness framework.
> *Business Horizons, 65*(3), 329–339. https://doi.org/10.1016/j.bushor.2021.03.006
>
> 4차원(**technologies · activities · boundaries · goals**) × 2시점(**current · future**)
> = 8셀 스코어카드, 0~4점(0 none · 1 low · 2 moderate · 3 high · 4 excellent) **자기보고**.
> 논문의 보험사 사례: 기술 4/2 · 활동 2/3 · 경계 1/2 · 목표 0/1 (현재/미래).

생성: `python readiness_scan.py` — 스캔 9,409건 → ax_core 후보 중 4차원 모두 커버 **474건**, 그중 프레임워크에 쓸 수 있는 **20건**(A 5 · B 9 · C 6), 초점 기업 **14곳**.

케이스별 상세 카드(셀별 발췌·빈 셀·산업·국가)는 짝 문서 **`docs/AI_READINESS_CASE_DETAILS.md`** 에 있다.

## 1. 판정 규칙 — 무엇을 '적합한 케이스'로 봤나

| 요건 | 규칙 |
|---|---|
| 담론 관련성 | `classify_v2` 의 `relevance == ax_core` (전환·조직·비용 프레이밍) |
| 4차원 커버 | technologies · activities · boundaries · goals 각각 근거 문장 ≥ 1 |
| 시점 분해 | 같은 문장의 시제 마커로 current / future 배정 (미배정분은 셀 충족에 미사용) |
| 티어 | **A** = 8셀 모두 · **B** = 6~7셀 · **C** = 4~5셀 |
| **평가 단위** | 프레임워크는 *AI를 도입하는 조직*을 재는 도구다 → `case_role` 로 발화 위치를 가른다 |
| AI 연결성 | 근거 문장은 자신 또는 ±1문장에 AI 어휘가 있어야 인정. AI 연결 문장 5개 미만이면 케이스 아님(IR 실적발표 배제) |
| 가치 언어 | 원 설문의 공통 프레이즈가 'value-adding' 이므로 가치·수치 문장 2개 이상을 요구 |
| 시제 전파 | 한국어 구어는 시제를 한 번만 밝히므로, 마커 없는 문장은 앞 2·뒤 1문장의 시제를 물려받는다 |
| 근거 범위 | 초점 조직이 화자가 아니고 제목에도 없으면, 그 기업이 언급된 문장 ±2 구간만 근거로 센다 (벤더 키노트의 자기 제품 서사가 고객사 사례로 계상되는 것을 막는다) |

| case_role | 뜻 | 프레임워크 적합성 | 건수 |
|---|---|---|---|
| `adopter_self` | 도입 조직 자기발화 | **1급** — 조직이 자기 전환을 진술 | 21 |
| `third_party_case` | 제3자가 보도·강연한 도입 사례 | **2급** — 초점 조직은 명확, 진술은 제3자(교차검증 필요) | 4 |
| `vendor_customer_story` | 벤더가 소개한 고객 사례 | **3급** — 초점=고객사, 벤더 홍보 필터 필요 | 14 |
| `expert_commentary` | 전문가·미디어 일반론 | 부적합 — 초점 조직 없음(설문 문항 설계에는 유용) | 57 |
| `vendor_selfpromo` | 벤더 제품 발화 | 부적합 — 공급측 제품 담론 | 378 |

`prov_*` 점수(0~4)는 **근거 문장 밀도 대리지표**다(1문장=1 · 2=2 · 3~4=3 · 5+=4). 원 논문의 self-report 점수와 같은 것이 아니며 케이스 정렬 기준으로만 쓴다.

## 2. 차원별 근거 충족률 — 논문의 '하락 패턴'이 재현되는가

논문의 보험사는 기술 → 활동 → 경계 → 목표 순으로 점수가 체계적으로 하락했다. 우리 코퍼스(사용 가능 케이스 기준)도 같은 순서로 얇아진다.

| 차원 | 현재 근거 있는 케이스 | 미래 근거 있는 케이스 | 평균 근거 문장(현재/미래) |
|---|---|---|---|
| Technologies(기술) | 19 (95%) | 17 (85%) | 6.2 / 5.3 |
| Activities(활동) | 17 (85%) | 17 (85%) | 3.8 / 2.6 |
| Boundaries(경계) | 15 (75%) | 13 (65%) | 1.6 / 0.9 |
| Goals(목표) | 11 (55%) | 17 (85%) | 1.0 / 2.4 |

읽는 법: **경계·목표 차원의 현재 근거가 가장 얇다**는 것이 이 코퍼스의 구조적 사실이다. 논문의 진단(기업은 기술을 말하고 목표를 말하지 않는다)과 같은 방향이며, 특별호 투고 시 '공개 담론에서도 경계·목표가 비어 있다'는 근거로 쓸 수 있다.

### 2-b. 벤더가 말하는 '고객 사례'는 고객사를 잴 만큼 말하지 않는다

초점 조직이 화자가 아니고 제목에도 없는 케이스 8건에 대해 그 기업이 언급된 구간(±2문장)만 다시 세어 보면, 4차원을 유지한 것은 **0건**뿐이다. 즉 SAP·Google Cloud 키노트의 'JPMorgan/L'Oréal 사례'는 실제로는 벤더 자기 제품 서사이고, 고객 조직의 준비도를 재기에는 진술이 없다. 벤더 채널을 케이스 소스로 쓰려면 고객사 단독 세션(customer keynote)을 따로 찾아야 한다.

## 3. 기업 단위 통합 스코어카드 (여러 영상 합산 · 상위 45)

사례 연구 단위는 기업이다. 아래는 **수요측 근거(1·2급 역할)만** 합산한 것으로, 숫자는 근거 문장 수(0~4 점수가 아니다). `영상` = 이 기업이 초점인 케이스 수.

| # | 기업 | 영상 | 셀 | 기술 현/미 | 활동 현/미 | 경계 현/미 | 목표 현/미 | 가치·수치 | 기간 | 대표 역할 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Zapier** | 3 | 8/8 | 12/10 | 21/14 | 2/4 | 4/14 | 12·8 | 2025-11~2026-03 | 도입 조직 자기발화 |
| 2 | **Siemens** | 2 | 8/8 | 24/12 | 7/8 | 13/3 | 3/8 | 7·5 | 2026-01~2026-03 | 도입 조직 자기발화 |
| 3 | **SK(지주·그룹)** | 1 | 8/8 | 8/2 | 4/3 | 2/1 | 3/2 | 8·4 | 2026-07~2026-07 | 제3자가 보도·강연한 도입 사례 |
| 4 | **Salesforce** | 2 | 7/8 | 34/37 | 16/13 | 0/1 | 2/1 | 11·14 | 2025-12~2026-02 | 도입 조직 자기발화 |
| 5 | **AWS** | 2 | 7/8 | 4/6 | 2/3 | 3/3 | 0/4 | 7·6 | 2026-02~2026-07 | 도입 조직 자기발화 |
| 6 | **ServiceNow** | 1 | 7/8 | 16/9 | 9/1 | 2/1 | 0/1 | 5·5 | 2026-05~2026-05 | 도입 조직 자기발화 |
| 7 | **Intel** | 1 | 7/8 | 3/1 | 1/2 | 0/1 | 2/2 | 3·2 | 2025-11~2025-11 | 도입 조직 자기발화 |
| 8 | **Unilever** | 2 | 6/8 | 4/0 | 6/3 | 5/0 | 1/1 | 14·1 | 2024-11~2024-11 | 도입 조직 자기발화 |
| 9 | **Schneider Electric** | 1 | 6/8 | 4/4 | 3/1 | 1/1 | 0/0 | 2·2 | 2026-07~2026-07 | 도입 조직 자기발화 |
| 10 | **Microsoft** | 1 | 6/8 | 2/9 | 0/1 | 1/0 | 3/9 | 1·1 | 2025-12~2025-12 | 도입 조직 자기발화 |
| 11 | **네이버** | 1 | 6/8 | 1/6 | 1/0 | 1/3 | 0/2 | 1·1 | 2026-07~2026-07 | 벤더가 소개한 고객 사례 |
| 12 | **OpenAI** | 1 | 5/8 | 8/0 | 3/0 | 1/0 | 2/1 | 3·4 | 2026-06~2026-06 | 도입 조직 자기발화 |
| 13 | **SoftBank** | 1 | 5/8 | 3/7 | 0/2 | 0/1 | 0/1 | 1·1 | 2026-06~2026-06 | 도입 조직 자기발화 |
| 14 | **SK하이닉스** | 1 | 5/8 | 0/3 | 3/1 | 1/0 | 0/2 | 3·0 | 2026-07~2026-07 | 제3자가 보도·강연한 도입 사례 |

## 4. 1급 케이스 — 도입 조직이 자기 전환을 말한 영상 (16건 중 상위 16)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | Zapier | A8 | 기술 4/4 · 활동 4/4 · 경계 1/1 · 목표 1/4 | 6·6 | 2025-11-24 | Zapier | Zapier's Big AI Plans for 2026 Revealed! - Leadership,… | [▶](https://www.youtube.com/watch?v=EfHm1Qjztd0) |
| 2 | Zapier | A8 | 기술 2/1 · 활동 4/4 · 경계 1/3 · 목표 3/2 | 4·2 | 2026-03-09 | Zapier | Leading through AI: How top executives are turning AI … | [▶](https://www.youtube.com/watch?v=g6q02hUd_Wc) |
| 3 | ServiceNow | B7 | 기술 4/4 · 활동 4/1 · 경계 2/1 · 목표 0/1 | 5·5 | 2026-05-07 | ServiceNow | Welcome to Agentic Business ／ ServiceNow Knowledge 202… | [▶](https://www.youtube.com/watch?v=jeo2V1w-Peg) |
| 4 | Siemens | A8 | 기술 4/2 · 활동 4/3 · 경계 2/1 · 목표 2/3 | 4·5 | 2026-01-07 | Siemens | The Industrial AI Revolution: Siemens Keynote at CES 2… | [▶](https://www.youtube.com/watch?v=R4Wm6YdoZSs) |
| 5 | Intel | B7 | 기술 3/1 · 활동 1/2 · 경계 0/1 · 목표 2/2 | 3·2 | 2025-11-19 | Intel | AI Industrialization: The Next Frontier for Global Ent… | [▶](https://www.youtube.com/watch?v=fSadUMtpwcY) |
| 6 | Siemens | A8 | 기술 4/4 · 활동 1/3 · 경계 4/2 · 목표 1/4 | 3·0 | 2026-03-24 | Siemens | Industrial AI Is Scaling Now ／ Roland Busch Keynote ／ … | [▶](https://www.youtube.com/watch?v=S3vM-v8cbjY) |
| 7 | Salesforce | B6 | 기술 4/4 · 활동 4/4 · 경계 0/0 · 목표 1/1 | 8·5 | 2026-02-24 | Salesforce | Win More Sales: Salesforce Agentforce for Sales Produc… | [▶](https://www.youtube.com/watch?v=fJxyv1bYJoc) |
| 8 | Salesforce | B6 | 기술 4/4 · 활동 3/4 · 경계 0/1 · 목표 1/0 | 3·9 | 2025-12-11 | Salesforce | Agentforce World Tour NYC ／ Main Keynote 2025 ／ Salesf… | [▶](https://www.youtube.com/watch?v=sSIB8rZTkew) |
| 9 | Unilever | C5 | 기술 2/0 · 활동 3/2 · 경계 2/0 · 목표 1/0 | 9·1 | 2024-11-26 | Unilever | Investor Event 2024 CEO Presentation ／ Unilever | [▶](https://www.youtube.com/watch?v=r_BOLVAd0Kw) |
| 10 | AWS | B6 | 기술 3/3 · 활동 2/0 · 경계 2/2 · 목표 0/2 | 2·2 | 2026-07-09 | AWS Events | NYC Executive Forum 2026 - Leading Transformation When… | [▶](https://www.youtube.com/watch?v=-7VeuZfH0DM) |
| 11 | Unilever | C5 | 기술 2/0 · 활동 3/1 · 경계 3/0 · 목표 0/1 | 5·0 | 2024-11-26 | Unilever | Investor Event 2024 ／ Unilever | [▶](https://www.youtube.com/watch?v=yuMA_iYdq4w) |
| 12 | Microsoft | B6 | 기술 2/4 · 활동 0/1 · 경계 1/0 · 목표 3/4 | 1·1 | 2025-12-16 | Microsoft | Is Agentic AI upending the corporate ladder? EY's Glob… | [▶](https://www.youtube.com/watch?v=ilaDQLa1Lrk) |
| 13 | Schneider Electric | B6 | 기술 3/3 · 활동 3/1 · 경계 1/1 · 목표 0/0 | 2·2 | 2026-07-09 | Schneider Electric | Is there an ROI in industrial AI? The truth behind dat… | [▶](https://www.youtube.com/watch?v=2cJD3hlyu6g) |
| 14 | OpenAI | C5 | 기술 4/0 · 활동 3/0 · 경계 1/0 · 목표 2/1 | 3·4 | 2026-06-11 | OpenAI | Customer Ignite Talk: Antonio Bravo Acin (Global Head … | [▶](https://www.youtube.com/watch?v=UNJSk90Lz1c) |
| 15 | Zapier | C5 | 기술 3/3 · 활동 4/3 · 경계 0/0 · 목표 0/1 | 2·0 | 2025-12-08 | Zapier | RevOps Strategy 2026: RevOps Leaders Reveal Their Plan | [▶](https://www.youtube.com/watch?v=J0dUy6VYmTs) |
| 16 | SoftBank | C5 | 기술 3/4 · 활동 0/2 · 경계 0/1 · 목표 0/1 | 1·1 | 2026-06-29 | SoftBank | Special Event Hosted by SoftBank Corp., SB OAI Japan G… | [▶](https://www.youtube.com/watch?v=9WXOHFQTJGM) |

## 5. 2급 케이스 — 제3자(미디어·강연)가 다룬 도입 사례 (2건 중 상위 2)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | SK(지주·그룹) | A8 | 기술 4/2 · 활동 3/3 · 경계 2/1 · 목표 3/2 | 8·4 | 2026-07 | 티타임즈TV | 현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장) | [▶](https://www.youtube.com/watch?v=b-tgY8Q0SbA) |
| 2 | SK하이닉스 | C5 | 기술 0/3 · 활동 3/1 · 경계 1/0 · 목표 0/2 | 3·0 | 2026-07 | 한 걸음 HRD | SK하이닉스는 이렇게 했다! AI 전환을 이끄는 HR 전략과 조직 혁신 사례 | [▶](https://www.youtube.com/watch?v=LkUqd-3KEdY) |

## 6. 3급 케이스 — 벤더가 소개한 고객사 사례 (2건 중 상위 2)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | AWS | B6 | 기술 1/3 · 활동 0/3 · 경계 1/1 · 목표 0/2 | 5·4 | 2026-02-07 | Siemens | How Physical AI is Transforming Industries: AWS and Si… | [▶](https://www.youtube.com/watch?v=EfYVIaGQwts) |
| 2 | 네이버 | B6 | 기술 1/4 · 활동 1/0 · 경계 1/3 · 목표 0/2 | 1·1 | 2026-07 | 안될공학 - IT 테크 신기술 | 한국을 거대한 AI 공장으로… 엔비디아가 한국 전체를 AI로 묶는 이유 ／ 삼성·SK·현대차·네이… | [▶](https://www.youtube.com/watch?v=Of_LDvvZmYA) |

## 7. 경계선 후보 (19건) — 역할은 케이스인데 게이트에 걸린 것

초점 조직이 불명이거나 가치·수치 문장이 2개 미만인 건들이다. 초점 조직을 손으로 지정하거나 같은 기업의 다른 영상과 합치면 살아난다.

| # | 초점 조직 | 역할 | 티어 | 가치·수치 | 제목 | 링크 |
|---|---|---|---|---|---|---|
| 1 | Zapier | 도입 조직 자기발화 | A8 | 1·0 | [AMA] Kickstart Your AI Fluency: Exec Ops & HR Trans… | [▶](https://www.youtube.com/watch?v=jONuMTU-_uM) |
| 2 | McKinsey | 도입 조직 자기발화 | B6 | 1·0 | The changing role of the CMO—and what it means for g… | [▶](https://www.youtube.com/watch?v=NTVuuPSohHI) |
| 3 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | B6 | 7·8 | Build the Future with Salesforce Headless 360 ／ TDX … | [▶](https://www.youtube.com/watch?v=aKsZdyyzcfU) |
| 4 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | B6 | 4·0 | Atlassian’s Most Controversial Growth Decision ／ Mik… | [▶](https://www.youtube.com/watch?v=S3RmvHfJll4) |
| 5 | Scale AI | 도입 조직 자기발화 | C5 | 1·0 | Scale AI AI Playbook for Business Leaders ／ ALL IN 2… | [▶](https://www.youtube.com/watch?v=TPN6hbY40TU) |
| 6 | Tesla | 도입 조직 자기발화 | C5 | 0·1 | Tesla Q3 2023 Financial Results and Q&A Webcast (Ful… | [▶](https://www.youtube.com/watch?v=O5aJbvWr4gs) |
| 7 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C5 | 4·4 | Alex Hormozi’s New Playbook: Entrepreneurship in the… | [▶](https://www.youtube.com/watch?v=6Ait5R-3-lI) |
| 8 | 카카오 | 도입 조직 자기발화 | C4 | 0·0 | [ifkakao2021] 추천 시스템 airflow 2 0 도입기 | [▶](https://www.youtube.com/watch?v=TXY6JCoOTu4) |
| 9 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C5 | 0·2 | The Power of Open Source: Building Giants in the Ope… | [▶](https://www.youtube.com/watch?v=aNCLqvTCxeg) |
| 10 | L'Oréal | 벤더가 소개한 고객 사례 | D4 | 2·3 | What's new in Google Cloud's agent platform | [▶](https://www.youtube.com/watch?v=FxnjRYo3fpU) |
| 11 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C4 | 1·3 | OpenClaw, Claude, Zapier MCP: Build Agents Safely & … | [▶](https://www.youtube.com/watch?v=WPwXCwlTdz4) |
| 12 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C4 | 1·0 | The New Creative Muse: Leveraging AI in Design, Writ… | [▶](https://www.youtube.com/watch?v=-VG_jT-aVtc) |
| 13 | 삼성전자 | 벤더가 소개한 고객 사례 | D2 | 2·2 | [AI&CLOUD2026] 세션1 AI-Native 기업으로의 전환 방안 및 사례 / 삼성SD… | [▶](https://www.youtube.com/watch?v=mHbsngztlHw) |
| 14 | 삼성전자 | 제3자가 보도·강연한 도입 사례 | D2 | 0·0 | AI-Native 기업으로 전환 전략과 사례 | [▶](https://www.youtube.com/watch?v=Y-ApGj-9ceI) |
| 15 | JPMorgan | 제3자가 보도·강연한 도입 사례 | D1 | 0·0 | 26 Years of Survival Keyword AX (Great AI Transforma… | [▶](https://www.youtube.com/watch?v=VRYJJJBqsDE) |
| 16 | Ericsson | 벤더가 소개한 고객 사례 | D2 | 0·0 | Customer Success Keynote: Connected to Win: From Mom… | [▶](https://www.youtube.com/watch?v=dG9aBkJCcso) |
| 17 | JPMorgan | 벤더가 소개한 고객 사례 | D2 | 0·0 | Global Keynote: The Beginning of Better ／ SAP Sapphi… | [▶](https://www.youtube.com/watch?v=9aa-etRsaLU) |
| 18 | Microsoft | 벤더가 소개한 고객 사례 | D2 | 0·0 | Building AI Doctors Can Trust ／ A Physician’s Perspe… | [▶](https://www.youtube.com/watch?v=_aAOELqwFJc) |
| 19 | 업스테이지 | 벤더가 소개한 고객 사례 | D1 | 0·0 | Fully Connected Tokyo: [Hands-on workshop] Automatio… | [▶](https://www.youtube.com/watch?v=3VJZhKEG4ik) |

## 8. 상세 — 셀별 근거 발췌 (상위 20)

발췌는 자동자막 원문이라 오탈자·오인식이 있다(예: '애플리케이션'→'애플'). **인용 전 원문 파일 확인 필수.**

### 1. Zapier — Zapier's Big AI Plans for 2026 Revealed! - Leadership, Culture, Tools, Governance

- 티어 A (8/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 36/10 · 2025-11-24 · 채널 Zapier · [영상](https://www.youtube.com/watch?v=EfHm1Qjztd0)
- 파일: `transcripts/channels/Zapier/Zapier's_Big_AI_Plans_for_2026_Revealed!_-_Leadership,_Cultu__EfHm1Qjztd0.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■■ 4 | ■■■■ 4 |
| Boundaries | ■··· 1 | ■··· 1 |
| Goals | ■··· 1 | ■■■■ 4 |

- **기술·현재**: “저희는 올해 하반기에만 AI 에이전트 빌더 세션부터 임원진 라운드 테이블까지 총 36개의 세션을 진행했습니다.”
- **기술·미래**: “이는 기본적으로 회사 및 조직별 데이터에 맞춰 조정된 에이전트 및 관련 워크플로우를 전반적으로 최적화하는 것으로, 조직 내 모든 구성원의 오른팔 역할을 하여 효율성, 품질 및 직원 경험을 의미 있게 향상시키는 것을 목표로 합니다 .”
- **활동·현재**: “그리고 좋은 소식은 우리가 이 여정을 시작한 지 2년 반이 지났고, 이제 AI 워크플로우를 구축, 배포 및 관리하는 데 있어 몇 가지 모범 사례, 즉 우리가 '황금 경로'라고 부르는 것들을 보기 시작했다는 것입니다 .”
- **활동·미래**: “Zap의 모든 팀은 내년에도 AI를 활용한 업무 방식을 지속적으로 개선하고, 업무에서 불필요한 반복 작업을 없애고, 고객 과의 업무 품질을 향상시킬 것입니다 .”
- **경계·현재**: “덴버에서 열린 워크숍에 참석 중이었는데, 호텔 방에서 휴대폰을 집어 들고 파트너에게 전화를 걸어 "방금 인공지능의 미래를 봤는데, 그걸 배우기 위해 할 수 있는 모든 일을 잠시 미뤄두려고 해."라고 말했습니다.”
- **경계·미래**: “하지만 저희는 회사 내 모든 직무에 일정 수준의 AI 활용 능력을 요구하는 것에 대해 전혀 사과할 생각이 없으며, 해당 AI 활용 능력 프레임워크도 오픈 소스로 공개했습니다 .”
- **목표·현재**: “저희는 이러한 AI 전환 과정에서 만족도와 참여도를 향상시킬 수 있었는데, 그 이유는 업무에 집중하고 학습을 위한 시간과 구조를 마련하는 등 우선순위를 효과적으로 설정했기 때문입니다.”
- **목표·미래**: “두 번째 전략은 AI 기반 가치 공학이라고 부릅니다.”

### 2. SK(지주·그룹) — 현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)

- 티어 A (8/8셀) · 역할 `third_party_case` · 톤 `washing` · 수요/공급 신호 38/1 · 2026-07 · 채널 티타임즈TV · [영상](https://www.youtube.com/watch?v=b-tgY8Q0SbA)
- 파일: `transcripts/2026-07-23/현장에서_AI_트랜스포메이션_이끌면서_배운_것_(황재선_SK_부사장)__b-tgY8Q0SbA.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■·· 2 |
| Activities | ■■■· 3 | ■■■· 3 |
| Boundaries | ■■·· 2 | ■··· 1 |
| Goals | ■■■· 3 | ■■·· 2 |

- **기술·현재**: “그러면은 전통적인 머신러닝, 딥러닝을 가지고 원래 DX 시절에 하려고 했던 그런 과제들, 생산 수유를 개선한다라든지 그다음에 가격을 예측한다라든지 이런 과정들을 통해 가지고 뭔가 효과를 보는 단계를 거치고 그리고 나서 저는 AI 에이전트 또는 에이전틱 AI에 맞는 회사로 진화될 거다.”
- **기술·미래**: “그럼이 에이전트가 막 실행을 할 건데 사람이 의사 결정해야 되는 포인트 그다음에 성과에 대한 평가는 사람이 해 줘야 되거든요.”
- **활동·현재**: “네시보드 자체는 아까 방금 얘기했던 재무적 성과, 비재무적 성과, 그다음에 AI 모델 자체의 성능, 그다음에이 서비스 자체에 대한 이용 같이 담겨야 되는 거고 그게 그 로드맵을 실행하면서 단기에는 아마도 파일럿이기 때문에 파일럿에서는 복잡한 거 없거든요.”
- **활동·미래**: “비록 기술에 대한 전문성이 100% 가지지 않더라도 의사 결정은 제대로 해 줘야 되기 때문에 이러한 AI 조직을 저는 도해야 된다라는 거고 그 맥락에서 이제 모든 회사는 AI 팀을 만들자라는 표현을 하고 있는 거고 AI 팀이 있다라고 보면은 결국 현장 현업에서이 어떤 필요성이 있는지 요구 사항이 있는지를 대변해 줘야 되는 현업 조직이 있는 거고 그 현업 조직이 온습이 좀 더 있어야 된다는 얘기를 드리는 거고이가 역할을 할 수 있는 사람들의 에 대한 육성도 같이해…”
- **경계·현재**: “딱 성과 측정 한 가지만 해 가지고 파일럿 한번 해 보고 이게 중기로 넘어가면은 전차적으로 이렇게 확대가 될 거기 때문에 그랬을 때는 조금 더 지금보다는 더 확장돼서 고민을 해 봐야 되는 거고 장기적으로 갔을 때는 BM의 전환이라든지 전체가 이제 A의 트랜스포메이션 될 거기 때문에 단기 중기 장기에 맞춰 가지고도 이러한 지표들을 조금 더 정교하게 설명드리는게 점점 더 투자를 가속화하고 전사를 확장할 때도 중요하더라라고 했던 부분들도 좀 챙겨야 에 되는 부분들이고…”
- **경계·미래**: “비록 기술에 대한 전문성이 100% 가지지 않더라도 의사 결정은 제대로 해 줘야 되기 때문에 이러한 AI 조직을 저는 도해야 된다라는 거고 그 맥락에서 이제 모든 회사는 AI 팀을 만들자라는 표현을 하고 있는 거고 AI 팀이 있다라고 보면은 결국 현장 현업에서이 어떤 필요성이 있는지 요구 사항이 있는지를 대변해 줘야 되는 현업 조직이 있는 거고 그 현업 조직이 온습이 좀 더 있어야 된다는 얘기를 드리는 거고이가 역할을 할 수 있는 사람들의 에 대한 육성도 같이해…”
- **목표·현재**: “네시보드 자체는 아까 방금 얘기했던 재무적 성과, 비재무적 성과, 그다음에 AI 모델 자체의 성능, 그다음에이 서비스 자체에 대한 이용 같이 담겨야 되는 거고 그게 그 로드맵을 실행하면서 단기에는 아마도 파일럿이기 때문에 파일럿에서는 복잡한 거 없거든요.”
- **목표·미래**: “책에는 실제 회사에서 진행하게 됐을 때는 어떠한 방법론 로드맵을 가지고 진행해야 될지 그리고 구체적으로 그 진행에 따른 뭐 전략이라든지 우리 CEO들의 어떤 생각이라든지 성과 측정이라든지 구체적인 사례들도 좀 말씀을 드렸고 지금 남들은 어떤 서비스 또는 AI를 활용하고 있지라는 부분들에서는 제가 지난 5년간 SK에서 또 많이 고민하면서 적용했을 때에 뭐 어떤 솔루션들을 앞으로 AI를 가지고 적용하면 좋을지에 대한 뭐 솔루션에 대한 소개라든지 지금이 AI를 이제 …”

### 3. Zapier — Leading through AI: How top executives are turning AI mandates into real business transfor…

- 티어 A (8/8셀) · 역할 `adopter_self` · 톤 `washing` · 수요/공급 신호 24/1 · 2026-03-09 · 채널 Zapier · [영상](https://www.youtube.com/watch?v=g6q02hUd_Wc)
- 파일: `transcripts/channels/Zapier/Leading_through_AI_How_top_executives_are_turning_AI_mandate__g6q02hUd_Wc.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■·· 2 | ■··· 1 |
| Activities | ■■■■ 4 | ■■■■ 4 |
| Boundaries | ■··· 1 | ■■■· 3 |
| Goals | ■■■· 3 | ■■·· 2 |

- **기술·현재**: “그리고 사람들이 상황을 제대로 파악하게 되면서 , 음, 작년에 정말 기억에 남는 일이 하나 있는데, 어느 날 챗봇이 다운됐어요.”
- **기술·미래**: “이러한 프로그램 중 일부는 오늘날 리더들과의 폭넓은 대화에서부터, 참가자들이 직접 AI 에이전트를 개발하거나 차세대 AI 에이전트를 구축하거나, 조직 내에서 AI를 더욱 효과적으로 활용하는 데 사용할 수 있는 프레임워크를 개발하는 실제 빌더 워크숍에 이르기까지 다양합니다.”
- **활동·현재**: “올해 중반 말부터 승진 심사 기준에 인공지능 활용 능력 기준이 포함됩니다 .”
- **활동·미래**: “저는 Zapier의 최고 인사 및 AI 혁신 책임자인 브랜든 수무트입니다 .”
- **경계·현재**: “웹플로우는 몇 년 전에 이 회사를 인수했고, 현재 CMO와 CEO가 있습니다.”
- **경계·미래**: “그래서 2026년 2분기에 Zapier의 AI 유창성 프레임워크 V2를 오픈 소스로 공개할 예정입니다.”
- **목표·현재**: “우리는 AI에 맞춰 비즈니스 OKR을 도입하고 기회의 우선순위를 정하기 시작했습니다.”
- **목표·미래**: “하지만 어떻게 하면 인공지능의 무작위적인 행동에서 벗어나 우리가 중요하게 생각하는 비즈니스 목표를 측정 가능한 방식으로 달성할 수 있을까요?”

### 4. ServiceNow — Welcome to Agentic Business ／ ServiceNow Knowledge 2026 Opening Keynote

- 티어 B (7/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 27/14 · 2026-05-07 · 채널 ServiceNow · [영상](https://www.youtube.com/watch?v=jeo2V1w-Peg)
- 파일: `transcripts/channels/ServiceNow/Welcome_to_Agentic_Business_ServiceNow_Knowledge_2026_Openin__jeo2V1w-Peg.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■■ 4 | ■··· 1 |
| Boundaries | ■■·· 2 | ■··· 1 |
| Goals | ···· 0 | ■··· 1 |

- **기술·현재**: “우리는 이미 에이전트형 AI를 통해 30% 이상의 생산성 향상을 달성하고 있습니다 .”
- **기술·미래**: “하지만 바로 이 시점에 수십억 개의 에이전트와 로봇이 온라인에 접속하고 있습니다.”
- **활동·현재**: “영업 측면에서 자율형 영업 CRM은 이미 고객에게 실질적인 성과를 제공하고 있습니다.”
- **활동·미래**: “이들은 귀사의 기업 데이터를 기반으로 하고, 귀사의 정책에 따라 관리되며, 모든 단계에 대한 완벽한 감사 기록을 남기면서, 완전한 워크플로우를 단 몇 초 만에 실행합니다.”
- **경계·현재**: “그리고 저희의 첫 번째 파트너 중 하나인 앤 트로픽(Anthropic)이 현재 이 기술을 실제로 적용하고 있습니다 .”
- **경계·미래**: “그들은 인간 인력을 보완하는 이상적인 파트너로서, 여러분 모두가 AI 혁명과 함께 성장할 수 있도록 보장합니다 .”
- **목표·미래**: “전 세계 노동력은 고령화되고 출산율은 감소하고 있으며, 2030년까지 최대 5천만 명의 노동력 부족에 직면할 것입니다.”

### 5. Siemens — The Industrial AI Revolution: Siemens Keynote at CES 2026

- 티어 A (8/8셀) · 역할 `adopter_self` · 톤 `neutral` · 수요/공급 신호 6/10 · 2026-01-07 · 채널 Siemens · [영상](https://www.youtube.com/watch?v=R4Wm6YdoZSs)
- 파일: `transcripts/channels/Siemens/The_Industrial_AI_Revolution_Siemens_Keynote_at_CES_2026__R4Wm6YdoZSs.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■·· 2 |
| Activities | ■■■■ 4 | ■■■· 3 |
| Boundaries | ■■·· 2 | ■··· 1 |
| Goals | ■■·· 2 | ■■■· 3 |

- **기술·현재**: “세멘스는 50년 이상 산업 분야에 AI를 적용해 온 경험을 바탕으로 이러한 솔루션을 구축할 수 있습니다.”
- **기술·미래**: “첫 번째 물결은 사람들이 AI를 챗봇으로 사용하는 것이었죠 , 그렇죠?”
- **활동·현재**: “이는 여러분 손에 들린 휴대폰부터 여러분이 운전하는 자동차에 이르기까지 제품을 설계하고 제조하는 방식을 재정의하고 있습니다.”
- **활동·미래**: “우리는 2026년에 독일에서 최초의 완전 AI 기반 적응형 제조 시설을 시작할 예정입니다.”
- **경계·현재**: “그렇기 때문에 마이크로소프트에게 Seammens와의 파트너십은 매우 중요합니다.”
- **경계·미래**: “두 회사가 협력하는 완벽한 파트너십처럼 들리지 않나요 ?”
- **목표·현재**: “산업용 AI 운영 체제도 같은 비전을 가져야 합니다.”
- **목표·미래**: “이것이 바로 3년 전에 저희가 이야기했던 비전이었고, 이제 그 여정의 시작점에 서게 되었습니다.”

### 6. Intel — AI Industrialization: The Next Frontier for Global Enterprises ／ Intel

- 티어 B (7/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 21/0 · 2025-11-19 · 채널 Intel · [영상](https://www.youtube.com/watch?v=fSadUMtpwcY)
- 파일: `transcripts/channels/Intel/AI_Industrialization_The_Next_Frontier_for_Global_Enterprise__fSadUMtpwcY.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■· 3 | ■··· 1 |
| Activities | ■··· 1 | ■■·· 2 |
| Boundaries | ···· 0 | ■··· 1 |
| Goals | ■■·· 2 | ■■·· 2 |

- **기술·현재**: “저희는 약 35,000명의 사무직 직원 모두 에게 코파일럿과 같은 생성형 AI 도구에 대한 접근 권한을 제공했습니다 .”
- **기술·미래**: “그래서 우리는 자동화 및 에이전트 기반 워크플로우 생성을 위한 이 엄청난 기회를 활용할 수 있는 매우 유리한 위치에 있습니다.”
- **활동·현재**: “이러한 출시 과정은 명확한 커뮤니케이션, 주간 라이브 세션, 자기 주도 학습, AI 활용 능력 캠페인 및 고위 경영진과의 적극적인 참여를 포함한 전사적 교육 프로그램을 통해 지원되었습니다.”
- **활동·미래**: “그의 노력은 PMI의 AI 팩토리를 구축하는 데 도움이 되었으며 , 이는 재사용 가능한 차세대 AI 기능을 통해 비즈니스 가치를 제공하도록 설계된 모듈식의 안전한 생태계입니다.”
- **경계·미래**: “그의 노력은 PMI의 AI 팩토리를 구축하는 데 도움이 되었으며 , 이는 재사용 가능한 차세대 AI 기능을 통해 비즈니스 가치를 제공하도록 설계된 모듈식의 안전한 생태계입니다.”
- **목표·현재**: “그래서 우리는 증가하는 관심을 관리하면서 동시에 우리가 제공할 수 있는 것과 가장 큰 가치를 제공할 수 있는 것에 우선순위를 두는 보다 확장 가능한 방법이 필요하다는 것을 분명히 알게 되었습니다.”
- **목표·미래**: “본론으로 들어가기 전에 잠시 시간을 내어 업계를 선도하는 AI 도입을 통해 어떻게 금연 미래라는 비전을 실현하고 있는지 간단히 설명드리겠습니다 .”

### 7. Siemens — Industrial AI Is Scaling Now ／ Roland Busch Keynote ／ Siemens RXD Summit Beijing

- 티어 A (8/8셀) · 역할 `adopter_self` · 톤 `washing` · 수요/공급 신호 10/16 · 2026-03-24 · 채널 Siemens · [영상](https://www.youtube.com/watch?v=S3vM-v8cbjY)
- 파일: `transcripts/channels/Siemens/Industrial_AI_Is_Scaling_Now_Roland_Busch_Keynote_Siemens_RX__S3vM-v8cbjY.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■··· 1 | ■■■· 3 |
| Boundaries | ■■■■ 4 | ■■·· 2 |
| Goals | ■··· 1 | ■■■■ 4 |

- **기술·현재**: “An industrial AI agent recommends what to do next, how to optimize the efficiency, the speed, the quality, and it doesn't stop there.”
- **기술·미래**: “Now, you will hear more in a minute, but the more we use industrial AI, the more compute we need, and that means mainly GPU compute.”
- **활동·현재**: “And imagine that the task is he's an online influencer trying to talk about online technology, you know, on Twitter, let's say.”
- **활동·미래**: “One out of three manufacturing machines worldwide run on a Siemens controller.”
- **경계·현재**: “It is where you, customers and partners, are driving this revolution.”
- **경계·미래**: “Here we are working with another partner, Nvidia.”
- **목표·현재**: “And all of this is not a vision.”
- **목표·미래**: “The strategy, of course, is in the future everything is going to be driven by AI.”

### 8. Salesforce — Win More Sales: Salesforce Agentforce for Sales Productivity

- 티어 B (6/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 14/6 · 2026-02-24 · 채널 Salesforce · [영상](https://www.youtube.com/watch?v=fJxyv1bYJoc)
- 파일: `transcripts/channels/Salesforce/Win_More_Sales_Salesforce_Agentforce_for_Sales_Productivity__fJxyv1bYJoc.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■■ 4 | ■■■■ 4 |
| Boundaries | ···· 0 | ···· 0 |
| Goals | ■··· 1 | ■··· 1 |

- **기술·현재**: “현재 Agent Force Sales Coach는 CRM에 있는 계정 및 기회 기록의 세부 정보를 사용하여 제 성과를 분석하고 개인 맞춤형의 실행 가능한 피드백을 제공하고 있습니다.”
- **기술·미래**: “저희는 Agent Force를 통해 어떻게 영업 생산성을 향상시키고 있는지, 그리고 지난 1년간 저희가 걸어온 여정에 대해 이야기 나누고자 합니다 .”
- **활동·현재**: “현재 Agent Force Sales Coach는 CRM에 있는 계정 및 기회 기록의 세부 정보를 사용하여 제 성과를 분석하고 개인 맞춤형의 실행 가능한 피드백을 제공하고 있습니다.”
- **활동·미래**: “저희는 Agent Force를 통해 어떻게 영업 생산성을 향상시키고 있는지, 그리고 지난 1년간 저희가 걸어온 여정에 대해 이야기 나누고자 합니다 .”
- **목표·현재**: “우리의 목표는 30일 안에 에이전트 이메일이 사람이 작성한 이메일보다 지속적으로 더 나은 수준이 되는 것이었습니다.”
- **목표·미래**: “그리고 이건 단순히 대체하는 게 아니라, 인간과 에이전트가 전략적으로 협력해야 한다는 겁니다.”

### 9. Salesforce — Agentforce World Tour NYC ／ Main Keynote 2025 ／ Salesforce

- 티어 B (6/8셀) · 역할 `adopter_self` · 톤 `neutral` · 수요/공급 신호 14/9 · 2025-12-11 · 채널 Salesforce · [영상](https://www.youtube.com/watch?v=sSIB8rZTkew)
- 파일: `transcripts/channels/Salesforce/Agentforce_World_Tour_NYC_Main_Keynote_2025_Salesforce__sSIB8rZTkew.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■· 3 | ■■■■ 4 |
| Boundaries | ···· 0 | ■··· 1 |
| Goals | ■··· 1 | ···· 0 |

- **기술·현재**: “자, 여러분, Agent Force Vibes가 Agent Force 360 ​​플랫폼과 완벽하게 연동되어 여러분 모두가 대화형 방식으로 프로토타입을 구축하고, 에이전트 시대에 제품 출시 시간을 단축할 수 있도록 지원하는 방식이 바로 이것입니다.”
- **기술·미래**: “하지만 이처럼 에이전트 중심적인 시대에는 아이디어를 실질적인 비즈니스 가치로 전환하는 방식이 극적으로 변화하고 있습니다.”
- **활동·현재**: “우리는 560억 건 이상의 아웃바운드 마케팅 메시지를 발송했습니다.”
- **활동·미래**: “바로 이 네 가지 계층 덕분에 상담원이 기업 전체 데이터를 기반으로 활동할 수 있으므로 정확성과 같은 놀라운 이점을 얻을 수 있습니다.”
- **경계·미래**: “맨 왼쪽에는 제 코딩 파트너인 에이전트 포스가 있죠 .”
- **목표·현재**: “네, 저희 목표는 아주 간단하다고 생각합니다.”

### 10. Unilever — Investor Event 2024 CEO Presentation ／ Unilever

- 티어 C (5/8셀) · 역할 `adopter_self` · 톤 `neutral` · 수요/공급 신호 15/13 · 2024-11-26 · 채널 Unilever · [영상](https://www.youtube.com/watch?v=r_BOLVAd0Kw)
- 파일: `transcripts/channels/Unilever/Investor_Event_2024_CEO_Presentation_Unilever__r_BOLVAd0Kw.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■·· 2 | ···· 0 |
| Activities | ■■■· 3 | ■■·· 2 |
| Boundaries | ■■·· 2 | ···· 0 |
| Goals | ■··· 1 | ···· 0 |

- **기술·현재**: “당사의 인재 풀 전반에 걸쳐 AI 기반 노동 계획 및 생성형 AI 진단과 같은 AI 이니셔티브를 통해 노동 효율성을 크게 향상시키고 있습니다.”
- **활동·현재**: “이미 말씀드렸지만, 다시 한번 강조하자면 공급망을 더욱 민첩하고 효율적으로 만들고, 순 생산성을 향상시키며, 인공 지능(AI)을 확장하는 것입니다.”
- **활동·미래**: “잠시 휴식을 취한 후, 페르난도가 우리가 어떻게 변화를 가속화하고 있는지, 그리고 2030 성장 실행 계획이 가치 창출과 재무 알고리즘 측면에서 어떤 의미를 갖는지에 대해 이야기할 것입니다.”
- **경계·현재**: “또한 최근 토론토에 개설된 유니레버의 글로벌 AI 연구소인 호라이즌 3(Horizon 3)와 협력하여 유니레버의 AI 연구 및 캐나다 연구 생태계를 활용해 유니레버의 차세대 생산성 및 성장을 이끌어갈 혁신적인 AI 애플리케이션을 개발하고 있습니다.”
- **목표·현재**: “임원진들은 이 계획의 주요 우선순위를 명확히 설명하는 데 도움을 줄 것입니다.”

### 11. AWS — NYC Executive Forum 2026 - Leading Transformation When Technology Won’t Wait

- 티어 B (6/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 14/1 · 2026-07-09 · 채널 AWS Events · [영상](https://www.youtube.com/watch?v=-7VeuZfH0DM)
- 파일: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_Leading_Transformation_When_Techn__-7VeuZfH0DM.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■· 3 | ■■■· 3 |
| Activities | ■■·· 2 | ···· 0 |
| Boundaries | ■■·· 2 | ■■·· 2 |
| Goals | ···· 0 | ■■·· 2 |

- **기술·현재**: “솔루션 도입의 이점과 비용을 문서화하고, 어떤 부분에서 이점이 발생하는지 파악하고 있습니다.”
- **기술·미래**: “저희는 자체 AI 도구인 IT Pro를 보유하고 있는데, 그 이면에는 바로 여러분의 경쟁사가 있습니다.”
- **활동·현재**: “네, 제품 개발 방식, 엔지니어 업무 방식, 심지어 GoDaddy가 현재 영위하는 사업에 대한 사고방식까지 바꿔놓았습니다.”
- **경계·현재**: “사이버 보안 문제에 대해 오픈소스로 공개된 AI 도구가 얼마나 많은지 알면 놀라실 겁니다.”
- **경계·미래**: “저희는 AWS를 포함한 모든 파트너와 협력하고 있습니다.”
- **목표·미래**: “2026년까지 저희는 AI 혁신을 네 가지 핵심 기둥으로 정의했습니다.”

### 12. Unilever — Investor Event 2024 ／ Unilever

- 티어 C (5/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 33/49 · 2024-11-26 · 채널 Unilever · [영상](https://www.youtube.com/watch?v=yuMA_iYdq4w)
- 파일: `transcripts/channels/Unilever/Investor_Event_2024_Unilever__yuMA_iYdq4w.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■·· 2 | ···· 0 |
| Activities | ■■■· 3 | ■··· 1 |
| Boundaries | ■■■· 3 | ···· 0 |
| Goals | ···· 0 | ■··· 1 |

- **기술·현재**: “인재풀 전반에 걸친 환경 AI AI 노동 계획과 같은 계획 생성형 AI 진단이 주도하고 있습니다.”
- **활동·현재**: “다시 그 이야기로 돌아가서, 우리의 공급망을 구축하는 것에 대해 이야기해 보겠습니다.”
- **활동·미래**: “가치 창출과 재무 알고리즘이니까 그 후에는 우리가 아주 열의를 보태게 됐죠.”
- **경계·현재**: “유니레버의 글로벌 AI 연구소와 파트너십을 맺었습니다.”
- **목표·미래**: “수익성 있는 사업을 유지하고 지속적으로 성장시키세요.”

### 13. Microsoft — Is Agentic AI upending the corporate ladder? EY's Global Consulting AI Leader shares what’…

- 티어 B (6/8셀) · 역할 `adopter_self` · 톤 `washing` · 수요/공급 신호 13/1 · 2025-12-16 · 채널 Microsoft · [영상](https://www.youtube.com/watch?v=ilaDQLa1Lrk)
- 파일: `transcripts/channels/Microsoft/Is_Agentic_AI_upending_the_corporate_ladder_EY's_Global_Cons__ilaDQLa1Lrk.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■·· 2 | ■■■■ 4 |
| Activities | ···· 0 | ■··· 1 |
| Boundaries | ■··· 1 | ···· 0 |
| Goals | ■■■· 3 | ■■■■ 4 |

- **기술·현재**: “We'll be talking about moving from pilot projects to real world impact, reskilling for the AI era, and what leadership looks like when humans and AI agents team up.”
- **기술·미래**: “They will just be managing a workforce that is an agentic-based workforce, one that is extremely powerful and sometimes clumsy.”
- **활동·미래**: “When you have that, that helps you set the mindset, skill set, and the tool set objective because you shift from an approach of just implementing AI everywhere, to start to think my marketing function, I'm going to completely reinvent my marketing function.”
- **경계·현재**: “And it really is a leadership challenge to champion this, to do it in partnership with your employees.”
- **목표·현재**: “The third is we have a historical dedication to a business model that is focused on effort, and we are looking to break that with AI.”
- **목표·미래**: “And so for that reason, I don't really see it changing the need to really focus on the mindset and the skill set, because what companies are going to be after is driving differentiation from their competitors and being able to create new markets.”

### 14. Schneider Electric — Is there an ROI in industrial AI? The truth behind data, automation, and value in CPG manu…

- 티어 B (6/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 8/1 · 2026-07-09 · 채널 Schneider Electric · [영상](https://www.youtube.com/watch?v=2cJD3hlyu6g)
- 파일: `transcripts/channels/Schneider_Electric/Is_there_an_ROI_in_industrial_AI_The_truth_behind_data,_auto__2cJD3hlyu6g.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■· 3 | ■■■· 3 |
| Activities | ■■■· 3 | ■··· 1 |
| Boundaries | ■··· 1 | ■··· 1 |
| Goals | ···· 0 | ···· 0 |

- **기술·현재**: “AI 에이전트를 포함한 모든 소프트웨어가 이미 설치되어 있어서 바로 업무를 시작할 수 있도록 해 줄 수 있나요 ?"라는 것입니다.”
- **기술·미래**: “그래서 더 이상 챗봇이나 LLM에 대한 이야기가 아닙니다.”
- **활동·현재**: “그래서 우리가 이야기할 주제는 진정한 제조 가치가 어디에서 창출되는지, 특히 인공지능의 가치는 어디에 있는지, 그리고 이를 어떻게 대규모로 달성할 수 있는지에 대한 것입니다.”
- **활동·미래**: “그러니까, 저희가 발견한 사용 사례 중 하나는 제조업체 입장에서 상당히 놀라운 점인데, 그들은 2차 협력업체이기 때문에 6개월마다 생산하는 제품을 바꾸는데, 그럴 때마다 AI 사용 사례를 포함한 모든 소프트웨어를 교체해야 한다는 것입니다.”
- **경계·현재**: “제 생각에는 말씀하시는 내용이 기존 시스템 통합 및 노후화된 시스템, 즉 소위 말하는 구식 시스템이나 오래된 시스템을 다루는 브라운필드 환경의 유산에 관한 것 같습니다 .”
- **경계·미래**: “그러니까, 저희가 발견한 사용 사례 중 하나는 제조업체 입장에서 상당히 놀라운 점인데, 그들은 2차 협력업체이기 때문에 6개월마다 생산하는 제품을 바꾸는데, 그럴 때마다 AI 사용 사례를 포함한 모든 소프트웨어를 교체해야 한다는 것입니다.”

### 15. OpenAI — Customer Ignite Talk: Antonio Bravo Acin (Global Head of AI Transformation, BBVA) & OpenAI

- 티어 C (5/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 12/1 · 2026-06-11 · 채널 OpenAI · [영상](https://www.youtube.com/watch?v=UNJSk90Lz1c)
- 파일: `transcripts/channels/OpenAI/Customer_Ignite_Talk_Antonio_Bravo_Acin_(Global_Head_of_AI_T__UNJSk90Lz1c.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ···· 0 |
| Activities | ■■■· 3 | ···· 0 |
| Boundaries | ■··· 1 | ···· 0 |
| Goals | ■■·· 2 | ■··· 1 |

- **기술·현재**: “저희는 여러 국가에 걸쳐 1,000명 이상의 직원 에게 80%의 시간 절약 효과를 제공하는 100개 이상의 GPT(Global Profit Technician)를 보유하고 있습니다 .”
- **활동·현재**: “그리고 아시다시피 , 저희는 사람들이 자동화 및 GPT를 구축하여 현재 수천 명의 직원이 사용하고 있으며, 많은 경우 시간을 70~80% 절감하는 매우 효과적인 사례들을 경험했습니다.”
- **경계·현재**: “저희는 실험에도 많은 노력을 기울이고 있으며, 이와 관련하여 잠시 후 자세히 설명드릴 파트너십이 매우 중요합니다.”
- **목표·현재**: “우선, 맷이 이미 언급했듯이 BBVA는 AI 전략을 이끌어갈 매우 하향식의 의제를 수립했습니다.”
- **목표·미래**: “그래서 저희는 AI를 가치 사슬 전반에 걸쳐 주요 영향 요소에 연결하는 것을 목표로 하는 계획을 세웠고, 이 계획에 대해서는 잠시 후에 자세히 설명드리겠습니다 .”

### 16. Zapier — RevOps Strategy 2026: RevOps Leaders Reveal Their Plan

- 티어 C (5/8셀) · 역할 `adopter_self` · 톤 `washing` · 수요/공급 신호 15/2 · 2025-12-08 · 채널 Zapier · [영상](https://www.youtube.com/watch?v=J0dUy6VYmTs)
- 파일: `transcripts/channels/Zapier/RevOps_Strategy_2026_RevOps_Leaders_Reveal_Their_Plan__J0dUy6VYmTs.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■· 3 | ■■■· 3 |
| Activities | ■■■■ 4 | ■■■· 3 |
| Boundaries | ···· 0 | ···· 0 |
| Goals | ···· 0 | ■··· 1 |

- **기술·현재**: “하지만 지금 우리는 확장성 문제를 해결할 수 있는 팀이 필요하지만, 동시에 매우 실험적이고 빠르게 움직이며 새로운 도구를 시도하고, 오류를 발견하고, 아직 완벽하지 않은 에이전트를 구축할 수 있는 팀도 필요하다는 것을 깨닫고 있습니다.”
- **기술·미래**: “만약 답이 '아니요'이고 단순히 특정 데이터 포인트만 필요해서 결정을 내리거나 임시 분석을 빠르게 실행하거나, 챗봇에 입력해서 흥미로운 정보를 얻을 수 있는지 확인해야 한다면, 음, 좋네요.”
- **활동·현재**: “저는 마케팅 운영 분야에서 경력을 시작했고, 현재는 마케팅, 영업, 고객 서비스 , 지원, 툴링 및 기술 시스템, AI, 자동화, 인사이트, 분석 , 예측 등 모든 분야를 아우르는 RevOps를 이끌고 있습니다.”
- **활동·미래**: “우리는 그것이 모든 업무 흐름의 일부가 되도록 하고 싶습니다.”
- **목표·미래**: “목표는 기본적으로 팀의 역량을 두 배로 늘리는 동시에 지원 담당자들이 더 어려운 문제에 집중할 수 있도록 하고, 디지털 트윈이 더 작고 사소한 문제들을 처리할 수 있도록 하는 것입니다.”

### 17. AWS — How Physical AI is Transforming Industries: AWS and Siemens on Manufacturing and Robotics

- 티어 B (6/8셀) · 역할 `vendor_customer_story` · 톤 `anti_washing` · 수요/공급 신호 3/4 · 2026-02-07 · 채널 Siemens · [영상](https://www.youtube.com/watch?v=EfYVIaGQwts)
- 파일: `transcripts/channels/Siemens/How_Physical_AI_is_Transforming_Industries_AWS_and_Siemens_o__EfYVIaGQwts.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■··· 1 | ■■■· 3 |
| Activities | ···· 0 | ■■■· 3 |
| Boundaries | ■··· 1 | ■··· 1 |
| Goals | ···· 0 | ■■·· 2 |

- **기술·현재**: “지난 2~3년 동안 생성형 AI, 더 나아가 인공지능의 성장과 영향력을 목격해 왔습니다.”
- **기술·미래**: “그래서 기존의 함수 블록이나 다른 엔지니어링 도구들을 넘어서, 이제는 AI 기반 코파일럿이 코드를 훨씬 빠르게 생성하고 자동화 솔루션 엔지니어링에서 생산성을 30~40% 향상시킬 수 있도록 지원하는 고전적인 프로그래밍 언어 방식 의 접근법이 가능해졌습니다 .”
- **활동·미래**: “음, 한 가지 덧붙이자면, 시먼스의 전문성과 수십 년, 수백 년에 걸친 제조 공정 관련 데이터, 그리고 AWS가 제공하는 클라우드 기술 및 AI 과학 역량과 결합하면 정말 엄청난 시너지 효과를 낼 수 있습니다.”
- **경계·현재**: “음, 호스 박사님께서 말씀하신 것처럼 Semens는 물리적 AI 분야에서 혁신을 주도하고 해당 생태계에서 가치를 창출하기 위해 여러 가지 노력을 기울이고 있습니다.”
- **경계·미래**: “이제 우리는 대규모 문제를 해결할 수 있고, 이러한 공동 연구와 협력을 통해 수많은 혁신이 탄생할 것입니다.”
- **목표·미래**: “SNS Insider의 최신 보고서에 따르면, 현재 50억 달러 규모인 SNS 시장은 2033년까지 500억 달러로 성장할 것으로 예측됩니다.”

### 18. SK하이닉스 — SK하이닉스는 이렇게 했다! AI 전환을 이끄는 HR 전략과 조직 혁신 사례

- 티어 C (5/8셀) · 역할 `third_party_case` · 톤 `anti_washing` · 수요/공급 신호 17/0 · 2026-07 · 채널 한 걸음 HRD · [영상](https://www.youtube.com/watch?v=LkUqd-3KEdY)
- 파일: `transcripts/2026-07-21/SK하이닉스는_이렇게_했다!_AI_전환을_이끄는_HR_전략과_조직_혁신_사례__LkUqd-3KEdY.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ···· 0 | ■■■· 3 |
| Activities | ■■■· 3 | ■··· 1 |
| Boundaries | ■··· 1 | ···· 0 |
| Goals | ···· 0 | ■■·· 2 |

- **기술·미래**: “그래서 디지털 영량에 대한 부분도 필요하고 AI 역량도 필요하고 그냥 AI가 아니라 생성형 AI 영량 그리고 도메인 자기 직무에 대한 지식이 모두 결합되어야 AI 구성원과의 협업 효과가 극대화 된다라는 이야기를 했습니다.”
- **활동·현재**: “그렇기 때문에 이미 데이터 분석이라든지 시각화, 통계, 코딩 이런 거에 대한 학습과 업무 활용을 통해서 아 뭔가 새로운 기술을 배워서 업무에 적용시켰더니 뭔가 효율적이고 효능감이 있었다라는 것들이 있었기 때문에 이런 것들이 좀 있지 않았나라는 생각을 좀 해 봅니다.”
- **활동·미래**: “어 언제나 스스로 자신의 능력과 앞으로 내가 능력을 키우기 위해서 어떤 교육 과정을 들어야 되는지에 대한 부분까지 어 구성을 했다라는게 있었고요.”
- **경계·현재**: “소수 정로 있는 각 직무에 도메인 전문가하고 DT 조직하고 외부 대학 서울대라든지 카이스트의 전문가들과 같이 협업해서 AI 심화 비즈니스 융합 과정을 운영했습니다.”
- **목표·미래**: “그리고 아까 말씀드렸던 CEO께서 어 AI 활용을 빠르게 확산시키고이를 재상세할 수 있는 사람이 핵심 경쟁력이다라는 말씀을 하셨다고 하셨는데요.”

### 19. SoftBank — Special Event Hosted by SoftBank Corp., SB OAI Japan GK, SoftBank Group Corp., and OpenAI

- 티어 C (5/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 4/4 · 2026-06-29 · 채널 SoftBank · [영상](https://www.youtube.com/watch?v=9WXOHFQTJGM)
- 파일: `transcripts/channels/SoftBank/Special_Event_Hosted_by_SoftBank_Corp.,_SB_OAI_Japan_GK,_Sof__9WXOHFQTJGM.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■· 3 | ■■■■ 4 |
| Activities | ···· 0 | ■■·· 2 |
| Boundaries | ···· 0 | ■··· 1 |
| Goals | ···· 0 | ■··· 1 |

- **기술·현재**: “그리고 기억하시겠지만, 저희는 2020년에 OpenAI에서 에이전트 프로그램과 사고 및 추론 프로그램을 시작했는데요, 그 이후로 모델들이 생산적으로 사용하는 컴퓨팅 자원의 양이 기하 급수적으로 계속 증가하고 있습니다.”
- **기술·미래**: “맨 아래에는 다양한 유형의 취약점( 인증, API 등)을 검색하는 데 도움이 되는 스킬을 부여받은 Codex 에이전트들이 나열되어 있습니다 .”
- **활동·미래**: “이러한 방법에는 AI 기반 보안 연구를 통해 취약점 목록을 생성 하고 검증하는 것, 또는 CI/CD 워크플로에 취약점 스캔을 통합하여 개발자가 작성하는 모든 풀 리퀘스트에 대해 취약점을 스캔하는 것 등이 포함될 수 있습니다.”
- **경계·미래**: “사람들은 AI 사용법을 이해하고 있으며, 특히 양국이 사이버 공격에 대한 대비를 강화하는 시점에 이를 파트너십으로 활용해야 한다고 생각합니다.”
- **목표·미래**: “에이전트들은 점점 더 협력하고 컴퓨팅을 병렬화하여 특정 목표를 달성하기 위해 협력할 수 있게 되었고, 앞으로도 이런 추세는 계속될 것으로 예상합니다.”

### 20. 네이버 — 한국을 거대한 AI 공장으로… 엔비디아가 한국 전체를 AI로 묶는 이유 ／ 삼성·SK·현대차·네이버의 역할 ／ 샌프란시스코 AI Summit

- 티어 B (6/8셀) · 역할 `vendor_customer_story` · 톤 `anti_washing` · 수요/공급 신호 2/0 · 2026-07 · 채널 안될공학 - IT 테크 신기술 · [영상](https://www.youtube.com/watch?v=Of_LDvvZmYA)
- 파일: `transcripts/2026-07-31/한국을_거대한_AI_공장으로…_엔비디아가_한국_전체를_AI로_묶는_이유_삼성·SK·현대차·네이버의_역할_샌프__Of_LDvvZmYA.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■··· 1 | ■■■■ 4 |
| Activities | ■··· 1 | ···· 0 |
| Boundaries | ■··· 1 | ■■■· 3 |
| Goals | ···· 0 | ■■·· 2 |

- **기술·현재**: “AI 경쟁의 단위가 모델 하나에서 반도체랑 데이터 센터, 데이터랑 서비스, 그리고 공장과 로봇이 연결된이 산업 시스템 전체로 커지고 있습니다.”
- **기술·미래**: “어떤 질문을 잘못 이해했는지, 에이전트가 어느 단계에서 실패를 했는지, 로봇이 어떤 상황에서 물체를 놓쳤는지 확인을 하고요.”
- **활동·현재**: “그리고 경쟁의 단위가 커질수록 한국이 이미 가지고 있던 메모리랑 제조업, 통신망이랑 인터넷 서비스의 가치도 함께 달라지고 있어요.”
- **경계·현재**: “SK 그룹이랑 엔비디아는 SK 텔레콤이 최대 2GW 규모의 베라루빈 DSX AI 팩토리를 구축을 하고 SK하이닉스가 차세대 AI 메모리를 장기 공급하고 공동 개발하는 협력 계획을 발표를 했습니다.”
- **경계·미래**: “현대차 그룹은 이번 서밋에서 엔비디아랑 로봇 레퍼런스 플랫폼을 공동 개발하겠다고 발표를 했습니다.”
- **목표·미래**: “첫 AI 팩토리는 2027년 가동을 목표로 하고 있다고 합니다.”

## 9. 프레임워크에 쓰지 않은 것 (454건)

| 이유 | 건수 | 그래도 쓸 곳 |
|---|---|---|
| `vendor_selfpromo` — 공급측 제품 담론 | 378 | 기술 차원의 '무엇이 시장에 있나' 레퍼런스, AI 워싱 측정 |
| `expert_commentary` — 초점 조직 없는 일반론 | 57 | 설문 문항 워딩 설계, 담론 지형 분석 |
| `framework_incomplete` — 4차원 미충족 | 1,303 | — |
| `ai_thin` — AI 연결 문장 5개 미만(IR 실적발표 등) | 1,000 | — |
| 가치언어 게이트 미달(가치·수치 문장 < 2) 또는 초점 불명 | 19 | 기술 도입 사실 확인용 |
| `ax_adjacent` / `off_topic` / `noise` | 3,369 / 2,294 / 969 | — |

## 10. 한계 (정직한 고지)

1. **자기보고가 아니다.** 원 프레임워크는 조직 구성원 self-report + 퍼실리테이션 워크숍이다. 여기 점수는 공개 발화의 근거 밀도이며 조직의 실제 준비도가 아니다. 논문으로 쓰려면 이 목록을 **케이스 선별·인터뷰 대상 선정**에 쓰고 점수는 워크숍/설문으로 다시 받아야 한다.
2. **규칙 기반**이라 반어·부정·가정법을 놓친다("목표가 없었다"도 목표 차원에 잡힌다).
3. **시제 전파의 대가**: 마커 없는 문장에 앞뒤 시제를 물려주므로, 화제가 문장 사이에서 바뀌면 현재 진술이 미래 셀에 들어갈 수 있다. 상세 문서의 발췌를 보고 셀 배정을 손으로 교정하는 것을 전제로 쓸 것 — 현재/미래 구분은 이 파이프라인에서 가장 약한 고리다.
4. **경계(boundaries) 차원 과대집계 위험** — 파트너십·조직개편 어휘는 벤더 발화에 흔하다. 1급 케이스라도 경계 발췌는 눈으로 확인할 것.
5. **초점 조직 귀속은 언급 빈도 기반 추정**이다. 한 영상이 여러 기업을 다루면 최다 언급 기업이 초점이 된다 — `mentions` 열로 반드시 교차 확인.
6. **공개 담론 표본 편향**: 성공 서사가 과표집되고 실패·중단은 과소표집된다. 논문의 보험사처럼 '목표 0점'인 조직은 유튜브에 나오지 않는다.
7. 수기 코딩 검증(표본 100~200건, Cohen's κ) 전에는 방법론적 방어가 불가하다.

## 11. 재현

```bash
python classify_v2.py      # relevance 게이트 갱신
python readiness_scan.py   # 본 문서 + CSV 2종 재생성
```

- `analysis/ai_readiness_cases.csv` — 영상별 8셀 근거 수·잠정점수·역할·발췌·링크
- `analysis/ai_readiness_firms.csv` — 기업별 합산 스코어카드
