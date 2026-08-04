# Vial(2019) DT 프레임워크 대응 사례 목록

> 자동 생성: `python map_vial.py` · 근거 문헌: Vial, G. (2019). Understanding digital transformation: A review and a research agenda. *JSIS, 28*(2), 118–144.

> 코퍼스 9,409건 전량을 8개 구성요소(B1–B8) + AX 교량 3축(X1–X3)으로 규칙 기반 태깅 → **사례 582건**(그 중 연구 주표본 ax_core 523건).

> 기계 판독본: `analysis/vial_cases.csv`(태깅 전량) · `analysis/vial_evidence.csv`(구성요소별 근거 문장).


---

## 1. 코딩 규칙

| 축 | 구성요소 | 판정 |
|---|---|---|
| B1 | 디지털·AI 기술의 활용 | 사전 적중 ≥2회 |
| B2 | 파괴: 소비자 행동·기대 | 사전 적중 ≥2회 |
| B2 | 파괴: 경쟁구도 | 사전 적중 ≥2회 |
| B2 | 파괴: 데이터 가용성 | 사전 적중 ≥2회 |
| B3 | 전략적 대응 | 사전 적중 ≥2회 |
| B4 | 가치제안 변화 | 사전 적중 ≥2회 |
| B4 | 가치네트워크·생태계 | 사전 적중 ≥2회 |
| B4 | 디지털 채널 | 사전 적중 ≥2회 |
| B4 | 민첩성·양손잡이 | 사전 적중 ≥2회 |
| B5 | 조직구조 변화 | 사전 적중 ≥2회 |
| B5 | 조직문화 변화 | 사전 적중 ≥2회 |
| B5 | 리더십·CDO/CAIO | 사전 적중 ≥2회 |
| B5 | 직무·역량 변화 | 사전 적중 ≥2회 |
| B6 | 장벽: 관성·저항 | 사전 적중 ≥2회 |
| B7 | 성과: 운영효율 | 사전 적중 ≥2회 |
| B7 | 성과: 조직성과 | 사전 적중 ≥2회 |
| B7 | 성과: 사회적 편익 | 사전 적중 ≥2회 |
| B8 | 부정 성과: 보안·프라이버시 | 사전 적중 ≥2회 |
| X1 | 정의 확장(DX→AX 계승) | 명시 문구 1회 이상, 또는 DX 어휘 ≥2 & AX 어휘 ≥2 동시 등장(복합 규칙) |
| X2 | Avenue 2 윤리·거버넌스 | 사전 적중 ≥2회 |
| X3 | Avenue 1 동적역량 | 사전 적중 ≥2회 |

- **사례(case) 채택**: 본문 200단어 이상 & 8개 블록 중 4개 이상 충족.
- **티어**: A = 블록 7개 이상 + 전략(B3) + 성과(B7/B8) → Vial 과정 사슬이 온전한 사례 · B = 블록 6개 · C = 블록 4~5개(부분 사례).
- 규칙 기반이라 문맥·반어를 완벽히 잡지 못한다(코드북 v2와 동일한 한계). 티어 A/B는 수기 검증 대상 후보 목록으로 쓰는 것이 정직하다.


---

## 2. 구성요소별 출현 분포

| 축 | 구성요소 | 전체 코퍼스 | 사례 내 | 사례 내 비율 |
|---|---|---:|---:|---:|
| B1 | 디지털·AI 기술의 활용 | 3,092 | 521 | 90% |
| B2 | 파괴: 소비자 행동·기대 | 460 | 201 | 35% |
| B2 | 파괴: 경쟁구도 | 193 | 116 | 20% |
| B2 | 파괴: 데이터 가용성 | 376 | 155 | 27% |
| B3 | 전략적 대응 | 377 | 220 | 38% |
| B4 | 가치제안 변화 | 61 | 27 | 5% |
| B4 | 가치네트워크·생태계 | 1,200 | 387 | 66% |
| B4 | 디지털 채널 | 87 | 39 | 7% |
| B4 | 민첩성·양손잡이 | 156 | 73 | 13% |
| B5 | 조직구조 변화 | 151 | 100 | 17% |
| B5 | 조직문화 변화 | 61 | 39 | 7% |
| B5 | 리더십·CDO/CAIO | 270 | 152 | 26% |
| B5 | 직무·역량 변화 | 404 | 195 | 34% |
| B6 | 장벽: 관성·저항 | 170 | 86 | 15% |
| B7 | 성과: 운영효율 | 733 | 320 | 55% |
| B7 | 성과: 조직성과 | 301 | 147 | 25% |
| B7 | 성과: 사회적 편익 | 87 | 27 | 5% |
| B8 | 부정 성과: 보안·프라이버시 | 902 | 303 | 52% |
| X1 | 정의 확장(DX→AX 계승) | 98 | 50 | 9% |
| X2 | Avenue 2 윤리·거버넌스 | 728 | 264 | 45% |
| X3 | Avenue 1 동적역량 | 903 | 252 | 43% |

### 티어 분포

| 티어 | 건수 | ax_core |
|---|---:|---:|
| A | 33 | 33 |
| B | 65 | 63 |
| C | 484 | 427 |

### 채널(기업)별 사례 수 상위 40

| 채널 | 사례 | A | ax_core |
|---|---:|---:|---:|
| McKinsey & Company | 39 | 0 | 37 |
| Weights & Biases | 37 | 0 | 30 |
| Zapier | 33 | 3 | 32 |
| Intel | 27 | 0 | 27 |
| Google Cloud Tech | 21 | 0 | 20 |
| Unilever | 20 | 0 | 20 |
| Pinecone | 19 | 0 | 15 |
| AWS Events | 18 | 1 | 18 |
| Cohere | 17 | 0 | 8 |
| IBM Technology | 16 | 0 | 12 |
| Weaviate | 16 | 0 | 11 |
| Databricks | 15 | 2 | 14 |
| Siemens | 15 | 1 | 14 |
| Snowflake | 15 | 3 | 14 |
| Salesforce | 12 | 0 | 12 |
| NVIDIA Developer | 12 | 0 | 11 |
| Microsoft Azure | 9 | 1 | 9 |
| Qdrant | 9 | 1 | 7 |
| SAP | 9 | 0 | 9 |
| NVIDIA | 7 | 0 | 7 |
| Microsoft | 7 | 0 | 5 |
| Hugging Face | 6 | 0 | 4 |
| Meta | 6 | 0 | 5 |
| Meta Developers | 6 | 0 | 5 |
| Palantir | 6 | 0 | 6 |
| Replit | 6 | 0 | 6 |
| ServiceNow | 5 | 2 | 4 |
| AMD | 5 | 0 | 5 |
| Oracle | 5 | 0 | 5 |
| Google Developers | 5 | 0 | 5 |
| NAVER Cloud | 5 | 0 | 2 |
| Orange | 5 | 0 | 5 |
| Schneider Electric | 5 | 0 | 4 |
| Infosys | 4 | 2 | 4 |
| Accenture | 4 | 0 | 3 |
| Anthropic | 4 | 0 | 3 |
| Telenor | 4 | 0 | 3 |
| Waymo | 4 | 0 | 4 |
| 티타임즈TV | 4 | 0 | 4 |
| Arm | 4 | 0 | 4 |

---

## 3. 티어 A — 과정 사슬이 온전한 사례 (33건, 전량)

> 기술 활용 → 파괴/전략 → 가치·구조 변화 → 성과까지 한 영상 안에서 이어지는 사례. Vial의 Fig. 1 과정 모형을 그대로 대입해 읽을 수 있다.


### The 7 Ways AI Adoption Fails in Enterprises — And How to Avoid Each One

- 채널: **AI Adoption Services, Webinars, and Keynotes** · 2026-08 · ko · 3,338단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B5·B6·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=J8CR3dY5lbo · 원문: `transcripts/2026-08-03/The_7_Ways_AI_Adoption_Fails_in_Enterprises_—_And_How_to_Avo__J8CR3dY5lbo.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 좋아하는 LLM 교재를 펴세요. |
| B2 파괴: 경쟁구도 | 그들은 경쟁자들이 사업 차질을 걱정하도록 내버려 두었다. |
| B3 전략적 대응 | Allin Intelligence는 제 경영진 및 이사회 고객을 위해 설계된 AI 관련 월간 특집 브리핑입니다 . |
| B5 조직구조 변화 | 홍보 효과는 좋지만 비용이 많이 드는 사일로를 만듭니다 . |
| B5 리더십·CDO/CAIO | 행동적 거버넌스, 새로운 유형의 리더십, 그리고 혁신 디자인. |
| B5 직무·역량 변화 | 릴리는 그들의 내부 AI로, '내부'라는 단어를 강조하며 , 94%의 도입률과 74%의 정기적인 사용률을 보였고, 1,900만 건의 문제를 해결했으며, 이제는 최종 채용 단계에서 AI에 대한 관심도를 기준으로 지원자를 선별합니다. |
| B6 장벽: 관성·저항 | 하지만 기존 사업은 레거시 기술, 레거시 브랜드, 레거시 제품, 기존 시장, 기존 리더의 사고방식 등 수많은 족쇄로 가득 차 있습니다. |
| B7 성과: 운영효율 | 투자 수익률(ROI)에서 아주 미미한 몇 퍼센트 포인트, 즉 0.1% 포인트 정도의 이득을 얻게 됩니다. |
| B7 성과: 조직성과 | 조종사와 부조종사를 영입하고, 아인슈타인의 매출을 늘리고, 이사회 분위기가 좋고, 주가도 좋아 보입니다. |
| B8 부정 성과: 보안·프라이버시 | 감시 체계는 파놉티콘과 같지만, 창의적인 호기심을 강요할 수는 없습니다. |

### Closing the Enterprise AI ROI Gap

- 채널: **AI:ROI Conversations with Section** · 2026-08 · en · 9,266단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=20lqu-d4cxc · 원문: `transcripts/2026-08-03/Closing_the_Enterprise_AI_ROI_Gap__20lqu-d4cxc.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | We know consumers love it and we know the ambitious amongst us and I would account you in that group understand that it's not just fun to chat with AI about you know relationships and and get get some free therapy free c… |
| B2 파괴: 경쟁구도 | I think there are three forces of disruption and there are probably many more but these are the three that I think matter most to me and I think most knowledge workers or knowledge work companies and they are the cost of… |
| B3 전략적 대응 | This is the basic AI strategy. |
| B4 민첩성·양손잡이 | They have to accept a lot of experimentation and therefore failure. |
| B5 리더십·CDO/CAIO | So of course they're not going to get the ROI and that's one of the gaps we have to close and we must close this leadership gap. |
| B5 직무·역량 변화 | I don't mean I don't mean reinvention but I think we'll we'll see um headcount move and organizations change. |
| B7 성과: 운영효율 | What we're today, what we're going to talk about is the ROI [snorts] gaps, the enterprise ROI gaps. |
| B8 부정 성과: 보안·프라이버시 | there are still uh you know constraints if you will or defects uh in the answers we're getting when you think about AI due to hallucinations but in general what we're seeing with customers and prospects is they they expe… |

### NYC Executive Forum 2026 - Leading Transformation When Technology Won’t Wait

- 채널: **AWS Events** · 2026-07 · ko · 3,675단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=-7VeuZfH0DM · 원문: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_Leading_Transformation_When_Techn__-7VeuZfH0DM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 생성형 AI와 Aentic AI는 개발 기간이 단축되었습니다. |
| B2 파괴: 소비자 행동·기대 | 구성 요소는 많지만, 이것이 바로 사용자 경험의 예시이며, 어떻게 하면 시민들의 삶을 더 나아지게 할 수 있을지에 대한 것입니다. |
| B3 전략적 대응 | 그들은 데이터 준비 상태에 대한 중요성을 높였고, 이사회와 경영진이 오늘날 묻고 있는 거버넌스, 인재, 투자와 관련된 완전히 새로운 질문들을 제기했습니다. |
| B4 가치네트워크·생태계 | 저는 데이터 AI 실험과 개발자 플랫폼 및 생태계를 총괄하는 엔지니어링 부사장입니다. |
| B4 디지털 채널 | 저희는 30개의 콜센터를 운영하고 있습니다. |
| B5 리더십·CDO/CAIO | 저희는 각 기관을 담당하는 27명의 기술 담당 부국장과 CTO, SISO, 최고 디지털 책임자 등과 같은 10개의 공유 서비스 직책을 두고 있습니다 . |
| B7 성과: 운영효율 | 음, 저는 또한 저희 AI 전환 프로젝트의 배송 책임자 중 한 명으로, 엔지니어와 직원들의 엔지니어링 효율성과 생산성을 향상시키는 역할을 맡고 있습니다. |
| B8 부정 성과: 보안·프라이버시 | 정책 의 이점은 이해하지만, 개인정보 보호 와 보안 문제도 고려해야 하기 때문입니다. |

### Webinar: AI transformation that works, lessons from the trenches

- 채널: **BOI (Board of Innovation)** · 2026-07 · ko · 6,165단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=PL3OWn143AI · 원문: `transcripts/2026-07-18/Webinar_AI_transformation_that_works,_lessons_from_the_trenc__PL3OWn143AI.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 제품 설명을 자동으로 생성하여 소셜 미디어에 게시해야 합니다. |
| B2 파괴: 소비자 행동·기대 | 소비자 행동 및 트렌드를 이해하고 고객을 파악하는 것과 같은 이러한 업무 범주를 통합하거나 축소할 수 있습니다. |
| B3 전략적 대응 | 네, 저는 AI 전략 담당 상무이사입니다. |
| B4 가치네트워크·생태계 | 예를 들어, 고객 경험에만 투자하고 공급망에는 투자하지 않는 식입니다 . |
| B4 디지털 채널 | 예를 들어, 콜센터 지원 혁신을 생각해 보겠습니다. |
| B5 조직구조 변화 | 음, 당신의 도구들은 좀 더 중앙집중화되어 있네요. |
| B5 리더십·CDO/CAIO | 야심찬 비전을 설정하면 사업 계획, 투자 방식, 그리고 리더십 방식이 완전히 달라지기 때문입니다 . |
| B7 성과: 운영효율 | 비용을 10% 절감하는 게 아닙니다 . |
| B8 부정 성과: 보안·프라이버시 | 첫 번째로, 성숙도 모델에 대해 간략히 이야기하고, 어떻게 그 성숙도 모델에 갇히게 되는지, 그리고 그 모델을 악용할 때 진정한 변화는 어떤 모습인지 살펴보겠습니다. |

### Enterprise AI Strategy and CEO Leadership, with McKinsey & Company | CXOTalk #851

- 채널: **CXOTalk** · 2026-08 · en · 7,836단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=uTRKdCY4HdE · 원문: `transcripts/2026-08-03/Enterprise_AI_Strategy_and_CEO_Leadership,_with_McKinsey_&_C__uTRKdCY4HdE.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | Another key consideration is risks.&nbsp;&nbsp; Boards, management teams, and CEOs are thinking&nbsp; about the risks of AI - unfettered access to it,&nbsp;&nbsp; use on the front line of generative AI. |
| B2 파괴: 경쟁구도 | Michael Krigsman: When we talk about&nbsp;&nbsp; leadership disruption is a crucial part of&nbsp; that. |
| B3 전략적 대응 | A third way to parse this is by considering the&nbsp;&nbsp; multi-year roadmap. |
| B4 가치네트워크·생태계 | Curt Strovink: I think maintaining optionality&nbsp;&nbsp; with partners is important, as we discussed&nbsp; earlier, because things are changing so rapidly.&nbsp;&nbsp; We have a group in our own firm with some of&nbsp;… |
| B4 민첩성·양손잡이 | There are probably several reasons why the&nbsp;&nbsp; softer skills historically weren't as focused&nbsp; on, but I think they've now come back into scope.&nbsp;&nbsp; Given the rapid changes in the world, I think the&n… |
| B5 조직문화 변화 | Finally, I'd say this is an area where you&nbsp;&nbsp; have to have a learning mindset. |
| B5 리더십·CDO/CAIO | I'm Michael Krigsman, and we are discussing&nbsp;&nbsp; leadership strategy and AI. |
| B7 성과: 운영효율 | That's crucial, because&nbsp; you can make investments too fast or too soon&nbsp;&nbsp; in one major area or partner, which can limit&nbsp; your strategic degrees of freedom downstream.&nbsp; I also think you need a stro… |
| B8 부정 성과: 보안·프라이버시 | Particularly in healthcare,&nbsp; she notes that the data used to train the models&nbsp;&nbsp; is biased, even "criminally biased" as she puts&nbsp; it. |

### AI Transformation Leader (AB-731) - Full Course - Pass The Exam!

- 채널: **Citizen Developer and Nathan Rose** · 2026-07 · ko · 10,042단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=Ox0m3iJG57M · 원문: `transcripts/2026-07-21/AI_Transformation_Leader_(AB-731)_-_Full_Course_-_Pass_The_E__Ox0m3iJG57M.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 반면 생성형 AI는 앞서 이야기했던 언어-의미 관계 모델(LLM)을 사용합니다. |
| B2 파괴: 데이터 가용성 | 그러면 머신은 작업을 수행하면서 시간이 지남에 따라 데이터를 수집하고 준비합니다. |
| B3 전략적 대응 | 이것은 단순히 에이전트 365에 관한 것이 아니라, 조직의 최고 경영진이 이 문제에 참여하여 우리 조직 에서 책임감 있는 AI가 어떤 모습인지 진정으로 정의해야 한다는 개념입니다 . |
| B4 가치네트워크·생태계 | 앞서 다양한 모델 유형에 대해 이야기했지만, 마이크로소프트 생태계 내에는 선택할 수 있는 다양한 대규모 언어 모델이 있습니다. |
| B4 디지털 채널 | 그러니까, 컨택센터, 서비스형 컨택센터를 생각해 보세요. |
| B5 조직구조 변화 | 거버넌스를 정의하자면 , 관리자와 같은 중앙 집중식 권한을 가진 조직이 에이전트 구축 및 관리, 조직 정책 시행, 에이전트 수명 주기 제어, 그리고 위험 감지 시 에이전트 및 도구의 사용 제한 또는 비활성화를 즉시 수행할 수 있도록 하는 것입니다 . |
| B5 리더십·CDO/CAIO | 마이크로소프트가 강조하는 주요 포인트 중 하나는 최고 경영진의 리더십입니다. |
| B7 성과: 운영효율 | 하지만 다시 한번 강조하지만, 비즈니스 리더의 입장에서 어떻게 하면 실제로 수익을 창출하고, 비용을 절감하고, 위험을 줄일 수 있을지에 대한 답을 찾아야 합니다. |
| B7 성과: 사회적 편익 | 챗봇이 있는데, 시각 장애인에게는 편리 하지만 시각 장애인에게는 도움이 되지 않거나, 청각 장애인에게도 도움이 되지 않는 경우가 있습니다 . |
| B8 부정 성과: 보안·프라이버시 | 그래서 ' 답변을 신뢰할 수 있을까?', ' 편향은 없을까?', '개인정보 보호 문제는 고려했나?', '출처를 명시했나?', '결과 도출 과정은 설명했나?'와 같은 질문을 많이 받게 될 겁니다. |

### Analythics Architecture:  Promising AI Use Cases for the Enterprise in 2026

- 채널: **DATAVERSITY** · 2026-08 · ko · 6,611단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B6·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=JhbsIutTwXM · 원문: `transcripts/2026-08-03/Analythics_Architecture_Promising_AI_Use_Cases_for_the_Enter__JhbsIutTwXM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 이 회사는 머신 러닝과 생성형 AI 예측 모델링을 제약 제조 파이프라인에 직접 통합하여 이 과정의 후처리 단계를 혁신하고 있습니다. |
| B2 파괴: 소비자 행동·기대 | 그래서 고객 기록이나 내부 비즈니스 컨텍스트 같은 정보를 입력한다고 해도, 근접성, 장소, 지역별 맥락, 예를 들어 특정 지역의 소비자 행동과 같은 요소에 대한 완전한 통찰력을 얻지 못할 수도 있다는 점을 생각해 봐야 합니다 . |
| B3 전략적 대응 | 전염병 대응 전략에 대해서는 예전에도 여러 번 이야기했지만, 우리 경영진은 AI 전략이 완벽하지 않다는 것을 인정해야 합니다 . |
| B4 가치네트워크·생태계 | 그래서 저희가 고객들이 이러한 격차를 해소하고 부족할 수 있는 데이터의 완전성을 확보하도록 돕는 방법은 바로 연결된 데이터 생태계를 구축하는 것입니다. |
| B6 장벽: 관성·저항 | AI에 대한 내부적인 저항은 거의 없습니다 . |
| B7 성과: 운영효율 | 이 모든 것을 하기 위해, 예를 들어 투자 수익률이 30% 증가했다는 것이 입증되었습니다 . |
| B8 부정 성과: 보안·프라이버시 | 이로 인해 정부의 집중적인 감시 와 EU AI법과 같은 엄격한 새로운 규정이 생겨났습니다. |

### Data + AI Summit Keynote 2026 | Day 1

- 채널: **Databricks** · 2026-06 · ko · 27,599단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B6·B8
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=Qux8E-L1mk8 · 원문: `transcripts/channels/Databricks/Data_+_AI_Summit_Keynote_2026_Day_1__Qux8E-L1mk8.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 자동 변환기를 사용하면 기존 데이터 웨어하우스에서 마이그레이션 온프레미스 또는 다른 곳에 있을 수 있는 것 클라우드에서 가능하며, 지금 바로 그렇게 할 수 있습니다. |
| B2 파괴: 소비자 행동·기대 | 정확히 어떤 일이 일어나고 있는지 개인화하세요 당신과 함께 혈당 수치와 인슐린 분비량을 조절하여 혈당을 조절합니다. |
| B2 파괴: 데이터 가용성 | 거대한 데이터베이스, 페타바이트, 그리고 당신 "저기, 이거 복제해 줄 수 있어?"라고 말할 수 있다. |
| B3 전략적 대응 | Databricks 이사회 회의. |
| B4 가치네트워크·생태계 | 여기에 모인 생태계는 바로 이것입니다. |
| B5 직무·역량 변화 | 저는 데이터 엔지니어링을 모두 하고 있습니다. |
| B6 장벽: 관성·저항 | 이 기기로 모든 운동을 할 수 있고, 이렇게 엄청난 저항을 만들어내는 것뿐이에요. |
| B8 부정 성과: 보안·프라이버시 | 비용 및 관리 통제권을 갖고 있으며 보안 문제는 해결됐는데, 그다음엔 어떻게 해야 할까요? |

### Developing and Deploying Databricks ai_parse_document for Intelligent Document Processing

- 채널: **Databricks** · 2025-12 · ko · 5,540단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: —
- 링크: https://www.youtube.com/watch?v=kH7p1lr4Be4 · 원문: `transcripts/channels/Databricks/Developing_and_Deploying_Databricks_ai_parse_document_for_In__kH7p1lr4Be4.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 저희 데이터베이스에는 수억 개의 행이 있는데, AI 파싱을 통해 좋은 결과를 많이 얻었고, 이를 통해 경영진에게 생성형 AI의 가치 제안을 보여주고 투자 대비 수익을 제시할 수 있었습니다. |
| B2 파괴: 데이터 가용성 | 저희의 목표는 AI를 사용하여 비정형 데이터를 빠르고 저렴하고 쉽게 처리하는 것입니다. |
| B3 전략적 대응 | 사실 이 제품은 데이터 브릭의 헥손 프로젝트에서 시작되었는데, 고객과 경영진으로부터 많은 관심을 받아서 지금의 제품을 만들게 되었습니다. |
| B4 가치제안 변화 | 저희 데이터베이스에는 수억 개의 행이 있는데, AI 파싱을 통해 좋은 결과를 많이 얻었고, 이를 통해 경영진에게 생성형 AI의 가치 제안을 보여주고 투자 대비 수익을 제시할 수 있었습니다. |
| B5 직무·역량 변화 | 그래서 음, 여기서 가장 멋진 점은 이 모든 것이 데이터 엔지니어들이 매우 익숙한 언어들과 아주 잘 통합된다는 것입니다. |
| B7 성과: 운영효율 | Aisha가 언급한 정확성과 비전 모델뿐만 아니라 비용 절감까지 고려했다는 점을 지적해 주셔서 정말 좋습니다. |
| B8 부정 성과: 보안·프라이버시 | 그런데, UI가 가끔씩 오작동하는 경우가 있다는 거 아시죠? |

### Enterprise AI: From Big Uncertainty to Massive ROI

- 채널: **ERP Suites | JD Edwards Insights** · 2026-08 · ko · 5,334단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: 정의 확장(DX→AX 계승)
- 링크: https://www.youtube.com/watch?v=FmcULDfEgvM · 원문: `transcripts/2026-08-03/Enterprise_AI_From_Big_Uncertainty_to_Massive_ROI__FmcULDfEgvM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 1980년대부터 2010년까지 머신러닝은 패턴을 찾아내고, 해로운 패턴뿐만 아니라 유익한 패턴까지 식별하는 능력에 많은 관심이 집중되었습니다. |
| B2 파괴: 소비자 행동·기대 | 하지만 몇 가지 패턴, 즉 고객 접점 프로세스, 마케팅, 판매, 고객 지원 등에서 제가 앞서 언급했던 것처럼 나타나는 패턴들이 있죠. |
| B3 전략적 대응 | 그렇다면 인공지능이 경영진에게 중요한 이유는 무엇일까요? |
| B4 가치네트워크·생태계 | 그리고 저는 유통 컨설턴트로서 항상 공급망 활용 사례를 강조해 왔습니다. |
| B5 리더십·CDO/CAIO | 음, CIO, CTO 같은 분들 말이죠? |
| B7 성과: 운영효율 | 효율성과 생산성 향상 측면에서. |
| B8 부정 성과: 보안·프라이버시 | 음, 아시 다시피 줄리도 언급했던 근접성 편향을 피하고, 더 큰 통찰력과 효율성, 그리고 비즈니스 가치를 얻는 것이 중요하죠. |

### Making AI Transformation Work: Avoiding the Mistakes from Digital Transformation

- 채널: **INSEAD** · 2026-07 · ko · 7,136단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B5·B6·B7·B8
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=CoPCP3f1DzM · 원문: `transcripts/2026-07-18/Making_AI_Transformation_Work_Avoiding_the_Mistakes_from_Dig__CoPCP3f1DzM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 퍼플렉시티나 챗 GPT 같은 대규모 언어 모델 도구들이 인터넷에 있는 모든 방대한 데이터를 이해하기 쉽게 만들어냈기 때문에 일반 대중에게는 마법처럼 느껴지는 것입니다. |
| B2 파괴: 소비자 행동·기대 | 고객 서비스 개인화에서 고객과의 개인적인 관계가 중요하지 않다는 점이 있습니다. |
| B2 파괴: 경쟁구도 | 하지만 제가 목격하고 있는 가장 큰 함정 중 하나는 , 모든 함정은 좋은 의도에서 비롯되지만, 제가 ' 파괴적 혁신의 함정'이라고 부르는 것입니다. |
| B2 파괴: 데이터 가용성 | 디지털 기술이 없으면 데이터를 수집할 수 없고, 데이터를 수집하지 못하면 그 안에 담긴 모든 가치를 제대로 활용할 수 없기 때문입니다. |
| B3 전략적 대응 | 같은 이야기를 전달할 수 없다면 경영진과 이사회가 뜻을 같이할 수 없고, 모두를 같은 방향으로 이끌고 나아가기가 매우 어렵습니다 . |
| B5 조직구조 변화 | 더 나은 것은 말씀하신 대로 내부적인 성격이 줄어들고 고객 중심적이며, 부서 간 장벽이 낮아지고, 때로는 실질적인 결과물을 가져오는 회의가 필요하다는 것을 의미합니다. |
| B5 리더십·CDO/CAIO | 네, 제 생각에는 리더십에서 시작된다는 뜻인 것 같아요 . |
| B6 장벽: 관성·저항 | 제가 보기에 가장 큰 함정은 사람들이 변화를 두려워한다는 점인데, 이는 바람직한 민감성입니다. |
| B7 성과: 운영효율 | 비용 절감은 물론 생산성 향상에도 기여합니다. |
| B7 성과: 조직성과 | 그러니까 만약 우리가 수익성을 확보하고 모든 기본 KPI가 그 두 가지 목표, 즉 수익성과 고객 만족이라는 목표에 부합하도록 구성되어 있다면, 그 목표를 중심으로 사업을 운영할 수 있고 다른 모든 KPI는 그 목표에 따라 움직이게 되는 거죠 . |
| B8 부정 성과: 보안·프라이버시 | 그들은 감시를 받지 않을 것입니다. |

### The Future of Customer Experience - Creativity, Trust & Technology | Davos 2026 (CMO Break

- 채널: **Infosys** · 2026-03 · ko · 8,611단어 · ax_core/neutral
- 블록 8/8: B1·B2·B3·B4·B5·B6·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=taeDyZI86h8 · 원문: `transcripts/channels/Infosys/The_Future_of_Customer_Experience_-_Creativity,_Trust_&_Tech__taeDyZI86h8.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 구글 검색뿐 아니라 ChatGPT, Perplexity, Gemini 같은 대체 검색 서비스도 이용할 수 있게 되었으니까요. |
| B2 파괴: 소비자 행동·기대 | 안녕하세요, 고객 경험, 마케팅, 신뢰, 창의성 및 기술의 미래에 대한 토론에 오신 것을 환영합니다. |
| B3 전략적 대응 | 음 , 맥킨지의 '2025년 AI 현황 보고서'에 따르면 마케팅 분야가 실제로 비즈니스 영역으로 떠오르고 있는데, 이는 1,000명 이상의 최고 경영진을 대상으로 한 설문조사를 바탕으로 마케팅이 차세대 AI 활용을 통해 가장 크고 빠른 매출 증가를 얻고 있다는 것을 보여줍니다. |
| B4 가치네트워크·생태계 | 제 말은, 그것도 결국 가치관, 진정성, 윤리적인 조달, 공급망의 투명성 같은 것들과 관련된 문제 아닌가요? |
| B4 민첩성·양손잡이 | 그래서 우리 내부적으로는 제가 항상 팀원들에게 실험 문화, 심지어는 학습 문화가 더 중요하다고 말합니다. |
| B5 직무·역량 변화 | 음, 그래서 저희 회사에서는 모든 직원이 도구를 사용하기 전에 AI 교육을 받습니다 . |
| B6 장벽: 관성·저항 | 목소리가 큰 사람들은 변화에 매우 저항적이다. |
| B7 성과: 운영효율 | 물론 스펜서 스튜어트는 마케팅에서 AI를 사용하는 것이 브랜드 신뢰도에 문제를 일으키고 있다고 말했고, 여러분 모두에게 비용 절감을 실현해야 한다는 엄청난 압력이 가해지고 있습니다. |
| B7 성과: 조직성과 | 음 , 맥킨지의 '2025년 AI 현황 보고서'에 따르면 마케팅 분야가 실제로 비즈니스 영역으로 떠오르고 있는데, 이는 1,000명 이상의 최고 경영진을 대상으로 한 설문조사를 바탕으로 마케팅이 차세대 AI 활용을 통해 가장 크고 빠른 매출 증가를 얻고 있다는 것을 보여줍니다. |
| B8 부정 성과: 보안·프라이버시 | 그런 현상은 창작 커뮤니티, 특히 광고 대행사나 일자리를 잃은 사람들로부터 많이 나타나는 것 같습니다. |

### The Boardroom Mandate: Scaling AI for Business Impact | Davos 2026

- 채널: **Infosys** · 2026-02 · ko · 6,313단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B6·B7
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=0ixUiXr2DVY · 원문: `transcripts/channels/Infosys/The_Boardroom_Mandate_Scaling_AI_for_Business_Impact_Davos_2__0ixUiXr2DVY.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | API 형태도 아니고, 오늘날 우리가 흔히 사용하는 챗봇이나 클라우드 코드 유형의 도구와도 정확히 일치하지 않을 수 있습니다 . |
| B2 파괴: 소비자 행동·기대 | 저는 당신이 고객이 원하는 것을 정확히 제공함으로써 결국 새로운 제품을 추가 판매하게 될 것이라고 확신합니다. |
| B2 파괴: 경쟁구도 | 왜냐하면 [코웃음] 오랜 기다림 끝에 AI를 통해 챔피언, 도전자, 그리고 신규 진입자 모두에게 공정한 경쟁의 장을 마련할 수 있는 기회를 찾았기 때문이죠. |
| B2 파괴: 데이터 가용성 | 데이터 양이 많고 정확도도 더 높은 경향이 있습니다. |
| B3 전략적 대응 | 따라서 이사회 와 경영진 사이에는 상당한 지식 격차가 존재한다고 생각합니다. |
| B4 가치네트워크·생태계 | 그리고 이제 인포시스에서의 여정에 대해 구체적으로 말씀드리자면, 저희는 지난 몇 년 동안 직원들을 세심하고 체계적으로 교육하고, 인재를 육성해 왔으며, 무엇보다 중요한 것은 저희의 경험에서 얻은 자산을 토파즈 패브릭이라는 생태계로 추상화하는 데 주력해 왔다는 것입니다. |
| B4 디지털 채널 | 그 모든 전화는 예전에도 저희 콜센터로 걸려오던 전화였습니다 . |
| B5 리더십·CDO/CAIO | 음, 그래서 저는 리더십, 즉 CEO와 나머지 경영진이 이사회를 설득하고 교육하는 데 책임이 있다고 생각합니다. |
| B5 직무·역량 변화 | 정말로 AI 개발 역량을 갖춘 인재를 채용해 오셨군요. |
| B6 장벽: 관성·저항 | 필요한 것은 기존 레거시 시스템이나 엑셀 스프레드시트에 숨겨져 있는 독립형 시스템 등 어디에 있든 데이터를 가져올 수 있는 기반 시설입니다 . |
| B7 성과: 운영효율 | 물론 투자 수익은 바로 나타나지 않습니다. |

### What is an AI Transformation Partner? (and how to become one)

- 채널: **Liam Ottley** · 2026-07 · ko · 5,160단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B6·B7
- AX 교량: —
- 링크: https://www.youtube.com/watch?v=aNrWN0M851k · 원문: `transcripts/2026-07-18/What_is_an_AI_Transformation_Partner_(and_how_to_become_one)__aNrWN0M851k.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 워크숍을 통해 모든 구성원들이 AI 기술이란 무엇인지, 생성형 AI란 무엇인지, 그리고 AI 교육의 강점과 약점은 무엇인지 빠르게 이해할 수 있도록 돕습니다. |
| B2 파괴: 경쟁구도 | 결국 고객과 훌륭한 관계를 구축하게 되는데, 그 이유는 고객을 처음부터 시작하여 이제는 실제로 의미 있는 변화를 가져오고 시장에서 경쟁 우위를 확보할 수 있는 시스템을 도입하도록 도와주었기 때문입니다. |
| B3 전략적 대응 | 따라서 여기에는 AI 전략도 포함됩니다 . |
| B4 가치네트워크·생태계 | 또한 지속적인 관리 및 파트너십 측면도 중요한데, 바로 이 부분에서 AITP 파트너십이 빛을 발합니다. |
| B5 직무·역량 변화 | 워크숍을 통해 모든 구성원들이 AI 기술이란 무엇인지, 생성형 AI란 무엇인지, 그리고 AI 교육의 강점과 약점은 무엇인지 빠르게 이해할 수 있도록 돕습니다. |
| B6 장벽: 관성·저항 | 티켓 가격이 높을수록 저항이 커지고 더 많은 신뢰가 필요하기 때문입니다. |
| B7 성과: 운영효율 | 시간을 단축하고 특정 작업에 필요한 노동력을 줄이며 발견 단계에 통합할 수 있는 도구나 시스템은 무엇일까요? |
| B7 성과: 조직성과 | 결국 고객과 훌륭한 관계를 구축하게 되는데, 그 이유는 고객을 처음부터 시작하여 이제는 실제로 의미 있는 변화를 가져오고 시장에서 경쟁 우위를 확보할 수 있는 시스템을 도입하도록 도와주었기 때문입니다. |

### Integrating Generative AI Into Business Strategy: Dr. George Westerman

- 채널: **MIT Corporate Relations** · 2026-07 · ko · 5,739단어 · ax_core/washing
- 블록 8/8: B1·B2·B3·B4·B5·B6·B7·B8
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=9RvWcXVaAng · 원문: `transcripts/2026-07-31/Integrating_Generative_AI_Into_Business_Strategy_Dr._George___9RvWcXVaAng.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 그래서 오늘 저는 생성형 AI에 대해 어떻게 생각하시는지, 그리고 전략에 어떻게 활용하시는지에 대해 이야기해 보려고 합니다. |
| B2 파괴: 소비자 행동·기대 | 저는 지금 집을 리모델링 중이라 홈디포에서 많은 시간을 보냈는데, FIM과 그의 팀은 정말 복잡한 매장에서 훌륭한 사용자 경험을 만들어냈습니다. |
| B3 전략적 대응 | 최고 경영진의 리더십과 디지털 혁신의 흥미로운 교차점에서 모든 산업 분야의 리더들에게 지속적으로 가치 있는 정보를 제공하기 위해 노력하고 계십니다. |
| B4 디지털 채널 | 크레스타(Cresta)는 특히 영업 분야 콜센터 도구입니다. |
| B5 조직구조 변화 | 프랑스의 대형 은행 중 하나인 소시에테 잘(Society Jal)에서는 매우 중앙 집중식 방식으로 접근했습니다. |
| B5 조직문화 변화 | 또한, 기업 문화는 실험하고 시도하며 빠르게 실패하는 것을 두려워하지 않고, 시작하기 전에 정답을 찾으려고 애쓰기보다는 새로운 것을 시도하는 데 얼마나 능숙해야 할까요? |
| B5 리더십·CDO/CAIO | 홈디포의 사례를 들자면, 저는 매년 MIT 슬론 CIO 리더십 어워드를 운영하는데, FIM은 작년에 최종 후보 중 한 명이었습니다. |
| B6 장벽: 관성·저항 | 준비가 되어 있지 않으면 저항할 것이고, 적극적으로 저항하거나, 아니면 "어렵네요. |
| B7 성과: 운영효율 | 시니어 개발자는 14%, 주니어 개발자는 34% 향상되었습니다. |
| B8 부정 성과: 보안·프라이버시 | 솔직히 말해서, 저는 딥페이크 기술을 아주 쉽게 사용할 수 있습니다. |

### Microsoft Digital Sovereignty Summit | Sovereign Cloud, AI & Security Highlights

- 채널: **Microsoft Azure** · 2026-04 · ko · 25,652단어 · ax_core/anti_washing
- 블록 8/8: B1·B2·B3·B4·B5·B6·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=YLL7UuVCerM · 원문: `transcripts/channels/Microsoft_Azure/Microsoft_Digital_Sovereignty_Summit_Sovereign_Cloud,_AI_&_S__YLL7UuVCerM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 주권이 어떻게 구현되고 있는가 클라우드, AI 및 보안 전반에 걸친 실무 경험. |
| B2 파괴: 경쟁구도 | 마이크로소프트와 경쟁사들은 잘 알고 있습니다. |
| B2 파괴: 데이터 가용성 | 음, 아시다시피 마이크로소프트는 데이터를 수집합니다. |
| B3 전략적 대응 | 감사인, 이사회, 그리고 시민들 매일같이 시행되는 것을 보게 될 것입니다. |
| B4 가치네트워크·생태계 | 고객, 파트너, 독립적인 사람들뿐만 아니라 생태계 전반의 목소리. |
| B5 리더십·CDO/CAIO | 그리고 이것에서 패널 토론에서는 리더십에 대해 집중적으로 다룰 것입니다. |
| B6 장벽: 관성·저항 | 유럽 ​​전역의 정부를 대상으로 하는 계약 회사에 대한 계약상 의무 만약 우리가 받게 된다면 이런 명령이라면 우리는 사실상 저항할 것이다. |
| B7 성과: 운영효율 | 손 여러분 사람들 중에서, 그리고 아시다시피, 혁신과 획기적인 발견을 이루어내는 것 생산성 향상. |
| B8 부정 성과: 보안·프라이버시 | 본질적으로 데이터 개인정보 보호에 기반을 두고 있었습니다. |

### Prepare for Microsoft Certification Exam AB-731: AI Transformation Leader

- 채널: **Microsoft Learn** · 2026-07 · en · 5,148단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=mj_lyhuWbig · 원문: `transcripts/2026-07-18/Prepare_for_Microsoft_Certification_Exam_AB-731_AI_Transform__mj_lyhuWbig.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | Let's go through these in a little more detail starting with understanding the difference between generative AI, traditional machine learning, and rule-based systems. |
| B2 파괴: 데이터 가용성 | First, look for high-value use cases in for content creation, customer support, document processing, and anything involving large volumes of unstructured data are strong signals for generative AI. |
| B3 전략적 대응 | ANDREW CONNIFF: Hello and welcome to "Preparing for Exam AB-731 AI Transformation Leader." I'm Andrew Conniff, a Microsoft Technical Trainer focusing on Copilot and AI strategy adoption. |
| B4 가치제안 변화 | Know the Azure AI subscription models and when each is appropriate. |
| B5 조직구조 변화 | Know that it drives cross-functional alignment across business, IT, legal, and compliance. |
| B5 리더십·CDO/CAIO | And one of the common barriers to AI adoption are primarily people, the trust, the processes, and the leadership, not the technology, so identifying people-related barriers, fear of job impact, low confidence, and lack o… |
| B7 성과: 운영효율 | So the value comes from time savings, productivity improvements, and quality outcomes, not just lower spending. |
| B7 성과: 조직성과 | And then we're going to look at training and evaluation. |
| B8 부정 성과: 보안·프라이버시 | So look for signals like prompt injection, data leakage, and model misuse. |

### Qdrant Vector Space Day 2025 | Opening Keynotes

- 채널: **Qdrant** · 2025-10 · ko · 8,087단어 · ax_core/neutral
- 블록 7/8: B1·B2·B3·B4·B5·B6·B7
- AX 교량: —
- 링크: https://www.youtube.com/watch?v=Vgbg7uIddnA · 원문: `transcripts/channels/Qdrant/Qdrant_Vector_Space_Day_2025_Opening_Keynotes__Vgbg7uIddnA.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | LLM, 제발 거짓말하지 마세요. |
| B2 파괴: 소비자 행동·기대 | 우리는 함께 기업 클라우드 컴퓨팅의 판도를 바꾸고, 모든 조직이 모든 엔터프라이즈 애플리케이션을 재구축하여 AI와 벡터 검색을 핵심으로 삼아 직원과 고객 경험을 혁신할 수 있도록 돕고 싶습니다. |
| B3 전략적 대응 | 그래서 저는 CMO로서 오늘 방금 들으신 로드맵을 활용하여 제 자신의 고객 경험에 전적으로 의존하고 있습니다 . |
| B4 가치제안 변화 | 가치 제안 측면에서 이것은 무엇을 의미합니까 ? |
| B4 가치네트워크·생태계 | 마이크로소프트와 쿠드랜드는 기술 파트너십을 맺고 있기 때문에, 쿠드랜드와 함께 이 무대에 서게 되어 매우 자랑스럽습니다 . |
| B5 리더십·CDO/CAIO | 저희는 쿼드런트 스타들과 그들이 어떻게 리더십을 발휘하고 있는지, 그리고 스타트업 프로그램에 대해 이야기했지만, 궁극적으로 이 플랫폼 자체는 모든 규모의 개발자를 위한 것입니다. |
| B6 장벽: 관성·저항 | 그리고 기존의 검색 도구, 제가 레거시라고 부르지는 않겠지만, 고전적인 검색 도구와는 항상 잘 작동하는 것은 아닙니다. |
| B7 성과: 조직성과 | 그들이 미칠 수 있는 영향력이 상당히 크기 때문에 그들의 기업 가치는 30억 달러에서 600억 달러 사이로 평가됩니다 . |

### The Blueprint for Agentic Business | ServiceNow Knowledge 2026 Day 2 Keynote

- 채널: **ServiceNow** · 2026-05 · ko · 8,694단어 · ax_core/neutral
- 블록 8/8: B1·B2·B3·B4·B5·B6·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=q8kaVEkTWho · 원문: `transcripts/channels/ServiceNow/The_Blueprint_for_Agentic_Business_ServiceNow_Knowledge_2026__q8kaVEkTWho.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 이 글은 OT(작업 치료) 및 의료 기기, IoT(사물 인터넷) 기기, 클라우드 및 코드, AI 에이전트에 관한 내용입니다. |
| B2 파괴: 소비자 행동·기대 | 워크플로 데이터 패브릭용 자동 기능을 사용하면 고객이 원하는 바를 일반적인 언어로 설명 하고 AI가 통합을 구축하도록 할 수 있습니다 . |
| B3 전략적 대응 | 마지막으로 가장 중요한 것은 이사회, 최고 경영진(ELT) 및 이해관계자의 참여입니다. |
| B4 가치네트워크·생태계 | 이를 가능하게 하는 방법 중 하나는 전략적 파트너십과 개방형 생태계를 구축하는 것입니다. |
| B5 리더십·CDO/CAIO | 두 번째는 Gemini Enterprise에서 누구나 ServiceNow 에이전트를 직접 생성할 수 있고, 해당 에이전트가 양쪽 플랫폼에 모두 등록되므로 조직, 특히 에이전트 확산 문제를 해결해야 하는 CIO, CTO, CDO 담당자들이 원활한 거버넌스를 구축할 수 있다는 점입니다 . |
| B6 장벽: 관성·저항 | 분자는 문제를 정의하고 기술 부채를 없애는 데 도움을 줍니다. |
| B7 성과: 운영효율 | 아미트가 앞서 언급한 CVS Health는 250만 건 이상의 AI 대화를 제공하여 환자 및 고객 응대 업무에 소요되는 귀중한 시간을 절약해 주었습니다 . |
| B8 부정 성과: 보안·프라이버시 | 예를 들어 , 제 음악용 컴퓨터에 문제가 생겼다고 가정해 볼게요. |

### Welcome to Agentic Business | ServiceNow Knowledge 2026 Opening Keynote

- 채널: **ServiceNow** · 2026-05 · ko · 9,200단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=jeo2V1w-Peg · 원문: `transcripts/channels/ServiceNow/Welcome_to_Agentic_Business_ServiceNow_Knowledge_2026_Openin__jeo2V1w-Peg.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 최근 들어본 AI 관련 홍보 자료들은 대부분 LLM(법학 석사)으로 시작하는 것 같습니다. |
| B2 파괴: 소비자 행동·기대 | 모든 역할은 고유한 인터페이스와 사용자 경험을 제공합니다. |
| B3 전략적 대응 | 저는 창립자이신 위대한 프레드 루디 와 이사회 동료이신 수바 배리 스트롬, 수석 이사 래리 퀸란, 그리고 폴 챔벌레인에게 감사를 드리고 싶습니다. |
| B4 가치네트워크·생태계 | 우리는 우리가 가진 전문성을 바탕으로 글로벌 공급망을 조율하고 가치 사슬의 상위 단계로 나아가고자 합니다. |
| B5 조직구조 변화 | ServiceNow를 통해 상담원들이 고객이 겪는 더욱 복잡한 문제들을 해결할 수 있도록 중앙 집중식 지식 기반을 제공할 수 있게 되었습니다. |
| B5 리더십·CDO/CAIO | 훌륭한 리더십에 감사드립니다. |
| B5 직무·역량 변화 | 우리는 채용부터 퇴직, 소싱부터 지급, 배송부터 수금까지 세 가지 핵심 프로세스에 걸쳐 매달 500만 건의 ServiceNow 워크플로우를 실행합니다. |
| B7 성과: 운영효율 | 도입률, 소비량, 투자 수익률, 생산성 및 비용 절감 효과를 모두 한 곳에서 확인하세요. |
| B7 성과: 조직성과 | 고객 만족도(CSAT)가 떨어지고 있습니다. |
| B7 성과: 사회적 편익 | 하지만 우리가 먼저 이해해야 할 것은 현재 AI는 일자리 창출에만 집중하고 있다는 점입니다. |
| B8 부정 성과: 보안·프라이버시 | 또한 AI가 실행되는 동안 환각, 편향, 유해 콘텐츠, 정보 유출 및 왜곡을 감지하고 자동으로 수정 작업을 시작합니다. |

### Building AI Factories: How Siemens and AWS Are Solving Data Center Engineering Challenges

- 채널: **Siemens** · 2026-01 · ko · 3,341단어 · ax_core/washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: —
- 링크: https://www.youtube.com/watch?v=ZLl184cSyYM · 원문: `transcripts/channels/Siemens/Building_AI_Factories_How_Siemens_and_AWS_Are_Solving_Data_C__ZLl184cSyYM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 음, 제 생각에는 AWS의 머신러닝 AI는 아직 새로운 분야인 것 같습니다. |
| B2 파괴: 소비자 행동·기대 | 그래서 중요한 건 바늘에 실을 적절한 위치에 정확하게 꿰는 방법이며, 이 모든 작업을 고객이 원하는 속도로 진행하는 것입니다. |
| B3 전략적 대응 | AWS의 주요 경영진으로서 말씀드릴 수 있는 것은, 앞으로 5년, 10년 후에도 우리는 항상 고객 중심적일 것이라는 점입니다. |
| B4 가치네트워크·생태계 | 네, 기술적 배경 과 아마존 같은 파트너사를 어떻게 도울 수 있는지에 대해 자세히 설명해주셔서 정말 감사합니다 . |
| B5 조직구조 변화 | 말씀하신 배터리 시스템의 신뢰성에 대해 말씀드리자면, 저희는 이미 오래전에 UPS 배터리 시스템, 특히 중앙 집중식 UPS 배터리 시스템을 없앴습니다. |
| B7 성과: 사회적 편익 | 네, 저희는 지금 적극적으로 일자리를 창출하고 있습니다 . |
| B8 부정 성과: 보안·프라이버시 | 뉴스를 보면 AI가 일자리를 대체할 것이라는 우려가 많은데, 현실적으로 AI는 일자리를 대체할 것입니다. |

### How AI Transforms Retail, Finance and Manufacturing in 2026

- 채널: **Snowflake** · 2025-12 · ko · 5,798단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=11degQs3L7c · 원문: `transcripts/channels/Snowflake/How_AI_Transforms_Retail,_Finance_and_Manufacturing_in_2026__11degQs3L7c.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 하지만 패스트 패션 트렌드가 있고, 그 안에서 생성형 AI가 소셜 미디어에서 사람들의 감정을 이해하는 데 사용되는 등 기존의 머신러닝 활용 사례들을 많이 대체하고 있습니다 . |
| B2 파괴: 소비자 행동·기대 | 이것이 바로 진정한 360도 고객 경험이며, 우리는 마침내 고객과 디지털 방식으로 소통할 수 있는 단계에 도달했습니다. |
| B2 파괴: 경쟁구도 | 이러한 모든 상황에서 제조업체는 적절한 데이터와 도구를 갖추면 경쟁사보다 한발 앞서 나갈 수 있는 더 빠르고 정확한 의사결정을 내릴 수 있습니다 . |
| B2 파괴: 데이터 가용성 | 음, 그러니까, 제 생각에는 당신의 질문은 비정형 데이터에 대한 내용도 포함하는 것 같네요, 그렇죠? |
| B3 전략적 대응 | 제 생각에는 "데이터 전략 없이는 AI 전략이 없다"라는 말처럼, AI 전략도 데이터 전략 없이는 불가능하다고 봅니다. |
| B4 가치네트워크·생태계 | 제 생각에는 미래에는 기업들이 공급망, 상품 기획, 구매, 조달 등 모든 분야에 걸쳐 여러 명의 에이전트를 두는 모습을 실제로 보게 될 것입니다. |
| B5 조직구조 변화 | 하지만 클라우드는 필수적인 역할을 하며, 특히 엣지의 사일로화된 시스템에서 관리되던 모든 데이터가 이제 클라우드에 통합되는 지점에서 중요한 역할을 합니다. |
| B5 리더십·CDO/CAIO | 언더아머의 최고 디지털 책임자(CDO)인 패트릭 D. |
| B7 성과: 운영효율 | 그래서 다소 복잡해질 수 있지만, 그렇게 함으로써 절감 효과와 생산성 향상, 그리고 적시 소비 방식이 크게 개선됩니다. |
| B7 성과: 조직성과 | 이는 예를 들어 초 개인화, 실시간 인사이트, 고객 유지와 같은 경험 지표를 통해 측정될 것이며, 또한 관계 관리자와 고객 참여 활동, 성장, 매출 성과와 같은 최고 수준의 분석 기능을 통해 측정될 것입니다. |
| B8 부정 성과: 보안·프라이버시 | 음, 저는 금융 서비스 업계가 위험 모니터링부터 감시, 고객 검토, 포트폴리오 운영에 이르기까지 핵심 비즈니스 프로세스에 AI 에이전트를 도입하기 시작할 것으로 예상합니다. |

### Snowflake Build London Keynote

- 채널: **Snowflake** · 2026-02 · ko · 9,281단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=9LOP86qaw34 · 원문: `transcripts/channels/Snowflake/Snowflake_Build_London_Keynote__9LOP86qaw34.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 데이터가 생성되는 시점이든, IoT 기기든 센서든 애플리케이션이든 데이터베이스든, 변환 과정을 거쳐 최종적으로 소비되는 시점이든, 모든 과정을 아우릅니다. |
| B2 파괴: 데이터 가용성 | 하지만 제가 "데이터를 수집하고 사일로를 허물고 있습니다"라고 말하기 전에 많은 분들이 생각하시는 또 다른 질문은 " 내 데이터 아키텍처는 어떻게 될까요?" 그리고 "저희는 여러분이 원하는 아키텍처를 지원하고 싶습니다"라는 것입니다. |
| B3 전략적 대응 | Snowflake와 AWS를 활용하여 음악 생성 AI 전략을 발전시키고, 인사이트를 높이고, 개발 속도를 높이고, 기술 스택을 간소화하세요. |
| B4 가치네트워크·생태계 | 다시 말하지만, 이 모든 것은 스노우플레이크 생태계 내에서 이루어집니다. |
| B5 조직구조 변화 | 하지만 제가 "데이터를 수집하고 사일로를 허물고 있습니다"라고 말하기 전에 많은 분들이 생각하시는 또 다른 질문은 " 내 데이터 아키텍처는 어떻게 될까요?" 그리고 "저희는 여러분이 원하는 아키텍처를 지원하고 싶습니다"라는 것입니다. |
| B5 직무·역량 변화 | 저희 창립자인 베누아와 티에리가 처음으로 채용한 직원은 보안 설계자였습니다. |
| B7 성과: 운영효율 | 결국 우리가 Cortis 코드로 하는 일의 상당 부분은 생산성 향상과 관련이 있습니다. |
| B8 부정 성과: 보안·프라이버시 | 저는 실제로 오케스트레이터를 개선하여 오류가 발생할 경우 재시도할 수 있는 논리적인 기능을 추가하고 싶었습니다 . |

### Snowflake Summit 2026 Platform Keynote

- 채널: **Snowflake** · 2026-06 · en · 13,214단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=CtqKJV6gyGQ · 원문: `transcripts/channels/Snowflake/Snowflake_Summit_2026_Platform_Keynote__CtqKJV6gyGQ.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | By uniting AI and data, the Snowflake AI data cloud delivers the ideal foundation to power your agentic enterprise. |
| B2 파괴: 소비자 행동·기대 | Uh there's competitive threats at every turn and so we have to do better to continue to deliver exceptional customer experience. |
| B2 파괴: 데이터 가용성 | We engineer a system that could seamlessly equate structured and semistructured data together, effectively unifying data warehouse and big data system with unprecedented performance at multipetabyte scale. |
| B3 전략적 대응 | My responsibility is to really deliver and drive an AI strategy to enable outcomes for the organization globally across the enterprise. |
| B4 가치네트워크·생태계 | So this fiduciary grade standard that we deliver to must be built on a trusted data foundation and we've really leveraged our partnership with with Snowflake and are our uh very appreciative of that. |
| B5 조직구조 변화 | First, data was siloed. |
| B5 직무·역량 변화 | Now my first demo is going to focus on data engineers and app developers who is excited even more now. |
| B7 성과: 운영효율 | We're introducing a massive new engine optimization that improves latency and throughput by roughly 8x and you see a schematic on if you tried hybrid tables in the past you should retire because it's gotten materially be… |
| B8 부정 성과: 보안·프라이버시 | We introduced earlier in the year Horizon AI guard rails which is protections into both cocoa and co-work to prevent high risk threats jailbreaking or prompt injection type of attacks and this is built in detecting zero … |

### Build, Test, and Deploy Production-Ready Enterprise AI Agents in Minutes | with @Informati

- 채널: **Solutions Review** · 2026-08 · ko · 5,365단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=P0kux8A8NbM · 원문: `transcripts/2026-08-03/Build,_Test,_and_Deploy_Production-Ready_Enterprise_AI_Agent__P0kux8A8NbM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | LLM AI 에이전트를 구축할 때 세 가지 핵심 구성 요소가 있죠 ? |
| B2 파괴: 소비자 행동·기대 | 인공 지능 에이전트는 애플리케이션에 통합될 경우 사용자 경험과 운영 효율성을 크게 향상시킬 수 있는 잠재력을 가지고 있습니다 . |
| B2 파괴: 데이터 가용성 | 클라우드 데이터 접근 관리를 통해 규정 준수를 보장하려면 데이터 개인정보 보호 제어 기능도 필요합니다 . |
| B3 전략적 대응 | 그래서 저는, 그리고 다시 말씀드리지만, 제가 확실히 알고 있는 것은 이사회부터 경영진에 이르기까지 2026년까지 AI 전략을 즉시 수립해야 한다는 압력이 매우 크다는 것입니다. |
| B4 가치네트워크·생태계 | 그래서 이것들은 LLM의 핵심이며, 우리는 이들과 협력하여 풍부한 파트너십과 광범위한 GSI 생태계를 구축해 왔습니다. |
| B5 직무·역량 변화 | 세 번째 사용 사례 유형은 Informatica 플랫폼을 사용하는 IT 개발자, 데이터 엔지니어 및 데이터 전문가를 위해 Informatica 및 데이터 관리 작업을 자동화하는 맞춤형 Informatica 에이전트를 구축하는 것입니다 . |
| B7 성과: 운영효율 | 인공 지능 에이전트는 애플리케이션에 통합될 경우 사용자 경험과 운영 효율성을 크게 향상시킬 수 있는 잠재력을 가지고 있습니다 . |
| B8 부정 성과: 보안·프라이버시 | 클라우드 데이터 접근 관리를 통해 규정 준수를 보장하려면 데이터 개인정보 보호 제어 기능도 필요합니다 . |

### Telefónica Capital Markets Day 2025 | ES

- 채널: **Telefónica** · 2025-11 · ko · 13,276단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=8HYvqTquKQM · 원문: `transcripts/channels/Telefónica/Telefónica_Capital_Markets_Day_2025_ES__8HYvqTquKQM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 주로 사이버 보안, 클라우드 분야에서 사물인터넷(IoT)과 인더스트리 4.0. |
| B2 파괴: 소비자 행동·기대 | 그만큼 초개인화와 관계 고객과 함께하는 디지털 탁월함을 달성하는 데 필요한 고객. |
| B2 파괴: 경쟁구도 | 경험 고객은 강력한 경쟁 우위 요소입니다. |
| B3 전략적 대응 | 의 전체 경영진의 일원 감사드립니다. |
| B4 가치네트워크·생태계 | 생태계 수익 증대 3.4% 복합 성장률 2025년부터 2028년까지 연간 보고서. |
| B5 직무·역량 변화 | 그것은 필요하다 역량을 개발하다 재교육 및 습득 새로운 인재들. |
| B7 성과: 운영효율 | 기업 센터 및 당사 사업부 글로벌 비즈니스 모델에 맞춰 조정하기 그룹의 새로운 현실과 그 역할 수정을 통해 이러한 운영 비용을 절감했습니다. |
| B7 성과: 조직성과 | 고객 만족도를 높여 매출 회전율을 줄입니다. |
| B8 부정 성과: 보안·프라이버시 | 주요 사이버 공격에 관하여 런던, 브루세라스, 베를린 공항 그리고 2025년의 더블린. |

### AI for AI: Building the Transformation Office That Drives Enterprise AI Adoption

- 채널: **Tigerhall** · 2026-07 · ko · 7,388단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B6·B7
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=OJwpw-8SkBM · 원문: `transcripts/2026-07-26/AI_for_AI_Building_the_Transformation_Office_That_Drives_Ent__OJwpw-8SkBM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 그러니 GPT, Gemini, Claude 또는 다른 어떤 모델이든 사용 가능한지 채팅창에 자유롭게 남겨주시고, 특정 모델을 사용하고 있다면 모델명도 함께 적어주세요. |
| B2 파괴: 소비자 행동·기대 | 예를 들어 개인화와 같은 것을 생각해 보면, 이는 제품이나 서비스의 도입을 촉진하는 데 있어 가장 효과적인 방법으로 알려져 있습니다. |
| B2 파괴: 경쟁구도 | 그러니까 만약 당신이 인류학적 모델을 사용하고 어떤 질문을 입력했는데, 경쟁자 중 누군가가 똑같은 질문을 입력한다면, 당신의 결과물도 완전히 똑같을 겁니다. |
| B3 전략적 대응 | 여기에는 도입에 대한 통찰력부터 업무 흐름 속에서 개인 맞춤형 동기 부여를 통해 관리자가 이사회 회의를 위한 경영진 스토리텔링을 구축할 수 있도록 지원하는 방법까지 모든 예시가 있습니다 . |
| B4 가치네트워크·생태계 | 예를 들어 SQL 데이터베이스를 살펴보면, 마이크로소프트 그래프는 마이크로소프트 생태계 전반에 걸쳐 있는 모든 작업을 한눈에 파악할 수 있도록 해주기 때문에 매우 유용합니다 . |
| B5 조직구조 변화 | 동시에, 컨텍스트를 중앙 집중화하고 컨텍스트 레이어를 중앙 두뇌로 활용하면서도 실행은 분산화하여 관리자, 리더, 그리고 리더뿐 아니라 모든 직원이 참여하고 개인화가 이루어지도록 할 수 있기 때문입니다 . |
| B5 직무·역량 변화 | 콘텐츠 제작은 AI의 가장 중요한 활용 사례이며, 이전에는 변화 활성화, 커뮤니케이션 캠페인 준비, 커뮤니케이션 배포, 교육 자료 제작, 역량 강화, 참고 자료, 문서 제작 등 모든 과정에 많은 시간이 소요되었습니다. |
| B6 장벽: 관성·저항 | 예를 들어, 레거시 시스템의 수명 주기를 살펴보면 여러 요소가 있는데, 각 요소가 얼마나 많은 시간을 소모하는지 파악하고, 이 모든 것을 종합적으로 고려하여 AI만으로 무엇을 할 수 있는지, AI를 어떻게 활용할 수 있는지 생각해 볼 수 있습니다. |
| B7 성과: 운영효율 | AI를 활용하면 기존의 수동 방식으로는 불가능했던 변화와 혁신을 대규모로 추진할 수 있으며, 이를 통해 투자 대비 수익률(ROI)을 크게 높일 수 있습니다 . |

### Enterprise strategies for agentic AI adoption in 2026 and beyond

- 채널: **Vertesia** · 2026-07 · en · 11,088단어 · ax_core/anti_washing
- 블록 7/8: B1·B3·B4·B5·B6·B7·B8
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=B4WgQotMVmE · 원문: `transcripts/2026-07-21/Enterprise_strategies_for_agentic_AI_adoption_in_2026_and_be__B4WgQotMVmE.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | In fact, I mean, chat GPT, which is where a lot of people learned about AI and artificial intelligence, only had its third birthday at the end of November last month. |
| B3 전략적 대응 | What are the cost, risk, and scalability implication of each approach and how to frame long-term AI strategy?" I think Tim, you're the best to answer this one. |
| B4 가치네트워크·생태계 | Well, I'm actually going to stick with you here, Mark, if that's okay, and ask you what partnerships or vendor relationships are critical for successful Aentic AI implementation. |
| B4 민첩성·양손잡이 | Um it was great to hear about some of the sort of assessment points of how um Mark and uh Michael are looking to implement uh AI applications but part of it is a degree of experimentation because I don't you know you kno… |
| B5 리더십·CDO/CAIO | I bring over 20 years of uh strategic operations and transformation leadership across financial services. |
| B5 직무·역량 변화 | And unfortunately, I've seen companies make layoffs more times than I care to remember. |
| B6 장벽: 관성·저항 | And so how can organizations effectively manage cultural resistance and stakeholder concerns during the agency implementation? |
| B7 성과: 운영효율 | So there are three uh that we have rolled out in 2025 that have brought the highest ROI, the fastest user adoption rates. |
| B8 부정 성과: 보안·프라이버시 | With privacy and data a big regulatory issue, how will it be possible to get this external data to train the AI agents? |

### How AI Is Changing Enterprise

- 채널: **Y Combinator** · 2026-07 · ko · 6,062단어 · ax_core/washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=aIKfA3gIXwo · 원문: `transcripts/2026-07-26/How_AI_Is_Changing_Enterprise__aIKfA3gIXwo.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 우리가 한동안 이야기해 왔고 아마 우리도 동의할 것 같은 주제가 있는데, GBT 래퍼 밈은 형편 없는 밈이었고, 사실 파운데이션 모델 회사들 위에 앱을 구축하는 데에는 많은 가치가 있고 항상 그래 왔다는 거예요. |
| B2 파괴: 소비자 행동·기대 | 모든 것은 최종 사용자 경험에 관한 것이었죠. |
| B2 파괴: 경쟁구도 | 최고의 모델은 결국 가격 경쟁에서 이기는 경쟁사의 가격에 맞춰야 한다는 것이죠. |
| B3 전략적 대응 | 네, 제 출장에서 늘 그렇듯이, 포춘 500대 기업의 고위 임원들과 그들의 기술 및 AI 전략에 대해 많은 시간을 이야기 나누셨잖아요. |
| B4 가치제안 변화 | 모델이 여러분의 가치 제안을 통합하는 것보다는, 모델 제공업체가 소비자 규모의 애플리케이션을 보유하고 있다면 Chachi BT가 자사 기능에 직접 통합할 수 있는 부분을 방해하고 싶지 않을 것입니다. |
| B4 가치네트워크·생태계 | 기업에 통합되거나 대규모 소비자 애플리케이션을 통해 일정 수준의 트래픽을 확보하여 사람들이 생태계 내에 머물도록 하는 등 다른 가치 제안이 충분하지 않으면, 순수 플레이어 모델은 매우 위험할 수 있습니다. |
| B5 리더십·CDO/CAIO | 예를 들어, 은행의 자산 관리 책임자는 신경 쓰지 않겠지만, CTO, AI 책임자, 그리고 해커 뉴스(Hacker News) 같은 곳에서 정보를 주고받는 IT 전문가들은 관심을 가질 것입니다. |
| B5 직무·역량 변화 | 기존 방식으로는 몇 달 동안 인력을 채용하고 팀을 구축해야 했지만, 이제는 일주일 만에 리드를 생성하고 바로 작업을 시작할 수 있게 되는 겁니다. |
| B7 성과: 운영효율 | 예를 들어 커서를 사용하는 생산성 향상을 보여주면 사람들이 완전히 납득할 테니까요. |
| B8 부정 성과: 보안·프라이버시 | 물론 개인정보보호위원회, 준법감시 위원회, 규제 기관 등 모든 것을 검토해야 하기 때문에 모두가 아직 초기 단계에 있지만, 클라우드 도입이 얼마나 큰 변화를 가져올지는 모두가 인지하고 있어요. |

### Lovable's Ryan Meadows on the New GTM Playbook

- 채널: **Zapier** · 2026-06 · ko · 5,142단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=FeZ93evIfbM · 원문: `transcripts/channels/Zapier/Lovable's_Ryan_Meadows_on_the_New_GTM_Playbook__FeZ93evIfbM.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 음, 요즘 소셜 미디어에서 뜨겁게 달아오르는 AI 관련 논쟁 중에, 긍정적인 면보다 부정적인 면이 더 크다고 생각하는 건 뭐예요? |
| B2 파괴: 경쟁구도 | 우리가 이 속도로 성장할 수 있는 도구를 가지고 있다면 , 경쟁사도, 미래의 경쟁사도 마찬가지일 텐데 말이죠. |
| B3 전략적 대응 | 은퇴해서 해변에서 여유로운 시간을 보낼 수도 있고, 투자도 하고, 이사회 활동도 하고, 다시 스타트업을 시작할 수도 있겠죠. |
| B4 가치네트워크·생태계 | 저는 인사팀 책임자인 메리 앤과 정말 좋은 파트너십을 맺고 있어요. |
| B5 리더십·CDO/CAIO | 기본적으로 저희는 최고의 경험이라고 생각하는 것들을 입력하고, LLM(Learning Leadership Model)에 옵션 메뉴를 제공합니다. |
| B5 직무·역량 변화 | 기술 인력을 더 많이 채용하고 있으며, 관리적인 고객 성공 업무보다는 변경 관리 및 배포에 훨씬 더 집중하고 있습니다. |
| B7 성과: 조직성과 | 연간 매출이 4억 달러를 넘어섰어요. |
| B8 부정 성과: 보안·프라이버시 | 저를 진심으로 믿었던 사람들이 신뢰를 잃기 시작했어요. |

### RevOps Strategy 2026: RevOps Leaders Reveal Their Plan

- 채널: **Zapier** · 2025-12 · ko · 7,727단어 · ax_core/washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=J0dUy6VYmTs · 원문: `transcripts/channels/Zapier/RevOps_Strategy_2026_RevOps_Leaders_Reveal_Their_Plan__J0dUy6VYmTs.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 예를 들어 저희가 구축한 것들 중 몇 가지를 말씀드리자면, ROE GPT 같은 것을 사람들이 계속해서 묻습니다. |
| B2 파괴: 소비자 행동·기대 | 그리고 이러한 전략을 영업 리더십 수준, CMO, 파트너십 담당 부사장, 고객 경험 책임자 등 이해관계자들과 공유하고, 이러한 목표를 뒷받침할 수 있는 핵심적인 투자 대상을 구체적으로 결정하는 것이 중요합니다. |
| B3 전략적 대응 | 하지만 아무도 "제가 이사회에 가서 리드 라우팅을 개선했거나 스코어링을 개선했습니다. |
| B4 가치네트워크·생태계 | 그러니까 마케팅, 영업, 고객 성공, 파트너십, 시장 진출 전략, 지원 뿐만 아니라 영업까지 고려해야 한다는 거죠. |
| B5 리더십·CDO/CAIO | 웹플로우의 RevOps 팀이 전환점을 맞이했고, 당신이 명확하고 적극적 이며 진정한 전략적 리더십을 발휘하여 조직을 이끌고 있다는 것을 분명히 느꼈습니다. |
| B5 직무·역량 변화 | 저희는 역량 강화와 채용 및 기대치 설정에 집중했습니다. |
| B7 성과: 운영효율 | 그러니 질문을 질문 탭에 넣어주시면, 마지막에 시간을 절약해서 여기서 실시간으로 질문들을 답변해 드리겠습니다. |
| B8 부정 성과: 보안·프라이버시 | RevOps와 관련해서 제가 우려하는 점은, 예를 들어 섀도우 AI 같은 경우 사람들이 시간 낭비하면서 엄청나게 부정확한 데이터를 쏟아내는 시스템을 구축하거나 활용하게 되는 것을 원치 않는다는 것입니다 . |

### Sunlight on Shadow AI: When Security Learns to Tinker—Rob T. Lee on AI Risk

- 채널: **Zapier** · 2025-12 · ko · 6,574단어 · ax_core/anti_washing
- 블록 7/8: B1·B2·B3·B4·B5·B7·B8
- AX 교량: Avenue 2 윤리·거버넌스 · Avenue 1 동적역량
- 링크: https://www.youtube.com/watch?v=qlCkwGSRP3w · 원문: `transcripts/channels/Zapier/Sunlight_on_Shadow_AI_When_Security_Learns_to_Tinker—Rob_T.___qlCkwGSRP3w.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 그러다 보면 딥러닝, 머신러닝 같은 전체적인 개념에 빠져들게 되죠. |
| B2 파괴: 소비자 행동·기대 | 소프트웨어는 고객이 원하는 기능을 수행할 수 있지만, 고객이 원하는 것을 소프트웨어에 어떻게 구현할지 함께 고민해야 합니다 . |
| B3 전략적 대응 | 경영진이자 이사회 구성원으로서 당신의 목표는 전략을 이끄는 것입니다. |
| B4 가치네트워크·생태계 | 집에서 아이들과의 개인적인 상호작용, 소라( Sora) 같은 기기를 사용하는 경우를 생각해 보면, 사람들은 무의식적으로 아주 사적인 데이터를 생태계에 입력하게 됩니다. |
| B5 리더십·CDO/CAIO | 오늘은 인공지능에 대해 이야기하고, 기술 발전 속도가 기존의 방식을 앞지르는 시대에 리더십은 어떤 모습이어야 하는지 살펴보겠습니다 . |
| B5 직무·역량 변화 | 왜 이렇게 뛰어난 인재를 세 명이나 채용했을까요? |
| B7 성과: 운영효율 | 하지만 약 6주 전에 발표된 MIT 연구는 조직이 AI를 통해 투자 수익률(ROI)을 달성할 수 있는지에 초점을 맞췄습니다. |
| B8 부정 성과: 보안·프라이버시 | 왜냐하면 그들은 AI를 악용하려고 하기 때문입니다. |

### In the era of AI transformation (AX), we'll teach you everything about AX in just 30 minut

- 채널: **메타코드M** · 2026-07 · ko · 3,426단어 · ax_core/anti_washing
- 블록 8/8: B1·B2·B3·B4·B5·B6·B7·B8
- AX 교량: 정의 확장(DX→AX 계승) · Avenue 2 윤리·거버넌스
- 링크: https://www.youtube.com/watch?v=ErviFf8I6K4 · 원문: `transcripts/2026-07-18/In_the_era_of_AI_transformation_(AX),_we'll_teach_you_everyt__ErviFf8I6K4.md`

| 구성요소 | 근거 문장(발췌) |
|---|---|
| B1 디지털·AI 기술의 활용 | 에저에 대해서 에저 클라우드 자체에 대해서 직접했지만 어 코파일러시나 AA 에이전트 멀티에나 에이전트 AI처럼 AI 에이전트에 대해서 제품을 통합해서 AI 중심적으로 업무 방식 자체를 재정하고 상품부도 재정이하고 있습니다. |
| B2 파괴: 소비자 행동·기대 | 두 번째는 초개인화 된 서비스 등국에는 비즈니스나 신규 고객이나 아니면 기존 충성도 있는 고객 그리고 유입을 리드할 수을 리드할 수 있는 부분 애프터 세이지한 부분에서 전반적인 고객 여정에 있어서 AI를 도입하고 활용하는지들이 점점점 커지고 있습니다. |
| B3 전략적 대응 | 어 구글 같은 경우에는 어 아마 잘 아시겠지만은 신규 뭐 광고나 광고 검색이나 여러 가지 뭐 G처럼 데이터의 여러 가지 AI 전략을 수립하고 있습니다. |
| B4 가치네트워크·생태계 | 마이크로소프트, 구글, 어, AWS처럼 각각에 있는 기업들도 어, 영업이나 자체적인 변화나 이런 것들을 파트너십을 통해서 전반적인 생태계를 만드는 것으로 집중하고 있습니다. |
| B5 조직문화 변화 | 그래서 어 어시서트라는 개념도 있지만 AI를 조금 도구에 도입을 도구 자체로 도입을 넘어서 조직문화와 비즈니스 모델 즉 사업 모델까지도 바꿀 수 있는 근본적인 혁신과 변화를 추구하는 의미라고 볼 수 있습니다. |
| B5 리더십·CDO/CAIO | 그래서 단순하게 AI 트랜스포메이션은 기술에만 집중하는게 아니라 조직 그리고 기업을 갖고 있는 문화 그리고 기업의 개개인별 임원뿐만 아니 관리자뿐만 아니라 실진내의 리더십까지 통합적인 변화를 요구하고 있습니다. |
| B6 장벽: 관성·저항 | 어 뭐 제조 기업에서는 특히 공장에서 사람 대체나 노동역의 대체처럼만 보이기 때문에 굉장한 저항도 있고요. |
| B7 성과: 운영효율 | 그래서 왼쪽에 있는 표와 오른쪽에 있는 수치들을 보면은 결국에는 ROI 그까 리턴 오브 인베스트죠. |
| B8 부정 성과: 보안·프라이버시 | 기업 AX 전략의 어 핵심 포인트는 첫 번째 AX와 DX의 차별점을 인지하고요. |

---

## 4. 티어 B — 사슬 대부분 충족 (65건, 전량)

| 제목 | 채널 | 월 | 블록수 | 블록 | 관련성/톤 |
|---|---|---|---:|---|---|
| [AMD at CES® 2026 Replay](https://www.youtube.com/watch?v=ypSay3Ehxow) | AMD | 2026-01 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/washing |
| [Advancing AI 2026 Replay | Build What's Next with @AMD](https://www.youtube.com/watch?v=8B_Gese-bdI) | AMD | 2026-07 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [AWS European Sovereign Cloud – Explained | AWS Events](https://www.youtube.com/watch?v=GbitrLroyMU) | AWS Events | 2026-06 | 6 | B1·B3·B4·B5·B7·B8 | ax_core/anti_washing |
| [AWS Summit Bengaluru 2026: Innovators Edition Keynote | AWS ](https://www.youtube.com/watch?v=CprBATdRoh0) | AWS Events | 2026-06 | 6 | B1·B2·B4·B5·B6·B7 | ax_core/anti_washing |
| [AWS Summit Washington DC 2026 - Keynote | Amazon Web Service](https://www.youtube.com/watch?v=QGaPF8NsOE4) | AWS Events | 2026-06 | 6 | B1·B4·B5·B6·B7·B8 | ax_core/anti_washing |
| [Top Banking Trends 2026 - Unconstrained Banking | Accenture](https://www.youtube.com/watch?v=MWvdwSD3ZRc) | Accenture | 2026-02 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [Leading AI Transformation: A Chief AI Officer's Perspective ](https://www.youtube.com/watch?v=LblTPS1LnLc) | Amazon Web Services | 2026-07 | 6 | B1·B3·B4·B5·B6·B7 | ax_core/neutral |
| [How AbbVie accelerates drug discovery with Claude](https://www.youtube.com/watch?v=NfoFdsc2ODQ) | Anthropic | 2025-10 | 6 | B1·B3·B4·B5·B7·B8 | ax_core/anti_washing |
| [What does AI mean for education?](https://www.youtube.com/watch?v=Uh98_aGhAuY) | Anthropic | 2025-12 | 6 | B1·B2·B4·B5·B7·B8 | ax_adjacent/anti_washing |
| [With 180 Years of Reinvention, Pearson Takes on the AI Era](https://www.youtube.com/watch?v=YBe0oiv01N0) | Boston Consulting Group | 2026-07 | 6 | B1·B3·B4·B5·B6·B7 | ax_core/anti_washing |
| [Cerebras CISO Naor Penso on AI Security & The CrowdStrike Pa](https://www.youtube.com/watch?v=sD2kVXOfhLs) | Cerebras | 2026-07 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Nikhil Pentapalli - Crafting a Successful AI Career & Transi](https://www.youtube.com/watch?v=IExfnhecorw) | Cohere | 2025-08 | 6 | B1·B2·B5·B6·B7·B8 | ax_core/anti_washing |
| [The Complete AI Transformation Blueprint - Live Workshop](https://www.youtube.com/watch?v=OcTMwjqje5Q) | Cole Medin | 2026-07 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Deploying AI Agents In The Enterprise](https://www.youtube.com/watch?v=cKGyiwsm66I) | Cresta | 2026-08 | 6 | B1·B2·B4·B6·B7·B8 | ax_core/anti_washing |
| [Unscripted: How Banks & Insurers Grow with Data, AI Agents a](https://www.youtube.com/watch?v=Vy5oNJgPdyQ) | Databricks | 2025-12 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Ali Ghodsi, Co-founder and CEO, Databricks kicks off Data + ](https://www.youtube.com/watch?v=M_rlJXln5KE) | Databricks | 2026-06 | 6 | B1·B2·B4·B5·B6·B8 | ax_core/neutral |
| [Beyond the hype: Orchestrating end-to-end developer workflow](https://www.youtube.com/watch?v=t6jH_GPFqgs) | Google Cloud Tech | 2026-06 | 6 | B1·B4·B5·B6·B7·B8 | ax_core/washing |
| [Building enterprise-grade AI agents: How enterprises scale b](https://www.youtube.com/watch?v=3vf9eL-LKUY) | Google Cloud Tech | 2026-06 | 6 | B1·B3·B4·B5·B6·B7 | ax_core/anti_washing |
| [The Power of Open Source: Building Giants in the Open](https://www.youtube.com/watch?v=aNCLqvTCxeg) | Hugging Face | 2025-11 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [Federated Learning: A New Era of Collaboration for Pharma | ](https://www.youtube.com/watch?v=_lhB9Zo915c) | Intel | 2024-12 | 6 | B1·B2·B4·B5·B6·B8 | ax_core/anti_washing |
| [Personalized Marketing: How Movable Ink Delivers with AI and](https://www.youtube.com/watch?v=22EBTikBULk) | Intel | 2024-12 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [Intel’s Whole Vehicle Advantage to SDV | Intel](https://www.youtube.com/watch?v=qmIFB8MC7bM) | Intel | 2025-01 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [AI’s Next Frontier: Human Collaboration, Data Strategy, and ](https://www.youtube.com/watch?v=hFTRv3Va5IE) | Intel | 2025-07 | 6 | B1·B3·B4·B5·B7·B8 | ax_core/washing |
| [Graph Technology Meets GenAI: A Neo4j Perspective | Intel](https://www.youtube.com/watch?v=7pdMtkezuVI) | Intel | 2025-08 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/washing |
| [Inside the AI-Powered Workplace: How Intel Sees the Future o](https://www.youtube.com/watch?v=F-_ZQo52sTQ) | Intel | 2025-09 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/neutral |
| [AI That Moves the World keynote | Intel](https://www.youtube.com/watch?v=JzZQTYCuxkM) | Intel | 2026-03 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [Agentic AI Adoption Secrets You Need to Know Now](https://www.youtube.com/watch?v=-0V6XUskt-k) | Kore.ai | 2026-07 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Why AI Projects Fail: Lessons from the US Army & Kotter | Ko](https://www.youtube.com/watch?v=jfpIvZy89UM) | Kotter International Inc | 2026-08 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Transforming R&D With AI: Breaking Barriers and Boosting Pro](https://www.youtube.com/watch?v=pNz4E6IX5K8) | McKinsey & Company | 2025-10 | 6 | B1·B3·B5·B6·B7·B8 | ax_core/anti_washing |
| [Agentic AI and the Future of Travel: What executives need to](https://www.youtube.com/watch?v=dmKFLspjYNw) | McKinsey & Company | 2025-12 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Rewired To Win: Reimagining the Enterprise With Tech and AI](https://www.youtube.com/watch?v=HoHFZ-Fzu_g) | McKinsey & Company | 2026-04 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Agentic AI and the future of Global Business Services](https://www.youtube.com/watch?v=LuHGabkzlGU) | McKinsey & Company | 2026-08 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/neutral |
| [Oracle AI Database@Azure Panel Discussion with MVPs](https://www.youtube.com/watch?v=bgx0TX45md8) | Microsoft Azure | 2026-04 | 6 | B1·B2·B3·B4·B6·B7 | ax_core/anti_washing |
| [Snap’s GPU-Accelerated Secret to Processing 10 Petabytes a D](https://www.youtube.com/watch?v=glT-zO8B_qk) | NVIDIA | 2026-05 | 6 | B1·B2·B3·B4·B5·B8 | ax_core/anti_washing |
| [Oracle at Gartner CSO: Demand More from Enterprise AI](https://www.youtube.com/watch?v=yhrBN_Ka-iA) | Oracle | 2026-07 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Vector Search in Retail ft. Jacob Zweig (Strong) and Mark Mo](https://www.youtube.com/watch?v=rVqNBYTpDLw) | Pinecone | 2022-08 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/neutral |
| [Customer Success Keynote: Connected to Win: From Moment to M](https://www.youtube.com/watch?v=dG9aBkJCcso) | SAP | 2026-05 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Customer Success Keynote: Connected to Win: From Moment to M](https://www.youtube.com/watch?v=WpDHkeHIezc) | SAP | 2026-05 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Global Keynote: The Beginning of Better | SAP Sapphire Orlan](https://www.youtube.com/watch?v=9aa-etRsaLU) | SAP | 2026-05 | 6 | B1·B2·B4·B5·B6·B7 | ax_core/anti_washing |
| [Win More Sales: Salesforce Agentforce for Sales Productivity](https://www.youtube.com/watch?v=fJxyv1bYJoc) | Salesforce | 2026-02 | 6 | B1·B2·B5·B6·B7·B8 | ax_core/anti_washing |
| [Siemens, Capgemini, EDP and Kraken on how AI will transform ](https://www.youtube.com/watch?v=tolLHQWJzKY) | Siemens | 2026-01 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/neutral |
| [BUILD 2025 Opening Keynote: Building the Agentic AI Future](https://www.youtube.com/watch?v=MPLMS0736zI) | Snowflake | 2025-11 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Snowflake Summit 2026 Builder Keynote](https://www.youtube.com/watch?v=WFR07HIvCrQ) | Snowflake | 2026-07 | 6 | B1·B4·B5·B6·B7·B8 | ax_core/anti_washing |
| [Telco Tech Talks: Why is Amazon so successful?](https://www.youtube.com/watch?v=u-hbE8vRNw8) | Telenor | 2022-09 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/neutral |
| [Telco Tech Talks: How do we develop our people to meet the f](https://www.youtube.com/watch?v=fythNeXmXnM) | Telenor | 2023-04 | 6 | B1·B2·B3·B4·B5·B6 | ax_core/anti_washing |
| [Investor Event 2024 CEO Presentation | Unilever](https://www.youtube.com/watch?v=r_BOLVAd0Kw) | Unilever | 2024-11 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/neutral |
| [Investor Event 2024 | Unilever](https://www.youtube.com/watch?v=yuMA_iYdq4w) | Unilever | 2024-11 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [CEO addresses Barclays Global Consumer Staples Conference 20](https://www.youtube.com/watch?v=yxNDSJUzFm8) | Unilever | 2025-09 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Consumer Analyst Group of New York Conference 2026 | Unileve](https://www.youtube.com/watch?v=SXT5EV4VR-U) | Unilever | 2026-02 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/neutral |
| [SXSW 2024 | Waymo’s Roadmap for a Multi-City AV Service](https://www.youtube.com/watch?v=Qot1uX2g9jk) | Waymo | 2024-03 | 6 | B2·B3·B4·B5·B7·B8 | ax_core/anti_washing |
| [Snowflake’s CEO Sridhar Ramaswamy on 700+ LLM enterprise use](https://www.youtube.com/watch?v=WUJIrkb3sow) | Weights & Biases | 2024-10 | 6 | B1·B2·B3·B4·B5·B8 | ax_core/anti_washing |
| [Deepseek, Stargate and AI’s $600 billion question with Sequo](https://www.youtube.com/watch?v=2Bpf7lOfYiA) | Weights & Biases | 2025-01 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [LLMOps in action: Streamlining the path from prototype to pr](https://www.youtube.com/watch?v=E1DTsgbZPhw) | Weights & Biases | 2025-01 | 6 | B1·B4·B5·B6·B7·B8 | ax_core/anti_washing |
| [AI, autonomy, and the future of naval warfare with Captain J](https://www.youtube.com/watch?v=guxzPymyz-w) | Weights & Biases | 2025-03 | 6 | B1·B2·B4·B5·B6·B7 | ax_core/anti_washing |
| [The Startup Powering The Data Behind AGI](https://www.youtube.com/watch?v=X39OZndIWSY) | Weights & Biases | 2025-09 | 6 | B1·B2·B4·B5·B7·B8 | ax_adjacent/anti_washing |
| [The $2B Company Cutting AI Costs By 60% | Tuhin Srivastava](https://www.youtube.com/watch?v=QJUsxm1Nmos) | Weights & Biases | 2025-11 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/neutral |
| [Are Humanoid Robots Actually Coming to Your Home? | Nikolaus](https://www.youtube.com/watch?v=vvvwWv5BK-s) | Weights & Biases | 2025-12 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Why Anthropic, Meta, and Tesla All Chose the Same Database |](https://www.youtube.com/watch?v=b7fGSA9mVYI) | Weights & Biases | 2026-03 | 6 | B1·B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Zapier AI Showcase: 50 Million Tasks Delegated (The Best Use](https://www.youtube.com/watch?v=pGjirCLK9qE) | Zapier | 2025-11 | 6 | B1·B2·B3·B5·B7·B8 | ax_core/anti_washing |
| [The Executive Blueprint for Responsible AI Governance: Pract](https://www.youtube.com/watch?v=-Y22OVH2w1o) | Zapier | 2026-04 | 6 | B1·B2·B3·B5·B7·B8 | ax_core/anti_washing |
| [Steal Zapier's AI Playbook for Accounting: How 8 People Run ](https://www.youtube.com/watch?v=CxrrXKFn6cg) | Zapier | 2026-05 | 6 | B1·B2·B3·B4·B7·B8 | ax_core/anti_washing |
| [The Business Impact of AI Agents: Use Cases, ROI, and Future](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) | [EN] VlogMe AI | 2026-08 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [26 Years of Survival Keyword AX (Great AI Transformation): W](https://www.youtube.com/watch?v=VRYJJJBqsDE) | 메타코드M | 2026-07 | 6 | B1·B4·B5·B6·B7·B8 | ax_core/anti_washing |
| [현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)](https://www.youtube.com/watch?v=b-tgY8Q0SbA) | 티타임즈TV | 2026-07 | 6 | B1·B3·B4·B5·B7·B8 | ax_core/washing |
| [AI 도입의 격차, 상위 5% 기업의 AI 활용 전략 - 마이크로소프트 백인송 이사 [AI TECH 2026](https://www.youtube.com/watch?v=p9Tj9ctxMr8) | 헬로티_매일 만나는 산업, IT News | 2026-07 | 6 | B1·B2·B4·B5·B7·B8 | ax_core/anti_washing |

---

## 5. 구성요소별 대표 사례 (적중 상위 15)

> 특정 구성요소를 집중적으로 다루는 사례. 개별 구성요소 심층 코딩의 출발점.


### B1 · 디지털·AI 기술의 활용 (사례 521건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [[Brown-Bag 런치세미나] 공공을 위한 클라우드 상품](https://www.youtube.com/watch?v=52qSYsUFIkw) | NAVER Cloud | 2023-10 | 206 | 4 |
| [Microsoft Digital Sovereignty Summit | Sovereign Cloud, AI](https://www.youtube.com/watch?v=YLL7UuVCerM) | Microsoft Azure | 2026-04 | 137 | 8 |
| [What's new in Cloud Run](https://www.youtube.com/watch?v=AoisAy_LGpI) | Google Cloud Tech | 2026-06 | 121 | 4 |
| [AWS European Sovereign Cloud – Explained | AWS Events](https://www.youtube.com/watch?v=GbitrLroyMU) | AWS Events | 2026-06 | 108 | 6 |
| [What's new in Cloud SQL: Drive performance, high availabil](https://www.youtube.com/watch?v=zKXbKmpqWB0) | Google Cloud Tech | 2026-06 | 97 | 4 |
| [[Brown-Bag 런치세미나] 2024년 보안트렌드 살펴보기](https://www.youtube.com/watch?v=6OUSU8wzvac) | NAVER Cloud | 2024-04 | 91 | 4 |
| [Build, Test, and Deploy Production-Ready Enterprise AI Age](https://www.youtube.com/watch?v=P0kux8A8NbM) | Solutions Review | 2026-08 | 89 | 7 |
| [Streamlining RAG Applications with Canopy](https://www.youtube.com/watch?v=d9QPDQ50B-A) | Pinecone | 2024-01 | 85 | 4 |
| [LLMOps in action: Streamlining the path from prototype to ](https://www.youtube.com/watch?v=E1DTsgbZPhw) | Weights & Biases | 2025-01 | 74 | 6 |
| [The Business Impact of AI Agents: Use Cases, ROI, and Futu](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) | [EN] VlogMe AI | 2026-08 | 73 | 6 |
| [Fully Connected Tokyo: [Hands-on workshop] From 0 to autom](https://www.youtube.com/watch?v=BX-AjQUUol8) | Weights & Biases | 2026-01 | 72 | 4 |
| [What’s New in SAP HANA Cloud | Deep Dive with Product Expe](https://www.youtube.com/watch?v=QrGR38jGGZo) | SAP | 2026-07 | 69 | 4 |
| [Data + AI Summit Keynote 2026 | Day 1](https://www.youtube.com/watch?v=Qux8E-L1mk8) | Databricks | 2026-06 | 66 | 7 |
| [Global Keynote: The Beginning of Better | SAP Sapphire Mad](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 62 | 5 |
| [Prepare for Microsoft Certification Exam AB-731: AI Transf](https://www.youtube.com/watch?v=mj_lyhuWbig) | Microsoft Learn | 2026-07 | 58 | 7 |

### B2 · 파괴: 소비자 행동·기대 (사례 201건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Aditri Bhagirath  - Persona Guided Personalization](https://www.youtube.com/watch?v=0X01DFnA2dc) | Cohere | 2026-01 | 28 | 5 |
| [Ahsaas Bajaj  - Production Grade ML in Practice  Evaluatio](https://www.youtube.com/watch?v=UkOvqHSskMw) | Cohere | 2026-01 | 19 | 5 |
| [Agentforce Marketing Keynote | Connections 2026](https://www.youtube.com/watch?v=9g-S56GGhN0) | Salesforce | 2026-06 | 19 | 4 |
| [CCW 2026: Dominion Energy’s AI-Powered Transformation with](https://www.youtube.com/watch?v=d2nUemwh30c) | AWS Events | 2026-07 | 17 | 4 |
| [CCW 2026: How Citizens Bank is building the AI-native cust](https://www.youtube.com/watch?v=O_Imo9L04mo) | AWS Events | 2026-07 | 17 | 4 |
| [Webinar: AI transformation that works, lessons from the tr](https://www.youtube.com/watch?v=PL3OWn143AI) | BOI (Board of Innovati | 2026-07 | 14 | 7 |
| [Unscripted: How Banks & Insurers Grow with Data, AI Agents](https://www.youtube.com/watch?v=Vy5oNJgPdyQ) | Databricks | 2025-12 | 14 | 6 |
| [Personalized Marketing: How Movable Ink Delivers with AI a](https://www.youtube.com/watch?v=22EBTikBULk) | Intel | 2024-12 | 14 | 6 |
| [The Business Impact of AI Agents: Use Cases, ROI, and Futu](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) | [EN] VlogMe AI | 2026-08 | 12 | 6 |
| [The Future of Customer Experience - Creativity, Trust & Te](https://www.youtube.com/watch?v=taeDyZI86h8) | Infosys | 2026-03 | 10 | 8 |
| [Qdrant Vector Space Day 2025 | Opening Keynotes](https://www.youtube.com/watch?v=Vgbg7uIddnA) | Qdrant | 2025-10 | 10 | 7 |
| [Expert AI Alliance Workshop – Full Version](https://www.youtube.com/watch?v=3aSJ0XdENkU) | LG AI Research | 2022-02 | 10 | 4 |
| [Inside Instacart's AI-Powered Smart Shopping Cart | NVIDIA](https://www.youtube.com/watch?v=Alz-bhXqyXM) | NVIDIA | 2026-06 | 10 | 4 |
| [In the era of AI transformation (AX), we'll teach you ever](https://www.youtube.com/watch?v=ErviFf8I6K4) | 메타코드M | 2026-07 | 9 | 8 |
| [CCW 2026: Be the 5%: What We Learned Shipping AI at Amazon](https://www.youtube.com/watch?v=Sww2jYuqk7w) | AWS Events | 2026-07 | 9 | 5 |

### B2 · 파괴: 경쟁구도 (사례 116건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Making AI Transformation Work: Avoiding the Mistakes from ](https://www.youtube.com/watch?v=CoPCP3f1DzM) | INSEAD | 2026-07 | 10 | 7 |
| [The Business Impact of AI Agents: Use Cases, ROI, and Futu](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) | [EN] VlogMe AI | 2026-08 | 10 | 6 |
| [2026 SEO Strategy: How Marketers Win The New LLM Search Ga](https://www.youtube.com/watch?v=BV_ZtkqyzkM) | Zapier | 2025-12 | 10 | 4 |
| [How AI Is Changing Enterprise](https://www.youtube.com/watch?v=aIKfA3gIXwo) | Y Combinator | 2026-07 | 9 | 7 |
| [Barclays Consumer Health Conference 2026](https://www.youtube.com/watch?v=oOyDsMsCmqI) | Unilever | 2026-06 | 8 | 5 |
| [Lead with Purpose, Adapt with Strategy | Phillip Benedetti](https://www.youtube.com/watch?v=c9-0LUYKwhI) | Boston Consulting Grou | 2026-08 | 8 | 4 |
| [Reckitt - Half Year 2025 Results](https://www.youtube.com/watch?v=KP7oflfrcMI) | Reckitt | 2025-07 | 8 | 4 |
| [Fireside Chat with Fernando Fernandez, Unilever CEO and Ce](https://www.youtube.com/watch?v=djVmMTAMEho) | Unilever | 2025-12 | 8 | 4 |
| [CEO addresses Barclays Global Consumer Staples Conference ](https://www.youtube.com/watch?v=yxNDSJUzFm8) | Unilever | 2025-09 | 7 | 6 |
| [Unilever | H1 2025 | Results | Webcast & Q&A – audio-descr](https://www.youtube.com/watch?v=oMDBIXBEv3Q) | Unilever | 2025-10 | 7 | 5 |
| [JP Morgan Consumer CEO Series: An interview with Kris Lich](https://www.youtube.com/watch?v=cAT6AqBk_-k) | Reckitt | 2025-07 | 7 | 4 |
| [Investor Event 2024 | Unilever](https://www.youtube.com/watch?v=yuMA_iYdq4w) | Unilever | 2024-11 | 6 | 6 |
| [Why Anthropic, Meta, and Tesla All Chose the Same Database](https://www.youtube.com/watch?v=b7fGSA9mVYI) | Weights & Biases | 2026-03 | 6 | 6 |
| [The Biggest AI Opportunity Isn’t Replacing People | Stanfo](https://www.youtube.com/watch?v=u76xdhpF474) | McKinsey & Company | 2026-08 | 6 | 5 |
| [Why Most Companies Aren't Seeing Meaningful Returns from A](https://www.youtube.com/watch?v=BHQyOFaARQI) | McKinsey & Company | 2026-07 | 6 | 5 |

### B2 · 파괴: 데이터 가용성 (사례 155건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Bits & Bytes: Vector Augmented Labeling & Classification](https://www.youtube.com/watch?v=RuJGoV87Et4) | Pinecone | 2024-06 | 22 | 4 |
| [Millions of Users and Billions of Files: Box CTO on Buildi](https://www.youtube.com/watch?v=B3E3qhTWSSg) | Zapier | 2025-10 | 19 | 5 |
| [Data + AI Summit Keynote 2026 | Day 1](https://www.youtube.com/watch?v=Qux8E-L1mk8) | Databricks | 2026-06 | 11 | 7 |
| [Build Custom Large-Scale Generative AI Models | NVIDIA GTC](https://www.youtube.com/watch?v=npQMSpCA4Lo) | NVIDIA Developer | 2026-04 | 10 | 4 |
| [NYC Executive Forum 2026 - A Leader’s Guide to Data Strate](https://www.youtube.com/watch?v=Piy37om0y6A) | AWS Events | 2026-07 | 9 | 5 |
| [Databricks x Palantir | Partnership Deep Dive](https://www.youtube.com/watch?v=BsSwqYuok1A) | Databricks | 2026-01 | 9 | 5 |
| [Ali Ghodsi, Co-founder and CEO, Databricks kicks off Data ](https://www.youtube.com/watch?v=M_rlJXln5KE) | Databricks | 2026-06 | 8 | 6 |
| [Empowering Agility: DraftKings’ Strategy for Compliance an](https://www.youtube.com/watch?v=F01IEeM3I-Y) | Snowflake | 2025-11 | 8 | 5 |
| [A leader's guide to data strategy in the era of agentic AI](https://www.youtube.com/watch?v=3XyNPfWWxiQ) | AWS Events | 2026-06 | 8 | 4 |
| [Operationalizing GraphRAG: Lettria’s Scalable Architecture](https://www.youtube.com/watch?v=3guLRa5yQEk) | Qdrant | 2025-07 | 8 | 4 |
| [Self-Driven Women: Engineering the future of autonomy](https://www.youtube.com/watch?v=cvqGkq2SGWQ) | Waymo | 2021-11 | 8 | 4 |
| [Making AI Transformation Work: Avoiding the Mistakes from ](https://www.youtube.com/watch?v=CoPCP3f1DzM) | INSEAD | 2026-07 | 7 | 7 |
| [Snowflake Summit 2026 Platform Keynote](https://www.youtube.com/watch?v=CtqKJV6gyGQ) | Snowflake | 2026-06 | 7 | 7 |
| [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 티타임즈TV | 2026-07 | 7 | 5 |
| [How AI Transforms Retail, Finance and Manufacturing in 202](https://www.youtube.com/watch?v=11degQs3L7c) | Snowflake | 2025-12 | 6 | 7 |

### B3 · 전략적 대응 (사례 220건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [The Boardroom Mandate: Scaling AI for Business Impact | Da](https://www.youtube.com/watch?v=0ixUiXr2DVY) | Infosys | 2026-02 | 30 | 7 |
| [Sequoia's Doug Leone on Building Enduring Companies in the](https://www.youtube.com/watch?v=afSmwxT0Y3o) | ElevenLabs | 2026-03 | 21 | 4 |
| [Scale AI AI Playbook for Business Leaders | ALL IN 2024](https://www.youtube.com/watch?v=TPN6hbY40TU) | Scale AI | 2024-09 | 19 | 5 |
| [Direct Connect 2025 Keynote | Intel](https://www.youtube.com/watch?v=0ED7n2g8lO0) | Intel | 2025-04 | 15 | 5 |
| [Making AI Transformation Work: Avoiding the Mistakes from ](https://www.youtube.com/watch?v=CoPCP3f1DzM) | INSEAD | 2026-07 | 13 | 7 |
| [현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)](https://www.youtube.com/watch?v=b-tgY8Q0SbA) | 티타임즈TV | 2026-07 | 12 | 6 |
| [No Lanes: How Claire Vo Runs an AI-Native Company on Her O](https://www.youtube.com/watch?v=_Wg2oTfwb4g) | Zapier | 2026-03 | 12 | 4 |
| [Microsoft Digital Sovereignty Summit | Sovereign Cloud, AI](https://www.youtube.com/watch?v=YLL7UuVCerM) | Microsoft Azure | 2026-04 | 11 | 8 |
| [Webinar: AI transformation that works, lessons from the tr](https://www.youtube.com/watch?v=PL3OWn143AI) | BOI (Board of Innovati | 2026-07 | 11 | 7 |
| [AI for AI: Building the Transformation Office That Drives ](https://www.youtube.com/watch?v=OJwpw-8SkBM) | Tigerhall | 2026-07 | 11 | 7 |
| [Sunlight on Shadow AI: When Security Learns to Tinker—Rob ](https://www.youtube.com/watch?v=qlCkwGSRP3w) | Zapier | 2025-12 | 11 | 7 |
| [How Executive Assistants Drive Strategic Impact with AI](https://www.youtube.com/watch?v=-gGwrSPc3tA) | Zapier | 2025-11 | 11 | 4 |
| [Top Banking Trends 2026 - Unconstrained Banking | Accentur](https://www.youtube.com/watch?v=MWvdwSD3ZRc) | Accenture | 2026-02 | 10 | 6 |
| [AI isn’t digital transformation, and leaders need to under](https://www.youtube.com/watch?v=eZ1NizUx9U4) | IBM | 2026-07 | 10 | 5 |
| [Eric Ries on Vibe Coding and Building Incorruptible Compan](https://www.youtube.com/watch?v=Qs33r-Nreb8) | Zapier | 2026-06 | 10 | 5 |

### B4 · 가치제안 변화 (사례 27건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y) | Infosys | 2026-07 | 7 | 5 |
| [Qdrant Vector Space Day 2025 | Opening Keynotes](https://www.youtube.com/watch?v=Vgbg7uIddnA) | Qdrant | 2025-10 | 6 | 7 |
| [How AI Is Changing Enterprise](https://www.youtube.com/watch?v=aIKfA3gIXwo) | Y Combinator | 2026-07 | 6 | 7 |
| [End of Islands - Unified Asset Lifecycle is the Digital Fa](https://www.youtube.com/watch?v=xjFSF4jCvpk) | Schneider Electric | 2026-07 | 6 | 4 |
| [Graph Technology Meets GenAI: A Neo4j Perspective | Intel](https://www.youtube.com/watch?v=7pdMtkezuVI) | Intel | 2025-08 | 5 | 6 |
| [The Serial Builder Advantage: Why Repeat Innovators Win](https://www.youtube.com/watch?v=kzAjzKCZAXs) | McKinsey & Company | 2026-07 | 4 | 4 |
| [Q3 Trading and Strategic Update](https://www.youtube.com/watch?v=zN3xR9s4uZM) | Reckitt | 2023-10 | 4 | 4 |
| [Move First or Fall Behind: How AI Is Rewriting the Rules o](https://www.youtube.com/watch?v=ieGq5bdmRcI) | McKinsey & Company | 2026-05 | 3 | 5 |
| [Meta Horizon Store: Paths to Engage and Monetize Your Audi](https://www.youtube.com/watch?v=DK5Q6C8Iepo) | Meta Developers | 2025-10 | 3 | 5 |
| [Alex Hormozi’s New Playbook: Entrepreneurship in the Age o](https://www.youtube.com/watch?v=6Ait5R-3-lI) | Replit | 2025-10 | 3 | 5 |
| [Why Big Tech Buys GPUs From CoreWeave | Corey Sanders](https://www.youtube.com/watch?v=h3SNaAPUxHY) | Weights & Biases | 2026-01 | 3 | 4 |
| [[ifkakao2021] Daum Mail Terraforming:  다음 메일 백엔ᄃ](https://www.youtube.com/watch?v=r2t4h3qMXzw) | kakao tech | 2026-06 | 3 | 4 |
| [Developing and Deploying Databricks ai_parse_document for ](https://www.youtube.com/watch?v=kH7p1lr4Be4) | Databricks | 2025-12 | 2 | 7 |
| [Prepare for Microsoft Certification Exam AB-731: AI Transf](https://www.youtube.com/watch?v=mj_lyhuWbig) | Microsoft Learn | 2026-07 | 2 | 7 |
| [Advancing AI 2026 Replay | Build What's Next with @AMD](https://www.youtube.com/watch?v=8B_Gese-bdI) | AMD | 2026-07 | 2 | 6 |

### B4 · 가치네트워크·생태계 (사례 387건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Direct Connect 2025 Keynote | Intel](https://www.youtube.com/watch?v=0ED7n2g8lO0) | Intel | 2025-04 | 74 | 5 |
| [Advancing AI 2026 Replay | Build What's Next with @AMD](https://www.youtube.com/watch?v=8B_Gese-bdI) | AMD | 2026-07 | 50 | 6 |
| [Intel Computex Keynote 2026](https://www.youtube.com/watch?v=7HvrdXjdlU8) | Intel | 2026-06 | 40 | 5 |
| [Global Keynote: The Beginning of Better | SAP Sapphire Orl](https://www.youtube.com/watch?v=9aa-etRsaLU) | SAP | 2026-05 | 34 | 6 |
| [Edge AI – The Next Transformation | Intel](https://www.youtube.com/watch?v=xPadduZuK4Q) | Intel | 2025-05 | 33 | 4 |
| [Expert AI Alliance Workshop – Full Version](https://www.youtube.com/watch?v=3aSJ0XdENkU) | LG AI Research | 2022-02 | 28 | 4 |
| [Investor Event 2024 | Unilever](https://www.youtube.com/watch?v=yuMA_iYdq4w) | Unilever | 2024-11 | 27 | 6 |
| [Meta Connect Keynote 2022](https://www.youtube.com/watch?v=hvfV-iGwYX8) | Meta | 2022-10 | 26 | 5 |
| [Microsoft Digital Sovereignty Summit | Sovereign Cloud, AI](https://www.youtube.com/watch?v=YLL7UuVCerM) | Microsoft Azure | 2026-04 | 25 | 8 |
| [AMD at CES® 2026 Replay](https://www.youtube.com/watch?v=ypSay3Ehxow) | AMD | 2026-01 | 25 | 6 |
| [Telco Tech Talks: How do we develop our people to meet the](https://www.youtube.com/watch?v=fythNeXmXnM) | Telenor | 2023-04 | 24 | 6 |
| [LG AI Talk Concert 2025 - Shaping the Future of AI](https://www.youtube.com/watch?v=EGzIMo4AizA) | LG AI Research | 2025-07 | 24 | 5 |
| [Data + AI Summit Keynote 2026 | Day 1](https://www.youtube.com/watch?v=Qux8E-L1mk8) | Databricks | 2026-06 | 23 | 7 |
| [Global Keynote: The Beginning of Better | SAP Sapphire Mad](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 23 | 5 |
| [Meet the new Slack. Where AI works.](https://www.youtube.com/watch?v=6DtrYEHRHw4) | Salesforce | 2026-04 | 23 | 5 |

### B4 · 디지털 채널 (사례 39건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [[Solution showcase] 자유롭고 유연한 커스텀 환경으로 차별화된 이커머스 구축](https://www.youtube.com/watch?v=J4BsujJyTBo) | NAVER Cloud | 2024-03 | 49 | 4 |
| [CCW 2026: How Citizens Bank is building the AI-native cust](https://www.youtube.com/watch?v=O_Imo9L04mo) | AWS Events | 2026-07 | 40 | 4 |
| [CCW 2026: Dominion Energy’s AI-Powered Transformation with](https://www.youtube.com/watch?v=d2nUemwh30c) | AWS Events | 2026-07 | 12 | 4 |
| [O-Ring Automation & the Economics of Bicycles for the Mind](https://www.youtube.com/watch?v=uUUBApVevNI) | Cohere | 2026-06 | 11 | 5 |
| [Reckitt Full Year Results 2025](https://www.youtube.com/watch?v=ExpojFs6mCg) | Reckitt | 2026-03 | 10 | 5 |
| [Build and monitor multi-agent contact centers using Weight](https://www.youtube.com/watch?v=MjqHVfmKEoM) | Weights & Biases | 2025-10 | 9 | 4 |
| [Deploying AI Agents In The Enterprise](https://www.youtube.com/watch?v=cKGyiwsm66I) | Cresta | 2026-08 | 8 | 6 |
| [Why Big Tech Buys GPUs From CoreWeave | Corey Sanders](https://www.youtube.com/watch?v=h3SNaAPUxHY) | Weights & Biases | 2026-01 | 8 | 4 |
| [Move First or Fall Behind: How AI Is Rewriting the Rules o](https://www.youtube.com/watch?v=ieGq5bdmRcI) | McKinsey & Company | 2026-05 | 7 | 5 |
| [Expert AI Alliance Workshop – Full Version](https://www.youtube.com/watch?v=3aSJ0XdENkU) | LG AI Research | 2022-02 | 7 | 4 |
| [CCW 2026: AI Can't Personalize What It Can't See: Turning ](https://www.youtube.com/watch?v=53A20B6Ras8) | AWS Events | 2026-07 | 6 | 5 |
| [How Orium’s AI Playbook Turned Complexity into 5x Growth |](https://www.youtube.com/watch?v=5st7XEHY_pA) | Zapier | 2025-11 | 6 | 4 |
| [Webinar: AI transformation that works, lessons from the tr](https://www.youtube.com/watch?v=PL3OWn143AI) | BOI (Board of Innovati | 2026-07 | 4 | 7 |
| [The Boardroom Mandate: Scaling AI for Business Impact | Da](https://www.youtube.com/watch?v=0ixUiXr2DVY) | Infosys | 2026-02 | 4 | 7 |
| [Unscripted: How Banks & Insurers Grow with Data, AI Agents](https://www.youtube.com/watch?v=Vy5oNJgPdyQ) | Databricks | 2025-12 | 4 | 6 |

### B4 · 민첩성·양손잡이 (사례 73건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [The new post-quantum cryptography executive order. Plus: W](https://www.youtube.com/watch?v=RYUR9BdDgyI) | IBM Technology | 2026-07 | 14 | 4 |
| [The Magic of Multilingual Search with Pinecone Serverless ](https://www.youtube.com/watch?v=moHIBWZiYdY) | Pinecone | 2024-09 | 9 | 4 |
| [Customer Success Keynote: Connected to Win: From Moment to](https://www.youtube.com/watch?v=WpDHkeHIezc) | SAP | 2026-05 | 7 | 6 |
| [AI Transformation AMA for HR Leaders](https://www.youtube.com/watch?v=lYOR4pgVdb0) | Zapier | 2025-09 | 7 | 5 |
| [Enterprise strategies for agentic AI adoption in 2026 and ](https://www.youtube.com/watch?v=B4WgQotMVmE) | Vertesia | 2026-07 | 6 | 7 |
| [Empowering Agility: DraftKings’ Strategy for Compliance an](https://www.youtube.com/watch?v=F01IEeM3I-Y) | Snowflake | 2025-11 | 6 | 5 |
| [Defining AI Fluency: A Fireside Chat With The Executives](https://www.youtube.com/watch?v=Rq1lzDDfTrU) | Zapier | 2025-12 | 6 | 5 |
| [Bruno Zerbib on AI, Intelligent Networks and the Future of](https://www.youtube.com/watch?v=xPpwRnoZzlo) | Orange | 2026-03 | 6 | 4 |
| [The Business Impact of AI Agents: Use Cases, ROI, and Futu](https://www.youtube.com/watch?v=vfQpQ2PwoEQ) | [EN] VlogMe AI | 2026-08 | 5 | 6 |
| [Agentic AI and the Future of Software Development: S3 E4](https://www.youtube.com/watch?v=eQ6tb7j3Z2U) | AMD | 2026-07 | 5 | 5 |
| [Enterprise AI Adoption in 2025: What Actually Works](https://www.youtube.com/watch?v=9MkMQ6zkjLw) | The Tech Trek | 2026-07 | 5 | 5 |
| [Tokyo Executive Forum 2026 - Fireside Chat with Jason Benn](https://www.youtube.com/watch?v=1YbKbO1p7GQ) | AWS Events | 2026-07 | 5 | 4 |
| [Closing the Enterprise AI ROI Gap](https://www.youtube.com/watch?v=20lqu-d4cxc) | AI:ROI Conversations w | 2026-08 | 4 | 7 |
| [Enterprise AI Strategy and CEO Leadership, with McKinsey &](https://www.youtube.com/watch?v=uTRKdCY4HdE) | CXOTalk | 2026-08 | 4 | 7 |
| [Advancing AI 2026 Replay | Build What's Next with @AMD](https://www.youtube.com/watch?v=8B_Gese-bdI) | AMD | 2026-07 | 4 | 6 |

### B5 · 조직구조 변화 (사례 100건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Snowflake Summit 2026 Platform Keynote](https://www.youtube.com/watch?v=CtqKJV6gyGQ) | Snowflake | 2026-06 | 12 | 7 |
| [Federated Learning: A New Era of Collaboration for Pharma ](https://www.youtube.com/watch?v=_lhB9Zo915c) | Intel | 2024-12 | 11 | 6 |
| [Brand Finance Global 500 Launch 2026 | AI Rising: The Evol](https://www.youtube.com/watch?v=2GboyaQ1VKs) | Infosys | 2026-03 | 11 | 5 |
| [A leader's guide to data strategy in the era of agentic AI](https://www.youtube.com/watch?v=3XyNPfWWxiQ) | AWS Events | 2026-06 | 9 | 4 |
| [NYC Executive Forum 2026 - A Leader’s Guide to Data Strate](https://www.youtube.com/watch?v=Piy37om0y6A) | AWS Events | 2026-07 | 8 | 5 |
| [NYC Executive Forum 2026 - A Leader’s Guide to Agentic AI](https://www.youtube.com/watch?v=vvyOHc7jsmg) | AWS Events | 2026-07 | 6 | 4 |
| [Reckitt - Half Year 2025 Results](https://www.youtube.com/watch?v=KP7oflfrcMI) | Reckitt | 2025-07 | 6 | 4 |
| [Making AI Transformation Work: Avoiding the Mistakes from ](https://www.youtube.com/watch?v=CoPCP3f1DzM) | INSEAD | 2026-07 | 5 | 7 |
| [Global Keynote: The Beginning of Better | SAP Sapphire Mad](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 5 | 5 |
| [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 티타임즈TV | 2026-07 | 5 | 5 |
| [Databricks on Databricks: How Marketers Use Data 3x More w](https://www.youtube.com/watch?v=zWHzl5tEW8A) | Databricks | 2026-06 | 5 | 4 |
| [Secure your RAG pipelines with fine grained authorization ](https://www.youtube.com/watch?v=S6xJ0Kkd7ss) | Pinecone | 2025-09 | 5 | 4 |
| [Core Computing](https://www.youtube.com/watch?v=8WyV487QG9Q) | Volvo Cars | 2021-07 | 5 | 4 |
| [Graph Technology Meets GenAI: A Neo4j Perspective | Intel](https://www.youtube.com/watch?v=7pdMtkezuVI) | Intel | 2025-08 | 4 | 6 |
| [BUILD 2025 Opening Keynote: Building the Agentic AI Future](https://www.youtube.com/watch?v=MPLMS0736zI) | Snowflake | 2025-11 | 4 | 6 |

### B5 · 조직문화 변화 (사례 39건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Why AI adoption fails (and how to fix it)](https://www.youtube.com/watch?v=mlXbfJf80k8) | Microsoft | 2026-07 | 8 | 4 |
| [Fostering a more inclusive workplace – from reactive to pr](https://www.youtube.com/watch?v=BVlPVaG34wI) | Nissan | 2023-09 | 8 | 4 |
| [Enterprise AI Strategy and CEO Leadership, with McKinsey &](https://www.youtube.com/watch?v=uTRKdCY4HdE) | CXOTalk | 2026-08 | 6 | 7 |
| [Is Agentic AI upending the corporate ladder? EY's Global C](https://www.youtube.com/watch?v=ilaDQLa1Lrk) | Microsoft | 2025-12 | 6 | 4 |
| [Claude for Financial Services Keynote](https://www.youtube.com/watch?v=50AhIyybR0M) | Anthropic | 2025-07 | 5 | 5 |
| [The future of work has no org chart | Microsoft Katy Georg](https://www.youtube.com/watch?v=r4qZz66GlNQ) | Microsoft | 2026-07 | 5 | 4 |
| [현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)](https://www.youtube.com/watch?v=b-tgY8Q0SbA) | 티타임즈TV | 2026-07 | 4 | 6 |
| [Agentic AI and the Future of Software Development: S3 E4](https://www.youtube.com/watch?v=eQ6tb7j3Z2U) | AMD | 2026-07 | 4 | 5 |
| [Integrating Generative AI Into Business Strategy: Dr. Geor](https://www.youtube.com/watch?v=9RvWcXVaAng) | MIT Corporate Relation | 2026-07 | 3 | 8 |
| [In the era of AI transformation (AX), we'll teach you ever](https://www.youtube.com/watch?v=ErviFf8I6K4) | 메타코드M | 2026-07 | 3 | 8 |
| [Intel’s Whole Vehicle Advantage to SDV | Intel](https://www.youtube.com/watch?v=qmIFB8MC7bM) | Intel | 2025-01 | 3 | 6 |
| [SXSW 2024 | Waymo’s Roadmap for a Multi-City AV Service](https://www.youtube.com/watch?v=Qot1uX2g9jk) | Waymo | 2024-03 | 3 | 6 |
| [LLMOps in action: Streamlining the path from prototype to ](https://www.youtube.com/watch?v=E1DTsgbZPhw) | Weights & Biases | 2025-01 | 3 | 6 |
| [Build core skills to thrive as an AI-era developer](https://www.youtube.com/watch?v=q_Jq4IgYImk) | Google Developers | 2026-05 | 3 | 5 |
| [Nissan Motor Co., Ltd. 123rd Ordinary General Meeting of S](https://www.youtube.com/watch?v=bxMwW7KnuqE) | Nissan | 2022-06 | 3 | 4 |

### B5 · 리더십·CDO/CAIO (사례 152건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Enterprise AI Strategy and CEO Leadership, with McKinsey &](https://www.youtube.com/watch?v=uTRKdCY4HdE) | CXOTalk | 2026-08 | 36 | 7 |
| [The Complete AI Transformation Blueprint - Live Workshop](https://www.youtube.com/watch?v=OcTMwjqje5Q) | Cole Medin | 2026-07 | 14 | 6 |
| [AI Transformation AMA for HR Leaders](https://www.youtube.com/watch?v=lYOR4pgVdb0) | Zapier | 2025-09 | 14 | 5 |
| [Advancing AI 2026 Replay | Build What's Next with @AMD](https://www.youtube.com/watch?v=8B_Gese-bdI) | AMD | 2026-07 | 13 | 6 |
| [Leading through AI: How top executives are turning AI mand](https://www.youtube.com/watch?v=g6q02hUd_Wc) | Zapier | 2026-03 | 13 | 5 |
| [Investor Event 2024 | Unilever](https://www.youtube.com/watch?v=yuMA_iYdq4w) | Unilever | 2024-11 | 12 | 6 |
| [AMD at CES® 2026 Replay](https://www.youtube.com/watch?v=ypSay3Ehxow) | AMD | 2026-01 | 11 | 6 |
| [Zapier's Big AI Plans for 2026 Revealed! - Leadership, Cul](https://www.youtube.com/watch?v=EfHm1Qjztd0) | Zapier | 2025-11 | 11 | 5 |
| [AI, autonomy, and the future of naval warfare with Captain](https://www.youtube.com/watch?v=guxzPymyz-w) | Weights & Biases | 2025-03 | 10 | 6 |
| [Panos Panay: On Humility and Empathy in Leadership](https://www.youtube.com/watch?v=YF7dcSd_3L0) | Arm | 2026-01 | 10 | 4 |
| [AI Changes Everything: What Leaders Must Get Right About A](https://www.youtube.com/watch?v=AF8rr7rCl38) | Oracle | 2026-06 | 10 | 4 |
| [Self-Driven Women: Opportunities and challenges for women ](https://www.youtube.com/watch?v=-x1c0URjbOE) | Waymo | 2020-08 | 10 | 4 |
| [Leading AI Transformation: A Chief AI Officer's Perspectiv](https://www.youtube.com/watch?v=LblTPS1LnLc) | Amazon Web Services | 2026-07 | 9 | 6 |
| [World Economic Forum: A Preview of Davos 2026](https://www.youtube.com/watch?v=2MWzmChPBTc) | McKinsey & Company | 2026-01 | 9 | 4 |
| [Fostering a more inclusive workplace – from reactive to pr](https://www.youtube.com/watch?v=BVlPVaG34wI) | Nissan | 2023-09 | 9 | 4 |

### B5 · 직무·역량 변화 (사례 195건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [What Netflix Knows About AI That Every Recruiter Should Le](https://www.youtube.com/watch?v=edY-3X18CHc) | Zapier | 2025-10 | 104 | 5 |
| [Top Job Application Skills to Help Get You Hired](https://www.youtube.com/watch?v=N8xrgemiO3E) | LinkedIn | 2024-05 | 43 | 4 |
| [Data Engineering from Ingestion to AI-Ready | BUILD 2025 K](https://www.youtube.com/watch?v=XwCnOsZMhyI) | Snowflake | 2025-11 | 38 | 4 |
| [Data + AI Summit Keynote 2026 | Day 1](https://www.youtube.com/watch?v=Qux8E-L1mk8) | Databricks | 2026-06 | 22 | 7 |
| [Lovable's Ryan Meadows on the New GTM Playbook](https://www.youtube.com/watch?v=FeZ93evIfbM) | Zapier | 2026-06 | 20 | 7 |
| [Ask Us Anything: Blair Ciesil and Marie Padberg get into y](https://www.youtube.com/watch?v=oJcziqz673U) | McKinsey & Company | 2025-10 | 19 | 4 |
| [AI Transformation AMA for HR Leaders](https://www.youtube.com/watch?v=lYOR4pgVdb0) | Zapier | 2025-09 | 18 | 5 |
| [The Skills Mismatch Economy | How AI is reshaping skill de](https://www.youtube.com/watch?v=HmuEoDwZnqg) | Accenture | 2026-04 | 16 | 5 |
| [Unlocking agentic data engineering with Lakeflow + Genie](https://www.youtube.com/watch?v=0WDGu-IPmZM) | Databricks | 2026-06 | 16 | 4 |
| [Prepare for Your NVIDIA Certification Exam](https://www.youtube.com/watch?v=Kd3nbaMZy8k) | NVIDIA Developer | 2025-02 | 16 | 4 |
| [What's new with data agents](https://www.youtube.com/watch?v=Z-AfOcWO_kk) | Google Cloud Tech | 2026-06 | 15 | 4 |
| [KT 에이블스쿨 10기 모집설명회](https://www.youtube.com/watch?v=0WphLSKUbDw) | KT | 2026-07 | 15 | 4 |
| [Cross-industry Collab: Driving Progress When Times Are Tou](https://www.youtube.com/watch?v=gjMutZzFLnA) | Snap | 2023-11 | 15 | 4 |
| [How Executive Assistants Drive Strategic Impact with AI](https://www.youtube.com/watch?v=-gGwrSPc3tA) | Zapier | 2025-11 | 14 | 4 |
| [Building agentic AI workflows with W&B Weave: a hiring ass](https://www.youtube.com/watch?v=tRGoT1QV8VA) | Weights & Biases | 2025-07 | 12 | 4 |

### B6 · 장벽: 관성·저항 (사례 86건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [[ifkakao2021] Daum Mail Terraforming:  다음 메일 백엔ᄃ](https://www.youtube.com/watch?v=r2t4h3qMXzw) | kakao tech | 2026-06 | 19 | 4 |
| [AWS Summit Washington DC 2026 - Keynote | Amazon Web Servi](https://www.youtube.com/watch?v=QGaPF8NsOE4) | AWS Events | 2026-06 | 11 | 6 |
| [Leading AI Transformation: A Chief AI Officer's Perspectiv](https://www.youtube.com/watch?v=LblTPS1LnLc) | Amazon Web Services | 2026-07 | 7 | 6 |
| [Federated Learning: A New Era of Collaboration for Pharma ](https://www.youtube.com/watch?v=_lhB9Zo915c) | Intel | 2024-12 | 7 | 6 |
| [The Secret to Successful AI Transition: A Step-by-Step AX ](https://www.youtube.com/watch?v=wdqRyiqH_OI) | 메타코드M | 2026-07 | 7 | 4 |
| [Microsoft Digital Sovereignty Summit | Sovereign Cloud, AI](https://www.youtube.com/watch?v=YLL7UuVCerM) | Microsoft Azure | 2026-04 | 6 | 8 |
| [Is there an ROI in industrial AI? The truth behind data, a](https://www.youtube.com/watch?v=2cJD3hlyu6g) | Schneider Electric | 2026-07 | 6 | 5 |
| [AWS Summit Bengaluru 2026: Innovators Edition Keynote | AW](https://www.youtube.com/watch?v=CprBATdRoh0) | AWS Events | 2026-06 | 5 | 6 |
| [Building AI Tools to Transform Sales and Marketing, an Ins](https://www.youtube.com/watch?v=J7wGwY0lX_E) | Intel | 2024-12 | 5 | 5 |
| [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 티타임즈TV | 2026-07 | 5 | 5 |
| [Beyond the hype: Orchestrating end-to-end developer workfl](https://www.youtube.com/watch?v=t6jH_GPFqgs) | Google Cloud Tech | 2026-06 | 4 | 6 |
| [Telco Tech Talks: How do we develop our people to meet the](https://www.youtube.com/watch?v=fythNeXmXnM) | Telenor | 2023-04 | 4 | 6 |
| [AWS Summit Mumbai 2026 Keynote | AWS Events](https://www.youtube.com/watch?v=0x_Q0wNux_U) | AWS Events | 2026-06 | 4 | 5 |
| [Why AI adoption fails – and how to get it right](https://www.youtube.com/watch?v=JBb2jRns3PA) | The CEO Magazine | 2026-07 | 4 | 5 |
| [[ifkakao2021] Knowledge Graph for Enterprise](https://www.youtube.com/watch?v=fMV_TRN5StI) | kakao tech | 2026-06 | 4 | 4 |

### B7 · 성과: 운영효율 (사례 320건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Unilever | H1 2025 | Results | Webcast & Q&A – audio-descr](https://www.youtube.com/watch?v=oMDBIXBEv3Q) | Unilever | 2025-10 | 39 | 5 |
| [Reckitt - Half Year 2025 Results](https://www.youtube.com/watch?v=KP7oflfrcMI) | Reckitt | 2025-07 | 38 | 4 |
| [Unilever | Full Year 2023 Results | Webcast & Q&A](https://www.youtube.com/watch?v=YUdGwlJiDUk) | Unilever | 2024-02 | 37 | 5 |
| [Q4 and full-year 2025 results webcast and Q&A audio descri](https://www.youtube.com/watch?v=m7GUG2IHJZY) | Unilever | 2026-03 | 36 | 4 |
| [Q4 and full-year 2025 results webcast and Q&A | Unilever](https://www.youtube.com/watch?v=G86AGZQwVVo) | Unilever | 2026-02 | 36 | 4 |
| [Unilever | H1 2025 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=_FqeVQgaPKM) | Unilever | 2025-07 | 35 | 4 |
| [Innovating & Measuring ROI for Enterprise Organizations Th](https://www.youtube.com/watch?v=U84H7KOAlyU) | Insight Solutions | 2026-08 | 27 | 4 |
| [Analythics Architecture:  Promising AI Use Cases for the E](https://www.youtube.com/watch?v=JhbsIutTwXM) | DATAVERSITY | 2026-08 | 24 | 7 |
| [Closing the Enterprise AI ROI Gap](https://www.youtube.com/watch?v=20lqu-d4cxc) | AI:ROI Conversations w | 2026-08 | 23 | 7 |
| [Unilever | H1 2024 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=Yc8FoPwlXxQ) | Unilever | 2024-07 | 22 | 4 |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=X59yNoX8xQs) | Unilever | 2025-11 | 22 | 4 |
| [Unilever | Q1 2026 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=IlduIhb63aU) | Unilever | 2026-04 | 21 | 5 |
| [The Boardroom Mandate: Scaling AI for Business Impact | Da](https://www.youtube.com/watch?v=0ixUiXr2DVY) | Infosys | 2026-02 | 20 | 7 |
| [Reduce Azure networking service costs: smart routing, loca](https://www.youtube.com/watch?v=KiF_Cn5PdfU) | Microsoft Azure | 2026-03 | 20 | 4 |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=xWdZMbXzL-M) | Unilever | 2025-10 | 20 | 4 |

### B7 · 성과: 조직성과 (사례 147건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [Unilever | H1 2025 | Results | Webcast & Q&A – audio-descr](https://www.youtube.com/watch?v=oMDBIXBEv3Q) | Unilever | 2025-10 | 92 | 5 |
| [Q4 and full-year 2025 results webcast and Q&A audio descri](https://www.youtube.com/watch?v=m7GUG2IHJZY) | Unilever | 2026-03 | 83 | 4 |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=X59yNoX8xQs) | Unilever | 2025-11 | 82 | 4 |
| [Q4 and full-year 2025 results webcast and Q&A | Unilever](https://www.youtube.com/watch?v=G86AGZQwVVo) | Unilever | 2026-02 | 37 | 4 |
| [Unilever | H1 2025 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=_FqeVQgaPKM) | Unilever | 2025-07 | 30 | 4 |
| [Measure and iterate on AI application performance using W&](https://www.youtube.com/watch?v=pxbNLZ9k9Bo) | Weights & Biases | 2025-04 | 28 | 4 |
| [Unilever | Q1 2026 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=IlduIhb63aU) | Unilever | 2026-04 | 27 | 5 |
| [Building agentic AI workflows with W&B Weave: a hiring ass](https://www.youtube.com/watch?v=tRGoT1QV8VA) | Weights & Biases | 2025-07 | 27 | 4 |
| [LLMOps in action: Streamlining the path from prototype to ](https://www.youtube.com/watch?v=E1DTsgbZPhw) | Weights & Biases | 2025-01 | 25 | 6 |
| [Unilever | Full Year 2023 Results | Webcast & Q&A](https://www.youtube.com/watch?v=YUdGwlJiDUk) | Unilever | 2024-02 | 25 | 5 |
| [Fully Connected Tokyo: [Hands-on workshop] From 0 to autom](https://www.youtube.com/watch?v=BX-AjQUUol8) | Weights & Biases | 2026-01 | 22 | 4 |
| [Unilever Foods to combine with McCormick | Webcast & Q&A](https://www.youtube.com/watch?v=MokfRDL0kqA) | Unilever | 2026-04 | 20 | 5 |
| [RAG Benchmarks with Nandan Thakur - Weaviate Podcast #124!](https://www.youtube.com/watch?v=x9zZ03XtAuY) | Weaviate | 2025-06 | 19 | 4 |
| [Unilever Investor Event 2024 - Key takeaways](https://www.youtube.com/watch?v=NdZLX0ZfZi0) | Unilever | 2024-12 | 17 | 4 |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast &](https://www.youtube.com/watch?v=xWdZMbXzL-M) | Unilever | 2025-10 | 17 | 4 |

### B7 · 성과: 사회적 편익 (사례 27건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [AI for Accessibility: How Sorenson Is Advancing Inclusive ](https://www.youtube.com/watch?v=vx1g4xu5qMk) | Intel | 2025-08 | 23 | 4 |
| [Open-Source AI 101: Enabling American Innovation | NVIDIA ](https://www.youtube.com/watch?v=VqIc2LJzZG0) | NVIDIA Developer | 2025-12 | 12 | 4 |
| [AI’s breakthrough in weather forecasting with Brightband’s](https://www.youtube.com/watch?v=xFgaEPMqfi4) | Weights & Biases | 2024-11 | 9 | 5 |
| [MGI event: Industry leaders discuss how to advance adaptat](https://www.youtube.com/watch?v=MtevcjCnO1w) | McKinsey & Company | 2026-03 | 9 | 4 |
| [NVIDIA & Coherent: Reindustrializing America, Manufacturin](https://www.youtube.com/watch?v=GsqW5MPFajw) | NVIDIA | 2026-06 | 7 | 4 |
| [Developer Preview: Introducing Meta Wearables Device Acces](https://www.youtube.com/watch?v=U0Ha6AmXBS0) | Meta Developers | 2025-10 | 6 | 4 |
| [Accelerating toward a circular economy – from idea to acti](https://www.youtube.com/watch?v=lX2NDGB6AB4) | Nissan | 2023-09 | 4 | 5 |
| [End Data Disparity: Using Geospatial Data To Improve Citie](https://www.youtube.com/watch?v=YFTTMP6meVQ) | Snowflake | 2026-01 | 4 | 5 |
| [AI Transformation Leader (AB-731) - Full Course - Pass The](https://www.youtube.com/watch?v=Ox0m3iJG57M) | Citizen Developer and  | 2026-07 | 3 | 7 |
| [Think You Know AI? 25 Startups Prove You Wrong](https://www.youtube.com/watch?v=D1x8ewtJAa0) | NVIDIA | 2026-04 | 3 | 5 |
| [La confiance, un facteur clé du déploiement de l'IA en san](https://www.youtube.com/watch?v=jjJkYvT4MjI) | Orange | 2026-06 | 3 | 5 |
| [Aaron Levie on AI Adoption and Enterprise Workflows | The ](https://www.youtube.com/watch?v=dvVbA9OcBqs) | a16z and MTS | 2026-07 | 3 | 5 |
| [10 Years of Zoox. Reflections and Predictions.](https://www.youtube.com/watch?v=DYcujjMs3Uo) | Zoox | 2024-07 | 3 | 4 |
| [Welcome to Agentic Business | ServiceNow Knowledge 2026 Op](https://www.youtube.com/watch?v=jeo2V1w-Peg) | ServiceNow | 2026-05 | 2 | 7 |
| [Building AI Factories: How Siemens and AWS Are Solving Dat](https://www.youtube.com/watch?v=ZLl184cSyYM) | Siemens | 2026-01 | 2 | 7 |

### B8 · 부정 성과: 보안·프라이버시 (사례 303건)

| 제목 | 채널 | 월 | 적중 | 블록수 |
|---|---|---|---:|---:|
| [[Brown-Bag 런치세미나] 2024년 보안트렌드 살펴보기](https://www.youtube.com/watch?v=6OUSU8wzvac) | NAVER Cloud | 2024-04 | 42 | 4 |
| [KLUE Seminar](https://www.youtube.com/watch?v=3SUBLhZtJGk) | Upstage | 2021-08 | 34 | 4 |
| [Building agentic AI workflows with W&B Weave: a hiring ass](https://www.youtube.com/watch?v=tRGoT1QV8VA) | Weights & Biases | 2025-07 | 33 | 4 |
| [Overcoming Zero-Sum Thinking on Privacy, Civil Liberties, ](https://www.youtube.com/watch?v=x-NEdIcgboo) | Palantir | 2025-08 | 29 | 4 |
| [2026 Cost of a Data Breach Report: AI Is Changing Cybersec](https://www.youtube.com/watch?v=b2PESRl7De4) | IBM Technology | 2026-07 | 28 | 4 |
| [Cohere Labs Connect Conference - Day 2](https://www.youtube.com/watch?v=Q-upWvYEx-E) | Cohere | 2025-11 | 27 | 4 |
| [Optimizing CI/CD model management and evaluation workflows](https://www.youtube.com/watch?v=Sw4M-b_GQZg) | Weights & Biases | 2024-10 | 26 | 5 |
| [The Cost of a Data Breach 2026, and what we can learn from](https://www.youtube.com/watch?v=lx41qvj80Jo) | IBM Technology | 2026-07 | 25 | 4 |
| [The Executive Blueprint for Responsible AI Governance: Pra](https://www.youtube.com/watch?v=-Y22OVH2w1o) | Zapier | 2026-04 | 24 | 6 |
| [Mastering model customization: fine-tuning Azure OpenAI se](https://www.youtube.com/watch?v=N1CI8Ld0-PA) | Weights & Biases | 2025-03 | 24 | 4 |
| [AI PCs and the Future of Cybersecurity: AI-Powered Protect](https://www.youtube.com/watch?v=GzFE6k-S3vA) | Intel | 2025-09 | 22 | 5 |
| [Weights & Biases and CoreWeave: Fully Connected 2025 Keyno](https://www.youtube.com/watch?v=09Ubfrdq508) | Weights & Biases | 2025-06 | 22 | 4 |
| [Unlocking the potential of MLOps and LLMOps](https://www.youtube.com/watch?v=7hxec4M48XY) | Weights & Biases | 2025-01 | 21 | 5 |
| [What do people use AI models for?](https://www.youtube.com/watch?v=VSmobknYl0E) | Anthropic | 2024-12 | 21 | 4 |
| [Deep research is just really smart rag w/ Robert Caulk](https://www.youtube.com/watch?v=wAcWJtWQVN8) | Qdrant | 2025-03 | 21 | 4 |

---

## 6. AX 연계 교량축 사례


### X1 · 정의 확장(DX→AX 계승) (사례 50건 · 상위 30)

| 제목 | 채널 | 월 | 적중 | 블록수 | 관련성 |
|---|---|---|---:|---:|---|
| [Global Keynote: The Beginning of Better | SAP Sapphire M](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 20 | 5 | ax_core |
| [현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)](https://www.youtube.com/watch?v=b-tgY8Q0SbA) | 티타임즈TV | 2026-07 | 14 | 6 | ax_core |
| [Global Keynote: The Beginning of Better | SAP Sapphire O](https://www.youtube.com/watch?v=9aa-etRsaLU) | SAP | 2026-05 | 13 | 6 | ax_core |
| [제조업 AX의 골든 타임 ⏰ 중요한 것은 AI 도입보다 이것?! 📢 IT슈다 EP. 제조](https://www.youtube.com/watch?v=iAbE9YXnbqA) | 삼성SDS and KASMO 인공지능혁신 | 2026-07 | 11 | 5 | ax_core |
| [Integrating Generative AI Into Business Strategy: Dr. Ge](https://www.youtube.com/watch?v=9RvWcXVaAng) | MIT Corporate Relation | 2026-07 | 9 | 8 | ax_core |
| [In the era of AI transformation (AX), we'll teach you ev](https://www.youtube.com/watch?v=ErviFf8I6K4) | 메타코드M | 2026-07 | 9 | 8 | ax_core |
| [Customer Success Keynote: Connected to Win: From Moment ](https://www.youtube.com/watch?v=dG9aBkJCcso) | SAP | 2026-05 | 7 | 6 | ax_core |
| [AI isn’t digital transformation, and leaders need to und](https://www.youtube.com/watch?v=eZ1NizUx9U4) | IBM | 2026-07 | 7 | 5 | ax_core |
| [KT 에이블스쿨 10기 모집설명회](https://www.youtube.com/watch?v=0WphLSKUbDw) | KT | 2026-07 | 7 | 4 | ax_core |
| [Making AI Transformation Work: Avoiding the Mistakes fro](https://www.youtube.com/watch?v=CoPCP3f1DzM) | INSEAD | 2026-07 | 6 | 7 | ax_core |
| [AI for AI: Building the Transformation Office That Drive](https://www.youtube.com/watch?v=OJwpw-8SkBM) | Tigerhall | 2026-07 | 6 | 7 | ax_core |
| [Top Banking Trends 2026 - Unconstrained Banking | Accent](https://www.youtube.com/watch?v=MWvdwSD3ZRc) | Accenture | 2026-02 | 6 | 6 | ax_core |
| [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y) | Infosys | 2026-07 | 6 | 5 | ax_core |
| [The race to rewire operations: How the story unfolded in](https://www.youtube.com/watch?v=rSJY396HQ1c) | McKinsey & Company | 2026-02 | 6 | 5 | ax_core |
| [The AI adoption playbook: Lessons from Microsoft's inter](https://www.youtube.com/watch?v=c51ToE4pPpY) | DX | 2026-08 | 5 | 5 | ax_core |
| [How NEC Is Becoming an AI-Native Enterprise with SAP, RI](https://www.youtube.com/watch?v=6utLfKSBIHg) | SAP | 2026-04 | 5 | 5 | ax_core |
| [Chad & Chris | Tariff Savings and Compliance through Pal](https://www.youtube.com/watch?v=xBTPNLd8Jv8) | Palantir | 2025-09 | 5 | 4 | ax_core |
| [Rewired To Win: Reimagining the Enterprise With Tech and](https://www.youtube.com/watch?v=HoHFZ-Fzu_g) | McKinsey & Company | 2026-04 | 4 | 6 | ax_core |
| [26 Years of Survival Keyword AX (Great AI Transformation](https://www.youtube.com/watch?v=VRYJJJBqsDE) | 메타코드M | 2026-07 | 4 | 6 | ax_core |
| [The Industrial AI Revolution: Siemens Keynote at CES 202](https://www.youtube.com/watch?v=R4Wm6YdoZSs) | Siemens | 2026-01 | 4 | 5 | ax_core |
| [CCW 2026: How Citizens Bank is building the AI-native cu](https://www.youtube.com/watch?v=O_Imo9L04mo) | AWS Events | 2026-07 | 4 | 4 | ax_core |
| [[Brown-Bag 런치세미나] 2024년 보안트렌드 살펴보기](https://www.youtube.com/watch?v=6OUSU8wzvac) | NAVER Cloud | 2024-04 | 4 | 4 | ax_core |
| [The Secret to Successful AI Transition: A Step-by-Step A](https://www.youtube.com/watch?v=wdqRyiqH_OI) | 메타코드M | 2026-07 | 4 | 4 | ax_core |
| [AI-Native 기업으로 전환 전략과 사례](https://www.youtube.com/watch?v=Y-ApGj-9ceI) | 삼성SDS AX | 2026-07 | 4 | 4 | ax_core |
| [Enterprise AI: From Big Uncertainty to Massive ROI](https://www.youtube.com/watch?v=FmcULDfEgvM) | ERP Suites | JD Edward | 2026-08 | 3 | 7 | ax_core |
| [With 180 Years of Reinvention, Pearson Takes on the AI E](https://www.youtube.com/watch?v=YBe0oiv01N0) | Boston Consulting Grou | 2026-07 | 3 | 6 | ax_core |
| [Steal Zapier's AI Playbook for Accounting: How 8 People ](https://www.youtube.com/watch?v=CxrrXKFn6cg) | Zapier | 2026-05 | 3 | 6 | ax_core |
| [LG AI Talk Concert 2025 - Shaping the Future of AI](https://www.youtube.com/watch?v=EGzIMo4AizA) | LG AI Research | 2025-07 | 3 | 5 | ax_core |
| [Is there an ROI in industrial AI? The truth behind data,](https://www.youtube.com/watch?v=2cJD3hlyu6g) | Schneider Electric | 2026-07 | 3 | 5 | ax_core |
| [Enterprise AI Adoption in 2025: What Actually Works](https://www.youtube.com/watch?v=9MkMQ6zkjLw) | The Tech Trek | 2026-07 | 3 | 5 | ax_core |

### X2 · Avenue 2 윤리·거버넌스 (사례 264건 · 상위 30)

| 제목 | 채널 | 월 | 적중 | 블록수 | 관련성 |
|---|---|---|---:|---:|---|
| [The Executive Blueprint for Responsible AI Governance: P](https://www.youtube.com/watch?v=-Y22OVH2w1o) | Zapier | 2026-04 | 69 | 6 | ax_core |
| [Prepare for Microsoft Certification Exam AB-731: AI Tran](https://www.youtube.com/watch?v=mj_lyhuWbig) | Microsoft Learn | 2026-07 | 58 | 7 | ax_core |
| [Enterprise strategies for agentic AI adoption in 2026 an](https://www.youtube.com/watch?v=B4WgQotMVmE) | Vertesia | 2026-07 | 45 | 7 | ax_core |
| [Microsoft Digital Sovereignty Summit | Sovereign Cloud, ](https://www.youtube.com/watch?v=YLL7UuVCerM) | Microsoft Azure | 2026-04 | 38 | 8 | ax_core |
| [Global Keynote: The Beginning of Better | SAP Sapphire M](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 38 | 5 | ax_core |
| [Overcoming Zero-Sum Thinking on Privacy, Civil Liberties](https://www.youtube.com/watch?v=x-NEdIcgboo) | Palantir | 2025-08 | 37 | 4 | ax_core |
| [AI Transformation Leader (AB-731) - Full Course - Pass T](https://www.youtube.com/watch?v=Ox0m3iJG57M) | Citizen Developer and  | 2026-07 | 32 | 7 | ax_core |
| [AI and Trust at Scale: S3 E3](https://www.youtube.com/watch?v=WOXtvwYq-7o) | AMD | 2026-06 | 31 | 4 | ax_core |
| [Snowflake Summit 2026 Platform Keynote](https://www.youtube.com/watch?v=CtqKJV6gyGQ) | Snowflake | 2026-06 | 27 | 7 | ax_core |
| [AWS European Sovereign Cloud – Explained | AWS Events](https://www.youtube.com/watch?v=GbitrLroyMU) | AWS Events | 2026-06 | 27 | 6 | ax_core |
| [Chad & Chris | Tariff Savings and Compliance through Pal](https://www.youtube.com/watch?v=xBTPNLd8Jv8) | Palantir | 2025-09 | 23 | 4 | ax_core |
| [Global Keynote: The Beginning of Better | SAP Sapphire O](https://www.youtube.com/watch?v=9aa-etRsaLU) | SAP | 2026-05 | 22 | 6 | ax_core |
| [26 Years of Survival Keyword AX (Great AI Transformation](https://www.youtube.com/watch?v=VRYJJJBqsDE) | 메타코드M | 2026-07 | 21 | 6 | ax_core |
| [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 티타임즈TV | 2026-07 | 21 | 5 | ax_core |
| [Nathan Calvin - Three People vs  Big AI  Policy, Power, ](https://www.youtube.com/watch?v=RV00BTMY5XA) | Cohere | 2026-02 | 21 | 4 | ax_core |
| [In the era of AI transformation (AX), we'll teach you ev](https://www.youtube.com/watch?v=ErviFf8I6K4) | 메타코드M | 2026-07 | 20 | 8 | ax_core |
| [Agentic AI Adoption Secrets You Need to Know Now](https://www.youtube.com/watch?v=-0V6XUskt-k) | Kore.ai | 2026-07 | 20 | 6 | ax_core |
| [How AI Transforms Retail, Finance and Manufacturing in 2](https://www.youtube.com/watch?v=11degQs3L7c) | Snowflake | 2025-12 | 19 | 7 | ax_core |
| [Building enterprise-grade AI agents: How enterprises sca](https://www.youtube.com/watch?v=3vf9eL-LKUY) | Google Cloud Tech | 2026-06 | 19 | 6 | ax_core |
| [Building agentic AI workflows with W&B Weave: a hiring a](https://www.youtube.com/watch?v=tRGoT1QV8VA) | Weights & Biases | 2025-07 | 19 | 4 | ax_core |
| [Snowflake Build London Keynote](https://www.youtube.com/watch?v=9LOP86qaw34) | Snowflake | 2026-02 | 18 | 7 | ax_core |
| [Snowflake Summit 2026 Builder Keynote](https://www.youtube.com/watch?v=WFR07HIvCrQ) | Snowflake | 2026-07 | 18 | 6 | ax_core |
| [Production Ready RAG in Healthcare with Pinecone and Aut](https://www.youtube.com/watch?v=93f7ZHPkpTk) | Pinecone | 2024-05 | 17 | 4 | ax_core |
| [Safeguard your users and brand with W&B Weave Guardrails](https://www.youtube.com/watch?v=KOwajQfIWC4) | Weights & Biases | 2025-04 | 17 | 4 | ax_core |
| [What's new in Google Cloud's agent platform](https://www.youtube.com/watch?v=FxnjRYo3fpU) | Google Cloud Tech | 2026-06 | 16 | 5 | ax_core |
| [AI Industrialization: The Next Frontier for Global Enter](https://www.youtube.com/watch?v=fSadUMtpwcY) | Intel | 2025-11 | 16 | 5 | ax_core |
| [Accelerating toward a circular economy – from idea to ac](https://www.youtube.com/watch?v=lX2NDGB6AB4) | Nissan | 2023-09 | 16 | 5 | ax_core |
| [Welcome to Agentic Business | ServiceNow Knowledge 2026 ](https://www.youtube.com/watch?v=jeo2V1w-Peg) | ServiceNow | 2026-05 | 15 | 7 | ax_core |
| [Sunlight on Shadow AI: When Security Learns to Tinker—Ro](https://www.youtube.com/watch?v=qlCkwGSRP3w) | Zapier | 2025-12 | 15 | 7 | ax_core |
| [Siemens, Capgemini, EDP and Kraken on how AI will transf](https://www.youtube.com/watch?v=tolLHQWJzKY) | Siemens | 2026-01 | 15 | 6 | ax_core |

### X3 · Avenue 1 동적역량 (사례 252건 · 상위 30)

| 제목 | 채널 | 월 | 적중 | 블록수 | 관련성 |
|---|---|---|---:|---:|---|
| [Self-Driven Women: Engineering the future of autonomy](https://www.youtube.com/watch?v=cvqGkq2SGWQ) | Waymo | 2021-11 | 20 | 4 | ax_core |
| [The Blueprint for Agentic Business | ServiceNow Knowledg](https://www.youtube.com/watch?v=q8kaVEkTWho) | ServiceNow | 2026-05 | 16 | 8 | ax_core |
| [LLMOps in action: Streamlining the path from prototype t](https://www.youtube.com/watch?v=E1DTsgbZPhw) | Weights & Biases | 2025-01 | 16 | 6 | ax_core |
| [Alibaba Cloud Claw Talks EP4 | Secure AI Agents Across F](https://www.youtube.com/watch?v=mm9Fl1LcBXI) | Alibaba Cloud | 2026-05 | 14 | 4 | ax_core |
| [The Startup Powering The Data Behind AGI](https://www.youtube.com/watch?v=X39OZndIWSY) | Weights & Biases | 2025-09 | 13 | 6 | ax_adjacent |
| [DSPy End-to-End: Meetup in San Francisco](https://www.youtube.com/watch?v=Y81DoFmt-2U) | Weaviate | 2024-05 | 13 | 5 | ax_core |
| [Jiafei Duan  - Building Robotics Foundation Model with R](https://www.youtube.com/watch?v=ZB5IAlFvt1c) | Cohere | 2026-04 | 13 | 4 | ax_core |
| [Ahsaas Bajaj  - Production Grade ML in Practice  Evaluat](https://www.youtube.com/watch?v=UkOvqHSskMw) | Cohere | 2026-01 | 12 | 5 | ax_core |
| [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y) | Infosys | 2026-07 | 12 | 5 | ax_core |
| [AI for AI: Building the Transformation Office That Drive](https://www.youtube.com/watch?v=OJwpw-8SkBM) | Tigerhall | 2026-07 | 10 | 7 | ax_core |
| [Aditri Bhagirath  - Persona Guided Personalization](https://www.youtube.com/watch?v=0X01DFnA2dc) | Cohere | 2026-01 | 10 | 5 | ax_adjacent |
| [Navigate the agentic shift in software development with ](https://www.youtube.com/watch?v=Z9Zz75pmOeg) | Google Cloud Tech | 2026-06 | 10 | 5 | ax_core |
| [Telefónica Capital Markets Day 2025 | ES](https://www.youtube.com/watch?v=8HYvqTquKQM) | Telefónica | 2025-11 | 9 | 7 | ax_core |
| [NYC Executive Forum 2026 - The Collective Edge: Cross-fu](https://www.youtube.com/watch?v=3JHA7ayOJuE) | AWS Events | 2026-07 | 9 | 5 | ax_core |
| [Build core skills to thrive as an AI-era developer](https://www.youtube.com/watch?v=q_Jq4IgYImk) | Google Developers | 2026-05 | 9 | 5 | ax_core |
| [Optimizing CI/CD model management and evaluation workflo](https://www.youtube.com/watch?v=Sw4M-b_GQZg) | Weights & Biases | 2024-10 | 9 | 5 | ax_core |
| [From Strategy to Performance: How leaders can build an o](https://www.youtube.com/watch?v=coXorr4pZJs) | McKinsey & Company | 2025-12 | 9 | 4 | ax_core |
| [Is SaaS really dead? Dharmesh Shah from HubSpot on AI, V](https://www.youtube.com/watch?v=R5MKxU5biPo) | Zapier | 2026-02 | 9 | 4 | ax_adjacent |
| [SWE-bench with John Yang and Carlos E. Jimenez - Weaviat](https://www.youtube.com/watch?v=8rwHAR4fsFg) | Weaviate | 2024-10 | 8 | 5 | ax_core |
| [How Zapier Runs AI Hack Week | Real Examples of AI Trans](https://www.youtube.com/watch?v=e1pk34c3oYU) | Zapier | 2025-09 | 8 | 5 | ax_core |
| [How AI Transforms Retail, Finance and Manufacturing in 2](https://www.youtube.com/watch?v=11degQs3L7c) | Snowflake | 2025-12 | 7 | 7 | ax_core |
| [26 Years of Survival Keyword AX (Great AI Transformation](https://www.youtube.com/watch?v=VRYJJJBqsDE) | 메타코드M | 2026-07 | 7 | 6 | ax_core |
| [NYC Executive Forum 2026 - A Leader’s Guide to Data Stra](https://www.youtube.com/watch?v=Piy37om0y6A) | AWS Events | 2026-07 | 7 | 5 | ax_core |
| ["Mastering Relevance in Search" with Doug Turnbull & Tre](https://www.youtube.com/watch?v=oiX7F1qi62Y) | Qdrant | 2025-08 | 7 | 5 | ax_adjacent |
| [Boz To The Future #26: The Future According to Ed Catmul](https://www.youtube.com/watch?v=4s1_DKMYQVo) | Meta | 2026-05 | 7 | 4 | ax_adjacent |
| [The Metaverse and How We'll Build It Together -- Connect](https://www.youtube.com/watch?v=Uvufun6xer8) | Meta | 2021-10 | 7 | 4 | ax_core |
| [Overcoming Zero-Sum Thinking on Privacy, Civil Liberties](https://www.youtube.com/watch?v=x-NEdIcgboo) | Palantir | 2025-08 | 7 | 4 | ax_core |
| [Inside Replit Agent with a lead AI engineer](https://www.youtube.com/watch?v=bJMriY-pqPE) | Replit | 2025-12 | 7 | 4 | ax_core |
| [Webinar: AI transformation that works, lessons from the ](https://www.youtube.com/watch?v=PL3OWn143AI) | BOI (Board of Innovati | 2026-07 | 6 | 7 | ax_core |
| [Welcome to Agentic Business | ServiceNow Knowledge 2026 ](https://www.youtube.com/watch?v=jeo2V1w-Peg) | ServiceNow | 2026-05 | 6 | 7 | ax_core |

### X1-a · DX→AX 계승을 **명시한** 발화 전량 (36건, 티어 무관)

> "디지털 전환 다음은 AI 전환"처럼 두 전환을 한 문장 안에서 잇는 발화. Vial의 정의에서 '수단(means)' 속성에 AI를 대입하는 이론적 지점이라, 블록 수가 적어 사례 기준(4블록)에 못 미쳐도 별도로 전량 남긴다.

| 제목 | 채널 | 월 | 명시 횟수 | 티어 | 블록수 | 관련성 |
|---|---|---|---:|---|---:|---|
| [작은 공장도 바로 적용 가능! 현장에서 검증된 AI 도입, 디지털 전환 공식🤖 (feat.스마트제조혁](https://www.youtube.com/watch?v=mUAndx0F8I0) | 중소벤처기업부 | 2026-07 | 5 | — | 0 | ax_core |
| [LG CNS | Leading the Future of Chemical Industry with AX](https://www.youtube.com/watch?v=tdUBajpHiGY) | LG CNS | 2026-07 | 4 | — | 2 | ax_core |
| [[2024 AI 트렌드 총정리 2] AI 도입시 기업이 반드시 고려해야 할 것 │ AI 시대, 기업들](https://www.youtube.com/watch?v=_FfB0sPuhr8) | 삼성SDS | 2026-07 | 4 | — | 3 | ax_core |
| [AI 전환(AX) 시대, 어떤 직무가 끝까지 살아남을까?ㅣ『AI 전환 절대 공식』저자 김건우](https://www.youtube.com/watch?v=7s8O1R8p0Rk) | AI 전환공식 김건우 | 2026-07 | 3 | — | 1 | ax_core |
| [AI 도입을 위해 AI 도입보다 더 중요한 것은? (김유신 상무)](https://www.youtube.com/watch?v=4n4xMvpuCDY) | 티타임즈TV | 2026-07 | 2 | — | 3 | ax_core |
| [현장에서 AI 트랜스포메이션 이끌면서 배운 것 (황재선 SK 부사장)](https://www.youtube.com/watch?v=b-tgY8Q0SbA) | 티타임즈TV | 2026-07 | 2 | B | 6 | ax_core |
| [지역 산업 AI 전환(AX)의 필연적 전략  | INSIGHT VIEW](https://www.youtube.com/watch?v=y634UN2bnvU) | 정보통신산업진흥원 NIPA | 2026-07 | 2 | — | 1 | ax_core |
| [The Efficiency Trap (DX vs. AX)](https://www.youtube.com/watch?v=XdYZNoBu_no) | CHRONO ETERNUS | 2026-08 | 2 | — | 1 | ax_core |
| [[네이버클라우드 금융 컨퍼런스 2023] 생성형 AI가 만드는 금융투자의 새로운 경험 (미래에셋증권 ](https://www.youtube.com/watch?v=ZrOl-SnRCmY) | NAVER Cloud | 2023-11 | 2 | — | 3 | ax_core |
| [Webinar: Accelerate Robotics and Real-Time AI Inference ](https://www.youtube.com/watch?v=5y7awlP6lvw) | NVIDIA Developer | 2025-11 | 2 | — | 2 | ax_core |
| [Customer Success Keynote: Connected to Win: From Moment ](https://www.youtube.com/watch?v=dG9aBkJCcso) | SAP | 2026-05 | 2 | B | 6 | ax_core |
| [AI for Manufacturing | Full panel hosted by Scale AI | #](https://www.youtube.com/watch?v=KN743U1UrNU) | Scale AI | 2022-11 | 2 | — | 3 | ax_core |
| [In the era of AI transformation (AX), we'll teach you ev](https://www.youtube.com/watch?v=ErviFf8I6K4) | 메타코드M | 2026-07 | 1 | A | 8 | ax_core |
| [[AI 시사상식] ‘AX’ 인공지능 전환 / KBS  2026.06.10.](https://www.youtube.com/watch?v=ZmCHLkystDY) | KBS강원 | 2026-07 | 1 | — | 1 | ax_core |
| [제조업 AX의 골든 타임 ⏰ 중요한 것은 AI 도입보다 이것?! 📢 IT슈다 EP. 제조](https://www.youtube.com/watch?v=iAbE9YXnbqA) | 삼성SDS and KASMO 인공지능혁신 | 2026-07 | 1 | C | 5 | ax_core |
| [The Secret to Successful AI Transition: A Step-by-Step A](https://www.youtube.com/watch?v=wdqRyiqH_OI) | 메타코드M | 2026-07 | 1 | C | 4 | ax_core |
| [AI-Native 기업으로 전환 전략과 사례](https://www.youtube.com/watch?v=Y-ApGj-9ceI) | 삼성SDS AX | 2026-07 | 1 | C | 4 | ax_core |
| [2026 'AI 로 구현하는 지역 AX' 시리즈 - 제3회 KLID-FNF 온라인세미나](https://www.youtube.com/watch?v=i6Br6_ImXaA) | 한국지역정보개발원 | 2026-07 | 1 | — | 3 | ax_core |
| [Integrating Generative AI Into Business Strategy: Dr. Ge](https://www.youtube.com/watch?v=9RvWcXVaAng) | MIT Corporate Relation | 2026-07 | 1 | A | 8 | ax_core |
| [With 180 Years of Reinvention, Pearson Takes on the AI E](https://www.youtube.com/watch?v=YBe0oiv01N0) | Boston Consulting Grou | 2026-07 | 1 | B | 6 | ax_core |
| [HiFS Hello Fintelligent World](https://www.youtube.com/watch?v=8HGlZR5okKU) | Huawei | 2026-06 | 1 | — | 2 | ax_core |
| [HiFS Hello Fintelligent World](https://www.youtube.com/watch?v=sGoHONSo0ng) | Huawei | 2026-06 | 1 | — | 2 | ax_core |
| [Huawei Cloud Powers Ninja Van's Cloud-Native Logistics](https://www.youtube.com/watch?v=yWCRAVdDJO4) | Huawei | 2026-05 | 1 | — | 2 | off_topic |
| [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y) | Infosys | 2026-07 | 1 | C | 5 | ax_core |
| [Rewired To Win: Reimagining the Enterprise With Tech and](https://www.youtube.com/watch?v=HoHFZ-Fzu_g) | McKinsey & Company | 2026-04 | 1 | B | 6 | ax_core |
| [The race to rewire operations: How the story unfolded in](https://www.youtube.com/watch?v=rSJY396HQ1c) | McKinsey & Company | 2026-02 | 1 | C | 5 | ax_core |
| [Meet Aizaz | Optical Fiber Test Engineer | Network Infra](https://www.youtube.com/watch?v=WVdres29twI) | Nokia | 2026-04 | 1 | — | 0 | ax_core |
| [How NEC Is Becoming an AI-Native Enterprise with SAP, RI](https://www.youtube.com/watch?v=6utLfKSBIHg) | SAP | 2026-04 | 1 | C | 5 | ax_core |
| [Scaling AI with Ericsson and Joule | SAP Sapphire Madrid](https://www.youtube.com/watch?v=gdl1rUlaWNw) | SAP | 2026-05 | 1 | — | 3 | ax_core |
| [How SharkNinja Builds Agents that Work with Real-World D](https://www.youtube.com/watch?v=3GQf_K42pAg) | Salesforce | 2026-05 | 1 | — | 1 | ax_core |
| [Scale AI | Virtual launch of the Canada wide STEM youth ](https://www.youtube.com/watch?v=Mrp0fARSA_g) | Scale AI | 2020-11 | 1 | — | 2 | ax_core |
| [Introducing the ServiceNow AI Platform Zurich release](https://www.youtube.com/watch?v=D2CpKOknTSo) | ServiceNow | 2025-09 | 1 | — | 3 | ax_core |
| [Industrial Metaverse and AI: Data Integration and Digita](https://www.youtube.com/watch?v=Ibk9YNzYPYw) | Siemens | 2026-01 | 1 | — | 3 | ax_core |
| [The Industrial AI Revolution: Siemens Keynote at CES 202](https://www.youtube.com/watch?v=R4Wm6YdoZSs) | Siemens | 2026-01 | 1 | C | 5 | ax_core |
| [個人投資家向けオンライン説明会「ソフトバンクの成長戦略」](https://www.youtube.com/watch?v=PfLNjF0aJoU) | SoftBank | 2026-03 | 1 | — | 3 | ax_core |
| [The AI powerhouse of Norway: What companies can gain fro](https://www.youtube.com/watch?v=MEHdEjafCfw) | Telenor | 2022-11 | 1 | — | 0 | ax_core |

---

## 7. 티어 C — 부분 사례 (484건, 전량)

> 블록 4~5개만 충족. 단일 구성요소 분석·보조 표본용.

<details><summary>목록 펼치기</summary>


| 제목 | 채널 | 월 | 블록수 | 블록 | 관련성/톤 |
|---|---|---|---:|---|---|
| [The Production AI Playbook: Deploying Agents at Enterprise S](https://www.youtube.com/watch?v=ObTPqBGsEbA) | AI Engineer | 2026-08 | 5 | B1·B2·B5·B7·B8 | ax_core/anti_washing |
| [오픈AI x 무신사 비공개 행사 후기, 코덱스 기업 도입 사례와 AI 네이티브 워크플로우 인사이트 총정리](https://www.youtube.com/watch?v=jYwDdt_3L8Q) | AI 겸임교수 이종범 | 2026-07 | 4 | B1·B5·B6·B8 | ax_core/anti_washing |
| [AI in Chip Design: S3E1](https://www.youtube.com/watch?v=fj1iRitQL4s) | AMD | 2026-03 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [AI and Trust at Scale: S3 E3](https://www.youtube.com/watch?v=WOXtvwYq-7o) | AMD | 2026-06 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Agentic AI and the Future of Software Development: S3 E4](https://www.youtube.com/watch?v=eQ6tb7j3Z2U) | AMD | 2026-07 | 5 | B1·B4·B5·B7·B8 | ax_core/anti_washing |
| [Building with Open Source at AWS & What's Next for Developer](https://www.youtube.com/watch?v=YduNJIcdRA8) | AWS Developers | 2024-11 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [A leader’s guide to advanced team structures in an agentic w](https://www.youtube.com/watch?v=O7u6myBRsns) | AWS Events | 2026-06 | 5 | B1·B2·B3·B5·B6 | ax_core/anti_washing |
| [AWS Summit Mumbai 2026 Keynote | AWS Events](https://www.youtube.com/watch?v=0x_Q0wNux_U) | AWS Events | 2026-06 | 5 | B1·B2·B4·B6·B7 | ax_core/neutral |
| [A leader's guide to data strategy in the era of agentic AI |](https://www.youtube.com/watch?v=3XyNPfWWxiQ) | AWS Events | 2026-06 | 4 | B1·B2·B4·B5 | ax_core/neutral |
| [CCW 2026: AI Can't Personalize What It Can't See: Turning Sc](https://www.youtube.com/watch?v=53A20B6Ras8) | AWS Events | 2026-07 | 5 | B1·B2·B4·B7·B8 | ax_core/washing |
| [CCW 2026: Be the 5%: What We Learned Shipping AI at Amazon S](https://www.youtube.com/watch?v=Sww2jYuqk7w) | AWS Events | 2026-07 | 5 | B1·B2·B3·B4·B5 | ax_core/anti_washing |
| [NYC Executive Forum 2026 - A Fireside Chat with Swami Sivasu](https://www.youtube.com/watch?v=CHtc71MVpdo) | AWS Events | 2026-07 | 5 | B1·B2·B3·B6·B7 | ax_core/washing |
| [NYC Executive Forum 2026 - A Leader’s Guide to Data Strategy](https://www.youtube.com/watch?v=Piy37om0y6A) | AWS Events | 2026-07 | 5 | B1·B2·B3·B4·B5 | ax_core/neutral |
| [NYC Executive Forum 2026 - The Collective Edge: Cross-functi](https://www.youtube.com/watch?v=3JHA7ayOJuE) | AWS Events | 2026-07 | 5 | B1·B3·B4·B5·B7 | ax_core/neutral |
| [Tokyo Executive Forum 2026 - A Leader's Guide to AI Strategy](https://www.youtube.com/watch?v=zCauJHa3UGo) | AWS Events | 2026-07 | 5 | B1·B2·B3·B5·B7 | ax_core/neutral |
| [Tokyo Executive Forum 2026 - A Leader's Guide to Advanced Te](https://www.youtube.com/watch?v=IfFVeLcr-co) | AWS Events | 2026-07 | 5 | B1·B2·B5·B7·B8 | ax_core/anti_washing |
| [CCW 2026: Dominion Energy’s AI-Powered Transformation with A](https://www.youtube.com/watch?v=d2nUemwh30c) | AWS Events | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [CCW 2026: How Citizens Bank is building the AI-native custom](https://www.youtube.com/watch?v=O_Imo9L04mo) | AWS Events | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [NYC Executive Forum 2026 - A Leader’s Guide to Agentic AI](https://www.youtube.com/watch?v=vvyOHc7jsmg) | AWS Events | 2026-07 | 4 | B1·B4·B5·B6 | ax_core/anti_washing |
| [Tokyo Executive Forum 2026 - Fireside Chat with Jason Bennet](https://www.youtube.com/watch?v=1YbKbO1p7GQ) | AWS Events | 2026-07 | 4 | B1·B4·B5·B6 | ax_core/neutral |
| [CES 2026 - Scaling agentic AI to achieve breakthrough transf](https://www.youtube.com/watch?v=Ba2KXHdbjR0) | Accenture | 2026-01 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [The Skills Mismatch Economy | How AI is reshaping skill dema](https://www.youtube.com/watch?v=HmuEoDwZnqg) | Accenture | 2026-04 | 5 | B1·B3·B4·B5·B8 | ax_core/anti_washing |
| [Consumers are handing decisions to AI agents: what brands ne](https://www.youtube.com/watch?v=-vqhuxajdWs) | Accenture | 2026-07 | 4 | B1·B2·B4·B7 | ax_adjacent/neutral |
| [Alibaba Cloud Claw Talks EP4 | Secure AI Agents Across Full ](https://www.youtube.com/watch?v=mm9Fl1LcBXI) | Alibaba Cloud | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [What do people use AI models for?](https://www.youtube.com/watch?v=VSmobknYl0E) | Anthropic | 2024-12 | 4 | B1·B6·B7·B8 | ax_core/anti_washing |
| [Claude for Financial Services Keynote](https://www.youtube.com/watch?v=50AhIyybR0M) | Anthropic | 2025-07 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [WWDC26: Meet Trust Insights | Apple](https://www.youtube.com/watch?v=jY-_rqz_VEM) | Apple Developer | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Inside Apple Intelligence and Xcode: Special Presentation | ](https://www.youtube.com/watch?v=Wpwjqk1UGnQ) | Apple Developer | 2026-06 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [WWDC26: What’s new in the Foundation Models framework | Appl](https://www.youtube.com/watch?v=Xrv8m_EHCbg) | Apple Developer | 2026-06 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Ashwini Vaishnaw: On India’s path to “Tech Powerhouse”](https://www.youtube.com/watch?v=dmU0LX5aI-0) | Arm | 2025-10 | 5 | B1·B4·B5·B7·B8 | ax_core/neutral |
| [Arm CEO Rene Haas on AI, chips, and the future of global com](https://www.youtube.com/watch?v=mpEnhLkwGrU) | Arm | 2026-01 | 4 | B2·B3·B4·B7 | ax_core/anti_washing |
| [Panos Panay: On Humility and Empathy in Leadership](https://www.youtube.com/watch?v=YF7dcSd_3L0) | Arm | 2026-01 | 4 | B1·B3·B4·B5 | ax_core/neutral |
| [Chris Bergey, EVP, Edge AI Business Unit, Arm, on the GSMA '](https://www.youtube.com/watch?v=nzXbAX4Yo90) | Arm | 2026-03 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [APO GAIA Podcast | Korea’s AI Policy and Manufacturing AX wi](https://www.youtube.com/watch?v=LogtwSzSdWw) | Asian Productivity Organ | 2026-07 | 5 | B3·B4·B5·B7·B8 | ax_core/neutral |
| [Lead with Purpose, Adapt with Strategy | Phillip Benedetti (](https://www.youtube.com/watch?v=c9-0LUYKwhI) | Boston Consulting Group | 2026-08 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Why Humanoids Are the Future of Manufacturing | Boston Dynam](https://www.youtube.com/watch?v=laexcnaTrDM) | Boston Dynamics | 2025-11 | 4 | B1·B2·B3·B7 | ax_core/anti_washing |
| [Tycho van der Ouderaa and Matt Beton - KPOP  Kronecker Preco](https://www.youtube.com/watch?v=1DTSdYy2RcU) | Cohere | 2025-08 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [Bell Canada and Dell Technologies discuss their partnership ](https://www.youtube.com/watch?v=dbJ7a2c6KoA) | Cohere | 2025-10 | 4 | B1·B2·B4·B5 | ax_core/neutral |
| [Cohere Labs Connect Conference - Day 3](https://www.youtube.com/watch?v=UAAHd6rMWp8) | Cohere | 2025-11 | 5 | B1·B2·B3·B5·B8 | ax_adjacent/anti_washing |
| [Cohere Labs Connect Conference - Day 1](https://www.youtube.com/watch?v=fbMqJHOel0U) | Cohere | 2025-11 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [Cohere Labs Connect Conference - Day 2](https://www.youtube.com/watch?v=Q-upWvYEx-E) | Cohere | 2025-11 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [How  Collaboration Accelerates Progress in AI Research - Sha](https://www.youtube.com/watch?v=b0ydOb6e_T0) | Cohere | 2025-11 | 4 | B1·B3·B5·B8 | ax_adjacent/neutral |
| [Weijia Shi and Xiaochuang Han - 𝐋𝐥𝐚𝐦𝐚𝐅𝐮𝐬𝐢𝐨𝐧  Adapting Pretra](https://www.youtube.com/watch?v=Mg4fr56eB_8) | Cohere | 2025-11 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [Wisdom Ikezogwo   Distilling Multimodal Pretraining Data and](https://www.youtube.com/watch?v=FiCr2yUafPE) | Cohere | 2025-12 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Aditri Bhagirath  - Persona Guided Personalization](https://www.youtube.com/watch?v=0X01DFnA2dc) | Cohere | 2026-01 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/anti_washing |
| [Ahsaas Bajaj  - Production Grade ML in Practice  Evaluation ](https://www.youtube.com/watch?v=UkOvqHSskMw) | Cohere | 2026-01 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Nathan Calvin - Three People vs  Big AI  Policy, Power, and ](https://www.youtube.com/watch?v=RV00BTMY5XA) | Cohere | 2026-02 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [Dr  Plamen Miltenoff - AI and XR in Education  From Curiosit](https://www.youtube.com/watch?v=Pb2t7U6vf7Y) | Cohere | 2026-03 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Jiafei Duan  - Building Robotics Foundation Model with Reaso](https://www.youtube.com/watch?v=ZB5IAlFvt1c) | Cohere | 2026-04 | 4 | B1·B2·B3·B8 | ax_core/anti_washing |
| [Zifeng Liu - Human–AI Collaboration in Educational Assessmen](https://www.youtube.com/watch?v=X84gmuT9RI8) | Cohere | 2026-04 | 4 | B1·B2·B5·B6 | ax_adjacent/neutral |
| [O-Ring Automation & the Economics of Bicycles for the Mind w](https://www.youtube.com/watch?v=uUUBApVevNI) | Cohere | 2026-06 | 5 | B1·B3·B4·B7·B8 | ax_core/neutral |
| [ML Summer School 2026 - Methodologies for Improving the Qual](https://www.youtube.com/watch?v=hbqSsYM5nbA) | Cohere | 2026-07 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/anti_washing |
| [Opening Keynote, Michael Truell | Compile 26](https://www.youtube.com/watch?v=fWa7uxyhVDE) | Cursor | 2026-06 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Running 128 Coding Agents at Once](https://www.youtube.com/watch?v=-jnwTZ789V0) | Cursor | 2026-06 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [The AI adoption playbook: Lessons from Microsoft's internal ](https://www.youtube.com/watch?v=c51ToE4pPpY) | DX | 2026-08 | 5 | B3·B4·B5·B7·B8 | ax_core/anti_washing |
| [Sam Altman and Ali Ghodsi: OpenAI + Databricks, AI Agents in](https://www.youtube.com/watch?v=gz1sOEETcgE) | Databricks | 2025-11 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [How Databricks + AWS Help Enterprises Take GenAI to Producti](https://www.youtube.com/watch?v=Q6jRdpF6yXE) | Databricks | 2025-12 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Databricks x Palantir | Partnership Deep Dive](https://www.youtube.com/watch?v=BsSwqYuok1A) | Databricks | 2026-01 | 5 | B1·B2·B3·B4·B8 | ax_core/neutral |
| [Dario Amodei and Ali Ghodsi: Anthropic + Databricks, AI Agen](https://www.youtube.com/watch?v=MTsoRWPS46o) | Databricks | 2026-03 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Getting Started with Unity Catalog: A Step-by-Step Databrick](https://www.youtube.com/watch?v=ORMH3pQG8yM) | Databricks | 2026-03 | 4 | B1·B2·B5·B8 | ax_core/neutral |
| [Building Enterprise-Ready Agents using Agent Bricks](https://www.youtube.com/watch?v=sjXgUdovOdM) | Databricks | 2026-05 | 5 | B1·B2·B3·B5·B8 | ax_core/neutral |
| [Building Trustworthy, High-Quality AI Agents with MLflow](https://www.youtube.com/watch?v=NcHCkPMww7Q) | Databricks | 2026-05 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [Databricks on Databricks: How Marketers Use Data 3x More wit](https://www.youtube.com/watch?v=zWHzl5tEW8A) | Databricks | 2026-06 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Defending against a tidal wave of AI attacks with Lakewatch,](https://www.youtube.com/watch?v=3GhVeYY3Bmo) | Databricks | 2026-06 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [Introducing LTAP (Lake Transactional/Analytical Processing):](https://www.youtube.com/watch?v=9J2-PovJppA) | Databricks | 2026-06 | 4 | B1·B2·B4·B5 | ax_adjacent/neutral |
| [Unlocking agentic data engineering with Lakeflow + Genie](https://www.youtube.com/watch?v=0WDGu-IPmZM) | Databricks | 2026-06 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [AI Agents: getting to 90%, the AI adoption playbook for Ente](https://www.youtube.com/watch?v=01NYw3PzqiI) | Dust - Transform how wor | 2026-07 | 4 | B1·B3·B5·B7 | ax_core/anti_washing |
| [Adam Evans at the ElevenLabs Summit](https://www.youtube.com/watch?v=L-I4WMzFjtM) | ElevenLabs | 2025-12 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [How BCG, Naturgy, and Konecta Are Deploying AI Agents in Pro](https://www.youtube.com/watch?v=TPV30xP1gyM) | ElevenLabs | 2026-03 | 5 | B1·B2·B3·B4·B7 | ax_core/neutral |
| [Sequoia's Doug Leone on Building Enduring Companies in the A](https://www.youtube.com/watch?v=afSmwxT0Y3o) | ElevenLabs | 2026-03 | 4 | B1·B3·B5·B7 | ax_core/anti_washing |
| [Deploying AI at Enterprise Scale - ElevenLabs Summit](https://www.youtube.com/watch?v=HdelDovObRU) | ElevenLabs | 2026-08 | 5 | B1·B2·B4·B6·B7 | ax_core/neutral |
| [How to Lead Your Organisation’s AI-Transformation • Rasmus L](https://www.youtube.com/watch?v=1uJZlKig0Tk) | GOTO Conferences | 2026-07 | 5 | B1·B3·B5·B7·B8 | ax_core/anti_washing |
| [Building a privacy-first smart home with Frank Nijhof | Epis](https://www.youtube.com/watch?v=al-JSC314dA) | GitHub | 2026-01 | 4 | B1·B2·B4·B8 | ax_adjacent/washing |
| [Inside Octoverse 2025 report: The rise of vibe coding & agen](https://www.youtube.com/watch?v=ve-tfDEQOG8) | GitHub | 2026-01 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Build AI agents on Cloud Run](https://www.youtube.com/watch?v=zthWHEU3Y7M) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/neutral |
| [Generative UI for any agent, anywhere: A2UI, AG-UI, MCP Apps](https://www.youtube.com/watch?v=UsMDkEsR-ok) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Navigate the agentic shift in software development with Goog](https://www.youtube.com/watch?v=Z9Zz75pmOeg) | Google Cloud Tech | 2026-06 | 5 | B1·B4·B6·B7·B8 | ax_core/washing |
| [Power intelligent agents with AI-native databases](https://www.youtube.com/watch?v=7awKinJhGPo) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/washing |
| [Power intelligent agents with AI-native databases](https://www.youtube.com/watch?v=quzn4hOXQmI) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/washing |
| [The Gemini 3 playbook: Optimizing for quality, cost, and sca](https://www.youtube.com/watch?v=lbUkqPj63eQ) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B3·B4·B6 | ax_core/anti_washing |
| [Under the hood for startups: How Google DeepMind makes model](https://www.youtube.com/watch?v=A4nNQfGqZIs) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B3·B4·B8 | ax_core/washing |
| [What's new in Google Cloud's agent platform](https://www.youtube.com/watch?v=FxnjRYo3fpU) | Google Cloud Tech | 2026-06 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Agent context engineering for production](https://www.youtube.com/watch?v=YKLkHvzjFDk) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B4·B8 | ax_adjacent/anti_washing |
| [From prototype to production: 45 minutes to a reliable Gemin](https://www.youtube.com/watch?v=fkCTifAqVGg) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [NoSQL for modern apps and AI: The future of Memorystore, Fir](https://www.youtube.com/watch?v=Y7HwVL3LdNo) | Google Cloud Tech | 2026-06 | 4 | B1·B4·B5·B7 | ax_core/washing |
| [Scale AI agents in production](https://www.youtube.com/watch?v=LHcjN11nNPU) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Startups shipping at scale with Google DeepMind](https://www.youtube.com/watch?v=RA_fQvXQ4aw) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B3·B5 | ax_core/anti_washing |
| [The agent-quality flywheel: Using Gemini Enterprise Agent Pl](https://www.youtube.com/watch?v=eLQAJqydXqY) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [What's new in AlloyDB: Scale PostgreSQL for agentic AI and h](https://www.youtube.com/watch?v=vw1AzTNUiE4) | Google Cloud Tech | 2026-06 | 4 | B1·B4·B5·B6 | ax_core/washing |
| [What's new in Cloud Run](https://www.youtube.com/watch?v=AoisAy_LGpI) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [What's new in Cloud SQL: Drive performance, high availabilit](https://www.youtube.com/watch?v=zKXbKmpqWB0) | Google Cloud Tech | 2026-06 | 4 | B1·B5·B7·B8 | ax_core/neutral |
| [What's new with Gemini from Google DeepMind](https://www.youtube.com/watch?v=92LvgAcR6fI) | Google Cloud Tech | 2026-06 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [What's new with data agents](https://www.youtube.com/watch?v=Z-AfOcWO_kk) | Google Cloud Tech | 2026-06 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [Build core skills to thrive as an AI-era developer](https://www.youtube.com/watch?v=q_Jq4IgYImk) | Google Developers | 2026-05 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [A fireside chat on the evolution of the developer craft](https://www.youtube.com/watch?v=VTYx7Ex-0bA) | Google Developers | 2026-05 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [Beyond the keynote with Sundar Pichai](https://www.youtube.com/watch?v=9C20esBUf-Q) | Google Developers | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [What's new in the Gemma open model family](https://www.youtube.com/watch?v=oUtiZbrehrw) | Google Developers | 2026-05 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Sameer Samat on Android 17 and the Future of Intelligent Com](https://www.youtube.com/watch?v=YvVsdZL2ogY) | Google Developers | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/neutral |
| ["Our North Star": IOH & AI Transforming Indonesia's Intellig](https://www.youtube.com/watch?v=QZZBEYvYq6g) | Huawei | 2025-08 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Smart Retailer DeFacto is Leading Fashion's "Phygital" Futur](https://www.youtube.com/watch?v=YOxwp5bzZvk) | Huawei | 2025-09 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Discipline, Not Hype, Will Define AI Innovation](https://www.youtube.com/watch?v=c6nYPWNgl7I) | Huawei | 2026-04 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [A Tour Through The Hugging Face Hub & A Hands on Guide To Gr](https://www.youtube.com/watch?v=k8sHYMeDitQ) | Hugging Face | 2022-04 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Machine Learning Experts - Lewis Tunstall](https://www.youtube.com/watch?v=igW5VWewuLE) | Hugging Face | 2022-04 | 4 | B1·B3·B4·B5 | ax_adjacent/washing |
| [Hugging Face Reading Group: Session 1](https://www.youtube.com/watch?v=8uVvfJIH_LY) | Hugging Face | 2022-10 | 4 | B1·B2·B4·B8 | ax_adjacent/neutral |
| [Hugging Face Reading Group: Session 3](https://www.youtube.com/watch?v=TrwshPQcWiM) | Hugging Face | 2022-11 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Hugging Face Reading Group: Session 4](https://www.youtube.com/watch?v=zQfSPn7zk7U) | Hugging Face | 2022-12 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [AI isn’t digital transformation, and leaders need to underst](https://www.youtube.com/watch?v=eZ1NizUx9U4) | IBM | 2026-07 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Live from Think 2026: AI operating model, VC funding & CAIO ](https://www.youtube.com/watch?v=YHKXflgkHak) | IBM Technology | 2026-05 | 5 | B1·B3·B4·B5·B8 | ax_core/anti_washing |
| [AI at college graduations and why Claude blackmails](https://www.youtube.com/watch?v=1h6e5MFg9I0) | IBM Technology | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [AI skills security, Open AI Deployment Company & zero days](https://www.youtube.com/watch?v=YCWwh70FZtQ) | IBM Technology | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Agent control planes & OpenAI model solves Erdős](https://www.youtube.com/watch?v=wVdivlahcm0) | IBM Technology | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [OpenAI’s Daybreak and Mistral’s Mythos competitor](https://www.youtube.com/watch?v=u2MFautDjuM) | IBM Technology | 2026-05 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Microsoft’s new AI models & bots dominate the internet](https://www.youtube.com/watch?v=SvBheXuKY8s) | IBM Technology | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [The future of software engineering, tokenmaxxing and AI in h](https://www.youtube.com/watch?v=EKULOf_Cy0w) | IBM Technology | 2026-06 | 5 | B1·B4·B5·B7·B8 | ax_core/anti_washing |
| [Claude Fable 5 & Apple’s NVIDIA deal](https://www.youtube.com/watch?v=aByPOYCEH6I) | IBM Technology | 2026-06 | 4 | B1·B2·B4·B8 | ax_adjacent/neutral |
| [New AI models, token minimization and IBM’s new sub-1nm chip](https://www.youtube.com/watch?v=d-hJa-yDJmQ) | IBM Technology | 2026-06 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Reddit cracks down on AI slop & the future of AI compute](https://www.youtube.com/watch?v=WHFLWrnFc1E) | IBM Technology | 2026-07 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/washing |
| [2026 Cost of a Data Breach Report: AI Is Changing Cybersecur](https://www.youtube.com/watch?v=b2PESRl7De4) | IBM Technology | 2026-07 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [GLM-5.2: The real security risk? Plus: Vibe hunting, the end](https://www.youtube.com/watch?v=qXGJ7pi-XOo) | IBM Technology | 2026-07 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [GPT-5.6 Sol, FIFA AI & Wall Street’s AI nerves](https://www.youtube.com/watch?v=tV5zXS78HzU) | IBM Technology | 2026-07 | 4 | B1·B2·B7·B8 | ax_core/neutral |
| [GPT-Red: Can AI red teams stop prompt injections?](https://www.youtube.com/watch?v=g4CNcUAqM4Q) | IBM Technology | 2026-07 | 4 | B1·B2·B6·B8 | ax_adjacent/neutral |
| [The Cost of a Data Breach 2026, and what we can learn from t](https://www.youtube.com/watch?v=lx41qvj80Jo) | IBM Technology | 2026-07 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [The new post-quantum cryptography executive order. Plus: Wha](https://www.youtube.com/watch?v=RYUR9BdDgyI) | IBM Technology | 2026-07 | 4 | B2·B3·B4·B8 | ax_core/washing |
| [Brand Finance Global 500 Launch 2026 | AI Rising: The Evolut](https://www.youtube.com/watch?v=2GboyaQ1VKs) | Infosys | 2026-03 | 5 | B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y) | Infosys | 2026-07 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Innovating & Measuring ROI for Enterprise Organizations Thro](https://www.youtube.com/watch?v=U84H7KOAlyU) | Insight Solutions | 2026-08 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Building AI Tools to Transform Sales and Marketing, an Insid](https://www.youtube.com/watch?v=J7wGwY0lX_E) | Intel | 2024-12 | 5 | B1·B5·B6·B7·B8 | ax_core/anti_washing |
| [AI PCs | Discover a New World of Experiences | Intel](https://www.youtube.com/watch?v=3PTyqM2BFpQ) | Intel | 2025-01 | 5 | B1·B2·B3·B4·B8 | ax_core/neutral |
| [Intel Keynote: AI Inside for a New Era | Intel](https://www.youtube.com/watch?v=8z9o2ltnFM0) | Intel | 2025-01 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [AI at the Edge | Transforming Industries and the Workplace​ ](https://www.youtube.com/watch?v=mrWTLjitaX4) | Intel | 2025-01 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Direct Connect 2025 Keynote | Intel](https://www.youtube.com/watch?v=0ED7n2g8lO0) | Intel | 2025-04 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Scaling Enterprise AI: Inference, Infrastructure, and the Fu](https://www.youtube.com/watch?v=UMc1ShyUcs8) | Intel | 2025-04 | 5 | B1·B2·B4·B5·B7 | ax_core/washing |
| [The AI-Powered Enterprise: Insights from Lumen Technologies ](https://www.youtube.com/watch?v=JUfwnwpbx0M) | Intel | 2025-04 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [From Smart Devices to Supply Chain: Lenovo's Blueprint for T](https://www.youtube.com/watch?v=Ojz9U4ao3go) | Intel | 2025-05 | 5 | B1·B2·B3·B4·B8 | ax_core/neutral |
| [Building Scalable and Sustainable AI Infrastructure | Intel](https://www.youtube.com/watch?v=U0oZkI_nYYA) | Intel | 2025-05 | 4 | B1·B4·B5·B7 | ax_core/neutral |
| [Edge AI – The Next Transformation | Intel](https://www.youtube.com/watch?v=xPadduZuK4Q) | Intel | 2025-05 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Designing Empathetic AI: The Future of Human-Centered Techno](https://www.youtube.com/watch?v=atZ1lRqE8wY) | Intel | 2025-06 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [AI for Accessibility: How Sorenson Is Advancing Inclusive Co](https://www.youtube.com/watch?v=vx1g4xu5qMk) | Intel | 2025-08 | 4 | B3·B4·B7·B8 | ax_core/neutral |
| [AI PCs and the Future of Cybersecurity: AI-Powered Protectio](https://www.youtube.com/watch?v=GzFE6k-S3vA) | Intel | 2025-09 | 5 | B1·B2·B4·B7·B8 | ax_core/neutral |
| [From PoC to Production: How Lenovo Turns AI into Enterprise ](https://www.youtube.com/watch?v=JI9W8S_6QbY) | Intel | 2025-09 | 4 | B3·B5·B7·B8 | ax_core/neutral |
| [The Age of With: Rethinking Enterprise Strategy Through Agen](https://www.youtube.com/watch?v=NgeYg6tyncs) | Intel | 2025-10 | 5 | B1·B2·B3·B4·B5 | ax_core/anti_washing |
| [Agentic AI in Action: Transforming Health, Education, and Co](https://www.youtube.com/watch?v=5wlY9FcvRiE) | Intel | 2025-10 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [AI Industrialization: The Next Frontier for Global Enterpris](https://www.youtube.com/watch?v=fSadUMtpwcY) | Intel | 2025-11 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Core Ultra Series 3 Launch Event | Intel](https://www.youtube.com/watch?v=KlIlFt2Fj1c) | Intel | 2026-01 | 5 | B1·B4·B5·B7·B8 | ax_core/anti_washing |
| [Executive overview of the 2026 Intel Platform Security Repor](https://www.youtube.com/watch?v=J5KlRWZm_fk) | Intel | 2026-03 | 5 | B1·B2·B3·B4·B8 | ax_core/anti_washing |
| [Intel Computex Keynote 2026](https://www.youtube.com/watch?v=7HvrdXjdlU8) | Intel | 2026-06 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [KT 에이블스쿨 10기 모집설명회](https://www.youtube.com/watch?v=0WphLSKUbDw) | KT | 2026-07 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [Expert AI Alliance Workshop – Full Version](https://www.youtube.com/watch?v=3aSJ0XdENkU) | LG AI Research | 2022-02 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [LG AI Talk Concert 2022 | 오프닝 & 키노트 배경훈 원장](https://www.youtube.com/watch?v=CPLCy-hG9wM) | LG AI Research | 2022-12 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [LG AI Talk Concert 2023](https://www.youtube.com/watch?v=tbeGE19qIk4) | LG AI Research | 2023-07 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [LG AI Talk Concert 2025 - Shaping the Future of AI](https://www.youtube.com/watch?v=EGzIMo4AizA) | LG AI Research | 2025-07 | 5 | B1·B4·B6·B7·B8 | ax_core/washing |
| [[2025년 9월 월간 D-Talks] Agentic AI, 설계·실행·검증을 빠르게! AI 에이전트 개발 ](https://www.youtube.com/watch?v=Ye-ewCPn8EE) | LG CNS | 2026-08 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Top Job Application Skills to Help Get You Hired](https://www.youtube.com/watch?v=N8xrgemiO3E) | LinkedIn | 2024-05 | 4 | B1·B5·B7·B8 | ax_adjacent/neutral |
| [Building trust: A powerful performance multiplier | Mayo Cli](https://www.youtube.com/watch?v=g-I1dJB2puo) | Mayo Clinic | 2026-07 | 4 | B5·B6·B7·B8 | ax_core/anti_washing |
| [The changing role of the CMO—and what it means for growth](https://www.youtube.com/watch?v=NTVuuPSohHI) | McKinsey & Company | 2025-08 | 4 | B2·B3·B4·B7 | ax_core/anti_washing |
| [Top trends disrupting how companies develop and commercializ](https://www.youtube.com/watch?v=PYTneT1j4_0) | McKinsey & Company | 2025-08 | 4 | B1·B2·B3·B7 | ax_core/neutral |
| [AI-Driven Consulting: Kate Smaje on Navigating the Future](https://www.youtube.com/watch?v=pomQmWBmbV0) | McKinsey & Company | 2025-10 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Ask Us Anything: Blair Ciesil and Marie Padberg get into you](https://www.youtube.com/watch?v=oJcziqz673U) | McKinsey & Company | 2025-10 | 4 | B3·B4·B5·B8 | ax_adjacent/anti_washing |
| [Inside the ”one firm” mindset at McKinsey: Global leadership](https://www.youtube.com/watch?v=DkwL7xDB2I8) | McKinsey & Company | 2025-11 | 4 | B3·B4·B5·B7 | ax_core/washing |
| [Productivity first: AI and the COO agenda](https://www.youtube.com/watch?v=O-aUZqfcLKg) | McKinsey & Company | 2025-11 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [Unlocking hidden value with process intelligence in healthca](https://www.youtube.com/watch?v=yoWyJnej0Iw) | McKinsey & Company | 2025-11 | 4 | B3·B4·B5·B7 | ax_core/washing |
| [The Future of Business: 13 tech trends that matter](https://www.youtube.com/watch?v=N4Ql_gatkJk) | McKinsey & Company | 2025-12 | 5 | B1·B3·B5·B6·B7 | ax_core/washing |
| [Unlocking Growth: The power of CEO, CMO, and CFO alignment](https://www.youtube.com/watch?v=ZS3QQtzcBiQ) | McKinsey & Company | 2025-12 | 5 | B2·B3·B4·B6·B7 | ax_core/anti_washing |
| [Agentic AI: Moving beyond pilots to enterprise impact](https://www.youtube.com/watch?v=-UVdUqPztMk) | McKinsey & Company | 2025-12 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [From Strategy to Performance: How leaders can build an opera](https://www.youtube.com/watch?v=coXorr4pZJs) | McKinsey & Company | 2025-12 | 4 | B2·B3·B4·B5 | ax_core/anti_washing |
| [How McKinsey helps you grow faster: Scott Rutherford on appr](https://www.youtube.com/watch?v=N0B5fX3VHaA) | McKinsey & Company | 2025-12 | 4 | B2·B3·B4·B5 | ax_adjacent/washing |
| [World Economic Forum: A Preview of Davos 2026](https://www.youtube.com/watch?v=2MWzmChPBTc) | McKinsey & Company | 2026-01 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [The paradigm shift: how agentic AI is redefining banking ope](https://www.youtube.com/watch?v=EnuwWHoUKpk) | McKinsey & Company | 2026-02 | 5 | B1·B2·B3·B4·B7 | ax_core/anti_washing |
| [The race to rewire operations: How the story unfolded in 202](https://www.youtube.com/watch?v=rSJY396HQ1c) | McKinsey & Company | 2026-02 | 5 | B1·B2·B4·B5·B7 | ax_core/washing |
| [Agents, Robots, and Us: What Executives Need To Know About A](https://www.youtube.com/watch?v=_z5ghnsWSsI) | McKinsey & Company | 2026-02 | 4 | B3·B4·B5·B7 | ax_core/anti_washing |
| [Trust In the Age of Agents](https://www.youtube.com/watch?v=Ne4HnJEjCSI) | McKinsey & Company | 2026-03 | 5 | B1·B3·B5·B7·B8 | ax_core/anti_washing |
| [MGI event: Book authors discuss how to achieve the next cent](https://www.youtube.com/watch?v=yHFybnKxy1I) | McKinsey & Company | 2026-03 | 4 | B4·B5·B7·B8 | ax_core/anti_washing |
| [MGI event: Industry leaders discuss how to advance adaptatio](https://www.youtube.com/watch?v=MtevcjCnO1w) | McKinsey & Company | 2026-03 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Winning the Race to Rewire in 2026: Capturing operational ad](https://www.youtube.com/watch?v=QHLntsXsVCQ) | McKinsey & Company | 2026-03 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [The Next Chapter of American Economic Competitiveness: A CEO](https://www.youtube.com/watch?v=iFXkNy7Elcg) | McKinsey & Company | 2026-04 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [Move First or Fall Behind: How AI Is Rewriting the Rules of ](https://www.youtube.com/watch?v=ieGq5bdmRcI) | McKinsey & Company | 2026-05 | 5 | B1·B2·B4·B5·B7 | ax_core/neutral |
| [Rewiring for AI: From Ambition to Advantage](https://www.youtube.com/watch?v=E7KxzkK2lYA) | McKinsey & Company | 2026-05 | 5 | B1·B2·B3·B4·B7 | ax_core/anti_washing |
| [Europe on the move: A conversation with Hitachi Energy’s CEO](https://www.youtube.com/watch?v=lNdU_vBBQ9Q) | McKinsey & Company | 2026-05 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [How CEOs Can Navigate Trade in 2026](https://www.youtube.com/watch?v=mCsWx9YgTig) | McKinsey & Company | 2026-05 | 4 | B2·B3·B4·B7 | ax_core/washing |
| [Global Trade Is Being Rewired: What Leaders Need to Know](https://www.youtube.com/watch?v=R2M9LLkgFTg) | McKinsey & Company | 2026-06 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Redefining Value: Fashion in the Age of AI](https://www.youtube.com/watch?v=EgbFkskWLWM) | McKinsey & Company | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [AP CEO on AI, Trust, and the Future of Journalism](https://www.youtube.com/watch?v=ifgkYPogEgU) | McKinsey & Company | 2026-07 | 5 | B1·B4·B5·B6·B7 | ax_core/neutral |
| [Powering Supply Chain With Agentic AI](https://www.youtube.com/watch?v=GJyp5SJNjyo) | McKinsey & Company | 2026-07 | 5 | B1·B4·B5·B7·B8 | ax_core/anti_washing |
| [Why Most Companies Aren't Seeing Meaningful Returns from AI](https://www.youtube.com/watch?v=BHQyOFaARQI) | McKinsey & Company | 2026-07 | 5 | B2·B3·B4·B5·B7 | ax_core/neutral |
| [AI Is Everywhere. The Agentic Organization Isn’t—Yet](https://www.youtube.com/watch?v=uqVT-2OOToo) | McKinsey & Company | 2026-07 | 4 | B1·B3·B4·B5 | ax_core/anti_washing |
| [Brain Health: Helping Individuals, Organizations, and Societ](https://www.youtube.com/watch?v=AApkPLFb_gc) | McKinsey & Company | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [The Serial Builder Advantage: Why Repeat Innovators Win](https://www.youtube.com/watch?v=kzAjzKCZAXs) | McKinsey & Company | 2026-07 | 4 | B1·B3·B4·B5 | ax_core/anti_washing |
| [The human advantage in an AI economy](https://www.youtube.com/watch?v=IGAFict9CS4) | McKinsey & Company | 2026-07 | 4 | B3·B4·B5·B7 | ax_core/anti_washing |
| [The Biggest AI Opportunity Isn’t Replacing People | Stanford](https://www.youtube.com/watch?v=u76xdhpF474) | McKinsey & Company | 2026-08 | 5 | B1·B2·B4·B5·B6 | ax_core/anti_washing |
| [The Metaverse and How We'll Build It Together -- Connect 202](https://www.youtube.com/watch?v=Uvufun6xer8) | Meta | 2021-10 | 4 | B1·B3·B4·B8 | ax_core/anti_washing |
| [Meta Connect Keynote 2022](https://www.youtube.com/watch?v=hvfV-iGwYX8) | Meta | 2022-10 | 5 | B1·B2·B3·B4·B5 | ax_core/washing |
| [Boz To The Future Podcast #23 - The Future According to Jame](https://www.youtube.com/watch?v=qOdjM14QW0s) | Meta | 2025-04 | 4 | B1·B3·B4·B8 | ax_core/anti_washing |
| [Boz To The Future # 24: The Future According to Francois Cha](https://www.youtube.com/watch?v=WpFCYR3f46U) | Meta | 2025-11 | 4 | B1·B2·B4·B5 | ax_core/washing |
| [Boz To The Future # 25: The Future According to Dylan Field](https://www.youtube.com/watch?v=diMGvhBfy74) | Meta | 2025-11 | 4 | B1·B2·B5·B6 | ax_core/washing |
| [Boz To The Future #26: The Future According to Ed Catmull](https://www.youtube.com/watch?v=4s1_DKMYQVo) | Meta | 2026-05 | 4 | B1·B2·B4·B6 | ax_adjacent/anti_washing |
| [Meta Horizon Store: Paths to Engage and Monetize Your Audien](https://www.youtube.com/watch?v=DK5Q6C8Iepo) | Meta Developers | 2025-10 | 5 | B1·B2·B3·B4·B7 | ax_adjacent/neutral |
| [Building Next-Gen Worlds with Meta Horizon Studio](https://www.youtube.com/watch?v=viXoK-MJRls) | Meta Developers | 2025-10 | 4 | B1·B3·B4·B8 | ax_core/anti_washing |
| [Developer Preview: Introducing Meta Wearables Device Access ](https://www.youtube.com/watch?v=U0Ha6AmXBS0) | Meta Developers | 2025-10 | 4 | B1·B3·B4·B7 | ax_core/neutral |
| [The State of the VR Ecosystem: Building a Sustainable Future](https://www.youtube.com/watch?v=_NMYZYzva6Q) | Meta Developers | 2026-04 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [VR 201: Essential Tools to Power Your Quest Development](https://www.youtube.com/watch?v=rVvqfcD3jmg) | Meta Developers | 2026-04 | 4 | B1·B2·B3·B7 | ax_core/neutral |
| [VR Performance Fundamentals for Quest 3/3S](https://www.youtube.com/watch?v=w-ys2nE-MgI) | Meta Developers | 2026-04 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [AI and automation expert on how leaders use AI agents to get](https://www.youtube.com/watch?v=HXy3J1mGHRE) | Microsoft | 2025-10 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Is Agentic AI upending the corporate ladder? EY's Global Con](https://www.youtube.com/watch?v=ilaDQLa1Lrk) | Microsoft | 2025-12 | 4 | B1·B2·B4·B5 | ax_core/washing |
| [The AI app transforming how Kenya’s small businesses grow](https://www.youtube.com/watch?v=be_LYViMr2k) | Microsoft | 2026-02 | 4 | B1·B2·B4·B7 | ax_adjacent/neutral |
| [The future of work: navigating the AI shift | On Second Thou](https://www.youtube.com/watch?v=KFsu0Hyf1XM) | Microsoft | 2026-02 | 4 | B1·B2·B4·B5 | ax_adjacent/washing |
| [AI's Mythos Moment: Preparing governments for AI | Former UK](https://www.youtube.com/watch?v=vHlFzbE78jk) | Microsoft | 2026-06 | 4 | B2·B4·B5·B8 | ax_core/anti_washing |
| [The future of work has no org chart | Microsoft Katy George](https://www.youtube.com/watch?v=r4qZz66GlNQ) | Microsoft | 2026-07 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Why AI adoption fails (and how to fix it)](https://www.youtube.com/watch?v=mlXbfJf80k8) | Microsoft | 2026-07 | 4 | B1·B4·B5·B6 | ax_core/neutral |
| [Optimize Azure Storage costs: smart tier, automation, and Az](https://www.youtube.com/watch?v=QOcCdyL1lLY) | Microsoft Azure | 2026-03 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Personalize Customer Experiences](https://www.youtube.com/watch?v=gaEgp-nEB9g) | Microsoft Azure | 2026-03 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Reduce Azure networking service costs: smart routing, locali](https://www.youtube.com/watch?v=KiF_Cn5PdfU) | Microsoft Azure | 2026-03 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [S2E1 | Are my agents hunting for data? — The Shift Podcast b](https://www.youtube.com/watch?v=uTv-E-vz570) | Microsoft Azure | 2026-03 | 4 | B1·B2·B5·B6 | ax_core/anti_washing |
| [S2E3 | Wait, my agent needs a database? — The Shift Podcast ](https://www.youtube.com/watch?v=k9QgmurnNCU) | Microsoft Azure | 2026-03 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [Voice of the MVP - Oracle AI Database@Azure](https://www.youtube.com/watch?v=-ZQx_b2lUCU) | Microsoft Azure | 2026-04 | 5 | B1·B3·B4·B7·B8 | ax_core/neutral |
| [S2E6 | Is Postgres the wave of the future? — The Shift Podca](https://www.youtube.com/watch?v=OBc1TyXH0WQ) | Microsoft Azure | 2026-04 | 4 | B1·B4·B6·B8 | ax_core/neutral |
| [Build agents where work happens: chats channels and meetings](https://www.youtube.com/watch?v=Q9uv_y04rJE) | Microsoft Developer | 2026-06 | 4 | B2·B4·B7·B8 | ax_core/anti_washing |
| [Migrating VLDBs from Oracle to Azure Database for PostgreSQL](https://www.youtube.com/watch?v=i4mbsBs1wOE) | Microsoft Developer | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Domain AI models fine-tuned with proprietary knowledge | AI ](https://www.youtube.com/watch?v=7evOiuXFkQo) | Mistral AI | 2026-07 | 5 | B2·B4·B5·B7·B8 | ax_core/anti_washing |
| [Luxembourg's sovereign AI playbook for Europe | AI Now Summi](https://www.youtube.com/watch?v=0lqZpQZLGKs) | Mistral AI | 2026-07 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Building custom code models for Ericsson proprietary silicon](https://www.youtube.com/watch?v=ArWG4pmTXPQ) | Mistral AI | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [The AI sovereignty paradox: Scalable ecosystems for trusted ](https://www.youtube.com/watch?v=xP-3iMTPav0) | Mistral AI | 2026-07 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [[Brown-Bag 런치세미나] 공공을 위한 클라우드 상품](https://www.youtube.com/watch?v=52qSYsUFIkw) | NAVER Cloud | 2023-10 | 4 | B1·B3·B5·B8 | ax_core/anti_washing |
| [[Solutions Showcase] Java 유료화와 성능 고민! Azul로 한 ](https://www.youtube.com/watch?v=EV2nN5ZHNrs) | NAVER Cloud | 2023-11 | 5 | B1·B2·B4·B7·B8 | off_topic/neutral |
| [[Solution showcase] 자유롭고 유연한 커스텀 환경으로 차별화된 이커머스 구축](https://www.youtube.com/watch?v=J4BsujJyTBo) | NAVER Cloud | 2024-03 | 4 | B1·B2·B4·B7 | ax_adjacent/neutral |
| [[Brown-Bag 런치세미나] 2024년 보안트렌드 살펴보기](https://www.youtube.com/watch?v=6OUSU8wzvac) | NAVER Cloud | 2024-04 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [AI 개발, 어디까지 해보셨어요? 네이버클라우드와 함께한 AI 포텐데이 기술밋업](https://www.youtube.com/watch?v=y0Plw95FAnM) | NAVER Cloud | 2025-03 | 4 | B1·B2·B4·B8 | ax_adjacent/anti_washing |
| [NVIDIA & Lilly: The AI Revolution in Drug Discovery | Jensen](https://www.youtube.com/watch?v=zbiEYMapsvw) | NVIDIA | 2026-02 | 4 | B1·B2·B4·B7 | ax_core/washing |
| [NVIDIA GTC Telecom Special Address: The AI Grid—Intelligentl](https://www.youtube.com/watch?v=cxiOhp9BJTs) | NVIDIA | 2026-03 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Think You Know AI? 25 Startups Prove You Wrong](https://www.youtube.com/watch?v=D1x8ewtJAa0) | NVIDIA | 2026-04 | 5 | B1·B2·B4·B7·B8 | ax_core/neutral |
| [Inside Instacart's AI-Powered Smart Shopping Cart | NVIDIA A](https://www.youtube.com/watch?v=Alz-bhXqyXM) | NVIDIA | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [NVIDIA & Coherent: Reindustrializing America, Manufacturing ](https://www.youtube.com/watch?v=GsqW5MPFajw) | NVIDIA | 2026-06 | 4 | B1·B4·B5·B7 | ax_core/washing |
| [How NVIDIA Runs Its Own AI Factory | AI Factory Insider Ep. ](https://www.youtube.com/watch?v=Jpsq_-1kJTo) | NVIDIA | 2026-07 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Prepare for Your NVIDIA Certification Exam](https://www.youtube.com/watch?v=Kd3nbaMZy8k) | NVIDIA Developer | 2025-02 | 4 | B1·B3·B4·B5 | ax_core/anti_washing |
| [A New Era for Generalist Robotics: The Rise of Humanoids | N](https://www.youtube.com/watch?v=BmD22FNOAY4) | NVIDIA Developer | 2025-04 | 4 | B1·B2·B4·B6 | ax_core/anti_washing |
| [An Introduction to Building Humanoid Robots | NVIDIA GTC 202](https://www.youtube.com/watch?v=Oyon1QDpU6g) | NVIDIA Developer | 2025-04 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Frontiers of AI and Computing: A Conversation With Yann LeCu](https://www.youtube.com/watch?v=eyrDM3A_YFc) | NVIDIA Developer | 2025-04 | 4 | B1·B2·B6·B8 | ax_core/anti_washing |
| [NVIDIA DGX Spark: Your Personal AI Supercomputer | NVIDIA GT](https://www.youtube.com/watch?v=S_k69qXQ9w8) | NVIDIA Developer | 2025-04 | 4 | B1·B4·B5·B8 | ax_core/neutral |
| [Quantum Computing: Where We Are and Where We’re Headed | NVI](https://www.youtube.com/watch?v=9XB-LsfpvCU) | NVIDIA Developer | 2025-04 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Accelerating Applications with Parallel Algorithms | CUDA C+](https://www.youtube.com/watch?v=Sdjn9FOkhnA) | NVIDIA Developer | 2025-11 | 4 | B1·B2·B7·B8 | ax_adjacent/washing |
| [Open-Source AI 101: Enabling American Innovation | NVIDIA GT](https://www.youtube.com/watch?v=VqIc2LJzZG0) | NVIDIA Developer | 2025-12 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Practical Context Engineering: Eliminate Bugs with High-Sign](https://www.youtube.com/watch?v=Kz-i33toG2g) | NVIDIA Developer | 2026-04 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Build Custom Large-Scale Generative AI Models | NVIDIA GTC](https://www.youtube.com/watch?v=npQMSpCA4Lo) | NVIDIA Developer | 2026-04 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Long-Running AI Agents: The Next Breakthrough in Enterprise ](https://www.youtube.com/watch?v=NHVtXHUcVXE) | NVIDIA Developer | 2026-06 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Continual Learning for Long-Running Agents: Agents That Keep](https://www.youtube.com/watch?v=SVWmuJx0hHM) | NVIDIA Developer | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Where the Gaps Exist With Enterprise AI Adoption](https://www.youtube.com/watch?v=cE4ppGayicY) | Nasdaq | 2026-07 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [Nissan Motor Co., Ltd. 123rd Ordinary General Meeting of Sha](https://www.youtube.com/watch?v=bxMwW7KnuqE) | Nissan | 2022-06 | 4 | B3·B4·B5·B7 | ax_core/anti_washing |
| [Accelerating toward a circular economy – from idea to action](https://www.youtube.com/watch?v=lX2NDGB6AB4) | Nissan | 2023-09 | 5 | B2·B3·B4·B6·B7 | ax_core/washing |
| [Fostering a more inclusive workplace – from reactive to proa](https://www.youtube.com/watch?v=BVlPVaG34wI) | Nissan | 2023-09 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [Networked | Automating, monetizing and delivering 5G at scal](https://www.youtube.com/watch?v=FMXZu8qREaA) | Nokia | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Networked | Driving reliable 5G with secure AI and cloud-nat](https://www.youtube.com/watch?v=-_qPtPJq6EQ) | Nokia | 2026-06 | 4 | B1·B2·B3·B4 | ax_core/neutral |
| [Networked | How private 5G, edge computing, and AI are redef](https://www.youtube.com/watch?v=Vrs17zzHv2c) | Nokia | 2026-06 | 4 | B1·B2·B3·B4 | ax_core/anti_washing |
| [Nokia, Elisa & NVIDIA Accelerating AI-RAN from concept to co](https://www.youtube.com/watch?v=O8WLc1_3EHI) | Nokia | 2026-07 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Fail Forward: Why AI Adoption Rewards the Willing](https://www.youtube.com/watch?v=XrD-W6013G0) | OnePint AI | 2026-08 | 4 | B1·B4·B6·B7 | ax_core/anti_washing |
| [Customer Ignite Talk: Antonio Bravo Acin (Global Head of AI ](https://www.youtube.com/watch?v=UNJSk90Lz1c) | OpenAI | 2026-06 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [What racing reveals about working with AI — the OpenAI Podca](https://www.youtube.com/watch?v=KNPjRpNtQ7s) | OpenAI | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [AI Changes Everything: Can You Insure AI Risk?](https://www.youtube.com/watch?v=45uxFcLk6jA) | Oracle | 2026-06 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [AI Changes Everything: What Leaders Must Get Right About AI](https://www.youtube.com/watch?v=AF8rr7rCl38) | Oracle | 2026-06 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [AI Changes Everything: Inside Oracle Red Bull Racing’s AI Ed](https://www.youtube.com/watch?v=KJUfigBy684) | Oracle | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [AI Changes Everything: Using AI to Help Prevent Human Traffi](https://www.youtube.com/watch?v=G6PZCdNSl68) | Oracle | 2026-07 | 4 | B1·B2·B3·B5 | ax_core/anti_washing |
| [Au cœur de la #recherche Orange : IA, cybersécurité et résea](https://www.youtube.com/watch?v=Fuz0TWocOsU) | Orange | 2025-11 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Science, Innovation and Technology: The vision of Bruno Zerb](https://www.youtube.com/watch?v=69tvTh7axU0) | Orange | 2025-11 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Bruno Zerbib on AI, Intelligent Networks and the Future of C](https://www.youtube.com/watch?v=xPpwRnoZzlo) | Orange | 2026-03 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [La confiance, un facteur clé du déploiement de l'IA en santé](https://www.youtube.com/watch?v=jjJkYvT4MjI) | Orange | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [The Impact of Agentic AI on Telco Transformation & Innovatio](https://www.youtube.com/watch?v=c1XCSgKzhp4) | Orange | 2026-06 | 5 | B1·B2·B4·B5·B8 | ax_core/washing |
| [Backstage Pass | AIPCon 5](https://www.youtube.com/watch?v=F47gTGFk2Bo) | Palantir | 2024-09 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Backstage Pass | AIPCon 7](https://www.youtube.com/watch?v=_8RokabwNG8) | Palantir | 2025-06 | 4 | B1·B2·B4·B5 | ax_core/washing |
| [Chad & Matt | Lightweight Data Transforms with Palantir AIP](https://www.youtube.com/watch?v=MITSJDI08R4) | Palantir | 2025-08 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Overcoming Zero-Sum Thinking on Privacy, Civil Liberties, an](https://www.youtube.com/watch?v=x-NEdIcgboo) | Palantir | 2025-08 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [Chad & Chris | Tariff Savings and Compliance through Palanti](https://www.youtube.com/watch?v=xBTPNLd8Jv8) | Palantir | 2025-09 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Paragon 2025](https://www.youtube.com/watch?v=UjkRz9HkldU) | Palantir | 2025-12 | 5 | B1·B2·B4·B5·B7 | ax_core/neutral |
| [Bringing the “Mojo of Medicine” Back: How Philips Is Using A](https://www.youtube.com/watch?v=0Ye83rPSxrc) | Philips | 2026-03 | 5 | B1·B4·B5·B7·B8 | ax_core/anti_washing |
| [The Future of Medicine Is Already Here | AI, Connected Care ](https://www.youtube.com/watch?v=wYmHA5Pr6_g) | Philips | 2026-03 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Why Lived Experience Matters in Digital Health & AI | Health](https://www.youtube.com/watch?v=NJzIYjcnYig) | Philips | 2026-03 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Search Like You Mean It: Semantic Search with NLP and a Vect](https://www.youtube.com/watch?v=7RF03_WQJpQ) | Pinecone | 2021-11 | 4 | B1·B2·B5·B6 | ax_core/washing |
| [Where CyberSecurity Meets AI](https://www.youtube.com/watch?v=mWplVuntklI) | Pinecone | 2022-12 | 4 | B1·B2·B4·B5 | ax_adjacent/anti_washing |
| [Beyond Chatbots: Making an impact with AI on multiple fronts](https://www.youtube.com/watch?v=jMwptQSOeuo) | Pinecone | 2023-08 | 5 | B1·B3·B5·B7·B8 | ax_core/anti_washing |
| [Launch Sooner: An integrated AI stack for faster deployment](https://www.youtube.com/watch?v=8dhOyt1dhjg) | Pinecone | 2023-08 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Streamlining RAG Applications with Canopy](https://www.youtube.com/watch?v=d9QPDQ50B-A) | Pinecone | 2024-01 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Pinecone Workshop: LLM Size Doesn't Matter — Context Does](https://www.youtube.com/watch?v=GkQ52svNUhM) | Pinecone | 2024-04 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [Production Ready RAG in Healthcare with Pinecone and Autoblo](https://www.youtube.com/watch?v=93f7ZHPkpTk) | Pinecone | 2024-05 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [RAG Brag with Andrew Lee of Shortwave](https://www.youtube.com/watch?v=xsb2FbU4YRA) | Pinecone | 2024-05 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [RAG Brag with Mike Heap and Alex Rainey of My AskAI](https://www.youtube.com/watch?v=QxkvhBMOGAA) | Pinecone | 2024-05 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Getting GenAI Right – A live panel discussion with Sarah Wan](https://www.youtube.com/watch?v=A0jOmaPdKM4) | Pinecone | 2024-06 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/anti_washing |
| [Bits & Bytes: Vector Augmented Labeling & Classification](https://www.youtube.com/watch?v=RuJGoV87Et4) | Pinecone | 2024-06 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [The Future of Multi-Modal Search](https://www.youtube.com/watch?v=v5b-3-4NibI) | Pinecone | 2024-07 | 4 | B1·B2·B7·B8 | ax_adjacent/neutral |
| [RAG Brag with Alex Bowcut from Hyperleap](https://www.youtube.com/watch?v=JbuliMwGraQ) | Pinecone | 2024-09 | 4 | B1·B4·B5·B7 | ax_adjacent/anti_washing |
| [RAG Brag with Peter Werry from Unblocked](https://www.youtube.com/watch?v=5Rq7AGfJLCE) | Pinecone | 2024-09 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [The Magic of Multilingual Search with Pinecone Serverless an](https://www.youtube.com/watch?v=moHIBWZiYdY) | Pinecone | 2024-09 | 4 | B1·B4·B5·B7 | ax_core/anti_washing |
| [Build Real-Time RAG with Pinecone, Databricks, and Fivetran](https://www.youtube.com/watch?v=wvwdWBeH6YE) | Pinecone | 2024-12 | 4 | B1·B2·B4·B5 | ax_core/neutral |
| [Secure your RAG pipelines with fine grained authorization us](https://www.youtube.com/watch?v=S6xJ0Kkd7ss) | Pinecone | 2025-09 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [AI/Agents in Production with Delphi, Seam AI, and APIsec](https://www.youtube.com/watch?v=OSvDO9VtypU) | Pinecone | 2025-11 | 5 | B1·B2·B3·B7·B8 | ax_core/anti_washing |
| [Deep research is just really smart rag w/ Robert Caulk](https://www.youtube.com/watch?v=wAcWJtWQVN8) | Qdrant | 2025-03 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Vector Space Talk: Video Recommendations with Twelve Labs](https://www.youtube.com/watch?v=dHwhQUdH0IY) | Qdrant | 2025-05 | 4 | B1·B2·B7·B8 | ax_core/washing |
| [Operationalizing GraphRAG: Lettria’s Scalable Architecture w](https://www.youtube.com/watch?v=3guLRa5yQEk) | Qdrant | 2025-07 | 4 | B1·B2·B4·B5 | ax_adjacent/anti_washing |
| ["Mastering Relevance in Search" with Doug Turnbull & Trey Gr](https://www.youtube.com/watch?v=oiX7F1qi62Y) | Qdrant | 2025-08 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/washing |
| [Qdrant & Neo4j - Relevant and Diverse Vector Search - MMR an](https://www.youtube.com/watch?v=W58itLg3qWA) | Qdrant | 2025-09 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [Modernizing Legacy Search with Semantic Retrieval in the AI ](https://www.youtube.com/watch?v=-IHb9Dv8OQQ) | Qdrant | 2026-02 | 5 | B1·B2·B6·B7·B8 | ax_core/neutral |
| [Qualcomm  | Practical Patterns for On-Device GenAI | Alan Zh](https://www.youtube.com/watch?v=FlAmmVSYbZY) | Qdrant | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Vector Space Meetup 2026 Highlights](https://www.youtube.com/watch?v=EEXUuI6ZSu8) | Qdrant | 2026-06 | 4 | B1·B2·B3·B8 | ax_core/anti_washing |
| [Q3 Trading and Strategic Update](https://www.youtube.com/watch?v=zN3xR9s4uZM) | Reckitt | 2023-10 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [JP Morgan Consumer CEO Series: An interview with Kris Licht,](https://www.youtube.com/watch?v=cAT6AqBk_-k) | Reckitt | 2025-07 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Reckitt - Half Year 2025 Results](https://www.youtube.com/watch?v=KP7oflfrcMI) | Reckitt | 2025-07 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Reckitt Full Year Results 2025](https://www.youtube.com/watch?v=ExpojFs6mCg) | Reckitt | 2026-03 | 5 | B2·B3·B4·B5·B7 | ax_core/washing |
| [Replit Tech Talks: December, 2024](https://www.youtube.com/watch?v=dtuwxIJrnS0) | Replit | 2025-01 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [Alex Hormozi’s New Playbook: Entrepreneurship in the Age of ](https://www.youtube.com/watch?v=6Ait5R-3-lI) | Replit | 2025-10 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [Inside Replit Agent with a lead AI engineer](https://www.youtube.com/watch?v=bJMriY-pqPE) | Replit | 2025-12 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Replit for Enterprise with Kody Low + Nick Co](https://www.youtube.com/watch?v=IP8SRLgqtWU) | Replit | 2026-05 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [Replit's President on Agents, Security and the Future of Wor](https://www.youtube.com/watch?v=8VAZkJWZvAw) | Replit | 2026-05 | 4 | B1·B4·B5·B8 | ax_core/washing |
| [The CRO Building Replit's Enterprise Machine | Ghazi Masood ](https://www.youtube.com/watch?v=PNBVzu4_G9c) | Replit | 2026-05 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [How NEC Is Becoming an AI-Native Enterprise with SAP, RISE w](https://www.youtube.com/watch?v=6utLfKSBIHg) | SAP | 2026-04 | 5 | B1·B2·B3·B4·B7 | ax_core/neutral |
| [Global Keynote: The Beginning of Better | SAP Sapphire Madri](https://www.youtube.com/watch?v=CocpyxAizwE) | SAP | 2026-05 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [The Future of Integration with SAP BTP | feat. Dr. Achim Kra](https://www.youtube.com/watch?v=ZzBZWAbinzE) | SAP | 2026-05 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Asset Management in SAP Cloud ERP | Expert Talk](https://www.youtube.com/watch?v=fyx68fY2be0) | SAP | 2026-06 | 5 | B1·B2·B3·B7·B8 | ax_core/neutral |
| [Is Your Leadership Ready for the AI Shift? | AI Voices, Epis](https://www.youtube.com/watch?v=rq5KpbaaZMY) | SAP | 2026-07 | 5 | B2·B3·B5·B6·B7 | ax_core/anti_washing |
| [What’s New in SAP HANA Cloud | Deep Dive with Product Expert](https://www.youtube.com/watch?v=QrGR38jGGZo) | SAP | 2026-07 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [[Analyst Interview | SK증권 한동희 위원] HBM 경쟁 심화 우려 속 SK하이닉스의 대응 ](https://www.youtube.com/watch?v=wQ67Mf4rRX4) | SK hynix | 2025-08 | 4 | B2·B5·B7·B8 | ax_adjacent/neutral |
| [Agentforce World Tour NYC | Main Keynote 2025 | Salesforce](https://www.youtube.com/watch?v=sSIB8rZTkew) | Salesforce | 2025-12 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Boost Advertising ROI: Data Cloud & Salesforce Platform Inte](https://www.youtube.com/watch?v=1eur1w4VfMQ) | Salesforce | 2026-02 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [Meet the new Slack. Where AI works.](https://www.youtube.com/watch?v=6DtrYEHRHw4) | Salesforce | 2026-04 | 5 | B1·B2·B4·B5·B8 | ax_core/washing |
| [Build the Future with Salesforce Headless 360 | TDX 2026 Key](https://www.youtube.com/watch?v=aKsZdyyzcfU) | Salesforce | 2026-04 | 4 | B1·B2·B4·B7 | ax_core/washing |
| [Introducing... the NEW Slack!](https://www.youtube.com/watch?v=vYUqOU-QV-o) | Salesforce | 2026-04 | 4 | B1·B4·B5·B7 | ax_core/washing |
| [Marc Benioff on Agentforce & the Future of AI Agents in Slac](https://www.youtube.com/watch?v=XY-s81fBXFU) | Salesforce | 2026-04 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Our Inside Perspective on Mission-Ready AI](https://www.youtube.com/watch?v=2lx6JDSPGoM) | Salesforce | 2026-04 | 4 | B1·B4·B5·B6 | ax_core/washing |
| [Welcome to Agentforce Demo Day!](https://www.youtube.com/watch?v=7a3TnSO0nps) | Salesforce | 2026-05 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [State of Service: How AI Agents are Delivering Results in Un](https://www.youtube.com/watch?v=H8A7Nu2KseI) | Salesforce | 2026-05 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [Dissecting the State of Marketing in 2026 | Salesforce](https://www.youtube.com/watch?v=rS5MfhB8RkY) | Salesforce | 2026-06 | 5 | B1·B2·B3·B5·B7 | ax_core/anti_washing |
| [Agentforce Marketing Keynote | Connections 2026](https://www.youtube.com/watch?v=9g-S56GGhN0) | Salesforce | 2026-06 | 4 | B1·B2·B3·B7 | ax_core/anti_washing |
| [Prefill vs Decode](https://www.youtube.com/watch?v=4w0M255awlE) | SambaNova | 2025-12 | 4 | B1·B4·B7·B8 | ax_core/neutral |
| [What Is a Model?](https://www.youtube.com/watch?v=Fcu-peZt0lM) | SambaNova | 2026-02 | 4 | B1·B4·B5·B8 | ax_core/neutral |
| [Scale AI |  Contrats et détention des droits | Pourquoi PI, ](https://www.youtube.com/watch?v=xhZsMRR9qAU) | Scale AI | 2022-08 | 4 | B2·B3·B4·B8 | ax_core/neutral |
| [Scale AI AI Playbook for Business Leaders | ALL IN 2024](https://www.youtube.com/watch?v=TPN6hbY40TU) | Scale AI | 2024-09 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Patents in AI: It's Time to Modernize Your Approach | Scale ](https://www.youtube.com/watch?v=4C67rUE96pM) | Scale AI | 2024-09 | 4 | B2·B4·B7·B8 | ax_core/washing |
| [Scale AI @ ALL IN 2025 | Back to the future of Canadian AI: ](https://www.youtube.com/watch?v=sXTycrc-b7Q) | Scale AI | 2025-10 | 4 | B1·B3·B4·B7 | ax_core/neutral |
| [Exploring DCIM and EcoStruxure IT Solutions](https://www.youtube.com/watch?v=jBVwPeRBC-I) | Schneider Electric | 2026-06 | 5 | B1·B3·B4·B5·B7 | ax_adjacent/neutral |
| [Chris Sharp & Steven Carlini: AI Factories: Power, Cooling &](https://www.youtube.com/watch?v=Vfj0etH-rD8) | Schneider Electric | 2026-06 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [Is there an ROI in industrial AI? The truth behind data, aut](https://www.youtube.com/watch?v=2cJD3hlyu6g) | Schneider Electric | 2026-07 | 5 | B1·B3·B5·B6·B7 | ax_core/anti_washing |
| [End of Islands - Unified Asset Lifecycle is the Digital Fabr](https://www.youtube.com/watch?v=xjFSF4jCvpk) | Schneider Electric | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Powering the AI factory - The grid-to-chip journey | Schneid](https://www.youtube.com/watch?v=lWYUvDXnudc) | Schneider Electric | 2026-07 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Enterprise AI Adoption: From Idea to Deployment](https://www.youtube.com/watch?v=xofWoVQ-ic4) | Sema4ai | 2026-07 | 5 | B1·B2·B4·B5·B6 | ax_core/anti_washing |
| [Michael Park's AI Whiteboard Masterclass](https://www.youtube.com/watch?v=0Fmw61s8CKc) | ServiceNow | 2025-09 | 5 | B1·B2·B4·B6·B7 | ax_core/anti_washing |
| [Introducing AI Experience by ServiceNow](https://www.youtube.com/watch?v=lrQylmrcbXs) | ServiceNow | 2025-10 | 4 | B1·B4·B5·B7 | ax_core/neutral |
| [Poisoning the Well: The Invisible Danger in Your AI Supply C](https://www.youtube.com/watch?v=CjHBPfPYuyg) | ServiceNow | 2026-01 | 4 | B1·B2·B4·B8 | ax_adjacent/anti_washing |
| [Die Zukunft der Industrie: CEOs von Siemens & Schaeffler übe](https://www.youtube.com/watch?v=jEvJOXlENOI) | Siemens | 2025-12 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Industrial AI in Practice: From Product Design to Factory Fl](https://www.youtube.com/watch?v=4boWnMQXZMw) | Siemens | 2026-01 | 5 | B1·B2·B4·B5·B7 | ax_core/washing |
| [The Industrial AI Revolution: Siemens Keynote at CES 2026](https://www.youtube.com/watch?v=R4Wm6YdoZSs) | Siemens | 2026-01 | 5 | B1·B2·B4·B5·B7 | ax_core/neutral |
| [Agentic AI: The Next Wave of Industrial AI | Analyst Insight](https://www.youtube.com/watch?v=Syk6BjIM6qE) | Siemens | 2026-01 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [How PepsiCo Uses Digital Twins & AI to Rethink Manufacturing](https://www.youtube.com/watch?v=YkTGMNQ9_FI) | Siemens | 2026-01 | 4 | B1·B3·B4·B5 | ax_core/neutral |
| [How Physical AI is Transforming Industries: AWS and Siemens ](https://www.youtube.com/watch?v=EfYVIaGQwts) | Siemens | 2026-02 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Roland Busch präsentiert Siemens Wachstumsstrategie und Indu](https://www.youtube.com/watch?v=BnLqYZQ2uCo) | Siemens | 2026-02 | 4 | B1·B2·B4·B7 | ax_core/washing |
| [Scaling Industrial AI from Months to Days, Siemens and AWS J](https://www.youtube.com/watch?v=356iStxtsoo) | Siemens | 2026-05 | 4 | B1·B2·B4·B7 | ax_core/neutral |
| [From Data to Value: Siemens Digital Enterprise for Consumer ](https://www.youtube.com/watch?v=W0UJXVK-Vhg) | Siemens | 2026-06 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [How to Scale Industrial AI in Real Factory Operations](https://www.youtube.com/watch?v=46KctH5TgSs) | Siemens | 2026-06 | 4 | B1·B4·B5·B6 | ax_core/anti_washing |
| [Physical AI, Digital Twins, and the Future of Factory Operat](https://www.youtube.com/watch?v=GAW048wxwGk) | Siemens | 2026-07 | 5 | B1·B2·B3·B4·B7 | ax_core/neutral |
| [AI-Based Process Control at Scale: Pringles and Siemens on D](https://www.youtube.com/watch?v=-B__O2eqRYc) | Siemens | 2026-07 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [Coca-Cola's Factory of the Future: Digital Twins and Industr](https://www.youtube.com/watch?v=CjVsewDPX3w) | Siemens | 2026-07 | 4 | B1·B3·B4·B5 | ax_adjacent/washing |
| [Cross-industry Collab: Driving Progress When Times Are Tough](https://www.youtube.com/watch?v=gjMutZzFLnA) | Snap | 2023-11 | 4 | B5·B6·B7·B8 | ax_adjacent/neutral |
| [Snap Ad Platform: Inside Our DR Improvements](https://www.youtube.com/watch?v=bSW2DcihnfI) | Snap | 2024-05 | 4 | B1·B4·B7·B8 | ax_adjacent/neutral |
| [Empowering Agility: DraftKings’ Strategy for Compliance and ](https://www.youtube.com/watch?v=F01IEeM3I-Y) | Snowflake | 2025-11 | 5 | B1·B2·B4·B5·B7 | ax_core/neutral |
| [Data Engineering from Ingestion to AI-Ready | BUILD 2025 Key](https://www.youtube.com/watch?v=XwCnOsZMhyI) | Snowflake | 2025-11 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [End Data Disparity | Looking Beyond Technology To Maximize D](https://www.youtube.com/watch?v=HehmwhyxX9Y) | Snowflake | 2025-11 | 4 | B2·B4·B5·B8 | ax_core/anti_washing |
| [From Analytics To Intelligence: BlackRock's Journey To Data ](https://www.youtube.com/watch?v=Me_H_-E6lSg) | Snowflake | 2025-11 | 4 | B1·B2·B3·B4 | ax_core/neutral |
| [The AI Blueprint for the Next Decade | BUILD 2025 Luminary C](https://www.youtube.com/watch?v=-HWNc-Hd90U) | Snowflake | 2025-11 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [AI And Real-World Data: A New Era For Identifying And Curing](https://www.youtube.com/watch?v=i9jLt1_iHK8) | Snowflake | 2025-12 | 4 | B2·B4·B7·B8 | ax_core/neutral |
| [End Data Disparity: Using Geospatial Data To Improve Cities](https://www.youtube.com/watch?v=YFTTMP6meVQ) | Snowflake | 2026-01 | 5 | B1·B2·B4·B7·B8 | ax_adjacent/anti_washing |
| [Snowflake Summit 2026 Opening Keynote With Sridhar Ramaswamy](https://www.youtube.com/watch?v=F34xlRoQ3eQ) | Snowflake | 2026-06 | 5 | B1·B3·B4·B5·B6 | ax_core/washing |
| [The 2026 Snowflake Startup Challenge Finale with Three Visio](https://www.youtube.com/watch?v=Nm9JhTrcREQ) | Snowflake | 2026-06 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Daikin Comfort: Building an AI-Ready Value Chain with SAP an](https://www.youtube.com/watch?v=0TyLwxQjk1g) | Snowflake | 2026-06 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [AI Transforms Health Care | Artificial Intelligence: The Fut](https://www.youtube.com/watch?v=wD1qn2i3Wb4) | Stanford Health Care | 2026-07 | 5 | B1·B2·B5·B7·B8 | ax_core/anti_washing |
| [Sigve Brekke and Kjerstin Braathen, CEO of DNB: Do banking a](https://www.youtube.com/watch?v=gDgq25NAbsg) | Telenor | 2021-06 | 4 | B1·B2·B4·B5 | ax_adjacent/anti_washing |
| [Telco Tech Talks: Modern technology's role in modern crises](https://www.youtube.com/watch?v=4rJPXX_M6Zo) | Telenor | 2022-11 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Why AI adoption fails – and how to get it right](https://www.youtube.com/watch?v=JBb2jRns3PA) | The CEO Magazine | 2026-07 | 5 | B1·B2·B5·B6·B8 | ax_core/anti_washing |
| [Enterprise AI Adoption in 2025: What Actually Works](https://www.youtube.com/watch?v=9MkMQ6zkjLw) | The Tech Trek | 2026-07 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [Unilever | Full Year 2023 Results | Webcast & Q&A](https://www.youtube.com/watch?v=YUdGwlJiDUk) | Unilever | 2024-02 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Unilever | H1 2024 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=Yc8FoPwlXxQ) | Unilever | 2024-07 | 4 | B2·B3·B4·B7 | ax_core/anti_washing |
| [Unilever Investor Event 2024 - Key takeaways](https://www.youtube.com/watch?v=NdZLX0ZfZi0) | Unilever | 2024-12 | 4 | B3·B4·B5·B7 | ax_core/neutral |
| [Unilever | H1 2025 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=_FqeVQgaPKM) | Unilever | 2025-07 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Unilever | H1 2025 | Results | Webcast & Q&A – audio-describ](https://www.youtube.com/watch?v=oMDBIXBEv3Q) | Unilever | 2025-10 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast & Q](https://www.youtube.com/watch?v=xWdZMbXzL-M) | Unilever | 2025-10 | 4 | B1·B3·B4·B7 | ax_core/neutral |
| [Unilever | Q3 2025 Trading Statement | Results | Webcast & Q](https://www.youtube.com/watch?v=X59yNoX8xQs) | Unilever | 2025-11 | 4 | B1·B3·B4·B7 | ax_core/neutral |
| [Fireside Chat with Fernando Fernandez, Unilever CEO and Celi](https://www.youtube.com/watch?v=djVmMTAMEho) | Unilever | 2025-12 | 4 | B2·B3·B5·B7 | ax_core/anti_washing |
| [Q4 and full-year 2025 results webcast and Q&A | Unilever](https://www.youtube.com/watch?v=G86AGZQwVVo) | Unilever | 2026-02 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Q4 and full-year 2025 results webcast and Q&A audio describe](https://www.youtube.com/watch?v=m7GUG2IHJZY) | Unilever | 2026-03 | 4 | B2·B4·B5·B7 | ax_core/anti_washing |
| [Unilever Foods to combine with McCormick | Webcast & Q&A](https://www.youtube.com/watch?v=MokfRDL0kqA) | Unilever | 2026-04 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Unilever | Q1 2026 Trading Statement | Results | Webcast & Q](https://www.youtube.com/watch?v=IlduIhb63aU) | Unilever | 2026-04 | 5 | B2·B3·B4·B5·B7 | ax_core/anti_washing |
| [Fernando and Warren Ackerman discuss Foods-McCormick combina](https://www.youtube.com/watch?v=NEQBDe8wSjk) | Unilever | 2026-04 | 4 | B2·B3·B5·B7 | ax_core/anti_washing |
| [Barclays Consumer Health Conference 2026](https://www.youtube.com/watch?v=oOyDsMsCmqI) | Unilever | 2026-06 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Deutsche Bank Global Consumer Conference 2026](https://www.youtube.com/watch?v=p0zFRz7jrQU) | Unilever | 2026-06 | 4 | B2·B3·B4·B7 | ax_core/anti_washing |
| [Unilever | Q2 & H1 2026 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=b_Db2XHcw18) | Unilever | 2026-07 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [KLUE Seminar](https://www.youtube.com/watch?v=3SUBLhZtJGk) | Upstage | 2021-08 | 4 | B1·B6·B7·B8 | ax_core/anti_washing |
| [Why Domain-Specific AI Wins in Underwriting: Amwins x Upstag](https://www.youtube.com/watch?v=997liHBHqW0) | Upstage | 2025-12 | 4 | B1·B2·B4·B7 | ax_core/anti_washing |
| [Core Computing](https://www.youtube.com/watch?v=8WyV487QG9Q) | Volvo Cars | 2021-07 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Self-Driven Women: Opportunities and challenges for women wo](https://www.youtube.com/watch?v=-x1c0URjbOE) | Waymo | 2020-08 | 4 | B1·B4·B5·B8 | ax_core/neutral |
| [#FTLive: Waymo CEO John Krafcik Keynote Interview](https://www.youtube.com/watch?v=TPve7x0GOT8) | Waymo | 2021-01 | 4 | B2·B4·B7·B8 | ax_core/anti_washing |
| [Self-Driven Women: Engineering the future of autonomy](https://www.youtube.com/watch?v=cvqGkq2SGWQ) | Waymo | 2021-11 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Instructor with Jason Liu - Weaviate Podcast #88!](https://www.youtube.com/watch?v=higlHgYDc5E) | Weaviate | 2024-02 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Zain and JP chat about: Vector embedding models for AI](https://www.youtube.com/watch?v=lpdN3aw-yTg) | Weaviate | 2024-04 | 4 | B1·B4·B7·B8 | ax_adjacent/neutral |
| [DSPy End-to-End: Meetup in San Francisco](https://www.youtube.com/watch?v=Y81DoFmt-2U) | Weaviate | 2024-05 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Guest Lecture: Vector Quantization Techniques with Etienne |](https://www.youtube.com/watch?v=0diVrgyQwXA) | Weaviate | 2024-05 | 4 | B1·B2·B7·B8 | ax_adjacent/neutral |
| [The Future of Search with Nils Reimers and Erika Cardenas - ](https://www.youtube.com/watch?v=DFqd34ikTH0) | Weaviate | 2024-06 | 4 | B1·B4·B7·B8 | ax_core/neutral |
| [AI-Native Development with Guy Podjarny and Bob van Luijt - ](https://www.youtube.com/watch?v=k6ZxYl2iI3k) | Weaviate | 2024-08 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [SWE-bench with John Yang and Carlos E. Jimenez - Weaviate Po](https://www.youtube.com/watch?v=8rwHAR4fsFg) | Weaviate | 2024-10 | 5 | B1·B2·B4·B7·B8 | ax_core/neutral |
| [Arctic Embed with Luke Merrick, Puxuan Yu, and Charles Piers](https://www.youtube.com/watch?v=Kjqv4uk3RCs) | Weaviate | 2024-12 | 5 | B1·B2·B5·B6·B7 | ax_adjacent/anti_washing |
| [Agent Experience with Matt Biilmann, Sebastian Witalec, and ](https://www.youtube.com/watch?v=MAE3I8O_w84) | Weaviate | 2025-02 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [Optimizing Retrieval Agents with Shirley Wu - Weaviate Podca](https://www.youtube.com/watch?v=4ZRhSuBHyNo) | Weaviate | 2025-02 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [Patronus AI with Anand Kannappan - Weaviate Podcast #122!](https://www.youtube.com/watch?v=I2jgU4waKFE) | Weaviate | 2025-05 | 5 | B1·B3·B4·B5·B8 | ax_core/anti_washing |
| [RAG Benchmarks with Nandan Thakur - Weaviate Podcast #124!](https://www.youtube.com/watch?v=x9zZ03XtAuY) | Weaviate | 2025-06 | 4 | B1·B2·B7·B8 | ax_adjacent/anti_washing |
| [Saurabh Mishra and Bob van Luijt on Weaviate and SAS - Weavi](https://www.youtube.com/watch?v=INKV21AaYjE) | Weaviate | 2025-10 | 5 | B1·B2·B3·B4·B8 | ax_core/anti_washing |
| [Multi-Vector Search with Amélie Chatelain and Antoine Chaffi](https://www.youtube.com/watch?v=44GC3E-WbHU) | Weaviate | 2026-03 | 4 | B1·B4·B6·B8 | ax_adjacent/anti_washing |
| [Booking.com and Weaviate with Başak Eskili - Weaviate Podcas](https://www.youtube.com/watch?v=O9edM9ZS_FQ) | Weaviate | 2026-05 | 5 | B1·B2·B4·B5·B8 | ax_core/anti_washing |
| [Founding Weaviate with Bob van Luijt and Etienne Dilocker - ](https://www.youtube.com/watch?v=pvv-vnT-LfQ) | Weaviate | 2026-07 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [Optimizing CI/CD model management and evaluation workflows](https://www.youtube.com/watch?v=Sw4M-b_GQZg) | Weights & Biases | 2024-10 | 5 | B1·B2·B5·B7·B8 | ax_core/anti_washing |
| [AI’s breakthrough in weather forecasting with Brightband’s J](https://www.youtube.com/watch?v=xFgaEPMqfi4) | Weights & Biases | 2024-11 | 5 | B1·B2·B3·B4·B7 | ax_core/anti_washing |
| [What’s the path to AGI? A conversation with Turing Co-founde](https://www.youtube.com/watch?v=DJS7cop0CCw) | Weights & Biases | 2024-11 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [How GenAI is powering the next generation of Mercari Marketp](https://www.youtube.com/watch?v=tEbLkgDCmzg) | Weights & Biases | 2024-11 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Unlocking the potential of MLOps and LLMOps](https://www.youtube.com/watch?v=7hxec4M48XY) | Weights & Biases | 2025-01 | 5 | B1·B4·B5·B7·B8 | ax_core/neutral |
| [Fine tuning Azure OpenAI Service Models with Weights & Biase](https://www.youtube.com/watch?v=2sfl0YqRODY) | Weights & Biases | 2025-01 | 4 | B1·B4·B5·B8 | ax_adjacent/anti_washing |
| [The rise of AI agents with João Moura of CrewAI](https://www.youtube.com/watch?v=Z2cy4CGfsbc) | Weights & Biases | 2025-02 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Mastering model customization: fine-tuning Azure OpenAI serv](https://www.youtube.com/watch?v=N1CI8Ld0-PA) | Weights & Biases | 2025-03 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [Measure and iterate on AI application performance using W&B ](https://www.youtube.com/watch?v=pxbNLZ9k9Bo) | Weights & Biases | 2025-04 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [Safeguard your users and brand with W&B Weave Guardrails](https://www.youtube.com/watch?v=KOwajQfIWC4) | Weights & Biases | 2025-04 | 4 | B1·B4·B7·B8 | ax_core/anti_washing |
| [From pharma to AGI hype, and developing AI in finance: Marti](https://www.youtube.com/watch?v=IzDEfkRFKmI) | Weights & Biases | 2025-05 | 5 | B1·B2·B3·B7·B8 | ax_core/anti_washing |
| [GitHub CEO Thomas Dohmke on Copilot and the Future of Softwa](https://www.youtube.com/watch?v=PPs5lZ2syv4) | Weights & Biases | 2025-06 | 5 | B1·B3·B4·B7·B8 | ax_core/anti_washing |
| [AI’s $600B Question: Scaling for what comes next](https://www.youtube.com/watch?v=DmfVlf1yHb4) | Weights & Biases | 2025-06 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [Building future-ready AI with agents & data flywheels: Insig](https://www.youtube.com/watch?v=innRr5Pleyg) | Weights & Biases | 2025-06 | 4 | B1·B2·B7·B8 | ax_adjacent/anti_washing |
| [Weights & Biases and CoreWeave: Fully Connected 2025 Keynote](https://www.youtube.com/watch?v=09Ubfrdq508) | Weights & Biases | 2025-06 | 4 | B1·B3·B4·B8 | ax_core/anti_washing |
| [Building agentic AI workflows with W&B Weave: a hiring assis](https://www.youtube.com/watch?v=tRGoT1QV8VA) | Weights & Biases | 2025-07 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [The AI that solves the market: A new era in forecasting with](https://www.youtube.com/watch?v=zbmXulPIJpo) | Weights & Biases | 2025-07 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [The future of multi-agents in enterprises](https://www.youtube.com/watch?v=GpbmI5NtuSQ) | Weights & Biases | 2025-07 | 4 | B1·B3·B4·B5 | ax_core/anti_washing |
| [Arvind Jain on building Glean and the future of enterprise A](https://www.youtube.com/watch?v=lYz5MQvK3wU) | Weights & Biases | 2025-08 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [Build and monitor multi-agent contact centers using Weights ](https://www.youtube.com/watch?v=MjqHVfmKEoM) | Weights & Biases | 2025-10 | 4 | B1·B2·B4·B8 | ax_core/neutral |
| [Defining factors for enterprise AI agents - JetBrains @ FC L](https://www.youtube.com/watch?v=igUpMlGqyWo) | Weights & Biases | 2025-12 | 5 | B1·B2·B5·B7·B8 | ax_core/anti_washing |
| [Fully Connected Tokyo 2025: Opening Keynote with W&B Cofound](https://www.youtube.com/watch?v=Uw2aEJ4CzwM) | Weights & Biases | 2025-12 | 4 | B1·B4·B7·B8 | ax_adjacent/anti_washing |
| [Atlassian’s Most Controversial Growth Decision | Mike Cannon](https://www.youtube.com/watch?v=S3RmvHfJll4) | Weights & Biases | 2026-01 | 5 | B1·B3·B5·B7·B8 | ax_core/anti_washing |
| [Fully Connected Tokyo: [Hands-on workshop] Automation of doc](https://www.youtube.com/watch?v=3VJZhKEG4ik) | Weights & Biases | 2026-01 | 4 | B1·B2·B3·B8 | ax_core/anti_washing |
| [Fully Connected Tokyo: [Hands-on workshop] From 0 to automat](https://www.youtube.com/watch?v=BX-AjQUUol8) | Weights & Biases | 2026-01 | 4 | B1·B5·B7·B8 | ax_adjacent/anti_washing |
| [Why Big Tech Buys GPUs From CoreWeave | Corey Sanders](https://www.youtube.com/watch?v=h3SNaAPUxHY) | Weights & Biases | 2026-01 | 4 | B1·B4·B5·B7 | ax_adjacent/washing |
| [She Raised $64M to Build an AI Math Prodigy | Carina Hong, C](https://www.youtube.com/watch?v=QxfsjDBDw3M) | Weights & Biases | 2026-02 | 4 | B1·B5·B6·B8 | ax_adjacent/anti_washing |
| [The $8.6B Self-Driving AI Backed by Nvidia and Uber | Alex K](https://www.youtube.com/watch?v=k5wgts8y-xU) | Weights & Biases | 2026-04 | 4 | B1·B2·B4·B8 | ax_core/anti_washing |
| [Curing Every Disease With Al by 2050 | Sam Rodriques, Edison](https://www.youtube.com/watch?v=Q7NpRG2gAxc) | Weights & Biases | 2026-05 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [AI Transformation AMA for HR Leaders](https://www.youtube.com/watch?v=lYOR4pgVdb0) | Zapier | 2025-09 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [How Zapier Runs AI Hack Week | Real Examples of AI Transform](https://www.youtube.com/watch?v=e1pk34c3oYU) | Zapier | 2025-09 | 5 | B1·B2·B4·B7·B8 | ax_core/anti_washing |
| [Build an AI First RevOps Team for MAXIMUM Impact](https://www.youtube.com/watch?v=4_vkQdMQ5xs) | Zapier | 2025-10 | 5 | B1·B2·B3·B5·B7 | ax_core/anti_washing |
| [From Zero to Millions in ARR: How AI-Powered Builders Are Sc](https://www.youtube.com/watch?v=rHyqHuZ93Z4) | Zapier | 2025-10 | 5 | B1·B2·B4·B6·B8 | ax_core/anti_washing |
| [Millions of Users and Billions of Files: Box CTO on Building](https://www.youtube.com/watch?v=B3E3qhTWSSg) | Zapier | 2025-10 | 5 | B1·B2·B3·B7·B8 | ax_core/washing |
| [What Netflix Knows About AI That Every Recruiter Should Lear](https://www.youtube.com/watch?v=edY-3X18CHc) | Zapier | 2025-10 | 5 | B1·B2·B5·B6·B7 | ax_core/washing |
| [She Built 1Mind — The AI That’s Outselling Humans | Agents o](https://www.youtube.com/watch?v=jKQ7yhlgcKI) | Zapier | 2025-10 | 4 | B1·B3·B5·B7 | ax_core/anti_washing |
| [The $50M Pricing Gamble and Intercom's AI Reinvention | Agen](https://www.youtube.com/watch?v=qMVhi485d8s) | Zapier | 2025-10 | 4 | B1·B4·B5·B8 | ax_core/anti_washing |
| [The New Creative Muse: Leveraging AI in Design, Writing, and](https://www.youtube.com/watch?v=-VG_jT-aVtc) | Zapier | 2025-11 | 5 | B1·B3·B4·B7·B8 | ax_core/anti_washing |
| [Zapier's Big AI Plans for 2026 Revealed! - Leadership, Cultu](https://www.youtube.com/watch?v=EfHm1Qjztd0) | Zapier | 2025-11 | 5 | B1·B3·B5·B6·B7 | ax_core/anti_washing |
| [How Executive Assistants Drive Strategic Impact with AI](https://www.youtube.com/watch?v=-gGwrSPc3tA) | Zapier | 2025-11 | 4 | B1·B3·B5·B7 | ax_core/anti_washing |
| [How Orium’s AI Playbook Turned Complexity into 5x Growth | A](https://www.youtube.com/watch?v=5st7XEHY_pA) | Zapier | 2025-11 | 4 | B1·B2·B4·B5 | ax_core/anti_washing |
| [Defining AI Fluency: A Fireside Chat With The Executives](https://www.youtube.com/watch?v=Rq1lzDDfTrU) | Zapier | 2025-12 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [2026 SEO Strategy: How Marketers Win The New LLM Search Game](https://www.youtube.com/watch?v=BV_ZtkqyzkM) | Zapier | 2025-12 | 4 | B1·B2·B5·B7 | ax_core/neutral |
| [From First Startup to AI-Powered Scale: Wes Schroll on Build](https://www.youtube.com/watch?v=HxortsDnCm8) | Zapier | 2026-01 | 5 | B1·B2·B4·B5·B7 | ax_core/anti_washing |
| [Is SaaS really dead? Dharmesh Shah from HubSpot on AI, Vibe-](https://www.youtube.com/watch?v=R5MKxU5biPo) | Zapier | 2026-02 | 4 | B1·B2·B5·B8 | ax_adjacent/anti_washing |
| [Getting back to startup speed took a cultural reset - and it](https://www.youtube.com/watch?v=LHd1plfMvXA) | Zapier | 2026-03 | 5 | B1·B2·B3·B5·B7 | ax_core/neutral |
| [Leading through AI: How top executives are turning AI mandat](https://www.youtube.com/watch?v=g6q02hUd_Wc) | Zapier | 2026-03 | 5 | B1·B2·B3·B5·B7 | ax_core/washing |
| [No Lanes: How Claire Vo Runs an AI-Native Company on Her Own](https://www.youtube.com/watch?v=_Wg2oTfwb4g) | Zapier | 2026-03 | 4 | B1·B3·B5·B7 | ax_core/neutral |
| [OpenClaw, Claude, Zapier MCP: Build Agents Safely & Easily |](https://www.youtube.com/watch?v=WPwXCwlTdz4) | Zapier | 2026-03 | 4 | B1·B2·B5·B8 | ax_core/anti_washing |
| [How Miro's talent team designs & ships HR systems employees ](https://www.youtube.com/watch?v=NuSnxrdODUE) | Zapier | 2026-04 | 5 | B1·B2·B3·B5·B8 | ax_core/anti_washing |
| [Guru's Rick Nucci on Building AI Your Team Can Trust](https://www.youtube.com/watch?v=YaSvETxH2jY) | Zapier | 2026-05 | 4 | B1·B3·B4·B7 | ax_core/anti_washing |
| [Brand Is Back: Guy Yalif on Marketing in the Agent Era](https://www.youtube.com/watch?v=tw8cpXGg41I) | Zapier | 2026-06 | 5 | B1·B3·B4·B5·B7 | ax_core/washing |
| [Eric Ries on Vibe Coding and Building Incorruptible Companie](https://www.youtube.com/watch?v=Qs33r-Nreb8) | Zapier | 2026-06 | 5 | B1·B3·B4·B5·B7 | ax_core/anti_washing |
| [Claude /connected: Share skills with your team | Build-Along](https://www.youtube.com/watch?v=xTmn8jcnzdM) | Zapier | 2026-07 | 4 | B1·B2·B3·B5 | ax_core/neutral |
| [Gong's Amit Bendov on Powering Your Company Brain](https://www.youtube.com/watch?v=YEbksTLOfjs) | Zapier | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/washing |
| [The Good, the Bad, and the Ugly: How Zapier Is Building an A](https://www.youtube.com/watch?v=tqnLffBM-og) | Zapier | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [10 Years of Zoox. Reflections and Predictions.](https://www.youtube.com/watch?v=DYcujjMs3Uo) | Zoox | 2024-07 | 4 | B1·B3·B5·B7 | ax_core/anti_washing |
| [Aaron Levie on AI Adoption and Enterprise Workflows | The a1](https://www.youtube.com/watch?v=dvVbA9OcBqs) | a16z and MTS | 2026-07 | 5 | B1·B3·B5·B7·B8 | ax_core/neutral |
| [[ifkakao2021] Daum Mail Terraforming:  다음 메일 백엔드 ](https://www.youtube.com/watch?v=r2t4h3qMXzw) | kakao tech | 2026-06 | 4 | B1·B4·B6·B8 | ax_core/neutral |
| [[ifkakao2021] Knowledge Graph for Enterprise](https://www.youtube.com/watch?v=fMV_TRN5StI) | kakao tech | 2026-06 | 4 | B1·B2·B5·B6 | ax_core/neutral |
| [상위 1%만 알고 있는 AI 활용법, 삶의 질이 10배 상승합니다 (김상윤 교수)](https://www.youtube.com/watch?v=AsQUoda0wB0) | 김작가 TV | 2026-08 | 4 | B1·B5·B7·B8 | ax_core/anti_washing |
| [AI 랠리 2라운드…승부는 실적ㅣ스페이스X 첫 실적 발표…머스크 뭐라고 말할까ㅣ트럼프 "일본 돕겠다"…엔화 ](https://www.youtube.com/watch?v=FvQF06brkAQ) | 매경 월가월부 | 2026-08 | 4 | B1·B3·B5·B7 | ax_adjacent/neutral |
| [The Secret to Successful AI Transition: A Step-by-Step AX St](https://www.youtube.com/watch?v=wdqRyiqH_OI) | 메타코드M | 2026-07 | 4 | B3·B5·B6·B7 | ax_core/anti_washing |
| [Only 2 employees left, yet... The shocking sign of Google's ](https://www.youtube.com/watch?v=syU5o1-BPUI) | 백만사전 | 2026-07 | 5 | B1·B2·B3·B4·B5 | ax_core/washing |
| [[AX Summit] 2. (키노트)AI Native 기업으로의 전환 방안과 사례(AX센터 AI사업팀장 신계](https://www.youtube.com/watch?v=PsfnMJwSoXs) | 삼성SDS AX | 2026-07 | 5 | B1·B2·B3·B4·B7 | ax_core/anti_washing |
| [AI-Native 기업으로 전환 전략과 사례](https://www.youtube.com/watch?v=Y-ApGj-9ceI) | 삼성SDS AX | 2026-07 | 4 | B1·B2·B7·B8 | ax_core/anti_washing |
| [제조업 AX의 골든 타임 ⏰ 중요한 것은 AI 도입보다 이것?! 📢 IT슈다 EP. 제조](https://www.youtube.com/watch?v=iAbE9YXnbqA) | 삼성SDS and KASMO 인공지능혁신추진 | 2026-07 | 5 | B1·B2·B4·B5·B6 | ax_core/anti_washing |
| [Breaking Down Google's Earnings: They're Scaling Up Investme](https://www.youtube.com/watch?v=CpKLKwscstc) | 손에잡히는경제 | 2026-07 | 4 | B1·B2·B3·B7 | ax_core/anti_washing |
| [Why Companies Are in Trouble After Relying on AI for Layoffs](https://www.youtube.com/watch?v=4-lOvLaVWSA) | 손에잡히는경제 | 2026-08 | 5 | B1·B3·B5·B7·B8 | ax_core/neutral |
| [지금 세계에서 AI 제일 잘 쓰는 기업들의 공통점ㅣ지식인초대석 EP.78 (장진석 파트너)](https://www.youtube.com/watch?v=3FW8c5T7fik) | 지식인사이드 | 2026-07 | 5 | B1·B2·B3·B4·B7 | ax_core/anti_washing |
| [💡 AX란 무엇인가? 직접 해본 스타트업 대표가 알려주는 AI 전환의 모든 것 | EP.2 Vibers.AI](https://www.youtube.com/watch?v=cRfy_RXX5WA) | 카카오벤처스 Kakao Ventures | 2026-07 | 4 | B4·B5·B6·B8 | ax_core/washing |
| [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 티타임즈TV | 2026-07 | 5 | B1·B2·B5·B6·B8 | ax_core/anti_washing |
| [AI 도입, 도입만 하면 끝일까? (김유신 상무)](https://www.youtube.com/watch?v=GiFlOiikYso) | 티타임즈TV | 2026-07 | 4 | B1·B2·B5·B7 | ax_core/anti_washing |
| [AI 에이전트 도입하려면 꼭 알아야 할 것 (이주환 스윗테크놀러지스 대표)](https://www.youtube.com/watch?v=7S5y1rwxIrw) | 티타임즈TV | 2026-08 | 4 | B1·B2·B4·B8 | ax_core/neutral |

</details>

