# AITF 사례 후보 — AI Transformation Framework 3축 매핑

> Holmström, J., & Magnusson, J. (2026). Navigating the organizational AI journey: The AI transformation framework. *Business Horizons, 69*(1), 89–100.

> 자동 생성물(`python map_aitf.py`). 수집 코퍼스의 `ax_core` 문서를 논문의 3차원 × 4항목(Level·Scope·Impact·Future) 구조로 코딩해 **사례 후보**를 뽑은 것이다.


## 0. 무엇을 잰 것인가 (타당성 고지)

| 구분 | 논문 Table 1 | 본 매핑 |
|---|---|---|
| 자료 | 조직 내부 자기보고 설문 | 공개 유튜브 담론(자막 전문) |
| 척도 | 5점 리커트 × 4항목 = 0~16 | 규칙 기반 대리지표 × 4항목 = 0~16 |
| 판정 | 8점 이하 low / 9점 이상 high | 동일 절단점 + 코퍼스 상대 절단점 병기 |
| 대상 | 특정 조직의 성숙도 | 발화의 **강조점**(claim), 성숙도 아님 |

측정 규칙: **Level** = 축 핵심어 밀도(1천 단어당), **Scope** = 전사·all employees 등 범위 표지가 축 핵심어 ±400자에 출현, **Impact** = 수치·효과 표지(%, 배, 절감 …)가 근처에 출현, **Future** = 전략·로드맵·계획 표지가 근처에 출현. 각 0~4점.

⚠️ 여기 뽑힌 것은 **사례 후보**다. 논문·발표에 인용하려면 원문(파일 링크)을 직접 확인해야 한다.


## 1. 세 축의 담론 강조 비교

| 축 | 평균(0~16) | 논문 절단점(≥9) 충족 | 상대 절단점(상위 10%) |
|---|---|---|---|
| 자동화 | 1.50 | 61건 (2.2%) | 5점 |
| 증강 | 0.77 | 12건 (0.4%) | 3점 |
| 데이터풍부성 | 1.20 | 37건 (1.3%) | 4점 |

총 2777건(ax_core) 기준. **논문 절단점을 그대로 적용하면 거의 모든 문서가 low**로 떨어진다 — 공개 담론은 네 하위항목(수준·범위·영향·전략)을 동시에 갖춰 말하는 일이 드물기 때문이다. 이것 자체가 관찰이다: 담론은 성숙도 진술이 아니라 **부분적 주장**의 형태를 띤다.

축 간 비교에서 **자동화 > 데이터 풍부성 > 증강** 순으로 강조된다. 논문이 integrated intelligence(3축 동시 high)를 목표점으로 제시한 것과 대비하면, 공개 담론은 자동화 쪽으로 치우쳐 있고 증강 서사가 가장 얇다.


## 2. 큐브 8개 상태별 사례 후보

셀 판정은 **코퍼스 상대 절단점**(자동화 ≥5, 증강 ≥3, 데이터 ≥4 → high)이다. 각 셀에서 세 축 합계 상위 문서를 뽑았다.


### H-H-H — integrated intelligence (논문 명명 · Fig.2 목표점)  (17건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| SAP | 자사 채널 | [Global Keynote: The Beginning of Better ／ SAP Sapphire Madri](https://www.youtube.com/watch?v=CocpyxAizwE) | 15 | 12 | 9 | These AI systems take care of the most complex tasks, including data migration, test automation, or business process re-engineering. All in all, we are aiming to reduce migration e |
| Insight Solutions | 미디어·검색 | [Innovating & Measuring ROI for Enterprise Organizations Thro](https://www.youtube.com/watch?v=U84H7KOAlyU) | 11 | 4 | 11 | 특정 목표를 달성하기 위해 직접 정보를 수집해야 하는 모든 작업은 이러한 기술을 통해 쉽게 자동화할 수 있습니다. 모든 기술을 다 설명드릴 수는 없지만, 대략적인 개념은 이러한 기술을 통해 구현할 수 있다는 것입니다. 제가 만나는 거의 모든 고객은 이미 수십 가지의 활용 사례를 파악하고 있습니다. 고객과 이러한 활용 사례 |
| Microsoft Azure | 자사 채널 | [Optimize Azure Storage costs: smart tier, automation, and Az](https://www.youtube.com/watch?v=QOcCdyL1lLY) | 11 | 7 | 7 | 따라서 현재 데이터 환경을 파악하고 스토리지 용량을 적절하게 조정하는 자동화된 방법을 마련하는 것은 데이터가 계속 증가함에 따라 지속 가능한 비용 절감을 달성하는 데 매우 중요합니다 . Azure 스토리지는 엑사 바이트 규모의 데이터와 수조 건의 트랜잭션을 처리할 수 있는 엄청난 확장성을 자랑하는 플랫폼입니다. Azure |
| SAP | 자사 채널 | [Global Keynote: The Beginning of Better ／ SAP Sapphire Orlan](https://www.youtube.com/watch?v=9aa-etRsaLU) | 9 | 8 | 8 | 이러한 AI 비서들은 데이터 마이그레이션, 테스트 자동화, 비즈니스 프로세스 재설계 등 가장 복잡한 작업까지 처리합니다. 종합적으로, 우리는 이주로 인한 노력을 최대 50%까지 줄이는 것을 목표로 하고 있습니다. 마이그레이션을 더욱 빠르고 비용 효율적으로 만들어 드립니다. 이 내용은 내일 토마스와 얀이 진행할 고객 기조연 |
| DATAVERSITY | 미디어·검색 | [Analythics Architecture:  Promising AI Use Cases for the Ent](https://www.youtube.com/watch?v=JhbsIutTwXM) | 9 | 7 | 8 | 기업들은 자동화된 에이전트가 일상적인 문의에 대해 토큰을 과도하게 할당하는 것을 방지하는 방법을 알아내는 데 한 해를 보냈습니다. 모든 게 장밋빛만은 아니잖아요, 그렇죠? H&amp;M은 고객 서비스를 제공하는데, 대화형 AI 챗봇을 활용하죠 ? 이 시스템은 대량의 고객 문의를 자동으로 처리하고 해결하여 전환율을 25%  |
| Weights & Biases | 자사 채널 | [What’s the path to AGI? A conversation with Turing Co-founde](https://www.youtube.com/watch?v=DJS7cop0CCw) | 9 | 10 | 5 | 예를 들어 언더라이팅 코파일럿은 성공적이었고, 그 덕분에 클레임 처리 코파일럿도 구축해 달라는 요청을 받았습니다. 많은 기업들이 여전히 ROI를 정확하게 측정하는 방법을 고민하고 있는 것 같습니다. 그리고 한 가지 어려운 점은 이러한 시스템이 대규모로 운영될 경우 많은 기업의 인력 수요가 줄어들 수 있다는 점입니다. 이로 |
| Intel | 자사 채널 | [AI’s Next Frontier: Human Collaboration, Data Strategy, and ](https://www.youtube.com/watch?v=hFTRv3Va5IE) | 7 | 6 | 7 | 하지만 좀 더 짧은, 그러니까 향후 2~3년 주기로 보면, 우선 단순 자동화에서 심층 증강으로 초점이 옮겨갈 거라고 생각합니다. 다시 말해, AI가 사람들의 업무를 더 효율적으로 만들어주는 것이죠. 소프트웨어 개발자부터 마케팅 관리자, 재무 분석가까지 모든 직원에게 진정한 조력자 역할을 하는 겁니다. 목표는 반복적인 작업 |
| Zapier | 자사 채널 | [Zapier AI Showcase: 50 Million Tasks Delegated (The Best Use](https://www.youtube.com/watch?v=pGjirCLK9qE) | 11 | 4 | 4 | HubSpot, Salesforce, Mailchimp와 같은 일상적인 앱을 Chat, GPT 또는 200개 이상의 AI 앱 중 하나와 통합하여 콘텐츠 요약, 이메일 개인화, 지원 자동화 등 다양한 작업을 수행할 수 있습니다. 저희 Zapier 또한 AI를 활용하여 운영 방식을 혁신했습니다 . 영업, 지원, 마케팅, 엔지 |

- `transcripts/channels/SAP/Global_Keynote_The_Beginning_of_Better_SAP_Sapphire_Madrid_2__CocpyxAizwE.md`
- `transcripts/2026-08-03/Innovating_&_Measuring_ROI_for_Enterprise_Organizations_Thro__U84H7KOAlyU.md`
- `transcripts/channels/Microsoft_Azure/Optimize_Azure_Storage_costs_smart_tier,_automation,_and_Azu__QOcCdyL1lLY.md`

### H-L-H — 데이터 기반 자동화 (사람 강화는 후순위)  (49건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| ai2learn | 미디어·검색 | [Why SMB Companies Fail at AI Transformation and How to Avoid](https://www.youtube.com/watch?v=gbP_TrZnPTs) | 12 | 0 | 9 | Open AI는 자체 개발한 에이전트를 통해 모든 직원을 자동화했습니다. 우리도 하나 만들면 안 될까요 ? 몇 명만 만들 수 있을 것 같은데 , 왜 이렇게 오래 걸리는 걸까요? 이런 말들, 어디선가 들어본 것 같지 않나요 ? 많은 리더들은 기술 기업의 사례를 스쳐 지나가듯 듣고는 곧바로 자신들의 조직에서도 단기간 내에 비 |
| Zapier | 자사 채널 | [Build an AI First RevOps Team for MAXIMUM Impact](https://www.youtube.com/watch?v=4_vkQdMQ5xs) | 8 | 2 | 9 | 그래서 AI를 시장 진출 전략에 어떻게 접목할지 생각할 때, 가장 먼저 해야 할 일은 실제 데이터 기반을 어떻게 구축할지 고민하는 것입니다. 만약 여러분의 주요 데이터 소스가 CRM 시스템이라면, 정말 큰 문제에 직면하게 될 겁니다. 왜냐하면 정확한 AI를 구현하는 데 필요한 데이터를 확보할 수 없을 것이기 때문입니다.  |
| 삼성SDS AX | 미디어·검색 | [ChatGPT Enterprise 도입전략](https://www.youtube.com/watch?v=oXxq-xeAoJQ) | 11 | 0 | 6 | 채의 기본 원리와 활용 방식의 이해 및 업무 적용 역량을 강화하고 프롬프트 활용과 반복 업무 자동화 시술을 통해 생산성과 업무 효율 향상을 지원합니다. 그리고 전문 분야별 채치 활용 전략 및 적용 방안을 제시하여 조직 내 AI 활용 확산과 실무 적용 자신감을 제고합니다. AX 컨설팅을 통해 삼성 SDS의 검증된 ITP 기 |
| AI Engineer | 미디어·검색 | [The Production AI Playbook: Deploying Agents at Enterprise S](https://www.youtube.com/watch?v=ObTPqBGsEbA) | 9 | 0 | 8 | 그러니까 AI에 질문을 던지면 AI가 답하고, 그 답을 테스트 세트와 비교하고, 이 전체 파이프라인을 자동화하는 겁니다. 이렇게 하면 AI를 실제 운영 환경에 배포했을 때, 해당 파이프라인이 실시간 응답을 받아 구축 중인 테스트 데이터 세트와 비교 평가하고, AI가 목표 대비 얼마나 잘 작동하는지 결과를 제공할 수 있게  |
| SAP | 자사 채널 | [How NEC Is Becoming an AI-Native Enterprise with SAP, RISE w](https://www.youtube.com/watch?v=6utLfKSBIHg) | 7 | 0 | 10 | 이에 대한 명확한 예는 우리가 데이터 기반 경영을 실제로 적용해 온 방식에서 찾아볼 수 있습니다 . 우리는 핵심 시스템을 클라우드로 이전하고, 프로세스 데이터를 표준화했으며, CEO를 중심으로 회사 전체의 혁신을 주도하는 조직을 만들었습니다 . 우리는 경영진을 위한 대시보드를 약 100개 정도 구축하여 사업 전반에서 실제 |
| Snowflake | 자사 채널 | [How AI Transforms Retail, Finance and Manufacturing in 2026](https://www.youtube.com/watch?v=11degQs3L7c) | 7 | 0 | 10 | 두 번째는 제가 조금 전에 언급했듯이 데이터 거버넌스와 AI 평가에 대한 통합적인 접근 방식이 이제 필수적이 되고 있다는 것입니다. 데이터가 분산되어 AI 시스템에 대한 신뢰가 무너지면 투자 대비 수익률(ROI)은 기대할 수 없을 것입니다. 그리고 세 번째 영역은 전통적인 데이터 거버넌스에서 모델 거버넌스 및 사용 거버넌 |
| Zapier | 자사 채널 | [The Capture, Store, Automate Blueprint: Your Masterclass in ](https://www.youtube.com/watch?v=jM4iA9gpmaU) | 11 | 2 | 4 | By 2025, 80% of organizations are expected to move from basic automations to advanced orchestration. This is becoming the default way modern businesses run. Second, the impact is c |
| Y Combinator | 미디어·검색 | [How AI Is Changing Enterprise](https://www.youtube.com/watch?v=aIKfA3gIXwo) | 10 | 2 | 4 | 그런데 이제 기업들은 이전에는 자동화하지 않았던 부분을 자동화하는 데 우선순위를 두게 될 거예요. 앞서 예시로 들었던 것처럼, 이 기술에 투자되는 돈은 사람들이 현재 하고 있는 일을 빼앗아 가는 게 아니라, 순전히 기존 업무에 추가되는 것뿐이에요. 소프트웨어의 활용 사례를 확장하는 것은 여러 가지로 연결될 수 있기 때문에 |

- `transcripts/2026-07-23/Why_SMB_Companies_Fail_at_AI_Transformation_and_How_to_Avoid__gbP_TrZnPTs.md`
- `transcripts/channels/Zapier/Build_an_AI_First_RevOps_Team_for_MAXIMUM_Impact__4_vkQdMQ5xs.md`
- `transcripts/2026-07-26/ChatGPT_Enterprise_도입전략__oXxq-xeAoJQ.md`

### L-H-H — 데이터 기반 증강 (자동화는 후순위)  (69건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| Citizen Developer and Na | 미디어·검색 | [AI Transformation Leader (AB-731) - Full Course - Pass The E](https://www.youtube.com/watch?v=Ox0m3iJG57M) | 2 | 12 | 8 | 그러한 영역이 바로 코파일럿 스튜디오의 영역입니다. 그리고 앞서 말씀드린 것처럼, 이제 Azure 기능과 Foundry 기능에 대해 더 자세히 살펴보겠습니다. 바로 이 부분에서 에이전트와 관련하여 전문가 수준의 코드 맞춤 설정이 가능합니다. 그래서. 예. 간단히 말해서, M365 내에서 개인 생산성이나 팀 생산성 향상을  |
| Microsoft Learn | 미디어·검색 | [Prepare for Microsoft Certification Exam AB-731: AI Transfor](https://www.youtube.com/watch?v=mj_lyhuWbig) | 2 | 11 | 7 | So Copilot is for using AI. Foundry is for running and managing AI at scale. You'll need to know how to map specific pre-built capabilities for language, vision, speech, and decisi |
| Pinecone | 자사 채널 | [Production Ready RAG in Healthcare with Pinecone and Autoblo](https://www.youtube.com/watch?v=93f7ZHPkpTk) | 3 | 7 | 10 | 임베딩이 무엇인지 간단히 복습하고, 벡터 데이터베이스가 무엇인지 설명한 다음, RAG(Retrieval Augmented Generation)에 대해 간략하게 이야기해 보겠습니다. 이것들은 하룬과 아담이 앞으로 보여줄 나머지 데모와 설명을 이해하기 위해 알아야 할 기본적인 개념들입니다. 다음 슬라이드로 넘어가겠습니다. 음 |
| Certification Practice | 미디어·검색 | [Microsoft AI Transformation Leader: The 5 Rules To Pass](https://www.youtube.com/watch?v=YRZEjVGBDSA) | 0 | 10 | 8 | 또한 신속한 엔지니어링 기법과 RAG(Retrieval Augmented Generation)가 AI 출력을 실제 데이터에 기반하여 생성하는 방식을 이해해야 합니다. 첫 번째 규칙. AI 출력 정확도 향상에 대한 질문을 받으면, 먼저 프롬프트 엔지니어링과 기본 원리를 생각해 보세요. 두 번째 규칙. 시나리오에서 신뢰할 수 |
| IBM Technology | 미디어·검색 | [10 Use Cases for AI Agents: IoT, RAG, & Disaster Response Ex](https://www.youtube.com/watch?v=Ts42JTye-AI) | 4 | 7 | 7 | 두 번째로 살펴볼 것은 검색 증강 생성과 관련된 것입니다. 저건 RAG야. 그리고 세 번째로 살펴볼 것은 멀티 에이전트 워크플로우인데, 말 그대로 여러 에이전트를 사용하는 워크플로우입니다. 그럼 한번 살펴보겠습니다 . 그럼 농업 과 AI 에이전트부터 시작해 보겠습니다. 이러한 시스템은 자율적으로 환경을 모니터링하고 농업  |
| NVIDIA Developer | 자사 채널 | [Teach AI to Code in Every Language with NVIDIA NeMo ／ NVIDIA](https://www.youtube.com/watch?v=d8yQ358u-rE) | 0 | 6 | 11 | 앞서 말씀드린 것처럼, 저희는 Hugging Face에서 제공하는 NeMo Tron 사전 학습 데이터 세트를 사용했습니다 . 음, 여기에서 영어 및 스페인어 위키피디아와 함께 사용한 여러 파일들을 보실 수 있습니다. 계획은 아주 간단합니다. 저희는 이러한 데이터 세트 중에서 콘텐츠의 71%는 코드, 약 9%는 수학, 일부 |
| Pinecone | 자사 채널 | [RAG Brag with Kap Sharma of Wipro](https://www.youtube.com/watch?v=i_EOgO7W-jM) | 0 | 6 | 11 | 여기 계신 분들 중 약 36%가 양질의 데이터 접근에 어려움을 겪고 있다고 답했습니다. 우리 모두 공감할 수 있는 부분이죠. 29%는 모델 정확도와 성능에 어려움을 겪고 있다고 답했습니다. 이는 항상 문제죠. 오류를 최대한 줄이고 싶으니까요. 그리고 거의 같은 36%가 양질의 데이터 접근, 높은 비용 및 예산 제약에 어려 |
| Pinecone | 자사 채널 | [Getting started with Pinecone monthly webinar (November 2025](https://www.youtube.com/watch?v=pY_7RSUnotk) | 3 | 6 | 7 | 하지만 Pine Cone은 비정형 데이터에 특화되어 설계되었습니다. 어, 이게 바로 우리가 하는 일이에요. 이것이 바로 우리가 만들어진 이유입니다. 그리고 당신은 그런 절충안을 택할 필요가 없습니다 . 그리고 여러분은 어떤 유형 의 지식이든, 어떤 AI 워크로드든 저희에게 가져오실 수 있습니다. 그러니까 임베딩으로 변환할 |

- `transcripts/2026-07-21/AI_Transformation_Leader_(AB-731)_-_Full_Course_-_Pass_The_E__Ox0m3iJG57M.md`
- `transcripts/2026-07-18/Prepare_for_Microsoft_Certification_Exam_AB-731_AI_Transform__mj_lyhuWbig.md`
- `transcripts/channels/Pinecone/Production_Ready_RAG_in_Healthcare_with_Pinecone_and_Autoblo__93f7ZHPkpTk.md`

### H-H-L — 자동화+증강, 데이터 기반 취약  (34건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| Intel | 자사 채널 | [AI Industrialization: The Next Frontier for Global Enterpris](https://www.youtube.com/watch?v=fSadUMtpwcY) | 11 | 6 | 3 | 그래서 우리는 AI를 전술적으로 활용하여 작업을 자동화하는 대신, 프로세스 혁신을 위해 AI를 우선시하는 전면적인 접근 방식을 채택했습니다 . 우리는 인공지능을 염두에 두고 프로세스를 처음부터 재설계하는 것이 인공지능의 잠재력을 최대한 발휘하는 열쇠라고 믿습니다. 따라서 오늘날 PMI에서 AI 산업의 산업화는 분산된 시범 |
| Zapier | 자사 채널 | [[AMA] Kickstart Your AI Fluency: Exec Ops & HR Transformatio](https://www.youtube.com/watch?v=jONuMTU-_uM) | 12 | 5 | 3 | 음, 그러니까 그런 간단한 것들을 개인적인 생활에 적용하거나, ' 이런 일이 생기면 이렇게 하라'는 것을 이해하기 시작하면, 시간이 지남에 따라 자동화된 사고방식을 갖게 될 거예요. 그리고 Satcha 님께서 사용 사례를 공유하는 것에 대한 훌륭한 팁을 주셨죠 . 개인적인 사용에서 팀 및 회사 전체의 사용으로 이어지는 가 |
| Vertesia | 미디어·검색 | [Enterprise strategies for agentic AI adoption in 2026 and be](https://www.youtube.com/watch?v=B4WgQotMVmE) | 6 | 10 | 2 | Uh that's an acronym for retrieval augmented generation. Um so if you were to think you know if you follow the Iron Man movies this is our Jarvis. Um you know almost uh so that is  |
| McKinsey & Company | 자사 채널 | [Agentic AI and the future of Global Business Services](https://www.youtube.com/watch?v=LuHGabkzlGU) | 12 | 6 | 0 | 우리는 기존 자동화 방식으로는 달성할 수 없었던 수준을 훨씬 뛰어넘고 있습니다. GBS(Global Business Strategy)는 AI 기반 조직 전반에 걸쳐 가치를 창출하는 데 여전히 중요한 역량이라는 점이 점점 더 분명해지고 있습니다 . 글로벌 비즈니스 서비스의 미래에 대해 이야기하기 위해 맥킨지 쾰른 사무소의  |
| TCS | 자사 채널 | [Navigating the Future of Tech with Dr Harrick Vin, Ray Wang,](https://www.youtube.com/watch?v=tHeXimKdKLA) | 9 | 6 | 2 | 제 생각에는 이 AI 천재, 혹은 전통적인 AI의 첫 번째 활용 물결은 사람들이 손쉽게 정보와 자동화 기능을 얻을 수 있도록 하는 데 더 중점을 두었던 것 같습니다. 우리는 그것을 사람들이 생산성을 향상시키도록 돕는 것이라고 부릅니다. 제 생각에 우리가 지금 막 시작하려는 다음 단계는 바로 그러한 지능을 활용하여 사람들의 |
| Weights & Biases | 자사 채널 | [GitHub CEO Thomas Dohmke on Copilot and the Future of Softwa](https://www.youtube.com/watch?v=PPs5lZ2syv4) | 5 | 12 | 0 | 아시다시피, 코파일럿 없이 작업할 때와 코파일럿을 사용할 때의 생산성 향상을 비교할 때 어려운 점은, 같은 작업을 두 번 다시 하지 않는다는 것입니다. 음, 사례 연구를 할 수 있는데, 55%라는 수치는 거기서 나온 겁니다. 50명의 개발자에게 코파일럿 없이 작업을 하도록 하고, 나머지 50명에게는 코파일럿을 사용해서 작 |
| Zapier | 자사 채널 | [Zapier's Big AI Plans for 2026 Revealed! - Leadership, Cultu](https://www.youtube.com/watch?v=EfHm1Qjztd0) | 11 | 4 | 2 | 그 고통의 핵심에 깊이 관여하고 있는 사람이 바로 인공지능을 활용해 그 고통을 자동화하는 데 가장 적합한 사람이다 . 그래서 저는 2026년에 Zapier 고객을 포함한 다른 사람들에게 자체적인 AI 솔루션을 구축하도록 멘토링을 제공할 계획입니다. 그리고 2026년까지 제 목표는 Zapier의 모든 직원 과 많은 고객들을 |
| 메타코드M | 미디어·검색 | [26 Years of Survival Keyword AX (Great AI Transformation): W](https://www.youtube.com/watch?v=VRYJJJBqsDE) | 6 | 8 | 2 | 어 저도 강연을 듣는 사람일 때도 있고 강연을 하는 사람일 수도 있는데 오늘 들으시는 분들은 같은 직장 동료로서 어 새로운 관점으로 조금 또는 비슷한 공감되는 관점을 조금 더 증강하고 저희가 디벨롭한다라는 관점으로 같이 봐 주시면 좋을 것 같습니다. 어 해당 발표에서는 기술 도입하는 업무 조직을 다시 설계하는 관점에서 조 |

- `transcripts/channels/Intel/AI_Industrialization_The_Next_Frontier_for_Global_Enterprise__fSadUMtpwcY.md`
- `transcripts/channels/Zapier/[AMA]_Kickstart_Your_AI_Fluency_Exec_Ops_&_HR_Transformation__jONuMTU-_uM.md`
- `transcripts/2026-07-21/Enterprise_strategies_for_agentic_AI_adoption_in_2026_and_be__B4WgQotMVmE.md`

### H-L-L — 데이터 없는 자동화 (효율만 좇는 상태)  (219건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| Palantir | 자사 채널 | [Paragon 2025](https://www.youtube.com/watch?v=UjkRz9HkldU) | 12 | 1 | 3 | 자동화를 통해 이 한 번의 전화 통화, 이 하나의 상호 작용에 포착된 뉘앙스가 일련의 활동을 생성하고 그에 따라 조치를 취합니다. 우리는 더 이상 누군가가 그것을 기록하고 그 일이 제대로 이루어지기를 기다릴 필요가 없습니다. 한 번의 간단한 대화로 조직 전체에서 실제로 측정 가능한 결과를 얻을 수 있습니다. 포트폴리오가  |
| Zapier | 자사 채널 | [How Executive Assistants Drive Strategic Impact with AI](https://www.youtube.com/watch?v=-gGwrSPc3tA) | 15 | 1 | 0 | 그러니까 , 이 작업을 자동화했기 때문에 다른 더 중요한 일에 집중할 수 있게 되었다는 거죠. 그래서 제가 지금 실현하고 있는 것과 같은 투자 수익률(ROI)은, 단순히 수치적인 지표가 아니라, 경영진이 장기적으로 기억할 만한 무언가라고 생각합니다 . 그래서 지표를 보여주실 수 있을 것 같은데, 요약하자면, 제가 좋아하는 |
| Zapier | 자사 채널 | [What Netflix Knows About AI That Every Recruiter Should Lear](https://www.youtube.com/watch?v=edY-3X18CHc) | 16 | 0 | 0 | 그러니까 인공지능 과 자동화를 특정한 목적을 가지고 사용하는 사람들, 그리고 더 나아가 투자 수익률(ROI)을 위해 명확한 목적을 가지고 매일 꾸준히 인공지능과 자동화를 활용하는 사람들이 있다는 거죠. 그래서 이제는 어떻게 하면 이 워크플로우를 바꿔서 시간을 절약하고 효율성을 높여 더 나은 품질과 이해 관계자 경험을 제공 |
| Unilever | 자사 채널 | [Investor Event 2024 CEO Presentation ／ Unilever](https://www.youtube.com/watch?v=r_BOLVAd0Kw) | 10 | 0 | 3 | 액센추어, 엔비디아와 같은 기술 파트너와의 협력을 통해 AI 기반 생산 자동화 및 노동 생산성 향상을 실현하고 있습니다. AI는 기업 전반에 걸쳐 생산성과 성장을 견인하고 있으며, 액센추어와 유니레버는 협력을 통해 효율성 향상과 획기적인 혁신을 가속화하고 있습니다. 유니레버의 인도 둠두마 공장에서는 최첨단 기술을 활용한  |
| Zapier | 자사 채널 | [Steal Zapier's AI Playbook for Accounting: How 8 People Run ](https://www.youtube.com/watch?v=CxrrXKFn6cg) | 8 | 2 | 3 | 이러한 자동화를 통해 달성한 결과 중 하나는 월말 결산 기간이 25% 단축되었다는 것입니다. 우리는 지난 몇 년 동안 Zapier의 동일한 내부 팀이 여러 가지 복잡한 요소, 새로운 법인, 통화, 빅4 회계법인 감사 등을 도입해 왔습니다. 저희는 매달 수십 건의 회계 전표 오류와 구매 전표 오류를 자동으로 발견하고 수정하 |
| 월가아재의 과학적 투자 | 미디어·검색 | [[월가아재] AI 혁명은 진짜다, 그런데 75년을 기다려야 한다? 스탠포드의 연구 ／ 채드 존스 2부](https://www.youtube.com/watch?v=OhiI-mQRVXA) | 12 | 0 | 0 | 아이디어 생산이 자동화되면은 성장은 가속이 되고 오형의 설정에 따라서 연 10%가 넘는 성장률도 가능하다. 그래서 존슨은 진지하게 이게 가능하다고 보고 있는데요. 연 10% 어느 정도냐? 지금의 2%에서는 생활 수준이 두 배가 되는데 한 세대 35년이 걸리는데 연 10%면은 초등학생이 중학생이 되는 사이 6, 7년 상간에 |
| Kotter International Inc | 미디어·검색 | [Why AI Projects Fail: Lessons from the US Army & Kotter ／ Ko](https://www.youtube.com/watch?v=jfpIvZy89UM) | 9 | 0 | 3 | 혹시 그런 경험이 있으시거나, 단순히 자동화하는 것과는 달리 프로세스를 재설계하는 방법에 대해 의견을 나눠주실 수 있을까요? 그래서 저는 맥킨지에서 가져온 ' 3단계 분석법'을 사용하는데, 처음에는 10% 정도의 변화를 통해 효율성을 얻는 방식입니다. 중간에는 연결고리가 있고, 그 너머에는 변혁적인 변화가 있습니다 . 때 |
| Zapier | 자사 채널 | [Defining AI Fluency: A Fireside Chat With The Executives](https://www.youtube.com/watch?v=Rq1lzDDfTrU) | 10 | 1 | 1 | Zap year's mission, make automation work for everyone. And I remember when I joined, you know, four and a half years ago, it was, you know, even back then known as like the most us |

- `transcripts/channels/Palantir/Paragon_2025__UjkRz9HkldU.md`
- `transcripts/channels/Zapier/How_Executive_Assistants_Drive_Strategic_Impact_with_AI__-gGwrSPc3tA.md`
- `transcripts/channels/Zapier/What_Netflix_Knows_About_AI_That_Every_Recruiter_Should_Lear__edY-3X18CHc.md`

### L-H-L — 데이터 없는 증강 (도구 배포에 그친 상태)  (223건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| SAP | 자사 채널 | [Global Keynote Highlights: Reimagined Joule, AI, & More in 1](https://www.youtube.com/watch?v=wU4FQd6Ps3Q) | 3 | 7 | 3 | 이러한 에이전트들이 모여 우리가 어시스턴트 또는 줄 어시스턴트라고 부르는 것을 형성합니다. 우리는 이러한 인공지능 비서들을 조직의 핵심 프로세스 전반에 걸친 역할에 배치했습니다. 왜냐하면 AI를 통해 가치를 실현하는 첫 번째 단계는 직원들이 더 많은 일을 더 잘하거나, 이전에는 불가능했던 일들을 할 수 있도록 지원하는 것 |
| 헬로티_매일 만나는 산업, IT News | 미디어·검색 | [AI 도입의 격차, 상위 5% 기업의 AI 활용 전략 - 마이크로소프트 백인송 이사 [AI TECH 2026](https://www.youtube.com/watch?v=p9Tj9ctxMr8) | 3 | 6 | 3 | 그리고 모빌리티, 통합 보안, 그리고 과거에 비해서 그런 PC에 단순히 저장하는 그런 내 데이터를 놔두는게 아니라 그 데이터들을 이제는 활용해서 어떻게 보면 인사이트를 얻고 우리 회사의 전략으로서 이제 활용할 수 있는 그런 데이터 기반의 업무 지원을 할 수 있는 그런 도구들도 필요할 겁니다. 요런게 잘 갖춰진 상태에서 이 |
| GitHub | 자사 채널 | [GitHub Copilot: Your AI Companion for Every Workflow](https://www.youtube.com/watch?v=DGt21BUu7qQ) | 4 | 8 | 0 | 코파일럿 CLI. 정말 놀랍습니다. 터미널을 사용하기 전까지는 이렇게 좋아하게 될 줄 몰랐는데, 솔직히 말해서 이제는 터미널 없이는 못 살겠어요. 슬랙이랑 팀즈에 있는 거죠? 팀원들과 대화를 나누거나, 팀즈를 통해 부조종사에게 무언가를 전달할 수도 있습니다. 꽤 멋지네요. DevOps, 기존 개발 방식, Jira 등 작업 |
| Intel | 자사 채널 | [Intel Keynote: AI Inside for a New Era ／ Intel](https://www.youtube.com/watch?v=8z9o2ltnFM0) | 0 | 11 | 1 | 2024년에는 코파일럿 플러스(Co-Pilot Plus)와 루나 레이크(Lunar Lake) PCS가 출시되었고, 윈도우 11 기반의 새로운 AI 혁신이 시작되었습니다. 코파일럿 플러스 PCS는 강력한 AI 성능을 갖춘 새로운 PC 카테고리로, 미래 PC의 생산성 향상 기준을 제시합니다. 마이크로소프트가 지금까지 만든 윈 |
| Microsoft Azure | 자사 채널 | [Grow Beyond Connectivity](https://www.youtube.com/watch?v=nt7II5sSzfQ) | 4 | 8 | 0 | 마이크로소프트 코파일럿은 통신사들이 AI를 통해 측정 가능한 수익을 창출할 수 있도록 지원하고 있습니다. Copilot은 일상적인 업무에서 발생하는 마찰을 제거함으로써 서비스 비용을 절감하고 판매 주기를 단축하며 음악 고객 평생 가치를 향상시킵니다. Work IQ는 조직 운영 방식, 고객 행동 방식, 가치 창출 지점을 파 |
| AI 전환공식 김건우 | 미디어·검색 | [AI 전환 (AX) 성공한 기업들은 무엇이 다를까? ／ JP모건·월마트 사례로 보는 AX 성공 공식 (AI ](https://www.youtube.com/watch?v=-B2A2gIxwIY) | 0 | 8 | 3 | 전사 업무 지원에 대한 제네를 만들었습니다. 150만 명 대산으로 AI 도구를 만들었고요. 기획하고 운영의 생산성을 향상했습니다. 그리고 공급망과 운영 AI에 대한 연결 지점들을 통합적으로 가져갔습니다. 여기서 포인트는요. 전사 업무 지원 구조로 확대된다. 교육 시작 자체는 특정 부서와 공통적인 부분들을 먼저 지점을 찾았 |
| Cohere | 자사 채널 | [Zhiwen Fan -  VLM 3R  Vision Language Models Augmented with ](https://www.youtube.com/watch?v=u86HPX5pJg8) | 4 | 6 | 1 | So today topic is about varian language model augmented with the instruction align 3D reconstruction. So the motivation of this work is kind of clearance and symbol. So how to enha |
| GitHub | 자사 채널 | [Run code generation in the background with GitHub Copilot co](https://www.youtube.com/watch?v=S1ch_6fjp5M) | 1 | 9 | 1 | 상황을 설명하고 코파일럿 코딩 에이전트를 소개하기 위해 간단히 말씀드리겠습니다. 모든 분들이 이 프로그램을 보거나 사용해 보신 건 아닐 테니까요 . Copilot 코딩 에이전트는 에이전트 모드, VS Code 또는 Copilot CLI와 같은 코딩 에이전트이지만, 로컬 저장소와 로컬 상태를 사용하는 컴퓨터의 환경에서 실행 |

- `transcripts/channels/SAP/Global_Keynote_Highlights_Reimagined_Joule,_AI,_&_More_in_14__wU4FQd6Ps3Q.md`
- `transcripts/2026-07-29/AI_도입의_격차,_상위_5%_기업의_AI_활용_전략_-_마이크로소프트_백인송_이사_[AI_TECH_2026__p9Tj9ctxMr8.md`
- `transcripts/channels/GitHub/GitHub_Copilot_Your_AI_Companion_for_Every_Workflow__DGt21BUu7qQ.md`

### L-L-H — 데이터만 쌓인 상태 (활용 미달)  (257건)

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| AWS Events | 자사 채널 | [A leader's guide to data strategy in the era of agentic AI ／](https://www.youtube.com/watch?v=3XyNPfWWxiQ) | 3 | 0 | 13 | 가트너는 2027년까지 데이터 거버넌스 이니셔티브의 80%가 실패할 것이라고 경고합니다. 정말 놀라운 수치입니다. 잠시 생각해 보세요. 값비싼 데이터 레이크는 제대로 활용되지 못하는 자산으로 남아 있습니다. 실제로 많은 조직들이 데이터의 가치보다 데이터의 양을 우선시해 왔습니다. 전직 CIO로서 말씀드리자면, 네, 저도  |
| Schneider Electric | 자사 채널 | [End of Islands - Unified Asset Lifecycle is the Digital Fabr](https://www.youtube.com/watch?v=xjFSF4jCvpk) | 2 | 2 | 11 | 개념 증명보다는 투자 수익률(ROI)을 제공하는 효과적인 사용 사례가 점점 더 중요해지고 있으며, 데이터 모델링 측면에서 프로세스와 전력 데이터 통합을 실현 하고 사용 사례를 제공할 수 있다는 것은 우리가 에너지 손실 의 근본 원인을 분석할 수 있음을 효과적으로 입증하는 것입니다 . 장비 성능의 근본 원인을 분석하고 ,  |
| AWS Events | 자사 채널 | [NYC Executive Forum 2026 - A Leader’s Guide to Data Strategy](https://www.youtube.com/watch?v=Piy37om0y6A) | 0 | 0 | 14 | 실제로 가트너는 데이터 거버넌스 프로젝트의 80%가 실패할 가능성이 높다고 말합니다. 데이터에 막대한 투자를 하고 수백만 달러를 쏟아부었음에도 불구하고, 우리는 여전히 곳곳에 제대로 활용되지 않는 데이터 레이크 문제로 어려움을 겪고 있습니다 . 하지만 이제 문제는 우리가 이 문제에 접근하는 방식이 완전히 잘못된 것은 아닌 |
| Weaviate | 자사 채널 | [Vertex AI RAG Engine with Lewis Liu and Bob van Luijt - Weav](https://www.youtube.com/watch?v=0HUCQkpQcPM) | 3 | 0 | 11 | 예를 들어, 말씀하신 것처럼 증류 과정을 모니터링하거나, RAG( Vertex Rag Engine)처럼 다양한 청킹 전략이나 임베딩 방식 등을 적용해서 어떤 모델을 선택할지 결정할 때, LLM을 활용하면 어떤 메타 최적화를 할 수 있을까요? 랙 엔진의 최적 구성을 조정하는 것에 관심이 있으신가요? 네, 물론이죠. 지금 랙 |
| 티타임즈TV | 미디어·검색 | [AI 도입을 위한 데이터 거버넌스 구축 전략은? (김유신 상무)](https://www.youtube.com/watch?v=vH_g9HIm154) | 0 | 2 | 11 | 그래서 데이터가 어느 정도 쌓여 있다라고 하는 기업에서는 데이터 거버넌스를 다시 한번 살펴보고 구축할 필요가 있습니다. 데이터 사일로 문제를 해결하자면 기술적뿐만 아니라 문화적인 측면도 있습니다. 조직이나 시스템 간의 데이터가 개별적으로 관리되다 보니 이런 서로의 데이터들에 대해서 이야기를 하지 않거나 교류가 되지 않는  |
| LG AI Research | 자사 채널 | [LG AI Talk Concert 2022 ／ Expert AI Applications for Custome](https://www.youtube.com/watch?v=5k4ncKiJCLw) | 0 | 1 | 12 | 의 성능은 초기 목표 수준을 달성하였고 국내 최고 수준이라는 경쟁사의 비실시간 엔드텐드 st의 성능을 뛰어넘고 있습니다 또한 실제 lg전자 상담원의 정성평가에서도 5점 만점 중 4.4점으로 대부분 이해가 용이한 수준 이상으로 평가되었습니다 TA 또한 각각의 기능별로 목표 수준과 기존의 소타 모델인 로베르타 라지나 코바토와 |
| SAP | 자사 채널 | [What’s New in SAP HANA Cloud ／ Deep Dive with Product Expert](https://www.youtube.com/watch?v=QrGR38jGGZo) | 4 | 0 | 9 | 저희는 온렘(onrem)에서 HANA 클라우드로 데이터를 복제하고 있기 때문에, 가장 큰 이점은 데이터 접근 시 지연 시간이 줄어들고, ABAB 및 ABBA 시맨틱스를 완벽하게 준수하는 ABOP SQL을 지원한다는 것입니다 . 또한 RTR과의 주요 차이점은 특정 조건에 따라 필터링할 수 있고, 필요한 열만 선택하여 HAN |
| Databricks | 자사 채널 | [Data + AI Summit Keynote 2026 ／ Day 1](https://www.youtube.com/watch?v=Qux8E-L1mk8) | 4 | 1 | 7 | 건축학 우리는 60개 이상의 데이터 레이크를 보유하고 있었는데, 이제는 하나가 되었습니다. 레이크하우스는 지금 운영 중입니다 데이터브릭스. 그리고 또한 ~로부터 음 단일체 구조에서 진정한 플러그형 레고 기반 아키텍처. 저것 우리에게 있어서 변화는 진정으로 우리가 어떻게 변화하는가를 의미합니다. 데이터가 지닌 가치를 활용하 |

- `transcripts/channels/AWS_Events/A_leader's_guide_to_data_strategy_in_the_era_of_agentic_AI_A__3XyNPfWWxiQ.md`
- `transcripts/channels/Schneider_Electric/End_of_Islands_-_Unified_Asset_Lifecycle_is_the_Digital_Fabr__xjFSF4jCvpk.md`
- `transcripts/channels/AWS_Events/NYC_Executive_Forum_2026_-_A_Leader’s_Guide_to_Data_Strategy__Piy37om0y6A.md`

### L-L-L — manual isolated data scarcity (논문 명명)  (1909건)

⚠️ 이 셀은 '조직이 그 상태'라는 뜻이 아니라 **세 축 어느 쪽도 강조하지 않은 발화**라는 뜻이다. 코퍼스의 69%가 여기 몰린다 — 담론 자료를 성숙도 진단으로 오독하면 안 되는 이유.

| 사례(채널) | 구분 | 영상 | 자동화 | 증강 | 데이터 | 근거 발췌 |
|---|---|---|---|---|---|---|
| ERP Suites | JD Edwards  | 미디어·검색 | [Enterprise AI: From Big Uncertainty to Massive ROI](https://www.youtube.com/watch?v=FmcULDfEgvM) | 3 | 2 | 3 | 그러니까 공급업체 요청서 나 고객 요청서 같은 게 있다면, 그걸 자동화할 수 있는 방법이 있어요. 정말 간단해요. 문서를 입력하면 AI 레이어가 그 문서를 이해하죠. 물론 몇 가지를 가르쳐줘야 해요. 로봇이니까 학습하는 거죠. 저는 AI를 '오케 스트레이터'라고 부르는 것보다 '인턴'이라고 부르는 게 더 좋아요. AI 인 |
| SAP | 자사 채널 | [Customer Success Keynote: Connected to Win: From Moment to M](https://www.youtube.com/watch?v=WpDHkeHIezc) | 4 | 1 | 3 | 그래서 저희 도매 주문의 80%는 자동화되어 있습니다. 자동으로 흐릅니다. 하지만 저희는 규모가 작은 소매업체들과도 많이 협력하고 있습니다. 그리고 주문의 20%는 수작업으로 처리됩니다. PDF, 이메일, 엑셀, 상상해 보세요. 그리고 긴 주문이라면, 사이즈, 색상 조합, 스타일 등을 말씀하시는 겁니다. 그건 정말 큰일일 |
| Snowflake | 자사 채널 | [The AI Blueprint for the Next Decade ／ BUILD 2025 Luminary C](https://www.youtube.com/watch?v=-HWNc-Hd90U) | 4 | 1 | 3 | 백그라운드에서 실행되도록 하여 추론 비용 측면에서 가장 큰 모델에 항상 더 많은 비용을 지출하지 않도록 함으로써, 이를 사용하여 자동화를 구현하는 개발자들의 비용을 절감할 수 있도록 하는 것입니다. 그래서 저는 앞으로 이 분야가 계속 진화할 것이고, 개방형 모델이 그 과정 에서 정말 중요한 역할을 할 것이라고 생각합니다. |

- `transcripts/2026-08-03/Enterprise_AI_From_Big_Uncertainty_to_Massive_ROI__FmcULDfEgvM.md`

## 3. 기업(자사 채널)별 큐브 좌표

영상 단위 점수를 채널별 상위 5건 평균(top5)으로 집계했다 — '그 조직이 가장 강하게 말할 때'의 수준. 상대 절단점(중앙값 분할): 자동화 4.0, 증강 2.0, 데이터 2.6.

| 기업(채널) | n | 자동화 | 증강 | 데이터 | 셀(상대) | 셀(논문절단점) |
|---|---|---|---|---|---|---|
| SAP | 79 | 8.8 | 8.0 | 8.6 | H-H-H | L-L-L |
| Zapier | 132 | 13.0 | 5.8 | 5.8 | H-H-H | H-L-L |
| Weights & Biases | 88 | 8.2 | 7.6 | 7.8 | H-H-H | L-L-L |
| Pinecone | 46 | 3.8 | 8.0 | 10.4 | L-H-H | L-L-H |
| Intel | 62 | 8.8 | 7.6 | 5.8 | H-H-H | L-L-L |
| Microsoft Azure | 51 | 6.8 | 7.4 | 6.6 | H-H-H | L-L-L |
| Siemens | 50 | 9.8 | 3.8 | 6.2 | H-H-H | H-L-L |
| AWS Events | 26 | 7.6 | 3.4 | 8.6 | H-H-H | L-L-L |
| Databricks | 65 | 6.8 | 4.2 | 8.6 | H-H-H | L-L-L |
| Weaviate | 55 | 4.6 | 5.2 | 9.4 | H-H-H | L-L-H |
| Cohere | 61 | 6.8 | 5.4 | 7.0 | H-H-H | L-L-L |
| McKinsey & Company | 89 | 9.8 | 4.0 | 4.4 | H-H-H | H-L-L |
| NVIDIA Developer | 85 | 4.6 | 4.8 | 8.4 | H-H-H | L-L-L |
| Snowflake | 57 | 6.0 | 2.0 | 9.0 | H-H-H | L-L-H |
| Google Cloud Tech | 69 | 5.6 | 3.6 | 7.4 | H-H-H | L-L-L |
| LG AI Research | 25 | 6.6 | 2.6 | 7.4 | H-H-H | L-L-L |
| Qdrant | 32 | 4.4 | 4.6 | 7.4 | H-H-H | L-L-L |
| ServiceNow | 45 | 8.8 | 2.8 | 4.6 | H-H-H | L-L-L |
| Palantir | 51 | 8.2 | 2.4 | 4.8 | H-H-H | L-L-L |
| Nokia | 45 | 9.8 | 0.2 | 4.4 | H-L-H | H-L-L |
| Salesforce | 63 | 6.0 | 3.4 | 5.0 | H-H-H | L-L-L |
| NAVER Cloud | 31 | 4.0 | 3.6 | 6.8 | H-H-H | L-L-L |
| IBM Technology | 46 | 5.2 | 4.6 | 4.4 | H-H-H | L-L-L |
| GitHub | 33 | 3.8 | 8.2 | 1.2 | L-H-L | L-L-L |
| Huawei | 49 | 5.6 | 1.4 | 6.2 | H-L-H | L-L-L |
| Mistral AI | 10 | 4.8 | 3.6 | 4.4 | H-H-H | L-L-L |
| NVIDIA | 49 | 4.8 | 2.6 | 5.2 | H-H-H | L-L-L |
| AWS Developers | 53 | 4.2 | 2.8 | 5.2 | H-H-H | L-L-L |
| Oracle | 32 | 5.0 | 0.4 | 6.0 | H-L-H | L-L-L |
| Apple Developer | 41 | 3.6 | 5.0 | 2.8 | L-H-H | L-L-L |
| Alibaba Cloud | 18 | 5.4 | 0.8 | 4.8 | H-L-H | L-L-L |
| kakao tech | 18 | 5.2 | 0.0 | 5.6 | H-L-H | L-L-L |
| Anthropic | 26 | 5.4 | 2.8 | 1.8 | H-H-L | L-L-L |
| OpenAI | 32 | 5.8 | 2.0 | 2.2 | H-H-L | L-L-L |
| Meta Developers | 33 | 3.6 | 4.4 | 1.6 | L-H-L | L-L-L |
| Replit | 28 | 6.2 | 1.4 | 1.8 | H-L-L | L-L-L |
| Schneider Electric | 35 | 4.8 | 0.4 | 4.2 | H-L-H | L-L-L |
| AMD | 29 | 2.8 | 4.8 | 1.6 | L-H-L | L-L-L |
| IQVIA | 37 | 2.6 | 1.2 | 5.2 | L-L-H | L-L-L |
| ElevenLabs | 28 | 4.0 | 2.0 | 2.8 | H-H-H | L-L-L |

전체 80개 기업: `analysis/aitf_company.csv`.


## 4. 수치 성과가 붙은 사례 발췌 (Impact 항목 상위)

논문 Table 1의 Impact 문항('변혁적 영향을 미쳤다')에 대응하는, **수치가 붙은 주장**만 모았다. 인용 가치가 가장 높은 후보군이다. 수치는 발화자의 주장이며 검증된 값이 아니다.

| 채널 | 구분 | 영상 | Impact(3축 합) | 근거 발췌 |
|---|---|---|---|---|
| DATAVERSITY | 미디어·검색 | [Analythics Architecture:  Promising AI Use Cases for th](https://www.youtube.com/watch?v=JhbsIutTwXM) | 10 | 기업들은 자동화된 에이전트가 일상적인 문의에 대해 토큰을 과도하게 할당하는 것을 방지하는 방법을 알아내는 데 한 해를 보냈습니다. 모든 게 장밋빛만은 아니잖아요, 그렇죠? H&amp;M은 고객 서비스를 제공하는데, 대화형 AI 챗봇을 활용하죠 ? 이 시스템은 대량의 고객 문의를 자동으로 처리하고 해결하여 전환율을 25% 향상시켜 직접적인  |
| Weights & Biases | 자사 채널 | [What’s the path to AGI? A conversation with Turing Co-f](https://www.youtube.com/watch?v=DJS7cop0CCw) | 10 | 예를 들어 언더라이팅 코파일럿은 성공적이었고, 그 덕분에 클레임 처리 코파일럿도 구축해 달라는 요청을 받았습니다. 많은 기업들이 여전히 ROI를 정확하게 측정하는 방법을 고민하고 있는 것 같습니다. 그리고 한 가지 어려운 점은 이러한 시스템이 대규모로 운영될 경우 많은 기업의 인력 수요가 줄어들 수 있다는 점입니다. 이로 인해 약간의 긴장 |
| SAP | 자사 채널 | [Global Keynote: The Beginning of Better ／ SAP Sapphire ](https://www.youtube.com/watch?v=CocpyxAizwE) | 9 | These AI systems take care of the most complex tasks, including data migration, test automation, or business process re-engineering. All in all, we are aiming to reduce migration efforts by  |
| Y Combinator | 미디어·검색 | [How AI Is Changing Enterprise](https://www.youtube.com/watch?v=aIKfA3gIXwo) | 8 | 그런데 이제 기업들은 이전에는 자동화하지 않았던 부분을 자동화하는 데 우선순위를 두게 될 거예요. 앞서 예시로 들었던 것처럼, 이 기술에 투자되는 돈은 사람들이 현재 하고 있는 일을 빼앗아 가는 게 아니라, 순전히 기존 업무에 추가되는 것뿐이에요. 소프트웨어의 활용 사례를 확장하는 것은 여러 가지로 연결될 수 있기 때문에, 향후 10년 안 |
| Databricks | 자사 채널 | [Unscripted: How Banks & Insurers Grow with Data, AI Age](https://www.youtube.com/watch?v=Vy5oNJgPdyQ) | 8 | 골드만삭스 리서치는 900개의 서로 다른 직업을 업무 수준에서 분석한 결과, 향후 미국 직업의 3분의 2, 즉 66%가 AI에 의한 자동화에 어느 정도 노출될 것으로 추정했습니다. 하지만 기업의 활용 사례를 살펴보면 몇 가지 냉혹한 현실이 드러납니다. AI를 어떤 규모로든 도입하고 있는 기업은 10%에 불과하며, 데이터브릭스에서도 매일 이 |
| Oracle | 자사 채널 | [Great Eastern Life Modernizes Data Platform with Oracle](https://www.youtube.com/watch?v=_aGhY3XJPtY) | 8 | 마지막으로, OCI [음악] 자율 AI 데이터베이스와 클라우드 네이티브 자동화를 통해 수작업을 줄이고 데이터 품질을 향상시키며 신뢰성, 확장성 및 전반적인 시스템 가용성을 강화했습니다. OCI를 통해 이러한 문제를 해결함으로써 10% 이상의 매출 성장을 달성했고 , 오라클의 클라우드 소비 모델을 통해 약 30%의 비용 절감을 이루었습니다  |
| SAP | 자사 채널 | [Global Keynote: The Beginning of Better ／ SAP Sapphire ](https://www.youtube.com/watch?v=9aa-etRsaLU) | 8 | 이러한 AI 비서들은 데이터 마이그레이션, 테스트 자동화, 비즈니스 프로세스 재설계 등 가장 복잡한 작업까지 처리합니다. 종합적으로, 우리는 이주로 인한 노력을 최대 50%까지 줄이는 것을 목표로 하고 있습니다. 마이그레이션을 더욱 빠르고 비용 효율적으로 만들어 드립니다. 이 내용은 내일 토마스와 얀이 진행할 고객 기조연설에서 더 자세히  |
| Weights & Biases | 자사 채널 | [GitHub CEO Thomas Dohmke on Copilot and the Future of S](https://www.youtube.com/watch?v=PPs5lZ2syv4) | 8 | 제 생각에는 상당 부분 자동화될 것입니다. 음, AI가 문서 작성이나 유닛 테스트 케이스 작성을 하는 것을 보면 이미 상당한 수준으로 작동하고 있습니다. 하지만 현실적으로 생각해 보면, 현재 가장 인기 있는 벤치마크인 ThreeBench와 SWBench는 12개의 Python 저장소에서 가져온 2,000쌍의 이슈와 풀 리퀘스트를 사용하는데 |
| 알컨연구소 | 미디어·검색 | [AI 상담봇 도입 실패하는 7가지 이유 ／ 도입 전 반드시 알아야 할 것들](https://www.youtube.com/watch?v=KFH0uH6DSSA) | 7 | 코그니지 에이젠 코파일럿은 상담 중 실시간으로 관련 정보와 응답 제한을 제공해 상담사의 업무 부담을 줄이고 해결률을 높힙니다. 일곱 번째 마지막 이유입니다. 성과 측정 체계가 없습니다. 74%의 CXAI 프로그램이 실패하는 근본 원인 중 하나가 바로 측정의 부제입니다. 98%의 컨택 센터가 AI를 도입했다고 말하지만 완전히 최적화된 전략을 |
| NVIDIA Developer | 자사 채널 | [Teach AI to Code in Every Language with NVIDIA NeMo ／ N](https://www.youtube.com/watch?v=d8yQ358u-rE) | 7 | 앞서 말씀드린 것처럼, 저희는 Hugging Face에서 제공하는 NeMo Tron 사전 학습 데이터 세트를 사용했습니다 . 음, 여기에서 영어 및 스페인어 위키피디아와 함께 사용한 여러 파일들을 보실 수 있습니다. 계획은 아주 간단합니다. 저희는 이러한 데이터 세트 중에서 콘텐츠의 71%는 코드, 약 9%는 수학, 일부는 영어와 스페인어 |
| Pinecone | 자사 채널 | [Semantic search and reranking with Cohere and Pinecone](https://www.youtube.com/watch?v=e7x1wJlmDjs) | 7 | 하지만 검색 결과 이후에 생성 모델을 사용하는 경우, 즉 검색 증강 생성을 사용하는 경우 애플리케이션의 전체 지연 시간을 줄일 수 있습니다. 생성 모델은 일반적으로 파이프라인에서 가장 용량이 큰 모델이기 때문에 생성 모델 에 전달하는 컨텍스트의 양을 줄이면 총 소유 비용(TCO) 측면에서 98%까지 절감할 수 있습니다. 랭커를 도입하는 것 |
| Unilever | 자사 채널 | [Unilever Investor Event 2024, Reginaldo Ecclissato, Chi](https://www.youtube.com/watch?v=ks7vFXlpsVA) | 7 | ' 운송 거리 줄이기 및 적재량 늘리기' 프로그램을 통해 효율성을 높이고 있으며, 자동화 이니셔티브를 활용하여 경로 와 적재 용량을 최적화하고 있습니다. 이미 평균 배송 거리를 15% 단축하고 트럭 활용률을 거의 10% 향상시켰습니다. 고객과 환경 모두에 이로운 AI 기반 인력 계획과 같은 인재 관리 이니셔티브를 추진하고 있습니다. 생성형 |
| MIT Corporate Relation | 미디어·검색 | [Integrating Generative AI Into Business Strategy: Dr. G](https://www.youtube.com/watch?v=9RvWcXVaAng) | 6 | 예를 들어 레모네이드(Lemonade)는 업무의 50%를 자동화하고, 위험도가 높은 업무는 50% 자동화합니다. 이러한 변화가 시작되고 있는 거죠. 그리고 기술 기업을 제외하고는 많이 볼 수 없는 것이 있는데, 바로 고객에게 직접적인 영향을 미치는 것입니다. 이를 어떻게 생각해 볼까요? 첫 번째 단계는 개인 생산성을 높이는 것입니다. |
| Databricks | 자사 채널 | [Agentic machine learning with Genie Code (includes demo](https://www.youtube.com/watch?v=C1rEj2VQtwU) | 6 | 머신러닝 산업은 항상 머신러닝 자동화에 관한 것이었고, 이제 우리는 마침내 그 과정을 구동할 인프라와 에이전트를 갖추게 되었습니다. 덕분에 머신 러닝을 100배 더 빠르게, 100배 더 많은 모델을 구축할 수 있게 되었고, 이제 우리는 비즈니스 전반의 모든 의사결정에 머신러닝을 적용하여 제품의 모든 부분에서 진정으로 개인화된 고객 경험을  |
| Infosys | 자사 채널 | [The Boardroom Mandate: Scaling AI for Business Impact ／](https://www.youtube.com/watch?v=0ixUiXr2DVY) | 6 | 자, Copilot은 바로 그런 역할을 합니다. 저희는 Copilot을 사용하는 고객들이 회의 시간을 13~14% 정도 절약한다고 생각합니다. 저희는 3,000명이 넘는 소프트웨어 개발자를 보유하고 있는데, 그중 상당수가 파트너사와 함께 GitHub 같은 소프트웨어 도구를 사용하며 생산성을 높이고 있습니다. 이런 경우에는 투자 대비 수익( |

## 5. 논문 3단계(path framing / narrating / stretching)용 후보

논문은 전환을 ① path framing(무엇을) ② path narrating(언제) ③ path stretching(어떻게 넓힐지)의 3단계로 서술한다. 각 단계에 대응하는 하위항목이 강한 문서를 후보로 붙인다. (하위항목↔단계 대응은 본 매핑의 해석이지 논문의 규정이 아니다.)


**path framing** — Level 항목(무엇을 AI로 바꿀지 정의하는 진술)

| 채널 | 영상 | 해당 항목 점수(3축 합) | 근거 발췌 |
|---|---|---|---|
| IBM Technology | [10 Use Cases for AI Agents: IoT, RAG, & Disaster Respon](https://www.youtube.com/watch?v=Ts42JTye-AI) | 12 | 인사 담당자는 워크플로 자동화의 중요성을 강조합니다. 이들은 Workday나 SAP와 같은 기업 시스템과 통합하여 신입 직원 온보딩과 같은 여러 단계의 프로세스를 자동으로 실행합니다 . IT 운영 측면에서 에이전트는 자동화된 문제 해결 기능을 사용하여 수천 건의 시스템 |
| Microsoft Azure | [Optimize Azure Storage costs: smart tier, automation, a](https://www.youtube.com/watch?v=QOcCdyL1lLY) | 10 | 따라서 현재 데이터 환경을 파악하고 스토리지 용량을 적절하게 조정하는 자동화된 방법을 마련하는 것은 데이터가 계속 증가함에 따라 지속 가능한 비용 절감을 달성하는 데 매우 중요합니다 . Azure 스토리지는 엑사 바이트 규모의 데이터와 수조 건의 트랜잭션을 처리할 수  |
| Pinecone | [Getting started with Pinecone monthly webinar (November](https://www.youtube.com/watch?v=pY_7RSUnotk) | 10 | 사실 저는 얼마 전에 PC를 조립하면서 어시스턴트를 가지고 뭔가를 시험해 보고 있었는데, 데이터베이스에서도 비슷한 방식으로 작동할 겁니다. 어, 그리고 저는 NLP를 사용한 것도 아니고, 오픈 AI 모델을 사용했습니다. 그래서 저는 비디오 파일에서 오디오를 추출하고,  |
| SAP | [Global Keynote: The Beginning of Better ／ SAP Sapphire ](https://www.youtube.com/watch?v=CocpyxAizwE) | 10 | These AI systems take care of the most complex tasks, including data migration, test automation, or business process re-engineering. All in all, we ar |
| ServiceNow | [Whiteboard 2.0 with Michael Park](https://www.youtube.com/watch?v=ZPlxlFY3qVM) | 10 | So, in the workflow layer, we continue to build deterministic workflows that are also augmented with the AI assistance to really tackle workflow autom |

**path narrating** — Future 항목(시간 순서·로드맵으로 서술한 진술)

| 채널 | 영상 | 해당 항목 점수(3축 합) | 근거 발췌 |
|---|---|---|---|
| NAVER Cloud | [[네이버클라우드 금융 컨퍼런스 2023] 생성형 AI 금융권 적용을 위한 제언 (네이버클라우드 한지](https://www.youtube.com/watch?v=WHqev4BHYEI) | 10 | 해 많이 쓰고 있는 것처럼 여러분들이 앞으로 업무에는 이런 AI 함께 병행하면서 업무 를 할 수 있는 이런 환경들로 추세가 변하 있다는 거를 보실 수 있습니다 어 이렇게 변화는 생성형 AI 통해서 여러분들이 어떻게 어 금융의 업무에 적용할 수 있는지 인사이트를 같이 한 |
| SAP | [Global Keynote: The Beginning of Better ／ SAP Sapphire ](https://www.youtube.com/watch?v=9aa-etRsaLU) | 10 | 이러한 AI 비서들은 데이터 마이그레이션, 테스트 자동화, 비즈니스 프로세스 재설계 등 가장 복잡한 작업까지 처리합니다. 종합적으로, 우리는 이주로 인한 노력을 최대 50%까지 줄이는 것을 목표로 하고 있습니다. 마이그레이션을 더욱 빠르고 비용 효율적으로 만들어 드립니 |
| Intel | [AI’s Next Frontier: Human Collaboration, Data Strategy,](https://www.youtube.com/watch?v=hFTRv3Va5IE) | 9 | 하지만 좀 더 짧은, 그러니까 향후 2~3년 주기로 보면, 우선 단순 자동화에서 심층 증강으로 초점이 옮겨갈 거라고 생각합니다. 다시 말해, AI가 사람들의 업무를 더 효율적으로 만들어주는 것이죠. 소프트웨어 개발자부터 마케팅 관리자, 재무 분석가까지 모든 직원에게 진 |
| Pinecone | [Production Ready RAG in Healthcare with Pinecone and Au](https://www.youtube.com/watch?v=93f7ZHPkpTk) | 9 | 음, 그럼 이제 검색 증강 생성이 무엇인지에 대해 이야기해 보겠습니다. 그럼 다음 슬라이드로 넘어가죠. 음, 안드라 카르파티의 트윗이 있는데요, [목을 가다듬으며] 음, 제 생각엔 시간이 지나도 여전히 괜찮은 것 같아요. 음, 그리고 기본적인 전제는 사람들이 LLM에  |
| Waymo | [Scale AI’s TransformX Fireside Chat with Waymo co-CEO D](https://www.youtube.com/watch?v=wF8m2Wt1Ij8) | 9 | 그리고 데이터 증강이나 시뮬레이션 같은 다양한 기법을 활용해서 이러한 사례들을 최대한 활용해야 합니다. 그래야 모델이 꼬리 부분까지 더 깊이 파고들 수 있죠. 물론 이 모든 과정을 자동화하는 것도 중요합니다. 프레임워크와 머신러닝 인프라에 투자하는 것도 저희의 주요 영 |

**path stretching** — Scope 항목(전사·전 부서로 넓히는 진술)

| 채널 | 영상 | 해당 항목 점수(3축 합) | 근거 발췌 |
|---|---|---|---|
| 삼성SDS AX | [ChatGPT Enterprise 도입전략](https://www.youtube.com/watch?v=oXxq-xeAoJQ) | 7 | 채의 기본 원리와 활용 방식의 이해 및 업무 적용 역량을 강화하고 프롬프트 활용과 반복 업무 자동화 시술을 통해 생산성과 업무 효율 향상을 지원합니다. 그리고 전문 분야별 채치 활용 전략 및 적용 방안을 제시하여 조직 내 AI 활용 확산과 실무 적용 자신감을 제고합니다 |
| Microsoft Learn | [Prepare for Microsoft Certification Exam AB-731: AI Tra](https://www.youtube.com/watch?v=mj_lyhuWbig) | 5 | So Copilot is for using AI. Foundry is for running and managing AI at scale. You'll need to know how to map specific pre-built capabilities for langua |
| Vertesia | [Enterprise strategies for agentic AI adoption in 2026 a](https://www.youtube.com/watch?v=B4WgQotMVmE) | 5 | Uh that's an acronym for retrieval augmented generation. Um so if you were to think you know if you follow the Iron Man movies this is our Jarvis. Um  |
| Cole Medin | [The Complete AI Transformation Blueprint - Live Worksho](https://www.youtube.com/watch?v=OcTMwjqje5Q) | 5 | So, like 1 to 4-hour sessions guiding enterprise teams on how to adopt a standard for using AI coding assistants across the organization. And that's a |
| Solutions Review | [Build, Test, and Deploy Production-Ready Enterprise AI ](https://www.youtube.com/watch?v=P0kux8A8NbM) | 5 | 당신은 조직 전체가 업무를 자동화할 수 있도록 지원하고 있습니다. 따라서 기업 사용자도 실제로 AI 에이전트 개발자가 될 수 있습니다. 이것이 바로 기업 전체에 AI를 확장하는 방법입니다. 세 번째 사용 사례 유형은 Informatica 플랫폼을 사용하는 IT 개발자, |

## 6. 한계

1. **담론 ≠ 성숙도.** 자사 채널 발화는 마케팅 목적이 섞인다. 논문 설문의 자기보고와도 다른 층위이므로, 두 자료를 같은 척도로 취급하면 안 된다.
2. **규칙 기반 코딩**이라 반어·부정·자막 오역에 취약하다(코드북 v2 §한계와 동일).
3. **상대 절단점은 코퍼스 의존적**이다. 표본이 바뀌면 셀 배치도 바뀐다. 논문 절단점 결과를 함께 보고하는 이유다.
4. 채널 단위 집계는 **기업 = 채널** 가정에 기댄다. 미디어·컨설팅 채널(source=keyword)은 기업 표에서 제외했다.

