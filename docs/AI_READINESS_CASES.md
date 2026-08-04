# AI readiness framework 적용 가능 케이스 (코퍼스 전량 스캔)

> Holmström, J. (2022). From AI to digital transformation: The AI readiness framework.
> *Business Horizons, 65*(3), 329–339. https://doi.org/10.1016/j.bushor.2021.03.006
>
> 4차원(**technologies · activities · boundaries · goals**) × 2시점(**current · future**)
> = 8셀 스코어카드, 0~4점(0 none · 1 low · 2 moderate · 3 high · 4 excellent) **자기보고**.
> 논문의 보험사 사례: 기술 4/2 · 활동 2/3 · 경계 1/2 · 목표 0/1 (현재/미래).

생성: `python readiness_scan.py` — 스캔 9,409건 → ax_core 후보 중 4차원 모두 커버 **474건**, 그중 프레임워크에 쓸 수 있는 **26건**(A 6 · B 12 · C 8), 초점 기업 **18곳**.

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
| Technologies(기술) | 25 (96%) | 23 (88%) | 9.5 / 6.8 |
| Activities(활동) | 23 (88%) | 23 (88%) | 4.2 / 2.8 |
| Boundaries(경계) | 19 (73%) | 15 (58%) | 2.0 / 1.0 |
| Goals(목표) | 15 (58%) | 22 (85%) | 1.0 / 2.7 |

읽는 법: **경계·목표 차원의 현재 근거가 가장 얇다**는 것이 이 코퍼스의 구조적 사실이다. 논문의 진단(기업은 기술을 말하고 목표를 말하지 않는다)과 같은 방향이며, 특별호 투고 시 '공개 담론에서도 경계·목표가 비어 있다'는 근거로 쓸 수 있다.

## 3. 기업 단위 통합 스코어카드 (여러 영상 합산 · 상위 45)

사례 연구 단위는 기업이다. 아래는 **수요측 근거(1·2급 역할)만** 합산한 것으로, 숫자는 근거 문장 수(0~4 점수가 아니다). `영상` = 이 기업이 초점인 케이스 수.

| # | 기업 | 영상 | 셀 | 기술 현/미 | 활동 현/미 | 경계 현/미 | 목표 현/미 | 가치·수치 | 기간 | 대표 역할 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **JPMorgan** | 2 | 8/8 | 33/14 | 17/3 | 9/7 | 2/3 | 22·16 | 2026-05~2026-07 | 벤더가 소개한 고객 사례 |
| 2 | **Zapier** | 3 | 8/8 | 12/10 | 21/16 | 2/4 | 4/18 | 12·8 | 2025-11~2026-03 | 도입 조직 자기발화 |
| 3 | **Siemens** | 2 | 8/8 | 24/12 | 7/8 | 13/3 | 3/8 | 7·5 | 2026-01~2026-03 | 도입 조직 자기발화 |
| 4 | **L'Oréal** | 1 | 8/8 | 26/27 | 4/2 | 1/1 | 2/2 | 4·5 | 2026-06~2026-06 | 벤더가 소개한 고객 사례 |
| 5 | **Salesforce** | 2 | 7/8 | 34/37 | 16/13 | 0/1 | 2/1 | 11·14 | 2025-12~2026-02 | 도입 조직 자기발화 |
| 6 | **삼성전자** | 2 | 7/8 | 59/22 | 10/10 | 5/0 | 3/6 | 15·8 | 2026-07~2026-07 | 제3자가 보도·강연한 도입 사례 |
| 7 | **AWS** | 2 | 7/8 | 4/6 | 2/3 | 3/3 | 0/4 | 7·6 | 2026-02~2026-07 | 도입 조직 자기발화 |
| 8 | **ServiceNow** | 1 | 7/8 | 16/10 | 9/1 | 2/1 | 0/2 | 5·5 | 2026-05~2026-05 | 도입 조직 자기발화 |
| 9 | **Intel** | 1 | 7/8 | 3/1 | 1/2 | 0/1 | 2/2 | 3·2 | 2025-11~2025-11 | 도입 조직 자기발화 |
| 10 | **SK(지주·그룹)** | 1 | 7/8 | 7/4 | 3/5 | 2/1 | 0/7 | 8·4 | 2026-07~2026-07 | 제3자가 보도·강연한 도입 사례 |
| 11 | **Ericsson** | 1 | 7/8 | 8/4 | 2/3 | 5/0 | 1/1 | 3·2 | 2026-05~2026-05 | 벤더가 소개한 고객 사례 |
| 12 | **Unilever** | 2 | 6/8 | 4/0 | 6/3 | 5/0 | 1/1 | 14·1 | 2024-11~2024-11 | 도입 조직 자기발화 |
| 13 | **Schneider Electric** | 1 | 6/8 | 4/4 | 3/1 | 1/1 | 0/0 | 2·2 | 2026-07~2026-07 | 도입 조직 자기발화 |
| 14 | **Microsoft** | 1 | 6/8 | 2/9 | 0/1 | 1/0 | 3/9 | 1·1 | 2025-12~2025-12 | 도입 조직 자기발화 |
| 15 | **네이버** | 1 | 6/8 | 1/6 | 1/0 | 1/3 | 0/2 | 1·1 | 2026-07~2026-07 | 벤더가 소개한 고객 사례 |
| 16 | **OpenAI** | 1 | 5/8 | 8/0 | 3/0 | 1/0 | 2/1 | 3·4 | 2026-06~2026-06 | 도입 조직 자기발화 |
| 17 | **SoftBank** | 1 | 5/8 | 3/7 | 0/2 | 0/1 | 0/1 | 1·1 | 2026-06~2026-06 | 도입 조직 자기발화 |
| 18 | **SK하이닉스** | 1 | 5/8 | 0/4 | 3/1 | 1/0 | 0/3 | 3·0 | 2026-07~2026-07 | 제3자가 보도·강연한 도입 사례 |

## 4. 1급 케이스 — 도입 조직이 자기 전환을 말한 영상 (16건 중 상위 16)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | Zapier | A8 | 기술 4/4 · 활동 4/4 · 경계 1/1 · 목표 1/4 | 6·6 | 2025-11-24 | Zapier | Zapier's Big AI Plans for 2026 Revealed! - Leadership,… | [▶](https://www.youtube.com/watch?v=EfHm1Qjztd0) |
| 2 | Zapier | A8 | 기술 2/1 · 활동 4/4 · 경계 1/3 · 목표 3/4 | 4·2 | 2026-03-09 | Zapier | Leading through AI: How top executives are turning AI … | [▶](https://www.youtube.com/watch?v=g6q02hUd_Wc) |
| 3 | ServiceNow | B7 | 기술 4/4 · 활동 4/1 · 경계 2/1 · 목표 0/2 | 5·5 | 2026-05-07 | ServiceNow | Welcome to Agentic Business ／ ServiceNow Knowledge 202… | [▶](https://www.youtube.com/watch?v=jeo2V1w-Peg) |
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
| 15 | Zapier | C5 | 기술 3/3 · 활동 4/3 · 경계 0/0 · 목표 0/2 | 2·0 | 2025-12-08 | Zapier | RevOps Strategy 2026: RevOps Leaders Reveal Their Plan | [▶](https://www.youtube.com/watch?v=J0dUy6VYmTs) |
| 16 | SoftBank | C5 | 기술 3/4 · 활동 0/2 · 경계 0/1 · 목표 0/1 | 1·1 | 2026-06-29 | SoftBank | Special Event Hosted by SoftBank Corp., SB OAI Japan G… | [▶](https://www.youtube.com/watch?v=9WXOHFQTJGM) |

## 5. 2급 케이스 — 제3자(미디어·강연)가 다룬 도입 사례 (4건 중 상위 4)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | SK(지주·그룹) | B7 | 기술 4/3 · 활동 3/4 · 경계 2/1 · 목표 0/4 | 8·4 | 2026-07 | 티타임즈TV | 현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장) | [▶](https://www.youtube.com/watch?v=b-tgY8Q0SbA) |
| 2 | 삼성전자 | B7 | 기술 4/4 · 활동 3/3 · 경계 4/0 · 목표 3/2 | 9·5 | 2026-07 | 삼성SDS AX | AI-Native 기업으로 전환 전략과 사례 | [▶](https://www.youtube.com/watch?v=Y-ApGj-9ceI) |
| 3 | JPMorgan | C5 | 기술 4/1 · 활동 3/1 · 경계 0/0 · 목표 1/0 | 8·6 | 2026-07 | 메타코드M | 26 Years of Survival Keyword AX (Great AI Transformati… | [▶](https://www.youtube.com/watch?v=VRYJJJBqsDE) |
| 4 | SK하이닉스 | C5 | 기술 0/3 · 활동 3/1 · 경계 1/0 · 목표 0/3 | 3·0 | 2026-07 | 한 걸음 HRD | SK하이닉스는 이렇게 했다! AI 전환을 이끄는 HR 전략과 조직 혁신 사례 | [▶](https://www.youtube.com/watch?v=LkUqd-3KEdY) |

## 6. 3급 케이스 — 벤더가 소개한 고객사 사례 (6건 중 상위 6)

| # | 초점 조직 | 티어 | 스코어카드(현재/미래) | 가치·수치 | 날짜 | 화자·채널 | 제목 | 링크 |
|---|---|---|---|---|---|---|---|---|
| 1 | JPMorgan | A8 | 기술 4/4 · 활동 4/2 · 경계 4/4 · 목표 1/3 | 14·10 | 2026-05-13 | SAP | Global Keynote: The Beginning of Better ／ SAP Sapphire… | [▶](https://www.youtube.com/watch?v=9aa-etRsaLU) |
| 2 | L'Oréal | A8 | 기술 4/4 · 활동 3/2 · 경계 1/1 · 목표 2/2 | 4·5 | 2026-06-25 | Google Cloud Tech | What's new in Google Cloud's agent platform | [▶](https://www.youtube.com/watch?v=FxnjRYo3fpU) |
| 3 | Ericsson | B7 | 기술 4/3 · 활동 2/3 · 경계 4/0 · 목표 1/1 | 3·2 | 2026-05-21 | SAP | Customer Success Keynote: Connected to Win: From Momen… | [▶](https://www.youtube.com/watch?v=dG9aBkJCcso) |
| 4 | AWS | B6 | 기술 1/3 · 활동 0/3 · 경계 1/1 · 목표 0/2 | 5·4 | 2026-02-07 | Siemens | How Physical AI is Transforming Industries: AWS and Si… | [▶](https://www.youtube.com/watch?v=EfYVIaGQwts) |
| 5 | 삼성전자 | C5 | 기술 4/4 · 활동 4/4 · 경계 0/0 · 목표 0/3 | 6·3 | 2026-07 | IT조선 | [AI&CLOUD2026] 세션1 AI-Native 기업으로의 전환 방안 및 사례 / 삼성SDS … | [▶](https://www.youtube.com/watch?v=mHbsngztlHw) |
| 6 | 네이버 | B6 | 기술 1/4 · 활동 1/0 · 경계 1/3 · 목표 0/2 | 1·1 | 2026-07 | 안될공학 - IT 테크 신기술 | 한국을 거대한 AI 공장으로… 엔비디아가 한국 전체를 AI로 묶는 이유 ／ 삼성·SK·현대차·네이… | [▶](https://www.youtube.com/watch?v=Of_LDvvZmYA) |

## 7. 경계선 후보 (13건) — 역할은 케이스인데 게이트에 걸린 것

초점 조직이 불명이거나 가치·수치 문장이 2개 미만인 건들이다. 초점 조직을 손으로 지정하거나 같은 기업의 다른 영상과 합치면 살아난다.

| # | 초점 조직 | 역할 | 티어 | 가치·수치 | 제목 | 링크 |
|---|---|---|---|---|---|---|
| 1 | Zapier | 도입 조직 자기발화 | A8 | 1·0 | [AMA] Kickstart Your AI Fluency: Exec Ops & HR Trans… | [▶](https://www.youtube.com/watch?v=jONuMTU-_uM) |
| 2 | McKinsey | 도입 조직 자기발화 | B6 | 1·0 | The changing role of the CMO—and what it means for g… | [▶](https://www.youtube.com/watch?v=NTVuuPSohHI) |
| 3 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | B6 | 7·8 | Build the Future with Salesforce Headless 360 ／ TDX … | [▶](https://www.youtube.com/watch?v=aKsZdyyzcfU) |
| 4 | 업스테이지 | 벤더가 소개한 고객 사례 | B7 | 1·0 | Fully Connected Tokyo: [Hands-on workshop] Automatio… | [▶](https://www.youtube.com/watch?v=3VJZhKEG4ik) |
| 5 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | B6 | 4·0 | Atlassian’s Most Controversial Growth Decision ／ Mik… | [▶](https://www.youtube.com/watch?v=S3RmvHfJll4) |
| 6 | Scale AI | 도입 조직 자기발화 | C5 | 1·0 | Scale AI AI Playbook for Business Leaders ／ ALL IN 2… | [▶](https://www.youtube.com/watch?v=TPN6hbY40TU) |
| 7 | Tesla | 도입 조직 자기발화 | C5 | 0·1 | Tesla Q3 2023 Financial Results and Q&A Webcast (Ful… | [▶](https://www.youtube.com/watch?v=O5aJbvWr4gs) |
| 8 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C5 | 4·4 | Alex Hormozi’s New Playbook: Entrepreneurship in the… | [▶](https://www.youtube.com/watch?v=6Ait5R-3-lI) |
| 9 | 카카오 | 도입 조직 자기발화 | C4 | 0·0 | [ifkakao2021] 추천 시스템 airflow 2 0 도입기 | [▶](https://www.youtube.com/watch?v=TXY6JCoOTu4) |
| 10 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C5 | 0·2 | The Power of Open Source: Building Giants in the Ope… | [▶](https://www.youtube.com/watch?v=aNCLqvTCxeg) |
| 11 | Microsoft | 벤더가 소개한 고객 사례 | C5 | 1·0 | Building AI Doctors Can Trust ／ A Physician’s Perspe… | [▶](https://www.youtube.com/watch?v=_aAOELqwFJc) |
| 12 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C4 | 1·3 | OpenClaw, Claude, Zapier MCP: Build Agents Safely & … | [▶](https://www.youtube.com/watch?v=WPwXCwlTdz4) |
| 13 | (초점 조직 불명) | 벤더가 소개한 고객 사례 | C4 | 1·0 | The New Creative Muse: Leveraging AI in Design, Writ… | [▶](https://www.youtube.com/watch?v=-VG_jT-aVtc) |

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

### 2. JPMorgan — Global Keynote: The Beginning of Better ／ SAP Sapphire Orlando 2026

- 티어 A (8/8셀) · 역할 `vendor_customer_story` · 톤 `anti_washing` · 수요/공급 신호 6/19 · 2026-05-13 · 채널 SAP · [영상](https://www.youtube.com/watch?v=9aa-etRsaLU)
- 파일: `transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Orlando___9aa-etRsaLU.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■■ 4 | ■■·· 2 |
| Boundaries | ■■■■ 4 | ■■■■ 4 |
| Goals | ■··· 1 | ■■■· 3 |

- **기술·현재**: “우리는 이미 에이전트를 통합하여 장부의 일상적인 관리를 더욱 효율적으로 만들기 위한 작업을 시작했습니다.”
- **기술·미래**: “그 결과는 필립이 보여준 SAP AI 에이전트 허브에서 추적되어 여러분과 여러분의 비즈니스에 완전한 투명성과 책임성을 보장합니다.”
- **활동·현재**: “하지만 표면 아래, 영업 데모 수준을 넘어 실제 비즈니스 세계로 들어가 보면 이러한 모델들이 여러분의 비즈니스 데이터와 프로세스를 기반으로 학습되지 않았다는 사실을 알게 될 것입니다.”
- **활동·미래**: “따라서 이러한 상담원들이 여러분의 업무 환경에 미치는 영향을 처음부터 끝까지 직접 확인할 수 있습니다.”
- **경계·현재**: “Joule Studio는 출시 이후 고객과 파트너들이 이미 놀라운 결과물을 만들어내는 데 기여해 왔습니다 .”
- **경계·미래**: “이번 인수가 완료되면 BDC는 모든 데이터 저장소와의 플러그 앤 플레이 상호 운용성을 위해 개방형 테이블 형식인 Apache Iceberg를 100% 지원할 것입니다.”
- **목표·현재**: “저희는 귀사의 자산이 어떻게 관리되는지, 제조 공정이 어떻게 진행되는지, 그리고 브랜드가 매장에서 어떻게 경쟁력을 확보하는지 잘 알고 있습니다.”
- **목표·미래**: “그리고 저희가 협력하고 있는 고객사 중 한 곳의 경우 , 계약 누수액을 1억 2천만 달러 줄이는 것을 목표로 하고 있습니다.”

### 3. Zapier — Leading through AI: How top executives are turning AI mandates into real business transfor…

- 티어 A (8/8셀) · 역할 `adopter_self` · 톤 `washing` · 수요/공급 신호 24/1 · 2026-03-09 · 채널 Zapier · [영상](https://www.youtube.com/watch?v=g6q02hUd_Wc)
- 파일: `transcripts/channels/Zapier/Leading_through_AI_How_top_executives_are_turning_AI_mandate__g6q02hUd_Wc.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■·· 2 | ■··· 1 |
| Activities | ■■■■ 4 | ■■■■ 4 |
| Boundaries | ■··· 1 | ■■■· 3 |
| Goals | ■■■· 3 | ■■■■ 4 |

- **기술·현재**: “그리고 사람들이 상황을 제대로 파악하게 되면서 , 음, 작년에 정말 기억에 남는 일이 하나 있는데, 어느 날 챗봇이 다운됐어요.”
- **기술·미래**: “이러한 프로그램 중 일부는 오늘날 리더들과의 폭넓은 대화에서부터, 참가자들이 직접 AI 에이전트를 개발하거나 차세대 AI 에이전트를 구축하거나, 조직 내에서 AI를 더욱 효과적으로 활용하는 데 사용할 수 있는 프레임워크를 개발하는 실제 빌더 워크숍에 이르기까지 다양합니다.”
- **활동·현재**: “올해 중반 말부터 승진 심사 기준에 인공지능 활용 능력 기준이 포함됩니다 .”
- **활동·미래**: “저는 Zapier의 최고 인사 및 AI 혁신 책임자인 브랜든 수무트입니다 .”
- **경계·현재**: “웹플로우는 몇 년 전에 이 회사를 인수했고, 현재 CMO와 CEO가 있습니다.”
- **경계·미래**: “그래서 2026년 2분기에 Zapier의 AI 유창성 프레임워크 V2를 오픈 소스로 공개할 예정입니다.”
- **목표·현재**: “우리는 AI에 맞춰 비즈니스 OKR을 도입하고 기회의 우선순위를 정하기 시작했습니다.”
- **목표·미래**: “두 번째 단계는 그 지침을 실제 로드맵과 같은 구체적인 진행 상황으로 옮기는 것입니다.”

### 4. ServiceNow — Welcome to Agentic Business ／ ServiceNow Knowledge 2026 Opening Keynote

- 티어 B (7/8셀) · 역할 `adopter_self` · 톤 `anti_washing` · 수요/공급 신호 27/14 · 2026-05-07 · 채널 ServiceNow · [영상](https://www.youtube.com/watch?v=jeo2V1w-Peg)
- 파일: `transcripts/channels/ServiceNow/Welcome_to_Agentic_Business_ServiceNow_Knowledge_2026_Openin__jeo2V1w-Peg.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■■ 4 | ■··· 1 |
| Boundaries | ■■·· 2 | ■··· 1 |
| Goals | ···· 0 | ■■·· 2 |

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

### 6. SK(지주·그룹) — 현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)

- 티어 B (7/8셀) · 역할 `third_party_case` · 톤 `washing` · 수요/공급 신호 38/1 · 2026-07 · 채널 티타임즈TV · [영상](https://www.youtube.com/watch?v=b-tgY8Q0SbA)
- 파일: `transcripts/2026-07-23/현장에서_AI_트랜스포메이션_이끌면서_배운_것_(황재선_SK_부사장)__b-tgY8Q0SbA.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■· 3 |
| Activities | ■■■· 3 | ■■■■ 4 |
| Boundaries | ■■·· 2 | ■··· 1 |
| Goals | ···· 0 | ■■■■ 4 |

- **기술·현재**: “그러면은 전통적인 머신러닝, 딥러닝을 가지고 원래 DX 시절에 하려고 했던 그런 과제들, 생산 수유를 개선한다라든지 그다음에 가격을 예측한다라든지 이런 과정들을 통해 가지고 뭔가 효과를 보는 단계를 거치고 그리고 나서 저는 AI 에이전트 또는 에이전틱 AI에 맞는 회사로 진화될 거다.”
- **기술·미래**: “그럼이 에이전트가 막 실행을 할 건데 사람이 의사 결정해야 되는 포인트 그다음에 성과에 대한 평가는 사람이 해 줘야 되거든요.”
- **활동·현재**: “딱 성과 측정 한 가지만 해 가지고 파일럿 한번 해 보고 이게 중기로 넘어가면은 전차적으로 이렇게 확대가 될 거기 때문에 그랬을 때는 조금 더 지금보다는 더 확장돼서 고민을 해 봐야 되는 거고 장기적으로 갔을 때는 BM의 전환이라든지 전체가 이제 A의 트랜스포메이션 될 거기 때문에 단기 중기 장기에 맞춰 가지고도 이러한 지표들을 조금 더 정교하게 설명드리는게 점점 더 투자를 가속화하고 전사를 확장할 때도 중요하더라라고 했던 부분들도 좀 챙겨야 에 되는 부분들이고…”
- **활동·미래**: “그다음에 재무적은 당연히 ROI라든지 뭐 비용이 얼마만큼 줄였냐, 매출이 얼마만큼 늘었나 이런 것들을 좀 다뤄야 돼서 이런 것들이 종합적으로 포함되어 있는 저 AI 부분에서 대시보드도 중요하다.”
- **경계·현재**: “딱 성과 측정 한 가지만 해 가지고 파일럿 한번 해 보고 이게 중기로 넘어가면은 전차적으로 이렇게 확대가 될 거기 때문에 그랬을 때는 조금 더 지금보다는 더 확장돼서 고민을 해 봐야 되는 거고 장기적으로 갔을 때는 BM의 전환이라든지 전체가 이제 A의 트랜스포메이션 될 거기 때문에 단기 중기 장기에 맞춰 가지고도 이러한 지표들을 조금 더 정교하게 설명드리는게 점점 더 투자를 가속화하고 전사를 확장할 때도 중요하더라라고 했던 부분들도 좀 챙겨야 에 되는 부분들이고…”
- **경계·미래**: “비록 기술에 대한 전문성이 100% 가지지 않더라도 의사 결정은 제대로 해 줘야 되기 때문에 이러한 AI 조직을 저는 도해야 된다라는 거고 그 맥락에서 이제 모든 회사는 AI 팀을 만들자라는 표현을 하고 있는 거고 AI 팀이 있다라고 보면은 결국 현장 현업에서이 어떤 필요성이 있는지 요구 사항이 있는지를 대변해 줘야 되는 현업 조직이 있는 거고 그 현업 조직이 온습이 좀 더 있어야 된다는 얘기를 드리는 거고이가 역할을 할 수 있는 사람들의 에 대한 육성도 같이해…”
- **목표·미래**: “책에는 실제 회사에서 진행하게 됐을 때는 어떠한 방법론 로드맵을 가지고 진행해야 될지 그리고 구체적으로 그 진행에 따른 뭐 전략이라든지 우리 CEO들의 어떤 생각이라든지 성과 측정이라든지 구체적인 사례들도 좀 말씀을 드렸고 지금 남들은 어떤 서비스 또는 AI를 활용하고 있지라는 부분들에서는 제가 지난 5년간 SK에서 또 많이 고민하면서 적용했을 때에 뭐 어떤 솔루션들을 앞으로 AI를 가지고 적용하면 좋을지에 대한 뭐 솔루션에 대한 소개라든지 지금이 AI를 이제 …”

### 7. 삼성전자 — AI-Native 기업으로 전환 전략과 사례

- 티어 B (7/8셀) · 역할 `third_party_case` · 톤 `anti_washing` · 수요/공급 신호 12/0 · 2026-07 · 채널 삼성SDS AX · [영상](https://www.youtube.com/watch?v=Y-ApGj-9ceI)
- 파일: `transcripts/2026-07-26/AI-Native_기업으로_전환_전략과_사례__Y-ApGj-9ceI.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■· 3 | ■■■· 3 |
| Boundaries | ■■■■ 4 | ···· 0 |
| Goals | ■■■· 3 | ■■·· 2 |

- **기술·현재**: “그래서 에이전트에 행동하는 동작 이런 부분들은 결국 토큰으로 다 치환이 되고 토큰은 바로 비용으로 체한될 수 있기 때문에 결국 ROI를 따질 때 투자 대비 효과를 뜰 때 투자는 결국 토큰으로 다 체환이 되겠다라고 해서 최근에 이제 토큰이란 말들이 지금 많이 화두가 되고 있는 거 같습니다.”
- **기술·미래**: “어 업무 프로세스를 새롭게 디자인하는 부분들 그리고 어이 프로세스를 디자인하 것들대로 구현을 하기 위해서 에이전트를 개발하고 에이전트를 운영하는 단계 그러면 그 수없이 많은 에이전트들이 생겨나 텐데 그런 에이전트들 어떻게 관리해 나가고 거버넌스를 가져갈 것이냐에 대한 부분도 중요할 것이고 또 한편으로는 이런 에이전트가 효율적으로 잘 사용되기 위해서는 기업이 업무에서 발생하고 있는 고객 접점에서 발생하고 있는 다양한 데이터들을 를 어떻게 에이전트가 잘 쓸 수 있게…”
- **활동·현재**: “반조체에서 수율 1%가 올라가면 몇 조 단위에 어 효과가 있거든요.”
- **활동·미래**: “그러면 어 앞으로 AI 시대로 전환이 된다고 했을 때는 그러면 기존에 벽에 있었던 업무와 업무관, 부서와 부서관의 업무들도 어떻게 혁신할 것인가에 대한 부분들도 다시 원점에서 한번 짚어봐야 어 더 많은 효과가 나올 것일 것이고 결국은 의사 결정을 하는 거 관점에서 어 재설계가 되어야 되겠다라는 걸로 저희가 보고 있습니다.”
- **경계·현재**: “오프소스는 최근에 뭐 MBDI 젠슨 강도 가장 성공적인 어 오픈소스 프로젝트다라고 좀 설명을 한 바가 있는데요.”
- **목표·현재**: “그래서 그런 식으로 KPI 연동된 어 사용량의 토큰량까지도 관리할 필요가 있어는 것입니다.”
- **목표·미래**: “그래서 그러면 AI 레디테이터로 싹 바꾸면 좋은데 그 결국 다 돈이 들고 비용과 시간이 드는 일들이기 때문에 결국 첫 번째로 어떤 데이터들을 먼저 전전략적으로 바꿀 것인가를 선정하는게 당연히 제일 중요한 업무가 될 것이고 데이터 품질 관리가 좀 매우 중요합니다.”

### 8. Intel — AI Industrialization: The Next Frontier for Global Enterprises ／ Intel

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

### 9. Siemens — Industrial AI Is Scaling Now ／ Roland Busch Keynote ／ Siemens RXD Summit Beijing

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

### 10. Salesforce — Win More Sales: Salesforce Agentforce for Sales Productivity

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

### 11. Salesforce — Agentforce World Tour NYC ／ Main Keynote 2025 ／ Salesforce

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

### 12. L'Oréal — What's new in Google Cloud's agent platform

- 티어 A (8/8셀) · 역할 `vendor_customer_story` · 톤 `anti_washing` · 수요/공급 신호 5/10 · 2026-06-25 · 채널 Google Cloud Tech · [영상](https://www.youtube.com/watch?v=FxnjRYo3fpU)
- 파일: `transcripts/channels/Google_Cloud_Tech/What's_new_in_Google_Cloud's_agent_platform__FxnjRYo3fpU.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■■ 4 |
| Activities | ■■■· 3 | ■■·· 2 |
| Boundaries | ■··· 1 | ■··· 1 |
| Goals | ■■·· 2 | ■■·· 2 |

- **기술·현재**: “따라서 에이전트 엔진이 이제 개별 에이전트가 최대 7일 동안 사람의 개입 없이 단일 플랜에서 실행될 수 있도록 지원한다는 소식을 알려드리게 되어 기쁩니다 .”
- **기술·미래**: “그럼 이제 토마스와 고티에를 초대해서 로레알에서 에이전트 플랫폼을 활용해 놀라운 성과를 내고 사업을 확장하는 방법에 대해 이야기 나눠보도록 하겠습니다 .”
- **활동·현재**: “상담원의 상호 작용과 행동을 모니터링할 수 있어야 하므로, 플랫폼에 직접 통합된 사전 예방적 위협 관리 기능을 출시했습니다.”
- **활동·미래**: “우리 입장에서 흥미로운 점은 입사 첫날부터 바로 업무에 투입될 수 있는 인재를 채용할 수 있다는 것입니다.”
- **경계·현재**: “우리가 이것을 만들 수 없어서가 아니라, 최고 수준의 기술과 파트너십을 맺음으로써 우리 에게 진정으로 중요한 것, 즉 로레알을 위한 가치 창출에 집중할 수 있었기 때문입니다.”
- **경계·미래**: “요약하자면, 올해 에이전트 플랫폼을 통해 더욱 심층적인 생태계, 상호 운용성에 대한 투자, 사용 편의성을 제공하여 팀 전체가 한 곳에서 작업할 수 있도록 지원하고, 맞춤 설정 기능을 통해 에이전트가 실제로 비즈니스에 도움이 되도록 할 것입니다.”
- **목표·현재**: “우리가 이것을 만들 수 없어서가 아니라, 최고 수준의 기술과 파트너십을 맺음으로써 우리 에게 진정으로 중요한 것, 즉 로레알을 위한 가치 창출에 집중할 수 있었기 때문입니다.”
- **목표·미래**: “오늘 우리는 배터리가 포함된 기본 구성 요소를 출시하지만, 우리의 비전은 거버넌스가 플랫폼 전체에 아키텍처적으로 통합되는 것입니다.”

### 13. JPMorgan — 26 Years of Survival Keyword AX (Great AI Transformation): We’ll Tell You Everything in Ju…

- 티어 C (5/8셀) · 역할 `third_party_case` · 톤 `anti_washing` · 수요/공급 신호 31/1 · 2026-07 · 채널 메타코드M · [영상](https://www.youtube.com/watch?v=VRYJJJBqsDE)
- 파일: `transcripts/2026-07-18/26_Years_of_Survival_Keyword_AX_(Great_AI_Transformation)_We__VRYJJJBqsDE.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■··· 1 |
| Activities | ■■■· 3 | ■··· 1 |
| Boundaries | ···· 0 | ···· 0 |
| Goals | ■··· 1 | ···· 0 |

- **기술·현재**: “엔터프라이 썼다라는 부분도 있지만 어 자체 GPT 결국에는 자발적으로 영역별로 어 만들 수 있는 것들을 어 아래처럼 직접 GPT 제작할 수 있는 사람들을 40%를 만들어서 어 자생적인 선순한 구조를 만들었습니다.”
- **기술·미래**: “그러니까 반복 쉽게 말해서 저희가 뭐 어 싼 표현으로는 반복적인 노가다 같은 업무들 반복 업무는 에이전트가 해 준다.”
- **활동·현재**: “어, 전사 수익 기업의 기업에 대한 부분은 소수고 파일럿 단계를 넘어서 운영 내제와 앞서 말씀드린 최적화 부분이 중요하고 어, 마이크로소프트의 트렌디 인덱스에서 보면은 AI를 조금 더 워크플로 통합에 어, 같이 함께 운영 모델로 만들어서 실험 이상의 지속 가능한 운영 고조를 만들어야 된다라고 말해 주고 있습니다.”
- **활동·미래**: “그리고 판단과 체금 휴먼 인더로프 결국에는 인간이 중간 개입을 해서 판단과 책임을 최종해야 된다라는 부분이고 협업 구조를 설계하는 것이에 워크플로우와 운영 모델을 설계하는 것이 트랜스포메이션의 어 포인트다라고 말씀드릴 수 있습니다.”
- **목표·현재**: “특히 전략 방향이나 AI 네이티브의 전략을 할 때이 단계를 기억하시고 접근을 하시면 굉장히 알 거 같고 당연한 모델들이긴 하지만이 스루패스가 조금 더 많이 도움이 되실 부분이 있을 거라 생각합니다.”

### 14. Unilever — Investor Event 2024 CEO Presentation ／ Unilever

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

### 15. AWS — NYC Executive Forum 2026 - Leading Transformation When Technology Won’t Wait

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

### 16. Unilever — Investor Event 2024 ／ Unilever

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

### 17. Microsoft — Is Agentic AI upending the corporate ladder? EY's Global Consulting AI Leader shares what’…

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

### 18. Schneider Electric — Is there an ROI in industrial AI? The truth behind data, automation, and value in CPG manu…

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

### 19. Ericsson — Customer Success Keynote: Connected to Win: From Moment to Momentum ／ SAP Sapphire Madrid …

- 티어 B (7/8셀) · 역할 `vendor_customer_story` · 톤 `anti_washing` · 수요/공급 신호 14/9 · 2026-05-21 · 채널 SAP · [영상](https://www.youtube.com/watch?v=dG9aBkJCcso)
- 파일: `transcripts/channels/SAP/Customer_Success_Keynote_Connected_to_Win_From_Moment_to_Mom__dG9aBkJCcso.md`

| 차원 | 현재 | 미래 |
|---|---|---|
| Technologies | ■■■■ 4 | ■■■· 3 |
| Activities | ■■·· 2 | ■■■· 3 |
| Boundaries | ■■■■ 4 | ···· 0 |
| Goals | ■··· 1 | ■··· 1 |

- **기술·현재**: “무엇보다 중요한 것은, 저희 파트너 생태계가 발전하고 여러분의 비즈니스 운영이 더욱 원활해질 수 있도록 줄 스튜디오(Joule Studio)의 에이전트와 어시스턴트를 제공하기 위해 1억 유로 규모의 펀드를 조성하고 있다는 소식을 들으셨을 겁니다 .”
- **기술·미래**: “그리고 어제 들으셨겠지만, 저희는 ISO 인증을 활용하여 해당 에이전트를 개발하고 있습니다.”
- **활동·현재**: “에릭슨은 AI를 네트워크 설계 방식, 운영 방식, 그리고 에릭슨의 일상적인 운영 방식에 접목하고 있습니다.”
- **활동·미래**: “그리고 직원들을 변화시킨다는 것은 그들이 새로운 업무 방식에 적응해야 한다는 것을 의미하죠 , 그렇죠?”
- **경계·현재**: “무엇보다 중요한 것은, 저희 파트너 생태계가 발전하고 여러분의 비즈니스 운영이 더욱 원활해질 수 있도록 줄 스튜디오(Joule Studio)의 에이전트와 어시스턴트를 제공하기 위해 1억 유로 규모의 펀드를 조성하고 있다는 소식을 들으셨을 겁니다 .”
- **목표·현재**: “에릭슨의 목표는 상상할 수 없는 것을 가능하게 하는 연결을 만드는 것이며, 우리의 비전은 무한한 연결성이 삶을 개선하고, 비즈니스를 재정의하며, 지속 가능한 미래를 개척하는 세상입니다.”
- **목표·미래**: “그리고 앞으로 저희는 인공지능 구현에 훨씬 더 집중할 것입니다 .”

### 20. OpenAI — Customer Ignite Talk: Antonio Bravo Acin (Global Head of AI Transformation, BBVA) & OpenAI

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

## 9. 프레임워크에 쓰지 않은 것 (448건)

| 이유 | 건수 | 그래도 쓸 곳 |
|---|---|---|
| `vendor_selfpromo` — 공급측 제품 담론 | 378 | 기술 차원의 '무엇이 시장에 있나' 레퍼런스, AI 워싱 측정 |
| `expert_commentary` — 초점 조직 없는 일반론 | 57 | 설문 문항 워딩 설계, 담론 지형 분석 |
| `framework_incomplete` — 4차원 미충족 | 1,303 | — |
| `ai_thin` — AI 연결 문장 5개 미만(IR 실적발표 등) | 1,000 | — |
| 가치언어 게이트 미달(가치·수치 문장 < 2) 또는 초점 불명 | 13 | 기술 도입 사실 확인용 |
| `ax_adjacent` / `off_topic` / `noise` | 3,369 / 2,294 / 969 | — |

## 10. 한계 (정직한 고지)

1. **자기보고가 아니다.** 원 프레임워크는 조직 구성원 self-report + 퍼실리테이션 워크숍이다. 여기 점수는 공개 발화의 근거 밀도이며 조직의 실제 준비도가 아니다. 논문으로 쓰려면 이 목록을 **케이스 선별·인터뷰 대상 선정**에 쓰고 점수는 워크숍/설문으로 다시 받아야 한다.
2. **규칙 기반**이라 반어·부정·가정법을 놓친다("목표가 없었다"도 목표 차원에 잡힌다). 시제 배정은 문장 내 마커에 의존하므로 자동자막의 문장 경계 오류에 취약하다.
3. **경계(boundaries) 차원 과대집계 위험** — 파트너십·조직개편 어휘는 벤더 발화에 흔하다. 1급 케이스라도 경계 발췌는 눈으로 확인할 것.
4. **초점 조직 귀속은 언급 빈도 기반 추정**이다. 한 영상이 여러 기업을 다루면 최다 언급 기업이 초점이 된다 — `mentions` 열로 반드시 교차 확인.
5. **공개 담론 표본 편향**: 성공 서사가 과표집되고 실패·중단은 과소표집된다. 논문의 보험사처럼 '목표 0점'인 조직은 유튜브에 나오지 않는다.
6. 수기 코딩 검증(표본 100~200건, Cohen's κ) 전에는 방법론적 방어가 불가하다.

## 11. 재현

```bash
python classify_v2.py      # relevance 게이트 갱신
python readiness_scan.py   # 본 문서 + CSV 2종 재생성
```

- `analysis/ai_readiness_cases.csv` — 영상별 8셀 근거 수·잠정점수·역할·발췌·링크
- `analysis/ai_readiness_firms.csv` — 기업별 합산 스코어카드
