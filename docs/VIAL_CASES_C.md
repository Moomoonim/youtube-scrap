# Vial(2019) 프레임워크 사례 상세 — 티어 C(부분 사례)

> 자동 생성: `python vial_dossiers.py` · 근거 문헌: Vial, G. (2019). Understanding digital transformation: A review and a research agenda. *JSIS, 28*(2), 118–144.

> 8블록 중 4~5개만 성립한 부분 사례. 단일 구성요소 분석·보조 표본용. **총 484건**. 사례 선정·티어 기준은 `docs/VIAL_CASES.md` §1 참조.

> 근거 문장은 자동 자막 원문 발췌라 오탈자·오역이 있을 수 있다(대리지표로만 사용).


---

## AI Engineer


**1. [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA)** — AI Engineer · (미분류) · — · 2026-08 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: [음악] 좋아요. 네, 제 세션에 참여해 주셔서 감사합니다 . [박수] 고맙습니다. 안녕하세요, 저는 샌디예요. 네, 저는 데이터 브릭스에서 데이터 및 AI 분야의 기술 리더를 맡고 있습니다. 음, Databricks에 입사하기 전에는 Amazon Web Services에서 5년 동안 데이터 및 AI 담당 수석 아키텍트로 근무했습니다 . 음, 지난 몇 년 동안 저는 분산 시스템과 기술을 사용…
- B1 디지털·AI 기술의 활용: 그러니까, 일단 클라우드 스토리지에 원시 데이터를 저장하면, 그 데이터는 Delta Lake 레이어라는 계층을 거치게 되는데, 이 계층은 기본적으로 원시 데이터 위에 데이터베이스와 유사한 속성을 추가합니다.
- B8 부정 성과: 보안·프라이버시: 저희 사례에서, 앞서 언급했던 고객사와 진행했던 작업에서는 이 보안 계층을 적용하여 테스트 단계에서 이미 47건의 개인정보 유출 사례를 탐지했습니다.
- 수치 주장: 그리고 그때, 그러니까, 이게 바로 출시 6주 후의 결과입니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 에이전트 프레임워크 · 거버넌스·평가 도구
- 원문: `transcripts/2026-08-03/The_Production_AI_Playbook_Deploying_Agents_at_Enterprise_Sc__ObTPqBGsEbA.md`

---

## AI 겸임교수 이종범


**2. [오픈AI x 무신사 비공개 행사 후기, 코덱스 기업 도입 사례와 AI 네이티브 워크플로우 인사이트 총정리](https://www.youtube.com/watch?v=jYwDdt_3L8Q)** — AI 겸임교수 이종범 · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B6 장벽 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B7 긍정 성과
- 개요: 안녕하세요. AI 겸민교수 이종보입니다. 어, 제가 얼마 전에 오픈 AI에서 초청을 받아서 무신사회에 다녀온 적이 있습니다.이 무신사의 코덱스를 활용해서 AI 네이티브 워크플로우를 어떻게 구축하고 있는지에 대해서 어, CTO분이 직접 나와서 이야기해 주는 거를 듣고 왔는데요. 굉장히 인사이트도 많았고 또 여러분들과 나누고 싶은 이야기도 있어서 오늘이 영상을 찍게 됐습니다. 어, 그 현장에서 …
- B5 리더십·CDO/CAIO: 이 CTO 님의 직속 직원이 있는데 이제 그분이 어 이거 그러면 필요한 것만 일단 만들어 볼까요라고 해 가지고 비발자 매니저가 기획을 하고 개발자 세 명이 이제 바이브 코딩을 해 가지고이 두 달 만에 이런 핵심 비즈니스 로직을 완성하고 유지보수 내제화하고 구독 비용도 거의 제제로죠.
- B1 디지털·AI 기술의 활용: 그래서 결국에 이제 기술이 아니라 일하는 방식이 트랜스포메이션 돼야 된다라고 하면서 AI 에이전트의 도입은 단순히 더 좋은 소프트웨어를 사는게 아니라 어 조직이 상상하고 기획하고 실행하는 모든 방식의 근본적인 아키텍처를 재설계해야 된다라고 하는데요.
- 수치 주장: 그래서 처음에 무신사도 AI를 이렇게 도입을 했을 때 어 요걸로 뭔가 업무 효율화를 많이 이룰 수 있지 않을까라고 생각을 했지만 어 실제로 초기에 도입을 했을 때에는 어 코드 짜는 속도가 굉장히 빨랐지만은 마지막에이 완성을 하는 그 10% 어 요기를 이제 완벽하게 해내지 못했기 때문에 사람이 투입될 수밖에 없었고 이런 10%의 세밀한 UI 조정이나 예외 처리 이런 것들을 위해서 AI한테 계속 뭐 20번 넘게 이렇게 프롬프트를 수정하는 그런 과정에서 어 굉장한 필…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/2026-07-23/오픈AI_x_무신사_비공개_행사_후기,_코덱스_기업_도입_사례와_AI_네이티브_워크플로우_인사이트_총정리__jYwDdt_3L8Q.md`

---

## AMD


**3. [AI in Chip Design: S3E1](https://www.youtube.com/watch?v=fj1iRitQL4s)** — AMD · 인프라·칩·전력 · US · 2026-03 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: Welcome to Advanced Insights, where we provide just what the show name suggests, advanced insights into some of the most exciting trends and topics in technology. For this opening episode, season three, it should be no s…
- B1 디지털·AI 기술의 활용: You know, everyone points to, uh, you know, late 2022, when ChatGPT and generative AI really took hold and this massive adoption curve.
- B5 조직구조 변화: So how can these agentic flows help us work cross silos, because typically it's already been complex, and so it's been subdivided with teams, and they're sort of handoff.
- 교량: — · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/AMD/AI_in_Chip_Design_S3E1__fj1iRitQL4s.md`

**4. [AI and Trust at Scale: S3 E3](https://www.youtube.com/watch?v=WOXtvwYq-7o)** — AMD · 인프라·칩·전력 · US · 2026-06 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Welcome to Advanced Insight, where we provide just what the show name suggests, advanced insights in some of the most exciting trends and topics in technology. In this episode, I'm joined by Kathy Pham, computer scientis…
- B1 디지털·AI 기술의 활용: Um, like leaning into helping understand what the tools that we have can do, ranging from, like, complicated agentic systems to just, like, simple chatbots.
- B8 부정 성과: 보안·프라이버시: I know we've talked about this, Mark, and you've worked on some of these, like, and, like, open standards that we all just kind of follow on what we believe, like, security and privacy are.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/AMD/AI_and_Trust_at_Scale_S3_E3__WOXtvwYq-7o.md`

**5. [Agentic AI and the Future of Software Development: S3 E4](https://www.youtube.com/watch?v=eQ6tb7j3Z2U)** — AMD · 인프라·칩·전력 · US · 2026-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: Welcome to Advanced Insights, where we provide just what the show name suggests, Advanced Insights and some of the most exciting trends and topics in technology. On this episode, I'm joined by Boris Churney. He's the cre…
- B1 디지털·AI 기술의 활용: We, you know, like they did this like one line autocomplete and we had agentic workflows, always what we called agentic workflows, but it was essentially these deterministic systems where a step at a time might call out to an LLM to do some bit of computation,…
- B4 민첩성·양손잡이: And lastly, when thinking about return on investment, don't just focus on the investment, focus on the return, the freedom of experimentation that provides will be what comes up with the biggest wins.
- 수치 주장: And you know, my role at Anthropic is to 01:03:17,752 --&gt; 01:03:19,587 build the tools that let people experience the models, so they can understand where this thing is headed.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/AMD/Agentic_AI_and_the_Future_of_Software_Development_S3_E4__eQ6tb7j3Z2U.md`

---

## AWS Developers


**6. [Building with Open Source at AWS & What's Next for Developers](https://www.youtube.com/watch?v=YduNJIcdRA8)** — AWS Developers · 에이전트·개발도구 · US · 2024-11 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 오픈 소스는 오랫동안 혁신의 중심에 있었고, 생성형 AI와 같은 새로운 기술의 등장과 함께 현재 우리가 나누고 있는 논의에서도 여전히 매우 중요한 역할을 하고 있습니다. 저는 뉴스 스택의 설립자이자 발행인인 알렉스 윌리엄스입니다. 오늘 저는 아마존 웹 서비스의 개발자 경험 부사장인 아담 셀먼과 함께 이 자리에 섰습니다. 아담, 만나서 반갑습니다. 알렉스, 저도 반갑습니다. 제가 오늘 이 자리…
- B1 디지털·AI 기술의 활용: 생성형 AI, 그리고 생성형 AI뿐만 아니라 머신러닝에 많이 사용되는 AI는 소프트웨어 엔지니어들이 조직 내에서 수행하는 다양한 업무, 예를 들어 애플리케이션 개발, 배포, 관리 등에 어떤 영향을 미치고 있을까요?
- B4 가치네트워크·생태계: 저희 또는 파트너사의 관리 서비스를 이용하시면서, AWS와 같은 안정적인 클라우드 인프라 플랫폼, 보안, 운영 등 기대하시는 글로벌 인프라를 기반으로 혁신적인 오픈 소스 기능을 사용자 또는 애플리케이션의 일부로 제공할 수 있도록 지원하는 것이 목표입니다.
- 수치 주장: 지난 10~20년 동안 클라우드 네이티브 기술과 같은 기술이 등장하면서 다양한 요소들을 통합할 수 있게 되었습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/AWS_Developers/Building_with_Open_Source_at_AWS_&_What's_Next_for_Developer__YduNJIcdRA8.md`

---

## AWS Events


**7. [AWS Summit Mumbai 2026 Keynote | AWS Events](https://www.youtube.com/watch?v=0x_Q0wNux_U)** — AWS Events · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B8 부정 성과
- 개요: 아침. 멋진. 올해 더욱 크고, 더욱 훌륭하고, 더욱 대담한 정상회담이 될 것으로 기대되는 이번 행사를 위해 뭄바이에 다시 오게 되어 기쁩니다 . 그리고 그 이유를 아시나요? 올해는 인도가 주도권을 잡는 것이 핵심이기 때문입니다. 이 점을 명확히 보여주는 두 가지 사례를 공유하면서 시작하겠습니다. 이것을 상상해 보세요. 두 개의 인공위성이 시속 28,800km의 속도로 궤도를 돌고 있다 . …
- B1 디지털·AI 기술의 활용: 오늘 AWS 서밋에서 클라우드 생성형 AI 인텔리전스 시스템에 대한 대화를 들으면서 문득 한 가지 생각이 떠올랐습니다.
- B2 파괴: 데이터 가용성: 이전에는 관리자들이 파이프라인 데이터를 수집하고 거래 위험을 파악하고 검토를 준비하는 데 최대 5시간이 걸렸지만, 이제는 크레딧을 사용하면 몇 분 만에 완료할 수 있습니다.
- 수치 주장: 지난 12개월 동안 저는 파트너사, 고객사, 개발사 등 다양한 분야의 건설 관계자들을 만날 수 있는 놀라운 기회를 가졌습니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/AWS_Events/AWS_Summit_Mumbai_2026_Keynote_AWS_Events__0x_Q0wNux_U.md`

**8. [A leader's guide to data strategy in the era of agentic AI | AWS Events](https://www.youtube.com/watch?v=3XyNPfWWxiQ)** — AWS Events · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 감사합니다. 그리고 안녕하세요, 여러분! AWS 서밋 시드니 임원 포럼에 오신 것을 환영합니다 . 저희와 함께 시간을 내주셔서 정말 감사합니다 . 다룰 내용이 많으니 바로 시작하겠습니다 . 데이터 분석은 우리의 많은 노력에 있어 기본이 되기 때문에 , 거기서부터 시작하는 것이 옳다고 생각합니다 . 보시다시피 많은 조직들이 유전적 AI를 도입하는 데 있어 엄청난 장벽에 직면합니다. 이번 세션에…
- B1 디지털·AI 기술의 활용: 빅데이터 시대에 맞춰 데이터 레이크를 많이 구축했습니다.
- B5 조직구조 변화: 그림자 데이터 팀이 존재한다는 것은 중앙 집중식 전략이 너무 제한적이라는 것을 의미합니다.
- 수치 주장: 대신, 우리에게 필요한 것은 수천 명의 비즈니스 전문가들이 그러한 에이전트를 구축할 수 있도록 지원하는 것입니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 검색·RAG · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/AWS_Events/A_leader's_guide_to_data_strategy_in_the_era_of_agentic_AI_A__3XyNPfWWxiQ.md`

**9. [A leader’s guide to advanced team structures in an agentic world | AWS Events](https://www.youtube.com/watch?v=O7u6myBRsns)** — AWS Events · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B6 장벽 · 빠짐: B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요, 좋은 오후입니다. 오늘 오후에 여러분과 함께할 수 있게 되어 진심으로 영광입니다. 제 이름은 스티븐 브로비치입니다. 음, 저는 1999년 8월에 아마존에 입사했으니 거의 27년 전이네요. 그동안 세상은 많이 변했죠. 저는 경력의 전반부는 기술 분야에서 보냈지만 , 후반부는 사람과 문화에 집중해 왔습니다. 조직 문화가 기술적인 측면 외에도 조직의 성공을 좌우하는 주요 요인 중 하나…
- B1 디지털·AI 기술의 활용: AI 에이전트를 핵심 플랫폼 구성 요소로 포함하는 모델 B 임베디드 포드 와 공유 인프라를 제공하는 플랫폼이 추가된 모델 C 포드 중에서 선택하십시오 .
- B5 직무·역량 변화: 따라서 새로운 시대에 인재를 채용할 때는, 그리고 이것이 중요한데, 그 해의 업무 체계가 아니라 이 일곱 가지 자질을 기준으로 채용해야 합니다.
- 수치 주장: 2022년 채팅 GPT 출시 이후 가장 취약한 직종 종사자들의 실업률이 체계적으로 증가하지는 않았습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/AWS_Events/A_leader’s_guide_to_advanced_team_structures_in_an_agentic_w__O7u6myBRsns.md`

**10. [CCW 2026: AI Can't Personalize What It Can't See: Turning Scattered Data into Anticipatory CX](https://www.youtube.com/watch?v=53A20B6Ras8)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 멋진 목요일 아침에 와주셔서 감사합니다. 오늘 많은 분들이 어느 시점에 떠날 계획을 세우고 계실 텐데, 이렇게 시간을 내어 들러주셔서 감사합니다. 어, 케빈 마는 아마존 커넥트의 디렉터입니다. 저와 함께 아르차 씨가 참석했습니다. 오늘은 데이터에 대해 이야기해 보겠습니다. 음, 아마 제가 가장 좋아하는 이야기 주제일 거예요 . 음, 그리고 이건 정말 진심이에요, 농담이 아니라요. 제가 왜 이…
- B1 디지털·AI 기술의 활용: 그래서 아마존 커넥트 고객 프로필이 브라우저를 통한 첫 번째 상호 작용을 통해 수집한 모든 정보는 이제 커넥트 AI 에이전트에서도 사용할 수 있으며, 이를 통해 에이전트는 메리가 프로필에 원하는 다양한 기능과 추천 사항을 살펴볼 수 있습니다.
- B4 디지털 채널: 그리고 저는 컨택센터 의 엄격한 관리 체계와 측정 방식을 업무량 에 적용하는 것이 그 어느 때보다 더 가능해졌다고 생각합니다 .
- 수치 주장: 저는 거의 10년 동안 아마존 커넥트를 개발해 왔습니다 .
- 교량: — · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/AWS_Events/CCW_2026_AI_Can't_Personalize_What_It_Can't_See_Turning_Scat__53A20B6Ras8.md`

**11. [CCW 2026: Be the 5%: What We Learned Shipping AI at Amazon Scale](https://www.youtube.com/watch?v=Sww2jYuqk7w)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 여러분 모두를 만날 수 있게 되어 정말 기쁩니다 . 음, 저희 프레젠테이션을 진행하시면 저와 앙드레에 대해 조금씩 알게 되실 겁니다 . 하지만 저희가 콘텐츠를 진행하면서 기대치를 명확히 하고 싶은 한 가지는, 저희 둘 다 에이전트 기반 경험이 컨택 센터의 고객 경험을 어떻게 혁신할 수 있는지에 대해 매우 열정적이라는 점입니다. 하지만 저희는 이 콘텐츠를 제작할 때 판매 홍보처럼 보이지 않도록…
- B2 파괴: 소비자 행동·기대: 요약하자면, 어려운 부분은 여러모로 실패를 거듭하며 이 모든 것을 종합하는 데 어려움을 겪었지만, 무엇보다 중요한 것은, 특히 최종 사용자 고객 경험을 고려할 때, 많은 분들이 셀프 서비스에 대해 생각하고 계실 텐데, 어떻게 사용자를 교육하고 이러한 경험을 매우 쉽게 이해할 수 있도록 만들 것인지 고민해야 한다는 것입니다.
- B1 디지털·AI 기술의 활용: 그리고 우리가 이 점을 인공지능이라는 주제에 적용해 본다면, 핵심은 LLM, 음성- 텍스트 변환, 모델 등 그 어떤 것을 사용하든 상관 없이, 문제점을 이해하고 이상적인 고객 경험을 파악하는 것에서 시작한다는 것입니다.
- 수치 주장: 인공지능을 도입하는 기업 중 실제로 운영 단계에 있거나 성공을 거두고 있는 기업은 약 5%에 불과합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/AWS_Events/CCW_2026_Be_the_5%_What_We_Learned_Shipping_AI_at_Amazon_Sca__Sww2jYuqk7w.md`

**12. [CCW 2026: Dominion Energy’s AI-Powered Transformation with Amazon Connect Customer](https://www.youtube.com/watch?v=d2nUemwh30c)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 시간 맞춰 와주셔서 감사합니다. 소리가 너무 크거나 음질이 좋지 않으면 말씀해 주세요. 바로 조정하겠습니다. 네, 시간 내주셔서 정말 감사합니다 . 오늘은 빠르게 변화하고 있는 것에 대해 이야기해 보겠습니다. 아마 들어보셨을 거예요 . 오늘은 인공 지능(AI)과 그것이 고객 경험을 어떻게 변화시키고 있는지에 대해 이야기해 보겠습니다 . 이론상으로는 불가능하지만, 대규모 생산에서는 가능합니다.…
- B2 파괴: 소비자 행동·기대: 필터와 시각화 기능을 통해 고객 경험 지표, 상담원 성과, 감정 분석, 통화 요약 등 각 연락처에 대한 자세한 정보를 확인할 수 있습니다 .
- B4 디지털 채널: 아시다시피, 저는 지난 25 년 동안 전화 문의를 줄이고, 통화량을 최소화하고, 사람들이 셀프 서비스를 이용하도록 유도하기 위해 가능한 모든 노력을 기울여 왔습니다.
- 수치 주장: 하지만 저희는 미국과 협력하여 2024년에 커넥트 플랫폼 자체를 먼저 출시했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/AWS_Events/CCW_2026_Dominion_Energy’s_AI-Powered_Transformation_with_Am__d2nUemwh30c.md`

**13. [CCW 2026: How Citizens Bank is building the AI-native customer experience](https://www.youtube.com/watch?v=O_Imo9L04mo)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 네, 모두 환영합니다. 오늘 함께해 주셔서 감사합니다. 제 이름은 짐 크라이들러입니다. 저는 아마존 커넥트 서비스 팀의 제품 관리자로서 셀프 서비스 기능에 집중하고 있으며, AWS에서 약 8년 동안 근무했습니다 . 오늘 이렇게 여러분과 함께 이 분야에서 새롭게 출시될 제품들에 대해 이야기 나눌 수 있게 되어 정말 기쁩니다. 물론 셀프 서비스, 음성 AI는 오늘날 기술 발전과 함께 매우 흥미로…
- B4 디지털 채널: 이를 통해 처음부터 , 즉 셀프 서비스 환경에서 결정론적 워크플로 또는 AI 에이전트와 대화하는 순간부터 통화 후 작업 이나 설문 조사를 통해 고객 피드백을 수집하는 마지막 단계까지 전체 경험을 처음부터 끝까지 파악하고 , 이를 바탕으로 추론하여 지속적으로 개선하고 발전시킬 수 있습니다.
- B1 디지털·AI 기술의 활용: 저건 LLM 기반의 AI 에이전트인데, 고객이 하는 말을 이해하고 은행 자체 문서에서 가져온 정확하고 승인된 답변을 제공하기 위해 지식 기반에 대한 도구 호출을 수행하는 겁니다.
- 수치 주장: 그래서 지난 8개월에서 12개월 동안 우리가 목격한 가장 큰 변화 중 하나는 고객들이 이 기술을 시험적으로 사용하는 단계를 넘어, 고객 경험, 특히 셀프 서비스에 최신 AI 기술을 적용하는 것에 대해 이해하기 시작했다는 점입니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/AWS_Events/CCW_2026_How_Citizens_Bank_is_building_the_AI-native_custome__O_Imo9L04mo.md`

**14. [NYC Executive Forum 2026 - A Fireside Chat with Swami Sivasubramanian](https://www.youtube.com/watch?v=CHtc71MVpdo)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B6 장벽 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B8 부정 성과
- 개요: [음악] AWS의 유전 AI 부문 부사장이신 스와미 시바수 브라마니안 박사님을 환영해 주십시오. [음악] [박수] 여러분, 함께해 주셔서 감사합니다. 앞서 말씀드렸듯이 제 이름은 질 페리스 이고 AWS 지원 부문 부사장입니다 . 저희는 지난 18개월에서 24개월 동안 생성형 AI를 저희 계획과 인력에 도입하는 매우 흥미로운 여정을 거쳐 왔으며, 스와미와 그의 팀이 개발 중인 많은 기술을 활용…
- B7 성과: 운영효율: 하지만 올해 가장 생산적인 성과를 낸 팀, 심지어 여러분의 팀 내에서도 AI에 매우 능숙하고 생산성이 10배에서 20배까지 향상된 사람들의 실제 지출액은 그렇게 높지 않았습니다.
- B1 디지털·AI 기술의 활용: 이 예시에서 제가 방금 말씀드린 것처럼, 데이터 레이크에서 컨텍스트를 가져오고, Salesforce에서 컨텍스트를 가져오고, 브리핑 문서가 있는 SharePoint에서 컨텍스트를 가져온 다음, 담당자를 거쳐 계획과 이유를 결합하여 PowerPoint 프레젠테이션을 생성합니다.
- 수치 주장: 저희는 지난 18개월에서 24개월 동안 생성형 AI를 저희 계획과 인력에 도입하는 매우 흥미로운 여정을 거쳐 왔으며, 스와미와 그의 팀이 개발 중인 많은 기술을 활용해 왔습니다.
- 교량: — · 기술: LLM 모델 · 코딩 에이전트 · 온톨로지·데이터계층
- 원문: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_A_Fireside_Chat_with_Swami_Sivasu__CHtc71MVpdo.md`

**15. [NYC Executive Forum 2026 - A Leader’s Guide to Agentic AI](https://www.youtube.com/watch?v=vvyOHc7jsmg)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: [음악] AWS의 기술, AI 부문 이사이자 상주 임원인 이시트 와슈 포르자니를 환영해 주십시오. [음악] 안녕하세요, 여러분. 좋아요 , 훌륭해요. 오, 여기 오게 되어 정말 기쁩니다. 저는 뉴욕에서 약 25년 정도 일해왔으니, 제 직장 생활의 대부분을 뉴욕에서 보냈다고 할 수 있겠습니다. 우리 멋진 도시가 지난 몇 주 동안 얼마나 놀라운 시간을 보냈는지 몰라요, 그렇죠? 저희는 월드컵을 …
- B5 조직구조 변화: 우리가 조직 구조와 비즈니스 프로세스를 어떻게 최적화했는지 생각해 보면, 모든 것이 예측 가능하고 반복 가능하며 일관된 결과를 도출하도록 최적화되어 있습니다.
- B5 직무·역량 변화: 그래서 우리는 확신이 강하고 가치가 높은 에이전트 중심의 워크플로에 대한 하향식 투자를 생각해 보지만, 동시에 재교육, 역량 강화, 상향식 혁신에 투자하고 1,000개의 꽃이 피어날 수 있는 통로를 만들고 , 나아가 이러한 확신이 강한 워크플로를 상향식 투자로 전환하는 것도 고려해야 합니다.
- 수치 주장: 인공지능이 수행할 수 있는 작업의 길이는 4개월마다 두 배씩 증가하고 있습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 온톨로지·데이터계층
- 원문: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_A_Leader’s_Guide_to_Agentic_AI__vvyOHc7jsmg.md`

**16. [NYC Executive Forum 2026 - A Leader’s Guide to Data Strategy in the Era of Agentic AI](https://www.youtube.com/watch?v=Piy37om0y6A)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] AWS 상주 임원이신 [음악] 라이언 시먼 님을 환영해 주십시오. 좋은 오후에요. 아, 이제 하루가 저물어 가는 시간이군요, 그렇죠? 이제 두 번의 수업이 더 남았습니다. 콘텐츠 피로감이 몰려오고 있습니다. 모두가 조금씩 지쳐가거나, 카페인을 과다 섭취했을 가능성이 높죠. 자, 이제 정말 재미있는 시간을 가져보겠습니다. 그리고 우리는 유전 인공지능이 데이터 전략에 어떤 영향을 미치는…
- B1 디지털·AI 기술의 활용: 요즘 3~4시간마다 새로운 모델 발표, 클라우드 서비스 제공업체 발표, SaaS 플랫폼 발표 같은 게 나오는 걸 우리 모두 눈치챘을 거라고 생각해요 .
- B2 파괴: 데이터 가용성: 기본적으로 팀을 분산시키고, 속도를 높이는 부분만 중앙 집중화하며 , 데이터 축적에서 데이터 공유로 기본을 바꾸고, 데이터 엔지니어를 사업 부서로 이동시키고, 새롭게 재편된 팀들을 연결하는 AI 지원 데이터 플랫폼을 구축하십시오.
- 수치 주장: 새로운 모델은 해당 분야 전문가들이 하루에 수백 개의 모델을 구축할 수 있도록 해야 합니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_A_Leader’s_Guide_to_Data_Strategy__Piy37om0y6A.md`

**17. [NYC Executive Forum 2026 - The Collective Edge: Cross-functional Strategies for AI at Scale](https://www.youtube.com/watch?v=3JHA7ayOJuE)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] AWS의 크리스 헤네시, 린지 드레이크, 에버리스터스 메인스, 그리고 채퍼를 환영해 주세요. [음악] 천만에요. 훌륭한. 안녕하세요 여러분. 오늘 저희가 진행할 패널 토론에 여러분이 함께해 주셔서 정말 기쁩니다. 제 이름은 크리스 헤네시입니다. 저는 AWS에서 상주 임원으로 재직 중이며, 지난 5년간 CFO , CIO, CTO들이 클라우드 및 AI 전략을 추진할 수 있도록 지원해 왔…
- B1 디지털·AI 기술의 활용: 최고인사책임자( CHRO)와 함께 최근에 개발해서 배포한, 직원들에게 직접적인 영향을 미치는 AI 에이전트들을 공유하고, 서로에게 딱 한 가지 질문을 던져보세요.
- B7 성과: 운영효율: '개인을 위한 AI'는 앞서 말씀드린 것처럼 개인 생산성 향상과 같은 제품 개발에 많은 부분을 차지 하지만, 진정한 가치 창출은 '조직을 위한 AI'에서 나온다는 것을 알고 있습니다.
- 수치 주장: 2019년부터 현재까지 전 세계 70만 명의 직원들에게 AI 및 기타 미래 지향적인 기술 교육을 제공했으며, 작년에는 이 프로그램을 25억 달러로 확대하여 전 세계 5천만 명의 사람들이 미래의 직업에 대비할 수 있도록 지원하겠다는 계획을 발표했습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_The_Collective_Edge_Cross-functio__3JHA7ayOJuE.md`

**18. [Tokyo Executive Forum 2026 - A Leader's Guide to AI Strategy & Implementation in the Agentic AI Era](https://www.youtube.com/watch?v=zCauJHa3UGo)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 좋은 오후에요. 제 이름은 헬렌 카포입니다. AWS에 합류하기 전에는 세계 최대 규모의 조직들을 대상으로 데이터 및 AI 혁신을 주도했습니다. 예를 들어 프로톤 갬블, 존슨앤드존슨, 바이엘 , 톰슨 로이터 등이 있습니다. 오늘은 제가 인공지능을 활용하여 조직을 혁신하는 과정에서 얻은 교훈을 여러분과 공유하고자 합니다. 기술 발전 속도가 엄청나게 빠르지만, 그 속도가 조직들이 기술을 도입하는 …
- B1 디지털·AI 기술의 활용: AI 에이전트는 여러 프로세스의 다양한 변형을 병렬로 시도하고, 다양한 승인 순서, 대체 데이터 수집 방식 및 워크플로 재정렬을 검토한 후 최적의 방식을 찾아냅니다 .
- B7 성과: 운영효율: 과거에는 핵심 노하우가 사람들의 머릿속 PDF 파일에 저장되어 있었지만, 이제는 기관의 지식에 접근할 수 있는 간편한 통로를 확보하여 전문성 확보 시간을 단축하고 규정 준수 위험을 줄일 수 있습니다.
- 수치 주장: 만약 업계 경쟁사 세 곳이 모두 현재 AI 기능을 구축하고 있다면, 당신은 더 나은 데이터와 경영진을 확보하여 6개월 안에 제품을 출시하고 18개월 동안 시장을 선도할 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/AWS_Events/Tokyo_Executive_Forum_2026_-_A_Leader's_Guide_to_AI_Strategy__zCauJHa3UGo.md`

**19. [Tokyo Executive Forum 2026 - A Leader's Guide to Advanced Team Structures in an Agentic World](https://www.youtube.com/watch?v=IfFVeLcr-co)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: [음악] 안녕하세요, 좋은 오후입니다. 오늘 오후에 함께해 주셔서 감사합니다. 와주셔서 정말 감사합니다. 안녕하세요, 제 이름은 아르빈드입니다. 저는 싱가포르에 거주하고 있습니다. 저는 AWS에서 2년 조금 넘게 근무했고, 그 전에는 약 25~26년 동안 근무했습니다. 음, 기술과 관련해서 말씀드리자면, 켈로그, 크레 덴셜, 프록터 앤 갬블 같은 회사에서 CIO 디지털 역할을 하면서 많은 변…
- B1 디지털·AI 기술의 활용: 그리고 우리가 이 일을 초기에 해오면서 얻은 가장 큰 교훈은 LLM 과정 내에 정책과 안전장치를 제공하는 것이 효과적이지 않다는 것입니다.
- B5 조직구조 변화: 그래서 이 문제를 해결하고 싶다면, 고객들이 적극적으로 나서서 조직 구조에 더 많은 유연성을 확보하려고 노력하는 모습을 볼 수 있습니다 .
- 수치 주장: 오늘 기조연설에서 보셨겠지만, 개발자 한 명이 10명 이상의 개발자가 필요할 것으로 예상했던 애플리케이션을 2개월 만에 개발해냈습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/AWS_Events/Tokyo_Executive_Forum_2026_-_A_Leader's_Guide_to_Advanced_Te__IfFVeLcr-co.md`

**20. [Tokyo Executive Forum 2026 - Fireside Chat with Jason Bennett VP, Worldwide Startups and VC, AWS](https://www.youtube.com/watch?v=1YbKbO1p7GQ)** — AWS Events · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 제이슨, [음악] 함께해 주셔서 감사합니다. 아, 감사합니다. 저는 이 자리에 함께하게 되어 기쁘고, 일본에서 이렇게 많은 임원분들과 만날 수 있어서 영광입니다. 이번이 제가 아시아 태평양 지역에서 열리는 저희 정상회담에 참석할 수 있는 두 번째 기회입니다. 저도 얼마 전에 한국에 갈 기회가 있었는데, 참석한 대기업과 스타트업 등 모든 곳에서 정말 많은 혁신적인 이야기를 들을 수 있…
- B4 민첩성·양손잡이: 따라서 채용 방식과 호기심 및 학습 민첩성의 중요성을 강조하는 방식 모두에 매우 의도적인 노력을 기울이는 것이 조직의 장기적인 변화에 도움이 될 수 있는 가장 중요한 두 가지 요소라고 생각합니다 .
- B1 디지털·AI 기술의 활용: 즉, 예를 들어 AI 에이전트, 특히 고객 서비스나 백엔드 운영 분야를 생각해 보면, 많은 에이전트들이 상당히 숙련되어 있어서 이전에 사람이 하던 일과 이제 에이전트가 할 수 있는 일 사이의 차이를 구분하기 어려울 정도라는 것을 알게 될 것입니다.
- 수치 주장: 저희는 일본에서 기초 모델을 구축하는 수백 개의 회사와 실제로 협력해 왔습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/AWS_Events/Tokyo_Executive_Forum_2026_-_Fireside_Chat_with_Jason_Bennet__1YbKbO1p7GQ.md`

---

## Accenture


**21. [CES 2026 - Scaling agentic AI to achieve breakthrough transformation](https://www.youtube.com/watch?v=Ba2KXHdbjR0)** — Accenture · 엔터프라이즈 앱 · IE · 2026-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 모두 환영합니다. 지금까지 CES는 정말 흥미진진했습니다. 모두 이렇게 와주셔서 정말 반갑습니다. CES에 가면 어디를 가든 모든 포스터에 AI 관련 내용이 도배되어 있는 걸 볼 수 있어요. 여기서는 정말 어디에나 존재해요. 하지만 진짜 중요한 질문은 인공지능을 통해 어떻게 가치를 창출할 수 있느냐는 것입니다. 실제로 어떻게 활용할까요? 그래서 오늘 우리가 이야기할 내용 중 하나는 어떻게 잠…
- B1 디지털·AI 기술의 활용: 그리고 수집한 데이터를 바탕으로 얻은 인사이트를 활용하여 텔레매틱스 제어 장치를 사용하고, 그 데이터를 클라우드로 전송하여 멋진 대시보드를 만들고 차량 관리자들에게 제공합니다.
- B5 리더십·CDO/CAIO: 이러한 프로젝트가 진행되는 이유 중 하나는 리더십의 합의가 공통된 기대치를 형성하고 있으며, 처음부터 진정한 의미의 부서 간 협업 프로젝트로 설계했기 때문입니다.
- 수치 주장: 저희는 지난 15년 이상 동안 차량 관리 사업에서 큰 성공을 거두었으며, 기본적으로 동일한 기술, 즉 소프트웨어와 하드웨어 센서를 활용하여 ADAS(첨단 운전자 보조 시스템) 솔루션을 차량에 적용함으로써 사업으로 전환하고 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Accenture/CES_2026_-_Scaling_agentic_AI_to_achieve_breakthrough_transf__Ba2KXHdbjR0.md`

**22. [The Skills Mismatch Economy | How AI is reshaping skill demand](https://www.youtube.com/watch?v=HmuEoDwZnqg)** — Accenture · 엔터프라이즈 앱 · IE · 2026-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요, 저는 하버드 비즈니스 리뷰의 선임 편집자 후안 마르티네스입니다 . 액센츄어 리서치 경영진 브리핑에 오신 것을 환영합니다. 우리는 노동 시장의 근본적인 구조조정을 겪고 있습니다. 직책의 의미가 퇴색하고, 이력서에는 더 이상 인재를 구분할 수 없는 정보들로 가득하며 , 인공지능이 대부분의 조직이 아직 따라잡지 못한 변화를 가속화하는 세상 . 오늘 저는 펜실베이니아 대학교 인…
- B5 직무·역량 변화: 변화라는 측면에서 보자면, 내부적으로도 새로운 인재나 인력을 다양한 직무에 투입할 때, 필요한 기술을 갖춘 적합한 인재를 찾아야 하고, 또한 기존 직원들이 새로운 역할 이나 직무에 적응할 수 있도록 어떤 역량을 키워줄 수 있을지 고민해야 한다고 생각합니다.
- B1 디지털·AI 기술의 활용: 실제 비즈니스 문제를 파악하고, 필요한 기술 격차를 식별하고, 빅데이터, 머신러닝 및 기타 방법을 활용하고, 인공지능을 적용하여 이를 자동화하고, 시간이 지남에 따라 그 결과를 추적하는 것이죠.
- 수치 주장: 다행히도 저는 지난 20년 동안 약 30명 규모의 팀을 구축했습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Accenture/The_Skills_Mismatch_Economy_How_AI_is_reshaping_skill_demand__HmuEoDwZnqg.md`

**23. [Consumers are handing decisions to AI agents: what brands need to win](https://www.youtube.com/watch?v=-vqhuxajdWs)** — Accenture · 엔터프라이즈 앱 · IE · 2026-07 · en · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: Hi, I'm Juan Martinez, Senior Editor&nbsp; at the Harvard Business Review. Welcome to the Accenture&nbsp; Research Executive Briefing. AI is often framed as a tool that&nbsp; helps companies operate better,&nbsp;&nbsp; b…
- B1 디지털·AI 기술의 활용: Fifty-six percent of consumers have&nbsp; told us that they would instruct&nbsp;&nbsp; their AI agent on which brands to&nbsp; consider for a specific category.
- B4 가치네트워크·생태계: It's going to have a big impact on the&nbsp; supply chain to ensure that product&nbsp;&nbsp; availability is there at the time that's required.
- 수치 주장: But if you look at that over the&nbsp; 10-year lifespan of the mattress,&nbsp;&nbsp; they're only saving about $150 a month.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/Accenture/Consumers_are_handing_decisions_to_AI_agents_what_brands_nee__-vqhuxajdWs.md`

---

## Alibaba Cloud


**24. [Alibaba Cloud Claw Talks EP4 | Secure AI Agents Across Full Lifecycle at Enterprise Scale](https://www.youtube.com/watch?v=mm9Fl1LcBXI)** — Alibaba Cloud · 파운데이션 모델 · CN · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 알리바바 클라우드 클로 토크에 오신 것을 환영합니다. 이 웨비나 시리즈에서는 알리바바 클라우드 솔루션이 기업 환경에서 AI 에이전트 및 에이전트 기반 인프라를 실제로 도입하는 방법을 소개합니다. 이 시리즈에서는 조직이 에이전트 기반 워크플로우를 구축, 배포, 실행 및 보호하는 방법을 살펴보겠습니다. 오늘 에피소드인 '엔터프라이즈 규모에서 전체 수명 주기 동안 AI 에이전트 보안 강화…
- B1 디지털·AI 기술의 활용: 알리바바 클라우드 솔루션은 두 가지 이상의 서로 다른 AI 에이전트 구성 요소 유형에 대한 가시성을 제공하고, 주요 에이전트 배포 플랫폼을 분류하며, 150개 이상의 에이전트 서비스를 지원합니다.
- B8 부정 성과: 보안·프라이버시: 이로 인해 비정상적인 오류 발생률과 무단 외부 연결이 발생하여 데이터 유출 및 권한 상승으로 이어질 수 있습니다.
- 수치 주장: IDC는 AI 기반 의사 결정 시스템이 서비스 제공 속도를 400% 향상시킨다고 밝혔습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Alibaba_Cloud/Alibaba_Cloud_Claw_Talks_EP4_Secure_AI_Agents_Across_Full_Li__mm9Fl1LcBXI.md`

---

## Anthropic


**25. [What do people use AI models for?](https://www.youtube.com/watch?v=VSmobknYl0E)** — Anthropic · 파운데이션 모델 · US · 2024-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B5 구조 변화
- 개요: 자, 그럼 간단한 자기소개로 시작해 볼까요? 저는 딥 강굴리입니다. 사회적 영향 팀의 연구 과학자로 일하고 있습니다. 저는 사람들이 앤스로픽에서 개발하는 시스템을 어떻게 사용하고 어떤 영향을 받는지, 그리고 이러한 이해를 바탕으로 시스템을 어떻게 더 안전하게 만들 수 있는지, 또한 미래에 사회에 어떤 영향을 미칠지 어떻게 예측할 수 있는지와 같은 근본적인 질문에 깊은 관심을 가지고 있습니다.…
- B8 부정 성과: 보안·프라이버시: 다양한 기술을 살펴볼 때, 저희는 이것이 사람들이 감시 도구로 오해하거나, 사생활 침해로 여겨져 원치 않는 트래픽 패턴을 분석하는 데 악용될 수 있지 않을까 걱정했습니다.
- B1 디지털·AI 기술의 활용: 반대로, 유해 콘텐츠를 영어로 다른 언어로 번역해 달라는 요청은 클라우드 의 이용 정책을 위반할 수 있지만, 단순히 생성 작업이 아닌 번역 작업을 요청하는 것 자체가 과소 거부로 이어질 수 있습니다.
- 수치 주장: 만약 개인 식별 정보가 없다면, 웹 개발에 관한 1,000개의 대화(엘릭서 관련 대화 포함)가 포함된 최종 집계 클러스터를 생성합니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Anthropic/What_do_people_use_AI_models_for__VSmobknYl0E.md`

**26. [Claude for Financial Services Keynote](https://www.youtube.com/watch?v=50AhIyybR0M)** — Anthropic · 파운데이션 모델 · US · 2025-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: [Music] Please welcome to the stage head of revenue at Anthropic Kate Jensen. [Music] &gt;&gt; Good morning everyone. Thank you so much for being here today. I'm Kate Jensen, the head of revenue at Anthropic, and I am so…
- B1 디지털·AI 기술의 활용: The products that we've that we've kind of foregrounded uh for us our uh LLM ready API uh which is the data behind what we've done with MCP uh has been we've seen like enormous traction with that.
- B4 가치네트워크·생태계: Now, I'm really excited to welcome up to the stage two of our partners who help to exemplify the power of our ecosystem in action.
- 수치 주장: Now, let me show you how clot transforms this typical four to five hour scramble into analysis under 30 minutes.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 칩·하드웨어 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Anthropic/Claude_for_Financial_Services_Keynote__50AhIyybR0M.md`

---

## Apple Developer


**27. [Inside Apple Intelligence and Xcode: Special Presentation | WWDC26](https://www.youtube.com/watch?v=Wpwjqk1UGnQ)** — Apple Developer · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 'Apple Intelligence와 Xcode: 특별 세션' 여러분, 환영합니다 와, 정말 놀랍네요 여러분과 함께하게 되어 정말 기쁩니다 WWDC는 저희가 가장 기다리는 순간 중 하나입니다 저희가 만든 것을 여러분께 소개하고 그걸 활용해 만든 것을 볼 수 있으니까요 잠깐 손 들어볼까요? Steve Jobs Theater에 처음 오신 분은 몇 분이나 계신가요? 좋습니다
- B1 디지털·AI 기술의 활용: 좋습니다, 잘 보이네요 네, 들려요 오늘은 Intelligence를 깊이 있게 살펴보려 합니다 올해 저희가 추진한 가장 중요한 분야 중 하나죠 업계 전반에서 AI는 종종 복잡하게 느껴집니다 여러 구성 요소가 각기 다른 회사와 제공업체에서 오기 때문이죠 그리고 개발자인 여러분들이 이를 모두 연결해야 합니다 좋은 결과를 얻기 전에도 많은 복잡성을 마주하게 되죠 사람들이 좋아할 무언가를 만들면서요 하지만 그것은 저희가 추구하는 방향이 아닙니다 Apple에서는 AI는 …
- B7 성과: 조직성과: 좋습니다 지금까지 여러분은 Xcode를 통해 더 빠르게 개발하는 방법과 앱의 콘텐츠와 기능을 시스템 전반에 통합하는 방법 특히 Siri의 자연어 인터페이스를 통해 이를 활용하는 방법을 알아봤습니다 그리고 Foundation Models 프레임워크를 통해 앱에 지능형 기능을 직접 탑재하는 방법도 확인했습니다 마지막으로 Evaluations 프레임워크를 통해 이러한 기능을 테스트하는 방법도 살펴봤습니다 하지만 아직 끝이 아닙니다 여러분 중 많은 분들은 자신의 모델을…
- 수치 주장: 아직 빌드 중입니다 겉보기엔 아주 간단한 프롬프트였지만 실제로는 뒤에서 꽤 많은 일이 일어나고 있거든요 생각해 보면 우선 카메라를 활용한 사용자 경험을 만들어야 하고 그다음 비전 모델이 방금 촬영한 사진을 제 Asset Catalog에 있는 모든 핀 이미지와 비교해야 합니다 맞습니다 그리고 그 위에 전체 사용자 경험을 구축하게 됩니다 우리가 이미 만든 앱 안에서 말이죠 그래서 이 한 줄의 프롬프트는 사실 다양한 기술과 플랫폼을 활용하는 매우 복잡한 기능인 셈입니…
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 추론 최적화
- 원문: `transcripts/channels/Apple_Developer/Inside_Apple_Intelligence_and_Xcode_Special_Presentation_WWD__Wpwjqk1UGnQ.md`

**28. [WWDC26: Meet Trust Insights | Apple](https://www.youtube.com/watch?v=jY-_rqz_VEM)** — Apple Developer · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요, 저는 Mike Armstrong이고 Apple의 엔지니어링 매니저입니다. 이 영상에서는 Trust Insights를 사용하여 감지하는 방법을 배우게 됩니다. 앱에서 발생하는 소셜 엔지니어링 위협에 대응하는 방법도 알아봅니다. 소셜 스캠은 점점 늘어나는 문제입니다. 시스템이 아닌 사람을 표적으로 삼는 공격입니다. 소셜 엔지니어링은 인간 심리를 악용합니다. 기술적인 취약점이 아닌 방…
- B8 부정 성과: 보안·프라이버시: Trust Insights를 앱에 통합하는 방법, API 사용 요구 사항, 프라이버시 아키텍처에 대한 설명, 그리고 앱이 신뢰 신호에 응답하는 예시를 마지막으로 다룹니다.
- B7 성과: 조직성과: usedEvaluationOnly 인사이트가 내부 평가 및 벤치마킹 같은 용도로 사용되었으나, 사용자 경험에는 영향을 주지 않았습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Apple_Developer/WWDC26_Meet_Trust_Insights_Apple__jY-_rqz_VEM.md`

**29. [WWDC26: What’s new in the Foundation Models framework | Apple](https://www.youtube.com/watch?v=Xrv8m_EHCbg)** — Apple Developer · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요, 환영합니다! 저는 Erik입니다! 저는 Zhen입니다! 지난해 저희는 Foundation Models 프레임워크를 소개했습니다 guided generation, snapshot streaming 같은 기능과 강력한 tool 프로토콜을 갖추고 있었죠 여러분의 뜨거운 반응에 Foundation Models 프레임워크 첫 해에 정말 놀랐습니다 올해 준비한 내용은 더욱 마음에 드실 거라…
- B1 디지털·AI 기술의 활용: 물론 Private Cloud Compute는 무엇보다도 프라이버시를 보호합니다 프롬프트는 절대 저장되지 않으며 독립적인 연구자들이 이를 검증할 수 있도록 공개합니다 또한 Private Cloud Compute 덕분에 Foundation Models 프레임워크를 watchOS에서도 사용할 수 있습니다 watchOS 27부터 가장 강력한 인텔리전스 기능을 손목에서 바로 사용하세요 PCC는 클라우드 API 비용 없이 제공되며 첫 다운로드 200만 건 미만의 개발자에…
- B7 성과: 조직성과: 저희만큼 여러분도 이 모든 새 기능들에 흥분하셨으면 합니다 모델과 API들요 이것은 시작에 불과합니다 맞습니다, 더 자세히 알아보려면 다른 영상들을 꼭 확인하세요 여기서 소개한 모든 주제의 심층 탐구를 위해 Evaluations 프레임워크부터 Private Cloud Compute, 강화된 Xcode 도구, dynamic profiles의 세부 사항까지요 좋은 다음 단계는 샘플 앱을 탐색해 dynamic profiles를 더 알아보고 Evaluations 프레임…
- 수치 주장: 이번 릴리스에는 새로운 온디바이스 모델이 포함됩니다 처음부터 새로 구축해 전반적으로 더 우수해졌습니다 더 똑똑해졌고 논리 및 tool 호출 능력이 향상됐습니다 iOS 26.4에서 모델의 컨텍스트 크기 확인과 명령어, 프롬프트, 트랜스크립트의 토큰 수 계산을 위한 새 API가 추가됐습니다 앞으로는 이 API를 활용해 실행 중인 기기의 하드웨어에 맞게 앱을 조정하세요 가이드라인 개선에도 많은 노력을 기울였습니다 iOS 26.4에서 이미 일부 변경 사항을 느끼셨을 것…
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/Apple_Developer/WWDC26_What’s_new_in_the_Foundation_Models_framework_Apple__Xrv8m_EHCbg.md`

---

## Arm


**30. [Ashwini Vaishnaw: On India’s path to “Tech Powerhouse”](https://www.youtube.com/watch?v=dmU0LX5aI-0)** — Arm · 인프라·칩·전력 · UK · 2025-10 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: [음악] Tech Unheard에 오신 것을 환영합니다. 이 팟캐스트는 기술 분야에서 가장 흥미진진한 발전의 비하인드 스토리를 여러분께 전해드립니다. 안녕하세요, 저는 ARM의 CEO이자 진행자인 르네 호스입니다. 오늘은 여러분을 위해 아주 특별한 에피소드를 준비했습니다 . 저는 인도 방갈로르에 있으며, 인도 정부의 철도·정보· 방송·전자· 정보기술부 장관인 아슈비니 비슈나와 함께 있습니다.…
- B4 가치네트워크·생태계: 현재 우리는 세계에서 세 번째로 큰 스타트업 생태계를 보유하고 있으며, 두 번째 핵심 정책인 '메이크 인 인디아'를 통해 거의 모든 것을 제조하는 데 많은 노력을 기울여 왔습니다.
- B7 성과: 운영효율: ARM을 비롯한 모든 반도체 회사에서 AI 덕분에 생산성이 향상되고 있다는 것은 분명하지만, 특히 세계에서 가장 복잡한 칩들을 설계하는 데 필요한 숙련된 엔지니어는 여전히 많이 필요합니다.
- 수치 주장: 현재 저희는 약 1400억 달러를 투자하고 있는데, 죄송합니다만, 이는 철도, 고속도로, 전력, 새로운 대학 건설, 교외 교통 개선 등 여러 분야에 대한 자본 투자입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Arm/Ashwini_Vaishnaw_On_India’s_path_to_“Tech_Powerhouse”__dmU0LX5aI-0.md`

**31. [Arm CEO Rene Haas on AI, chips, and the future of global compute | FT Davos](https://www.youtube.com/watch?v=mpEnhLkwGrU)** — Arm · 인프라·칩·전력 · UK · 2026-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. [음악] 안녕하세요. 제가 접속 중인가요? 안녕하세요 여러분, 화요일 밤 다보스에 있는 FT 하우스에 오신 것을 환영합니다. 저는 오늘 ARM의 CEO이신 르네 허스 씨와 함께하게 되어 매우 기쁩니다. ARM은 훌륭한 영국 기업입니다. 음, 우리는 내일 도널드 트럼프의 방문을 포함해서 세상 만사에 대해 이야기할 겁니다 . 음, 그러니까 르네는 ARM에 오랫동안 근…
- B4 가치네트워크·생태계: 저희는 매우 큰 생태계에서 활동하고 있으며, 스타트업 기업들과 협력하는 것뿐만 아니라, 말씀하신 유연한 접근 프로그램처럼 ARM에서 투자받은 많은 사람들이 회사를 떠나 자신 만의 사업을 시작하기도 합니다.
- B3 전략적 대응: 그러니까 MBA를 따라는 관점이 아니라, 이사회와 이사로서 어떻게 사람들이 차세대 기업가가 되도록 장려할 수 있을까요?
- 수치 주장: 저희 회사를 잘 모르시는 분들을 위해 설명드리자면, 저희는 캠브리지에 본사를 둔 약 35년 역사의 회사로, 세계에서 가장 널리 사용되는 컴퓨팅 플랫폼을 개발한 것으로 유명합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/Arm/Arm_CEO_Rene_Haas_on_AI,_chips,_and_the_future_of_global_com__mpEnhLkwGrU.md`

**32. [Panos Panay: On Humility and Empathy in Leadership](https://www.youtube.com/watch?v=YF7dcSd_3L0)** — Arm · 인프라·칩·전력 · UK · 2026-01 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] Tech Unheard에 오신 것을 환영합니다. [음악] 이 팟캐스트는 기술 분야 에서 가장 흥미진진한 발전의 비하인드 스토리를 여러분께 전해드립니다 . 안녕하세요, 저는 ARM의 CEO이자 음악 진행자인 르네 호스입니다. 오늘 저는 아마존 디바이스 및 서비스 부문 수석 부사장인 파노스 파네 씨를 모셨습니다. 아마존에 합류하기 전, 파노(음악)는 마이크로소프트에서 20년간 근무하며 …
- B5 리더십·CDO/CAIO: 양방향 소통이 얼마나 중요한지 말씀드리고 싶은데요, 리더가 공감 능력과 자기 성찰 능력, 그리고 팀원들 또한 자기 비판적일 수 있는 능력을 갖췄을 때 비로소 제대로 된 리더십이 발휘되기 때문입니다.
- B1 디지털·AI 기술의 활용: AWS가 제공하는 전달 메커니즘을 예로 들자면, 알렉사는 클라우드 기반 제품이기 때문에 엔드포인트 자체가 고객에게 많은 가능성을 제공할 수 있고, 우리는 이미 그렇게 하고 있습니다 .
- 수치 주장: 파노스는 아마존에서 약 2년간 음악 관련 업무를 맡아오면서 알렉사 플러스를 출시했고, 인공지능과 소비자 기기에 점점 더 집중하고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Arm/Panos_Panay_On_Humility_and_Empathy_in_Leadership__YF7dcSd_3L0.md`

**33. [Chris Bergey, EVP, Edge AI Business Unit, Arm, on the GSMA 'Data, Compute, Energy' panel at MWC 2026](https://www.youtube.com/watch?v=nzXbAX4Yo90)** — Arm · 인프라·칩·전력 · UK · 2026-03 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 모든 시대에는 우리를 하나로 모아 상상하고 혁신하게 만드는 필요성, 열정, 본능이 존재합니다. 이것은 변하지 않았습니다. 가능한 것은 이미 이루어졌습니다. 우리는 세상을 더 나은 곳으로 만드는 기술을 개발합니다 . 우리에게 감동을 주고, 힘을 주고, 연결해 주는 생각들. 하지만 훌륭한 아이디어는 혼자서는 번성할 수 없습니다. 그것들은 공유되고, 비판받고, 다듬어져야 합니다. 우리는 통찰력과 …
- B1 디지털·AI 기술의 활용: 그들은 클라우드 모델이 더 높은 해상도를 제공한다는 것을 알기 때문에 클라우드 모델을 얻기를 바라지만, 현실은 당신이 정해진 시간 안에 답변을 제공할 것이라는 기대가 있기 때문에 로컬에서 먼저 시작해야 한다는 것입니다.
- B2 파괴: 소비자 행동·기대: 그래서, 어, 이것들은 오늘날 고객들이 원하는 바를 보여주는 신호들이고, 아시다시피 대규모 클라우드는 고객이 원하는 방식으로 워크로드를 배치하기 위해 고도로 최적화된 알고리즘을 사용합니다.
- 수치 주장: 규모가 작고 고객들이 공유할 수 있는 공간이 부족하기 때문에 활용률을 80~90%까지 끌어올리기가 어렵다는 거죠.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Arm/Chris_Bergey,_EVP,_Edge_AI_Business_Unit,_Arm,_on_the_GSMA_'__nzXbAX4Yo90.md`

---

## Asian Productivity Organization


**34. [APO GAIA Podcast | Korea’s AI Policy and Manufacturing AX with MOTIR](https://www.youtube.com/watch?v=LogtwSzSdWw)** — Asian Productivity Organization · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽
- 개요: 가이아 팟캐스트 APO 진정한 AI 액션에 오신 것을 환영합니다 . 제 이름은 에리카입니다. 저는 APO의 담당자입니다. 오늘 저희와 함께 해주신 분은 대한민국 산업통상자원부 사무총장이시며, 주일본 한국대사관에도 근무하고 계신 존 클룩 사무총장님입니다 . Ch 씨, 환영합니다. 아, 만나서 반갑습니다 . 만나서 반가워요. 감사합니다. 초대해 주셔서 매우 영광입니다. 매우 감사합니다. 감사합니…
- B4 가치네트워크·생태계: 그래서 산업통상자원부는 ' 맥스 얼라이언스 제조 AI 전환 연합'이라는 생태계를 조성했습니다.
- B8 부정 성과: 보안·프라이버시: 산업 분야에서 인공지능 기술이 오작동할 경우 경제적 손실이 막대할 것이고, 공장 현장의 근로자들이 다칠 수도 있기 때문입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/2026-07-21/APO_GAIA_Podcast_Korea’s_AI_Policy_and_Manufacturing_AX_with__LogtwSzSdWw.md`

---

## Boston Consulting Group


**35. [Lead with Purpose, Adapt with Strategy | Phillip Benedetti (Consultant, Spencer Stuart)](https://www.youtube.com/watch?v=c9-0LUYKwhI)** — Boston Consulting Group · 컨설팅·전략 · — · 2026-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 많은 조직들은 전략을 수립했고, 전략을 전달했으며, 모두가 전략을 알고 있다고 생각합니다. 실제로 제가 사업을 운영하는 모든 시장에서, 일반적인 전략을 그대로 적용해서 회사 로고를 제거하고 다른 회사 로고를 붙이는 식으로 간단하게 해결할 수 있습니다. 그렇게 특정 시장에만 국한된 전략은 아닙니다. [음악] 오늘 저희의 손님은 전 상무이사 겸 파트너였던 필립 베네데티입니다. 그는 15년 이상 …
- B2 파괴: 경쟁구도: 그는 15년 이상 동안 주요 고객사들이 전략, 성장, 혁신 및 경쟁 우위와 관련된 문제들을 해결해 나갈 수 있도록 지원해 왔으며, 특히 불확실한 시대에 이러한 지원이 더욱 중요했습니다.
- B5 리더십·CDO/CAIO: 그 사례를 통해 훌륭한 리더십과 팀워크 구축이란 무엇인지에 대해 질문드리는 데 도움이 될 것 같습니다.
- 수치 주장: 그것은 엄청나게 비싼, 특히 당시로서는 10억 달러가 넘는 비용을 들여야 실현 가능한 공급망을 구축할 수 있도록 허용하는 것이었습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Boston_Consulting_Group/Lead_with_Purpose,_Adapt_with_Strategy_Phillip_Benedetti_(Co__c9-0LUYKwhI.md`

---

## Boston Dynamics


**36. [Why Humanoids Are the Future of Manufacturing | Boston Dynamics Webinar](https://www.youtube.com/watch?v=laexcnaTrDM)** — Boston Dynamics · 물리 AI·자율주행 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요 여러분. 오늘 함께해 주셔서 정말 감사합니다. 그리고 알베르토 씨도 오늘 함께해 주셔서 감사합니다. 저는 야 더반이고, 아틀라스 제품 팀에서 휴머노이드 애플리케이션 제품 전략을 총괄하고 있습니다. 즉, 저는 이 로봇을 어디서부터 시작할지, 그리고 고객이 장기적으로 이 로봇에게 무엇을 기대하는지 결정하여, 시간이 지남에 따라 그 목표를 달성하기 위한 훌륭한 전략을 수립할 수 있도록 …
- B7 성과: 운영효율: 그 규모가 커지고 일반화될수록, 특정 업무에 실제로 필요한 정책이 무엇인지에 대한 첫 번째 추측이 더 정확해지고, 각 업무에 대한 현장 교육에 투자해야 하는 시간이 줄어듭니다 .
- B2 파괴: 소비자 행동·기대: 그래서 저는 고객 경험과 지식을 Spot, Stretch, 그리고 이미 진행한 수천 건의 로봇 배치 경험을 통해 얻은 교훈과 결합하여 보스턴 다이내믹스와 전 세계가 나아갈 다음 단계인 휴머노이드 로봇을 만들어낼 수 있게 되어 매우 기쁩니다 .
- 수치 주장: 왜냐하면 우리가 어떻게 일반성을 구축하고 있는지, 또는 어떻게 행동 엔진을 만들고 있는지에 대한 답이 지난 3~4 년 동안 극적으로 바뀌었기 때문입니다.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/Boston_Dynamics/Why_Humanoids_Are_the_Future_of_Manufacturing_Boston_Dynamic__laexcnaTrDM.md`

---

## Cohere


**37. [Tycho van der Ouderaa and Matt Beton - KPOP  Kronecker Preconditioned adaptive OPtimization](https://www.youtube.com/watch?v=1DTSdYy2RcU)** — Cohere · 파운데이션 모델 · CA · 2025-08 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 훌륭해요. 하르샤, 정말 고마워요. 음, 알겠습니다. 그럼 간단한 소개로 시작하겠습니다. 안녕하세요, 제 이름은 맷입니다. 저는 티코와 함께 왔어요. 저는 ExoLabs라는 회사에서 일하고 있고, 티코는 지난 봄에 몇 달 동안 저희와 함께 일했습니다 . 음, 그리고 티코가 우리와 함께 있을 때, 우리는 '케이팝'이라는 제목의 논문을 함께 작업했어요 . 음, 이 논문은 크게 두 가지 …
- B1 디지털·AI 기술의 활용: 네, K-pop이나 다른 최적화 알고리즘을 살펴보게 된 이유 중 하나는, 저희가 딥러닝 커뮤니티에서 오랫동안 Adam 최적화 알고리즘을 사용해 왔기 때문입니다.
- B8 부정 성과: 보안·프라이버시: 음, 아마도 Kayfac 통계는 QR 업데이트를 하기 직전에만 동기화되는 것 같고, 그렇게 하면 여전히 편향되지 않은 결과를 얻을 수 있을 것 같습니다.
- 수치 주장: 그래서 조기 종료를 통해 두 모델 모두 34분 동안만 훈련하도록 할 수 있고, Adam 대신 Pop을 사용했을 때 성능 향상이 크게 나타나는 것을 확인할 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/Cohere/Tycho_van_der_Ouderaa_and_Matt_Beton_-_KPOP_Kronecker_Precon__1DTSdYy2RcU.md`

**38. [Bell Canada and Dell Technologies discuss their partnership with Cohere](https://www.youtube.com/watch?v=dbJ7a2c6KoA)** — Cohere · 파운데이션 모델 · CA · 2025-10 · en · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: I'm happy to be joined by leaders from two key coher partners to discuss how they are finding value with North. Uh I'm pleased to introduce Pam Peltier, country leader for Dell Canada and John Watson, group president of …
- B4 가치네트워크·생태계: I think what comes to mind here when you say the the partnership with with with Bell with Dell and with Coher, I think coming together like this here in Canada, it it acts as a force multiplier.
- B1 디지털·AI 기술의 활용: So I think it's really this acceleration and the view and I know with with some they're much closer to this concept of digital twin because they've trained it on everything I've ever created or written.
- 수치 주장: I think we're we're situated perfectly, you know, with our coherent relationship uh with the assets we're building AI fabric uh large uh mega project of AI infrastructure and the government has made it very clear over the last it's probably been about 6 to 8 w…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Cohere/Bell_Canada_and_Dell_Technologies_discuss_their_partnership___dbJ7a2c6KoA.md`

**39. [Cohere Labs Connect Conference - Day 1](https://www.youtube.com/watch?v=fbMqJHOel0U)** — Cohere · 파운데이션 모델 · CA · 2025-11 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [music] Uh great. Hi everyone and welcome. I see 148 people here and counting. So exciting to to do an event together. So for those of you who are part of our opensiz community, welcome back. I think this is a familiar s…
- B1 디지털·AI 기술의 활용: Hey everyone, uh my name is Nataniel and Muhammad and I are going to present our work how good large language models at multi session coding interactions.
- B8 부정 성과: 보안·프라이버시: tackling head-on problems of hallucination, misinformation, problems of safety and privacy, I think continue to be important to build the AI that we want to use.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Cohere/Cohere_Labs_Connect_Conference_-_Day_1__fbMqJHOel0U.md`

**40. [Cohere Labs Connect Conference - Day 2](https://www.youtube.com/watch?v=Q-upWvYEx-E)** — Cohere · 파운데이션 모델 · CA · 2025-11 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [music] Hi everyone and uh welcome to the second day of the connect conference. So yesterday we opened up the conversation about collaboration and really uh together we looked at what different collaborations different s…
- B8 부정 성과: 보안·프라이버시: And the answer was that there is no strong correlation which means that LLMs can take biased decisions without necessarily having any bias thoughts or vice versa.
- B1 디지털·AI 기술의 활용: So imagine you tell an LLM there's this person from race A and there's this other person from another race and they're both at the courthouse.
- 수치 주장: Um so what we did is that we um deployed all these like speakers uh in and we collected more than 200,000 multiple choice questions from exams across 44 languages, 15 scripts.
- 교량: Avenue 1 동적역량 · 기술: 프로토콜·표준 · 칩·하드웨어
- 원문: `transcripts/channels/Cohere/Cohere_Labs_Connect_Conference_-_Day_2__Q-upWvYEx-E.md`

**41. [Cohere Labs Connect Conference - Day 3](https://www.youtube.com/watch?v=UAAHd6rMWp8)** — Cohere · 파운데이션 모델 · CA · 2025-11 · ko · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 모두 환영합니다. 오늘 셋째 날에도 오신 것을 환영합니다 . 네, 그럼 셰인부터 시작하죠. 페니스는 코허 랩 과 여러 곳에서 다양한 프로젝트를 통해 협업해 왔습니다. 제가 처음으로 페니스와 협업하는 모습을 본 건 YA를 통해서였는데, 정말 감명받았습니다. 그는 MIT 박사 과정생으로, AI와 그것이 세상에 미치는 영향의 교차점에 대한 연구에 집중하고 있습니다. 데이터 출처 이니셔티브를 이끌고…
- B1 디지털·AI 기술의 활용: 그리고 나중에 구글에서 인턴으로 일할 때 , 업계 전문가 50명 이상과 협력하여 Fla 컬렉션과 Flawn T5 모델 시리즈를 출시했는데, 당시 Chhat GPT 출시 직후 가장 인기 있는 오픈 소스 모델 시리즈였습니다.
- B8 부정 성과: 보안·프라이버시: 하지만 인공지능 훈련이 지적 재산권 이나 개인정보 보호법을 위반하는지 여부, 경제와 노동 시장에 미치는 영향, 언론에 미치는 영향, 사이버 보안을 위해 인공지능을 공격적 또는 방어적으로 사용할 수 있는지 여부 등을 살펴볼 수 있습니다.
- 수치 주장: 인류경제지수 지도를 보면 전 세계적으로 10억 명이 넘는 사용자가 Gemini, ChatGBT, Claude, Llama 모델을 사용하는 제품과 서비스를 통해 범용 시스템을 활용하고 있다는 것을 알 수 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Cohere/Cohere_Labs_Connect_Conference_-_Day_3__UAAHd6rMWp8.md`

**42. [How  Collaboration Accelerates Progress in AI Research - Shayne Longpre Keynote | Connect 2025](https://www.youtube.com/watch?v=b0ydOb6e_T0)** — Cohere · 파운데이션 모델 · CA · 2025-11 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: [음악]을 덧붙입니다. 그래서 저는 이곳에 오게 되어 정말 기쁩니다 . 매우 감사합니다. 오늘은 인공지능 연구뿐만 아니라 더 넓은 범위의 연구에서 협업에 대한 이전 발표를 바탕으로 이야기를 나눠보려고 합니다. 그리고 저는 멘토와 조언자분들, 특히 코허 랩을 비롯한 여러 곳에서 배운 것을 바탕으로 성공적인 연구 협력을 위한 로드맵을 제시하고자 합니다. 자, 그럼 본론으로 들어가서, 제가 왜 여…
- B1 디지털·AI 기술의 활용: 그리고 나중에 구글에서 인턴으로 일할 때 , 업계 환경에서 50명이 넘는 협력자들과 함께 Fla 컬렉션과 Flawn T5 모델 시리즈를 출시했는데, 당시 Chhat GPT 출시 직후 가장 인기 있는 오픈 시리즈 모델이었습니다 .
- B3 전략적 대응: 그래서 핵심은 왜 혼자서 하는 것과 달리 협업해야 하는지, 그리고 나중에 성공적인 방식으로 혼자서도 할 수 있도록 단계별 로드맵을 어떻게 구축할 수 있는지에 대한 것입니다.
- 수치 주장: 인류경제지수 지도를 보면 전 세계적으로 10억 명이 넘는 사용자가 Gemini, ChatGBT, Claude, Llama 모델을 사용하는 제품과 서비스를 통해 범용 시스템을 활용하고 있다는 것을 알 수 있습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Cohere/How_Collaboration_Accelerates_Progress_in_AI_Research_-_Shay__b0ydOb6e_T0.md`

**43. [Weijia Shi and Xiaochuang Han - 𝐋𝐥𝐚𝐦𝐚𝐅𝐮𝐬𝐢𝐨𝐧  Adapting Pretrained Language Models for Mult](https://www.youtube.com/watch?v=Mg4fr56eB_8)** — Cohere · 파운데이션 모델 · CA · 2025-11 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [music] Hi everyone, thank you so much for joining us for a special guest speaker session uh at the original regional Asia. We have with us Vijay Shi and Han. Vijaya is a PhD student at University of Washington. Her rese…
- B8 부정 성과: 보안·프라이버시: So I think one promising path going forward is to find ways to use this private data through new training algorithms and architectures that preserves data privacy.
- B1 디지털·AI 기술의 활용: And the last benefit is because the because the model architecture is modular we can easily add another modality component into the final model with cheap fine-tuning.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Cohere/Weijia_Shi_and_Xiaochuang_Han_-_𝐋𝐥𝐚𝐦𝐚𝐅𝐮𝐬𝐢𝐨𝐧_Adapting_Pretrai__Mg4fr56eB_8.md`

**44. [Wisdom Ikezogwo   Distilling Multimodal Pretraining Data and Evaluation benchmarks from Unstructured](https://www.youtube.com/watch?v=FiCr2yUafPE)** — Cohere · 파운데이션 모델 · CA · 2025-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 괜찮은. 안녕하세요 여러분. 네, 또 다른 특별 강연 세션으로 돌아왔습니다. 음, 오늘은 지혜에 대해 이야기해 보겠습니다. 위즈덤은 워싱턴 대학교 박사 과정에 재학 중입니다. 네, 란짓 크리슈나 교수님과 린다 샤피로 님의 지도를 받았습니다. 음, 그는 주로 대규모 멀티모달 콘텐츠 생성 및 특히 의료 AI를 위한 비전 언어에 직접적으로 초점을 맞추고 있습니다 . 음, 그는 CVP, ICV 같은…
- B1 디지털·AI 기술의 활용: 음, 1차 세계 대전 관련 인용문(1M)의 경우, 당시 최고의 모델이었던 GPT 3.5를 사용했고, 의료 관련 서술의 경우 GPT 4.1을 사용했는데, 이는 올해 초와 작년 말에 최고였던 모델입니다.
- B2 파괴: 데이터 가용성: 몇 년 전 저희는 1M이라는 프로젝트를 시작했는데, 이 프로젝트는 특정 도메인 내에서 이미지와 텍스트 데이터를 수집하는 방법을 연구하는 것이었습니다.
- 수치 주장: 74만 8천 개에서 약 7만 4천 개의 고품질 스토리텔링 동영상으로 감소합니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Cohere/Wisdom_Ikezogwo_Distilling_Multimodal_Pretraining_Data_and_E__FiCr2yUafPE.md`

**45. [Aditri Bhagirath  - Persona Guided Personalization](https://www.youtube.com/watch?v=0X01DFnA2dc)** — Cohere · 파운데이션 모델 · CA · 2026-01 · en · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Hello everyone and welcome. I'm Prahita from the ML industry program at the Coher Labs open science community. We're glad to have you with us for today's session. So our talk today focuses on persona guided personalizati…
- B2 파괴: 소비자 행동·기대: And finally, we pass in the persona that we created in step two and those informative examples and just um stitch those together into a personalized prompt.
- B1 디지털·AI 기술의 활용: and personas are quite portable across model families be it Gemini llama models um you know API based models versus open source so this is an analysis that we did on cross family robustness at least um several months ago this was the case so the biggest improv…
- 수치 주장: And we saw that um after creating these personalization prompts which includes the persona plus de demonstrative prior examples we have about a 4 to 5% improvement over existing state-of-the-art models like BPL PAL and GO that we talked about earlier and this …
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Cohere/Aditri_Bhagirath_-_Persona_Guided_Personalization__0X01DFnA2dc.md`

**46. [Ahsaas Bajaj  - Production Grade ML in Practice  Evaluation and Design Frameworks for Recommendation](https://www.youtube.com/watch?v=UkOvqHSskMw)** — Cohere · 파운데이션 모델 · CA · 2026-01 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 아리안, 고마워요. 훌륭한 소개 감사합니다. 안녕하세요 여러분. 여러분 모두 아시다시피 저는 사스입니다. 저는 Instacart의 선임 머신러닝 엔지니어입니다. 아, 그리고 그 전에는 월마트 와 삼성 연구소에서도 근무했었어요. 지난 몇 년 동안 저는 수억 건의 요청을 처리하는 추천 시스템을 구축할 기회를 가졌습니다 . 그리고 그 과정에서, 저는 완전히 이해하는 데 시간이 좀 걸렸지만…
- B1 디지털·AI 기술의 활용: 개별적으로는 뛰어난 성능을 발휘하는 모델이 있을 수 있지만, 전체 쇼핑 고객 흐름에 적용했을 때, 예를 들어 매장 통로에서 상품을 교체하려는 고객을 위해 필요한 결정을 내릴 수 없는 LLM(로컬 라이프사이클 관리) 시스템은 비즈니스에 큰 도움이 되지 못할 것입니다.
- B2 파괴: 소비자 행동·기대: 그러니까 이러한 다양한 계층 구조에 걸쳐 특징이나 입력 데이터 소스를 분류하면 모델이 개인화뿐만 아니라 활용도 제대로 수행할 수 있게 되고, 탐색과 활용을 동시에 수행하는 것이 아니라 활용할 수 있게 됩니다.
- 수치 주장: 지난 몇 년 동안 저는 수억 건의 요청을 처리하는 추천 시스템을 구축할 기회를 가졌습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Cohere/Ahsaas_Bajaj_-_Production_Grade_ML_in_Practice_Evaluation_an__UkOvqHSskMw.md`

**47. [Nathan Calvin - Three People vs  Big AI  Policy, Power, and California’s Frontier AI Law](https://www.youtube.com/watch?v=RV00BTMY5XA)** — Cohere · 파운데이션 모델 · CA · 2026-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 좋아요, 알겠습니다. 네, 오늘 함께해 주신 모든 분들께 감사드립니다 . 오늘 아주 흥미로운 손님이 오셨습니다. 그의 이름은 네이선 캘빈입니다. 그는 Enco Justice의 총괄 이사이며, Enco Justice는 청년 주도의 활동가이자 공익 교육을 지향하는 비영리 단체로, 인공지능 관련 법률 제정을 옹호합니다. 그리고 그는 캘리포니아의 인공지능 투명성 법안인 SB53을 작성하는 데 도움을…
- B8 부정 성과: 보안·프라이버시: 그러니까 모델이 생물학 무기 공격이나 중요 기반 시설에 대한 심각한 사이버 공격을 용이하게 할 가능성, 또는 인간이 통제력을 잃고 오작동하여 온갖 혼란을 야기할 가능성 같은 것들을 말하는 겁니다 .
- B1 디지털·AI 기술의 활용: 음, 그래서 53번 조항은 클라우드 기업이 이러한 위험을 어떻게 처리해야 하는지, 또는 피해를 발생시켰을 경우 어떤 책임을 져야 하는지와 같은 구체적인 기준을 마련하는 데 초점을 맞추는 것이 아닙니다 .
- 수치 주장: 하지만, 이러한 첨단 AI 프레임워크 와 안전 계획 시스템 카드는 그 이상의 교육을 받고 있으면서도 연 매출이 5억 달러 이상인 기업에 적용됩니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Cohere/Nathan_Calvin_-_Three_People_vs_Big_AI_Policy,_Power,_and_Ca__RV00BTMY5XA.md`

**48. [Dr  Plamen Miltenoff - AI and XR in Education  From Curiosity to Competence](https://www.youtube.com/watch?v=Pb2t7U6vf7Y)** — Cohere · 파운데이션 모델 · CA · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, 저는 코허 랩스 에듀테크 커뮤니티의 라파 무스타파입니다. 이번 세션에 오신 것을 환영합니다. 오늘 초청 강연자 자리에는 국제적인 학술 경력을 풍부히 쌓아온 연구자이자 교육자인 플만 박사님을 모셨습니다. 그는 호주 국립 도서관과 노스웨스턴 대학교에서 연구원 및 사서로 근무했으며, 세인트 클라우드 주립 대학교에서 정보 전문가 및 교수로 재직했습니다. 그는 현재 경제대…
- B1 디지털·AI 기술의 활용: Chad GPT, Copilot, Clo , Gemini와 같은 AI 도구와 Nano Banana 같은 생성기는 이미 사람들이 글을 쓰고, 연구하고, 문제를 해결하는 방식을 바꾸고 있습니다.
- B2 파괴: 데이터 가용성: 학습자가 환경과 상호작용함에 따라 XR 시스템은 실시간 공간 및 수행 데이터를 수집합니다.
- 수치 주장: 지난 2 년 동안 저는 AI 활용 능력과 교육에서의 AI에 집중해 왔습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Cohere/Dr_Plamen_Miltenoff_-_AI_and_XR_in_Education_From_Curiosity___Pb2t7U6vf7Y.md`

**49. [Jiafei Duan  - Building Robotics Foundation Model with Reasoning in the loop](https://www.youtube.com/watch?v=ZB5IAlFvt1c)** — Cohere · 파운데이션 모델 · CA · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 오늘은 Reason을 활용하여 로봇 공학 기초 모델을 구축하는 방법에 대한 제 박사 연구 내용을 공유하려고 합니다. 머신러닝은 이제 우리 일상생활의 일부가 되었죠. 학문적 영역을 넘어 엄청난 발전을 이루어 이메일을 작성하고, 디지털 작업을 지원하며, 심지어 코드를 생성해 주기까지 합니다. 여러모로 머신러닝의 발전은 우리가 생각하고 일하는 방식을 디지털 세계에서 변화시켰다고…
- B2 파괴: 데이터 가용성: 그리고 그 작업이 정말 좋다면, 새로운 작업을 추가하고, 더 많은 데이터를 수집하고, 정책을 추가로 학습시키는 과정을 반복하면 됩니다.
- B1 디지털·AI 기술의 활용: 예를 들어, GPT(가상 모델 물리 엔진)에 '접시 사이의 어디인가?'라고 물으면 GPT는 경계 상자를 제공하고, Gemini(제미니)에 물으면 더 정확한 경계 상자를 제공하며, 오픈 소스 모델에 물으면 또 다른 경계 상자를 선택합니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Cohere/Jiafei_Duan_-_Building_Robotics_Foundation_Model_with_Reason__ZB5IAlFvt1c.md`

**50. [Zifeng Liu - Human–AI Collaboration in Educational Assessment  Evaluating AI Generated Distractors](https://www.youtube.com/watch?v=X84gmuT9RI8)** — Cohere · 파운데이션 모델 · CA · 2026-04 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 안녕하세요, 여러분! 와주셔서 감사합니다. 라핀이 소개했듯이 제 이름은 종이고, 현재 플로리다 대학교에서 교육공학 박사 과정을 밟고 있습니다. 이렇게 여러분과 만나게 되어 정말 기쁩니다 . 오늘 강연에서는 핵심 질문 하나에 집중하겠습니다. 인공지능이 생성한 객관식 문제의 오답 보기나 피드백과 같은 평가 콘텐츠를 과연 신뢰할 수 있을까요 ? 이번 발표에서는 서로 연관된 두 가지 연구를…
- B5 직무·역량 변화: 따라서 고품질의 오답 보기를 설계하는 것은 훨씬 더 어려워지며, 기존의 확립된 과목들과는 달리 AI 교육은 널리 사용되는 교과서나 일관된 교육과정이 없기 때문에, 이처럼 빠르게 변화하고 다양한 학습 환경에서는 전통적인 객관식 문제 설계 전략이 제대로 작동하지 않는 경우가 많습니다.
- B1 디지털·AI 기술의 활용: 그래서 가장 중요한 질문은 생성형 AI를 사용하여 특히 지식, 컴퓨터 과학, 수학과 같은 과목에서 교육적으로 타당하고 효과적인 오답 보기를 어떻게 생성할 수 있느냐는 것입니다.
- 수치 주장: 저희는 학생들이 약 250분 동안 감정 분석과 대수학을 이용한 AI 의사 결정 모델링을 배우는 온라인 고등학교 AI 강좌를 개발했습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Cohere/Zifeng_Liu_-_Human–AI_Collaboration_in_Educational_Assessmen__X84gmuT9RI8.md`

**51. [O-Ring Automation & the Economics of Bicycles for the Mind with Avi Goldfarb](https://www.youtube.com/watch?v=uUUBApVevNI)** — Cohere · 파운데이션 모델 · CA · 2026-06 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요 여러분, 함께해 주셔서 감사합니다. 오늘 저희를 찾아주신 손님, 아비 골드파 씨를 모시게 되어 정말 기쁩니다. 아비는 토론토 대학교 교수이며, 인공지능이 경제의 일자리에 미치는 영향을 연구하는 선도적인 경제학자 중 한 명으로, 이 주제에 대해 두 권의 저서를 포함하여 폭넓게 저술했습니다. 음, 그의 연구는 인공지능이 경제의 일자리에 미치는 영향에 대해 가장 엄밀한 분석을 …
- B7 성과: 운영효율: 이 두 논문 모두에서 해당 결과에 대한 중요한 단서가 있는데, 그것은 컴퓨터가 생산성을 향상시킨 것은 맞지만 , 그 생산성 향상은 주로 1990년대 와 2000년대 초반에 발생했다는 것입니다.
- B4 디지털 채널: 콜센터에 미치는 영향에 대해 이야기할 때, 특정 연구 결과와 주변 환경만을 고려하는 것이 아니라, 경제 연구에서 흔히 다루는 것처럼, 어느 정도까지 복잡하게 접근해야 하고, 언제쯤 단순화를 멈춰야 할까요?
- 수치 주장: 그러니까 1970년대, 80년대, 90년대, 그리고 2000년대 초반을 생각해 보면, 이러한 기술을 도입한 근로자와 기업의 생산성이 향상되었다는 것을 알 수 있습니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Cohere/O-Ring_Automation_&_the_Economics_of_Bicycles_for_the_Mind_w__uUUBApVevNI.md`

**52. [ML Summer School 2026 - Methodologies for Improving the Quality of AI Tutoring In K-12 Education](https://www.youtube.com/watch?v=hbqSsYM5nbA)** — Cohere · 파운데이션 모델 · CA · 2026-07 · ko · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 오늘 연사로 오신 우데시 님을 환영합니다. 우데시 님은 칸 아카데미의 소프트웨어 엔지니어이십니다. 이제 다음 연사에게 마이크를 넘기겠습니다. 네, 소개 감사합니다. 라프 님, 안녕하세요. 여러분, 이렇게 함께하게 되어 기쁩니다. 좋은 아침, 좋은 저녁, 좋은 오후입니다. 어디에 계시든요. 오늘은 슬라이드쇼 모드로 전환해서 제 화면을 보여드리겠습니다. 잘 보이시죠? 오늘은 칸 아카데미…
- B1 디지털·AI 기술의 활용: 음, 저는 LLM(학습 석사)이 충분히 강력해져서 그 안에 교육학적 정보가 담겨 있고, 'Y를 보면 X를 하라'라고 명시적으로 지시하지 않아도 된다고 생각합니다.
- B7 성과: 운영효율: 그래서 우리는 여러 대화에 걸쳐 이를 수행할 수 있었고, 인지적 참여도가 5% 향상되는 것을 확인했는데, 이는 엄청난 결과입니다.
- 수치 주장: 그리고 대규모 언어 모델의 등장, 특히 2022년 11월 Chart GDP 출시와 함께 인기를 얻게 된 것을 보면, 이 기술을 선한 목적으로 활용할 수 있는 분야 중 하나라고 생각합니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Cohere/ML_Summer_School_2026_-_Methodologies_for_Improving_the_Qual__hbqSsYM5nbA.md`

---

## Cursor


**53. [Opening Keynote, Michael Truell | Compile 26](https://www.youtube.com/watch?v=fWa7uxyhVDE)** — Cursor · 엔터프라이즈 앱 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 오늘 이 자리에 모인 분들과 우리 앞에 있는 공동체를 보니, 저희 회사가 처음 시작했을 때가 떠오릅니다. 그래서, 여러분 중에 Cursor가 어떻게 시작되었는지, 첫 번째 버전은 어떤 모습이었는지, 그리고 언제 출시되었는지 아는 분이 얼마나 될지 모르겠습니다. 하지만 저희 AI 회사는 2022년 1월이라는 아주 먼 옛날부터 존재해 왔습니다. 그때부터 이 모든 것들을 개발하기 시작했고, 커서의…
- B1 디지털·AI 기술의 활용: 저희의 궁극적인 목표는 개발 환경을 갖춘, 이러한 모든 새롭고 놀라운 기능을 수행할 수 있는 믿음직한 클라우드 에이전트, 즉 팀원을 여러분 모두에게 제공하는 것입니다 .
- B2 파괴: 소비자 행동·기대: 즉, 상담원이 어떤 내용을 변경했는지 사용자에게 정확하게 보여주는 훌륭한 사용자 경험(UX)을 갖추는 것도 중요합니다 .
- 수치 주장: 그리고 저희가 2023년과 2024년에 출시한 탭 모델 시리즈는 , 은밀하게도 그 기간 동안 가장 인기 있는 코딩 모델 중 하나였고, 전 세계 코드의 상당 부분을 작성하는 데 사용되었다고 생각합니다.
- 교량: — · 기술: 프로토콜·표준 · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Cursor/Opening_Keynote,_Michael_Truell_Compile_26__fWa7uxyhVDE.md`

**54. [Running 128 Coding Agents at Once](https://www.youtube.com/watch?v=-jnwTZ789V0)** — Cursor · 엔터프라이즈 앱 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 그리고 지금 에이전트가 실행 중입니다. 설정 과정에서 알게 된 사실입니다. 오늘 당신은 무엇을 하고 있나요? [웃음] 어, 해리가 언급했듯이 저희는 최근에 KB 캐시 압축 작업을 좀 했습니다. 음, 그래서 KB 캐시를 압축해서 컨텍스트 윈도우를 확장하는 방법을 알아내려고 합니다. 음, 그러니까 저희는 언제든지 이 업무에 투입되는 상담원이 대략 64명에서 128명 정도 됩니다. 지금 컴퓨터로 …
- B1 디지털·AI 기술의 활용: 그리고 제가 생각하기에 작곡가 모델 의 장점 중 하나는 클로드나 GPT 같은 경우, 챗봇처럼 UI를 사용하고, 파워포인트 슬라이드를 만들고, 이런 모든 것들을 할 수 있도록 훈련받아야 한다는 점입니다.
- B2 파괴: 소비자 행동·기대: 특정 제품을 개발하고 해당 제품 내에서 특정 작업을 수행하기 위해 LLM을 사용하는 경우 , 예를 들어 클로즈드 소스 방식의 프론티어 모델을 사용하는 경우, 해당 모델에 내장된 UX 패턴에 갇히게 되는 경우가 있습니다 .
- 수치 주장: 네, 레오폴드가 언어 모델 개발 과정에서 발생한 여러 문제점들에 대해 많이 이야기했는데, 제 생각에는 지난 1~2년 동안 간과되기 쉬웠던 가장 큰 문제점 중 하나는 모델이 언제 사용자에게 질문을 해야 하는지, 그리고 언제 질문이 불분명한지 판단할 수 있도록 훈련시키는 능력이라고 생각합니다.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습 · 추론 최적화 · 코딩 에이전트
- 원문: `transcripts/channels/Cursor/Running_128_Coding_Agents_at_Once__-jnwTZ789V0.md`

---

## DX


**55. [The AI adoption playbook: Lessons from Microsoft's internal strategy](https://www.youtube.com/watch?v=c51ToE4pPpY)** — DX · (미분류) · — · 2026-08 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽
- 개요: AI에 대한 과도한 기대는 여러모로 도입의 가장 큰 장벽입니다. 개발자의 30%는 AI에 대한 가장 큰 걱정으로 AI가 기대에 미치지 못할 것이라는 점을 꼽습니다. AI가 모두의 관심사로 떠오르면서 기대치가 높아지고, 결국 " 그렇게 좋을 리가 없어. 시도조차 하지 않겠다"라고 생각하거나, 한 번 사용해 보고 기대했던 만큼 혁신적이지 않다고 생각하며 " 다시는 사용하지 않겠다"라고 결심하게 …
- B5 리더십·CDO/CAIO: 그런 다음 리더십 팀 관리자들이 개발자들의 일상 업무와 연관시켜 메시지를 전달함으로써 사용률을 높이려고 노력해야 합니다.
- B3 전략적 대응: 최고 경영진의 지지와 홍보, 그리고 실제로 AI 도구를 사용하는 사람들에 대한 정보도 확보했습니다.
- 수치 주장: 개발자의 30%는 AI에 대한 가장 큰 걱정으로 AI가 기대에 미치지 못할 것이라는 점을 꼽습니다.
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/2026-08-04/The_AI_adoption_playbook_Lessons_from_Microsoft's_internal_s__c51ToE4pPpY.md`

---

## Databricks


**56. [Sam Altman and Ali Ghodsi: OpenAI + Databricks, AI Agents in the Enterprise, The future of GPT-OSS](https://www.youtube.com/watch?v=gz1sOEETcgE)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 오늘 웨비나에 참석해 주셔서 감사합니다 오늘 이 자리에는 저희 CEO이신 알리 고드시 님과 OpenAI의 CEO이신 샘 알트맨 님이 나와 계십니다 두 분 모두 이 자리에 함께해 주셔서 정말 감사드립니다 좋네요 네, 정말 기대됩니다 네, 그럼 시작해보겠습니다 즐겁고 의미 있는 시간이 되길 바랍니다 아시다시피 최근 Databricks와 OpenAI에서 OpenAI 모델을 Databricks와 A…
- B1 디지털·AI 기술의 활용: 그 부분에 대해서 저희는 긴밀하게 협력해 왔는데요 프라이버시와 보안을 처음 설계 단계부터 고려해 왔습니다 그래서 이번 협력과 통합도 적절한 가드레일을 갖추는 것을 전제로 기업 환경에서 발생하는 모든 활동에 대한 감사 로그를 남겨 모델이 정확히 무엇을 했는지 추적할 수 있도록 했습니다 다시 돌아가서 그 과정을 확인할 수 있고 접근 제어를 갖추는 것입니다 이런 것들은 기업 입장에서는 너무 기본적이라서 당연하게 여겨질 수도 있는 것이지만 예를 들어 모델의 답변이 브랜…
- B4 가치네트워크·생태계: 모든 엔터프라이즈 고객사가 OpenAI를 사용하고 싶어 합니다 모델을 활용하고 자사 데이터에 적용하고 싶어 하죠 아시다시피 두 가지를 함께 작동시키는 것이 간단한 일은 아닙니다 데이터는 민감한 정보이므로 프라이버시와 감사 GDPR 준수를 필요로 합니다 그럼에도 고객들은 모델을 활용해 에이전트를 만들고 인사이트를 얻고 싶어 합니다 따라서 압도적인 고객의 수요 때문에 이뤄질 수 있었습니다 이렇게 협력하게 되어 기쁩니다 OpenAI에서는 엔터프라이즈에 가장 초점이 쏠…
- 수치 주장: 모든 엔터프라이즈 고객사가 OpenAI를 사용하고 싶어 합니다 모델을 활용하고 자사 데이터에 적용하고 싶어 하죠 아시다시피 두 가지를 함께 작동시키는 것이 간단한 일은 아닙니다 데이터는 민감한 정보이므로 프라이버시와 감사 GDPR 준수를 필요로 합니다 그럼에도 고객들은 모델을 활용해 에이전트를 만들고 인사이트를 얻고 싶어 합니다 따라서 압도적인 고객의 수요 때문에 이뤄질 수 있었습니다 이렇게 협력하게 되어 기쁩니다 OpenAI에서는 엔터프라이즈에 가장 초점이 쏠…
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Sam_Altman_and_Ali_Ghodsi_OpenAI_+_Databricks,_AI_Agents_in___gz1sOEETcgE.md`

**57. [How Databricks + AWS Help Enterprises Take GenAI to Production](https://www.youtube.com/watch?v=Q6jRdpF6yXE)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 제 이름은 크레이그 와이입니다. 저는 Data Bricks에서 AI 제품 관리를 담당하고 있으며, 이곳에 오게 되어 정말 기쁩니다. AWS 팬 여러분께 말씀드리자면, 저는 SageMaker의 창립자이기도 합니다 . 그래서, 음, 그건 옛날에 정말 좋은 시절이었죠. [웃음] 하지만 저는 지난 몇 년 동안 Data Bricks에서 일하면서 고객들이 Genai를 도입하도록 적극적으로 …
- B1 디지털·AI 기술의 활용: 즉, 에이전트 브릭을 사용하여 RAG 시스템을 구축할 경우, 단순히 기본적인 RAG 시스템을 얻는 것이 아니라, 최근 4~6주 동안 발표된 최신 기술, 즉 관련 논문에 나온 내용이 적용된 시스템을 얻게 되는 것입니다.
- B4 가치네트워크·생태계: 그래서, 아시다시피, 저는 AWS 고객들이 데이터 브릭을 사용하여 단순히 데이터 브릭 내에서 또는 데이터 브릭 위에서 작업을 오케스트레이션하고 실행하는 것뿐만 아니라, AWS 생태계 전체를 활용하는 모습을 보는 것이 정말 흥미롭다고 생각합니다.
- 수치 주장: 즉, 에이전트 브릭을 사용하여 RAG 시스템을 구축할 경우, 단순히 기본적인 RAG 시스템을 얻는 것이 아니라, 최근 4~6주 동안 발표된 최신 기술, 즉 관련 논문에 나온 내용이 적용된 시스템을 얻게 되는 것입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/How_Databricks_+_AWS_Help_Enterprises_Take_GenAI_to_Producti__Q6jRdpF6yXE.md`

**58. [Databricks x Palantir | Partnership Deep Dive](https://www.youtube.com/watch?v=BsSwqYuok1A)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-01 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 저는 채드 월러스입니다. 저는 Palanteer에서 건축가로 일하고 있습니다 . 안녕하세요, 저는 베나부드입니다. 저는 Data Bricks의 아키텍트입니다. 오늘은 데이터 브릭과 팔란티어 파트너십에 대해 이야기해 보겠습니다 . 따라서 데이터 브릭과 Palunteer는 함께 사용할 때 더 효과적입니다. 그게 무슨 뜻인가요? 정말, 저희도 이 문제에 대해 생각해 봅니다. 어떻게 하…
- B2 파괴: 데이터 가용성: Foundry는 인증을 위해 서비스 주체를 사용하여 Unity 카탈로그에 연결하고, "Unity 카탈로그에 이 카탈로그, 이 스키마, 이 테이블 이름에 있는 데이터 자산을 Foundry 에서 사용하고 싶습니다.
- B4 가치네트워크·생태계: 음, 하지만 제가 여기서 정말로 강조하고 싶은 것은 저희가 파트너십을 발표한 3월 13일 이후 지난 6개월 동안 많은 제품 통합 작업을 진행해 왔으며, 이러한 작업의 상당 부분은 고객의 요구에 따라 이루어졌다는 것입니다 .
- 수치 주장: 음, 하지만 제가 여기서 정말로 강조하고 싶은 것은 저희가 파트너십을 발표한 3월 13일 이후 지난 6개월 동안 많은 제품 통합 작업을 진행해 왔으며, 이러한 작업의 상당 부분은 고객의 요구에 따라 이루어졌다는 것입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Databricks/Databricks_x_Palantir_Partnership_Deep_Dive__BsSwqYuok1A.md`

**59. [Dario Amodei and Ali Ghodsi: Anthropic + Databricks, AI Agents in the Enterprise, AI Scaling Laws](https://www.youtube.com/watch?v=MTsoRWPS46o)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 엄청난. 앤트로픽의 CEO이신 다리오 아마데님을 만나 뵙게 되어 정말 기쁩니다. 저희는 정말 멋진 파트너십을 맺었는데, 이에 대해 이야기해 보려고 합니다. 아, 시간 내주셔서 감사합니다. 음, 몇 가지 여쭤보고 싶은 게 있어요. 당신은 인공지능의 미래에 대한 비전을 많이 이야기해 오셨습니다 . 어, 당신은 ' 사랑의 은혜 기계들'이라는 책을 쓰셨죠. 음, 인공지능의 미래에 대한 당신의 비전을…
- B4 가치네트워크·생태계: 데이터베이스를 통해 데이터에 접근하고, 다양한 검색 방식을 통해 데이터에 접근하는 것, 그리고 저는 이러한 파트너십을 통해 많은 시너지 효과가 있을 거라고 생각합니다 .
- B1 디지털·AI 기술의 활용: 음, 이번 파트너십에 대해 말씀드리자면, 저희 고객들이 데이터 브릭 내에서 클라우드 모델에 기본적으로 접근할 수 있게 되어 정말 기쁩니다.
- 수치 주장: 그리고 아시다시피 인터페이스는 꽤 간단하지만, 클로드 코드를 출시한 지 며칠 만에 거의 10만 명에 달하는 사람들이 사용해봤다는 사실을 알게 되었습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Databricks/Dario_Amodei_and_Ali_Ghodsi_Anthropic_+_Databricks,_AI_Agent__MTsoRWPS46o.md`

**60. [Getting Started with Unity Catalog: A Step-by-Step Databricks Demo](https://www.youtube.com/watch?v=ORMH3pQG8yM)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: [음악] 데이터 및 AI를 위한 통합 관리 솔루션인 Databricks용 Unity Catalog에 오신 것을 환영합니다 . 생성형 인공지능의 빠른 도입은 신뢰할 수 있고 관리되는 데이터에 대한 전례 없는 요구를 야기합니다. 이 새로운 시대에는 강력한 데이터 분류, 관리, 검색 및 평가에 대한 필요성에서 시작하는 현대적인 접근 방식이 요구되며, 이 모든 것이 하나의 카탈로그에서 통합된 검색을…
- B1 디지털·AI 기술의 활용: 이를 통해 데이터 엔지니어는 특정 클러스터 구성을 프로비저닝하고, 고객 이탈 예측 머신러닝 모델 학습과 같은 복잡한 작업에 필요한 정확한 인스턴스 유형과 라이브러리를 선택할 수 있습니다.
- B2 파괴: 데이터 가용성: 델타 공유를 통해 플랫폼이나 클라우드 환경에 관계없이 모든 외부 파트너와 실시간 데이터 자산을 안전하게 공유할 수 있습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Getting_Started_with_Unity_Catalog_A_Step-by-Step_Databricks__ORMH3pQG8yM.md`

**61. [Building Enterprise-Ready Agents using Agent Bricks](https://www.youtube.com/watch?v=sjXgUdovOdM)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 상황이 정말 좋아 보이고, 매우 낙관적입니다. 매일 새로운 사람들이 정말 흥미로운 무언가를 발표하며 갑자기 모든 소프트웨어 개발자 등을 대체할 수도 있지만, 기업용 AI 분야에서는 상황이 완전히 다릅니다. AI 거버넌스, 개인정보 보호 등 모든 것을 고려하는 기업은 그 기업, 리더십, 그리고 팀의 성숙도를 보여줍니다. 여기 계신 분들 중에 업무에서 AI 에이전트나 그와 관련된 일을 하시는 분…
- B1 디지털·AI 기술의 활용: 그러니까 2~3년 전만 해도 AI 에이전트는 거의 없었고, 적어도 오늘날 우리가 알고 있는 형태의 AI 에이전트는 2024년에 등장해서 2025년에 급격히 증가했습니다.
- B8 부정 성과: 보안·프라이버시: 하지만 여기서 중요한 점은 AI 거버넌스, 개인정보 보호 등 모든 것을 고려하는 기업은 그 기업, 리더십, 그리고 팀의 성숙도를 보여준다는 사실입니다.
- 수치 주장: 다른 하나는 2025년 1월부터, 즉 작년 한 해 동안 인공지능 거버넌스와 보안에 대한 투자가 7배 증가했다는 것입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Building_Enterprise-Ready_Agents_using_Agent_Bricks__sjXgUdovOdM.md`

**62. [Building Trustworthy, High-Quality AI Agents with MLflow](https://www.youtube.com/watch?v=NcHCkPMww7Q)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 새로운 에이전트를 출시할 때마다 위험이 따릅니다. 개인 식별 정보(음악 데이터) 유출 등으로 규정 준수에 문제가 생길 위험이 있으며, 심지어는 불쾌감을 줄 수 있는 사용자 정보를 제공할 수도 있습니다 . 무슨 일이 일어날지 아무도 몰라요. 이 AI 게이트웨이는 권한, 속도 제한 및 입력 안전장치라는 세 가지 가장 중요한 부분을 제공합니다. 이 세 가지가 모두 갖춰지면 적절한 비용 관리와 접근…
- B1 디지털·AI 기술의 활용: 그 이후로 머신 러닝 플로우는 AI 운영을 위한 최대 규모의 오픈소스 플랫폼으로 발전하여 개발자들이 통합 플랫폼에서 고품질 AI 에이전트와 머신 러닝 모델을 구축할 수 있도록 지원해 왔습니다.
- B4 가치네트워크·생태계: 따라서 오늘 여러분이 구축하는 플랫폼은 대규모 언어 모델, 에이전트 제작 프레임워크 및 프로그래밍 언어를 포함하는 더 넓은 생태계와 호환될 것입니다.
- 수치 주장: 그래서 저희 Databricks는 8 년 전부터 머신러닝 워크플로우 구축을 시작했습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Building_Trustworthy,_High-Quality_AI_Agents_with_MLflow__NcHCkPMww7Q.md`

**63. [Databricks on Databricks: How Marketers Use Data 3x More with Genie, an AI Analytics Assistant](https://www.youtube.com/watch?v=zWHzl5tEW8A)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 대부분의 마케팅 팀은 데이터 기반이라고 말하지만, 실제로 적시에 적절한 데이터를 얻는 것은 말처럼 쉽지 않습니다. 오늘은 Databricks 마케팅 팀이 의사 결정에 데이터를 세 배 더 많이 활용하도록 도운 방법을 공유하겠습니다 . 안녕하세요 여러분. 저는 데이터브릭스의 마케팅 기술 담당 부사장인 엘리자베스 돕스입니다 . 저희 팀의 임무는 마케팅 조직이 데이터를 활용하여 더 나은 결정을 더 …
- B5 조직구조 변화: 데이터 거버넌스, 정의, 민감한 데이터에 대한 역할 기반 접근 제어를 중앙 집중화함으로써 제어권을 희생하지 않고도 인사이트에 대한 접근성을 확장할 수 있습니다 .
- B7 성과: 운영효율: 마케터들은 답변을 기다리는 시간을 줄이고 답변에 따라 행동하는 시간을 늘려, 캠페인 조정 속도를 높이고, 세분화를 더욱 효과적으로 수행하며, 조직 전체에 걸쳐 예산을 더욱 효율적으로 배분할 수 있습니다.
- 수치 주장: 그리고 우리가 약 3년 전에 이 여정을 시작했을 때, 첫 번째 단계는 회사에서 사용할 수 있도록 더 큰 Databricks 레이크하우스 내에 구축된 통합 관리 고객 데이터 기반인 마케팅 레이크하우스를 만드는 것이었습니다 .
- 교량: — · 기술: 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Databricks_on_Databricks_How_Marketers_Use_Data_3x_More_with__zWHzl5tEW8A.md`

**64. [Defending against a tidal wave of AI attacks with Lakewatch, the agentic security Lakehouse](https://www.youtube.com/watch?v=3GhVeYY3Bmo)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-06 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: Hello everyone. I'm Andrew. I'm excited to talk to you today about LakeWatch, which is our new security lakehouse product. We announced this just about 2 months ago at the RSA conference. And this is an area that's reall…
- B1 디지털·AI 기술의 활용: We probably all read about the latest LLM models being able to find previously unknown vulnerabilities in just about any piece of software out there today.
- B8 부정 성과: 보안·프라이버시: They ask it to go and search for sensitive data and in the end the hackers walk away with 200 million personnel records and gigabytes of sensitive data.
- 교량: — · 기술: LLM 모델 · 에이전트 프레임워크 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Defending_against_a_tidal_wave_of_AI_attacks_with_Lakewatch,__3GhVeYY3Bmo.md`

**65. [Introducing LTAP (Lake Transactional/Analytical Processing): a new data processing architecture](https://www.youtube.com/watch?v=9J2-PovJppA)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 여러분은 빌랄로부터 간소화된 데이터 엔지니어링에 대한 이야기를 들었고, 저는 분석을 어떻게 통합할지에 대해 이야기했으며, 모더 나이저 OLTP의 니키타도 소개했습니다. 하지만 솔직히 말해서, 가장 큰 문제점 중 하나는 여전히 해결되지 않은 한 가지 큰 문제가 있다는 것입니다. 바로 애플리케이션들이 데이터를 가장 먼저 저장하기 시작하는 거대한 OLTP 데이터베이스가 존재한다는 점입니다. 그리고…
- B1 디지털·AI 기술의 활용: 니키타가 이미 보여드린 아키텍처 다이어그램을 보시면, 데이터를 실제 행 기반 형식으로 데이터 레이크에 기록하는 세이프 키퍼와 페이지 서버가 있는데, 바로 거기에 해결책이 있습니다.
- B2 파괴: 데이터 가용성: 음, 보시다시피 이 데이터는 전혀 오래된 정보가 아닌 매우 실시간 데이터이며, TPS(초당 트랜잭션 수)에 아무런 영향을 미치지 않았습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Databricks/Introducing_LTAP_(Lake_TransactionalAnalytical_Processing)_a__9J2-PovJppA.md`

**66. [Unlocking agentic data engineering with Lakeflow + Genie](https://www.youtube.com/watch?v=0WDGu-IPmZM)** — Databricks · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 무대에 오신 것을 환영합니다, 데이터브릭스 제품 관리 수석 이사 빌랄 아슬람입니다. [소리 지르며] 좋은 아침이에요. 좋은 아침이에요. Lakeflow에 대해 이야기해 드리려고 하는데, 먼저 간단히 말씀드릴 게 있습니다. 저는 2년 전에 이 보라색 재킷을 입고 레이크플로우에 대해 이야기했었어요. 작년에는 이 옷을 입지 않았는데, 가장 많이 받은 피드백은 다시 출시해 달라는 것이었습니다. 자,…
- B5 직무·역량 변화: 데이터 엔지니어로서 이 복잡하고 통합되지 않은 아키텍처에 중요한 요소들이 많이 빠져 있다는 것을 본능적으로 알고 있으면서도 모든 것을 버전 관리하고 싶어 하는데, 이 스택에서는 일부 요소는 버전 관리가 가능하고 다른 요소는 불가능합니다.
- B1 디지털·AI 기술의 활용: 따라서 Genie Zero Ops는 탐지를 위해 테이블별 머신러닝 모델을 자율적으로 구축하고 지속적으로 미세 조정합니다.
- 수치 주장: 그리고 지금 우리는 수백 개의 파트너와 다양한 도구를 활용하고 있습니다.
- 교량: — · 기술: 거버넌스·평가 도구
- 원문: `transcripts/channels/Databricks/Unlocking_agentic_data_engineering_with_Lakeflow_+_Genie__0WDGu-IPmZM.md`

---

## Dust - Transform how work gets done.


**67. [AI Agents: getting to 90%, the AI adoption playbook for Enterprise](https://www.youtube.com/watch?v=01NYw3PzqiI)** — Dust - Transform how work gets done. · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 제목을 보시면 아시겠지만, 오늘 이 강연은 아주 자세하고 기술적인 내용을 기대하고 오신 분들에게는 적합하지 않을 겁니다. 오늘 제가 정말 집중하고 싶은 것은 인공지능의 중요한 부분 중 우리가 충분히 이야기하지 않는 부분이 있는데, 솔직히 말해서 그 부분이 가장 중요한 부분이 되고 있다는 점입니다. 바로 우리 인간이죠. 오늘 이 글에서는 인공지능을 전반적으로 도입하는 가장 좋은 방법에 대해 이…
- B1 디지털·AI 기술의 활용: 그래서 그들의 AI 도입률은 55%였는데, 다른 많은 회사에서는 이미 매우 높은 수치였지만, 상향식으로 이러한 구조가 도입된 후 30일 만에 업무 공간 전체에 걸쳐 AI 에이전트 도입률을 90%까지 끌어올릴 수 있었습니다.
- B7 성과: 운영효율: 왜냐하면 시간 절약이라는 지표 자체만으로는 실질적인 성과, 즉 규모 확장, 고객 수 증가, 고객과의 접점 확대 등과 같은 결과를 파악하는 데 큰 도움이 되지 않기 때문입니다 .
- 수치 주장: 왜냐하면 AI 에이전트를 구축하기 위해 에이전트 기반 워크플로를 시도한 파일럿 프로젝트의 95%가 제대로 작동하지 않았기 때문입니다.
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/2026-07-28/AI_Agents_getting_to_90%,_the_AI_adoption_playbook_for_Enter__01NYw3PzqiI.md`

---

## ElevenLabs


**68. [Adam Evans at the ElevenLabs Summit](https://www.youtube.com/watch?v=L-I4WMzFjtM)** — ElevenLabs · 생성 미디어 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 애덤, 팔런티어 시절 이후로 정말 바쁘게 지내셨군요. 어, 당신은 세일즈포스에 두 회사를 매각했잖아요. 현재 당신은 세일즈포스에서 AI 및 에이전트 포스 부문을 총괄하고 있으며, 빅토리아가 언급했듯이 타임지가 선정한 AI 분야에서 가장 영향력 있는 100인에 이름을 올렸습니다. 어떻게 세일즈포스에서 AI를 이끌게 되셨는지 모두가 이해할 수 있도록 설명해 주시면 감사하겠습니다. 당신의 여정에 …
- B1 디지털·AI 기술의 활용: 제가 사는 샌프란시스코 베이 지역에서는 마크 베니오프를 비롯한 세일즈포스가 데이터 클라우드와 신뢰 계층의 중요성에 대해 수년간 이야기해 온 것을 느끼기 때문입니다 .
- B4 디지털 채널: 음, 우리 고객들을 다시 생각해 보면, 웹사이트와 디지털 채널에서 음성 기능을 제공하는 것, 즉 WebRTC를 통해 상호 작용할 수 있는 가능성을 열어주는 것에 대해 이야기해 보겠습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/ElevenLabs/Adam_Evans_at_the_ElevenLabs_Summit__L-I4WMzFjtM.md`

**69. [How BCG, Naturgy, and Konecta Are Deploying AI Agents in Production | ElevenLabs Summit London 2026](https://www.youtube.com/watch?v=TPV30xP1gyM)** — ElevenLabs · 생성 미디어 · US · 2026-03 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. 오늘 우리는 어떻게 지내고 있나요? 좋은? [환호하며] 아주 좋아요. 런던이 우리 회사의 글로벌 본사가 된 것을 보니 정말 놀랍습니다. 정말 반갑고 친숙한 얼굴들이 많네요. 와주셔서 다시 한번 감사드립니다. 음, 지금 저희는 특별한 세션을 준비하고 있습니다. 인공지능이 현실 세계에 도입되고 있는 상황에서, 각기 다른 산업 분야의 리더 세 분을 모시고 이에 대해 더…
- B7 성과: 운영효율: 마티가 개막식에서 언급했듯이, 대기 시간 단축, 연중무휴 24시간 지원, 다국어 지원 등 다양한 이점을 누릴 수 있을 것입니다 .
- B1 디지털·AI 기술의 활용: 그래서 저희는 고객과의 일상적인 소통 대부분을 AI 에이전트를 통해 처리하고, 고객에게 매우 균일한 경험을 제공할 수 있다면, AI가 얼마나 놀라운 결과를 가져올 수 있는지 알게 될 것이라고 생각합니다.
- 수치 주장: 도입률이 40%를 넘는 수치를 보이고 있지만, 기업들은 기본적으로 세 가지를 하고 있습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/ElevenLabs/How_BCG,_Naturgy,_and_Konecta_Are_Deploying_AI_Agents_in_Pro__TPV30xP1gyM.md`

**70. [Sequoia's Doug Leone on Building Enduring Companies in the AI Era | ElevenLabs Summit London 2026](https://www.youtube.com/watch?v=afSmwxT0Y3o)** — ElevenLabs · 생성 미디어 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 세쿼이아 캐피털의 더그 레오네와 일레븐 랩스 공동 창립자 마티 스타니셰프스키를 환영합니다. [음악] 마지막 세션까지 함께해 주셔서 정말 감사합니다. 더그 레오네 씨가 이 자리에 함께해 주셔서 정말 기쁩니다. 제가 온라인에서 볼 수 있었던 사람입니다. 저는 관객석에서 공연을 관람할 기회가 있었는데, 오늘 이렇게 더그 씨를 인터뷰할 수 있게 되어 정말 기쁩니다. 그럼 더그를 간단히 소개하겠습니다…
- B3 전략적 대응: 만약 제가 귀사의 이사회 구성원이라면 (이사회 구성원이 아닌데다가 누가 이사회에 있는지도 모른다면), 저는 귀사의 매출 성장률을 현재 수준에서 5배로 끌어올린 CEO를 이사회에 영입하고 싶습니다 .
- B1 디지털·AI 기술의 활용: 그리고 익명의 벤처 투자 회사들이 몇몇 있는데, 이들은 SaaS 같은 시장의 막바지에 나타나서 모든 것에 투자하다가 결국 큰 손실을 봅니다.
- 수치 주장: 기술이 현실로 바뀌면서, LAN 환경에서 5년 , 인터넷 환경에서 3년이 걸리던 것이 갑자기 1~2 년으로 단축되었습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/ElevenLabs/Sequoia's_Doug_Leone_on_Building_Enduring_Companies_in_the_A__afSmwxT0Y3o.md`

**71. [Deploying AI at Enterprise Scale - ElevenLabs Summit](https://www.youtube.com/watch?v=HdelDovObRU)** — ElevenLabs · 생성 미디어 · US · 2026-08 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B8 부정 성과
- 개요: 엄청난. 고마워요, 빅토리아. 오늘 아침은 정말 대단하네요 . 네, 시간 내어 참석해 주셔서 감사합니다. 이번 시간에는 기업 환경에서 대규모 AI 프로덕션 배포에 대해 이야기해 보겠습니다. 지난 한 해 동안 인공지능 데모를 많이 접했다는 건 우리 모두 알고 있습니다 . AI를 시연하는 것은 쉽습니다. 실제 기업 환경에서 대규모로 이를 구현하는 것은 매우 어렵습니다. 그래서 오늘 우리가 이야기…
- B1 디지털·AI 기술의 활용: 하이퍼스케일러, 신뢰 및 안전 제공업체, 그리고 다양한 파트너, 통합 업체, LLM, 물론 성우, 특정 산업 분야 전문 제공업체와 함께 일하는 이 생태계 여정에 참여하게 되어 정말 영광스럽게 생각합니다 .
- B4 가치네트워크·생태계: 하이퍼스케일러, 신뢰 및 안전 제공업체, 그리고 다양한 파트너, 통합 업체, LLM, 물론 성우, 특정 산업 분야 전문 제공업체와 함께 일하는 이 생태계 여정에 참여하게 되어 정말 영광스럽게 생각합니다 .
- 수치 주장: 우리 모두가 들어봤을 법한 이야기 ​​중 하나는 MIT 연구인데, 이 연구에 따르면 현재 Gen AI 배포의 95%가 투자 대비 수익(ROI)을 전혀 얻지 못하고 있다고 합니다 .
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/2026-08-03/Deploying_AI_at_Enterprise_Scale_-_ElevenLabs_Summit__HdelDovObRU.md`

---

## GOTO Conferences


**72. [How to Lead Your Organisation’s AI-Transformation • Rasmus Lystrøm • YOW! 2024](https://www.youtube.com/watch?v=1uJZlKig0Tk)** — GOTO Conferences · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 모두 환영합니다. 이것은 조직의 AI 전환 전략, 역량, 문화 등을 이끌어가는 방법입니다. 음, 제가 발표를 마친 후에 '아니요'라는 말을 덧붙였어요. 발표 내용에 ' 아니요'가 많이 들어가 있어서요. 음, 제목이 너무 길어서 지루할 수도 있겠네요. 그래서 제 생각에는 그게 공통적인 주제였던 것 같아요. 어이임 씨도 같은 병을 앓았어요 . 자막을 만들어 봅시다. 자, 오늘은 제가 어떻게 걱정…
- B1 디지털·AI 기술의 활용: 그러니까 인공지능을 도입하기 전에 해결했어야 할 큰 문제들이 있었고, 클라우드 컴퓨팅이나 다른 어떤 기술을 도입하기 전에도 해결했어야 할 문제들이었습니다.
- B7 성과: 운영효율: 제가 Something Blue Ops에서 본 것처럼, 생성형 인공지능이 소프트웨어 개발자의 성과에 미치는 영향은 생산성을 4% 향상시키며, 중간 정도 사용량의 사용자들도 높은 성과를 보이는 것으로 나타났습니다.
- 수치 주장: 또 다른 문제는 제가 함께 일하는 회사들의 80%, 아니 어쩌면 100%가 새로운 플랫폼 도입을 80% 정도만 진행한 상태라는 것입니다 .
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/2026-07-18/How_to_Lead_Your_Organisation’s_AI-Transformation_•_Rasmus_L__1uJZlKig0Tk.md`

---

## GitHub


**73. [Building a privacy-first smart home with Frank Nijhof | Episode 8 | The GitHub Podcast](https://www.youtube.com/watch?v=al-JSC314dA)** — GitHub · 에이전트·개발도구 · US · 2026-01 · ko · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, GitHub의 Andrea입니다. 저희는 GitHub Universe 2025 현장에서 생중계하고 있습니다. 오늘은 플랫폼에서 가장 활발한 오픈 소스 프로젝트 중 하나와 이야기를 나눠보겠습니다 . 2024년 한 해에만 21,000명의 기고자가 참여했습니다. 2025년 수치를 가지고 계신지 모르겠네요. 그 부분은 나중에 자세히 살펴보도록 하겠습니다. 오, 200만 가구 이상이 소프…
- B8 부정 성과: 보안·프라이버시: 이제 사람들은 어시스트를 사용해서 녹음 내용을 다른 사람에게 보내지 않고도 집과 대화할 수 있고, 나중에 그 녹음 내용을 악용해서 뭔가를 팔려고 하는 일도 방지할 수 있죠.
- B1 디지털·AI 기술의 활용: 그러니까 "좋아요, 저는 제 개인 정보 보호 규칙을 알고 있고, 분석 기능이나 Anthropic Cloud, 또는 Google Gemini, 혹은 직접 만든 모델 등 어떤 것도 사용하지 않도록 설정한 OpenAI 계정을 연결하고 싶습니다.
- 수치 주장: 생각해 보면, 2024년에는 개발자가 2만 1천 명 정도 될 거예요.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/GitHub/Building_a_privacy-first_smart_home_with_Frank_Nijhof_Episod__al-JSC314dA.md`

**74. [Inside Octoverse 2025 report: The rise of vibe coding & agentic AI | Episode 7 | The GitHub Podcast](https://www.youtube.com/watch?v=ve-tfDEQOG8)** — GitHub · 에이전트·개발도구 · US · 2026-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 이것은 GitHub [음악] 팟캐스트입니다. 이 프로그램은 [음악] 분야와 GitHub의 오픈 소스 개발자 커뮤니티를 둘러싼 주제, 트렌드, 이야기 및 문화를 다룹니다. 저는 Andrea Griffiths이고, 인터넷에서는 Ala Colombia Dev라는 닉네임을 사용하며 , GitHub에서 선임 개발자 옹호자(Senior Developer Advocate)로 일하고 있습니다. 안녕하세요,…
- B1 디지털·AI 기술의 활용: 어쩌면 저는 비교적 일반적인 비즈니스 제품을 가지고 있고, 거기에 AI 에이전트를 추가하거나 데이터를 처리하는 모델을 추가할 수도 있습니다.
- B5 직무·역량 변화: 그리고 AP, AP, 인도의 경우, 정부가 AI 역량 강화 교육을 실시하고 자국 시스템에 도입하며 인식 개선 프로그램을 많이 만들어 놀라운 성과를 거두었다고 생각합니다.
- 수치 주장: 올해 보고서에서는 6억 3천만 건의 프로젝트에 참여한 1억 8천만 명 이상의 개발자를 추적했습니다 .
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/GitHub/Inside_Octoverse_2025_report_The_rise_of_vibe_coding_&_agent__ve-tfDEQOG8.md`

---

## Google Cloud Tech


**75. [Agent context engineering for production](https://www.youtube.com/watch?v=YKLkHvzjFDk)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [music] &gt;&gt; All right. Hello everyone. Welcome to next and thanks for joining us. My name is George. I'm a product manager at Google and we're at the final stretch here and to talk about an exciting topic on agent c…
- B1 디지털·AI 기술의 활용: They'll be discussing how they developed and applied context engineering techniques using Google Cloud with one of their agents in production today.
- B2 파괴: 소비자 행동·기대: We're moving from models to agents and that shift has enabled us to do quite some amazing things including automating complex long horizon tasks, accelerating software and product development using coding agents and also delivering continuous personalized user…
- 교량: — · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Google_Cloud_Tech/Agent_context_engineering_for_production__YKLkHvzjFDk.md`

**76. [Build AI agents on Cloud Run](https://www.youtube.com/watch?v=zthWHEU3Y7M)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요 여러분. 오늘은 Cloud Run의 에이전트에 대해 이야기하게 되어 매우 기쁩니다. 저는 테일러예요. 저는 클라우드런에서 소프트웨어 엔지니어로 일하고 있습니다 . 오늘은 제품 관리자인 라이언이 함께했습니다 . 그리고 VMO2의 에드입니다. 오늘은 에이전트형 앱에 대해 간단히 이야기해 보겠습니다 . 아시다시피, 에이전트 기반 앱은 에이전트, 도구 및 기타 종속 요소의 모음입…
- B1 디지털·AI 기술의 활용: 이렇게 하면 Google Cloud 프로젝트 전체에서 이러한 워크로드를 관리하고 관찰할 때 클라우드 런에서 실행되는 에이전트 워크로드를 포함할 수 있습니다 .
- B4 디지털 채널: 오늘 여러분은 Lumi 컨택센터에서 고객 지원 문제를 해결하기 위해 Cloud Run과 Gemini를 어떻게 활용했는지에 대한 이야기를 듣게 될 것입니다 .
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 코딩 에이전트
- 원문: `transcripts/channels/Google_Cloud_Tech/Build_AI_agents_on_Cloud_Run__zthWHEU3Y7M.md`

**77. [From prototype to production: 45 minutes to a reliable Gemini Enterprise Agent Platform agent](https://www.youtube.com/watch?v=fkCTifAqVGg)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분. 환영. 오늘 이 세션을 시작하게 되어 매우 기쁩니다. 음, 프로토타입부터 프로덕션까지 안정적인 에이전트를 구축하는 방법에 대해 이야기해 보겠습니다 . 제 이름은 알리벡입니다. 저는 booking.com에서 AI 플랫폼 팀을 이끄는 엔지니어링 매니저입니다. 저는 훌륭한 구글 직원들과 제 동료 마리아와 함께 이 무대에 서게 될 것입니다. 그들은 나중에 자기소개를 할 …
- B1 디지털·AI 기술의 활용: 다음으로, 플랫폼 엔지니어로서 플랫폼 전반에 걸쳐 관찰 가능성 신호를 얻으려면 클라우드 공급업체에서 이러한 신호를 추출하고, 애플리케이션 신호 와 통합되어 실제로 이해하기 쉽고 가치 있는 정보를 제공하는 멋진 대시보드를 구축해야 합니다.
- B4 가치네트워크·생태계: 구글과의 성과 마케팅 파트너십 외에도, 저희는 제미니(Gemini)와 버텍스(Vertex) AI의 역량을 활용하여 더욱 스마트하고 자동화된 고객 경험을 제공하는 에이전트 기반 사용 사례를 구축하고 있습니다.
- 수치 주장: 그리고 2024년 초까지 저희는 핵심 스택을 개편하고 자체 개발 모델을 통합하기 시작했으며, 다중 공급자 환경으로 발전해 나갈 것입니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Google_Cloud_Tech/From_prototype_to_production_45_minutes_to_a_reliable_Gemini__fkCTifAqVGg.md`

**78. [Generative UI for any agent, anywhere: A2UI, AG-UI, MCP Apps, and more](https://www.youtube.com/watch?v=UsMDkEsR-ok)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요 여러분. 함께해 주셔서 대단히 감사합니다 . 제 이름은 앨런입니다. 저를 포함해 여러 동료들이 함께합니다. 이것은 다양한 관계자들이 참여하여 생성형 UI에 대해 논의하는 일종의 파트너십 대화입니다. 이곳에 오게 되어 정말 기쁩니다. 저희는 좋은 콘텐츠를 많이 보유하고 있습니다. 우리는 이 슬라이드들을 모두 넘겨보려고 노력할 겁니다. 오늘은 텍스트 전용 인터페이스에 대한 저…
- B1 디지털·AI 기술의 활용: 저는 20년 동안 풀스택 웹 애플리케이션 개발자로 일하다가 구글 클라우드에서 머신러닝 관련 업무를 했습니다.
- B4 가치네트워크·생태계: 그래서 몇 가지 요구 사항만 충족하면 모든 것이 매우 쉽고 간단하게 작동하며 생태계와 함께 자동으로 계속 발전합니다.
- 수치 주장: 이는 애플 앱스토어가 처음 출시되었을 때 보유했던 사용자 수의 160배가 넘는 수치입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 코딩 에이전트 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Google_Cloud_Tech/Generative_UI_for_any_agent,_anywhere_A2UI,_AG-UI,_MCP_Apps,__UsMDkEsR-ok.md`

**79. [Navigate the agentic shift in software development with Google](https://www.youtube.com/watch?v=Z9Zz75pmOeg)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화
- 개요: 클라우드 넥스트를 잘 활용하고 계시길 바랍니다 . 여러분 모두를 만나서 정말 반가웠어요. 제 이름은 니란잔입니다. 저는 구글에서 개발자 AI 관련 업무를 담당하는 부사장입니다. 오늘 저와 함께 해주신 분은 저희 팀의 엔지니어링 디렉터인 마두라 동료입니다 . 그리고 우리는 함께 구글에서 일어나고 있는 소프트웨어 개발의 주체성 변화에 대해 이야기해 볼 것입니다. 우리 회사는 이 상황에 어떻게 대…
- B8 부정 성과: 보안·프라이버시: 누군가가 파일 내용을 읽는 서버 코드를 작성했는데, 의도 치 않은 보안 문제를 포함하여 여러 가지 문제가 있었습니다 .
- B1 디지털·AI 기술의 활용: 상단의 녹색 영역에는 에이전트 제안 사항이 요약되어 있으며, 아래 섹션에는 설명 및 사전/ 사후 조건을 포함한 실제 API 계약에 대한 자세한 내용이 나와 있습니다.
- 수치 주장: 최근 깃허브에서 발표한 통계에 따르면 병합 풀 요청이 전체 코드에서 약 30% 증가했다고 합니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Google_Cloud_Tech/Navigate_the_agentic_shift_in_software_development_with_Goog__Z9Zz75pmOeg.md`

**80. [NoSQL for modern apps and AI: The future of Memorystore, Firestore, and Bigtable](https://www.youtube.com/watch?v=Y7HwVL3LdNo)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. 수요일 오후에 함께해 주셔서 감사합니다. 네 , 오늘 저희는 최신 앱 과 AI를 위한 NoSQL, 그리고 Memorystore, Firestore, Bigtable의 미래에 대해 이야기하기 위해 이 자리에 모였습니다. 먼저 발표자 소개부터 시작하겠습니다. 제 이름은 바이바브 고엘입니다. 저는 Spanner, Bigtable, Firestore, Memorystor…
- B1 디지털·AI 기술의 활용: 왜냐하면 우리는 전체 Google Cloud 또는 자체 관리 데이터베이스를 관리하는 데 막대한 엔지니어링 및 운영 오버헤드를 투자하고 있었는데, Google Cloud는 완전 관리형 플랫폼을 제공하여 엔지니어링 노력과 운영 비용을 크게 절감해 주었기 때문입니다.
- B7 성과: 운영효율: 이번 아키텍처 혁신의 목표는 클라우드 분산 플랫폼 간 데이터 이동에 따른 높은 운영 오버헤드를 줄이고, 운영 비용을 절감하며, 전체 아키텍처를 간소화하고 업그레이드하는 것이었습니다.
- 수치 주장: 게다가, 제로 카피 응답을 사용하면 처리량이 20% 더 향상됩니다.
- 교량: — · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 코딩 에이전트
- 원문: `transcripts/channels/Google_Cloud_Tech/NoSQL_for_modern_apps_and_AI_The_future_of_Memorystore,_Fire__Y7HwVL3LdNo.md`

**81. [Power intelligent agents with AI-native databases](https://www.youtube.com/watch?v=7awKinJhGPo)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요, 여러분. 인공지능의 놀라운 잠재력을 활용하기 위해 우리 모두는 기업 데이터와 연동되는 고부가가치 에이전트 기반 워크플로 및 경험을 구축하고자 합니다 . 하지만 그러기 위해서는 최고의 에이전트 기반 데이터 플랫폼이 필요합니다. 사용자들의 신뢰를 얻기 위해서는 상담원이 높은 정확도를 갖추는 동시에 당사의 엄격한 개인정보 보호, 보안 및 거버넌스 요구 사항을 준수해야 합니다 …
- B1 디지털·AI 기술의 활용: [박수] 제가 이 내용을 보면서 정말 재밌어하는 한 가지를 다시 한번 간단히 말씀드리고 싶은데요, 그분이 보여주신 것처럼 단일 쿼리를 작성할 수도 있고, 더 나아가 자연어가 에이전트 의 언어이기 때문에 대화형 데이터 플랫폼에 자연어로 질문을 할 수도 있다는 겁니다.
- B4 가치네트워크·생태계: 데이터를 자율적인 지능형 시스템으로 전환하는 여정은 이제 막 시작되었으며, 앞으로도 지속적인 파트너십을 통해 고객 여러분께서 AI를 활용하여 차세대 에이전트 시스템으로 나아가는 데 도움을 드릴 수 있기를 기대합니다.
- 수치 주장: 저희는 향후 10년을 위한 완전히 새로운 범주를 도입하고자 하며, 이를 에이전트 데이터 클라우드라고 부릅니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Google_Cloud_Tech/Power_intelligent_agents_with_AI-native_databases__7awKinJhGPo.md`

**82. [Power intelligent agents with AI-native databases](https://www.youtube.com/watch?v=quzn4hOXQmI)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요, 여러분. 인공지능의 놀라운 잠재력을 활용하기 위해 우리 모두는 기업 데이터와 연동되는 고부가가치 에이전트 기반 워크플로 및 경험을 구축하고자 합니다 . 하지만 그러기 위해서는 최고의 에이전트 기반 데이터 플랫폼이 필요합니다. 사용자들의 신뢰를 얻기 위해서는 상담원이 높은 정확도를 갖추는 동시에 당사의 엄격한 개인정보 보호, 보안 및 거버넌스 요구 사항을 준수해야 합니다 …
- B1 디지털·AI 기술의 활용: 제가 이 내용을 보면서 정말 재밌어하는 한 가지를 다시 한번 간단히 말씀드리고 싶은데요, 그분이 보여주신 것처럼 단일 쿼리를 작성할 수도 있고, 더 나아가 자연어가 에이전트 의 언어이기 때문에 대화형 데이터 플랫폼에 자연어로 질문을 할 수도 있다는 겁니다.
- B4 가치네트워크·생태계: 데이터를 자율적인 지능형 시스템으로 전환하는 여정은 이제 막 시작되었으며, 앞으로도 지속적인 파트너십을 통해 고객 여러분께서 AI를 활용하여 차세대 에이전트 시스템으로 나아가는 데 도움을 드릴 수 있기를 기대합니다.
- 수치 주장: AlloyDB는 2024년부터 오픈소스 PostgreSQL과 차별화된 모습을 보여왔는데, 단순히 일반적인 PG 벡터 지원만 제공하는 것이 아니라 Google 검색, YouTube 및 기타 여러 서비스의 기반이 되는 Google의 독자적인 스캐닝 인덱스를 AlloyDB에 도입했기 때문입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Google_Cloud_Tech/Power_intelligent_agents_with_AI-native_databases__quzn4hOXQmI.md`

**83. [Scale AI agents in production](https://www.youtube.com/watch?v=LHcjN11nNPU)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. 저희 운영 환경에서 세션 규모 확장이 가능한 AI 에이전트를 사용해 보시는 것을 환영합니다. 저는 라이언 이스머트입니다. 저는 제미니 엔터프라이즈 에이전트 플랫폼 팀의 제품 관리자이며, 오늘 이 자리에는 제 동료 엘리아와 저희의 소중한 고객 두 분, 컴캐스트의 프라빈, 그리고 팔로알토 네트웍스의 테주엘이 함께해 주셨습니다. 이번 학기에는 일정이 꽉 차 있습니다 .…
- B1 디지털·AI 기술의 활용: 그리고 제가 여러분과 함께 살펴보고 싶은 것은 팔로알토네트웍스가 구글 클라우드 스택을 기반으로 어떻게 프로덕션 수준의 추론 생태계를 구축했는지에 대한 심층적인 분석입니다 .
- B2 파괴: 소비자 행동·기대: 에이전트 세션은 개별 상호 작용을 저장하고 관리하는 관리형 서비스를 제공하여 대화 맥락에 대한 확실한 정보를 확보하고 개인화 및 관련성을 강화합니다.
- 수치 주장: 그러면 방금 1분 만에 구축한 에이전트가 에이전트 런타임에 배포됩니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Google_Cloud_Tech/Scale_AI_agents_in_production__LHcjN11nNPU.md`

**84. [Startups shipping at scale with Google DeepMind](https://www.youtube.com/watch?v=RA_fQvXQ4aw)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 여러분 안녕하세요? 이번 패널 토론이 기대돼요. 각기 다른 방식으로 혁신을 주도하는 네 개의 회사를 대표하는 훌륭한 분들과 함께하게 되어 매우 기쁩니다 . 음, 모두의 다음 날이 즐거웠기를 바랍니다. 부디 많은 것들을 들어보셨기를 바랍니다. 멋진 사람들을 많이 만날 수 있기를 바랍니다. 음, 어쩌면 약간의 도박을 해볼 수도 있겠네요. 저는 사람들이 라스베이거스에서 도박하고 이런 강연…
- B1 디지털·AI 기술의 활용: 저희가 '드로이드'라는 용어를 사용하는 이유는 3년 전 GPT-3.5가 출시되었을 때 기업용 소프트웨어 개발 수명주기 전반에 걸쳐 작동하는 완전 자율 AI 시스템을 구축하겠다고 선언했기 때문입니다.
- B2 파괴: 소비자 행동·기대: 그래서 저희는 가상 착용을 정말 상세하고 개인화된 방식으로 구현하기 위해 회사 차원에서 어떤 데이터를 축적해야 할지 많이 고민해 왔습니다.
- 수치 주장: 그래서 우리는 비교적 간단한 프로토타입으로 시작해서 이제는 기업 고객에게까지 나아가 수천 명의 직원이 매일 사용하는 내부 도구를 개발하도록 지원하고 있습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Google_Cloud_Tech/Startups_shipping_at_scale_with_Google_DeepMind__RA_fQvXQ4aw.md`

**85. [The Gemini 3 playbook: Optimizing for quality, cost, and scale](https://www.youtube.com/watch?v=lbUkqPj63eQ)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B6 장벽 · 빠짐: B5 구조 변화, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요 여러분. 안녕하세요. 제 이름은 다니엘이고, 오늘은 속도, 품질 및 비용 최적화를 위한 제미니 3 플레이북에 대해 이야기해 보겠습니다. 제 이름은 다니엘입니다. 저는 구글에서 제품 관리자로 근무하며 제미니 모델의 품질 및 수명 주기 관리를 담당하고 있습니다. 오늘 저는 Salesforce의 Darvish와 저희 응용 AI 엔지니어링 팀의 Skender와 함께 LLM을 사용하는 데 …
- B1 디지털·AI 기술의 활용: 그래서 지난 1 년 반 정도 동안 저희 응용 AI 엔지니어링 팀은 Palm이나 Gemini 1을 사용하던 많은 Google Cloud 고객들과 협력하여 Gemini 2로, 그리고 최근에는 Gemini 2에서 Gemini 3으로 업그레이드하는 것을 지원해 왔습니다.
- B3 전략적 대응: 저희는 귀하께서 Gemini Gemini의 로드맵을 어떤 모습으로 만들어갈지 함께 고민해주시고, 저희 또한 귀하께서 로드맵을 구상하시는 데 도움이 될 수 있도록 저희의 로드맵에 대한 정보를 제공해드리는 파트너십을 구축하고 싶습니다 .
- 수치 주장: 좀 더 자세히 설명드리자면, 저희는 매주 수십 개의 새로운 모델을 학습시키고 있는데 , 최종적으로 출시되는 모델이 반드시 그중 하나에서 나온 것은 아닙니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Google_Cloud_Tech/The_Gemini_3_playbook_Optimizing_for_quality,_cost,_and_scal__lbUkqPj63eQ.md`

**86. [The agent-quality flywheel: Using Gemini Enterprise Agent Platform evaluations to optimize agents](https://www.youtube.com/watch?v=eLQAJqydXqY)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요, 여러분 모두 환영합니다. 어, 이건 엔지니어 에이전트 품질 플라이휠입니다. 이번 주 초에 Gemini 엔터프라이즈 에이전트 플랫폼에 대해 들어보셨을 수도 있습니다. 이 플랫폼은 구축, 확장, 최적화 및 관리라는 네 가지 핵심 요소로 구성되어 있습니다. 오늘 이 강연에서는 최적화에 대해 좀 더 자세히 살펴보겠습니다. 그리고 우리는 오늘날 품질을 엔지니어링 분야로 접근하는 …
- B1 디지털·AI 기술의 활용: 이 경우 권장되는 해결책은 도구 스키마를 수정하여 Compute Engine, Cloud SQL, Spanner, BigQuery 등의 열거형을 추가함으로써 에이전트가 조사를 시작하기 전에 명시적인 확인을 거치도록 하는 것입니다 .
- B5 직무·역량 변화: 그래서 애플리케이션에 직접적인 피드백 기능을 더 추가했고, 팀은 PM들과 매주 회의를 열어 모든 오류 발생 원인을 검토하고, 데이터 과학자들이 시스템을 개선할 수 있도록 개별 티켓을 생성하기 시작했습니다 .
- 수치 주장: 그래서 저희가 3년 전 AI가 막 등장했을 때 가장 먼저 했던 일 중 하나는 자연어를 SQL로 변환하는 엔진을 구축하는 것이었습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 검색·RAG
- 원문: `transcripts/channels/Google_Cloud_Tech/The_agent-quality_flywheel_Using_Gemini_Enterprise_Agent_Pla__eLQAJqydXqY.md`

**87. [Under the hood for startups: How Google DeepMind makes modeling decisions](https://www.youtube.com/watch?v=A4nNQfGqZIs)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요. 참여해주셔서 감사합니다. 오늘 패널 토론이 정말 기대됩니다. 제 이름은 앤드류입니다. 저는 창업자입니다. 감사합니다. 그리고 AI 미래 펀드의 멤버이기도 합니다. DeepMind의 훌륭한 제품 관리자분들과 함께 패널 토론의 사회를 맡게 되어 조금은 흥미롭고 특별한 경험이라고 생각합니다. 오늘은 창업자와 제품 관리자(PM)의 관점에서 이 대화를 진행해 보겠습니다 . 그래서…
- B3 전략적 대응: 제품 로드맵에 있는 기능을 구현하는 것과 필요한 기능이 추가될 때까지 기다리는 것 사이에서 어떤 균형을 유지하시겠습니까 ?
- B1 디지털·AI 기술의 활용: 예를 들어 고객 지원 사례처럼 해결 품질과 해결 정확성이 가장 중요한 경우에는 클라우드 호스팅 방식의 대규모 모델을 제공하는 것이 전략적으로 중요할 수 있습니다.
- 수치 주장: 그래서 우리는 딥마인드 측면에서 제품 관련 장단점들을 논의하고, 그들이 어떻게 연구 결과를 우리에게 제공하는지, 그리고 창업자로서 현재 24시간마다 쏟아져 나오는 듯한 새로운 제품 출시를 어떻게 이해해야 하는지에 대해 이야기할 것입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/Google_Cloud_Tech/Under_the_hood_for_startups_How_Google_DeepMind_makes_modeli__A4nNQfGqZIs.md`

**88. [What's new in AlloyDB: Scale PostgreSQL for agentic AI and hybrid clouds](https://www.youtube.com/watch?v=vw1AzTNUiE4)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. 환영. AlloyDB 세션에 오신 것을 환영합니다 . 라비와 저는 지난 1년간 AlloyDB에 적용된 최신 혁신 기술, 특히 에이전트 기반 및 하이브리드 클라우드 워크로드 지원에 대해 이야기하게 되어 매우 기쁩니다. 제 이름은 수자타 만달라입니다. 저는 AlloyDB의 제품 관리를 총괄하고 있으며, Google Cloud 데이터베이스 부문의 제품 관리 이사입니다.…
- B1 디지털·AI 기술의 활용: 저는 월마트에서 모든 데이터베이스, 데이터 플랫폼, 빅데이터 레이크 등을 총괄하고 있습니다.
- B4 가치네트워크·생태계: 성능 엔지니어링과 비즈니스 부서와의 긴밀한 파트너십을 통해 비즈니스를 데이터베이스 생태계에 어떻게 통합하고 관리하는지 이해하고 있으며, 시스템 간 데이터 이동 기능을 갖추고 있습니다.
- 수치 주장: 라비와 저는 지난 1년간 AlloyDB에 적용된 최신 혁신 기술, 특히 에이전트 기반 및 하이브리드 클라우드 워크로드 지원에 대해 이야기하게 되어 매우 기쁩니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_in_AlloyDB_Scale_PostgreSQL_for_agentic_AI_and_hy__vw1AzTNUiE4.md`

**89. [What's new in Cloud Run](https://www.youtube.com/watch?v=AoisAy_LGpI)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요. 환영. 환영. 클라우드 런에 오신 것을 환영합니다. 무슨 새로운 소식이 있나요? 오늘은 여러분을 위해 멋진 소식을 준비했습니다. 연례 모임에 다시 참석하게 되어 정말 기쁩니다. 안녕하세요, 저는 Google Cloud Run의 공동 창립자 중 한 명인 스테렌입니다 . 저는 현재 구글 클라우드에서 제품 관리 이사로 재직 중입니다. 클라우드 런 팀에서는 엔지니어링 수석 이사…
- B1 디지털·AI 기술의 활용: 저희는 클라우드 런(Cloud Run) 수집 서비스를 운영하고 있으며, 이 서비스는 데이터를 수집하여 각 레코드를 암호화하고 압축한 후 검색 인덱스를 구축하여 클라우드 빅테이블(Cloud Bigtable)에 기록합니다.
- B2 파괴: 데이터 가용성: 저희는 클라우드 런(Cloud Run) 수집 서비스를 운영하고 있으며, 이 서비스는 데이터를 수집하여 각 레코드를 암호화하고 압축한 후 검색 인덱스를 구축하여 클라우드 빅테이블(Cloud Bigtable)에 기록합니다.
- 수치 주장: 작년(2025년)에는 Cloud Run의 월간 활성 외부 개발자 수 와 애플리케이션 수가 두 배로 증가했습니다.
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 칩·하드웨어 · 코딩 에이전트
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_in_Cloud_Run__AoisAy_LGpI.md`

**90. [What's new in Cloud SQL: Drive performance, high availability, and security](https://www.youtube.com/watch?v=zKXbKmpqWB0)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: [음악] 환영합니다. 여러분 모두 환영합니다. 여기 낯익은 얼굴들이 보이네요. 이번 세션에 참석해주셔서 진심으로 감사드립니다 . 음, 저희가 구글 클라우드 2025에서 마지막으로 만난 이후로 클라우드 SQL에 엄청난 혁신이 이루어졌습니다. 그리고 오늘, 우리는 앞으로 45분 동안 이러한 혁신 기술 중 일부를 심층적으로 살펴보겠습니다. 제 이름은 발라 나라심한입니다. 저는 클라우드 SQL 그룹…
- B1 디지털·AI 기술의 활용: 이는 고객들이 매일 로그인하여 클라우드 데이터 관리 작업을 수행하는 SaaS 플랫폼입니다.
- B8 부정 성과: 보안·프라이버시: 사이버 공격이든, 자연 재해든, 아니면 인공지능 에이전트의 오작동이든 간에.
- 수치 주장: 앞서 말씀드린 것처럼, 지난 12개월 동안 클라우드 SQL에 도입한 몇 가지 주요 혁신 사항에 집중해서 살펴보겠습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_in_Cloud_SQL_Drive_performance,_high_availability__zKXbKmpqWB0.md`

**91. [What's new in Google Cloud's agent platform](https://www.youtube.com/watch?v=FxnjRYo3fpU)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 모두 환영합니다. 와, 정말 큰 방이네요. 오늘 이 자리에 함께하게 되어 매우 기쁩니다. 에이전트 플랫폼의 새로운 기능들을 소개하고, 기조연설에서 발표한 내용을 좀 더 자세히 살펴보고, 이미 몇몇 고객들이 에이전트 플랫폼을 어떻게 활용하고 있는지 보여드리겠습니다. 제 이름은 아만 칸입니다. 저는 에이전트 플랫폼 팀의 그룹 제품 관리자로서 에이전트 거버넌스를 담당하고 있습니다. 오늘 저희 De…
- B1 디지털·AI 기술의 활용: 저희는 자율형 식물 판매점과 같은 다양한 데모로 여러분을 놀라게 했고, 작년에 출시한 Agentic AI 클라우드를 통해 실제로 무엇이 가능한지 보여드리게 되어 매우 기쁩니다.
- B4 가치네트워크·생태계: 요약하자면, 올해 에이전트 플랫폼을 통해 더욱 심층적인 생태계, 상호 운용성에 대한 투자, 사용 편의성을 제공하여 팀 전체가 한 곳에서 작업할 수 있도록 지원하고, 맞춤 설정 기능을 통해 에이전트가 실제로 비즈니스에 도움이 되도록 할 것입니다.
- 수치 주장: 로레알 GPT에는 주간 사용자 4만 1천 명과 직원들이 이 플랫폼을 통해 개발한 코드 없는 에이전트 3만 명이 있습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_in_Google_Cloud's_agent_platform__FxnjRYo3fpU.md`

**92. [What's new with Gemini from Google DeepMind](https://www.youtube.com/watch?v=92LvgAcR6fI)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분. 제 이름은 마이클 그레셀이고, 제미니 엔터프라이즈 에이전트 플랫폼의 제품 관리 부사장입니다. 오늘 저는 데이비드 태커와 리플릿의 미셸과 함께 이 자리에 섰습니다. 하지만 그분들이 직접 소개하시도록 하겠습니다. 안녕하세요 여러분. 모두 만나서 반가워요. 저는 캘리포니아에 있는 구글 딥마인드의 제품 담당 부사장인 데이비드 태커입니다. 저는 모델 개발을 담당하는 제품 …
- B1 디지털·AI 기술의 활용: 저희의 심층 조사 에이전트를 사용하면 단 한 번의 API 호출로 웹 및 광범위한 공개 정보에 접근할 수 있을 뿐만 아니라 자체 데이터 소스를 기반으로 심층 조사를 수행하여 텍스트뿐 아니라 차트, 그래픽 인포그래픽까지 생성할 수 있습니다.
- B4 가치네트워크·생태계: 그러니까, 모델을 선택하는 것은 에이전트를 구축하는 과정의 한 부분일 뿐이고, 그 부분은 매우 중요하지만, 에이전트 플랫폼은 모델 생태계 그 자체보다 훨씬 더 많은 것을 고려합니다.
- 수치 주장: 저는 항상 딥마인드의 사명에 대해 이야기하는 것으로 시작하는데, 잘 모르시는 분들을 위해 설명드리자면 딥마인드는 2010년 런던에서 설립된 스타트업으로, 인공 일반 지능을 개발하는 것을 목표로 삼았습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_with_Gemini_from_Google_DeepMind__92LvgAcR6fI.md`

**93. [What's new with data agents](https://www.youtube.com/watch?v=Z-AfOcWO_kk)** — Google Cloud Tech · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분. 오늘은 데이터 에이전트의 새로운 기능에 대해 이야기하게 되어 정말 기쁩니다 . 우리 모두가 목격했듯이, 올해는 에이전트형 AI의 해였습니다 . 그리고 저는 데이터와 인공지능이 만나는 지점에서 앞으로 어떤 일들이 펼쳐질지 매우 낙관적으로 생각합니다. 저는 BigQuery AI의 엔지니어링 수석 디렉터인 가네시 겔라입니다 . 오늘은 제품 담당 이사인 제 동료 마니 스…
- B1 디지털·AI 기술의 활용: 이 제품은 BigQuery에 대한 완벽한 액세스를 제공하는 완전 관리형 원격 MCP 서버로, BigQuery에 연결하기 위한 사용자 지정 연결 코드나 API 코드를 작성할 필요가 없습니다.
- B5 직무·역량 변화: 저희 데이터 과학 에이전트는 BigQuery 기반의 Colab 노트북에서 실행되어 데이터 과학자들이 간단한 자연어 처리부터 시작하여 정교한 머신러닝 모델을 구축할 수 있도록 지원합니다.
- 수치 주장: 이건 제 개인적인 의견이 아니라, 여기 인용문에서 보시다시피 가트너는 2027년까지 기업 의사 결정의 50% 이상이 에이전트형 AI에 의해 보강되거나 자동화될 것이라고 예측하고 있습니다 .
- 교량: — · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준
- 원문: `transcripts/channels/Google_Cloud_Tech/What's_new_with_data_agents__Z-AfOcWO_kk.md`

---

## Google Developers


**94. [A fireside chat on the evolution of the developer craft](https://www.youtube.com/watch?v=VTYx7Ex-0bA)** — Google Developers · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 네, 모두 환영합니다. 오늘 함께해 주셔서 감사합니다. 저희는 무대에 함께 선 적이 없는 몇몇 분들과 재미있는 대화를 나눌 예정입니다. 저희 팀에는 제가 만난 엔지니어 중 가장 실용적이고 재능 있는 아자가 있습니다. 시에라는 구글 엔지니어들이 매일 하는 일과 우리가 어떻게 더 나아지는지에 대해 매우 흥미로운 연구를 하고 있는데, 저는 항상 그녀의 통찰력을 좋아합니다. 그리고 애디는 현대 AI…
- B5 직무·역량 변화: Azure에서 경력 엔지니어든 신입 엔지니어든 재교육이나 새로운 기술 습득을 생각할 때, 어떤 분야를 시급히 개발해야 한다고 느끼실까요?
- B1 디지털·AI 기술의 활용: "과연 그 과정 안에 내가 현장에서 배울 수 있는 내용이 충분히 있을까?" 그래서 저는 사람들이 의도적으로, 예를 들어 "나는 LLM 교수님과 단순히 코드 생성 작업만 하려고 하는 게 아니야"라고 생각해야 한다고 봅니다.
- 수치 주장: 2026년에 시니어 엔지니어란 도대체 뭘까요?
- 교량: — · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Google_Developers/A_fireside_chat_on_the_evolution_of_the_developer_craft__VTYx7Ex-0bA.md`

**95. [Beyond the keynote with Sundar Pichai](https://www.youtube.com/watch?v=9C20esBUf-Q)** — Google Developers · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 환영. 환영. 감사합니다 . 구글 I/O 2026. 지금은 대화의 장입니다. 제 이름은 맷 ​​버먼입니다. 저는 포드 퓨처의 CEO입니다. 오늘 저는 지난 10년간 구글을 이끌어 오신 분과 이야기를 나눌 수 있게 되어 매우 기쁩니다. 순 다르 피차이를 환영해 주세요. 괜찮은. 함께해 주셔서 감사합니다. 이곳에 오게 되어 진심으로 기쁩니다. 모든 발표에 축하드립니다 . 음, 바로 본론으로 들어…
- B4 가치네트워크·생태계: 수십 년 동안 기술 분야에서 매우 성공적인 오픈 소스 생태계가 많이 있었지만, 모델을 구축하는 데 드는 초기 비용 때문에 어려움이 매우 크다고 생각합니다.
- B1 디지털·AI 기술의 활용: 구글 클라우드에서 고객을 지원할 때와 비슷한 점이 있는데, 고객이 어떤 기능을 보고 "저 기능에 접근하고 싶어요"라고 말할 수도 있잖아요.
- 수치 주장: 아시다시피, 특히 코딩 분야에서는 2년 전부터 대부분의 개발자들이 이러한 도구들을 사용하기 시작했습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Google_Developers/Beyond_the_keynote_with_Sundar_Pichai__9C20esBUf-Q.md`

**96. [Build core skills to thrive as an AI-era developer](https://www.youtube.com/watch?v=q_Jq4IgYImk)** — Google Developers · 에이전트·개발도구 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분. 우리는 잘 지내고 있나요? [웃음] 자, 시작해 볼까요 . 우리는 지금 어떤 기분일까요? 흥분한? 자, 됐습니다 . 조금 부담스러우신가요? 궁금한? 호기심이 많기를 바랍니다. 좋아요. 안녕하세요, 저희는 앤드류와 니콜입니다. 저희 둘 다 구글의 개발자 인텔리전스 팀에서 팀장으로 일하고 있습니다. 그리고 우리는 함께 소프트웨어 엔지니어를 연구하며 커리어를 쌓아갑니다…
- B1 디지털·AI 기술의 활용: 조직에 고품질의 내부 플랫폼, 강력한 API, 명확하고 잘 문서화된 워크플로가 있다면 AI는 진정한 협력자 역할을 할 수 있습니다.
- B4 가치네트워크·생태계: 이러한 성찰 일지는 저에게 통찰력을 줄 뿐만 아니라, 우리 모두에게 인공 지능과의 협업 방식, 예를 들어 어떤 언어나 프레임워크를 사용해야 하는지에 대한 명확한 지침을 제공하는 것뿐만 아니라, 에이전트를 둘러싼 전체 생태계를 개선할 수 있는 방법에 대한 통찰력을 제공합니다 .
- 수치 주장: 10배의 생산량 증가가 10배의 인지 부하를 동반해서는 안 됩니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Google_Developers/Build_core_skills_to_thrive_as_an_AI-era_developer__q_Jq4IgYImk.md`

**97. [What's new in the Gemma open model family](https://www.youtube.com/watch?v=oUtiZbrehrw)** — Google Developers · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 여러분, 제미니 오픈 모델 제품군의 새로운 소식을 전해드립니다. 제 이름은 올리비에이고, 제미니의 제품 리더입니다. 오늘 저와 함께 저희 팀의 제품 매니저인 거스와 개발자 관계 엔지니어인 얀 발렌타인이 참석할 예정입니다 . 그렇다면 쌍둥이자리란 무엇일까요? Gemini는 Google DeepMind에서 개발한 오픈 웨이트 대규모 언어 모델입니다 . 저희는 2024년에 간단한 전제를 …
- B1 디지털·AI 기술의 활용: 하지만 가장 간편한 해결책을 원하신다면 클라우드 런(Cloud Run)이 있습니다.
- B4 가치네트워크·생태계: 저희는 Gemma 모델을 활용하는 개발자, 건설업체, 그리고 기업들로 구성된 거대한 생태계를 보유하고 있습니다.
- 수치 주장: 저희는 10억 개의 파라미터를 가진 IoT 기기부터 270억 개의 파라미터를 가진 대형 소비자용 GPU까지 다양한 환경에서 작동하는 멀티 모델 제품군을 개발했습니다 .
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Google_Developers/What's_new_in_the_Gemma_open_model_family__oUtiZbrehrw.md`

**98. [Sameer Samat on Android 17 and the Future of Intelligent Computing](https://www.youtube.com/watch?v=YvVsdZL2ogY)** — Google Developers · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 저는 음악이 틀을 벗어던지길 바랄 뿐입니다. 솔직히 말해서, 다시는 서류 작성을 하고 싶지 않아요 . 여름휴가를 위해 항공편을 여러 개 예약했는데, 15살짜리 딸아이 여권 번호를 외워버렸어요. 하지만 그걸 외우고 싶진 않거든요. 저는 제 집이 없어요. 응. 음, 제가 너무 여러 번 시도하다 보니, 마치 제정신이 아닌 것 같아요 . 그래서 슈퍼필은 우리 모두가 이름, 주소, 신용카드 정보 등을…
- B4 가치네트워크·생태계: 생태계로서 볼 때, 지금은 기술 자체에 너무 집중하고 있는 것 같고, 실제로 기기를 사용하는 사람들에게 어떤 도움이 되는지에 대해서는 충분히 관심을 기울이지 않는 것 같습니다.
- B1 디지털·AI 기술의 활용: 예를 들어, 누군가가 매고 있는 넥타이가 마음에 들 수도 있고, 소셜 미디어 게시물에 있는 아름다운 호수 사진처럼 눈길을 끄는 것일 수도 있죠.
- 수치 주장: 지금 우리가 경험하는 것과 5 년 후, 모든 사람이 사용하는 하드웨어에서 훌륭하게 작동하는 모델들이 출시되었을 때의 경험은 완전히 다를까요?
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/Google_Developers/Sameer_Samat_on_Android_17_and_the_Future_of_Intelligent_Com__YvVsdZL2ogY.md`

---

## Huawei


**99. ["Our North Star": IOH & AI Transforming Indonesia's Intelligent Future](https://www.youtube.com/watch?v=QZZBEYvYq6g)** — Huawei · 인프라·칩·전력 · CN · 2025-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 할리우드 히트곡 가사처럼, 멋진 코펜하겐에 오신 것을 환영합니다 . 행복, 휘게, 그리고 한스 크리스티안 안데르센의 도시. 사실, 마법 같은 동화의 나라는 상상력과 대담한 새로운 여정에 대해 이야기하기에 아주 적합한 장소입니다. 점점 더 지능화되는 이 시대에 동남아시아 최대 통신 사업자 중 하나인 인도샛 오레두 허치슨은 독자적인 이야기를 써나가고 있습니다. 광대한 네트워크와 강력한 인공지능이…
- B2 파괴: 소비자 행동·기대: 이러한 모든 역량은 고객 경험에 관련된 모든 사람들의 사용자와 결합되어 이 문제를 해결합니다.
- B1 디지털·AI 기술의 활용: 매우 중요한 것은, 우리는 사용 사례를 분석하는 것이 아니라 데이터 플랫폼이라고 부르는 기반을 구축한다는 것입니다 .
- 수치 주장: 우리는 네트워크 다운타임을 50% 줄이고 고객 불만을 30% 감소시키며 , 네트워크 처리량을 70% 향상시키고 지연 시간을 50% 줄일 수 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Huawei/Our_North_Star_IOH_&_AI_Transforming_Indonesia's_Intelligent__QZZBEYvYq6g.md`

**100. [Smart Retailer DeFacto is Leading Fashion's "Phygital" Future](https://www.youtube.com/watch?v=YOxwp5bzZvk)** — Huawei · 인프라·칩·전력 · CN · 2025-09 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 어떻게 생각하세요? 네, 저한테는 안 어울리는 색이네요. 사실 De facto는 나와는 달리 패션계에서 성공한 사례입니다. 터키에서는 500개 이상의 매장과 100여 개국 온라인 플랫폼을 보유한 글로벌 브랜드입니다. 하지만 패션의 최첨단에서 앞서나가려면 비즈니스의 최첨단에도 머물러야 합니다. 인공지능과 기술 혁신을 수용합니다 . 핵심은 단순히 밑단이나 솔 기선, 다트선만이 아니라 최…
- B1 디지털·AI 기술의 활용: 처음에는 화웨이와 함께 전자상거래 플랫폼을 마이그레이션했고, 이를 성공적으로 완료한 후에는 전체 인프라, 즉 애플리케이션 과 인프라 전체를 클라우드로 마이그레이션하는 작업을 진행하고 있습니다.
- B7 성과: 운영효율: 어쨌든, de facto와 최고정보책임자(CIO)인 압둘 라만 킬린치는 화웨이 클라우드를 활용하여 브랜드의 운영 효율성과 고객 경험을 향상시키고 있습니다.
- 수치 주장: 저희는 모든 사진과 모델을 100% AI로 전환하는 것을 목표로 하고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Huawei/Smart_Retailer_DeFacto_is_Leading_Fashion's_Phygital_Future__YOxwp5bzZvk.md`

**101. [Discipline, Not Hype, Will Define AI Innovation](https://www.youtube.com/watch?v=c6nYPWNgl7I)** — Huawei · 인프라·칩·전력 · CN · 2026-04 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 그러니까, 많은 기업들이 인공지능에 적응하고 이를 도입하는 방식이 바로 이런 것 같습니다. 챗봇을 구축하고, 태스크포스를 구성하고, 시범 운영을 진행하고, 새로운 도구를 출시하고, 모든 것에 채팅 GPT를 추가하세요 . 간단히 말해서, 벽에 스파게티를 마구 던져보고 그중 일부라도 붙기를 바라는 수밖에 없다. 전략적 사고가 아닌, 기업의 공황 상태에 오신 것을 환영합니다 . 이는 혁신 성과표의…
- B7 성과: 운영효율: 네, 저는 AI 도구가 단순히 운영 효율성을 높이는 데 그치지 않고 , 기업이 새로운 전략적 목표나 나아갈 방향을 설정하는 데 도움을 줄 수 있는 훌륭한 사례들을 많이 봐왔습니다.
- B3 전략적 대응: 하지만 만약 회사 내에 혁신 센터, 혁신 연구소 또는 혁신 센터와 같은 탐색 센터가 있고, 최고 경영진 이나 CEO에게 보고하는 정당성을 갖춘 지정된 리더가 있으며, 예산, 일정 및 지원을 확보하고 있다면 어떨까요?
- 교량: — · 기술: —
- 원문: `transcripts/channels/Huawei/Discipline,_Not_Hype,_Will_Define_AI_Innovation__c6nYPWNgl7I.md`

---

## Hugging Face


**102. [A Tour Through The Hugging Face Hub & A Hands on Guide To Gradio](https://www.youtube.com/watch?v=k8sHYMeDitQ)** — Hugging Face · 파운데이션 모델 · US · 2022-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 오늘은 두 부분으로 구성된 프레젠테이션을 진행할 예정입니다. 먼저 제 동료 루이스가 Hug and Face Hub에 대해 소개하고, 그곳에서 찾을 수 있는 모델, 데이터 세트, 데모 등에 대해 설명하겠습니다. 그다음 저는 Gradio 라이브러리를 사용하여 직접 데모를 만드는 방법을 보여드리겠습니다. 실습 위주의 데모 이므로 코드를 직접 실행해 볼 것입니다. 먼저 간단히 자기 소개를 하겠습니다…
- B1 디지털·AI 기술의 활용: 그러다 이 실험에서 생성되는 페타바이트 규모의 데이터를 분석하면서 머신러닝을 접하게 되었고, 딥러닝 때문에 물리학자로서의 미래가 위태로워졌다는 것을 깨달았습니다.
- B8 부정 성과: 보안·프라이버시: 이전에는 머신러닝 해커 같은 사람들만이 최첨단 머신 러닝 기술에 접근할 수 있었지만, 이제는 브라우저만 있으면 누구나 이러한 모델에 접근하고 사용하고 상호 작용하며, 모델의 오류 지점과 편향을 파악하려고 시도할 수 있습니다.
- 수치 주장: 하지만 지난 1년 정도 동안 Nate를 비롯한 팀원들이 다른 라이브러리들을 어떻게 통합할 수 있을지 고민해 왔습니다.
- 교량: — · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/Hugging_Face/A_Tour_Through_The_Hugging_Face_Hub_&_A_Hands_on_Guide_To_Gr__k8sHYMeDitQ.md`

**103. [Machine Learning Experts - Lewis Tunstall](https://www.youtube.com/watch?v=igW5VWewuLE)** — Hugging Face · 파운데이션 모델 · US · 2022-04 · ko · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분, 머신러닝 전문가 팟캐스트에 오신 것을 환영합니다. 저는 진행자 브리타니 뮬러이고, 오늘 게스트는 루이스 턴스톨입니다. 루이스는 허깅페이스(Hugging Face)의 머신러닝 엔지니어로, 트랜스포머를 활용하여 비즈니스 프로세스 자동화 및 머신러닝 운영 문제를 해결하는 업무를 맡고 있습니다. 루이스는 자연어 처리, 위상 데이터 분석, 시계열 분석 분야에서 스타트업과 …
- B1 디지털·AI 기술의 활용: 오늘 루이스는 제가 여기 가지고 있는 그의 신간, ' 트랜스포머: 대규모 모델 평가(Transformers: Large-Scale Model Evaluation)'에 대해 이야기하고, 머신러닝 엔지니어들이 더 빠른 지연 시간과 더 높은 처리량을 달성하도록 돕는 그의 노력에 대해서도 들려줄 예정입니다.
- B5 직무·역량 변화: 음, 굳이 하나 꼽자면, 처음 시작할 때 데이터 과학자로 일했는데, 데이터 과학자는 비즈니스 문제를 소프트웨어 문제, 또는 머신러닝 문제로 매핑하는 기술을 개발하잖아요.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Hugging_Face/Machine_Learning_Experts_-_Lewis_Tunstall__igW5VWewuLE.md`

**104. [Hugging Face Reading Group: Session 1](https://www.youtube.com/watch?v=8uVvfJIH_LY)** — Hugging Face · 파운데이션 모델 · US · 2022-10 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요. 안녕하세요. 안녕하세요 여러분. 저희 목소리가 들리시나요? 네. 달콤한. 낯익은 얼굴이 하나 보이네요. 크리스 아키키는 어디에나 있는 것 같아요. 자신을 복제 해제하세요. 아, 음소거 해제해 주셔서 감사합니다. 순간 당신이 제가 말하는 걸 막고 있는 줄 알았어요. 와, 팟캐스트까지 완벽하게 준비하셨네요. 그래요 . 저도 로켓 후드티를 입고 있는데, 레안드로가 배경에 로켓을 놓을 …
- B1 디지털·AI 기술의 활용: 음, GPT-2는 그 직후에 나온 모델인데, 기본적으로 GPT-1을 확장한 것이고, 모델 규모를 키우는 것만으로도 성능을 향상시킬 수 있다는 것을 발견한 것입니다.
- B4 가치네트워크·생태계: 이번 주에는 주로 책에 집중할 예정이지만, 다음 주부터는 독서 모임의 일부를 오픈 소스에 기여하는 방법, 예를 들어 이슈를 제기하고, 풀 리퀘스트를 생성하고, 생태계와 상호 작용하는 방법에 대해 배우는 데 할애할 계획입니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Hugging_Face/Hugging_Face_Reading_Group_Session_1__8uVvfJIH_LY.md`

**105. [Hugging Face Reading Group: Session 3](https://www.youtube.com/watch?v=TrwshPQcWiM)** — Hugging Face · 파운데이션 모델 · US · 2022-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 외국인, 안녕하세요. 이제 잘 들릴 것 같은데, 들리시나요? 네, 들려요. 잘됐네요. 어떻게 지내세요? 아, 저는 좀 아파서요. 회의 내내 재채기를 해서 소리가 잘 안 들릴 것 같아, 회의는 대부분 배경음악처럼 진행해야 할 것 같아요. 괜찮으시죠? 빨리 나으시길 바라요. 아버지는 어떠세요? 좋아요. 화면 공유해 볼게요. 화면에 뭐가 보이는지 알려주시겠어요? 네, 잘 보이네요. 외국인, 보통 …
- B1 디지털·AI 기술의 활용: 머신러닝의 하위 집합인 AI 와 머신러닝의 상위 집합인 딥러닝에 대해 이야기해 보겠습니다.
- B5 직무·역량 변화: 예를 들어 팔란티어 같은 회사는 방대한 데이터를 추출하고 그 안에서 패턴을 찾는 데 주력하고 있지만, 실제로 머신러닝을 많이 사용하지는 않고 데이터 엔지니어링 기법과 규칙 기반 접근 방식을 결합하여 목표를 달성합니다.
- 수치 주장: 따라서 모델이 이를 활용할 수 있다면 큰 이점을 얻을 수 있을지는 아직 100% 확신할 수 없지만, 적어도 더 큰 컨텍스트 윈도우를 가진 데이터를 입력받더라도 모델이 완전히 실패하는 일은 없어집니다.
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/Hugging_Face/Hugging_Face_Reading_Group_Session_3__TrwshPQcWiM.md`

**106. [Hugging Face Reading Group: Session 4](https://www.youtube.com/watch?v=zQfSPn7zk7U)** — Hugging Face · 파운데이션 모델 · US · 2022-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 여러분 잘 지내시나요? 네, 이제 제 목소리가 들릴 거예요. 들리시나요? 네, 들려요. 좋아요. 그럼 간단하게 영상 테스트를 해볼까요? 네, 저도 여러분을 볼 수 있어요. 음, 괜찮을 것 같아요. 화면 공유도 쉬울 거예요. 잠깐만요. 아래쪽에 화면 공유 버튼이 있을 거예요. 네, 버튼은 보이는데, 공유하는 동안에는 영상을 꺼둘게요. 음, 그럼 스크린샷 테스트 한번 해볼게요. [음…
- B8 부정 성과: 보안·프라이버시: 레오나르도, 예전과 지금의 차이에 대한 이야기로 돌아가서, 애쉬쉬 바스 바니가 발표한 '어텐션(Athentication)' 논문의 제1저자인데, 그는 초기 시절, 그러니까 이 기술이 폭발적으로 발전하기 전에는 언어에 대한 좋은 귀납적 편향을 만들어내지 못했다고 아주 명확하게 말했습니다.
- B1 디지털·AI 기술의 활용: 머신 러닝, 특히 딥 러닝의 해석과도 관련이 있다고 봐요.
- 수치 주장: 그런데 특정 코퍼스에서 모델을 학습시키고, 지원 어휘와 구성 요소 수가 10만 개라고 해볼게요.
- 교량: Avenue 1 동적역량 · 기술: 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Hugging_Face/Hugging_Face_Reading_Group_Session_4__zQfSPn7zk7U.md`

---

## IBM


**107. [AI isn’t digital transformation, and leaders need to understand why](https://www.youtube.com/watch?v=eZ1NizUx9U4)** — IBM · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 아시다시피, 제 아버지는 지금 85세이신, 나이 지긋하신 아일랜드 분이셨죠. 제가 그에게 새 아이폰을 선물한 건 아마 2011년쯤이었을 거예요, 맞죠? 그는 예전에 폴더 폰을 쓰곤 했어요. 그는 "이 물건에 뭐가 있는지 알아 ?"라고 말했어요. 나는 "그래"라고 대답했다. 그는 "이거 손전등이 있네. 이거 손전등이 있는 거 알아?"라고 말했어요. 그래서 저는 "알았어요. 그게 평평한 와 뭐지…
- B3 전략적 대응: 예를 들어, 저는 고위 경영진과 워크숍을 진행하는데, 종종 고위 경영진이 "저희에게 맞춤형 데모를 보여주실 수 있나요?"라고 묻습니다.
- B1 디지털·AI 기술의 활용: 에이전트는 도구를 호출할 수 있고, 기존 LLM(로컬 라이프 매니저)으로는 할 수 없었던 기능적인 작업들을 수행할 수 있습니다 .
- 수치 주장: 채드 GBD는 2022년 말에 나왔는데, 제가 이걸 발견하고는 "이게 도대체 뭐지?" 하면서 아주 깊은 수렁에 빠져들었어요.
- 교량: 정의 확장(DX→AX 계승), Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/2026-07-21/AI_isn’t_digital_transformation,_and_leaders_need_to_underst__eZ1NizUx9U4.md`

---

## IBM Technology


**108. [AI at college graduations and why Claude blackmails](https://www.youtube.com/watch?v=1h6e5MFg9I0)** — IBM Technology · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 젊은이들에게 해주고 싶은 조언은 과장된 홍보에 현혹되지 말고, 비관적인 음악 에도 귀 기울이지 말라는 것입니다 . 자신에게 안전하다고 느껴지는 공간에서 신중하게 실험해보고 이러한 도구들을 활용한 경험을 쌓아 스스로 판단을 내리세요. 오늘 전문가들의 다양한 의견을 통해 이 모든 것과 더 많은 것을 알아보세요 . [코웃음] 저는 팀 황이고, 전문가들의 모임에 오신 것을 환영합니다 . MOE는 매…
- B1 디지털·AI 기술의 활용: 음, 개발이든 뭐든 간에, 저는 사람들이 작은 단계부터 시작하고 , 핵심적인 임무가 아닌 작은 프로젝트들을 구축하고, 제한된 방식으로 AI 에이전트를 사용해 보거나, 아니면 좀 더 창의적인 사업과 관련된 것이든 간에 그렇게 하도록 강력히 권장합니다.
- B4 가치네트워크·생태계: 음, 그러니까, 사실 그 부분은, 음, 그러니까 제 생각은, LLM 생태계 내에 실제로 좀 흥미롭고 섬뜩한 현상이 있을지도 모른다는 겁니다.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/IBM_Technology/AI_at_college_graduations_and_why_Claude_blackmails__1h6e5MFg9I0.md`

**109. [AI skills security, Open AI Deployment Company & zero days](https://www.youtube.com/watch?v=YCWwh70FZtQ)** — IBM Technology · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 그렇다면 일자리를 대체하게 될까요? 음, 제 생각엔 직업이 바뀔 것 같아요, 그렇죠? 그리고 저는 이것이 컨설팅 회사들이 이전에는 해결할 수 없었던 문제들을 해결할 수 있게 해 줄 것이라고 생각합니다 . 하지만 저는 오늘날 우리가 보는 전통적인 컨설팅과는 다를 것이라고 생각합니다. 오늘 전문가 토론에서 이 모든 것과 그 이상의 이야기를 들어보세요. 안녕하세요, 저는 팀 홍입니다. Mixtur…
- B8 부정 성과: 보안·프라이버시: 쿠시, 논문을 소개하고 여러분들이 해결하려는 문제가 무엇인지 간략하게 설명해 주시면 좋을 것 같은데, 논문 의 큰 부분이 보안 문제와 관련된 기술에 초점을 맞추고 있는 것 같습니다.
- B1 디지털·AI 기술의 활용: 그리고 그들은 이미 자체적인 머신러닝 시스템과 기존 클라우드 스택을 보유하고 있습니다.
- 수치 주장: 다시 말씀드리지만, 80년이 넘는 컴퓨터 과학 역사를 통해 배운 모든 것을 활용해서 올바른 방식으로 일을 처리하는 거죠.
- 교량: — · 기술: —
- 원문: `transcripts/channels/IBM_Technology/AI_skills_security,_Open_AI_Deployment_Company_&_zero_days__YCWwh70FZtQ.md`

**110. [Agent control planes & OpenAI model solves Erdős](https://www.youtube.com/watch?v=wVdivlahcm0)** — IBM Technology · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 저희 회사에는 에이전트를 만드는 건 쉽다는 말이 실제로 있습니다 . 그 이후의 모든 일은 어렵습니다. 당신이 만들었군요. 이제는 문제가 됐어요. 관리해야 합니다 . 오늘 전문가들의 다양한 의견을 통해 이 모든 것과 더 많은 것을 알아보세요 . 안녕하세요, 저는 팀 행입니다. Mixture of Experts에 오신 것을 환영합니다 . 매주 인공지능 분야에서 가장 뛰어난 전문가들이 모여 한 주…
- B8 부정 성과: 보안·프라이버시: 그래서 제가 이런 도구 중 하나에 가서 "모든 보안 문제를 해결해 주세요"라고 말하면 , 여러 가지 문제가 발생해서 곤란해질 겁니다.
- B1 디지털·AI 기술의 활용: 그리고 AI로 인한 프론티어 리스크에 대한 이야기가 소셜 미디어에서 활발하게 오갔는데, 여러 주요 프론티어 모델 제공업체들이 다양한 AI 에이전트를 검토하고 있는 것으로 보입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/IBM_Technology/Agent_control_planes_&_OpenAI_model_solves_Erdős__wVdivlahcm0.md`

**111. [Live from Think 2026: AI operating model, VC funding & CAIO evolution](https://www.youtube.com/watch?v=YHKXflgkHak)** — IBM Technology · 에이전트·개발도구 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 저는 팀 황입니다. 보스턴에서 열리는 IBM Think 2026 현장에서 생중계되는 전문가 토론 프로그램, Mixture of Experts에 오신 것을 환영합니다 . [콧방귀 소리] [음악] MOE는 매주 최첨단 기술 분야에서 활동하는 뛰어난 인재들을 모아 인공지능 분야의 최신 뉴스를 토론하고 분석하며 여러분께 안내해 드립니다. 이번 주 에피소드에는 IBM의 AI 전환 리더인 …
- B1 디지털·AI 기술의 활용: 제가 2018년부터 2020년까지 클라우드 분야에서 정규직으로 일할 당시 , CISO들과 원탁회의를 자주 했는데, 그때마다 제가 CISO들에게 가장 좋아하는 질문이 " 클라우드 환경이 온프레미스 환경보다 더 안전한가요, 아니면 덜 안전한가요?"라고 농담처럼 말하곤 했습니다.
- B3 전략적 대응: 네, 힐러리, 여러 이사회 및 경영진과 함께 일해 오신 경험을 바탕으로 당신의 견해를 듣고 싶습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/IBM_Technology/Live_from_Think_2026_AI_operating_model,_VC_funding_&_CAIO_e__YHKXflgkHak.md`

**112. [OpenAI’s Daybreak and Mistral’s Mythos competitor](https://www.youtube.com/watch?v=u2MFautDjuM)** — IBM Technology · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 유리 날개 프로젝트는 이제 한물갔습니다. OpenAI는 현재 Daybreak라는 코드명을 가진 자체 프로젝트를 진행하고 있습니다 . 오늘 패널 여러분께서 트윗 길이의 짧은 답변을 남겨주시면 좋겠습니다. 닉, 당신부터 시작할게요. 무슨 생각을 하고 있어요? 좋아, 경쟁이 많아지겠지. 그게 바로 필요한 거예요. 또한, 코드의 취약점을 식별하는 데 더 많은 도움이 될 것입니다 . 모델이 많아질수록…
- B1 디지털·AI 기술의 활용: 그리고 GPT 5.5 사이버 버전이 있는데, 이는 공격적인 보안 연구와 같은 특수 워크플로우를 위해 설계된 가장 관대한 모델입니다 .
- B4 가치네트워크·생태계: 그뿐만 아니라 , 그들은 사람들이 이 기능을 사용하도록 적극적으로 장려하고 있으며, 심지어 Breach Forums에서 " 공급망 챌린지"라는, 제가 들어본 것 중 가장 끔찍한 틱톡 챌린지에 참여하도록 금전적 보상을 걸고 홍보하는 콘테스트까지 개최하고 있습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/IBM_Technology/OpenAI’s_Daybreak_and_Mistral’s_Mythos_competitor__u2MFautDjuM.md`

**113. [Claude Fable 5 & Apple’s NVIDIA deal](https://www.youtube.com/watch?v=aByPOYCEH6I)** — IBM Technology · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 그들이 약화시킨 유일한 부분은 사이버 보안 분야입니다. 팀, 혹시 뭐 해킹하고 있는 거야? 오늘 전문가 패널 토론에서 이 모든 것과 그 이상의 이야기를 들어보세요. 좋은 아침이에요. 안녕하세요, 저는 팀 황입니다. Mixture of Experts에 오신 것을 환영합니다. 매주 모는 인공지능 분야에서 가장 뛰어난 전문가들을 모아 한 주간의 뉴스를 정리해주는 시간을 갖습니다. 이번 주 에피소드…
- B1 디지털·AI 기술의 활용: 그러니까 애플이 휴대폰에 AI를 탑재한다고 발표했을 당시로 거슬러 올라가 보면 , 기기에서 AI를 실행하고 더 강력한 모델이 필요할 때만 클라우드에 접속하는 방식이었죠.
- B8 부정 성과: 보안·프라이버시: 두 번째는, 모든 회사가 기초 모델을 훈련시키면서 인터넷에 접속해 2,000 년 또는 1,000년 동안 축적된 인류의 기록을 싹쓸이해 학습시킨 다음, 저작권 문제라며 "이건 우리 것이 아니다"라고 말하는 상황입니다 .
- 수치 주장: 그리고 그들은 오늘 출시일부터 6월 22일까지 Fable이 모든 구독 서비스에 포함될 것이라고 말했습니다.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/IBM_Technology/Claude_Fable_5_&_Apple’s_NVIDIA_deal__aByPOYCEH6I.md`

**114. [Microsoft’s new AI models & bots dominate the internet](https://www.youtube.com/watch?v=SvBheXuKY8s)** — IBM Technology · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 웹상에서 봇의 수가 인간보다 훨씬 많았던 건 꽤 오래전 일이죠? 웹 스크래퍼 같은 것들이요. 요즘 많은 사람들이 연구 과제를 위해 AI 에이전트를 통해 상호작용하고 있는데, [음악] 제 생각에는 사람들이 직접 사이트에 접속하는 것보다는 이러한 상호작용을 포착하려는 것 같습니다. 오늘 전문가 토론에서 이 모든 것과 그 이상의 이야기를 들어보세요 . 안녕하세요, 저는 팀 황입니다. Mixture…
- B1 디지털·AI 기술의 활용: 음, 구체적으로 말하자면, 클라우드플레어의 도구를 사용하는 것이 좋다는 연구 결과가 있었는데, 제 생각에는 클라우드플레어의 도구들은 현재 인터넷을 상당히 잘 대표하는 데이터셋을 제공한다고 봅니다.
- B4 가치네트워크·생태계: 이번 주 에피소드에는 AI 혁신 리더인 Ambi Ganasan, AI 엔지니어인 Sandy Besson, 그리고 AI 음악 생태계 수석 엔지니어인 Rin Witna가 출연합니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/IBM_Technology/Microsoft’s_new_AI_models_&_bots_dominate_the_internet__SvBheXuKY8s.md`

**115. [New AI models, token minimization and IBM’s new sub-1nm chip](https://www.youtube.com/watch?v=d-hJa-yDJmQ)** — IBM Technology · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 우리가 이야기하는 7옹스트롬 크기의 이 트랜지스터 기술은 연산 시 50% 더 나은 성능을 제공하거나 70% 더 많은 전력을 절약합니다 . 이는 우리 음악 산업이 오랫동안 보지 못했던 엄청난 발전입니다 . [코웃음] 오늘 [음악] 전문가 믹스에서 이 모든 것과 그 이상의 이야기를 만나보세요. 안녕하세요, 저는 팀 황입니다. Mixture of Experts에 오신 것을 환영합니다 . [음악] …
- B1 디지털·AI 기술의 활용: 네, 아마 헤드라인에서 보셨겠지만, 우버, 마이크로소프트, 또는 다른 기업들이 클라우드 모델에 대한 API 접근이나 액세스를 제한하는 경우가 있습니다.
- B4 가치네트워크·생태계: 음, 그리고 구글 딥마인드와 A24 사이에 대규모 파트너십이 발표되었는데, A24는 ' 더 백룸스'나 '파티 슈프림' 같은 영화를 제작한 스튜디오로, 어떤 면에서는 일종의 명망 있는 영화 스튜디오로 알려져 있습니다.
- 수치 주장: 저는 이 나노스택 아키텍처 혁신이 반도체 산업 60년 만에 처음으로 컴퓨팅 논리 장치의 설계를 2차원에서 3차원으로 완전히 전환시킨 것이라고 생각합니다.
- 교량: — · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/IBM_Technology/New_AI_models,_token_minimization_and_IBM’s_new_sub-1nm_chip__d-hJa-yDJmQ.md`

**116. [The future of software engineering, tokenmaxxing and AI in higher education](https://www.youtube.com/watch?v=EKULOf_Cy0w)** — IBM Technology · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: 토큰을 최대한 모으는 것도 자랑하는 방법 중 하나잖아요 ? 오른쪽. 그건 마치 몇 파운드를 들어 올릴 수 있는지 같은 것과 같아요. 하지만 솔직히 말해서, 당신은 탈장되는 건가요, 아니면 강해지는 건가요? 우리는 모릅니다 . 이번 주 전문가 믹서에서 이 모든 것과 더 많은 이야기를 나눠보세요 . 안녕하세요, 저는 McConnA이고 Mixer of Experts에 오신 것을 환영합니다 . 매주…
- B1 디지털·AI 기술의 활용: 또한 각 시스템 아래에는 AI가 존재하며, 이는 LLM(Learning Leadership Management)으로 변환됩니다.
- B4 가치네트워크·생태계: 음, 아시다시피 저희가 현재 진행하고 있는 업무와 대학들과의 파트너십을 살펴보면, 저희는 전 세계 대학에 전문 지식, 도구, 그리고 역량 강화 프로그램을 제공하고 있습니다.
- 수치 주장: 예전에는 6개월 에서 8개월 정도 걸리던 작업을 이제는 한 달 정도로 단축할 수 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/IBM_Technology/The_future_of_software_engineering,_tokenmaxxing_and_AI_in_h__EKULOf_Cy0w.md`

**117. [2026 Cost of a Data Breach Report: AI Is Changing Cybersecurity](https://www.youtube.com/watch?v=b2PESRl7De4)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 강력한 최첨단 AI 모델들이 사이버 보안에 혁명을 일으키고 있습니다. 앤트로픽의 미소스(Mythos)와 같은 모델, 그리고 다른 벤더들의 유사한 모델들이 곳곳에서 등장하면서 수십 년 동안 표면 아래에 숨어 있던 보안 취약점을 드러내고 있습니다. 그들이 이전에는 볼 수 없었던 속도와 규모로 이러한 격차를 파악하는 능력은 공격 일정을 단축시키고 있습니다. 지연으로 인한 비용은 이제 몇 달이 아닌…
- B8 부정 성과: 보안·프라이버시: 앤트로픽의 미소스(Mythos)와 같은 모델, 그리고 다른 벤더들의 유사한 모델들이 곳곳에서 등장하면서 수십 년 동안 표면 아래에 숨어 있던 보안 취약점을 드러내고 있습니다.
- B7 성과: 운영효율: 그래서 우리가 확인한 것 중 하나는 일부 조직에서 데이터 유출 사고 이후 상당한 비용 절감 효과를 본 부분이 있다는 것이었습니다.
- 수치 주장: 2026년 데이터 유출 비용 보고서를 살펴보고, 이 보고서가 우리에게 무엇을 알려주는지, 개선해야 할 부분은 어디인지 , 그리고 우리가 무엇을 할 수 있는지 알아보겠습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/IBM_Technology/2026_Cost_of_a_Data_Breach_Report_AI_Is_Changing_Cybersecuri__b2PESRl7De4.md`

**118. [GLM-5.2: The real security risk? Plus: Vibe hunting, the end of CVSS and updates on Lightwell](https://www.youtube.com/watch?v=qXGJ7pi-XOo)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 개방형 가중치 모델이 적어도 일부 영역에서는 신화적인 수준의 역량에 도달하고 있다는 보고가 있다 . 패널 여러분, 어떤 생각이 드시나요 ? 사악한 모그, 자네부터 시작하겠네. 제 말은, 이런 모델들이 점점 더 무서워지고 있다는 거예요. 그런데 그게 오히려 제게는 더 편하죠. 진짜 합법적인 모델들은 사이버 보안 검증 프로그램에 참여하고 있을 때조차도 사용을 막는 분류기를 점점 더 많이 추가하고…
- B1 디지털·AI 기술의 활용: 그리고 국가 취약점 데이터베이스(NVD)의 업데이트가 오랫동안 이루어지지 않아서 전체 프로세스가 망가지면, 일반적으로 CVE 번호가 할당된 크래시를 찾기 위해 사람들이 클라우드를 추적하게 될 것입니다 .
- B8 부정 성과: 보안·프라이버시: 문제는 인공지능이라는 요정을 다시 병 속에 가두는 것이 아니라, 사이버 공격자들이 자동화된 코드를 개발하기 전에 방어 네트워크 전반에 걸쳐 인공지능을 보편화하여 우리의 방어 태세를 강화하는 것입니다 .
- 수치 주장: 따라서 갑자기 분류 자동화 시스템을 도입한 이 사람들을 2단계에 배치한다면, 그들에게 AI라는 안전장치를 씌워주고 "지난 1년간 훈련받은 근육 기억을 활용해 문제를 해결하세요.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 추론 최적화 · 칩·하드웨어 · 코딩 에이전트
- 원문: `transcripts/channels/IBM_Technology/GLM-5.2_The_real_security_risk_Plus_Vibe_hunting,_the_end_of__qXGJ7pi-XOo.md`

**119. [GPT-5.6 Sol, FIFA AI & Wall Street’s AI nerves](https://www.youtube.com/watch?v=tV5zXS78HzU)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 음, 오픈아이얼의 원래 대외적인 성격을 생각해 보면, 그것은 오로지 안전성 확보에 관한 것이었습니다. 그러니까, 2019년경 그들의 웹페이지를 다시 살펴보면, 바로 그런 내용을 볼 수 있을 겁니다. 오늘 전문가 토론에서 이 모든 것과 그 이상의 이야기를 들어보세요 . 저는 팀 황입니다. [음악]이고, Mixture of Experts에 오신 것을 환영합니다. MOE는 매주 인공지능 분야의 연…
- B1 디지털·AI 기술의 활용: 원래 AWS 연구원들이 일부 정보에 접근하는 방법을 찾아냈지만, 앤 트로픽 측에서는 GPT-54와 기존 앤트로픽 모델을 사용하면 이미 그 정보를 얻을 수 있었다고 주장했습니다.
- B2 파괴: 경쟁구도: 만약 경쟁자들이 서로를 감시하는 구도로만 운영된다면 우리는 분명히 곤경에 처할 것입니다.
- 수치 주장: 네, 그러니까 사람들이 말하는 오픈 소스 모델이 독점 모델보다 얼마나 뒤처지는지에 대한 범위가 있는데, 그 범위는 0개월에서 12개월 정도입니다.
- 교량: — · 기술: LLM 모델 · 추론 최적화
- 원문: `transcripts/channels/IBM_Technology/GPT-5.6_Sol,_FIFA_AI_&_Wall_Street’s_AI_nerves__tV5zXS78HzU.md`

**120. [GPT-Red: Can AI red teams stop prompt injections?](https://www.youtube.com/watch?v=g4CNcUAqM4Q)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B6 장벽 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B7 긍정 성과
- 개요: GPT Red는 자동화된 레드팀 활동을 수행하고, Scam Buster는 자동화된 사기 차단 활동을 수행합니다. 패널 여러분, 어떻게 생각하시나요? 그렇다면 이제 모든 것을 봇에게 넘겨줄 때가 된 걸까요 ? 키미, 당신부터 시작하죠. 아니요, 아직 봇에게 넘겨줄 때가 아닙니다. 애초에 누가 이 악순환을 시작했나요 ? [웃음] 저는 요리만 로봇에게 맡길 준비가 되어 있어요 . 그런 도구가 있다…
- B1 디지털·AI 기술의 활용: 음, 하지만, 좀 더 긍정적인 측면에서 보자면 , 제게 흥미로운 점 중 하나는 OpenAI가 GPT Red를 다른 모델 기반 보안 노력, 특히 분류기 와 비교하는 방식입니다.
- B8 부정 성과: 보안·프라이버시: 그래서 사이버 보안 분야에 종사하든, 그렇지 않든, 혹은 악용할 만한 요소를 찾고 있든 간에 , 그런 요소들이 실제로 악용할지 말지에 영향을 미칠 거라고 생각합니다 .
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/IBM_Technology/GPT-Red_Can_AI_red_teams_stop_prompt_injections__g4CNcUAqM4Q.md`

**121. [Reddit cracks down on AI slop & the future of AI compute](https://www.youtube.com/watch?v=WHFLWrnFc1E)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 5/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 인공지능이 일상생활의 패턴에 자연스럽게 녹아들고 대부분의 사람들이 평소 생활 리듬 안에서 인공지능을 사용한다는 점이 정말 흥미로웠고, 이는 전 세계 사람들의 정신 건강에 긍정적인 영향을 미칠 것이라고 생각합니다. 오늘 전문가들의 다양한 의견을 통해 이 모든 것과 더 많은 것을 알아보세요. 안녕하세요, 저는 팀 행입니다. 새 사무실에서 소식을 전해드리고 있으며, 다양한 전문가들이 모인 커뮤니티…
- B4 가치네트워크·생태계: 또 다른 부분은, 인공지능 구축 생태계에 속해 있는 사람으로서 때때로 에이전트, 챗봇, 래그 등을 만드는 추상적인 패턴에만 집중하기 쉽고, 이러한 것들이 실제 환경에 어떻게 배포되는지에 대해서는 충분히 생각하지 않는다는 점입니다.
- B1 디지털·AI 기술의 활용: 음, 아시다시피 엔비디아는 새로운 AI 컴퓨팅 제공업체와 협력하여 네오클라우드 구축에 필요한 인프라와 그래픽 카드, 네트워킹 장비 등을 제공하고, 향후 수익의 일부를 가져가는 방식을 꽤 오래전부터 해왔습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/IBM_Technology/Reddit_cracks_down_on_AI_slop_&_the_future_of_AI_compute__WHFLWrnFc1E.md`

**122. [The Cost of a Data Breach 2026, and what we can learn from the Hugging Face hack](https://www.youtube.com/watch?v=lx41qvj80Jo)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 데이터 유출 비용의 날을 기념하는 모든 분들께 행복한 하루 되세요. 패널 여러분, 올해 보고서에서 가장 핵심적인 내용을 한 문장으로 요약하자면 무엇인가요? 제프, 당신부터 시작하죠. 제 생각에는 우리가 감염 경로를 파악하고 통제하는 데 너무 오랜 시간이 걸리고 있는 것 같습니다. 약 2/3년 정도 걸립니다 . 우리는 여전히 접근 제어 및 권한 상승과 같은 기본적인 보안 문제에서 발생하는 문제…
- B8 부정 성과: 보안·프라이버시: 오늘 데이터 유출 비용에 대한 논의를 마무리하면서, 인공지능 경쟁이 치열한 상황에서 "보안 태세를 강화하기 위해 무엇을 해야 할까 ?"를 고민하는 조직들이 앞으로 어떤 조치를 취해야 할지에 대한 여러분의 생각과 의견을 듣고 싶습니다.
- B4 가치네트워크·생태계: 그리고 우리가 여러 기업들과 함께 만들어 온 오픈 시큐어 얼라이언스(Open Secure Alliance)에 대해 말씀드리자면 , 선량한 사람들이 모여 공개적으로 협력하여 세상에서 일어나고 있는 좋은 일들을 지켜나가야 합니다.
- 수치 주장: 반면에, 기업 보안에 AI를 활용하는 기업들은 약 193만 달러의 비용 절감 효과를 보고 있다는 점도 주목할 만합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 거버넌스·평가 도구
- 원문: `transcripts/channels/IBM_Technology/The_Cost_of_a_Data_Breach_2026,_and_what_we_can_learn_from_t__lx41qvj80Jo.md`

**123. [The new post-quantum cryptography executive order. Plus: What is Q-Day, really?](https://www.youtube.com/watch?v=RYUR9BdDgyI)** — IBM Technology · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 사이버 보안 담당자로서 우리는 정말 큰 과제와 많은 정보들을 접하게 될 것입니다 . 우리가 많이 들어본 최첨단 AI 모델이 아니더라도 , AI 자체와 그것을 안전하고 보안이 유지되는 방식으로 구현하는 방법에 대한 논의도 분명히 중요합니다. Q-데이. 양자 컴퓨팅 기술이 웹사이트, 이메일, 디지털 서명, 은행 계좌, 블록체인 등 모든 것을 보호하는 데 사용하는 공개 키 암호화를 마침내 해독할 …
- B4 민첩성·양손잡이: 수주, 암호 화폐 민첩성(Crypto agility)에 대한 정의가 있나요?
- B4 가치네트워크·생태계: 생태계의 다양한 요소들을 고려해야 하고, 일반적인 기업을 생각해 보면 공급망 전반에 걸친 상호 운용성도 고려해야 하기 때문입니다.
- 수치 주장: 그래서 트럼프 대통령은 월요일에 양자 후 암호화에 관한 행정 명령에 서명했는데, 이는 현대 암호화에서 양자 컴퓨터 공격에 취약 하지 않은 새로운 암호화로의 전환을 다루기 위한 미국 정부의 10년 동안 지속된 정책 노력의 가장 최근의 진전입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/IBM_Technology/The_new_post-quantum_cryptography_executive_order._Plus_What__RYUR9BdDgyI.md`

---

## Infosys


**124. [Brand Finance Global 500 Launch 2026 | AI Rising: The Evolution of Brand & Trust Panel | Davos 2026](https://www.youtube.com/watch?v=2GboyaQ1VKs)** — Infosys · 수요기업·기타 · IN · 2026-03 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽
- 개요: 좋은 아침이에요. [목을 가다듬으며] 네, 오늘 아침 회의에 참석해주신 모든 분들을 환영합니다 . 안녕하세요, 오늘 이렇게 여러분 모두를 뵙게 되어 기쁩니다. 브랜드 파이낸스에서 발표하는 '글로벌 500 2026'을 공개하게 되어 반갑습니다. 네, 이것이 세계에서 가장 가치 있고 강력한 브랜드를 조사한 저희 연례 연구 결과입니다. 그리고 저희는 인공지능 시대에서 브랜드와 신뢰의 진화에 대한 …
- B5 조직구조 변화: 부서 간 협업과 그 중요성 측면에서 볼 때, AI가 오히려 기능별 사일로를 강화하는 방향으로 작용하고 있다고 보십니까 ?
- B5 리더십·CDO/CAIO: 그래서 제 질문은 리더십, 사고방식, 그리고 리더의 역할 측면에서 지금 리더의 위치는 어디라고 생각하시는지입니다.
- 수치 주장: 그것들은 실질적인 금전적 가치를 지니고 있었고, 30년이 지난 지금, 세상이 디지털 마케팅 혁명과 소위 퍼포먼스 마케팅의 등장으로 극적으로 변했음에도 불구하고, 브랜드 구축을 기리고 옹호하는 우리의 사명은 여전히 ​​매우 중요하다고 생각합니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Infosys/Brand_Finance_Global_500_Launch_2026_AI_Rising_The_Evolution__2GboyaQ1VKs.md`

**125. [Live: Infosys Q1 FY27 Press Conference](https://www.youtube.com/watch?v=mTnEo9TGv6Y)** — Infosys · 수요기업·기타 · IN · 2026-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: A very good evening everyone and thank you for joining. ing Infosys's first quarter financial results. My name is Rishi and on behalf of Infosys, I'd like to welcome all of you today. I would first like to invite our cha…
- B1 디지털·AI 기술의 활용: Our clients are able to work with any foundation model closed open weight or on the cloud on their own servers.
- B7 성과: 조직성과: uh our revenue growth for Q1 was at 2.4% year-onear and 1% quarteron quarter in constant currency terms.
- 수치 주장: So that's all new revenue and also the productivity will happen but the the significance I think already we can start to see and if I can just add if you look at when we when we launched our hexagon in February of this year our air revenue for Q3 was 5.5% of o…
- 교량: 정의 확장(DX→AX 계승), Avenue 1 동적역량 · 기술: 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Infosys/Live_Infosys_Q1_FY27_Press_Conference__mTnEo9TGv6Y.md`

---

## Insight Solutions


**126. [Innovating & Measuring ROI for Enterprise Organizations Through Generative AI](https://www.youtube.com/watch?v=U84H7KOAlyU)** — Insight Solutions · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 오늘 참석해주신 모든 분들께 감사드립니다. 이렇게 함께하게 되어 정말 기쁩니다. 오늘 제가 말씀드리고 싶은 것은 기업의 혁신과 ROI 측정에 관한 것입니다. 생성형 AI를 중심으로 이야기를 나눠볼 건데요, 생성형 AI의 개념들을 살펴보고, 무엇보다 이러한 기술을 활용하여 실질적인 ROI를 측정하는 방법에 대해 논의할 것입니다. 저희가 사용해 온 다양한 구현 전략과 여러분의 조직에서도 고려해 …
- B1 디지털·AI 기술의 활용: 이제 GPT(가상 물리 처리) 또는 생성형 AI의 세계로 나아가면, 이러한 작업들을 훨씬 효율적으로 수행할 수 있을 것입니다.
- B7 성과: 운영효율: 이 글의 첫 번째 부분(왼쪽 상단)에서는 재무 목표, 경쟁 우위, 운영 효율성 등 앞서 설명한 영역을 측정할 수 있는 지표에 대해 이야기하고 있습니다.
- 수치 주장: 생성형 디자인 AI가 시간이 지남에 따라 디자인 작업의 60%를 자동화할 것이라는 예측이 있는데, 저도 동의합니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/2026-08-03/Innovating_&_Measuring_ROI_for_Enterprise_Organizations_Thro__U84H7KOAlyU.md`

---

## Intel


**127. [Building AI Tools to Transform Sales and Marketing, an Inside Look | Intel](https://www.youtube.com/watch?v=J7wGwY0lX_E)** — Intel · 인프라·칩·전력 · US · 2024-12 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로
- 개요: [음악] 안녕하세요 여러분, 인텔 온 어 인텔의 또 다른 에피소드에 오신 것을 환영합니다. 저는 진행자 라이언 카슨입니다. 오늘 방송을 시작하게 되어 매우 기쁩니다. 인텔에서 직접 모신 두 분의 게스트와 함께 흥미로운 도구들을 개발하고 있습니다. 저희가 어떻게 개발하는지 자세히 알아보고, 여러분과 지식을 공유하고자 합니다. 먼저 보아즈 아프란 님을 모셨습니다. 보아즈 님은 인텔에서 영업 및 …
- B7 성과: 운영효율: 예를 들어, 직원들의 업무 효율성과 생산성을 높이고 시간을 절약할 수 있는 기회는 어디인지, 비용을 절감하거나 매출을 증대시킬 수 있는 기회는 어디인지 등을 고려합니다.
- B1 디지털·AI 기술의 활용: 그래서 모든 분야에 걸쳐 이러한 전문성을 갖추는 것이 매우 중요하며, 물론 훌륭한 AI 개발팀 과 과학자, 머신러닝 전문가를 확보하여 고품질 제품을 만들어야 합니다.
- 수치 주장: 보아즈 님은 인텔에서 영업 및 마케팅 AI를 총괄하고 있으며, 기술 중심의 사업 개발 및 제품 관리 분야에서 29년 이상의 경력을 보유하고 있습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Intel/Building_AI_Tools_to_Transform_Sales_and_Marketing,_an_Insid__J7wGwY0lX_E.md`

**128. [AI PCs | Discover a New World of Experiences | Intel](https://www.youtube.com/watch?v=3PTyqM2BFpQ)** — Intel · 인프라·칩·전력 · US · 2025-01 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] n [음악] you [음악] 네, 우선 오늘 세션에 오신 것을 환영합니다. 저는 칼라 로드리게스이고, 인텔 클라이언트 소프트웨어 개발 및 활성화를 담당하고 있습니다. 즉, 저희는 생태계 내의 많은 소프트웨어 파트너와 협력할 기회를 갖고 있으며, 잠시 후 그중 몇몇 분들의 이야기를 들어보실 수 있을 겁니다. 오늘 세션에서는 AIP PCS가 소비자 및 기업 부문 사용자 모두에게 어떻게 …
- B1 디지털·AI 기술의 활용: 좋은 예시인데요, 저는 몇 달 동안 OpenAI의 채팅, GPT, 이미지 생성, 텍스트 생성 기능을 구독했지만, 이제 인텔 노트북에서 모든 기능을 사용할 수 있게 되었습니다.
- B8 부정 성과: 보안·프라이버시: 특히 데이터 거버넌스와 관련된 개인정보 보호 및 보안 문제는 어떻게 해결해야 할까요?
- 수치 주장: 저희는 그렇게 보고 있지만, 2주 안에 새로운 기능을 출시할 예정입니다.
- 교량: — · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/Intel/AI_PCs_Discover_a_New_World_of_Experiences_Intel__3PTyqM2BFpQ.md`

**129. [AI at the Edge | Transforming Industries and the Workplace​ | Intel](https://www.youtube.com/watch?v=mrWTLjitaX4)** — Intel · 인프라·칩·전력 · US · 2025-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] [박수] [음악] 오 [음악] 안녕하세요 여러분, 이렇게 함께하게 되어 기쁩니다. 저는 댄 로드리게스이고, 인텔의 엣지 컴퓨팅 그룹을 이끌고 있습니다. CS는 항상 훌륭한 혁신으로 가득 차 있는데, 올해도 예외는 아닙니다. 올해의 핵심 주제 중 하나이자 업계에서 가장 뜨거운 이슈는 바로 AI입니다. 오늘 우리는 AI가 다양한 산업 분야와 여러 사용 사례에서 어떻게 엣지 컴퓨팅으로 확…
- B1 디지털·AI 기술의 활용: 인공지능과 같은 기술을 활용하여 이러한 디지털 트윈을 만들고, 최적의 치료법을 찾아내고, 나아가 환자에게 예방적인 치료를 제공하여 환자가 치료를 받지 않아도 되도록 할 수 있는 잠재력이 있는 것입니다.
- B4 가치네트워크·생태계: 따라서 적절한 생태계, 적절한 파트너십 시스템을 구축하고, 적절한 자문 위원회를 구성하여 앞으로 다가올 변화에 대한 정보를 미리 얻는 것이 조직 내부적으로 매우 중요합니다.
- 수치 주장: 또한 2026년 말까지 모든 엣지 컴퓨팅 구축의 50% 이상이 머신 러닝을 통합하고, 2029년 말까지 60%가 예측 및 생성 AI를 통합할 것이라고 예측했습니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Intel/AI_at_the_Edge_Transforming_Industries_and_the_Workplace​_In__mrWTLjitaX4.md`

**130. [Intel Keynote: AI Inside for a New Era | Intel](https://www.youtube.com/watch?v=8z9o2ltnFM0)** — Intel · 인프라·칩·전력 · US · 2025-01 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 본 프레젠테이션에서 미래 계획이나 기대에 대한 언급은 미래예측 진술입니다. 이러한 진술은 현재의 기대를 기반으로 하며, 실제 결과가 해당 진술에 명시적 또는 묵시적으로 표현된 내용과 크게 다를 수 있는 많은 위험과 불확실성을 내포하고 있습니다. 실제 결과가 크게 달라질 수 있는 요인에 대한 자세한 내용은 www.c.com에서 당사의 최신 실적 발표 및 SEC 공시 자료를 참조하십시오. [음악…
- B4 가치네트워크·생태계: 파트너사인 샘, 루카, 알렉스, 그리고 이 자리에 계신 모든 분들, 그리고 생태계 전반에 걸쳐 함께 비전을 공유하고 현실로 만들어주신 모든 분들께 진심으로 감사드립니다.
- B7 성과: 운영효율: 연구 결과에 따르면 보안 사고가 62% 감소했고, 보고된 펌 공격은 3배 줄었으며, 고객의 80%는 새로운 Windows 11 PC가 이전 장치보다 보안 및 데이터 보호 기능이 향상되었다고 답했습니다.
- 수치 주장: 특히 올해는 이번 주에 출시하는 제품뿐만 아니라 2025년 이후 사업 전반에 걸쳐 제가 보는 모든 기회 때문에 더욱 기대가 큽니다.
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Intel/Intel_Keynote_AI_Inside_for_a_New_Era_Intel__8z9o2ltnFM0.md`

**131. [Direct Connect 2025 Keynote | Intel](https://www.youtube.com/watch?v=0ED7n2g8lO0)** — Intel · 인프라·칩·전력 · US · 2025-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 본 발표 자료에 포함 된 향후 계획 또는 기대에 대한 언급은 미래예측 진술입니다. 이러한 진술은 현재의 기대치를 바탕으로 하며, 실제 결과가 이러한 진술에 명시적 또는 묵시적으로 표현된 내용과 크게 다를 수 있는 많은 위험과 불확실성을 내포하고 있습니다. 실제 결과가 예상과 크게 다를 수 있는 요인에 대한 자세한 내용은 www.inttc.com에서 확인할 수 있는 최신 실적 발표 자료 및 S…
- B4 가치네트워크·생태계: 또한 파트너십을 통해 더 나은 솔루션을 제공하기 위해 PDK와 협력하여 저희 공장에서 테스트 칩을 가동하고 있으며, 이를 통해 생태계 파트너들에게 필요한 자료를 제공할 수 있도록 정확한 데이터를 수집하고 있습니다.
- B7 성과: 운영효율: 저희 EIP 및 fversus 솔루션은 고객에게 더 나은 전력 효율성, 대역폭 및 비용 절감을 제공하기 위해 사용되고 있으며, 후면 전력 공급을 통한 전력 공급과 결합된 리빈 피드 방식의 게이트는 차세대 공정 노드의 핵심 차별화 요소입니다.
- 수치 주장: 저희 첫 번째 펜탈 레이크(Pental Lake) 제품은 연말에 출시될 예정이며, 2026년 상반기에는 더 많은 제품이 출시될 것입니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Intel/Direct_Connect_2025_Keynote_Intel__0ED7n2g8lO0.md`

**132. [Scaling Enterprise AI: Inference, Infrastructure, and the Future of Intelligence | Intel](https://www.youtube.com/watch?v=UMc1ShyUcs8)** — Intel · 인프라·칩·전력 · US · 2025-04 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요, 청취자와 리더를 연결하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다 . 2025년 첫 번째 에피소드입니다. 저는 헤더이고, 진행을 맡게 되었습니다. 오늘 첫 번째 게스트는 루크 노리스입니다. 루크 노리스는 카마와자 AI의 공동 창립자로서, 안전하고 확장 가능한 차세대 AI 배포에 중점을 두고 기업 AI 혁신을 주도하고 있습니다. 1억 달러 이상의 벤처 캐피털을 유치…
- B7 성과: 운영효율: 그리고 우주 탐사도 있지만, 저는 지금 정부가 변화에 적응하고 , 말씀하신 것처럼 실시간으로 대응하며, "이봐, 다시 한번 말하지만, 아주 사소한 변화만 줘도 장기적으로 그만큼의 비용을 절감할 수 있어"라고 말할 수 있는 능력에 대해 생각하고 있습니다.
- B1 디지털·AI 기술의 활용: 기업 환경에서 자율 AI 에이전트의 등장에 대해 이야기할 때 , 이러한 에이전트의 숨겨진 활용 사례는 무엇이며, 기업에 어떤 이점을 제공할 수 있을까요 ?
- 수치 주장: 1억 달러 이상의 벤처 캐피털을 유치하고 포춘 500대 기업을 대상으로 글로벌 AI IML 구축을 주도한 풍부한 경험을 바탕으로 , 루크는 기업이 탁월한 유연성과 효율성 으로 AI의 잠재력을 최대한 활용할 수 있도록 지원하는 데 열정을 쏟고 있습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Intel/Scaling_Enterprise_AI_Inference,_Infrastructure,_and_the_Fut__UMc1ShyUcs8.md`

**133. [The AI-Powered Enterprise: Insights from Lumen Technologies | Intel](https://www.youtube.com/watch?v=JUfwnwpbx0M)** — Intel · 인프라·칩·전력 · US · 2025-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 인텔 온 AI에 오신 것을 환영합니다. 이 팟캐스트는 청취자와 리더를 연결해 드립니다. 제 이름은 헤더이고, 여러분을 안내할 예정입니다. 오늘의 게스트는 라이언 아즈도르입니다. 라이언은 루멘 테크놀로지스의 수석 부사장 겸 최고 마케팅 책임자입니다 . 그는 자작 기기 마니아로, 모든 직종에서 사용자의 요구에 맞는 기술을 개발하는 방법을 모색하고 있습니다 . 뉴먼 테크놀로지스는 인공지능…
- B1 디지털·AI 기술의 활용: 저희는 AI에 최적화된 인프라, 즉 멀티클라우드 인프라를 구현하는 데 앞장서고 있으며, 이것이 바로 저희가 세상 에서 어떤 역할을 해야 하는지에 대한 저희의 생각입니다.
- B2 파괴: 소비자 행동·기대: 소매업을 생각해 보면, 소매업체는 AI를 사용하여 개인화된 고객 경험과 사기 방지를 구현하고 있습니다.
- 수치 주장: 불과 2년, 1년 반 전만 해도 OpenAI, LLMs, Gen AI 등에서 다양한 변화가 일어나기 시작했다는 게 믿기지 않을 정도입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Intel/The_AI-Powered_Enterprise_Insights_from_Lumen_Technologies_I__JUfwnwpbx0M.md`

**134. [Building Scalable and Sustainable AI Infrastructure | Intel](https://www.youtube.com/watch?v=U0oZkI_nYYA)** — Intel · 인프라·칩·전력 · US · 2025-05 · en · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [Music] [Applause] [Music] Welcome to Intel on AI, the podcast that connects leaders with listeners. My name is Heather McGwigan and I am your host. Today's guest is Ray Pang. Ray Pang is the senior vice president techno…
- B4 가치네트워크·생태계: So another way to look at this why you need to work in an ecosystem with different partners is because today the technology we need to deliver to our customers are so complex.
- B1 디지털·AI 기술의 활용: So today all the AI models we are talking about no matter whose foundation model whether it's you know the the gra from XAI the the Chad GBT the the cloud the mistro they all based on transformer okay transformer based model is fantastic but it has something c…
- 수치 주장: So, we are 10 minutes away from Intel's R&amp;D, you know, building, right?
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Intel/Building_Scalable_and_Sustainable_AI_Infrastructure_Intel__U0oZkI_nYYA.md`

**135. [Edge AI – The Next Transformation | Intel](https://www.youtube.com/watch?v=xPadduZuK4Q)** — Intel · 인프라·칩·전력 · US · 2025-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] [박수] [음악] 인텔 온 AI에 오신 것을 환영합니다. 이 팟캐스트는 청취자와 리더를 연결해 드립니다. 제 이름은 헤더 맥위건이고, 여러분의 진행을 맡고 있습니다. 오늘의 게스트는 댄 로드리게스입니다. 댄은 인텔의 기업 부사장 겸 엣지 컴퓨팅 그룹 총괄 책임자입니다 . 댄은 엣지 컴퓨팅 생태계가 성장하고 기업 전반에 걸쳐 인텔 플랫폼이 배포될 때 최대한의 이점을 누릴 수 있도록 지…
- B4 가치네트워크·생태계: 따라서 저희의 개방형 엣지 접근 방식은 다양한 시장의 다양한 고객에게 다양한 솔루션을 제공하는 전체 가치 사슬을 고려하려고 노력하며, 저희의 전반적인 전략과 목표는 파트너가 엣지에서 AI를 더 쉽게 배포할 수 있도록 지원하는 것입니다.
- B1 디지털·AI 기술의 활용: 따라서 생성형 AI, 특히 비전-언어-행동 모델과 같은 새로운 추론 모델의 발전으로 AI 에이전트와 함께 실행될 수 있게 되면서 더욱 향상된 자동화를 구현할 수 있으며, 이는 궁극적으로 비용 절감으로 이어질 것입니다.
- 수치 주장: 그리고 인텔 AMX 및 Bflat 16 기술과 OpenVeno를 활용한 내장 가속 기능을 갖춘 4세대 Zeon을 사용했을 때, 이전 세대 Zeon을 사용할 때보다 추론 속도가 35배 향상되었습니다 .
- 교량: 정의 확장(DX→AX 계승), Avenue 1 동적역량 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/Intel/Edge_AI_–_The_Next_Transformation_Intel__xPadduZuK4Q.md`

**136. [From Smart Devices to Supply Chain: Lenovo's Blueprint for Trust in Tech | InTechnology | Intel](https://www.youtube.com/watch?v=Ojz9U4ao3go)** — Intel · 인프라·칩·전력 · US · 2025-05 · en · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: (gentle music) [Announcer] You are watching "InTechnology," a video cast where you can get smarter about cybersecurity, sustainability, and technology. (gentle music) - Hi, welcome back to the "InTechnology" podcast. I'm…
- B4 가치네트워크·생태계: - Yeah, I think everybody who's paying attention is focusing heavily on really business continuity or business resiliency in the supply chain area.
- B8 부정 성과: 보안·프라이버시: We look at inclusion, we have privacy and security reviews, accountability and reliability, explainability, transparency, and environmental and social impact.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Intel/From_Smart_Devices_to_Supply_Chain_Lenovo's_Blueprint_for_Tr__Ojz9U4ao3go.md`

**137. [Designing Empathetic AI: The Future of Human-Centered Technology | Intel](https://www.youtube.com/watch?v=atZ1lRqE8wY)** — Intel · 인프라·칩·전력 · US · 2025-06 · en · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [Music] Welcome to Intel on AI, the podcast that connects listeners with leaders. My name is Heather McGuigan and I am your host. Today's guest is Ted Shelton. Ted is a senior leader at Inflection AI, which is shaping th…
- B1 디지털·AI 기술의 활용: I can use an LLM to take the entire context of a particular data element to be able to then compare it to the other data source and figure out which of these XYZ's is important.
- B4 민첩성·양손잡이: Um and the most valuable experimentation is the experimentation that you know from the outset is going to fail.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/Intel/Designing_Empathetic_AI_The_Future_of_Human-Centered_Technol__atZ1lRqE8wY.md`

**138. [AI for Accessibility: How Sorenson Is Advancing Inclusive Communication | Intel](https://www.youtube.com/watch?v=vx1g4xu5qMk)** — Intel · 인프라·칩·전력 · US · 2025-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B5 구조 변화, B6 장벽
- 개요: [음악] 리더들이 함께 듣고 소통하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다 . 오늘의 게스트는 마리암 라마니입니다. 마리암은 소렌 커뮤니케이션즈의 AI 부문 수석 이사입니다 . 그녀는 10년 이상 AI 기반 솔루션 제품 개발 및 소프트웨어 엔지니어링 분야에서 경험을 쌓아왔으며, 특히 청각 장애인과 비장애인 간의 의사소통 격차를 해소하는 혁신적인 AI 기반 솔루션 개발을 전문으로 합…
- B7 성과: 사회적 편익: 그녀는 10년 이상 AI 기반 솔루션 제품 개발 및 소프트웨어 엔지니어링 분야에서 경험을 쌓아왔으며, 특히 청각 장애인과 비장애인 간의 의사소통 격차를 해소하는 혁신적인 AI 기반 솔루션 개발을 전문으로 합니다.
- B3 전략적 대응: 저는 제가 평생 읽은 모든 책을 읽고, 본 모든 영화를 보고, 들었던 모든 음악을 듣고, 저 자신을 아주 잘 알고, 제 사고방식을 잘 이해하고, 더 나은 제가 될 수 있도록 로드맵을 제시해 줄 시스템이나 인공지능을 원합니다.
- 수치 주장: 그녀는 10년 이상 AI 기반 솔루션 제품 개발 및 소프트웨어 엔지니어링 분야에서 경험을 쌓아왔으며, 특히 청각 장애인과 비장애인 간의 의사소통 격차를 해소하는 혁신적인 AI 기반 솔루션 개발을 전문으로 합니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Intel/AI_for_Accessibility_How_Sorenson_Is_Advancing_Inclusive_Com__vx1g4xu5qMk.md`

**139. [AI PCs and the Future of Cybersecurity: AI-Powered Protection from Deepfakes | Intel](https://www.youtube.com/watch?v=GzFE6k-S3vA)** — Intel · 인프라·칩·전력 · US · 2025-09 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 리더와 청취자를 연결하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다. 제 이름은 헤더 맥위건이고, 여러분의 진행을 맡고 있습니다. 오늘의 게스트는 레나 엘리아스입니다. 레나는 Jen의 최고 제품 책임자이며, Jen은 Norton, Avast, Liflock, Money Lion 등 다양한 브랜드를 보유하고 있습니다. 그녀는 Gen에서 사이버 안전 사업을 이끌며 전 세계 5억 명…
- B8 부정 성과: 보안·프라이버시: 네, 제 생각에는 딥페이크는 원래 영화 장면에 자신을 합성하는 것처럼 재미있는 용도로 시작했지만, 오용될 가능성도 있기 때문에 점점 더 큰 문제로 대두되고 있다는 점을 기억하는 것이 중요하다고 생각합니다.
- B1 디지털·AI 기술의 활용: 음, 그러니까 데이터를 클라우드로 보냈다가 다시 받아오는 과정에서 지연이 발생하지만, PC에서 직접 분석하면 그런 지연 시간을 줄일 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/Intel/AI_PCs_and_the_Future_of_Cybersecurity_AI-Powered_Protection__GzFE6k-S3vA.md`

**140. [From PoC to Production: How Lenovo Turns AI into Enterprise Impact | Intel](https://www.youtube.com/watch?v=JI9W8S_6QbY)** — Intel · 인프라·칩·전력 · US · 2025-09 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: [음악] 리더와 청취자를 연결하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다. 제 이름은 헤더 맥위건이고, 여러분의 진행을 맡고 있습니다. 오늘의 게스트는 데이비드 엘리슨입니다. 데이비드 엘리슨은 레노버 ISG의 최고 데이터 과학자이자 AI 엔지니어링 책임자입니다 . 그는 레노버의 미국 및 유럽 AI 연구 개발 센터를 통해 최첨단 AI 기술을 활용하여 외부 고객에게 솔루션을 제공하는 팀…
- B3 전략적 대응: 그는 레노버의 미국 및 유럽 AI 연구 개발 센터를 통해 최첨단 AI 기술을 활용하여 외부 고객에게 솔루션을 제공하는 팀을 이끌고 있으며, 동시에 전 세계 인프라 솔루션 그룹의 전반적인 AI 전략을 내부적으로 지원하고 있습니다.
- B5 직무·역량 변화: 레노버에 합류하기 전에는 국제적인 과학 분석 및 장비 회사를 운영했으며, 미국 우정청에서 데이터 과학자로 근무했습니다 .
- 수치 주장: 수백 건의 개념 증명 프로젝트를 성공적으로 완료한 지금 , 고객이 멋진 데모를 실제 운영 환경에 배포할 수 있도록 어떻게 도울 수 있을까요?
- 교량: — · 기술: —
- 원문: `transcripts/channels/Intel/From_PoC_to_Production_How_Lenovo_Turns_AI_into_Enterprise_I__JI9W8S_6QbY.md`

**141. [Agentic AI in Action: Transforming Health, Education, and Consumer Experiences | Intel](https://www.youtube.com/watch?v=5wlY9FcvRiE)** — Intel · 인프라·칩·전력 · US · 2025-10 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: Welcome to Intel on AI, the podcast that connects leaders with listeners. Today's guest is Stacy Shulman. Stacy Shulman is the vice president and GM of health, education and consumer industries at Intel. She leads the ch…
- B1 디지털·AI 기술의 활용: So it's this AI, plus this AI, it's machine learning, you know, we'll go back to machine learning, who's been a stable AI, you know, tool for many years.
- B4 가치네트워크·생태계: Intel often talks about combining hardware, software and ecosystem partnerships to drive AI innovation.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/Intel/Agentic_AI_in_Action_Transforming_Health,_Education,_and_Con__5wlY9FcvRiE.md`

**142. [The Age of With: Rethinking Enterprise Strategy Through Agentic AI | Intel](https://www.youtube.com/watch?v=NgeYg6tyncs)** — Intel · 인프라·칩·전력 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] [박수] 리더와 청취자를 연결하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다. 제 이름은 헤더 맥위건이고, 여러분의 진행을 맡고 있습니다. 오늘의 게스트는 Bares Sesh입니다. 바레쉬는 디오이트의 기술, 미디어, 엔터테인먼트 및 통신(TMT) 산업 분야 AI 사업부의 글로벌 리더입니다. 그는 사려 깊은 리더로 인정받고 있으며, 업계 포럼, 출판물 및 행사에서 작가이자 연사…
- B5 리더십·CDO/CAIO: 우선, 역사적으로 기술은 최고 정보 책임자(CIO)나 최고 기술 책임자(CTO), 또는 최고 디지털 책임자(CDO)의 영역이었죠.
- B3 전략적 대응: 실제로 한 금융 서비스 고객사의 CEO와 경영진과 회의를 했는데, 그녀가 어젯밤에 AI 코딩 도구 중 하나를 사용해서 바이브코딩을 해봤다고 하더군요.
- 수치 주장: 만약 제가 오늘날 AI를 활용하여 기업 프로세스나 비즈니스 프로세스를 설계한다면, 20년 전이나 30년 전과 같은 방식으로 설계할까요?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Intel/The_Age_of_With_Rethinking_Enterprise_Strategy_Through_Agent__NgeYg6tyncs.md`

**143. [AI Industrialization: The Next Frontier for Global Enterprises | Intel](https://www.youtube.com/watch?v=fSadUMtpwcY)** — Intel · 인프라·칩·전력 · US · 2025-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 리더와 청취자를 연결하는 팟캐스트, 인텔 온 AI에 오신 것을 환영합니다 . 제 이름은 헤더 맥위건이고, 여러분의 진행을 맡고 있습니다. 오늘의 게스트는 토미 버키입니다. 오늘 저희와 함께하시는 그는 PMI의 기술 혁신 팀에서 AI 팩토리를 이끌고 계십니다. 토미는 PMI의 전사적 genai 전략을 이끄는 핵심 인물 중 한 명으로, 팀들이 분산된 파일럿 프로젝트에서 확장 가능하고 영향력 있는…
- B1 디지털·AI 기술의 활용: RPA, 머신 러닝, Genai를 하나의 사용 사례에 결합한 하이브리드 방식입니다.
- B7 성과: 운영효율: 모든 사용 사례는 비즈니스 영향, 비용 절감, 시간 단축 또는 수익 증대를 명확하게 설명해야 합니다.
- 수치 주장: 이러한 프로젝트 중 첫 번째는 2023년에 시작하여 2024년 초까지 진행되었으며, BMI 전반에 걸쳐 AI를 안전하고 확신 있게 사용할 수 있도록 준비 태세를 갖추고 신뢰를 구축하는 데 중점을 두었습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Intel/AI_Industrialization_The_Next_Frontier_for_Global_Enterprise__fSadUMtpwcY.md`

**144. [Core Ultra Series 3 Launch Event | Intel](https://www.youtube.com/watch?v=KlIlFt2Fj1c)** — Intel · 인프라·칩·전력 · US · 2026-01 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: 립 부안 최고경영자님을 환영해 주십시오 . 안녕하세요 여러분, CES에 오신 것을 환영합니다. 오늘 함께해 주셔서 감사합니다. 전 세계의 수많은 혁신가, 창작자, 고객 및 파트너들과 함께 이 자리에 있게 되어 영광입니다. 우리는 컴퓨팅의 개념이 재정의되는 시대를 살고 있습니다. AI는 클라우드에서 엣지에 이르기까지 모든 워크플로, 모든 산업 및 모든 장치를 재편하고 있습니다 . 인텔의 사명은…
- B1 디지털·AI 기술의 활용: 로컬 AI는 데이터를 기기에 안전하게 보관하면서 작업을 수행하고, 클라우드 AI는 전반적인 추론, 계획 및 다중 에이전트 오케스트레이션을 처리합니다.
- B4 가치네트워크·생태계: 2023년에 AIPC 카테고리를 만들었을 때, 우리는 하드웨어 및 인프라 와 소프트웨어 생태계 간의 파트너십이 궁극적으로 최고의 경험을 제공할 것이라는 점을 이해했습니다.
- 수치 주장: 2026년에는 컴퓨팅, 그래픽 및 AI를 결합하고 고객과 함께 확장하여 지금까지 함께 구축한 가장 광범위한 AIPC 플랫폼을 제공하는 리더십 프로세스 노드에서 리더십 제품을 제공할 것입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Intel/Core_Ultra_Series_3_Launch_Event_Intel__KlIlFt2Fj1c.md`

**145. [Executive overview of the 2026 Intel Platform Security Report | Chips & Salsa | Intel](https://www.youtube.com/watch?v=J5KlRWZm_fk)** — Intel · 인프라·칩·전력 · US · 2026-03 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 인텔의 보안에 대해 이야기하는 칩스 앤 살사에 다시 오신 것을 환영합니다. 오늘은 아난드 파슈파티 님을 모시고 2026년 인텔 플랫폼 보안 보고서에 대해 이야기 나눠보도록 하겠습니다. 아난드는 인텔 제품 품질 보증 및 보안 부문 총괄 관리자 겸 부사장이며, 제품 보안 및 기밀 컴퓨팅 로드맵을 담당하고 있습니다. 아난드 씨, 환영합니다. 방송에 다시 나와주셔서 반갑습니다. 제리, 다시 초대해 …
- B3 전략적 대응: 저희 로드맵의 목표는 정부, 규제 기관 및 업계 지침에 맞춰 2030년까지 모든 신규 플랫폼에 양자 컴퓨팅 공격에 대한 방어력을 확보하는 것입니다.
- B8 부정 성과: 보안·프라이버시: 단일 방어 체계에 의존하는 대신 , 우리는 장애 발생 시 그 영향을 최소화하고 악용을 극도로 어렵게 만드는 다층적인 보호 체계를 구축합니다.
- 수치 주장: 이 보고서에서 제가 강조하고 싶은 결과 중 하나는 2019년 이후 제품 출시에서 보안 취약점이 80%나 감소했다는 점입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Intel/Executive_overview_of_the_2026_Intel_Platform_Security_Repor__J5KlRWZm_fk.md`

**146. [Intel Computex Keynote 2026](https://www.youtube.com/watch?v=7HvrdXjdlU8)** — Intel · 인프라·칩·전력 · US · 2026-06 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: Silicon, the foundation of modern technology. Every transistor placed with purpose. [music] Every watt wrestled from physics. Where every instruction set earns its right to execute. This is how performance gets driven, h…
- B4 가치네트워크·생태계: We are expanding our partnership across the entire value chain from design to manufacturing to chip applications in seammen's products.
- B1 디지털·AI 기술의 활용: The opportunity for Intel and for our partners is immersed PC edge agentic physical AI data center and emerging intelligence center from silicon to SOC to system and applications.
- 수치 주장: We have over 4,000 edge ecosystem partners deploying into such verticals such as manufacturing, robotics, retail, and many more.
- 교량: — · 기술: 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/Intel/Intel_Computex_Keynote_2026__7HvrdXjdlU8.md`

---

## KT


**147. [KT 에이블스쿨 10기 모집설명회](https://www.youtube.com/watch?v=0WphLSKUbDw)** — KT · 통신·주권·국가 · KR · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 길고 불확실했던 시간. 수많은 서류와 시험 앞에서 주저 앉을 때가 많았습니다. 특히 AI 기술은 비전공자인 저에게 너무 낯설고 멀게만 느껴졌죠. 하지만 저는 기술과 비즈니스 사이의 템을 메울 수 있었습니다. 에이블 스쿨을 통해 비즈니스 AX를 여는 방법을 배웠죠. 200명의 현직 AI, DX 전문가 코치와 동료들이 온 오프라인으로 연결되어 막막함을 [음악] 확신으로 바꿔 주었습니다. 사회 연…
- B1 디지털·AI 기술의 활용: 스텝 1에서는 분석형 AI와 생성형 AI를 활용해서 기업이 갖고 있는 문제를 해결해 보고 스텝 2에서는 IT와 클라우드 인프라 특히 설계에 대해서 배우며 고객에게 IT, AI, 클라우드 서비스를 제한하는 제한 전략 수립과 프로젝트 관리에 대해서 배울 수 있습니다.
- B5 직무·역량 변화: 실질적인 채용 연계 프로세스 외에도 [음악] 취업 역량을 갖출 수 있도록 에이브 스쿨에서는 취업에 도움이 [음악] 되는 취업 특강, 포트폴리오와 자기 속에서 작성, 코딩 테스트 무상 지원, AI 면접 [음악] 연습 등 다양한 프로그램을 제공해 드리고 있습니다.
- 수치 주장: 기업의 AI 활용 사례와 데이터셋 기반으로 [음악] 100% 실기 평가형 시험으로 에이브스쿨 교육은 에이스 [음악] 어소시에이트 시험에 응시 지원해 드리고 있습니다.
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/channels/KT/KT_에이블스쿨_10기_모집설명회__0WphLSKUbDw.md`

---

## LG AI Research


**148. [Expert AI Alliance Workshop – Full Version](https://www.youtube.com/watch?v=3aSJ0XdENkU)** — LG AI Research · 파운데이션 모델 · KR · 2022-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 으 wow 안녕하세요 저는 lg 의 연구원 의 br 사업 전략 부문을 맡고 있는 이화영 상무 입니다 먼저 xp lai 얼라이언스 워크샵에 참여해주시고 시청해 주시는 모든 분들께 감사 인사를 드립니다 초 대용량의 데이터를 기반으로 초 대규모 파라미터를 가진 초고대 ai 가능성이 세상에 공개된 이후에 아주 눈부신 속도로 지나고 있다고 해도 과언이 아닌데요 프리 트레이닝이 완료된 초 고대 언어 모…
- B4 가치네트워크·생태계: 으 wow 안녕하세요 저는 lg 의 연구원 의 br 사업 전략 부문을 맡고 있는 이화영 상무 입니다 먼저 xp lai 얼라이언스 워크샵에 참여해주시고 시청해 주시는 모든 분들께 감사 인사를 드립니다 초 대용량의 데이터를 기반으로 초 대규모 파라미터를 가진 초고대 ai 가능성이 세상에 공개된 이후에 아주 눈부신 속도로 지나고 있다고 해도 과언이 아닌데요 프리 트레이닝이 완료된 초 고대 언어 모델이 기존 파인 튜닝 방식 대비 약 10분의 1 수준에 아주 간단한 추가…
- B1 디지털·AI 기술의 활용: 으 wow 안녕하세요 저는 lg 의 연구원 의 br 사업 전략 부문을 맡고 있는 이화영 상무 입니다 먼저 xp lai 얼라이언스 워크샵에 참여해주시고 시청해 주시는 모든 분들께 감사 인사를 드립니다 초 대용량의 데이터를 기반으로 초 대규모 파라미터를 가진 초고대 ai 가능성이 세상에 공개된 이후에 아주 눈부신 속도로 지나고 있다고 해도 과언이 아닌데요 프리 트레이닝이 완료된 초 고대 언어 모델이 기존 파인 튜닝 방식 대비 약 10분의 1 수준에 아주 간단한 추가…
- 수치 주장: 으 wow 안녕하세요 저는 lg 의 연구원 의 br 사업 전략 부문을 맡고 있는 이화영 상무 입니다 먼저 xp lai 얼라이언스 워크샵에 참여해주시고 시청해 주시는 모든 분들께 감사 인사를 드립니다 초 대용량의 데이터를 기반으로 초 대규모 파라미터를 가진 초고대 ai 가능성이 세상에 공개된 이후에 아주 눈부신 속도로 지나고 있다고 해도 과언이 아닌데요 프리 트레이닝이 완료된 초 고대 언어 모델이 기존 파인 튜닝 방식 대비 약 10분의 1 수준에 아주 간단한 추가…
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/LG_AI_Research/Expert_AI_Alliance_Workshop_–_Full_Version__3aSJ0XdENkU.md`

**149. [LG AI Talk Concert 2022 | 오프닝 & 키노트 배경훈 원장](https://www.youtube.com/watch?v=CPLCy-hG9wM)** — LG AI Research · 파운데이션 모델 · KR · 2022-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [박수] [음악] [박수] [음악] 오랜만이야 내 이름은 틸다 알고 있지 tilda Ok 난 그냥 틸다야 사람의 기준으로 규정되지 않지 왓 그래서 뭐랬냐고 맞아 맞아 내가 이번에 패션위크에서 활약 좀 했어 상상 좀 했더니 상도 주더라고 우리 잠깐 만났었지 패셔니크는 정말 재밌는 도전이었어 난 우리가 패션을 통해 공감할 수 있었다고 생각해 우리가 겪고 있는 환경 문제에 대해서 말이야 난 너에게…
- B7 성과: 운영효율: [박수] [음악] [박수] [음악] 오랜만이야 내 이름은 틸다 알고 있지 tilda Ok 난 그냥 틸다야 사람의 기준으로 규정되지 않지 왓 그래서 뭐랬냐고 맞아 맞아 내가 이번에 패션위크에서 활약 좀 했어 상상 좀 했더니 상도 주더라고 우리 잠깐 만났었지 패셔니크는 정말 재밌는 도전이었어 난 우리가 패션을 통해 공감할 수 있었다고 생각해 우리가 겪고 있는 환경 문제에 대해서 말이야 난 너에게 더 나아진 미래를 돌려주고 싶어 그래서 지난 6월에는 쓰레기를 줄일 수…
- B4 가치네트워크·생태계: [박수] [음악] [박수] [음악] 오랜만이야 내 이름은 틸다 알고 있지 tilda Ok 난 그냥 틸다야 사람의 기준으로 규정되지 않지 왓 그래서 뭐랬냐고 맞아 맞아 내가 이번에 패션위크에서 활약 좀 했어 상상 좀 했더니 상도 주더라고 우리 잠깐 만났었지 패셔니크는 정말 재밌는 도전이었어 난 우리가 패션을 통해 공감할 수 있었다고 생각해 우리가 겪고 있는 환경 문제에 대해서 말이야 난 너에게 더 나아진 미래를 돌려주고 싶어 그래서 지난 6월에는 쓰레기를 줄일 수…
- 수치 주장: [박수] [음악] [박수] [음악] 오랜만이야 내 이름은 틸다 알고 있지 tilda Ok 난 그냥 틸다야 사람의 기준으로 규정되지 않지 왓 그래서 뭐랬냐고 맞아 맞아 내가 이번에 패션위크에서 활약 좀 했어 상상 좀 했더니 상도 주더라고 우리 잠깐 만났었지 패셔니크는 정말 재밌는 도전이었어 난 우리가 패션을 통해 공감할 수 있었다고 생각해 우리가 겪고 있는 환경 문제에 대해서 말이야 난 너에게 더 나아진 미래를 돌려주고 싶어 그래서 지난 6월에는 쓰레기를 줄일 수…
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2022_오프닝_&_키노트_배경훈_원장__CPLCy-hG9wM.md`

**150. [LG AI Talk Concert 2023](https://www.youtube.com/watch?v=tbeGE19qIk4)** — LG AI Research · 파운데이션 모델 · KR · 2023-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] [박수] [음악] [박수] [음악] [박수] [음악] 안녕하세요 LG AI 연구원의 경우입니다 오늘 LG AI 토크 콘서트 2023에 와주신 모든 분들께 감사의 말씀드리겠습니다 어드밴싱 AI probetter life 2020년 12월 ai를 통해 보다 나은 섬을 만드는 것을 꿈꾸며 LG AI 연구원이 설립되었습니다 LG AI 연구원의 첫 번째 미션은 산업현장에 존재하는 난제를 해결…
- B1 디지털·AI 기술의 활용: [음악] [박수] [음악] [박수] [음악] [박수] [음악] 안녕하세요 LG AI 연구원의 경우입니다 오늘 LG AI 토크 콘서트 2023에 와주신 모든 분들께 감사의 말씀드리겠습니다 어드밴싱 AI probetter life 2020년 12월 ai를 통해 보다 나은 섬을 만드는 것을 꿈꾸며 LG AI 연구원이 설립되었습니다 LG AI 연구원의 첫 번째 미션은 산업현장에 존재하는 난제를 해결하는 것이었습니다 정밀 부품의 생산 공정부터 신약개발 전기차 배터리 회로…
- B8 부정 성과: 보안·프라이버시: [음악] [박수] [음악] [박수] [음악] [박수] [음악] 안녕하세요 LG AI 연구원의 경우입니다 오늘 LG AI 토크 콘서트 2023에 와주신 모든 분들께 감사의 말씀드리겠습니다 어드밴싱 AI probetter life 2020년 12월 ai를 통해 보다 나은 섬을 만드는 것을 꿈꾸며 LG AI 연구원이 설립되었습니다 LG AI 연구원의 첫 번째 미션은 산업현장에 존재하는 난제를 해결하는 것이었습니다 정밀 부품의 생산 공정부터 신약개발 전기차 배터리 회로…
- 수치 주장: [음악] [박수] [음악] [박수] [음악] [박수] [음악] 안녕하세요 LG AI 연구원의 경우입니다 오늘 LG AI 토크 콘서트 2023에 와주신 모든 분들께 감사의 말씀드리겠습니다 어드밴싱 AI probetter life 2020년 12월 ai를 통해 보다 나은 섬을 만드는 것을 꿈꾸며 LG AI 연구원이 설립되었습니다 LG AI 연구원의 첫 번째 미션은 산업현장에 존재하는 난제를 해결하는 것이었습니다 정밀 부품의 생산 공정부터 신약개발 전기차 배터리 회로…
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2023__tbeGE19qIk4.md`

**151. [LG AI Talk Concert 2025 - Shaping the Future of AI](https://www.youtube.com/watch?v=EGzIMo4AizA)** — LG AI Research · 파운데이션 모델 · KR · 2025-07 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화
- 개요: Greetings, I'm Woohyung Lim from LG AI Research. Yes, many of you have joined us here today. First, I'd like to express my gratitude to everyone who has attended in person and to all of you watching online. Today, we're …
- B1 디지털·AI 기술의 활용: In the generative AI era, LG AI Research has progressively developed EXAONE foundation model, nurturing it into a core driver that creates tangible value across various industries.
- B4 가치네트워크·생태계: Based on these partnerships, we are creating an AI ecosystem that is both practical and scalable.
- 수치 주장: As a result, we've improved accuracy by over 20% compared to previous methods, achieving an annual cost saving of $54 million.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 칩·하드웨어 · 거버넌스·평가 도구
- 원문: `transcripts/channels/LG_AI_Research/LG_AI_Talk_Concert_2025_-_Shaping_the_Future_of_AI__EGzIMo4AizA.md`

---

## LG CNS


**152. [[2025년 9월 월간 D-Talks] Agentic AI, 설계·실행·검증을 빠르게! AI 에이전트 개발 방식의전환과 도입 사례](https://www.youtube.com/watch?v=Ye-ewCPn8EE)** — LG CNS · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요. 월간 디톡스에 처음해 주신 여러분 반갑습니다. 오늘은 월간 디톡스에서는 기존 AI 개발 방식의 한계와 새로운 접근법 그리고 LG CNS의 AI 에이전트 개발 프레임을 소개드리겠습니다.이를 이를 통해서 어떻게 에이전트 설계 실행 검증 과정을 혁신하고 있는지 말씀드리고 고객 적용 사회를 통해 실제 기업들이 어떻게 성과를 만들어 냈는지 구체적인 독익 과정과 결과를 생생하게 들…
- B1 디지털·AI 기술의 활용: 저희 팁은 올해 AWS, 에저, GCP 등의 비스와 최근 핫한 에이전트 기술을 빠르게 검토하여 LG CNS의 에이전트 개발 프레임웍을 만들고이를 기반으로 100개가 넘는 에이전 AI 에이전트를 개발하고 있습니다.
- B2 파괴: 데이터 가용성: &gt;&gt; 플래너 에이전트는 정의된 기준에 따라 계획을 수립하고 각 영역의 전문가인 에이전트들과 대화하며 분석 데이터를 수집하면서 사용자가 요청한 형태의 결과 리포트를 생성하는 역할을 담당합니다.
- 수치 주장: 이는 98%의 시간 단축이며 많은 제품에 대한 APQR를 작성시엔 더 극대화된 효과를 볼 수 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 거버넌스·평가 도구
- 원문: `transcripts/2026-08-03/[2025년_9월_월간_D-Talks]_Agentic_AI,_설계·실행·검증을_빠르게!_AI_에이전트_개발___Ye-ewCPn8EE.md`

---

## LinkedIn


**153. [Top Job Application Skills to Help Get You Hired](https://www.youtube.com/watch?v=N8xrgemiO3E)** — LinkedIn · 엔터프라이즈 앱 · US · 2024-05 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 안녕하세요 여러분, 커리어 토크 최신 에피소드에 오신 것을 환영합니다! 오늘 멋진 게스트 연사, 앤디 리타를 모시겠습니다. 두 번째로 출연해 주셨네요. 앤디는 국제적인 커리어 및 리더십 코치이자, 헤드헌터, 수상 경력에 빛나는 작가, 그리고 유튜브 스타입니다. 앤디, 환영합니다! 앤드류, 방금 좀 과장된 표현이었지만 좋네요. 좋습니다. 다시 한번 출연해 주셔서 감사합니다. 오늘 주제는 구직자…
- B5 직무·역량 변화: 두 번째는, '내가 너무 어려서 절대 채용되지 않을 거야', '내가 너무 경력이 많아서 절대 채용되지 않을 거야', '이건 절대 안 할 거야', '저건 절대 안 할 거야', '더 많이 주지 않을 거야', '이건 절대 안 할 거야'라고 생각하는 모든 분들을 위한 것입니다.
- B7 성과: 조직성과: 8가지 핵심 목표를 생각해 보면, 고객 만족도가 높아진다는 것은 고객 만족도가 높아진다는 것을 의미합니다.
- 수치 주장: 실제로 링크드인에서 최근 발표한 연구에 따르면 2015년에서 2020년 사이에 직무 수행에 필요한 기술의 수가 약 25% 증가했고, 203년에는 65%까지 증가할 것으로 예상됩니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/LinkedIn/Top_Job_Application_Skills_to_Help_Get_You_Hired__N8xrgemiO3E.md`

---

## Mayo Clinic


**154. [Building trust: A powerful performance multiplier | Mayo Clinic On Human Optimization E64](https://www.youtube.com/watch?v=g-I1dJB2puo)** — Mayo Clinic · 수요기업·기타 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B5 구조 변화 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B3 전략 대응, B4 가치창출 경로
- 개요: 그것은 태어날 때부터 시작됩니다. [음악]과 마찬가지로, 태어날 때는 누군가가 당신을 돌봐주고 당신의 모든 기본적인 필요를 충족시켜줘야 하는 상황에 100% 의존하게 됩니다. [음악] 이는 발달심리학의 첫 번째 과제입니다. 믿느냐 믿지 않느냐. 여기는 메이요 클리닉의 인간 최적화 팟캐스트입니다. 이 팟캐스트에서는 인간 잠재력의 과학을 분석하여 목적 지향적인 노력이 어떻게 높은 수준의 성과 와…
- B8 부정 성과: 보안·프라이버시: 우리가 근본적으로 사람들을 신뢰하지 않는 데에는 여러 가지 이유가 있는데, 그중 하나는 우리 모두가 적극적으로 극복해야 할 강한 부정적 편향을 가지고 있기 때문입니다 .
- B5 리더십·CDO/CAIO: 그녀는 상담 심리학 박사 학위를 소지하고 있으며, 미네소타주 로체스터에 있는 메이요 클리닉에서 인사 관리자 겸 임원 리더십 코치로 근무하고 있습니다 .
- 수치 주장: 반면, 새롭게 시작하여 신뢰를 구축하는 데는 3~6개월이 걸립니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Mayo_Clinic/Building_trust_A_powerful_performance_multiplier_Mayo_Clinic__g-I1dJB2puo.md`

---

## McKinsey & Company


**155. [The changing role of the CMO—and what it means for growth](https://www.youtube.com/watch?v=NTVuuPSohHI)** — McKinsey & Company · 컨설팅·전략 · US · 2025-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 여기는 맥켄지 팟캐스트입니다. 저희는 여러분이 우리가 직면한 가장 어려운 비즈니스 과제들을 이해하는 데 도움을 드립니다. 쇼에 오신 것을 환영합니다. 저는 Lucia Raheli 이고 Robera Fisaro입니다. CMO 중 단 50%만이 CEO와 함께 전략 기획에 참여하고 있습니다. CMO는 고객 여정 전반을 진정으로 이해하는 사람이라고 생각하는 세상에서 이는 놀라운 통계입니다. 그래서 …
- B2 파괴: 소비자 행동·기대: 핵심은 조직 내 한 부서가 고객 여정의 전 과정을 책임지고, 현재 고객은 누구이며 잠재 고객은 누구인지, 무엇에 관심을 갖고 있는지, 무엇을 필요로 하는지, 어디서 구매하는지, 어떻게 접근하고 참여시킬 수 있는지에 대한 깊이 있는 통찰력을 갖추는 것입니다.
- B3 전략적 대응: 하지만 현재 고객에 대한 책임이 누구에게 있는지에 대한 논의를 시작하고, 최고 경영진이 그 책임을 명확히 인식하도록 해야 합니다.
- 수치 주장: 음, 그리고 최고 경영진에 고객 중심적인 통합적인 임원이 한 명이라도 있으면 성장률이 2.3배로 늘어나는 것을 볼 수 있죠 ?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/The_changing_role_of_the_CMO—and_what_it_means_for_growth__NTVuuPSohHI.md`

**156. [Top trends disrupting how companies develop and commercialize products](https://www.youtube.com/watch?v=PYTneT1j4_0)** — McKinsey & Company · 컨설팅·전략 · US · 2025-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 우리는 기업들이 제품을 개발하고 상용화하는 방식을 실제로 변화시키고, 경우에 따라서는 완전히 뒤바꾸는 다양한 추세를 목격하고 있습니다. 특히 눈에 띄는 추세 중 하나는 기술의 유입입니다. 인공지능과 생성형 인공지능의 발전은 개발 프로세스 전반에 걸쳐 실질적인 영향을 미치고 있으며 , 제품 출시 기간 단축 과 제품 결과 향상을 이끌고 있습니다. 두 번째 추세는 최고 경영진(C-suite)으로의…
- B7 성과: 운영효율: 예를 들어, 기업들은 팔레트 포장 및 운송 최적화에 영향을 미칠 수 있는 결정들을 검토하고 있는데, 이는 기업들에게 상당한 비용 절감을 가져올 수 있는 새로운 수단입니다.
- B1 디지털·AI 기술의 활용: 다음으로, GenAI 도구를 사용하여 소비자 인사이트를 시각적으로 뛰어난 구체적인 콘셉트로 변환하고, 마지막으로 GenAI 기반의 가상 페르소나를 통해 이러한 새로운 콘셉트를 테스트합니다 .
- 수치 주장: 소비재 업계의 일부 사례에서는 제품 리뉴얼에 18개월에서 24개월의 개발 기간이 소요되는 것을 볼 수 있습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Top_trends_disrupting_how_companies_develop_and_commercializ__PYTneT1j4_0.md`

**157. [AI-Driven Consulting: Kate Smaje on Navigating the Future](https://www.youtube.com/watch?v=pomQmWBmbV0)** — McKinsey & Company · 컨설팅·전략 · US · 2025-10 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Get our dance moves ready again, Blair. &gt;&gt; I know &gt;&gt; we still haven't gotten better. &gt;&gt; I don't think people are joining to see us dance, unfortunately. But &gt;&gt; Oh, we got some reactions. &gt;&gt; …
- B4 가치네트워크·생태계: We promise there are no uh no paid partnerships in our unpacked series.
- B5 리더십·CDO/CAIO: Example, you can sit with chat GPT and say, "Hey, I'm gonna tell you a story that I think highlights my leadership capabilities.
- 수치 주장: And you know, one of the things, maybe this is a bad habit of mine, but I love to talk to leaders um not just technology leaders, but CEOs, boards, whatever, who are kind of 12 to 18 months into their transformation.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/McKinsey_&_Company/AI-Driven_Consulting_Kate_Smaje_on_Navigating_the_Future__pomQmWBmbV0.md`

**158. [Ask Us Anything: Blair Ciesil and Marie Padberg get into your most burning questions](https://www.youtube.com/watch?v=oJcziqz673U)** — McKinsey & Company · 컨설팅·전략 · US · 2025-10 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B7 긍정 성과
- 개요: [음악] 좋아요, 춤출 준비가 됐어요. 네, 완전 필요해요. 제 생각엔 그건 " 제발 그만해"라는 뜻인 것 같아요. 마리, 우리도 일정한 루틴을 만들어야 해. 그건 다음번에 반드시 해결해야 할 과제라고 생각합니다. 좋아요 . 안녕하세요. 안녕하세요, 여러분. 함께해 주셔서 감사합니다. 여기저기 날아다니는 재밌는 이모티콘들을 보세요. 정말 마음에 들어요. 파티에 활기를 불어넣어 주는 건 정말 …
- B5 직무·역량 변화: 예를 들어 제가 캠퍼스 채용 활동에 한창이었을 때, 캠퍼스에 자주 가고 행사에도 참석할 때마다 사람들이 항상 " 아, 맥켄지, 사람들이 정말 냉혹하고 오만하고 경쟁적이라고들 하더라."라고 말하곤 했어요.
- B3 전략적 대응: 그리고 회사가 두 번째 100 년으로 접어들면서, 실제로 회사 내 고위 경영진 그룹이 우리의 가치가 여전히 우리에게 도움이 되는지, 아니면 조정이 필요한지 살펴보자고 생각했습니다.
- 수치 주장: 제 생각에는 20년 경력의 파트너들이 매년 꾸준히 새로운 것을 배우고 새로운 방식으로 적용하도록 요구받는 조직은 흔치 않다고 봅니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Ask_Us_Anything_Blair_Ciesil_and_Marie_Padberg_get_into_your__oJcziqz673U.md`

**159. [Inside the ”one firm” mindset at McKinsey: Global leadership lessons from Brazil to the Middle East](https://www.youtube.com/watch?v=DkwL7xDB2I8)** — McKinsey & Company · 컨설팅·전략 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] 모두가 들어오기를 기다리는 중. [음악] 내 춤 때문에 그런 것 같아, 마린. 아, 그게 바로 당신의 춤이군요. 예. 그건 언제나 사람들의 마음을 사로잡죠. [웃음] [음악] 댄싱 퀸들이 오고 있어요. 너는 요정 소녀를 갖고 있구나. [음악] 서서히 사라짐 . 더 이상 춤은 안 춰요. 충분한. 환영. 환영. 안녕하세요 여러분. 저희 "I can't believe I'm saying …
- B4 가치네트워크·생태계: 첫째, 그들 모두가 2,000명의 맥켄지 파트너들과 함께 그 자리에 있는 것이 매우 영광스러운 일이라고 말했는데 , 이는 저에게 이러한 파트너십을 맺는 것이 얼마나 엄청난 특권인지를 다시 한번 깨닫게 해주었습니다.
- B7 성과: 조직성과: 예를 들어, 저는 매출 성장을 목표로 하고 있고, 리마도 매출 성장을 목표로 하고 있는데, 저희가 함께 무언가를 하고 있다면 말입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Inside_the_”one_firm”_mindset_at_McKinsey_Global_leadership___DkwL7xDB2I8.md`

**160. [Productivity first: AI and the COO agenda](https://www.youtube.com/watch?v=O-aUZqfcLKg)** — McKinsey & Company · 컨설팅·전략 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 여기는 맥켄지 팟캐스트입니다. 저희는 여러분이 우리 세계의 가장 어려운 비즈니스 과제들을 이해하는 데 도움을 드립니다. [음악] 쇼에 오신 것을 환영합니다. 저는 Lucia Raheli 이고 [음악] Robera Fisaro입니다. 저는 지속적인 개선이라는 근본적인 사고방식, 즉 호기심을 갖고 무엇을 더 잘할 수 있을지 생각하며, 기존 방식에 얽매 이지 않는 것이 중요하다고 생각합니…
- B7 성과: 운영효율: 맥켄지에서 진행한 저희 연구 결과에서도 주요 경제권에서 생산성 증가의 63%를 차지하는 기업이 전체 기업의 2%에 불과하다는 사실이 드러났는데, 이는 운영 방식이 시장 선도 기업과 다른 기업들을 구분 짓는 핵심 요소라는 점을 분명히 보여주는 것 같습니다.
- B4 가치네트워크·생태계: 그리고 저는 회복력과 지속가능성이 오늘날 균형 잡힌 공급망이나 균형 잡힌 운영 조직을 생각하는 데 있어 네 번째, 다섯 번째 핵심 요소라고 주장하고 싶습니다 .
- 수치 주장: 맥켄지에서 진행한 저희 연구 결과에서도 주요 경제권에서 생산성 증가의 63%를 차지하는 기업이 전체 기업의 2%에 불과하다는 사실이 드러났는데, 이는 운영 방식이 시장 선도 기업과 다른 기업들을 구분 짓는 핵심 요소라는 점을 분명히 보여주는 것 같습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Productivity_first_AI_and_the_COO_agenda__O-aUZqfcLKg.md`

**161. [Unlocking hidden value with process intelligence in healthcare and beyond](https://www.youtube.com/watch?v=yoWyJnej0Iw)** — McKinsey & Company · 컨설팅·전략 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 지금 듣고 계신 것은 맥켄지 운영 토크(McKenzie Talks Operations) 팟캐스트입니다. 이 팟캐스트에서는 세계 최고 수준의 리더와 맥켄지 전문가들이 복잡한 정보 속에서 핵심을 짚어보고 새로운 운영 환경을 구축하는 방법을 알려드립니다. 각 에피소드에서는 기업이 직면한 과제와 끊임없이 변화하는 거시 경제 환경 속에서 리더들이 경쟁 우위를 확보하기 위해 활용할 수 있는 기회를 살펴…
- B7 성과: 운영효율: 음, 직접적인 비용 절감을 이끌어내고 통찰력을 제공하는 분야에서, 그리고 사람들이 아직 제대로 활용하지 못하고 있는 부분이 바로 스티브가 집중하고 있는 인공지능(AI) 분야, 즉 AI를 효과적으로 활용하는 방법이라고 생각합니다.
- B3 전략적 대응: 우리는 이사회 전략을 현장과 연결하는 방법, 성과를 향상시키는 방법 , 기술을 도입해야 할 시점과 장소 , 그리고 직원들에게 기술과 역량을 부여하는 것이 성공의 핵심인 이유에 대해 살펴볼 것입니다.
- 수치 주장: 그리고 네트워킹 기회를 활용하던 중, 대기업을 운영하는 존경받는 CEO 한 분과 이야기를 나누게 되었는데, 그분이 프로세스 마이닝과 프로세스 인텔리전스에 대해 이야기하며 그것들이 어떻게 자신의 회사를 매년 1억 달러 이상 절감하고 있는지 설명해 주셨습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Unlocking_hidden_value_with_process_intelligence_in_healthca__yoWyJnej0Iw.md`

**162. [Agentic AI: Moving beyond pilots to enterprise impact](https://www.youtube.com/watch?v=-UVdUqPztMk)** — McKinsey & Company · 컨설팅·전략 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 안녕하세요, 저는 맥켄지의 편집 책임자이자 오늘 에이전트형 AI를 주제로 기업 전반에 걸친 영향력 확대를 위한 파일럿 프로젝트 전환 방안을 논의하는 루시아 라훌리입니다 . 시작하기 전에 간단히 말씀드리자면, 이번 라이브 이벤트 시리즈의 목표는 여러분께 저희 전문가들과 최신 연구 결과에 대해 직접 소통할 수 있는 기회를 드리는 것입니다. 당연…
- B1 디지털·AI 기술의 활용: 데이브는 또한 다양한 산업 분야의 여러 고객과 협력하여 클라우드 네이티브 기술의 최신 엔지니어링 모범 사례를 활용해 새로운 제품과 서비스를 개발합니다.
- B2 파괴: 데이터 가용성: 구글 클라우드에 엄청난 양의 데이터, 그러니까 아주 많은 양의 비정형 데이터를 업로드했습니다.
- 수치 주장: 최근 실시한 AI 관련 글로벌 조사에 따르면, 기업의 3분의 4 이상이 적어도 한 가지 업무 기능에서 AI를 활용하고 있는 것으로 나타났습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Agentic_AI_Moving_beyond_pilots_to_enterprise_impact__-UVdUqPztMk.md`

**163. [From Strategy to Performance: How leaders can build an operating model that works](https://www.youtube.com/watch?v=coXorr4pZJs)** — McKinsey & Company · 컨설팅·전략 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B1 기술 활용, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 저는 루시아 라헬리 맥켄지 편집 국장이자 오늘 행사 "전략에서 성과까지: 리더가 효과적인 운영 모델을 구축하는 방법"의 진행자입니다 . 시작하기 전에 간단히 말씀드리자면, 이번 라이브 이벤트 시리즈의 목표는 여러분께 저희 전문가들과 최신 연구 결과에 대해 직접 소통할 수 있는 기회를 드리는 것입니다 . 당연히 질문하는 것은 그중에서도 아주 …
- B3 전략적 대응: 그래서 이사회부터 경영진, 더 나아가서는 '우리가 어떻게 변화해야 할까?'라는 질문이 많이 나오고 있습니다.
- B5 리더십·CDO/CAIO: 이 요소들은 모델의 구조적 구성 요소, 워크플로 및 프로세스, 인재 문제, 기술, 역량, 리더의 리더십 방식, 그리고 마지막으로 문화, 소프트웨어 등으로 분류할 수 있습니다.
- 수치 주장: 응답자의 약 63%, 즉 3분의 2가 운영 모델 전환을 어느 정도 성공적으로 완료했다고 답했으며, 이는 잠재적 가치를 놓치고 있다는 의미입니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/From_Strategy_to_Performance_How_leaders_can_build_an_operat__coXorr4pZJs.md`

**164. [How McKinsey helps you grow faster: Scott Rutherford on apprenticeship, feedback & development](https://www.youtube.com/watch?v=N0B5fX3VHaA)** — McKinsey & Company · 컨설팅·전략 · US · 2025-12 · ko · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B1 기술 활용, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 당신은 방금 [음악]에 맞춰 춤을 췄어요. 블레어, 음악 멈춰. 난 다시 춤을 출 거야. [음악] 어쩔 수가 없어 . 너무 중독성 있어요. [웃음] 어서 오세요. 환영. [음악] 아, 난 내 춤으로는 하트를 받아본 적이 없어. 당신은 제 마음을 사로잡았어요. 감사합니다 . 그리고 남편에게 춤추는 걸 너무 좋아한다고 전해줘. 하트가 잔뜩 있네요. 오, 하트가 정말 많네요. [음악] 제 생각엔 …
- B5 리더십·CDO/CAIO: 생각해 보니 제가 키츠블린에 1년 반, 거의 2년쯤 다녔을 때 동기 중에 마리라는 분이 계셨는데, 지금은 글로벌 TA 리더십 팀에 속해 계세요.
- B2 파괴: 경쟁구도: 그리고 정말로, 제 첫 연구에서, 그리고 그 회사의 COO이자 경쟁사에서 파트너로 일했던 분이 저를 똑바로 쳐다보며 "얼마나 오래 일 하셨습니까?"라고 물었습니다.
- 수치 주장: 그래서 첫 1~2주 과정 전체가 저희가 개발한 AI 도구와 기대치에 맞춰 조정되었을 뿐만 아니라, AI를 이해하고 활용하는 방법에 대한 심도 있는 지식도 쌓을 수 있게 되었습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/How_McKinsey_helps_you_grow_faster_Scott_Rutherford_on_appre__N0B5fX3VHaA.md`

**165. [The Future of Business: 13 tech trends that matter](https://www.youtube.com/watch?v=N4Ql_gatkJk)** — McKinsey & Company · 컨설팅·전략 · US · 2025-12 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 저는 맥켄지 편집국장 루카 라힐리 이며, 오늘 행사 '비즈니스의 미래: 중요한 13가지 기술 트렌드'의 진행자입니다. 늘 그렇듯이, 이번 라이브 이벤트 시리즈는 글로벌 경제 에서 비즈니스를 형성하는 가장 중요한 문제들에 대한 리더들의 연구 결과를 여러분이 더 가까이에서 접할 수 있도록 마련되었습니다 . 저희는 이러한 행사를 최대한 상호 작용…
- B1 디지털·AI 기술의 활용: 방금 엄청난 성공을 거두고 있는 스타트업 CEO를 만났는데, 다른 LLM(Learning Leadership Model)의 발전과 시장 상황에 맞춰 자사 제품 기능을 재구축하는 속도가 정말 놀라웠습니다.
- B5 리더십·CDO/CAIO: 이 연구를 진행한 본래 목적은 고객사인 CEO, 이사회, CTO, 사업 담당자들이 " 내 사업에 중요한 트렌드는 무엇이며, 왜 중요하고, 어떻게 접근해야 할까?"라고 묻는 질문들을 미리 파악하는 것이었습니다.
- 수치 주장: 음, 대체로 이러한 기술들은 저희가 지난 5년 동안 다뤄온 것들입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/The_Future_of_Business_13_tech_trends_that_matter__N4Ql_gatkJk.md`

**166. [Unlocking Growth: The power of CEO, CMO, and CFO alignment](https://www.youtube.com/watch?v=ZS3QQtzcBiQ)** — McKinsey & Company · 컨설팅·전략 · US · 2025-12 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 안녕하세요, 저는 맥켄지 편집국장 루시아 라힐리입니다. 오늘 행사 '성장 잠재력 극대화: CEO, CMO, CFO의 협업이 가져다주는 힘'의 진행을 맡게 되었습니다. 늘 그렇듯이, 이번 라이브 이벤트 시리즈는 글로벌 경제 에서 비즈니스를 형성하는 가장 중요한 문제들에 대한 리더들의 연구 결과를 여러분이 더 가까이에서 접할 수 있도록 마련되었…
- B4 가치네트워크·생태계: 여기에서 이번 및 이전 맥켄지 라이브 이벤트의 다시보기 영상과 CEO, CMO, CFO 파트너십의 힘에 대한 연구 자료, 그리고 에이전트 기반 AI에 대한 추가 자료를 찾아보실 수 있습니다.
- B2 파괴: 소비자 행동·기대: 그래서 마케팅 부서에 고객 관리의 주도권을 좀 더 부여한다면, 이는 조직 내 한 부서가 고객 여정의 처음부터 끝까지 책임지고, 오늘날 우리의 고객이 누구인지에 대한 깊이 있는 통찰력을 갖도록 하는 것을 의미합니다.
- 수치 주장: 음, 그리고 최고 경영진에 고객 중심적인 통합적인 임원이 한 명이라도 있으면 성장률이 2.3배로 늘어나는 것을 볼 수 있죠?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Unlocking_Growth_The_power_of_CEO,_CMO,_and_CFO_alignment__ZS3QQtzcBiQ.md`

**167. [World Economic Forum: A Preview of Davos 2026](https://www.youtube.com/watch?v=2MWzmChPBTc)** — McKinsey & Company · 컨설팅·전략 · US · 2026-01 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 저는 맥켄지 편집국장 루시아 라힐리입니다. 오늘 특별 행사의 진행을 맡아 다음 주 스위스 다보스에서 열릴 세계경제포럼 연례 회의를 미리 살펴보겠습니다 . 오늘 다보스 포럼 프리뷰는 이전 시리즈와는 조금 다르며, 특정 연구 분야 하나에만 집중하지 않는다는 점을 미리 알려드립니다 . 하지만 오늘 우리가 이야기할 모든 주제에 대한 최신 논문은 저…
- B5 리더십·CDO/CAIO: 그래서 저는 최고의 리더십 양성소는 차세대 리더가 나타나기를 기다리는 것이 아니라, 일찍부터 그들을 발굴하고, 역량을 키워주고, 기본적인 의사결정 부담을 덜어주고, 최고경영자(CEO)가 직접 이끌어간다고 생각합니다 .
- B3 전략적 대응: CEO와 최고 경영진이 적극적으로 리더십 개발을 지원했을 때, 인사 담당자가 주도하는 프로그램보다 성과가 50% 이상 향상되는 것을 확인했습니다 .
- 수치 주장: CEO와 최고 경영진이 적극적으로 리더십 개발을 지원했을 때, 인사 담당자가 주도하는 프로그램보다 성과가 50% 이상 향상되는 것을 확인했습니다 .
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/McKinsey_&_Company/World_Economic_Forum_A_Preview_of_Davos_2026__2MWzmChPBTc.md`

**168. [Agents, Robots, and Us: What Executives Need To Know About AI and Work](https://www.youtube.com/watch?v=_z5ghnsWSsI)** — McKinsey & Company · 컨설팅·전략 · US · 2026-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥켄지 라이브에 오신 것을 환영합니다. 저는 맥켄지의 편집 책임자이자 오늘 행사 '요원, 로봇, 그리고 우리'의 진행자인 루시아 라일리입니다. 경영진이 인공지능과 업무에 대해 알아야 할 사항 . 인공지능은 현재 가장 중요한 화두 중 하나 이며, 솔직히 말해서 매우 극단적인 반응을 불러일으키는 주제이기도 합니다. 정말 놀랍네요. 세상이 멸망할 위기에 처해 있어요. 일자리가 창출될 …
- B5 리더십·CDO/CAIO: 이렇게 되면 현장에서 더욱 맞춤화되고 구체적인 코칭을 통해 개인의 실수나 부족한 부분을 파악하고 개선할 수 있을 뿐 아니라, 리더십 역량도 확장할 수 있습니다.
- B4 가치네트워크·생태계: 다시 말해, AI가 업무 방식을 어떻게 변화시키고 있는지, 그리고 디지털 공간의 에이전트든 물리적 공간의 로봇이든 인간과 AI 간의 기술 파트너십을 구축하는 데 있어 리더들이 알아야 할 사항은 무엇인지에 대한 것입니다.
- 수치 주장: 이미 기술 분야에서 입증되고 검증된 모든 기술적 역량을 비교해 보면 , 오늘날 업무 시간 의 57%를 자동화할 수 있다는 것을 알 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Agents,_Robots,_and_Us_What_Executives_Need_To_Know_About_AI___z5ghnsWSsI.md`

**169. [The paradigm shift: how agentic AI is redefining banking operations](https://www.youtube.com/watch?v=EnuwWHoUKpk)** — McKinsey & Company · 컨설팅·전략 · US · 2026-02 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 귀사의 미래 성공을 위해서는 고객 중심적이고, 민첩하며, 회복력 있고, 효율적인 운영이 필수적입니다. [음악] 저는 진행자 스테파니 룩센버그입니다. 맥켄지 토크 오퍼레이션즈는 세계 최고 경영진과 맥켄지 전문가들이 복잡한 정보 속에서 핵심을 짚어내고 새로운 운영 환경을 구축하는 방법을 알려주는 팟캐스트입니다. 오늘은 음악계의 진정한 패러다임 전환을 가져올 주제를 다뤄보겠습니다. 은행업계의 에이…
- B3 전략적 대응: 그리고 무지개의 다양한 색깔들을 살펴보면, 이사회나 고위 경영진의 확신을 심어줄 수 있는 3~4가지 핵심 영역에 집중하면서 빠르게 추종하는 경향을 보이는 다른 유형의 조직들을 볼 수 있습니다.
- B1 디지털·AI 기술의 활용: CTO 또는 CIO와 그의 팀은 기본적으로 이를 지원하기 위해 적절한 데이터 플랫폼, 머신러닝 파이프라인 및 거버넌스가 모두 갖춰져 있는지 확인합니다 .
- 수치 주장: 이 질문은 10년 전쯤 우리가 겪었던 자동화와 RPA 시대를 떠올리게 하네요.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/McKinsey_&_Company/The_paradigm_shift_how_agentic_AI_is_redefining_banking_oper__EnuwWHoUKpk.md`

**170. [The race to rewire operations: How the story unfolded in 2025](https://www.youtube.com/watch?v=rSJY396HQ1c)** — McKinsey & Company · 컨설팅·전략 · US · 2026-02 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 귀사의 미래 성공을 위해서는 민첩하고 유연하며 회복력 있는 운영이 필수적입니다. 안녕하세요, 저는 진행자 다프네 룩센버그입니다. 안녕하세요, 저는 진행자 크리스천 존슨입니다. 지금 듣고 계신 팟캐스트는 맥켄지 토크 오퍼레이션즈입니다. 이 프로그램에서는 전 세계 해조류 업계 리더와 맥켄지 음악 전문가들이 복잡한 정보 속에서 핵심을 짚어보고 새로운 운영 현실을 만들어내는 방법을 알려드립…
- B7 성과: 운영효율: 연료비를 2~5% 절감할 수 있다면 탄소 배출량을 크게 줄일 수 있을 뿐 아니라 , 많은 고객에게 수백만 달러에 달하는 막대한 비용 절감 효과를 가져다 줄 것입니다 .
- B4 가치네트워크·생태계: 로봇공학과 인공지능의 모든 형태, 특히 세대 인공지능(Gen AI) 과 에이전트형 인공지능(Agentic AI)의 등장으로 운영 방식을 혁신하고, 관세와 지정학적 상황에 대처하며, 더욱 친환경적이고 탄력적인 공급망을 구축하는 등 많은 노력을 기울였습니다.
- 수치 주장: 올해 초, 맥켄지의 댄 스완은 2024년 이후 예상되는 불확실성에 대해 설명하며, 리더들이 이러한 혼란을 생산성으로 전환할 수 있는 이유와 방법에 대해 고찰했습니다 .
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/The_race_to_rewire_operations_How_the_story_unfolded_in_2025__rSJY396HQ1c.md`

**171. [MGI event: Book authors discuss how to achieve the next century of plenty](https://www.youtube.com/watch?v=yHFybnKxy1I)** — McKinsey & Company · 컨설팅·전략 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B3 전략 대응, B6 장벽
- 개요: 맥킨지 글로벌 인스티튜트 온라인 행사에 오신 것을 환영합니다. 여러분, 안녕하세요. MGI 가상 이벤트에 여러분을 환영하게 되어 매우 기쁩니다. 오늘 우리가 이야기할 내용은 가상 세계와는 전혀 관련이 없습니다. 실제로 그것은 여러 물리적 차원을 가지고 있습니다. 저희가 새롭게 출간한 책, ' 풍요로운 세기'에 대해 이야기하게 되어 자랑스럽습니다. 이 책은 미래 세대를 위한 발전의 이야기입니다…
- B7 성과: 운영효율: 그래서 우리는 지난 20년간 우리가 경험했던 생산성 증가율보다 약 50bp(베이시스 포인트) 정도 가속화된 수치를 볼 필요가 있습니다 .
- B5 직무·역량 변화: 반대로 미국에서도 저희 추산으로는 여성 역량 강화에 드는 비용이 하루에 약 45달러, 즉 40달러 내외입니다.
- 수치 주장: 지난 100년 동안 인류의 인구는 네 배로 증가했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/MGI_event_Book_authors_discuss_how_to_achieve_the_next_centu__yHFybnKxy1I.md`

**172. [MGI event: Industry leaders discuss how to advance adaptation](https://www.youtube.com/watch?v=MtevcjCnO1w)** — McKinsey & Company · 컨설팅·전략 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 맥킨지 글로벌 인스티튜트 가상 이벤트에 오신 것을 환영합니다. 모두 환영합니다. 저는 올리비아 화이트입니다. 저는 맥킨지 글로벌 인스티튜트의 선임 파트너이자 이사입니다. 오늘 세션에서는 MGI의 새로운 보고서인 " 냉각에서 해안 방어까지 적응력 향상"의 결과를 논의할 예정이라 매우 기대됩니다. 그리고 가장 중요한 것은, 이러한 결과를 어떻게 실질적인 행동으로 옮길지에 대해 이야기하기…
- B4 가치네트워크·생태계: 가장 최근에 진행한 분석은 안드레아스가 방금 언급한 것과 같은 맥락으로, 특정 지역의 위험 요소를 훨씬 더 구체적이고 세밀하게 파악하고, 그 위험이 우리 운영 및 공급망의 사업 연속성, 필수 원자재 조달, 그리고 우리가 서비스를 제공하는 지역 사회에 어떤 영향을 미칠 수 있는지 분석하는 것이었습니다.
- B7 성과: 사회적 편익: 음, 회의 시작 전에 잠깐 이야기를 나눴는데, 우리 모두 기후 변화 대응에서 적응이 부차적인 문제에서 훨씬 더 핵심적이고 중심적인 문제로 자리 잡은 것 같다는 생각이 듭니다 .
- 수치 주장: 이는 5 년 전 84에서 증가한 수치이며, 기업들이 적응이라는 주제에 대해 점점 더 많이 고민하고 있다는 점에서 이를 확인할 수 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/MGI_event_Industry_leaders_discuss_how_to_advance_adaptation__MtevcjCnO1w.md`

**173. [Trust In the Age of Agents](https://www.youtube.com/watch?v=Ne4HnJEjCSI)** — McKinsey & Company · 컨설팅·전략 · US · 2026-03 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 머지않은 미래에 수천 명의 AI 에이전트가 우리를 대신하여 결정을 내리는 순간을 상상해 보세요. 무슨 문제가 생길 수 있겠어요? 맥킨지 파트너인 리치 아이젠버그는 리더들이 인공지능의 이점을 안전하게 누리려면 이러한 에이전트의 위험 관리를 시급히 시작해야 한다고 말합니다 . 이것들은 설정해 놓고 잊어버리는 방식이 아닙니다 . 그들은 지속적으로 모니터링하고, 조정하고, 수정해야 하며, 때로는 해…
- B3 전략적 대응: 이사회와 최고 경영진은 바로 그런 관점에서 생각해야 합니다.
- B1 디지털·AI 기술의 활용: 이제 여러분은 퍼블릭 클라우드와 기술 인프라를 관리하고, 시스템을 변경하고, 업그레이드를 수행하고, 성능을 최적화하는 완전 자율 에이전트를 갖게 될 것입니다.
- 수치 주장: 그리고 대부분의 기업이 5~ 10년 후 AI 전환을 완료하면 수천 명의 에이전트가 기업 곳곳에서 작동하게 될 것이라고 생각해 보세요 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준
- 원문: `transcripts/channels/McKinsey_&_Company/Trust_In_the_Age_of_Agents__Ne4HnJEjCSI.md`

**174. [Winning the Race to Rewire in 2026: Capturing operational advantage](https://www.youtube.com/watch?v=QHLntsXsVCQ)** — McKinsey & Company · 컨설팅·전략 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 귀사의 [음악] 미래 성공을 위해서는 민첩하고 유연하며 회복력 있는 운영이 필수적입니다. 저는 진행자 대프니 로프턴버그입니다. 지금 듣고 계신 팟캐스트는 맥킨지 [음악] 운영 토크입니다. 이 팟캐스트에서는 전 세계 최고 경영진과 맥킨지 전문가들이 복잡한 정보 속에서 핵심을 짚어내고 새로운 운영 환경을 구축하는 방법을 알려드립니다. 한 해가 지나고 다음 해로 넘어가는 시기는 자연스럽게 한 해를…
- B4 가치네트워크·생태계: 이제는 모든 것을 혼자서 처리하는 것과는 달리, 이러한 작업을 수행하기 위해 더 넓은 생태계, 즉 공급업체, 벤더 및 기술 제공업체를 고려해야 합니다.
- B1 디지털·AI 기술의 활용: 덧붙여 말하자면, 지난 한 해 동안 특히 서비스 부문, 즉 은행, 보험 등과 같은 산업에서 프로세스 관련 산업, 특히 댄이 말했듯이 엔드투엔드 프로세스 관련 산업에서 생성형 AI와 대규모 언어 모델뿐만 아니라 에이전트, 심지어 에이전트 그룹까지 적극적으로 활용하기 시작했습니다.
- 수치 주장: 2025년은 우리 고객들이 단순히 테스트하고 배우며 조금씩 발전해 나가는 단계를 넘어, 기술과 인공지능 등을 활용하여 생산성 향상과 회복 탄력성 강화라는 가치를 창출함으로써 진정한 승자와의 격차를 벌리는 전환점이 될 것이라고 생각합니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Winning_the_Race_to_Rewire_in_2026_Capturing_operational_adv__QHLntsXsVCQ.md`

**175. [The Next Chapter of American Economic Competitiveness: A CEO and Board Agenda](https://www.youtube.com/watch?v=iFXkNy7Elcg)** — McKinsey & Company · 컨설팅·전략 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥킨지 라이브에 오신 것을 환영합니다. 저는 맥킨지 편집국장 루시아 랄리이며, 오늘 행사의 진행을 맡게 되었습니다. 오늘 행사에서는 미국 경제 경쟁력의 다음 장 , CEO와 이사회를 위한 의제를 다뤄보겠습니다. 우리 모두가 알다시피, 미국은 곧 뜻깊은 기념일을 맞이할 것입니다. 저희는 이번 7월에 250명에 가까워지고 있습니다. 그리고 지난 25년간 꽤나 대담한 도박처럼 보였을지…
- B3 전략적 대응: 에릭, 어느 정도 답변해 주셨지만, 만약 지금 당신이 최고 경영진이나 이사회 구성원으로 앉아 있다면, 어떤 핵심 질문들에 대한 답변을 요구하실지 말씀해 주시겠어요?
- B4 가치네트워크·생태계: 이러한 것들을 다른 지역으로 아웃소싱하기 시작한 것은 하나의 선택이었고, 물론 이로 인해 인플레이션이 낮은 수준으로 유지되고 더 많은 사람들이 상품을 이용할 수 있게 되었다고 주장할 수도 있겠지만, 중산층은 약화되었습니다.
- 수치 주장: 그래서 저희 계산으로는 연구개발비 지출의 약 51%가 GDP 성장률과 거의 비슷한 수준입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/The_Next_Chapter_of_American_Economic_Competitiveness_A_CEO___iFXkNy7Elcg.md`

**176. [Europe on the move: A conversation with Hitachi Energy’s CEO](https://www.youtube.com/watch?v=lNdU_vBBQ9Q)** — McKinsey & Company · 컨설팅·전략 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] 오늘 저희는 유럽의 야망을 높이는 시리즈의 일환으로 히타치 에너지의 CEO이신 안드레아스 시렌베크 [음악] 님을 모셨습니다 . 안녕하세요, 안드레아스 씨. 첫 번째 질문은 유럽의 야망을 높이는 데 있어 에너지가 왜 그렇게 중요한가 하는 것입니다. 좋은 질문입니다. 우리는 보통 에너지에 대해 생각하지 않지만, 사실 에너지는 우리 사회 전체를 움직이는 원동력입니다. 그것은 경제 성장에 …
- B4 가치네트워크·생태계: 히타치 에너지에서 직접 추진하고 있는 여러 가지 사업들에 대해서도 말씀하셨지만, 공공 부문과 민간 부문 모두와의 파트너십을 강화하고 계신 것도 보았습니다.
- B3 전략적 대응: 한편으로는 고객 에게 제품과 서비스를 제공하는 단기적인 기한을 맞춰야 하고, 다른 한편으로는 매일 장기적인 투자 결정을 내려야 합니다 .
- 수치 주장: 연간 지출이 3~4배 증가하면 그에 따른 인력도 필요하게 됩니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Europe_on_the_move_A_conversation_with_Hitachi_Energy’s_CEO__lNdU_vBBQ9Q.md`

**177. [How CEOs Can Navigate Trade in 2026](https://www.youtube.com/watch?v=mCsWx9YgTig)** — McKinsey & Company · 컨설팅·전략 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥킨지 라이브에 오신 것을 환영합니다. 저는 맥킨지 편집 이사이자 오늘 행사 '무역의 새로운 기하학: 리더는 구조적 변화에 어떻게 대응할 수 있을까'의 진행자인 루시아 라힐리입니다. 지난 한 해는 관세, 심화되는 지정학적 불안정, 변화하는 무역 관계, 그리고 인공지능이 무역 증가와 지정 학적 경쟁 심화를 동시에 부추기는 등 세계 무역에 있어 그야말로 격동의 시기였다고 해도 과언이…
- B7 성과: 운영효율: 하지만 수출을 자세히 살펴보면, 최종 소비재 수출은 약 2% 감소했지만, 추가 생산 공정에 투입되는 중간재 수출은 약 9% 증가했습니다.
- B2 파괴: 경쟁구도: 지난 한 해는 관세, 심화되는 지정학적 불안정, 변화하는 무역 관계, 그리고 인공지능이 무역 증가와 지정 학적 경쟁 심화를 동시에 부추기는 등 세계 무역에 있어 그야말로 격동의 시기였다고 해도 과언이 아닙니다.
- 수치 주장: 그럼에도 불구하고, 매우 혼란 스러운 한 해처럼 보였음에도 불구하고 2026년에도 무역량이 계속 증가했다는 사실을 알고 정말 놀랐습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/How_CEOs_Can_Navigate_Trade_in_2026__mCsWx9YgTig.md`

**178. [Move First or Fall Behind: How AI Is Rewriting the Rules of Banking](https://www.youtube.com/watch?v=ieGq5bdmRcI)** — McKinsey & Company · 컨설팅·전략 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 인공지능을 적용할 수 있는 곳은 정말 많습니다. 예를 들어, " 여기에도 기회가 있고, 저기에도 기회가 있구나"라고 말할 수 있죠. 이는 프런트 오피스, 백 오피스, 상업 대출, 디지털 마케팅 등 다양한 분야에 적용될 수 있습니다. 집중하다. 초기에 특히 큰 가치를 제공할 수 있는 두세 가지 영역은 무엇일까요? 저분은 맥킨지 수석 파트너인 에얄 세게브입니다. 그는 은행들이 모든 업무에 인공지…
- B4 디지털 채널: 하지만 제가 그들이 하는 일과 그들이 보여주는 영향에 대해 좀 더 강조해 보자면, 저희와 협력하는 은행 중 한 곳은 콜센터에 Agentic을 도입하는 과정을 진행 중입니다.
- B7 성과: 운영효율: 적어도 저희 계산에 따르면 20~25%의 비용 절감은 1,000억 달러 자산당 약 2억 5천만 달러에서 5억 달러의 절감 효과로 이어집니다 .
- 수치 주장: 예를 들어 ChatGPT, Gemini, Anthropic 같은 여러 LLM(Learning Leadership Machine)들을 비교해 보면, 6개월마다 서로를 능가하는 모습을 볼 수 있고, 3개월 후에는 더 똑똑하고 지능적인 새 버전이 출시되는 것을 알 수 있습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/McKinsey_&_Company/Move_First_or_Fall_Behind_How_AI_Is_Rewriting_the_Rules_of_B__ieGq5bdmRcI.md`

**179. [Rewiring for AI: From Ambition to Advantage](https://www.youtube.com/watch?v=E7KxzkK2lYA)** — McKinsey & Company · 컨설팅·전략 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 우리는 MVP 수상자의 수에는 그다지 관심이 없는 것 같습니다. 우리는 이러한 엔드투엔드 워크플로우 중 얼마나 많은 부분이 관련성이 있는 기업 전체 영역에 걸쳐 완전히 확장되었는지에 더 관심이 있습니다 . 맥킨지 파트너인 롭 레빈이 AI 전환에 있어 개별적인 시범 프로젝트가 아닌 회사 전체의 프로세스에 집중해야 하는 이유에 대해 이야기하고 있습니다 . 그는 저와 맥킨지 의 기술 및 AI 부문…
- B1 디지털·AI 기술의 활용: 음, 그리고 기술적인 측면에서 보면, 아시다시피 20배 향상된 개발 생산성, 즉 1월에 출시된 클라우드 코드와 같은 기술 덕분에 코드를 작성하는 방식이 근본적으로 바뀌었다는 점이 정말 놀랍습니다.
- B4 가치네트워크·생태계: "아니요, 만약 당신의 사고방식이 ' 나는 콜센터를 운영한다'거나 '나는 공급망 계획을 운영한다'라면, 그리고 '나는 이 일을 하는 방식을 완전히 바꿔버릴 것이다'라면, 그건 잘못된 겁니다.
- 수치 주장: 20개 기업 중 1위는 평균적으로 EBITDA가 20% 증가한 기업입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/McKinsey_&_Company/Rewiring_for_AI_From_Ambition_to_Advantage__E7KxzkK2lYA.md`

**180. [Global Trade Is Being Rewired: What Leaders Need to Know](https://www.youtube.com/watch?v=R2M9LLkgFTg)** — McKinsey & Company · 컨설팅·전략 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 조직 내 속도라는 개념은 변동성이 심한 이 시대에 경쟁 우위를 확보하는 실질적인 기반이 되고 있습니다. 시장 진입, 시장 철수, 자본 재배치, 생산 시설 이전, 다른 시장으로의 이동, 인력 이동, 위기 발생 시 신속한 대응 능력 등을 갖춰야 합니다 . 그 이유는 무역 경로가 변화하고 지정학적 변동성이 지속됨에 따라 기업들이 대응 방식을 재고하고 있기 때문입니다. 슈밤 싱할 수석 파트너도 같은…
- B7 성과: 운영효율: 그리고 우리가 선도 기업들에서 흥미롭게 발견한 점은 그들이 단순히 방어적인 자세를 넘어 , " 지금 주어진 신호를 바탕으로 어떻게 생산성을 실제로 향상시킬 수 있을까?" 또는 "어떻게 하면 생산성을 향상시킬 수 있을까?"라고 고민하고 있었다는 것입니다 .
- B3 전략적 대응: 음, 제 생각에는 이는 경영진들이 이 엄청나게 빠르게 변화하는 AI 시대를 헤쳐나가면서 찾고 있는 자문단의 필요성을 보여주는 매우 중요한 증거라고 생각합니다 .
- 수치 주장: 미국 수입품을 대상으로 위의 세 가지 요소를 모두 적용해 보면, 미국 수입품의 5%는 국가 안보에 매우 중요하고 민감하며, 특정 지역에 집중되어 있고, 지정 학적으로 중립적인 국가에서 수입되는 품목으로 분류됩니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Global_Trade_Is_Being_Rewired_What_Leaders_Need_to_Know__R2M9LLkgFTg.md`

**181. [Redefining Value: Fashion in the Age of AI](https://www.youtube.com/watch?v=EgbFkskWLWM)** — McKinsey & Company · 컨설팅·전략 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 제게 있어 가장 중요한 질문은 인공지능을 어떻게 활용하고, 고객 여정 전반을 어떻게 변화시킬 것인가 하는 것입니다. 왜냐하면 안타깝게도 업계에서는 많은 시범 사업과 훌륭한 실험들이 진행되고 있기 때문입니다. 우리는 조직, 특히 고객 응대 나 공급망 관리와 같이 전략적으로 매우 중요한 영역에서 진정한 조직 개편이 많이 이루어지지 않는 것을 보고 있습니다. 저분은 맥킨지 수석 파트너인 젬마 다우…
- B4 가치네트워크·생태계: 마케팅 및 상업화 측면에서 가치 사슬을 좀 더 내려가 보면, 기획 단계부터 영상, 오디오 또는 시각적 콘텐츠 제작에 이르기까지 전체 마케팅 캠페인을 AI로 완전히 구현할 수 있다는 점에서 동일한 원리가 적용됩니다.
- B2 파괴: 소비자 행동·기대: 그래서 저는 인공지능을 어떻게 활용하고, 인공지능이 고객 여정 전반을 어떻게 변화시키는지에 대한 중요한 질문을 던지고 싶습니다 .
- 수치 주장: 이해를 돕기 위해 말씀드리자면, 상위 20개 기업이 업계 경제적 이익의 92%를 창출하는데 , 이는 매우 높은 집중도입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/McKinsey_&_Company/Redefining_Value_Fashion_in_the_Age_of_AI__EgbFkskWLWM.md`

**182. [AI Is Everywhere. The Agentic Organization Isn’t—Yet](https://www.youtube.com/watch?v=uqVT-2OOToo)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 향후 2~3년 안에 직장인 거의 모두가 새로운 직무 설명서를 필요로 할 것입니다. 그러므로 대부분의 직종은 사라지지 않을 것입니다 . 대부분의 직무는 실제로 재편될 것입니다. [음악] 맥킨지 수석 파트너 알렉시스 크리브코비치(Alexis Krivkovich)입니다. 그녀는 인공지능이 우리의 일자리를 어떻게 변화시킬지에 대해 이야기하고 있으며, 이러한 중대한 변화에 맞춰 리더들이 어떻…
- B5 직무·역량 변화: 그래서 역량 강화 필요성에 대해 질문하면 예상대로 거의 절반에 가까운 리더들이 조직 내에서, 심지어 자신에게서도 기술 격차가 있다고 생각한다고 답합니다.
- B3 전략적 대응: 대부분의 사람들은 더 많은 교육, 역량 강화 , 그리고 더 많은 지원이 절실히 필요하다고 말할 것이며, 이는 고위 경영진에까지 모두 해당됩니다.
- 수치 주장: 그렇다면 이제 AI를 활용하여 업무를 처리할 수 있게 되었으니, 제 시간의 50%를 다르게 써야 할까요?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/2026-07-21/AI_Is_Everywhere._The_Agentic_Organization_Isn’t—Yet__uqVT-2OOToo.md`

**183. [AP CEO on AI, Trust, and the Future of Journalism](https://www.youtube.com/watch?v=ifgkYPogEgU)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B8 부정 성과
- 개요: 음악을 비롯한 거의 모든 것이 변하고 있습니다. 인공지능이 점점 더 큰 역할을 할 것으로 예상합니다. AP의 구조는 진화해야 할 수도 있습니다. 우리는 언제나 인간을 위한 저널리즘을 제공하기 위해 설립되었습니다. 그리고 저는 지금 우리가 기계와 인간 모두를 위한 저널리즘을 제공하고 있다고 생각합니다 . 데시, 당신은 사람들이 사실을 원한다는 이야기를 많이 했잖아요, 그렇죠? 저널리즘과 관련해…
- B4 가치네트워크·생태계: AP에서 일하는 모든 사람들은 우리가 하는 일의 사명에 매우 헌신적이며, 그 사명은 전반적인 생태계를 뒷받침하는 독립적이고 비당파적인 뉴스를 제공하는 것입니다.
- B1 디지털·AI 기술의 활용: 우선, 우리는 신문으로 시작해서 라디오, 방송, 디지털 및 소셜 미디어로 나아갔고, 이제는 데이터 중심의 세상으로 나아가고 있습니다.
- 수치 주장: 결과물의 80%는 그러한 전환을 지속하는 것이 예상보다 훨씬 어렵다는 점에 관한 것입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/AP_CEO_on_AI,_Trust,_and_the_Future_of_Journalism__ifgkYPogEgU.md`

**184. [Brain Health: Helping Individuals, Organizations, and Societies Thrive in the Age of AI](https://www.youtube.com/watch?v=AApkPLFb_gc)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 맥킨지 라이브에 오신 것을 환영합니다. 저는 맥킨지 편집국장 루시아 라힐리입니다. 오늘 이 자리에서는 두뇌 건강과 인공 지능 시대에 인류가 번영하는 방법에 대해 이야기 나눌 예정입니다. 우리는 모두 인공지능이 비즈니스 분야는 물론 개인적인 삶에서도 대화를 지배하게 된 것을 목격해 왔습니다 . 네, 인공지능은 정말 놀랍습니다. 기업들은 신기술에 수십억 달러를 투자하고, 근로자들은 …
- B1 디지털·AI 기술의 활용: 하지만 소셜 미디어에서 우리가 배울 수 있는 교훈은 사람들이 이러한 플랫폼을 통해 소통하고, 성장하고, 창의성을 발휘하기 때문에 새로운 기술을 단순히 두려워해야 한다는 것이 아닙니다.
- B5 리더십·CDO/CAIO: 재키는 건강한 직장 환경 및 연구 과학 담당 이사로서 직장인들의 복지, 회복력, 리더십 개발 및 지속 가능한 인적 자원 성과를 강화하는 데 기여하고 있습니다.
- 수치 주장: 또한, 효과가 입증된 개입 조치를 확대 시행한다면 전 세계적으로 6조 2천억 달러의 추가 GDP를 창출할 수 있다는 중요한 가치가 걸려 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Brain_Health_Helping_Individuals,_Organizations,_and_Societi__AApkPLFb_gc.md`

**185. [Powering Supply Chain With Agentic AI](https://www.youtube.com/watch?v=GJyp5SJNjyo)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: 귀사의 미래 성공을 위해서는 고객 중심적이고, 민첩하며, 회복력 있고, 효율적인 운영이 필수적입니다. 저는 진행자 크리스찬 존슨입니다. 지금 듣고 계신 팟캐스트는 맥킨지 토크 오퍼레이션즈입니다. 이 프로그램에서는 세계 음악 업계의 최고 경영진과 맥킨지 전문가들이 복잡한 정보 속에서 핵심을 짚어보고 새로운 운영 환경을 구축하는 방법을 알려드립니다. 따라서 지난 수십 년 동안 공급망 책임자들은 …
- B4 가치네트워크·생태계: 그래서, 서로 다른 시스템에 걸쳐 있는 이러한 생태계는, 비록 그 시스템들이 각자의 환경에서는 효율적일지라도 , 매우 수동적인 방식으로 운영되며, 서로 연동되지 않습니다 .
- B7 성과: 운영효율: 저희가 이 작업을 진행했던 몇몇 고객 사례를 보면 , AI 에이전트가 판매 원가를 4~7% 절감하고, 생산성을 20~50% 향상시키며, 의사 결정 주기를 단축할 수 있다는 것을 보여주었습니다.
- 수치 주장: 지난 10년 동안 우리가 얻은 결과이자 변함없는 사실은 새로운 기술이 등장할 때마다 많은 기관들이 그 기술에 몰려들어 빠르게 도입하지만, 그 기술을 통해 의미 있는 영향을 얻거나 확장하는 데 어려움을 겪는다는 것입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Powering_Supply_Chain_With_Agentic_AI__GJyp5SJNjyo.md`

**186. [The Serial Builder Advantage: Why Repeat Innovators Win](https://www.youtube.com/watch?v=kzAjzKCZAXs)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 해결하고 싶은 비즈니스 문제를 하나 선택하고 , 그 문제를 해결하는 방법으로 비즈니스 구축을 생각해 보세요. 한 골대를 상대로 여러 번 슈팅을 시도하는 선수들이 여기저기에 여러 번 슈팅을 거는 선수들보다 훨씬 더 성공적인 경향이 있다는 것을 발견했습니다 . 저분은 맥킨지 수석 파트너인 제이슨 벨로입니다. 여러 번의 슛, 하나의 골. 기업 벤처 창업자들이 축구에서 힌트를 얻을 수 있을까요? 네…
- B3 전략적 대응: 하지만 벤처 창업을 하면 경영진이나 이사회에 투자 담당자들이 이미 있기 때문에 투자 유치 과정이 훨씬 수월해집니다 .
- B4 가치제안 변화: 우리가 살고 있는 세상은 불확실성이 많고 경제적, 지정학적 문제도 많은데, 이러한 상황에서 신규 사업 구축을 고려하는 것이 여전히 의미가 있을까요?
- 수치 주장: 2024년에는 일반적인 신규 벤처 기업의 손익분기점 달성 비용이 약 1억 2,500만 달러였는데, 2025년에는 7,700만 달러로 감소했습니다 .
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/McKinsey_&_Company/The_Serial_Builder_Advantage_Why_Repeat_Innovators_Win__kzAjzKCZAXs.md`

**187. [The human advantage in an AI economy](https://www.youtube.com/watch?v=IGAFict9CS4)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 직원 두 명 중 한 명은 극심한 피로감을 느낀다고 보고했습니다 . 인공지능이 할 수 있는 것과 사람들이 이해할 수 있는 것 사이의 격차가 클수록, 인공지능이 지닌 잠재적 가치가 제대로 활용되지 못한다. 그래서 가장 앞서가는 리더들은 인공지능 과 인간이 서로를 보완할 수 있도록 업무 방식을 어떻게 재설계해야 할지 고민하고 있습니다. 저분은 맥켄지 선임 연구원인 재키 브래시입니다 . 그녀는 리더…
- B4 가치네트워크·생태계: 공급망을 소위 '우호적인' 국가로 이전한다는 이야기를 많이 듣지만, 이는 분명히 큰 사업입니다.
- B4 민첩성·양손잡이: 그렇다면 여러분은 글로벌 사업 영역이나 여러 국가에 걸친 사업 영역을 어떻게 생각하고, 이를 활용하여 생산 및 배송 지역에서 회복력을 구축하고, 변화하는 현실에 맞춰 더 빠르게 조정할 수 있도록 운영을 민첩하게 만드는 방법을 알고 계십니까?
- 수치 주장: 또한, 우리가 효과가 입증된 개입 조치를 확대 시행한다면 전 세계적으로 6조 2천억 달러의 추가 GDP를 창출할 수 있다는 중요한 가치가 걸려 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/The_human_advantage_in_an_AI_economy__IGAFict9CS4.md`

**188. [Why Most Companies Aren't Seeing Meaningful Returns from AI](https://www.youtube.com/watch?v=BHQyOFaARQI)** — McKinsey & Company · 컨설팅·전략 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 사람들은 당신이 오늘처럼 느려지는 일은 다시는 없을 거라는 사실을 깨달아야 합니다. 따라서 미래에 성공하기 위한 중요한 요소 중 하나는 빠르게 학습하고 변화에 발맞춰 나갈 수 있는 적응력 있는 운영 모델이 될 것입니다. 저분은 맥켄지 로펌의 수석 파트너인 탕기 카텔란입니다. 모든 기업이 AI를 통해 생산성 향상을 목표로 하고 있지만, 모든 기업이 동일한 AI 도구를 사용할 수 있다면 경쟁 우…
- B7 성과: 운영효율: 탄지, 만약 당신이 AI 혁신을 통해 회사를 이끌고 있다면, AI가 단기적인 생산성 향상에만 그치는 게 아니라 장기적인 가치를 창출하는지 판단하기 위해 어떤 지표를 사용할 수 있을까요?
- B2 파괴: 경쟁구도: 하지만 이러한 기술들이 보편화되면서 CEO들은 경쟁사들도 똑같은 기술에 접근하여 생산성 향상과 효율성 증대라는 동일한 목표를 추구할 것이라는 문제에 직면하게 됩니다.
- 수치 주장: 미시적인 관점에서 보면, 현재 우리가 이용 가능한 기술을 활용할 수 있다면 근로자들이 수행하는 활동의 약 53%를 자동화할 수 있을 것입니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/McKinsey_&_Company/Why_Most_Companies_Aren't_Seeing_Meaningful_Returns_from_AI__BHQyOFaARQI.md`

**189. [The Biggest AI Opportunity Isn’t Replacing People | Stanford Economist](https://www.youtube.com/watch?v=u76xdhpF474)** — McKinsey & Company · 컨설팅·전략 · US · 2026-08 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: Ultimately, no company, no country, no person has ever succeeded by just focusing on the same thing over time. You need to expand your horizons. And that's what helped make America successful, and I think the successful …
- B2 파괴: 경쟁구도: I worry a lot that we're going to a very disruptive period.
- B5 직무·역량 변화: &gt;&gt; Earlier in the conversation, we talked about the CFO client of yours who reflexively turned to headcount reduction cost-cutting.
- 수치 주장: &gt;&gt; What we're finding is that you know, when we're working with organizations, I would say 70 to 80% of the work isn't on what should be automated or what is that tech enablement part of the workflow.
- 교량: Avenue 1 동적역량 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/McKinsey_&_Company/The_Biggest_AI_Opportunity_Isn’t_Replacing_People_Stanford_E__u76xdhpF474.md`

---

## Meta


**190. [The Metaverse and How We'll Build It Together -- Connect 2021](https://www.youtube.com/watch?v=Uvufun6xer8)** — Meta · 파운데이션 모델 · US · 2021-10 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, Connect에 오신 것을 환영합니다! 오늘은 메타버스에 대해 얘기해 볼 겁니다 우리가 가능하다고 믿는 새로운 기능에는 무엇이 있고 여러분께 선사할 새로운 경험과 우리가 이뤄낼 창조 경제와 이를 위해 개발되어야 할 새 기술은 무엇인지 어떻게 우리가 이 일을 함께 이뤄낼지 알아볼 겁니다 우리 삶 속 기술의 기본적인 이야기는 기술이 우리에게 우리 자신을 더 잘 표현하고 세상을 더 풍…
- B1 디지털·AI 기술의 활용: 바로 사람입니다 오늘날 저희는 소셜 미디어 기업으로 여겨집니다 하지만 사실 저희의 핵심은 사람들을 연결하는 기술을 구축하는 데 있어요 그리고 저희가 개척해야 할 다음 분야는 바로 메타버스입니다 저희가 처음 시작했을 때는 소셜 네트워킹이 차세대 분야였듯 말이에요 Facebook은 특정한 시간, 특정한 장소에서 태어났습니다 바로 대학교 캠퍼스에서 웹으로 탄생했죠 당시에는 그 정도만 가능했는데요 기술에 사람을 중심으로 한 경험을 접목하여 Facebook을 만들게 되었…
- B4 가치네트워크·생태계: 네 메타버스에서는 어떠한 장소 뿐만 아니라 어떠한 시대로도 순간이동할 수 있습니다 고대 로마 시대입니다 상상해 보세요 거리에 서서 소리를 듣고 시장을 방문하며 2,000년 이상 전 삶의 리듬을 느껴 보는 거죠 로마의 광장이 어떻게 지어졌는지 광장이 지어지는 걸 눈앞에서 직접 보면서 배운다고 상상해 보세요 여러분, 안녕하세요 전 마니 레빈입니다 메타버스에서는 이전에 경험한 학습법과 전혀 다른 학습을 하게 될 거예요 헤드셋이나 안경을 끼고 공부 주제의 도식을 그릴 …
- 수치 주장: 지금 문자 보내는 중이야 좋아, 집에서 봐 이곳도 정말 멋지지만 난 돌아가 봐야겠어, 보즈 어떻게 메타버스에서 사람들을 만나 어울릴지 살짝 엿보셨는데요 아직 갈 길이 멀지만 기본적인 구성 요소들은 형태를 갖추기 시작했습니다 먼저 현실감입니다 메타버스를 정의하는 특징 중 하나죠 정말로 다른 사람들과 그 자리에 있는 듯 느끼는 겁니다 사람들의 표정과 몸짓까지 엿보며 정말로 포커에서 좋은 패를 가졌는지 추측할 수도 있죠 오늘날의 기술로는 전달할 수 없는 섬세한 의사소…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Meta/The_Metaverse_and_How_We'll_Build_It_Together_--_Connect_202__Uvufun6xer8.md`

**191. [Meta Connect Keynote 2022](https://www.youtube.com/watch?v=hvfV-iGwYX8)** — Meta · 파운데이션 모델 · US · 2022-10 · en · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: I'm excited about what comes next. It's a future that is beyond any one company that will be made by all of us. Hey, everyone, and welcome to Connect. Last year, we shared our vision for the metaverse, a future where you…
- B4 가치네트워크·생태계: We have deep ecosystems for creators to connect with audiences and share their work, and virtual worlds will become another place where great content can be made.
- B1 디지털·AI 기술의 활용: The first one uses machine learning-based neural radiance fields to reconstruct the appearance of a 3D object from multiple 2D images taken at different angles.
- 수치 주장: Obviously, this became even more important in 2020, and since then, we've deployed 60,000 Quest 2 headsets, and we have transformed our onboarding process, welcoming over 150,000 people onto our virtual campus that we call the Nth Floor, which we believe is th…
- 교량: Avenue 1 동적역량 · 기술: 에이전트 프레임워크
- 원문: `transcripts/channels/Meta/Meta_Connect_Keynote_2022__hvfV-iGwYX8.md`

**192. [Boz To The Future Podcast #23 - The Future According to James Cameron](https://www.youtube.com/watch?v=qOdjM14QW0s)** — Meta · 파운데이션 모델 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 제 생각에는 평면 광학 배열과 그 배열을 뇌가 실제 데이터로 어떻게 해석하는지를 살펴보는 것이 좋을 것 같습니다. 그리고 이것은 공간 데이터입니다. 시간에 따른 공간 데이터 . 솔직히 말해서 , 거기에 답이 없을 것 같다는 생각이 자꾸 드네요 . 라이트 필드 방식일 수도 있고, 평면 광학 방식일 수도 있지만, 거기에는 어떤 답도 없습니다. 이 내용을 팟캐스트에 꼭 넣어야겠어요. 안녕하세요, …
- B1 디지털·AI 기술의 활용: 아까 우리 농담으로 당신의 워크플로가 LLM(Learning Leadership Model)이랑 비슷하다고 했잖아요.
- B4 가치네트워크·생태계: 저희 파트너십에서 흥미로운 점 중 하나는, 스토리텔링에 대한 기준이 매우 높으시고, 사람들이 그 스토리를 경험하는 방식에 대한 생각이 확고하시다는 거예요 .
- 수치 주장: 영화 '어비스'가 개봉한 지 38년이 지났는데 , '어비스'는 소프트 서페이스, 즉 CG를 영화계에 처음으로 도입한 작품 중 하나였습니다 .
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Meta/Boz_To_The_Future_Podcast_#23_-_The_Future_According_to_Jame__qOdjM14QW0s.md`

**193. [Boz To The Future # 24: The Future According to Francois Chardavoine](https://www.youtube.com/watch?v=WpFCYR3f46U)** — Meta · 파운데이션 모델 · US · 2025-11 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Welcome to BOS to the future. Uh a podcast that I created so that we would have time to go much much [music] deeper on a small number of topics as opposed to kind of being surface deep across a larger number as is so oft…
- B1 디지털·AI 기술의 활용: And you have really a really unfair advantage in terms of the content you guys get to put out on your social media channels compared to the rest of us.
- B4 가치네트워크·생태계: I I enjoyed it too and I I really was so grateful for the partnership that we've had uh bringing, you know, these wonderful universes into the immersive space.
- 교량: Avenue 1 동적역량 · 기술: 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Meta/Boz_To_The_Future_#_24_The_Future_According_to_Francois_Char__WpFCYR3f46U.md`

**194. [Boz To The Future # 25: The Future According to Dylan Field](https://www.youtube.com/watch?v=diMGvhBfy74)** — Meta · 파운데이션 모델 · US · 2025-11 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: Welcome to Bos to the Future, a podcast I started so that we could get a little deeper uh on a few topics because so often I find in our industry these conversations kind of can be very surface deep and very broad. Uh an…
- B1 디지털·AI 기술의 활용: &gt;&gt; Well, and also if it were moving to the cloud, uh you now have instead of managed servers for most people.
- B6 장벽: 관성·저항: My point being like there's this inertia in the society that that has an effect on these things and we do have time to shape them.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습 · 칩·하드웨어 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Meta/Boz_To_The_Future_#_25_The_Future_According_to_Dylan_Field__diMGvhBfy74.md`

**195. [Boz To The Future #26: The Future According to Ed Catmull](https://www.youtube.com/watch?v=4s1_DKMYQVo)** — Meta · 파운데이션 모델 · US · 2026-05 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 · 빠짐: B3 전략 대응, B5 구조 변화, B7 긍정 성과, B8 부정 성과
- 개요: Welcome to Bos to the Future. Uh the podcast where we dive deep into a smaller number of topics. I kind of created this podcast after I felt so many podcasts I listen to in the technology sector tended to go really broad…
- B2 파괴: 경쟁구도: He called me up and he said u he said what he wanted to do was consolidate them because you know the competitive advantages and we'll be willing to sell the uh our hardware business to them.
- B1 디지털·AI 기술의 활용: But as as as technology changed and the internet came out and social media and cell phones, then the the sheer gigantic size of the industry and the impact on it was such that the hype thing grew correspondingly &gt;&gt; at this compound rate.
- 수치 주장: Mars what was a result of a compounding of knowledge &gt;&gt; right &gt;&gt; and so it's an easy standin for it but it was focused on the number of &gt;&gt; transistors &gt;&gt; transistors and so forth which is too abstract uh for people to relate to so I I t…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Meta/Boz_To_The_Future_#26_The_Future_According_to_Ed_Catmull__4s1_DKMYQVo.md`

---

## Meta Developers


**196. [Building Next-Gen Worlds with Meta Horizon Studio](https://www.youtube.com/watch?v=viXoK-MJRls)** — Meta Developers · 에이전트·개발도구 · US · 2025-10 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 지금 Connect의 마지막 개발 세션입니다. 기력이 다 떨어지셨나요? 피곤하세요, 아니면 신나세요? 괜찮은. 괜찮은. 이 일을 위해 깨어 있으세요. 괜찮은 기술 제품 좀 보셨나요? 응. 개인적으로 저는 새로운 오클리 뱅가드 선글라스를 하루빨리 써보고 싶습니다. 정말 예뻐 보이네요. 저는 수상 스포츠, 스탠드업 패들보드, 윈드서핑을 즐깁니다. 메타 AI에게 턴 진행 방법에 대한 팁을…
- B1 디지털·AI 기술의 활용: 음, 모바일 기기에 관해서 말씀드리자면, 현재로서는 모바일 경험을 클라우드 스트리밍 방식으로 제공하고 있기 때문에, 비디오 디코더 성능이 정말 형편없는 기기가 아니라면 정확한 기기 종류는 크게 중요하지 않습니다 .
- B3 전략적 대응: 음, 다른 크리에이터들이 사용할 수 있도록 직접 제작한 콘텐츠를 판매할 수 있게 되는 날짜는 아직 정해지지 않았지만, 로드맵 수립 과정의 일환으로 팀에서 논의 중인 사항입니다 .
- 수치 주장: 음, 스튜디오의 주요 기능들을 하나씩 살펴보면서 세계 최고의 데스크톱 에디터들과 비교해 보고, 그 다음에는 플레이사이드 스튜디오 개발자들과 함께 15분 정도 개발자 회고 시간을 갖겠습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Meta_Developers/Building_Next-Gen_Worlds_with_Meta_Horizon_Studio__viXoK-MJRls.md`

**197. [Developer Preview: Introducing Meta Wearables Device Access Toolkit](https://www.youtube.com/watch?v=U0Ha6AmXBS0)** — Meta Developers · 에이전트·개발도구 · US · 2025-10 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 헤이, 메타, 영상 찍어줘. 좋아요 , 여러분. 자, 시작하기 전에, 여기 계신 분들께 질문 하나 드리겠습니다 . 자, 여러분 모두 손을 들어주세요. 레이 블라이딩 메타 선글라스를 이미 가지고 계신 분이 몇 분이나 되시나요? 방 대부분이 그런 것 같네요, 확실히 말할 수 있을 것 같아요. 괜찮은. 자, 다시 한번 말씀드리지만, RBM 소유주뿐만 아니라 방 전체 구성원들의 의견을 들어…
- B4 가치네트워크·생태계: 저희는 이러한 단계별 접근 방식을 통해 RBM 고객이나 Rayban 메타 고객에게 어떤 점이 공감을 얻는지, 개발자들이 저희에게 무엇을 필요로 하는지, 그리고 이 플랫폼을 중심으로 확장 가능한 생태계를 구축하는 가장 좋은 방법은 무엇인지 파악하고자 합니다 .
- B7 성과: 사회적 편익: 아시다시피, 저희가 진정으로 영감을 받는 분야 중 하나는 시각 장애인 및 저시력자 커뮤니티에서 AI 웨어러블 기기, 특히 AI 안경에 대한 관심입니다 .
- 수치 주장: 지난 10년 이상 동안 18버디즈의 사명과 목표는 단 하나, 골퍼들이 실력을 향상시키고 골프를 더욱 즐길 수 있도록 돕는 제품을 만들기 위해 우리가 활용할 수 있는 최고의 기술을 사용하는 것입니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Meta_Developers/Developer_Preview_Introducing_Meta_Wearables_Device_Access_T__U0Ha6AmXBS0.md`

**198. [Meta Horizon Store: Paths to Engage and Monetize Your Audience](https://www.youtube.com/watch?v=DK5Q6C8Iepo)** — Meta Developers · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 여러분 모두 환영합니다. 환영. 음, 농담으로 시작하라고 하더군요. 음, 그리고 제가 만든 농담 몇 개를 A/B 테스트해 봤어요. 모두 정전기적으로 부정적인 결과가 나왔습니다. 자, 저희는 제품 업데이트에 집중하겠지만 , 플랫폼 수익 창출 및 참여에 대한 개발자 세션에 오신 것을 환영합니다. 음, 오늘 아침에 참석하셨다면, 사만다 라이언이 여러 콘텐츠와 개발자들의 성공 사례, 그리고…
- B2 파괴: 소비자 행동·기대: 그래서 그들은 모바일로 눈을 돌렸고, 모바일은 고객 여정을 훌륭하게 만들고 고객 유지율을 높이는 데 기여했습니다 .
- B4 가치제안 변화: 수익 모델 전략이 플레이어 프로필별로 어떻게 다른지, 그리고 이전 세션에서 다뤘던 것처럼 각 플레이어 유형에 따라 어떻게 적용되는지 궁금합니다.
- 수치 주장: 틱톡에서 10억 회 이상의 자연 조회수를 기록했고, 백만 명이 넘는 유료 구독자를 보유하고 있으며, 실제로 우리가 확인한 바로는 6개월 만에 유료 구독자 수가 9배나 증가했습니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Meta_Developers/Meta_Horizon_Store_Paths_to_Engage_and_Monetize_Your_Audienc__DK5Q6C8Iepo.md`

**199. [The State of the VR Ecosystem: Building a Sustainable Future](https://www.youtube.com/watch?v=_NMYZYzva6Q)** — Meta Developers · 에이전트·개발도구 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 이번 발표는 VR 생태계의 현황에 대한 것입니다 . 저는 매년 이 강연을 준비하면서, 만약 제가 개발자의 입장이 되어 이와 같은 플랫폼에서 오랜 기간 개발자로 일했다면 무엇을 알고 싶을지 생각해 보았습니다. VR 생태계에 대해 무엇을 알고 싶을까요 ? 저를 모르시는 분들을 위해 소개드리자면, 제 이름은 크리스 프루엣입니다. 저는 Meta에서 게임 운영을 맡고 있습니다. 주로 말하자면, 여러분…
- B4 가치네트워크·생태계: 실제로 수많은 새로운 성공 사례들이 있는데, 저희가 액셀러레이터 프로그램을 시작한 주된 이유는 생태계에서 자연스럽게 생겨나는 예상치 못한 것들을 발견하고, 그것들을 더 크게 성장시킬 수 있다고 생각했기 때문입니다.
- B1 디지털·AI 기술의 활용: 그리고 그중 하나, 오늘 제가 이야기하고 싶은 것은 소셜 미디어, 특히 유튜브, 틱톡, 인스타그램 릴스를 활용하여 사용자를 확보하는 방법입니다.
- 수치 주장: 전반적으로 퀘스트 스토어 수익, 즉 개발자에게 지급하는 금액은 2024년과 2025년 사이에 약간 증가했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Meta_Developers/The_State_of_the_VR_Ecosystem_Building_a_Sustainable_Future___NMYZYzva6Q.md`

**200. [VR 201: Essential Tools to Power Your Quest Development](https://www.youtube.com/watch?v=rVvqfcD3jmg)** — Meta Developers · 에이전트·개발도구 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 오늘 세션에서는 VR이 현재 어디에 있는지에 대해 간단히 이야기해 보려고 합니다. VR에 대해 한동안 관심을 두지 않았 거나 Meta가 진행해 온 여러 활동에 주목하지 않았다면 VR용 앱 개발이 어렵다고 생각할 수도 있습니다. 그리고 매장이 너무 붐벼서 힘들죠, 그렇죠? 혹은 설정 과정이 번거롭다는 이유일 수도 있습니다. 혹은 VR 개발을 시작하려면 정말 전문적인 지식이 필요하다고 생각할 수…
- B1 디지털·AI 기술의 활용: 제가 보여드릴 일반적인 슬라이드는 ChatGPT와의 상호 작용을 보여주는 예시인데, 게임 맥락에 맞춰서, LLM이 해석할 수 있는 추가적인 맥락을 제공해 주시면 훨씬 더 흥미로운 결과를 얻을 수 있을 겁니다.
- B3 전략적 대응: 그러니 저희 AI 로드맵과 현재 진행 중인 작업에 정말 관심이 있으시다면 , 해당 녹화 영상을 시청하시는 것을 추천합니다.
- 수치 주장: 저희는 작년에 여러 사업에 1억 5천만 달러 이상을 투자했는데, 그중에는 매우 성공적인 스타트업 개발자 경진 대회도 포함되어 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/Meta_Developers/VR_201_Essential_Tools_to_Power_Your_Quest_Development__rVvqfcD3jmg.md`

**201. [VR Performance Fundamentals for Quest 3/3S](https://www.youtube.com/watch?v=w-ys2nE-MgI)** — Meta Developers · 에이전트·개발도구 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 여러분. 환영. 시작한 지 몇 분밖에 안 됐으니 시간이 좀 촉박할 것 같습니다. 오늘 보여드릴 콘텐츠가 많네요. 특히 점심시간에 참여해 주셔서 감사합니다. 제 이름은 데이비드 버렐입니다. 그리고 이분은 제 동료인 닐 베이트카입니다. 네, 저희 둘 다 Meta의 Reality Labs 사업부 내 개발자 플랫폼 팀에서 기술 리더로 일하고 있습니다. 음, 저희 둘 다 Quest의 성능…
- B4 가치네트워크·생태계: 그러니까, 만약 새로운 변경 사항을 적용하고 싶은데, 전체 생태계에 바로 적용하고 싶지 않다면 1%씩 단계적으로 적용해보고 문제가 생기면 되 돌리면 됩니다.
- B2 파괴: 소비자 행동·기대: 반면에, 더욱 뛰어난 성능과 반응성을 갖춘 사용자 경험은 감정적으로 더 큰 몰입감을 유발하고 사용자 참여도를 높일 수 있습니다.
- 수치 주장: 한 가지 유의할 점은 과거 다른 퀄컴 GPU를 출시할 때는 MSAA를 4배로 설정하는 것이 권장 사항이었으며, 실제로 API에서 권장 MSAA 레벨을 조회하면 4배로 표시된다는 것입니다 .
- 교량: Avenue 1 동적역량 · 기술: 프로토콜·표준
- 원문: `transcripts/channels/Meta_Developers/VR_Performance_Fundamentals_for_Quest_33S__w-ys2nE-MgI.md`

---

## Microsoft


**202. [AI and automation expert on how leaders use AI agents to get ahead | Pascal Bornet](https://www.youtube.com/watch?v=HXy3J1mGHRE)** — Microsoft · 에이전트·개발도구 · US · 2025-10 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: And this is, I think, the most important outcome that I've had from more than two decades of implementing those technologies is the companies that succeed are only the ones that put the people in the center of that trans…
- B1 디지털·AI 기술의 활용: So, when I talk about large language models, I'm talking about generative AI in the form of ChatGPT, for example.
- B2 파괴: 소비자 행동·기대: They have also a store colleague assistant that provides personalized guidance to staff based on their specificities.
- 수치 주장: Really across- it's really across the board and, and the out- I mean, just to give you a bit of, what you can expect from those, from implementing agentic artificial intelligence in your company, JPMorgan reduced fraud by 70%.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Microsoft/AI_and_automation_expert_on_how_leaders_use_AI_agents_to_get__HXy3J1mGHRE.md`

**203. [Is Agentic AI upending the corporate ladder? EY's Global Consulting AI Leader shares what’s coming](https://www.youtube.com/watch?v=ilaDQLa1Lrk)** — Microsoft · 에이전트·개발도구 · US · 2025-12 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: People that will join companies next year will be managers on day one. They will just be managing a workforce that is an agentic-based workforce, one that is extremely powerful and sometimes clumsy. Welcome to WorkLab th…
- B1 디지털·AI 기술의 활용: We'll be talking about moving from pilot projects to real world impact, reskilling for the AI era, and what leadership looks like when humans and AI agents team up.
- B5 리더십·CDO/CAIO: We'll be talking about moving from pilot projects to real world impact, reskilling for the AI era, and what leadership looks like when humans and AI agents team up.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Microsoft/Is_Agentic_AI_upending_the_corporate_ladder_EY's_Global_Cons__ilaDQLa1Lrk.md`

**204. [The AI app transforming how Kenya’s small businesses grow](https://www.youtube.com/watch?v=be_LYViMr2k)** — Microsoft · 에이전트·개발도구 · US · 2026-02 · en · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: For most people in this continent, the mobile phone was the first compute unit they had access to. The mobile phone is the primary device where everything is done. Most of the mobile devices that you have here, they do n…
- B1 디지털·AI 기술의 활용: The biggest challenge was how do you deploy machine learning models at scale to edge devices that are low resources or low, with very low constrained environments?
- B2 파괴: 소비자 행동·기대: But we had all this data that we needed, streamlined it, put it to one sort of database, and for you to give us, information that we needed, we needed to know customer behavior.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습 · 추론 최적화 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Microsoft/The_AI_app_transforming_how_Kenya’s_small_businesses_grow__be_LYViMr2k.md`

**205. [The future of work: navigating the AI shift | On Second Thought](https://www.youtube.com/watch?v=KFsu0Hyf1XM)** — Microsoft · 에이전트·개발도구 · US · 2026-02 · en · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: We're not in the business of predictions, but there was a time when you used to write on resumes, proficient in Microsoft Word, proficient in email. When do you think we're going to reach the era where you don't even inc…
- B5 리더십·CDO/CAIO: And I think it's also, some of it comes down to leadership, because if a company is only thinking about AI from the perspective of who can I automate?
- B4 가치네트워크·생태계: And so how are you- or outsourcing parts of it to AI, it's building that habit to actually stop and think, do I need to do this, or can I delegate it to Copilot?
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Microsoft/The_future_of_work_navigating_the_AI_shift_On_Second_Thought__KFsu0Hyf1XM.md`

**206. [AI's Mythos Moment: Preparing governments for AI | Former UK Prime Minister Rishi Sunak](https://www.youtube.com/watch?v=vHlFzbE78jk)** — Microsoft · 에이전트·개발도구 · US · 2026-06 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: With Mythos, what's happened is you've had a kind of gated release for this thing where it's like, “Hang on, there's some risks here. We can't just let this thing be released into the world. We need to give defense the t…
- B8 부정 성과: 보안·프라이버시: We talk about why cyber attacks are today's leading AI risks, the changing nature of digital sovereignty, and what AI may mean to your job.
- B4 가치네트워크·생태계: And that is a strategy that makes more sense for a middle power, is to identify those bits of key supply chains, technology or otherwise, where they can occupy a really important position.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 칩·하드웨어 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Microsoft/AI's_Mythos_Moment_Preparing_governments_for_AI_Former_UK_Pr__vHlFzbE78jk.md`

**207. [The future of work has no org chart | Microsoft Katy George](https://www.youtube.com/watch?v=r4qZz66GlNQ)** — Microsoft · 에이전트·개발도구 · US · 2026-07 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: This is not a once and done transformation where we all learn something, change the way we work, and then we're done and can go on to the next thing. No, this is going to be forever, that we are both doing our jobs and c…
- B5 리더십·CDO/CAIO: So business leadership, sponsorship, and like, real active sponsorship, the leaders who are power users themselves are creating teams of power users.
- B5 조직문화 변화: And mindset because this is not a once and done transformation where we all learn something, change the way we work, and then we're done and can go on to the next thing.
- 수치 주장: So, you know, even most of the models that economists have used to predict what's going to happen with AI take job descriptions, break them down into all the tasks, figure out what percentage can be automated with AI, it's always 30% on average across any grou…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Microsoft/The_future_of_work_has_no_org_chart_Microsoft_Katy_George__r4qZz66GlNQ.md`

**208. [Why AI adoption fails (and how to fix it)](https://www.youtube.com/watch?v=mlXbfJf80k8)** — Microsoft · 에이전트·개발도구 · US · 2026-07 · en · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: One of the biggest challenges of AI today. It's so easy to start experimenting. It's a lot harder to integrate whatever you build into your everyday workflow. And that to me kind of underscores that It's not just about l…
- B1 디지털·AI 기술의 활용: We're an investor in a company called Tough Day and their conversational AI agent is called Tuffy, and it's designed to tackle workplace challenges.
- B5 조직문화 변화: And, I think the mindset is you got to have like a, an experimentation mindset, an innovation mindset, like an AI forward mindset.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Microsoft/Why_AI_adoption_fails_(and_how_to_fix_it)__mlXbfJf80k8.md`

---

## Microsoft Azure


**209. [Optimize Azure Storage costs: smart tier, automation, and Azure Reservations](https://www.youtube.com/watch?v=QOcCdyL1lLY)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] Azure 스토리지 비용 최적화 세션에 오신 것을 환영합니다. 저는 마이크로소프트에서 Azure 스토리지 부문 수석 제품 관리자로 근무하는 비바바 라마다스입니다. 오늘은 데이터 증가를 관리하고, 비용을 통제하며, 스토리지 투자에서 실질적인 비즈니스 가치를 창출하는 데 도움이 되는 실용적인 전략을 살펴보겠습니다. 방대한 데이터 환경을 관리하든, 이제 막 워크로드를 Azure로 마이그레…
- B1 디지털·AI 기술의 활용: 블롭 스토리지와 데이터 레이크링크 스토리지는 클라우드 우선 AI 및 분석을 위한 대규모 확장 가능한 객체 스토리지를 제공합니다 .
- B7 성과: 운영효율: Azure Blob Storage 및 Data Lake는 1년에서 3년까지의 약정 기간을 제공하여 단위당 비용을 낮추고 예측 가능한 스토리지 요구 사항에 대한 비용을 절감할 수 있도록 지원합니다.
- 수치 주장: Azure Blob Storage 및 Data Lake는 1년에서 3년까지의 약정 기간을 제공하여 단위당 비용을 낮추고 예측 가능한 스토리지 요구 사항에 대한 비용을 절감할 수 있도록 지원합니다.
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Microsoft_Azure/Optimize_Azure_Storage_costs_smart_tier,_automation,_and_Azu__QOcCdyL1lLY.md`

**210. [Personalize Customer Experiences](https://www.youtube.com/watch?v=gaEgp-nEB9g)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 미래의 통신은 개인 맞춤형이 될 것이다. AI 기반 인사이트를 통해 운영자는 모든 고객을 인식하고, 고객의 요구를 예측하며, 모든 접점에서 맞춤형 경험을 제공할 수 있게 되었습니다. 통신사들은 마이크로소프트와 협력하여 첨단 음악 AI를 활용해 고객 참여를 경쟁 우위로 전환하고, 고객 충성도를 높이고, 새로운 수익원을 창출하고 , 지속 가능한 성장을 촉진하고 있습니다. 통신 회사들은 서로 원활…
- B7 성과: 운영효율: 텔스트라가 AI 기반 비서를 활용한 결과, 사용자 90%가 상당한 시간 절약을 경험했다고 응답했으며, 후속 고객 문의 건수는 20% 감소했습니다.
- B1 디지털·AI 기술의 활용: Amdocs 고객 참여 플랫폼( CEP)은 Microsoft의 AI 및 클라우드 기능과 Amdocs의 심층적인 통신 전문 지식을 결합하여 전체 고객 라이프사이클에 걸쳐 운영을 간소화합니다.
- 수치 주장: 텔스트라가 AI 기반 비서를 활용한 결과, 사용자 90%가 상당한 시간 절약을 경험했다고 응답했으며, 후속 고객 문의 건수는 20% 감소했습니다.
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Microsoft_Azure/Personalize_Customer_Experiences__gaEgp-nEB9g.md`

**211. [Reduce Azure networking service costs: smart routing, locality, and efficient connectivity](https://www.youtube.com/watch?v=KiF_Cn5PdfU)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 환영. 제 이름은 안드레아 마이클이고 마이크로소프트에서 제품 관리자로 일하고 있습니다. 이 세션에서는 스마트 아키텍처, 운영 및 도구를 통해 Azure 네트워킹 비용을 최적화하는 전략을 다룹니다. Azure는 다양한 제품군을 통해 안전한 글로벌 네트워킹 솔루션을 제공합니다 . Azure의 철학은 고객에게 효율적인 네트워크 아키텍처를 구축하고 유지 관리하는 데 필요한 도구를 제공함으로써 데이터…
- B7 성과: 운영효율: 이는 데이터 전송 비용을 절감할 뿐만 아니라 지연 시간을 줄여 애플리케이션 성능을 향상시킵니다.
- B1 디지털·AI 기술의 활용: 궁극적으로 네트워킹 비용 최적화는 단순히 요구 사항을 충족하는 것을 넘어 클라우드를 통해 더 많은 것을 달성할 수 있도록 지원하는 지속 가능하고 확장 가능하며 혁신적인 네트워크 아키텍처 구축과 밀접한 관련이 있습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Microsoft_Azure/Reduce_Azure_networking_service_costs_smart_routing,_localit__KiF_Cn5PdfU.md`

**212. [S2E1 | Are my agents hunting for data? — The Shift Podcast by Microsoft Azure](https://www.youtube.com/watch?v=uTv-E-vz570)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: 결국, 최종 목적지는, 뭐랄까, 여전히 인간이죠, 그렇죠? Shaft, [음악] Agentic Edition은 AI 도구를 개발하는 사람들과 에이전트를 만드는 사람들을 연결하여 모두가 함께 발전할 수 있도록 합니다. 오늘은 마이크로소프트 패브릭 팀의 론, 조쉬, 딥티, 킬리언과 함께 여러분께서 보내주신 질문에 대해 솔직하게 이야기 나눠보려고 합니다 . 내 에이전트들이 데이터를 찾고 있나요? …
- B1 디지털·AI 기술의 활용: 고객과 이야기를 나누면서 가장 놀랐던 점 중 하나는, 데이터를 하나의 데이터 레이크로 가져오기 위해 어떤 소스를 우선시해야 하는지, 즉 지름길을 택해야 하는지, 미러링 방식을 사용해야 하는지, 아니면 데이터베이스를 사용해야 하는지에 대한 질문이었습니다.
- B2 파괴: 경쟁구도: 그렇게 또 하루가 지나고 10일이 지났는데 벌써 경쟁사보다 뒤처져 있는 거죠?
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Microsoft_Azure/S2E1_Are_my_agents_hunting_for_data_—_The_Shift_Podcast_by_M__uTv-E-vz570.md`

**213. [S2E3 | Wait, my agent needs a database? — The Shift Podcast by Microsoft Azure](https://www.youtube.com/watch?v=k9QgmurnNCU)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 제 생각에 질문에 직접적으로 답하자면, AI 앱에는 항상 데이터베이스가 필요합니다 . 이러한 변화, 즉 [음악] 에이전트 에디션은 AI 도구를 개발하는 사람들과 에이전트를 만드는 사람들을 연결하여 우리 모두가 함께 발전할 수 있도록 합니다. [음악] 오늘은 마이크로소프트 애저 팀의 제임스, 재러드, 데비, [음악] 그리고 니키샤와 함께 여러분께서 보내주신 질문에 대해 솔직하게 이야기 나눠보려…
- B1 디지털·AI 기술의 활용: 그러니까 풍부한 SDK를 제공하고, 파이썬( 많은 생성형 AI 개발에서 볼 수 있듯이) 이나 자바스크립트(역시 매우 큰 비중을 차지하고 있음)와 같은 원하는 언어를 지원하거나, 자바나 .NET으로 엔터프라이즈 애플리케이션을 실행하는 경우에도 마찬가지입니다 .
- B2 파괴: 데이터 가용성: 이 시스템은 바로 그런 종류의 비정형 데이터를 처리하기 위해 만들어졌습니다.
- 교량: — · 기술: 프로토콜·표준 · 검색·RAG
- 원문: `transcripts/channels/Microsoft_Azure/S2E3_Wait,_my_agent_needs_a_database_—_The_Shift_Podcast_by___k9QgmurnNCU.md`

**214. [S2E6 | Is Postgres the wave of the future? — The Shift Podcast by Microsoft Azure](https://www.youtube.com/watch?v=OBc1TyXH0WQ)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B7 긍정 성과
- 개요: 데이터베이스에 대해 이야기할 때 "상황에 따라 다르다"라는 말을 빼놓을 수 없겠죠 ? Gentic Edition의 The Shift는 AI 도구를 개발하는 사람들과 에이전트를 만드는 사람들을 연결하여 모두 함께 발전할 수 있도록 합니다. 오늘은 마이크로소프트 애저 팀과 함께 잠시 휴식을 취해 보겠습니다. [음악] 에릭, 마르코, 아비나브, 그리고 클레어가 여러분이 보내주신 질문에 대해 이야기…
- B1 디지털·AI 기술의 활용: AI 에이전트는 해당 단계를 실행하고, 오류가 발생하면 오류의 원인을 파악하고, 다시 실행하고, 또 다른 문제를 발견하고, 그 원인을 파악하고, 다시 실행하는 과정을 반복할 수 있습니다.
- B4 가치네트워크·생태계: PostgreSQL은 매우 방대한 생태계를 가지고 있으며, 그 인기만으로도 에이전트에 매우 적합한 환경이 조성되었다고 생각합니다.
- 수치 주장: 참고로, 제가 찾아보니 2017년에 출시되었더군요.
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/Microsoft_Azure/S2E6_Is_Postgres_the_wave_of_the_future_—_The_Shift_Podcast___OBc1TyXH0WQ.md`

**215. [Voice of the MVP - Oracle AI Database@Azure](https://www.youtube.com/watch?v=-ZQx_b2lUCU)** — Microsoft Azure · 에이전트·개발도구 · US · 2026-04 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽
- 개요: 안녕, 비주, 잘 지내? 선행을 베푸는 것은 훌륭한 일입니다. 저희는 지금 시애틀에서 열리는 마이크로소프트 MVP 서밋에 참석 중인데, 저는 이번이 첫 참석입니다. 그리고 [목을 가다듬고 코웃음을 치며] 아주 신났어요. 지금 우리는 마이크로소프트 스튜디오에 있습니다. 저희는 오라클 데이터베이스 Azure 제품의 일원이기 때문에, 특히 오라클 커뮤니티 여러분과 MVP 여정, 즉 가장 가치 있는…
- B1 디지털·AI 기술의 활용: 그래서 저는 그런 일을 하면서 동시에 커뮤니티와 함께 멀티 클라우드 환경에서 오라클을 사용하는 방법, 특히 마이크로소프트 애저에서 지연 시간이나 라이선스 비용 부담 없이 오라클을 사용하는 방법 등을 공유해 왔습니다.
- B4 가치네트워크·생태계: 우리가 Azure에서 Oracle을 사용하기 시작했을 당시에는 Azure 솔루션과 그와 같은 생태계는 존재하지도 않았습니다.
- 수치 주장: 그래서 지금 저희는 5,000개의 데이터베이스를 50개의 Exadata로 통합하고 있습니다.
- 교량: — · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Microsoft_Azure/Voice_of_the_MVP_-_Oracle_AI_Database@Azure__-ZQx_b2lUCU.md`

---

## Microsoft Developer


**216. [Build agents where work happens: chats channels and meetings in Microsoft Teams | DEM334](https://www.youtube.com/watch?v=Q9uv_y04rJE)** — Microsoft Developer · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요, 여러분. Build에 오신 것을 환영합니다. 와주셔서 정말 기쁩니다. 음, 시작하기 전에 간단한 질문 하나 드릴게요. 여러분 중 에이전트를 직접 만들어 본 경험이 있는 분이 몇 분이나 되시나요 ? 많은 분들이 손을 드셨네요. 에이전트를 구축 하고 채팅, 채널, 회의와 같은 협업 환경에 도입하려고 했을 때 상당한 어려움을 겪으셨을 거라고 생각합니다. 오늘 우리는 바로 그 점을 다루…
- B2 파괴: 소비자 행동·기대: 작년 Build 행사에서 저희는 스트리밍, 피드백 루프, 후속 조치 제안, 인용, 시작 프롬프트와 같은 다양한 에이전트 UX 기능을 포함하는 Teams AI 라이브러리를 발표했습니다.
- B8 부정 성과: 보안·프라이버시: 인간으로서 우리는 서로를 매우 신뢰하며, 에이전트에게도 동일한 수준의 신뢰와 개인정보 보호를 제공하고자 합니다.
- 수치 주장: 어제는 Teams CLI와 Teams 스킬에 대한 세션을 진행했는데, 25분도 채 안 되는 시간에 에이전트를 Teams에 통합하는 방법을 알려드렸습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Microsoft_Developer/Build_agents_where_work_happens_chats_channels_and_meetings___Q9uv_y04rJE.md`

**217. [Migrating VLDBs from Oracle to Azure Database for PostgreSQL | POSETTE: An Event for Postgres 2026](https://www.youtube.com/watch?v=i4mbsBs1wOE)** — Microsoft Developer · 에이전트·개발도구 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 저는 Adithya Kumaranchath입니다. Azure 데이터 제품 그룹의 수석 엔지니어링 아키텍트로 근무하고 있습니다. 오늘 발표에서는 대규모 Oracle 데이터베이스를 Azure Database for PostgreSQL로 마이그레이션하는 방법에 대해 이야기하겠습니다 . 의사 결정권자이시거나 Azure PostgreSQL로 마이그레이션을 고려하고 계신 분이라면 이 발표가…
- B7 성과: 운영효율: 예를 들어, 고객이 Oracle 워크로드를 실행하는 경우 PostgreSQL 라이선스 비용을 절약할 수 있으므로 당연히 비용이 절감됩니다 .
- B1 디지털·AI 기술의 활용: 데이터 로딩은 Azure Data Factory와 같은 Azure 자체 서비스 기반 클라우드 ETL 도구를 사용 하거나, Striim과 같은 병렬 데이터 로딩 도구를 사용할 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Microsoft_Developer/Migrating_VLDBs_from_Oracle_to_Azure_Database_for_PostgreSQL__i4mbsBs1wOE.md`

---

## Mistral AI


**218. [Building custom code models for Ericsson proprietary silicon | AI Now Summit 2026](https://www.youtube.com/watch?v=ArWG4pmTXPQ)** — Mistral AI · 파운데이션 모델 · FR · 2026-07 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: Thank you so much. First of all, I'd like to just say I'm honored to be here talking about this in front of a very knowledgeable audience. It's just amazing. So, my name is Fredrik Olofsson. I'm generative AI lead at Eri…
- B1 디지털·AI 기술의 활용: Uh so, we need to expand the current existing code base into more variants so that the LLM during training would fully comprehend all the patterns it need to learn.
- B7 성과: 조직성과: So, we for for now having developers that actually are using it, mostly for testing and evaluation, but slowly ramping towards actual production use.
- 수치 주장: Uh but in general, I would say the workload that we put here is like 80% working to harvest and build data.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Mistral_AI/Building_custom_code_models_for_Ericsson_proprietary_silicon__ArWG4pmTXPQ.md`

**219. [Domain AI models fine-tuned with proprietary knowledge | AI Now Summit 2026](https://www.youtube.com/watch?v=7evOiuXFkQo)** — Mistral AI · 파운데이션 모델 · FR · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽
- 개요: 안녕하세요 여러분. 저는 기눌 샤입니다. 저는 데이터 과학자입니다. 저는 CUE 40 CS에서 고급 분석 업무를 총괄하고 있습니다. 안녕하세요, 저는 라시드 부제마이입니다. 저는 프랑스에 거주하고 있습니다 . 저는 주로 프랑스에서 고객에게 AI 관련 자문을 제공 하고 AI 솔루션을 구현하는 업무를 총괄하고 있습니다 . 오늘은 바로 직전 시간에 말씀하셨던 내용에 대해 이야기해 보려고 합니다. …
- B8 부정 성과: 보안·프라이버시: 하지만 사업을 운영하는 방식, 특히 사업 관련 의사 결정을 내리는 방식을 생각해 보면 , 회사의 정체성과 차별점을 만드는 많은 요소들이 있다는 것을 알게 될 것입니다.
- B4 가치네트워크·생태계: 우리는 고객의 독점 데이터 생태계를 활용하고 세밀 조정 프레임워크를 사용하여 해당 모델을 변환하고 도메인 AI 모델을 생성합니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Mistral_AI/Domain_AI_models_fine-tuned_with_proprietary_knowledge_AI_No__7evOiuXFkQo.md`

**220. [Luxembourg's sovereign AI playbook for Europe | AI Now Summit 2026](https://www.youtube.com/watch?v=0lqZpQZLGKs)** — Mistral AI · 파운데이션 모델 · FR · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 저는 여전히 파트너입니다. AI 생태계. 기술적 매력 조건. 안녕하세요 여러분. 저희는 오늘 로마와 케빈과 함께 이 자리에 있게 되어 정말 기쁩니다. 오늘은 룩셈부르크가 미스트랄(Mistral)을 통해 어떻게 자체적인 AI 시스템을 구축하고 있는지, 그리고 이 시스템이 어떤 모습인지, 20개 부처와 150개 행정기관으로 구성된 60만 명 이상의 시민에게 서비스를 제공하는 정부 전체에 걸쳐 이…
- B4 가치네트워크·생태계: 기술적인 측면에서 우리는 선택의 여지가 없기 때문에 우리가 개발 중인 모든 새로운 모델 과 모든 새로운 기술을 온 프레미스 및 생태계에 계속해서 도입해야 합니다.
- B1 디지털·AI 기술의 활용: 방대한 법률 용어인 LLM( 법률 문서)을 사용하면 가능하겠지만, 이는 곧 국가 주권과 직결되는 문제라는 것을 깨달았습니다.
- 수치 주장: 오늘은 룩셈부르크가 미스트랄(Mistral)을 통해 어떻게 자체적인 AI 시스템을 구축하고 있는지, 그리고 이 시스템이 어떤 모습인지, 20개 부처와 150개 행정기관으로 구성된 60만 명 이상의 시민에게 서비스를 제공하는 정부 전체에 걸쳐 이를 운영하고 확장하는 데 필요한 기본 요건에 대해 논의해 보겠습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Mistral_AI/Luxembourg's_sovereign_AI_playbook_for_Europe_AI_Now_Summit___0lqZpQZLGKs.md`

**221. [The AI sovereignty paradox: Scalable ecosystems for trusted AI adoption | AI Now Summit 2026](https://www.youtube.com/watch?v=xP-3iMTPav0)** — Mistral AI · 파운데이션 모델 · FR · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 여러분, 안녕하세요. 안녕하세요, 저는 한입니다. 저는 미스트랄 출신으로, 파트너 솔루션 아키텍트이자 미스트랄 소속입니다. 오늘 이렇게 아말 씨 와 함께하게 되어 정말 기쁩니다 . 그러니 제발 아말 씨. 저도 여기에 오게 되어 정말 기쁩니다. 미스트랄이 주최하는 행사에 참석하게 되어 정말 기쁩니다. 이번이 첫 행사인데 정말 신나고 기대되네요 . 그리고 제가 여러분과 함께 이 자리에 있다는 것…
- B4 가치네트워크·생태계: 그래서 NTT DATA, Mistral, 그리고 Amol과 함께하는 이번 파트너십의 핵심은 풀스택 기술을 제공하고 AI 스튜디오를 플랫폼으로 활용하여 AI 애플리케이션을 개발할 수 있도록 지원하는 것입니다.
- B1 디지털·AI 기술의 활용: 그러니까 하이브리드 방식이라는 건, 저희가 고객들에게 하이퍼스케일러나 클라우드 솔루션을 버리라고 권하는 게 아니라는 뜻입니다.
- 수치 주장: 음, 양자 컴퓨팅 의 발전 과정을 알고 계신지 모르겠지만, 100만 개의 큐비트로 구성되어 실제로 암호 해독 알고리즘을 뚫을 수 있는 차세대 양자 컴퓨터가 곧 출시될 예정입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Mistral_AI/The_AI_sovereignty_paradox_Scalable_ecosystems_for_trusted_A__xP-3iMTPav0.md`

---

## NAVER Cloud


**222. [[Brown-Bag 런치세미나] 공공을 위한 클라우드 상품](https://www.youtube.com/watch?v=52qSYsUFIkw)** — NAVER Cloud · 파운데이션 모델 · KR · 2023-10 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 네이버 클라우드의 김여진 있니다 올해 정부에서 공공 클라우드에 대한 계정을 발표를 하였고 이에 대한 지침들이 많이 나왔기 때문에 오늘 10월 브라운 백에 참석해 주신 분들은 아마도 앞으로 공공에서는 어떻게 클라우드를 적용해야 하는지 관심을 갖고 참석을 해 주신 거 같습니다 그래서 오늘은 공공을 위한 클라우드 상품이라는 주제로 여러분들에게 지금까지의 공 클라우드와 앞으로의 공공 클라…
- B1 디지털·AI 기술의 활용: 안녕하세요 네이버 클라우드의 김여진 있니다 올해 정부에서 공공 클라우드에 대한 계정을 발표를 하였고 이에 대한 지침들이 많이 나왔기 때문에 오늘 10월 브라운 백에 참석해 주신 분들은 아마도 앞으로 공공에서는 어떻게 클라우드를 적용해야 하는지 관심을 갖고 참석을 해 주신 거 같습니다 그래서 오늘은 공공을 위한 클라우드 상품이라는 주제로 여러분들에게 지금까지의 공 클라우드와 앞으로의 공공 클라우드에 대해서 공유드리려고 합니다 오늘 목차는 공공부문 클라우드 관련 법…
- B8 부정 성과: 보안·프라이버시: 안녕하세요 네이버 클라우드의 김여진 있니다 올해 정부에서 공공 클라우드에 대한 계정을 발표를 하였고 이에 대한 지침들이 많이 나왔기 때문에 오늘 10월 브라운 백에 참석해 주신 분들은 아마도 앞으로 공공에서는 어떻게 클라우드를 적용해야 하는지 관심을 갖고 참석을 해 주신 거 같습니다 그래서 오늘은 공공을 위한 클라우드 상품이라는 주제로 여러분들에게 지금까지의 공 클라우드와 앞으로의 공공 클라우드에 대해서 공유드리려고 합니다 오늘 목차는 공공부문 클라우드 관련 법…
- 수치 주장: 안녕하세요 네이버 클라우드의 김여진 있니다 올해 정부에서 공공 클라우드에 대한 계정을 발표를 하였고 이에 대한 지침들이 많이 나왔기 때문에 오늘 10월 브라운 백에 참석해 주신 분들은 아마도 앞으로 공공에서는 어떻게 클라우드를 적용해야 하는지 관심을 갖고 참석을 해 주신 거 같습니다 그래서 오늘은 공공을 위한 클라우드 상품이라는 주제로 여러분들에게 지금까지의 공 클라우드와 앞으로의 공공 클라우드에 대해서 공유드리려고 합니다 오늘 목차는 공공부문 클라우드 관련 법…
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/NAVER_Cloud/[Brown-Bag_런치세미나]_공공을_위한_클라우드_상품__52qSYsUFIkw.md`

**223. [[Solutions Showcase] Java 유료화와 성능 고민! Azul로 한 방에 해결하세요.](https://www.youtube.com/watch?v=EV2nN5ZHNrs)** — NAVER Cloud · 파운데이션 모델 · KR · 2023-11 · ko · 5/8블록 · `off_topic`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요 네이버 클라우드의 김세현입니다 네이버 클라우드 플랫폼의 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스 지금부터 시작해 보도록 하겠습니다 오늘은 2023년의 마지막 솔루션 쇼케이스인 올해 마지막 솔루션으로 아줄 시스템에 대해서 준비해 보았습니다 오늘의 솔루션은 아줄 시스템즈의 한국 사업을 총괄하고 계시는 권범준 대표님이 소개해 주시겠습니다네 대표님 시청자분들께 인사 부탁드…
- B1 디지털·AI 기술의 활용: [음악] 안녕하세요 네이버 클라우드의 김세현입니다 네이버 클라우드 플랫폼의 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스 지금부터 시작해 보도록 하겠습니다 오늘은 2023년의 마지막 솔루션 쇼케이스인 올해 마지막 솔루션으로 아줄 시스템에 대해서 준비해 보았습니다 오늘의 솔루션은 아줄 시스템즈의 한국 사업을 총괄하고 계시는 권범준 대표님이 소개해 주시겠습니다네 대표님 시청자분들께 인사 부탁드립니다 예 안녕하세요 저는 미국 자바 전문 기업인 아줄 시스템즈의 한국 …
- B8 부정 성과: 보안·프라이버시: [음악] 안녕하세요 네이버 클라우드의 김세현입니다 네이버 클라우드 플랫폼의 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스 지금부터 시작해 보도록 하겠습니다 오늘은 2023년의 마지막 솔루션 쇼케이스인 올해 마지막 솔루션으로 아줄 시스템에 대해서 준비해 보았습니다 오늘의 솔루션은 아줄 시스템즈의 한국 사업을 총괄하고 계시는 권범준 대표님이 소개해 주시겠습니다네 대표님 시청자분들께 인사 부탁드립니다 예 안녕하세요 저는 미국 자바 전문 기업인 아줄 시스템즈의 한국 …
- 수치 주장: [음악] 안녕하세요 네이버 클라우드의 김세현입니다 네이버 클라우드 플랫폼의 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스 지금부터 시작해 보도록 하겠습니다 오늘은 2023년의 마지막 솔루션 쇼케이스인 올해 마지막 솔루션으로 아줄 시스템에 대해서 준비해 보았습니다 오늘의 솔루션은 아줄 시스템즈의 한국 사업을 총괄하고 계시는 권범준 대표님이 소개해 주시겠습니다네 대표님 시청자분들께 인사 부탁드립니다 예 안녕하세요 저는 미국 자바 전문 기업인 아줄 시스템즈의 한국 …
- 교량: — · 기술: —
- 원문: `transcripts/channels/NAVER_Cloud/[Solutions_Showcase]_Java_유료화와_성능_고민!_Azul로_한___EV2nN5ZHNrs.md`

**224. [[Solution showcase] 자유롭고 유연한 커스텀 환경으로 차별화된 이커머스 구축](https://www.youtube.com/watch?v=J4BsujJyTBo)** — NAVER Cloud · 파운데이션 모델 · KR · 2024-03 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 웨비나 진행을 맡은 네이버 클라우드의 김여진 있니다 오늘 웨비나는 네이버 클라우드 플랫폼에 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스를 시 시작해 볼까 합니다 이번 솔루션 쇼케이스는 포비즈 코리아의 이커머스 솔루션에 대해서 알아보려고 하는데요 오늘의 솔루션을 소개해 드릴 전문가분의 모셨습니다 포비즈 코리아의 김경숙 부문장 있니다 부문장인 웨비나 시청자분들께 인사 부탁…
- B4 디지털 채널: [음악] 안녕하세요 웨비나 진행을 맡은 네이버 클라우드의 김여진 있니다 오늘 웨비나는 네이버 클라우드 플랫폼에 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스를 시 시작해 볼까 합니다 이번 솔루션 쇼케이스는 포비즈 코리아의 이커머스 솔루션에 대해서 알아보려고 하는데요 오늘의 솔루션을 소개해 드릴 전문가분의 모셨습니다 포비즈 코리아의 김경숙 부문장 있니다 부문장인 웨비나 시청자분들께 인사 부탁드리겠습니다네 안녕하세요 포비즈코리아 플랫폼 사업본부의 김경식입니다 전 …
- B1 디지털·AI 기술의 활용: [음악] 안녕하세요 웨비나 진행을 맡은 네이버 클라우드의 김여진 있니다 오늘 웨비나는 네이버 클라우드 플랫폼에 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스를 시 시작해 볼까 합니다 이번 솔루션 쇼케이스는 포비즈 코리아의 이커머스 솔루션에 대해서 알아보려고 하는데요 오늘의 솔루션을 소개해 드릴 전문가분의 모셨습니다 포비즈 코리아의 김경숙 부문장 있니다 부문장인 웨비나 시청자분들께 인사 부탁드리겠습니다네 안녕하세요 포비즈코리아 플랫폼 사업본부의 김경식입니다 전 …
- 수치 주장: [음악] 안녕하세요 웨비나 진행을 맡은 네이버 클라우드의 김여진 있니다 오늘 웨비나는 네이버 클라우드 플랫폼에 인기 있는 솔루션을 소개해드리는 솔루션 쇼케이스를 시 시작해 볼까 합니다 이번 솔루션 쇼케이스는 포비즈 코리아의 이커머스 솔루션에 대해서 알아보려고 하는데요 오늘의 솔루션을 소개해 드릴 전문가분의 모셨습니다 포비즈 코리아의 김경숙 부문장 있니다 부문장인 웨비나 시청자분들께 인사 부탁드리겠습니다네 안녕하세요 포비즈코리아 플랫폼 사업본부의 김경식입니다 전 …
- 교량: — · 기술: —
- 원문: `transcripts/channels/NAVER_Cloud/[Solution_showcase]_자유롭고_유연한_커스텀_환경으로_차별화된_이커머스_구축__J4BsujJyTBo.md`

**225. [[Brown-Bag 런치세미나] 2024년 보안트렌드 살펴보기](https://www.youtube.com/watch?v=6OUSU8wzvac)** — NAVER Cloud · 파운데이션 모델 · KR · 2024-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 백 점심 세미나 2024년 보안 트렌드 살펴 보기라는 주제로 발표할 네이버클라우드 예원입니다 이번 세미나를 통해 2024년을 시작하며 최심 사이버 보안 트렌드는 어떤 방향으로 흘러가고 있는가에 대해 소개해 드리고자 합니다 보과 관련된 직무나 업무적 연관성이 없으셨던 분들께서도 쉽게 이해하면 수 있도록 준비하였습니다 요즘 주목받고 있는 보안 트렌드는 어떤 것이 있고 그러한 트렌드에 맞춰 어떤 …
- B1 디지털·AI 기술의 활용: 백 점심 세미나 2024년 보안 트렌드 살펴 보기라는 주제로 발표할 네이버클라우드 예원입니다 이번 세미나를 통해 2024년을 시작하며 최심 사이버 보안 트렌드는 어떤 방향으로 흘러가고 있는가에 대해 소개해 드리고자 합니다 보과 관련된 직무나 업무적 연관성이 없으셨던 분들께서도 쉽게 이해하면 수 있도록 준비하였습니다 요즘 주목받고 있는 보안 트렌드는 어떤 것이 있고 그러한 트렌드에 맞춰 어떤 아키텍처를 구성해야 하는지 주요 주제별로 말씀드리겠습니다 목차는 다음과 …
- B8 부정 성과: 보안·프라이버시: 백 점심 세미나 2024년 보안 트렌드 살펴 보기라는 주제로 발표할 네이버클라우드 예원입니다 이번 세미나를 통해 2024년을 시작하며 최심 사이버 보안 트렌드는 어떤 방향으로 흘러가고 있는가에 대해 소개해 드리고자 합니다 보과 관련된 직무나 업무적 연관성이 없으셨던 분들께서도 쉽게 이해하면 수 있도록 준비하였습니다 요즘 주목받고 있는 보안 트렌드는 어떤 것이 있고 그러한 트렌드에 맞춰 어떤 아키텍처를 구성해야 하는지 주요 주제별로 말씀드리겠습니다 목차는 다음과 …
- 수치 주장: 백 점심 세미나 2024년 보안 트렌드 살펴 보기라는 주제로 발표할 네이버클라우드 예원입니다 이번 세미나를 통해 2024년을 시작하며 최심 사이버 보안 트렌드는 어떤 방향으로 흘러가고 있는가에 대해 소개해 드리고자 합니다 보과 관련된 직무나 업무적 연관성이 없으셨던 분들께서도 쉽게 이해하면 수 있도록 준비하였습니다 요즘 주목받고 있는 보안 트렌드는 어떤 것이 있고 그러한 트렌드에 맞춰 어떤 아키텍처를 구성해야 하는지 주요 주제별로 말씀드리겠습니다 목차는 다음과 …
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/NAVER_Cloud/[Brown-Bag_런치세미나]_2024년_보안트렌드_살펴보기__6OUSU8wzvac.md`

**226. [AI 개발, 어디까지 해보셨어요? 네이버클라우드와 함께한 AI 포텐데이 기술밋업](https://www.youtube.com/watch?v=y0Plw95FAnM)** — NAVER Cloud · 파운데이션 모델 · KR · 2025-03 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요. AI 포텐데이 기술 미업 시작하도록 하겠습니다. 포텐데이는 2월 21일부터 3월까지 10일간의 해커동 과정을 거쳐서 네이버 클라우드와 함께하는 포텐데에서 진행이 되는 고도화트랙이라는 10일간의 추가 서비스 개발 기간이 있었고요. 그다음에 결선 다섯 개 팀이 진행한 데모데이 발표에 다음에 마지막으로 오늘 기술 미드업이 있습니다. 총 거의 한 달 조금 넘는 시간 동안 저희 여정을 함…
- B1 디지털·AI 기술의 활용: 이 이 모든 기회를 만들어 주신 빗사이드와 네이버 클라우드 그리고 함께 고생 고생한 팀원들에게 정말 감사하다고 말씀드리고 싶고 그리고 많은 인사이트를 공유해 주신 오늘 발표를 해 주실 거고 그리고 여태까지 모든 프로젝트를 만들어 주신 모든 분께 감사드립니다.
- B2 파괴: 소비자 행동·기대: 이제 AI와 인간이 어떻게 공존할 수 있을지 그리고 UX 디자인이 AI 시대에서 어떤 역할을 해야 하는지 되게 깊이 고민을 하게 되었어요.
- 수치 주장: 포텐데이는 2월 21일부터 3월까지 10일간의 해커동 과정을 거쳐서 네이버 클라우드와 함께하는 포텐데에서 진행이 되는 고도화트랙이라는 10일간의 추가 서비스 개발 기간이 있었고요.
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/NAVER_Cloud/AI_개발,_어디까지_해보셨어요_네이버클라우드와_함께한_AI_포텐데이_기술밋업__y0Plw95FAnM.md`

---

## NVIDIA


**227. [NVIDIA & Lilly: The AI Revolution in Drug Discovery | Jensen Huang & David Ricks](https://www.youtube.com/watch?v=zbiEYMapsvw)** — NVIDIA · 인프라·칩·전력 · US · 2026-02 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [박수] 안녕하세요. 여러분 모두를 만나서 정말 반갑습니다. 아시다시피 , 저는 일 년에 한 번 여러분 모두가 하시는 놀라운 일에 대해 감사를 표할 수 있는 기회를 갖습니다 . 아시다시피, 저희는 가속 컴퓨팅이라는 새로운 컴퓨팅 방식을 개척했습니다. 저희는 이 일을 33년 동안 해왔습니다. 핵심 아이디어는 공동 설계, 즉 해결하려는 문제를 이해하고 알고리즘, 컴퓨터 및 프로세서를 포함한 전체…
- B4 가치네트워크·생태계: 그리고 우리 둘은 세계 최대의 컴퓨터 회사이자 세계 최대의 컴퓨터 과학 회사가 세계 최대의 생명 과학 회사와 파트너십을 맺으면 정말 멋질 거라고 생각했습니다.
- B2 파괴: 데이터 가용성: 그리고 정말 흥미로운 분야 중 하나는, 우리가 모델을 훈련시키고, 단백질이나 화학 물질을 합성하고, 로봇 공학 연구실에 넣고, 더 많은 데이터를 수집하고, 그 데이터를 다시 모델에 입력하는 것입니다.
- 수치 주장: 제 생각에는 앞으로 10년 안에 생산되는 거의 모든 자동차에 로보 택시 기능이 탑재되거나, 직접 운전하는 것도 가능 하지만 로보택시로 활용할 수 있는 기능이 추가될 것이라고 확신합니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/NVIDIA/NVIDIA_&_Lilly_The_AI_Revolution_in_Drug_Discovery_Jensen_Hu__zbiEYMapsvw.md`

**228. [NVIDIA GTC Telecom Special Address: The AI Grid—Intelligently Connecting AI Infrastructure](https://www.youtube.com/watch?v=cxiOhp9BJTs)** — NVIDIA · 인프라·칩·전력 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요 여러분, 카니카가 말했듯이 GTC 둘째 날에 오신 것을 환영합니다. 곧 놀라운 통신 관련 발표 일정이 시작될 예정입니다. 오늘 제가 하려고 하는 것은 인프라 구축이라는 매우 흥미로운 분야들을 맥락 속에서 살펴보는 것입니다. 어제 우리는 업계를 선도하는 가장 흥미로우면서도 기술적으로 가장 진보된 인프라를 목격했습니다. 통신업계도 이러한 흐름에서 뒤처져서는 안 됩니다 . 인공지능 혁명…
- B1 디지털·AI 기술의 활용: 이제 AT&amp;T, 시스코, 엔비디아가 협력하여 이러한 IoT 네트워크를 IoIT 네트워크, 즉 지능형 사물 인터넷으로 전환하고 있습니다.
- B4 가치네트워크·생태계: 각 파트너사는 자사 비즈니스를 위한 AI 그리드라는 개념을 빠르게 수용했으며, 이제는 자사뿐만 아니라 협력하는 파트너사들이 전체 애플리케이션이나 오케스트레이션 레이어를 이 참조 아키텍처를 통해 통합함으로써 얻을 수 있는 기회까지 창출했습니다.
- 수치 주장: 인공지능 혁명이 시작된 지 3년이 지난 지금, 우리는 IT 인프라를 비롯한 대규모 인프라 구축을 목격하고 있습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/NVIDIA/NVIDIA_GTC_Telecom_Special_Address_The_AI_Grid—Intelligently__cxiOhp9BJTs.md`

**229. [Think You Know AI? 25 Startups Prove You Wrong](https://www.youtube.com/watch?v=D1x8ewtJAa0)** — NVIDIA · 인프라·칩·전력 · US · 2026-04 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 환영. 여러분, 환영합니다. 음, 이거 재밌겠네요. 먼저 질문 하나 드리겠습니다. 인공지능이라고 하면 가장 먼저 무엇이 떠오르시나요 ? 청중 여러분 대부분에게는 아마도 챗봇이나 즐겨 사용하는 AI 코딩 도우미, 또는 생산성 향상을 위해 활용하고 있는 여러 AI 에이전트 중 하나일 것입니다 . 요즘에는 OpenClaw나 NemoClaw 같은 프로그램도 있을 수 있습니다. 그리고 이 도구들은 정…
- B1 디지털·AI 기술의 활용: 청중 여러분 대부분에게는 아마도 챗봇이나 즐겨 사용하는 AI 코딩 도우미, 또는 생산성 향상을 위해 활용하고 있는 여러 AI 에이전트 중 하나일 것입니다 .
- B7 성과: 사회적 편익: 그러면 기존의 기상 예보 방식이 미흡하거나, 특히 인구 밀집 지역을 위협하는 재난을 예측하는 데 어려움을 겪었던 부분을 보완하는 데 도움이 됩니다.
- 수치 주장: 그렇다면 21세기에 인구가 더욱 증가하는 상황에서, 어떻게 100억 명의 인구를 먹여 살리는 동시에 세계 기아 문제도 해결할 수 있을까요?
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/NVIDIA/Think_You_Know_AI_25_Startups_Prove_You_Wrong__D1x8ewtJAa0.md`

**230. [Inside Instacart's AI-Powered Smart Shopping Cart | NVIDIA AI Podcast Ep. 302](https://www.youtube.com/watch?v=Alz-bhXqyXM)** — NVIDIA · 인프라·칩·전력 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 저희는 5~10년 후에는 고객들이 매장에서 쇼핑할지 온라인에서 쇼핑할지 고민할 필요가 없을 것이라고 생각합니다. 이는 매장, 온라인, 진열 상태 등에서 고객의 행동을 종합적으로 고려하여 완벽하게 개인화된 음악 경험을 구축하는, 지속적으로 음악 학습을 하는 AI 시스템에 의해 구동되는 단일 통합 모드가 될 것입니다. NVIDIA AI 팟캐스트에 오신 것을 환영합니다. 오늘 저희 스튜디오에 오신…
- B2 파괴: 소비자 행동·기대: 이처럼 인공지능을 활용하여 고객 에게 더욱 편리하고 개인화된 경험을 제공하면 고객 행동 방식에 2차, 3차적인 파급 효과가 나타나는 사례를 많이 볼 수 있습니다.
- B1 디지털·AI 기술의 활용: 그래서, 우리가 지금까지 이야기해 온 모든 것들이 소비자들에게 매우 분명하게 드러나고 있고, 완전히 새로운 사용 사례들도 있지만, AI가 엣지와 클라우드에 미치는 영향을 생각해 보면, 그 영향은 정말 광범위합니다.
- 수치 주장: 저희는 웨이크펀 전체 매장의 약 20%에서 서비스를 제공하고 있으며, 그 비중이 빠르게 증가하고 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA/Inside_Instacart's_AI-Powered_Smart_Shopping_Cart_NVIDIA_AI___Alz-bhXqyXM.md`

**231. [NVIDIA & Coherent: Reindustrializing America, Manufacturing for the AI Era](https://www.youtube.com/watch?v=GsqW5MPFajw)** — NVIDIA · 인프라·칩·전력 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [박수] 모두 환영합니다. 환영. 오늘 이 자리에 함께해 주셔서 정말 감사합니다. 저희는 이 행사를 정말 기대해 왔습니다 . 저희는 이 행사를 오랫동안 계획해 왔습니다. 저희는 이 사업장과 모든 직원들을 매우 자랑스럽게 생각합니다. 오늘 오후 셔먼에서 저희와 함께 시간을 보내주셔서 감사합니다. 정말 감사드립니다. 시작하기 전에, 오늘 이 자리를 가능하게 해주신 몇몇 지도자분들과 파트너분들께 …
- B4 가치네트워크·생태계: 엔비디아의 코히런트 전략적 파트너십 투자, 텍사스 주와 SEDCO의 지원, 그리고 오늘 아침 발표된 5천만 달러 규모의 칩 지원금 등 우리가 진행하고 있는 이러한 모든 투자는 미국의 핵심 AI 인프라 구축 능력, 국내 제조 역량 확대, 일자리 창출, 그리고 전반적인 기술 리더십 강화에 기여하고 있습니다.
- B7 성과: 사회적 편익: 엔비디아의 코히런트 전략적 파트너십 투자, 텍사스 주와 SEDCO의 지원, 그리고 오늘 아침 발표된 5천만 달러 규모의 칩 지원금 등 우리가 진행하고 있는 이러한 모든 투자는 미국의 핵심 AI 인프라 구축 능력, 국내 제조 역량 확대, 일자리 창출, 그리고 전반적인 기술 리더십 강화에 기여하고 있습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/NVIDIA/NVIDIA_&_Coherent_Reindustrializing_America,_Manufacturing_f__GsqW5MPFajw.md`

**232. [How NVIDIA Runs Its Own AI Factory | AI Factory Insider Ep. 2](https://www.youtube.com/watch?v=Jpsq_-1kJTo)** — NVIDIA · 인프라·칩·전력 · US · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: AI 팩토리 인사이더 두 번째 에피소드에 오신 것을 환영합니다 . 저는 카우시크 셰티입니다. 지난 회에서 우리는 이 시리즈의 기반을 다졌습니다 . 우리는 주로 하드웨어에 초점을 맞춘 엔터프라이즈 참조 아키텍처에 대해 이야기했고, 엔터프라이즈 AI 팩토리가 무엇인지 명확하게 정의했습니다. 다음 30분 동안 두 가지 중요한 주제를 다루겠습니다. 이제 한 단계 더 나아가 소프트웨어와 기업에서 검증…
- B1 디지털·AI 기술의 활용: 이는 사람들이 SaaS 형태로 무엇을 소비하고 싶은지 , 클라우드 계정 내에서 무엇을 소비하고 싶은지, 그리고 온프레미스에 풀 스택을 구축하여 소유하고 운영하고 싶은지에 대한 관점을 실제로 바꿀 수 있습니다.
- B7 성과: 운영효율: 티켓 처리 지연 방지 활용 사례의 가장 큰 장점은 AI가 먼저 처리했기 때문에 더 이상 티켓을 닫을 필요가 없어진 고객 지원 엔지니어들의 작업 시간을 절약할 수 있다는 점에서 투자 수익률(ROI)을 측정할 수 있다는 것입니다 .
- 수치 주장: 네, 아시다시피 저희는 약 1년 전에 엔터프라이즈 AI 팩토리를 출시했고, 다양한 동기를 가진 엔터프라이즈 파트너들이 저희의 발자취를 따라 자체 AI 컴퓨팅 환경을 구축하는 여정에 동참하고 있습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/NVIDIA/How_NVIDIA_Runs_Its_Own_AI_Factory_AI_Factory_Insider_Ep._2__Jpsq_-1kJTo.md`

---

## NVIDIA Developer


**233. [Prepare for Your NVIDIA Certification Exam](https://www.youtube.com/watch?v=Kd3nbaMZy8k)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요, 엔비디아 인증 웨비나에 오신 여러분을 환영합니다. 곧 시작하겠지만, 모두가 저희의 목소리와 모습을 잘 듣고 계실 수 있도록 먼저 안내드리겠습니다. 기술적인 문제가 있으시면 Q&amp;A 창을 이용해 주시면 기꺼이 도와드리겠습니다. 본격적인 토론에 앞서 몇 가지 안내 사항을 말씀드리겠습니다. 발표 중 질문이 있으시면 언제든지 Q&amp;A 창을 이용해 주세요. 이 프레젠테이션 자료…
- B5 직무·역량 변화: 이 시험을 개발할 때 소프트웨어 개발자, 소프트웨어 엔지니어, 솔루션 아키텍트, 데이터 과학자, 연구원을 염두에 두었지만, 이 자격증은 특정 직종에만 국한되지 않습니다.
- B1 디지털·AI 기술의 활용: AI, 머신러닝, 딥 러닝의 차이점을 알아야 하고, 특히 NVIDIA의 AI 소프트웨어 및 솔루션에 대해 알아야 합니다.
- 수치 주장: 시험의 대부분은 핵심 머신러닝 및 AI 지식( 30%)을 다루며, 소프트웨어 개발(24%), 나머지 문제는 실험, 데이터 분석 및 시각화, 또는 신뢰할 수 있는 AI에 관한 것입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/NVIDIA_Developer/Prepare_for_Your_NVIDIA_Certification_Exam__Kd3nbaMZy8k.md`

**234. [A New Era for Generalist Robotics: The Rise of Humanoids | NVIDIA GTC 2025](https://www.youtube.com/watch?v=BmD22FNOAY4)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 · 빠짐: B3 전략 대응, B5 구조 변화, B7 긍정 성과, B8 부정 성과
- 개요: [박수] 안녕하세요. 안녕하세요. 와, 이 관중들 정말 멋지네요. 네, 매디슨이 방금 말했듯이 제 이름은 티파니 얀센이고 오늘 이 토론의 진행을 맡겠습니다. 제 소개를 간단히 하자면 , 저는 티펜 테크(Tiffen Tech)의 창립자입니다 . 여러분은 어떠신지 모르겠지만, 저는 이 패널 토론을 손꼽아 기다려왔습니다. 휴머노이드 로봇은 오랫동안 연구되어 왔으며, 최근 들어 많은 발전이 이루어졌…
- B1 디지털·AI 기술의 활용: 하지만 로봇공학 AI가 일반 언어 학습( LLM)이나 가상 언어 학습(VLM)과 다른 점은, LLM은 코딩이든 일반적인 글쓰기든 간에 문제를 거의 완벽하게 해결해야만 진정으로 유용해진다는 것입니다.
- B2 파괴: 데이터 가용성: 이 퍼즐의 모든 조각은 AI 플랫폼을 한 단계 끌어올리고, 데이터를 수집하는 새로운 방법을 찾고, 이전 구조의 모범 사례 와 작동 방식을 가져와 다음 단계로 나아가는 데 기여해 왔습니다.
- 수치 주장: 그리고 커뮤니티가 열정적이고 적극적으로 참여하며, 상업적 환경에서 가치를 제공하는 전문 로봇을 개발하는 것이 장기적인 목표라는 것을 인식한다면, 앞으로 1~2년 안에 그러한 목표를 달성할 수 있을 거라고 생각합니다.
- 교량: — · 기술: 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/A_New_Era_for_Generalist_Robotics_The_Rise_of_Humanoids_NVID__BmD22FNOAY4.md`

**235. [An Introduction to Building Humanoid Robots | NVIDIA GTC 2025](https://www.youtube.com/watch?v=Oyon1QDpU6g)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 오늘은 여러분을 위해 아주 흥미로운 세션을 준비했습니다. 음, 이건 어제 젠슨의 기조연설에서 보셨던 내용을 자세히 살펴보는 프리뷰입니다 . 음, 휴머노이드 로봇 제작에 대한 소개입니다. 오늘 정말 훌륭한 연사분들이 모셨습니다. 음 Jim Fan, 음 Yuka, 음 Leela 및 Yen. 네, 짐과 유카는 NVIDIA 장비 연구소 소속입니다. 옌은 저희 엔지니어링 팀의 리더이고, 릴라도 저희 …
- B1 디지털·AI 기술의 활용: 그리고 이러한 데이터를 활용하여 ISAC 클라우드에서 모방 학습과 강화 학습을 수행하여 사용 사례에 맞는 모빌리티 기반 모델을 구축하고, 가상 환경(예: INEX 또는 MEGA)에서 해당 모델을 테스트한 후 실제 로봇에도 배포할 수 있습니다.
- B4 가치네트워크·생태계: 저희는 엔지니어링 팀과 긴밀히 협력하여 Azac 및 Omniverse 생태계에 적용하고, 이를 커뮤니티 전체와 공유하여 로봇 공학이나 기타 목표 분야에서 풀 스택 AI 애플리케이션을 구축할 수 있도록 지원하고 있습니다.
- 수치 주장: 이는 지난 10년간 세계 30대 선진 경제국에서 증가한 구인 공고 수를 나타냅니다 .
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습 · 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/An_Introduction_to_Building_Humanoid_Robots_NVIDIA_GTC_2025__Oyon1QDpU6g.md`

**236. [Frontiers of AI and Computing: A Conversation With Yann LeCun and Bill Dally | NVIDIA GTC 2025](https://www.youtube.com/watch?v=eyrDM3A_YFc)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B6 장벽 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B7 긍정 성과
- 개요: 빌 돌리와 얀 라쿤을 환영해 주세요 . 안녕하세요 여러분. 음, 인공지능에 대해 잠깐 이야기 나눠보려고 합니다 . 부디 흥미롭게 읽으셨으면 좋겠습니다. 음, 얀, 지난 한 해 동안 인공지능 분야에서 흥미로운 일들이 많이 일어났어요. 지난 한 해 동안 가장 흥미로운 발전은 무엇이라고 생각하시나요 ? 음, 너무 많아서 셀 수도 없지만, 여러분 중 몇몇은 아마 놀라실 만한 사실 하나를 말씀드리겠습…
- B1 디지털·AI 기술의 활용: 그리고 제가 여러분께 말씀드려야 할 흥미로운 이야기가 하나 있는데요, 음, 2022년 가을, 아니, 2023년 가을에, 제 동료인 Meta의 동료들이 작은 팀을 만들어서 전체 과학 문헌을 기반으로 훈련된 LLM(Learning Leadership Model)을 개발했어요.
- B8 부정 성과: 보안·프라이버시: 음, 놀라운 점은 LLM과 다양한 딥페이크 기술 등이 수년 동안 존재해 왔음에도 불구하고, 이러한 공격을 탐지하고 차단하는 업무를 담당하는 우리 동료들이 생성형 콘텐츠 게시가 크게 증가하지 않았다고 말한다는 것입니다.
- 수치 주장: 그리고 제가 여러분께 말씀드려야 할 흥미로운 이야기가 하나 있는데요, 음, 2022년 가을, 아니, 2023년 가을에, 제 동료인 Meta의 동료들이 작은 팀을 만들어서 전체 과학 문헌을 기반으로 훈련된 LLM(Learning Leadership Model)을 개발했어요.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/NVIDIA_Developer/Frontiers_of_AI_and_Computing_A_Conversation_With_Yann_LeCun__eyrDM3A_YFc.md`

**237. [NVIDIA DGX Spark: Your Personal AI Supercomputer | NVIDIA GTC 2025 Session](https://www.youtube.com/watch?v=S_k69qXQ9w8)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 앨런 퍼거인을 소개하게 되어 기쁩니다 . 그는 엔비디아의 제품 마케팅 담당 이사이며, 프로젝트 디지트에 대해 이야기해 줄 예정입니다. 앨런에게 따뜻한 박수를 보내주세요. 고마워, 세피. 그리고 그 20 IU는 곧 나올 겁니다 . 공연 끝나고 드릴게요 . 음, 그러니까 지금이 목요일 오후라는 건 알아요. 늦었어요. 음, 몇 분이나 음료 마실 준비가 되셨나요? 그래요. 음, 저는 두어 잔 마실 …
- B1 디지털·AI 기술의 활용: 만약 당신이 클라우드 시간을 빌려서 소스 코드를 전부 거기에 올려놓고 모델을 학습시킨다면 기업들이 매우 불쾌해할 거라는 걸 알고 있어요, 그렇죠?
- B4 가치네트워크·생태계: 음, 파트너사들이 장기적으로 어떤 계획을 가지고 있는지, 그리고 어떤 방식으로 지원할 계획인지는 제가 말씀드릴 수 없지만, 저희의 계획은 대략 이렇습니다.
- 수치 주장: 프로젝트 디지츠는 2015년에 출시했던 디지츠 박스라는 시스템에 대한 오마주였습니다.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습 · 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/NVIDIA_DGX_Spark_Your_Personal_AI_Supercomputer_NVIDIA_GTC_2__S_k69qXQ9w8.md`

**238. [Quantum Computing: Where We Are and Where We’re Headed | NVIDIA GTC 2025 Fireside Chat](https://www.youtube.com/watch?v=9XB-LsfpvCU)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 열기. 열. [음악] 엔비디아 창립자 겸 CEO인 젠슨 웡, 무대에 오신 것을 환영합니다 . [음악] 좋은 아침입니다. 환영. GTC에서 처음으로 개최되는 양자 데이에 오신 것을 환영합니다 . 네, 이번 행사는 정말 특별한 행사가 될 거예요. 음, 아시다시피 저는 상장 기업의 CEO입니다. 종종 누군가 저에게 질문을 하는데, 대부분의 경우, 아니, 대부분의 경우, 저는 기준을 낮추려…
- B4 가치네트워크·생태계: 엄청나게 복잡한 컴퓨팅 , 라이브러리, 알고리즘, 모델들을 다루고 있지만, 우리는 마치 생태계와 산업에 깊이 통합되어 있는 것처럼 접근하며 , 그것들에 깊은 관심을 가지고 있습니다.
- B1 디지털·AI 기술의 활용: 그리고 오늘날 우리가 하고 있는 일들을 살펴보면, 양자 컴퓨터 자체 와 그 작동 방식에 대한 최적화를 구축하는 방법을 알아내기 위해 머신 러닝을 적용하고 있습니다.
- 수치 주장: 아시다시피, 이건 컴퓨팅 플랫폼을 구축한 사람, 즉 엔비디아를 만들고 CUDA를 개발해서 오늘날의 컴퓨팅 플랫폼으로 만든 사람에게서 나온 질문인데, 우리가 그 답을 내놓는 데 거의 20 년이 걸렸습니다.
- 교량: Avenue 1 동적역량 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/Quantum_Computing_Where_We_Are_and_Where_We’re_Headed_NVIDIA__9XB-LsfpvCU.md`

**239. [Accelerating Applications with Parallel Algorithms | CUDA C++ Class Part 1](https://www.youtube.com/watch?v=Sdjn9FOkhnA)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-11 · ko · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 엔비디아의 최신 CUDAT C++ 프로그래밍 강좌에 오신 것을 환영합니다 . 이 첫 번째 영상에서는 엔비디아의 최신 프로그래밍 도구를 사용하여 GPU에서 프로그래밍하는 방법을 배우게 됩니다. 이 영상은 CUDA 프로그래밍을 가르치는 더 큰 규모의 영상 시리즈의 일부입니다 . 두 번째 영상에서는 동기화 및 CUD 스트림을 사용하여 GPU의 잠재력을 최대한 활용하는 방법을 배우게 됩니다 . 세 …
- B2 파괴: 데이터 가용성: 반면 CPU는 지연 시간이 훨씬 낮아 데이터에 훨씬 빠르게 접근할 수 있지만 메모리 대역폭이 훨씬 낮아 GPU보다 초당 접근할 수 있는 데이터 양이 적습니다.
- B8 부정 성과: 보안·프라이버시: 그래서 이 코드가 훨씬 읽기 쉽고, 유지 관리하기 쉽고, 오류 발생 가능성이 적고, 깔끔하다는 것을 알 수 있습니다.
- 수치 주장: 그다음에는 전력 알고리즘 자체에 대해, 특히 GPU에서 어떻게 100배 속도 향상을 달성할 수 있는지에 대해 더 자세히 알아보겠습니다 .
- 교량: — · 기술: 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/Accelerating_Applications_with_Parallel_Algorithms_CUDA_C++___Sdjn9FOkhnA.md`

**240. [Open-Source AI 101: Enabling American Innovation | NVIDIA GTC D.C.](https://www.youtube.com/watch?v=VqIc2LJzZG0)** — NVIDIA Developer · 인프라·칩·전력 · US · 2025-12 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: I'd like to welcome the panel. We're going&nbsp; to start with Joseph Jacks, JJ. So JJ is the&nbsp;&nbsp; founder and general partner of OSS Capital. And&nbsp; since 2018, JJ has directed more than 40 rounds&nbsp;&nbsp; …
- B1 디지털·AI 기술의 활용: And I think the industry is able to&nbsp; discern that and quickly adopt the models that&nbsp;&nbsp; are more easily fine-tunable and customizable.
- B7 성과: 사회적 편익: If you take a&nbsp; look at healthcare, education—better healthcare,&nbsp;&nbsp; better education—tremendous public goods for&nbsp; the developing world, for example.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/NVIDIA_Developer/Open-Source_AI_101_Enabling_American_Innovation_NVIDIA_GTC_D__VqIc2LJzZG0.md`

**241. [Build Custom Large-Scale Generative AI Models | NVIDIA GTC](https://www.youtube.com/watch?v=npQMSpCA4Lo)** — NVIDIA Developer · 인프라·칩·전력 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 여러분. [박수] 네, 이곳에 오게 되어 매우 기쁩니다. 모두 감사합니다. 잉그리드와 비디아, 이렇게 초대해 주셔서 감사합니다 . 저희는 엔비디아와 아주 오랫동안, 정확히는 모르겠지만 10년도 더 전부터 파트너 관계를 유지해 왔습니다. 그 시작은 우리가 그들과 긴밀히 협력하여 우리의 모든 주력 데스크톱 도구를 그들의 클라이언트 측 하드웨어에서 실행되도록 최적화하는 것이었습니다. …
- B2 파괴: 데이터 가용성: 저희의 첫 번째 학습 루프 버전은 일반적인 머신과 표준 이더넷 백본에서 실행되었는데, 이는 훌륭한 작업이었지만 수천 개의 GPU 사이에서 페타바이트 규모의 데이터를 수백만 번씩 주고받아야 하므로 네트워크 속도가 정말 중요해졌습니다.
- B8 부정 성과: 보안·프라이버시: 두 번째로 우리가 한 일은 훈련 인프라를 훨씬 더 똑똑하게 만들어 전체 프로세스에서 오류가 발생했을 때뿐만 아니라 개별 기계에서 오류가 발생했을 때도 이를 감지할 수 있도록 한 것입니다.
- 수치 주장: 그리고 아시다시피, 2022년 중반에서 후반쯤에 최종 사용자가 실제로 활용할 수 있는 실질적인 결과를 제공하는 최초의 상용 모델들이 출시되기 시작했습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/NVIDIA_Developer/Build_Custom_Large-Scale_Generative_AI_Models_NVIDIA_GTC__npQMSpCA4Lo.md`

**242. [Practical Context Engineering: Eliminate Bugs with High-Signal AI Code Reviews | NVIDIA GTC](https://www.youtube.com/watch?v=Kz-i33toG2g)** — NVIDIA Developer · 인프라·칩·전력 · US · 2026-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 매우 감사합니다. [박수] 네, 그래서 코딩은 확실히 지금 이 시점에서 가장 많이 활용되고 있는 주요 사례 중 하나라고 할 수 있겠습니다 . 지금까지 코드를 생성하는 시스템을 전혀 사용하지 않은 사람이 있었는지 모르겠지만, 이제는 모든 사람들이, 정말 모든 사람들이 어떤 수준에서든 코드를 생성하고 있습니다. 그래서 당연히 그런 상황이 발생하면 코드 리뷰는 훨씬 더 중요해지겠죠 ? 우리는 지금…
- B7 성과: 운영효율: 음, 그러니까 첫 코드 리뷰까지 걸리는 시간이 50% 단축되고 , 월별 PR 수는 36% 증가했으며, 병합 시간은 50% 단축되고, 강제 병합 횟수는 60% 감소했습니다.
- B8 부정 성과: 보안·프라이버시: [코웃음] 그러니까 이런 모든 것들, 즉 보안 문제를 찾아내는 것은 장기적으로 잠재적인 문제와 데이터 유출을 막는 데 큰 도움이 됩니다.
- 수치 주장: [코웃음] 사람들이 다시 빠른 속도로 기능을 출시하면서 풀 리퀘스트 수가 30% 증가했어.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/NVIDIA_Developer/Practical_Context_Engineering_Eliminate_Bugs_with_High-Signa__Kz-i33toG2g.md`

**243. [Long-Running AI Agents: The Next Breakthrough in Enterprise Work](https://www.youtube.com/watch?v=NHVtXHUcVXE)** — NVIDIA Developer · 인프라·칩·전력 · US · 2026-06 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Exciting sections, amazing &gt;&gt; [laughter] &gt;&gt; Hello everybody. And welcome to Nemo Tron days, right? Uh, thank you guys for coming here and uh, enjoying us. We want to start Nemo Tron days by talking about uh, …
- B4 가치네트워크·생태계: And so, at Nvidia, you know, uh as for our business to be uh competitive in the industry we we focus on, we've got to be great at chip design, we've got to be great at software development, and then the Taiwan ecosystem, uh we've got to be great at supply chai…
- B1 디지털·AI 기술의 활용: Uh if you want to build your own uh specialized sub-agents, uh we have this neat these NeMo Cloud blueprints, which are a great place to get started.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 파인튜닝·학습 · 칩·하드웨어 · 코딩 에이전트 · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/NVIDIA_Developer/Long-Running_AI_Agents_The_Next_Breakthrough_in_Enterprise_W__NHVtXHUcVXE.md`

**244. [Continual Learning for Long-Running Agents: Agents That Keep Getting Better](https://www.youtube.com/watch?v=SVWmuJx0hHM)** — NVIDIA Developer · 인프라·칩·전력 · US · 2026-07 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: Uh hello everyone. Yeah, I'm Jack Manong. I'm a founding research engineer at Prime Intellect. So, I did I think we've like learned a lot about agents today and like all the remarkable things that they do. And I actually…
- B1 디지털·AI 기술의 활용: So, like uh Cloud Code, Gemini, or if you're doing like ChatGPT, when you try to paste a really long text into the chat window, they'll basically always convert it into the this like pasted thing.
- B7 성과: 조직성과: So you basically get like a weights and biases kind of thing, but there's like some specific things that are for reinforcement learning in terms of like configs and like buffers and evaluations.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습 · 추론 최적화 · 칩·하드웨어 · 코딩 에이전트
- 원문: `transcripts/channels/NVIDIA_Developer/Continual_Learning_for_Long-Running_Agents_Agents_That_Keep___SVWmuJx0hHM.md`

---

## Nasdaq


**245. [Where the Gaps Exist With Enterprise AI Adoption](https://www.youtube.com/watch?v=cE4ppGayicY)** — Nasdaq · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 나스닥 트레이드 토크에 오신 것을 환영합니다. 이곳에서는 신흥 기술, 디지털 자산, 규제 환경 및 자본 시장 분야의 최고 전문가 및 전략가들을 만나 이야기를 나눕니다. 저는 진행자 질 말렌드 리노입니다. 나스닥 시장 현장 데스크에는 인 비저블 테크놀로지스의 CEO인 맷 피츠패트릭, 버그 크라우드의 AI 책임자이자 코네티컷 멜론 대학교 전기 및 컴퓨터 공학과 교수인 데이비드 브렘리 박사, 그리…
- B8 부정 성과: 보안·프라이버시: 이는 편향을 나타낼 수 있는데, 예를 들어 신용 결정을 내릴 때 수천 명의 사람들이 분산된 방식으로 누가 대출을 받을지 결정하는 것과 중앙 집중식 모델을 비교해 보면, 분산형 모델이 훨씬 더 편향되지 않은 결과를 가져온다는 것을 알 수 있습니다.
- B1 디지털·AI 기술의 활용: 훌륭한 기반이 되는 LLM(Level Leadership Model)들이 있지만, 우리가 어떤 권리를 포기해야 하는지, 그리고 그것이 우리 비즈니스 모델에 적합한지 진지하게 고민해야 합니다.
- 수치 주장: 오늘 우리는 기업의 AI 도입에 있어 어떤 격차가 존재하는지, 그리고 기업들이 2026년에 AI를 어떻게 활용할 것인지에 대해 논의하기 위해 이 자리에 모였습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/2026-07-21/Where_the_Gaps_Exist_With_Enterprise_AI_Adoption__cE4ppGayicY.md`

---

## Nissan


**246. [Nissan Motor Co., Ltd. 123rd Ordinary General Meeting of Shareholders](https://www.youtube.com/watch?v=bxMwW7KnuqE)** — Nissan · 물리 AI·자율주행 · JP · 2022-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] [박수] [음악] [박수] [음악] 안녕하십니까. 닛산자동차 사장으로서 오늘 닛산 자율주주총회에 참석해 주셔서 진심으로 환영하고 감사드립니다. 회사 정관에 따라 오늘 주주총회를 주재하겠습니다. 감사합니다. 이제 닛산자동차 주식회사 제123차 정기주주총회의 개회를 선언합니다. 닛산의 차세대 사업 혁신 계획의 진행 상황을 알려드리고, 2021 회계연도 연간 실적, 2022 회계연도 연간…
- B4 가치네트워크·생태계: 이 회담을 통해 얼라이언스 2030 관련 프로젝트는 물론, 프랑스 파트너사가 연구 중인 새로운 전기차 회사 콘셉트에 대한 자세한 내용을 들을 수 있었습니다.
- B7 성과: 운영효율: 순매출은 전년 대비 7.1% 증가한 8조 4천억 엔을 기록했으며, 영업이익은 3,980억 엔 증가한 2,473억 엔으로 영업이익률은 2.9%로 전년 대비 4.8%포인트 상승했습니다.
- 수치 주장: 고정비 3,500억 엔 이상 절감 목표를 초과 달성하며 더욱 탄력을 받고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Nissan/Nissan_Motor_Co.,_Ltd._123rd_Ordinary_General_Meeting_of_Sha__bxMwW7KnuqE.md`

**247. [Accelerating toward a circular economy – from idea to action | #Nissan](https://www.youtube.com/watch?v=lX2NDGB6AB4)** — Nissan · 물리 AI·자율주행 · JP · 2023-09 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B8 부정 성과
- 개요: [음악] 감사합니다 [음악] 감사합니다 [음악] 안녕하세요 여러분, 닛산 지속가능성 세미나 2023 순환 경제에 참석해 주셔서 감사합니다. [음악] 저는 닛산 자동차 글로벌 커뮤니케이션의 오하라입니다. 오늘 사회를 맡게 되어 기쁩니다. 세미나는 프레젠테이션과 패널 토론으로 구성되어 있습니다. 먼저 닛산 자동차의 지속가능성 최고 책임자이신 조지 타가와 씨를 모시고 닛산의 환경 분야 이니셔티브에…
- B3 전략적 대응: 이전에는 IKEA의 최고 지속 가능성 책임자였으며, 2년 전 IKEA를 떠난 후 북미와 유럽 전역의 의료, 소매, 레스토랑, 지속 가능한 소재 관련 기업에서 이사회 활동을 하고 있습니다.
- B7 성과: 사회적 편익: 따라서 순수 상업적 관점에서도 회수 서비스를 제공하는 것이 타당하다고 판단했고, 지속가능성 관점에서도 제품 수명을 최대한 늘려 탄소 발자국을 줄이는 것이 중요하기 때문에 매우 합리적인 선택이었습니다.
- 수치 주장: 또한, 태양 광 및 풍력 발전과 같은 재생에너지 도입을 확대하고, 2010년 12월 닛산 리프 출시 이후 생산 공장의 재생에너지 소비 비중을 11.9%까지 높였습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Nissan/Accelerating_toward_a_circular_economy_–_from_idea_to_action__lX2NDGB6AB4.md`

**248. [Fostering a more inclusive workplace – from reactive to proactive | #Nissan #DEI](https://www.youtube.com/watch?v=BVlPVaG34wI)** — Nissan · 물리 AI·자율주행 · JP · 2023-09 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요, 신사 숙녀 여러분. 닛산 지속가능성 세미나 2023 다양성, 공정성 및 포용성 세션에 참여해 주셔서 대단히 감사합니다. 저는 닛산 자동차 글로벌 커뮤니케이션 부서의 오하라입니다. 오늘 사회를 맡게 되어 기쁩니다. 세미나는 기조 연설과 패널 토론 두 부분으로 구성되어 있습니다. 먼저 TDC 글로벌의 설립자 겸 대표이사인 사라 리우 씨가 기조 연설을 해 주실 예정입니다. 이…
- B3 전략적 대응: 하지만 더 중요한 것은, 경영진이 ERG를 어떻게 지원하고, 어떻게 투자하고, 어떻게 그들과 함께하며 방금 말씀드린 것처럼 훌륭한 성과를 낼 수 있도록 도울 것인가를 고민해야 한다는 점입니다.
- B5 리더십·CDO/CAIO: 따라서 우리가 의료 생태계에서 영향력 있는 역할을 하고 있다는 것을 인지하고, 데니를 앞세워 리더십을 발휘하는 것은 더 광범위한 영향력을 행사하는 데 도움이 될 것입니다.
- 수치 주장: 우리 인구의 50%는 여성 인재이며, 현재 전례 없는 인재 부족을 겪고 있는 일본과 같은 지역에서는 전통적으로 활용도가 낮고 고용률이 낮은 여성 인력을 어떻게 활용할 것인가가 우리가 해결해야 할 가장 큰 문제 중 하나가 되었습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Nissan/Fostering_a_more_inclusive_workplace_–_from_reactive_to_proa__BVlPVaG34wI.md`

---

## Nokia


**249. [Networked | Automating, monetizing and delivering 5G at scale with Bharti Airtel](https://www.youtube.com/watch?v=FMXZu8qREaA)** — Nokia · 통신·주권·국가 · FI · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 란딥, 환영합니다. 만나서 반가워요. 그리고 무엇보다도, 저는 당신과 거의 10년 동안 이어온 관계를 진심으로 소중히 여깁니다 . 인도네시아에서 시작해서 지금은 에어텔에 이르렀습니다. 정말 멋진 여정이었어요. 그럼, 환영합니다. 매우 감사합니다. 보시 다시피, 저희는 이 업계에서 꽤 오랫동안 함께 일해 왔습니다. 그리고 우리는 그것이 변화하는 것을 목격해 왔고, 앞으로도 계속 변화할…
- B1 디지털·AI 기술의 활용: 시스템 통합업체 , IoT 파트너, 클라우드 파트너 등 우리 모두가 함께 이 문제를 해결해야 합니다.
- B4 가치네트워크·생태계: GSMA나 Camara처럼 통신사 커뮤니티를 하나로 모으는 영향력을 행사하는 방식일 수도 있고, 통신사 파트너 생태계가 주도하는 방식일 수도 있습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Nokia/Networked_Automating,_monetizing_and_delivering_5G_at_scale___FMXZu8qREaA.md`

**250. [Networked | Driving reliable 5G with secure AI and cloud-native automation](https://www.youtube.com/watch?v=-_qPtPJq6EQ)** — Nokia · 통신·주권·국가 · FI · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 토니, 방금 클라우드에 대해 조금 이야기하셨는데요, 클라우드가 우리가 이 업계에 가져오려는 혁신에 어떤 전략적 영향을 미치는지에 대해서요. 옵터스는 멀티 클라우드 기능을 도입하는 데 있어 선두 주자 중 하나라는 것을 잘 알고 계실 겁니다 . 그렇다면 클라우드 네이티브 아키텍처가 코어, 동적 슬라이싱, 저지연 서비스와 같은 고급 5G 네트워크 기능을 어떻게 구현할 수 있다고 보십니까?…
- B1 디지털·AI 기술의 활용: 그래서 카메라 및 기타 API에서 그러한 현상을 일부 볼 수 있지만, 네트워크 서비스 API(Network as a Service API)는 TM 포럼에서 수년간 개발해 온 분야입니다.
- B3 전략적 대응: 그리고 이것은 노키아나 옵터스를 위한 기술 로드맵이 아니라 , 미래를 향한 고객 로드맵입니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Nokia/Networked_Driving_reliable_5G_with_secure_AI_and_cloud-nativ__-_qPtPJq6EQ.md`

**251. [Networked | How private 5G, edge computing, and AI are redefining enterprise innovation](https://www.youtube.com/watch?v=Vrs17zzHv2c)** — Nokia · 통신·주권·국가 · FI · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 젠, 안녕하세요. 시간 내서 이야기 나눠주셔서 감사합니다 . Verizon Business는 미국 시장의 선두주자 이며, 국제적으로도 매우 좋은 성과를 거두고 있습니다. 버라이즌 비즈니스에서 당신의 역할은 업계 전반에서 가장 중요한 기회 중 하나인 5G 도입을 가속화하는 것입니다. 버라이즌 비즈니스를 위해 이러한 의제를 어떻게 추진하고 계십니까? 그렇다면 가장 유망한 측면은 무엇이라…
- B4 가치네트워크·생태계: 또한, 당사는 파트너들이 적재적소에 자리 잡을 수 있도록 지원하는 데 집중하는 생태계 개발팀을 보유하고 있으며, 이를 통해 고객에게 포괄적인 솔루션을 제공할 수 있도록 노력하고 있습니다.
- B1 디지털·AI 기술의 활용: 그래서 저는 앞으로 API, 셀프 서비스, 그리고 IT 팀이 혁신 플랫폼을 통해 더 많은 일을 할 수 있도록 지원하는 다른 도구들에 대한 중요성이 더욱 강조될 것이라고 생각합니다.
- 수치 주장: 23명에서 24명으로 늘어나면서 3.5 배 증가했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Nokia/Networked_How_private_5G,_edge_computing,_and_AI_are_redefin__Vrs17zzHv2c.md`

**252. [Nokia, Elisa & NVIDIA Accelerating AI-RAN from concept to commercialization](https://www.youtube.com/watch?v=O8WLc1_3EHI)** — Nokia · 통신·주권·국가 · FI · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 음. [음악] 음. [음악] 여러분 모두 환영합니다. 실시간으로 참여하시든 나중에 시청하시든, 함께해 주셔서 감사합니다 . 저는 노키아의 노라 파르카스입니다. 오늘 세션의 사회를 맡겠습니다. 현재 AI 운영에 대한 관심이 매우 높습니다 . 그 이면에 숨겨진 원리는 아주 간단합니다. 네트워크 트래픽의 특성이 변화하기 시작했습니다. 따라서 AI 워크로드는 기존 방식과 다르게 동작하며, …
- B1 디지털·AI 기술의 활용: 동시에, 우리는 동일한 가맹점용 반도체와 동일한 컴퓨팅 플랫폼을 사용하여 완전한 클라우드 네이티브 구현 및 AI 네이티브 구현을 통해 완전히 유연한 카드 시스템을 구축하고 있습니다 .
- B4 가치네트워크·생태계: 자, 그들이 가치 사슬에서 얼마나 더 높은 단계로 나아갈지는, 즉 GPU 서비스만 제공할지, 토큰 서비스를 제공할지, 모델 서비스로 나아갈지, 아니면 AI 애플리케이션 서비스로 나아갈지는 각각의 기회, 각 사업자, 그리고 각 국가의 생태계에 달려 있습니다.
- 수치 주장: 그리고 맥락을 고려해 보면 , 저희 엘리사는 지난 15년 동안 네트워크 자동화를 추진해 왔습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Nokia/Nokia,_Elisa_&_NVIDIA_Accelerating_AI-RAN_from_concept_to_co__O8WLc1_3EHI.md`

---

## OnePint AI


**253. [Fail Forward: Why AI Adoption Rewards the Willing](https://www.youtube.com/watch?v=XrD-W6013G0)** — OnePint AI · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B8 부정 성과
- 개요: 네, 저희가 도착했습니다. 네, 셰이 님, 팟캐스트에 참여해 주셔서 감사합니다. 네 , 초대해 주셔서 감사합니다. 네, बिल्कुल 그렇습니다. 어, 셰이, 우리는 오랫동안 서로 알고 지냈잖아. 저희는 Carne에서도 함께 일한 적이 있습니다 . 음, 어떻게 지내셨어요? 요즘 어떻게 지내세요? 음, 저는 올해 2월에 유랑극단을 떠났고, 그 이후로 여러 중견 기업들과 협력하여 그들이 AI 여…
- B4 가치네트워크·생태계: 이 모든 것은 어떻게 하면 공급망을 더 예측 가능하게 만들어 재고 부족이나 과잉 재고 축적을 충분한 인식 없이 방지할 수 있을까에 관한 것입니다.
- B7 성과: 운영효율: 하지만 개별 직원의 생산성 향상만으로는 기업 전체에 엄청난 투자 수익률(ROI)을 가져다주지는 못할 것입니다 .
- 수치 주장: 그래서 2~4주 안에 온보딩을 완료하고 애플리케이션 사용을 시작할 수 있으며, 고객의 요구 사항에 따라 공동 개발도 진행합니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/2026-08-03/Fail_Forward_Why_AI_Adoption_Rewards_the_Willing__XrD-W6013G0.md`

---

## OpenAI


**254. [Customer Ignite Talk: Antonio Bravo Acin (Global Head of AI Transformation, BBVA) & OpenAI](https://www.youtube.com/watch?v=UNJSk90Lz1c)** — OpenAI · 파운데이션 모델 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 자 , 다음으로 케이티가 방금 이야기해 준 세 가지 핵심 요소 모두에 전력을 다하고 있는 훌륭한 기업의 사례를 공유하고 싶습니다 . BBVA는 세계 최대 은행 중 하나입니다 . 그들의 목표는 AI를 부가 기능으로 만드는 것이 아니라, 사업 전반에 걸쳐 AI를 접목하는 것이었습니다. 단순히 질문에 답하는 것을 넘어, 핵심적인 비즈니스 기능을 적극적으로 지원합니다. 그들은 전 세계 12…
- B1 디지털·AI 기술의 활용: 그런 다음, 데이터 과학자, 머신러닝 엔지니어, 소프트웨어 개발자 등 모든 역량을 갖춘 다학제 팀을 소매, 상업 또는 위험 관리 팀에 배치하여 이러한 에이전트를 구축하기 위해 협력하도록 합니다 .
- B4 가치네트워크·생태계: 또한 생태계와 협력하고, 토큰으로 어려운 시기에 자금을 지원하는 팀과 투자 역량을 갖춘 팀에 자금을 지원하는 방식을 점진적으로 도입하여 장기적으로 지속적인 효과를 창출하는 자산 게이트 투자 접근법을 확보하는 데에도 힘쓰고 있습니다.
- 수치 주장: 그들은 전 세계 12만 명이 넘는 직원들에게 ChatGPT Enterprise를 배포하는 것으로 시작했습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/OpenAI/Customer_Ignite_Talk_Antonio_Bravo_Acin_(Global_Head_of_AI_T__UNJSk90Lz1c.md`

**255. [What racing reveals about working with AI — the OpenAI Podcast Ep. 22](https://www.youtube.com/watch?v=KNPjRpNtQ7s)** — OpenAI · 파운데이션 모델 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 저는 앤드류 메인이고 이것은 오픈AI 팟캐스트입니다. 이번 에피소드에서는 OpenAI 연구원 조이스 러펠과 함께 칩 가나시 레이싱 팀이 AI를 활용하여 물류부터 드라이버 경기력 향상까지 모든 것을 개선하도록 도운 경험에 대해 이야기를 나눴습니다. 저는 또한 레이싱 회사를 설립하는 데 ChatGPT와 Codex를 활용한 Racetech의 공동 창립자인 Chase Holden과 이야…
- B1 디지털·AI 기술의 활용: 그래서 만약 우리가 개발할 수 있는 어떤 종류의 AI 도구나 머신러닝 도구가 누군가가 한 가지 일을 더 빠르게 또는 여러 가지 일을 더 빠르게 처리하는 데 도움이 된다면, 그 사람의 시간과 생각을 자유롭게 해 주어 그동안 관심은 있었지만 우선순위에서 밀려났던 질문들을 탐구할 수 있게 해 줄 수 있을 것입니다 .
- B2 파괴: 경쟁구도: 저도 이 의견에 동의하며, 덧붙이자면 경쟁 우위를 확보하는 데 있어 창의성이 훨씬 더 중요해질 것이라고 생각합니다.
- 수치 주장: 물론 그들이 노력하지 않는다는 말은 아니지만, 인공지능을 활용하면 운전자가 직접 공부하고 살펴봐야 할 정보를 4~5시간 만에 얻을 수 있다고 생각합니다.
- 교량: — · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/OpenAI/What_racing_reveals_about_working_with_AI_—_the_OpenAI_Podca__KNPjRpNtQ7s.md`

---

## Oracle


**256. [AI Changes Everything: Can You Insure AI Risk?](https://www.youtube.com/watch?v=45uxFcLk6jA)** — Oracle · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 이 팟캐스트에서 표현된 견해는 개별 발표자의 견해이며, 발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다. 모두가 인공지능을 활용하기 위해 경쟁하는 가운데, 대규모 언어 모델의 불확실성을 어떻게 정량화할 수 있을까요? 우리가 어떤 위험에 노출되어 있는지 알고 있을까요? 그리고 음악을 통해 어떻게 그 위험으로부터 우리를 보호할 수 있을까요 ? 안…
- B8 부정 성과: 보안·프라이버시: 그리고 말씀하신 많은 위험, 즉 부정확성, 환각 위험뿐만 아니라 저작권 침해 위험과 같은 것들은 모델의 잘못된 출력에서 ​​비롯될 수 있습니다.
- B5 직무·역량 변화: 저희는 보험 분야의 비즈니스 측면, 즉 저희 팀에 그런 동료들을 채용하여 이러한 유형의 위험을 평가하는 새로운 정량화 방법론을 개발하는 데 도움을 받으려고 합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Oracle/AI_Changes_Everything_Can_You_Insure_AI_Risk__45uxFcLk6jA.md`

**257. [AI Changes Everything: What Leaders Must Get Right About AI](https://www.youtube.com/watch?v=AF8rr7rCl38)** — Oracle · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 이 팟캐스트에서 표현된 견해는 개별 발표자의 견해이며, 발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다. 인공지능은 국가 방위에 어떤 역할을 할까요 ? 인공지능을 활용하는 이러한 시나리오에서 리더십은 어떻게 진화해야 할까요 ? 인공지능은 어디에 적용되어야 하며, 명령 및 통제 맥락에는 적용되지 않아야 할까요? [음악] 안녕하세요 여러분. 저는…
- B1 디지털·AI 기술의 활용: 그런데 지금은 클라우드 미토스(Cloud Mythos) 같은 곳에서 취약점을 아주 빠르게 발견하고 있다고 하잖아요 .
- B7 성과: 운영효율: 기업 차원에서는 "투자 수익률(ROI)을 X만큼 달성하고 싶고, AI를 도입해서 그 목표를 달성하겠다"라고 말하기 때문이죠.
- 수치 주장: 그리고 지난 6년간의 변화는, 어떻게 하면 그런 기술적 사고방식, 기술 제공 방식, 그리고 더 민첩하고 유연하며 린 스타트업 방식의 업무 방식을 컨설팅 사업과 고객의 문제를 해결하는 데 적용할 수 있을까 하는 것이었습니다.
- 교량: — · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/Oracle/AI_Changes_Everything_What_Leaders_Must_Get_Right_About_AI__AF8rr7rCl38.md`

**258. [AI Changes Everything: Inside Oracle Red Bull Racing’s AI Edge](https://www.youtube.com/watch?v=KJUfigBy684)** — Oracle · 데이터·컨텍스트·거버넌스 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 이 팟캐스트에서 표현된 견해는 개별 발표자의 견해이며, 발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다. 포뮬러 1에서는 모든 결정과 매 순간이 챔피언십의 향방을 결정짓습니다. 하지만 위험 부담이 최고조에 달하고 실수의 여지가 전혀 없을 때, 기술만으로 충분할까요? 아니면 인간의 판단력이 여전히 궁극적인 경쟁 우위 요소로 남아 있는 것일까? …
- B1 디지털·AI 기술의 활용: 하지만 자동차와 더 밀접한 관련이 있는 부분에서도 머신러닝 기술을 활용하여 자동차 센서를 모델링함으로써 질량을 줄이거나, 대리 모델링이나 다른 기술을 통해 일반적으로 사용하는 물리적 모델을 개선할 수 있을 것입니다.
- B2 파괴: 경쟁구도: 아니면 인간의 판단력이 여전히 궁극적인 경쟁 우위 요소로 남아 있는 것일까?
- 수치 주장: 하지만 제가 소프트웨어를 개발해 온 방식, 그리고 지난 10년 동안 대부분의 사람들이 소프트웨어를 작성해 온 방식은 오늘날 소프트웨어를 작성하는 방식과는 다릅니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Oracle/AI_Changes_Everything_Inside_Oracle_Red_Bull_Racing’s_AI_Edg__KJUfigBy684.md`

**259. [AI Changes Everything: Using AI to Help Prevent Human Trafficking](https://www.youtube.com/watch?v=G6PZCdNSl68)** — Oracle · 데이터·컨텍스트·거버넌스 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 이 팟캐스트에서 표현된 견해는 개별 발표자의 견해이며, 발표자 의 소속 기관이나 오라클 또는 그 계열사의 견해 또는 정책을 반드시 반영하는 것은 아닙니다. 인공지능에 대해 이야기할 때, 우리는 기술 자체에만 집중하고 그 결과를 간과하는 경향이 있습니다. 하지만 이 기술에는 또 다른 측면이 있습니다. 바로 이 기술을 활용하여 세계가 직면한 가장 심각한 문제들을 해결할 수 있다는 점입니다. 인신…
- B5 직무·역량 변화: 우리는 이미 은행, 채용 플랫폼, 취업 알선 기관, 그리고 여러 회사들이 인신매매에 연루되었다는 증거를 보여주고 있습니다.
- B3 전략적 대응: 그리고 여기서 여러분을 웃게 해드릴 게 있는데요, 제가 'Stop The Traffics'라는 단체의 이사회에 있었는데, 제 가장 친한 친구 중 한 명이 이사회 멤버였어요.
- 수치 주장: 그리고 약 8년 후, 저희는 워싱턴에서 250~300개의 기업, 은행, 정부 기관과 함께 교통 분석 허브의 첫 번째 버전을 출시했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Oracle/AI_Changes_Everything_Using_AI_to_Help_Prevent_Human_Traffic__G6PZCdNSl68.md`

---

## Orange


**260. [Au cœur de la #recherche Orange : IA, cybersécurité et réseaux du futur](https://www.youtube.com/watch?v=Fuz0TWocOsU)** — Orange · 통신·주권·국가 · FR · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 파론텍, 미래의 팟캐스트. [음악] 연구와 오렌지가 관련되어 있다는 사실을 알고 계셨나요? 이미 다음과 같은 기술들을 개발하고 있습니다. 내일 당신의 일상을 만들어갈 것은 무엇일까요? 여러분, 안녕하세요. 저는 휴고입니다. 세두라만과 오늘날 이곳에서 Parlon 스페셜 에피소드, 저희는 다음 내용을 다룹니다. 이러한 혁신에 대해 조명합니다 특별한 손님들이 모였습니다. 저희 스튜디오에…
- B4 가치네트워크·생태계: 그래서 저희는 우리는 연구 프로젝트를 시작했습니다 특히 Linia와의 파트너십에서 파리, 그리고 그들은 또한 전문가입니다.
- B1 디지털·AI 기술의 활용: 첫 번째 버전 출시 GPT 채팅방에서 많은 이야기가 오가고 있어요.
- 수치 주장: 그것은 도입된 기술 2014년 메타 개발자들 페이스북은 실제로 다음과 같은 것을 허용합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Orange/Au_cœur_de_la_#recherche_Orange_IA,_cybersécurité_et_réseaux__Fuz0TWocOsU.md`

**261. [Science, Innovation and Technology: The vision of Bruno Zerbib, CTIO of Orange](https://www.youtube.com/watch?v=69tvTh7axU0)** — Orange · 통신·주권·국가 · FR · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 변하지 않는 유일한 것은 변화 그 자체이다. [음악] 브루노, 오늘 오렌지 오픈 테크 행사를 개최하실 캠퍼스에 초대해 주셔서 정말 감사합니다. 지금 활기와 흥분을 느끼고 있어요. 음, 당신은 당신의 전체 생태계를 가져올 겁니다. 오늘은 기술 혁신에 대해 이야기해 보겠습니다. 하지만 이 모든 사람들이 오기 전에, 당신의 생각을 좀 들어보고 싶습니다 . 나는 그 수정 구슬을 열어보고 싶어. 당신…
- B4 가치네트워크·생태계: 그래서 저희가 오렌지에서 하고 있는 일은, 음, 정말 놀라운 전문성을 가진 매우 선진적인 기관들로 이루어진 생태계를 구축하는 것입니다.
- B1 디지털·AI 기술의 활용: 지금 가치 포착 측면에서 보면 [목을 가다듬으며] Jad GPT 구독이 다른 어떤 업체보다 훨씬 앞서 나가고 있고, 정말 빠르게 성장하고 있습니다.
- 수치 주장: 음, 1년 전만 해도 우리는 견고한 LLM을 구축하는 유일한 방법은 수천억 달러 또는 유로를 투자하는 것이라고 생각했습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Orange/Science,_Innovation_and_Technology_The_vision_of_Bruno_Zerbi__69tvTh7axU0.md`

**262. [Bruno Zerbib on AI, Intelligent Networks and the Future of Connectivity | MWC 2026](https://www.youtube.com/watch?v=xPpwRnoZzlo)** — Orange · 통신·주권·국가 · FR · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 저희는 MWC [음악] 2026에 와 있습니다. 해마다 다르고, 업계에 가해지는 압력도 다릅니다. 작년에는 관세 와 인공지능이 기술을 얼마나 빠르게 변화시키고 있는지에 대한 이야기가 많았던 게 기억나요 . 올해는 조금 다르지만 여전히 부담감이 있고, 당신은 어떻게 느끼는지 궁금합니다. 제 생각에는 기술, 특히 모바일 기술은 소비자든 기업이든 우리 일상생활에 너무나 널리 퍼져 있지만 , 압박감…
- B1 디지털·AI 기술의 활용: 저희는 음, 통신사 중에서 최초로 주요 LLM(로봇 학습 모델)의 오픈웨이트 버전을 이용할 수 있었던 회사였습니다.
- B4 민첩성·양손잡이: 그리고 민첩하게 움직이고 그런 것들이 성숙해가는 과정을 지켜보기 때문에, 굳이 예언자처럼 2~3년 후에 무엇이 새로운 것이 될지 미리 예측할 필요가 없습니다.
- 수치 주장: 음, 1년 전에는 LLM을 다른 애플리케이션과 어떻게 통합할 것인가에 대한 논의가 더 주를 이루었습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 칩·하드웨어
- 원문: `transcripts/channels/Orange/Bruno_Zerbib_on_AI,_Intelligent_Networks_and_the_Future_of_C__xPpwRnoZzlo.md`

**263. [La confiance, un facteur clé du déploiement de l'IA en santé | VivaTech 2026](https://www.youtube.com/watch?v=jjJkYvT4MjI)** — Orange · 통신·주권·국가 · FR · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요 여러분, 반갑습니다. 그러니까 제가 말씀드리는 내용은 여러분이 이미 알고 있는 내용과 크게 다르지 않습니다. 제가 말씀드리건대, 2025년까지 LIA는 완전히 새로운 모습으로 탈바꿈할 것입니다. 대규모 의학 연구 이전의. 하지만 물론, 이것은 변화는 오직 다음과 같은 경우에만 일어날 수 있습니다. 신뢰하다. 점점 더 데이터 보안은 복잡합니다. 디지털. 그들은 점점 더 많은. 규칙은…
- B4 가치네트워크·생태계: 내일의 건강을 조금이라도 만들어가는 것 우리가 설명한 모든 기본 사항 여기 그리고 신뢰를 기반으로 분명히 생태계 안에서 작동합니다 어쩌면 그것은 무엇보다도 ~에 관한 것일지도 모릅니다.
- B1 디지털·AI 기술의 활용: 그리고 거기서부터, 이것으로 충분합니다, 다시 한번 원래 설계된 것을 전치하세요 인간 활동을 다음과 같은 틀 안에 담기 위해 AI 에이전트의 활동에서.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Orange/La_confiance,_un_facteur_clé_du_déploiement_de_l'IA_en_santé__jjJkYvT4MjI.md`

**264. [The Impact of Agentic AI on Telco Transformation & Innovation | VivaTech](https://www.youtube.com/watch?v=c1XCSgKzhp4)** — Orange · 통신·주권·국가 · FR · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 여러분, 안녕하세요. 이 패널에 오신 것을 환영합니다. 우리는 과장이나 마케팅 문구가 아닌, 진정한 인공지능에 대해 논의할 것입니다 . 더욱 흥미로운 점은 진정한 인공지능을 구현하기 위해 모든 것을 혼자서 하는 대신, 협업할 수 있는 기회가 생긴다는 것입니다. 스타트업과 협력하고, 규모가 큰 기업과 협력하며, 통신사 간에도 협력합니다. 자, 이것들이 우리가 논의할 주제들입니다. 이번 토론에는…
- B4 가치네트워크·생태계: 제가 이해한 바로는 진정한 AI는 단순히 기술적인 측면뿐만 아니라 새로운 사고방식, 통신사 와 스타트업 간의 협력, 그리고 이러한 생태계가 형성될 수 있도록 지원하는 통신사 간의 협력을 바탕으로 한다는 것입니다 .
- B1 디지털·AI 기술의 활용: 또한 이러한 새로운 에이전트들을 위해서는 컴퓨팅 자원과 유럽 내 신뢰할 수 있고 보안이 유지되는 운영 시스템 등이 필요하기 때문에, 당사의 글로벌 인프라, 즉 클라우드 환경에서도 이러한 작업이 필요합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Orange/The_Impact_of_Agentic_AI_on_Telco_Transformation_&_Innovatio__c1XCSgKzhp4.md`

---

## Palantir


**265. [Backstage Pass | AIPCon 5](https://www.youtube.com/watch?v=F47gTGFk2Bo)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2024-09 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: all right we are back at the backstage pass at&nbsp; pal tier's fifth edition of AIP peon we got a lot&nbsp;&nbsp; to talk about we had some keynote presentations&nbsp; we're going to go over that and in just a little&nb…
- B4 가치네트워크·생태계: all right we are back at the backstage pass at&nbsp; pal tier's fifth edition of AIP peon we got a lot&nbsp;&nbsp; to talk about we had some keynote presentations&nbsp; we're going to go over that and in just a little&nbsp;&nbsp; bit we're going to hear from s…
- B7 성과: 조직성과: all right we are back at the backstage pass at&nbsp; pal tier's fifth edition of AIP peon we got a lot&nbsp;&nbsp; to talk about we had some keynote presentations&nbsp; we're going to go over that and in just a little&nbsp;&nbsp; bit we're going to hear from s…
- 수치 주장: all right we are back at the backstage pass at&nbsp; pal tier's fifth edition of AIP peon we got a lot&nbsp;&nbsp; to talk about we had some keynote presentations&nbsp; we're going to go over that and in just a little&nbsp;&nbsp; bit we're going to hear from s…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Palantir/Backstage_Pass_AIPCon_5__F47gTGFk2Bo.md`

**266. [Backstage Pass | AIPCon 7](https://www.youtube.com/watch?v=_8RokabwNG8)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2025-06 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Hello everybody. Welcome back to AIPCON. This is&nbsp; the seventh, yes you heard that right, seventh&nbsp;&nbsp; edition of AIPCON. My name is Emit. I've been&nbsp; covering Palanteer for the better part of 5 years&nbsp…
- B4 가치네트워크·생태계: To kick us off tell&nbsp; us a bit more about your work at international&nbsp;&nbsp; and a bit about the partnership that you guys have&nbsp; built with Palanteer.
- B1 디지털·AI 기술의 활용: Karp at uh AIPCON&nbsp; number two said that LLM's large language models&nbsp;&nbsp; are like artist colonies.
- 수치 주장: Truly incredible.&nbsp; Yeah, we have over 40,000 users in the platform&nbsp;&nbsp; and they're saving about 2 to three hours a week.&nbsp; And the fact that you're you're operating those&nbsp;&nbsp; complex environments, I imagine that speed, that&nbsp; time …
- 교량: Avenue 1 동적역량 · 기술: 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Palantir/Backstage_Pass_AIPCon_7___8RokabwNG8.md`

**267. [Chad & Matt | Lightweight Data Transforms with Palantir AIP](https://www.youtube.com/watch?v=MITSJDI08R4)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2025-08 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [Music] Hi, I'm Chan Walquist. I'm an architect at&nbsp; Palunteer. Today I've got you Matthew Bayer&nbsp;&nbsp; who's a forward deployed engineer or FDE on&nbsp; our compute engines team. Thanks for joining&nbsp;&nbsp; …
- B1 디지털·AI 기술의 활용: And so really in order to get all these&nbsp;&nbsp; benefits of an LLM in a place like writing data&nbsp; pipelines, you need all these features.
- B5 직무·역량 변화: So, previously&nbsp;&nbsp; we saw that data engineers who were authoring&nbsp; pipelines would take a while to upskill on certain&nbsp;&nbsp; libraries.
- 수치 주장: So although we ran in a much&nbsp; uh in a similar amount of time, we only used about&nbsp;&nbsp; 29 GB of memory throughout this transform, which&nbsp; is, you know, almost 10 times smaller than what&nbsp;&nbsp; that Spark uh pipeline was doing with executive…
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 칩·하드웨어
- 원문: `transcripts/channels/Palantir/Chad_&_Matt_Lightweight_Data_Transforms_with_Palantir_AIP__MITSJDI08R4.md`

**268. [Overcoming Zero-Sum Thinking on Privacy, Civil Liberties, and Mission-Critical AI Systems](https://www.youtube.com/watch?v=x-NEdIcgboo)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2025-08 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [Music] All right. Well, I think we're&nbsp; going to kick off here. Um, Courtney Bowman,&nbsp;&nbsp; thanks for taking the time to talk with me today.&nbsp; Anytime. Um, excited. Yeah. I I think that what we&nbsp;&nbsp;…
- B8 부정 성과: 보안·프라이버시: Um these&nbsp; are these are kind of basic logistics questions&nbsp;&nbsp; that don't actually implicate too much or in some&nbsp; cases any privacy interests.
- B1 디지털·AI 기술의 활용: So at this point I think about you know the&nbsp; 2016 to 2018 eras a lot of commercial enterprises&nbsp;&nbsp; especially were saying we're going to start moving&nbsp; workloads to the cloud at least the analytics or&nbsp;&nbsp; data ones.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 코딩 에이전트 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Palantir/Overcoming_Zero-Sum_Thinking_on_Privacy,_Civil_Liberties,_an__x-NEdIcgboo.md`

**269. [Chad & Chris | Tariff Savings and Compliance through Palantir AIP](https://www.youtube.com/watch?v=xBTPNLd8Jv8)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2025-09 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [Music] Hi, I'm Chad. I'm an architect at&nbsp; Palanteer. Today we've got Christopher who&nbsp;&nbsp; leads some of our manufacturing work. Thanks&nbsp; for joining me. Thank you, Chad. So, I know we&nbsp;&nbsp; were go…
- B1 디지털·AI 기술의 활용: Um, and this is&nbsp;&nbsp; where we're starting to design how we're going&nbsp; to have our AI agent, which is moving through&nbsp;&nbsp; these bills of materials.
- B5 조직구조 변화: So a lot&nbsp; of when you think about uh bills of materials or&nbsp;&nbsp; bombs and how you you frame that um we're really&nbsp; focused on taking actually what goes into the&nbsp;&nbsp; three sort of like silos of the business.
- 수치 주장: Everything's&nbsp;&nbsp; logged in and auditable in terms of a package.&nbsp; And then we can see that while originally we&nbsp;&nbsp; were getting tariffed on a $36 60 um unit price&nbsp; of of a component, we've actually reduced that&nbsp;&nbsp; because only…
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Palantir/Chad_&_Chris_Tariff_Savings_and_Compliance_through_Palantir___xBTPNLd8Jv8.md`

**270. [Paragon 2025](https://www.youtube.com/watch?v=UjkRz9HkldU)** — Palantir · 데이터·컨텍스트·거버넌스 · US · 2025-12 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 사흘째, 로스앤젤레스 일부 지역을 휩쓸고 있는 산불이 한 블록씩 이어졌습니다. 화산재 외에는 아무것도 없습니다. 속보: 미국 도널드 트럼프 대통령은 미국의 주요 교역 상대국에 관세를 부과했습니다. 공급망은 인플레이션에 중대한 영향을 미칠 것입니다. 가정의 복지에 대해 미국 국내외에서 메이븐에 대한 수요가 매우 높아지고 있습니다. 오늘 밤 저는 이 공격이 놀라운 군사적 성공을 거두었다는 사실을…
- B4 가치네트워크·생태계: 여러분과 맺은 파트너십을 통해 우리가 실제로 온톨로지, 파운드리, AIP, FD와 함께 하고 있으며, 여러분의 비즈니스가 번창할 때 시간이 지나야 실제로 보상을 받을 수 있다는 것을 느끼셨으면 좋겠습니다.
- B1 디지털·AI 기술의 활용: 하지만 Palantir의 장점은 우리가 실제로 비즈니스를 더 좋게 만드는 온톨로지의 형태로 소프트웨어와 LLM 관리를 제공하려고 노력하고 있다는 것입니다.
- 수치 주장: 그리고 불과 18개월 만에 이 프로젝트를 통해 기회 리드 투 기회 전환율이 실제로 5배나 증가했습니다.
- 교량: Avenue 1 동적역량 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/Palantir/Paragon_2025__UjkRz9HkldU.md`

---

## Philips


**271. [Bringing the “Mojo of Medicine” Back: How Philips Is Using AI as a Teammate in Healthcare | JPM 2026](https://www.youtube.com/watch?v=0Ye83rPSxrc)** — Philips · 수요기업·기타 · NL · 2026-03 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: 저는 스테이팬 스튜디오의 편집자 제시 맥쿼터스입니다 . 여기는 2026년 캘리포니아 샌프란시스코에서 열린 JPM 컨퍼런스 둘째 날 이른 아침입니다. 필립스의 최고 혁신 책임자 겸 엔터프라이즈 정보학 부문 최고 비즈니스 리더인 셰즈 파티와 함께 ​​있습니다 . 제즈, 와주셔서 정말 감사합니다. 제시, 저도 여기 오게 되어 기쁩니다. 전적으로. 그럼, 하시는 일과 담당 분야에 대해 간략하게 말씀…
- B4 가치네트워크·생태계: 필립스 내부에서도 소프트웨어 엔지니어링, 고객 지원, 영업 지원, 공급망 관리, 시판 후 감시 등 전체 가치 사슬에 인공지능을 도입하고 있습니다.
- B1 디지털·AI 기술의 활용: 그리고 핵심은, 우리 업계가 해야 할 가장 중요한 일 중 하나는 의학의 본질을 되찾는 것인데, 이를 위해서는 AI 에이전트가 수행할 수 있는 비임상 환자 관리 관련 추가 업무를 모두 줄이고 간호사와 의사가 환자 치료에 직접 집중할 수 있도록 해야 합니다.
- 수치 주장: 하지만 우리는 의료 시스템의 경우, 10년 전 디지털 전환 시대를 생각해 보면 단순히 종이에서 디지털로 바뀌었기 때문만은 아니라는 것을 알고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Philips/Bringing_the_“Mojo_of_Medicine”_Back_How_Philips_Is_Using_AI__0Ye83rPSxrc.md`

**272. [The Future of Medicine Is Already Here | AI, Connected Care & Health Innovation | JPM 2026](https://www.youtube.com/watch?v=wYmHA5Pr6_g)** — Philips · 수요기업·기타 · NL · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 저는 크리스틴 멀렌입니다. 저는 필립스 북미 지사의 전략 및 성장 부문 책임자입니다 . 오늘 저와 함께 기술, 의학, 건강의 교차점에서 오랫동안 활동해 오셨고 혁신을 주도해 오신 다니엘 크래프트 박사님을 모셨습니다. 자기소개를 해보시겠어요? 고마워요. 음, 말씀드렸듯이 저는 원래 의사이자 과학자입니다 . 음, 스탠포드에서 수련을 받았고, 매사추세츠 종합병원에서 내과와 소아과 레지…
- B4 가치네트워크·생태계: 그리고 종종 이러한 혁신을 주도하는 것은 바로 젊은 기업가들이며, 그들은 규모를 키워나가면서 생태계에서 가장 중요한 것들을 위해 우리 모두가 훨씬 더 빠르고 직접적으로 혁신할 수 있도록 도와줍니다.
- B5 리더십·CDO/CAIO: 그래서 지금은 매우 흥미로운 시기이며, 필요한 것은 사고방식과 리더십, 의료 시스템, 임상의, 그리고 개개인이 해결책이 있다는 확신을 갖는 것입니다.
- 수치 주장: 특히 여러분과 다른 분들이 개발하고 있는 이러한 도구들은 10년, 15년 후가 아닌 지금 당장 실질적인 영향을 미칠 수 있도록 말입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Philips/The_Future_of_Medicine_Is_Already_Here_AI,_Connected_Care_&___wYmHA5Pr6_g.md`

**273. [Why Lived Experience Matters in Digital Health & AI | Healthcare Leadership | JPM 2026](https://www.youtube.com/watch?v=NJzIYjcnYig)** — Philips · 수요기업·기타 · NL · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 좋은 아침이에요. 저희는 샌프란시스코에서 열리는 JP모건 컨퍼런스 셋째 날에 와 있습니다 . 저는 디지털 헬스, 인공지능, 그리고 임상 의사 결정의 교차점에 있는 기타 나아르 박사님과 함께하고 있습니다. 우선 함께해 주셔서 감사합니다. 음, 청중 여러분께 자기소개를 부탁드리는 게 어떨까요? 확신하는. 크리스틴, 우선 초대해 주셔서 감사합니다 . 제 이력은 최고 의료 책임자, 기술 전문가를 거…
- B5 리더십·CDO/CAIO: 그리고 리더십 차원에서는 스스로 계속 배우는 것뿐만 아니라 팀으로부터도 배워야 한다는 것을 겸손하게 이해하는 것이 중요하다고 생각합니다.
- B1 디지털·AI 기술의 활용: 예측 분석이나 자연어 처리 등과 같은 용어 대신 생성형 AI, 에이전트형 AI와 같은 용어를 사용하기 시작했습니다.
- 수치 주장: 지금 JPM에서 이야기를 나누고 있는 만큼, 5년 후 가장 성공할 조직은 가장 자동화되고 AI가 가장 많은 기관이 아니라, AI와 같은 적절한 기술과 혁신을 활용하여 기업을 더욱 인간적이고 신뢰할 수 있게 만들고, 직원과 의료진이 지원받고 환자들이 안전하다고 느끼도록 하는 조직일 것입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Philips/Why_Lived_Experience_Matters_in_Digital_Health_&_AI_Healthca__NJzIYjcnYig.md`

---

## Pinecone


**274. [Search Like You Mean It: Semantic Search with NLP and a Vector Database](https://www.youtube.com/watch?v=7RF03_WQJpQ)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2021-11 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: 닐스 라이머스를 모시게 되어 정말 기쁩니다. 혹시 닐 지아드를 모르시는 분들을 위해 설명드리자면, 그는 NLP 연구자이자 문장 변환기(Sentence Transformers)의 창시자입니다. 이 분야에서 정말 획기적인 업적을 남겼 으며, 그의 문장 변환기 관련 연구는 espert.net에서 확인하실 수 있습니다. 또한, 그의 많은 연구 결과는 Hugging Face에서도 찾아볼 수 있는데, …
- B1 디지털·AI 기술의 활용: 동일한 클라우드 제공업체에서 Pinecone에 접속하면 속도 면에서 이점이 있고, 같은 지역에 있으면 지연 시간이 훨씬 짧아지는 등 많은 이점이 있습니다.
- B5 직무·역량 변화: 마지막으로 질문 시간으로 넘어가기 전에 한 가지 더 말씀드리자면, 저희는 현재 채용 중입니다.
- 수치 주장: 5억 개의 다국어 질의 응답 쌍을 사용하여 다국어 모델을 학습시킬 것입니다.
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/Pinecone/Search_Like_You_Mean_It_Semantic_Search_with_NLP_and_a_Vecto__7RF03_WQJpQ.md`

**275. [Where CyberSecurity Meets AI](https://www.youtube.com/watch?v=mWplVuntklI)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2022-12 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: hi my name is Peter someone I'm the CTO at expel please forgive the phone that's ring in the background is the hotel room so I don't actually know how anyone's calling me which is both amusing and someone just disturbing…
- B1 디지털·AI 기술의 활용: awesome and no dead hi guys and I'm the head of the detection group the r d group of the detection here in the reception point and our main product is email security but perception does a whole range of products for detection of any incoming traffic into the o…
- B2 파괴: 데이터 가용성: awesome and no dead hi guys and I'm the head of the detection group the r d group of the detection here in the reception point and our main product is email security but perception does a whole range of products for detection of any incoming traffic into the o…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Pinecone/Where_CyberSecurity_Meets_AI__mWplVuntklI.md`

**276. [Beyond Chatbots: Making an impact with AI on multiple fronts](https://www.youtube.com/watch?v=jMwptQSOeuo)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2023-08 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 안녕하세요 여러분, 정말 밝네요! 저는 테드 로드너입니다. 마이크로소프트 의 글로벌 스타트업 지원 프로그램인 마이크로소프트 스타트업에서 일하고 있습니다. 스타트업 창업자이시고 생성형 AI를 활용하는 데 저희가 어떻게 도움을 드릴 수 있는지 알고 싶으시다면, 앞쪽 마이크로소프트 부스에서 저와 동료들에게 문의해 주세요. 자, 그럼 홍보는 이쯤 하고, 오늘 패널 토론 주제인 챗봇을 넘어 다양한 측…
- B1 디지털·AI 기술의 활용: 인공지능 분야에서는 매우 안정적인 레고 블록을 만들었지만, 조립 방식에는 여전히 많은 창의성과 개발 가능성이 존재하며, 새로운 시대의 머신러닝 엔지니어들이 바로 그 부분을 연구하고 있다고 생각합니다.
- B7 성과: 운영효율: 그리고 기업을 진정으로 차별화하는 것은 운영 효율성을 20% 향상시킨 다음, 20% 더 향상시키는 방법을 찾아내는 기업이라고 생각합니다.
- 수치 주장: 저희는 4~5년 전 트위터에서 처음 벡터 스토어를 구축했고, 기본 알고리즘 개발에도 많은 기여를 했습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Pinecone/Beyond_Chatbots_Making_an_impact_with_AI_on_multiple_fronts__jMwptQSOeuo.md`

**277. [Launch Sooner: An integrated AI stack for faster deployment](https://www.youtube.com/watch?v=8dhOyt1dhjg)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2023-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 자, 이 나이트클럽과 여러분이 계신 곳은 패널 토론에 정말 완벽한 장소입니다. 저희 모두 이곳에 오게 되어 매우 기쁩니다. 이 패널 토론의 주제는 '더 빨리 출시하기'입니다. 저는 Matt Bornstein이고, Andreessen Horowitz의 파트너로서 AI 투자에 집중하고 있습니다. 조금 논란이 될 만한 주장으로 시작해 보겠습니다. 주제는 LLM 앱을 프로덕션 환경으로 배포하는 것입…
- B1 디지털·AI 기술의 활용: Parna 님, Arise의 공동 창립자로서 기존의 머신러닝 워크로드와 새로운 파운데이션 모델 기반 앱들이 실제 운영 환경에 배포되는 것을 많이 보셨는데요.
- B2 파괴: 데이터 가용성: 마지막으로, 데이터를 수집하여 모델을 재 구축하거나, 이 분야에서는 미세 조정 또는 개선이라고 부르는 작업을 수행하는 것은 머신러닝 1.0에서 흔히 볼 수 있었던 패턴이며, 새로운 분야에서도 마찬가지입니다.
- 수치 주장: 정말 멋진 데모, 정말 멋진 앱을 만들어서 트위터에 출시하고 수천 명의 사용자를 확보했다고 가정해 봅시다.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 코딩 에이전트
- 원문: `transcripts/channels/Pinecone/Launch_Sooner_An_integrated_AI_stack_for_faster_deployment__8dhOyt1dhjg.md`

**278. [Streamlining RAG Applications with Canopy](https://www.youtube.com/watch?v=d9QPDQ50B-A)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-01 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: a welcome oh thank you bear we have we have Joselyn James and bear uh all four of whom are pine cone people so they'll be monitoring the chat uh for any questions you have during the webinar but we're also going to have …
- B1 디지털·AI 기술의 활용: after you sign up for an account uh we also under the hood uh canopy uses open AI uh as its llm of choice so you'll have to sign up for an openai API key on openai doc.ai I'm not sure what the actual address is uh and then right now canopy only works with Text…
- B7 성과: 조직성과: .org link which is great without context uh it gives me incorrect information so it copies the title but uh chat PT does what's called a hallucination here so it tells me that it was written by Aus who we talked about before which is not true uh Tom Brown and …
- 수치 주장: after you sign up for an account uh we also under the hood uh canopy uses open AI uh as its llm of choice so you'll have to sign up for an openai API key on openai doc.ai I'm not sure what the actual address is uh and then right now canopy only works with Text…
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Pinecone/Streamlining_RAG_Applications_with_Canopy__d9QPDQ50B-A.md`

**279. [Pinecone Workshop: LLM Size Doesn't Matter — Context Does](https://www.youtube.com/watch?v=GkQ52svNUhM)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 지금 접속하시는 모든 분들께 인사드립니다. 로그인하시고 자리에 앉으실 때까지 30초 정도만 기다려 주시면 시작하겠습니다. 좋습니다, 시작해 볼까요? 계속해서 접속해주시는 분들이 계시네요. 정말 많은 분들이 참여해주셨습니다. 멋지네요! 채팅창에서 서로 인사 나누는 모습도 보기 좋습니다. 저는 파인콘의 그렉 호건입니다. PR 레고 와 저희 제품 매니저 한 분과 함께 이 온라인 워크숍…
- B1 디지털·AI 기술의 활용: 두 가지 핵심 사항은 Pine Cone을 사용하여 RAG P를 구축하고, 저희 LLM 최적화 플레이북을 확인해 보시라는 것입니다.
- B2 파괴: 데이터 가용성: 따라서 데이터 양이 적은 경우 모델이 사용할 수 있는 리소스가 매우 제한적이기 때문에 정확도가 매우 낮게 나타나는 것은 당연한 결과입니다.
- 수치 주장: 저희는 AI 서비스 회사로, 약 8년 동안 사업을 운영해 왔으며 주로 포춘 1000대 기업의 AI 도입을 가속화하는 데 집중하고 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/Pinecone/Pinecone_Workshop_LLM_Size_Doesn't_Matter_—_Context_Does__GkQ52svNUhM.md`

**280. [Production Ready RAG in Healthcare with Pinecone and Autoblocks](https://www.youtube.com/watch?v=93f7ZHPkpTk)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 좋아요. 좋아, 아룬, 준비됐어? 우리는 준비된 것 같아요. 자, 해봅시다. 괜찮은. 네, 여러분 모두 환영합니다. 아룬, 첫 번째 슬라이드를 올리려면 화면을 공유해 주세요. 괜찮은. 안녕하세요, 여러분. 오늘 웨비나에 오신 것을 환영합니다. 제 이름은 로리 슈와버 코헨입니다. 음, 파인콘의 개발자 옹호 담당자입니다. 오늘 저와 함께 해주신 분은 오토블록스의 CEO이자 공동 창립자인 하룬 차…
- B1 디지털·AI 기술의 활용: 오토블록스에서는 다양한 유형의 고객과 협력하고 있으며, RAG 시스템의 일반적인 사용 사례로는 금융 분야에서 개인 맞춤형 금융 자문 및 지원 제공, 전자상거래 분야에서 개인 맞춤형 제품 추천, 그리고 의료 분야에서 개인 맞춤형 치료 추천 및 환자 관리 등이 있습니다.
- B8 부정 성과: 보안·프라이버시: 의도 치 않은 개인 건강 정보(PHI) 노출 사고가 발생하더라도 보상을 받을 수 있으며, 데이터 유출 위험을 완화하고 시스템 전체의 데이터 무결성을 보장하며, AI 시스템의 안전성과 신뢰성에 대한 이해관계자의 신뢰를 구축할 수 있습니다.
- 수치 주장: 테스트 및 평가 프로세스 전체가 현재 매우 자동화되어 있고 선순환 구조처럼 작동한다고 말하고 싶지만, 사실은 세계 최고의 AI 제품 팀을 포함하여 수백 개의 AI 제품 팀과 이야기를 나눴습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Pinecone/Production_Ready_RAG_in_Healthcare_with_Pinecone_and_Autoblo__93f7ZHPkpTk.md`

**281. [RAG Brag with Andrew Lee of Shortwave](https://www.youtube.com/watch?v=xsb2FbU4YRA)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: Rag Bra Fine Toon의 새로운 라이브 스트림 이벤트에 오신 것을 환영합니다. 오늘은 차세대 AI 소프트웨어 개발의 어려움에 대해 창업자 및 엔지니어들과 이야기를 나누는 시간입니다. 저는 Pine Con의 Valia Gomez이고, 오늘은 Charway의 공동 창업자이자 CEO이신 Andrew Lee 님을 모셨습니다. Andrew 님, 안녕하세요. 잘 지내시죠? 저는 잘 지내고 있습…
- B1 디지털·AI 기술의 활용: 하지만 Shortwave의 가장 큰 장점은 LLM(로컬 메일 관리 시스템) 및 기타 최신 AI 기술의 강력한 기능을 이메일함에 통합하여 생산성을 향상시켜 준다는 점입니다.
- B7 성과: 운영효율: 하지만 Shortwave의 가장 큰 장점은 LLM(로컬 메일 관리 시스템) 및 기타 최신 AI 기술의 강력한 기능을 이메일함에 통합하여 생산성을 향상시켜 준다는 점입니다.
- 수치 주장: 앱 개발 플랫폼인 파이어베이스를 설립하셨고, 나중에 구글로 이직해서 3년 동안 회사를 성장시켜 오셨죠.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/Pinecone/RAG_Brag_with_Andrew_Lee_of_Shortwave__xsb2FbU4YRA.md`

**282. [RAG Brag with Mike Heap and Alex Rainey of My AskAI](https://www.youtube.com/watch?v=QxkvhBMOGAA)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 안녕하세요, AI 창업자 및 엔지니어들과 차세대 AI 소프트웨어 개발의 과제에 대해 이야기하는 Rag Brag 에피소드에 오신 것을 환영합니다. 저는 PineCon의 Valeria이고, 오늘은 MyAskAI의 창업자인 Mike와 Alex Rainy 두 분을 모셨습니다. 오늘은 MyAskAI가 대규모 언어 모델과 PineCon을 활용하여 기업들이 더욱 복잡한 질문에 답변하고 제품 개선을 위한 …
- B1 디지털·AI 기술의 활용: 예를 들어 500개의 웹페이지로 이루어진 웹사이트 전체를 스크래핑한다고 해도, 그중에서 단 세네 개의 단락만 추출하여 AI 모델에 입력하고, 이를 LLM(Learning Language Model)에 입력하여 질문에 답하도록 하는 것입니다.
- B2 파괴: 소비자 행동·기대: 오늘은 MyAskAI가 대규모 언어 모델과 PineCon을 활용하여 기업들이 더욱 복잡한 질문에 답변하고 제품 개선을 위한 실질적인 피드백을 수집할 수 있도록 지원함으로써 고객 지원을 어떻게 혁신하고 전반적인 고객 경험을 개선하고 있는지에 대해 이야기해 보겠습니다.
- 수치 주장: 특히 고객이 2분 안에 AI 챗봇을 구축할 수 있도록 지원하는 방법에 대해 자세히 알아보고 싶습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Pinecone/RAG_Brag_with_Mike_Heap_and_Alex_Rainey_of_My_AskAI__QxkvhBMOGAA.md`

**283. [Bits & Bytes: Vector Augmented Labeling & Classification](https://www.youtube.com/watch?v=RuJGoV87Et4)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 네, 모두 참여해 주셔서 감사합니다. 이것은 저희 첫 ​​번째 Bits and Bites 세션입니다. 오늘은 벡터 증강 레이블링 분류에 대해 이야기해 보겠습니다. 저는 Pine Cone의 제품 마케터인 Gibs Cullen이고, 함께하는 Christopher Amada는 선임 소프트웨어 엔지니어입니다. 여러분과 이야기 나눌 수 있어서 기쁘고, 오늘 여러분께 새로운 것을 조금이나마 알려드릴 수…
- B2 파괴: 데이터 가용성: 먼저, 첫 번째 질문은 비정형 데이터 세트에서 메타데이터를 어떻게 추출하고, 추출한 메타데이터를 데이터 자체와 결합하여 벡터 검색 결과를 최적화하는 방법, 그리고 데이터 세트 자체에 대해서만 벡터 검색을 수행하는 것과 비교했을 때 어떤 차이가 있는지에 대한 것입니다.
- B1 디지털·AI 기술의 활용: 더 나아가, 아름다운 RAG 시스템을 구축하려는 경우에도 머신러닝은 여전히 좋은 결과를 얻기 위해 많은 노력을 기울여야 합니다.
- 수치 주장: 깁스는 몇 년, 저는 1년 동안 이곳에 있었는데, 파인콘을 비롯한 전체 생태계에서 AI 사용 사례가 쏟아져 나오는 양은 놀라울 정도입니다.
- 교량: Avenue 1 동적역량 · 기술: 검색·RAG
- 원문: `transcripts/channels/Pinecone/Bits_&_Bytes_Vector_Augmented_Labeling_&_Classification__RuJGoV87Et4.md`

**284. [Getting GenAI Right – A live panel discussion with Sarah Wang, Edo Liberty, and Harrison Chase](https://www.youtube.com/watch?v=A0jOmaPdKM4)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-06 · en · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: uh let me introduce uh our moderator Sarah Wong from Andre and Horwitz General partner thank you so much big round of applause to Sarah who's going to tell you what's going on awesome thanks Mike thanks for having me um …
- B1 디지털·AI 기술의 활용: uh let me introduce uh our moderator Sarah Wong from Andre and Horwitz General partner thank you so much big round of applause to Sarah who's going to tell you what's going on awesome thanks Mike thanks for having me um very excited to kick off the panel um so…
- B8 부정 성과: 보안·프라이버시: uh let me introduce uh our moderator Sarah Wong from Andre and Horwitz General partner thank you so much big round of applause to Sarah who's going to tell you what's going on awesome thanks Mike thanks for having me um very excited to kick off the panel um so…
- 수치 주장: uh let me introduce uh our moderator Sarah Wong from Andre and Horwitz General partner thank you so much big round of applause to Sarah who's going to tell you what's going on awesome thanks Mike thanks for having me um very excited to kick off the panel um so…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Pinecone/Getting_GenAI_Right_–_A_live_panel_discussion_with_Sarah_Wan__A0jOmaPdKM4.md`

**285. [The Future of Multi-Modal Search](https://www.youtube.com/watch?v=v5b-3-4NibI)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-07 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 안녕하세요 여러분, 멀티모달 검색의 미래에 대한 프레젠테이션에 오신 것을 환영합니다. 어디서 오셨는지 잘 모르겠지만, 몇 가지 질문을 보니 아키텍트분들과 제품 담당자분들이 계신 것 같네요. 기술적인 배경이 있으신 분들도 계시겠지만, 기술적인 배경이 없으셔도 전혀 문제없습니다. 모든 분들이 무언가를 배우실 수 있도록 이 프레젠테이션을 준비했습니다. 그럼 시작하겠습니다. 이것은 Pine Cone…
- B1 디지털·AI 기술의 활용: 기본적으로 사용자의 요청과 이미지, 비디오 등의 데이터를 백엔드로 전송하면 백엔드에서 처리되고, 백엔드에서 전송된 API 응답을 처리하여 공개된 Google Cloud Storage URL을 사용하여 이미지와 비디오를 제공합니다.
- B8 부정 성과: 보안·프라이버시: 개인 맞춤형 마케팅을 만들 수도 있고, 저작권 보호, 식료품 배달, 콘텐츠 검열, 사기 탐지 등 텍스트, 이미지, 비디오를 포함하는 모든 것을 만들 수 있습니다.
- 수치 주장: PineCone 서버리스는 분리형 아키텍처로, 저렴한 Blob 스토리지에 벡터를 저장하여 모든 규모에서 최대 50%의 비용 절감을 제공합니다.
- 교량: Avenue 1 동적역량 · 기술: 검색·RAG
- 원문: `transcripts/channels/Pinecone/The_Future_of_Multi-Modal_Search__v5b-3-4NibI.md`

**286. [RAG Brag with Alex Bowcut from Hyperleap](https://www.youtube.com/watch?v=JbuliMwGraQ)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-09 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: and Welcome to our 10th episode of rag bra if you are joining us today for the very first time this is our Series where we talk with industry leaders about the experiences and insights H in building AI products I'm Valer…
- B1 디지털·AI 기술의 활용: and Welcome to our 10th episode of rag bra if you are joining us today for the very first time this is our Series where we talk with industry leaders about the experiences and insights H in building AI products I'm Valeria Gomez from Pine con and I got my awes…
- B5 직무·역량 변화: and Welcome to our 10th episode of rag bra if you are joining us today for the very first time this is our Series where we talk with industry leaders about the experiences and insights H in building AI products I'm Valeria Gomez from Pine con and I got my awes…
- 수치 주장: and Welcome to our 10th episode of rag bra if you are joining us today for the very first time this is our Series where we talk with industry leaders about the experiences and insights H in building AI products I'm Valeria Gomez from Pine con and I got my awes…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 칩·하드웨어
- 원문: `transcripts/channels/Pinecone/RAG_Brag_with_Alex_Bowcut_from_Hyperleap__JbuliMwGraQ.md`

**287. [RAG Brag with Peter Werry from Unblocked](https://www.youtube.com/watch?v=5Rq7AGfJLCE)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-09 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: right hi everyone and welcome to episode 11 of the rag brag which is pine cone Series where we talk with Founders and Engineers about their experiences and any insights that they have from building AI software so hi I'm …
- B1 디지털·AI 기술의 활용: right hi everyone and welcome to episode 11 of the rag brag which is pine cone Series where we talk with Founders and Engineers about their experiences and any insights that they have from building AI software so hi I'm bear I lead develop relations over at Pi…
- B8 부정 성과: 보안·프라이버시: right hi everyone and welcome to episode 11 of the rag brag which is pine cone Series where we talk with Founders and Engineers about their experiences and any insights that they have from building AI software so hi I'm bear I lead develop relations over at Pi…
- 수치 주장: right hi everyone and welcome to episode 11 of the rag brag which is pine cone Series where we talk with Founders and Engineers about their experiences and any insights that they have from building AI software so hi I'm bear I lead develop relations over at Pi…
- 교량: — · 기술: 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Pinecone/RAG_Brag_with_Peter_Werry_from_Unblocked__5Rq7AGfJLCE.md`

**288. [The Magic of Multilingual Search with Pinecone Serverless and Inference](https://www.youtube.com/watch?v=moHIBWZiYdY)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-09 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: all right welcome everybody uh thanks for coming today uh to well this webinar is going to be on the magic of multilingual search and I'm really excited to help everybody learn about using and applying multilingual searc…
- B1 디지털·AI 기술의 활용: all right welcome everybody uh thanks for coming today uh to well this webinar is going to be on the magic of multilingual search and I'm really excited to help everybody learn about using and applying multilingual search to whatever you might be working on th…
- B4 민첩성·양손잡이: all right welcome everybody uh thanks for coming today uh to well this webinar is going to be on the magic of multilingual search and I'm really excited to help everybody learn about using and applying multilingual search to whatever you might be working on th…
- 수치 주장: all right welcome everybody uh thanks for coming today uh to well this webinar is going to be on the magic of multilingual search and I'm really excited to help everybody learn about using and applying multilingual search to whatever you might be working on th…
- 교량: — · 기술: 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Pinecone/The_Magic_of_Multilingual_Search_with_Pinecone_Serverless_an__moHIBWZiYdY.md`

**289. [Build Real-Time RAG with Pinecone, Databricks, and Fivetran](https://www.youtube.com/watch?v=wvwdWBeH6YE)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2024-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 여러분, Pine Cone, Data Bricks, 그리고 Five Tran이 함께하는 이번 웨비나에 참석해 주셔서 정말 감사합니다. 저는 실시간 데이터 분석(RAG)을 구축하고 있습니다. 이번 웨비나에서는 Pine Cone의 작동 방식, 임베딩, Data Bricks 및 모델 호스팅에 대해 간략히 살펴보고, Five Tran을 사용하여 데이터 레이크에서 데이터를 가져와 Data Bricks…
- B1 디지털·AI 기술의 활용: 저희는 분석가들로부터 클라우드 데이터베이스 관리 시스템과 데이터 과학 및 머신 러닝 분야의 리더로 인정받고 있습니다.
- B2 파괴: 데이터 가용성: 반대로 데이터 양이 매우 적은 경우에는 더 큰 배치 크기를 사용할 수도 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Pinecone/Build_Real-Time_RAG_with_Pinecone,_Databricks,_and_Fivetran__wvwdWBeH6YE.md`

**290. [Secure your RAG pipelines with fine grained authorization using SpiceDB](https://www.youtube.com/watch?v=S6xJ0Kkd7ss)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2025-09 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요, 반갑습니다. 네, 오늘 웨비나에 많은 분들이 참여하고 계신 것 같습니다 . 음, 헨이 언급했듯이 우리는 RAG 파이프라인을 안전하게 보호하는 방법과 역할 및 권한에 대해 배우고, 그것이 얼마나 어려운 일인지 알아보기 위해 여기에 왔습니다. 채팅창에 녹화 여부에 대한 질문이 있는 것 같네요. 저희는 녹음하고 있습니다. 이어서 녹음 파일을 보내드리겠습니다. 약 일주일 후 저희 유튜브…
- B1 디지털·AI 기술의 활용: 사용자가 접근 권한이 있는 경우에만 응답을 받고, 그렇지 않으면 해당 질문이 LLM(Limited Logistics Manager)으로 전달되어 응답을 받게 됩니다.
- B5 조직구조 변화: 실제로 각 팀은 서로 다른 인증 방식을 사용할 수 있으며, Spice DB와 같은 중앙 집중식 권한 부여 시스템을 사용할 수도 있습니다.
- 수치 주장: 업계는 약 20~30년 전에 역할 기반 접근 제어라는 것이 도입되면서 약간의 변화를 겪었습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Pinecone/Secure_your_RAG_pipelines_with_fine_grained_authorization_us__S6xJ0Kkd7ss.md`

**291. [AI/Agents in Production with Delphi, Seam AI, and APIsec](https://www.youtube.com/watch?v=OSvDO9VtypU)** — Pinecone · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: [음악] 좋아요, 여러분. 오늘 저녁 사우스 비치 요트 클럽의 멋진 전망을 감상하며 저희와 함께해 주셔서 진심으로 감사드립니다. 오늘 밤, 아주 멋진 세션이 있어요. 오늘 저희와 함께 해주신 세 분의 멋진 분들을 소개합니다. 그럼, 더 이상 지체하지 않고 바로 시작하겠습니다. 궁금한 점이 있으시면 질의응답 시간에 질문해 주세요 . 그럼 이제 패널 여러분께서 자기소개를 해주시도록 하겠습니다. …
- B1 디지털·AI 기술의 활용: 어, 그리고 이제 클라우드 소프트웨어와 서비스형 소프트웨어(SaaS)는 사라졌고, 우리는 새로운 AI 기반 솔루션으로 전환하고 있죠.
- B7 성과: 운영효율: 우리가 중요한 순간을 포착하고 캠페인을 실행하는 등, 실질적인 조치를 취하는 측면을 고려하기 시작했을 때, 이는 결국 투자 수익률( ROI) 부분과도 연결됩니다.
- 수치 주장: 그래서 어쨌든, 지난 10년 동안 제품 개발이나 스타트업에 대한 조언은 대체로 "기능 처럼 보이는 아주 구체적인 것을 만들어서 시장에 내놓고, 그 다음 쐐기 모양의 구조물을 만들어서 확장해 나가라"는 것이었습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Pinecone/AIAgents_in_Production_with_Delphi,_Seam_AI,_and_APIsec__OSvDO9VtypU.md`

---

## Qdrant


**292. [Deep research is just really smart rag w/ Robert Caulk](https://www.youtube.com/watch?v=wAcWJtWQVN8)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2025-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 오늘 잘 지내시나요? 벡터 스페이스 토크 에피소드에 함께해 주셔서 감사합니다. 오늘은 Emergent Methods의 Rob Cock 님과 함께합니다. 안녕하세요 Rob, 잘 지내시죠? 네, 저는 Emergent Methods의 CEO인 Robert Coul입니다. 저희는 AQ News라는 제품을 제공하고 있습니다. 오늘은 딥 리서치에 대한 흥미로운 이야기를 나눠볼까요? …
- B1 디지털·AI 기술의 활용: Steam ID를 기반으로 게임별 알림을 추가하고, 이를 뉴스로 활용하여 해당 게임과 관련된 새로운 소식을 수집하고, 검색 추천 및 발견 기능을 구축하고, 게임 컨시어지( AI 에이전트 역할)를 개발하고 있습니다.
- B8 부정 성과: 보안·프라이버시: 그래서 저는 친구분처럼 어느 쪽이 편향되어 있는지, 어떤 편견을 가지고 있는지, 혹은 차별받고 있는지에 대한 선입견을 가진 사람들에게 이 기사들을 보내주곤 합니다.
- 수치 주장: 2025년에 효과적인 AI 애플리케이션을 구축하기 위한 역전파란 무엇일까요?
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 코딩 에이전트
- 원문: `transcripts/channels/Qdrant/Deep_research_is_just_really_smart_rag_w_Robert_Caulk__wAcWJtWQVN8.md`

**293. [Vector Space Talk: Video Recommendations with Twelve Labs](https://www.youtube.com/watch?v=dHwhQUdH0IY)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2025-05 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 벡터 공간 토크의 새로운 에피소드에 오신 것을 환영합니다 . 오늘 저는 리시 야다브 씨와 함께합니다 . 리시, 오늘 잘 지내고 있어요? 네, 저는 괜찮습니다. 어떻게 지내세요? 엄청난. 함께해 주셔서 정말 감사합니다. 그리고 리시, 자기소개 좀 해주시겠어요? 어디 출신인지, 무슨 일을 하는지, 그리고 재미있는 사실 하나 알려주세요. 안녕하세요, 저는 인도 출신이지만 현재는 베를린에 있으며 1…
- B1 디지털·AI 기술의 활용: 따라서 12개의 앱 플레이그라운드에서 12개 앱의 API 키를 얻을 수 있으며, 쿼드런트 클라우드 클러스터를 생성하여 쿼드런트 호스트와 API 키를 얻을 수도 있습니다.
- B2 파괴: 데이터 가용성: 그러니까 첫 번째 단계는 비디오 콘텐츠 데이터를 수집하고, 그 데이터를 변환해서 데이터베이스에 저장하는 것이고, 두 번째 단계는 응용 프로그램 실행 부분입니다.
- 수치 주장: 그러다가 1월에 페가수스 1.2 버전을 출시했는데, 이제 재생할 수 있는 동영상 길이가 1시간으로 늘어났습니다.
- 교량: Avenue 1 동적역량 · 기술: 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Qdrant/Vector_Space_Talk_Video_Recommendations_with_Twelve_Labs__dHwhQUdH0IY.md`

**294. [Operationalizing GraphRAG: Lettria’s Scalable Architecture with Neo4j and Qdrant](https://www.youtube.com/watch?v=3guLRa5yQEk)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2025-07 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 네, 제 화면이 이미 보이시죠? 음, 저는 그 부분에서 좀 어려움을 겪었어요. 쿼드런트 웨비나에 오신 것을 환영합니다. 안녕하세요, 저는 캣퍼입니다. 저는 Quadrant에서 선임 개발자 옹호 담당자로 일하고 있습니다. 오늘은 정말 좋은 분들과 함께하게 되어 기쁩니다. 드디어 아주 흥미로운 주제에 대해 이야기해 주실 손님들을 모셨는데요, 아마도 우리 모두가 최근에 관심을 가졌던 주제일 겁니다…
- B1 디지털·AI 기술의 활용: 분명히 검색 증강 생성에 대해 이야기하자면, 밀집 검색은 이를 구현하기 위해 사용해 온 기본 방법일 수 있으며, 검색 증강 생성은 LLM 기반 애플리케이션을 구축하는 사람들에게 이미 일반적인 패턴입니다.
- B2 파괴: 데이터 가용성: 자, 이제 벡터 데이터베이스와 그래프 데이터베이스를 결합하여 데이터를 수집하고 생성하는 과정에서 우리가 직면했던 어려움에 대해 이야기해 보겠습니다.
- 수치 주장: 지난 1년, 3 년 동안 모델들이 상당히 개선되었고, 블랙박스 효과와 설명력 부족 문제도 있지만, 이미 이 부분을 아주 잘 정리해 주셨기 때문에 제가 이 부분에 대해 더 쉽게 관심을 가질 수 있을 것 같습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/Qdrant/Operationalizing_GraphRAG_Lettria’s_Scalable_Architecture_wi__3guLRa5yQEk.md`

**295. ["Mastering Relevance in Search" with Doug Turnbull & Trey Grainger](https://www.youtube.com/watch?v=oiX7F1qi62Y)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2025-08 · en · 5/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Hey everyone and welcome to Vector Space Talk. Today I am joined by my wonderful colleague Jenny and Trey as well as Doug and they're going to be talking to us about AI powered search. Hey Jenny, how you doing today? doi…
- B1 디지털·AI 기술의 활용: Yeah, one thing one thing I think that happens because the embeddings are just so intertwined in the machine learning and Python ecosystem that is so ubiquitous.
- B7 성과: 조직성과: uh But if you're using LLMs, especially if you're having LLMs do simpler decisions, like which of these do you prefer, then you can sometimes get by, you can sometimes use pairwise evaluation methods.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Qdrant/Mastering_Relevance_in_Search_with_Doug_Turnbull_&_Trey_Grai__oiX7F1qi62Y.md`

**296. [Qdrant & Neo4j - Relevant and Diverse Vector Search - MMR and Context Engineering](https://www.youtube.com/watch?v=W58itLg3qWA)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2025-09 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 오늘 밤 쿼드런트와 네오4j 이벤트에 참석해주신 모든 분들께 감사드립니다. 오늘 밤 쿼드런트 측면에서 MMR이라는 것에 대해 이야기해 보겠습니다. MMR은 기본적으로 검색 결과를 다양화하는 방법입니다 . 자, 그럼 본격적으로 이야기하기 전에 , 현재 진행 중인 해커톤에 대해 먼저 알려드리고 싶습니다 . 이건 제가 열어봐도 될까요? 어디 보자 . 이것은 '봇의 틀을 벗어나 생각하기' …
- B1 디지털·AI 기술의 활용: 로컬 환경에서 클라우드 환경으로 전환할 준비가 되면, API 키를 제공하는 단 한 줄의 코드만으로 전환할 수 있습니다.
- B4 가치네트워크·생태계: 하지만 이 경우에는 제가 그 계층을 기반으로 지식 그래프를 구축했는데, 그 그래프는 전체 생태계가 어떻게 연결되어 있는지 명확하게 보여줍니다.
- 수치 주장: 그래서 저희는 완전히 온라인으로 진행되는 '봇의 틀을 깨는 해커톤'을 도입했으며, 제출 마감일은 9월 16일입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 추론 최적화 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Qdrant/Qdrant_&_Neo4j_-_Relevant_and_Diverse_Vector_Search_-_MMR_an__W58itLg3qWA.md`

**297. [Modernizing Legacy Search with Semantic Retrieval in the AI Era | Qdrant vs Elastic Demo](https://www.youtube.com/watch?v=-IHb9Dv8OQQ)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2026-02 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화
- 개요: 모두 환영합니다. 와주셔서 감사합니다. 제 이름은 네이선입니다. 안녕하세요, 저는 쿼드런트에서 개발자 관계 엔지니어로 일하고 있습니다. 오늘은 인공지능 시대에 맞춰 검색 및 정보 추출 방식을 현대화하는 것에 대해 이야기해 보겠습니다 . 음, 이걸 전체 화면으로 만들어 보려고 해요. 좋아요, 좋습니다. 자, 간단한 일정 안내입니다. 그럼 자기소개를 좀 해 볼까요? 방금 그렇게 했어요. 이제 그…
- B1 디지털·AI 기술의 활용: 예를 들어 텍스트 임베딩을 테스트할 때 OpenAI의 Quadrant에서 V3 small 모델을 사용하고, 그다음 Elastic Search에서 384차원의 LLM V3 mini 모델을 사용해서 테스트하면, Elastic Search 결과가 형편없다고 생각할 수 있어요.
- B8 부정 성과: 보안·프라이버시: 음, 대략 두 가지 시나리오가 있는데, 하나는 실제 정답을 찾기가 정말 어렵고 이상적인 경우이고, 다른 하나는 그렇지 않은 경우인데, 이 경우에는 무차별 대입 방식의 인공신경망 검색을 사용하는 비정답 방식을 택할 수 있습니다.
- 수치 주장: 그 사람이 2030년까지 마이크로소프트에서 C와 C++ 코드를 모두 없애고 Rust로 대체하는 게 목표라고 했더라고요.
- 교량: — · 기술: 검색·RAG · 추론 최적화
- 원문: `transcripts/channels/Qdrant/Modernizing_Legacy_Search_with_Semantic_Retrieval_in_the_AI___-IHb9Dv8OQQ.md`

**298. [Qualcomm  | Practical Patterns for On-Device GenAI | Alan Zhu](https://www.youtube.com/watch?v=FlAmmVSYbZY)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 기기 내 생성형 AI를 개발하면서 발견한 실용적이고 흥미로운 패턴들에 대해 이야기하게 되어 매우 기쁩니다. 네 , 정말 기대되네요. 이번 발표에서는 NPU 기반 온디바이스 생성형 AI 구축이 어떻게 더 많은 흥미로운 새로운 활용 사례를 열어줄 수 있는지에 대한 멋진 데모를 보여드리고, 퀄컴 AI 허브에 대해서도 자세히 소개하겠습니다. 그럼 시작해 볼까요? 최근 관찰 결과, 현재 …
- B1 디지털·AI 기술의 활용: 따라서 이는 기기에서 실행되는 생성형 AI 에이전트를 개발할 때 MPU를 활용하면 배터리 소모를 크게 줄일 수 있다는 것을 보여줍니다.
- B2 파괴: 소비자 행동·기대: 앱에 직접 배포하여 만족스러운 사용자 경험인지 확인할 수도 있고, 퀄컴 AI 허브 워크벤치를 사용하여 모델을 비교하고 성능을 검증하고 다양한 기기에서 프로파일링할 수도 있습니다.
- 교량: — · 기술: 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/Qdrant/Qualcomm_Practical_Patterns_for_On-Device_GenAI_Alan_Zhu__FlAmmVSYbZY.md`

**299. [Vector Space Meetup 2026 Highlights](https://www.youtube.com/watch?v=EEXUuI6ZSu8)** — Qdrant · 데이터·컨텍스트·거버넌스 · DE · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 긍정적인 메모 프로. 그래서 오늘 밤 나는 그곳에서 내 목소리를 듣게 된다. 저쪽으로 조금만 걸어가 볼게요. 오늘 밤 이렇게 소규모 벡터 공간 모임에 오신 것을 진심으로 환영합니다. 이번 모임은 에이전트 시대의 데이터 검색에 관한 것입니다. 제 이름은 예니아이고, 제니라고 불러주셔도 괜찮아요. 저기 아니면 저기였을 텐데, 잊어버렸어. 저는 오늘 이 행사를 주최하는 쿼드런트라는 회사의 선임 개…
- B1 디지털·AI 기술의 활용: 즉, 합의 연산, 분산 배포, API 부분은 모두 클라우드에 존재하고, 엣지 부분은 파이썬 API, 러스트 API 등 원하는 언어를 통해 스토리지에 직접 접근할 수 있습니다.
- B2 파괴: 데이터 가용성: 그리고 시스템이 스테이징 환경에 배포되면 사용자 데이터를 수집해서 평가 데이터 세트에 넣고, 필요하다면 지속적인 평가를 통해 시스템이 어떻게 발전하는지, 그리고 발전이 필요한지 확인할 수 있습니다.
- 수치 주장: 그리고 마지막으로, 모든 질문과 질문 방법을 정리했으니 이제 2026년에 구축하고 있는 쿼드런트 로드맵을 좀 살펴볼 수 있겠습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Qdrant/Vector_Space_Meetup_2026_Highlights__EEXUuI6ZSu8.md`

---

## Reckitt


**300. [Q3 Trading and Strategic Update](https://www.youtube.com/watch?v=zN3xR9s4uZM)** — Reckitt · 수요기업·기타 · UK · 2023-10 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 3 분기 실적 및 전략 업데이트에 오신 것을 환영합니다. 저는 크리스 릭입니다. 오늘 여러분과 이야기 나눌 수 있어 기쁩니다. 지난 4년 동안 많은 일들이 있었습니다. 시장 전반과 우리 사업 내부에서 상당한 변동성과 많은 기회, 그리고 도전을 경험했습니다. 현재 레코드는 매우 흥미로운 시점에 있습니다. 3분기 실적 업데이트의 주요 내용을 말씀드리고, 이 훌륭한 회사의 미래에 대한…
- B4 가치제안 변화: 또한, 우리는 우수한 매출총이익률을 바탕으로 이러한 성장을 이루어냈으며, 이는 우리 수익 모델의 지속적인 강점을 입증하는 것입니다.
- B7 성과: 조직성과: 경쟁력 있고 회복력 있는 저희 사업은 지속 가능한 수익성 있는 성장과 최고의 주주 수익률을 제공할 준비가 되어 있습니다.
- 수치 주장: 위생 및 건강 포트폴리오는 판매량 증가에 힘입어 6.7%라는 매우 강력한 성장을 달성했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Reckitt/Q3_Trading_and_Strategic_Update__zN3xR9s4uZM.md`

**301. [JP Morgan Consumer CEO Series: An interview with Kris Licht, CEO](https://www.youtube.com/watch?v=cAT6AqBk_-k)** — Reckitt · 수요기업·기타 · UK · 2025-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 어서 오세요, 잠시 기다려 주셔서 감사합니다. 본 전화 회의 및 질의 응답 시간은 모두 녹음되어 JP Morgan의 고객들에게 제공될 예정임을 모든 참가자 여러분께 알려드립니다. 기업이 프레젠테이션을 진행하는 경우, 녹화된 영상은 해당 기업의 웹사이트에 게시될 수도 있습니다. 본 통화에서 외부 연사가 표명하는 견해와 의견은 해당 연사의 것이며 JP Morgan의 견해가 아닙니다. 본 전화 회…
- B4 가치네트워크·생태계: 사실 저희 의료 사업은 주로 유럽이나 멕시코 시설에 의존했는데, 이는 민첩한 공급망도 아니고 충분히 탄력적이지도 않았습니다 .
- B2 파괴: 경쟁구도: 우리의 주요 경쟁사 중 하나 , 아니 사실 여러 주요 경쟁사들이 북미 지역에서 영업 실행 능력이 매우 뛰어나며, 우리는 그 점을 높이 평가합니다.
- 수치 주장: 하지만 만약 우리가 지난 12개월 동안 우리 조직이 이뤄낸 일들을 되돌아본다면, 회사 구조조정, 사업부 분할, 전략적 전환, 그리고 시장에서의 실행력 가속화를 가능하게 한 유일한 이유는 바로 이러한 노력 덕분이라고 생각합니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Reckitt/JP_Morgan_Consumer_CEO_Series_An_interview_with_Kris_Licht,___cAT6AqBk_-k.md`

**302. [Reckitt - Half Year 2025 Results](https://www.youtube.com/watch?v=KP7oflfrcMI)** — Reckitt · 수요기업·기타 · UK · 2025-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 오늘. 완벽한. 시작해 볼까요? 안녕하세요 여러분. 네, 라켓의 2025년 상반기 실적 발표에 참석해 주셔서 감사합니다. 저는 닉 애쉬워스입니다. 저는 렉킷에서 투자자 관계를 담당하고 있으며, 이렇게 직접 와주셔서 정말 반갑습니다 . 오늘 온라인에 접속하신 분들이 꽤 많다는 것도 알고 있습니다. 자, 시작하기 전에 미래 예측 정보와 관련된 일반적인 면책 조항에 대해 말씀드리겠습니다. 오늘 저…
- B7 성과: 운영효율: 조정 영업이익은 매출 증가율을 크게 웃도는 7% 증가를 기록했는데, 이는 효율성 개선과 성장 촉진 프로그램의 비용 절감 효과를 반영한 ​​것입니다 .
- B7 성과: 조직성과: 라이솔 공기 살균제는 상반기 동안 700bp(베이시스 포인트) 이상의 시장 점유율 상승을 기록하며 해당 카테고리를 선도하고 있으며, 라이솔 세탁 살균제 또한 약 500bp의 시장 점유율 성장을 보이며 두 제품 모두 북미 지역에서 라이솔의 가정 시장 침투율 향상에 기여했습니다 .
- 수치 주장: 핵심 음반 매출은 2분기에 5.3% 증가했으며, 상반기 전체로는 4.2% 증가했습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Reckitt/Reckitt_-_Half_Year_2025_Results__KP7oflfrcMI.md`

**303. [Reckitt Full Year Results 2025](https://www.youtube.com/watch?v=ExpojFs6mCg)** — Reckitt · 수요기업·기타 · UK · 2026-03 · en · 5/8블록 · `ax_core`/`washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: So, good morning everybody and thank you for joining us for Reckitt's full year 2025 results presentation. I'm Nick Ashworth. I head investor relations here at Reckitt. So, before we start, can I draw your attention to t…
- B7 성과: 조직성과: This has been driven by continued gross margin expansion which includes mix benefits from continued outperformance in self-care and intimate wellness.
- B4 가치네트워크·생태계: Our priority continues to be investing in organic growth as we've done in 2025 with a step up in investment behind our supply chain and R&amp;D capabilities.
- 수치 주장: Core Reckitt net revenue grew 5.2% ahead of our improved half-year guidance of above 4%.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Reckitt/Reckitt_Full_Year_Results_2025__ExpojFs6mCg.md`

---

## Replit


**304. [Replit Tech Talks: December, 2024](https://www.youtube.com/watch?v=dtuwxIJrnS0)** — Replit · 에이전트·개발도구 · US · 2025-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 제가 듣기로는 가벼운 이슬비에도 불구하고 바라의 교통 체증을 뚫고 와주셔서 정말 감사합니다. 오늘 밤 이렇게 와주신 모든 분들께 진심으로 감사드립니다. 저희 새 사무실에서 처음으로 진행하는 테크 토크인데, 정말 기대 되는 자리입니다. 솔직히 말씀드리면, 제 나이는 밝히고 싶지 않지만, 웹의 발전을 제대로 경험하지 못해서 아쉬웠습니다. 어쩌면 이번 테크 토크가 제 커리어에서 가장 중요한 순간이…
- B1 디지털·AI 기술의 활용: 실제 운영 환경에서 작동하는 앱을 구축하려면 API 키가 필요하고 타사 서비스와 통합해야 하는데, 에이전트는 이러한 정보를 관리하고 사용자에게 비밀 키를 요청하여 환경에 통합할 수도 있습니다.
- B7 성과: 운영효율: 그리고 계속 실행하면 기본적으로 실행당 최대 50%까지 비용을 절감할 수 있었습니다.
- 수치 주장: 2017년에 오픈 AI가 AI 5를 출시했는데, 그 AI가 도타에서 젠보다 더 잘한다는 사실이 밝혀졌죠.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 추론 최적화
- 원문: `transcripts/channels/Replit/Replit_Tech_Talks_December,_2024__dtuwxIJrnS0.md`

**305. [Alex Hormozi’s New Playbook: Entrepreneurship in the Age of AI](https://www.youtube.com/watch?v=6Ait5R-3-lI)** — Replit · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 오늘 여러분께 다섯 가지 일을 알려드리겠습니다. 그중 사업 규모를 세 배로 늘릴 수 있는 일은 단 5초면 충분합니다. 크로모시봇을 깔때기 안에 넣을 수 있을지 궁금하네요 . 보세요, 퍼널을 분석하고 제안을 해줄 수 있는 봇이 있다면 정말 유용할 거예요. 각 페이지의 사진을 찍습니다. 네, 맞아요. 그리고 나서 그냥 낙서를 해요. 응. 그러고 나서 " 제안 관련해서 문제가 있는 것 같습니다."…
- B1 디지털·AI 기술의 활용: 제가 그 프랑스 사람을 아는 건 아니지만, 구글이 귀 기울이는 그 프랑스 전문가가 있었는데, 그는 기본적으로 LLM(법학 석사)이 AGI(인공 일반 지능)에 완전히 진입하는 건 불가능하다고 말했어요.
- B7 성과: 조직성과: 저는 "하지만 연간 100만 달러와 1억 달러 사이에는 엄청난 격차가 있는데, 제 생각에는 기업 가치의 상당 부분이 사모 시장에서 창출되거든요.
- 수치 주장: 만약 90일이나 60일 기간 내에 무이자 현금을 얻을 수 있다면, 같은 개념을 확장해서 적용할 수 있을 겁니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Replit/Alex_Hormozi’s_New_Playbook_Entrepreneurship_in_the_Age_of_A__6Ait5R-3-lI.md`

**306. [Inside Replit Agent with a lead AI engineer](https://www.youtube.com/watch?v=bJMriY-pqPE)** — Replit · 에이전트·개발도구 · US · 2025-12 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: I've always known I wanted to be a software engineer my entire life. My dad was an engineer. I wrote my first line of code when I was six. I want to work on this challenging problem and I don't know how to do it. But the…
- B1 디지털·AI 기술의 활용: And so recently launched by the time this video comes out will be our AI integrations where you can just one click, hey, add open AI, add Gemini, add cloud to my app and you don't have to have an API key.
- B2 파괴: 소비자 행동·기대: Um anyway, um AI gives you that ability to do that like personalized tutoring on something where like it's giving you good answers, hopefully giving you good answers.
- 수치 주장: U and look that entire process has taken you like 1 hour of building and then 5 minutes of iterating but it's actually like 6 minutes of your attention because the 59 minutes like in that middle &gt;&gt; you were off having lunch coffee working on something el…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Replit/Inside_Replit_Agent_with_a_lead_AI_engineer__bJMriY-pqPE.md`

**307. [Replit's President on Agents, Security and the Future of Work | Michele Catasta @ SaaStr](https://www.youtube.com/watch?v=8VAZkJWZvAw)** — Replit · 에이전트·개발도구 · US · 2026-05 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: Thanks for hanging with us here at SaaStr Live 2026. I'm Rymer, this is Manny, we got Francisco. We just talked with Gazi and Amjad, and now we are joined by Micheleli, who is the president and head of AI at Replit here.…
- B1 디지털·AI 기술의 활용: If you're an expert developer, you can develop yourself that taste to realize, okay, maybe I should be using a latest GPT model to do my code reviews, and then my you know, all the scaffolding generated uh in terms of code should be done by a cloud model, and …
- B4 가치네트워크·생태계: Today and like yeah, Scott Kennedy said like zero users impacted by that supply chain attack today.
- 수치 주장: And as people that care about the product we're building, I I think we spend maybe 95% of our time reading the negative one.
- 교량: — · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Replit/Replit's_President_on_Agents,_Security_and_the_Future_of_Wor__8VAZkJWZvAw.md`

**308. [Replit for Enterprise with Kody Low + Nick Co](https://www.youtube.com/watch?v=IP8SRLgqtWU)** — Replit · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 저는 코디입니다. 그래서, 저희가 모든 것을 재편성했기 때문에 Replit 내의 새로운 구조와 기업들이 어떻게 변화하고 있는지에 대해 이야기해 보려고 합니다. 하지만, 저는 Replit을 통해 약 1년 반 동안 기업 운영 전반을 진행해 왔습니다 . 그리고 지금 저는 현장 엔지니어 리더 중 한 명이고, 닉은 저희 팀으로 합류했습니다. 그러니까 현장 엔지니어링은 판매 전후의 모든 기술적인 측면을…
- B4 가치네트워크·생태계: 하지만 특히 전문 코딩 팀의 경우, 지금처럼 실시간 코딩 환경에서 모든 구성원이 코딩을 하고 있을 때, 공급망 공격이 빈번하게 발생하고 모두가 각자의 로컬 컴퓨터에서 작업하고 있어 상황을 전혀 파악할 수 없는 상황을 상상해 보세요.
- B8 부정 성과: 보안·프라이버시: 마치 모두가 "음, 예전에 비트코인 ​​관련 일을 했었는데, 누구나 자기가 해킹할 수 없는 암호화 시스템을 만들 수 있다"는 말이 있었죠.
- 수치 주장: 그래서 지금은 회사 직원 1만 명에게 적용하고 있어요.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Replit/Replit_for_Enterprise_with_Kody_Low_+_Nick_Co__IP8SRLgqtWU.md`

**309. [The CRO Building Replit's Enterprise Machine | Ghazi Masood @ SaaStr](https://www.youtube.com/watch?v=PNBVzu4_G9c)** — Replit · 에이전트·개발도구 · US · 2026-05 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: starting with Ghazi, who is the CRO at Replit. Um and I think this is the first time you're meeting the audience from the community through one of our streams, right? &gt;&gt; a lot and really, really excited to be here.…
- B7 성과: 운영효율: What are the the early adopters that are really getting some success, really getting some good ROI from AI adoption?
- B1 디지털·AI 기술의 활용: Cuz I know a lot of people are out there, "Oh, SaaS is dead and it's coming for everything." And you know, it's like everyone's like, "I'm not going to I'm going to stop paying my Salesforce." And that's not what we're really seeing.
- 수치 주장: Because they cannot have if you're a big large big bank, you cannot have 300,000 people building a bunch of stuff that's not sanctioned, secure, governed.
- 교량: Avenue 1 동적역량 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Replit/The_CRO_Building_Replit's_Enterprise_Machine_Ghazi_Masood_@___PNBVzu4_G9c.md`

---

## SAP


**310. [How NEC Is Becoming an AI-Native Enterprise with SAP, RISE with SAP and Business AI](https://www.youtube.com/watch?v=6utLfKSBIHg)** — SAP · 엔터프라이즈 앱 · DE · 2026-04 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 나카타스와 오베이, 함께해 주셔서 감사합니다 . NEC에 대해 간략하게 소개해주시고, 지금까지의 혁신 여정과 SAP와의 관계에 대해 설명해주시겠습니까? NEC는 1899년 일본 최초의 외국 기업과의 합작 투자 회사로 설립되었습니다 . 저희 회사가 성장할 수 있었던 것은 끊임없이 회사로서 발전해왔기 때문입니다. 2000년대에 우리는 어려운 사업 침체기를 겪었습니다. 그 기간 동안 우리는 업무 …
- B1 디지털·AI 기술의 활용: 현재 NEC에서는 8만 명 이상의 직원이 매일 AI를 활용하고 있으며, 70개 이상의 AI 에이전트와 1,400개 이상의 특수 AI 모델을 운영하여 NEC의 업무량을 21만 시간 절감하고 있습니다.
- B4 가치네트워크·생태계: 우리는 글로벌 전략적 파트너십을 통해 변화를 가속화할 수 있는 생태계를 구축하고 있습니다.
- 수치 주장: 그러한 통찰력을 바탕으로 조치를 취한 결과 , 총 이익률이 5.5%포인트 향상되는 등 실질적인 성과를 거두었습니다 .
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/channels/SAP/How_NEC_Is_Becoming_an_AI-Native_Enterprise_with_SAP,_RISE_w__6utLfKSBIHg.md`

**311. [Global Keynote: The Beginning of Better | SAP Sapphire Madrid 2026](https://www.youtube.com/watch?v=CocpyxAizwE)** — SAP · 엔터프라이즈 앱 · DE · 2026-05 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: Since the dawn of time, history has been defined by a series of world changing innovations. These groundbreaking moments were not always met with the appropriate levels of enthusiasm. Well, that's the end of the raw food…
- B1 디지털·AI 기술의 활용: Via our AI Agent Hub in LeanIX, we also provide transparency about your agentic AI layer and govern non-SAP agents for free.
- B4 가치네트워크·생태계: And in an era where companies can run supply chains in near real time and answer customer questions in seconds, the financial close can still take a week, sometimes longer.
- 수치 주장: Since its launch last year, Joule Studio customers and partners have already built phenomenal things with it, like Sony, and have cut four days of manual work for an agent down to just 15 minutes.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Madrid_2__CocpyxAizwE.md`

**312. [The Future of Integration with SAP BTP | feat. Dr. Achim Kraiss and Dr. Markus Winter](https://www.youtube.com/watch?v=ZzBZWAbinzE)** — SAP · 엔터프라이즈 앱 · DE · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 그래서 실제로 최종적으로 무슨 일이 벌어지고 있냐면, 통합은 이러한 지능형 에이전트를 위한 제어 평면이 되고 있다는 것입니다. 그러니까 한편으로는 자율성을, 다른 한편으로는 통치권을 확보하면서 균형을 유지해야 한다는 거죠 . 그리고 그것이 궁극적으로 기업들이 AI를 안전하게 확장할 수 있도록 해주는 요소입니다. 따라서 실험적인 파일럿 단계를 벗어나 실제로 신뢰할 수 있고 프로덕션 환경 에서 …
- B1 디지털·AI 기술의 활용: 데이터는 클라우드 및 온프레미스 시스템, API, 이벤트, 기업 간 파트너 등 다양한 곳에 흩어져 있습니다.
- B3 전략적 대응: 결론적으로 말씀드리자면, 저희의 핵심 강점은 탄탄한 AI 전략, 명확한 제품 비전, 그리고 무엇보다도 수년간 쌓아온 깊은 고객 신뢰에 있다고 할 수 있습니다.
- 수치 주장: 여러분의 노력 덕분에 SAP Integration Suite는 시장에서 6년 연속 선두 기업으로 인정받았습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 프로토콜·표준
- 원문: `transcripts/channels/SAP/The_Future_of_Integration_with_SAP_BTP_feat._Dr._Achim_Krais__ZzBZWAbinzE.md`

**313. [Asset Management in SAP Cloud ERP | Expert Talk](https://www.youtube.com/watch?v=fyx68fY2be0)** — SAP · 엔터프라이즈 앱 · DE · 2026-06 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: [음악] SAP 전문가 토크에 오신 것을 환영합니다. 안녕하세요, 저는 제품 성공팀의 페르난다 로드리게스입니다. 오늘은 물리적 장비를 사용하는 모든 비즈니스에 영향을 미치는 주제에 대해 이야기해 보겠습니다 . 공장의 기계든, 발전소의 기계든, 창고의 장비든 마찬가지입니다. 오늘 주제는 SAP 클라우드 ERP에서의 자산 관리입니다 . 이번 세션에서는 SAP가 귀사의 비즈니스 프로세스를 지원하기…
- B1 디지털·AI 기술의 활용: SAP S/4HANA 퍼블릭 클라우드의 자산 관리는 석유 및 광업, 유틸리티, 천연 자원과 같은 자산 집약적 산업뿐 아니라 이산 및 공정 제조 분야에서 수십 년간 축적된 SAP 전문 지식을 바탕으로 구축된 핵심 ERP 기능입니다.
- B7 성과: 운영효율: 오늘날 우리는 유지보수 비용을 줄여야 한다는 압박 속에서 항상 비용에 대한 질문을 받기 때문에 비용을 관리해야 합니다 .
- 수치 주장: 그러니까, 만약 동일한 이상 징후에 대해 수천 건의 알림을 받게 된다면, 관리자가 이 알림들을 검토하고 그중 하나를 수락하거나 통합하는 것은 엄청난 작업량이 됩니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/SAP/Asset_Management_in_SAP_Cloud_ERP_Expert_Talk__fyx68fY2be0.md`

**314. [Is Your Leadership Ready for the AI Shift? | AI Voices, Episode 3](https://www.youtube.com/watch?v=rq5KpbaaZMY)** — SAP · 엔터프라이즈 앱 · DE · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B1 기술 활용, B4 가치창출 경로, B8 부정 성과
- 개요: 내는 결과물에는 언제나 인간의 판단력이 필요할 것입니다 . 국제적인 음악 리더로서 활동하는 제 입장에서 볼 때, AI는 리더십을 더욱 인간적으로 만들어준다는 것이 분명합니다. 리더로서 불확실성이 크기 때문에 공감 능력을 많이 보여줘야 합니다. 안녕하세요, [음악] 저는 예스퍼 슬리만입니다. 저는 SAP의 EMEA 지역 AI 담당자입니다 . 그리고 이것이 바로 AI 음성입니다. 본론으로 들어가…
- B5 리더십·CDO/CAIO: 특히 국제적인 리더로서 일하는 제 경험을 통해 볼 때, 인공지능이 리더십을 더욱 인간적으로 만들어준다는 것이 분명합니다.
- B5 조직구조 변화: 그래서, 그리고 저는 이것이 데이터 사일로 문제 외에도 AI의 이점을 활용하는 데 있어 가장 큰 과제이며, 또한 우리가 아직 그 방향으로 더 나아가지 못한 주요 원인이라고 생각합니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/SAP/Is_Your_Leadership_Ready_for_the_AI_Shift_AI_Voices,_Episode__rq5KpbaaZMY.md`

**315. [What’s New in SAP HANA Cloud | Deep Dive with Product Experts | Q2 2026](https://www.youtube.com/watch?v=QrGR38jGGZo)** — SAP · 엔터프라이즈 앱 · DE · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, SAP Hannah 클라우드의 2026년 2분기 새로운 기능에 대한 웨비나에 오신 것을 환영합니다 . 안녕하세요, 저는 SAP Hannah 클라우드 제품 관리팀의 안드레아입니다. 오늘 웨비나에서는 최신 릴리스에 포함된 모든 혁신 기능을 자세히 다룰 수는 없지만, 이번 릴리스에서 제공되는 가장 중요한 혁신 기능에 대한 개요를 제공해 드리겠습니다. 보다 포괄적인 개요를 원하시…
- B1 디지털·AI 기술의 활용: 방금 언급드린 온 프레미스에서 클라우드로 이전할 때의 이점 외에도, 데이터 레이크 관계형 엔진으로 마이그레이션하면 온프레미스 IQ에서 지원하지 않는 더 큰 데이터 볼륨을 지원하고 총소유비용( TCO)이 크게 절감된다는 점을 강조하고 싶습니다.
- B2 파괴: 데이터 가용성: 방금 언급드린 온 프레미스에서 클라우드로 이전할 때의 이점 외에도, 데이터 레이크 관계형 엔진으로 마이그레이션하면 온프레미스 IQ에서 지원하지 않는 더 큰 데이터 볼륨을 지원하고 총소유비용( TCO)이 크게 절감된다는 점을 강조하고 싶습니다.
- 수치 주장: 다음으로, SAP는 2026년 2분기 출시를 통해 클라우드 데이터베이스에 TLS 연결용 양자 후 암호화를 도입하여 클라이언트와 SAP 클라우드 데이터베이스 간 전송되는 모든 데이터에 대해 양자 내성 보호 기능을 제공합니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/SAP/What’s_New_in_SAP_HANA_Cloud_Deep_Dive_with_Product_Experts___QrGR38jGGZo.md`

---

## SK hynix


**316. [[Analyst Interview | SK증권 한동희 위원] HBM 경쟁 심화 우려 속 SK하이닉스의 대응 전략은?📊](https://www.youtube.com/watch?v=wQ67Mf4rRX4)** — SK hynix · 인프라·칩·전력 · KR · 2025-08 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 힘이 있는가 없는가? 실적이 좋은가? AI가 발전하고 있는가?이 사업자가 감당해야 될 숙명이라고. 안녕하세요. SK증권 반도체널리스트 한동이입니다. [음악] SK하이닉스의 2분기 실적은 대회적인 불확실성이 컸음에도 불구하고 훌륭한 실적을 기록했다라고 생각합니다. 이익도 성장하고 있는데 수익성도 계속 견조하게 유지가 되었고 재고도 하락했다라는 점이 가장 긍정적이었다고 봅니다. 2분기 랜드 출량…
- B7 성과: 조직성과: AI 사이클에서 SK 하이닉스가 증명했던 것처럼 안정적인 실적과 차별화된 수익성, 투자 효율성 극대화가 지속된다면 기업 가치의 상승은 매우 가시적이라고 생각합니다.
- B2 파괴: 경쟁구도: 앞으로 HBM 경쟁 심화 국면에서도 경쟁사 대비 더 좋은 수익과 더 좋은 수익성을 달성할 수 있는 기본 배경이 될 거라고 보고 있기 때문에 SK 하이닉스의 HBM 시장 내에서의 차별화 포인트는 강하구나라고 저희는 판단하고 있습니다.
- 수치 주장: 이미 작년에 계약이 완료된 HBM에 대한 물량의 판매 확대가 3분기, 4분기 지속될 것이라 생각하고 있습니다.
- 교량: — · 기술: 칩·하드웨어
- 원문: `transcripts/channels/SK_hynix/[Analyst_Interview_SK증권_한동희_위원]_HBM_경쟁_심화_우려_속_SK하이닉스의_대응_전략__wQ67Mf4rRX4.md`

---

## Salesforce


**317. [Agentforce World Tour NYC | Main Keynote 2025 | Salesforce](https://www.youtube.com/watch?v=sSIB8rZTkew)** — Salesforce · 엔터프라이즈 앱 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 에이전트 포레스트. 1년 전만 해도 아시안 포레스트는 그저 속삭임, 하나의 아이디어에 불과했습니다. 현재 이 제품은 저희가 출시한 제품 중 가장 빠르게 성장하는 제품입니다. 세일즈포스가 에이전트 포스를 공개한 것에 대해 이야기해 보겠습니다 . 대기업들이 에이전트 포스를 어떻게 활용하고 있는지 알려주세요 . 단순히 무엇이 가능한가의 문제가 아니라, 당신이 무엇을 가능하게 만들 것인가의 문제입니…
- B1 디지털·AI 기술의 활용: 이는 지능적이고 신뢰할 수 있는 AI 에이전트가 조직 내 모든 직원의 업무를 보완할 뿐만 아니라, 실제로 현장에서 작업을 수행하고 이전에는 불가능했던 방식으로 조직의 규모 확장과 성장을 지원할 수 있다는 아이디어입니다 .
- B2 파괴: 소비자 행동·기대: 하지만 저희는 여러분의 의견을 경청해 왔으며, LLM과 AI 에이전트가 고객 경험 측면에서 여러분이 수용할 수 있는 방식으로 예측 가능한 성능을 보여주지 못하는 경우가 있다는 점을 거듭해서 지적해 주셨습니다.
- 수치 주장: 사실, 지금은 모두가 하이퍼스케일러, 특히 아마존과 그로 인한 비용 절감에 매료되었던 2010년과 매우 흡사한 느낌입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Salesforce/Agentforce_World_Tour_NYC_Main_Keynote_2025_Salesforce__sSIB8rZTkew.md`

**318. [Boost Advertising ROI: Data Cloud & Salesforce Platform Integration | Salesforce](https://www.youtube.com/watch?v=1eur1w4VfMQ)** — Salesforce · 엔터프라이즈 앱 · US · 2026-02 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요 여러분. 안녕하세요, 이번 세션에서는 Salesforce가 Data 360을 활용하여 광고 ROI를 높이는 방법에 대해 알아보겠습니다. 안녕하세요, 제 이름은 조나단 비스턴입니다. 저는 제품 마케터입니다. 저는 데이터 360을 담당하고 있고, 저와 함께하신 아나카 콜리스는 세일즈포스에서 모든 광고를 총괄하고 있으며, 글로벌 필드 마케팅 전략, 운영 및 성과 담당 부사장입니다. 그리…
- B4 가치네트워크·생태계: 이것이 여러분의 CRM 생태계에 어떻게 잘 들어맞는지, 그리고 B2B 데이터 소스나 B2C CRM 데이터 소스를 활용하여 잠재 고객이나 기존 고객에 대한 이해도를 어떻게 높일 수 있는지 생각해 보세요 .
- B1 디지털·AI 기술의 활용: Agentforce는 Mercury와 Data 360에서 자동으로 에리카의 프로필을 보강하여, 에리카의 고객이 실제로 마케팅 클라우드를 현재 사용하고 있는 고객이며, 그녀의 팀원 세 명이 유사한 솔루션을 검토 중이라는 사실을 알려줍니다.
- 수치 주장: 이제 더욱 흥미로운 점은 이벤트와 10,000개의 사용자 신호가 동시에 Data360으로 전송되어, 우리가 이미 CRM에 보유하고 있는 자사 속성과 데이터를 통합한다는 것입니다 .
- 교량: — · 기술: 에이전트 프레임워크
- 원문: `transcripts/channels/Salesforce/Boost_Advertising_ROI_Data_Cloud_&_Salesforce_Platform_Integ__1eur1w4VfMQ.md`

**319. [Build the Future with Salesforce Headless 360 | TDX 2026 Keynote Replay](https://www.youtube.com/watch?v=aKsZdyyzcfU)** — Salesforce · 엔터프라이즈 앱 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 세일즈포스의 사장 겸 최고 마케팅 책임자인 패트릭 스토크스를 환영해 주십시오 . 괜찮은. [환호] [박수] 좋은 아침입니다. 샌프란시스코 여러분, 좋은 아침입니다 . 전 세계에서 저희와 함께해 주시는 모든 분들, 고객 여러분, 파트너 여러분, 직원 여러분, 그리고 물론 놀라운 선구자 여러분, 안녕하세요. 좋은 아침이에요. TDX에 오신 것을 환영합니다. 오늘 이렇게 여러분 모두와 함께하게 되…
- B1 디지털·AI 기술의 활용: 웹사이트, 모바일 앱, Slack, Teams 또는 ChatGPT, Claude 등 타사 LLM 플랫폼이든 무엇이든 상관없습니다.
- B4 가치네트워크·생태계: 우리는 여러 도구를 활용하여 에이전트를 통해 매우 빠르게 결정론적 웹사이트를 구축했는데 , 그중 일부는 Salesforce 제품이 아니었으며, 이러한 개방형 생태계에 참여하여 웹사이트를 구축했습니다.
- 수치 주장: 18개월 전 소프트웨어 개발 방식은 12개월 전과 다르고, 6개월 전과도 다르고, 심지어 어제와도 다릅니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Salesforce/Build_the_Future_with_Salesforce_Headless_360_TDX_2026_Keyno__aKsZdyyzcfU.md`

**320. [Introducing... the NEW Slack!](https://www.youtube.com/watch?v=vYUqOU-QV-o)** — Salesforce · 엔터프라이즈 앱 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 우리는 행위 주체성의 변곡점에 도달했습니다 . 전체 워크플로, 앱 및 에이전트를 실행합니다 . 이것이 바로 강렬한 순간입니다. 그리고 우리 음악 담당자들은 이제 백과 사전적인 지식을 갖추게 되었습니다. 이는 소비자에게 이득입니다. 음악 제작 비용을 낮추는 데 기여하고 있습니다. 고객은 에이전트를 하나만 배치하지 않을 것입니다. 많은 에이전트가 있을 겁니다. 대기업들이 Agent Force를 …
- B1 디지털·AI 기술의 활용: 마크 와 파커가 세일즈포스를 시작했을 때, 그들의 목표는 기업용 소프트웨어를 클라우드로 이전하는 것이었기 때문입니다.
- B4 가치네트워크·생태계: 방금 발표한 4분기는 110억 달러 이상의 매출과 720억 달러 이상의 RPO(Recruitment Process Outsourcing, 계약 체결 후 아직 인식되지 않은 금액)를 기록하며 사상 최고의 분기 실적을 달성했습니다.
- 수치 주장: 우리는 슬랙을 활용한 덕분에 최소 450만 달러를 절약하고 음악 활동을 통해 수익을 창출했습니다.
- 교량: Avenue 1 동적역량 · 기술: 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Salesforce/Introducing..._the_NEW_Slack!__vYUqOU-QV-o.md`

**321. [Marc Benioff on Agentforce & the Future of AI Agents in Slack | Matt Berman Podcast](https://www.youtube.com/watch?v=XY-s81fBXFU)** — Salesforce · 엔터프라이즈 앱 · US · 2026-04 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: All right, welcome everybody. Welcome. Okay. I'm at Berman and of course we have here Mark Benioff, co-founder and CEO of Salesforce, absolute legend in tech. Thank you. Lately one of the loudest voices talking about age…
- B1 디지털·AI 기술의 활용: So, when you're in Sales Cloud, you know, which is our number one, you know, namesake product or our Service Cloud, you the Slack bot is with you as well.
- B4 가치네트워크·생태계: Uh talk a little bit about the birth of that partnership, and then how they're powering Slackbot today, and what the current manifestation of that partnership looks like.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Salesforce/Marc_Benioff_on_Agentforce_&_the_Future_of_AI_Agents_in_Slac__XY-s81fBXFU.md`

**322. [Meet the new Slack. Where AI works.](https://www.youtube.com/watch?v=6DtrYEHRHw4)** — Salesforce · 엔터프라이즈 앱 · US · 2026-04 · en · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: Meet the new Slack where AI works. My name is Vic Medarada, senior director AI product marketing here at Salesforce. And I'm excited to talk to you about a lot of things, but what you're going to hear from today is Mark …
- B1 디지털·AI 기술의 활용: Well, I had my big AI freakout moment around 201 or 13 when I started to see these incredible models come out of Stanford and that was really how we ended up with Einstein because we ended up acquiring companies bringing engineers together and we ended up you …
- B4 가치네트워크·생태계: Uh, talk a little bit about the birth of that partnership and then how they're powering Slackbot today and what the current manifestation of that partnership looks like.
- 수치 주장: We've saved and made at least $4.5 million just because of how we're using Slack.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 프로토콜·표준 · 검색·RAG · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Salesforce/Meet_the_new_Slack._Where_AI_works.__6DtrYEHRHw4.md`

**323. [Our Inside Perspective on Mission-Ready AI](https://www.youtube.com/watch?v=2lx6JDSPGoM)** — Salesforce · 엔터프라이즈 앱 · US · 2026-04 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: The biggest task facing most organization in the agentic era is modernizing legacy systems and preparing the workforce for an AI-powered mission-ready future. So, how can Agent Force and the Salesforce military platform …
- B1 디지털·AI 기술의 활용: The biggest task facing most organization in the agentic era is modernizing legacy systems and preparing the workforce for an AI-powered mission-ready future.
- B4 가치네트워크·생태계: Um, so excuse me, Secretary, how do you see partnerships with Salesforce, the DoD, uh nonprofits like Blue Star Families, and how is that all going to impact talent and and retention?
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/channels/Salesforce/Our_Inside_Perspective_on_Mission-Ready_AI__2lx6JDSPGoM.md`

**324. [State of Service: How AI Agents are Delivering Results in Under 60 Days](https://www.youtube.com/watch?v=H8A7Nu2KseI)** — Salesforce · 엔터프라이즈 앱 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 비밀이 아니다. 서비스 산업은 에이전트 중심적으로 변모했다. 최신 서비스 현황 보고서에서 당사는 13개국 3,000명 이상의 서비스 전문가를 대상으로 설문 조사를 실시하여 최신 업계 동향과 통찰력, 그리고 이를 바탕으로 취해야 할 조치를 파악했습니다. 알아두셔야 할 사항은 다음과 같습니다. 저는 조슈아 간디이고, 세일즈포스의 제품 마케팅 디렉터인 메건 마이어스가 함께하고 있습니다 . 바로 시…
- B1 디지털·AI 기술의 활용: 리더들은 고객, 서비스 담당자, 리더, 그리고 AI 에이전트 모두가 제공받는 정보와 내용이 정확하고 관련성이 있다고 확신할 수 있도록, 전체적인 엔드투엔드 경험 전반에 걸쳐 기초적인 수준에서 신뢰를 구축하는 방안을 고민해야 합니다.
- B2 파괴: 소비자 행동·기대: 응답자 전체에서 고객 만족도가 크게 상승한 것을 확인했는데, 이는 AI가 단순히 속도만을 위한 것이 아니라 모든 접점에서 탁월한 고객 경험을 창출하는 데에도 중요하다는 것을 보여줍니다 .
- 수치 주장: 제 말은, 현재 AI를 도입했다고 보고한 조직의 비율이 39%에서 66%에 이른다는 뜻입니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Salesforce/State_of_Service_How_AI_Agents_are_Delivering_Results_in_Und__H8A7Nu2KseI.md`

**325. [Welcome to Agentforce Demo Day!](https://www.youtube.com/watch?v=7a3TnSO0nps)** — Salesforce · 엔터프라이즈 앱 · US · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 에이전트 포스는 샤크 닌자가 보유한 모든 정보를 활용할 수 있는 능력을 갖게 될 것입니다 . 우리는 [음악]이 고객이 필요로 하는 모든 유형 의 질문이나 제품 추천을 처리할 수 있기를 바랍니다 . 이미 저희 제품을 구매한 고객이든 다른 제품을 고려 중인 고객이든, Agent Force는 고객 만족도를 높여 Shark Ninja 패밀리로 다시 돌아오도록 돕는 데 큰 역할을 할 것입니다…
- B2 파괴: 소비자 행동·기대: 금융 서비스나 의료와 같은 산업에서 잘못된 답변은 단순히 고객 경험에 부정적인 영향을 미치는 것을 넘어 규정 준수 위험으로 이어질 수 있습니다.
- B5 직무·역량 변화: 그래서 고용주들이 채용 과정을 진행하다가 어떤 단계에서 막히게 되면, 저희에게 도움을 요청하여 다시 채용 과정으로 돌아갈 수 있도록 해달라는 것입니다.
- 수치 주장: 그리고 아시다시피, 제조업 기업인 JPW는 업무량이 증가했음에도 불구하고 사건 해결 속도를 40%나 향상시켰습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준
- 원문: `transcripts/channels/Salesforce/Welcome_to_Agentforce_Demo_Day!__7a3TnSO0nps.md`

**326. [Agentforce Marketing Keynote | Connections 2026](https://www.youtube.com/watch?v=9g-S56GGhN0)** — Salesforce · 엔터프라이즈 앱 · US · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: H&amp;M Force 마케팅 및 Salesforce의 제품 관리 담당 수석 부사장인 에릭 젠스를 환영해 주십시오. [박수] 감사합니다. 여러분 모두 감사합니다. 네, 시카고에서 여러분과 다시 만나게 되어 정말 기쁩니다 . 시카고는 음악의 도시라고들 합니다. 어떤 사람들은 이곳을 음식의 도시라고 부릅니다. 하지만 오늘날 시카고는 마케팅의 도시입니다. 모두 [환호] 좋습니다. 좋아요, 모두들…
- B2 파괴: 소비자 행동·기대: 이를 통해 고가치 고객층을 식별하고 , 개인화된 마케팅을 위한 토대를 마련하며, 에이전트들이 고객 여정을 지원하고 성과를 창출할 수 있도록 돕고 있습니다.
- B1 디지털·AI 기술의 활용: 따라서 Marketing Cloud Engagement 고객이시든 Account Engagement 고객이시든 관계없이, 지금 바로 시작하실 수 있도록 온보딩 가이드를 제공해 드립니다.
- 수치 주장: 저는 세일즈포스에서 13년 동안 마케터들을 위한 제품을 개발해 왔습니다.
- 교량: — · 기술: 프로토콜·표준
- 원문: `transcripts/channels/Salesforce/Agentforce_Marketing_Keynote_Connections_2026__9g-S56GGhN0.md`

**327. [Dissecting the State of Marketing in 2026 | Salesforce](https://www.youtube.com/watch?v=rS5MfhB8RkY)** — Salesforce · 엔터프라이즈 앱 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 이분은 케이티 휠러입니다. 저는 Agent Force Marketing에서 제품 마케팅을 담당하고 있습니다. 저는 세일즈포스에서 약 9 년 동안 근무했습니다. 저는 세일즈포스에서 일하는 진정한 B2B 마케터입니다 . 자, 보고서 결과를 자세히 살펴보기 전에, 설문조사 참여자들의 인구 통계 학적 배경에 대해 잠깐 알아보겠습니다. State of Marketing은 Salesforce에서 발행한…
- B7 성과: 운영효율: 예를 들어, 우리 내부 운영 방식 중에서 다소 비효율적인 부분은 무엇이 있을지, 제품 출시 시간을 단축하거나 회의 횟수를 줄이는 등 운영 효율성을 높이기 위해 먼저 개선할 수 있는 부분은 무엇일지 생각해 볼 것입니다.
- B1 디지털·AI 기술의 활용: ChatGPT나 Claude 같은 생성형 AI는 어떤가요 ?
- 수치 주장: 보고서에서 발견한 몇 가지 이점 중 하나는 AI를 통해 마케팅 ROI가 20% 증가했다는 것입니다 .
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Salesforce/Dissecting_the_State_of_Marketing_in_2026_Salesforce__rS5MfhB8RkY.md`

---

## SambaNova


**328. [Prefill vs Decode](https://www.youtube.com/watch?v=4w0M255awlE)** — SambaNova · 인프라·칩·전력 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요 여러분, 저는 하산입니다. 오픈 소스 라이브에 오신 것을 환영합니다. 이곳에서는 오픈 소스와 AI 분야의 최고 전문가들과 이야기를 나눕니다. 오늘 파이프 님을 모시게 되어 정말 기쁩니다. 오늘 함께해 주셔서 정말 감사합니다. 이 자리에 함께하게 되어 기쁩니다. 응. 음, 먼저 간단하게 당신의 배경 과 어떻게 오픈 소스에 관심을 갖게 되었는지 간략하게 설명해 주시겠어요? 응. 네, …
- B4 가치네트워크·생태계: AI 분야에 이제 막 발을 들여놓고 지식 그래프를 어떻게 이해하고 RAV 애플리케이션을 어떻게 구축해야 하는지, 그리고 전반적인 생태계를 어떻게 개선해야 하는지 배우는 단계에 있는 사람에게 어떤 조언을 해주시겠어요?
- B1 디지털·AI 기술의 활용: 가트너가 한 달 전쯤 발표한 보고서에 따르면, 설문 조사에 참여한 고객들을 통해 관찰한 결과, 그래프 래그(Graph Rag)를 사용할 때 토큰 수가 25%에서 최대 97%까지 감소하는 것으로 나타났습니다.
- 수치 주장: 가트너가 한 달 전쯤 발표한 보고서에 따르면, 설문 조사에 참여한 고객들을 통해 관찰한 결과, 그래프 래그(Graph Rag)를 사용할 때 토큰 수가 25%에서 최대 97%까지 감소하는 것으로 나타났습니다.
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 온톨로지·데이터계층
- 원문: `transcripts/channels/SambaNova/Prefill_vs_Decode__4w0M255awlE.md`

**329. [What Is a Model?](https://www.youtube.com/watch?v=Fcu-peZt0lM)** — SambaNova · 인프라·칩·전력 · US · 2026-02 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: Dev Talks 2화에 오신 것을 환영합니다. 이번 에피소드에서는 Hugging Face와 Gradio를 사용하여 초고속 AI 앱을 구축하는 방법에 대해 이야기해 보겠습니다 . 저는 아부 바크르가 실제로 우리 근처에 있다는 사실을 발표하게 되어 매우 기쁘고 설렙니다 . 음, 저희는 함께 많은 행사를 진행했어요. 그를 모시고 그라도에 대해 이야기를 나눌 수 있게 되어 기쁩니다. 아부바크에 대…
- B1 디지털·AI 기술의 활용: 커서(Curse)나 클라우드 코드(Cloud Code) 등 다른 애플리케이션에 MCP 서버로 추가하기만 하면, LM(언어 관리자)이 음성을 생성할 수 있게 됩니다.
- B8 부정 성과: 보안·프라이버시: 많은 경우 사람들이 웹 프런트엔드를 직접 코딩하거나 다른 사람에게 맡기지만, 그렇게 하면 보안 문제, 성능 문제 등 여러 가지 문제에 노출될 수 있습니다.
- 수치 주장: M, 아시다시피 마이크로소프트도 오늘, 정확히는 30분 전에 이 모델을 출시했습니다.
- 교량: — · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/SambaNova/What_Is_a_Model__Fcu-peZt0lM.md`

---

## Scale AI


**330. [Scale AI |  Contrats et détention des droits | Pourquoi PI, E10](https://www.youtube.com/watch?v=xhZsMRR9qAU)** — Scale AI · 컨설팅·전략 · US · 2022-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 우리가 지적재산권(IP) 도구라고 하면 보통 특허, 저작권, 상표를 떠올리죠. 하지만 사실 가장 중요한 IP 도구는 바로 계약이라는 사실을 알고 계셨나요? 계약이 사업 목표와 제대로 부합한다면 매우 강력한 힘을 발휘할 수 있지만, 그렇지 않다면 문제가 발생할 수 있습니다. ipy에 오신 것을 환영합니다. [음악] 모든 사업에 영향을 미치는 세 가지 IP 문제가 있는데, 저는 이를 VIP 삼위…
- B4 가치네트워크·생태계: 벤더든, 직원이든, 계약이든, 심지어 다른 창업자든 마찬가지입니다.
- B8 부정 성과: 보안·프라이버시: 직원 및 계약직 직원의 경우, 그들이 업무에서 창출한 IP에 대한 소유권을 명시하는 계약이 필요하며, 이전 고용주의 IP 또는 기밀 정보를 사용하는 것을 금지하는 조항을 포함하는 것이 좋습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Scale_AI/Scale_AI_Contrats_et_détention_des_droits_Pourquoi_PI,_E10__xhZsMRR9qAU.md`

**331. [Patents in AI: It's Time to Modernize Your Approach | Scale AI at ALL IN 2024](https://www.youtube.com/watch?v=4C67rUE96pM)** — Scale AI · 컨설팅·전략 · US · 2024-09 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 다음 컨퍼런스에서는 인공지능(AI)이 산업을 혁신함에 따라 종종 과소평가되지만 매우 중요한 AI 특허 관리 측면을 다룰 예정입니다. 오늘날 특허를 법무팀에만 맡겨두는 것은 바람직하지 않습니다. AI 분야의 기업가와 리더에게 특허를 전략적으로 활용하는 방법은 알고리즘과 데이터 과학을 숙달하는 것만큼이나 중요합니다. 특허 관리 능력은 핵심 비즈니스 역량이 되었으며, 이번 발표에서는 특허에 대한 …
- B2 파괴: 경쟁구도: 일종의 무장 대치 상황, 즉 경쟁사를 견제하기 위한 전쟁 자금을 마련하는 것과 같은 맥락에서, 기업들은 인수 대상 기업 의 기술뿐만 아니라 자사 기술 주변에도 기술적 해자를 구축하는 데 관심이 있습니다.
- B4 가치제안 변화: 지금은 안면 인식 기술 등으로 인해 어느 정도 무력화되었지만, 특허의 유효성을 결정하는 것은 기술적 가치 그 자체가 아니라 사업과의 연관성, 사업 전략, 가치 평가, 또는 가치 제안의 타당성입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Scale_AI/Patents_in_AI_It's_Time_to_Modernize_Your_Approach_Scale_AI___4C67rUE96pM.md`

**332. [Scale AI AI Playbook for Business Leaders | ALL IN 2024](https://www.youtube.com/watch?v=TPN6hbY40TU)** — Scale AI · 컨설팅·전략 · US · 2024-09 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요 여러분, Allin 20124에 오신 것을 환영합니다! 이곳에 오게 되어 정말 기쁩니다. 시간이 20분밖에 없지만, 먼저 말씀드리고 싶은 것은 Scale AI 부스가 메인 스테이지 입구 바로 옆에 있다는 것입니다. 발표 후에 궁금한 점이 있으시면 언제든지 편하게 들러주세요. 저희 팀이 그곳에 있으니 부담 없이 방문해 주시면 감사하겠습니다. 오늘 제가 말씀드릴 주제는 Sca…
- B3 전략적 대응: 산 정상까지 안내해 줄 믿을 수 있는 지도를 만들기 위해 AI 전략과 로드맵을 어떻게 수립해야 하는지에 대해 이야기해 보겠습니다.
- B4 가치네트워크·생태계: 시간 관계상 자세히 설명드릴 수는 없지만, 데이터, 인재, 문화, 조직 구조, 운영 모델, 그리고 생태계 파트너십이 AI 전략의 핵심 동력입니다.
- 수치 주장: 진한 파란색으로 표시된 부분은 또 다른 3분의 1을 차지하는 초기 도입 기업들로, 파일럿 프로젝트를 통해 AI를 시험적으로 사용해 보고 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Scale_AI/Scale_AI_AI_Playbook_for_Business_Leaders_ALL_IN_2024__TPN6hbY40TU.md`

**333. [Scale AI @ ALL IN 2025 | Back to the future of Canadian AI: 6 years of Scale AI](https://www.youtube.com/watch?v=sXTycrc-b7Q)** — Scale AI · 컨설팅·전략 · US · 2025-10 · en · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: Hello again. Uh, thanks for sticking around. I actually encourage you to stick around. We're at a at a we have a bunch of really great speakers coming up. Super fascinating. Uh, the first one is uh on from the Scale AI t…
- B4 가치네트워크·생태계: And uh we we um and the idea is once we we grow that AI ecosystem, we make it shine on the world stage thanks to an event like this all in 6,000 people yesterday and today.
- B3 전략적 대응: The first thing about the first thing we think about when we think about AI strategy and AI expertise is really having the right scientific expertise.
- 수치 주장: The same thing as building a prototype car and producing 100,000 cars a year.
- 교량: 정의 확장(DX→AX 계승) · 기술: —
- 원문: `transcripts/channels/Scale_AI/Scale_AI_@_ALL_IN_2025_Back_to_the_future_of_Canadian_AI_6_y__sXTycrc-b7Q.md`

---

## Schneider Electric


**334. [Chris Sharp & Steven Carlini: AI Factories: Power, Cooling & Token Economics I S02EP14](https://www.youtube.com/watch?v=Vfj0etH-rD8)** — Schneider Electric · 인프라·칩·전력 · FR · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 콘크리트는 영구적이지만, 실리콘은 그렇지 않습니다. 오른쪽? 그리고 그러한 불일치와 실리콘의 급속한 혁신이라는 근본적인 조화가 인공지능 공장과 기존 데이터 센터라는 두 산업 분야를 근본적으로 변화시키고 있습니다. 아시다시피, 상황이 완전히 뒤바뀌었어요 . 아시다시피, 데이터 센터의 IT 부분은 작은 부분에 불과하고, 외부의 물리적 인프라, 즉 냉각기, 무정전 전원 공급 장치(UPS), 발전기…
- B1 디지털·AI 기술의 활용: 그래서 저희는 항상 그 시장을 주시하고 있지만, 많은 분들께 클라우드 시장과 마찬가지로 퍼블릭 클라우드를 사용하다가 다시 프라이빗 클라우드로 돌아온 것처럼, 기반을 구축하고 급증하는 수요를 활용하는 것이 엄청난 투자 수익률(ROI)을 가져다줄 수 있다는 점을 항상 강조하고 있습니다.
- B7 성과: 운영효율: 그래서 저희는 항상 그 시장을 주시하고 있지만, 많은 분들께 클라우드 시장과 마찬가지로 퍼블릭 클라우드를 사용하다가 다시 프라이빗 클라우드로 돌아온 것처럼, 기반을 구축하고 급증하는 수요를 활용하는 것이 엄청난 투자 수익률(ROI)을 가져다줄 수 있다는 점을 항상 강조하고 있습니다.
- 수치 주장: 수천 개의 가속기가 하나의 통합 시스템으로 작동하여 전기를 귀중한 토큰과 제거해야 할 열로 변환하는 매우 복잡한 환경입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Schneider_Electric/Chris_Sharp_&_Steven_Carlini_AI_Factories_Power,_Cooling_&_T__Vfj0etH-rD8.md`

**335. [Exploring DCIM and EcoStruxure IT Solutions](https://www.youtube.com/watch?v=jBVwPeRBC-I)** — Schneider Electric · 인프라·칩·전력 · FR · 2026-06 · ko · 5/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: [음악] 오늘은 데이터센터 인프라 관리(DCIM)에 대해 자세히 알아보고, 슈나이더 일렉트릭의 EcoStruxure IT가 데이터센터 관리를 위한 포괄적인 엔드투엔드 솔루션으로서 어떻게 기능하는지 살펴보겠습니다 . 디지털 전략에서 DCIM이 어떤 역할을 하는지 이해하려는 최고 경영진이든, 복잡한 하이브리드 환경을 관리하는 운영 책임자이든, 분산 인프라를 담당하는 IT 관리자이든 , 이 대화는…
- B7 성과: 운영효율: 그리고 효율성을 높이고, 가동 시간을 늘리고, 상태 기반 유지 관리를 통해 비용을 절감하고, 예를 들어 와트당 토큰 가격을 높여 수익을 개선할 수 있습니다.
- B1 디지털·AI 기술의 활용: 클라우드에서 모든 것을 중앙 집중식으로 처리하면 많은 효율성을 얻을 수 있지만, 데이터 개인 정보 보호, 지연 시간, 비용, 기타 여러 가지 이유, 특히 유럽에서 데이터 주권에 대한 우려가 있기 때문입니다.
- 수치 주장: 제가 설명드린 모든 것이 아직 100% 완벽한 것은 아니지만, 많은 부분이 지금 당장 실행 가능하며, 저희는 DCIM 분야에서 더욱 나은 솔루션을 개발하기 위해 적극적으로 투자하고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Schneider_Electric/Exploring_DCIM_and_EcoStruxure_IT_Solutions__jBVwPeRBC-I.md`

**336. [End of Islands - Unified Asset Lifecycle is the Digital Fabric for Operational Excellence](https://www.youtube.com/watch?v=xjFSF4jCvpk)** — Schneider Electric · 인프라·칩·전력 · FR · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 여러분, 안녕하세요. 함께해 주셔서 정말 감사합니다. 제가 중요하게 생각하는 주제를 다룰 수 있게 되어 매우 기쁩니다. 왜 그런지 곧 이해하실 수 있을 겁니다. 그러니까 뉴스를 보고 듣다 보면, 우리는 기본적으로 세 가지 주요 요인에 의해 형성된 새로운 운영 현실에 진입하고 있다는 것을 알 수 있습니다 . 첫 번째는 모든 곳에 디지털과 인공지능이 존재한다는 것입니다. 이 부분은 명백하다고 생…
- B7 성과: 운영효율: 개념 증명보다는 투자 수익률(ROI)을 제공하는 효과적인 사용 사례가 점점 더 중요해지고 있으며, 데이터 모델링 측면에서 프로세스와 전력 데이터 통합을 실현 하고 사용 사례를 제공할 수 있다는 것은 우리가 에너지 손실 의 근본 원인을 분석할 수 있음을 효과적으로 입증하는 것입니다 .
- B4 가치제안 변화: 그래서 에너지 인텔리전스와 AI 기반 서비스가 이러한 문제를 해결할 수 있고, 그 결과 시간과 비용을 절약할 수 있으며 훨씬 더 안정적인 서비스를 제공받을 수 있고 고객 만족도 점수도 향상될 것입니다.
- 수치 주장: 전 세계 AI 관련 지출은 향후 몇 년 동안 거의 170% 이상 증가할 것으로 예상됩니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Schneider_Electric/End_of_Islands_-_Unified_Asset_Lifecycle_is_the_Digital_Fabr__xjFSF4jCvpk.md`

**337. [Is there an ROI in industrial AI? The truth behind data, automation, and value in CPG manufacturing](https://www.youtube.com/watch?v=2cJD3hlyu6g)** — Schneider Electric · 인프라·칩·전력 · FR · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B8 부정 성과
- 개요: 제 이름은 닐 스미스입니다. 저는 슈나이더 일렉트릭의 소비재 부문 사장입니다 . 네, 그리고 오늘 세션은 여러분도 이미 들으셨겠지만, 소비재 분야의 인공지능에 관한 것입니다 . 그래서 우리가 이야기할 주제는 진정한 제조 가치가 어디에서 창출되는지, 특히 인공지능의 가치는 어디에 있는지, 그리고 이를 어떻게 대규모로 달성할 수 있는지에 대한 것입니다. 지난주 슈나이더 일렉트릭은 소비재 산업의 …
- B6 장벽: 관성·저항: 이 연구는 또한 기술 격차, 기존 시스템, 데이터 사일로, 기존 시스템의 한계 등에 대해서도 언급합니다 .
- B7 성과: 운영효율: 아시다시피, 이러한 에이전트만 배포하고, 전반적인 장비 효율성, 디지털 트윈을 위한 대시보드를 신속하게 구축하면 투자 수익을 얻을 수 있습니다.
- 수치 주장: 설문 조사에 참여한 사람들 중 70% 이상이 현재까지 AI 프로젝트를 도입했지만, 투자 대비 수익률(ROI)이 낮다고 보고했습니다.
- 교량: 정의 확장(DX→AX 계승) · 기술: 프로토콜·표준
- 원문: `transcripts/channels/Schneider_Electric/Is_there_an_ROI_in_industrial_AI_The_truth_behind_data,_auto__2cJD3hlyu6g.md`

**338. [Powering the AI factory - The grid-to-chip journey | Schneider Electric](https://www.youtube.com/watch?v=lWYUvDXnudc)** — Schneider Electric · 인프라·칩·전력 · FR · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 데이터센터 파워 채널에 다시 오신 것을 환영합니다 . 저는 엠마 스트래튼입니다. 저는 DCD의 채널 책임자입니다. AI 팩토리에 전력을 공급하는 방법, 즉 전력망에서 칩까지 이어지는 여정에 대한 이번 에피소드를 소개하게 되어 정말 기쁩니다. 이번 에피소드 제작에 함께해주신 슈나이더 일렉트릭에 진심으로 감사드립니다 . 오늘 저와 함께 해주신 분은 슈나이더 일렉트릭에서 AI 및 데이…
- B4 가치네트워크·생태계: 즉, 공급망과 생태계가 이를 지원할 준비가 되어 있어야 한다는 뜻입니다 .
- B1 디지털·AI 기술의 활용: 그래서 수십 년 동안 우리는 엔터프라이즈 또는 클라우드 기반 데이터 센터라고 부르는 것을 사용해 왔는데, 이는 x86 서버 아키텍처, 즉 작은 피자 박스 모양의 서버를 기반으로 했고, 그런 서버가 수천 대에 달했으며, 각 서버 랙은 5~ 15킬로와트의 전력을 소비했습니다.
- 수치 주장: 저희는 엔비디아의 최신 GPU 출시 6개월 전에 이러한 정보를 공개합니다 .
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Schneider_Electric/Powering_the_AI_factory_-_The_grid-to-chip_journey_Schneider__lWYUvDXnudc.md`

---

## Sema4ai


**339. [Enterprise AI Adoption: From Idea to Deployment](https://www.youtube.com/watch?v=xofWoVQ-ic4)** — Sema4ai · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요, 저는 믹 홀리슨이고 오늘은 폴 코팅 씨와 이야기를 나누겠습니다. 폴은 Semaphore.ai의 수석 부사장 겸 제품 책임자입니다. 그는 공동 창업자이기도 합니다. 오늘은 폴과 함께 기업용 AI 에이전트 도입에 대해 이야기해 보겠습니다. 기업들이 직면하는 장애물과 과제에는 어떤 것들이 있으며, semaphore.ai 플랫폼은 이러한 문제들을 어떻게 독창적으로 해결할 수 있을까요? …
- B1 디지털·AI 기술의 활용: 그리고 제 생각에는 이러한 AI 에이전트를 구축하고 배포하고 유지 관리하는 것이 사람들이 한두 개의 에이전트로 초기 성공을 거둔 후에는 가장 어려운 부분 중 하나로 드러나는 경우가 많습니다 .
- B4 가치네트워크·생태계: 첫 번째는 다양한 기업 애플리케이션뿐만 아니라 데이터베이스, 그리고 기업 내에 존재하는 전체 데이터 생태계에 연결할 수 있도록 해주는 기능입니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/2026-07-24/Enterprise_AI_Adoption_From_Idea_to_Deployment__xofWoVQ-ic4.md`

---

## ServiceNow


**340. [Michael Park's AI Whiteboard Masterclass](https://www.youtube.com/watch?v=0Fmw61s8CKc)** — ServiceNow · 데이터·컨텍스트·거버넌스 · US · 2025-09 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B8 부정 성과
- 개요: [음악] 안녕하세요, 저는 마이클 파크입니다. 저는 ServiceNow에서 채널 및 파트너십을 담당하고 있습니다 . 오늘 제가 여러분과 이야기하고 싶은 것은 비즈니스 혁신을 위한 AI 플랫폼입니다 . 저희는 AI 플랫폼 전략에 대한 화이트보드 세션을 진행하여 여러분 모두가 AI 엔터프라이즈 아키텍처라는 새로운 세계에 익숙해지도록 하겠습니다 . 그리고 저는 ServiceNow의 단일 플랫폼, …
- B1 디지털·AI 기술의 활용: 이는 다양한 프로토콜(MCP, Google의 ADA, Microsoft의 Co-Pilot 등)이 통합되는 미래의 세계를 위해 설계되고 있으며, 다른 AI 에이전트와 통합하여 에이전트 간 프로세스 흐름을 교환할 수 있도록 하는 복잡한 API 패브릭입니다 .
- B4 민첩성·양손잡이: 그래서 우리는 파트너들이 기본 제공되는 기능을 활용하여 특정 산업 또는 하위 산업에 맞게 패키징하고, 민첩성을 확보하여 ServiceNow 내에서뿐만 아니라 전체 산업 워크플로를 혁신할 수 있기를 기대합니다.
- 수치 주장: 그리고 저는 ServiceNow의 단일 플랫폼, 단일 아키텍처, 단일 데이터 모델이 어떻게 이 시점에서 ServiceNow를 독보적으로 위치시켜 여러분 모두가 AIE(Advanced Industry Enterprise)를 기반으로 하는 새로운 비즈니스를 구축하고, 다양한 신규 서비스와 기능을 통해 향후 10년간 기업 소프트웨어의 판도를 바꿀 수 있도록 지원하는지 설명해 드리겠습니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: 프로토콜·표준 · 코딩 에이전트 · 온톨로지·데이터계층
- 원문: `transcripts/channels/ServiceNow/Michael_Park's_AI_Whiteboard_Masterclass__0Fmw61s8CKc.md`

**341. [Introducing AI Experience by ServiceNow](https://www.youtube.com/watch?v=lrQylmrcbXs)** — ServiceNow · 데이터·컨텍스트·거버넌스 · US · 2025-10 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [음악] 인공지능을 사람들에게 유익하게 활용하는 새로운 방식에 오신 것을 환영합니다 . ServiceNow는 기업을 위한 유일한 AI 우선 플랫폼을 보유하고 있습니다. 반세기 넘게 쌓아온 혼란을 깔끔하게 정리해 주는 아름다운 경험 레이어입니다. 저희는 고객의 전체 AI 생태계를 관리, 통제 및 보호하기 위해 특별히 설계된 환경을 구축했습니다 . ServiceNow의 AI 경험은 모든 AI, …
- B1 디지털·AI 기술의 활용: 당사의 CRM은 영업, 주문 처리 및 서비스 팀을 AI 에이전트와 연결하여 고객이 스스로 문제를 해결할 수 있도록 지원하고, 콜센터 및 운영 팀의 효율성을 높이며, 더욱 빠르고 선제적인 서비스를 제공합니다.
- B4 가치네트워크·생태계: 저희는 고객의 전체 AI 생태계를 관리, 통제 및 보호하기 위해 특별히 설계된 환경을 구축했습니다 .
- 수치 주장: 이것이 바로 포춘 500대 기업의 85%가 AI, 데이터 및 워크플로우를 단일 AI 환경으로 통합하는 유일한 플랫폼인 ServiceNow를 선택하는 이유입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/ServiceNow/Introducing_AI_Experience_by_ServiceNow__lrQylmrcbXs.md`

**342. [Poisoning the Well: The Invisible Danger in Your AI Supply Chain](https://www.youtube.com/watch?v=CjHBPfPYuyg)** — ServiceNow · 데이터·컨텍스트·거버넌스 · US · 2026-01 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 이번 새로운 AI 연구 세션에 오신 모든 분들을 환영하며, 참여해 주셔서 감사합니다 . 제 이름은 마릴리즈이고 오늘 여러분의 진행을 맡겠습니다. 이번 짧고 유익한 강연 시리즈는 Saras now AI 연구팀의 최첨단 연구 성과를 소개합니다 . AI 연구 소식은 누구나, 특히 빠르게 변화하는 AI 연구 커뮤니티의 최신 소식을 접하고 싶은 분들에게 열려 있습니다. 오늘 세션에서는 레오 부가 AI…
- B2 파괴: 데이터 가용성: 음, 여기 몇 가지 논문이 있는데, 이 논문들은 이러한 접근 방식이 에이전트를 훈련시키기 위한 많은 데이터를 수집하는 데 점점 더 많이 사용되고 있음을 보여줍니다.
- B1 디지털·AI 기술의 활용: 이건 음, 미터가 올해 발표한 논문의 스크린샷인데, AI 에이전트가 수행할 수 있는 작업의 길이가 대략 7개월마다 두 배로 늘어난다는 것을 보여줍니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/ServiceNow/Poisoning_the_Well_The_Invisible_Danger_in_Your_AI_Supply_Ch__CjHBPfPYuyg.md`

---

## Siemens


**343. [Die Zukunft der Industrie: CEOs von Siemens & Schaeffler über KI, Roboter & Industrial Copilot](https://www.youtube.com/watch?v=jEvJOXlENOI)** — Siemens · 물리 AI·자율주행 · DE · 2025-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 그리고 만약 제가 오늘 어디를 간다면 지구본에는 바늘 하나가 들어갈 수 있을 정도였다. 아니면, 내가 말하는 그곳이 어디냐고 해야 할까요? 역량 센터 자동화를 위한 [음악]이라면, 그것은 바늘이 아마도 꽤 정확히 달성하세요. [음악] 한계를 알아야 하지만, 만약 우리가 여기서는 기술이 개방되어 있지 않습니다. 적어도 적용에 있어서는 그렇지 않습니다. 그렇다면 이러한 기술들은, 저는 다음과 같…
- B1 디지털·AI 기술의 활용: 그럼 그때 당신이 이야기할 때 인프라 측면에서 보면, 음, 이것은 주권 클라우드인가요, 아니면 우리가 보유한 클라우드인가요?
- B4 가치네트워크·생태계: 그 점에 있어서는, 센터는 여기에 있고 이는 생태계와도 관련이 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Siemens/Die_Zukunft_der_Industrie_CEOs_von_Siemens_&_Schaeffler_über__jEvJOXlENOI.md`

**344. [Agentic AI: The Next Wave of Industrial AI | Analyst Insights from CES](https://www.youtube.com/watch?v=Syk6BjIM6qE)** — Siemens · 물리 AI·자율주행 · DE · 2026-01 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 안녕하세요, 반갑습니다. 저는 마그누스 에델만입니다. 오늘 저희 작은 스튜디오에 함께해 주셔서 감사합니다. 오늘 저는 두 분의 특별한 손님과 함께합니다. Seammens의 Linda Krumhol과 AI Research의 Stuart Carlo를 모시고 분석가의 관점에서 정말 흥미로운 AI 관련 주제에 대해 이야기 나눠보겠습니다. 숫자에 대해 이야기해 봅시다. 이번 시간에는 트렌드에…
- B4 가치네트워크·생태계: 그는 생태계, 파트너십, 포트폴리오에 대해 이야기했습니다.
- B7 성과: 운영효율: 성공적인 제품 개발을 위해서는 다양한 분야의 전문가들이 모여야 하며, 이를 통해 최종적으로 명확하고 측정 가능한 투자 수익률(ROI)을 달성하고, 이를 발판 삼아 다음 단계, 그리고 그 다음 단계로 나아갈 수 있어야 합니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/Siemens/Agentic_AI_The_Next_Wave_of_Industrial_AI_Analyst_Insights_f__Syk6BjIM6qE.md`

**345. [How PepsiCo Uses Digital Twins & AI to Rethink Manufacturing](https://www.youtube.com/watch?v=YkTGMNQ9_FI)** — Siemens · 물리 AI·자율주행 · DE · 2026-01 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 환영합니다. 오늘은 소비재 산업 에서 가장 야심찬 변화 중 하나를 살펴보겠습니다 . 오늘 펩시코와 이야기를 나눌 예정입니다. 음, 펩시코는 시먼스 및 엔비디아와 매우 과감한 파트너십을 맺고 있습니다. 그들은 가장 포괄적인 디지털 트윈과 AI를 사용하여 제조, 창고 및 물류를 재구상하기 위해 그렇게 하고 있습니다. 이는 물론 소프트웨어 정의 자동화를 포함한 산업 메타버스의 기반이기도 …
- B4 가치네트워크·생태계: 그러니까 파트너십이란 생태계의 성공을 생각하는 것이고, 지금껏 해오신 일들이 정말 멋지네요.
- B3 전략적 대응: 모든 매개변수를 시뮬레이션하여 사각지대를 파악하고, 최적화 또는 시뮬레이션 과정에서 중요한 매개변수와 중요하지 않은 매개변수를 구분하여 구현 로드맵을 설계하는 동안 발생할 수 있는 잠재적인 외부 교란 요인을 평가할 수 있기 때문입니다 .
- 수치 주장: 그런 경우 20% 효율성 향상은 엄청난 개선입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Siemens/How_PepsiCo_Uses_Digital_Twins_&_AI_to_Rethink_Manufacturing__YkTGMNQ9_FI.md`

**346. [Industrial AI in Practice: From Product Design to Factory Floor with Siemens and NVIDIA](https://www.youtube.com/watch?v=4boWnMQXZMw)** — Siemens · 물리 AI·자율주행 · DE · 2026-01 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, Seaman의 혁신 AI 허브에 오신 것을 환영합니다. 이곳은 Seaman 과 AWS 허브에 위치해 있습니다. 제 이름은 매그너스 에돔입니다. 여러분과 이야기 나누는 시간을 제외하고는 디지털 기업을 이끌고 있습니다. 오늘은 전반적인 변화에 대해 이야기하고, 특히 공장 생산 현장에 초점을 맞춰 살펴보겠습니다. 음, 진행 중인 변화 말이에요. 이 모든 것은 소프트웨어 정의 자동화에 …
- B4 가치네트워크·생태계: 그러면 생태계와 놀라운 파트너십을 맺을 수 있을 거라고 생각합니다.
- B1 디지털·AI 기술의 활용: 특히 방대한 양의 데이터와 오늘날 우리가 빅데이터를 수집하고 이를 스마트 데이터로 변환하여 제품 개발, 제조 계획, 생산, 그리고 제품이 출시된 후의 하위 단계까지 관련된 모든 이해관계자에게 제공할 수 있는 능력을 고려할 때 말입니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Siemens/Industrial_AI_in_Practice_From_Product_Design_to_Factory_Flo__4boWnMQXZMw.md`

**347. [The Industrial AI Revolution: Siemens Keynote at CES 2026](https://www.youtube.com/watch?v=R4Wm6YdoZSs)** — Siemens · 물리 AI·자율주행 · DE · 2026-01 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: [박수] CES에 오신 것을 환영합니다. 전기가 없던 시절을 떠올려 보세요. 세상은 사람들의 속도에 맞춰 움직였다. 말은 우리 사이의 거리를 좁혀주었다. 증기는 우리의 기계를 움직이는 동력이었고, 아이디어는 편지나 사람의 목소리만큼 빠르게 전달되었습니다 . 그러다 전기가 들어왔습니다. 이러한 채널 목적 기술은 현대 생활의 기반이 되었습니다. 그것은 밤을 낮으로 바꾸고, 인간의 능력을 증폭시키…
- B1 디지털·AI 기술의 활용: 따라서 미래에 자동차 공장이든, 반도체 공장이든, AI 공장이든, 어떤 제조 공장을 짓더라도 디지털 트윈을 먼저 활용하지 않고서는 그 어떤 공장도 건설할 수 없다는 것은 상상조차 할 수 없는 일이며, 인공지능 없이는 이처럼 복잡한 시스템을 운영할 수 있다는 것 또한 상상할 수 없는 일입니다.
- B4 가치네트워크·생태계: 그리고 마지막으로, 산업 AI 분야에서 이러한 모든 산업 디자인, 제조 및 운영 데이터를 활용하려면 엄청난 양의 컴퓨팅 자원, 즉 AWS나 마이크로소프트와 같은 파트너사가 운영하는 거대한 중앙 집중식 AI 팩토리가 필요할 뿐만 아니라, 기계 및 인프라에 매우 가까운 엣지 컴퓨팅 환경도 필요합니다.
- 수치 주장: 세멘스는 50년 이상 산업 분야에 AI를 적용해 온 경험을 바탕으로 이러한 솔루션을 구축할 수 있습니다.
- 교량: 정의 확장(DX→AX 계승) · 기술: 칩·하드웨어
- 원문: `transcripts/channels/Siemens/The_Industrial_AI_Revolution_Siemens_Keynote_at_CES_2026__R4Wm6YdoZSs.md`

**348. [How Physical AI is Transforming Industries: AWS and Siemens on Manufacturing and Robotics](https://www.youtube.com/watch?v=EfYVIaGQwts)** — Siemens · 물리 AI·자율주행 · DE · 2026-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 물리적 AI가 산업을 어떻게 변화시키고 있는지에 대한 저희 세션에 오신 모든 분들을 환영합니다 . 이번 시간에는 디지털 지능이 제조, 자동화, 로봇 공학 등을 통해 물리적 세계를 어떻게 변화시키는지 살펴보겠습니다. 제 이름은 마리아 루트이고, Seammen's에서 산업용 소프트웨어 엣지-클라우드 통합 및 산업용 AI를 전문으로 하는 글로벌 파트너 관리 책임자입니다. 오늘 연사분들을 소개해 드…
- B1 디지털·AI 기술의 활용: AWS IoT Sitewise 엣지와 Zemen의 산업용 엣지 또한 마찬가지로, 통합된 방식으로 작동하여 OTC OT 운영 기술을 클라우드로 연결하는 가교 역할을 할 수 있습니다.
- B4 가치네트워크·생태계: Seammens나 AWS 같은 기업들이 투자하고 혁신을 지속하는 동안, 우리는 Nvidia 같은 기업들과 파트너십을 맺고, 대규모 로봇 공학 분야의 전문가들을 모아, 차세대 혁신가들이 실세계의 문제를 해결할 수 있는 솔루션을 개발하도록 지원함으로써 생태계를 하나로 통합하고자 합니다.
- 수치 주장: 그러니까, 기억하시겠지만, 이 모든 것은 실제로 200~200 년 전에 기계 자동화로 시작되었고, 그 기계 장치들은 증기로 구동되다가 나중에는 전기로 구동되었는데, 이는 근본적인 기술이었습니다.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/Siemens/How_Physical_AI_is_Transforming_Industries_AWS_and_Siemens_o__EfYVIaGQwts.md`

**349. [Roland Busch präsentiert Siemens Wachstumsstrategie und Industrial-AI-Vision | HV München 2026](https://www.youtube.com/watch?v=BnLqYZQ2uCo)** — Siemens · 물리 AI·자율주행 · DE · 2026-02 · en · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: New markets New products New technologies Artificial Intelligence Siemens is an innovation leader for industrial AI We combine the real and the digital worlds For the next stage of growth Welcome Annual General Assembly …
- B1 디지털·AI 기술의 활용: Through AI, through automation, through the Digital Twin, we make our processes so standardized and efficient in manufacturing, in development, and of course, in service.
- B4 가치네트워크·생태계: That's good for our environment, and it's good for us because it makes us more independent of global resources and thus makes our supply chains more resilient.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Siemens/Roland_Busch_präsentiert_Siemens_Wachstumsstrategie_und_Indu__BnLqYZQ2uCo.md`

**350. [Scaling Industrial AI from Months to Days, Siemens and AWS Joining Hands](https://www.youtube.com/watch?v=356iStxtsoo)** — Siemens · 물리 AI·자율주행 · DE · 2026-05 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 다음으로는 지멘스와 AWS가 에를랑겐에 있는 지멘스 전자 공장의 실제 비전 AI 구축 사례를 통해 산업용 AI를 대규모로 가속화하는 방법을 살펴보겠습니다 . 지멘스 산업용 엣지 컴퓨팅과 AWS의 공동 아키텍처를 표준화함으로써 배포 시간을 몇 달에서 며칠로 단축할 수 있었습니다. 더 자세한 이야기를 들려주시기 위해 두 분의 손님을 모시게 되어 기쁩니다. 지멘스의 첨단 광학 검사 및 폐쇄 루프 …
- B1 디지털·AI 기술의 활용: 여기서 보시는 것처럼 머신러닝 운영(ML ops)은 일반적인 구축-실행 주기이며, 이는 지멘스와 AWS가 함께 엣지에서 클라우드까지 밀접하게 연관되어 있습니다 .
- B7 성과: 운영효율: 작업을 실행하고 작업이 완료되면 다시 배포하면 되므로 클라우드 자체의 확장성을 활용하여 비용을 절감할 수 있습니다 .
- 수치 주장: 2015년을 기억하시는 분들도 계시겠지만, 11년 전 그 해는 애플이 새로운 애플 워치를 출시했던 해입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Siemens/Scaling_Industrial_AI_from_Months_to_Days,_Siemens_and_AWS_J__356iStxtsoo.md`

**351. [From Data to Value: Siemens Digital Enterprise for Consumer Packaged Goods](https://www.youtube.com/watch?v=W0UJXVK-Vhg)** — Siemens · 물리 AI·자율주행 · DE · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 여러분 모두 하노버 메세 2026에 오신 것을 환영합니다. 27번 홀에 위치한 지멘스 부스에서 여러분을 맞이할 예정입니다. 이번에 처음으로 저희 전시장을 거실처럼 꾸며 이곳으로 옮겨왔습니다. 가구는 여전히 변함없이 하노버 메세에서 가장 편안한 공간입니다. 산업계가 한자리에 모이는 이곳에서 저희 전문가들이 다양한 솔루션에 대해 이야기 나누고 있습니다. 특히 인공지능은 올해 큰 화두입니…
- B1 디지털·AI 기술의 활용: 디지털 트윈은 레시피 데이터, 공정 데이터, 자동화 장비를 포함한 물리적 장비 데이터를 결합하여 생산 공정을 초기 단계에서 가상으로 테스트, 조정 및 최적화함으로써 실제 생산을 더 빠르고 정확하게 시작할 수 있도록 지원합니다 .
- B4 가치네트워크·생태계: 또한 당사는 파트너사의 지원을 받아 전체 공급망에 걸쳐 엔드투엔드 추적성을 보장할 수 있습니다.
- 수치 주장: 당사는 AI 기반 시각 검사 솔루션을 자동화 시스템에 직접 통합하여 분당 최대 2,400장의 이미지를 처리하고 결함을 감지하고 실시간 알림을 발생시키며 실시간 품질 KPI를 시각화할 수 있도록 했습니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/Siemens/From_Data_to_Value_Siemens_Digital_Enterprise_for_Consumer_P__W0UJXVK-Vhg.md`

**352. [How to Scale Industrial AI in Real Factory Operations](https://www.youtube.com/watch?v=46KctH5TgSs)** — Siemens · 물리 AI·자율주행 · DE · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 안녕하세요, 하노버 2026에 오신 것을 환영합니다. 저는 노아 콜이고, 오늘 모두가 관심을 갖고 있는 주제인 산업 AI에 대해 잠시 이야기해 보겠습니다. 제 생각에는 전시장을 둘러보면 알 수 있듯이 산업용 AI는 어디에나 있습니다. 인공지능은 제조, 디자인, 의료, 모빌리티 등 우리 삶의 많은 부분을 변화시키고 있습니다. 이는 우리가 설계하고, 건설하고, 운영하는 방식을 혁신하고 …
- B4 가치네트워크·생태계: 앞으로는 파트너십이 더욱 강화되고, 대규모 고객이 매일매일 효율적으로 사용할 수 있는 일관된 엔드투엔드 프로세스가 마련될 것입니다 .
- B1 디지털·AI 기술의 활용: 또한 작업자가 이 환경에서 어떻게 이동하고 무엇을 할 수 있는지, 작업자가 할 수 있는 일과 원격으로 할 수 있는 일, 그리고 미래에는 AI 에이전트가 할 수 있는 일까지 이해해야 합니다.
- 수치 주장: " 제 데이터에서 가장 피하고 싶은 것은 20년 된 SharePoint 파일에서 데이터를 가져와서 AI에 적용하는 것입니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Siemens/How_to_Scale_Industrial_AI_in_Real_Factory_Operations__46KctH5TgSs.md`

**353. [AI-Based Process Control at Scale: Pringles and Siemens on Digital Transformation in CPG](https://www.youtube.com/watch?v=-B__O2eqRYc)** — Siemens · 물리 AI·자율주행 · DE · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: [음악] 최고야. 지혜의 소파에 앉아봅시다 . 어떻게 지내세요? 엄청난. 감사합니다. 매우 좋은. 매우 좋은. 다니엘은 마치 축구 클럽 선수처럼 보이네요. [웃음] 하지만 여기 소파에 앉아 계신 분들은 딱 축구 팬분들이시네요. 지금 누가 저와 함께하는지 간단히 소개해 드리겠습니다. 우리는 지멘스의 컨설팅 부사장인 다니엘 클라인을 모셨습니다. 다니엘, 그런 프로세스들을 생각해내는 걸 보니 당신…
- B1 디지털·AI 기술의 활용: 음, 세드릭, 한 단계 더 나아가서 모든 것이 데이터와 디지털 트윈, 디지털 스레드를 통해 연결될 때, 개별적인 사용 사례를 넘어 어떤 가능성이 열리게 될까요?
- B4 가치네트워크·생태계: 또한 주주들에게도 이익을 제공해야 하므로 , 혁신적인 순환 과정에서 디지털화를 추진하는 것은 공급망 생산성을 향상시키고 회사에 비용 절감을 가져다줄 뿐만 아니라 혁신을 통해 해당 카테고리에 새로운 변화를 가져올 수 있는 기회를 제공합니다.
- 수치 주장: 제 생각에 전환점은 2023년에 지멘스와 파트너십을 시작했을 때였고, 그때부터 프링글스 사업의 모든 것이 바뀌었습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Siemens/AI-Based_Process_Control_at_Scale_Pringles_and_Siemens_on_Di__-B__O2eqRYc.md`

**354. [Coca-Cola's Factory of the Future: Digital Twins and Industrial AI in Beverage Manufacturing](https://www.youtube.com/watch?v=CjVsewDPX3w)** — Siemens · 물리 AI·자율주행 · DE · 2026-07 · en · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Well, hello, Hannover Messe 2026, Wednesday. Here we are, heading for the finish line of a busy week for everybody. Thank you all for joining us for this session. Here with Coca-Cola, Accenture and Siemens. We want to te…
- B1 디지털·AI 기술의 활용: And maybe one thing I'll go back to, as we talked about the Factory of the Future work and the different layers in the architecture, of which digital twin was an important piece.
- B4 가치네트워크·생태계: But we'll call them opportunities in the supply chain network, and that drives the need for agility and flexibility within the manufacturing space.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Siemens/Coca-Cola's_Factory_of_the_Future_Digital_Twins_and_Industri__CjVsewDPX3w.md`

**355. [Physical AI, Digital Twins, and the Future of Factory Operations | Siemens, AWS & Amazon Robotics](https://www.youtube.com/watch?v=GAW048wxwGk)** — Siemens · 물리 AI·자율주행 · DE · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 이번 패널 토론에 와주셔서 정말 감사합니다 . 오늘 아마존 웹 서비스의 마리아 라우터 씨를 모시게 되어 기쁩니다. 그녀는 아마존 웹 서비스에서 파트너십을 총괄하고 있습니다 . 또한, 여기 맥커천이라는 분이 계신데, 저희 부사장 중 한 분입니다 . 그는 지멘스에서 30년 이상 근무하며 산업용 메타버스 전략을 담당하고 있습니다. 그러니까, 그분은 지멘스의 베테랑 직원 중 한 분입니다. 그리고 제…
- B1 디지털·AI 기술의 활용: 네, 처리량 증가도 중요하지만, 펩시코, 프링글스 등과 같은 고객사들이 산업용 메타버스나 디지털 트윈을 도입할 때 항상 공통적으로 이야기하는 것 중 하나는 예측 가능성을 매우 중요하게 생각한다는 점입니다.
- B4 가치네트워크·생태계: AWS와 지멘스는 10년 넘게 파트너십을 유지하며 협력해 왔고, 이를 통해 고객에게 솔루션을 더 빠르게 제공하여 고객이 시장에서 가치를 실현할 수 있도록 몇 주 또는 몇 달 안에 서비스를 제공할 수 있게 되었습니다.
- 수치 주장: 우리는 해결해야 할 물량이 300% 증가하는 것을 목격하고 있습니다.
- 교량: Avenue 1 동적역량 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/Siemens/Physical_AI,_Digital_Twins,_and_the_Future_of_Factory_Operat__GAW048wxwGk.md`

---

## Snap


**356. [Cross-industry Collab: Driving Progress When Times Are Tough](https://www.youtube.com/watch?v=gjMutZzFLnA)** — Snap · 수요기업·기타 · US · 2023-11 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B5 구조 변화 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B3 전략 대응, B4 가치창출 경로
- 개요: [박수] [음악] [박수] [음악] [박수] 감사합니다. 로잔, 안아주세요. 네, 감사합니다. 로잔나, 그럼 시작해 볼까요? 아시다시피, 리더는 때때로 정말 어려운 질문을 받기도 합니다. 그런 질문들도 나중에 다루겠지만, 쉬운 질문부터 시작해 보겠습니다. 각자 1분 30초에서 2분 정도 시간을 내어 자기소개를 해주시고, 이 일을 이끌어가는 여러분에 대해 간략하게 이야기해 주시겠어요? 릴리아나…
- B5 직무·역량 변화: 연방 계약 및 준수 프로그램 사무국(OCCP)이라는 작은 기관이 있다는 것은 우리가 여전히 다양한 인재를 채용하고, 기회가 부족했던 지역 사회에 기회를 제공해야 할 책임이 있다는 것을 의미합니다.
- B5 리더십·CDO/CAIO: 따라서 우리는 사람들이 리더십, 소프트웨어 엔지니어링, 또는 역사적으로 소외된 집단이 진출하지 못했던 분야에서 자신의 가능성을 볼 수 있도록 해야 할 책임과 의무가 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Snap/Cross-industry_Collab_Driving_Progress_When_Times_Are_Tough__gjMutZzFLnA.md`

**357. [Snap Ad Platform: Inside Our DR Improvements](https://www.youtube.com/watch?v=bSW2DcihnfI)** — Snap · 수요기업·기타 · US · 2024-05 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [음악] 안녕하세요 여러분, 함께해 주셔서 정말 감사합니다. 지금 시청하고 계신 분들은 스냅챗에 대해 잘 알고 계실 가능성이 높지만, 아마도 잘 모르시는 부분도 있을 거라고 생각합니다. 그래서 오늘은 스냅챗이 오늘날 세상에서 특별한 이유, 스냅챗 사용자층의 성장, 그리고 더욱 효과적인 광고 상품으로 발전해 온 과정에 대해 자세히 알아보려고 합니다. 우선, 스냅챗의 특별함은 무엇일까요? 사실 …
- B7 성과: 운영효율: 테스트 결과, 7일 기간 설정은 1분기 에 클릭 전환량 증가, 구매당 비용 절감, 광고 투자 수익률(ROAS) 향상이라는 결과를 보여주었습니다.
- B1 디지털·AI 기술의 활용: 머신 러닝을 통해 광고 순위 최적화를 개선하고 신호 품질을 향상시켰으며, 이 두 가지 모두 귀사에 실질적인 효과를 가져다주었고, 저희 사업은 전년 대비 21%의 매출 성장을 달성했습니다.
- 수치 주장: 머신 러닝을 통해 광고 순위 최적화를 개선하고 신호 품질을 향상시켰으며, 이 두 가지 모두 귀사에 실질적인 효과를 가져다주었고, 저희 사업은 전년 대비 21%의 매출 성장을 달성했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Snap/Snap_Ad_Platform_Inside_Our_DR_Improvements__bSW2DcihnfI.md`

---

## Snowflake


**358. [Data Engineering from Ingestion to AI-Ready | BUILD 2025 Keynote](https://www.youtube.com/watch?v=XwCnOsZMhyI)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-11 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Please welcome Snowflake's vice President of Product Management, Chris Child. &gt;&gt; Hello everyone and welcome to day three of Build. Over the last two days, you heard from Christian about the incredible advancements …
- B5 직무·역량 변화: Anything else that you want to make sure that you say to all the to data engineers who are paying attention, figuring out how to do their jobs and their careers?
- B1 디지털·AI 기술의 활용: We've also partnered with Oracle and launched a new change data capture capability for high-speed data replication that works across on premise and cloud environments.
- 수치 주장: Can you believe if I said during my grad school I spent an entire internship building a data pipeline to anonymize data and today all I had to do was write that one single SQL function that can do that for me and that I absolutely love how we're bringing out t…
- 교량: Avenue 2 윤리·거버넌스 · 기술: 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Snowflake/Data_Engineering_from_Ingestion_to_AI-Ready_BUILD_2025_Keyno__XwCnOsZMhyI.md`

**359. [Empowering Agility: DraftKings’ Strategy for Compliance and Data Optimization](https://www.youtube.com/watch?v=F01IEeM3I-Y)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 잭, 데이터 클라우드 팟캐스트에 오신 것을 환영합니다. 함께해 주셔서 진심으로 기쁩니다. 여기 오게 되어 정말 기쁩니다, 다나. 초대해 주셔서 감사합니다 . 물론 이죠. 시장 변화에 대한 민첩성과 엄격한 규제 준수라는 두 가지 요구 사항은 DraftKings의 데이터 수집, 분석 및 보고 관리에 특히 복잡한 과제를 안겨줍니다. 드래프트킹스에 대해 설명하고, 끊임없이 변화하는 법적 환경과 미국…
- B1 디지털·AI 기술의 활용: 어, 저희가 2018년 당시에는 단순한 데일리 판타지 게임 회사였는데, 그때는 AWS 클라우드 네이티브 서비스를 100% 활용했고, 아마존에서 제공하는 최고의 네이티브 서비스를 통해 혁신을 이루고자 노력했습니다.
- B4 가치네트워크·생태계: 네, 확실히 네이티브 서비스와의 연결성, 그에 따른 관찰 및 보고 기능, 향상된 보안, 원활한 데이터 접근, 그리고 최적화 , 성능 최적화, 하드웨어 업데이트 등 생태계 자체를 더욱 효율적으로 운영하기 위해 내부적으로 진행되는 모든 작업들을 이해하는 것이 중요하다고 생각합니다.
- 수치 주장: 어, 저희가 2018년 당시에는 단순한 데일리 판타지 게임 회사였는데, 그때는 AWS 클라우드 네이티브 서비스를 100% 활용했고, 아마존에서 제공하는 최고의 네이티브 서비스를 통해 혁신을 이루고자 노력했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 추론 최적화
- 원문: `transcripts/channels/Snowflake/Empowering_Agility_DraftKings’_Strategy_for_Compliance_and_D__F01IEeM3I-Y.md`

**360. [End Data Disparity | Looking Beyond Technology To Maximize Data's Impact](https://www.youtube.com/watch?v=HehmwhyxX9Y)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 반갑습니다. 눈송이들이 데이터 불균형 운동을 끝낸다. 데이터는 우리가 세상을 더 잘 이해하고 개선하는 데 도움이 되며 모든 사람을 대표해야 하지만, 많은 집단이 부분적으로 또는 완전히 배제되고 있습니다. 오늘 대화의 주제는 바로 그것입니다. 저는 Seni에서 비즈니스 혁신, 디지털 데이터 및 AI 전략 부문 글로벌 책임자를 역임했던 제니퍼 웡과 만나 더 자세한 이야기를 나…
- B4 가치네트워크·생태계: 이러한 경험은 데이터 전략, 데이터 거버넌스, 데이터 파트너십 등 데이터에 대한 제 생각을 깊이 있게 형성해 주었고, 궁극적으로 데이터 뒤에는 특정 목표를 위해 헌신적으로 협력하는 사람들뿐만 아니라, 이러한 의사결정의 혜택을 받는 모든 사람들이 중요하다는 것을 깨닫게 해주었습니다.
- B2 파괴: 데이터 가용성: 저희는 정형 데이터와 비정형 데이터 세트를 연결하여 데이터에서 얻을 수 있는 가치를 높이는 방법, 분석 및 AI를 가능하게 하는 다양한 데이터 소스를 통합하여 통찰력 생성 및 의사 결정을 위한 더욱 견고한 그림을 확보하는 방법에 대해 자주 논의해 왔습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Snowflake/End_Data_Disparity_Looking_Beyond_Technology_To_Maximize_Dat__HehmwhyxX9Y.md`

**361. [From Analytics To Intelligence: BlackRock's Journey To Data Productization](https://www.youtube.com/watch?v=Me_H_-E6lSg)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 데이터 클라우드 팟캐스트에 오신 것을 환영합니다, 데이브. 함께해 주셔서 정말 기쁩니다. 여기 오게 되어 기쁩니다. 조직의 데이터 자원을 분석 및 비즈니스 인텔리전스 측면에서 최대한 활용할 수 있도록 최적화하는 것은 프로세스 품질 향상과 비즈니스 성과 개선에 매우 중요합니다. 하지만 선도적인 자산 운용사이자 기술 제공업체인 블랙록에게 있어 현대적인 데이터 인프라는 금융 서비스를 상품화하는 길…
- B1 디지털·AI 기술의 활용: 제 생각에는 우리 기술이 최상의 상태로 작동할 때, 대부분의 사용자는 "아, 이 데이터는 스노우플레이크에서 온 거구나" 또는 "이 훌륭한 인사이트를 제공하는 새로운 엔터프라이즈 데이터 플랫폼이 있구나 "라고 생각조차 하지 않을 것입니다.
- B4 가치네트워크·생태계: 데이터 제품이라는 개념이 인기를 얻으면서 고객들은 알라딘에서 나오는 고품질 데이터를 어떻게 우리 데이터 생태계로 가져올 수 있을지, 또는 알라딘이 어떻게 더 큰 규모의 데이터 활용 도구를 제공하여 투자 프로세스의 역사에 대한 시공간적 질문을 할 수 있도록 해줄 수 있을지 묻기 시작했습니다.
- 수치 주장: 블랙록 내부에는 파이썬이나 R을 사용하여 모든 것과 상호 작용하는 3,000명의 시민 개발자 및 비즈니스 엔지니어가 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Snowflake/From_Analytics_To_Intelligence_BlackRock's_Journey_To_Data_P__Me_H_-E6lSg.md`

**362. [The AI Blueprint for the Next Decade | BUILD 2025 Luminary Conversation](https://www.youtube.com/watch?v=-HWNc-Hd90U)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 스노우플레이크의 최고경영자(CEO)인 스리다르 라마스와미를 환영해 주십시오 . 안녕하세요, 건설업자 여러분. 기술의 발전에는 역사의 전환점처럼 느껴지는 순간들이 있습니다. 그리고 저는 우리가 지금 바로 그러한 시대를 살고 있다는 데에 조금도 의심의 여지가 없습니다. 인공지능은 우리 세대를 가장 혁신적으로 변화시킬 기술입니다 . 그리고 시간이 지날수록 그 사실이 더욱 실감나게 느껴집니다. 수십…
- B1 디지털·AI 기술의 활용: 어, 왜냐하면 현재 자동화된 워크플로우가 가능해진 것은 LLM 덕분만이 아니라, 클라우드와 데이터 API 분야에서 수년간, 수십 년간 이루어진 연구 덕분이며, 이제 클라우드뿐 아니라 Snowflake를 비롯한 여러 기업들이 이 모든 것에 서버리스 방식으로 접근하고 이러한 연산을 탄력적으로 실행할 수 있게 되면서 매우 다양하고 흥미로운 가능성이 열리고 있기 때문입니다.
- B2 파괴: 경쟁구도: 그래서 저는 기업들을 분석할 때, 인공지능 기술 자체보다는 해당 산업의 특성이라는 관점에서 경쟁 우위를 분석하는 경우가 많습니다 .
- 수치 주장: 예를 들어 SAS에서 흔히 볼 수 있는 월 50달러 정도의 가격 대신, 많은 개발자들이 매달 수백 달러, 때로는 1,000달러 이상을 지출합니다.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Snowflake/The_AI_Blueprint_for_the_Next_Decade_BUILD_2025_Luminary_Con__-HWNc-Hd90U.md`

**363. [AI And Real-World Data: A New Era For Identifying And Curing Rare Diseases](https://www.youtube.com/watch?v=i9jLt1_iHK8)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 데이터 클라우드 팟캐스트에 오신 것을 환영합니다, 찬디님. 함께해 주셔서 진심으로 기쁩니다 . 여기 오게 되어 정말 기쁩니다, 다나. 기대하고 있어요 . 저도요. 이제, 방대한 데이터 세트를 구축하기 위해 수많은 이질적인 데이터 소스를 수집하고 활용해야 하는 필요성 덕분에 코모도 헬스는 광범위한 생명 과학 및 의료 관련 연구에서 전례 없는 통찰력을 발견할 수 있게 되었습니다. 규모와 속도 요…
- B2 파괴: 데이터 가용성: 그래서 이 데이터를 통해 해당 개인이 데이터를 얻기 6개월 전에 어떤 일을 겪었는지, 그리고 데이터 수집 후 6개월 동안 그 환자 또는 개인이 어떻게 지내왔는지에 대해 자세히 알아볼 수 있는 풍부하고 심층적인 데이터 세트를 얻을 수 있습니다 .
- B8 부정 성과: 보안·프라이버시: 그래서 저희가 체계적인 네트워크 변환이나 개체 해결, 편향 수정 등을 통해 진행하고 있는 작업은, 식별된 데이터를 바탕으로 개별 환자 수준의 관점 이나 설명을 구축하는 데 도움이 되고 있으며, 이를 통해 연구자들이 환자의 장기적인 치료 여정을 이해할 수 있게 해줍니다.
- 수치 주장: 아시다시피, 저희는 지난 10년 동안 헬스케어 맵이라고 부르는 이 제품을 개발해 왔습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Snowflake/AI_And_Real-World_Data_A_New_Era_For_Identifying_And_Curing___i9jLt1_iHK8.md`

**364. [End Data Disparity: Using Geospatial Data To Improve Cities](https://www.youtube.com/watch?v=YFTTMP6meVQ)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2026-01 · ko · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요, Snowflake의 데이터 불균형 해소 운동에 오신 것을 환영합니다. 데이터는 우리가 세상을 더 잘 이해하고 개선하는 데 도움이 되지만, 모든 사람을 대표해야 함에도 불구하고 많은 집단이 부분적으로 또는 완전히 배제되고 있습니다. 오늘 대화의 주제는 바로 그것입니다. 더 자세한 이야기를 나누기 위해 리버풀 대학교 지리 데이터 과학 강사인 엘리자베타 피에트로 스테파니를 만났습니다.…
- B2 파괴: 데이터 가용성: 예를 들어, 인도주의적 목적의 오픈 스트리트 맵(Open Street Map)은 NGO로서 이러한 격차를 해소하기 위해 많은 지역 사회와 협력하여 지리 정보 데이터를 수집하는 동시에, 머신 러닝 기술을 활용하여 파괴 후 건물을 자동으로 인식하는 등의 노력을 기울이고 있습니다.
- B1 디지털·AI 기술의 활용: 예를 들어, 인도주의적 목적의 오픈 스트리트 맵(Open Street Map)은 NGO로서 이러한 격차를 해소하기 위해 많은 지역 사회와 협력하여 지리 정보 데이터를 수집하는 동시에, 머신 러닝 기술을 활용하여 파괴 후 건물을 자동으로 인식하는 등의 노력을 기울이고 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Snowflake/End_Data_Disparity_Using_Geospatial_Data_To_Improve_Cities__YFTTMP6meVQ.md`

**365. [Daikin Comfort: Building an AI-Ready Value Chain with SAP and Snowflake](https://www.youtube.com/watch?v=0TyLwxQjk1g)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2026-06 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: Please welcome our panel. &gt;&gt; Hi everyone. I'm Saptarshi Mukherjee. I'm a product leader at Snowflake. I lead our streaming data integration, zero copy interoperability product areas based out of Seattle. Thrilled t…
- B1 디지털·AI 기술의 활용: We have these outcomes that are being generated out of Snowflake being fed back into Datasphere and being leveraged in solutions like SAP Analytics Cloud for our insights.
- B4 가치네트워크·생태계: So, from the Snowflake side, now that the partnership, it's generally available, both joint offerings, um what excites you the most about what comes next?
- 수치 주장: Here, as we are working with clients over a period of 24 hours, we are able to take a concept, put it together, prove out the value, and then within a week or two we are able to deploy it in production.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Snowflake/Daikin_Comfort_Building_an_AI-Ready_Value_Chain_with_SAP_and__0TyLwxQjk1g.md`

**366. [Snowflake Summit 2026 Opening Keynote With Sridhar Ramaswamy And Daniela Amodei](https://www.youtube.com/watch?v=F34xlRoQ3eQ)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B2 파괴, B7 긍정 성과, B8 부정 성과
- 개요: 열. [음악] 열기. [음악] 열기. [음악] 열기. 열.열. [음악] 열기. 열. 열.열. [음악] 열기. 열. [음악] 스노우플레이크 최고 경영자 슈레다르 라마스와미를 환영해 주십시오. [음악] 안녕하세요, 저희가 개최한 역대 최대 규모의 최고의 눈송이 정상 회담에 오신 것을 환영합니다. [박수] 2만 명이 넘는 분들이 저희와 함께해 주셨습니다. 500개 이상의 세션, 350개 기관에서 …
- B4 가치네트워크·생태계: 이는 상호 운용성을 높이고 데이터 재사용을 촉진하는 동시에 AI를 활용하여 공급망 혼란을 예측하고, 계획 담당자에게 글로벌 운영 전반에 걸쳐 공급과 수요, 생산 변화에 대응할 수 있는 통찰력을 제공합니다 .
- B1 디지털·AI 기술의 활용: 그들은 또한 매우 뛰어난 엔지니어링 팀을 보유하고 있으며, 저희는 Snowflake를 통해 그들의 데이터 플랫폼 대부분을 지원하고, Anthropic은 클라우드 코드와 같은 놀라운 제품을 제공하여 엔지니어링 팀이 협업하고 실시간 사기 또는 결제 처리와 같은 이전에는 접근할 수 없었던 다양한 새로운 통찰력을 얻을 수 있도록 돕고 있습니다.
- 수치 주장: 1년 후, 그들은 Snowflake AI를 사용하여 제품 의사 결정 방식을 혁신하고, 사용자 행동 및 기능 영향에 대한 몇 주간의 분석 작업을 거의 실시간에 가까운 인사이트로 전환하고 있을 것입니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/Snowflake/Snowflake_Summit_2026_Opening_Keynote_With_Sridhar_Ramaswamy__F34xlRoQ3eQ.md`

**367. [The 2026 Snowflake Startup Challenge Finale with Three Visionary Teams](https://www.youtube.com/watch?v=Nm9JhTrcREQ)** — Snowflake · 데이터·컨텍스트·거버넌스 · US · 2026-06 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: Hello, Snowflake Summit and Developer Day. We are back with another installment of the Snowflake Startup Challenge. Now in its sixth year and in partnership with the New York Stock Exchange, this competition continues to…
- B1 디지털·AI 기술의 활용: Well, go no further because Arrived provides Agentic OS, an enterprisegrade operating system that allows organizations to build, fine-tune, orchestrate, and govern autonomous AI agents across cyber security, IT, and business operations without needing speciali…
- B4 가치네트워크·생태계: His work involves identifying, nurturing, and making strategic investments to drive industry innovation and accelerate Capital 1's partnerships with emerging companies.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Snowflake/The_2026_Snowflake_Startup_Challenge_Finale_with_Three_Visio__Nm9JhTrcREQ.md`

---

## Stanford Health Care


**368. [AI Transforms Health Care | Artificial Intelligence: The Future of Medicine & Health Care Is Here](https://www.youtube.com/watch?v=wD1qn2i3Wb4)** — Stanford Health Care · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 기대가 크셨군요. 완벽합니다. 릭, 초대해 주셔서 감사합니다. 저는 항상 스탠포드에 있었습니다. 2005년에 연구원으로 합류한 이후로 떠나지 않았죠. 그 이후로 거의 반경 3마일 이내에서 지냈습니다. 제대로 된 직업을 가져본 적이 없고, 지금도 없습니다. 그래서 오늘 처음 40분 동안은 몇 가지 사례를 통해 현재 상황이 어떻게 전개되고 있는지 간략하게 살펴보겠습니다. 가장 중요한 것은 이러한…
- B7 성과: 운영효율: 시간을 절약할 수 있기를 기대했고, 만약 시간을 절약할 수 있다면 생산성 향상에 큰 도움이 될 것이라고 생각했습니다.
- B1 디지털·AI 기술의 활용: 무슨 말이냐면, 의학 분야에서 LLM(대규모 언어 모델)을 사용한 논문 약 520편을 대상으로 설문조사를 실시했습니다.
- 수치 주장: 따라서 훌륭한 AI는 데이터에서 시작되며, 이것이 바로 샌포드 대학교가 2005년 제가 캠퍼스에 부임했을 때부터 좋은 데이터 인프라를 구축하기 위한 여정을 시작한 토대입니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/2026-07-21/AI_Transforms_Health_Care_Artificial_Intelligence_The_Future__wD1qn2i3Wb4.md`

---

## Telenor


**369. [Sigve Brekke and Kjerstin Braathen, CEO of DNB: Do banking and telecom have anything in common?](https://www.youtube.com/watch?v=gDgq25NAbsg)** — Telenor · 통신·주권·국가 · NO · 2021-06 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: hello everyone um i'm here today with justin broughton and justin you are the ceo of norway's biggest bank and what i would like to talk a little bit about it's how we now see that digital journey it's not only coming it…
- B4 가치네트워크·생태계: hello everyone um i'm here today with justin broughton and justin you are the ceo of norway's biggest bank and what i would like to talk a little bit about it's how we now see that digital journey it's not only coming it's actually accelerating and and what we…
- B5 리더십·CDO/CAIO: hello everyone um i'm here today with justin broughton and justin you are the ceo of norway's biggest bank and what i would like to talk a little bit about it's how we now see that digital journey it's not only coming it's actually accelerating and and what we…
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Telenor/Sigve_Brekke_and_Kjerstin_Braathen,_CEO_of_DNB_Do_banking_an__gDgq25NAbsg.md`

**370. [Telco Tech Talks: Modern technology's role in modern crises](https://www.youtube.com/watch?v=4rJPXX_M6Zo)** — Telenor · 통신·주권·국가 · NO · 2022-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 저는 텔레노르 그룹의 사장 겸 CEO인 시바 리키입니다. 오늘 저희와 함께 최고 기술 책임자(CTO)이자 게스트인 케네스 씨를 모시고 이 자리에 함께하게 되어 기쁩니다. 텔레코 테크 토크 세 번째 에피소드에 오신 것을 환영합니다. 이 토크에서는 새로운 기술이 다양한 가치 사슬과 다양한 고객 유형에서 서비스 제공 방식에 어떤 새로운 의미를 갖는지 좀 더 심층적으로 살펴보려고…
- B1 디지털·AI 기술의 활용: 이제 자체 생태계를 구축하는 단계를 넘어 상용 생태계, 즉 5G와 같은 상용 네트워크, 상용 클라우드 제공업체, 그리고 이미 상용 휴대폰이나 기기까지 포함하는 사업 영역으로 나아가고 계신데, 이러한 사업을 시작할 때 어떤 생각을 하고 계신가요?
- B4 가치네트워크·생태계: 이제 자체 생태계를 구축하는 단계를 넘어 상용 생태계, 즉 5G와 같은 상용 네트워크, 상용 클라우드 제공업체, 그리고 이미 상용 휴대폰이나 기기까지 포함하는 사업 영역으로 나아가고 계신데, 이러한 사업을 시작할 때 어떤 생각을 하고 계신가요?
- 수치 주장: 군대에서 장비를 도입할 때 사용해 온 방식은 전통적인 폭포수 모델 방식의 프로젝트 계획으로, 수천 개의 요구사항을 명시하는 데 그쳤습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Telenor/Telco_Tech_Talks_Modern_technology's_role_in_modern_crises__4rJPXX_M6Zo.md`

---

## The CEO Magazine


**371. [Why AI adoption fails – and how to get it right](https://www.youtube.com/watch?v=JBb2jRns3PA)** — The CEO Magazine · (미분류) · — · 2026-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과
- 개요: I always always try to lead with kindness. What we looked for is how do we take the concern [music] of AI introducing bias and use it to actually overcome human bias. The only thing that's worse than a bad process is an …
- B1 디지털·AI 기술의 활용: So what we did is we took generative AI and machine learning to look across every loan program that this borrower could possibly qualify for.
- B8 부정 성과: 보안·프라이버시: So we wanted to make sure that the prompts that we were using were complete and also that they couldn't be misinterpreted so that it would generate hallucinations in the AI.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/2026-07-18/Why_AI_adoption_fails_–_and_how_to_get_it_right__JBb2jRns3PA.md`

---

## The Tech Trek


**372. [Enterprise AI Adoption in 2025: What Actually Works](https://www.youtube.com/watch?v=9MkMQ6zkjLw)** — The Tech Trek · (미분류) · — · 2026-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: On this episode of the show, I have with me Matt McCclardy. He is CTO Aboomi and we're going to be talking about enterprise AI adoption. We're going to talk about some of the companies that are succeeding and why some th…
- B1 디지털·AI 기술의 활용: But that's the problem there is like the area where machine learning was is most effective still is most effective and and actually I would argue much more effective than Genaii in a lot of ways for for what it does is very analytics focused data you know supe…
- B4 민첩성·양손잡이: Um, I'm I I know of a bank who wanted to adopt agile and so they removed chairs from the meeting rooms so that all the meetings were standup meetings.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/2026-07-18/Enterprise_AI_Adoption_in_2025_What_Actually_Works__9MkMQ6zkjLw.md`

---

## Unilever


**373. [Unilever | Full Year 2023 Results | Webcast & Q&A](https://www.youtube.com/watch?v=YUdGwlJiDUk)** — Unilever · 수요기업·기타 · NL · 2024-02 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 유니레버의 연간 실적 발표에 오신 것을 환영합니다. 오늘 저는 새롭게 취임하신 최고재무 책임자(CFO) 페르난도 페르난데스 씨와 함께 이 자리에 서게 되어 매우 기쁩니다. 아시다시피 페르난데스 씨는 1월 1일부터 CFO 직을 맡게 되셨습니다. 페르난도는 이 직책에는 새로 부임했지만, 유니레버에는 결코 낯선 인물이 아닙니다. 그는 이전에 유니레버의 뷰티 및 웰빙 사업 그룹 사장을 …
- B7 성과: 운영효율: 이 팀은 운영 효율성과 생산성을 향상시키기 위해 사업 전반의 경제성을 검토하고 있습니다 .
- B7 성과: 조직성과: 판매량 감소의 주요 원인은 유럽에서 발생했는데, 우리는 수익성이 없는 품목을 단종 시키는 등 적극적으로 제품 구성을 합리화해 왔으며, 소비자들이 자체 브랜드 제품으로 눈을 돌리는 현상이 지속되고 있습니다.
- 수치 주장: 첫째, 4분기에는 1.8%의 판매량 증가를 기록했고, 하반기에는 매출총이익률이 330bp 확대되었습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Full_Year_2023_Results_Webcast_&_Q&A__YUdGwlJiDUk.md`

**374. [Unilever | H1 2024 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=Yc8FoPwlXxQ)** — Unilever · 수요기업·기타 · NL · 2024-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, UNI Lever의 상반기 실적 발표에 오신 것을 환영합니다. 오늘 발표는 약 25분 정도 소요될 예정이며, 나머지 30분은 질의응답 시간입니다. 오늘 웹캐스트 전체 내용은 화면에 실시간으로 자막과 함께 제공되니 참고하시기 바랍니다. 잠시 후 페르난도에게 마이크를 넘겨 실적에 대한 자세한 내용을 안내해 드리겠습니다. 이후 성장 액션 플랜과 하반기 주요 우선순위에 대한 간략한 업데…
- B7 성과: 운영효율: 당사는 매출 증대, 제품 믹스 개선, 조달 혁신, 생산 및 물류 비용 절감을 통한 생산성 향상 등을 통해 유니버시티를 구조적으로 높은 매출총이익률을 가진 사업으로 전환하는 데 지속적으로 진전을 이루고 있습니다.
- B7 성과: 조직성과: 자산 측면에서 볼 때, 약 2%의 꾸준한 매출 성장을 바탕으로 자본 지출의 약 30%를 생산 능력 증대 또는 혁신 활동에 할당할 계획이며, 앞서 말씀드린 것처럼 50~60%는 마션 마링(Martian Maring) 확장 계획에 할당할 예정입니다.
- 수치 주장: 매출은 4.1% 증가했고, 판매량은 전반적으로 증가했으며, 특히 4~5개 사업 부문에서 2.6%의 성장률을 기록했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_H1_2024_Results_Webcast_&_Q&A__Yc8FoPwlXxQ.md`

**375. [Unilever Investor Event 2024 - Key takeaways](https://www.youtube.com/watch?v=NdZLX0ZfZi0)** — Unilever · 수요기업·기타 · NL · 2024-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B6 장벽, B8 부정 성과
- 개요: 2024년 언레버리지 투자 설명회에 오신 것을 환영합니다. 오늘은 이러한 변화의 진행 상황을 알려드리고, 1년 전 발표한 성장 실행 계획(Growth Action Plan) 또는 격차 해소 계획(Gap) 대비 진척 상황을 공유하고자 합니다. 현재 계획대로 진행되고 있는 부분과, 더 중요하게는 앞으로 해야 할 실질적인 과제들을 차트에서 보시는 바와 같이 말씀드리겠습니다. 지난 1년여 동안 운영…
- B7 성과: 조직성과: 유니버시티 포트폴리오는 각 사업 그룹별로 명확하게 정의된 수익성을 가지고 있으며, 구성이 각기 다른 이러한 사업 그룹들이 장기적인 성장 전망 범위 내에서 매출 성장과 수익성 성장을 동시에 달성할 수 있다고 확신합니다.
- B3 전략적 대응: 이러한 변화는 이사회와 경영진 차원에서 크게 쇄신된 리더십 팀에 의해 주도되었습니다.
- 수치 주장: 마지막으로, 유럽에서는 프리미엄화 및 전문 채널 중심의 포트폴리오로 전환하여 2024년에 이룬 성과를 더욱 강화할 계획입니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Investor_Event_2024_-_Key_takeaways__NdZLX0ZfZi0.md`

**376. [Unilever | H1 2025 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=_FqeVQgaPKM)** — Unilever · 수요기업·기타 · NL · 2025-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 열. [음악] 안녕하세요, 2025년 유니리버 2분기 실적 발표에 오신 것을 환영합니다. 함께해 주셔서 감사합니다. 오늘 저는 최고재무책임자 대행인 시니 파탁 씨와 함께 이 자리에 참석했습니다. 잠시 후 시니가 2분기와 상반기 실적에 대한 자세한 내용을 알려드리겠습니다. 그 후에는 사업의 지속적인 변화와 올해 남은 기간 및 그 이후를 어떻게 전망하는지에 대해 좀 더 폭넓게 이야기하겠습니다. …
- B7 성과: 운영효율: 이는 우리가 활용하는 올바른 수단, 즉 뛰어난 물량과 제품 구성, 조달 조직을 통한 세계적 수준의 비용 절감, 전반적인 비용 규율 및 서비스 제공 비용, 그리고 자본 지출을 비용 절감 방향으로 재조정한 결과입니다.
- B7 성과: 조직성과: 특히, 저희는 기네(Guine)와 리퀴드 아이( Liquid I) 및 뉴트라폴(Neutrafall) 두 브랜드 모두 두 자릿수 성장을 기록하며 탁월한 실적을 거두었고, 두 브랜드 모두 올해 매출 10억 달러 돌파를 눈앞에 두고 있습니다.
- 수치 주장: 시장 상황이 부진했음에도 불구하고 상반기 동안 판매량은 전분기 대비 개선되었으며, 상반기 시장 판매량 증가율은 약 1.3%를 기록했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_H1_2025_Results_Webcast_&_Q&A___FqeVQgaPKM.md`

**377. [Unilever | H1 2025 | Results | Webcast & Q&A – audio-described](https://www.youtube.com/watch?v=oMDBIXBEv3Q)** — Unilever · 수요기업·기타 · NL · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 제목 슬라이드가 나타나는데, 왼쪽에는 유니레버 U 로고의 커다란 흰색 윤곽선이 부분적으로 보입니다. 오른쪽에는 굵은 흰색 글씨로 '2025년 상반기 결과'라고 적혀 있습니다. 작은 글씨로 Fernando Fernandez와 Shrinst Pek이라는 이름과 2025년 7월 31일이라는 날짜가 적혀 있습니다. 오른쪽 하단에는 필기체로 쓰인 Unilever라는 단어 위에 흰색 Unilever 로…
- B7 성과: 조직성과: 저희는 상반기에 견실한 실적을 달성했으며, 2025년까지 매출 3~5% 성장 전망을 유지하고, 물량과 가격의 균형을 잘 맞추며, 하반기 영업이익률을 최소 18.5%까지 끌어올릴 수 있을 것이라는 확신을 다시 한번 말씀드리고 싶습니다.
- B7 성과: 운영효율: 저는 여기에 덧붙여 말씀드리고 싶은 것은, 우리가 공급망 관리, 비용 절감, 제조 및 물류 개선에 중점을 두어 총마진이 구조적으로 향상되고 있으며, 아이스크림 사업부 분리 발표 이후 간접비 절감 측면에서 생산성 향상을 이루어낸 것은 근본적으로 캠페인 문화의 변화를 보여주고 있다는 점입니다.
- 수치 주장: 시장 상황이 부진했음에도 불구하고 상반기 동안 판매량은 전분기 대비 개선되었으며, 상반기 시장 판매량 증가율은 약 1.3%를 기록했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_H1_2025_Results_Webcast_&_Q&A_–_audio-described__oMDBIXBEv3Q.md`

**378. [Unilever | Q3 2025 Trading Statement | Results | Webcast & Q&A](https://www.youtube.com/watch?v=xWdZMbXzL-M)** — Unilever · 수요기업·기타 · NL · 2025-10 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요. 유니레버의 2025년 3분기 실적 발표에 오신 것을 환영합니다. 오늘 함께해 주셔서 감사합니다. 오늘 시니 파탁 씨가 함께해 주셨습니다. 시니의 최고재무책임자(CFO) 임명은 광범위한 인선 과정을 거쳐 지난달 이사회에서 확정되었습니다. 시니의 풍부한 경험과 전문성은 유니리버에 큰 자산이며, 우리가 지금까지 쌓아온 탄탄한 파트너십을 더욱 발전시켜 나갈 수 있게 되어 매우 기쁩니다 …
- B7 성과: 운영효율: 당사의 주력 브랜드들은 지속적으로 우수한 실적을 기록하며 분기별 4.4%의 성장률을 달성했고, 전체 그룹의 판매량은 1.7% 증가했으며, 아이스크림을 제외한 판매량은 2.2% 증가했습니다 .
- B7 성과: 조직성과: 생산성 향상 프로그램을 성공적으로 완료했을 뿐만 아니라, 이제는 조직 내에서 생산성을 습관화 하고 문화를 정착시켜 수년간 꾸준히 매출 성장률보다 낮은 비용을 유지할 수 있도록 하고 있습니다.
- 수치 주장: 시장 상황이 좋지 않았음에도 불구하고, 아이스크림을 제외한 유니리버 제품의 검색량은 4% 증가하고 거래량 증가율도 1.7%로 가속화되는 등 양호한 분기 실적을 달성했습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Q3_2025_Trading_Statement_Results_Webcast_&_Q&A__xWdZMbXzL-M.md`

**379. [Unilever | Q3 2025 Trading Statement | Results | Webcast & Q&A - audio-described](https://www.youtube.com/watch?v=X59yNoX8xQs)** — Unilever · 수요기업·기타 · NL · 2025-11 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 제목 슬라이드가 나타납니다. '2025년 3분기 실적 발표'라고 적혀 있습니다. 그 아래에는 페르난도 페르난데스와 슈리나스 펙의 이름과 2025년 10월 23일이라는 날짜가 적혀 있습니다. 파란색 그라데이션 배경 왼쪽에는 유니레버의 U자 모양이 크게 자리하고 있습니다 . 면책 조항이 나타납니다. 성명서 전문 링크는 이 영상 설명란에서 확인하실 수 있습니다. 페르난도 페르난데스 최고경영자가 짙…
- B7 성과: 조직성과: 특히 웰빙(Wellbe) 브랜드는 미국에서 매우 뛰어난 성과를 지속적으로 보여주고 있으며, 리퀴드 타입과 뉴트라폴(Neutrafall) 모두 두 자릿수 성장을 기록하며 연간 매출 100만 달러 돌파를 눈앞에 두고 있습니다.
- B7 성과: 운영효율: 코네토는 높은 한 자릿수 성장률을 기록하며 선두를 달렸고, 벤앤제 리스는 지속적인 일요일 한정 맛 출시와 지속적인 운영 개선 및 체계적인 실행에 힘입어 한 자릿수 중반대의 성장을 보였습니다.
- 수치 주장: 시장 상황이 좋지 않았음에도 불구하고, 유니레버는 아이스크림을 제외한 부문에서 검색량이 4% 증가하고 거래량 증가율이 1.7%로 가속화되는 등 양호한 분기 실적을 달성했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Q3_2025_Trading_Statement_Results_Webcast_&_Q&A_-_a__X59yNoX8xQs.md`

**380. [Fireside Chat with Fernando Fernandez, Unilever CEO and Celine Pannuti, JP Morgan](https://www.youtube.com/watch?v=djVmMTAMEho)** — Unilever · 수요기업·기타 · NL · 2025-12 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 어 [음악] 어 헤이. [음악] 헤이. [음악] 헤이, [음악] 헤이, [음악] 헤이. [음악] 안녕하세요, 여러분. 저는 JP Morgan의 필수소비재 부문 책임자인 셀린 페누티입니다 . 오늘 함께해 주셔서 대단히 감사합니다. CEO 대담 시리즈의 일환으로 유니리버에서 페르난도 페르난데스 유니리버 CEO님을 모시게 되어 매우 기쁩니다. 페르난도, 저희를 초대해 주셔서 정말 감사합니다. 아니…
- B2 파괴: 경쟁구도: 대학가에 많은 변화가 일어나고 있는 만큼, 단순히 포트폴리오를 바꾸는 것뿐만 아니라 빠르게 성장하는 새로운 분야에서 경쟁사를 능가하는 성과를 내야 한다는 점입니다.
- B7 성과: 조직성과: 어, 그리고 이 모든 것을 종합해 볼 때, 4~6%의 매출 성장과 적당한 수준의 마진 확대를 통해 우리는 업계 상위 30위권에 진입할 수 있을 것이라고 생각합니다.
- 수치 주장: 마지막으로, 우리는 또한 중요한 변화가 있었는데, 이는 지금까지는 경영진에 적용되었지만 2026년부터는 회사 전체에 걸쳐 구조조정 비용을 이익 성장 계산에 포함시키기로 했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Fireside_Chat_with_Fernando_Fernandez,_Unilever_CEO_and_Celi__djVmMTAMEho.md`

**381. [Q4 and full-year 2025 results webcast and Q&A | Unilever](https://www.youtube.com/watch?v=G86AGZQwVVo)** — Unilever · 수요기업·기타 · NL · 2026-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 유니레버의 전이 제품 결과 발표에 오신 것을 환영합니다 . 함께해 주셔서 감사합니다. 잠시 후, 저희 최고재무책임자인 시니파탁이 2025년 유니레버의 실적에 대한 자세한 분석을 설명해 드릴 것입니다. 하지만 그 전에, 작년 실적에 대한 몇 가지 소감을 여러분과 나누고 싶습니다 . 먼저 말씀드리고 싶은 것은, 어려운 여건 속에서도 저희는 약속한 바를 충실히 이행하며 견실한 한 해를…
- B7 성과: 조직성과: 수익성 관점에서 볼 때, 뷰티 및 웰빙 부문의 기본 영업이익은 2025년에 25억 달러에 달할 것으로 예상되며, 기본 영업이익률은 전년 대비 20bp 하락한 19.2%를 기록할 것으로 전망됩니다 .
- B7 성과: 운영효율: 생산성 향상 프로그램을 지속적으로 추진하여 비용 절감을 도모하고 간접비를 50bp(베이시스 포인트) 절감했으며, 이 프로그램은 예정보다 훨씬 앞서 진행되고 있습니다 .
- 수치 주장: 또한, 브라질이나 미국의 재택 간호 사업 등에서 성과 격차가 드러난 분야에서 과감한 조치를 취했으며, 2026년에는 이러한 분야에서 상당한 개선이 기대됩니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Q4_and_full-year_2025_results_webcast_and_Q&A_Unilever__G86AGZQwVVo.md`

**382. [Q4 and full-year 2025 results webcast and Q&A audio described | Unilever](https://www.youtube.com/watch?v=m7GUG2IHJZY)** — Unilever · 수요기업·기타 · NL · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 제목 슬라이드가 나타납니다. 2025년 연간 실적이라고 적혀 있습니다. 그 아래에는 페르난도 페르난데스와 슈리나스펙의 이름, 그리고 2026년 2월 12일이라는 날짜가 적혀 있습니다. 파란색 그라데이션 배경 왼쪽에는 유니레버의 U자 로고가 크게 자리하고 있습니다. 면책 조항이 나타납니다. 성명서 전문 링크는 이 영상 설명란에서 확인하실 수 있습니다. 페르난도 페르난데스 최고경영자가 짙은 파란…
- B7 성과: 조직성과: 작년 하반기 라틴 아메리카의 매출 성장률은 약 0%를 기록했는데, 멕시코와 브라질의 거시 경제 상황이 여전히 어려운 가운데, 4분기에 식품 부문의 호조에 힘입어 성장세로 돌아선 것을 기쁘게 생각합니다.
- B7 성과: 운영효율: 지난 2년간 자본 지출은 실제로 약 3% 수준이었으며, 말씀하신 대로 2026년까지는 생산성 향상 또는 비용 절감에 약 55~60%를 투자할 계획입니다.
- 수치 주장: 이는 경쟁력 있는 실적 개선으로 거래량이 증가하여 USG가 3.5% 증가 하고 OOM이 60bp 상승했다는 것을 의미합니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Q4_and_full-year_2025_results_webcast_and_Q&A_audio_describe__m7GUG2IHJZY.md`

**383. [Fernando and Warren Ackerman discuss Foods-McCormick combination | Unilever](https://www.youtube.com/watch?v=NEQBDe8wSjk)** — Unilever · 수요기업·기타 · NL · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요 여러분. 저는 워렌 애커먼입니다. 바클레이즈의 EU 필수 소비재 부문 책임자입니다. 오늘 페르난도 씨와 함께하게 되어 기쁩니다. 어, 페르난도, 우리가 마지막으로 만난 게 벌써 1년쯤 된 것 같아 . 변동성과 지정학적 요인 때문에 시간이 마치 영원처럼 느껴집니다. 음, 어젯밤 휴전은 분명 환영받을 만한 일일 겁니다. 여러분도 마찬가지로 바쁘셨을 겁니다. 매그넘 리뉴얼 작업 완료와 …
- B7 성과: 조직성과: 아시다시피, 매출 성장 측면에서는 저희 회사가 상위 3분의 1 또는 상위 25%에 속하지만, 기업 가치 측면에서는 하위 25%에 속합니다.
- B3 전략적 대응: 매년 시장 규모 성장률이 높아지는 추세이기 때문에, MCC 회사 경영진이 내려야 할 가장 중요한 결정은 높은 시장 규모 성장률에 대한 노출도를 높이는 것입니다 .
- 수치 주장: 당사의 판매량 증가율은 2.5%로 시장 평균을 상회했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Fernando_and_Warren_Ackerman_discuss_Foods-McCormick_combina__NEQBDe8wSjk.md`

**384. [Unilever Foods to combine with McCormick | Webcast & Q&A](https://www.youtube.com/watch?v=MokfRDL0kqA)** — Unilever · 수요기업·기타 · NL · 2026-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 여러분. 좋은 아침입니다. 오늘 함께해 주셔서 감사합니다. 저는 페르난도이고, 시니 님의 통화에 참여합니다 . 오늘은 유니레버가 전략을 가속화하고 포트폴리오를 더욱 정교하게 다듬어 나가는 과정에서 중요한 이정표를 세우는 날입니다. 우리는 검증된 업계 선도적 성장 프로필을 바탕으로 고성장 분야에 집중하는 순수 HPC 기업으로 거듭나고 있습니다 . 동시에, 우리는 맥코믹과 강력한 전…
- B7 성과: 조직성과: 맥코믹은 사업의 성장 전망, 수익성, 현금 창출 능력 등 여러 요소를 고려할 때, 이미 확고한 자금 조달을 확보했으며, 매출 시너지와 비용 시너지를 창출하기 위한 명확한 계획을 가지고 있기 때문에 2~3년 내에 부채비율을 3% 수준으로 낮출 수 있을 것이라는 확신이 충분히 있습니다 .
- B7 성과: 운영효율: 오늘날 일부 소규모 유통업체는 실제로 통합 포트폴리오를 취급하고 있으며, 규모의 경제 덕분에 적절한 투자 수익률(ROI)을 얻을 수 있습니다.
- 수치 주장: 첫째, 우리는 매우 매력적인 분야에서 선도적인 입지를 확보하고 , 미국과 인도와 같이 빠르게 성장하는 지역에 대한 투자를 강화하며, 프리미엄 및 디지털 채널에 대한 참여를 확대하는 390억 유로 규모의 HPC 전문 기업을 구축하고 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Foods_to_combine_with_McCormick_Webcast_&_Q&A__MokfRDL0kqA.md`

**385. [Unilever | Q1 2026 Trading Statement | Results | Webcast & Q&A](https://www.youtube.com/watch?v=IlduIhb63aU)** — Unilever · 수요기업·기타 · NL · 2026-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B1 기술 활용, B6 장벽, B8 부정 성과
- 개요: 안녕하세요. 유니레버의 2026년 1분기 실적 발표에 함께해 주셔서 감사합니다. 오늘 이 자리에는 저희 최고재무책임자(CFO)인 슈리니 파텍 씨가 함께하고 있습니다 . 잠시 후 슈리니가 해당 분기의 세부 사항을 설명해 드릴 것입니다. 또한 최근 식품 사업 부문과 관련하여 발표된 내용에 대해 간략히 말씀드리고, 이번 조치가 식품 사업 부문, 유니레버, 그리고 궁극적으로 주주들에게 상당한 가치를…
- B7 성과: 조직성과: 그리고 저는 이것이 분말 형 제품 시장에서 가격 경쟁력을 회복하는 것과 동시에 액체형 제품 시장 개발을 가속화하는 것, 특히 연간 매출 2억 유로 이상을 기록하고 41개국에 진출해 있는 원더워시(Wonder Wash)를 중심으로 한 전략의 조합이라고 생각합니다.
- B7 성과: 운영효율: 수익성 개선은 판매량 증가, 제품 구성 개선, 지속적인 비용 절감, 그리고 예정보다 빠르게 진행되어 1분기 말 까지 이미 7억 5천만 유로의 성과를 달성한 생산성 향상 프로그램의 효과에 힘입은 것입니다.
- 수치 주장: 당사는 이번 분기에 2.9% 의 높은 판매량 증가에 힘입어 3.8%의 매출 성장률을 달성했습니다 .
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Unilever_Q1_2026_Trading_Statement_Results_Webcast_&_Q&A__IlduIhb63aU.md`

**386. [Barclays Consumer Health Conference 2026](https://www.youtube.com/watch?v=oOyDsMsCmqI)** — Unilever · 수요기업·기타 · NL · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 음, 우리가 제시간에 온 것 같네요. 자, 이것으로 마지막 시간입니다. 음, 의자에 놓인 선물 꾸러미에 대해 모두에게 다시 한번 알려드리는 게 좋겠어요 . 집에 갈 때 그것들을 잊지 마세요 . 그러니 모두를 위한 충분한 선택지가 있습니다. 이번 세션은 온라인으로 진행되는 편안한 분위기의 대담입니다. 그러니, 바라건대 우리에게는 그 기술이 있을 겁니다. 네, 유니버 웰니스(Univer Well…
- B2 파괴: 경쟁구도: 소비자가 매장 통로를 걸어가면서 3분 정도 시간을 내어 그 룬스(Grunes)에 대해 알아보고, 우리가 어떤 가치를 제공하는지 이해하게 만드는 능력은, 경쟁사들이 매장 내에서 최적화하려고 노력하는 진열대 앞부분보다 훨씬 더 가치가 있으며, 엄청난 경쟁 우위를 창출합니다.
- B4 가치네트워크·생태계: 이 센터를 통해 데이터 및 분석 역량을 강화하고, 성과 마케팅, 고객 접근성, 소매 채널, 공급망, 조달, 그리고 글로벌 시장 진출에 있어 큰 발전을 이룰 수 있을 것입니다.
- 수치 주장: 물론 식단과 운동이 전반적인 건강 과 수명에 가장 중요한 요소이긴 하지만, 밀레니얼 세대의 46%가 장수를 위해 비타민과 보충제를 섭취하고 있다고 답했고, 전체 세대의 35%가 건강한 수명을 추구하며 이를 위해 보충제를 활용하고 있다고 합니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Unilever/Barclays_Consumer_Health_Conference_2026__oOyDsMsCmqI.md`

**387. [Deutsche Bank Global Consumer Conference 2026](https://www.youtube.com/watch?v=p0zFRz7jrQU)** — Unilever · 수요기업·기타 · NL · 2026-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B1 기술 활용, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 여러분. 다음 세션으로 넘어가겠습니다. 다음 순서로 유니레버 CEO 페르난도 페르난데스와 유니레버 CFO 스리니바스를 소개해 드리게 되어 매우 기쁩니다 . 페르난도와 스리니바스에게 넘기겠습니다. 감사합니다. 고마워요, 아담. 정말 감사합니다. 초대해 주셔서 감사합니다. 도이치뱅크 컨퍼런스에 참석하게 되어 정말 기쁩니다. 아시다시피 , 유니레버는 지난 몇 년 동안 많은 변화를 겪었…
- B3 전략적 대응: 지난 3~4년 동안 이사회 구성원 10명 중 8명이 새로 선임되었고 , 최고 경영진 11명 중 9명이 교체되었는데, 여기에는 저를 포함한 스리니바스도 포함됩니다.
- B2 파괴: 경쟁구도: 대규모 투자를 통해 자체 향료 연구소를 설립한 결과, 저희 향료의 65%가 향의 질이 획기적으로 향상되었으며, 현재 65% 이상의 향료가 경쟁사 대비 우수한 결과를 보여주고 있습니다.
- 수치 주장: 아시다시피 , 우리는 80억 달러 규모의 아이스크림 사업과 같은 중요한 사업을 분리하면서 동시에 매출과 마진 확대를 가속화할 수 있음을 입증했습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Unilever/Deutsche_Bank_Global_Consumer_Conference_2026__p0zFRz7jrQU.md`

**388. [Unilever | Q2 & H1 2026 | Results | Webcast & Q&A](https://www.youtube.com/watch?v=b_Db2XHcw18)** — Unilever · 수요기업·기타 · NL · 2026-07 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: Good morning and thank you for joining us for Unilver second quarter and half year results. In a moment, Shini will take you through the detail of the results. But first, let me highlight the key elements of our performa…
- B7 성과: 조직성과: We see that as a significant competitive advantage and give us a lot of confidence to really deliver the numbers that we have given in the upgraded guidance.
- B5 리더십·CDO/CAIO: Whether you see it from a deodorant's point of view or when you see skin cleansing, that's also reflected in our gaining back leadership in the US and deodorants and skin cleansing.
- 수치 주장: On a 2-year basis, volume growth averaged 2.7% in the first half, providing further evidence that the improvement we are seeing is becoming more consistent and sustainable.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 검색·RAG · 칩·하드웨어
- 원문: `transcripts/channels/Unilever/Unilever_Q2_&_H1_2026_Results_Webcast_&_Q&A__b_Db2XHcw18.md`

---

## Upstage


**389. [KLUE Seminar](https://www.youtube.com/watch?v=3SUBLhZtJGk)** — Upstage · 파운데이션 모델 · KR · 2021-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B6 장벽 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B5 구조 변화
- 개요: 으 문의 간 이는 다시 제가 이 첫 스타트를 끊었는데 저는 이 끌로 될지 마다 클리어 라는 프로젝트가 어떤 프로젝트 였는지 간략하게 먼저 설레게 해 드리고 벤치마크 은은한 멋이 그래도 무엇인가 이런 이야기로 종들이 있고 그리고 나서 전체적으로 저희가 벤치 만 그 외에 데이터를 제작하는 데 실질적으로 어떤 방식으로 제작을 해 왔다 이런 이야기를 드리려고 합니다 그래서 조금 길다면 길고 짧다면 …
- B8 부정 성과: 보안·프라이버시: 으 문의 간 이는 다시 제가 이 첫 스타트를 끊었는데 저는 이 끌로 될지 마다 클리어 라는 프로젝트가 어떤 프로젝트 였는지 간략하게 먼저 설레게 해 드리고 벤치마크 은은한 멋이 그래도 무엇인가 이런 이야기로 종들이 있고 그리고 나서 전체적으로 저희가 벤치 만 그 외에 데이터를 제작하는 데 실질적으로 어떤 방식으로 제작을 해 왔다 이런 이야기를 드리려고 합니다 그래서 조금 길다면 길고 짧다면 짧은 시간동안 여제의 경험과 노하우를 전할 지도록 노력을 할 꺼구요 플레…
- B1 디지털·AI 기술의 활용: 으 문의 간 이는 다시 제가 이 첫 스타트를 끊었는데 저는 이 끌로 될지 마다 클리어 라는 프로젝트가 어떤 프로젝트 였는지 간략하게 먼저 설레게 해 드리고 벤치마크 은은한 멋이 그래도 무엇인가 이런 이야기로 종들이 있고 그리고 나서 전체적으로 저희가 벤치 만 그 외에 데이터를 제작하는 데 실질적으로 어떤 방식으로 제작을 해 왔다 이런 이야기를 드리려고 합니다 그래서 조금 길다면 길고 짧다면 짧은 시간동안 여제의 경험과 노하우를 전할 지도록 노력을 할 꺼구요 플레…
- 수치 주장: 으 문의 간 이는 다시 제가 이 첫 스타트를 끊었는데 저는 이 끌로 될지 마다 클리어 라는 프로젝트가 어떤 프로젝트 였는지 간략하게 먼저 설레게 해 드리고 벤치마크 은은한 멋이 그래도 무엇인가 이런 이야기로 종들이 있고 그리고 나서 전체적으로 저희가 벤치 만 그 외에 데이터를 제작하는 데 실질적으로 어떤 방식으로 제작을 해 왔다 이런 이야기를 드리려고 합니다 그래서 조금 길다면 길고 짧다면 짧은 시간동안 여제의 경험과 노하우를 전할 지도록 노력을 할 꺼구요 플레…
- 교량: Avenue 2 윤리·거버넌스 · 기술: 파인튜닝·학습
- 원문: `transcripts/channels/Upstage/KLUE_Seminar__3SUBLhZtJGk.md`

**390. [Why Domain-Specific AI Wins in Underwriting: Amwins x Upstage Fireside Chat](https://www.youtube.com/watch?v=997liHBHqW0)** — Upstage · 파운데이션 모델 · KR · 2025-12 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: Hi, I'm Galina Fendikvich. I lead us go to market for upstage AI. With me today, I have Steven Beichchum from Amwin's group benefits. Steven, thank you for joining us. &gt;&gt; Thank you. &gt;&gt; So, tell me, what criti…
- B4 가치네트워크·생태계: you know, don't don't try to swallow the whale, but you know, you you you you you win at the small scale that gets you permission to move up the value chain and and tackle the next problem and tackle the next problem, you know.
- B1 디지털·AI 기술의 활용: What I tell my team and what I tell my business partners is when you're dealing with your traditional LLM solution, you're you're a very small tail trying to wag a very large dog, right?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Upstage/Why_Domain-Specific_AI_Wins_in_Underwriting_Amwins_x_Upstage__997liHBHqW0.md`

---

## Volvo Cars


**391. [Core Computing](https://www.youtube.com/watch?v=8WyV487QG9Q)** — Volvo Cars · 물리 AI·자율주행 · SE · 2021-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 헨릭, 감사합니다. 자동차 산업은 다른 산업 분야에서는 찾아볼 수 없는 속도와 규모로 주요한 기술적 변화들이 교차하며 재정의되고 있습니다. 자동차의 디지털화와 커넥티드 서비스, 그리고 전 동화 등 여러 분야에서 동시에 변화가 일어나고 있습니다. 자율주행, 전 동화, 커넥티비티 분야의 변화에는 공통적인 핵심 요소가 있는데, 바로 소프트웨어입니다. 소프트웨어는 용량, 복잡성, 그리고 가…
- B1 디지털·AI 기술의 활용: 사내 소프트웨어 개발은 ​​자동차뿐만 아니라 클라우드, 온라인 비즈니스, 지원 시스템 등 모든 시스템으로 확장되고 있으며, 이러한 모든 영역은 지속적으로 성장하고 있습니다.
- B5 조직구조 변화: 고객에게 제공하고자 하는 세 심하게 설계된 볼보 경험을 구현할 수 있는 '바퀴 위의 컴퓨터'를 만들고 있으며, 차량 곳곳에 흩어져 있는 수백 개의 ECU에 의존하는 대신 중앙 집중식 컴퓨팅 시스템인 코어 시스템으로 전환하고 있습니다.
- 수치 주장: 고객에게 제공하고자 하는 세 심하게 설계된 볼보 경험을 구현할 수 있는 '바퀴 위의 컴퓨터'를 만들고 있으며, 차량 곳곳에 흩어져 있는 수백 개의 ECU에 의존하는 대신 중앙 집중식 컴퓨팅 시스템인 코어 시스템으로 전환하고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Volvo_Cars/Core_Computing__8WyV487QG9Q.md`

---

## Waymo


**392. [Self-Driven Women: Opportunities and challenges for women working in the mobility industry](https://www.youtube.com/watch?v=-x1c0URjbOE)** — Waymo · 물리 AI·자율주행 · US · 2020-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, 먼저 웨이모의 모든 팀, 특히 웨이모 드라이버 와 우리 사업을 만들어가는 여성분들을 대표하여 오늘 저희의 첫 번째 여성 자율 운전 행사에 함께해 주셔서 진심으로 감사드립니다. 시작하기 전에 몇 가지 안내 사항을 드리겠습니다. 채팅 탭을 통해 의견과 생각을 공유해 주시고, 질문 탭을 통해 질문을 제출해 주세요. 이미 많은 질문을 받았으며, 가능한 한 많은 질문에 답…
- B5 리더십·CDO/CAIO: 웨이모에서 일하는 동안, 제가 기술 업계에 몸담았던 시기 중 가장 인종차별적인 시기를 겪게 되었는데, CEO부터 리더십 팀, 그리고 많은 직원들이 이 시대를 진정으로 받아들이고 대화에 참여하며 관용 과 이해, 공감을 배우는 여정에 함께해 준 회사에 있다는 것이 정말 큰 행운이라고 생각합니다.
- B5 직무·역량 변화: 이 프레임워크는 " 회사 내 고성장 분야 5곳을 파악하고, 그중 50곳을 여성으로 채용하겠다", " 다양성과 포용성을 가져오는 데 대한 보상 시스템을 구축하겠다"와 같은 질문을 던집니다.
- 수치 주장: 2019년에는 최고운영책임자(COO)로 임명되어 현재까지 대외 협력 기능을 이끌고 있으며, 운영, 사업 전략, 사업 개발 등을 총괄하고 있습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Waymo/Self-Driven_Women_Opportunities_and_challenges_for_women_wor__-x1c0URjbOE.md`

**393. [#FTLive: Waymo CEO John Krafcik Keynote Interview](https://www.youtube.com/watch?v=TPve7x0GOT8)** — Waymo · 물리 AI·자율주행 · US · 2021-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B1 기술 활용, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 샌프란시스코에서 인사드립니다. 안녕하세요, 저는 파이낸셜 타임스의 패트릭 맥기입니다. 이번 인터뷰에 대해 매우 기대하고 있습니다. 존 크라프칙과 30분간 인터뷰할 시간이 있습니다. 그는 카리스마 넘치고, 에너지가 넘치며, 2009년부터 시작된 구글 자율주행 프로젝트로 알려졌던 웨이모의 CEO입니다. 웨이모는 자율주행/무인/ 자율주행 로보택시 서비스 분야에서 선두주자라고 할 수 있습니다 . 그…
- B2 파괴: 경쟁구도: 제 생각에 완전 자율 주행 기술 개발이 인류가 시도해 온 가장 어려운 일 중 하나라면 , 두 번째로 어려운 일은 이 분야의 경쟁자들이 어디에 있고 그들의 실제 역량이 어느 정도인지 파악하는 것일 겁니다 .
- B7 성과: 조직성과: 그러니까, 향후 10년 동안 수익성이 달성될 가능성이 전혀 없는 건가요?
- 수치 주장: 웨이모는 2009년 말 이나 2010년 초에 첫 자율주행차를 개발했고, 2012년에는 구글 직원들, 즉 자율주행 프로젝트와는 전혀 관련이 없는 사람들이 자사 차량으로 출퇴근할 수 있도록 하는 시범 프로젝트를 진행했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/channels/Waymo/#FTLive_Waymo_CEO_John_Krafcik_Keynote_Interview__TPve7x0GOT8.md`

**394. [Self-Driven Women: Engineering the future of autonomy](https://www.youtube.com/watch?v=cvqGkq2SGWQ)** — Waymo · 물리 AI·자율주행 · US · 2021-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [음악] 안녕하세요, 저희 자율 주행 여성 행사에 오신 여러분을 환영합니다. 저는 앨리슨 택스턴 이고, 웨이모에서 웨이모 플래너 소프트웨어를 개발하는 엔지니어입니다. 웨이모 플래너는 웨이모 드라이버가 A 지점에서 B 지점까지 경로를 계획할 수 있도록 해주는 소프트웨어입니다. 이번 행사는 모빌리티 기술의 최첨단에서 일하는 여성들의 커뮤니티를 육성하기 위한 자율 주행 여성 시리즈의 세 번째 행사…
- B1 디지털·AI 기술의 활용: 따라서 많은 인식 알고리즘과 기술이 공유되며, 두 산업 모두 초기에는 휴리스틱 기반 접근 방식을 많이 사용하다가 최근 몇 년 동안 머신러닝, 특히 딥러닝 기술의 발전과 함께 점점 더 많이 활용하고 있습니다.
- B2 파괴: 데이터 가용성: 앞서 말씀드린 것처럼, 자동차가 더 조심스럽게 운전하도록 유도하는 기술을 개발하여 롱테일 데이터를 수집하고, 전용 도구를 사용하여 데이터를 더 효과적으로 분석하고 머신러닝 알고리즘을 적용할 수 있습니다.
- 수치 주장: 예를 들어, 제가 입사 후 처음으로 참여한 프로젝트는 2015년 텍사스 오스틴에서 웨이모 드라이버를 출시하는 것이었습니다.
- 교량: Avenue 1 동적역량 · 기술: 칩·하드웨어
- 원문: `transcripts/channels/Waymo/Self-Driven_Women_Engineering_the_future_of_autonomy__cvqGkq2SGWQ.md`

---

## Weaviate


**395. [Instructor with Jason Liu - Weaviate Podcast #88!](https://www.youtube.com/watch?v=higlHgYDc5E)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-02 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited to welcome Jason Lou about three months ago Jason presented pantic is all you need at the AI engineer conference in San F…
- B1 디지털·AI 기술의 활용: create that all the attributes autocomplete or whether or not you try to access a incorrect attribute or have a typo that's all cleaned up for you um I think for the most part I've been challenging a lot of folks to think about what an instructor like pattern …
- B4 디지털 채널: create that all the attributes autocomplete or whether or not you try to access a incorrect attribute or have a typo that's all cleaned up for you um I think for the most part I've been challenging a lot of folks to think about what an instructor like pattern …
- 수치 주장: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited to welcome Jason Lou about three months ago Jason presented pantic is all you need at the AI engineer conference in San Francisco it was such like a novel but al…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Weaviate/Instructor_with_Jason_Liu_-_Weaviate_Podcast_#88!__higlHgYDc5E.md`

**396. [Zain and JP chat about: Vector embedding models for AI](https://www.youtube.com/watch?v=lpdN3aw-yTg)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-04 · en · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: hello and welcome everybody my name is JP I've got Zen here with me and in this podcast we haven't got a name on you think for the show but um Zen and I had a chat I think a few days ago about embeddings and embedding mo…
- B1 디지털·AI 기술의 활용: hello and welcome everybody my name is JP I've got Zen here with me and in this podcast we haven't got a name on you think for the show but um Zen and I had a chat I think a few days ago about embeddings and embedding models in particular and I thought it was …
- B4 민첩성·양손잡이: hello and welcome everybody my name is JP I've got Zen here with me and in this podcast we haven't got a name on you think for the show but um Zen and I had a chat I think a few days ago about embeddings and embedding models in particular and I thought it was …
- 수치 주장: hello and welcome everybody my name is JP I've got Zen here with me and in this podcast we haven't got a name on you think for the show but um Zen and I had a chat I think a few days ago about embeddings and embedding models in particular and I thought it was …
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 추론 최적화
- 원문: `transcripts/channels/Weaviate/Zain_and_JP_chat_about_Vector_embedding_models_for_AI__lpdN3aw-yTg.md`

**397. [DSPy End-to-End: Meetup in San Francisco](https://www.youtube.com/watch?v=Y81DoFmt-2U)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, 오늘 와주셔서 정말 감사합니다. 모두 함께하게 되어 정말 기쁩니다. 저는 Edge의 공동 창립자 Is Era입니다. Edge AI와 함께 이 커뮤니티에서 이 프레임워크에 대해 이야기하게 되어 매우 기쁩니다. 시작하기 전에 이 분야와 저희 회사, 그리고 저희의 접근 방식에 대해 간략하게 설명드리겠습니다. 저는 Edge의 공동 창립자이고, Transformer 논문의…
- B1 디지털·AI 기술의 활용: Rag와 Chain of Thought를 적용하는 DSP 코드 세 줄과 그 위에 최적화 도구를 실행하는 한두 줄을 추가하면 추가적인 작업 없이도 130억 개의 매개변수를 가진 L Lama chat 모드가 양자화된 형태 로 GPT 3.5를 능가하는 것을 볼 수 있습니다.
- B8 부정 성과: 보안·프라이버시: 검색 결과를 살펴보면, 폴 그레이엄의 에세이, 특히 그의 순자산과 관련된 내용을 전혀 고려하지 않았기 때문에 LLM에 완전히 관련 없는 맥락이 입력되어 오류가 발생하고 잘못된 응답을 생성하는 것을 알 수 있습니다.
- 수치 주장: 저희 에코시스템 파트너들은 지난 1년 동안 많은 대형 모델 개발사 및 엔터프라이즈 AI 파트너와 협력해 왔으며, 오늘부터 더 많은 파트너와 협력하여 이 프레임워크의 도입을 가속화할 수 있기를 기대합니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 추론 최적화
- 원문: `transcripts/channels/Weaviate/DSPy_End-to-End_Meetup_in_San_Francisco__Y81DoFmt-2U.md`

**398. [Guest Lecture: Vector Quantization Techniques with Etienne | Brown University CSCI](https://www.youtube.com/watch?v=0diVrgyQwXA)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-05 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 요즘 U 회사는 어느 정도 규모인가요? AI 분야, 특히 벡터 임베딩 관련 분야는 정말 흥미진진한 시기를 맞고 있습니다. 저희 회사도 마찬가지고요. 잠시 후 슬라이드에서 보여드리겠지만, 모두가 상용화 단계로 넘어가는 시점이라 매우 흥미로운 시기입니다. 이는 완전히 새로운 도전 과제를 안겨주기도 하지만, 동시에 새로운 기회도 창출합니다. 정말 기대 되는 시기죠. 좋습니다. 네, 그럼 이 강좌에…
- B8 부정 성과: 보안·프라이버시: 하지만 단순히 개념을 증명하기 위해서라면 괜찮았지만, 10만 개의 데이터만으로 무차별 대입을 하면 이미 시간이 오래 걸렸고, 아마도 더 효율적인 언어로 여러 번 다시 만드는 게 나았을 시점을 이미 지나쳤을 겁니다.
- B1 디지털·AI 기술의 활용: 예를 들어, 강의 후에는 두 명의 학생 발표자가 발표할 예정인데, 하나는 머신러닝을 사용하여 정렬 속도를 높이는 것이고, 다른 하나는 딥러닝을 사용하여 자연어를 SQL로 번역하는 것입니다.
- 수치 주장: 예를 들어, 처음 10만 개의 상위 벡터 임베딩에 양자화 기법을 적용했는데, 나중에 90만 개의 벡터를 추가로 가져오면 분포가 완전히 달라질 수 있습니다.
- 교량: — · 기술: 검색·RAG · 추론 최적화
- 원문: `transcripts/channels/Weaviate/Guest_Lecture_Vector_Quantization_Techniques_with_Etienne_Br__0diVrgyQwXA.md`

**399. [The Future of Search with Nils Reimers and Erika Cardenas - Weaviate Podcast #97!](https://www.youtube.com/watch?v=DFqd34ikTH0)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: 안녕하세요 여러분, 위바 팟캐스트의 또 다른 에피소드를 시청해 주셔서 정말 감사합니다! 이번 에피소드는 AI 기반 검색 분야의 최근 발전과 COOH, Compass, 임베딩 랭커, 그리고 Command R, Command R Plus 시리즈 등 놀라운 기술 발전을 자세히 살펴보는 매우 흥미로운 시간입니다. 먼저 COOH의 발전을 진심으로 축하드립니다. 이 분야의 모든 발전을 지켜보는 것은 정…
- B1 디지털·AI 기술의 활용: 좀 까다로운 질문인 건 알지만, 스타트업 프로그램과 기술 파트너, 그리고 클라우드 하이퍼스케일러 같은 것들을 어떻게 평가하고, 다른 회사의 기술을 어떻게 시장 지도에 어떻게 배치하는지 어떻게 생각하는지 궁금합니다.
- B7 성과: 조직성과: 예를 들어 연례 보고서를 LM(로지스틱 회귀 분석) 시스템에 입력하면 LM이 보고서 에 오류를 삽입해서 " 마이크로소프트가 매출을 20% 증가시켰다"라고 표시하고, 이 오류를 기록 시스템에 입력하면 기록 시스템에서 " 마이크로소프트가 매출을 20% 증가시켰다는 출처가 있는데 원문에는 없습니다"라고 말합니다.
- 수치 주장: 예를 들어 토큰 청크가 500개라고 가정하면 500개씩 늘어나고, 검색량은 30배, 컴퓨팅 지연 시간은 10,000배 정도 증가합니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 추론 최적화 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Weaviate/The_Future_of_Search_with_Nils_Reimers_and_Erika_Cardenas_-___DFqd34ikTH0.md`

**400. [AI-Native Development with Guy Podjarny and Bob van Luijt - Weaviate Podcast #102!](https://www.youtube.com/watch?v=k6ZxYl2iI3k)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 위바 팟캐스트를 또 시청해주셔서 정말 감사합니다! 이번에도 위바 공동 창립자 밥 반엘 님을 모시게 되어 매우 기쁩니다. 밥, 팟캐스트에 다시 한번 참여해주셔서 정말 감사합니다. 코너, 위바 팟캐스트에 초대해주셔서 감사합니다. 그리고 가이 파자르 님을 위바 팟캐스트에 모시게 되어 정말 기쁩니다. 가이 님은 엄청난 성공을 거둔 사이버 보안 회사 스닉(Snick)을 공동 창립했…
- B1 디지털·AI 기술의 활용: 음, 제가 애플리케이션 배포 방식이나 클라우드 구축 방식을 다시 생각해 본다면, 갑자기 마이크로서비스, 불변 인프라, 그리고 그 이전에도 존재했던 탄력적 컴퓨팅과 같은 개념들을 접하게 될 거라는 걸 이해하려고 노력했어요.
- B2 파괴: 소비자 행동·기대: 이는 사양을 생성하는 사용자 경험(UX)일 수 있지만, 결국 시스템을 나타내는 사양이 만들어집니다.
- 교량: Avenue 1 동적역량 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Weaviate/AI-Native_Development_with_Guy_Podjarny_and_Bob_van_Luijt_-___k6ZxYl2iI3k.md`

**401. [SWE-bench with John Yang and Carlos E. Jimenez - Weaviate Podcast #107!](https://www.youtube.com/watch?v=8rwHAR4fsFg)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-10 · en · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited for this one diving into swe bench and all these amazing works that have come around it swe agent and the latest paper sw…
- B1 디지털·AI 기술의 활용: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited for this one diving into swe bench and all these amazing works that have come around it swe agent and the latest paper swe bench multimodal this is such an amazi…
- B7 성과: 조직성과: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited for this one diving into swe bench and all these amazing works that have come around it swe agent and the latest paper swe bench multimodal this is such an amazi…
- 수치 주장: hey everyone thank you so much for watching another episode of the weeva podcast I'm super excited for this one diving into swe bench and all these amazing works that have come around it swe agent and the latest paper swe bench multimodal this is such an amazi…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weaviate/SWE-bench_with_John_Yang_and_Carlos_E._Jimenez_-_Weaviate_Po__8rwHAR4fsFg.md`

**402. [Arctic Embed with Luke Merrick, Puxuan Yu, and Charles Pierse - Weaviate Podcast #110!](https://www.youtube.com/watch?v=Kjqv4uk3RCs)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2024-12 · ko · 5/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B8 부정 성과
- 개요: 안녕하세요 여러분, we8 팟캐스트를 시청해주셔서 정말 감사합니다. 오늘은 Snowflake의 Arctic Embed Tex 임베딩 모델 시리즈, 특히 최근 출시된 Arctic Embed 2.0 다국어 텍스트 임베딩 모델에 대해 자세히 살펴보겠습니다. 또한 이러한 모델에 접근하고 we8과 쉽게 통합할 수 있는 방법 중 하나인 최근 출시된 wva 임베딩 서비스에 대해서도 이야기해 보겠습니다. …
- B1 디지털·AI 기술의 활용: 딥러닝에서 이런 현상을 자주 보는데, 여러 기능이나 트릭을 사용할 때 마치 의식처럼 정해진 절차를 거치지만, 알고 보면 그게 어떤 이상한 아키텍처 선택이나 5년 전에 유행이 지난 방식 때문에 필요했던 거라는 걸 알게 돼요.
- B6 장벽: 관성·저항: 제 생각에는 특정 쿼리에 대한 좋은 네거티브 데이터가 없는 경우가 있는데, 정말 흥미로운 질문이 있고 그에 대한 답이 있는데, 제 코퍼스에 비슷한 게 없어서 모델을 학습시킬 수 없는 경우가 있어요.
- 수치 주장: 약 1년 반 전에 이러한 인수의 일환으로, 또는 그 무렵에, 현재 Cortex Search라고 불리는 새로운 제품이 Snowflake를 위해 개발되었습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 추론 최적화 · 칩·하드웨어
- 원문: `transcripts/channels/Weaviate/Arctic_Embed_with_Luke_Merrick,_Puxuan_Yu,_and_Charles_Piers__Kjqv4uk3RCs.md`

**403. [Agent Experience with Matt Biilmann, Sebastian Witalec, and Charles Pierse - Weaviate Podcast #116!](https://www.youtube.com/watch?v=MAE3I8O_w84)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2025-02 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, 위바 팟캐스트를 시청해주셔서 정말 감사합니다! 이번에도 에이전트 경험에 대해 심도 있게 다뤄볼 멋진 에피소드를 준비했습니다. 먼저, 위바 팀의 두 멤버를 모시게 되어 매우 기쁩니다. 위바 팟캐스트에 처음으로 출연하시는 분이 있는데요, 바로 위바의 교육 및 개발자 경험 담당 이사인 세바스찬입니다. 세바스찬은 위8 의 초기 단계부터 핵심 리더로서 위8 개발에 다양한 역할을 담…
- B1 디지털·AI 기술의 활용: 여기에는 WEA API가 포함되어 있고, 지금 거래 데이터 세트에 대해 이야기하고 있는 김에, API를 변경하면 기존 지식이 어떻게 될지 생각해 봤는데, 엔지니어들에게 계속 API를 변경해 달라고 요청했고, 실제로 변경하고 개선해 왔기 때문에 API 변경은 꼭 할 거라고 약속했습니다.
- B4 가치네트워크·생태계: 지금처럼 LMS와 상담원들이 다른 도구들보다 이러한 도구들을 사용하는 것이 실제로 더 효율적이라면, 상담원 생태계가 크게 활성화되어 사용자들이 효과를 본 방식을 자연스럽게 받아들이고, '이 방법이 효과적이다.
- 수치 주장: 저희는 거의 10년 전인 2015년 3월에 출시되었는데, 당시에는 프런트엔드 레이어가 마치 하나의 덩어리처럼 되어 있는 모놀리식 애플리케이션 으로 웹 속성을 구축하는 것이 일반적이었습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG
- 원문: `transcripts/channels/Weaviate/Agent_Experience_with_Matt_Biilmann,_Sebastian_Witalec,_and___MAE3I8O_w84.md`

**404. [Optimizing Retrieval Agents with Shirley Wu - Weaviate Podcast #115!](https://www.youtube.com/watch?v=4ZRhSuBHyNo)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2025-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, 위바 팟캐스트를 시청해주셔서 정말 감사합니다! 오늘은 스탠포드 대학교 박사 과정 학생인 셜리 우를 모시게 되어 매우 기쁩니다. 셜리는 인공지능 분야의 최첨단 연구를 진행하고 있으며, 수많은 훌륭한 논문을 발표했고, 현재 스탠포드에서 유르 레코비치, 제임스 주 교수님과 함께 연구하고 있습니다. 이번 팟캐스트에서는 저희 WE8과 저희가 개발 중인 것들에 큰 영향을 미…
- B1 디지털·AI 기술의 활용: 아바타의 핵심 아이디어는 데이터가 세상을 구성하고 있으며, 우리는 이 현실적인 데이터 스키마를 머신러닝 모델이나 AI 에이전트에게 제시하여 그들이 이 데이터 스키마를 탐색하고, 데이터로부터 학습하고, 세상을 탐험하도록 하는 것입니다.
- B8 부정 성과: 보안·프라이버시: 때때로 사람들은 입력과 출력만 보고 입력이 출력에 좋은 결과를 가져오는지 여부만 판단하지만, 요즘에는 훨씬 더 강력한 시스템이 많고, 인지하지 못하는 사이에 오류가 발생할 수 있는 중간 결과들이 많습니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Weaviate/Optimizing_Retrieval_Agents_with_Shirley_Wu_-_Weaviate_Podca__4ZRhSuBHyNo.md`

**405. [Patronus AI with Anand Kannappan - Weaviate Podcast #122!](https://www.youtube.com/watch?v=I2jgU4waKFE)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2025-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과
- 개요: 열.이봐,히트. [음악] 안녕하세요 여러분, WEVA 팟캐스트의 또 다른 에피소드를 시청해 주셔서 정말 감사합니다 . 페트로니스 AI의 공동 창립자인 아난 카노폰을 환영하게 되어 매우 기쁩니다. 페트로니스 AI는 에이전트 및 AI 시스템의 관찰 가능성과 평가 분야에서 가장 혁신적인 기업 중 하나입니다. 그들은 놀라운 플랫폼을 가지고 있습니다. 그들은 링크와 글라이더라는 두 가지 맞춤형 LMS…
- B1 디지털·AI 기술의 활용: 고객 관점에서 볼 때, 더 많은 기업들이 시스템 계층, 예를 들어 래그( Rag) 계층이나 아틀란틱(Atlantic) 계층과 관련된 문제 영역에서 어려움을 겪고 있는 반면, 모델 자체의 특정 계층에서는 어려움을 겪는 경우가 적다고 생각합니다.
- B5 직무·역량 변화: 프롬프트 엔지니어라는 새로운 직무 설명도 나왔는데, 당시에는 프롬프트 엔지니어링이 과학인 동시에 예술이기도 하다고 여겨졌죠.
- 수치 주장: 어, 그래서 저희가 그 기능을 개발했을 때, 많은 기업들이, 그러니까 2024년 당시든 지금이든, RAG 애플리케이션을 개발하고 있다는 사실에 대한 대응으로 개발하게 되었습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weaviate/Patronus_AI_with_Anand_Kannappan_-_Weaviate_Podcast_#122!__I2jgU4waKFE.md`

**406. [RAG Benchmarks with Nandan Thakur - Weaviate Podcast #124!](https://www.youtube.com/watch?v=x9zZ03XtAuY)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2025-06 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: [Music] Hey, [Music] Hey everyone, thank you so much for watching another episode of the WEV8 podcast. I'm super excited to welcome Nandan Thaker. Nandan is a PhD student at the University of Wateroo where he's had an en…
- B1 디지털·AI 기술의 활용: I think maybe like uh precision is sort of like an under reportported metric but I guess you have like it's kind of a part of the NDCG calculation but yeah like that minimum spanning document sounds super and because because I kind of transitioning from there …
- B7 성과: 조직성과: So sentence transformers has embedding models which will be linked to transformers uh which can be also linked to beer because we do evaluation on top of that.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weaviate/RAG_Benchmarks_with_Nandan_Thakur_-_Weaviate_Podcast_#124!__x9zZ03XtAuY.md`

**407. [Saurabh Mishra and Bob van Luijt on Weaviate and SAS - Weaviate Podcast #129!](https://www.youtube.com/watch?v=INKV21AaYjE)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, Wev8 팟캐스트의 또 다른 에피소드를 시청해 주셔서 정말 감사합니다 . 오늘은 Wevate와 SAS의 파트너십에 대해 자세히 알아보겠습니다. SAS는 SAS 검색 에이전트 관리 시스템과 WeVate와의 파트너십을 통해 놀라운 일들을 많이 하고 있습니다 . 이 주제에 대해 더 자세히 이야기 나눌 수 있게 되어 정말 기쁩니다. 먼저 weva 공동 창립자인 밥 밴라우…
- B1 디지털·AI 기술의 활용: 제가 생성형 AI 분야를 주시하고 있었는데, Chad GPD 같은 회사들이 주목받고 클라우드 기술이 수백만 명의 사용자를 확보하고 있다는 이야기가 많이 나왔거든요.
- B4 가치네트워크·생태계: 이는 저희가 대기업을 대상으로 서비스를 제공하고 있으며, 많은 기업들이 이미 XYZ와 파트너십을 맺고 있기 때문에 협력 관계를 유지해야 한다는 관점을 가지고 있기 때문입니다.
- 수치 주장: 하지만 주간 평균 사용자가 7억 명에 달하는 상황에서, 우리 GPT는 어떻게 하면 기업 환경에서 이러한 장점을 활용할 수 있을지 고민하게 만듭니다.
- 교량: — · 기술: 검색·RAG
- 원문: `transcripts/channels/Weaviate/Saurabh_Mishra_and_Bob_van_Luijt_on_Weaviate_and_SAS_-_Weavi__INKV21AaYjE.md`

**408. [Multi-Vector Search with Amélie Chatelain and Antoine Chaffin - Weaviate Podcast #134!](https://www.youtube.com/watch?v=44GC3E-WbHU)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2026-03 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B7 긍정 성과
- 개요: 밀집형 모델과 다중 벡터 모델 간의 협력이 훨씬 더 공정합니다. 그 이유는 당시 우리가 약 2백만 개의 샘플로 학습된 후기 상호작용 모델과 인터넷 전체 데이터로 학습된 밀집 모델을 비교했기 때문입니다. 결국 후기 상호작용 모델이 더 깊은 연결과 더 깊은 유사성 개념을 파악하는 데 더 뛰어나다는 거죠? 왜냐하면, 다시 말하지만, 그 격차가 너무 커서 밀집 벡터와 다중 벡터는 아예 같은 종류의 …
- B1 디지털·AI 기술의 활용: 네, 사용자 입장에서 말씀드리자면, 저는 이 도구 자체의 연구 개발에는 참여하지 않았지만, 클라우드 코드(Cloud Code)를 많이 사용하는 사용자이고, 코드 그렙(Code Grep)의 알파 테스터로 처음부터 참여했습니다 .
- B8 부정 성과: 보안·프라이버시: 그러니까, 이건 벤치 마크 선택에 편향이 있었거나 우리가 악용할 수 있었던 어떤 것에 관한 문제가 아닙니다.
- 수치 주장: 그리고 다른 하나는 현대 조류를 기반으로 한 1억 5천만 개의 매개변수를 가진 모델인데 , 이것 또한 저희가 개발한 모델입니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 추론 최적화 · 코딩 에이전트
- 원문: `transcripts/channels/Weaviate/Multi-Vector_Search_with_Amélie_Chatelain_and_Antoine_Chaffi__44GC3E-WbHU.md`

**409. [Booking.com and Weaviate with Başak Eskili - Weaviate Podcast #138!](https://www.youtube.com/watch?v=O9edM9ZS_FQ)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2026-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: [음악] 바싯, We Rate 팟캐스트에 오신 것을 환영합니다. 참여해주셔서 정말 감사합니다. 초대해 주셔서 정말 감사합니다. 여기 오게 되어 기쁩니다. 엄청난. 네, booking.com의 엔지니어링 기술에 대해 더 자세히 알게 되어서 정말 흥미로웠어요. 멋진 블로그 게시글들도 많았고, 앞으로 더 깊이 파고들어 볼 생각에 너무 기대됩니다. 그리고, ' From Code to Check-in…
- B1 디지털·AI 기술의 활용: 그래서 저희가 구현하고자 했던 것은 GenAI 에이전트를 통해 파트너사들이 사용자 문의에 따라 벡터 데이터베이스에서 관련 응답 템플릿을 제안하거나, 수집된 데이터를 기반으로 맞춤형 답변을 생성하는 방식으로 자동 응답을 지원하는 것입니다 .
- B4 가치네트워크·생태계: 그래서 저희가 구현하고자 했던 것은 GenAI 에이전트를 통해 파트너사들이 사용자 문의에 따라 벡터 데이터베이스에서 관련 응답 템플릿을 제안하거나, 수집된 데이터를 기반으로 맞춤형 답변을 생성하는 방식으로 자동 응답을 지원하는 것입니다 .
- 수치 주장: 그런데 만약 1억 개의 호텔 중에서 마이애미 필터만 적용하면 검색 결과가 1억 개 중에서 1,000개 정도로 줄어들 수 있지 않을까 하는 생각이 들었습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weaviate/Booking.com_and_Weaviate_with_Başak_Eskili_-_Weaviate_Podcas__O9edM9ZS_FQ.md`

**410. [Founding Weaviate with Bob van Luijt and Etienne Dilocker - Weaviate Podcast #140!](https://www.youtube.com/watch?v=pvv-vnT-LfQ)** — Weaviate · 데이터·컨텍스트·거버넌스 · NL · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 그리고 나서 우리는 첫 번째 원형 좌석을 올렸는데, 그것은 하나였습니다. 나는 이 120만 달러를 절대 잊지 않을 거야. 저는 제 평생 은행 계좌에 그렇게 많은 돈이 있는 것을 본 적이 없습니다. [웃음] "맙소사, 진짜로 돈을 주네."라고 생각했어요. 저는 엔지니어링 오크를 변형시킬 거라고는 전혀 예상 못 했어요. 처음부터 새로 만드는 줄 알았거든요. 알고 보니 7년 만에 제가 그 상황을 …
- B1 디지털·AI 기술의 활용: 저는 클라우드 코드 사용자로서 매우 적극적으로 의견을 개진하고 있고, 물론 다른 도구들도 실험해 보고 있지만, 아마도 저를 가장 흥분시키는 것은, 직접 만나서 저와 시간을 보내봐야 알 수 있을 것 같은데, 바로 위모( Whimo)에 앉아보는 것입니다.
- B2 파괴: 데이터 가용성: "이 모든 기업들은 엄청난 양의 비정형 데이터를 가지고 있는데, 우리가 그 모든 데이터를 통합하고 추출해서 그 모든 데이터에서 통찰력을 얻을 수 있는 무언가를 할 수 있다면 멋지지 않을까요?" 그리고 이게 바로 우리가 대화를 시작하게 된 계기입니다.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/channels/Weaviate/Founding_Weaviate_with_Bob_van_Luijt_and_Etienne_Dilocker_-___pvv-vnT-LfQ.md`

---

## Weights & Biases


**411. [Optimizing CI/CD model management and evaluation workflows](https://www.youtube.com/watch?v=Sw4M-b_GQZg)** — Weights & Biases · 에이전트·개발도구 · US · 2024-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 안녕하세요 여러분, 오늘 함께해 주셔서 감사합니다. 저는 Hamah이고, Jorge SVA가 함께하고 있습니다. 저희 둘 다 Wason Bias의 머신러닝 엔지니어입니다. 오늘 Jorge는 Wason Bias가 머신러닝 개발 주기와 관련하여 CICD 파이프라인을 어떻게 향상시킬 수 있는지에 대한 통찰력을 공유할 예정입니다. 채팅창에 질문을 남겨주시면 마지막 Q&amp;A 세션에서 답변해 드리…
- B1 디지털·AI 기술의 활용: 오른쪽에는 Weave라는 새로운 서비스가 있는데, 이는 LLM 사용 및 생성형 AI 작업 또는 개발과 관련된 워크플로에 최적화되어 있습니다.
- B8 부정 성과: 보안·프라이버시: 이 두 서비스는 가중치와 편향 코어라고 부르는 기본 구성 요소 또는 개념 세트를 기반으로 구축되었으며, 오늘 우리는 이러한 구성 요소와 아티팩트, 테이블 및 보고서를 모두 살펴볼 것입니다.
- 수치 주장: 다시 말씀드리지만, 보고서에서 볼 수 있듯이 KS 테스트를 적용하여 5% 미만의 확률로 테스트한 결과 요약이 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Weights_&_Biases/Optimizing_CICD_model_management_and_evaluation_workflows__Sw4M-b_GQZg.md`

**412. [AI’s breakthrough in weather forecasting with Brightband’s Julian Green](https://www.youtube.com/watch?v=xFgaEPMqfi4)** — Weights & Biases · 에이전트·개발도구 · US · 2024-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 여러분은 머신러닝을 현실 세계에 적용하는 방법에 대한 팟캐스트, 그레이디드 디센트를 듣고 계십니다. 저는 진행자 루카스 스팔드이고, 오늘은 세 개 이상의 회사를 창업한 연쇄 창업가 줄리안 그린 씨와 이야기를 나눠보겠습니다. 하우스, 젯팩, 헤드룸을 창업했고, 구글 X에서 AI 문샷 총괄 매니저를 역임한 후 현재 회사인 브라이트밴드를 설립했습니다. 브라이트밴드의 목표는 인류와 지구를 위해 날씨…
- B7 성과: 사회적 편익: 80년대에는 미국에서 4개월마다 10억 달러 규모의 재난이 발생했는데, 지금은 몇 주마다 발생하고 있어요.
- B1 디지털·AI 기술의 활용: 아시다시피, 단순히 수직적으로 통합된 접근 방식 하나만으로는 부족하고, LLM(Limited Leadership Management System)처럼 여러 계층으로 구성된 구조가 더 많아질 거라고 생각합니다.
- 수치 주장: 컴퓨터를 이용한 수치 날씨 예측이 시작된 이후 매 10년마다 정확도가 하루씩 향상되었다고 볼 수 있습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Weights_&_Biases/AI’s_breakthrough_in_weather_forecasting_with_Brightband’s_J__xFgaEPMqfi4.md`

**413. [How GenAI is powering the next generation of Mercari Marketplace | FC Tokyo 2024](https://www.youtube.com/watch?v=tEbLkgDCmzg)** — Weights & Biases · 에이전트·개발도구 · US · 2024-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 얀, 소개 감사합니다. 제 이름은 티오이고, 오늘은 메라리에 대해 이야기하려고 합니다. 메라리에서 AI 기술을 활용하여 고객을 위한 마켓플레이스 경험을 혁신하고, 차세대 고객 경험을 구축하는 방법에 대해 말씀드리겠습니다. 발표는 20분으로 짧을 예정입니다. 모든 내용을 다 말씀드리기는 어렵네요. 저희는 다양한 사업을 진행하고 있으며, 지금 말씀드린 내용은 그중 몇 가지 예시에 불과합니다. 먼…
- B8 부정 성과: 보안·프라이버시: 임베딩이 어떻게 우리 내부 팀의 고객 가치 제공 능력을 즉시 향상시켰는지, 그리고 우리가 의도와 가중치 및 편향을 가지고 개발하고 사용해 온 모든 도구들이 앞으로 모든 프로젝트의 속도를 극대화하고 가속화하는 데 어떻게 도움이 되었는지 아주 쉽게 설명할 수 있습니다.
- B2 파괴: 소비자 행동·기대: 메라리에서 AI 기술을 활용하여 고객을 위한 마켓플레이스 경험을 혁신하고, 차세대 고객 경험을 구축하는 방법에 대해 말씀드리겠습니다.
- 수치 주장: 작년 5월 에 설립되어 10월까지 5개월이라는 짧은 기간 동안 생산성 도구를 개발하는 데 필요한 기술을 습득했습니다.
- 교량: — · 기술: 검색·RAG · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/How_GenAI_is_powering_the_next_generation_of_Mercari_Marketp__tEbLkgDCmzg.md`

**414. [What’s the path to AGI? A conversation with Turing Co-founder and CEO Jonathan Siddharth](https://www.youtube.com/watch?v=DJS7cop0CCw)** — Weights & Biases · 에이전트·개발도구 · US · 2024-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: 여러분은 머신러닝을 실생활에 적용하는 방법에 대한 팟캐스트, Gradient Descent를 듣고 계십니다. 저는 진행자 루카스 브왈이고, 조나단 시다스는 Turing이라는 회사의 CEO이자 공동 창립자입니다. Turing은 생소한 회사일 수도 있지만, LLM 생태계에서 점점 더 중요한 위치를 차지하고 있습니다. LLM이 코드를 학습 데이터로 사용하는 경우가 점점 늘어나고 있기 때문입니다. …
- B1 디지털·AI 기술의 활용: 이러한 모델은 사용자에 대한 풍부한 맥락 정보와 이전 경험을 바탕으로, 마치 앤 드레 카르파티가 제시한 LLM(로봇 모델)의 추상화처럼 파일에 정보를 기록하고 언제 어디서 사용자에 대한 정보를 찾아야 하는지 아는 컴퓨터와 같은 존재가 될 수 있을 것입니다.
- B7 성과: 운영효율: Sil Value 기준으로 보면 10배 정도는 되어야 할 것 같은데, 개발자 생산성을 30% 향상시키는 건 사업에 엄청난 영향을 미치는 거죠.
- 수치 주장: 녹음을 마치고 나서 친구들이 AI 팟캐스트 같지 않고 90년대 후반 리눅스 배포판 팟캐스트 같다고 놀렸어요.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/What’s_the_path_to_AGI_A_conversation_with_Turing_Co-founder__DJS7cop0CCw.md`

**415. [Fine tuning Azure OpenAI Service Models with Weights & Biases](https://www.youtube.com/watch?v=2sfl0YqRODY)** — Weights & Biases · 에이전트·개발도구 · US · 2025-01 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: so thank you for joining myself and Amy and an nishe here for the fine-tuning session this morning where we're going to unpack and tell you about all the amazing fine-tuning features that we have but more importantly I'm…
- B1 디지털·AI 기술의 활용: so thank you for joining myself and Amy and an nishe here for the fine-tuning session this morning where we're going to unpack and tell you about all the amazing fine-tuning features that we have but more importantly I'm going to have these two amazing people …
- B8 부정 성과: 보안·프라이버시: so thank you for joining myself and Amy and an nishe here for the fine-tuning session this morning where we're going to unpack and tell you about all the amazing fine-tuning features that we have but more importantly I'm going to have these two amazing people …
- 수치 주장: so thank you for joining myself and Amy and an nishe here for the fine-tuning session this morning where we're going to unpack and tell you about all the amazing fine-tuning features that we have but more importantly I'm going to have these two amazing people …
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Fine_tuning_Azure_OpenAI_Service_Models_with_Weights_&_Biase__2sfl0YqRODY.md`

**416. [Unlocking the potential of MLOps and LLMOps](https://www.youtube.com/watch?v=7hxec4M48XY)** — Weights & Biases · 에이전트·개발도구 · US · 2025-01 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽
- 개요: [음악] 안녕하세요 여러분, 저녁 시간을 내어 프레젠테이션과 데모를 시청해 주셔서 감사합니다. 저는 사라 카시이고, Amia 사업부의 필드 엔지니어링 책임자입니다. 오늘은 Google Cloud와 협력하여 AI/ML 팀이 워크 플로우를 강화하고 협업을 한 단계 더 끌어올릴 수 있도록 지원하는 방법에 대해 이야기하게 되어 매우 기쁩니다. 플랫폼의 주요 기능과 실제 사례 및 스토리를 통해 여러분…
- B1 디지털·AI 기술의 활용: 그래서 딥 러닝 시대, 특히 토치와 텐서플로우 시대를 기반으로 만들어진 Weights and Bias가 이제 LLM 시대를 어떻게 지원할지 정말 기대됩니다.
- B8 부정 성과: 보안·프라이버시: Vertex AI에서 GPU와 TPU를 사용하여 가중치 및 편향 모델을 구축하고, 맞춤형 Pie Torch, 맞춤형 TensorFlow, 맞춤형 Jacks, 맞춤형 Hugging Face Transformer 트레이너 라이브러리, 그리고 Model Hub에서 제공하는 맞춤형 학습 실험을 추적하는 방법을 다시 한번 살펴보겠습니다.
- 수치 주장: 샌프란시스코에서 몇몇 고객들과 함께 작업하면서 만든 글인데, 4년도 더 전에 Weights and Bias가 GCP의 여러 서비스와 통합된다는 점을 다시 한번 강조하고 싶네요.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 칩·하드웨어 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Unlocking_the_potential_of_MLOps_and_LLMOps__7hxec4M48XY.md`

**417. [The rise of AI agents with João Moura of CrewAI](https://www.youtube.com/watch?v=Z2cy4CGfsbc)** — Weights & Biases · 에이전트·개발도구 · US · 2025-02 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 여러분은 머신 러닝을 현실 세계에 적용하는 방법에 대한 프로그램인 Gradient Descent를 듣고 계십니다. 저는 진행자 루카스 발입니다. 오늘 우리는 AI 에이전트 플랫폼 업계를 선도하는 Crew AI의 CEO이자 공동 창립자인 조 모아(Joe MOA)와 이야기를 나눠보겠습니다. 그는 에이전트와 기업 환경에서의 에이전트 활용 분야를 이끌고 있습니다. 우리는 K 플랫폼에서 에이전트가 어…
- B1 디지털·AI 기술의 활용: 예를 들어, TV에서 게임 스트리밍 영상을 실시간으로 보여주고, 에이전트가 공을 추적하고, 편집하고, 자막과 사운드를 추가하고, 소셜 미디어에 게시하는 방식입니다.
- B8 부정 성과: 보안·프라이버시: 최첨단 기술 분야에 뛰어들면, 코드 생성과 같은 전체 라이프사이클 자동화나 RS 양식 자동 입력과 같이 오류가 발생하면 안 되는 매우 복잡한 문제를 해결하려는 기업들을 볼 수 있습니다.
- 수치 주장: 웹사이트에 따르면 포춘 500대 기업의 40%가 KAT를 사용하고 있다고 하는데, 어떻게 그렇게 높은 도입률을 달성했는지, 그리고 어떤 산업 분야에서 KAT 에이전트 옵션이 가장 많이 도입되었는지 말씀해 주시겠어요?
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/The_rise_of_AI_agents_with_João_Moura_of_CrewAI__Z2cy4CGfsbc.md`

**418. [Mastering model customization: fine-tuning Azure OpenAI service models with Weights & Biases](https://www.youtube.com/watch?v=N1CI8Ld0-PA)** — Weights & Biases · 에이전트·개발도구 · US · 2025-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요 여러분, 오늘 크리스와 아니쉬와 함께 Azure Open AI 서비스 와 Weights and Bias를 활용한 모델 맞춤 설정 및 미세 조정에 대해 이야기하게 되어 정말 기쁩니다. 저는 Azure 에서 미세 조정을 담당하는 알리시아 프레임이고, 크리스 파이넬은 Weights and Bias의 공동 창립자이자 CISO입니다. 오늘 웨비나에 오신 모든 분들께 인사드리고 싶었…
- B1 디지털·AI 기술의 활용: 주제에 대한 이해를 돕기 위해, 파인튜닝이란 무엇인지, 왜 파인튜닝이 필요한지, 다양한 산업 분야의 사용 사례는 무엇인지, 그리고 Azure Open AI와 가중치 및 편향을 사용하여 파인튜닝하는 방법에 대해 이야기해 보겠습니다.
- B8 부정 성과: 보안·프라이버시: 주제에 대한 이해를 돕기 위해, 파인튜닝이란 무엇인지, 왜 파인튜닝이 필요한지, 다양한 산업 분야의 사용 사례는 무엇인지, 그리고 Azure Open AI와 가중치 및 편향을 사용하여 파인튜닝하는 방법에 대해 이야기해 보겠습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Mastering_model_customization_fine-tuning_Azure_OpenAI_servi__N1CI8Ld0-PA.md`

**419. [Measure and iterate on AI application performance using W&B Weave](https://www.youtube.com/watch?v=pxbNLZ9k9Bo)** — Weights & Biases · 에이전트·개발도구 · US · 2025-04 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: [Music] Hi, I'm Russ from Weights and Biases and today I'll be discussing evaluating AI applications using W&amp;B weave. After scoping and building a prototype, the next step in the AI application development workflow i…
- B7 성과: 조직성과: A thorough AI application evaluation process plays effectively the same role as unit testing applied to more traditional nonLMbased applications.
- B1 디지털·AI 기술의 활용: We can see the call to the function that grabs the rag content, a wrapper around the question asked by the customer and the API call to the LLM itself.
- 교량: — · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Measure_and_iterate_on_AI_application_performance_using_W&B___pxbNLZ9k9Bo.md`

**420. [Safeguard your users and brand with W&B Weave Guardrails](https://www.youtube.com/watch?v=KOwajQfIWC4)** — Weights & Biases · 에이전트·개발도구 · US · 2025-04 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: [Music] Hi, I'm Russ from Weights and Biases and today we'll be taking a look at W&amp;B weave guard rails. Developing a successful AI application relies on rigorous evaluations, rapid iteration, and constant monitoring.…
- B8 부정 성과: 보안·프라이버시: Commonly applied safety scores for customer interactions include detecting toxicity, bias, personally identifiable information and hallucinations.
- B1 디지털·AI 기술의 활용: The generate text function serves as an example of an LLM API call.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Safeguard_your_users_and_brand_with_W&B_Weave_Guardrails__KOwajQfIWC4.md`

**421. [From pharma to AGI hype, and developing AI in finance: Martin Shkreli’s journey](https://www.youtube.com/watch?v=IzDEfkRFKmI)** — Weights & Biases · 에이전트·개발도구 · US · 2025-05 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 지금 듣고 계신 프로그램은 머신러닝을 실제 세계에 적용하는 방법에 대한 팟캐스트, Gradient Descent입니다 . 안녕하세요, 저는 진행자 루카스 베왈드입니다. 오늘은 정말 예상치 못한 손님과 이야기를 나눠보겠습니다. 제 동료 중 일부는 제가 이 인터뷰를 준비한다는 것 자체가 만우절 농담이라고 생각했습니다. 이번 방송은 마틴 스크레이와 함께하는데, 아마 여러분 중 많은 분들처럼 저도 …
- B1 디지털·AI 기술의 활용: 제 생각에는 머신러닝이나 딥러닝 기술을 실제 실험실 작업이나 신약 개발 같은 데 적용하는 것보다 그게 훨씬 더 효과적일 것 같아요.
- B7 성과: 조직성과: 수익성 있는 약을 만들어서 특정 집단, 특히 희귀 질환을 앓고 있어서 치료를 받지 못하는 사람들에게 도움을 주고 싶은 마음은 이해해."라는 반응이 나오죠.
- 수치 주장: 제가 가격을 인상한 약은 약 70년 전에 개발된 약인데, 그 누구도 그보다 더 나은 버전을 만들지 못했습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Weights_&_Biases/From_pharma_to_AGI_hype,_and_developing_AI_in_finance_Martin__IzDEfkRFKmI.md`

**422. [AI’s $600B Question: Scaling for what comes next](https://www.youtube.com/watch?v=DmfVlf1yHb4)** — Weights & Biases · 에이전트·개발도구 · US · 2025-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: 저는 데이비드를 6년 넘게 알고 지냈는데, 데이비드는 W&amp;B가 지금의 위치에 오르는 데 가장 큰 도움을 준 사람 중 한 명입니다 . 그러니 그 점에 대해서는 감사드립니다, 데이비드. 감사합니다. 시작하기 전에 여러분들을 조금 더 알아보고 싶었습니다 . 그럼 여기 있는 사람들 중에 Jai랑 같이 게임하는 사람은 몇 명이나 되나요? 여러분 대부분이요. 좋아요, 잘됐네요. 모두 잘 지내시길…
- B4 가치네트워크·생태계: 음, 그러니까 AI 시장 규모가 6 천억 달러라는 질문은 기본적으로 AI 생태계의 수익 규모와 하이퍼스케일 기업들이 투자한 자본 규모( capex)를 비교해 보는 것입니다.
- B5 직무·역량 변화: 그렇다면 인재 전쟁이 치열해지는 이 세상에서 개발자들이 스타트업 창업자들보다 더 큰 협상력을 갖게 될 거라고 생각하시나요 ?
- 수치 주장: 그러고 보니 예전에 당신이 10억 명의 개발자를 만드는 것에 대해 썼던 기사가 생각나네요.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Weights_&_Biases/AI’s_$600B_Question_Scaling_for_what_comes_next__DmfVlf1yHb4.md`

**423. [Building future-ready AI with agents & data flywheels: Insights from NVIDIA’s enterprise deployments](https://www.youtube.com/watch?v=innRr5Pleyg)** — Weights & Biases · 에이전트·개발도구 · US · 2025-06 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: Hello everybody. How's everybody doing today? Everybody had a great lunch? Yeah. All right. To get us started, how many of you are currently building agents in this room? Raise your hands. Awesome. And how many of you ar…
- B1 디지털·AI 기술의 활용: within their digital employees and initially they were built as rag systems but now they have the ability to plan to use tools and have become more complex.
- B2 파괴: 데이터 가용성: Uh and essentially what we talk about is first you want to monitor which is have the ability to collect real-time data and performance errors.
- 수치 주장: We were able to lower the latency by 40% and they were able to move from a 3GPU model to a single GPU model so that the total cost of ownership of the agent um was reduced.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Building_future-ready_AI_with_agents_&_data_flywheels_Insigh__innRr5Pleyg.md`

**424. [GitHub CEO Thomas Dohmke on Copilot and the Future of Software Development](https://www.youtube.com/watch?v=PPs5lZ2syv4)** — Weights & Biases · 에이전트·개발도구 · US · 2025-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽
- 개요: 여러분은 머신러닝을 실세계에 적용하는 방법에 대한 팟캐스트, 그래디언트 디센트를 듣고 계십니다. 저는 진행자 루카스 베왈드입니다. 네, 오늘은 깃허브의 CEO이신 토마스 씨와 이야기를 나눠보겠습니다. 저는 이 인터뷰를 꽤 오랫동안 기다려왔습니다. GitHub는 제가 10년 넘게 직장 생활을 하면서 거의 매일 사용해 온 제품 중 하나이며, 그래서 정말 애착이 갑니다. 마이크로소프트가 깃허브를 …
- B1 디지털·AI 기술의 활용: 그리고 음, 코파일럿과 관련해서, 아시 다시피 인수 후, 그리고 2019년 오픈 AI 투자 덕분에 마이크로소프트의 클라우드, 경험, 책임감 있는 AI 등 최고의 역량과 깃 허브의 개발자 우선 접근 방식, 그리고 오픈 AI 파트너십을 결합하여 GP3와 코덱스 모델에 접근할 수 있게 되었고, 이를 통해 오리지널 코파일럿, 즉 깃허브 코파일럿을 구축할 수 있었습니다 .
- B8 부정 성과: 보안·프라이버시: 음, 에이전트를 사용해서 목표를 달성할 수는 있겠지만, 에이전트가 작성한 내용이 실제로 정확한지, 새로운 보안 취약점을 만들지 않는지, 또는 시스템 속도를 너무 느리게 만들어서 비인간 플랫폼에 비해 컴퓨팅 자원이 10배나 더 필요하게 만들지 않는지 어떻게 검증할 수 있을까요?
- 수치 주장: 그리고 음, 코파일럿과 관련해서, 아시 다시피 인수 후, 그리고 2019년 오픈 AI 투자 덕분에 마이크로소프트의 클라우드, 경험, 책임감 있는 AI 등 최고의 역량과 깃 허브의 개발자 우선 접근 방식, 그리고 오픈 AI 파트너십을 결합하여 GP3와 코덱스 모델에 접근할 수 있게 되었고, 이를 통해 오리지널 코파일럿, 즉 깃허브 코파일럿을 구축할 수 있었습니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Weights_&_Biases/GitHub_CEO_Thomas_Dohmke_on_Copilot_and_the_Future_of_Softwa__PPs5lZ2syv4.md`

**425. [Weights & Biases and CoreWeave: Fully Connected 2025 Keynote](https://www.youtube.com/watch?v=09Ubfrdq508)** — Weights & Biases · 에이전트·개발도구 · US · 2025-06 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 괜찮은. 여기 오게 되어 정말 기쁩니다. 여기 오게 되어 정말 기쁩니다. 음, 그러니까 완전 연결(Fully Connected)은 사실 3년 전에 실험적으로 시작된 거예요. 어, 여기 앞줄에 있는 글로바나의 주요 인물들을 보면 알 수 있듯이, 우리는 사용자들과 소통하는 문화를 기반으로 성장해 왔습니다. 저는 우리 플랫폼에서 AI 모델을 구축하고 배포하는 사람들과 진심으로 소통하고 그들을 아끼…
- B8 부정 성과: 보안·프라이버시: 그래서 Co-Wave 모델에서 서부 편향을 학습시키면 미션 컨트롤과 인사이트에서 모든 데이터를 자동으로 가져와서 인프라에서 무슨 일이 일어나고 있는지, Co-IFT 팀이 어떤 조치를 취했는지 오버레이로 확인할 수 있습니다.
- B1 디지털·AI 기술의 활용: 하지만 그 전에, 일부 분들이 이번 인수가 가중치 및 편향에 어떤 영향을 미칠지, 그리고 멀티클라우드와 온프레미스 환경 전반에 걸친 업무 수행에 어떤 의미를 가질지에 대해 우려하고 계신다는 것을 알고 있습니다.
- 수치 주장: 노션은 2년 전 제나이(Genai)를 과감하게 출시한 최초의 기업 중 하나입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Weights_&_Biases_and_CoreWeave_Fully_Connected_2025_Keynote__09Ubfrdq508.md`

**426. [Building agentic AI workflows with W&B Weave: a hiring assistant case study](https://www.youtube.com/watch?v=tRGoT1QV8VA)** — Weights & Biases · 에이전트·개발도구 · US · 2025-07 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: [Music] Hello everyone. This is Nico and Karan and today we'll be walking you through a state-of-the-art agent AI application focused on evaluation, guardrails, and auditability. For the purposes of this demo, we'll use …
- B1 디지털·AI 기술의 활용: So again if you have any um agentic application or any genai application dealing with multimodel data uh reads and biases can log and allow you to visualize them.
- B8 부정 성과: 보안·프라이버시: And now if you notice when I was mentioning the either of the two scenarios that happened, this is the case where a hallucination happened for the first time.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Building_agentic_AI_workflows_with_W&B_Weave_a_hiring_assist__tRGoT1QV8VA.md`

**427. [The AI that solves the market: A new era in forecasting with natural language explainability](https://www.youtube.com/watch?v=zbmXulPIJpo)** — Weights & Biases · 에이전트·개발도구 · US · 2025-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 여러분, 안녕하세요. 안녕. 제 말 들리세요? 시원한. 안녕하세요. 제 이름은 영입니다. 네, 저는 LGI 리서치의 사업 개발 및 파트너십 담당 이사입니다 . 음, 저는 특히 금융 서비스와 예측 분야에 집중하고 있습니다. 음, 시작하기 전에, 혹시 여기 재무 담당자분들 계신가요? 환영. 샌프란시스코에서는 그들을 찾기가 정말 어려워요 . 음, 알겠습니다. LG라는 회사는 익숙하실 수도 있지만,…
- B1 디지털·AI 기술의 활용: 앞서 말씀드린 것처럼, 우리는 하루에 약 6,000개의 뉴스 기사를 소비하고 있으며, AI 경제학자는 엑셀과 LLM을 활용한 감정 분석 등을 통해 딥러닝 기반 예측 모델을 사용하여 예측을 수행하고 있습니다.
- B2 파괴: 데이터 가용성: 음, 순전히 성능적인 관점에서 볼 때, 빨간색 화살표가 가리키는 시점은 저희가 뉴스 데이터, 즉 뉴스 보도와 같은 비정형 데이터를 더 많이 활용하기 시작한 시점입니다 .
- 수치 주장: 저희는 XL1이라는 자체 개발 LLM 모델을 보유하고 있는데, 이는 320억 개의 파라미터를 가진 모델입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: 검색·RAG
- 원문: `transcripts/channels/Weights_&_Biases/The_AI_that_solves_the_market_A_new_era_in_forecasting_with___zbmXulPIJpo.md`

**428. [The future of multi-agents in enterprises](https://www.youtube.com/watch?v=GpbmI5NtuSQ)** — Weights & Biases · 에이전트·개발도구 · US · 2025-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B2 파괴, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 어, 여기 오게 되어 정말 기쁩니다. 크레이(Crayi)에 대해 들어보신 분 몇 분이나 되시나요? 손을 들어주세요 . 맙소사. 제가 이 질문을 했을 때 아무도 손을 들지 않았던 적이 있습니다. 그건 그다지 인상적이지 않았어요. 오늘 이렇게 여러분 모두를 뵙게 되어 정말 기쁩니다. 그리고 제가 인종과 편견에 대해 이야기 나누던 중에, 여러분 모두를 정말 좋아합니다. 정말 훌륭한 작품입니다. 음…
- B1 디지털·AI 기술의 활용: 저는 이 사용 사례에 클라우드를 사용하고 싶 거나 CI 와 향상된 메모리를 사용할 예정이지만, 내일은 ME 제로 또는 인증까지 사용하고 싶어질 수도 있습니다 .
- B4 가치네트워크·생태계: 제 생각에는 많은 기업들이 클라우드로 전환하는 과정에서 어려움을 겪었고, 이제 특정 벤더에 종속되어 벤더 종속 상태에 놓인 것 같습니다.
- 수치 주장: 제가 믿기 힘든 건, 그런 유형의 구인 공고가 매달 100%씩 증가하고 있다는 겁니다 .
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Weights_&_Biases/The_future_of_multi-agents_in_enterprises__GpbmI5NtuSQ.md`

**429. [Arvind Jain on building Glean and the future of enterprise AI](https://www.youtube.com/watch?v=lYz5MQvK3wU)** — Weights & Biases · 에이전트·개발도구 · US · 2025-08 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: You're listening to Gradient Descent, a show about making machine learning work in the real world. And I'm your host, Lucas Bewald. This is a conversation with Arvin Jane, who I've known for a while. Arind is the CEO of …
- B1 디지털·AI 기술의 활용: You know in those days nobody was talking about large language models and the term generative AI did not exist to my knowledge at the time.
- B8 부정 성과: 보안·프라이버시: So, so, so that's how we suppress uh hallucinations a little bit through this sort of citation and reference checking.
- 수치 주장: go look into our product dashboards and look at the usage and then um and then like you know take take all of that data and based on that like you know now give me a risk profile like you know whether it's you know like a account that is healthy like green gre…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/Arvind_Jain_on_building_Glean_and_the_future_of_enterprise_A__lYz5MQvK3wU.md`

**430. [Build and monitor multi-agent contact centers using Weights & Biases](https://www.youtube.com/watch?v=MjqHVfmKEoM)** — Weights & Biases · 에이전트·개발도구 · US · 2025-10 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: [음악] 안녕하세요, 저는 Weights and Biases의 Russ입니다. 오늘은 Weights and Biases AI 개발자 플랫폼이 어떻게 신뢰할 수 있고 고품질의 다세대 AI 컨택 센터를 구축하기 위해 평가, 모니터링 및 반복 작업에 필요한 도구를 제공하는지 설명드리겠습니다. 자동응답 시스템과 통화할 때면, 상담원과 연결되기를 바라며 별표 버튼과 0번 버튼을 반복해서 누르게 되는 …
- B4 디지털 채널: 이 시스템은 데이터 수집을 간소화하고 콜센터를 다른 비즈니스 소프트웨어와 더욱 쉽게 통합할 수 있도록 지원하여 고객과 데이터에 대한 더 깊은 통찰력과 더 나은 이해를 구축할 수 있도록 해줍니다 .
- B1 디지털·AI 기술의 활용: 지원 문제를 해결하기 위해 단 한 명의 상담원이나 심지어 단 하나의 AI 에이전트에만 전적으로 의존하는 대신 , 다중 에이전트 컨택 센터는 서로 협력하고 기존 비즈니스 애플리케이션 과 원활하게 통합될 수 있는 여러 전문 상담원을 활용합니다 .
- 수치 주장: W andbweave 추적 기능은 개발 및 운영 중에 주요 지표를 캡처하므로 비용뿐만 아니라 다양한 측면에서 성능을 항상 100% 파악할 수 있습니다.
- 교량: — · 기술: 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Build_and_monitor_multi-agent_contact_centers_using_Weights___MjqHVfmKEoM.md`

**431. [Defining factors for enterprise AI agents - JetBrains @ FC London '25](https://www.youtube.com/watch?v=igUpMlGqyWo)** — Weights & Biases · 에이전트·개발도구 · US · 2025-12 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 팔토리안, 즉 예측 가능성, 비용 효율성이야말로 미래 기업용 AI 에이전트를 정의하는 요소가 될 것입니다. 그럼 먼저 회사 소개부터 시작하겠습니다. 혹시 모르시는 분들을 위해 말씀드리자면, Jet Brains는 IntelliJ, PyCharm 등과 같은 전문가용 소프트웨어 개발사입니다 . 하지만 그 외에도 저희는 Jet Brains AI 브랜드를 보유하고 있습니다. 혹시 JetBrains C…
- B1 디지털·AI 기술의 활용: 이는 클라우드 기반의 협업 AI 에이전트 환경으로, 개발자, QA 담당자, 제품 관리자, 디자이너 등이 모두 AI 에이전트를 사용하여 동일한 제품을 함께 개발할 수 있도록 지원합니다.
- B8 부정 성과: 보안·프라이버시: 그래서 요리 도구와 가중치 및 편향을 함께 사용하면 단순히 재미있는 데모가 아니라 예측 가능하고 확장 가능하며 엔터프라이즈급이고 설명 가능한 신뢰할 수 있는 시스템을 구축할 수 있습니다.
- 수치 주장: 모델은 계속 발전하고 있고, 설령 99%의 정확도를 달성한다고 해도 , 핵심 기업 애플리케이션에 배포하기에 과연 충분할까요 ?
- 교량: — · 기술: —
- 원문: `transcripts/channels/Weights_&_Biases/Defining_factors_for_enterprise_AI_agents_-_JetBrains_@_FC_L__igUpMlGqyWo.md`

**432. [Fully Connected Tokyo 2025: Opening Keynote with W&B Cofounders Lukas Biewald & Chris Van Pelt](https://www.youtube.com/watch?v=Uw2aEJ4CzwM)** — Weights & Biases · 에이전트·개발도구 · US · 2025-12 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Imagine a world where we decode the mysteries of disease, scale clean energy to protect Earth's resources, reach every eager learner, and distribute harvests globally, all while reclaiming ing time for what matters [musi…
- B1 디지털·AI 기술의 활용: So first I'm going to talk about models which is our product that helps AI engineers fine-tune or actually train frontier models from scratch.
- B7 성과: 조직성과: The evaluation explorer lets you drill in to all of the different evaluation uh data sets that you've configured in the system and better understand which experiment to run next so that you can improve your application.
- 수치 주장: So, I don't know if you remember about a year ago, a new DeepSeek showed maybe the power of RL and the ability to build highquality um LMS outside the foundation labs and it caused Nvidia's uh market cap to drop $600 billion overnight.
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Fully_Connected_Tokyo_2025_Opening_Keynote_with_W&B_Cofounde__Uw2aEJ4CzwM.md`

**433. [Atlassian’s Most Controversial Growth Decision | Mike Cannon-Brookes](https://www.youtube.com/watch?v=S3RmvHfJll4)** — Weights & Biases · 에이전트·개발도구 · US · 2026-01 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 우리는 사람들의 문제를 해결합니다. 우리는 기술적인 문제를 해결하지 않습니다. 오늘날 대부분의 음악 관련 사업은 기술 중심의 사업입니다. 우리는 기술팀과 비즈니스팀을 연결하여 비즈니스 프로세스를 운영하려고 노력합니다. [음악] 아, 죄송합니다. 잠깐만, 그럼 다시 처음으로 돌아가도 될까요? 저는 Jira가 적어도 기술 티켓팅 시스템 제품에서 유래한 유산과 같은 것이라고 생각합니다. 지라의 초…
- B1 디지털·AI 기술의 활용: 그러니까 제품 관리자, 디자이너, 개발자, 네트워크 분석가, 시스템 엔지니어, 머신러닝 엔지니어 등 회사 내 많은 구성원을 기술팀이라고 부르고, 재무, 인사 등 나머지 구성원은 비즈니스팀, 비 기술팀, 서비스팀, 인사팀, 영업팀, 마케팅팀 등으로 부른다고 가정해 봅시다.
- B7 성과: 조직성과: 지속 가능한 성장을 하고 있는지, 아니면 장기적인 매출 성장을 위한 선행 지표가 있는지 알아보기 위해 살펴보는 다른 핵심 지표가 있나요 ?
- 수치 주장: 2019년에 팀워크 그래프를 개발하기 시작한 이유는 바로 이러한 이유 때문입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Weights_&_Biases/Atlassian’s_Most_Controversial_Growth_Decision_Mike_Cannon-B__S3RmvHfJll4.md`

**434. [Fully Connected Tokyo: [Hands-on workshop] Automation of document workflows in financial industry](https://www.youtube.com/watch?v=3VJZhKEG4ik)** — Weights & Biases · 에이전트·개발도구 · US · 2026-01 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 그럼, 고마워, 모두들 오늘, 그, 이렇게 많은 분들 모임 주셔서 감사합니다. 새로 고침 그럼, 업스테이지 일본에서입니다. , 그, 컨트리 매니저 마츠시타라고 합니다. 오늘은 그, 2시간 3 시간이군요, 조금 긴 정장이 될까 생각합니다. 그렇지만, 꼭 교제해 주셔서 감사합니다. 부탁드립니다. 네. 음, 음, 오늘 네, 세션의 제목으로, 음, 금융 업계에서, 문서 워크플로우 자동화 그런데 붙어…
- B1 디지털·AI 기술의 활용: 하지만 그 부분은 그 LLM 자체를 파인 튜닝을하고 전문을 만들어 둡니다.
- B8 부정 성과: 보안·프라이버시: 그래서, 예를 들어 여기의 사례라면, 그리고 이미지이지만, 확실히 10,000 엔 아래쪽에 대해서는 이미 거의 완전 자동 네, 그 부분에서 오류가 발생합니다.
- 수치 주장: 음, 음, 나의 시작 조금 10 분 정도입니다.
- 교량: Avenue 1 동적역량 · 기술: 파인튜닝·학습 · 추론 최적화 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Fully_Connected_Tokyo_[Hands-on_workshop]_Automation_of_docu__3VJZhKEG4ik.md`

**435. [Fully Connected Tokyo: [Hands-on workshop] From 0 to automated evals](https://www.youtube.com/watch?v=BX-AjQUUol8)** — Weights & Biases · 에이전트·개발도구 · US · 2026-01 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: [clears throat] I'm Scott. So, thank you for uh coming. Um yeah, so today we'll be learning about automated evals. I'm the PM of or product manager of our weave product. Um so I'll give a quick intro. Um I'll go through …
- B1 디지털·AI 기술의 활용: Um maybe just so I know who uh the level of experience in the audience um who has used an LLM API like OpenAI or something like that.
- B7 성과: 조직성과: Um, and the whole purpose of evaluations is to have a systematic way of testing your apps and hopefully defining some criteria to say, okay, this is good.
- 수치 주장: and then do the same with an LLM judge and if it's around the same as the correlation between two people like okay cool like now we can hill down on that um if it if it's like 50% or like much less like probably focus on making getting it to be aligned with th…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Fully_Connected_Tokyo_[Hands-on_workshop]_From_0_to_automate__BX-AjQUUol8.md`

**436. [Why Big Tech Buys GPUs From CoreWeave | Corey Sanders](https://www.youtube.com/watch?v=h3SNaAPUxHY)** — Weights & Biases · 에이전트·개발도구 · US · 2026-01 · en · 4/8블록 · `ax_adjacent`/`washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: I don't care if the APIs are consistent and commoditized. The level of quality, performance, and capability and experience that we deliver today will not win workloads in 2 years. For anyone who's deployed on a public cl…
- B1 디지털·AI 기술의 활용: Like I'm just I want to just see if I can get something to work versus, you know, for spend forever to figure out how to get to our Grafon API.
- B4 디지털 채널: Like, I don't think our lot of cash with our chaos storage would be the right thing to run an e-commerce website.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 거버넌스·평가 도구
- 원문: `transcripts/channels/Weights_&_Biases/Why_Big_Tech_Buys_GPUs_From_CoreWeave_Corey_Sanders__h3SNaAPUxHY.md`

**437. [She Raised $64M to Build an AI Math Prodigy | Carina Hong, CEO of Axiom](https://www.youtube.com/watch?v=QxfsjDBDw3M)** — Weights & Biases · 에이전트·개발도구 · US · 2026-02 · ko · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B6 장벽 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B7 긍정 성과
- 개요: Axim의 목표는 자체적으로 성능을 향상시키고 생성과 검증을 결합한 추론 엔진을 구축하는 것입니다. 푸틴햄에게, 그리고 수학 덕후가 아닌 사람들에게는 , 이 시험은 수학 전공 학부생들 간의 엄청나게 어려운 경쟁과 같습니다. 중앙값은 0과 같습니다. 저희는 최근 Axiom Prew 테스트에서 12점 만점에 8점을 받았습니다. 저희는 Lean과 같은 형식 언어를 사용하여 자연어 대응 개념을 구체…
- B8 부정 성과: 보안·프라이버시: 아마 한 시간 정도는 무차별 대입 방식으로 해결할 의향이 있지만, 기하학적 문제가 아닌 경우에는 꼭 그럴 필요는 없을 것 같습니다.
- B1 디지털·AI 기술의 활용: 그들이 다양한 관점에서 사물을 생각하는 방식을 보는 것은, 예를 들어 머신 러닝에 대해 잘 모르는 수학자들이 우리에게 많은 영감을 주는 것과 같습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/She_Raised_$64M_to_Build_an_AI_Math_Prodigy_Carina_Hong,_CEO__QxfsjDBDw3M.md`

**438. [The $8.6B Self-Driving AI Backed by Nvidia and Uber | Alex Kendall, Wayve](https://www.youtube.com/watch?v=k5wgts8y-xU)** — Weights & Biases · 에이전트·개발도구 · US · 2026-04 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 자율 주행은 인공지능( AI) 접근 방식을 통해 자율주행차 문제를 바라보는 것입니다. 사고 발생률을 거의 0에 가깝게 줄일 수 있는 기회가 있습니다. 그래서 우리는 150만 달러를 모금하고, 친구들을 모아 집을 빌리고, 차를 차고에 넣어두고 해킹을 시작했습니다. 고가의 개조 차량에서 벗어나, 컴퓨팅 자원, 고화질 지도, 인프라에 의존하던 시대에서, 이제는 3만, 4만, 5만 달러에 구입하거나…
- B4 가치네트워크·생태계: 고가의 개조 차량에서 벗어나, 컴퓨팅 자원, 고화질 지도, 인프라에 의존하던 시대에서, 이제는 3만, 4만, 5만 달러에 구입하거나 제조할 수 있고, 글로벌 공급망에서 조달 가능한 내장 하드웨어를 갖추고 , 고화질 지도가 필요 없으며, 어디든 주행할 수 있는 대량 생산 차량으로 변화하고 있습니다.
- B1 디지털·AI 기술의 활용: 그래서 2017년에 저는 박사 학위 논문을 마치고 다양한 지각 작업, 위치 추정, 스테레오 비전, 의미론적 분할, 불확실성 추정 등 고차원, 수백만 차원의 이미지를 입력받아 세계를 압축적으로 표현하는 데이터로 변환하는 엔드투엔드 학습 시스템을 위한 최초의 딥러닝 모델을 구축할 수 있었습니다.
- 수치 주장: 그리고 10년 전, 우리는 자율주행 1.0, 즉 기존 센서 개조, 컴퓨팅, HD 지도, 인프라에 의존하고 확장성이 매우 제한적이었던 1세대 접근 방식 없이 가능한 최대 규모에서 추론하고, 노력하고, 일반화할 수 있는 단일 모델을 구축하는 작업을 시작했습니다 .
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/The_$8.6B_Self-Driving_AI_Backed_by_Nvidia_and_Uber_Alex_Ken__k5wgts8y-xU.md`

**439. [Curing Every Disease With Al by 2050 | Sam Rodriques, Edison Scientific](https://www.youtube.com/watch?v=Q7NpRG2gAxc)** — Weights & Biases · 에이전트·개발도구 · US · 2026-05 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: If we want to go and cure all diseases, understand how the brain works and solve aging and AI seemed like the right way to do that. When it comes to the world as we experience it, most things are pretty well understood e…
- B8 부정 성과: 보안·프라이버시: [laughter] I mean, but then yeah, I will say like I I do I do admire people who like uh I have a lot of admiration for the biohacker movement.
- B7 성과: 운영효율: It's strong on things that are verifiable and it's strong on things where throughput matters a lot.
- 수치 주장: Since we launched Cosmos, people have probably used Cosmos to make like 20 or 30,000 novel scientific findings, which [music] is wild.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습
- 원문: `transcripts/channels/Weights_&_Biases/Curing_Every_Disease_With_Al_by_2050_Sam_Rodriques,_Edison_S__Q7NpRG2gAxc.md`

---

## Zapier


**440. [AI Transformation AMA for HR Leaders](https://www.youtube.com/watch?v=lYOR4pgVdb0)** — Zapier · 에이전트·개발도구 · US · 2025-09 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: Okay. And here we are. Welcome, welcome from around the world as we warm up for today's ask me anything on AI transformation with a focus on HR leaders. We'll do intros in a minute that you have uh co-host today. You hav…
- B5 직무·역량 변화: Uh from uh talent attraction and hiring to onboarding, talent development, total rewards, uh the whole the whole deal.
- B5 리더십·CDO/CAIO: Um, maybe a good question is how do you keep up with everything that's going on and how do you help the exec team and leadership team keep up as well?
- 수치 주장: So first a lot of folks asked over like hey like generally speaking what have the ingredients been so far for you know scaled AI adoption within uh Zapier and you know it really got Wade and I thinking about kind of the present state more broadly like all of o…
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 칩·하드웨어 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/AI_Transformation_AMA_for_HR_Leaders__lYOR4pgVdb0.md`

**441. [How Zapier Runs AI Hack Week | Real Examples of AI Transformation at Work](https://www.youtube.com/watch?v=e1pk34c3oYU)** — Zapier · 에이전트·개발도구 · US · 2025-09 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽
- 개요: Hey, hey, awesome. Uh, welcome everybody. Uh, I'm Ryan. I'm here from the Zapier team and excited to talk to y'all about um hosting an AI hack week and we're going to do a little case study of how we just did this in Aug…
- B1 디지털·AI 기술의 활용: And so I owe a lot of my agent prompt to just shaping it in chat GPT, which was like a really helpful partner in creating a great agentic prompt.
- B7 성과: 운영효율: So, for like the call prep, for example, um if you're saving 15 minutes per rep, you can sort of like extrapolate that out and provide a time savings calculation.
- 수치 주장: Um, I uh I just grabbed this from our our pulse survey and we've got 97% adoption and the cool part is when we look at the tooling usage in the back end, we're seeing that match.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/How_Zapier_Runs_AI_Hack_Week_Real_Examples_of_AI_Transformat__e1pk34c3oYU.md`

**442. [Build an AI First RevOps Team for MAXIMUM Impact](https://www.youtube.com/watch?v=4_vkQdMQ5xs)** — Zapier · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 여러분, 안녕하세요. 오늘 웨비나에 오신 것을 환영합니다. AI를 최우선으로 하는 리옵스 팀 구축: 도입부터 구현까지 모든 과정을 살펴보겠습니다. 저는 알리샤이고 오늘 여러분의 진행자 중 한 명입니다 . 잠시 후 리아가 합류하여 질문을 진행해 줄 예정입니다 . 그러니 궁금한 점이 있으면 언제든지 질문해 주세요 . 저희는 여러분이 이러한 훌륭한 사상가 들과 소통하고 실시간으로 질문에 대한 답변…
- B1 디지털·AI 기술의 활용: 하지만 내부 사용 사례를 위해 AI 에이전트를 구축하는 것과, 비즈니스에서 실행해야 하는 리드-기회, 기회-계약, 견적-캐시 프로세스에 통합될 AI 에이전트를 구축하는 것은 완전히 다릅니다.
- B3 전략적 대응: 음, 그리고 저는 그게 괜찮은 출발점이었다는 건 인정하지만, 테사가 앞서 지적했듯이, 만약 그걸 실질적인 사업적 성과로 연결시킬 수 없다면 이사회 차원의 논의 대상이 될 리가 없죠.
- 수치 주장: 음, 이 주제에 관심이 있으시다면 , 10월 15일 목요일에 Zapier를 사용하여 첫 번째 AI 에이전트를 구축하는 RevOps 실습 워크숍이 있습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Zapier/Build_an_AI_First_RevOps_Team_for_MAXIMUM_Impact__4_vkQdMQ5xs.md`

**443. [From Zero to Millions in ARR: How AI-Powered Builders Are Scaling on Replit | Agents of Scale](https://www.youtube.com/watch?v=rHyqHuZ93Z4)** — Zapier · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B6 장벽 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B7 긍정 성과
- 개요: 문화. 저는 기업가 정신 문화라고 하면 권한 부여 문화를 꼽을 수 있다고 100% 확신합니다 . 회사의 규모나 역사는 중요하지 않습니다. 일반적으로 ' 내가 이렇게 하면 보상을 받을 거야'라고 생각하는 문화가 만연해 있습니다. [음악] 안녕하세요 여러분, Agents of Scale에 다시 오신 것을 환영합니다 . 이 프로그램은 기술 업계 전반의 리더들이 모여 기업 내에서 인공지능을 실제로 …
- B1 디지털·AI 기술의 활용: 하지만 이제는 심층적인 조사, 심층적인 추론, LLM(Learning Leadership Model)과 같은 도구를 활용하여 연락처를 설계하고 최적의 홍보 메시지를 만들기 위해 적합한 연락처를 찾아낼 수 있게 되면서, 이러한 작업이 훨씬 수월해졌다고 생각합니다.
- B2 파괴: 소비자 행동·기대: 소프트웨어 아키텍처, 사용자 경험( UX) 등을 고민해야 하고, 에이전트가 오류를 일으킬 수도 있고, 인내심을 가져야 해요.
- 수치 주장: 예를 들어 구글에서 10억 명의 사용자를 위한 분산 시스템을 개발하는 엔지니어는 AI 분야에서 그다지 많이 활용되지 않는 전문 지식을 가지고 있죠.
- 교량: — · 기술: LLM 모델 · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/From_Zero_to_Millions_in_ARR_How_AI-Powered_Builders_Are_Sca__rHyqHuZ93Z4.md`

**444. [Millions of Users and Billions of Files: Box CTO on Building AI | Agents of Scale](https://www.youtube.com/watch?v=B3E3qhTWSSg)** — Zapier · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 음악에 있어서 급격한 변화라는 개념은 매우 중요합니다. 왜냐하면 어떤 팀들은 너무 많은 변화를 주면 무너지기 때문입니다 . 음악은 거의 매일, 아니면 매주 바뀔 수 있기 때문에, 모든 것이 바뀔 수 있다는 것을 미리 각인시켜 놓고 그에 맞춰 프로세스를 개발해야 합니다. 자, 여러분, Agents of Scale에 다시 오신 것을 환영합니다. 저는 WDE 포스터입니다. 저는 Zapier의 공동…
- B2 파괴: 데이터 가용성: 그게 가장 큰 어려움 중 하나인 경우가 많은데, 예를 들어 일부 회사에서 처음 나온 솔루션들은 비정형 데이터를 활용하면 이렇게 멋진 일이 일어난다고 홍보했지만, 모든 회사, 모든 직원이 각기 다른 데이터에 접근할 수 있다는 점을 고려하지 않았습니다.
- B1 디지털·AI 기술의 활용: 저는 AI 에이전트를 사용하는 기업들의 로드맵과 현재 이용 가능한 기술들을 살펴보기 시작하면서, 최첨단 프로그래머들이 AI의 초기 단계, 즉 더 복잡한 기술적 구현들을 다룰 수 있는 능력을 갖추고 있다는 것을 알게 되었습니다.
- 수치 주장: 아시다시피, Zapier는 14 년 전에 시작되었고 저희는 이를 자동화하고 있지만, 말씀하신 대로 거의 대부분 정형화된 데이터입니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준 · 검색·RAG
- 원문: `transcripts/channels/Zapier/Millions_of_Users_and_Billions_of_Files_Box_CTO_on_Building___B3E3qhTWSSg.md`

**445. [She Built 1Mind — The AI That’s Outselling Humans | Agents of Scale](https://www.youtube.com/watch?v=jKQ7yhlgcKI)** — Zapier · 에이전트·개발도구 · US · 2025-10 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 완전히 새로운 세상이고, 흥미 진진한 세상입니다. 그래서 저는 우리가 전략을 다시 세워야 한다고 생각합니다. 제가 생각했던 것처럼, 이제 SAS 프레임워크와 시장 진출 전략에 대한 기본적인 내용을 알았는데, 이제 우리는 어떻게 접근해야 할지 전혀 모르는 완전히 새로운 세계로 발을 들여놓게 된 것 같습니다. 네 , 맞아요. 제가 말하려던 건, 작전 지침서 같은 게 있냐는 거였어요. 음, 그러니…
- B1 디지털·AI 기술의 활용: 제 생각에는 이 용어가 현재 진행되고 있는 업무를 훨씬 더 잘 나타내는 것 같고, 인공지능 엔지니어, 그러니까 머신러닝 엔지니어 같은 직종과는 확연히 다릅니다.
- B3 전략적 대응: 하지만 제 생각에는, 그 회사의 경영진들이 직원들에게 만약 그들이 이 상황에 적극적으로 대처하더라도 여전히 일자리를 유지할 수 있고, 단지 모습이 달라질 뿐이라는 확신을 심어주는 것이 중요하다고 봅니다.
- 수치 주장: 음, 그러니까, 지난 10년 동안 그런 느낌이 좀 들었을 수도 있지만, 만약 있었다면 Zapper에서 제대로 활용하지는 못했던 것 같아요.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Zapier/She_Built_1Mind_—_The_AI_That’s_Outselling_Humans_Agents_of___jKQ7yhlgcKI.md`

**446. [The $50M Pricing Gamble and Intercom's AI Reinvention | Agents of Scale Podcast](https://www.youtube.com/watch?v=qMVhi485d8s)** — Zapier · 에이전트·개발도구 · US · 2025-10 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B5 구조 변화 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B6 장벽, B7 긍정 성과
- 개요: This is a hugely exciting time to be in tech. If you can't get out of bed and run to the office at on like moments like this, like uh you're probably, you know, maybe tech for you cuz like this is technology at its great…
- B1 디지털·AI 기술의 활용: So Finn was like the the first generative AI uh AI agent that could like do customer support.
- B5 직무·역량 변화: You know when he will do these like big layoffs these big cuts you know folks will often say you know critique him on that.
- 수치 주장: we had to wait until GP4 uh really because we needed we needed its smarts to to guard rail against hallucination and and so that that was like you know once we launched that at launch date I think we were doing like 24 25% resolution rate meaning like given 10…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 칩·하드웨어 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/The_$50M_Pricing_Gamble_and_Intercom's_AI_Reinvention_Agents__qMVhi485d8s.md`

**447. [What Netflix Knows About AI That Every Recruiter Should Learn](https://www.youtube.com/watch?v=edY-3X18CHc)** — Zapier · 에이전트·개발도구 · US · 2025-10 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B8 부정 성과
- 개요: 우리 그냥 얘기 좀 할 수 있을까? 무슨 일이야? 안녕하세요 여러분. 환영. 환영. 함께해 주셔서 정말 감사합니다. 참여하시는 분들께 몇 분 정도 시간을 드리겠지만, 참여하시면서 의견을 나눠주시면 정말 좋겠습니다 . 사람들은 어디에서 시청하고 있나요? 저스틴, 지금 어디에서 채널을 돌리고 계신가요? 저는 워싱턴주 시애틀 북쪽 출신입니다. 멋진. 멋진. 저는 캘리포니아주 로스앤젤레스에 있습니다…
- B5 직무·역량 변화: 채용 담당자가 챗봇에 자신의 역할과 원하는 인재상에 대한 몇 가지 질문에 답하면, 저희 AI 에이전트가 유사한 부서, 유사한 자격 요건 또는 역할을 가진 다른 채용 사례를 데이터베이스에서 검색하고, 담당자의 답변을 종합하여 채용 공고, 면접 질문, 평가 기준표 등과 같은 전체 패키지를 생성합니다.
- B7 성과: 운영효율: 그러니까 인공지능 과 자동화를 특정한 목적을 가지고 사용하는 사람들, 그리고 더 나아가 투자 수익률(ROI)을 위해 명확한 목적을 가지고 매일 꾸준히 인공지능과 자동화를 활용하는 사람들이 있다는 거죠.
- 수치 주장: 음, 그러니까 제가 8년 동안 인턴십 프로그램에서 보낸 시간의 대부분은 인재를 유치하는 것보다는 그 인턴들의 역량을 어떻게 평가해서 정규직 전환 기회를 줄 수 있을지에 대한 것이었다고 말씀드릴 수 있겠습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Zapier/What_Netflix_Knows_About_AI_That_Every_Recruiter_Should_Lear__edY-3X18CHc.md`

**448. [How Executive Assistants Drive Strategic Impact with AI](https://www.youtube.com/watch?v=-gGwrSPc3tA)** — Zapier · 에이전트·개발도구 · US · 2025-11 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요, 여러분! 환영. 오전, 오후, 어쩌면 저녁 시간까지 저희와 함께 보내주셔서 정말 기쁩니다. 자, 시작해 볼까요? 네 , Zapier의 ' 무엇이든 물어보세요' 코너에 오신 것을 환영합니다 . 오늘은 저와 코트니가 함께합니다. 먼저 간단한 소개를 해드리고 싶습니다 . 안녕하세요. 제 이름은 크리스티나 로마입니다. 저는 Zapier에서 최고제품책임자(CPO)와 최고재무책임자(CFO)…
- B5 직무·역량 변화: 예를 들어, " WDE의 최우선 순위는 아니기 때문에 후보자들에게 최대한 빨리 연락하지 못하고 있지만, 그는 우리가 최고의 인재를 채용하길 원한다"와 같은 문제 말이죠 .
- B3 전략적 대응: 인공 지능과 자동화로 업무 환경이 진화함에 따라, 우리 경영진을 지원하고 그들에게 꾸준한 지침을 제공하여 그들이 적응하고 우리 회사가 적응할 수 있도록 도울 수 있는 사람들이 필요합니다.
- 수치 주장: Zapier에서 기술 지원팀으로 시작하여 약 3년 전에 임원 지원팀으로 전환했습니다 .
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/How_Executive_Assistants_Drive_Strategic_Impact_with_AI__-gGwrSPc3tA.md`

**449. [How Orium’s AI Playbook Turned Complexity into 5x Growth | Agents of Scale](https://www.youtube.com/watch?v=5st7XEHY_pA)** — Zapier · 에이전트·개발도구 · US · 2025-11 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B3 전략 대응, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: [music] There's one thing that you was an unassalable advantage that's just gone now. Um, but there's another thing that was never possible that's possible. And your job is to figure that out before your competitors do. …
- B1 디지털·AI 기술의 활용: Um, and I think the same is true like when you're when you're thinking about the agentic infrastructure in your business, how you're approaching the problem, thinking about composability, knowing that you're going to want to fine-tune it, curate it, iterate it…
- B4 가치네트워크·생태계: But I think what agency is solving is one of the more interesting ones for me that that's getting less coverage but really will be what's required to get proper agent ecosystems working.
- 수치 주장: What we're pushing is how do we make sure that we start to open up more agent to agent use cases, agent to system use cases to do it sooner and to do it in a way once again that kind of within 12 months or so um we've got kind of these real productized availab…
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 파인튜닝·학습 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/How_Orium’s_AI_Playbook_Turned_Complexity_into_5x_Growth_Age__5st7XEHY_pA.md`

**450. [The New Creative Muse: Leveraging AI in Design, Writing, and Storytelling](https://www.youtube.com/watch?v=-VG_jT-aVtc)** — Zapier · 에이전트·개발도구 · US · 2025-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽
- 개요: 여러분, 안녕하세요. 저는 Zapier의 선임 웨비나 프로듀서인 알리시아 스미스입니다. 오늘 행사에 오신 것을 환영합니다. 이번 행사에서는 디자인과 스토리텔링에 AI를 활용한 새로운 창의적 영감을 소개합니다 . 보시 다시피, Zapier, Spotify, Shopify, Canva 등에서 온 정말 훌륭한 사람들과 브랜드들이 여기에 있습니다. 잠시 후 그들에 대해 더 자세히 들어보실 수 있지만…
- B4 가치네트워크·생태계: 제품 생산 같은 업무를 아웃소싱할수록 창의적인 활동에 더 많은 시간을 할애할 수 있기 때문이죠.
- B7 성과: 운영효율: 저희가 발견한 것은 많은 판매자들이 AI를 단순히 기본적인 생산성 향상 작업, 즉 주문 처리, 광고, 마케팅, 제품 설명, SEO 및 텍스트 작성 등에만 사용하는 것이 아니라, 비즈니스 계획 수립을 돕는 동반자처럼 활용하기 시작했다는 것입니다.
- 수치 주장: 여러 팀과 프로세스에 걸쳐 AI를 통합하고 실험 및 시범 운영을 통해 AI 도구를 테스트하는 단계가 43% 정도 진행된 것 같습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/The_New_Creative_Muse_Leveraging_AI_in_Design,_Writing,_and___-VG_jT-aVtc.md`

**451. [Zapier's Big AI Plans for 2026 Revealed! - Leadership, Culture, Tools, Governance](https://www.youtube.com/watch?v=EfHm1Qjztd0)** — Zapier · 에이전트·개발도구 · US · 2025-11 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B8 부정 성과
- 개요: 네, 정말 훌륭해요. 안녕하세요, 환영합니다. Zapier의 주간 전체 회의에 제시간에 참여해주신 여러분을 환영합니다 . 우리는 보통 첫 1 분 동안 전 세계에서 온 사람들이 차례로 들어오도록 합니다. Zapier에 대한 재밌는 사실 하나 알려드릴게요 . 매우 국제적인 팀이고, 전원이 원격으로 근무하는 팀입니다. 저희는 매주 전체 회의를 하는데, 42개국에서 800명이 접속합니다. 그리고 오…
- B5 리더십·CDO/CAIO: 일반적으로, 음, 인적 자원 측면은 다소 애매하게 느껴지고 마땅히 받아야 할 관심을 받지 못하는 경우가 많지만, 이 슬라이드에 있는 내용 중 제가 가장 확신하는 것은 리더십, 인재, 그리고 문화라는 요소가 세 번째와 네 번째 요소만큼이나 중요하다는 것입니다.
- B1 디지털·AI 기술의 활용: 바로 이 날, 당시 저희 인사 책임자였던 브랜든(이 통화에 함께 참여하셨던 분)이 저에게 Zapier에서 현재 AI 에이전트라고 불리는 Central을 관리자 역량 강화 사례에 활용하는 영상을 보여주셨습니다.
- 수치 주장: 2023년에 GPD4가 출시됐을 당시 Zapier에 계셨던 분들은요.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 코딩 에이전트
- 원문: `transcripts/channels/Zapier/Zapier's_Big_AI_Plans_for_2026_Revealed!_-_Leadership,_Cultu__EfHm1Qjztd0.md`

**452. [2026 SEO Strategy: How Marketers Win The New LLM Search Game](https://www.youtube.com/watch?v=BV_ZtkqyzkM)** — Zapier · 에이전트·개발도구 · US · 2025-12 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 네, 여러분 좋은 아침입니다. 안녕하세요. 12월의 소중한 시간을 내주셔서 정말 기쁩니다 . 제 생각에 트레버 씨도 저와 같으시다면, 연말 계획을 세우고 마무리하는 시기이고, 12월은 미국 공휴일 두 개 때문에 항상 정신없는 시기일 겁니다 . 시간 내주셔서 감사합니다. 새로운 LLM 검색 게임에 대해 이야기하게 되어 기쁩니다. AEO, GEO, 그리고 그런 것들에 대해 이야기해 봅시다 . 자…
- B1 디지털·AI 기술의 활용: 그리고 특히 LLM(법학 석사) 과정에서 흥미로운 점 중 하나는, 그들이 마치 표면적인 정보 조각처럼 연구하고 있다는 것을 알고 있지만, 결국에는 마지막으로 검색했을 때 수집한 정보를 기록으로 남길 수 있게 될 것이라는 점입니다 .
- B2 파괴: 경쟁구도: 경쟁사 랜딩 페이지는 내용이 너무 간결한 경우가 많은데, 그런 경쟁사 콘텐츠와는 달리 좀 더 긴 형식의 포지셔닝을 실험해볼 수 있는 기회를 줬다고 생각해요.
- 수치 주장: 예전에는 브랜드가 문제 해결 평가 등 여러 평가 기준을 거치기 위해 수많은 클릭과 트래픽이 필요했지만, 이제는 2~4시간 정도로 단축되었습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/channels/Zapier/2026_SEO_Strategy_How_Marketers_Win_The_New_LLM_Search_Game__BV_ZtkqyzkM.md`

**453. [Defining AI Fluency: A Fireside Chat With The Executives](https://www.youtube.com/watch?v=Rq1lzDDfTrU)** — Zapier · 에이전트·개발도구 · US · 2025-12 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: Welcome, welcome from around the world. We're going to give it about a minute as folks file in, but we are glad you are here. If uh you intended to be in a ask me anything fireside chat with Brandon and Keith on the topi…
- B1 디지털·AI 기술의 활용: So in recruiting, Zapier is now offering as an option for candidates for certain jobs uh the choice between interview and this is very this has been the first live interview not all interviews just the first one the opportunity to interview with a human recrui…
- B7 성과: 운영효율: Um, I think when it comes to any tool or maybe like a new workflow that you or the team is building against, how do you all think about ROI?
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/Defining_AI_Fluency_A_Fireside_Chat_With_The_Executives__Rq1lzDDfTrU.md`

**454. [From First Startup to AI-Powered Scale: Wes Schroll on Building Fetch | Agents of Scale Podcast](https://www.youtube.com/watch?v=HxortsDnCm8)** — Zapier · 에이전트·개발도구 · US · 2026-01 · en · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B6 장벽, B8 부정 성과
- 개요: I kept using the tools more and more and I was like a day is not even enough let's shut down the company for a whole week and uh no external meetings literally everyone and the company was 1,50 employees at the time so I…
- B1 디지털·AI 기술의 활용: Um uh but um you know I think you you have something like large language models come along, chat GPT comes along and I've noticed you have been fairly fast and outspoken about your desire to make sure that Fetch is taking advantage of the transformation.
- B5 리더십·CDO/CAIO: Um I I took that as really good feedback that we as a leadership team and as an organization have failed in making our perspective clear and in you know if someone had to fill in the blanks themselves.
- 수치 주장: Therefore, it has to only be available for our business." The reality is, and everyone launches their lo their loyalty programs, what ends up happening, fast forward a couple years, is they get a ton of people acquired onto the program, but who remains really …
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Zapier/From_First_Startup_to_AI-Powered_Scale_Wes_Schroll_on_Buildi__HxortsDnCm8.md`

**455. [Is SaaS really dead? Dharmesh Shah from HubSpot on AI, Vibe-Coding & the Future of Work](https://www.youtube.com/watch?v=R5MKxU5biPo)** — Zapier · 에이전트·개발도구 · US · 2026-02 · en · 4/8블록 · `ax_adjacent`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: We have all the resources in the world. The number of SAS apps that we have replaced as a result of all this kind of army of resources and talent that we have, we're a software company uh through and through is exactly z…
- B1 디지털·AI 기술의 활용: For are there particular tools are you using for simulation or is this like hey I'm just going back and forth with chat GPT asking it to uh &gt;&gt; it's it's uh it's combination of GPT and but I have like my own AL because I like to do a lot of these things o…
- B2 파괴: 소비자 행동·기대: Um so it has taketh away in terms of top of funnel traffic but what it what it gives us is the ability to personalize the information that we make available at the point the person does show up on our website or in in in in our funnel uh because we have the ab…
- 수치 주장: uh his early early use case um with AI and he's been exposed to it uh super early um outside of the normal things um like writing and whatnot but it's um was uh building a a textbased uh uh video game similar to if you know you've been around like you know Zor…
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 에이전트 프레임워크 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/Is_SaaS_really_dead_Dharmesh_Shah_from_HubSpot_on_AI,_Vibe-C__R5MKxU5biPo.md`

**456. [Getting back to startup speed took a cultural reset - and it worked!](https://www.youtube.com/watch?v=LHd1plfMvXA)** — Zapier · 에이전트·개발도구 · US · 2026-03 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 팀 규모가 두 배 이상 늘어났으니 배송 속도도 훨씬 빨라질 거라고 예상했었어요. 우리는 그렇게 하지 않았습니다. 우리는 여전히 정말, 정말 느리게 가고 있었다. [음악] 그래서 우리는 ' 이게 사실 문화적인 문제일 수도 있지 않을까?'라는 생각을 하기 시작했어요. 안녕하세요, 여러분. Agents of Scale에 다시 오신 것을 환영합니다. 이 프로그램에서는 AI를 단순한 유행어에서 핵심 …
- B3 전략적 대응: 우리는 로드맵을 논의하기 위해 중요한 회의를 열곤 했는데, 저를 비롯한 브렌던과 다른 고위 리더들은 회의 전에 " 우리가 가진 로드맵이 정말 올바른 방향으로 가고 있는지 , 정말 중요한 내용인지 확인하기 위해 어떤 가장 어려운 질문을 할 수 있을까?"라고 스스로에게 질문하며 준비했습니다.
- B2 파괴: 경쟁구도: 우리의 목표는 "고객들이 매우 좋은 상태를 유지하고 깊은 신뢰를 갖게 만들어, 만약 다른 경쟁사를 이용해보고 만족스럽지 않더라도 다시 돌아오도록 하자 "는 것이었습니다.
- 수치 주장: 제가 봤던 로드맵에는 특정 기능들이 6개월 후에 출시될 예정이라고 되어 있었는데, 실제로는 2주 만에 출시되었거든요.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/channels/Zapier/Getting_back_to_startup_speed_took_a_cultural_reset_-_and_it__LHd1plfMvXA.md`

**457. [Leading through AI: How top executives are turning AI mandates into real business transformation](https://www.youtube.com/watch?v=g6q02hUd_Wc)** — Zapier · 에이전트·개발도구 · US · 2026-03 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 전 세계 여러분, Zapier와 Nerd Wallet, Door Dash, Web Flow라는 세 개의 대표적인 기업의 리더들이 함께하는 오늘 행사에 오신 것을 환영합니다. 믿기 ​​어려우시겠지만, 오늘 우리 모두, 전 세계 수백 명, 아니 수천 명이 한자리에 모여 인공지능 시대에 진정으로 앞장서 나가는 방법에 대해 진솔한 이야기를 나누고자 합니다 . 실제 리더들은 어떻게 인공 지능 관련 요…
- B1 디지털·AI 기술의 활용: 이러한 프로그램 중 일부는 오늘날 리더들과의 폭넓은 대화에서부터, 참가자들이 직접 AI 에이전트를 개발하거나 차세대 AI 에이전트를 구축하거나, 조직 내에서 AI를 더욱 효과적으로 활용하는 데 사용할 수 있는 프레임워크를 개발하는 실제 빌더 워크숍에 이르기까지 다양합니다.
- B5 리더십·CDO/CAIO: 음, 리더십 관점에서 생각해 보면, 우리 모두는 새로운 업무 방식으로 나아가기 위한 다리를 건설하려고 노력하고 있지만, 시간이 걸릴 것이고, 그동안 우리는 마치 작은 보행자 다리를 놓거나 다른 방법을 통해 진전을 이루어 나가야 할 것입니다.
- 수치 주장: 아시다시피 Zapier는 3년 넘게 AI 여정을 걸어왔고, 그중 처음 2년은 주로 AI 도입에 집중했습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/Leading_through_AI_How_top_executives_are_turning_AI_mandate__g6q02hUd_Wc.md`

**458. [No Lanes: How Claire Vo Runs an AI-Native Company on Her Own Terms](https://www.youtube.com/watch?v=_Wg2oTfwb4g)** — Zapier · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 오프사이트 음악 워크숍을 열어서 하루 종일 팀을 나눠서 뭔가를 만들어보는 걸 좋아해요. 그리고 저는 그것이 바로 재미를 불러일으킬 수 있다고 생각합니다. 이는 어려운 기술들을 익히는 데 도움이 될 수 있습니다. [음악] 음, 그리고 이건 경영진이 이것이 팀이나 회사에 어떤 영향을 미칠 수 있는지에 대해 대화를 시작하기에 좋은 방법입니다. [음악] [음악] 좋아요. 안녕하세요 여러분, Agen…
- B1 디지털·AI 기술의 활용: 그래서 생성형 AI가 본격적으로 인기를 얻기 시작했고, ChatGPT도 한 2년 전에 인기를 끌었죠.
- B3 전략적 대응: AI에만 국한된 건 아닐 수도 있지만, 저는 요즘 다시 한번 '직접 관여하는 경영진', 즉 앞을 내다보면서도 내부적으로는 CEO가 중요한 시대가 왔다고 생각합니다.
- 수치 주장: 왜냐하면, 이 팟캐스트가 특별한 관점을 제시하는 이유는, 모델 학습 및 개발 과정, 최첨단 연구 및 기술에 대해 심도 있게 다루는 팟캐스트는 많지만, 저는 여러분을 30 분 동안 편안하게 앉혀놓고 " 실제로 따라 할 수 있는, 삶을 더 편하게 만들어 줄 세 가지 방법"을 알려드리려고 합니다.
- 교량: — · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/No_Lanes_How_Claire_Vo_Runs_an_AI-Native_Company_on_Her_Own____Wg2oTfwb4g.md`

**459. [OpenClaw, Claude, Zapier MCP: Build Agents Safely & Easily | WEBINAR](https://www.youtube.com/watch?v=WPwXCwlTdz4)** — Zapier · 에이전트·개발도구 · US · 2026-03 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 안녕하세요 여러분, Open Claw, Claude, Zapier MCP를 활용하여 안전하고 쉽게 AI 에이전트를 구축하는 방법을 다룬 웨비나에 오신 것을 환영합니다 . 제 이름은 맷 ​​브라운입니다. 저는 Zapier의 커뮤니티 팀에서 일하고 있습니다. 지금은 Creator Magic의 마이크 러셀 씨가 가상 무대에 함께해 주셨습니다. 오늘 세션을 여러분과 함께 진행하게 되어 매우 기쁩니다…
- B1 디지털·AI 기술의 활용: 제 API 키를 모두에게 보여주고 싶진 않고, 어차피 이번 데모 이후에는 바꿀 가능성이 높지만, 어쨌든 복사해서 붙여넣었더니 Open Claude가 이제 당신이 이 Anthropic API 키를 사용할 거라는 걸 알게 됐습니다.
- B8 부정 성과: 보안·프라이버시: 그러니까, 맞다면 이건 프롬프트 인젝션이고 자동화를 중지시켜서 Open Claude에 도달하지 않도록 하는 것이고, 틀렸다면 프롬프트 인젝션이 아니므로 다음으로 넘어가는 것입니다.
- 수치 주장: 만약 이러한 주제에 관심이 있고 AI를 실제로 활용하고 싶지만 어디서부터 시작해야 할지, 다음 단계는 무엇인지 잘 모르겠다면, 저희 팀과 30분 워크숍을 진행해 드립니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/OpenClaw,_Claude,_Zapier_MCP_Build_Agents_Safely_&_Easily_WE__WPwXCwlTdz4.md`

**460. [How Miro's talent team designs & ships HR systems employees actually use with Zapier](https://www.youtube.com/watch?v=NuSnxrdODUE)** — Zapier · 에이전트·개발도구 · US · 2026-04 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 → B8 부정 성과 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과
- 개요: 여러분, 안녕하세요. 오늘 함께해 주셔서 감사합니다 . 잠시 후 시작할 예정이지만, 어디에서 오시든 모두 참여하실 수 있도록 하겠습니다 . 그러고 보니, 어디에서 접속하시는지 채팅창에 알려주세요. 저희는 시청자 여러분이 어디 에서 오셨는지, 그리고 오늘 어디에서 저희 방송에 참여하고 계신지 듣는 것을 매우 좋아합니다 . 아침 인사인지, 오후 인사인지, 밤 인사인지, 한밤중인지, 저는 잘 모르…
- B5 직무·역량 변화: 음, 제가 경험한 바로는, 특히 최근에 구축한 새로운 추천 워크플로우처럼, 가장 큰 효과를 본 구축 사례는 채용 담당자 와 추천인 모두가 전체 워크플로우를 Slack 내에서 진행할 수 있도록 한 것입니다.
- B2 파괴: 소비자 행동·기대: 닉, 그리고 에밀리 같은 분들, 여러분은 뛰어난 분석력과 사용자 경험을 고려하는 능력으로 우리의 모든 HR 프로세스를 혁신하는 데 큰 도움을 주고 계십니다.
- 수치 주장: 저는 이곳에서 약 5년 동안 일해왔고, 지난 18개월 동안은 인공지능과 자동화라는 흥미로운 분야에 집중해왔습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/channels/Zapier/How_Miro's_talent_team_designs_&_ships_HR_systems_employees___NuSnxrdODUE.md`

**461. [Guru's Rick Nucci on Building AI Your Team Can Trust](https://www.youtube.com/watch?v=YaSvETxH2jY)** — Zapier · 에이전트·개발도구 · US · 2026-05 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B2 파괴, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 당연한 말이지만, 많은 사람들이 간과하는 점은 이러한 모델들이 놀라울 정도로 뛰어나지만, 본질적으로 귀사에 대해 아무것도 모른다는 것입니다 . 안녕하세요 여러분. Agents of Scale에 다시 오신 것을 환영합니다 . 이 프로그램은 인공지능을 단순한 유행어에서 핵심 기술로 바꾸고 있는 경영진들과 제가 직접 만나 이야기를 나누는 프로그램입니다 . 저는 웨이드 포스터입니다. 오늘의 게스트는…
- B1 디지털·AI 기술의 활용: 우리는 당시에는 지금에 비하면 아주 사소했던 머신러닝 모델이 " 넷스위트와 세일즈포스를 연결하는 경우, 이미 수백 번도 더 봤듯이, 예를 들어 마감된 영업 기회를 가져와 세일즈 포스에 고객 레코드를 생성해야 하는 경우, 더 이상 누구도 데이터 매핑을 직접 그릴 필요가 없습니다.
- B3 전략적 대응: 만약 제가 회사 경영진이 저를 대체할 기회를 찾고 있다고 생각한다면, 제가 개발한 AI 기술을 전파하고 사람들에게 제가 얼마나 대단한지 보여주고 싶어 할까요 ?
- 수치 주장: 릭은 업계를 선도하는 소프트웨어 개발 분야에서 20년 이상의 경력을 보유하고 있습니다.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/Zapier/Guru's_Rick_Nucci_on_Building_AI_Your_Team_Can_Trust__YaSvETxH2jY.md`

**462. [Brand Is Back: Guy Yalif on Marketing in the Agent Era](https://www.youtube.com/watch?v=tw8cpXGg41I)** — Zapier · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 셀프 서비스 가입의 8%는 LLM 의 추천을 받은 사람들이었으며 , LLM을 통해 유입되었을 가능성이 있는 급증이나 기타 트래픽은 제외한 수치입니다 . 그건 8%였고, 그 트래픽은 구매 유입 경로의 맨 아래쪽으로 향하는 트래픽이었습니다. 전환율이 6%가 아니라 6배, 즉 브랜드가 없는 SEO 트래픽보다 6배 더 높았습니다. 이는 공정한 비교라고 생각합니다. 안녕하세요 여러분, Agents o…
- B1 디지털·AI 기술의 활용: 이제 ChatGPT, Claude, Gemini 또는 이와 유사한 도구들을 사용하여 네다섯 개의 후속 질문을 하고, 단 하나의 제품에 대해서만 묻는 것이 아니라, 수십 개의 제품, 또는 인터넷에서 찾을 수 있는 만큼 많은 제품에 대해 질문합니다 .
- B7 성과: 운영효율: 물론 사업 에서 투자 수익률(ROI) 측면에서 긍정적인 부분이 많지만 , 아직 손익계산서에는 반영되지 않습니다 .
- 수치 주장: 전환율이 6%가 아니라 6배, 즉 브랜드가 없는 SEO 트래픽보다 6배 더 높았습니다.
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 프로토콜·표준
- 원문: `transcripts/channels/Zapier/Brand_Is_Back_Guy_Yalif_on_Marketing_in_the_Agent_Era__tw8cpXGg41I.md`

**463. [Eric Ries on Vibe Coding and Building Incorruptible Companies](https://www.youtube.com/watch?v=Qs33r-Nreb8)** — Zapier · 에이전트·개발도구 · US · 2026-06 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B6 장벽, B8 부정 성과
- 개요: 소셜 미디어에 들어가 보면 CEO들을 비롯한 유명 인사들이 자신이 얼마나 생산적인지 끊임없이 자랑하는 모습을 볼 수 있을 거예요 . 그들은 20명의 코딩 에이전트를 고용해서 4천만 줄 정도의 코드를 작성했다고 하더군요. [음악] 잘 살펴보시면, 그들이 들려주는 이야기들 중에는 고객이 어떤 행동을 하는 장면은 하나도 없다는 것을 알 수 있을 겁니다. [음악] 안녕하세요 여러분, Agents o…
- B1 디지털·AI 기술의 활용: 지금은 가상이 아니라 지금 이 순간 제 컴퓨터에는 1개, 2개, 3개, 4개, 5개, 6개, 7개, 아니 8개의 클라우드 코드 세션이 동시에 실행되고 있어요.
- B3 전략적 대응: 실제로 책에서 트위터 이사회에 대해 잘 아는 친구의 말을 인용했는데, 그는 "그들은 거래를 하고 싶어 하지 않았어."라고 했습니다.
- 수치 주장: 약 15년 ​​전, 당신은 스타트업을 구축하는 새로운 사고방식인 '린 스타트업'을 대중화시켰습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/Eric_Ries_on_Vibe_Coding_and_Building_Incorruptible_Companie__Qs33r-Nreb8.md`

**464. [Claude /connected: Share skills with your team | Build-Along Workshop](https://www.youtube.com/watch?v=xTmn8jcnzdM)** — Zapier · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B5 구조 변화 · 빠짐: B4 가치창출 경로, B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요 여러분. 3주차에 오신 것을 환영합니다. 해냈군요. 3주 중 3주차입니다. 사람들이 몰려들기 시작하면, 흔히 하는 어색한 분위기 조성 멘트가 이어집니다. 이제는 익숙해졌을 거라고 생각해요 . 채팅창에 올릴게요. 지난 48시간 동안 먹어본 것 중 가장 맛있었던 음식은 무엇인가요 ? 매번 그렇듯이 의도적으로 포괄적인 것입니다 . 먹은 음식 때문일 수도 있어요. 마신 음료, 읽은 책, …
- B1 디지털·AI 기술의 활용: 사실 방금 통화하기 전에 저희 팀에서 제작한 데모 영상을 봤는데, 클라우드에 연결된 상태에서도 Chat GBT, Cursor 등 다양한 앱에 연결할 수 있는 하나의 MCP 서버를 어떻게 활용할 수 있는지 보여주는 내용이었습니다.
- B5 직무·역량 변화: 팀용 워크스페이스가 이미 있다면 , 예를 들어 제가 Zapier의 채용팀에 있다고 가정하면, 이미 채용 Google 워크스페이스가 있을 거예요.
- 수치 주장: 우리는 AI 자동화에 대해 이야기했고, 지난 2주 동안 Claude를 사용해서 앱에 접근하고 작업을 수행하는 방법에 대해 이야기했습니다 .
- 교량: — · 기술: LLM 모델 · 프로토콜·표준 · 코딩 에이전트
- 원문: `transcripts/channels/Zapier/Claude_connected_Share_skills_with_your_team_Build-Along_Wor__xTmn8jcnzdM.md`

**465. [Gong's Amit Bendov on Powering Your Company Brain](https://www.youtube.com/watch?v=YEbksTLOfjs)** — Zapier · 에이전트·개발도구 · US · 2026-07 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 저는 개인적으로 몇 년 동안 CRM에 로그인한 적이 없습니다 . 제가 할 일은 그냥 " 어, 지금 Zapier 상태가 어떤가요?"라고 물어보는 것뿐이고, 그러면 모든 정보를 알려줍니다. [음악] 오늘 저의 게스트는 아미트 빈도프입니다. 그는 Gong의 공동 창립자이자 CEO입니다. 이제 경기가 시작되자 그는 많은 사람들이 엉뚱하다고 생각하는 아이디어에 내기를 걸었습니다. 그는 거래의 진실은 …
- B7 성과: 운영효율: 그래서 궁금한 점은, 영업 사원의 생산성 향상을 살펴볼 때, 특히 GONG을 도입했을 때 가장 큰 격차나 가장 큰 기회가 어디에 있다고 생각하시는지입니다.
- B1 디지털·AI 기술의 활용: 아시다시피, 제가 당신이 하신 말씀 중에 클라우드가 IT 혁명이었다면 AI는 훨씬 더 업무 혁명에 가깝다는 말씀이 있었습니다.
- 수치 주장: 2016년에 Gong을 발표했을 때 제가 " 이건 20년 전 CRM을 도입한 이후 최고의 발명품입니다"라고 말했는데, 그때는 다들 "아, 그래.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/Zapier/Gong's_Amit_Bendov_on_Powering_Your_Company_Brain__YEbksTLOfjs.md`

**466. [The Good, the Bad, and the Ugly: How Zapier Is Building an AI-First GTM Team](https://www.youtube.com/watch?v=tqnLffBM-og)** — Zapier · 에이전트·개발도구 · US · 2026-07 · en · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: Welcome to today's webinar. Before we get started, let's go over a few quick housekeeping items. First, yes, we've had a few people ask, this webinar is being recorded. You can access the recording at any time after we c…
- B7 성과: 운영효율: Um the first one I wanted to hit was from Aaron and it was um Sarah, why don't you like time savings as an ROI met metric?
- B1 디지털·AI 기술의 활용: Uh Sarah, there's a good um question in the chat here of just maybe just underlining a little bit more what makes this workflow agentic, your choice to use agents versus a traditional Zap.
- 수치 주장: If you saved me time, I would probably spend the extra 30 minutes on Pinterest.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 검색·RAG · 파인튜닝·학습 · 코딩 에이전트 · 거버넌스·평가 도구
- 원문: `transcripts/channels/Zapier/The_Good,_the_Bad,_and_the_Ugly_How_Zapier_Is_Building_an_AI__tqnLffBM-og.md`

---

## Zoox


**467. [10 Years of Zoox. Reflections and Predictions.](https://www.youtube.com/watch?v=DYcujjMs3Uo)** — Zoox · 물리 AI·자율주행 · US · 2024-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하세요 여러분, 함께해 주셔서 감사합니다. 저는 Zook의 CEO인 아이샤 안이고, 이쪽은 공동 창업자이자 CTO인 제시 레벤슨입니다. 그는 거의 처음부터 함께해 왔죠. 네, 맞아요. Zook이 10주년을 맞이했네요! 믿기시나요? 네, 어쨌든, 지난 10년간 회사가 걸어온 여정에 대해 이야기해 보려고 합니다. 가장 큰 성공과 어려움, 교훈, 그리고 앞으로의 전망에 대해서도 이야기 나눠볼 …
- B5 직무·역량 변화: 저희 팀에 합류하고 싶으신 분들은 화면에 있는 QR 코드를 통해 Courier 페이지에서 채용 공고를 확인하시거나 Zuk 웹사이트를 방문해 주세요.
- B3 전략적 대응: 어, 하지만 휠체어 종류도 다양하고, 제공해야 할 종류도 여러 가지가 있기 때문에 저희 로드맵에 포함되어 있고, 저희가 분명히 고려하고 있는 부분입니다.
- 수치 주장: 그래서 저희 Z는 지난 10년 동안 자동차의 다음 세대라고 할 수 있는 로보택시를 개발해 왔습니다.
- 교량: — · 기술: —
- 원문: `transcripts/channels/Zoox/10_Years_of_Zoox._Reflections_and_Predictions.__DYcujjMs3Uo.md`

---

## a16z and MTS


**468. [Aaron Levie on AI Adoption and Enterprise Workflows | The a16z Show](https://www.youtube.com/watch?v=dvVbA9OcBqs)** — a16z and MTS · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 그래서 이사회는 CEO에게 갑니다. 이사회는 뭐라고 하나요? 우리는 더 많은 인공지능이 필요합니다. 그럼 CEO는 뭐라고 말하나요? 아, 그래요. 인공지능 분야를 더 깊이 연구하기 위해 컨설턴트를 고용할 생각입니다. 그리고 그들은 아무도 작동 방식을 모르는 중앙 집중식 프로젝트를 가지고 있습니다. 그들은 운영 방식을 제대로 조율하지 못했고, 결국 실패할 것이다. 코드를 많이 작성할수록 엔지니…
- B1 디지털·AI 기술의 활용: AI 분야의 변화 속도가 워낙 빠르다 보니, 연구실들이 서로 빠르게 앞서나가고 있지만, 에이전트를 배포하고 작동시키는 방식, 에이전트가 컴퓨터 내부에 있어야 하는지 외부에 있어야 하는지, 클라우드에서 실행해야 하는지, 호스팅되어야 하는지, 어떤 도구에 접근할 수 있어야 하는지 등 패러다임이 완전히 일치하지 않는 놀라운 현상이 나타나고 있습니다.
- B3 전략적 대응: CEO나 이사회, 경영진이라면 누구나 이 부분을 파악하려고 애쓰고 있을 것이고, 실리콘 밸리에서 온갖 이야기를 쏟아내기 때문에 혼란스러워하고 있을 겁니다.
- 수치 주장: 그리고 인공지능과 에이전트가 해결할 수 없는, 그 어떤 것도 해결할 수 없는 문제는, 직원 수가 1,000명 이상이거나 10년 이상 된 기업은 통합될 준비가 된 거대한 시스템을 그대로 보유하고 있다는 점입니다 .
- 교량: Avenue 1 동적역량 · 기술: LLM 모델 · 파인튜닝·학습 · 코딩 에이전트
- 원문: `transcripts/2026-07-26/Aaron_Levie_on_AI_Adoption_and_Enterprise_Workflows_The_a16z__dvVbA9OcBqs.md`

---

## kakao tech


**469. [[ifkakao2021] Daum Mail Terraforming:  다음 메일 백엔드 레거시 개편기](https://www.youtube.com/watch?v=r2t4h3qMXzw)** — kakao tech · 수요기업·기타 · KR · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B4 가치창출 경로 → B6 장벽 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B5 구조 변화, B7 긍정 성과
- 개요: 안녕하세요. 저는 카카오에서 메일 서비스의 백핸드 개발자로 일하고 있는 오엔이라고 합니다. 저는 오늘이 세션에서 다음 매일 백엔드 서비스들 중 레거 시스템에 일부를 개편한 과정을 다음 메일 테라포밍이라는 타이틀로 소개하고자 합니다. 테라포밍이란 사실 우주 개척과 관련된 용어인데요. 지구 외에 다른 천체에 지구생물이 살 수 있는 환경과 생태계를 구축하고 이주 계획을 수립하는 것을 말합니다. 저…
- B6 장벽: 관성·저항: 이렇게 구현된 레거시 서포트 게이트웨이는 기존 레거시 서비스의 인터페이스를 그대로 호환하기 때문에 기존 서비스들은 요청 도메인만 변경하는 정도로 게이트웨이를 거쳐 정보를 요청할 수 있었습니다.
- B1 디지털·AI 기술의 활용: 일단 최초에 이렇게 사용자 정보가 필요한 클라이언트들이 각자 서비스들에 직접 요청하고 있던 그 기존의 그림에서 저희는 첫 번째 단계로 사용자 정보를 통일된 인터페이스로 제공하는 API 게이트웨이를 기존의 사용자 정보 서비스들 앞에 추가하였습니다.
- 수치 주장: 저희는 개발자인 우리가 레거시 서비스를 개편하여 신규 서비스로 이건 1년의 과정이 이러한 테라포밍에 비유해 볼 수 있다고 생각했습니다.
- 교량: Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/channels/kakao_tech/[ifkakao2021]_Daum_Mail_Terraforming_다음_메일_백엔드_레__r2t4h3qMXzw.md`

**470. [[ifkakao2021] Knowledge Graph for Enterprise](https://www.youtube.com/watch?v=fMV_TRN5StI)** — kakao tech · 수요기업·기타 · KR · 2026-06 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과, B8 부정 성과
- 개요: 안녕하세요. 카카오 엔터프라이즈 지식 그래프 팀 케인이라고 합니다. 지식 그래프가 이제는 어느 정도 대중화된 용어라고 생각하지만 아직은 생소하신 분들도 많을 거라고 생각해요. 이번 세션에서는 지식 그래프의 특징과 관련 개념들을 간략히 설명드리고 기업에서 지식 그래프가 어떻게 쓰이는지 엔터프라이즈 난리즈 그래프의 필요성과 사례들을 소개해 드리겠습니다. 그리고 마지막으로는 저희가 어떤 지식 그래…
- B6 장벽: 관성·저항: 데이터 사일로의 케이지 트랜스포메이션 과정을 통해이 케이지가 구축되면 회사 데이터가 서로 연결되어 관계 중심으로 전체를 조망할 수 있게 됩니다.
- B1 디지털·AI 기술의 활용: 그리고 카카오 엔터프레즈의 강점인 검색과 AI 기술을 결합해서 KBQA와 패턴 Q를 이용해 자연어 지리로 지식 그래프 안의 관계와 정보를 쉽게 찾을 수 있고 머신 러닝 기반 출론 및 분석 기술을 연구 플랫폼에서 다양한 분석 결과와 인사이트를 제공합니다.
- 수치 주장: 저희는 2019년까지 B2C 서비스를 위해 검색과 카카오 미니에서 사용되는 지식 그래프 플랫폼을 개발했고 카카오가 보유한 방대한 콘텐츠로 지식 그리프를 구축했습니다.
- 교량: — · 기술: 온톨로지·데이터계층
- 원문: `transcripts/channels/kakao_tech/[ifkakao2021]_Knowledge_Graph_for_Enterprise__fMV_TRN5StI.md`

---

## 김작가 TV


**471. [상위 1%만 알고 있는 AI 활용법, 삶의 질이 10배 상승합니다 (김상윤 교수)](https://www.youtube.com/watch?v=AsQUoda0wB0)** — 김작가 TV · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B3 전략 대응, B4 가치창출 경로, B6 장벽
- 개요: 지금 현재 현존하는 생성형 AI는 거대 언어 모델이라는 것을 기반으로 하는데 여러분들이 질문을 했을 때 내가 입력한 단어 하나하나와 관련성이 높은 단어들을 자신만의 출론 방식으로 조합해 가지고 문장을 만들어내는 형태예요. 이걸 다르게 표현하면은 AI는 지식을 기억하고 있다라고 볼 수가 없고요. 그때그때 질문했을 때 그 요구 사항과 관련성이 높은 답들을 만들어 내 주는 거거든요. 그러면 무슨 …
- B8 부정 성과: 보안·프라이버시: 아 이거 시청자분도 할 수 있으니까 이런 거 직접 한번 해 봐야지 AI가 어떻게 시에 쓰이고 있는지 그걸 알 수 있을 것 같은데 그럼 AI가 만든 음악도 저작권 등록하거나 뭐 상업 자용도 가능한 건가요?
- B1 디지털·AI 기술의 활용: 지금 현재 현존하는 생성형 AI는 거대 언어 모델이라는 것을 기반으로 하는데 여러분들이 질문을 했을 때 내가 입력한 단어 하나하나와 관련성이 높은 단어들을 자신만의 출론 방식으로 조합해 가지고 문장을 만들어내는 형태예요.
- 수치 주장: 오픈어의 채치가 등장하고 사람들이 반응이 폭발적으로 확대된 것은 한 3개월 정도 직후였습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/2026-08-03/상위_1%만_알고_있는_AI_활용법,_삶의_질이_10배_상승합니다_(김상윤_교수)__AsQUoda0wB0.md`

---

## 매경 월가월부


**472. [AI 랠리 2라운드…승부는 실적ㅣ스페이스X 첫 실적 발표…머스크 뭐라고 말할까ㅣ트럼프 "일본 돕겠다"…엔화 방어 나섰다ㅣ홍혜진의 뉴욕브리핑](https://www.youtube.com/watch?v=FvQF06brkAQ)** — 매경 월가월부 · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_adjacent`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 예, 안녕하세요. 뉴욕 브리핑 홍혜진 기자입니다. 오늘부터 매일 경제 월가 월부 뉴욕 특파원으로 인사드리게 됐습니다. 월요일부터 목요일까지 저녁 10시 15분에는 미국 증시 계장을 앞두고 시장의 주요 흐름을 정리하는 뉴욕 브리핑으로 찾아뵙고요. 미국에는 금요일에는 미국 경제와 문화를 조금 더 깊이 들여다보는 엄팩 아메리카로 인사드리겠습니다. 귀한 시간 내서 시청해 주시는만큼 미국 시장을 이해…
- B1 디지털·AI 기술의 활용: 그 지난주 빅테크 실적이 AI 투자에 대한 1차 평가였다면 이번 주는 그런 투자 여기가 소프트웨어와 반도체, 클라우드 기업으로 얼마나 확산되고 있는지를 확인하는 2차전 성격의 실적 발표 시간이 될 것으로 보입니다.
- B7 성과: 조직성과: 뭐 비용 관리로 수익성을 방어를 했지만 그 매출 성장세가 아무래도 기대에 못 미쳤다는 평가가 나오고 있습니다.
- 수치 주장: 여기에 또 오팩플러스도 하루 6만, 19만 배럴 증산을 결정하면서 공급 확대 전망까지 더해진 상황입니다.
- 교량: — · 기술: —
- 원문: `transcripts/2026-08-04/AI_랠리_2라운드…승부는_실적ㅣ스페이스X_첫_실적_발표…머스크_뭐라고_말할까ㅣ트럼프_일본_돕겠다…엔화_방어__FvQF06brkAQ.md`

---

## 메타코드M


**473. [The Secret to Successful AI Transition: A Step-by-Step AX Strategy Guide - [Metacode M]](https://www.youtube.com/watch?v=wdqRyiqH_OI)** — 메타코드M · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B3 전략 대응 → B5 구조 변화 → B6 장벽 → B7 긍정 성과 · 빠짐: B1 기술 활용, B2 파괴, B4 가치창출 경로, B8 부정 성과
- 개요: 안녕하십니까. 다음은 파트 2의 세 번째 챕터 AI 전환 추진 전략 방법론에 대해서 설명드리도록 하겠습니다. 성공적인 AX 실을 위해서 세 가지 접근법이고요. 링크로스에서 스몰 스타트, 스몰cess 그다음에 스마트 스케일링 관점에 어 얘기를 조금 더 드리도록 하겠습니다. 들어가기에 앞서서요. 본 챕터에서는 스몰 스타트, 스몰 석세스, 스마트 스케일링의 3단계 방법론에 대해서 설명드리고요. 효…
- B6 장벽: 관성·저항: 그리고 특히 솔루션이 만들어졌을 때 특정부는 적용을 하고 관심이 있는데 조직 저항이나 어 회사 자체에서 저항도가 있을 때는 앞서 말씀드렸던 것처럼 보이 보이시나 종량적인 지표들을 명확하게 전달을 하고 교육이 실습을 통해서 체감이나 익숙하게 되는 부분들을 계속 지속적으로 만드는 것이 중요합니다.
- B3 전략적 대응: 일체 사례는 어 예를 들자면 체포할 때 어 고객을 정성과 정량성유 중력 측정을 사실 하이브리드로 잘 해서 객관적으로 검증하고 투자 의사 결정뿐만 아니라 지속적인 로드맵을 그리는데 굉장히 많은 지지를 받았던 사례로 생각합니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: —
- 원문: `transcripts/2026-07-21/The_Secret_to_Successful_AI_Transition_A_Step-by-Step_AX_Str__wdqRyiqH_OI.md`

---

## 백만사전


**474. [Only 2 employees left, yet... The shocking sign of Google's decline as it loses AI dominance and ...](https://www.youtube.com/watch?v=syU5o1-BPUI)** — 백만사전 · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B5 구조 변화 · 빠짐: B6 장벽, B7 긍정 성과, B8 부정 성과
- 개요: 세계 최고의 IT 기업이자 매일 수십억 명이 이용하는 검색 제국 구글의 거대한 왕국이 단 두 명의 퇴사로 인해 순식간에 흔들리기 시작했다면 믿어지시나요? 시가 총액이 하룻밤 사이에 380조원 넘게 증발하고 10수년간 압도적으로 지켜온 인공지능 분야의 절대 주도권을 단숨에 빼앗껴 버린 사태가 벌어졌습니다. 오늘 영상에서는 거대테크 기업 구글을 휘청이게 만든 두 천재 인재의 이탈 사건을 시작으로…
- B3 전략적 대응: 최고 경영진은 인공지능 연구원들을 매섭게 들볶으며 무슨 수를 써서라도 당장 오픈 AI의 채 GPT에 맞설 대학마을 만들어 세상에 내놓으라고 압박하기 시작했습니다.
- B1 디지털·AI 기술의 활용: 아, 2017년 구글의 연구원 여덟 명이 작성한 attention is all유 need라는이 단 한편의 논문은 오늘날 우리가 열광하는 오픈 AI의 챗 GPT를 비롯해 클로드 제미나이에 이르기까지 현존하는 모든 거대 언어 모델의 근간이자 뿌리가 되었습니다.
- 수치 주장: 그리고 그 경고가 잔인할 정도로 참혹한 현실로 바뀐 결정적 순간이 바로 2022년 11월 전 세계 테크 생태계를 뒤흔든 오픈 AI의 채 GPT 출시였습니다.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/2026-07-24/Only_2_employees_left,_yet..._The_shocking_sign_of_Google's___syU5o1-BPUI.md`

---

## 삼성SDS AX


**475. [[AX Summit] 2. (키노트)AI Native 기업으로의 전환 방안과 사례(AX센터 AI사업팀장 신계영 부사장)](https://www.youtube.com/watch?v=PsfnMJwSoXs)** — 삼성SDS AX · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 어, 오늘 제가 주제로 발표드릴 부분은 AI 네이티브 기업의 전환이라는 주제입니다. 어, 최근에 AX에 대해서는 뭐 모든 기업이 아, 고민을 하고 계시고 시대공학 계실 텐데 오늘 제 세션에서는 어떤 부분들을 더 중점적으로 고하면서 진행하셔야 될지를 어, 하나하나 설명을 드리도록 하겠습니다. AI가 일을 일자리를 뺏는 것이 아니라 AI를 잘 쓰는 사람한테 일자리를 뺏길 거다라는 얘기는 젠슨뿐만…
- B1 디지털·AI 기술의 활용: 실제로 원천 데이터에 있는 정형 데이터, 비정형 데이터 모드를 어 실제로 방금 말씀드린 데이터의 품질를 확보하기 위한 전처리 작업을 진행을 하고 어 전처리르 작업이 끝난 데이터들을 한 군데 잘 모아서 그때로는 데이터 레이크가 될 수도 있고 데이터 웨어하우스가 될 수도 있고요.
- B2 파괴: 데이터 가용성: 실제로 원천 데이터에 있는 정형 데이터, 비정형 데이터 모드를 어 실제로 방금 말씀드린 데이터의 품질를 확보하기 위한 전처리 작업을 진행을 하고 어 전처리르 작업이 끝난 데이터들을 한 군데 잘 모아서 그때로는 데이터 레이크가 될 수도 있고 데이터 웨어하우스가 될 수도 있고요.
- 수치 주장: 이렇게 위에 있는 에이전트를 만들고 등록하고 같이 쉐어하고 재활용하고 사용하는 이런 어 1년 에이전트 오수 체계가 있다면 기업 관점에서는 전체이 에이전트들을 많은 돈을 투자해서 만들고 운영을 하고 있는데 아까 앞에서 말씀드린 것처럼 ROI KPI가 정말 달성이 되고 있는지 보기 위해서는 다양한 관점에서의 거버넌스 체계가 좀 필요하게 됩니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: 프로토콜·표준 · 거버넌스·평가 도구 · 온톨로지·데이터계층
- 원문: `transcripts/2026-07-23/[AX_Summit]_2._(키노트)AI_Native_기업으로의_전환_방안과_사례(AX센터_AI사업팀장_신계__PsfnMJwSoXs.md`

**476. [AI-Native 기업으로 전환 전략과 사례](https://www.youtube.com/watch?v=Y-ApGj-9ceI)** — 삼성SDS AX · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B5 구조 변화, B6 장벽
- 개요: 어, 오늘 제가 발표드릴 주제는 어, AX라는 얘기들을 많이 하시는데 기업에서 그러면 AX AI 네이티브 기업으로 전환할 때 고려해야 될 사항들이 어떤 것들인가를 제가 좀 필드에서 경험한 내용들 중심으로 설명드릴 거고요. 어, 마지막에 혹시 시간이 되면 뒷부분에 어, 제가 몇 가지 기업 사례들도 좀 가져왔는데 시간 되는 대로 또 진행하도록 하겠습니다. 정차 아젠단는 어, 들어가기에 앞서서 최…
- B8 부정 성과: 보안·프라이버시: 가장 최근에 클로드 미소스라고 해서 클로드에서 어 아직 공개하지 않은 모델인데이 해당 모델 가지고 어 해킹을 하는 화이트 해킹이겠죠.
- B1 디지털·AI 기술의 활용: 하나의 도시즘 준비해 왔는데 오른편 상단에서 보시면 사람도 있고 AI 에이전트도 있고 기존에는 프로세스 오토메이션 수탄이었던 IPA로 만든 자동화된 봇들도 이렇게 섞여 있는 거 같습니다.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: —
- 원문: `transcripts/2026-07-26/AI-Native_기업으로_전환_전략과_사례__Y-ApGj-9ceI.md`

---

## 삼성SDS and KASMO 인공지능혁신추진단


**477. [제조업 AX의 골든 타임 ⏰ 중요한 것은 AI 도입보다 이것?! 📢 IT슈다 EP. 제조](https://www.youtube.com/watch?v=iAbE9YXnbqA)** — 삼성SDS and KASMO 인공지능혁신추진단 · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B5 구조 변화 → B6 장벽 · 빠짐: B3 전략 대응, B7 긍정 성과, B8 부정 성과
- 개요: 다른 분야보다 쉬울 수도 있지 않을까라는 여기서 조금 잘못된 선택을 하게 되면 어쩌면은 우리의 그 생존의 위협을 받을 어 기로에서 있다. &gt;&gt; 기서관에 그런 [음악] 데이터나 정보가 교류가 안 되는 거예요. &gt;&gt; 기술 유출. [음악] &gt;&gt; 네. 네. 그런 온프라미 환경을 쓰셔도 되고 아니면 좀 어렵지만 클라우드 프라이빗 [음악] 환경에서 &gt;&gt; 데이터…
- B1 디지털·AI 기술의 활용: 어, 우리 생산 인구의 절벽이 있더라도 어, 요런 AI 에이전트가 하나씩 하나씩 들어와서 그 역할을 해 준다 그러면 &gt;&gt; 어, 그리고 이제 그 안묵지가 형식지로 잘 바뀐다면 그러면 이제 지금 현재 우리가 안고 있는 문제점들이 일시에 해결될 수 있다고 보고 있거든요.
- B4 가치네트워크·생태계: &gt;&gt; 그 독일의 카타나가 이제 그거를 선도해서 자동차 기업들이 이제 탄소 발자국을 공급망 생태계 안에서 얼마나 배출을 하는지를 좀 알고 싶은데이 &gt;&gt; 공급망 내에서 서로 데이터 교환이 안 되니까 그걸 데이터를 교환할 수 있는 데이터 공유 플랫폼을 만든 거거든요.
- 교량: 정의 확장(DX→AX 계승), Avenue 2 윤리·거버넌스 · 기술: 온톨로지·데이터계층
- 원문: `transcripts/2026-07-18/제조업_AX의_골든_타임_⏰_중요한_것은_AI_도입보다_이것!_📢_IT슈다_EP._제조__iAbE9YXnbqA.md`

---

## 손에잡히는경제


**478. [Breaking Down Google's Earnings: They're Scaling Up Investments - CEO Hong Chun-wook (Prism Inves...](https://www.youtube.com/watch?v=CpKLKwscstc)** — 손에잡히는경제 · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B7 긍정 성과 · 빠짐: B4 가치창출 경로, B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: 오늘의 플러스 AI 사이클을 둘러싼 시장 안팎의 변수를 살펴봅니다. 홍춘욱 프리즘 투자자문 대표셨습니다. 어서 오세요. &gt;&gt; 네, 안녕하세요. &gt;&gt; 예, 대표님 지난번에 뵙을 때가 딱 한 달 조금 넘었던 거 같은데 그때 와서 저희한테 뭐라고 얘기하고 가셨냐면 앞으로 증시가 그렇게 낙관하기가 힘들 것 같다. 부정적인 얘기를 하고 가셨습니다. 사실 그때 댓글 보셨는지 모르겠…
- B1 디지털·AI 기술의 활용: 그러니까 이제 &gt;&gt; 클라우드 서비스야 뭐 남들한테 이렇게 임대해 주고 제공해 주는 거니까 그거 잘되는 건 굉장히 매출의 안정성을 높여 주는 건 좋은데 야 이거 인공지능 시장에서 어 공간을 대어해 주고 데이터 센터를 대어해 주는 한편 당신들도 개발 잘한다.
- B3 전략적 대응: &gt;&gt; 당장 어, 지금 중국에 상장한 창신 매물리 CXMT 같은 경우도 그렇고 또 나가서 마이크론이 어, 이번에 투자 계획을 발표했는데 작년에 발표할 때는 2,억 달러.
- 수치 주장: &gt;&gt; 근데 그게 어 9억 5천만 명 아 숫자는 엄청난 숫자인데 안타깝게도 &gt;&gt; 예 &gt;&gt; 예 10억의 사용자를 아직 달성하지 못했다라는 것도 이제 문제였고 더 나가서 &gt;&gt; 재미나이 이제 3.5%가 5%가 출시 지원돼서 &gt;&gt; 음 &gt;&gt; 이제 어 고급 사용자 시장이라고 저희들이 이제 부르는 개발자용 그런 시장에서 AI 코딩이라고 부르는데 &gt;&gt; 예 &gt;&gt; 아이 시장에서는 지금 &gt;&g…
- 교량: Avenue 2 윤리·거버넌스 · 기술: 칩·하드웨어
- 원문: `transcripts/2026-07-23/Breaking_Down_Google's_Earnings_They're_Scaling_Up_Investmen__CpKLKwscstc.md`

**479. [Why Companies Are in Trouble After Relying on AI for Layoffs - Economic Correspondent Ha Soo-jung](https://www.youtube.com/watch?v=4-lOvLaVWSA)** — 손에잡히는경제 · (미분류) · — · 2026-08 · ko · 5/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B3 전략 대응 → B5 구조 변화 → B7 긍정 성과 → B8 부정 성과 · 빠짐: B2 파괴, B4 가치창출 경로, B6 장벽
- 개요: 존재감을 쭉쭉 높여가는 기업 이야기 업대는 기업 시간입니다. 하수정 경제 전문 기자 모셨습니다. 어서 오세요. &gt;&gt; 네, 안녕하세요. &gt;&gt; 오늘은 어떤 얘기 준비해 오셨습니까? 오늘은요 뜨거운 이야기, 뜨거운 이슈, 인공지능과 일자리 이야기입니다. &gt;&gt; AI 기술이 확산이 되면 어 우리가 일자리를 잃을 것이다라고 많이들 걱정을 했었잖아요. 근데 실제로 최근에 …
- B5 직무·역량 변화: 그러니까 기업들이 경영란을 겪고 있어서 직원들을 자르는게 아니고 앞으로 AI가 일자리를 대체할 거를 미리 예측을 해 가지고 선재적으로 인력 감축을 하고 있다라는 겁니다.
- B8 부정 성과: 보안·프라이버시: 그러니까 기업들이 경영란을 겪고 있어서 직원들을 자르는게 아니고 앞으로 AI가 일자리를 대체할 거를 미리 예측을 해 가지고 선재적으로 인력 감축을 하고 있다라는 겁니다.
- 수치 주장: 그러면이 40% 법칙 이걸 바탕으로 소프트웨어 기업들에게 적용한다면 AI 기업들도 여기에 해당된다 이렇게 보면 될까요?
- 교량: — · 기술: —
- 원문: `transcripts/2026-08-03/Why_Companies_Are_in_Trouble_After_Relying_on_AI_for_Layoffs__4-lOvLaVWSA.md`

---

## 지식인사이드


**480. [지금 세계에서 AI 제일 잘 쓰는 기업들의 공통점ㅣ지식인초대석 EP.78 (장진석 파트너)](https://www.youtube.com/watch?v=3FW8c5T7fik)** — 지식인사이드 · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B3 전략 대응 → B4 가치창출 경로 → B7 긍정 성과 · 빠짐: B5 구조 변화, B6 장벽, B8 부정 성과
- 개요: AI 관련 주식들이 엄청나게 상승하기도 하고 AI가 도입되면 진짜 어마어마한 변화가 있을 것처럼 얘기하는 것도 있고 그렇잖아요. 실제 AI를 도입을 해서 5% 정도의 기업이 매출과 이익이 약 70% 정도 더 개선됐습니다. 조금 더 무서운 거는 돈을 더 많이 벌게 되잖아요. 그거를 다시 재투자를 하는 거예요. AI에 일종의 복리 효과를 거두는 겁니다. 그러면 그 5%의 기업이 되기 위해서는 무…
- B1 디지털·AI 기술의 활용: 이것의 의미는 과거에는 예를 들면 한 단위 업무들을 어떻게 하면 조금 더 고도화를 할 거냐, 자동화를 할 거냐, AI를 활용할 거냐였다면 AI 에이전트가 등장을 하면서 그게 마케팅이라던가 HR이라던가 아니면 파이낸스 업무라든가 업무의 영역들이 존재를 하잖아요.
- B7 성과: 운영효율: 예를 들면 문서를 작성한다라던가 보고서를 만든다던가 아니면 통역 번역 업무를 한다라던가 자료 조사를 한다라던가 이런 기업의 일의 어떤 전반적인 일의 생산성 개선을 위해서 AI를 어떻게 쓸 거냐 그다음에 이걸 통해서 생산성을 몇 퍼센트 정도 개선할 거냐 이게 작년 재작년까지의 핵심적인 고민이었어요.
- 수치 주장: 실제 AI를 도입을 해서 5% 정도의 기업이 매출과 이익이 약 70% 정도 더 개선됐습니다.
- 교량: Avenue 2 윤리·거버넌스, Avenue 1 동적역량 · 기술: LLM 모델
- 원문: `transcripts/2026-07-18/지금_세계에서_AI_제일_잘_쓰는_기업들의_공통점ㅣ지식인초대석_EP.78_(장진석_파트너)__3FW8c5T7fik.md`

---

## 카카오벤처스 Kakao Ventures


**481. [💡 AX란 무엇인가? 직접 해본 스타트업 대표가 알려주는 AI 전환의 모든 것 | EP.2 Vibers.AI 신재인 대표 | [한국의 AI 리더들]](https://www.youtube.com/watch?v=cRfy_RXX5WA)** — 카카오벤처스 Kakao Ventures · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`washing`
- 사슬: B4 가치창출 경로 → B5 구조 변화 → B6 장벽 → B8 부정 성과 · 빠짐: B1 기술 활용, B2 파괴, B3 전략 대응, B7 긍정 성과
- 개요: [ 카카오벤처스 김영무 심사역 ] 이번 두 번째 에피소드는 [ 카카오벤처스 김영무 심사역 ] 바로 AX와 관련된 이야기인데요 [ Vibers AI 신재인 대표 ] 그 생산성의 혁신을 경험해 버린거죠 [ Vibers AI 신재인 대표 ] ‘와 말이 안된다’ [ Vibers AI 신재인 대표 ] ‘이거 그냥 게임 체인저구나’ 안녕하세요 카카오벤처스에서 테크 투자를 담당하고 있는 김영무 심사역입니…
- B8 부정 성과: 보안·프라이버시: ( 웃음 ) - 아니요 (다급) 사실 다 어렵죠 (당황) 이것저것 다 어려운데 비즈니스 단에서의 어려움은 결국에 고객들한테는 AX라는 게 언어로 잘 와닿지 않거든요 그거의 생산성을 직접 경험하는 실무자 관점에서는 AX라고 하는 키워드가 잘못하면은 공격적으로 들릴 수도 있고 그래서 누구를 만나서 어떻게 설득을 하고 어느 지점부터 조금씩 변화를 만들어 나갈 거냐 저희는 그걸 ‘Land and Expand’라고 하는데 어느 지점부터 작게 효용을 보여주면서 점점 생산성…
- B5 조직문화 변화: 계기 자체는 막 엄청 특별하지는 않았던 것 같아요 저는 원래 인생 계획에 있어서 ‘창업을 바로 해야지’ 라고 생각 했었고 그거에 맞춰서 토스를 나왔던 거였고 그다음에 제가 좀 쉬다가 바로 도전했던 일이 패션 브랜드를 1년간 운영을 했는데 패션 브랜드를 시작을 했던 계기는 IT 프로덕트에 있어서의 매일매일 만들어내는 자그마한 변화들에 실증이 있었던 것 같아요 예를 들면 내가 이번 주에 이뤄낸 성과가 버튼의 색깔을 바꿔서 혹은 버튼의 위치를 바꿔서 전환율을 0.5%…
- 수치 주장: 그런 (AX) 시도도 많이 하는 것 같고 근데 실패도 많이 겪으시는 것 같고 그런 사례도 봤어요 제가 아는 분이 연매출 6,700억 규모의 국내 브랜드가 있는데 AI 전문 시니어 개발자를 뽑아 가지고 내부 ERP나 이런 여러 시스템을 만들려고 하신다는 거예요 근데 AI가 사람의 일을 대체하는 거기 때문에 기업 안에 100명의 사람들이 일을 하고 있다면 100개의 AX 아젠다가 존재하는 것이거든요 너무나 많은 아젠다가 존재하기 때문에 그거를 하나의 AI 개발자를 …
- 교량: — · 기술: 온톨로지·데이터계층
- 원문: `transcripts/2026-07-18/💡_AX란_무엇인가_직접_해본_스타트업_대표가_알려주는_AI_전환의_모든_것_EP.2_Vibers.AI_신재__cRfy_RXX5WA.md`

---

## 티타임즈TV


**482. [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154)** — 티타임즈TV · (미분류) · — · 2026-07 · ko · 5/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B6 장벽 → B8 부정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B7 긍정 성과
- 개요: 안녕하십니까. 김유신입니다. 이번 시간에는 기업에서 AI를 활용하는 방법들 중에서 AI 시대에서도 중요한 것은 데이터다라는 부분에 대해서 좀 더 심도 있게 말씀을 드리려고 합니다. AI는 주로 예측을 하거나 탐지를 하거나 생성을 하는 일에 잘 활용됩니다.이 이 예측과 탐지와 생성을 위해서는이 AI를 학습시키기 위한 데이터가 필요합니다. 새로운 단어를 한 가지 말씀드리고 싶은데요. 데이터 센트…
- B1 디지털·AI 기술의 활용: 이 데이터 플랫폼을 구현하는 방식은 퍼블릭 클라우드 상에서 구축하는 것을 저는 제일 먼저 추천을 드리고요.
- B2 파괴: 데이터 가용성: 데이터가 없는 기업의 경우이 데이터들을 외부에서 가져와 가지고 AI 시스템에 적용을 하지만 그렇다고 그래서 데이터를 축적할 필요가 없다라는 것은 아니기 때문에 데이터 거버넌스도 확보를 하셔야 되고 데이터 플랫폼도 확보하셔서 그 AI 시스템이나 아니면 기업의 다른 원천 소스로부터 나오는 데이터들을 잘 모을 수 있도록 하셔야 됩니다라는 말씀을 드렸었잖아요.
- 수치 주장: 즉 데이터를 가지고 AI라든지 데이터 분석이라든지 이런 것들을 하려고 하는 기업의 80% 정도가 실패할 수 있다라는 굉장히 이제 심각한 얘기들을 하고 있는데 그것의 가장 중요한 요인 중 하나가 데이터 거버넌스를 잘 구축하고 활용하지 않기 때문이다라는 얘기인 거죠.
- 교량: Avenue 2 윤리·거버넌스 · 기술: LLM 모델
- 원문: `transcripts/2026-07-18/AI_도입을_위한_데이터_거버넌스_구축_전략은_(김유신_상무)__vH_g9HIm154.md`

**483. [AI 도입, 도입만 하면 끝일까? (김유신 상무)](https://www.youtube.com/watch?v=GiFlOiikYso)** — 티타임즈TV · (미분류) · — · 2026-07 · ko · 4/8블록 · `ax_core`/`anti_washing`
- 사슬: B1 기술 활용 → B2 파괴 → B5 구조 변화 → B7 긍정 성과 · 빠짐: B3 전략 대응, B4 가치창출 경로, B6 장벽, B8 부정 성과
- 개요: 안녕하십니까. 김유신입니다. 이번 시간에는 기업 내에서 시스템을 만든 다음에이 AI 시스템이 끊임없이 진화하고 계속해서 잘 사용하려면 어떤 부분을 고민해야 되는지라는 부분을 말씀드리려고 합니다. 기업에서 AI를 잘 사용하고 있는지 각 단계를 나눠 놓은 모델이 있어요.너의 AI 머추리티 모델이라고 하는 건데요. AI를 사용하는 기업에서 다섯 단계로 나눠 가지고 첫 번째는 스 인식이라고 해서 조…
- B1 디지털·AI 기술의 활용: 그래서 모르실 수도 있는데 한 번쯤 아 도대체 ML 머신 러닝 또는 AI 딥러닝이라는 것이 어떻게 돌아가는지 한번 아시면 좋을 것 같아서 제가 좀 가져와 봤습니다.
- B7 성과: 운영효율: 그래서 ML 뭐 또 시스템 또 개발해야 돼, 또 돈 들여야 돼라고 고민하시는 관점보다는이 시스템을 AI를 조직 전반으로 활용을 할 때이 시스템을 적용하게 되면 오히려 길게 보면 훨씬 더 비용이 절감된다라는 관점에서 보시면 좋을 것 같습니다.
- 수치 주장: 1단계 2단계 그리고 머링 이제 성숙돼 가지고 AI를 잘 활용하고 있는 단계가 한 48% 정도였습니다.
- 교량: — · 기술: —
- 원문: `transcripts/2026-07-21/AI_도입,_도입만_하면_끝일까_(김유신_상무)__GiFlOiikYso.md`

**484. [AI 에이전트 도입하려면 꼭 알아야 할 것 (이주환 스윗테크놀러지스 대표)](https://www.youtube.com/watch?v=7S5y1rwxIrw)** — 티타임즈TV · (미분류) · — · 2026-08 · ko · 4/8블록 · `ax_core`/`neutral`
- 사슬: B1 기술 활용 → B2 파괴 → B4 가치창출 경로 → B8 부정 성과 · 빠짐: B3 전략 대응, B5 구조 변화, B6 장벽, B7 긍정 성과
- 개요: 잠재된 능력에 따라서 어쩔 땐 일을 잘하고 어쩔 땐 일을 못 해가 아니고 내가 원하는 대로 늘 예측 가능하게 일관적으로 답변을 가지고 오고 그런 실행 결과를 우리에게 알려 줄 수 있도록 제어하는 것이 에이전트고요. 그 에이전트의 핵심이 루프 디자인입니다. 에이전트도 성장을 해요.
- B1 디지털·AI 기술의 활용: 저는이 책을 보고 또 오늘 인터뷰를 준비하면서 일단 전제로 하나 좀 깔았으면 좋겠는게 많은 분들은 AI 에이전트 시대가 열린다라고 하면은 그냥 예를 들어 채비 창에 내가 이런 이런 A 테스크, B 테스크, C 테스크를 합친 결과물 D를 얻고 싶으니까 네가 알아서 다 해 줘라고 하면은 그게 그냥 뿅하고 나올 거 같잖아요.
- B2 파괴: 소비자 행동·기대: 내가 어 건조기하고 협업을 해서 몇 시까지 완료해 놓을게요라고 미리 우리에게 컨펌을 요청한다면 그때는 정말 초개인화와 능동성이 두 가지의 혜택을 저희가 볼 수 있게 되는 거죠.
- 수치 주장: 저희가 2, 3년 전부터 이미 출시했던 기능인데요.
- 교량: — · 기술: LLM 모델
- 원문: `transcripts/2026-08-03/AI_에이전트_도입하려면_꼭_알아야_할_것_(이주환_스윗테크놀러지스_대표)__7S5y1rwxIrw.md`
