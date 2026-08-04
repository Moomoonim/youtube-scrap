# Verhoef 3단계 프레임으로 본 코퍼스 사례집

> **이론틀**: Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q.,
> Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary
> reflection and research agenda. *Journal of Business Research, 122*, 889–901.
> https://doi.org/10.1016/j.jbusres.2019.09.022
>
> 생성: `python classify_verhoef.py` · 원자료: `analysis/verhoef_stages.csv`

## 이 문서는 무엇인가

수집된 유튜브 AX 담론 전량을 Verhoef et al.(2021)의 **디지털 변화 3단계**로
태깅하고, 단계별로 **어떤 회사의 어떤 사례가 그 단계에 해당하는지**를
근거 문장과 함께 모은 것이다. 논문이 개념적 리뷰(스코핑 리뷰)라 사례가 없는
자리에, 이 코퍼스가 **2020–2026년 AI 국면의 사례 증거**를 채워 넣는 구조다.

| 단계 | 논문 정의 | 목표 | 이 코퍼스에서의 판별 신호 |
|---|---|---|---|
| **S1 digitization**(전산화) | 아날로그 정보의 디지털 변환. 가치창출 활동 자체는 불변 | 비용 절감 | 종이·수기·스캔·OCR·전산화·전자문서·데이터 입력 |
| **S2 digitalization**(디지털화) | 디지털 기술로 **기존 프로세스**를 변경·최적화 | 비용 절감 + 고객경험 | 프로세스/업무 자동화·RPA·ERP/CRM·클라우드 전환·챗봇·콜센터·리드타임 |
| **S3 digital transformation**(디지털 전환) | 전사적 차원의 **새 비즈니스 모델**과 가치창출·전유 로직 | 사업 논리 재구성 | 비즈니스 모델·수익구조 전환·플랫폼 비즈니스·생태계·구독/서비스화·가치사슬 재편 |
| **S4c**(보조축, 논문 밖) | AX가 DX의 연장(제4단계)인지 질적으로 다른 전환인지 논증할 후보 | — | 의사결정 알고리즘화·자율 에이전트·AI 인력화 |

**S4c는 Verhoef의 프레임이 아니다.** 논문은 AI를 IoT·블록체인과 함께 외부
동인의 하나로만 다루고, 2018년까지의 문헌만 포괄한다(생성형 AI 이전).
따라서 이 축은 "이 담론이 3단계 중 어디를 말하는가"를 판별한 뒤,
**3단계로 담기지 않는 잔여**를 표시하기 위한 것이다 — AX를 제4단계로 볼지
별개 전환으로 볼지는 이 잔여를 근거로 논증해야 한다.

## 방법 (재현 가능)

1. `transcripts/**/*.md` 전량(자막 스크립트)을 읽는다.
2. 단계별 정규식 사전(`classify_verhoef.py` 상단)의 **등장 횟수**를 센다.
3. 단계 배정: 3단계는 **누적·위계적**(전환은 디지털화를 포함)이므로
   **상위 단계부터** 최소 2회 기준을 넘는 첫 단계로 배정한다.
   어느 단계도 미달이면 `unassigned`(사례로 볼 근거 부족).
4. 근거 문장: 단계 마커가 든 문장 중 **수치·행동 동사·AI 문맥** 점수가
   가장 높은 한 문장을 발췌한다.
5. Table 1의 네 전략 요소(디지털 자원·조직구조·성장전략·지표)를 보조 축으로
   0/1 코딩한다.

> ⚠️ 규칙 기반 1차 태깅이다. 발화 주체(벤더 홍보 vs 도입 기업 증언)와 맥락은
> 자동으로 완전히 가려지지 않는다. **인용 전 원문 스크립트·영상 확인 필수.**

## 기존 코드북(DX/AX/AT)과의 관계

이 저장소의 `docs/CODEBOOK.md`는 DX → AX → AT를 심화 스펙트럼으로 본다.
Verhoef 프레임은 그중 **DX 한 칸을 셋으로 쪼갠다**:

```
CODEBOOK:   DX ─────────────────────▶ AX ────────▶ AT
Verhoef:    S1 ─▶ S2 ─▶ S3           (논문 밖: S4c 보조축)
            전산화  디지털화  전환
```

즉 기존 `DX_hits`는 S1(전산화)·S2(프로세스 최적화)·S3(BM 재구성)을 **하나로
뭉뚱그린 지표**였다. 이 태깅의 실익은 "DX를 말한다"는 담론이 실제로는 대부분
**S2에 머문다**는 것을 분리해 보여주는 데 있다 — AX 담론이 S2의 반복인지
S3의 재구성인지를 가르는 것이 AX 연구의 핵심 질문이기 때문이다.

## 1. 단계 분포

전체 9,409건 · 연구용 주 표본(`relevance=ax_core`) 2,777건

| 단계 | 전체 | 비율 | ax_core | 비율(ax_core) |
|---|---:|---:|---:|---:|
| S1 digitization(전산화) | 153 | 1.6% | 52 | 1.9% |
| S2 digitalization(디지털화) | 1,443 | 15.3% | 1,125 | 40.5% |
| S3 digital transformation(디지털 전환) | 183 | 1.9% | 133 | 4.8% |
| unassigned(근거 부족) | 7,630 | 81.1% | 1,467 | 52.8% |

> S4c(알고리즘 전환 후보) 신호는 ax_core 45건(1.6%)에서 관측된다 — 단계 배정과 별개의 보조 축이다.

**단계 혼합**(한 영상이 여러 단계 기준을 동시에 넘는 경우) — 3단계가 누적적이라는 논문의 주장과 대조할 지점:

| 혼합 유형 | ax_core 건수 |
|---|---:|
| - | 1,467 |
| S2 | 1,040 |
| S1+S2 | 85 |
| S2+S3 | 62 |
| S3 | 58 |
| S1 | 52 |
| S1+S2+S3 | 10 |
| S1+S3 | 3 |

**읽는 법.** 단계가 배정된 1,310건 중 **S2가 1,125건으로
S3(133건)의 8.5배**다. 즉 이 코퍼스의 AX 담론은 압도적으로 **기존 프로세스의
자동화·최적화**(Verhoef의 digitalization)를 말하고 있고, **비즈니스 모델과 가치창출
로직을 바꾸는 이야기**(digital transformation)는 소수다. Verhoef et al.(2021)이
"기술 도입 문제가 아니라 비즈니스 모델 혁신 문제"라고 재정의한 지점과 대조하면,
현재 AX 담론의 대부분은 **S2 언어로 S3를 자칭**하고 있다는 가설을 세울 수 있다.
S1(전산화)이 52건으로 희소한 것은 2020년대 코퍼스로서 자연스럽다 —
아날로그→디지털 변환은 이미 지나온 단계이기 때문이다.

`unassigned` 1,467건은 "AX 담론이지만 **단계 언어를 쓰지 않는**"
경우다(모델·에이전트 기술 소개, 전략 일반론 등). 3단계 프레임이 AI 국면의 담론을
얼마나 담아내지 못하는지를 보여주는 수치이기도 하다.

### 월별 추이 (ax_core, 단계별 건수)

| 월 | S1 | S2 | S3 | unassigned |
|---|---:|---:|---:|---:|
| 2020-01 | 0 | 0 | 0 | 1 |
| 2020-02 | 0 | 0 | 0 | 2 |
| 2020-05 | 0 | 0 | 0 | 3 |
| 2020-06 | 0 | 0 | 0 | 1 |
| 2020-08 | 0 | 0 | 0 | 1 |
| 2020-09 | 0 | 0 | 1 | 4 |
| 2020-10 | 0 | 0 | 0 | 1 |
| 2020-11 | 0 | 0 | 0 | 2 |
| 2020-12 | 0 | 1 | 0 | 5 |
| 2021-01 | 0 | 0 | 1 | 0 |
| 2021-02 | 0 | 0 | 1 | 1 |
| 2021-03 | 0 | 0 | 0 | 2 |
| 2021-04 | 0 | 0 | 0 | 1 |
| 2021-05 | 0 | 1 | 0 | 2 |
| 2021-06 | 0 | 0 | 1 | 1 |
| 2021-07 | 0 | 2 | 0 | 3 |
| 2021-08 | 0 | 0 | 0 | 2 |
| 2021-09 | 0 | 0 | 0 | 1 |
| 2021-10 | 0 | 0 | 1 | 4 |
| 2021-11 | 2 | 2 | 0 | 2 |
| 2021-12 | 0 | 1 | 1 | 3 |
| 2022-02 | 0 | 3 | 0 | 1 |
| 2022-03 | 0 | 0 | 1 | 1 |
| 2022-04 | 0 | 1 | 0 | 5 |
| 2022-06 | 0 | 0 | 0 | 1 |
| 2022-07 | 0 | 0 | 0 | 1 |
| 2022-08 | 0 | 1 | 0 | 2 |
| 2022-09 | 0 | 0 | 1 | 2 |
| 2022-10 | 0 | 1 | 0 | 3 |
| 2022-11 | 0 | 2 | 0 | 4 |
| 2022-12 | 1 | 5 | 0 | 6 |
| 2023-01 | 0 | 0 | 0 | 3 |
| 2023-02 | 0 | 0 | 0 | 3 |
| 2023-03 | 0 | 0 | 0 | 7 |
| 2023-04 | 0 | 1 | 1 | 3 |
| 2023-05 | 0 | 1 | 0 | 3 |
| 2023-06 | 0 | 2 | 0 | 2 |
| 2023-07 | 0 | 2 | 1 | 1 |
| 2023-08 | 0 | 9 | 0 | 0 |
| 2023-09 | 1 | 3 | 2 | 1 |
| 2023-10 | 0 | 1 | 2 | 5 |
| 2023-11 | 0 | 4 | 1 | 4 |
| 2023-12 | 0 | 0 | 0 | 2 |
| 2024-01 | 0 | 1 | 0 | 2 |
| 2024-02 | 0 | 1 | 0 | 8 |
| 2024-03 | 1 | 1 | 0 | 5 |
| 2024-04 | 1 | 4 | 0 | 2 |
| 2024-05 | 1 | 8 | 0 | 8 |
| 2024-06 | 0 | 3 | 0 | 6 |
| 2024-07 | 0 | 3 | 2 | 6 |
| 2024-08 | 0 | 5 | 0 | 3 |
| 2024-09 | 0 | 3 | 0 | 15 |
| 2024-10 | 1 | 8 | 1 | 8 |
| 2024-11 | 0 | 13 | 4 | 7 |
| 2024-12 | 0 | 8 | 0 | 6 |
| 2025-01 | 0 | 12 | 1 | 9 |
| 2025-02 | 0 | 10 | 2 | 5 |
| 2025-03 | 1 | 9 | 0 | 23 |
| 2025-04 | 1 | 16 | 2 | 19 |
| 2025-05 | 0 | 9 | 2 | 20 |
| 2025-06 | 1 | 17 | 1 | 33 |
| 2025-07 | 0 | 14 | 2 | 41 |
| 2025-08 | 0 | 14 | 3 | 38 |
| 2025-09 | 2 | 29 | 4 | 36 |
| 2025-10 | 3 | 48 | 6 | 52 |
| 2025-11 | 1 | 54 | 3 | 73 |
| 2025-12 | 2 | 72 | 8 | 76 |
| 2026-01 | 4 | 35 | 6 | 74 |
| 2026-02 | 6 | 45 | 4 | 61 |
| 2026-03 | 3 | 65 | 6 | 113 |
| 2026-04 | 1 | 72 | 9 | 81 |
| 2026-05 | 3 | 113 | 6 | 108 |
| 2026-06 | 7 | 196 | 23 | 164 |
| 2026-07 | 9 | 154 | 18 | 227 |
| 2026-08 | 0 | 40 | 5 | 36 |

## 2. Table 1 전략 요소 × 단계 (ax_core 기준 출현율)

논문 Table 1은 단계가 올라갈수록 (1) 디지털 자원이 자산→민첩성·네트워킹→빅데이터 분석 역량으로 누적되고, (2) 조직이 표준 위계→분리된 애자일 유닛→내재화된 유연 조직으로 이동하며, (3) 성장전략이 플랫폼 기반으로 확장되고, (4) 지표가 전통 KPI→디지털 KPI로 옮겨간다고 본다. 코퍼스에서 그 패턴이 실제로 관측되는지 대조한 표다.

| 요소 | S1 | S2 | S3 |
|---|---:|---:|---:|
| **(1) 디지털 자원** | | | |
| res_asset | 8% | 6% | 11% |
| res_agility | 12% | 11% | 21% |
| res_networking | 29% | 27% | 40% |
| res_bigdata | 15% | 16% | 20% |
| **(2) 조직구조** | | | |
| org_hierarchy | 4% | 7% | 14% |
| org_separate_unit | 0% | 3% | 5% |
| org_embedded | 0% | 6% | 14% |
| **(3) 성장전략** | | | |
| growth_penetration | 2% | 3% | 14% |
| growth_cocreation | 4% | 5% | 8% |
| growth_diversification | 2% | 5% | 17% |
| **(4) 지표** | | | |
| kpi_traditional | 21% | 19% | 30% |
| kpi_digital | 8% | 14% | 25% |

## 3. S3 digital transformation(디지털 전환) — 사례 66건 / 39개 회사·채널

회사(채널)별로 단계 신호가 강한 순으로 최대 3건씩. 근거 문장은 **행동 동사가 든 문장**만 뽑았다(일반론 배제). 전량은 `analysis/verhoef_stages.csv` 참조.

### McKinsey & Company (5건 · 컨설팅·전략 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | a massive number of companies are going through some sort of digital transformation just about 90% of them according to McKenzie research all with varying levels of success it is show me the money time for digital transformations to succeed in a digital transformation it needs to be a CEO agenda ite… | 4 | [영상](https://www.youtube.com/watch?v=eR0Vtsp9YAM) · [script](../transcripts/2026-07-18/What_really_works_when_it_comes_to_digital_and_AI_transforma__eR0Vtsp9YAM.md) |
| 2026-07 | anti_washing | 제이슨, AI가 신규 사업 구축에 도움이 될 수 있는 다른 영역이 있을까요 ? | 3 | [영상](https://www.youtube.com/watch?v=kzAjzKCZAXs) · [script](../transcripts/channels/McKinsey_&_Company/The_Serial_Builder_Advantage_Why_Repeat_Innovators_Win__kzAjzKCZAXs.md) |
| 2026-07 | neutral | 음, 저는 그러한 마찰 비용이 제거될 것이고, 하나의 서비스 제공업체가 모든 것을 조율하여 통합된 경험을 제공하는 비즈니스 모델이 등장할 것이라고 생각합니다. | 3 | [영상](https://www.youtube.com/watch?v=BHQyOFaARQI) · [script](../transcripts/channels/McKinsey_&_Company/Why_Most_Companies_Aren't_Seeing_Meaningful_Returns_from_AI__BHQyOFaARQI.md) |

### Siemens (4건 · 물리 AI·자율주행 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | washing | Like I said, our whole portfolio is there and we're seeing 4x year-over-year growth in marketplace uh procurement adoption uh from our customers. | 21 | [영상](https://www.youtube.com/watch?v=2xvZL44AoG0) · [script](../transcripts/channels/Siemens/Agentic_AI_in_Action_AWS_and_Siemens_Partnership_Driving_Ind__2xvZL44AoG0.md) |
| 2026-01 | neutral | 그래서 Seammens를 통해서도 Nvidia, AWS와 같은 기업들과 협력 관계를 맺고 있으며, 이러한 협력 관계는 모두에게 누적적인 이점을 가져다줄 수 있는 생태계 구축을 주도하고 있습니다. | 4 | [영상](https://www.youtube.com/watch?v=Syk6BjIM6qE) · [script](../transcripts/channels/Siemens/Agentic_AI_The_Next_Wave_of_Industrial_AI_Analyst_Insights_f__Syk6BjIM6qE.md) |
| 2026-02 | washing | We will also deploy a product there that we will bring to our Siemens Xcelerator marketplace in the summer, the Digital Twin Composer. | 3 | [영상](https://www.youtube.com/watch?v=BnLqYZQ2uCo) · [script](../transcripts/channels/Siemens/Roland_Busch_präsentiert_Siemens_Wachstumsstrategie_und_Indu__BnLqYZQ2uCo.md) |

### Telenor (4건 · 통신·주권·국가 · NO)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2021-02 | neutral | i'm so pleased to be here together with um uh you marcus lavik the ceo and i think you're the founder also of uh knight uh uh larry thank you for joining yeah sure thanks a lot for you know for having me i think when i'm thinking about very successful startups in norway and when i'm thinking about t… | 8 | [영상](https://www.youtube.com/watch?v=0mdPRkxm12U) · [script](../transcripts/channels/Telenor/Sigve_Brekke_discusses_the_Digitalisation_of_Industry_with_C__0mdPRkxm12U.md) |
| 2022-03 | anti_washing | iOS와 안드로이드 운영체제는 하드웨어 위에 구축된 운영체제이고, 수백만 명의 개발자들이 그 위에 앱을 개발할 수 있도록 마켓플레이스와 생태계를 조성합니다. | 5 | [영상](https://www.youtube.com/watch?v=fnk7ByPs13A) · [script](../transcripts/channels/Telenor/Sigve_Brekke_and_Erlend_Prestgard,_CEO_of_WG2_How_technologi__fnk7ByPs13A.md) |
| 2021-06 | anti_washing | what we really see now it's that digitalization is accelerating things happens much faster than even us uh thought about before the coffee situation and i'm here with uh with uh sventor holster and we are in very different businesses but there are actually also similarities we are both two global co… | 5 | [영상](https://www.youtube.com/watch?v=qaSx9CLqmPQ) · [script](../transcripts/channels/Telenor/Sigve_Brekke_and_Svein_Tore_Holsether_(CEO,_Yara)_on_how_bus__qaSx9CLqmPQ.md) |

### Weights & Biases (4건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-11 | anti_washing | 메라리에서 AI 기술을 활용하여 고객을 위한 마켓플레이스 경험을 혁신하고, 차세대 고객 경험을 구축하는 방법에 대해 말씀드리겠습니다. | 8 | [영상](https://www.youtube.com/watch?v=tEbLkgDCmzg) · [script](../transcripts/channels/Weights_&_Biases/How_GenAI_is_powering_the_next_generation_of_Mercari_Marketp__tEbLkgDCmzg.md) |
| 2025-12 | anti_washing | 너무 광범위하게 사용되고 있고, 시각화 및 기타 여러 가지 요소를 실제로 활용할 수 있는 제대로 된 비즈니스 모델이 없다는 것이 문제입니다 . | 3 | [영상](https://www.youtube.com/watch?v=vvvwWv5BK-s) · [script](../transcripts/channels/Weights_&_Biases/Are_Humanoid_Robots_Actually_Coming_to_Your_Home_Nikolaus,_R__vvvwWv5BK-s.md) |
| 2025-02 | anti_washing | 예를 들어, 저희의 고급 고객 중에는 400~500개 기업이 간단한 사용 사례로 시작해서 이제는 가격 책정 프로세스를 자동화하고, 마켓플레이스나 다른 곳에서 에이전트를 사용하여 가격을 조정하는 방식을 사용하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=Z2cy4CGfsbc) · [script](../transcripts/channels/Weights_&_Biases/The_rise_of_AI_agents_with_João_Moura_of_CrewAI__Z2cy4CGfsbc.md) |

### Snowflake (4건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | anti_washing | 그렇다면 AI를 활용하여 양면 시장을 구축하고, 이를 통해 강력한 경쟁 우위를 확보할 수 있다는 말씀이신가요? | 6 | [영상](https://www.youtube.com/watch?v=-HWNc-Hd90U) · [script](../transcripts/channels/Snowflake/The_AI_Blueprint_for_the_Next_Decade_BUILD_2025_Luminary_Con__-HWNc-Hd90U.md) |
| 2026-01 | washing | [음악] Anomalo는 Snowflake Marketplace에서 이용 가능하며 , Snowflake 네이티브 앱으로 배포할 수 있으므로 Snowpark 컨테이너 서비스를 사용하여 제어 플레인과 데이터 플레인 모두 Snowflake 계정 내에 존재합니다 . | 3 | [영상](https://www.youtube.com/watch?v=gUaimG4dcQM) · [script](../transcripts/channels/Snowflake/How_to_Automate_Data_Quality_for_AI_and_Analytics_with_Snowf__gUaimG4dcQM.md) |
| 2026-06 | anti_washing | We built a global data network and marketplace where collaborating with external data is just as seamless as working with your own data. | 3 | [영상](https://www.youtube.com/watch?v=CtqKJV6gyGQ) · [script](../transcripts/channels/Snowflake/Snowflake_Summit_2026_Platform_Keynote__CtqKJV6gyGQ.md) |

### Unilever (4건 · 수요기업·기타 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 프리미엄 세그먼트는 미국과 인도에서 디지털 네이티브 방식으로 분해 노출을 확대합니다. | 4 | [영상](https://www.youtube.com/watch?v=m7GUG2IHJZY) · [script](../transcripts/channels/Unilever/Q4_and_full-year_2025_results_webcast_and_Q&A_audio_describe__m7GUG2IHJZY.md) |
| 2026-02 | anti_washing | 저희는 특히 미국과 인도 시장에서 프리미엄 부문, 디지털 네이티브 브랜드, 그리고 디지털 전환을 통한 제품 및 서비스 제공에 중점을 두고 뷰티, 웰빙, 퍼스널 케어 분야에 집중하고 있습니다 . | 3 | [영상](https://www.youtube.com/watch?v=G86AGZQwVVo) · [script](../transcripts/channels/Unilever/Q4_and_full-year_2025_results_webcast_and_Q&A_Unilever__G86AGZQwVVo.md) |
| 2024-11 | neutral | 하지만 우리는 그 변화를 위해 무엇이 필요한지 알고 있으며, 외부뿐만 아니라 인수한 디지털 네이티브 브랜드인 프레스티지 및 웰빙 포트폴리오에서 얻은 경험을 활용하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=r_BOLVAd0Kw) · [script](../transcripts/channels/Unilever/Investor_Event_2024_CEO_Presentation_Unilever__r_BOLVAd0Kw.md) |

### Palantir (3건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-02 | washing | [Music] all right I'm Chad walquist I'm an architect&nbsp; here at paler today I have Alex Scott Wald&nbsp;&nbsp; with me thanks for joining me great to be here&nbsp; thanks Chad so what do you do at paler how long&nbsp;&nbsp; you been here I lead our Telecom practice I've&nbsp; been at paler for th… | 2 | [영상](https://www.youtube.com/watch?v=1YLXeZHekZM) · [script](../transcripts/channels/Palantir/Chad_Interviews_Alex_How_Palantir_Powers_Operations_Across_T__1YLXeZHekZM.md) |
| 2025-08 | anti_washing | One&nbsp;&nbsp; less component of those AI agents running in the&nbsp; background is you can accelerate your build with&nbsp;&nbsp; a couple marketplace products. | 2 | [영상](https://www.youtube.com/watch?v=F57OKeI7JAU) · [script](../transcripts/channels/Palantir/Chad_&_Agathe_How_Palantir_Powers_AI_Automation_Across_Procu__F57OKeI7JAU.md) |
| 2025-04 | neutral | You're futureproofing your your business.&nbsp; I heard also multiple customers talking about&nbsp;&nbsp; marketplace and Palunteer DevOps and how they can&nbsp; then build on OSDK. | 2 | [영상](https://www.youtube.com/watch?v=QxZOHsp2mhU) · [script](../transcripts/channels/Palantir/Chad_Interviews_Zoë_Palantir_for_Builders__QxZOHsp2mhU.md) |

### Hugging Face (2건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-10 | neutral | 하지만 이제 가장 중요한 것은 AWS Marketplace에서 배포하는 방법을 살펴보는 것입니다. | 14 | [영상](https://www.youtube.com/watch?v=m6CGGPbwHCY) · [script](../transcripts/channels/Hugging_Face/🤗_Hugging_Cast_S2E5_-_Introducing_HUGS_-_Scale_your_AI_with___m6CGGPbwHCY.md) |
| 2025-11 | anti_washing | 그곳은 GPU 마켓플레이스이고, 모든 좋은 마켓플레이스가 그렇듯, 그들이 하려는 일은 시장의 유동성, 즉 GPU의 대체 가능성을 높이는 것입니다. | 7 | [영상](https://www.youtube.com/watch?v=aNCLqvTCxeg) · [script](../transcripts/channels/Hugging_Face/The_Power_of_Open_Source_Building_Giants_in_the_Open__aNCLqvTCxeg.md) |

### Schneider Electric (2건 · 인프라·칩·전력 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | neutral | 제품 혁신, 즉 순환 경제에 관한 유명한 3A를 활용하는 것은 더 쉽지만, 결국 순환 경제를 가속화하는 것은 비즈니스 모델의 문제라는 것을 알 수 있습니다. | 9 | [영상](https://www.youtube.com/watch?v=WX_3IjhXlvg) · [script](../transcripts/channels/Schneider_Electric/Episode_5-_What_is_next_for_circularity_Schneider_Electric__WX_3IjhXlvg.md) |
| 2026-05 | neutral | 순환 경제와 관련해서는 주로 신제품 디자인, 시장 진출 전략, 비즈니스 모델 개발에 집중하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=Y11nv7bWc00) · [script](../transcripts/channels/Schneider_Electric/Episode_4-_How_do_we_make_circularity_practical_Schneider_El__Y11nv7bWc00.md) |

### Google Developers (2건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | anti_washing | 그리고 이러한 새로운 비즈니스 모델 덕분에 우리는 인프라와 연구 개발에 지속적으로 투자하고 모든 사용자를 위해 미친 듯이 혁신할 수 있습니다. | 7 | [영상](https://www.youtube.com/watch?v=5OR4c87Xt-E) · [script](../transcripts/channels/Google_Developers/Gemini_in_Chrome_Your_agentic_browsing_assistant__5OR4c87Xt-E.md) |
| 2026-06 | neutral | 네, 인공지능을 얼마나 적극적으로 활용할지 말지 균형을 맞추는 데 있어서 가장 큰 긴장 요소 중 하나는 바로 말씀하신 것처럼 플랫폼 전환기에 접어든 지금, 사람들이 '이 시기에 누구에게 투자해야 할까 ?'라는 고민을 하고 있다는 점인 것 같습니다. | 4 | [영상](https://www.youtube.com/watch?v=YvVsdZL2ogY) · [script](../transcripts/channels/Google_Developers/Sameer_Samat_on_Android_17_and_the_Future_of_Intelligent_Com__YvVsdZL2ogY.md) |

### Microsoft (2건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-12 | washing | For us, we are a business model that has been built on the billable hour, where people monetize their efforts. | 5 | [영상](https://www.youtube.com/watch?v=ilaDQLa1Lrk) · [script](../transcripts/channels/Microsoft/Is_Agentic_AI_upending_the_corporate_ladder_EY's_Global_Cons__ilaDQLa1Lrk.md) |
| 2026-06 | anti_washing | And as a platform company, our job and our commitment is to keep you developers building at the absolute frontier. | 2 | [영상](https://www.youtube.com/watch?v=OvLIae4HCeM) · [script](../transcripts/channels/Microsoft/Microsoft_AI_CEO_unveils_7_new_AI_models_Mustafa_Suleyman_at__OvLIae4HCeM.md) |

### Salesforce (2건 · 엔터프라이즈 앱 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | washing | 그럼 데모를 통해 Engine 팀이 Slackbot과 Slack 마켓플레이스의 최신 기능을 어떻게 활용할 수 있는지 예시를 살펴보겠습니다 . | 4 | [영상](https://www.youtube.com/watch?v=vYUqOU-QV-o) · [script](../transcripts/channels/Salesforce/Introducing..._the_NEW_Slack!__vYUqOU-QV-o.md) |
| 2026-07 | neutral | Elevance Health가 Salesforce와 AWS Marketplace를 도입함으로써 현재 음악 관련 투자의 위험을 줄이는 동시에 미래 혁신을 위한 유연성을 확보하게 되었습니다 . | 3 | [영상](https://www.youtube.com/watch?v=qflNfjfZ_fs) · [script](../transcripts/channels/Salesforce/Elevance_Health_Improves_Member_Care_with_Salesforce_and_AWS__qflNfjfZ_fs.md) |

### Arm (2건 · 인프라·칩·전력 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | anti_washing | 사진에서 보시는 것처럼 저희는 GitHub의 Eclipse Ply에서 소스 코드를 공개적으로 제공하고 있으며, AWS 마켓플레이스에도 등록되어 있으므로 누구나 지금 바로 사용해보고 통합해 볼 수 있습니다. | 4 | [영상](https://www.youtube.com/watch?v=NjI6mujXlb0) · [script](../transcripts/channels/Arm/Inside_SOAFEE_Blueprint_roundtable__NjI6mujXlb0.md) |
| 2026-06 | neutral | 우리는 소프트웨어 생태계 구축에 많은 시간을 투자했습니다 . | 2 | [영상](https://www.youtube.com/watch?v=M_7MUDwMUvI) · [script](../transcripts/channels/Arm/Arm_Viewpoints_The_Arm_AGI_CPU_launch_and_future_of_AI_infra__M_7MUDwMUvI.md) |

### AWS Developers (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-09 | neutral | 하지만 다른 공급업체의 소규모 신흥 모델을 시험해보고 싶은 개발자라면 아마존 베드락 마켓플레이스를 통해 현재 업계를 선도하는 모델들과 더불어 100개 이상의 인기 있는 전문 기반 모델을 찾아보고 테스트하고 사용할 수 있습니다 . | 9 | [영상](https://www.youtube.com/watch?v=e36xut_NGWg) · [script](../transcripts/channels/AWS_Developers/Mistral_AI_Models_on_Amazon_Bedrock_When_to_Use_Pixtral_Larg__e36xut_NGWg.md) |

### Nokia (1건 · 통신·주권·국가 · FI)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 우리는 AI RAN이 활용도, 새로운 비즈니스 모델, 그리고 효율성을 모두 제공할 수 있도록 노력할 것이며, 실제로 그렇게 할 것입니다. | 7 | [영상](https://www.youtube.com/watch?v=O8WLc1_3EHI) · [script](../transcripts/channels/Nokia/Nokia,_Elisa_&_NVIDIA_Accelerating_AI-RAN_from_concept_to_co__O8WLc1_3EHI.md) |

### Nissan (1건 · 물리 AI·자율주행 · JP)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2023-09 | washing | 자기소개에서 2년 전까지 이케아에 계셨다고 말씀하셨는데, 이케아는 순환 경제를 위한 다양한 노력을 기울여 회수 프로그램을 포함한 순환 비즈니스 모델을 개발해 왔습니다. | 6 | [영상](https://www.youtube.com/watch?v=lX2NDGB6AB4) · [script](../transcripts/channels/Nissan/Accelerating_toward_a_circular_economy_–_from_idea_to_action__lX2NDGB6AB4.md) |

### [EN] VlogMe AI (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | My clear take is that the strategic adoption of AI agents will redefine business operations, driving efficiency and innovation while creating new opportunities for workers. | 5 | [영상](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) · [script](../transcripts/2026-08-03/The_Business_Impact_of_AI_Agents_Use_Cases,_ROI,_and_Future-__vfQpQ2PwoEQ.md) |

### The Next New Thing (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | washing | 그렇게 하면 지속적으로 서비스를 제공할 수 있고, 더 광범위한 마진 모델보다는 안정적인 수익 모델을 구축할 수 있기 때문입니다 . | 5 | [영상](https://www.youtube.com/watch?v=2CmZ_6ji5Jk) · [script](../transcripts/2026-07-30/Why_is_Morning_Brew’s_founder_selling_“AI_Transformation”__2CmZ_6ji5Jk.md) |

### Boston Consulting Group (1건 · 컨설팅·전략)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그리고 비즈니스 모델 관점에서 그러한 적응성을 어떻게 구축하는지 항상 궁금합니다. | 5 | [영상](https://www.youtube.com/watch?v=c9-0LUYKwhI) · [script](../transcripts/channels/Boston_Consulting_Group/Lead_with_Purpose,_Adapt_with_Strategy_Phillip_Benedetti_(Co__c9-0LUYKwhI.md) |

### Meta Developers (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | neutral | 단순히 MCP 도구뿐만 아니라 CLI 도구, 호스팅된 MCP 도구 등을 출시하여 마켓플레이스나 관련 지식에 접근할 수 있도록 함으로써 기존 개발 환경을 더욱 강력하고 접근하기 쉽게 만들려고 합니다. | 4 | [영상](https://www.youtube.com/watch?v=iz7sR5nh_X8) · [script](../transcripts/channels/Meta_Developers/VR_401_Accelerating_Quest_Development_with_Agentic_Workflows__iz7sR5nh_X8.md) |

### Zapier (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-01 | anti_washing | And here's why I think it's really important for us to be an AI first company because it will make uh, you know, all of us be able to spend more time in our zone of genius of creation versus just running day-to-day stuff that can be automated away. | 4 | [영상](https://www.youtube.com/watch?v=HxortsDnCm8) · [script](../transcripts/channels/Zapier/From_First_Startup_to_AI-Powered_Scale_Wes_Schroll_on_Buildi__HxortsDnCm8.md) |

### Philips (1건 · 수요기업·기타 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | Yeah, when you think about um kind of trust, I think I think of it from a um a perspective of the co-creation and co-inovation is really going to drive the adoption at scale. | 4 | [영상](https://www.youtube.com/watch?v=_aAOELqwFJc) · [script](../transcripts/channels/Philips/Building_AI_Doctors_Can_Trust_A_Physician’s_Perspective_on_A___aAOELqwFJc.md) |

### Weaviate (1건 · 데이터·컨텍스트·거버넌스 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-01 | anti_washing | hey everyone thank you so much for watching another episode of the wva podcast I'm super excited to welcome arvine kaju arvine is a principal software engineer at Morning Star where he's leading the effort behind the Morning Star intelligence engine firstly I want to give a huge thank you to our sal… | 3 | [영상](https://www.youtube.com/watch?v=TWPR_CmDSFM) · [script](../transcripts/channels/Weaviate/Morningstar_Intelligence_Engine_with_Aravind_Kesiraju_-_Weav__TWPR_CmDSFM.md) |

### SAP (1건 · 엔터프라이즈 앱 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 하지만 아시다시피 에너지 전환이 진행됨에 따라 우리는 다른 비즈니스 모델을 모색하고 있으며, 다양한 결정을 내려야 합니다 . | 3 | [영상](https://www.youtube.com/watch?v=WpDHkeHIezc) · [script](../transcripts/channels/SAP/Customer_Success_Keynote_Connected_to_Win_From_Moment_to_Mom__WpDHkeHIezc.md) |

### AI:ROI Conversations with Section (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | So the bubble will burst and everybody will all the you know it'll be all this I told you so stuff about the these models don't work and they're just prediction machines and these LLM have not scaled and all that stuff and the business models are broken and you know it's a shell game. | 3 | [영상](https://www.youtube.com/watch?v=20lqu-d4cxc) · [script](../transcripts/2026-08-03/Closing_the_Enterprise_AI_ROI_Gap__20lqu-d4cxc.md) |

### IT조선 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서이 에이전트 빌더에서 만든 에이전트 또는 서드 파티에 있는 에이전트 이미 만들어져 있어서 사회에서 돌고 있는 에이전트들도 전체 어 회사 관점에서는 통합적인 거버스를 가져가기 위해서 사내에서 만든 에이전트, 사회에서 만들어진 에이전트를 마켓플레이스에 이제 등록하는 것부터 저희는 진행을 합니다. | 3 | [영상](https://www.youtube.com/watch?v=mHbsngztlHw) · [script](../transcripts/2026-07-21/[AI&CLOUD2026]_세션1_AI-Native_기업으로의_전환_방안_및_사례_삼성SDS_신계영_AX센터__mHbsngztlHw.md) |

### Huawei (1건 · 인프라·칩·전력 · CN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-09 | neutral | 어떤 기술이든 찾을 수 있고, 어떤 서비스든 고객에게 제공할 수 있지만, 그것을 비즈니스 모델과 프로세스에 통합하는 것은 상당히 어렵습니다. | 3 | [영상](https://www.youtube.com/watch?v=YOxwp5bzZvk) · [script](../transcripts/channels/Huawei/Smart_Retailer_DeFacto_is_Leading_Fashion's_Phygital_Future__YOxwp5bzZvk.md) |

### 메타코드M (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그리고 효율화 그리고 고객 경험 및 비즈니스 임팩트 등 결국에는 영향도 있는 부분들을 기술단위뿐만 아니라 회사의 사업 전략이나 비즈니스 모델이나 회사 변화 관리 측면에서 AI AX를 도입하고 고민하고 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=ErviFf8I6K4) · [script](../transcripts/2026-07-18/In_the_era_of_AI_transformation_(AX),_we'll_teach_you_everyt__ErviFf8I6K4.md) |

### AWS Events (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 여기에는 컴퓨팅, 스토리지, 데이터베이스, 분석, 네트워킹, 머신 러닝 및 인공 지능, 개발자 도구, 보안 서비스, 엔터프라이즈 애플리케이션, 컨테이너, 클라우드 재무 관리 및 AWS 마켓플레이스가 포함됩니다. | 3 | [영상](https://www.youtube.com/watch?v=GbitrLroyMU) · [script](../transcripts/channels/AWS_Events/AWS_European_Sovereign_Cloud_–_Explained_AWS_Events__GbitrLroyMU.md) |

### NVIDIA Developer (1건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | anti_washing | 그래서 오픈 소스와 함께 또는 오픈 소스를 기반으로 구축할 수 있는 비즈니스 모델은 솔루션이 어떻게 사용되는지에 따라 달라집니다. | 3 | [영상](https://www.youtube.com/watch?v=43mHY4HA0lo) · [script](../transcripts/channels/NVIDIA_Developer/Accelerate_AI_through_Open_Source_Inference_NVIDIA_GTC__43mHY4HA0lo.md) |

### Oracle (1건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그렇게 하면 실제로 파괴적 혁신을 확대할 수 있는 특정 지역을 대상으로 할 수 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=G6PZCdNSl68) · [script](../transcripts/channels/Oracle/AI_Changes_Everything_Using_AI_to_Help_Prevent_Human_Traffic__G6PZCdNSl68.md) |

### 삼성SDS and KASMO 인공지능혁신추진단 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 어, 일단 그 이분은 이제 제조 산업에서 데이터 생태계 구축을 하는 일을 하고 계신 거 같고 이제 아까 말씀하셨던 그 현장 인터뷰 이야기도 지금 좀 나오는 거 같아요. | 3 | [영상](https://www.youtube.com/watch?v=iAbE9YXnbqA) · [script](../transcripts/2026-07-18/제조업_AX의_골든_타임_⏰_중요한_것은_AI_도입보다_이것!_📢_IT슈다_EP._제조__iAbE9YXnbqA.md) |

### IQVIA (1건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | neutral | 물론 그 기간 동안 많은 것이 바뀌었고, 이번 최신 연구는 비즈니스 모델, 증거 요건, 수익 기회, 현재 상황, 앞으로의 전망, 음악, 그리고 개발자, 정책 입안자, 지불자, 제공자, 환자에게 미치는 영향에 초점을 맞추고 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=WaNTDsbrKFo) · [script](../transcripts/channels/IQVIA/Research_Brief_Digital_Health_Trends_2025_The_IQVIA_Institut__WaNTDsbrKFo.md) |

### Orange (1건 · 통신·주권·국가 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | anti_washing | 만약 그 사실을 무시한다면, 전혀 말이 안 되는 것에 기반한 비즈니스 모델을 구축하는 것이고, 몇 달 후에는 새로운 데이터 포인트로 인해 비즈니스 모델이 완전히 재설정될 것입니다. | 3 | [영상](https://www.youtube.com/watch?v=69tvTh7axU0) · [script](../transcripts/channels/Orange/Science,_Innovation_and_Technology_The_vision_of_Bruno_Zerbi__69tvTh7axU0.md) |

### Upstage (1건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-12 | anti_washing | I think that there's a significant uh degree of manual labor that goes into the extraction of data just purely in the extraction of uh unstructured information from incoming sources uh whether those are brokers or other third party sources of data that are really important in the underwriting decisi… | 2 | [영상](https://www.youtube.com/watch?v=ei0lhXOYiI0) · [script](../transcripts/channels/Upstage/Fireside_Chat_with_Upstage_How_Tricura_Reimagines_Underwriti__ei0lhXOYiI0.md) |

### Accenture (1건 · 엔터프라이즈 앱 · IE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-01 | anti_washing | 단순히 새로운 센서와 기술을 적용하여 새로운 제품을 만드는 것을 넘어, 서비스 관리와 관련된 완전히 새로운 비즈니스 모델까지 구상하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=Ba2KXHdbjR0) · [script](../transcripts/channels/Accenture/CES_2026_-_Scaling_agentic_AI_to_achieve_breakthrough_transf__Ba2KXHdbjR0.md) |

### Intel (1건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-05 | neutral | I was asked a year ago to take on this role as the chief AI officer, and the reason why is because they wanted the visibility and responsibility, much like I've driven in security, to take that same motion in AI, creating a structure that ensures that we're doing the right things with our products a… | 2 | [영상](https://www.youtube.com/watch?v=Ojz9U4ao3go) · [script](../transcripts/channels/Intel/From_Smart_Devices_to_Supply_Chain_Lenovo's_Blueprint_for_Tr__Ojz9U4ao3go.md) |

### Meta (1건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2021-10 | anti_washing | 이거 완전 멋지다 이것 좀 봐 "NFT &amp; 가상 상품" 자선 경매 중이네 근사하다 뒤풀이에 가서 다른 팬들을 만나볼 수 있죠 제일 좋아하는 노래의 새 버전도 들어보고요 막 출시된 상품을 구경할 수도 있습니다 이거 맘에 드네 꼭 사야겠는걸 메타버스는 우리가 소통할 수 있는 세계에 새로운 레이어를 더함으로써 더욱 풍부한 경험을 선사합니다 크리에이터와 예술가는 청중과 새롭게 만나 소통하고 그들과 경험을 공유할 수 있게 되죠 그런 경험을 위해서는 개발되어야 할 기술이 많지만 이런 기술 중 일부는 바로 지금 Spark AR에서 작업 … | 2 | [영상](https://www.youtube.com/watch?v=Uvufun6xer8) · [script](../transcripts/channels/Meta/The_Metaverse_and_How_We'll_Build_It_Together_--_Connect_202__Uvufun6xer8.md) |

### kakao tech (1건 · 수요기업·기타 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 시장의 니지에 따라 데이터 사이언티스트 분들께서 연구 개발해 주신 여러 AI가 서비스화 수준을 밟게 됩니다. | 2 | [영상](https://www.youtube.com/watch?v=TSGPpuM6ffM) · [script](../transcripts/channels/kakao_tech/[ifkakao2021]_DFerence,_클라우드_기반_AI_서빙_플랫폼__TSGPpuM6ffM.md) |


## 4. S2 digitalization(디지털화) — 사례 836건 / 132개 회사·채널

회사(채널)별로 단계 신호가 강한 순으로 최대 3건씩. 근거 문장은 **행동 동사가 든 문장**만 뽑았다(일반론 배제). 전량은 `analysis/verhoef_stages.csv` 참조.

### Zapier (82건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | anti_washing | 주택 서비스 업계에서는 라이언 블랙번이 챗봇을 개발했는데, 이 챗봇은 첫 해에 고객사에게 13만 4천 달러 이상의 매출을 창출했습니다 . | 138 | [영상](https://www.youtube.com/watch?v=pGjirCLK9qE) · [script](../transcripts/channels/Zapier/Zapier_AI_Showcase_50_Million_Tasks_Delegated_(The_Best_Use___pGjirCLK9qE.md) |
| 2026-05 | anti_washing | 저희는 알림 및 승인에는 Slack을, 문서 저장에는 Google Drive를 , 지급 계정 관리에는 Zip을 , Claude, ChatgPT, Zapier MCP, 그리고 Zapier 내부에 자체 개발한 AI 단계를 사용하며 , 모든 도구는 워크플로에 따라 달라집니다. | 55 | [영상](https://www.youtube.com/watch?v=CxrrXKFn6cg) · [script](../transcripts/channels/Zapier/Steal_Zapier's_AI_Playbook_for_Accounting_How_8_People_Run_a__CxrrXKFn6cg.md) |
| 2026-06 | anti_washing | 그리고 실제로 한 달에 1만 번 실행될 워크플로에 적용할 때는 효율성과 비용을 최적화하고 싶을 것입니다. | 43 | [영상](https://www.youtube.com/watch?v=Zg3IU1cA0vU) · [script](../transcripts/channels/Zapier/Zapier_AI_Benchmark_How_to_choose_the_right_AI_model_for_you__Zg3IU1cA0vU.md) |

### Google Cloud Tech (40건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 이곳에서 저는 호텔 예약용 AI 챗봇 또는 예약 도우미를 개발하고 있습니다 . | 33 | [영상](https://www.youtube.com/watch?v=tQGalTBL1Ek) · [script](../transcripts/channels/Google_Cloud_Tech/Agent_development_and_AgentOps_with_BigQuery,_ADK,_and_MCP__tQGalTBL1Ek.md) |
| 2026-06 | neutral | 이곳에서 저는 호텔 예약용 AI 챗봇 또는 도우미를 개발하고 있습니다 . | 31 | [영상](https://www.youtube.com/watch?v=AKGV5wPQdd8) · [script](../transcripts/channels/Google_Cloud_Tech/Agent_development_and_AgentOps_with_BigQuery,_ADK,_and_MCP__AKGV5wPQdd8.md) |
| 2026-06 | neutral | 이러한 도구들은 기술 전문가 와 비기술 전문가 모두가 AI 기반 워크플로우를 구축하고 관리하는 데 널리 사용됩니다. | 31 | [영상](https://www.youtube.com/watch?v=zthWHEU3Y7M) · [script](../transcripts/channels/Google_Cloud_Tech/Build_AI_agents_on_Cloud_Run__zthWHEU3Y7M.md) |

### Weights & Biases (38건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | neutral | 지원 문제를 해결하기 위해 단 한 명의 상담원이나 심지어 단 하나의 AI 에이전트에만 전적으로 의존하는 대신 , 다중 에이전트 컨택 센터는 서로 협력하고 기존 비즈니스 애플리케이션 과 원활하게 통합될 수 있는 여러 전문 상담원을 활용합니다 . | 27 | [영상](https://www.youtube.com/watch?v=MjqHVfmKEoM) · [script](../transcripts/channels/Weights_&_Biases/Build_and_monitor_multi-agent_contact_centers_using_Weights___MjqHVfmKEoM.md) |
| 2025-04 | anti_washing | Weave는 에이전트 개발 워크플로의 모든 단계를 지원하도록 특별히 설계되었습니다 . | 21 | [영상](https://www.youtube.com/watch?v=sJNjw6U2Tvg) · [script](../transcripts/channels/Weights_&_Biases/Building_agentic_AI_applications_with_W&B_Weave__sJNjw6U2Tvg.md) |
| 2025-12 | anti_washing | 인공지능 개발 워크플로에서 늘 그렇듯이, 반복과 평가가 핵심입니다. | 20 | [영상](https://www.youtube.com/watch?v=q4YnO0MBaeI) · [script](../transcripts/channels/Weights_&_Biases/Build_reliable_AI_agents_using_W&B_Training__q4YnO0MBaeI.md) |

### Salesforce (34건 · 엔터프라이즈 앱 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 즉, 기존 워크플로에 데이터를 가져와 코딩 에이전트에 인사이트를 다시 적용함으로써 이전보다 훨씬 더 효율적으로 에이전트를 구축하고 오케스트레이션할 수 있다는 의미입니다 . | 49 | [영상](https://www.youtube.com/watch?v=7a3TnSO0nps) · [script](../transcripts/channels/Salesforce/Welcome_to_Agentforce_Demo_Day!__7a3TnSO0nps.md) |
| 2025-12 | anti_washing | 그리고 이번에 새롭게 출시된 Agent Force 360을 통해 상담원과 사람이 함께 고객, 직원, 운영 및 상담원과 완전히 새로운 방식으로 소통할 수 있도록 지원합니다. | 45 | [영상](https://www.youtube.com/watch?v=1HwD8Nk56AU) · [script](../transcripts/channels/Salesforce/See_What's_New_in_Agentforce_World_Tour_NYC_2025_Salesforce__1HwD8Nk56AU.md) |
| 2026-04 | washing | 즉, 인간과 AI 에이전트가 모든 워크플로우에서 협력하여 더 나은 고객 경험을 구축하고, 이전에는 볼 수 없었던 생산성 향상을 위한 프로세스를 구축하는 모델로 나아가야 합니다 . | 42 | [영상](https://www.youtube.com/watch?v=aKsZdyyzcfU) · [script](../transcripts/channels/Salesforce/Build_the_Future_with_Salesforce_Headless_360_TDX_2026_Keyno__aKsZdyyzcfU.md) |

### SAP (29건 · 엔터프라이즈 앱 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 우리는 AI 기반과 비즈니스 데이터 클라우드 및 비즈니스 기술 플랫폼을 통합하여 ERP 시스템에 저장된 50년의 비즈니스 노하우를 LLM(법률 전문가)과 결합하고 있습니다. | 44 | [영상](https://www.youtube.com/watch?v=9aa-etRsaLU) · [script](../transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Orlando___9aa-etRsaLU.md) |
| 2026-05 | anti_washing | n8n is a workflow automation platform that orchestrates AI agents, business process integrations across the whole enterprise stack. | 23 | [영상](https://www.youtube.com/watch?v=CocpyxAizwE) · [script](../transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Madrid_2__CocpyxAizwE.md) |
| 2026-05 | anti_washing | AI와 에이전트 기반 워크플로가 점점 더 보편화됨에 따라 통합 또한 진화하고 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=ZzBZWAbinzE) · [script](../transcripts/channels/SAP/The_Future_of_Integration_with_SAP_BTP_feat._Dr._Achim_Krais__ZzBZWAbinzE.md) |

### NVIDIA Developer (28건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-06 | neutral | 오늘은 엔비디아 Nim을 사용하여 디지털 휴먼 및 AI 디자인 파이프라인과 같은 고급 AI 워크플로우를 구축하는 방법에 대해 알려드리겠습니다. | 26 | [영상](https://www.youtube.com/watch?v=pJ12IMuWlAs) · [script](../transcripts/channels/NVIDIA_Developer/Digital_Humans_and_AI_Design_with_NVIDIA_NIM_on_RTX_PCs_Micr__pJ12IMuWlAs.md) |
| 2025-03 | neutral | 함수 안에서 다른 함수를 호출할 수 있고, 임의로 중첩된 에이전트를 구현하여 상당히 정교한 워크플로를 구축할 수 있습니다. | 18 | [영상](https://www.youtube.com/watch?v=H65OluZaiZQ) · [script](../transcripts/channels/NVIDIA_Developer/How_to_Develop_Teams_of_AI_Agents_with_NVIDIA_NeMo_Agent_Ope__H65OluZaiZQ.md) |
| 2025-04 | anti_washing | 다음으로는 인권 보호를 위한 이동성 또는 지역적 조작을 구축할 수 있도록 하는 몇 가지 워크플로우를 공유하겠습니다 . | 13 | [영상](https://www.youtube.com/watch?v=Oyon1QDpU6g) · [script](../transcripts/channels/NVIDIA_Developer/An_Introduction_to_Building_Humanoid_Robots_NVIDIA_GTC_2025__Oyon1QDpU6g.md) |

### McKinsey & Company (27건 · 컨설팅·전략 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | neutral | 하지만 제가 그들이 하는 일과 그들이 보여주는 영향에 대해 좀 더 강조해 보자면, 저희와 협력하는 은행 중 한 곳은 콜센터에 Agentic을 도입하는 과정을 진행 중입니다. | 18 | [영상](https://www.youtube.com/watch?v=ieGq5bdmRcI) · [script](../transcripts/channels/McKinsey_&_Company/Move_First_or_Fall_Behind_How_AI_Is_Rewriting_the_Rules_of_B__ieGq5bdmRcI.md) |
| 2025-11 | anti_washing | 기업들이 생산성 향상을 위해 인공지능과 같은 기술을 활용하려 함에 따라 최고운영책임자(COO)의 역할이 점점 더 중요해지고 있습니다 . | 14 | [영상](https://www.youtube.com/watch?v=O-aUZqfcLKg) · [script](../transcripts/channels/McKinsey_&_Company/Productivity_first_AI_and_the_COO_agenda__O-aUZqfcLKg.md) |
| 2026-03 | anti_washing | 고객 서비스 접수 업무를 에이전트형 기술로 대체하고 있습니다. | 13 | [영상](https://www.youtube.com/watch?v=Ne4HnJEjCSI) · [script](../transcripts/channels/McKinsey_&_Company/Trust_In_the_Age_of_Agents__Ne4HnJEjCSI.md) |

### Pinecone (25건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | anti_washing | 음, 그러니까 그런 신뢰할 수 있는 데이터를 워크플로에 통합할 수 있다는 거죠. | 30 | [영상](https://www.youtube.com/watch?v=Gcaygufjt6M) · [script](../transcripts/channels/Pinecone/Build_RAG_Workflows_in_Minutes_with_Pinecone_+_n8n__Gcaygufjt6M.md) |
| 2024-08 | anti_washing | 일단 답변을 만들어내면, 상담원에게 미리 작성된 답변을 제공하여 티켓 접수 즉시 응대할 수 있도록 하는 등 다양한 활용이 가능합니다. | 17 | [영상](https://www.youtube.com/watch?v=kuKBzkKDaQ0) · [script](../transcripts/channels/Pinecone/RAG_Brag_with_John_Wang_of_Assembled__kuKBzkKDaQ0.md) |
| 2023-08 | anti_washing | 이 회사는 개인 맞춤형 LLM을 구축해 주는데, 마치 챗봇처럼 작동합니다. | 16 | [영상](https://www.youtube.com/watch?v=8dhOyt1dhjg) · [script](../transcripts/channels/Pinecone/Launch_Sooner_An_integrated_AI_stack_for_faster_deployment__8dhOyt1dhjg.md) |

### Google Developers (25건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 자, 이제 안드로이드 개발을 위한 에이전트 기반 워크플로우에 대해 자세히 살펴보겠습니다 . | 25 | [영상](https://www.youtube.com/watch?v=eC7t22gDwWo) · [script](../transcripts/channels/Google_Developers/Developer_Keynote_(Google_IO_'26)_-_Audio_Described__eC7t22gDwWo.md) |
| 2026-03 | anti_washing | ADK 에이전트를 배포하는 전체 워크플로는 무엇입니까? | 19 | [영상](https://www.youtube.com/watch?v=jDCkirAz4-E) · [script](../transcripts/channels/Google_Developers/Prototype_to_Production_with_ADK__jDCkirAz4-E.md) |
| 2026-01 | neutral | Opal은 Google Labs에서 개발한 새로운 실험적인 도구로, 자연어 및 시각적 워크플로를 사용하여 몇 분 만에 연결된 AI 시스템을 구축하고 테스트할 수 있습니다. | 17 | [영상](https://www.youtube.com/watch?v=gphcuJu8iHo) · [script](../transcripts/channels/Google_Developers/How_to_Automate_PR_Summaries_with_Opal_AI__gphcuJu8iHo.md) |

### Weaviate (22건 · 데이터·컨텍스트·거버넌스 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-02 | neutral | 또한 다른 사람들이 에이전트를 구축하고 즉시 워크플로를 추가할 수 있도록 툴링도 제공하기 시작했습니다. | 37 | [영상](https://www.youtube.com/watch?v=MAE3I8O_w84) · [script](../transcripts/channels/Weaviate/Agent_Experience_with_Matt_Biilmann,_Sebastian_Witalec,_and___MAE3I8O_w84.md) |
| 2025-05 | anti_washing | 음, 그러니까, 네, 특히 상담원과 관련해서 흥미로운 점은, 특히 제품이나 고객 관점에서 볼 때, 기업들이 상담원 워크플로우가 더 오래 지속되는 것에 대해 대체로 괜찮다고 생각한다는 점입니다. | 18 | [영상](https://www.youtube.com/watch?v=I2jgU4waKFE) · [script](../transcripts/channels/Weaviate/Patronus_AI_with_Anand_Kannappan_-_Weaviate_Podcast_#122!__I2jgU4waKFE.md) |
| 2025-03 | anti_washing | 모든 것을 툴 호출로 정의하면 범용성이 높아져 워크플로우 에이전트, 채팅 에이전트 등 다양한 용도로 활용할 수 있습니다. | 15 | [영상](https://www.youtube.com/watch?v=JgBKaI6MNpQ) · [script](../transcripts/channels/Weaviate/Letta_AI_with_Sarah_Wooders_-_Weaviate_Podcast_#117!__JgBKaI6MNpQ.md) |

### Intel (22건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | anti_washing | 이러한 솔루션들은 대부분 챗봇 형태의 보조 모델을 중심으로 구축되어 있습니다. | 17 | [영상](https://www.youtube.com/watch?v=NgeYg6tyncs) · [script](../transcripts/channels/Intel/The_Age_of_With_Rethinking_Enterprise_Strategy_Through_Agent__NgeYg6tyncs.md) |
| 2025-07 | anti_washing | 하지만 에이전트의 강력한 기능과 모든 데이터 소스 에 연결할 수 있는 능력을 통해 워크플로를 진정으로 분석하고 "내 워크플로는 다른 어떤 것과도 비교할 수 없을 만큼 독특하며, 이를 해결하기 위해 AI를 매우 독창적인 방식으로 적용해야겠다"라고 말할 수 있게 됩니다 . | 15 | [영상](https://www.youtube.com/watch?v=6u9xF_V4ZtU) · [script](../transcripts/channels/Intel/AI_That_Works_How_Google_Cloud_Delivers_Impact_Intel__6u9xF_V4ZtU.md) |
| 2025-01 | anti_washing | 따라서 고객 또는 고객과 협력하는 입장에서 가장 큰 과제는 기존 워크플로에 AI를 통합하여 모든 기존 워크로드와 함께 작동하도록 함으로써 올바른 비즈니스 성과를 달성하는 동시에 파트너가 적절한 총소유비용(TCO)을 달성할 수 있도록 지원하는 것입니다. | 6 | [영상](https://www.youtube.com/watch?v=mrWTLjitaX4) · [script](../transcripts/channels/Intel/AI_at_the_Edge_Transforming_Industries_and_the_Workplace​_In__mrWTLjitaX4.md) |

### Databricks (20건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 그래서 저희 Databricks는 8 년 전부터 머신러닝 워크플로우 구축을 시작했습니다. | 25 | [영상](https://www.youtube.com/watch?v=NcHCkPMww7Q) · [script](../transcripts/channels/Databricks/Building_Trustworthy,_High-Quality_AI_Agents_with_MLflow__NcHCkPMww7Q.md) |
| 2025-12 | anti_washing | 규모와 기술이 생산성 향상을 가져온다고 생각하기 쉽지만, 실제로 일부 팀의 생산성이 약 4% 감소했다는 분석 결과가 나왔습니다. | 23 | [영상](https://www.youtube.com/watch?v=Vy5oNJgPdyQ) · [script](../transcripts/channels/Databricks/Unscripted_How_Banks_&_Insurers_Grow_with_Data,_AI_Agents_an__Vy5oNJgPdyQ.md) |
| 2026-05 | neutral | 3단계는 기본적으로 특수 워크플로우, 즉 요청을 분류하고 목적에 맞게 구축된 워크플로우로 라우팅하는 LLM(Level Management Module)을 사용하는 단계입니다. | 13 | [영상](https://www.youtube.com/watch?v=UrIybbk-aY4) · [script](../transcripts/channels/Databricks/AI_Agents_That_Remember_Building_Stateful_Systems_with_Lakeb__UrIybbk-aY4.md) |

### AWS Events (19건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서 지난 8개월에서 12개월 동안 우리가 목격한 가장 큰 변화 중 하나는 고객들이 이 기술을 시험적으로 사용하는 단계를 넘어, 고객 경험, 특히 셀프 서비스에 최신 AI 기술을 적용하는 것에 대해 이해하기 시작했다는 점입니다. | 92 | [영상](https://www.youtube.com/watch?v=O_Imo9L04mo) · [script](../transcripts/channels/AWS_Events/CCW_2026_How_Citizens_Bank_is_building_the_AI-native_custome__O_Imo9L04mo.md) |
| 2026-07 | neutral | 고객 입장에서는 도미니언 상담원의 평균 응답률(ASA)이 60% 감소한 것을 확인했죠 ? | 57 | [영상](https://www.youtube.com/watch?v=d2nUemwh30c) · [script](../transcripts/channels/AWS_Events/CCW_2026_Dominion_Energy’s_AI-Powered_Transformation_with_Am__d2nUemwh30c.md) |
| 2026-07 | neutral | 다른 기준도 있지만, 일단 고객님의 문의 사유가 실제로 비정상적인 운영과 관련된 것인지 확인하고 해당 절차로 안내해 드리면, 출시 이후 해당 절차를 거친 고객의 약 40%가 상담원 연결 없이 문제를 해결하고 나가는 것으로 나타났습니다. | 18 | [영상](https://www.youtube.com/watch?v=re3Nsk5H3CI) · [script](../transcripts/channels/AWS_Events/CCW_2026_United_Airlines_raises_the_bar_for_CX_with_Multimod__re3Nsk5H3CI.md) |

### Apple Developer (19건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 더 복잡한 워크플로를 구축할 수 있습니다. | 15 | [영상](https://www.youtube.com/watch?v=sbdA41c2o88) · [script](../transcripts/channels/Apple_Developer/WWDC26_Build,_deliver,_and_automate_with_Xcode_Cloud_Apple__sbdA41c2o88.md) |
| 2026-06 | neutral | 또는 iOS 또는 iPadOS 앱을 visionOS로 재컴파일하고 Xcode 설정에서 visionOS를 배포 대상으로 추가하면 됩니다 이 두 가지 경로 모두 간편한 방법을 제공해 경험을 visionOS로 가져올 수 있습니다 두 번째 경로는 공간 컴퓨팅을 위해 처음부터 설계된 앱을 위한 것입니다 이를 통해 경험이 사람들의 환경과 원활하게 융합되고 반응합니다 이 경우 두 가지 옵션이 있습니다 네이티브 프레임워크를 사용해 플랫폼을 개발할 수 있습니다 SwiftUI, RealityKit 등을 Reality Composer Pro와 같은 도… | 12 | [영상](https://www.youtube.com/watch?v=S_qt8iu_Ljw) · [script](../transcripts/channels/Apple_Developer/WWDC26_Build_next-generation_experiences_with_visionOS_27_Ap__S_qt8iu_Ljw.md) |
| 2026-06 | neutral | Device Hub가 개발 워크플로에 어떻게 맞아들어가는지 보여드릴 것입니다. | 7 | [영상](https://www.youtube.com/watch?v=a2N1qAJRFIk) · [script](../transcripts/channels/Apple_Developer/WWDC26_Get_the_most_out_of_Device_Hub_Apple__a2N1qAJRFIk.md) |

### IBM Technology (19건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 이러한 시스템은 API, 데이터베이스 및 비즈니스 워크플로와의 긴밀한 통합이 필요합니다. | 10 | [영상](https://www.youtube.com/watch?v=ZVPlLaehjLk) · [script](../transcripts/channels/IBM_Technology/Agentic_AI_Frameworks_Explained_Workflows,_Multi-Agent,_&_Pr__ZVPlLaehjLk.md) |
| 2026-06 | anti_washing | 이 패턴은 단일 이벤트가 종속성을 가진 다단계 워크플로를 트리거하는 모든 곳에서 적용됩니다. | 10 | [영상](https://www.youtube.com/watch?v=4Vg2aVtrX8k) · [script](../transcripts/channels/IBM_Technology/Building_AI_Agents_for_Real-World_Problems_&_Workflows__4Vg2aVtrX8k.md) |
| 2026-06 | anti_washing | "만약 내가 기존의 레거시 워크플로우에서 인건비를 20억 달러 절감했다고 가정해 보자. | 8 | [영상](https://www.youtube.com/watch?v=EKULOf_Cy0w) · [script](../transcripts/channels/IBM_Technology/The_future_of_software_engineering,_tokenmaxxing_and_AI_in_h__EKULOf_Cy0w.md) |

### AWS Developers (18건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 하지만 중요한 워크플로의 경우, 안정성 향상을 위해 그만한 가치가 있는 경우가 많습니다. | 19 | [영상](https://www.youtube.com/watch?v=5rwTCUFV4Ak) · [script](../transcripts/channels/AWS_Developers/Improve_Agent_Reliability_with_Strands_Steering__5rwTCUFV4Ak.md) |
| 2026-02 | anti_washing | 기존 백엔드와 통합하거나, 요청이 상담원에게 도달하기 전에 로직을 실행하거나, 상담원을 전혀 거치지 않는 엔드포인트를 추가해야 할 때 이 패턴이 적합합니다 . | 14 | [영상](https://www.youtube.com/watch?v=jI4AYvvA7ck) · [script](../transcripts/channels/AWS_Developers/We_Need_to_Talk_About_AI_Agent_Architectures__jI4AYvvA7ck.md) |
| 2026-07 | anti_washing | 그것들이 없다면, 시간이 지남에 따라 상담원의 실력이 향상되는지 아니면 악화되는지 실제로 알 수 없습니다. | 8 | [영상](https://www.youtube.com/watch?v=rDtcfG4aZV4) · [script](../transcripts/channels/AWS_Developers/Evaluating_Agents__rDtcfG4aZV4.md) |

### ServiceNow (17건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-09 | anti_washing | 작년 5월에 출시한 제품에는 지난 20 년간 IT, HR, 구매, CRM 등 다양한 분야에서 서비스 관리 사고를 처리하는 방식에 대한 모든 노하우를 바탕으로 구축된 수백 개의 즉시 사용 가능한 에이전트가 포함되어 있습니다. | 52 | [영상](https://www.youtube.com/watch?v=0Fmw61s8CKc) · [script](../transcripts/channels/ServiceNow/Michael_Park's_AI_Whiteboard_Masterclass__0Fmw61s8CKc.md) |
| 2026-05 | anti_washing | 우리는 이미 에이전트형 AI를 통해 30% 이상의 생산성 향상을 달성하고 있습니다 . | 46 | [영상](https://www.youtube.com/watch?v=jeo2V1w-Peg) · [script](../transcripts/channels/ServiceNow/Welcome_to_Agentic_Business_ServiceNow_Knowledge_2026_Openin__jeo2V1w-Peg.md) |
| 2026-05 | neutral | 그리고 데이터, AI, 워크플로 및 보안을 하나의 플랫폼에 통합하는 것은 ServiceNow뿐입니다. | 37 | [영상](https://www.youtube.com/watch?v=q8kaVEkTWho) · [script](../transcripts/channels/ServiceNow/The_Blueprint_for_Agentic_Business_ServiceNow_Knowledge_2026__q8kaVEkTWho.md) |

### Nokia (16건 · 통신·주권·국가 · FI)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 그러니까 기본적으로 자신에게 맞는 워크플로우를 찾아서 적용하면 됩니다. | 18 | [영상](https://www.youtube.com/watch?v=psGgcVsJirk) · [script](../transcripts/channels/Nokia/Nokia_Core_TV_series_#64Nokia_Cloud_Operations_Manager_Evo_S__psGgcVsJirk.md) |
| 2026-08 | neutral | 따라서 우리는 5분 이내에 9가지 제품을 배포할 수 있으며, 이는 Enkom Evo의 동적 역량과 Enkom Evo 워크플로의 다른 기능적 역량을 보여줍니다 . | 15 | [영상](https://www.youtube.com/watch?v=P1DoJN9K48Y) · [script](../transcripts/channels/Nokia/Nokia_Core_TV_series_#65_Nokia_Cloud_Operations_Manager_Evo___P1DoJN9K48Y.md) |
| 2026-07 | neutral | 이 에이전트들은 실시간으로 상관관계를 분석하고, 패턴을 파악하고, 고객 경험을 이해하며, 문제가 발생하기 전에 조치를 취함으로써 고객 경험을 개선할 것입니다. | 8 | [영상](https://www.youtube.com/watch?v=D_xxni9ZJYY) · [script](../transcripts/channels/Nokia/Networked_How_will_AI_transform_the_future_of_networks,_auto__D_xxni9ZJYY.md) |

### Replit (14건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-09 | neutral | 에이전트 기반 워크플로우를 구축해 본 경험이 있다면, 가장 어려운 점 중 하나는 각 단계를 디버깅하고 각 노드가 의도한 대로 제대로 작동하는지 확인하는 것임을 알 것입니다 . | 60 | [영상](https://www.youtube.com/watch?v=WI-mA0SEnRk) · [script](../transcripts/channels/Replit/Agent_3_Livestream_Building_with_the_community__WI-mA0SEnRk.md) |
| 2025-09 | washing | 다른 사람들은 에이전트를 워크플로 자동화 도구와 같다고 말하기도 합니다. | 16 | [영상](https://www.youtube.com/watch?v=4FxNXFOdt6w) · [script](../transcripts/channels/Replit/Replit_Agent_3_First_Look__4FxNXFOdt6w.md) |
| 2025-10 | neutral | 결론적으로, Replet의 가장 강력한 점은 사용자가 직접 맞춤형 애플리케이션과 워크플로우를 구축할 수 있도록 해준다는 것입니다. | 15 | [영상](https://www.youtube.com/watch?v=Aoj095r_288) · [script](../transcripts/channels/Replit/Custom_Sales_Tools_with_Replit_Your_Salesforce,_Your_Way__Aoj095r_288.md) |

### GitHub (14건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 저는 제 저장소에서 약 4분 정도 사용해 봤는데, 우선 AITO 워크플로우가 무엇인지 설명해 주시고, 사용자들이 오늘 바로 활용할 수 있는 실질적인 방법들을 보여주시면 정말 감사하겠습니다. | 42 | [영상](https://www.youtube.com/watch?v=XisVQoz5grw) · [script](../transcripts/channels/GitHub/How_to_use_agentic_workflows_for_your_repos_GitHub_Checkout__XisVQoz5grw.md) |
| 2026-04 | neutral | 브랜치에서 배포하거나 GitHub Actions 워크플로를 사용할 수 있습니다. | 11 | [영상](https://www.youtube.com/watch?v=b2r9Cdvssi0) · [script](../transcripts/channels/GitHub/Getting_started_with_GitHub_Pages_for_beginners_Tutorial__b2r9Cdvssi0.md) |
| 2026-05 | anti_washing | 이것은 헤드리스 키트에서 Copilot과 상호 작용할 수 있는 첫 번째 모드이며, 자동화 파이프라인에서 Copilot이 생성하는 출력을 워크플로에 삽입할 수 있다는 점을 고려하면 다양한 가능성을 생각해 볼 수 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=zS_40Tfl75w) · [script](../transcripts/channels/GitHub/Less_TODO_more_done_with_GitHub_Copilot_CLI__zS_40Tfl75w.md) |

### Qdrant (14건 · 데이터·컨텍스트·거버넌스 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 자동화 환경에서 Nitn을 사용하면 상담원을 사실상 수천 개의 서비스와 연결할 수 있으며, Nitn은 기업 수준의 상담원에게 적합한 다양한 기능을 제공합니다. | 18 | [영상](https://www.youtube.com/watch?v=EEXUuI6ZSu8) · [script](../transcripts/channels/Qdrant/Vector_Space_Meetup_2026_Highlights__EEXUuI6ZSu8.md) |
| 2025-08 | anti_washing | 이 영상이 끝날 때쯤이면, 적어도 저는 그렇게 되기를 진심으로 바랍니다만, 여러분은 법률 자료 검색 하이브리드 파이프라인을 처음부터 끝까지 직접 구축하고, 테스트하고, 심지어 법률 전문 챗봇에서 사용해 볼 수도 있을 것입니다. | 15 | [영상](https://www.youtube.com/watch?v=7LEhwjETnu4) · [script](../transcripts/channels/Qdrant/Hybrid_Search_in_Legal_AI_with_Qdrant_&_n8n__7LEhwjETnu4.md) |
| 2025-10 | neutral | 하나의 기능 에이전트와 하나의 워크플로우를 처음 부터 구축합니다. | 15 | [영상](https://www.youtube.com/watch?v=ytWskQWsAA4) · [script](../transcripts/channels/Qdrant/Qdrant_x_LlamaIndex_Advanced_RAG_Patters_and_Agent_Workflows__ytWskQWsAA4.md) |

### Siemens (13건 · 물리 AI·자율주행 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 물론 소규모 기업들이 에이전트를 구축하고 특정 시스템, 프로세스, 워크플로우를 최적화하는 것에 대한 이야기도 많이 나오고 있습니다. | 19 | [영상](https://www.youtube.com/watch?v=46KctH5TgSs) · [script](../transcripts/channels/Siemens/How_to_Scale_Industrial_AI_in_Real_Factory_Operations__46KctH5TgSs.md) |
| 2026-07 | anti_washing | 그리고 저희 Quanta 와 Techman은 디지털 연결 워크플로우를 도입하고 진정한 연결 제조를 실현하기 위한 파트너로 저희를 선택해 주셔서 정말 기쁩니다. | 11 | [영상](https://www.youtube.com/watch?v=1slvyDDaZKE) · [script](../transcripts/channels/Siemens/Connected_Manufacturing_With_Quanta_Computer_and_Techman_Rob__1slvyDDaZKE.md) |
| 2026-07 | anti_washing | 우리가 사는 세상에서는 챗봇을 통해 전력 공급을 개선하는 방법을 알 수는 없지만, 전력이 안정적이고 안전하게 공급되어야 하는 곳에서 그 해답을 찾을 수 있습니다. | 5 | [영상](https://www.youtube.com/watch?v=Eexy56SkqFs) · [script](../transcripts/channels/Siemens/From_Grid_Operations_to_Asset_Management_Deploying_AI_in_Ind__Eexy56SkqFs.md) |

### NVIDIA (13건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 저희는 에이전트를 사용하여 모든 입력을 분석하고, 연결된 데이터베이스와 관련 지식을 활용하여 해결하려는 문제를 파악하고 계획을 수립한 후, 다른 API를 호출하거나 워크플로를 실행하거나 환자, 의사, 간호사 등 사용자에게 응답을 제공하는 등의 조치를 취합니다. | 12 | [영상](https://www.youtube.com/watch?v=iWsKSxyfRIA) · [script](../transcripts/channels/NVIDIA/GTC_SJ_2026_The_AI_Native_Digital_Health_Stack_A_Developer's__iWsKSxyfRIA.md) |
| 2026-07 | neutral | 에이전트 기반 워크플로가 도입하기 시작한 모든 것, 그리고 우리가 일상적으로 수용하기 시작한 모든 것은 스토리지의 의미 자체를 바꾸고 있습니다. | 11 | [영상](https://www.youtube.com/watch?v=TY2EilHUR1c) · [script](../transcripts/channels/NVIDIA/Powering_Agentic_AI_with_AI-Ready_Data_Platforms_That_Turn_D__TY2EilHUR1c.md) |
| 2026-05 | neutral | 여러분은 LLM을 중심으로 다양한 구조와 워크플로우를 구축하게 될 것입니다 . | 10 | [영상](https://www.youtube.com/watch?v=c-fsL0gsmo0) · [script](../transcripts/channels/NVIDIA/Harrison_Chase_of_LangChain_on_Deep_Agents,_LangSmith,_and_E__c-fsL0gsmo0.md) |

### Snowflake (11건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 인공지능 기능이 발전함에 따라 기업들은 데이터를 기반으로 한 의미 있는 셀프 서비스 분석에 대한 수요가 증가했습니다. | 20 | [영상](https://www.youtube.com/watch?v=WFR07HIvCrQ) · [script](../transcripts/channels/Snowflake/Snowflake_Summit_2026_Builder_Keynote__WFR07HIvCrQ.md) |
| 2025-12 | anti_washing | 네, 이는 30년 전 프로세스 재설계 이후로 일종의 이상향이었는데, 인공지능 자체도 훌륭한 능력을 가지고 있지만, 오랫동안 미뤄져 왔던 이러한 엔드투엔드 통합을 가속화하거나 촉진하는 촉매제 역할을 하는 것 같습니다 . | 13 | [영상](https://www.youtube.com/watch?v=11degQs3L7c) · [script](../transcripts/channels/Snowflake/How_AI_Transforms_Retail,_Finance_and_Manufacturing_in_2026__11degQs3L7c.md) |
| 2026-02 | anti_washing | 이러한 프롬프트를 활용하고, 데이터를 파악하고, 계정 설정을 파악한 다음, 기본적으로 머신 러닝 워크플로를 자동화하는 것입니다. | 12 | [영상](https://www.youtube.com/watch?v=9LOP86qaw34) · [script](../transcripts/channels/Snowflake/Snowflake_Build_London_Keynote__9LOP86qaw34.md) |

### Meta Developers (11건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | neutral | 우리가 개발자 워크플로 프로세스에 인공지능을 도입하는 목적은 그러한 요소들을 최대한 제거하는 것입니다 . | 13 | [영상](https://www.youtube.com/watch?v=0v4_2pLH4jg) · [script](../transcripts/channels/Meta_Developers/Harness_the_Potential_of_AI_to_Supercharge_VR_Innovation__0v4_2pLH4jg.md) |
| 2026-04 | anti_washing | 그래서 우리가 흔히 발견하는 것은 개발자들이 따르는 매우 일반적인 워크플로가 있다는 것입니다. | 13 | [영상](https://www.youtube.com/watch?v=w-ys2nE-MgI) · [script](../transcripts/channels/Meta_Developers/VR_Performance_Fundamentals_for_Quest_33S__w-ys2nE-MgI.md) |
| 2026-04 | neutral | 지금은 인공지능의 힘을 활용하여 개발 워크플로우를 획기적으로 개선하고 창의성과 생산성을 새로운 차원으로 끌어올릴 수 있는 매우 흥미로운 시기입니다 . | 8 | [영상](https://www.youtube.com/watch?v=rVvqfcD3jmg) · [script](../transcripts/channels/Meta_Developers/VR_201_Essential_Tools_to_Power_Your_Quest_Development__rVvqfcD3jmg.md) |

### Anthropic (10건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-07 | anti_washing | 그래서 상담원 활용에 아주 좋은 사례입니다. | 18 | [영상](https://www.youtube.com/watch?v=XSZP9GhhuAc) · [script](../transcripts/channels/Anthropic/Prompting_for_Agents_Code_w_Claude__XSZP9GhhuAc.md) |
| 2025-09 | neutral | 터미널은 개발자의 워크플로에서 필수적인 요소입니다. | 8 | [영상](https://www.youtube.com/watch?v=vLIDHi-1PVU) · [script](../transcripts/channels/Anthropic/Designing_Claude_Code__vLIDHi-1PVU.md) |
| 2026-01 | neutral | Like, the machine learning class I was taking this semester, they have their own chatbot actually they built to specifically answer student questions, and if they wanna refer to lecture notes specifically, it's pretty helpful for it. | 6 | [영상](https://www.youtube.com/watch?v=N5yJJA0NCU0) · [script](../transcripts/channels/Anthropic/AI_on_campus__N5yJJA0NCU0.md) |

### OpenAI (10건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그러면 상담원은 온디맨드 도구를 사용하여 이러한 온디맨드 도구를 완벽하게 활용할 수 있습니다. | 11 | [영상](https://www.youtube.com/watch?v=jyuyY86GJnA) · [script](../transcripts/channels/OpenAI/Build_Hour_Valuemaxxing_with_GPT-5.6__jyuyY86GJnA.md) |
| 2026-06 | neutral | 오늘날 ChatGPT, Codex 및 API를 사용하여 구축할 수 있으며, 금융 서비스 워크플로에 특화된 에이전트, 플러그인 및 스킬을 즉시 사용할 수 있도록 더욱 쉽게 배포하고자 합니다. | 8 | [영상](https://www.youtube.com/watch?v=fAxlEcXiSts) · [script](../transcripts/channels/OpenAI/Operationalizing_AI_in_workflows_Lee_Spacagna,_Solutions_Eng__fAxlEcXiSts.md) |
| 2026-06 | neutral | 저희는 재무 워크플로우에 직접 통합되는 에이전트를 개발했습니다. | 6 | [영상](https://www.youtube.com/watch?v=1NtS2KdnDok) · [script](../transcripts/channels/OpenAI/OpenAI_on_OpenAI_Stacie_Faggioli,_Business_Finance_Officer_A__1NtS2KdnDok.md) |

### Unilever (9건 · 수요기업·기타 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-02 | anti_washing | 저는 매출의 3%만 투자하고, 그중 절반은 생산성 향상에 투입한다는 기존 방침에도 불구하고, 어떻게 더 높은 매출 성장률을 기대할 수 있는지 이해하려고 노력하고 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=YUdGwlJiDUk) · [script](../transcripts/channels/Unilever/Unilever_Full_Year_2023_Results_Webcast_&_Q&A__YUdGwlJiDUk.md) |
| 2026-04 | anti_washing | 수익성 개선은 판매량 증가, 제품 구성 개선, 지속적인 비용 절감, 그리고 예정보다 빠르게 진행되어 1분기 말 까지 이미 7억 5천만 유로의 성과를 달성한 생산성 향상 프로그램의 효과에 힘입은 것입니다. | 6 | [영상](https://www.youtube.com/watch?v=IlduIhb63aU) · [script](../transcripts/channels/Unilever/Unilever_Q1_2026_Trading_Statement_Results_Webcast_&_Q&A__IlduIhb63aU.md) |
| 2024-11 | neutral | 급변하는 세상에서 Li는 생산성 향상, 효율적이고 민첩한 공급망 유지, AI 의 혁신적인 잠재력 활용을 통해 운영 우수성을 달성하는 데 필요한 역량을 가속화하고 있습니다. | 4 | [영상](https://www.youtube.com/watch?v=ks7vFXlpsVA) · [script](../transcripts/channels/Unilever/Unilever_Investor_Event_2024,_Reginaldo_Ecclissato,_Chief_Bu__ks7vFXlpsVA.md) |

### Microsoft Azure (9건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 솔루션이나 비즈니스 문제를 일련의 확정적인 단계로 구성할 수 있다면, 저희 프레임워크에서 제공하는 워크플로 API를 활용하게 될 것입니다 . | 10 | [영상](https://www.youtube.com/watch?v=EXoIFK8viVM) · [script](../transcripts/channels/Microsoft_Azure/S2E2_How_do_agents_work_together_—_The_Shift_Podcast_by_Micr__EXoIFK8viVM.md) |
| 2026-04 | anti_washing | 손 여러분 사람들 중에서, 그리고 아시다시피, 혁신과 획기적인 발견을 이루어내는 것 생산성 향상. | 6 | [영상](https://www.youtube.com/watch?v=YLL7UuVCerM) · [script](../transcripts/channels/Microsoft_Azure/Microsoft_Digital_Sovereignty_Summit_Sovereign_Cloud,_AI_&_S__YLL7UuVCerM.md) |
| 2026-04 | neutral | 제품 피드백은 저희가 정말 중요하게 생각하는 부분 중 하나이며, 고객과 직접 소통하던 방식에서 개발자와 직접 소통하는 방식으로, 이제는 상담원이 고객이 되는 단계까지 나아가고 있는 것 같습니다. | 5 | [영상](https://www.youtube.com/watch?v=OBc1TyXH0WQ) · [script](../transcripts/channels/Microsoft_Azure/S2E6_Is_Postgres_the_wave_of_the_future_—_The_Shift_Podcast___OBc1TyXH0WQ.md) |

### Alibaba Cloud (8건 · 파운데이션 모델 · CN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 챗봇 GPT나 코파일럿과는 다른, 24시간 내내 백그라운드에서 실행되는 능동적인 에이전트로의 전환은 소프트웨어와의 관계를 근본적으로 바꿔놓습니다. | 56 | [영상](https://www.youtube.com/watch?v=xk6ACweQTVM) · [script](../transcripts/channels/Alibaba_Cloud/Alibaba_Cloud_Claw_Talks_EP5_Personal_AI_Agents_for_Compound__xk6ACweQTVM.md) |
| 2026-05 | anti_washing | QuinPai가 개인 AI 워크스테이션과 로컬 자동화를 어떻게 지원하는지, 그리고 Hik Clouder가 팀 워크플로우를 위해 투명하고 사람이 참여하는 다중 에이전트 협업을 어떻게 가능하게 하는지 살펴보겠습니다. | 20 | [영상](https://www.youtube.com/watch?v=7_FL9_RbLMY) · [script](../transcripts/channels/Alibaba_Cloud/Alibaba_Cloud_Claw_Talks_EP3_Build_AI_Agents_with_HiClaw_and__7_FL9_RbLMY.md) |
| 2026-07 | neutral | 따라서 이 하나의 클립은 이미 영화 감독과 전자상거래 광고 디자이너로부터 광범위한 업계 노하우를 축적했으며, 이러한 창의적인 경험과 워크플로를 정제하여 플랫폼 내에 사전 구축된 에이전트 기능으로 구현했습니다. | 17 | [영상](https://www.youtube.com/watch?v=-Ahk-Jr0oyA) · [script](../transcripts/channels/Alibaba_Cloud/Agent_Talks_EP1_Scaling_Video_Creation_Through_AI-Assisted_W__-Ahk-Jr0oyA.md) |

### ElevenLabs (8건 · 생성 미디어 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 그 이유는 이미 챗봇을 구축했기 때문입니다. | 24 | [영상](https://www.youtube.com/watch?v=HdelDovObRU) · [script](../transcripts/2026-08-03/Deploying_AI_at_Enterprise_Scale_-_ElevenLabs_Summit__HdelDovObRU.md) |
| 2026-03 | neutral | 두 번째로 눈에 띄는 것은, AI를 도입하는 기업의 80%가 실천하고 있는 강력한 추세인데, 바로 사업부 전체를 재편하고, 고객 서비스를 혁신하고, 엔지니어의 업무 방식을 바꾸고, 디지털 마케팅 방식을 혁신하는 것입니다 . | 18 | [영상](https://www.youtube.com/watch?v=TPV30xP1gyM) · [script](../transcripts/channels/ElevenLabs/How_BCG,_Naturgy,_and_Konecta_Are_Deploying_AI_Agents_in_Pro__TPV30xP1gyM.md) |
| 2026-06 | neutral | 이 솔루션은 원활한 오케스트레이션, 구성, 통합 및 모니터링을 하나의 플랫폼에서 제공하며, 이미 500만 명의 상담원이 매일 2년 반 분량의 대화를 처리하고 있습니다. | 15 | [영상](https://www.youtube.com/watch?v=va9CLYXfAjA) · [script](../transcripts/channels/ElevenLabs/New_Models_and_the_Future_of_Voice_AI_Mati_Staniszewski,_Ele__va9CLYXfAjA.md) |

### Runway (8건 · 생성 미디어 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | neutral | 사용자 지정 워크플로 구축에 대해서는 다른 에피소드에서 자세히 다루도록 하고, 지금은 여기에 있는 내용을 실행해 보겠습니다. | 17 | [영상](https://www.youtube.com/watch?v=MsVl_CKu_gk) · [script](../transcripts/channels/Runway/Using_Workflows_Runway_Academy__MsVl_CKu_gk.md) |
| 2025-11 | neutral | 오늘은 사용자 지정 워크플로를 구축해 보겠습니다. | 14 | [영상](https://www.youtube.com/watch?v=KQ1nXVT8iJM) · [script](../transcripts/channels/Runway/How_to_Build_Custom_Workflows_Runway_Academy__KQ1nXVT8iJM.md) |
| 2026-01 | neutral | Discord에 방문하시면 저희 크리에이티브 커뮤니티에서 워크플로우를 어떻게 활용하고 있는지 확인하실 수 있습니다. | 9 | [영상](https://www.youtube.com/watch?v=lkoIxZu6X0c) · [script](../transcripts/channels/Runway/Character_Creator_Workflow_Runway_Academy__lkoIxZu6X0c.md) |

### Oracle (8건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 여기에는 성능 저하 또는 발생할 수 있는 기타 문제에 대한 예측 알림을 수신하고 패치 및 롤백 워크플로를 자동화하는 것이 포함됩니다. | 9 | [영상](https://www.youtube.com/watch?v=2fz5FvOpybg) · [script](../transcripts/channels/Oracle/Lead_the_Change_Innovate_with_AI_Built_Into_Your_Database._E__2fz5FvOpybg.md) |
| 2026-07 | anti_washing | 여러분은 인공지능을 활용한 생산성 향상에 대해 많은 이야기를 들어보셨을 것이고, 인공지능으로 무엇을 할 수 있는지, 그리고 인공지능이 여러분의 개별적인 작업 해결을 어떻게 도울 수 있는지 알고 계실 겁니다. | 8 | [영상](https://www.youtube.com/watch?v=yhrBN_Ka-iA) · [script](../transcripts/channels/Oracle/Oracle_at_Gartner_CSO_Demand_More_from_Enterprise_AI__yhrBN_Ka-iA.md) |
| 2026-05 | neutral | 매개변수는 노트북을 프로그래밍 방식으로 실행하고 재사용 가능한 워크플로를 구축할 때 유용합니다. | 7 | [영상](https://www.youtube.com/watch?v=VtacaXYjNMo) · [script](../transcripts/channels/Oracle/How_to_Use_Parameters_in_Workflows_in_Oracle_AI_Data_Platfor__VtacaXYjNMo.md) |

### Arm (7건 · 인프라·칩·전력 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | neutral | 이를 통해 기존 컴퓨팅 인프라에 AI 가속 워크플로, 추론 엔진, 강화 학습 기반 모델을 추가하여 로봇 시스템에 매우 긴밀하게 통합할 수 있기 때문입니다. | 5 | [영상](https://www.youtube.com/watch?v=i7RToTgWszY) · [script](../transcripts/channels/Arm/Arm_Viewpoints_How_AI_and_advanced_robotics_are_redefining_a__i7RToTgWszY.md) |
| 2026-02 | anti_washing | 그러니까 보시다시피, 이건 기기에서 컴퓨팅 작업이 실행되고, 그 작업이 퍼블릭 클라우드의 기능을 활용하는 전형적인 에이전트 기반 워크플로의 예입니다. | 5 | [영상](https://www.youtube.com/watch?v=2v2XHgH0zCQ) · [script](../transcripts/channels/Arm/Arm_Viewpoints_The_rise_of_hybrid_AI__2v2XHgH0zCQ.md) |
| 2026-01 | anti_washing | 워크플로우를 생각해 보면, SAP나 Salesforce 또는 기업 내부에 있는 다른 시스템 들을 완전히 AI 기반으로 전환하는 데는 상당한 시간이 걸릴 것입니다. | 4 | [영상](https://www.youtube.com/watch?v=mpEnhLkwGrU) · [script](../transcripts/channels/Arm/Arm_CEO_Rene_Haas_on_AI,_chips,_and_the_future_of_global_com__mpEnhLkwGrU.md) |

### Cohere (6건 · 파운데이션 모델 · CA)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 이 두 논문 모두에서 해당 결과에 대한 중요한 단서가 있는데, 그것은 컴퓨터가 생산성을 향상시킨 것은 맞지만 , 그 생산성 향상은 주로 1990년대 와 2000년대 초반에 발생했다는 것입니다. | 18 | [영상](https://www.youtube.com/watch?v=uUUBApVevNI) · [script](../transcripts/channels/Cohere/O-Ring_Automation_&_the_Economics_of_Bicycles_for_the_Mind_w__uUUBApVevNI.md) |
| 2025-11 | anti_washing | 그리고 디지털 병리학이 급속도로 성장함에 따라 매일 수천 건의 새로운 사례가 스캔되고 있으며, 진단 워크플로는 이러한 새로운 데이터를 활용하도록 진화하고 있습니다 . | 6 | [영상](https://www.youtube.com/watch?v=naW98Kh-xvE) · [script](../transcripts/channels/Cohere/Fatemeh_Ghezloo_-_Making_Sense_of_Slides_From_Multimodal_Dat__naW98Kh-xvE.md) |
| 2026-02 | anti_washing | 또한 최근에는 A 플로어 또는 SPO와 같은 자동화된 워크플로우 설계를 사용하는 사례가 늘고 있는데, 이는 명확한 문제를 정의하고 모델이 에이전트 시스템의 최적 구성 요소를 스스로 찾아내도록 하는 방식입니다. | 5 | [영상](https://www.youtube.com/watch?v=d33qvh7a5VA) · [script](../transcripts/channels/Cohere/Yanjun_Shao_-_MedAgentsBench_Benchmarking_Reasoning_Models_a__d33qvh7a5VA.md) |

### Palantir (6건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-12 | neutral | Palantir와 협력할 대상을 결정했을 때, 실질적인 변화를 가져올 워크플로를 개선할 수 있는 곳이 필요하다는 것을 알았습니다. | 17 | [영상](https://www.youtube.com/watch?v=UjkRz9HkldU) · [script](../transcripts/channels/Palantir/Paragon_2025__UjkRz9HkldU.md) |
| 2025-02 | neutral | [Music] hi I'm ched West I'm an architect at paler&nbsp; today I have a conversation with honor rude he&nbsp;&nbsp; leads our commercial and retail business at paler&nbsp; thank you for joining me thank you for having me&nbsp;&nbsp; yeah so maybe you could tell us a little bit about&nbsp; your your … | 4 | [영상](https://www.youtube.com/watch?v=hPiDyTDT080) · [script](../transcripts/channels/Palantir/Chad_Interviews_Anirudh_How_Palantir_Powers_Retail_Operation__hPiDyTDT080.md) |
| 2025-11 | neutral | 에이전트된 워크플로우가 있는 SDK를 통합할 수 있습니다. | 4 | [영상](https://www.youtube.com/watch?v=YDAxITCNcko) · [script](../transcripts/channels/Palantir/Palantir_Ontology_Overview__YDAxITCNcko.md) |

### LG AI Research (6건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2021-12 | neutral | 복소수 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 쎄 안녕하세요 nga r2 설치 양진석 입니다 이번 발표에서 lg ai 연구원에서 진행하고 있는 air 기반 제품 부품 김 &amp; 폴 캐스팅 과제를 설명드리겠습니다 디맨드 폴 캐스팅은 수요를 예측하고 이를 기반으로 회사의 이익 창출을 위한 원활한 의사 결정을 지원하는 도구입니다 다시 말하면 수요에 측은 과거에 대한 정보를 기반으로 미래를 예측하는 분야인데요 이에 대한 간단한 예제를 안에 그리면서 보겠습니다 아래 그림은 4개의 제품들의 분… | 11 | [영상](https://www.youtube.com/watch?v=zikZEWOD6LI) · [script](../transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2021_Applied_AI_세션_4_-_양진석_리더__zikZEWOD6LI.md) |
| 2022-12 | anti_washing | [음악] 안녕하세요 어플라이드 에어 리서치 랩을 맡고 있는 이무영입니다 이번 세션에서는 엑스퍼트 afo productivity 다시 말해 생산성을 높이는 전문가 ai에 대해 말씀드리려고 합니다 LG AI 연구원에서는 LG 그룹의 다양한 난제들을 ai를 활용하여 해결하기 위한 연구를 진행하고 있습니다 LG 그룹에는 ai를 실질적으로 활용하고 있는 다양한 사례들이 만들어지고 있는데요 오늘은 그 중 가장 대표적인 사례인 PCB 오토라우팅 납사 스케줄링 디맨드 폴캐스팅 비전 인스펙션에 대해 말씀드리려고 합니다 모두 현업에 어려운 문제들을 … | 6 | [영상](https://www.youtube.com/watch?v=XbqJfvyg6hk) · [script](../transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2022_Expert_AI_Applications_for_Productiv__XbqJfvyg6hk.md) |
| 2023-07 | anti_washing | [음악] [박수] [음악] [박수] [음악] [박수] [음악] 안녕하세요 LG AI 연구원의 경우입니다 오늘 LG AI 토크 콘서트 2023에 와주신 모든 분들께 감사의 말씀드리겠습니다 어드밴싱 AI probetter life 2020년 12월 ai를 통해 보다 나은 섬을 만드는 것을 꿈꾸며 LG AI 연구원이 설립되었습니다 LG AI 연구원의 첫 번째 미션은 산업현장에 존재하는 난제를 해결하는 것이었습니다 정밀 부품의 생산 공정부터 신약개발 전기차 배터리 회로 설계 대형 플랜트 섭이 운영까지 다양한 산업 분야에서 난제를 발굴하고 … | 3 | [영상](https://www.youtube.com/watch?v=tbeGE19qIk4) · [script](../transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2023__tbeGE19qIk4.md) |

### Mistral AI (6건 · 파운데이션 모델 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그리고 이를 오늘날 현실 세계에 적용해 보면, 현재 모바일 애플리케이션의 은행 상담원 사용자가 100만 명에 달합니다. | 11 | [영상](https://www.youtube.com/watch?v=lluXpzkLpZo) · [script](../transcripts/channels/Mistral_AI/Best_practices_for_building_autonomous_AI_workflows_AI_Now_S__lluXpzkLpZo.md) |
| 2026-07 | anti_washing | 따라서 보험금 청구 처리와 같은 대규모 워크플로우를 처리하는 BFSI 분야의 다양한 활용 사례에서, 생성형 AI를 특정 접점에서 실제로 적용하려는 경우 해당 분야의 AI 전문 지식이 필요하며 모델을 조정하고 구축해야 합니다 . | 7 | [영상](https://www.youtube.com/watch?v=7evOiuXFkQo) · [script](../transcripts/channels/Mistral_AI/Domain_AI_models_fine-tuned_with_proprietary_knowledge_AI_No__7evOiuXFkQo.md) |
| 2026-07 | neutral | 개인 사용자로서 챗봇과 에이전트를 사용하여 AI를 활용하면서 생산성이 크게 향상되었다고 느끼고 있지만, 아직 배포되지 않은 애플리케이션들은 데이터 형식이 적합하지 않거나, 데이터가 접근하기 어렵거나, 데이터가 생성되는 곳과 컴퓨팅 자원이 너무 멀리 떨어져 있기 때문입니다. | 6 | [영상](https://www.youtube.com/watch?v=QxgcNjBO580) · [script](../transcripts/channels/Mistral_AI/AI_infrastructure_is_the_new_critical_infrastructure_AI_Now___QxgcNjBO580.md) |

### Microsoft Developer (5건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 하지만 상담원을 단일 사용자 인터페이스에 통합하면 상호 작용은 일대일로 이루어집니다. | 46 | [영상](https://www.youtube.com/watch?v=Q9uv_y04rJE) · [script](../transcripts/channels/Microsoft_Developer/Build_agents_where_work_happens_chats_channels_and_meetings___Q9uv_y04rJE.md) |
| 2026-06 | anti_washing | 자, 여기서는 CI/CD 워크플로우의 잠재적 개선 사항을 살펴보겠습니다. | 7 | [영상](https://www.youtube.com/watch?v=sOYxgLTa_EE) · [script](../transcripts/channels/Microsoft_Developer/DevOps_in_the_Age_of_AI_with_GitHub_&_Azure__sOYxgLTa_EE.md) |
| 2026-06 | anti_washing | 고객, 동료, 그리고 커뮤니티 구성원들과 마찬가지로, SQL Server 환경에 AI 워크플로우를 도입하려는 사람들에게 가장 중요한 조언은 무엇일까요? | 5 | [영상](https://www.youtube.com/watch?v=tLAfkruOOWo) · [script](../transcripts/channels/Microsoft_Developer/Giving_AI_agents_visibility_into_SQL_Server_with_MCP_Data_Ex__tLAfkruOOWo.md) |

### Cursor (5건 · 엔터프라이즈 앱 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 이러한 신뢰성과 성능 향상은 상담원이 24시간 내내 근무할 때 진정으로 나타납니다. | 25 | [영상](https://www.youtube.com/watch?v=fWa7uxyhVDE) · [script](../transcripts/channels/Cursor/Opening_Keynote,_Michael_Truell_Compile_26__fWa7uxyhVDE.md) |
| 2026-06 | anti_washing | 우리는 매우 복잡한 기능들을 자동화 시스템 뒤에 숨겨두었기 때문에 상담원들은 그 자동화 시스템을 호출하고 다양한 구성 요소를 활용하여 필요한 여러 작업을 수행할 수 있습니다. | 8 | [영상](https://www.youtube.com/watch?v=zxvyO5vnknI) · [script](../transcripts/channels/Cursor/Agents_and_Infrastructure,_Sam_Lambert_Compile_26__zxvyO5vnknI.md) |
| 2026-06 | anti_washing | 여러분도 이렇게 하는지는 모르겠지만, 저희는 내부적으로 반복적으로 사용하는 프롬프트나 워크플로를 발견하면, 그것을 스킬로 패키징하고, 내부적으로 게시하고, 경우에 따라 모델이 검색할 수 있도록 하여 다른 사람들도 활용할 수 있도록 하는 데 큰 노력을 기울이고 있습니다. | 8 | [영상](https://www.youtube.com/watch?v=-jnwTZ789V0) · [script](../transcripts/channels/Cursor/Running_128_Coding_Agents_at_Once__-jnwTZ789V0.md) |

### GE HealthCare (5건 · 수요기업·기타 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 결론적으로 요약하자면, 볼타 매핑 시스템과 GE 시스템 기록 시스템 중에서 어떤 환자에게 최적의 워크플로우를 적용할지 고민할 때, AI 기반 매핑 시스템을 이용한 심방세동 절제술이 임상적으로 환자의 치료 결과를 개선하는 것으로 나타났다고 말하는 것이 매우 타당하다고 생각합니다 . | 11 | [영상](https://www.youtube.com/watch?v=TabAqdd4gkQ) · [script](../transcripts/channels/GE_HealthCare/Workflow_optimization_with_GE_HealthCare_CardioLab_AI.i_and___TabAqdd4gkQ.md) |
| 2026-02 | anti_washing | 청중들에게 엑스레이 워크플로우에 적용된 디자인 변경 사항 중 가장 큰 영향을 미친 몇 가지 사례를 공유해 주시겠습니까 ? | 7 | [영상](https://www.youtube.com/watch?v=uIoKgJC3lAU) · [script](../transcripts/channels/GE_HealthCare/X-ray_matters_-_How_empathy_in_design_shapes_the_patient_exp__uIoKgJC3lAU.md) |
| 2026-02 | anti_washing | 이 워크플로는 판단을 대체하기 위한 것이 아니라, 복잡성에서 명확성으로의 전환을 지원하기 위해 설계되었습니다. | 3 | [영상](https://www.youtube.com/watch?v=EVcRu2rMefA) · [script](../transcripts/channels/GE_HealthCare/MUSE_User_Group_Meeting_January_2026_–_Dr_Cihan_Ilyas_Sevgic__EVcRu2rMefA.md) |

### Scale AI (5건 · 컨설팅·전략 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | Temporal이 지원하는 기본 요소들을 자세히 살펴보니, 그중 상당수가 우리가 구축하고자 하는 AI 워크플로우 유형, 특히 사람이 단순히 한 가지를 입력하고 응답을 받는 것이 아니라 에이전트 자체가 작업을 주도하는 장기 실행 비동기 에이전트에 매우 적합하다는 것을 알게 되었습니다 . | 7 | [영상](https://www.youtube.com/watch?v=rEhkP6oztMw) · [script](../transcripts/2026-08-03/Introducing_Agentex_Open-Source_Infrastructure_for_Enterpris__rEhkP6oztMw.md) |
| 2025-10 | neutral | So the typical use case those models address are internal workflow automation or knowledge management. | 5 | [영상](https://www.youtube.com/watch?v=sXTycrc-b7Q) · [script](../transcripts/channels/Scale_AI/Scale_AI_@_ALL_IN_2025_Back_to_the_future_of_Canadian_AI_6_y__sXTycrc-b7Q.md) |
| 2024-09 | anti_washing | 반면 AI 지원 조직은 AI를 프로세스 개선 및 조직 효율성 향상을 위한 도구로 활용하는 것을 의미합니다. | 4 | [영상](https://www.youtube.com/watch?v=TPN6hbY40TU) · [script](../transcripts/channels/Scale_AI/Scale_AI_AI_Playbook_for_Business_Leaders_ALL_IN_2024__TPN6hbY40TU.md) |

### kakao tech (4건 · 수요기업·기타 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 그래서 결론적으로는 약 8개월 정도 전 의사 결정 당시 에어플로우를 워크플로우 관리틀로 선택하기로 했고 1.10.2 버전을 적용해 에어플로우를 운영하기 시작했습니다. | 17 | [영상](https://www.youtube.com/watch?v=TXY6JCoOTu4) · [script](../transcripts/channels/kakao_tech/[ifkakao2021]_추천_시스템_airflow_2_0_도입기__TXY6JCoOTu4.md) |
| 2026-06 | anti_washing | 에어플로는 개발자가 작성한 워크플로우를 관리하는 역할이라고 보시면 될 것 같습니다. | 7 | [영상](https://www.youtube.com/watch?v=621c_vgwyMc) · [script](../transcripts/channels/kakao_tech/[ifkakao2021]_티스토리에서_airflow활용기__621c_vgwyMc.md) |
| 2026-06 | neutral | 이러한 레거시 시스템에 대해 저희 개발팀에서도 어려움을 겪었던 경험이 있었는데요. | 3 | [영상](https://www.youtube.com/watch?v=r2t4h3qMXzw) · [script](../transcripts/channels/kakao_tech/[ifkakao2021]_Daum_Mail_Terraforming_다음_메일_백엔드_레__r2t4h3qMXzw.md) |

### Infosys (4건 · 수요기업·기타 · IN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | anti_washing | 그리고 또 다른 예로, 저희는 지난 10월에 모바일 뱅킹에 AI 챗봇을 출시했는데, 이미 고객 문의의 20%를 처리하고 있습니다 . | 14 | [영상](https://www.youtube.com/watch?v=0ixUiXr2DVY) · [script](../transcripts/channels/Infosys/The_Boardroom_Mandate_Scaling_AI_for_Business_Impact_Davos_2__0ixUiXr2DVY.md) |
| 2026-03 | anti_washing | 은행 라이선스를 획득한 것도 물론 기능적 신뢰 구축에 중요한 요소이지만, Revolute는 여기에 관계적 요소를 더해 탁월한 고객 서비스를 제공함으로써 신뢰를 더욱 강화하고 있습니다. | 9 | [영상](https://www.youtube.com/watch?v=2GboyaQ1VKs) · [script](../transcripts/channels/Infosys/Brand_Finance_Global_500_Launch_2026_AI_Rising_The_Evolution__2GboyaQ1VKs.md) |
| 2026-03 | neutral | 그래서 저는 모든 마케터들이 " 내가 가진 도구들과 AI가 제공하는 모든 기능을 활용해서 어떻게 하면 고객 개개인에게 완벽하게 맞춤화된 훨씬 더 정교한 고객 경험을 제공할 수 있을까?"라고 고민해야 한다고 생각합니다. | 8 | [영상](https://www.youtube.com/watch?v=taeDyZI86h8) · [script](../transcripts/channels/Infosys/The_Future_of_Customer_Experience_-_Creativity,_Trust_&_Tech__taeDyZI86h8.md) |

### Cerebras (4건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 이는 단순히 회사의 사업 성과와 생산성 향상, 그리고 회사 규모 확장에 도움이 되기 때문만이 아니라, 보안 전문가인 우리가 AI를 도입하지 않으면 매우 빠르게 보안 침해를 당할 것이기 때문입니다. | 7 | [영상](https://www.youtube.com/watch?v=sD2kVXOfhLs) · [script](../transcripts/channels/Cerebras/Cerebras_CISO_Naor_Penso_on_AI_Security_&_The_CrowdStrike_Pa__sD2kVXOfhLs.md) |
| 2026-03 | anti_washing | 소비자 인터페이스, 예를 들어 챗봇 같은 것을 사용하는 것보다는 소프트웨어 개발 워크플로에 통합하여 다단계 음악 에이전트를 개발하는 것이 더 중요합니다. | 4 | [영상](https://www.youtube.com/watch?v=lVkZswKIZeY) · [script](../transcripts/channels/Cerebras/Arena_Founder_Anastasios_Angelopoulos_on_AI_Trends_for_2026__lVkZswKIZeY.md) |
| 2026-07 | neutral | 빠른 추론 기능을 통해 시간이 오래 걸리는 에이전트 워크플로우 속도를 높일 수 있으며, 실시간 번역 및 특정 음성 에이전트와 같이 지연 시간에 민감한 실시간 LLM 애플리케이션도 활용할 수 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=0m-G6hOIDH4) · [script](../transcripts/channels/Cerebras/Cerebras_and_DeepLearning.AI_-_Build_ultra-fast_LLM_applicat__0m-G6hOIDH4.md) |

### Hugging Face (4건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 최근 들어 안정적인 AI 워크플로우를 구축하는 데 있어 코딩 하네스가 가장 중요한 요소 중 하나라는 점이 매우 분명해졌습니다 . | 4 | [영상](https://www.youtube.com/watch?v=qo1QNxWcm28) · [script](../transcripts/channels/Hugging_Face/Tau_Crash_Course_The_Python_Port_of_Pi__qo1QNxWcm28.md) |
| 2026-04 | neutral | 스토리지 버킷은 AI 워크플로우를 위한 매우 간단한 스토리지 단위이지만, 잠시 후 살펴보겠지만 AI 워크플로우뿐만 아니라 매우 다재다능하게 활용될 수 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=N7y0OFz98Po) · [script](../transcripts/channels/Hugging_Face/Introducing_Storage_Buckets__N7y0OFz98Po.md) |
| 2024-12 | neutral | CPU에서 워크플로우를 확장하고 더 효율적이고 확장 가능한 플랫폼에 더 많은 학습 및 추론 워크플로우를 적용할 수 있도록 지원하는 다양한 기술, 데이터 유형 및 양자화 기술에 대해 알아보겠습니다. | 3 | [영상](https://www.youtube.com/watch?v=Rc0-pjfPgW8) · [script](../transcripts/channels/Hugging_Face/🤗_Hugging_Cast_S2E6_-_Scale_LLMs_with_Intel_Gaudi_and_Xeon__Rc0-pjfPgW8.md) |

### Orange (4건 · 통신·주권·국가 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | washing | 네, 제 생각에 에이전트 QAI는 완전 자율 시스템이 아니라 비용 절감, 프로세스 자동화, 의사 결정 가속화와 같은 특정 작업이나 가치 사슬의 특정 부분에서 실제로 도움이 되는 시스템 및 도구입니다 . | 4 | [영상](https://www.youtube.com/watch?v=c1XCSgKzhp4) · [script](../transcripts/channels/Orange/The_Impact_of_Agentic_AI_on_Telco_Transformation_&_Innovatio__c1XCSgKzhp4.md) |
| 2026-06 | neutral | 그러니까, 만약 우리가 처음 이용하는 사용자들의 고객 경험을 개선하는 데 도움을 주고 협력해 줄 적합한 스타트업을 찾는다면 , 우리는 기꺼이 투자할 것입니다. | 4 | [영상](https://www.youtube.com/watch?v=FltorFwspZ8) · [script](../transcripts/channels/Orange/Social_Inclusion_and_Fintech_Balancing_Innovation_and_Equity__FltorFwspZ8.md) |
| 2026-06 | neutral | 구찌는 현재 H 컴퍼니의 글로벌 상업적 확장을 주도하고 있으며, 주요 기업들이 복잡한 B2B 워크플로우를 처리하기 위해 자율 AI 에이전트를 배포하는 방식을 혁신하고 있습니다 . | 2 | [영상](https://www.youtube.com/watch?v=h5PkiTd_AVU) · [script](../transcripts/channels/Orange/Agentic_AI,_Trust_&_Scale_Jérôme_Berger_(Orange)_&_Gautier_C__h5PkiTd_AVU.md) |

### Philips (3건 · 수요기업·기타 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 기술 산업, 데이터 센터 산업, 빅 데이터, 하이퍼바이저 분야에서 15년 또는 20년 전을 되돌아보면 생산성 향상을 위해 이러한 기술들을 어떻게 도입해 왔는지 알 수 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=WVAO4A3M-ac) · [script](../transcripts/channels/Philips/How_Philips_Is_Turning_AI_Into_Real_Healthcare_Impact_Jeff_D__WVAO4A3M-ac.md) |
| 2026-03 | anti_washing | 그래서 방금 말씀하신 AI 관련 흥미로운 점들 외에도, AI는 워크플로우 개선에도 도움을 주고 있으며, 이를 통해 의료진이 더 많은 시간을 확보하고, 더 빠르고 정확한 진단을 내릴 수 있게 되는 것을 확인할 수 있습니다. | 7 | [영상](https://www.youtube.com/watch?v=wYmHA5Pr6_g) · [script](../transcripts/channels/Philips/The_Future_of_Medicine_Is_Already_Here_AI,_Connected_Care_&___wYmHA5Pr6_g.md) |
| 2026-07 | neutral | 첫째, 직원과 의사에게 새로운 애플리케이션이나 개선된 워크플로(음악)를 교육하면 한두 명의 환자뿐 아니라 장기적으로 수천 명의 환자에게 영향을 미칠 수 있습니다 . | 3 | [영상](https://www.youtube.com/watch?v=5ZGTAN9zPUs) · [script](../transcripts/channels/Philips/Help_Transform_Patient_Care_at_Philips_as_a_Clinical_Solutio__5ZGTAN9zPUs.md) |

### NAVER Cloud (3건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | anti_washing | 앞서 이제 제가 보여 드렸던 모든 부분들에 대해서 뭐 데이터 프로세싱을 통해서 데이터셋 만들고 커스터마이징 하고 그리고 이제 그거에 대한 이밸루에이트를 통해서 어 님을 통해서 또 배포를 하고 그리고 가드레이를 통해서 또 인하우스에 대한 프로트 제어를 하고 그리고 실제로 운영을 하면서 발생하는 여러 로그 로그 데이터라든가 아니면 신규 뉴논놀리 난리지에 대한 어떤 데이터 셋들을 또 이제 저장을 해서 또 후처리 데이터에 대한 프로세싱 통하고 요런 1년에 하나의 작업 작업들을 앞서 말씀드렸던 것처럼 아르 워크플로우를 통해서 템플릿화할 수 … | 9 | [영상](https://www.youtube.com/watch?v=Wfa3epgeN-E) · [script](../transcripts/channels/NAVER_Cloud/HyperCLOVA_X_모델_운영_자동화_NVIDIA_NeMo_기반_GPU_서빙_가이드_(네이버클라우드_윤성__Wfa3epgeN-E.md) |
| 2024-04 | neutral | 네이버 클라우드 플랫폼에 클라우드 서비스의 전환은 아주 만족스러웠습니다 클라우드 전환을 통해 인프라 안정성과 서비스 품질을 높이고 장애 위험을 최소화했기 때문입니다 저희 브리지는 공항을 기반으로 한 마케팅 사업 운영 아웃소싱 공항 리무진 세 가지 부분의 사업이 브리지가 제공하는 주요 서비스는 전 세계 공항 라운지 서비스가 있고 공항 호텔 골프 등 프리미엄 서비스를 개발하여 고객사에게 제공하고 있습니다 브리지가 개발한 더 라운지는 해외 파트너사와 제휴하여 전 세계 1200년의 공학 라운지를 소비자가 편리하게 이용할 수 있는 서비스 플… | 8 | [영상](https://www.youtube.com/watch?v=ey957aIun2A) · [script](../transcripts/channels/NAVER_Cloud/더라운지_운영사,_이브릿지가_네이버_클라우드_플랫폼을_선택한_이유!__ey957aIun2A.md) |
| 2023-11 | anti_washing | [음악] [박수] 네 반갑습니다 여러분 네이버 클라우드에서 AI 산행 연구 글로벌 AI 생태계 전략을 총괄하고 있는 하정우라는 평소 때만 달리 저는 오늘이 생성형 AI 하는이 기술이 어떻게 산업과 사회를 변화시키고 나오고 있고 금융이라는이 산업에 어떤 영향을 주게 될지에 좀 집중을 해서 설명을 드리려고 합니다 예 유명한 두 분이 이런 말씀하셨습니다 오른쪽에 있는 앤드류 교수 딥러닝 4대 친 중에 한 분이라 불리우죠 AI 전기와 같은 다목적 기술이다 얘기를 했습니다 이분은 업게 있는 분이니까 이렇게 말씀하실 수 있죠 근데 왼쪽에 있는… | 2 | [영상](https://www.youtube.com/watch?v=geRDaOiQWlo) · [script](../transcripts/channels/NAVER_Cloud/[네이버클라우드_금융_컨퍼런스_2023]_생성형_AI_시대,_금융을_위한_기술_경쟁력_(네이버클라우드_하정우__geRDaOiQWlo.md) |

### TCS (3건 · 엔터프라이즈 앱 · IN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-09 | neutral | 고객 서비스부터 재무 운영에 이르기까지, Wisdom Next Agentic은 가장 큰 운영상의 병목 현상을 경쟁 우위로 전환시켜 드립니다. | 6 | [영상](https://www.youtube.com/watch?v=FhQSMJT0vwc) · [script](../transcripts/channels/TCS/TCS_AI_WisdomNext__FhQSMJT0vwc.md) |
| 2025-12 | neutral | 그래서 일정 수준의 레거시 시스템이 존재하고, 그 레거시 시스템에는 지식 관련 문제가 있으며, 이러한 문제들을 모두 새로운 기술 도입 으로 해결할 수는 없습니다. | 4 | [영상](https://www.youtube.com/watch?v=891VU8DOK9E) · [script](../transcripts/channels/TCS/TCS_in_Conversation_with_Fintech_Futures_-_Part_2__891VU8DOK9E.md) |
| 2025-09 | neutral | 이러한 변화 과정에서 신뢰성, 안전성 확보 및 향상된 고객 경험 제공은 여전히 ​​매우 중요합니다 . | 2 | [영상](https://www.youtube.com/watch?v=upxDsTADR3o) · [script](../transcripts/channels/TCS/TCS_Software-Defined_Vehicle_(SDV)_Platform_for_Vehicle_Diag__upxDsTADR3o.md) |

### Huawei (3건 · 인프라·칩·전력 · CN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-08 | neutral | 그들은 고객 경험 관련 업무를 수행하는 데 인공지능을 활용할 것입니다 . | 4 | [영상](https://www.youtube.com/watch?v=QZZBEYvYq6g) · [script](../transcripts/channels/Huawei/Our_North_Star_IOH_&_AI_Transforming_Indonesia's_Intelligent__QZZBEYvYq6g.md) |
| 2026-04 | neutral | 챗봇을 구축하고, 태스크포스를 구성하고, 시범 운영을 진행하고, 새로운 도구를 출시하고, 모든 것에 채팅 GPT를 추가하세요 . | 2 | [영상](https://www.youtube.com/watch?v=c6nYPWNgl7I) · [script](../transcripts/channels/Huawei/Discipline,_Not_Hype,_Will_Define_AI_Innovation__c6nYPWNgl7I.md) |
| 2025-09 | neutral | 하나의 통합된 다목적 플랫폼을 통해 100단계 이상의 워크플로우 뿐만 아니라 상담원도 자동으로 생성할 수 있습니다 . | 2 | [영상](https://www.youtube.com/watch?v=P4Nymzu3r-s) · [script](../transcripts/channels/Huawei/Introducing_Huawei's_ACT_Pathway_for_Industrial_Intelligence__P4Nymzu3r-s.md) |

### Schneider Electric (3건 · 인프라·칩·전력 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 제 생각에는 말씀하시는 내용이 기존 시스템 통합 및 노후화된 시스템, 즉 소위 말하는 구식 시스템이나 오래된 시스템을 다루는 브라운필드 환경의 유산에 관한 것 같습니다 . | 4 | [영상](https://www.youtube.com/watch?v=2cJD3hlyu6g) · [script](../transcripts/channels/Schneider_Electric/Is_there_an_ROI_in_industrial_AI_The_truth_behind_data,_auto__2cJD3hlyu6g.md) |
| 2026-07 | neutral | 공장들은 흔히 전기 시스템과 공정 자동화 시스템을 분리하여 운영하는데, 이로 인해 시스템 간 장벽이 생기고 비효율성이 증가하며 안전 위험이 발생하고 운영 비용이 높아집니다 . | 2 | [영상](https://www.youtube.com/watch?v=3HDL6WY8zww) · [script](../transcripts/channels/Schneider_Electric/EcoStruxure_Power_&_Process_Unified_Operations_Schneider_Ele__3HDL6WY8zww.md) |
| 2026-05 | anti_washing | 프랑스에 위치한 이 회사는 직원 24명의 시스템 통합 업체이며, 슈나이더 일렉트릭의 시스템 통합 업체 제휴 프로그램에 참여하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=lU8FwS9OWyM) · [script](../transcripts/channels/Schneider_Electric/Episode_3-_Real_stories,_real_impact_Schneider_Electric__lU8FwS9OWyM.md) |

### 삼성SDS AX (2건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 업무 환경에서이 개인들이 만드는 GPT를 좀 넘어서서 팀단위의 업무를 수행할 수 있는 GPT 어 그리고 이제 모든 직원들의 이제 공통 업무를 수행하는 GPT를 만들게 되면 산내의 뭔가 AI 워크플로우를 위한 생태계를이 GPT로 구축할 수 있다라는 점이었죠. | 14 | [영상](https://www.youtube.com/watch?v=oXxq-xeAoJQ) · [script](../transcripts/2026-07-26/ChatGPT_Enterprise_도입전략__oXxq-xeAoJQ.md) |
| 2026-07 | anti_washing | 우리는 금융 회사지만 우리는 앞으로 AX 회사다라고 선언을 어 대표님께서 선언을 하시면서 1년 동안 5대 업무를 선정을 하고 5대 업무에이 27개 핵심 업무에 175개 이상의 에이전트를 만들겠다라고 디자인을 하셨고 어 올해부터는 저희 STS와 함께 해당 에이전트들을 고객 관리 기업 여신에서부터 자산 관리 업무자동화까지이 전반적인 전체의 업무 프로세스들을 에이전트 기반으로 바꾸는 작업 여전 여정을 어 저희 SS와 진행을 하고 계십니다. | 12 | [영상](https://www.youtube.com/watch?v=PsfnMJwSoXs) · [script](../transcripts/2026-07-23/[AX_Summit]_2._(키노트)AI_Native_기업으로의_전환_방안과_사례(AX센터_AI사업팀장_신계__PsfnMJwSoXs.md) |

### Telenor (2건 · 통신·주권·국가 · NO)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2023-04 | anti_washing | 하지만 문제는, 그리고 우리는 당신이 BT와 이전 직장에서 디지털화의 간소화를 위해 많은 노력을 기울여 왔다는 것을 알고 있습니다만, 핵심 질문은 바로 레거시 시스템에 대한 의존성을 어떻게 끊어내고 혁신의 규모와 속도를 촉진하고 가속화하며 고객 경험을 개선하고 완전한 디지털화를 달성할 수 있느냐는 것입니다. | 9 | [영상](https://www.youtube.com/watch?v=fythNeXmXnM) · [script](../transcripts/channels/Telenor/Telco_Tech_Talks_How_do_we_develop_our_people_to_meet_the_fu__fythNeXmXnM.md) |
| 2022-08 | anti_washing | 마지막으로, 제가 시스템 통합이라고 부르는 부분에 큰 책임을 졌다는 것도 말씀드리고 싶습니다. | 2 | [영상](https://www.youtube.com/watch?v=b-QPcJfgViw) · [script](../transcripts/channels/Telenor/Telco_Tech_Talks_Tareq_Amin,_CEO_of_Rakuten_Mobile__b-QPcJfgViw.md) |

### SambaNova (2건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-12 | neutral | [음악] 에이전트가 전자 건강 기록을 조회하는 워크플로에서 이 세 가지 모델을 호출함에 따라 모델 전환이 빠르게 이루어지는 것을 보실 수 있습니다 . | 8 | [영상](https://www.youtube.com/watch?v=2cwvj07cY8s) · [script](../transcripts/channels/SambaNova/Running_Agentic_GraphRAG_workflows_for_Electronic_Health_Rec__2cwvj07cY8s.md) |
| 2025-12 | anti_washing | 제 주변에 전자상거래 기업의 CRM 제품에서 워크플로 자동화를 위한 에이전트 시스템을 구축하고 있는 초보 친구들이 몇 명 있습니다 . | 2 | [영상](https://www.youtube.com/watch?v=w8C2d__ArIA) · [script](../transcripts/channels/SambaNova/ACE_Explained_by_the_Creators_How_Agentic_Context_Engineerin__w8C2d__ArIA.md) |

### Boston Dynamics (2건 · 물리 AI·자율주행 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2023-06 | neutral | 이번 업데이트의 새로운 기능은 플랫폼에 내장된 세 가지 유형의 검사 기능을 제공하고, 더욱 원활하고 빠르고 간편한 사용자 경험을 위해 검사 구성 워크플로를 개선했다는 점입니다. | 7 | [영상](https://www.youtube.com/watch?v=qgHeCfMa39E) · [script](../transcripts/channels/Boston_Dynamics/Spot_Levels_Up_Boston_Dynamics__qgHeCfMa39E.md) |
| 2025-11 | anti_washing | 제 임무는 사람들이 이러한 로봇과 직접 상호 작용할 수 있는 인터페이스를 구축하고, 이러한 창고 환경에서 발생할 수 있는 다양한 유형의 예외 및 문제를 처리하는 워크플로를 구축하는 것이었습니다 . | 4 | [영상](https://www.youtube.com/watch?v=laexcnaTrDM) · [script](../transcripts/channels/Boston_Dynamics/Why_Humanoids_Are_the_Future_of_Manufacturing_Boston_Dynamic__laexcnaTrDM.md) |

### Boston Consulting Group (2건 · 컨설팅·전략)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 오늘날 기업들은 이미 이러한 기술들을 챗봇 경험의 일부로 활용하여 소비자들과 실시간으로 대화하고 양방향 상호작용을 가능하게 하고 있습니다 . | 6 | [영상](https://www.youtube.com/watch?v=MKhYZVAMgkY) · [script](../transcripts/channels/Boston_Consulting_Group/Eliminating_Friction_in_the_Customer_Journey__MKhYZVAMgkY.md) |
| 2026-07 | anti_washing | 저희 회사 규모에 비해 시스템 통합 업체가 60곳이 넘었습니다. | 4 | [영상](https://www.youtube.com/watch?v=YBe0oiv01N0) · [script](../transcripts/channels/Boston_Consulting_Group/With_180_Years_of_Reinvention,_Pearson_Takes_on_the_AI_Era__YBe0oiv01N0.md) |

### 티타임즈TV (2건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | washing | 예를 들어서 같은 콜센터의 채볼을 도입했다고 하더라도 어느 회사는 몇 시간을 절감을 했고 이걸 돈으로 환산하니 연간 예를 들어서 1.5억의 절감 비용이 나옵니다 라고를 과제를 그렇게 정리한 회사가 있는 반면에 어느 회사는 아 우리는 그게 아니고 그냥 서버이 좋네요. | 4 | [영상](https://www.youtube.com/watch?v=b-tgY8Q0SbA) · [script](../transcripts/2026-07-23/현장에서_AI_트랜스포메이션_이끌면서_배운_것_(황재선_SK_부사장)__b-tgY8Q0SbA.md) |
| 2026-07 | anti_washing | 기업 내부의 대부분의 업무들, 대부분의 워크플로우들과 운영 전반에 걸쳐서 AI를 활용하는 것이 확대가 되고 이것을 통해 가지고 새로운 디지털 비즈니스 모델을 발굴하거나 비즈니스에서의 어떤 운영 방식이나 이런 것들을 AI 기준으로 근본적으로 변화시키기 위한 기본이 되고 있는 기초가 되고 있는 단계입니다. | 2 | [영상](https://www.youtube.com/watch?v=GiFlOiikYso) · [script](../transcripts/2026-07-21/AI_도입,_도입만_하면_끝일까_(김유신_상무)__GiFlOiikYso.md) |

### 일잘러 장피엠 (2건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 뭐 이런 것들을 좀 정량적으로 따져서 실제로 연결될 수 있게끔 하는 것이 이제 3개월 있다가도 계속 쓰시면서 기업의 이제 자연스러운 워크플로우로 이렇게 적용될 수 있는 그런 비즈니스 임팩트가 될 거 같습니다. | 4 | [영상](https://www.youtube.com/watch?v=_M0admzUkuo) · [script](../transcripts/2026-08-03/[Real_AX]_Why_aren't_AI_agents_performing_as_well_as_expecte___M0admzUkuo.md) |
| 2026-08 | washing | 2단계 자동화는 딱 시키는 것만 하는 것이라면 3단계 조직화 방식은 목표를 부여하고 업무 지시서 수준에 상세한 업무 프로세스와 가이드를 주면 AI가 알아서 일을 하는 것입니다. | 3 | [영상](https://www.youtube.com/watch?v=wP48xJLWuB0) · [script](../transcripts/2026-08-03/If_you're_using_AI_diligently_and_seeing_no_change,_you_don'__wP48xJLWuB0.md) |

### AMD (2건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | anti_washing | Finally, Yocto Project offers standard toolchains and libraries, providing developers with a comprehensive set of tools to simplify software integration and streamline development. | 4 | [영상](https://www.youtube.com/watch?v=clpQEmPeYhw) · [script](../transcripts/channels/AMD/Yocto_Project™_Basics__clpQEmPeYhw.md) |
| 2025-11 | anti_washing | And, of course, it, and we've talked about in the financial services sector, there's lots of anomaly detection, process automation. | 2 | [영상](https://www.youtube.com/watch?v=AR0JpYQwhBc) · [script](../transcripts/channels/AMD/AI_in_Finance_with_BNY_Advanced_Insights_S2E8__AR0JpYQwhBc.md) |

### Google (2건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 이렇게 하면 사용자가 [음악] 도구를 확인하고 워크플로에 통합할 수 있는 고유 링크가 생성됩니다. | 4 | [영상](https://www.youtube.com/watch?v=ECquAokER_8) · [script](../transcripts/channels/Google/How_to_use_Tools_in_Google_Flow_Find_Your_Flow__ECquAokER_8.md) |
| 2026-05 | neutral | 제가 관심을 갖는 것은 창작 과정에서 새로운 도구를 활용하고 창작 워크플로우를 확장할 수 있는 새로운 방법을 찾는 것입니다 . | 2 | [영상](https://www.youtube.com/watch?v=_qWItNk5a9Q) · [script](../transcripts/channels/Google/Exploring_Tools_in_Google_Flow_In_the_Flow___qWItNk5a9Q.md) |

### Volvo Cars (2건 · 물리 AI·자율주행 · SE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2021-07 | neutral | 볼보 팀은 구글 팀과 오랜 시간 협력해 왔으며, 처음에는 기술 통합에서 시작했지만, 이제는 시스템 통합으로까지 발전했습니다. | 3 | [영상](https://www.youtube.com/watch?v=TMfKGcpN_d0) · [script](../transcripts/channels/Volvo_Cars/Future_connected_experience__TMfKGcpN_d0.md) |
| 2021-07 | anti_washing | 이러한 현실을 염두에 두고 우리는 고객 경험을 최적화하고 있으며, 핵심 역량 중 하나는 고객 차량의 수명 주기 동안 소프트웨어를 빈번하고 지속적으로 배포하는 것입니다. | 2 | [영상](https://www.youtube.com/watch?v=8WyV487QG9Q) · [script](../transcripts/channels/Volvo_Cars/Core_Computing__8WyV487QG9Q.md) |

### AI Master (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 이와 같은 작업 공간은 AI 기반 연구, 콘텐츠 제작 및 워크플로 자동화에 사용됩니다. | 51 | [영상](https://www.youtube.com/watch?v=bcM9dP_uXJU) · [script](../transcripts/2026-08-03/How_to_Build_an_AI_Agent_with_Claude_Code_(Claude_AI_Agent_T__bcM9dP_uXJU.md) |

### Solutions Review (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 여러분 모두 기업 출장 예약 및 경비 관리 챗봇, 법무팀을 위한 법률 보조 챗봇, RFP 답변 작성을 지원하는 RFP 보조 챗봇 등과 같은 직원 생산성 챗봇을 구축해 본 경험이 있을 것입니다 . | 33 | [영상](https://www.youtube.com/watch?v=P0kux8A8NbM) · [script](../transcripts/2026-08-03/Build,_Test,_and_Deploy_Production-Ready_Enterprise_AI_Agent__P0kux8A8NbM.md) |

### Tigerhall (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 워크플로 개선이나 수동에서 전략으로의 전환 등 우리가 논의해 온 모든 것들을 넘어, 특히 향후 3~5년 동안 변화와 혁신 과정에서 가장 큰 변화는 전문가 중심에서 모든 사람이 참여하는 분산화라고 생각합니다. | 18 | [영상](https://www.youtube.com/watch?v=OJwpw-8SkBM) · [script](../transcripts/2026-07-26/AI_for_AI_Building_the_Transformation_Office_That_Drives_Ent__OJwpw-8SkBM.md) |

### DATAVERSITY (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 따라서 이러한 에이전트 기반 워크플로는 중간 사무실 간접비를 줄이고 기본 운영 비용을 약 40% 절감함으로써 상당한 재정적 이점을 가져다줍니다. | 18 | [영상](https://www.youtube.com/watch?v=JhbsIutTwXM) · [script](../transcripts/2026-08-03/Analythics_Architecture_Promising_AI_Use_Cases_for_the_Enter__JhbsIutTwXM.md) |

### Kore.ai (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 클라우드 도입을 통해 교훈을 얻으려는 기업들이 앞으로 5년, 10년을 내다보며 소수의 AI 기업에 핵심 사업 운영을 전적으로 의존하게 되는 상황을 우려한다면, 어떤 조언을 하시겠습니까? | 18 | [영상](https://www.youtube.com/watch?v=-0V6XUskt-k) · [script](../transcripts/2026-07-26/Agentic_AI_Adoption_Secrets_You_Need_to_Know_Now__-0V6XUskt-k.md) |

### 알컨연구소 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 어디아의 2025년 디지털 CX 조사에 따르면 북미 컨택 센터 리더의 75%가 AI 도입이 오히려 상담사 스트레스를 높이고 있다고 답했습니다. | 18 | [영상](https://www.youtube.com/watch?v=KFH0uH6DSSA) · [script](../transcripts/2026-08-04/AI_상담봇_도입_실패하는_7가지_이유_도입_전_반드시_알아야_할_것들__KFH0uH6DSSA.md) |

### Citizen Developer and Nathan Rose (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 간단히 말해서, M365 내에서 개인 생산성이나 팀 생산성 향상을 위한 에이전트가 필요한 경우라면, 그 범위가 바로 M365 Copilot 에이전트의 한계입니다. | 18 | [영상](https://www.youtube.com/watch?v=Ox0m3iJG57M) · [script](../transcripts/2026-07-21/AI_Transformation_Leader_(AB-731)_-_Full_Course_-_Pass_The_E__Ox0m3iJG57M.md) |

### 메타코드M (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 갖고 있는 업무 프로세스 그리고 의사 결정 방식, 책임 소재 등 그리고 책임 구조 롤 같이 이런 부분들을 다시 디자인하는 것들을 같이 해보면 조금 더 현실적이고 어떻게 보면 AI 전환이라는게 나를 그리고 회사의 시스템을 다시 돌아보는 관점부터 시작하는 것들이 맞지 않을까라는 질문의 핵심이라고 말씀드릴 수 있습니다. | 17 | [영상](https://www.youtube.com/watch?v=VRYJJJBqsDE) · [script](../transcripts/2026-07-18/26_Years_of_Survival_Keyword_AX_(Great_AI_Transformation)_We__VRYJJJBqsDE.md) |

### Cresta (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 개인화된 상호작용을 제공하는 C 센터와 같은 시스템을 구축하려면, 수억 명의 고객을 보유한 B2C 기업들이 필요하지만, 오늘날 고객당 평균 가치가 낮기 때문에 콜센터를 운영할 여력이 없습니다. | 17 | [영상](https://www.youtube.com/watch?v=cKGyiwsm66I) · [script](../transcripts/2026-08-03/Deploying_AI_Agents_In_The_Enterprise__cKGyiwsm66I.md) |

### Jeff Su (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | CHBT, Google Gemini, Claude와 같은 인기 있는 AI 챗봇은 대규모 언어 모델(LLM)을 기반으로 구축된 애플리케이션으로, 텍스트 생성 및 편집에 매우 뛰어납니다 . | 17 | [영상](https://www.youtube.com/watch?v=FwOTs4UxQS4) · [script](../transcripts/2026-08-03/AI_Agents,_Clearly_Explained__FwOTs4UxQS4.md) |

### BOI (Board of Innovation) (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 지금 바로 자체 모델을 학습시키고, 고객 서비스나 비즈니스의 여러 부분을 지원할 수 있는 에이전트 시스템을 구축하기 시작하면 계속해서 성장할 수 있기 때문입니다. | 16 | [영상](https://www.youtube.com/watch?v=PL3OWn143AI) · [script](../transcripts/2026-07-18/Webinar_AI_transformation_that_works,_lessons_from_the_trenc__PL3OWn143AI.md) |

### LG CNS (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | LG CNS는 글로벌 ERP, 클라우드, AI, 빅 데이터, 스마트 팩토리, 스마트 물류, 스마트 시티 등 다양한 분야에서 고객의 디지털 전환(DX)을 선도하는 디지털 비즈니스 혁신 기업입니다. | 16 | [영상](https://www.youtube.com/watch?v=2jX9XkIhR0s) · [script](../transcripts/2026-08-03/LG_CNS_AX,AI-Based_ERP_Asset_Portal_for_Global_Business_Oper__2jX9XkIhR0s.md) |

### AI Engineer (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그래서 제가 이 고객사와 함께 일했을 때, 그들은 소매 금융 회사였고, 소매 금융 챗봇을 개발하고 있었어요. | 16 | [영상](https://www.youtube.com/watch?v=ObTPqBGsEbA) · [script](../transcripts/2026-08-03/The_Production_AI_Playbook_Deploying_Agents_at_Enterprise_Sc__ObTPqBGsEbA.md) |

### GCP Study Hub (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그리고 여기 네 번째 경로는 워크플로 자동화입니다. | 15 | [영상](https://www.youtube.com/watch?v=5MxBkBgdCJc) · [script](../transcripts/2026-08-03/Gemini_Enterprise_Agent_Platform_is_here._(RIP_Vertex_AI)__5MxBkBgdCJc.md) |

### Cole Hastings (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 2024년 디지털 교육 위원회의 조사에 따르면 대학생의 86%가 학습에 AI를 활용하고 있으며, 54%는 적어도 매주 AI를 사용하고 있는 것으로 나타났고 , 그중 챗봇 GPT가 가장 인기 있는 것으로 조사되었습니다. | 14 | [영상](https://www.youtube.com/watch?v=GwEjuhpo26o) · [script](../transcripts/2026-08-03/How_AI_is_Ruining_Education_For_Everyone__GwEjuhpo26o.md) |

### 한국지역정보개발원 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서 지역 문제를 워크플로 단위로 왜 나눠야 되냐면 우리가 허떠한 지역 문제에 대한 문제를 발견하고 데이터를 수집하고 연결하고 그리고 우리가 실질적으로 분석하고 추천하고 인간이 판단하고 현장에 개입하고 결과 피드백하는이 정과정에서 결과적으로는 어떤 AI 기술이 어떠한 부분을 대체할 것인가들을 굉장히 잘 분석해 내야 되는 거죠. | 13 | [영상](https://www.youtube.com/watch?v=i6Br6_ImXaA) · [script](../transcripts/2026-07-27/2026_'AI_로_구현하는_지역_AX'_시리즈_-_제3회_KLID-FNF_온라인세미나__i6Br6_ImXaA.md) |

### 까칠한AI (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 업무 자동화 말고 이거에 대해서도 한번 고민해볼 필요가 있다고 생각이 듭니다 안녕하세요 까칠한 AI 황현태입니다 반갑습니다 또 몇 달 더 AX를 하다 보니까 공유 드리고 싶어가지고 카메라를 켰습니다 AX 효능감에 대해서 말씀드리려고 해요 기관들을 돌아다녀 보니까 옛날에는 AX 어떻게 해야 되냐를 요즘은 실무자 입장에서 너무 경영진의 큰 얘기들은 공감되지 않는다 그리고 경영진 입장에서는 실무 AX, 실무 업무 자동화를 굉장히 지원을 많이 했는데 이런 고민을 많이 말씀을 하시고 그래서 저희도 고민을 많이 했습니다 그래서 과연 어떻게 해… | 13 | [영상](https://www.youtube.com/watch?v=pnn4QZU2TnA) · [script](../transcripts/2026-07-18/Why_AI_transformation_doesn't_feel_like_it's_working_in_your__pnn4QZU2TnA.md) |

### 테디노트 TeddyNote (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 그건 아니고 팔란티어를 도입하지 않더라도 우리가 하고 있는 일에 대해서 어떤 에이전트를 만든다고 하면 지금 당장은 우리가 시간에 쫓겨서 어떤 워크플로상의 한 단계를 맞는 에이전트를 만든다. | 11 | [영상](https://www.youtube.com/watch?v=ctKz2bkgkPQ) · [script](../transcripts/2026-08-03/#팔란티어_#온톨로지_로_미리보는_Al_Agent의_미래__ctKz2bkgkPQ.md) |

### MIT Corporate Relations (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | washing | 하지만 고객 경험 측면 과 백오피스 측면에서 시스코가 적용하는 다양한 기술들을 볼 수 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=9RvWcXVaAng) · [script](../transcripts/2026-07-31/Integrating_Generative_AI_Into_Business_Strategy_Dr._George___9RvWcXVaAng.md) |

### 바이브코딩 레인 RaiN (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그러나 영상은 여러분께 이제 100% 퍼스널라이즈 된 업무 자동화가 아니기 때문에 좀 아쉬우실 수도 있어요. | 10 | [영상](https://www.youtube.com/watch?v=hmWSM6HMyZU) · [script](../transcripts/2026-07-31/I_Handed_Off_My_Daily_Busywork_to_AI_From_Build_to_Deploymen__hmWSM6HMyZU.md) |

### IBM (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 사람들은 사고방식에 있어서 매우 제한적이며, 단지 AI 에이전트를 사용하여 기존의 워크플로를 대체하고 있을 뿐입니다. | 10 | [영상](https://www.youtube.com/watch?v=eZ1NizUx9U4) · [script](../transcripts/2026-07-21/AI_isn’t_digital_transformation,_and_leaders_need_to_underst__eZ1NizUx9U4.md) |

### 샘 호트만 : AI 엔지니어의 시선 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 뭐 이런 식의 프롬프트를 한번 던져 보셔 가지고 좋은 에이전트 워크플로우를 개발을 하신 걸 추천드리고요. | 10 | [영상](https://www.youtube.com/watch?v=8P_U-9GaNYA) · [script](../transcripts/2026-07-25/AI_활용_수준을_바꾸는_SKILL을_상위_1%처럼_쓰는_나만의_노하우_모음_(w._콘텐츠_시스템)__8P_U-9GaNYA.md) |

### INSEAD (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 말씀하신 것처럼 코딩 분야뿐만 아니라 마케팅, 고객 서비스 등 다양한 분야에서 활용될 수 있는 사례가 많습니다. | 10 | [영상](https://www.youtube.com/watch?v=CoPCP3f1DzM) · [script](../transcripts/2026-07-18/Making_AI_Transformation_Work_Avoiding_the_Mistakes_from_Dig__CoPCP3f1DzM.md) |

### Slack (1건 · 엔터프라이즈 앱 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 따라서 워크플로를 구축할 때 이 두 단계 중 하나를 선택하여 워크플로에서 사용할 수 있습니다. | 10 | [영상](https://www.youtube.com/watch?v=SfQqs9EsaJU) · [script](../transcripts/channels/Slack/Slack_School_Deploying_Your_First_Slack_App__SfQqs9EsaJU.md) |

### ERP Suites | JD Edwards Insights (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 아시다시피 50년대에는 신경망 유형의 연구 개발이 진행되었고, 실제로 그 당시 최초의 디지털 비서 또는 챗봇인 엘리자(Eliza)가 50년대에 만들어졌습니다. | 9 | [영상](https://www.youtube.com/watch?v=FmcULDfEgvM) · [script](../transcripts/2026-08-03/Enterprise_AI_From_Big_Uncertainty_to_Massive_ROI__FmcULDfEgvM.md) |

### PMI Sydney Australia Chapter (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그러니까 AI 에이전트가 기존 챗봇을 뛰어넘어 워크플로의 여러 요소를 자동화하고, 인간의 개입 없이 또는 반자율적인 인간의 도움을 받아 이를 수행할 수 있게 된다는 것입니다. | 9 | [영상](https://www.youtube.com/watch?v=KhteXbyW3sI) · [script](../transcripts/2026-08-03/How_Enterprises_Use_AI_in_Project_Management_Real_World_Case__KhteXbyW3sI.md) |

### Swisscom (1건 · 통신·주권·국가 · CH)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 주로 K와 이야기하기 전에 챗봇 또는 부가가치세 및 GPT를 출시하는 곳 사실 세상이 통제하고 있지만, 사실 K는 이미 매우 랑구스라서 예를 들어, 저는 K명의 십대 자녀를 두고 있는데, 그들은 소셜 미디어를 사용합니다. | 9 | [영상](https://www.youtube.com/watch?v=zNFVjqSv5rU) · [script](../transcripts/channels/Swisscom/Kids_&_KI_-_Chancen_und_Risiken_Online-Elternabend__zNFVjqSv5rU.md) |

### SoftBank (1건 · 수요기업·기타 · JP)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 이러한 방법에는 AI 기반 보안 연구를 통해 취약점 목록을 생성 하고 검증하는 것, 또는 CI/CD 워크플로에 취약점 스캔을 통합하여 개발자가 작성하는 모든 풀 리퀘스트에 대해 취약점을 스캔하는 것 등이 포함될 수 있습니다. | 8 | [영상](https://www.youtube.com/watch?v=9WXOHFQTJGM) · [script](../transcripts/channels/SoftBank/Special_Event_Hosted_by_SoftBank_Corp.,_SB_OAI_Japan_GK,_Sof__9WXOHFQTJGM.md) |

### Stanford Health Care (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서 우리는 모델 구축 자체보다 워크플로 측면, 즉 전반적인 과정에 훨씬 더 많은 신경을 쓰고 있습니다. | 8 | [영상](https://www.youtube.com/watch?v=wD1qn2i3Wb4) · [script](../transcripts/2026-07-21/AI_Transforms_Health_Care_Artificial_Intelligence_The_Future__wD1qn2i3Wb4.md) |

### OnePint AI (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 모두가 이 여정을 거쳐야 한다면, 어떻게 하면 빠르게 AI를 도입하여 조직이나 비즈니스 워크플로우를 혁신할 수 있을까요? | 8 | [영상](https://www.youtube.com/watch?v=XrD-W6013G0) · [script](../transcripts/2026-08-03/Fail_Forward_Why_AI_Adoption_Rewards_the_Willing__XrD-W6013G0.md) |

### 손에잡히는경제 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | &gt;&gt; 사진 자료 보시면 AI를 썼다 썼더니만 회계사는 55% 생산성 향상됐고요. | 7 | [영상](https://www.youtube.com/watch?v=4-lOvLaVWSA) · [script](../transcripts/2026-08-03/Why_Companies_Are_in_Trouble_After_Relying_on_AI_for_Layoffs__4-lOvLaVWSA.md) |

### Whatfix (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 인공지능은 이미 여러 산업을 변화시키고 있지만, 단순히 생산성 향상이나 예측 모델에 관한 것만은 아닙니다. | 7 | [영상](https://www.youtube.com/watch?v=BCQcC7nClts) · [script](../transcripts/2026-08-03/Why_AI_Adoption_Fails_and_How_a_People-First_Strategy_Can_Sa__BCQcC7nClts.md) |

### Team Atn (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 이제 최소네 명이 2주 되는데 밤을 세도 시간이 모자할 것 같아서 이때는 워크플로우 분석이거 뭐거 없었고 그냥 제가 처음부터 끝까지 다 로직을 짜고 에이전트를 만들고 마지막에 이제 인터뷰 제작하는 것까지 바이브 코팅으로 이제 배포를 했었습니다. | 7 | [영상](https://www.youtube.com/watch?v=j9qz5ja6AZU) · [script](../transcripts/2026-07-28/[AI_Builders_Meetup_#4]_Any_Sufficiently_Advanced_AX_Is_Indi__j9qz5ja6AZU.md) |

### AI 겸임교수 이종범 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서 처음에 무신사도 AI를 이렇게 도입을 했을 때 어 요걸로 뭔가 업무 효율화를 많이 이룰 수 있지 않을까라고 생각을 했지만 어 실제로 초기에 도입을 했을 때에는 어 코드 짜는 속도가 굉장히 빨랐지만은 마지막에이 완성을 하는 그 10% 어 요기를 이제 완벽하게 해내지 못했기 때문에 사람이 투입될 수밖에 없었고 이런 10%의 세밀한 UI 조정이나 예외 처리 이런 것들을 위해서 AI한테 계속 뭐 20번 넘게 이렇게 프롬프트를 수정하는 그런 과정에서 어 굉장한 필요함을 느꼈다고 합니다. | 7 | [영상](https://www.youtube.com/watch?v=jYwDdt_3L8Q) · [script](../transcripts/2026-07-23/오픈AI_x_무신사_비공개_행사_후기,_코덱스_기업_도입_사례와_AI_네이티브_워크플로우_인사이트_총정리__jYwDdt_3L8Q.md) |

### Artıfısıal (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | So basically like AI trans AI transformation it means we we replace like some like legacy systems into the AI so that we can make the system more efficient. | 7 | [영상](https://www.youtube.com/watch?v=yVDDB4XAP_Y) · [script](../transcripts/2026-07-21/AI_&_AX_Automation_Explained_How_AI-Native_Companies_Transfo__yVDDB4XAP_Y.md) |

### 홍아린 AI (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | washing | 두 번째 단계는 AI 워크플로우 정해진 자동화 흐름입니다. | 7 | [영상](https://www.youtube.com/watch?v=MkScRelUMhQ) · [script](../transcripts/2026-08-03/제발_챗GPT만_쓰지_마세요._AI_에이전트_핵심_총정리__MkScRelUMhQ.md) |

### Vertesia (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | Um and I think you know we speak to a lot of organizations where they've started down a particular uh route and because of the newness of the technology and the fact that it isn't you know well you know an ERP implementation something like an SAP or an Oracle financials there's probably 15 20 30,000… | 6 | [영상](https://www.youtube.com/watch?v=B4WgQotMVmE) · [script](../transcripts/2026-07-21/Enterprise_strategies_for_agentic_AI_adoption_in_2026_and_be__B4WgQotMVmE.md) |

### Kotter International Inc (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그래서 생산성 향상을 위한 노력일 수도 있고, 분석 및 통찰력 확보일 수도 있고, 소프트웨어 개발이나 제품 개발일 수도 있습니다. | 6 | [영상](https://www.youtube.com/watch?v=jfpIvZy89UM) · [script](../transcripts/2026-08-03/Why_AI_Projects_Fail_Lessons_from_the_US_Army_&_Kotter_Kotte__jfpIvZy89UM.md) |

### Amazon Web Services (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 자, 회사에서 언급하고 싶어하는 또 다른 중요한 점이자 제가 측정하고 싶어하는 점, 그리고 모든 사람이 최고 AI 책임자에게 기대하는 점은 바로 조직의 생산성 향상에 어떻게 기여하고 있느냐는 것입니다. | 6 | [영상](https://www.youtube.com/watch?v=LblTPS1LnLc) · [script](../transcripts/2026-07-18/Leading_AI_Transformation_A_Chief_AI_Officer's_Perspective_A__LblTPS1LnLc.md) |

### ai2learn (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 예를 들어, 한 회사는 글로벌 기업들이 챗봇을 이용해 고객 지원을 자동화했다는 소식을 듣고 비슷한 솔루션을 신속하게 도입했습니다. | 6 | [영상](https://www.youtube.com/watch?v=gbP_TrZnPTs) · [script](../transcripts/2026-07-23/Why_SMB_Companies_Fail_at_AI_Transformation_and_How_to_Avoid__gbP_TrZnPTs.md) |

### Sema4ai (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 두 번째 이유는 에이전트를 기존 기업 레거시 시스템과 통합하는 과정이 매우 복잡하다는 점입니다. | 6 | [영상](https://www.youtube.com/watch?v=xofWoVQ-ic4) · [script](../transcripts/2026-07-24/Enterprise_AI_Adoption_From_Idea_to_Deployment__xofWoVQ-ic4.md) |

### Beyondtraining (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 생산성 향상은 필연적으로 긍정적인 결과를 가져온다. | 6 | [영상](https://www.youtube.com/watch?v=mjx4GV7BXk8) · [script](../transcripts/2026-08-02/Revealing_AI_Transform_Strategies!_Increase_Efficiency,_Redu__mjx4GV7BXk8.md) |

### Liam Ottley (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 맞춤 코딩된 챗봇에 15,000달러를 청구하는 대신 , VoiceFlow나 초창기에는 Botress와 같은 노코드 플랫폼을 사용하여 고객을 위한 솔루션을 구축 하고 가격대를 낮추고 개발 난이도 도 낮출 수 있었습니다. | 5 | [영상](https://www.youtube.com/watch?v=aNrWN0M851k) · [script](../transcripts/2026-07-18/What_is_an_AI_Transformation_Partner_(and_how_to_become_one)__aNrWN0M851k.md) |

### 카툰경제학 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 한 IT 기업 인사팀에서 내부적으로 조사한 자료를 보면 보고서 작성, 데이터 분석, 고객 응대 같은 업무에서 AI를 활용한 직원 한 명이 AI 없이 일하는 직원 세 명에서 다섯 명만큼의 성과를 낸다는 결과가 나왔어요. | 5 | [영상](https://www.youtube.com/watch?v=moja9e9m55A) · [script](../transcripts/2026-08-03/IMF_때보다_더_심각하다_3만원짜리_AI로_전부_대체_중,_줄줄이_희망퇴직_받는_대기업_정규직의_몰락__moja9e9m55A.md) |

### Brave Achievers (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 이러한 상담원 중심의 경험은 운영을 간소화할 뿐만 아니라 대기 시간을 최소화하고 정확한 답변을 제공하여 고객 만족도를 향상시킵니다. | 5 | [영상](https://www.youtube.com/watch?v=Kho24ymyTLM) · [script](../transcripts/2026-07-21/The_Birth_of_AI_Agent_Experience_(AX)—A_New_Kind_of_UX__Kho24ymyTLM.md) |

### DX (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 로컬 챔피언은 우리 팀의 고유한 워크플로에서 AI를 활용하여 개발자 경험을 개선하는 방법을 찾아냅니다. | 5 | [영상](https://www.youtube.com/watch?v=c51ToE4pPpY) · [script](../transcripts/2026-08-04/The_AI_adoption_playbook_Lessons_from_Microsoft's_internal_s__c51ToE4pPpY.md) |

### Google DeepMind (1건 · 파운데이션 모델 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 그래서 우리는 그러한 환각 현상을 인지하고, 그러한 환각 현상이 점점 더 드물어지고 앞으로도 계속 줄어들기를 바라며, 진행 중인 작업 흐름을 방해하지 않도록 워크플로에 통합해야 합니다 . | 5 | [영상](https://www.youtube.com/watch?v=V04bm-3d6EQ) · [script](../transcripts/channels/Google_DeepMind/When_millions_of_AI_agents_meet__V04bm-3d6EQ.md) |

### Accenture (1건 · 엔터프라이즈 앱 · IE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | anti_washing | 그리고 우리가 목격하고 있는 것은 주요 은행들이 운영 체제를 넘어 워크플로 및 기타 애플리케이션과 같은 상위 계층으로 애플리케이션 기능을 확장하고 오픈 소스로 전환하는 동일한 사고방식을 보이고 있다는 것입니다. | 4 | [영상](https://www.youtube.com/watch?v=MWvdwSD3ZRc) · [script](../transcripts/channels/Accenture/Top_Banking_Trends_2026_-_Unconstrained_Banking_Accenture__MWvdwSD3ZRc.md) |

### Microsoft (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | anti_washing | McKinsey reduced client onboarding lead time by 90%. | 4 | [영상](https://www.youtube.com/watch?v=HXy3J1mGHRE) · [script](../transcripts/channels/Microsoft/AI_and_automation_expert_on_how_leaders_use_AI_agents_to_get__HXy3J1mGHRE.md) |

### Reckitt (1건 · 수요기업·기타 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2022-02 | neutral | 우리는 기업 전반의 효율성을 높이기 위해 업계 최고 수준의 생산성 향상 프로그램을 운영하고 있으며, 목표 투자액을 4년 동안 20억 파운드로 늘렸습니다. | 4 | [영상](https://www.youtube.com/watch?v=vfnLF2JcGYA) · [script](../transcripts/channels/Reckitt/Rejuvenating_Reckitt_Two_years_of_transformation__vfnLF2JcGYA.md) |

### Telefónica (1건 · 통신·주권·국가 · ES)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-11 | anti_washing | 업무 프로세스를 개선함으로써, 시스템, 상품 및 하드웨어 우리는 순추천고객지수(NPS)를 높일 것입니다. | 4 | [영상](https://www.youtube.com/watch?v=8HYvqTquKQM) · [script](../transcripts/channels/Telefónica/Telefónica_Capital_Markets_Day_2025_ES__8HYvqTquKQM.md) |

### GOTO Conferences (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 당신이 이 제품을 구매했거나 이 애플리케이션을 적용했는데, 왜 아무도 우리 챗봇을 사용하지 않거나 우리가 구매한 이 제품을 사용하지 않는 건가요? | 4 | [영상](https://www.youtube.com/watch?v=1uJZlKig0Tk) · [script](../transcripts/2026-07-18/How_to_Lead_Your_Organisation’s_AI-Transformation_•_Rasmus_L__1uJZlKig0Tk.md) |

### 한경 글로벌마켓 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 그런데 기존 시스템에 기존 레거시 시스템에 AI 도입하려고 통합하려고 하니까 데이터도 준비가 안 되어 있고 이거 보안이나 책임 권한 이런 것들도 다 문제고 또 너무 비싸기도 하고 이런 여러 가지 어려움들을 지금 겪고 있는 상황입니다. | 4 | [영상](https://www.youtube.com/watch?v=Wr8-UEAQgQ8) · [script](../transcripts/2026-07-24/[마지막화]_메모리_부족은_시작일_뿐_돈이_고이는_AI_병목들_빈난새의_빈틈없이월가__Wr8-UEAQgQ8.md) |

### 그린코끼리 AI (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 분한 내용을 바탕으로 마지막 단계인 자동화를 위해 실제 워크플로우를 설계해 달라고 요청했습니다. | 4 | [영상](https://www.youtube.com/watch?v=hLNn4mDhR9c) · [script](../transcripts/2026-08-03/제발_카피하세요._클로드_AI_업무_자동화_3단계__hLNn4mDhR9c.md) |

### Dust - Transform how work gets done. (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 왜냐하면 AI 에이전트를 구축하기 위해 에이전트 기반 워크플로를 시도한 파일럿 프로젝트의 95%가 제대로 작동하지 않았기 때문입니다. | 3 | [영상](https://www.youtube.com/watch?v=01NYw3PzqiI) · [script](../transcripts/2026-07-28/AI_Agents_getting_to_90%,_the_AI_adoption_playbook_for_Enter__01NYw3PzqiI.md) |

### Matt Song (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 파일럿 프로젝트를 실제로 돌린 기업은 20%로 줄어들었고 워크플로우에 통합되어 정규 업무로 자리 잡은 기업은 단지 5%뿐입니다. | 3 | [영상](https://www.youtube.com/watch?v=ksXsgaS0cGg) · [script](../transcripts/2026-07-27/AX(AI전환)의_현황과_추진방향__ksXsgaS0cGg.md) |

### Engineering Leaders Community (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | washing | 그러니까 테스트를 최대한 개선하고 프로세스를 최적화하고 더 나은 에이전트 워크플로를 구축하는 방법을 찾고 계시겠죠. | 3 | [영상](https://www.youtube.com/watch?v=HDJaNBuRWYI) · [script](../transcripts/2026-08-03/Why_AI_Adoption_Fails_in_Engineering_Teams_I_Meetup_#39__HDJaNBuRWYI.md) |

### 김작가 TV (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | anti_washing | 그러면 이제 기업에서도 요즘 AI 교육 많은 걸로 알고 있는데 기업 실무자들은 AR 이용이 어떤 업무 자동화 있고 어떻게 생산성을 높이나요? | 3 | [영상](https://www.youtube.com/watch?v=AsQUoda0wB0) · [script](../transcripts/2026-08-03/상위_1%만_알고_있는_AI_활용법,_삶의_질이_10배_상승합니다_(김상윤_교수)__AsQUoda0wB0.md) |

### 헬로티_매일 만나는 산업, IT News (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 여기에도 지금 어 코파일러이 이제 연동이 돼 있고 그다음에 파워 오토메이션이나 아니면 이런 자동화 툴들에도 저희가 전목이 돼 있으면서 어 다이너지스 같은 저희 이제 그 SCM이나 CRM ERP 쪽 이런 비즈니스 솔루션 쪽에서도 코파일럿이 또 전목이 되 있습니다. | 3 | [영상](https://www.youtube.com/watch?v=p9Tj9ctxMr8) · [script](../transcripts/2026-07-29/AI_도입의_격차,_상위_5%_기업의_AI_활용_전략_-_마이크로소프트_백인송_이사_[AI_TECH_2026__p9Tj9ctxMr8.md) |

### 온라인 이커머스 설계 기록 / 자사몰 구축 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | ERP 도입할 때도 ERP 사서 설치하면 업무가 좋아질 거라고 생각하는데 업무 프로세스를 안 바꾸면 엑셀 쓰던 것과 비슷합니다. | 3 | [영상](https://www.youtube.com/watch?v=nfigZxE58ys) · [script](../transcripts/2026-08-03/AI_도입_전에_이것부터_하세요_25년_커머스_현장_경험__nfigZxE58ys.md) |

### First Up Media, LLC (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-08 | neutral | 직원들은 업무 프로세스를 개선할 방법을 끊임없이 모색합니다 . | 3 | [영상](https://www.youtube.com/watch?v=V2vnUl2vq_E) · [script](../transcripts/2026-08-04/Solving_the_Implementation_Gap_AI_Adoption_Problems_and_the___V2vnUl2vq_E.md) |

### Meta (1건 · 파운데이션 모델 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-04 | anti_washing | 그리고 제 목표는 GenAI를 VFX 워크플로우에 통합하는 것이었습니다. | 3 | [영상](https://www.youtube.com/watch?v=qOdjM14QW0s) · [script](../transcripts/channels/Meta/Boz_To_The_Future_Podcast_#23_-_The_Future_According_to_Jame__qOdjM14QW0s.md) |

### 채널 원티드 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 아, &gt;&gt; 그래서 그게 한 네다섯 가지의 어떤 여러 가지 로직들이 결합이 됐는데 한 다섯 가지 시스템을 하나씩 만들어 가지고 결합을 하니까 정말 틀림없이 &gt;&gt; 그 데이터를 뽑아냈고 전화 업무에만 집중할 수 있고 그 팀은 통화 시간이 이제 매출로 볼 수 있는 팀이다 보니까 그렇게 정량화해 볼 수도 있고 그 팀이 생산성이 되게 많이 좋아진 사례 &gt;&gt; 아 앞 오전에 해야 되는 그 업무 시간이 줄어들으로써네 &gt;&gt; 전환 시간이 거의 두 배로 &gt;&gt; 확보가 되고 또 데이터에 대해서 정확도 되… | 2 | [영상](https://www.youtube.com/watch?v=PLaXDf3UzLg) · [script](../transcripts/2026-07-27/Look_at_companies_that_only_mimic_AX._How_to_set_up_an_envir__PLaXDf3UzLg.md) |

### 전인구경제연구소 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | AI 대전환을 위해서 산업 경쟁력 강화 전력으로 업무 생산성 향상을 위한 A비즈, 기업 생산 공정 개선을 위한 제조 AI 솔루션, 크래프톤의 게임 AI를 통한 실시간 캐릭터 대화 및 자유행동 구현, AI 모델을 물리 행동 영역으로 확장한 휴먼노이드 로봇 기술 등 활용 분야를 이렇게 넓혀 나갈 수가 있어요. | 2 | [영상](https://www.youtube.com/watch?v=xduBTqb_mXM) · [script](../transcripts/2026-07-22/소버린AI에_한국의_미래가_달렸습니다.__xduBTqb_mXM.md) |

### Upstage (1건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-03 | neutral | 또한 SageMaker Studio, SageMaker SDK, SageMaker 콘솔 및 자동화된 머신 러닝 워크플로에서 모델을 사용자 지정하고 미세 조정할 수 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=e2ehr1oBqnA) · [script](../transcripts/channels/Upstage/Try_'Solar'_with_Amazon_SageMaker_Jumpstart!_Upstage_LLM__e2ehr1oBqnA.md) |

### 데이브의 개발 생활 | AI 소모임 대표 채널 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 이것만 정리하면 결국 이걸 그대로 AI한테 던져서 업무 자동화를 만들 수 있을 정도로 아주 아주 디테일하게 작성하는 업무를 구조로 보는 눈을 키워 주셔야 합니다. | 2 | [영상](https://www.youtube.com/watch?v=W3AtQ9LvteU) · [script](../transcripts/2026-07-22/How_to_Implement_AX_The_Ultimate_Guide_for_Team_Leaders__W3AtQ9LvteU.md) |

### 프리세일즈랩 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 그래서 일단 세일즈 엔지니어들의 생산성 향상이 굉장히 좀 도움이 되고 있는 걸 어 볼 수가 있었고요. | 2 | [영상](https://www.youtube.com/watch?v=1EThrc_f49o) · [script](../transcripts/2026-07-25/AX_전략_세미나_발표_-_AI_전환의_다음_목적지,_Revenue_AI__1EThrc_f49o.md) |

### IQVIA (1건 · 데이터·컨텍스트·거버넌스 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | neutral | IBP 콜렉트와 IBP 흡입은 수작업으로 단편 [음악]화 된 보고서 비즈니스를 통합 한 지능형 워크플로우로 진화했습니다. | 2 | [영상](https://www.youtube.com/watch?v=fGQ7vYVsWQ8) · [script](../transcripts/channels/IQVIA/医薬品安全性情報の収集・インテイクの効率化を、高度に自動化された統合ワークフローで実現するIQVIA_IVP_Colle__fGQ7vYVsWQ8.md) |

### LinkedIn (1건 · 엔터프라이즈 앱 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-05 | anti_washing | 저희가 도입하려고 했던 고객 시스템은 , 이 프로젝트를 진행하게 된 이유는 고객 서비스 담당자들의 통화 대기 시간이 너무 길었기 때문입니다. | 2 | [영상](https://www.youtube.com/watch?v=8NDPNAP0L14) · [script](../transcripts/channels/LinkedIn/Successful_Interview_Strategies_How_to_Answer_Any_Question_Y__8NDPNAP0L14.md) |

### Stability AI (1건 · 생성 미디어 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | neutral | 그리고 이 분에게는 아웃페인트 워크플로우를 적용할 수 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=evivLLoXGY0) · [script](../transcripts/channels/Stability_AI/How_to_put_together_your_first_workflow_in_Brand_Studio__evivLLoXGY0.md) |


## 5. S1 digitization(전산화) — 사례 28건 / 18개 회사·채널

회사(채널)별로 단계 신호가 강한 순으로 최대 3건씩. 근거 문장은 **행동 동사가 든 문장**만 뽑았다(일반론 배제). 전량은 `analysis/verhoef_stages.csv` 참조.

### Siemens (4건 · 물리 AI·자율주행 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 또한 주주들에게도 이익을 제공해야 하므로 , 혁신적인 순환 과정에서 디지털화를 추진하는 것은 공급망 생산성을 향상시키고 회사에 비용 절감을 가져다줄 뿐만 아니라 혁신을 통해 해당 카테고리에 새로운 변화를 가져올 수 있는 기회를 제공합니다. | 3 | [영상](https://www.youtube.com/watch?v=-B__O2eqRYc) · [script](../transcripts/channels/Siemens/AI-Based_Process_Control_at_Scale_Pringles_and_Siemens_on_Di__-B__O2eqRYc.md) |
| 2026-06 | neutral | 이를 통해 생명과학 산업의 디지털화 선두주자인 로슈는 수백만 달러의 비용 절감을 실현할 수 있었습니다. | 2 | [영상](https://www.youtube.com/watch?v=904bgIMDVbk) · [script](../transcripts/channels/Siemens/Simulation-Driven_Planning_in_Pharma_Roche_Project_Apollo__904bgIMDVbk.md) |
| 2026-07 | neutral | 그러므로 중소기업들이 디지털화와 인공지능 도입에 발맞춰 나갈 수 있도록 지원하는 것이 성공의 원동력이 될 것입니다. | 2 | [영상](https://www.youtube.com/watch?v=noO0bsrzR3U) · [script](../transcripts/channels/Siemens/Why_Latin_America_Matters_Globalization,_SMEs,_and_AI_Adopti__noO0bsrzR3U.md) |

### GE HealthCare (3건 · 수요기업·기타 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | anti_washing | 하지만 인공 지능이 우리가 스캔하는 부위에 대한 기본적인 해부학적 이해를 대체해서는 안 된다는 점을 아무리 강조해도 지나치지 않습니다. | 6 | [영상](https://www.youtube.com/watch?v=miUbiJp3t2o) · [script](../transcripts/channels/GE_HealthCare/AI_in_Regional_Anesthesia_Smarter_Ultrasound_Guidance__miUbiJp3t2o.md) |
| 2026-02 | neutral | 기술자와 간호사가 서로 연결되지 않은 종이 기반 워크플로를 사용하는 경우, 증가하는 경보 부담에 대처하기 위해 자원을 신속하게 동원하는 데 어려움을 겪을 수 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=-mytTR4lhTU) · [script](../transcripts/channels/GE_HealthCare/Digital_CMU_Care_that_can_respond_to_the_moments_that_matter__-mytTR4lhTU.md) |
| 2026-06 | anti_washing | 그래서 이제 SPECT CT 스캔과 같은 방법을 통해 방사선량을 어디에 전달하는지 확인할 수 있게 되면서, 방사성 의약품 치료가 방사선 종양학에서 우리가 가장 익숙한 분야인 치료 계획 수립에 적용될 수 있게 되었습니다. | 2 | [영상](https://www.youtube.com/watch?v=NeDgw9PTrcg) · [script](../transcripts/channels/GE_HealthCare/Converging_Beams_Radiation_Therapy_meets_Radioligand_Therapy__NeDgw9PTrcg.md) |

### Schneider Electric (3건 · 인프라·칩·전력 · FR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 디지털화로 나아가 말씀하신 이점을 누리려면 고품질 데이터가 필요한데, 현재 이용 가능한 데이터의 80%가 고객에 의해 활용되지 않고 있습니다. | 5 | [영상](https://www.youtube.com/watch?v=xjFSF4jCvpk) · [script](../transcripts/channels/Schneider_Electric/End_of_Islands_-_Unified_Asset_Lifecycle_is_the_Digital_Fabr__xjFSF4jCvpk.md) |
| 2026-07 | neutral | 저희의 독보적인 노하우는 음악 분야에 전력화 및 디지털화 기술을 대규모로 적용하는 데 있으며, 이를 저희 스스로 시작하여 고객과 공급업체까지 확대해 나가고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=na6ZRJOgJQM) · [script](../transcripts/channels/Schneider_Electric/Impact_2030_The_Cycle_-_A_film_about_our_sustainability_jour__na6ZRJOgJQM.md) |
| 2026-07 | anti_washing | 음, 이러한 대규모 건설 프로젝트의 디지털화, 자동화 및 운영 인텔리전스에 대해 논의할 시간을 갖고 있습니다 . | 2 | [영상](https://www.youtube.com/watch?v=lWYUvDXnudc) · [script](../transcripts/channels/Schneider_Electric/Powering_the_AI_factory_-_The_grid-to-chip_journey_Schneider__lWYUvDXnudc.md) |

### NVIDIA Developer (2건 · 인프라·칩·전력 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-06 | neutral | 기본 차원 축소 및 클러스터링 방식 대신, UMAP을 이용한 차원 축소와 HTTP 스캔을 이용한 클러스터링을 통해 성능을 향상시켰습니다. | 8 | [영상](https://www.youtube.com/watch?v=8TBaLWvJBuE) · [script](../transcripts/channels/NVIDIA_Developer/Reduce_Noise_and_Improve_BERTopic_Results_with_GPU-Accelerat__8TBaLWvJBuE.md) |
| 2025-04 | anti_washing | 그리고 아시다시피, 그들은 여러 세대에 걸쳐 완전히 아날로그 방식의 신경망을 구축했고, 그 후 아날로그와 디지털 방식을 혼합하다가 90년대 중반에 이르러서는 완전히 디지털 방식으로 전환했습니다. | 4 | [영상](https://www.youtube.com/watch?v=eyrDM3A_YFc) · [script](../transcripts/channels/NVIDIA_Developer/Frontiers_of_AI_and_Computing_A_Conversation_With_Yann_LeCun__eyrDM3A_YFc.md) |

### Weaviate (2건 · 데이터·컨텍스트·거버넌스 · NL)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-02 | anti_washing | 지금 AI 스타트업들이 가장 주목하는 혁신 분야 중 하나는 OCR 전사 레이어의 비용을 절감하는 것이라고 할 수 있습니다. | 5 | [영상](https://www.youtube.com/watch?v=BzEV2gGtmKw) · [script](../transcripts/channels/Weaviate/IRPAPERS_Explained!__BzEV2gGtmKw.md) |
| 2025-11 | neutral | 그래서 그 계획을 논리적으로 표현하자면, 먼저 모든 연구 논문을 훑어보는 스캔 과정을 거치고, 그 다음에는 필터를 적용하는 필터링 과정을 거치는 것입니다. | 4 | [영상](https://www.youtube.com/watch?v=koPBr9W4qU0) · [script](../transcripts/channels/Weaviate/Semantic_Query_Engines_with_Matthew_Russo_-_Weaviate_Podcast__koPBr9W4qU0.md) |

### Huawei (2건 · 인프라·칩·전력 · CN)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-04 | neutral | 예를 들어, 셰이크 안타 디옵 공과대학교는 첨단 기술을 바탕으로 과학 연구를 위한 데이터베이스 확장 , 교육을 위한 가상 머신의 유연한 배포, 이러닝 플랫폼 업데이트의 기반 마련, 그리고 전자 문서 워크플로 자동화 구현 등 더 많은 디지털화 기회를 모색할 수 있게 되었습니다. | 3 | [영상](https://www.youtube.com/watch?v=0sZoZTHy5u8) · [script](../transcripts/channels/Huawei/IT_Infrastructure_Is_Powering_Data‑Driven_Universities__0sZoZTHy5u8.md) |
| 2026-07 | neutral | 또한, 우리가 추진하고 있는 디지털화의 일환으로 병원에는 풍부한 데이터가 있기 때문에 데이터 기반 의사결정 시스템을 도입하고자 합니다. | 3 | [영상](https://www.youtube.com/watch?v=Fii9aqiUUVk) · [script](../transcripts/channels/Huawei/How_Digital_Infrastructure_Brings_Cardiac_Care_to_Rural_Area__Fii9aqiUUVk.md) |

### Cohere (1건 · 파운데이션 모델 · CA)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-01 | anti_washing | 보시다시피, 저희 성능은 초점 스캔을 통해 지속적으로 향상되고 있습니다 . | 8 | [영상](https://www.youtube.com/watch?v=nugtUgq014w) · [script](../transcripts/channels/Cohere/Yingsi_Qin_-_Spatially_Varying_Autofocus__nugtUgq014w.md) |

### Arm (1건 · 인프라·칩·전력 · UK)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | anti_washing | 그래서 저희는 가나 보건 서비스와 협력하여 그들이 모든 것을 디지털화할 수 있도록 이 플랫폼을 구축하는 것을 돕고 있습니다. | 7 | [영상](https://www.youtube.com/watch?v=vQBRR7c_8IM) · [script](../transcripts/channels/Arm/Arm_Viewpoints_How_AI_and_biometrics_are_powering_equitable___vQBRR7c_8IM.md) |

### GitHub (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-01 | neutral | " 일단 이걸 공개하면 , WEBP 이미지를 대규모로 스캔할 수 있도록 백그라운드에서 필요한 서비스를 구축해둬야 할 거야." 어, 그래서 일단 그게 마련되니까 , 마치 "좋아, 완벽한 타이밍이었어"라는 생각이 들었죠. | 6 | [영상](https://www.youtube.com/watch?v=DW_vw8BkcBU) · [script](../transcripts/channels/GitHub/GitHub’s_year_in_review_accessibility,_MCP,_and_tiny_wins_Ep__DW_vw8BkcBU.md) |

### IBM Technology (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-05 | anti_washing | 더 빠른 스캔, 더 빠른 패치, 대응 주기 단축이 중요했습니다. | 4 | [영상](https://www.youtube.com/watch?v=ftUlJzuzdU4) · [script](../transcripts/channels/IBM_Technology/First_findings_from_Project_Glasswing__ftUlJzuzdU4.md) |

### Upstage (1건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-04 | neutral | 여러분이 가진 열정과 전문성을 통해 업 스테이지와 함께 미래를 만들어 나갈 수 있길 진심으로 기원하며 여러분의 도전을 [음악] 응원합니다 안녕하세요 업스테이지 AI 솔루션 매니저 팀 리더 권민찬 있니다 이전에는 테크 기업과 금융사에서 커리어를 싸고요 업스테이지 조인한지는 10개월 정도 되었습니다 안녕하세요 저는 업스테이지 AI 솔루션 매니저 팀에서 PM 역할을 수행하고 있는 제입니다 저는 업스테이지 양한 프로젝트의으로써 고객사의 성공을 돕는 역할을 수행하고 있습니다 업 스테이지에 AI 솔루션 매니저는 프로젝트의 성공과 고객 만족을 … | 3 | [영상](https://www.youtube.com/watch?v=0CgJPwfESZw) · [script](../transcripts/channels/Upstage/고객의_성공은_곧_우리의_성공!_💪ㅣAI_스타트업ㅣ업스테이지ㅣ채용ㅣ취업__0CgJPwfESZw.md) |

### Microsoft Developer (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-06 | neutral | 에이전트, 테넌트, 파일 버전별로 필터링된 레코드에 직접 접근하는 인덱스 스캔 작업 덕분에 성능이 크게 향상되었습니다. | 3 | [영상](https://www.youtube.com/watch?v=RN5FgORdS6Y) · [script](../transcripts/channels/Microsoft_Developer/Production_RAG_at_Scale_with_Azure_Database_for_PostgreSQL_P__RN5FgORdS6Y.md) |

### AWS Developers (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2024-10 | neutral | Amazon Q 개발자 메뉴를 열고 팝업 메뉴에서 "프로젝트 스캔 실행"을 선택합니다. | 3 | [영상](https://www.youtube.com/watch?v=dCNQdzEEBG8) · [script](../transcripts/channels/AWS_Developers/Time-saving_Software_Development_Tips_in_VS_Code__dCNQdzEEBG8.md) |

### LG AI Research (1건 · 파운데이션 모델 · KR)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2022-12 | anti_washing | [음악] 안녕하세요 LG AI 연구원의 머티리얼 인포머틱스 랩을 맡고 있는 한세희입니다 오늘은 사이언티픽 디스커버리 분야에서 ai가 만들어가는 변화와 그동안의 연구 성과에 대해 말씀드리겠습니다 광학과 전자계약 기술의 집약체인 망원경이 인간의 시야와 세상을 확장해 주었고 천문학이나 천체물류학과 같은 새로운 과학의 폭발적인 발전을 가져왔습니다 마찬가지로 데이터와 신경망에 대한 연구로 탄생한 인공지능이 또 다른 사이언티픽 리서치의 발전에 기여할 수 있다고 생각합니다 신소재 개발 분야의 관점에서 살펴보겠습니다 일반적으로 화학자들이 소재 개… | 2 | [영상](https://www.youtube.com/watch?v=5Pen3g0HmWA) · [script](../transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2022_Expert_AI_Applications_for_Scientifi__5Pen3g0HmWA.md) |

### 중소벤처기업부 (1건 · 키워드검색)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | neutral | 이게 AI를 도입을 한다는 거에 있어서는 결국에는 공장에 있는 오프라인 정보들이 온라인상 혹은 디지털화가 돼야 되는 거잖아요. | 2 | [영상](https://www.youtube.com/watch?v=mUAndx0F8I0) · [script](../transcripts/2026-07-30/작은_공장도_바로_적용_가능!_현장에서_검증된_AI_도입,_디지털_전환_공식🤖_(feat.스마트제조혁신3.0__mUAndx0F8I0.md) |

### AWS Events (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-07 | anti_washing | 플랫폼팀은 물론 인프라도 볼 수 있지만, 예, 개발 때문에, CD 파이프 라인 관리에서 있거나 보안 스캔 설계 있다든가, 운용 감시의 방식이라든가 , 글쎄, 그런 것들도 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=kamNuuevbno) · [script](../transcripts/channels/AWS_Events/Tokyo_Executive_Forum_2026_-_A_Leader's_Guide_to_Cloud-Nativ__kamNuuevbno.md) |

### BMW (1건 · 물리 AI·자율주행 · DE)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2026-03 | neutral | 저희는 모든 시스템과 차량을 실제 교통 상황에서 테스트하지만, 개발 과정에서 항상 디지털화를 우선시합니다. | 2 | [영상](https://www.youtube.com/watch?v=hY8e0CJH70Q) · [script](../transcripts/channels/BMW/Innovation_Insights_BMW_Driving_Simulation_Centre__hY8e0CJH70Q.md) |

### Meta Developers (1건 · 에이전트·개발도구 · US)

| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |
|---|---|---|---:|---|
| 2025-10 | anti_washing | 네 , 그러니까 아까 말씀드렸듯이 다음 강의 때는 잠시 방을 나갔다가 다시 들어오셔야 스캔 후 크레딧을 적용해 드릴 수 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=BTkWwoIS89E) · [script](../transcripts/channels/Meta_Developers/Small_Screen,_Big_Impact_Building_Mobile-First_Worlds_on_Met__BTkWwoIS89E.md) |


## 6. S4c — 3단계로 담기지 않는 잔여 (AX 위치 논쟁용) · 28건

의사결정의 알고리즘화·자율 에이전트·AI 인력화를 말하는 사례다. Verhoef의 S3(비즈니스 모델 전환)와 **겹치는지 남는지**가 'AX = DX의 제4단계인가, 질적으로 다른 전환인가' 논증의 경험적 근거가 된다. 아래가 전량이다.

| 회사·채널 | 월 | 배정 단계 | 톤 | 근거 문장 | 신호 | 출처 |
|---|---|---|---|---|---:|---|
| SAP | 2026-05 | S2 digitalization(디지털화) | anti_washing | And today, I'm super proud to launch our new SAP Business AI Platform, which forms the basis for our vision of the future of business, the Autonomous Enterprise where agents run the business and you can focus on what really matters. | 15 | [영상](https://www.youtube.com/watch?v=CocpyxAizwE) · [script](../transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Madrid_2__CocpyxAizwE.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | anti_washing | 이러한 공간들은 독특하고, 상황에 맞춰 설계되었으며, 당면한 과제를 위해 구축되었고, 결과 중심적이며, 인간과 자율 에이전트가 조화롭게 협력하는 공간입니다 . | 8 | [영상](https://www.youtube.com/watch?v=9aa-etRsaLU) · [script](../transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Orlando___9aa-etRsaLU.md) |
| AI:ROI Conversations with Section | 2026-08 | S3 digital transformation(디지털 전환) | anti_washing | It'll just be a net cut in terms of headcount. | 6 | [영상](https://www.youtube.com/watch?v=20lqu-d4cxc) · [script](../transcripts/2026-08-03/Closing_the_Enterprise_AI_ROI_Gap__20lqu-d4cxc.md) |
| Google Cloud Tech | 2026-06 | S2 digitalization(디지털화) | neutral | 자율 에이전트에 대해 이야기할 때, 특히 지난주에 많이 언급되었던 에이전트 개발 키트(ADK)에 대해 이야기하자면, 저희는 1년 전에 이를 발표했고, 오늘날의 모습으로 발전하는 데 큰 역할을 했습니다. | 6 | [영상](https://www.youtube.com/watch?v=nfCTJN42LyE) · [script](../transcripts/channels/Google_Cloud_Tech/Enable_autonomous_data_agents_with_BigQuery_and_Cloud_Run__nfCTJN42LyE.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | anti_washing | 하지만 개별 사용 사례에서 벗어나 생각해 보면, 어제 크리스티안이 언급했듯이 , 이러한 에이전트 기반 워크플로우를 구축하면서 연결된 자율 기업을 실제로 만들어낼 수 있다는 점이 매우 흥미롭습니다. | 6 | [영상](https://www.youtube.com/watch?v=dG9aBkJCcso) · [script](../transcripts/channels/SAP/Customer_Success_Keynote_Connected_to_Win_From_Moment_to_Mom__dG9aBkJCcso.md) |
| SAP | 2026-05 | S3 digital transformation(디지털 전환) | anti_washing | 저희는 1억 달러를 투자하여 자율 기업으로 전환할 때 업계를 선도하는 데 필요한 전문 지식과 공동 혁신 역량을 확보할 수 있도록 지원하고 있습니다 . | 5 | [영상](https://www.youtube.com/watch?v=WpDHkeHIezc) · [script](../transcripts/channels/SAP/Customer_Success_Keynote_Connected_to_Win_From_Moment_to_Mom__WpDHkeHIezc.md) |
| Tigerhall | 2026-07 | S2 digitalization(디지털화) | anti_washing | 그러니까 FTE 주(근무 시간 기준)로 환산했을 때 효율성과 소요 시간 변화는 많은 경우 90%까지 감소합니다. | 5 | [영상](https://www.youtube.com/watch?v=OJwpw-8SkBM) · [script](../transcripts/2026-07-26/AI_for_AI_Building_the_Transformation_Office_That_Drives_Ent__OJwpw-8SkBM.md) |
| NVIDIA Developer | 2026-06 | unassigned | anti_washing | Um and CrowdStrike is starting to build autonomous agents to help with security operations centers do, you know, automatic triage of uh of alerts so that they can help security analysts understand uh what might be a false positive and which which issues that they might need to d- dig deeper on. | 5 | [영상](https://www.youtube.com/watch?v=NHVtXHUcVXE) · [script](../transcripts/channels/NVIDIA_Developer/Long-Running_AI_Agents_The_Next_Breakthrough_in_Enterprise_W__NHVtXHUcVXE.md) |
| NVIDIA | 2026-06 | S2 digitalization(디지털화) | anti_washing | 또 다른 예로, 저희는 새로운 추천 알고리즘을 출시했는데, 그 결과 매장 매출이 1% 이상 증가하는 절대적인 개선을 보였습니다. | 3 | [영상](https://www.youtube.com/watch?v=Alz-bhXqyXM) · [script](../transcripts/channels/NVIDIA/Inside_Instacart's_AI-Powered_Smart_Shopping_Cart_NVIDIA_AI___Alz-bhXqyXM.md) |
| DATAVERSITY | 2026-08 | S2 digitalization(디지털화) | anti_washing | 앞서 언급했듯이 회의적인 시각도 있지만, 챗봇에서 자율 에이전트로의 전환이 있었습니다. | 3 | [영상](https://www.youtube.com/watch?v=JhbsIutTwXM) · [script](../transcripts/2026-08-03/Analythics_Architecture_Promising_AI_Use_Cases_for_the_Enter__JhbsIutTwXM.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | neutral | 저는 이것이 자율 기업을 위한 에이전트를 구축하는 데 있어 판도를 바꾸는 계기가 될 것이라고 생각합니다 . | 3 | [영상](https://www.youtube.com/watch?v=6NtRz1d4Qqs) · [script](../transcripts/channels/SAP/Global_Keynote_Highlights_Reimagined_Joule,_AI,_&_More_in_6___6NtRz1d4Qqs.md) |
| Weights & Biases | 2025-12 | S2 digitalization(디지털화) | anti_washing | 현재 많은 재고 관리가 자동화된 자율 에이전트에 의해 이루어지고 있는데, 이 에이전트들은 특정 접근 권한을 가지고 재고 관리를 수행합니다. | 3 | [영상](https://www.youtube.com/watch?v=4_BybRqrYcc) · [script](../transcripts/channels/Weights_&_Biases/Understanding_the_new_AI_tech_stack_Infrastructure,_models,___4_BybRqrYcc.md) |
| AWS Events | 2026-06 | S2 digitalization(디지털화) | anti_washing | 한 번의 개발 세션에서 작업하는 대신, 시간이 지남에 따라 Kira 자율 에이전트는 워크플로와 함께 지속적으로 실행됩니다. | 3 | [영상](https://www.youtube.com/watch?v=CprBATdRoh0) · [script](../transcripts/channels/AWS_Events/AWS_Summit_Bengaluru_2026_Innovators_Edition_Keynote_AWS_Eve__CprBATdRoh0.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | neutral | 당사의 새로운 AI 플랫폼은 자율 운영 솔루션 제품군과 함께 귀사를 자율 운영 기업으로 전환할 수 있는 기능을 제공합니다 . | 3 | [영상](https://www.youtube.com/watch?v=CMHCTgnroa0) · [script](../transcripts/channels/SAP/AI_Adoption_with_SAP_RISE_and_GROW_SAP_Sapphire_Orlando_2026__CMHCTgnroa0.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | neutral | 자율 기업은 인공 지능, 자율 프로세스 및 에이전트를 고객의 비즈니스 환경에 도입하여 실질적인 가치를 창출하고, 단순히 있으면 좋은 기술적 구현이나 개념 증명(POC) 수준을 넘어설 수 있도록 하는 다음 단계의 도약입니다. | 3 | [영상](https://www.youtube.com/watch?v=Ou_Q9mM_jFo) · [script](../transcripts/channels/SAP/Inside_SAP_Sapphire_2026_Joule_Studio_and_Autonomous_Enterpr__Ou_Q9mM_jFo.md) |
| Salesforce | 2026-07 | S2 digitalization(디지털화) | neutral | [음악] 이는 인간, 자율 에이전트, 그리고 귀사가 이미 매일 사용하는 도구들이 [음악] 개발 단계에만 머무르는 멋진 시범 프로젝트가 아닌, 실제 운영에 바로 적용 가능한 결과물을 제공할 수 있도록 격차를 해소합니다 . | 3 | [영상](https://www.youtube.com/watch?v=XjQfm2618t4) · [script](../transcripts/channels/Salesforce/Enterprise_Agentic_AI_Architecture_Explained_with_Tiff_in_Te__XjQfm2618t4.md) |
| ServiceNow | 2026-05 | S2 digitalization(디지털화) | neutral | 또한 기업에 자율 운영을 도입하는 방식과 관련하여 파트너십을 크게 확장했다고 발표했습니다 . | 3 | [영상](https://www.youtube.com/watch?v=q8kaVEkTWho) · [script](../transcripts/channels/ServiceNow/The_Blueprint_for_Agentic_Business_ServiceNow_Knowledge_2026__q8kaVEkTWho.md) |
| Salesforce | 2026-04 | S2 digitalization(디지털화) | anti_washing | Agent Force helps IT departments scale and be efficient without adding headcount while reducing resolution time. | 3 | [영상](https://www.youtube.com/watch?v=p0fNwmKUkvU) · [script](../transcripts/channels/Salesforce/Scale_Mission_Impact_with_Data_and_AI_Agentic_Government__p0fNwmKUkvU.md) |
| Salesforce | 2025-12 | S2 digitalization(디지털화) | neutral | AgentForce를 출시한 지 불과 1년 반 만에 현재 12,000명의 고객이 Agentic Enterprise로 거듭나기 위한 여정에 동참했습니다 . | 2 | [영상](https://www.youtube.com/watch?v=sSIB8rZTkew) · [script](../transcripts/channels/Salesforce/Agentforce_World_Tour_NYC_Main_Keynote_2025_Salesforce__sSIB8rZTkew.md) |
| TCS | 2026-01 | unassigned | neutral | 에이전트를 활용하고 있기 때문에 의사결정 자동화가 폭발적으로 성장하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=tHeXimKdKLA) · [script](../transcripts/channels/TCS/Navigating_the_Future_of_Tech_with_Dr_Harrick_Vin,_Ray_Wang,__tHeXimKdKLA.md) |
| Telenor | 2021-02 | S3 digital transformation(디지털 전환) | neutral | i'm so pleased to be here together with um uh you marcus lavik the ceo and i think you're the founder also of uh knight uh uh larry thank you for joining yeah sure thanks a lot for you know for having me i think when i'm thinking about very successful startups in norway and when i'm thinking about t… | 2 | [영상](https://www.youtube.com/watch?v=0mdPRkxm12U) · [script](../transcripts/channels/Telenor/Sigve_Brekke_discusses_the_Digitalisation_of_Industry_with_C__0mdPRkxm12U.md) |
| 손에잡히는경제 | 2026-08 | S2 digitalization(디지털화) | neutral | 그러니까 기업들이 경영란을 겪고 있어서 직원들을 자르는게 아니고 앞으로 AI가 일자리를 대체할 거를 미리 예측을 해 가지고 선재적으로 인력 감축을 하고 있다라는 겁니다. | 2 | [영상](https://www.youtube.com/watch?v=4-lOvLaVWSA) · [script](../transcripts/2026-08-03/Why_Companies_Are_in_Trouble_After_Relying_on_AI_for_Layoffs__4-lOvLaVWSA.md) |
| SAP | 2026-05 | S2 digitalization(디지털화) | neutral | 흥미로운 점은 이러한 에이전트 기반 워크플로우를 구축하면서 실제로 연결된 자율 기업을 어떻게 만들 수 있는지 확인할 수 있다는 것입니다. | 2 | [영상](https://www.youtube.com/watch?v=rxAVv6aRyhg) · [script](../transcripts/channels/SAP/Customer_Success_Keynote_Highlights_AI,_Joule,_and_More_in_9__rxAVv6aRyhg.md) |
| Snowflake | 2026-06 | S3 digital transformation(디지털 전환) | anti_washing | My new venture twine is building AI employee who execute complex cyber task from A to Z. | 2 | [영상](https://www.youtube.com/watch?v=Nm9JhTrcREQ) · [script](../transcripts/channels/Snowflake/The_2026_Snowflake_Startup_Challenge_Finale_with_Three_Visio__Nm9JhTrcREQ.md) |
| Google Developers | 2026-04 | S2 digitalization(디지털화) | anti_washing | 하지만 클라우드 측, 즉 백엔드 시스템 측에서도 에이전트 와 자율 에이전트를 실행하는 데 필요한 스킬들을 통합하고 있습니다. | 2 | [영상](https://www.youtube.com/watch?v=WYPdz3OZfuQ) · [script](../transcripts/channels/Google_Developers/Fireside_chat_on_an_agentic_simulation_Race_Condition__WYPdz3OZfuQ.md) |
| LG AI Research | 2020-12 | unassigned | anti_washing | 안녕하세요 lg ai 연구한 데이터 인텔리전스 데브리 더 임무 형입니다 오늘은 lga 아 연구한 출범에 맞춰 저희 레비 하고 있는데 그리고 추구하는 연구 방향에 대해 소개해드리려고 합니다 말씀드릴 내용은 다음과 같습니다 먼저 저희 레벨 미션과 비전을 설명드리고 진행하고 있는 연구 분야를 말씀드리고 관련된 과제 들도 함께 말씀드리도록 하겠습니다 현재 주목받고 있는 인공지능은 음성인식 영상인식 언어이해 가상 비서 자율주행 과 같은 것들이 있습니다 예전에 비해서는 매우 획기적인 개선이 이루어 졌고 실제로 더 많이 사용되기 시작했는데요 하… | 2 | [영상](https://www.youtube.com/watch?v=4oLL1W5MxFc) · [script](../transcripts/channels/LG_AI_Research/Data_Intelligence_Lab_-_Woohyung_Lim_(임우형)__4oLL1W5MxFc.md) |
| Cole Medin | 2026-07 | unassigned | anti_washing | So, he deployed an autonomous agent for customer onboarding. | 2 | [영상](https://www.youtube.com/watch?v=OcTMwjqje5Q) · [script](../transcripts/2026-07-21/The_Complete_AI_Transformation_Blueprint_-_Live_Workshop__OcTMwjqje5Q.md) |
| Hugging Face | 2022-04 | unassigned | anti_washing | 여기서 이의 제기 가능성이란 누군가가 자동화된 의사 결정 시스템에 의해 단독으로 권한을 부여받지 못했을 때, 이의를 제기하고 문제를 제기할 수 있는 능력을 의미합니다. | 2 | [영상](https://www.youtube.com/watch?v=dsCI22jbhLc) · [script](../transcripts/channels/Hugging_Face/AI_Ethics_Around_Machine_Learning_Datasets_and_Models_-_Emil__dsCI22jbhLc.md) |

## 7. 한계와 사용법

1. **규칙 기반 1차 태깅**이다. 문맥·반어·부정을 완전히 잡지 못하고, 자동자막
   오인식('음악' 치환 등)이 마커를 훼손할 수 있다. 신호는 대리지표로만 쓴다.
2. **발화 주체**가 벤더 홍보인지 도입 기업 증언인지는 `source`(channel=vendor /
   keyword=media)까지만 자동 구분된다. 사례로 인용하려면 원문 확인이 필요하다.
3. **담론이지 실제 비용구조가 아니다.** "했다고 말한 것"의 집계이므로, K1(기업
   공개 자료)·인터뷰와의 삼각검증 없이는 성과 주장으로 읽을 수 없다.
4. **Verhoef의 프레임 자체가 2018년까지의 문헌**에 기반한다(생성형 AI 이전).
   이 코퍼스(2020–2026)를 그 프레임으로 읽을 때는 시점 한계를 명시해야 한다 —
   S4c 축을 따로 둔 이유다.
5. 단계 배정은 **상위 우선**이라 S3 신호가 2회 이상이면 S2/S1 신호가 더 많아도
   S3로 간다. 누적성 가정을 검증하려면 `stage_mix`와 원점수(`s1_*`·`s2_*`·`s3_*`)를
   직접 보라.
