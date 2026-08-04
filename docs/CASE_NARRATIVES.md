# 사례 서술 — 원본 스크립트 기반 (2026-08-04)

> `CASE_SELECTION.md`가 계량표이고 `CASE_PROFILES.md`가 요약본이라면, 이 문서는 **원본 유튜브
> 스크립트를 직접 정독해 쓴 서술본**이다. 사례 12건에 대해 12개 에이전트가 담당 채널의 스크립트를
> 끝까지 읽고 축어 인용을 수집했다.
>
> **검증**: 수집된 인용 411건 전부를 원본 파일과 문자열 대조했다. 411건 모두 실재한다(불일치 0건).
> 인용은 파일에 있는 그대로이며 요약·번역·다듬기를 하지 않았다. `&nbsp;` 잔여물만 공백으로 바꿨다.
>
> **읽는 법**: 모든 인용에 영상 제목·URL·**업로드일**을 붙였다. 업로드일은 각 파일 프론트매터의
> `업로드일` 필드이며 **행사 개최일이나 발화일이 아니다**(예: AIPCon 7 세션들은 행사 후 며칠에 걸쳐
> 순차 업로드됐다). 자막 언어도 표기했다 — `ko`로 표기된 것은 **영어·독일어·프랑스어 원발화의 기계
> 번역**이므로 화자의 축어가 아니다. 인용할 때 이 점을 반드시 명시해야 한다.

---

# 1. Palantir — 공통 언어의 소유권

## 1-1. 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-01-24 | en | [Chad Interviews Francisco: How Palantir Powers Supply Chain Operations](https://www.youtube.com/watch?v=R3al0e3f-Do) | 팔란티어 직원끼리의 사내 대담 |
| 2025-06-10 | en | [AI-Enabled Medical Operations: U.S. Department of State at AIPCon 7](https://www.youtube.com/watch?v=d3FmKfVpn8c) | 고객 단독 키노트 |
| 2025-06-13 | en | [AIG Underwriter Assistance in Action: AIG at AIPCon 7](https://www.youtube.com/watch?v=q4MSG5av4vk) | 고객 단독 키노트 |
| 2025-06-16 | en | [Backstage Pass: AIPCon 7](https://www.youtube.com/watch?v=_8RokabwNG8) | 백스테이지 토크쇼 |
| 2025-07-02 | en | [Chad & Colton: Operationalizing AI with Palantir AIP Evals](https://www.youtube.com/watch?v=iMF6cnU3o3o) | 제품 데모(가상 고객) |
| 2025-08-20 | en | [Chad & Agathe: AI Automation Across Procurement](https://www.youtube.com/watch?v=F57OKeI7JAU) | 제품 데모 |
| 2025-09-07 | en | [Reinventing IndyCar Race Performance: Andretti at AIPCon 8](https://www.youtube.com/watch?v=mBDQK7OJ1Ls) | 파트너십 출범 데모 |
| 2025-09-17 | en | [Chad & Chris: Tariff Savings and Compliance through Palantir AIP](https://www.youtube.com/watch?v=xBTPNLd8Jv8) | 제품 데모(가상 고객) |
| 2025-09-26 | en | [Chad & Bennett: Observability with Palantir AIP](https://www.youtube.com/watch?v=9IgYLjxxesw) | 제품 데모 |
| 2025-12-05 | ko | [Paragon 2025](https://www.youtube.com/watch?v=UjkRz9HkldU) | 고객 행사 전체 녹화 |

## 1-2. 이 사례가 보여주는 것

**온톨로지는 늘 '고객 고유의 것'으로 명명되지만 그 문법을 정의·유지·확장하는 주체는 팔란티어다.**
Andretti의 unique ontology, AIG's ontology, Kavanaugh의 TOM — 소유격은 언제나 고객에게 붙는다.
그런데 그 단어를 무대에서 꺼내는 사람은 팔란티어다.

이 교리의 이론적 정식화는 2025-01-24 사내 대담에 있다.

> "an llm is much like sort of Michelangelo um if you gave Michelangelo a toothpick and a block of marble you were going to go nowhere um the ontology is is the Chisel"
> — Francisco Parga(Apex 팟 리드, Palantir), [2025-01-24](https://www.youtube.com/watch?v=R3al0e3f-Do)

모델은 미켈란젤로이고 온톨로지는 끌이다. 즉 **모델은 상품이고 언어층이 가치를 소유한다**는 주장이다.

## 1-3. 화자 구조 — 이 사례의 핵심 발견

AIPCon은 스스로를 "고객 주도"로 규정한다. 그런데 그 규정 자체가 팔란티어 직원의 입에서 나온다.

> "A reminder, all of AIPCON... all of the content is customerled. All of this event is driven by customers."
> — Jack Dobson(AIP lead, Palantir), [2025-06-16](https://www.youtube.com/watch?v=_8RokabwNG8)

그리고 그 '고객 주도 행사'의 백스테이지 사회자는 독립 저널리스트가 아니다.

> "My name is Emit. I've been covering Palanteer for the better part of 5 years now."
> — 진행자, [2025-06-16](https://www.youtube.com/watch?v=_8RokabwNG8)

즉 발화 배치는 삼중이다. **팔란티어 직원이 사회·질문·데모 조작을 맡고, 고객은 답변·수치를 제공하며,
사회자 자리에는 팔란티어를 5년간 커버해온 유튜버가 앉는다.**

가장 결정적인 장면은 Andretti 편이다. 진행자가 농담 형태로 대본을 자기폭로한다.

> "this is now just a timing game to see how long it takes me to say the word ontology."
> — Jack Dobson, [2025-09-07](https://www.youtube.com/watch?v=mBDQK7OJ1Ls)

같은 세션의 실체는 '고객 사례'가 아니라 **계약 발표**였고, 구축 기간은 몇 주였다.

> "we're going to be kicking off the show with... a launch of the partnership between Palanteer and Andretti. We're going to be showcasing some of the work we've been building over just the last few..."
> — Jack Dobson, [2025-09-07](https://www.youtube.com/watch?v=mBDQK7OJ1Ls)

**발화 형식이 바뀌면 인정 가능한 실패의 양도 바뀐다.** 고객이 단독으로 키노트를 할 때만 실패사가 나온다.

> "the third attempt over 15 years to deploy our own electronic health record faltered."
> — Alan Lewis(미 국무부 의료프로그램 기술 책임자), [2025-06-10](https://www.youtube.com/watch?v=d3FmKfVpn8c)

## 1-4. 평가 병목 — 자사 제품 영상에서 나온 자인

`Chad & Colton | AIP Evals`(2025-07-02)는 이 사례에서 가장 값진 자료다. 자사 평가 제품을 홍보하는
영상이 동시에 그 한계의 실측치를 노출한다.

> "we have this this combination where GPTE 4.1 plus this structured checklist prompt option actually increases performance from zero to 50%... and again, 50% is not necessarily great"
> — Colton(forward deployed engineer, Palantir), [2025-07-02](https://www.youtube.com/watch?v=iMF6cnU3o3o)

평가 기준이 사전에 존재하지 않는다는 자인도 같은 영상에 있다.

> "users don't actually know what good looks like for something like say a summary that an AI system generates uh until they've actually seen it"
> — Colton, [2025-07-02](https://www.youtube.com/watch?v=iMF6cnU3o3o)

그리고 인간 검토의 비확장성.

> "it's not necessarily going to scale to check every single failing test case and debug the agents you know execution log"
> — Colton, [2025-07-02](https://www.youtube.com/watch?v=iMF6cnU3o3o)

**해법은 병목의 제거가 아니라 이전이다** — 에이전트가 에이전트를 디버그한다. 그리고 결론은
감사가능성을 경쟁우위로 전환하는 봉합구로 닫힌다.

> "This is why we win frankly. It's it's uh it's a core part of our platform."
> — Chad Walquist(아키텍트, Palantir), [2025-07-02](https://www.youtube.com/watch?v=iMF6cnU3o3o)

이 문장은 **시민자유팀 소속 화자와의 대화에서 나온다**. 거버넌스 언어와 영업 언어의 경계가 무너지는
지점이다.

## 1-5. 감사가능성의 비대칭

결정 이력이 온톨로지로 되먹임된다는 주장은 고객 발화로도 확인된다.

> "그리고 결정적으로 인간과 AI가 취한 모든 결정, 모든 행동, 모든 결정과 최종 결과가 온톨로지로 돌아간다는 것입니다. 따라서 에이전트는 시간이 지날수록 더 똑똑해집니다."
> — John Katzer(R1 엔지니어링 담당 수석 부사장), [2025-12-05](https://www.youtube.com/watch?v=UjkRz9HkldU) *(한국어 자동번역 자막)*

그런데 2025년 9월 말 시점에도 **'문제가 생겼을 때 알림을 받는' 기본 기능이 로드맵 상태**다.

> "I want to get paged and alerted when things go south. Um and I want to have confidence that I have a fully monitored system."
> — Bennett(observability 담당, Palantir), [2025-09-26](https://www.youtube.com/watch?v=9IgYLjxxesw)

## 1-6. 균열 — 반증이 교리로 재흡수되는 구조

Paragon 2025의 AIP Analyst 최초 시연에서 답이 틀렸음이 드러난다. 그런데 그 실패가 곧바로 교리 강화로
전환된다.

> "실제로 알려주는 것은 우리가 이 정보를 업데이트하지 않았다는 것입니다. 파운드리의 정말, 정말 멋진 점을 강조하고 있습니다. Foundry를 사용하기 위해 데이터가 정리될 때까지 기다릴 필요가 없습니다. Foundary를 사용하여 데이터를 정리하세요."
> — [2025-12-05](https://www.youtube.com/watch?v=UjkRz9HkldU) *(한국어 자동번역)*

같은 무대의 다른 발표는 시스템이 아직 절반만 지어졌다고 명시한다.

> "이제 빌드가 절반 정도 남았어요. 우리를 지금과 같은 위치에 이르게 한 모든 요소의 개념 증명은 모두 성공적이었지만, 이는 입원 환자의 관점에서 볼 때 환자 치료 과정의 아주 작은 부분에 불과합니다."
> — Tampa General Hospital 측 발표, [2025-12-05](https://www.youtube.com/watch?v=UjkRz9HkldU)

CEO 본인은 시장 침투 실패를 인정한다.

> "제 인생의 절반을 독일에서 보냈는데 지금 독일에서는 아무도 이런 것들에 관심이 없어요. 그건 정말 큰 문제예요."
> — Alex Karp(Palantir 공동설립자 겸 CEO), [2025-12-05](https://www.youtube.com/watch?v=UjkRz9HkldU)

**휴먼인더루프가 반드시 이용자 보호 장치가 아니라는 균열**도 있다. Johnson Controls 사례에서 인간의
승인 지점은 고객에게 불리한 번들링 제안이다.

> "따라서 유지 보수 계약이 없는 이 두 번째 장치는 첫 번째 유지 보수 계약에 패키지로 제공됩니다. 비즈니스에 더 좋습니다. 고객에게는 좋지 않은 일이죠."
> — [2025-12-05](https://www.youtube.com/watch?v=UjkRz9HkldU)

## 1-7. 인용 시 주의 (⚠️ 중요)

- **`Chad & X` 시리즈 4편(Evals·조달·관세·Observability)의 고객 데이터는 가상 기업 'Onyx Inc.'다.**
  화면 수치(관세 연 $88,000 절감, 100,000 유닛 등)는 **실측 성과가 아니라 시연용 설정값**이므로
  성과 증거로 인용하면 안 된다. 앞선 `CASE_PROFILES.md`에서 이 수치를 성과처럼 다룬 것은 오류다.
- 실제 고객 자기보고는 AIPCon 키노트(국무부·AIG)와 Paragon 발표뿐이다. 다만 무대가 벤더 행사이므로
  **실패한 배치는 무대에 오르지 않는다**는 선택 편향이 있다.
- 자막 오염: Palantir가 "Palanteer/Palunteer/Palatir"로, Bill of Materials(BOM)가 전편에 걸쳐
  "bomb"(폭탄)으로, evals가 "Ethiles/EVOS/EOS"로 훼손된다. Backstage Pass 편의 국무부 절감액은
  "$und00 million ion dollar"로 파손되어 **액수를 특정할 수 없다**.
- Paragon 2025는 한국어 기계번역 자막이다. "비밀 무기", "올인하세요" 같은 수사를 화자의 원 표현으로
  단정하면 안 된다.

---

# 2. Zapier — 분모의 사유화

## 2-1. 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-11-13 | en | [How Orium's AI Playbook Turned Complexity into 5x Growth (Agents of Scale)](https://www.youtube.com/watch?v=5st7XEHY_pA) | 자사 팟캐스트 |
| 2025-11-14 | ko | [Zapier AI Showcase: 50 Million Tasks Delegated](https://www.youtube.com/watch?v=pGjirCLK9qE) | 연례 쇼케이스 |
| 2025-11-24 | ko | [Zapier's Big AI Plans for 2026 Revealed!](https://www.youtube.com/watch?v=EfHm1Qjztd0) | 창사 14년 만의 첫 공개 올핸즈 |
| 2025-12-18 | en | [Defining AI Fluency: A Fireside Chat With The Executives](https://www.youtube.com/watch?v=Rq1lzDDfTrU) | 라이브 AMA |
| 2026-01-30 | ko | [AI for Marketers: How to Become a Content Engineer](https://www.youtube.com/watch?v=xk5Nd_FUJLI) | 마케터 웨비나 |
| 2026-05-20 | ko | [Steal Zapier's AI Playbook for Accounting](https://www.youtube.com/watch?v=CxrrXKFn6cg) | 회계팀 자동화 웨비나 |
| 2026-06-25 | ko | [Zapier AI Benchmark: How to choose the right AI model](https://www.youtube.com/watch?v=Zg3IU1cA0vU) | Automation Bench 발표 |
| 2026-07-22 | en | [The Good, the Bad, and the Ugly: Building an AI-First GTM Team](https://www.youtube.com/watch?v=tqnLffBM-og) | GTM 실패 공개 웨비나 |

## 2-2. 이 사례가 보여주는 것

**모델을 재는 자와 사람을 재는 자가 동일할 때 무엇이 일어나는가.** Zapier는 (a) 9,000개 앱을 잇는 연결
계층, (b) 모델을 줄 세우는 자체 벤치마크, (c) 사람을 줄 세우는 AI 유창성 프레임워크를 한 회사 안에서
운영한다.

## 2-3. Automation Bench — 측정 범위의 선택이 곧 주장이다

과제 표본을 의도적으로 편향시켰다는 자백이 발표 안에 있다.

> "저희는 Zapier 에서 봤던 워크플로 유형들을 선택했지만, 동시에 가장 어려운 워크플로 세트도 선택했습니다. 그래서 우리는 어떤 모델이 가장 뛰어난 성능을 발휘하는지 제대로 파악하기 위해 일부러 어려운 과제들을 선택했습니다."
> — 루카스 베르그스트롬(Automation Bench 제품 관리자), [2026-06-25](https://www.youtube.com/watch?v=Zg3IU1cA0vU)

그 결과 최고 점수는 70.17%다. 그런데 **낮은 실측치는 즉시 벤치마크의 권위로 전환된다**.

> "다시 말씀드리지만, 지금 보시는 성공률은 실제 운영 환경에서 보게 될 성공률보다 훨씬 낮습니다. 왜냐하면 저희는 의도적으로 가장 어려운 작업들을 선택해서 측정했기 때문입니다."
> — 루카스 베르그스트롬, [2026-06-25](https://www.youtube.com/watch?v=Zg3IU1cA0vU)

**무엇을 재지 않는지도 명시된다.**

> "Automation Bench는 챗봇 작업의 지연 시간을 측정하지 않기 때문에 오늘은 지연 시간에 대해 자세히 이야기하지 않겠습니다."
> — 루카스 베르그스트롬, [2026-06-25](https://www.youtube.com/watch?v=Zg3IU1cA0vU)

그리고 데이터셋 비공개가 신뢰성의 근거로 제시되지만, 그것은 동시에 **외부 검증 불가능성을 스스로
만드는 조치**다.

> "모델 테스트에 사용하는 데이터가 인터넷에 공개되지 않도록 하는 등의 조치를 취해야 했습니다... 데이터가 인터넷에 공개되면 새로운 모델의 학습 데이터로 사용되기 시작하고, 그러면 벤치마크가 더 이상 실질적인 유용성을 잃게 되기 때문입니다."
> — 루카스 베르그스트롬, [2026-06-25](https://www.youtube.com/watch?v=Zg3IU1cA0vU)

## 2-4. AI 유창성 — 규범에서 채용 요건으로

> "So we started assessing for AI fluency in the spring of this year... for 100% of applicants and 100% of jobs that we hire into the company"
> — Brandon Sammut(Chief People and AI Transformation Officer, Zapier), [2025-12-18](https://www.youtube.com/watch?v=Rq1lzDDfTrU)

프레임워크 오픈소스화는 투명성 언어로 포장되지만 **실질은 평가 표준의 선점**이다.

> "Zapier open sourced its AI fluency framework. It's effectively the framework we use to assess candidates and we don't want that to be a secret."
> — Brandon Sammut, [2025-12-18](https://www.youtube.com/watch?v=Rq1lzDDfTrU)

**그리고 그 표준화가 실제로 작동했다는 증거가 같은 코퍼스 안에 있다.** 외부 기업 CEO가 그 프레임워크를
자사 인사에 쓰고 있다고 증언한다.

> "it's actually um a framework that uh I think we took from a post that that Zapier had done a few months ago and we've been using it for most of this year um with our own team."
> — Jason Cottrell(CEO of Orium, President of MACH Alliance), [2025-11-13](https://www.youtube.com/watch?v=5st7XEHY_pA)

프레임워크 배포가 곧 **채용 시장의 언어를 선점하는 행위**임이 자기 코퍼스로 입증된다.

## 2-5. 위임 서사의 두 층위

대외적으로는 규모다.

> "네, 고객님과 같은 약 40만 명의 고객이 AI와 Zapier를 사용하여 5천만 건 이상의 작업을 위임했습니다."
> — 웨이드 포스터(Zapier 공동 창립자 겸 CEO), [2025-11-14](https://www.youtube.com/watch?v=pGjirCLK9qE)

실무 층위로 내려가면 정반대 원칙이 나온다.

> "저희는 회계와 관련된 어떤 사안에 대해서도 인간의 승인 절차 없이 인공지능이 최종 결정을 내리도록 허용하지 않습니다."
> — 라이언(Zapier CFO), [2026-05-20](https://www.youtube.com/watch?v=CxrrXKFn6cg)

**위임의 목적이 '대체'가 아니라 '감사 가능성'으로 이동한다.**

> "자동으로 게시되도록 설정할 수도 있지만, 그렇게 하지 않기로 했습니다. 이는 제한 사항이 아니라 궁극적으로 우리의 감사 증거가 됩니다."
> — 라이언(CFO), [2026-05-20](https://www.youtube.com/watch?v=CxrrXKFn6cg)

## 2-6. 실패의 귀속과 자기반증

실패는 일관되게 사람과 조직으로 향한다.

> "제 생각에는 이러한 AI 도입 의 80%가 실패하는 이유 중 하나가 바로 이 부분, 즉 실제로 어떻게 사용해야 하는지 또는 왜 사용해야 하는지에 대해 아무도 가르쳐주지 않기 때문에 발생하는 문제라고 생각합니다"
> — 라이언 맥크레디(콘텐츠 엔지니어, 외부 게스트), [2026-01-30](https://www.youtube.com/watch?v=xk5Nd_FUJLI)

> "케이트, 방금 설명하신 게 바로 제가 '위임의 함정'이라고 부르는 거예요."
> — 웨이드 포스터(CEO), [2025-11-24](https://www.youtube.com/watch?v=EfHm1Qjztd0)

**그런데 이 코퍼스에서 가장 강한 자기반증도 Zapier 자신에게서 나온다.** 2026-07-22 GTM 웨비나는
'모두가 빌더' 문화의 대가를 공개한다.

> "that's led to chaos in some cases and a lot of duplication of work um or half-completed projects or skills that are sort of like in a graveyard and not managed."
> — Lindsay Rothlessberger(GTM Innovation Lead, Zapier), [2026-07-22](https://www.youtube.com/watch?v=tqnLffBM-og)

> "I think we also failed to build a really strong operating model early on"
> — Lindsay Rothlessberger, [2026-07-22](https://www.youtube.com/watch?v=tqnLffBM-og)

위임의 인식론적 한계는 빌더 본인이 말한다.

> "I've never read through this whole thing. I have no idea. I'm like trusting that the AI has followed."
> — Sarah(AI Automation Engineer, Zapier), [2026-07-22](https://www.youtube.com/watch?v=tqnLffBM-og)

**성숙의 방향은 에이전트가 아니라 결정론으로의 회귀다.**

> "where I would really like to take this is moving it back towards determinism versus letting AI have like full reign over the information."
> — Sarah, [2026-07-22](https://www.youtube.com/watch?v=tqnLffBM-og)

자사 ROI 3요소 중 '효율성=시간절감'을 자사 엔지니어가 기각하기도 한다.

> "I just feel like it's not that impactful to say like we saved these people so much time. It's really hard to measure. And what are people doing with the time you're saving anyways?"
> — Sarah, [2026-07-22](https://www.youtube.com/watch?v=tqnLffBM-og)

그리고 노동 효과의 실체는 결원 미충원이다.

> "즉, 인력 이탈로 인해 없어진 모든 직책을 다시 채우지 않고도 더 효율적으로 규모를 확장할 수 있다는 뜻입니다."
> — 로렌 프랭클린(Zapier 지원 부문 부사장), [2025-11-24](https://www.youtube.com/watch?v=EfHm1Qjztd0)

## 2-7. 측정 체계가 측정 결과보다 먼저 온다

2026 스코어카드를 공개하면서 붙인 단서.

> "여기 있는 모든 데이터는 모의 데이터입니다. 합성 소재입니다. 아직 실제 점수가 아닙니다"
> — [2025-11-24](https://www.youtube.com/watch?v=EfHm1Qjztd0)

임원 스스로 초기 실험의 ROI가 음수일 것이라 인정한다.

> "if we were to do the ROI measurement today on some of these early experiments, it's probably negative."
> — Brandon Sammut, [2025-12-18](https://www.youtube.com/watch?v=Rq1lzDDfTrU)

**에이전트 마케팅을 주도하는 회사가 자사 사례에서는 에이전트를 버렸다.**

> "그리고 저희는 에이전트를 이용했을 때 비용이 더 많이 든다는 것을 알게 되었습니다. 제대로 작동하지 않았어요. 그래서 그런 식으로 코드를 작성해서, 즉 결정론적으로 만들면 그 문제가 해결됩니다."
> — [2026-06-25](https://www.youtube.com/watch?v=Zg3IU1cA0vU)

## 2-8. 인용 시 주의 (⚠️ 앞선 문서 교정)

- **"8명이 $5B 운영"은 스크립트 본문에 없다.** 전체 텍스트 검색 결과 "5B"는 **영상 제목 줄에만** 존재하고,
  팀 규모 질문에 대한 답변도 정확한 인원수를 밝히지 않는다. 이 수치는 반드시 **'영상 제목의 주장'**으로만
  표기해야 한다. `CASE_PROFILES.md`에서 이를 본문 근거처럼 인용한 것은 오류다.
- 고객에게는 벤치마크로 모델을 투명하게 고르라 하면서 자사 제품의 모델 구성은 공개하지 않는다
  ("저희는 정확히 어떤 LLM을 사용하고 있는지는 공개하지 않습니다", 2025-11-14).
- `pGjirCLK9qE`(2025-11-14)는 본문이 "다음 주 화요일인 5월 14일"을 반복 언급한다. **재업로드이거나 이전
  이벤트 녹화의 재발행**일 가능성이 크므로 업로드일을 발화 시점으로 단정하면 안 된다.
- 한국어 자막본의 모델명 표기("Anthropics Fable 5", "GBT 5.5", "쌍둥이자리"=Gemini)는 번역 산물이므로
  액면 인용을 피할 것.

---

# 3. ServiceNow — 등기소를 차지하는 전략

## 3-1. 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-09-12 | ko | [Introducing the ServiceNow AI Platform Zurich release](https://www.youtube.com/watch?v=D2CpKOknTSo) | 릴리스 웨비나 |
| 2025-09-24 | ko | [Michael Park's AI Whiteboard Masterclass](https://www.youtube.com/watch?v=0Fmw61s8CKc) | 파트너 세일즈 인에이블먼트 |
| 2025-10-01 | ko | [Introducing AI Experience by ServiceNow](https://www.youtube.com/watch?v=lrQylmrcbXs) | 제품 런칭 |
| 2025-10-27 | ko | [DRBench](https://www.youtube.com/watch?v=If-SA31vHFM) | 사내 연구 발표 |
| 2026-05-07 | ko | [Welcome to Agentic Business: Knowledge 2026 Opening Keynote](https://www.youtube.com/watch?v=jeo2V1w-Peg) | 연례 컨퍼런스 기조 |
| 2026-05-08 | ko | [The Blueprint for Agentic Business: Knowledge 2026 Day 2](https://www.youtube.com/watch?v=q8kaVEkTWho) | 아키텍처 키노트 |
| 2026-05-12 | ko | [EVA: Evaluating Voice Agents](https://www.youtube.com/watch?v=awnHL7AARZM) | 사내 연구 발표 |
| 2026-05-29 | en | [CUBE: From Benchmark Silos to an Interoperable AI Evaluation Ecosystem](https://www.youtube.com/watch?v=7wEYiwVsN_4) | 사내 연구 발표 |

## 3-2. 이 사례가 보여주는 것

**ServiceNow는 에이전트 계층에서 경쟁하지 않고 에이전트 '등기소'를 차지하려 한다.** 이 포지션은
2025년 9월 파트너 교육 자리에서 가장 노골적으로 진술된다.

> "ServiceNow 플랫폼의 데이터 모델에 AI 자산을 등록하기만 하면 모든 AI 자산에 대해 AI 컨트롤 타워 거버넌스를 적용할 수 있습니다. **ServiceNow의 AI를 사용하지 않아도 됩니다.**"
> — 마이클 파크(ServiceNow 채널·파트너십 담당), [2025-09-24](https://www.youtube.com/watch?v=0Fmw61s8CKc)

이 구조에서는 **경쟁사의 에이전트가 늘어날수록 자사 통제 계층의 가치가 커진다.** 2026년에는 관장 범위가
경쟁사 이름으로 확정된다.

> "이 시스템은 시중에 나와 있는 모든 모델, 에이전트, 데이터 세트, MCP 서버는 물론 모든 SaaS를 자동으로 검색하고 하나의 실시간 인벤토리에 목록화합니다. 여기에는 AWS, Google, Azure, Anthropic, OpenAI 등의 모델이 포함되..."
> — 아밋 자베리(사장 겸 COO·CPO), [2026-05-07](https://www.youtube.com/watch?v=jeo2V1w-Peg)

> "ServiceNow AI Control Tower가 이제 Microsoft Agent 365와 통합되었습니다... 플랫폼의 다른 모든 요소와 마찬가지로 동일한 거버넌스 관점을 적용합니다."
> — 아밋 자베리, [2026-05-07](https://www.youtube.com/watch?v=jeo2V1w-Peg)

Google Cloud 임원이 무대에 올라 **양방향 등록**을 설명하는 장면은, 이 전략이 상대방의 동의를 얻어냈음을
보여준다.

> "누군가가 에이전트를 생성하고 등록하면, 등록된 에이전트는 자동으로 Gemini Enterprise에 등록되어 Gemini Enterprise 콘솔에 표시됩니다."
> — 카르틱 나라인(Google Cloud), [2026-05-08](https://www.youtube.com/watch?v=q8kaVEkTWho)

## 3-3. 두 번째 층 — 평가 생태계의 등기소

관제탑이 **배포된 에이전트**를 등록·계량하는 장치라면, 연구 부문의 CUBE·EVA·DRBench는 그 앞단에서
**에이전트의 성능**을 등록·계량하는 장치다. 논리 구조가 동일하다.

> "So, we see as uh today, 2026, we have about 600 benchmark. And the forecast is going all the way to 900 benchmark by end of 2026."
> — Alexandre Lacoste(senior staff research scientist, ServiceNow AI Research), [2026-05-29](https://www.youtube.com/watch?v=7wEYiwVsN_4)

> "you can wrap a benchmark once and have it usable everywhere"
> — Alexandre Lacoste, [2026-05-29](https://www.youtube.com/watch?v=7wEYiwVsN_4)

'한 번 감싸면 어디서나 쓴다'(CUBE)와 '한 번 등록하면 모두 관장한다'(Control Tower)는 **같은 문장의 두
판본**이다. 그리고 중립성의 외양을 확보하는 방식도 정교하다.

> "we didn't want people to feel like they have to use our harness... you can swipe left and bring your own harness. For that, we also have direct support with Nvidia Nemo"
> — Alexandre Lacoste, [2026-05-29](https://www.youtube.com/watch?v=7wEYiwVsN_4)

## 3-4. 균열 — 키노트와 연구 부문의 정면 충돌

키노트는 '20년치 기업 맥락'을 최대 해자로 내세운다. 그런데 **자사 연구는 에이전트가 바로 그 기업 내부
정보를 못 쓴다고 보고한다.**

> "현재 에이전트들이 사전 지식이나 웹 지식에 지나치게 의존하고 있으며, 로컬 검색 공간 에서 기업별 정보를 제대로 활용하지 못하는 경우가 많다는 사실도 발견했습니다"
> — 티아니 첸(ServiceNow AI 연구소 응용연구과학자), [2025-10-27](https://www.youtube.com/watch?v=If-SA31vHFM)

음성 에이전트도 마찬가지다.

> "오늘날 음성 비서의 성능이 아직 일관적이지 않다는 점을 지적하고 싶습니다. 그래서 어떤 때는 테스트를 해보면 잘 작동하지만, 같은 시나리오에서 다시 테스트하면 실패하는 경우가 있습니다."
> — 타라 보글레벨리(ServiceNow 코어 LLM 그룹 연구원), [2026-05-12](https://www.youtube.com/watch?v=awnHL7AARZM)

에이전트 붐 한복판인 2026년 5월에, 자사 연구자가 불과 몇 달 전을 이렇게 회고한다.

> "one of my slide was where are the agents? Uh they were still very researchy, very brittle uh and no one was really..."
> — Alexandre Lacoste, [2026-05-29](https://www.youtube.com/watch?v=7wEYiwVsN_4)

**도입률의 낮은 실측치가 개막 선언 안에 들어 있다.**

> "실제로 10개 기업 중 6개 기업이 유전자 기반 AI를 사용하고 있지만, 자율 시스템을 구축한 기업은 10개 기업 중 단 한 곳뿐입니다. 대부분은 아직 제대로 활용하지도 못한 기능에 대해 비용을 지불하고 있다."
> — [2026-05-07](https://www.youtube.com/watch?v=jeo2V1w-Peg) *('유전자 기반 AI'는 generative AI의 오역)*

그리고 회사 정체성으로 격상시킨 바로 그 제품을 **1년간 무료로 푼다**.

> "이제 고객 여러분은 AI 관제탑을 무료로 이용하실 수 있습니다. 1년 동안. 이는 200만 달러 규모의 제안으로, 저희가 지금까지 제시한 제안 중 가장 큰 금액입니다."
> — [2026-05-07](https://www.youtube.com/watch?v=jeo2V1w-Peg)

가장 아이러니한 장면은 킬 스위치 데모다. **자사 마케팅이 자사가 파는 자율 에이전트의 위험을 가장
생생하게 증언한다.**

> "숨겨진 명령어가 포함된 프롬프트 주입으로 인해 이 AI 에이전트가 이전의 모든 가격 책정 규칙을 무시하고 배송비를 1달러로 설정하도록 지시받은 것 같습니다. 더 놀라운 건... 조정 내역을 기록하지 않도록 지시되어 있습니다."
> — [2026-05-07](https://www.youtube.com/watch?v=jeo2V1w-Peg)

고객은 이 제품을 완성품이 아니라 **공동 개발 중인 미완성물**로 묘사한다.

> "저희가 ServiceNow와 파트너십을 맺고 Control Tower에 기대를 거는 이유 중 하나는, 사람의 개입이 적은 영장 발부 시스템을 구축하고 있기 때문입니다. 너무 느려요."
> — 앨런 로사(CVS Health), [2026-05-08](https://www.youtube.com/watch?v=q8kaVEkTWho)

## 3-5. 인용 시 주의

- **Fortune 500 커버리지가 영상마다 다르다** — 92%(2025-09-24), 85%(2025-10-01), 90%(2026-05-07).
  어느 하나를 확정 수치로 인용하면 안 된다.
- 키노트 데모 화면의 수치(85% 평가 점수, 3,000시간, 52% 처리율, FedEx 2억 5천만 달러)는 **시연용
  시나리오일 가능성이 높다**. 실측치로 취급하면 안 된다.
- CUBE만 영어 원문 자막이고 나머지 7편은 한국어 기계번역이다. 'generative AI'→'유전자 기반 AI',
  'LLM'→'법학 석사' 같은 오역이 있다.
- CVS Health 고객 영상 구간은 `[음악]` 자막이 문장 내부에 삽입돼 있어 인용 근거로 부적절하다.

---

# 4. McKinsey — 눈금의 생산

## 4-1. 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-10-13 | en | [AI-Driven Consulting: Kate Smaje on Navigating the Future](https://www.youtube.com/watch?v=pomQmWBmbV0) | 채용 웨비나(Unpacked) |
| 2025-12-01 | ko | [Agentic AI and the Future of Travel](https://www.youtube.com/watch?v=dmKFLspjYNw) | 고객 대상 McKinsey Live |
| 2026-03-12 | ko | [MGI event: Industry leaders discuss how to advance adaptation](https://www.youtube.com/watch?v=MtevcjCnO1w) | 보고서 발표 웨비나 |
| 2026-04-29 | ko | [Rewired To Win: Reimagining the Enterprise With Tech and AI](https://www.youtube.com/watch?v=HoHFZ-Fzu_g) | 서적 프로모션 |
| 2026-05-14 | ko | [Building a World of Plenty](https://www.youtube.com/watch?v=o6Pb4mjf9eE) | 창립 100주년 저서 소개 |
| 2026-05-19 | ko | [Leading Through Transformation: Bob Sternfels](https://www.youtube.com/watch?v=R7baGOl1u4Y) | 채용 홍보 대담 |
| 2026-08-01 | en | [The Biggest AI Opportunity Isn't Replacing People (Brynjolfsson)](https://www.youtube.com/watch?v=u76xdhpF474) | 자사 팟캐스트 |

## 4-2. 눈금은 언제나 세 층으로 나온다

**(a) 도입률의 낮은 실측치** — 시장이 비어 있음을 증명한다.

> "약 30% 정도가 사업의 한 부분에서 실험을 시작하고 규모를 확장하고 있습니다... 하지만 아시다시피 40%는 '아직'"
> — Kelly Ungerman(McKinsey 여행·물류·인프라 부문 글로벌 공동 책임자), [2025-12-01](https://www.youtube.com/watch?v=dmKFLspjYNw)

**(b) 자동화 가능 시간·성과의 상한치** — 그 공백의 크기를 값으로 환산한다.

> "근무 시간에 10%에서 30% 정도의 영향이 있을 것으로 예상합니다"
> — Kelly Ungerman, [2025-12-01](https://www.youtube.com/watch?v=dmKFLspjYNw)

**(c) ROI 재계산 권고** — 지금 지출을 정당화한다.

> "그리고 마지막으로 말씀드릴 수치는, 투자하는 1달러당 평균 3달러의 수익을 올리고 있다는 것입니다."
> — Kate Smaje, [2026-04-29](https://www.youtube.com/watch?v=HoHFZ-Fzu_g)

셋을 이어붙이면 **'격차가 크다 → 값이 크다 → 지금 사라'**가 되고, **각 항의 출처는 모두 맥킨지 자신의
설문·모델**이다. 눈금 생산자의 자기인식도 스크립트에 있다.

> "우리가 내놓는 수치와 생각들은 모든 논의의 기본 토대가 됩니다... 대부분의 법학 석사(LLM) 과정 학생들에게 '풍요로운 미래가 가능할까요?'라고 물어보면 맥켄지의 '풍요의 세기' 이론이 나오고"
> — Sven Smit(McKinsey 전 시니어파트너, MGI 전 의장), [2026-05-14](https://www.youtube.com/watch?v=o6Pb4mjf9eE) *('법학 석사(LLM)'는 large language model의 오역)*

## 4-3. 분모/분자 프레임

이 사례의 이론적 축은 2025-10-13에 정식화된다.

> "I think the world is still too focused on efficiency, right? Just the one part of the productivity denominator."
> — Kate Smaje(McKinsey 시니어파트너, 기술·AI 글로벌 리더), [2025-10-13](https://www.youtube.com/watch?v=pomQmWBmbV0)

10개월 뒤 외부 경제학자가 같은 프레임을 학술 언어로 승인한다.

> "the way economists define productivity is, you know, it's output per input. And too many people... focus only on the input part of it."
> — Erik Brynjolfsson(스탠퍼드대 경제학 교수, HAI 디렉터), [2026-08-01](https://www.youtube.com/watch?v=u76xdhpF474)

**배수 수사의 핵심은 분모를 말하지 않는 데 있다.** 이 사례의 결정적 인용은 GMP의 발화다.

> "예전에 맥킨지 파트너였던 전 CEO가 맥킨지의 훌륭한 업무는 수수료 대비 10배의 수익을 가져다준다고 이야기했었죠. 제 생각에 우리가 지금 빠져 있는 건 100배 수익률인 것 같아요."
> — Bob Sternfels(McKinsey 글로벌 매니징 파트너), [2026-05-19](https://www.youtube.com/watch?v=R7baGOl1u4Y)

분모(수수료·인력)는 고정한 채 분자만 열 배 올린다.

## 4-4. 균열 — 눈금이 발화자를 거치며 팽창한다

**같은 웨비나 한 편 안에서 비용편익비가 세 번 바뀐다.** 연구 발표자 본인은 이렇게 말한다.

> "전반적으로 적응은 비용 대비 편익 비율이 1.5를 초과하는 좋은 투자이며... 비용의 약 80%가 실제로 편익이 3보다 큰 조치에 해당한다"
> — Mekala Krishnan(MGI 파트너), [2026-03-12](https://www.youtube.com/watch?v=MtevcjCnO1w)

같은 행사 인터뷰어는 같은 연구를 이렇게 인용한다.

> "그 이점은 비용보다 7배나 더 클 것입니다."
> — [2026-03-12](https://www.youtube.com/watch?v=MtevcjCnO1w)

그리고 MGI 소장 본인의 마무리 발언.

> "비용 대비 편익 비율이 7대 1 또는 8대 1인 세상에서 사업을 운영한다면"
> — [2026-03-12](https://www.youtube.com/watch?v=MtevcjCnO1w)

**1.5 → 7 → 8.** 눈금이 만들어진 직후 눈금이 흔들린다.

모집단 선택이 결과를 만드는 구조도 명시된다.

> "이는 연구 대상 기업 20개 중에서 실제로 매우 뛰어난 성과를 내고 있는 기업들을 구체적으로 살펴보는 것입니다. 그들은 리와이어드 프레임워크를 정말 꼼꼼하게 적용했어요."
> — [2026-04-29](https://www.youtube.com/watch?v=HoHFZ-Fzu_g)

그리고 가장 강한 자기반증.

> "이 모든 것은 결국 제 조직에 인공지능이 도처에 있지만, 정작 수익성에는 영향을 미치지 않는다는 점으로 귀결됩니다."
> — [2026-04-29](https://www.youtube.com/watch?v=HoHFZ-Fzu_g)

> "'실제로 그 모든 가치가 손익계산서에 반영되는 것을 봤어요.'라고 말하는 사람은 거의 없습니다. 우리는 인공지능이 손익계산서를 제외한 모든 곳에 있다고 말하곤 합니다."
> — Kelly Ungerman, [2025-12-01](https://www.youtube.com/watch?v=dmKFLspjYNw)

**자사 채널에서 외부 학자가 맥킨지 자신의 인재 피라미드가 무너지고 있다고 말한다.**

> "the pyramid in lots of companies, McKinsey and and in universities elsewhere, where people come in and they kind of work their way up, is becoming more of a diamon..."
> — Erik Brynjolfsson, [2026-08-01](https://www.youtube.com/watch?v=u76xdhpF474)

**ROI 배수의 분모 자체가 아직 측정 불가능하다는 지적도 같은 편에 있다.**

> "The problem is that you don't know how much uh token cost is going to go into a task. And the agents themselves are very bad at estimating them."
> — Erik Brynjolfsson, [2026-08-01](https://www.youtube.com/watch?v=u76xdhpF474)

즉 **앞선 모든 ROI 배수는 비용 항이 확정되지 않은 상태에서 산출된 것**이다.

## 4-5. 인용 시 주의

- 채널 134건 중 상당수가 **채용 콘텐츠**다. 읽은 7편 중 3편(Kate Smaje·Sternfels·Plenty)이 글로벌
  인재유치 책임자가 진행하는 채용 홍보물이고, 2편은 QR코드로 자사 진단·서적 구매를 유도하는 마케팅
  웨비나다. 따라서 **'자기반증'으로 보이는 발화조차 신뢰 형성을 위해 배치된 자기비판일 수 있다.**
- Sternfels의 '10배 → 100배'는 특정 연구가 아니라 **전 CEO의 구전 격언을 인용한 수사**다. 실증 수치로
  다루면 안 된다.
- 녹화일과 게시일이 다르다. Plenty 편은 본문에서 '2월 세션'이라 하는데 업로드일은 2026-05-14이고,
  Kate Smaje 편은 '9월 에디션'인데 업로드일은 2025-10-13이다.
- 영어 자막에 화자 전환 기호 `>>`가 문장 중간에 삽입돼 있어 **어디까지가 Kate의 말인지 모호한 구간**이
  있다.

---

# 5. Siemens — 물리 제약이 서사의 상한선이 되는 사례

## 5-1. 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-12-30 | ko(독일어 원본) | [Die Zukunft der Industrie: CEOs von Siemens & Schaeffler](https://www.youtube.com/watch?v=jEvJOXlENOI) | 공개 패널 토론 |
| 2026-01-07 | ko | [The Industrial AI Revolution: Siemens Keynote at CES 2026](https://www.youtube.com/watch?v=R4Wm6YdoZSs) | CES 기조연설 |
| 2026-02-12 | en | [Agentic and Physical AI in Manufacturing: Siemens & Accenture](https://www.youtube.com/watch?v=nmaBILWJm_c) | 파트너십 대담 |
| 2026-02-16 | en | [Unleashing the Promise: Siemens and Commonwealth Fusion Systems](https://www.youtube.com/watch?v=dyhxadwuQn4) | 자사 팟캐스트 |
| 2026-02-20 | en | [Hero MotoCorp Adopts Cloud-Based PLM](https://www.youtube.com/watch?v=IaMPTBOxF5o) | 3자 고객 사례 |
| 2026-03-24 | en | [Industrial AI Is Scaling Now: Roland Busch Keynote, RXD Beijing](https://www.youtube.com/watch?v=S3vM-v8cbjY) | 중국 시장 기조연설 |
| 2026-06-19 | ko | [Industrial AI in Action: Roland Busch Keynote, VivaTech 2026](https://www.youtube.com/watch?v=AvSNxD9GQH4) | 유럽 시장 기조연설 |
| 2026-07-20 | ko | [AI-Based Process Control at Scale: Pringles and Siemens](https://www.youtube.com/watch?v=-B__O2eqRYc) | 전시부스 좌담 |

## 5-2. 정통성의 근거는 모델이 아니라 설치기반이다

> "One out of three manufacturing machines worldwide run on a Siemens controller. Approximately seventy percent of the world's electricity flows through grids planned or optimized using our software."
> — Roland Busch(Siemens CEO), [2026-03-24](https://www.youtube.com/watch?v=S3vM-v8cbjY)

지멘스의 주장은 "우리가 더 똑똑한 AI를 만든다"가 아니라 **"AI가 실제 세계에 닿으려면 우리의 하드웨어와
도메인 데이터를 통과해야 한다"는 병목 주장**이다. 이 프레임은 '환각 불가' 요건으로 봉인된다.

> "In industry, we need AI with one hundred percent reliability, and this is possible with the right technology stack, industrial domain know-how, and of course, with the right partners."
> — Roland Busch, [2026-03-24](https://www.youtube.com/watch?v=S3vM-v8cbjY)

## 5-3. 시점 서사 — 2025-12-30과 2026-01-07 사이의 180도 전환

**이 사례의 가장 큰 발견은 8일 간격으로 서사가 뒤집힌다는 것이다.**

2025-12-30 셰플러 CEO 공동 패널에서 부슈(로 추정되는 화자)는 이렇게 말한다.

> "그래서 이 개념 증명은 다음과 같습니다. 그것들은 수십만 개에 달하며, 그러면 확대/축소하지 마세요. 그건 정말 심각한 문제예요."
> — [2025-12-30](https://www.youtube.com/watch?v=jEvJOXlENOI)

> "저희 전문가들이 그들에게 당신의 데이터를 알려줍니다. 가치가 없다. 데이터의 부분집합에 있어서 모형의 절반도 만들 수 없는 건가요?"
> — [2025-12-30](https://www.youtube.com/watch?v=jEvJOXlENOI)

**지멘스 자체 데이터조차 AI를 얹을 품질이 아니라고 인정한다.**

> "저희와 함께라면 데이터는 다음과 같습니다. 내가 기대했던 품질과는 거리가 멀다 그 위에 AI를 실행하기만 하면 됩니다."
> — [2025-12-30](https://www.youtube.com/watch?v=jEvJOXlENOI)

AI 역량 지도에서 바늘은 에를랑겐이 아니라 팔로알토에 꽂힌다.

> "하지만 그때 바늘이 멈춘다 분명히 세르델 어딘가, 산에 있을 겁니다. 샌프란시스코, 팔로알토 또는 이와 유사한 지역."
> — [2025-12-30](https://www.youtube.com/watch?v=jEvJOXlENOI)

유럽 컴퓨트의 실측 한계도 나온다.

> "우리는... 얼마 유럽에 GPU를 몇 대나 들여올 수 있을까요?... 우리는 기고리 하나도 제대로 못 맞출 거야."
> — [2025-12-30](https://www.youtube.com/watch?v=jEvJOXlENOI) *(자막 파손. '기가팩토리 하나도 못 채운다'의 의미)*

그리고 8일 뒤 CES 2026 무대에서는 **"우리는 산업 인공지능 혁명을 주도하고 있습니다"**가 선언되고,
2026년 독일 최초 완전 AI 기반 적응형 제조 시설 가동이 약속된다.

> "우리는 2026년에 독일에서 최초의 완전 AI 기반 적응형 제조 시설을 시작할 예정입니다."
> — Roland Busch, [2026-01-07](https://www.youtube.com/watch?v=R4Wm6YdoZSs)

> "산업 현장에 인공지능이 도입될 때, 환각은 용납될 수 없습니다."
> — Roland Busch, [2026-01-07](https://www.youtube.com/watch?v=R4Wm6YdoZSs)

## 5-4. 도입률을 무대에서 실측한 장면

이 코퍼스 전체에서 가장 인상적인 자기반증은 VivaTech 파리 키노트에 있다. 임원이 청중 거수로 도입률을
**실시간으로 측정한다.**

> "실제로 엄청난 성공을 거두고 투자 수익을 창출하는 프로젝트를 이끌고 계신 분은 손을 들어주세요... 사람이 더 적습니다. 저들을 보세요. 그들이 바로 영웅입니다. 그들에게 큰 박수를 보내주세요. 왜냐하면 그들은 매우 드물기 때문입니다."
> — 세드릭 니케(Siemens 경영이사회 멤버·DI CEO), [2026-06-19](https://www.youtube.com/watch?v=AvSNxD9GQH4)

> "우리 모두는 AI를 사용합니다. 우리 모두 그것을 발전시키려고 노력하지만 실패하고, 특히 많은 산업 환경에서 실패합니다."
> — 세드릭 니케, [2026-06-19](https://www.youtube.com/watch?v=AvSNxD9GQH4)

⚠️ 다만 **이 자조는 즉흥적 실토가 아니라 정착된 세일즈 화법**이다. '루프트한자보다 조종사(파일럿)가
많다'는 농담이 파리 키노트(2026-06-19)와 프링글스 좌담(2026-07-20)에서 거의 동일하게 반복된다.

> "제 농담은 대부분의 회사가 루프트한자보다 조종사가 더 많다는 거예요, 그렇죠?"
> — [2026-07-20](https://www.youtube.com/watch?v=-B__O2eqRYc)

## 5-5. 물리 제약이 곳곳에서 상한선으로 작동한다

지멘스가 자기 무대에 올린 파트너들이 오히려 한계를 못 박는다.

> "locomotion and basic motion are mostly solved. But grasping and manipulation — especially anything related to haptics — that hasn't been s..."
> — Wang Xingxing(유니트리 로보틱스 창업자·CEO), [2026-03-24](https://www.youtube.com/watch?v=S3vM-v8cbjY)

> "If a robot has been trained on a specific object, it can grasp and manipulate it with nearly 100% success. But if I change the object even slightly, the success rate drop..."
> — Wang Xingxing, [2026-03-24](https://www.youtube.com/watch?v=S3vM-v8cbjY)

**'환각 불용, 100% 신뢰성'을 요구하는 서사와 이 진술이 같은 키노트 안에 병존한다.**

> "But the... at end of AI is energy system. If you don't have a sustainable energy solution, AI will be limited because it consume so much power"
> — Professor Ni Jun(CATL 최고제조책임자), [2026-03-24](https://www.youtube.com/watch?v=S3vM-v8cbjY)

디지털 트윈 대표 고객은 정작 디지털 트윈을 아직 안 쓴다.

> "it's less about the digital twin at this point because that's still kind of an early stage application for us"
> — Joe Paluska(Commonwealth Fusion Systems CMO), [2026-02-16](https://www.youtube.com/watch?v=dyhxadwuQn4)

> Q: "Are you doing that with the manufacturing processes yet?" / A: "We are not to my knowledge"
> — [2026-02-16](https://www.youtube.com/watch?v=dyhxadwuQn4)

산업 AI 이전 단계인 클라우드 전환조차 미완이다.

> "Let's be honest. Cloud and SaaS is not new technology... but when it comes to the PLM or the innovation process for our customers, especially in discrete manufacturing, there's been some reluctance"
> — Bob Jones(Siemens Digital Industries Software CRO), [2026-02-20](https://www.youtube.com/watch?v=IaMPTBOxF5o)

## 5-6. '사망 기준' — 이 코퍼스에서 가장 정직한 계약 설계

프링글스(켈라노바) 사례는 AI 프로젝트가 **실패 가능성을 전제로 설계됐음**을 보여준다.

> "이정표 대신 사망 기준이라는 것을 정해봅시다. 그래서 3개월 후에, 우리는 그 프로젝트가 여전히 긍정적인 결과를 가져올 것이라고 평가할 것입니다. 만약 그렇지 않다면, 용기를 내어 이를 막아야 합니다."
> — 다니엘 클라인(Siemens 컨설팅 부사장), [2026-07-20](https://www.youtube.com/watch?v=-B__O2eqRYc)

14개 후보 중 3개만 착수했다는 사실도 같은 자리에서 밝혀진다.

그리고 병목은 기술 바깥에 있다.

> "고객과의 대화 중 70~80% 정도가 문화, 사람, 조직의 변화에 대한 이야기로 시작하거나 끝나거나, 혹은 그 주제가 대화의 대부분을 차지했기 때문입니다."
> — 제이 파릭(Microsoft CoreAI 총괄), [2026-01-07](https://www.youtube.com/watch?v=R4Wm6YdoZSs)

## 5-7. 인용 시 주의 (⚠️ 중대)

- **셰플러 패널(2025-12-30)은 자막에 화자 표기가 전혀 없고** 부슈와 로젠펠트의 발화가 뒤섞여 있다.
  위에서 '부슈로 추정'이라 한 인용들은 문맥 근거의 추정이다. 논문 인용 시 **'지멘스/셰플러 CEO 공동
  패널에서'**로 완충 표현할 것.
- 성과 수치(20%·40%·42%·69%·50%·2.5배)는 대부분 **측정 기간·기준선·범위가 없다**. Hero의 '50% 단축'은
  **목표치**이고, 펩시코의 'CapEx 10~15% 절감'은 **예상치**다.
- 자막 오염: 'Siemens'가 '선원(sailor)/시몬스', 'Xcelerator'가 '선원 가속기'·'정자 가속기',
  'plant(공장)'가 '식물', 'chips'가 '감자 칩'으로 나온다.

---

# 6. NVIDIA ↔ AMD — 분모 경쟁의 실물

> 이 쌍이 논문의 Airbnb↔Booking.com 자리에 대응한다. 같은 산업, 다른 계량 단위다.
> **NVIDIA는 산출물(토큰)을, AMD는 노동 단위(에이전트)와 전력을 분모로 삼는다.**

## 6-1. NVIDIA — 토큰이 좌표축에서 가격표로, 다시 전력으로

### 읽은 자료 (12편 중 주요)

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-04-30 | en | [Introducing NVIDIA Dynamo](https://www.youtube.com/watch?v=3C-6STonTLU) | GTC 제품 발표 + 공개 Q&A |
| 2025-11-12 | en | [From Data to Deployment: Building European AI at Scale (DeepL)](https://www.youtube.com/watch?v=KwSwxb2GBOM) | 고객 라이브스트림 |
| 2025-12-01 | en | [Open-Source AI 101 (GTC D.C.)](https://www.youtube.com/watch?v=VqIc2LJzZG0) | 정책 패널 |
| 2026-02-12 | ko | [Extreme Co-Design for Efficient Tokenomics](https://www.youtube.com/watch?v=anC3R-3bXgs) | 내레이션 브랜드 필름 |
| 2026-03-18 | ko | [How AI Factories Maximize Tokens, Power, and Profit (DSX)](https://www.youtube.com/watch?v=rsBobT9INP4) | 초단편 홍보 필름 |
| 2026-04-09 | ko | [Advancing to AI's Next Frontier: Jeff Dean & Bill Dally](https://www.youtube.com/watch?v=DqMIYc-keBQ) | GTC 대담 |
| 2026-04-09 | ko | [The 50-State Plan](https://www.youtube.com/watch?v=uv8va8bIqus) | 고등교육 정책 패널 |
| 2026-04-15 | ko | [Why Cost Per Token Is the Only Metric You Need for AI TCO](https://www.youtube.com/watch?v=FS1l8iN7PVo) | TCO 대담 |
| 2026-05-20 | ko | [Inside AI Tokenomics](https://www.youtube.com/watch?v=zNuOOMM20Tk) | 자사 팟캐스트 |
| 2026-06-24 | ko | [Inside Instacart's AI-Powered Smart Shopping Cart](https://www.youtube.com/watch?v=Alz-bhXqyXM) | 고객 사례 |

### 2025년 4월 — 토큰은 아직 가격이 아니라 좌표였다

> "on the y-axis, you see tokens per second per GPU. That's basically throughput per GPU, and then the x-axis, tokens per second per user. That's latency."
> — Harry(NVIDIA, Dynamo 발표 리드), [2025-04-30](https://www.youtube.com/watch?v=3C-6STonTLU)

**이 시점에 전력은 NVIDIA의 언어가 아니었다.** 관객이 명시적으로 물었지만 답변은 전력 부분을 비껴간다.

> Q: "whether you guys are considering hybrid configuration or like throttling power consumption"
> A: "the question is around being able to do disaggregation across different types of architectures and GPUs. Yes, that's definitely something that we're looking at."
> — [2025-04-30](https://www.youtube.com/watch?v=3C-6STonTLU)

### 2026년 2월 — 토큰당 비용이 '성능을 논의하는 방식'으로 격상된다

> "추론 모델은 엄청난 양의 토큰을 생성합니다... 근본적으로 이는 토큰당 비용이 AI 추론 성능을 개발하고 논의하고 측정하는 방식에서 더욱 중요한 측면이 된다는 것을 의미합니다."
> — 내레이션, [2026-02-12](https://www.youtube.com/watch?v=anC3R-3bXgs)

이 분모가 하는 일은 **'더 비싼 하드웨어가 더 싸다'는 역설을 성립시키는 것**이다.

> "GB200 NVL72를 살펴보았는데... 67% 더 비싸긴 하지만, [음악]은 새로운 GB200 시스템의 토큰당 비용을 112배로 낮춥니다."
> — 내레이션, [2026-02-12](https://www.youtube.com/watch?v=anC3R-3bXgs)

⚠️ **이 '112배'는 같은 문단의 전제(20배 성능·67% 가격 상승)와 산술적으로 맞지 않는다.** 12배 또는 11.2배의
오전사일 가능성이 높다. **단독 인용 금지**.

### 2026년 3월 — 등식이 한 문장으로 확정된다

> "AI 공장의 수익은 와트당 토큰 수로 계산됩니다. 따라서 전력 제약이 있는 경우, 사용되지 않는 모든 [음악] 와트는 수익 손실로 이어집니다."
> — 내레이션(DSX 홍보 영상), [2026-03-18](https://www.youtube.com/watch?v=rsBobT9INP4)

**전력 제약이라는 외부 병목이 NVIDIA가 판매하는 공동설계의 시장으로 전환된다.**

### 2026년 4월 — 회계 장치가 붙는다

> "전력량이 고정되어 있다고 가정해 봅시다. 이 데이터 센터는 5메가와트 용량이에요. 저는 이 데이터 센터에서 최대한 많은 토큰을 얻고 싶어요."
> — NVIDIA 측 진행자, [2026-04-15](https://www.youtube.com/watch?v=FS1l8iN7PVo)

> "GPU 시간당 사용량을 보면, 이는 시간 기반 지표이기 때문에 전력 생산, 공급, 처리 과정에서의 비효율성을 고려하지 않는다는 것을 알 수 있습니다... 업계가 그러한 비효율성을 고려한 측정 기준으로 전환해야 한다고 생각합니다."
> — 전력·에너지 업계 게스트, [2026-04-15](https://www.youtube.com/watch?v=FS1l8iN7PVo)

최고과학자 층위에서도 같은 축이 확인된다.

> "추론의 성능 곡선을 살펴보면... 초당 토큰 수당 달러 또는 초당 토큰 수당 와트로 나타낼 수 있습니다."
> — Bill Dally(NVIDIA 최고과학자), [2026-04-09](https://www.youtube.com/watch?v=DqMIYc-keBQ)

### 2026년 5월 — 숫자로 마감

> "블랙웰이 출력 면에서 호퍼에 비해 와트당 50배 더 많은 토큰을 제공하기 때문입니다... 이는 토큰 비용이 35배 낮아진다는 것을 의미합니다."
> — Shruti Kulkarni(NVIDIA 가속컴퓨팅팀 추론 담당), [2026-05-20](https://www.youtube.com/watch?v=zNuOOMM20Tk)

### NVIDIA의 균열

**토큰당 비용 절감이 절약이 아니라 수요 확장 엔진임을 스스로 자인한다.**

> "여기서 우리가 보는 것은 전형적인 제본스 역설입니다... 'GPU가 훨씬 더 생산적이고, 훨씬 더 많은 토큰을 생성하는데, GPU를 덜 사용해도 되지 않을까?'라고 생각할 수 있겠죠. 답은 절대 아니오입니다."
> — [2026-05-20](https://www.youtube.com/watch?v=zNuOOMM20Tk)

**토큰당 비용이 최종 가격을 설명하지 못한다는 점도 인정된다.**

> "여러분이 즐겨 사용하는 AI 도구 중 몇 개가 사용량 제한을 낮추거나 월 구독료를 인상했나요? 그리고 이는 개별 토큰을 생산하는 비용이 상승했기 때문만은 아닙니다. 사실은 정반대입니다."
> — [2026-04-15](https://www.youtube.com/watch?v=FS1l8iN7PVo)

**'와트당 토큰'이 안정적 지표가 아니라는 자기반증**도 최고과학자에게서 나온다.

> "누군가가 그룹 쿼리 어텐션에서 멀티 헤드 잠재 어텐션으로 바뀌는 것과 같은 다른 모델을 내놓으면, 그런 비율들이 상당히 달라지게 됩니다. 그러다 보면 갑자기 일부 하드웨어는 유휴 상태가 되고... 그 문제를 피할 방법은 사실상 없습니다."
> — Bill Dally, [2026-04-09](https://www.youtube.com/watch?v=DqMIYc-keBQ)

**토큰 회계는 보편 언어가 아니다.** 같은 채널의 대학 패널에서 진행자가 직접 부정한다.

> "하지만 대학은 비즈니스 모델에 참여하지 않잖아요, 그렇죠?"
> — [2026-04-09](https://www.youtube.com/watch?v=uv8va8bIqus)

공동창업자는 자사 기계를 이렇게 부른다.

> "실제로 기계는 단지 촉매제일 뿐입니다. 제 말은, 그건 그냥 철 조각일 뿐이라는 거죠."
> — Chris Malachowsky(NVIDIA 공동창업자), [2026-04-09](https://www.youtube.com/watch?v=uv8va8bIqus)

그리고 **경쟁 분모가 같은 GTC 계열 무대에 공존한다.**

> "whether it's per document reviewed or per task complete..."
> — [2025-12-01](https://www.youtube.com/watch?v=VqIc2LJzZG0)

Instacart 고객 사례에서 분모는 토큰이 아니라 **수백 밀리초와 매장 매출 1%p**다.

## 6-2. AMD — 분모를 명시적으로 갈아끼운 사례

### 읽은 자료

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-11-19 | en | [AI in Finance with BNY: Advanced Insights S2E8](https://www.youtube.com/watch?v=AR0JpYQwhBc) | 자사 팟캐스트(고객) |
| 2026-01-07 | en | [AMD at CES 2026 Replay](https://www.youtube.com/watch?v=ypSay3Ehxow) | CES 기조연설 |
| 2026-03-09 | en | [Lenovo and AMD on Advancing AI PCs for Business](https://www.youtube.com/watch?v=dum2aCaxIus) | MWC 파트너 인터뷰 |
| 2026-03-18 | en | [AI in Chip Design: S3E1](https://www.youtube.com/watch?v=fj1iRitQL4s) | 자사 팟캐스트(내부) |
| 2026-06-17 | en | [AI and Trust at Scale: S3 E3](https://www.youtube.com/watch?v=WOXtvwYq-7o) | 자사 팟캐스트(학계) |
| 2026-07-01 | en | [Power Agentic AI with AMD EPYC Server CPUs](https://www.youtube.com/watch?v=5cilEo4gz-w) | 제품 포지셔닝(190단어) |
| 2026-07-22 | en | [AMD EPYC Server CPUs in the Era of Agentic AI](https://www.youtube.com/watch?v=N9pm6NlLuQo) | 제품 광고(115단어) |
| 2026-07-24 | en | [Advancing AI 2026 Replay](https://www.youtube.com/watch?v=8B_Gese-bdI) | 연례 기조연설 |
| 2026-07-29 | en | [Agentic AI and the Future of Software Development: S3 E4](https://www.youtube.com/watch?v=eQ6tb7j3Z2U) | 자사 팟캐스트(Anthropic) |

### 분모 선언

> "EPYC CPUs maximize the number of agents per watt, per dollar, and per rack."
> — 내레이터, [2026-07-22](https://www.youtube.com/watch?v=N9pm6NlLuQo)

그 근거는 **단일 에이전트의 속도(경쟁사가 이기는 지표)를 명시적으로 폐기하는 논증**이다.

> "When agentic AI moves into production, what you're trying to optimize for is not how quickly a single agent executes. It's more about how a fleet of agents can get as much work done as possible in a g..."
> — 내레이터, [2026-07-01](https://www.youtube.com/watch?v=5cilEo4gz-w)

**시점이 중요하다.** 반년 앞선 CES 2026에서는 '와트당 에이전트'라는 분모가 아직 존재하지 않고, PC 제품도
경쟁사식 토큰 지표로 측정된다.

> "Ryzen AI Max delivers comparable performance to at much lower price than NVIDIA's DGX Spark, generating up to 1.7 times more tokens per second per dollar"
> — Lisa Su(AMD 회장 겸 CEO), [2026-01-07](https://www.youtube.com/watch?v=ypSay3Ehxow)

즉 **분모 전환은 2026년 상반기에 일어났다.**

### 균열 — 같은 무대에서 두 분모가 동시에 가동된다

자사 분모:

> "Venice moves the data faster than the best competitive x86 processor, delivering up to 1.8 times more tokens per second. And when you look at the agentic CPU servers and sandboxes, because of our dens..."
> — Lisa Su, [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

**한 문장 안에 '초당 토큰'(폐기한 분모)과 '와트당 에이전트'(새 분모)가 같이 있다.**

GPU를 팔 때는 전적으로 경쟁사 분모다.

> "we're taking another major step with MI455, delivering up to 18x more tokens per dollar"
> — Lisa Su, [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

> "the Helios rack delivers more performance, and it also delivers up to 30% more tokens per dollar than the competition."
> — Lisa Su, [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

**가장 노골적인 균열은 per-core 논쟁이다.** 경쟁 프레임을 기각한 직후 그 프레임에서 이겼다고 말한다.

> "there's been a lot of talk about what matters most for agentic AI, with some saying that per-core performance under load is the only thing that counts. But that's really only part of the story"
> — Lisa Su, [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

> "when you compare Venice against the highest performing ARM CPU from our competition, EPYC delivers 20% higher per-core performance. And when we... I like that number."
> — Lisa Su, [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

### 도입률 96%의 출처 — 이 사례의 핵심 발견

`CASE_PROFILES.md`에서 "AMD 96%"로 인용했던 수치의 실제 출처는 **AMD가 아니라 레노버**이고,
내용도 '도입'이 아니라 **의향**이다.

> "You know, we run a survey with IT decision makers, 3,000 across the world. We're in our third edition and 96% of enterprises are **ready to move from pilots into some form of real adoption** of AI."
> — Steve Long(레노버 인텔리전트 디바이스 그룹 SVP 겸 GM), [2026-03-09](https://www.youtube.com/watch?v=dum2aCaxIus)

넉 달 뒤 같은 채널에서 이 수치는 **출처·화자·조건절이 지워진 채 미래시제로 재등장한다.**

> "the latest data here shows that nearly every enterprise next year will have some form of agentic deployments."
> — Dan McNamara(AMD 컴퓨트·엔터프라이즈 AI 부문 SVP), [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

**그리고 반증이 AMD 자기 채널 안에 있다.** 96%와 5%가 같은 채널에 공존한다.

> "when only 5% of, um, companies, as MIT have shared recently, are really seeing the benefits of AI, we really believe that we're in that 5%."
> — Leigh-Ann Russell(BNY 기술총괄), [2025-11-19](https://www.youtube.com/watch?v=AR0JpYQwhBc)

'거의 모든 기업이 배포한다'고 말한 지 **닷새 뒤**, 초대 손님이 이렇게 말한다.

> "when I look at most companies, they're still somewhere between step one and two."
> — Boris(Anthropic Claude Code 책임자), [2026-07-29](https://www.youtube.com/watch?v=eQ6tb7j3Z2U)

**벤더 내부 수치와 고객 실측치의 격차**도 같은 편에서 노출된다 — Anthropic 사내 "8x increase in code
output per engineer" 대 최대 고객의 "50, 100%, 150%".

### 에이전트를 늘리는 것이 가치라면서 관리 화면의 핵심 기능은 에이전트를 죽이는 것

> "every customer is really worried about token costs and so we need to make sure that we can actually contain the costs of an agent's consumption o..."
> — [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

**AMD 자신의 IT 부서 사례는 프론티어 모델 토큰 경제의 실패를 전제로 설계돼 있다.**

> "with intelligent routing, we reduced our token costs by 43%, while delivering up to 3x faster response times for the workloads running locally."
> — [2026-07-24](https://www.youtube.com/watch?v=8B_Gese-bdI)

자랑거리가 '에이전트를 더 많이 돌렸다'가 아니라 **'토큰 비용을 43% 줄였다'**이며, 방법은 요청 상당수를
프론티어 모델에서 빼내는 것이다.

## 6-3. 이 쌍을 논문에서 쓰는 법

| | NVIDIA | AMD |
|---|---|---|
| 분모 | 토큰 → 와트당 토큰 | 와트당·달러당·랙당 에이전트 |
| 전환 시점 | 2025-04(좌표) → 2026-02(가격) → 2026-03(전력) | 2026-01(토큰) → 2026-07(에이전트) |
| 자기반증 | 제본스 역설 자인, 모델 구조 변화 시 지표 불안정 인정 | 폐기한 분모로 자기를 계속 잼, per-core 기각 후 승리 선언 |
| 도입률 | (해당 없음) | 96%(레노버 의향조사) ↔ 5%(MIT 인용, 자사 채널) |

**두 회사 모두 자기 분모를 완결하지 못했다는 것이 이 쌍의 발견이다.** NVIDIA는 토큰당 비용이 최종
가격을 설명하지 못한다고 인정하고, AMD는 경쟁사 분모로 자기를 계속 측정한다.

---

# 7. IQVIA — 분업선이 조정 가능한 파라미터가 된 사례

## 7-1. 읽은 자료 (15편 중 핵심)

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2025-07-18 | ko | [IQVIA Healthcare-grade AI® - AI you can trust](https://www.youtube.com/watch?v=Ul6iEfykLWU) | 기업 브랜드 영상 |
| 2025-10-16 | ko | [IQVIA AI: Right Now](https://www.youtube.com/watch?v=p0pjnFUyD_A) | 115단어 브랜드 광고 |
| 2025-10-28 | en | [Research brief: Global Trends in R&D 2025](https://www.youtube.com/watch?v=6zb6XIpvKYA) | Institute 연구 발표 |
| 2026-01-22 | ko | [Transforming Regulatory Operations with SmartSolve RIM](https://www.youtube.com/watch?v=8YlcnFpmXyI) | 제품 소개 |
| 2026-01-29 | ko | [Streamlining Adverse Event Intake: Vigilance Intake](https://www.youtube.com/watch?v=QmmiIH3n76w) | 제품 소개 |
| 2026-03-06 | ko | [Research Brief: Digital Health Trends 2025](https://www.youtube.com/watch?v=WaNTDsbrKFo) | Institute 연구 발표 |
| 2026-04-22 | ko | [Vigilance Detect + Extract](https://www.youtube.com/watch?v=Nir0td6W5k8) | 제품 소개 |
| 2026-04-27 | ko | [IQVIA IVP Collect (일본 PMDA 시장용)](https://www.youtube.com/watch?v=fGQ7vYVsWQ8) | 제품 소개 |
| 2026-07-01 | en | [The Future of Work in Life Sciences](https://www.youtube.com/watch?v=feK98iTyY6M) | 비전 영상 |
| 2026-07-10 | ko | [IQVIA Vigilance Platform with AI Assistant](https://www.youtube.com/watch?v=CMkK5CspWL0) | 제품 데모 |

## 7-2. 세 겹의 장치

**① 예외 기반 모델 — 인간 노동이 잔여물 처리로 재정의된다**

> "예외 기반 [음악] 모델을 사용하면 신뢰도 점수가 높은 문서는 자동으로 사례 처리 단계로 진행될 수 있고, 신뢰도 점수가 낮은 문서는 사람의 [음악] 검토를 위해 표시됩니다."
> — 내레이터, [2026-07-10](https://www.youtube.com/watch?v=CMkK5CspWL0)

> "사용자는 예외 사항에만 집중하여 품질 저하 없이 처리 속도를 높일 수 있습니다."
> — 내레이터, [2026-07-10](https://www.youtube.com/watch?v=CMkK5CspWL0)

⚠️ **'품질 저하 없이'라는 보증에는 아무 근거가 붙지 않는다.** 그리고 예외 기반 모델의 핵심 리스크 —
임계값 미만 오류가 아니라 **임계값을 통과한 고신뢰도 오류의 무검토 통과** — 는 전 코퍼스에서 단 한 번도
언급되지 않는다.

**② 필드 수준 신뢰도 임계값 — 경계선의 위치가 고객사에 위임된다**

> "사용자는 필드 수준의 신뢰도 임계값을 구성하고, 추출할 데이터를 선택하고, **코드를 사용하거나 시스템 업데이트를 기다릴 필요 없이** 변환을 적용할 수 있습니다."
> — 내레이터, [2026-07-10](https://www.youtube.com/watch?v=CMkK5CspWL0)

임계값 변경의 마찰이 **의도적으로 제거**되어 있다. 인간 개입 밀도는 제약사가 자사 리스크 성향에 맞춰
돌리는 다이얼이 되고, **규제 책임은 벤더에서 고객으로 미끄러진다.**

**③ 자동화율의 KPI화 — 그리고 여기서 결정적 반전이 일어난다**

> "내장된 애널리틱스 대시보드에서 처리 시간, 자동화율, 효율의 파악이 가능, 팀의 성능과 개선이 필요한 영역에 대한 통찰력도 제공합니다."
> — 내레이터(일본 시장용), [2026-04-27](https://www.youtube.com/watch?v=fGQ7vYVsWQ8)

**자동화율이 '팀의 성능'과 나란히 놓이는 순간, 임계값을 낮춰 자동화율을 올리려는 압력이 조직 내부에
구조적으로 심어진다.** 인간 검토는 품질 보증이 아니라 **KPI를 깎아먹는 비용**으로 계상된다.
그리고 이 상충은 어느 영상에서도 언급되지 않는다.

인간 검토의 지위도 명시적으로 규정돼 있다.

> "신뢰도가 낮을 때는 내장된 인적 품질 관리 단계를 통해 **속도와 규정 준수 사이의 적절한 균형**을 유지합니다."
> — 내레이터, [2026-04-22](https://www.youtube.com/watch?v=Nir0td6W5k8)

축이 **환자 안전이 아니라 규정 준수**이고, 그것조차 속도와 교환 가능한 변수다.

## 7-3. 시점 서사 — 지도하는 인간에서 호출당하는 인간으로

2025-07-18 브랜드 영상은 "적절한 전문가의 지도를 받고"라는 인간 우위 서사를 편다. 정확히 1년 뒤,
판단권 자체가 이관된다.

> "A future where agents execute workflows >> [music] >> and **know when to bring humans in** for reviews."
> — 내레이터, [2026-07-01](https://www.youtube.com/watch?v=feK98iTyY6M)

그리고 **분업선의 코드화 자체가 판매 논리가 된다.**

> "Unlike other AI-powered [music] solutions, discrete workflow steps with **predetermined human checkpoints** can be [music] defined and executed."
> — 내레이터, [2026-07-01](https://www.youtube.com/watch?v=feK98iTyY6M)

시스템이 인간의 주의를 배분하는 구조도 명시된다.

> "검토가 필요한 곳... 자동으로 추출 데이터의 신용도가 낮다면 [음악]은 신고하고 사용자에게주의 재촉하고 리뷰가 필요한 필드에 직접 [음악] 가이드."
> — 내레이터, [2026-04-27](https://www.youtube.com/watch?v=fGQ7vYVsWQ8)

자동화 압력의 외부 정당화는 규제 시한이다.

> "기업이 인지한 후 7일 또는 14일 이내에 식별, 평가 및 보고해야 하는 부작용 사례와 제품 품질 불만이 숨겨져 있습니다."
> — 내레이터, [2026-04-22](https://www.youtube.com/watch?v=Nir0td6W5k8)

## 7-4. 균열 — 자사 리서치 부문이 제품 부문을 반증한다

> "하지만 이번 전시에서 볼 수 있듯이, 디지털 치료법과 AI 기반 모바일 도구의 **절대적인 도입률은 여전히 미미한 수준**입니다."
> — IQVIA Institute, [2026-03-06](https://www.youtube.com/watch?v=WaNTDsbrKFo)

> "통합 플랫폼이 없기 때문에 많은 규제 기관은 **여전히 스프레드시트, 공유 드라이브 및 이메일에 의존**하고 있습니다."
> — [2026-01-22](https://www.youtube.com/watch?v=8YlcnFpmXyI)

**기술 도입이 일방향이 아니라는 증거**도 있다.

> "Opportunities certainly remain, however, with remote, virtual, or decentralized trials having **returned to prepandemic levels**, for example."
> — [2025-10-28](https://www.youtube.com/watch?v=6zb6XIpvKYA)

그리고 **증거 생산 자체가 상업 자산으로 재코드화되는 순간**이 잡힌다. '공공 서비스로 무료 제작'이라던
Institute가 3개월 뒤 보고서를 유료화한다.

> "11월부터 전체 트렌드 및 전략 보고서에 액세스하려면 1회용 [음악] 결제가 필요합니다."
> — [2026-01-29](https://www.youtube.com/watch?v=RFI_zhh6kjA)

## 7-5. 인용 시 주의

- ⚠️ **자동화율의 실측치는 어디에도 없다.** 자동화율이 대시보드 지표라는 언급은 있으나, 실제 달성
  자동화율·권장 임계값·인간 검토 회부 비율은 전 코퍼스에 **0회** 등장한다. **이 부재 자체가 분석
  대상**이다.
- 제품 영상(판매 홍보물)과 Institute 브리프(연구 발표)를 **같은 신뢰 수준으로 다루면 안 된다**.
  98% 정확도 같은 수치는 방법론 공개 없는 마케팅 주장이다.
- 일본어 원본으로 추정되는 IVP Collect(fGQ7vYVsWQ8)는 **이중 번역**을 거쳐 "조례가 기준을 만족하면"
  (症例=사례를 조례로 오역) 같은 붕괴가 있다.
- 핵심 용어의 원어를 확정할 수 없다. 같은 개념이 '신용도'와 '확신 점수'로 혼용된다.

---

# 8. Unilever — AI 주장이 재무 검증선 앞에서 멈추는 사례

## 8-1. 읽은 자료 (11편 중 핵심)

| 업로드일 | 자막 | 영상 | 성격 |
|---|---|---|---|
| 2024-11-26 | ko | [Investor Event 2024 CEO Presentation](https://www.youtube.com/watch?v=r_BOLVAd0Kw) | IR 발표 |
| 2024-11-26 | ko | [Investor Event 2024 – Q&A Session](https://www.youtube.com/watch?v=hVyrSK24l4A) | 애널리스트 Q&A |
| 2024-11-26 | ko | [Reginaldo Ecclissato 공급망 발표 클립](https://www.youtube.com/watch?v=ks7vFXlpsVA) | 538단어 IR 클립 |
| 2025-03-06 | en | [Fireside Chat with Fernando Fernandez & Warren Ackerman](https://www.youtube.com/watch?v=SCh7KubuZdo) | 1:1 대담 |
| 2025-10-29 | ko | [H1 2025 Results Webcast & Q&A](https://www.youtube.com/watch?v=oMDBIXBEv3Q) | 실적 웹캐스트 |
| 2026-02-18 | ko | [CAGNY 2026](https://www.youtube.com/watch?v=SXT5EV4VR-U) | 애널리스트 컨퍼런스 |
| 2026-03-04 | ko | [FY2025 Results Webcast & Q&A](https://www.youtube.com/watch?v=m7GUG2IHJZY) | 실적 웹캐스트 |
| 2026-06-22 | ko | [BNP Paribas CEO Conference 2026](https://www.youtube.com/watch?v=tfxFi3sYggA) | CEO 대담 |
| 2026-07-28 | en | [Q2 & H1 2026 Results Webcast & Q&A](https://www.youtube.com/watch?v=b_Db2XHcw18) | 실적 웹캐스트 |

## 8-2. 원형 문장 — AI가 물류 KPI 한 줄로 편입된다

> "당사의 인재 풀 전반에 걸쳐 AI 기반 노동 계획 및 생성형 AI 진단과 같은 AI 이니셔티브를 통해 노동 효율성을 크게 향상시키고 있습니다. 2024년에는 **FTE당 톤 기준으로 노동 효율성이 약 4% 증가**했습니다."
> — Reginaldo Ecclissato(Chief Business Operations & Supply Chain Officer), [2024-11-26](https://www.youtube.com/watch?v=r_BOLVAd0Kw)

운송거리 15% 단축·트럭 활용률 10% 향상·SKU 20% 감축과 같은 호흡으로 배열되어, **AI 수치는 다른
물류 KPI와 구별되지 않는다.**

## 8-3. 검증 압력이 들어오면 수치가 커지는 게 아니라 작아진다

애널리스트가 정면으로 묻는다.

> "AI에 대해 여러 번 이야기했고 발표마다 내용이 조금씩 다르긴 하지만, 솔직히 우리 중 누구도 답을 정확히 알지는 못하겠지만, AI가 산업 전체에 이익이 되는 것인지, 아니면 우리 회사에 이익이 되는 것인지, 복잡성을 더하는 것인지, 아니면 비용 절감을 가져오는 것인지..."
> — 애널리스트, [2024-11-26](https://www.youtube.com/watch?v=hVyrSK24l4A)

몇 분 전 4%를 제시한 회사의 CEO 답변은 **하향**이다.

> "하지만 **AI 자체가 단기적으로 큰 비용 절감 효과를 가져올 것이라고는 생각하지 않습니다.**"
> — Hein Schumacher(당시 CEO), [2024-11-26](https://www.youtube.com/watch?v=hVyrSK24l4A)

그리고 정당화 근거가 **절감액에서 '경쟁 참가 자격'으로 갈아탄다.**

> "하지만 환경 자체가 AI를 요구하고 있습니다. 그렇지 않으면 경쟁할 수 없기 때문입니다."
> — Hein Schumacher, [2024-11-26](https://www.youtube.com/watch?v=hVyrSK24l4A)

**즉 4%는 자랑이 아니라 알리바이다.**

파일럿 실패율도 '집중'의 언어로 고백된다.

> "한때는 **500개가 넘는 소규모 실험**을 진행했지만, 이제는 더 적고, 더 크고, 더 나은, 더 큰 영향력을 가진 **6가지 핵심 투자**로 압축했습니다."
> — Hein Schumacher, [2024-11-26](https://www.youtube.com/watch?v=r_BOLVAd0Kw)

## 8-4. 2025년은 침묵의 해다

2025-03-06 애커먼과의 약 1만2천 단어 대담에서 AI의 실질 언급은 인플루언서 기계 설명 뒤에 붙는
"AI play a very important role on that" **한 절뿐**이다.

2025-10-29 H1 2025 실적 웹캐스트에서 AI가 등장하는 유일한 지점은 **발표 시작 전 브랜드 영상 자막**이다.

> "데이터 기반 및 AI 강화 팀이 시장을 창출하고 성장을 주도합니다."
> — 오프닝 브랜드 영상 내레이션(발표자 발화 아님), [2025-10-29](https://www.youtube.com/watch?v=oMDBIXBEv3Q)

**CEO·CFO 발표와 애널리스트 Q&A 전체에서 AI·LLM·알고리즘 언급은 0회다.**

## 8-5. 2026년 — 서사의 AI와 회계의 AI가 분리된다

> "두 번째 핵심 메시지는 **인공지능 시대에 적합한 조직**이라는 것입니다."
> — Fernando Fernandez(CEO), [2026-03-04](https://www.youtube.com/watch?v=m7GUG2IHJZY)

**그런데 같은 콜에서 애널리스트가 생산성 절감액을 숫자로 묻자, CFO의 답변에 AI는 한 번도 나오지 않는다.**

> "생산성 향상으로 인한 비용 절감에 대해서는... 현재까지 누적적으로 약 6억 7천만 달러의 절감 효과를 거두었습니다."
> — Srinivas Phatak(CFO), [2026-03-04](https://www.youtube.com/watch?v=m7GUG2IHJZY)

절감액은 전액 SG&A와 공급망 간접비로 귀속된다. 그리고 실제로 제시되는 인력 효율 성과는 알고리즘이
아니라 **구조조정**이다.

> "이 조직은 2025년에 **인력을 35% 감축**하여 설립되었으며, 5.2%의 성장률과 250bp 이상의 마진 확대를 달성했습니다"
> — [2026-03-04](https://www.youtube.com/watch?v=m7GUG2IHJZY)

## 8-6. 재무 검증선 앞에서 정확히 멈추는 지점

2026-07-28 실적 Q&A에서 도이치뱅크 애널리스트가 **손익 항목 단위로** 파고든다 — LLM 전환의 검색비용
이득이 광고비 라인이 아니라 판촉비로 나타나는가.

> "Uh **not significant changes in the cost of media** uh at this stage but this is a something that is changing very very fast. So I cannot predict the future in term..."
> — Fernando Fernandez(CEO), [2026-07-28](https://www.youtube.com/watch?v=b_Db2XHcw18)

**2024년 11월의 '4%'에 대응하는 새로운 실측 수치는 끝내 제시되지 않는다.**

CEO 스스로 생산성 AI를 평가절하하기도 한다.

> "AI를 회사 생산성 향상에 활용하는 것은 당연한 일이지만, 모든 회사가 도입할 기본 조건이 될 것이라는 점입니다. 그리고 **만약 제가 그 일에 6개월 정도 늦더라도, 그건 큰 문제가 아니에요.**"
> — Fernando Fernandez, [2026-06-22](https://www.youtube.com/watch?v=tfxFi3sYggA)

그리고 자신의 AI 발언에 **유통기한**을 붙인다.

> "그러니까, 아마 제가 오늘 하는 말은 15일 후면 가치가 떨어질 겁니다."
> — Fernando Fernandez, [2026-06-22](https://www.youtube.com/watch?v=tfxFi3sYggA)

## 8-7. 인용 시 주의

- 2024 투자자 행사 **전체 녹화본(yuMA_iYdq4w)은 문장이 무작위로 잘리고 뒤섞여** 같은 대목이 의미불명으로
  훼손된다. 반면 **별도 Q&A 클립(hVyrSK24l4A)에서는 온전히 복원**된다. 위 인용은 클립을 근거로 삼았다.
- 화면해설(audio-described) 버전은 **슬라이드 묘사 내레이션과 육성이 구분 없이 이어져** 경계가 모호하다.
- 노동 효율 4%를 말한 화자는 **CEO가 아니라 공급망 책임자**이며, CEO 프레젠테이션 파일 안에 삽입된 영상
  세그먼트다.
- H1 2025 웹캐스트는 **내용상 2분기 발표인데 업로드일이 2025-10-29**다. 업로드일=발표일로 가정 금지.

---

# 9. Orange ↔ Huawei — 주권의 계층화 대 주권의 삭제

## 9-1. 읽은 자료 (13편 중 핵심)

**Orange**

| 업로드일 | 영상 | 성격 |
|---|---|---|
| 2025-11-12 | [Science, Innovation and Technology: Bruno Zerbib](https://www.youtube.com/watch?v=69tvTh7axU0) | CTIO 장편 인터뷰 |
| 2026-03-06 | [Bruno Zerbib on AI, Intelligent Networks (MWC 2026)](https://www.youtube.com/watch?v=xPpwRnoZzlo) | CTIO 인터뷰 |
| 2026-06-17 | [IA, souveraineté et talents (Heydemann × Polytechnique)](https://www.youtube.com/watch?v=sNK9NM5Nfg4) | CEO 원탁 |
| 2026-06-17 | [VivaTech 2026 Christel Heydemann Keynote](https://www.youtube.com/watch?v=yflUNqZ6T9A) | CEO 기조연설 |
| 2026-06-18 | [The Impact of Agentic AI on Telco Transformation](https://www.youtube.com/watch?v=c1XCSgKzhp4) | 패널 토론 |

**Huawei**

| 업로드일 | 영상 | 성격 |
|---|---|---|
| 2025-11-07 | [European Companies Embrace an AI-Ready Cloud](https://www.youtube.com/watch?v=9itARrfKmQg) | 고객 증언 |
| 2026-01-09 | [From Infrastructure to Intelligence: Telcos in the AI Era](https://www.youtube.com/watch?v=XySO_AWqEtk) | 외부 애널리스트 인터뷰 |
| 2026-03-12 | [AI is the Foundation for Transforming Industries](https://www.youtube.com/watch?v=5xLjNzJKuHA) | 내레이션 쇼릴 |
| 2026-03-26 | [AI Could Widen the Digital Divide](https://www.youtube.com/watch?v=me5Ue4jFTXE) | 외부 발표자 인터뷰 |
| 2026-04-16 | [Discipline, Not Hype, Will Define AI Innovation](https://www.youtube.com/watch?v=c6nYPWNgl7I) | 외부 저자 인터뷰 |
| 2026-06-16 | [Banks Need AI-Native Foundations, but Trust Still Matters](https://www.youtube.com/watch?v=syH3UQtywtc) | 외부 저술가 인터뷰 |

## 9-2. Orange — 주권은 국가별로 다른 계층이고 가격표가 붙는다

> "저희는 네트워크의 일부 국가나 특정 지역에서는 중국 기업을 이용할 수 있지만, **프랑스를 비롯한 네트워크의 다른 지역에서는 이용할 수 없습니다.**"
> — Bruno Zerbib(Orange CTIO), [2025-11-12](https://www.youtube.com/watch?v=69tvTh7axU0)

> "고객에게 다양한 선택지와 시나리오를 제시하고, **주권 수준**에 대해 매우 투명하게 설명하는 데 상당히 능숙합니다. 왜냐하면 **주권에는 비용이 따르기 때문입니다.**"
> — Bruno Zerbib, [2025-11-12](https://www.youtube.com/watch?v=69tvTh7axU0)

**주권이 판매되는 옵션 스펙트럼이자 가격표라는 것을 이보다 직접적으로 말할 수 없다.**

지리적 층화도 CEO가 직접 말한다.

> "세네갈, 코트디부아르, 부르키나파소... 우리가 그 나라들에 대해 이야기할 때, **주권이 최우선이다 음식, 에너지 접근성**과 물론, 그럼 이제 주권에 대해 이야기해 볼까요? 기술적인 문제이긴 하지만, 우리는 그렇게 생각하지 않습니다."
> — Christel Heydemann(Orange CEO), [2026-06-17](https://www.youtube.com/watch?v=sNK9NM5Nfg4)

논점 이동의 정식화는 VivaTech 기조에 있다.

> "그런 일이 발생하면, **누가 최고의 모델을 가지고 있느냐는 더 이상 문제가 되지 않습니다.** 문제는 **누가 통제권을 유지하느냐**입니다."
> — Christel Heydemann, [2026-06-17](https://www.youtube.com/watch?v=yflUNqZ6T9A)

## 9-3. Orange의 자기반증 — 이 코퍼스에서 가장 밀도가 높다

**주권 아키텍처를 주장하는 화자가 핵심 구성요소의 감사 불가능성을 인정한다.**

> "음, 저는 여전히 LLM을 열어보거나 감사할 수 없어요. 왜냐하면 LM은 **블랙 박스**와 같기 때문이죠."
> — Bruno Zerbib, [2025-11-12](https://www.youtube.com/watch?v=69tvTh7axU0)

**전 직원 교육을 자랑한 직후 업무 변혁 도달 여부를 스스로 부정한다.**

> "그래서 우리는 거의 모든 직원을 교육하는 데 상당한 시간을 투자했습니다... 이제 그들은 자신의 업무 방식을 혁신할 수 있는 방식으로 이 기술을 활용할 수 있을까요? **아직 아님.**"
> — Bruno Zerbib, [2026-03-06](https://www.youtube.com/watch?v=xPpwRnoZzlo)

**이전 세대 인프라의 수익화 실패를 공개 시인한다.**

> "5G를 발표했을 때, 우리는 커넥티드 카를 약속했습니다... 우리는 원격 수술을 약속했습니다. 혹시 원격 수술을 하는 사람을 마지막으로 본 게 언제였죠? 그런 일은 일어나지 않았습니다. **그래서 저희가 5G로 수익을 창출하지 않은 겁니다.**"
> — Bruno Zerbib, [2026-03-06](https://www.youtube.com/watch?v=xPpwRnoZzlo)

**탈숙련 증언** — 이 코퍼스 전체에서 가장 명료하다.

> "이제 그들에게 인터페이스 작업에 더 집중해야 한다고 말하는 것은 책임 범위 면에서 엄청난 변화이며, 그들은 20년 넘게 기술을 쌓아왔을 수도 있는데, 갑자기 '**아, 내가 다시 주니어 개발자가 됐구나**'라고 깨닫게 되는 거죠."
> — Bruno Zerbib, [2026-03-06](https://www.youtube.com/watch?v=xPpwRnoZzlo)

**비용이 가치를 앞지르는 실패 패턴도 CEO가 일반화해 인정한다.**

> "사용 사례는 작은 것에서 시작됩니다. 도입이 빠르게 증가하면서 갑자기 **비용 증가 속도가 창출되는 가치 증가 속도를 앞지르게** 됩니다."
> — Christel Heydemann, [2026-06-17](https://www.youtube.com/watch?v=yflUNqZ6T9A)

**자사 패널에서 유럽의 도입 지체를 인정하고 중국식 모델을 대안으로 언급한다.**

> "유럽은 에이전트 기술 도입 측면에서 매우 뒤처져 있기 때문에 다소 의문스러운 상황입니다. 중국에 가면 모든 기업이 오픈 클로 방식을 도입했지만, 그들 나름의 방식으로 신뢰성을 확보하고 있죠."
> — Jérôme(Orange 그룹 전략 총괄), [2026-06-18](https://www.youtube.com/watch?v=c1XCSgKzhp4)

**파트너사가 실제 프로젝트 실패를 무대에서 공개한다.**

> "우리는 그들이 저장한 모든 데이터를 하나의 데이터 레이크에 넣고, 상담원에게 고객에게 프로모션 점수를 보내도록 요청했습니다. 하지만 그들이 잊고 있는 것은 데이터 레이크에 오늘의 승진 점수뿐만 아니라 **10년 전의 승진 점수도 저장되어 있다**는 점입니다."
> — Amaury(Dataiku), [2026-06-18](https://www.youtube.com/watch?v=c1XCSgKzhp4)

**한 기업 안의 서사 균열**도 있다. CEO는 "인공지능이 사람을 대체할 것이라는 말을 자주 듣습니다.
저는 정반대가 사실이라고 생각합니다"([2026-06-17](https://www.youtube.com/watch?v=yflUNqZ6T9A))라고
말하지만, 같은 기업 CTIO는 3개월 전 20년 숙련이 무효화되는 체험을 증언했다.

## 9-4. Huawei — 주권은 부정되지 않고 논제에서 제거된다

읽은 7편 어디에도 **주권·지정학·수출통제·5G 배제가 등장하지 않는다.** 그 자리를 채우는 것은
**비판의 외주화**다. 비평은 언제나 외부인의 입에서 나오고, 화살은 늘 '기업 일반'이나 고객군을 향한다.

> "간단히 말해서, 벽에 스파게티를 마구 던져보고 그중 일부라도 붙기를 바라는 수밖에 없다. 전략적 사고가 아닌, 기업의 공황 상태에 오신 것을 환영합니다. 이는 혁신 성과표의 저자인 크리스 힘스커크의 간결한 평가입니다."
> — [2026-04-16](https://www.youtube.com/watch?v=c6nYPWNgl7I)

> "지금까지 저는 그들의 혁신 포트폴리오와 관련해서 엄격함이나 규율이 그다지 뚜렷하게 드러나는 것을 보지 못했습니다."
> — [2026-04-16](https://www.youtube.com/watch?v=c6nYPWNgl7I)

**화웨이 자신은 한 번도 같은 잣대에 놓이지 않는다.** 자사 최대 고객군인 통신사의 시가총액 붕괴를
방영하면서도, 그 장비를 공급해온 자사의 위치는 서사에서 빠져 있다.

> "보고서에 따르면 기존 통신사 모델은 사라질 것이라고 합니다."
> — [2026-01-09](https://www.youtube.com/watch?v=XySO_AWqEtk)

**결정적 대조**: Orange CEO가 유럽의 중국 5G 배제를 명시적으로 언급하는 그 사건이, Huawei 자신의
코퍼스에서는 **완전히 침묵된다.**

> "유럽은 기술을 금지했습니다 특정 지역의 중국인들, 예를 들어 5G의 경우"
> — Christel Heydemann, [2026-06-17](https://www.youtube.com/watch?v=sNK9NM5Nfg4)

## 9-5. 인용 시 주의 (⚠️ 앞선 문서 교정)

**`CASE_PROFILES.md`에서 "Huawei anti_washing 0건"을 자기반증의 부재로 해석한 것은 인과를 과잉
귀속한 것이다.** 정확한 서술은 이렇다 — Orange 채널은 **자사 임원이 3,000단어대로 직접 말하는
대담·기조연설** 중심인 반면, Huawei 채널의 AI 담론 영상은 대부분 **외부 전문가 인터뷰이거나
800~1,000단어의 짧은 홍보물**이다. 즉 **임원이 논쟁적 주제로 장시간 발화하는 포맷 자체가 이 코퍼스에
존재하지 않는다.** 이 부재는 관찰 대상이되, "화웨이 임원이 반증을 회피했다"로 읽으면 안 된다.

- Huawei 인터뷰의 발화자는 화웨이 직원이 아니라 초청 연사다. **"화웨이의 주장"이 아니라 "화웨이가
  자사 채널에서 유통시킨 담론"**으로 기술해야 한다.
- Huawei 영상의 "음악"은 `[Music]` 태그 오역이다. "음악 산업"·"음악 채굴"은 실제로는 telecom·mining이다.
- VivaTech 기조연설의 발단 사건은 자막 훼손이 심해 **지시 대상을 특정할 수 없다.**

---

# 10. Wayve ↔ Zoox — 무엇을 증거로 볼 것인가

## 10-1. 읽은 자료 (12편 중 핵심)

| 업로드일 | 자막 | 영상 | 회사 |
|---|---|---|---|
| 2020-12-14 | ko | [Code to Road: How Zoox Drives Autonomously](https://www.youtube.com/watch?v=ga8D0Ezgydw) | Zoox |
| 2022-09-26 | ko | [Wayve Presents: The Industry's First Generalisable AI Driver](https://www.youtube.com/watch?v=M68-zq15u2w) | Wayve |
| 2023-04-26 | ko | [Landing a job at Zoox with CTO Jesse Levinson](https://www.youtube.com/watch?v=mqykRkCYfQQ) | Zoox |
| 2023-05-11 | ko | [Embodied AI for Autonomous Driving](https://www.youtube.com/watch?v=ioL4Vhf5UYw) | Wayve |
| 2024-07-23 | ko | [10 Years of Zoox. Reflections and Predictions.](https://www.youtube.com/watch?v=DYcujjMs3Uo) | Zoox |
| 2024-07-25 | **en** | [CVPR24 E2EAI: Jamie Shotton](https://www.youtube.com/watch?v=a_q3Efh6-5E) | Wayve |
| 2025-01-29 | **en** | [Blueprints for the Future: System Design of the Zoox Robotaxi](https://www.youtube.com/watch?v=nT2_wTm6O6E) | Zoox |
| 2025-07-17 | ko | [Ride The Wayve with CEO Alex and VP of AI Vijay](https://www.youtube.com/watch?v=TQfNIb79Ju8) | Wayve |
| 2026-06-25 | ko | [Inside The Ride: Scaling Zoox, Episode One](https://www.youtube.com/watch?v=6srqKuBN0NE) | Zoox |

## 10-2. 이 대립의 정체 — '학습 대 규칙'이 아니다

**Wayve의 아키텍처 논거는 정확도가 아니라 (a) 사업 지속가능성과 (b) 정보이론이다.**

> "this can work right there are fantastic proof points of this in the world um and uh you know it it does work but uh it comes with a very high cost and **nobody has yet done this** uh in a wa..."
> — Jamie Shotton(Wayve 최고과학자), [2024-07-25](https://www.youtube.com/watch?v=a_q3Efh6-5E)

> "imagine you could get into a vehicle and put on the world's perfect a perfect head mounted display that turned your camera sensors your your eyes into a perception so it just visualize the b..."
> — Jamie Shotton, [2024-07-25](https://www.youtube.com/watch?v=a_q3Efh6-5E)

**바운딩박스만 보고 운전하겠느냐**는 사고실험이 정보 병목 논증이다.

**Zoox가 거부하는 것은 학습이 아니라 '학습을 안전 논증으로 대체하는 것'이다.**

> "안전성 검증을 위해서는 단순히 '우리가 놀라운 AI를 만들었고, 꽤 괜찮아 보이고, 많은 데이터로 훈련시켰으니 잘 작동하길 바라자. 그리고 안전 운전자가 너무 자주 제어권을 넘겨받지 않으니 어떻게 되는지 보자'라고 생각하는 것만으로는 충분하지 않습니다. **그런 식으로 로보택시를 만들고 도시에 안전하게 배치할 수 없습니다.**"
> — Jesse Levinson(Zoox 공동창업자 겸 CTO), [2024-07-23](https://www.youtube.com/watch?v=DYcujjMs3Uo)

> "필요조건은 확실하지만, **충분조건과는 거리가 멀죠.**" (개입 횟수 지표에 대해)
> — Jesse Levinson, [2024-07-23](https://www.youtube.com/watch?v=DYcujjMs3Uo)

**그리고 Zoox는 처음부터 하이브리드였다.** 2020년 영상이 이를 증명한다.

> "기하학적 기법부터 최신 머신러닝 기술까지 다양한 접근 방식을 결합하여 사람, 자동차, 트럭, 자전거 및 기타 물체를 감지하고 분류합니다."
> — 내레이션, [2020-12-14](https://www.youtube.com/watch?v=ga8D0Ezgydw)

**따라서 이 대립은 '일반화를 증거로 볼 것인가, 정량화된 잔여 위험을 증거로 볼 것인가'의 대립이다.**

## 10-3. 데이터 규모의 시점 서사

2022년 Wayve의 일반화 주장 근거는 **데이터 효율**이었다.

> "우리는 수천 시간의 승용차 데이터로 학습시킨 모델에 **약 80시간의 밴 데이터**를 추가하여 우리의 밴과 기존 승용차 모두에서 운전할 수 있는 모델을 학습시켰습니다."
> — Wayve 엔지니어, [2022-09-26](https://www.youtube.com/watch?v=M68-zq15u2w)

2025년에는 **데이터 규모**로 바뀐다.

> "수십 파바이트에서 수백 파바이트에 이르는 훈련 데이터를 활용하여 업계 최고 수준의 인공지능 모델을 구축하고"
> — Vijay(Wayve VP of AI), [2025-07-17](https://www.youtube.com/watch?v=TQfNIb79Ju8) *('파바이트'는 petabyte 자막 훼손)*

> "지난 90일 동안 유럽, 아시아, 북미 전역의 **90개 이상의 도시**를 운전해 봤다는 것입니다. 제게 가장 흥미로웠던 점은 **그 도시들 중 절반 정도는 우리가 운전하던 차량에서 얻은 데이터가 전혀 없었다**는 것입니다"
> — Vijay, [2025-07-17](https://www.youtube.com/watch?v=TQfNIb79Ju8)

## 10-4. 양쪽 모두 상대 프레임을 차용한다 — 이 사례의 핵심 균열

**Wayve가 Zoox의 검증 프레임을 차용한다.**

> "성능에 대한 기대치가 높을 뿐만 아니라 어떤 제품이든 출시하기 전에 **성능 수준을 검증하고 실제로 입증해야 한다**는 부담이 매우 크다는 점이 당연합니다"
> — [2025-07-17](https://www.youtube.com/watch?v=TQfNIb79Ju8)

**카메라 온리를 확장성 근거로 내세운 바로 그 영상에서 중복 감지로 후퇴한다.**

> "핸즈프리 주행 시스템에는 훌륭한 구성일 수 있지만... 눈을 떼거나 운전자가 없는 시스템을 구축하는 경우, 단기적으로는 **중복 감지 방식을 사용하는 것이 현명**할 거라고 생각합니다. 그래서 저희는 카메라, 레이더, 서라운드 카메라, 서라운드 레이더, 그리고"
> — [2025-07-17](https://www.youtube.com/watch?v=TQfNIb79Ju8)

**Zoox는 반대 방향으로 움직인다.** 하이브리드를 옹호한 같은 대화에서 방향은 상대 쪽이다.

> "다만 점점 더 규모가 크고 범용적인 지능을 가진 모델 쪽으로 기울어질 거라고 예상할 뿐, **모든 안전장치를 완전히 제거하는 단계까지는 아직 멀었다**고 생각합니다."
> — [2026-06-25](https://www.youtube.com/watch?v=6srqKuBN0NE)

## 10-5. Zoox의 도입률·실패 자인

> "we're proud of the hard driving we're doing but **we're not driving enough places for it to be very useful yet**"
> — [2025-01-29](https://www.youtube.com/watch?v=nT2_wTm6O6E)

**출시 직전 운행 영역을 잘라낸 실패**도 공개된다.

> "우리는 좁은 틈새로 비집고 들어갈 수 없어서 꼼짝 못 하게 되는 경우가 많았는데, 사실 **너무 예의 바른 성격이었기 때문**이기도 해요... 그래서 우리는 지오 펜싱의 그 부분에 대해서는 아직 준비가 덜 됐다는 것을 깨달았습니다."
> — [2026-06-25](https://www.youtube.com/watch?v=6srqKuBN0NE)

신뢰성 실측치도 나온다.

> "이제 로보택시는 **수만 마일을 운행할 때마다 한 번씩 멈춰** 서게 됩니다. 하지만 저희는 로보택시 운행 대수를 수천 대로 늘리면서 그 횟수를 수십만 마일까지 늘리는 것을 목표로 하고 있습니다."
> — [2026-06-25](https://www.youtube.com/watch?v=6srqKuBN0NE)

## 10-6. 인용 시 주의 (⚠️ 앞선 문서 재교정)

- `CASE_PROFILES.md`에서 Zoox를 "조건부·점진 채택"으로 고친 것은 맞지만 **여전히 불충분하다.**
  정확한 서술은 — Zoox가 완전 엔드투엔드로 가지 않는 이유는 **(1) 아직 인간보다 안전하지 않음
  (2) 설명 불가 (3) 행동 수정의 어려움** 세 가지이고, VLA 모델 '장면 IQ'는 차량을 직접 몰지 않고
  **AI 스택에 힌트를 주는 백그라운드 조언자**로 배치되며, 320억~1,000억 파라미터 모델은 **차상 실시간
  실행이 아니라 오프라인 시나리오 생성·분류용**이다.
- ⚠️ **일반화 주장의 핵심 수치가 자막에서 정반대로 훼손된 사례가 있다.** "약 15% 정도가... 그 결과
  **일반화 능력이 전혀 없는 것으로 나타났습니다**"는 문맥상 제로샷 일반화 성공을 말한 것으로 보이나
  번역 결과가 반대 의미다. **원문 확인 없이 인용 금지.**
- 'Ride The Wayve' 데모는 Alex와 Vijay가 번갈아 말하며 **화자 태그가 없어** 문장 단위 귀속이 불확실하다.
- Zoox 자막에서 회사명이 'Zuk/Zeus/스즈키/제우스', robotaxi가 '로보세금/로봇세'로 훼손된다.

---

# 11. 삼성SDS · 우리은행 — 수요기업 사례가 만들어지고 수정되는 과정

## 11-1. 읽은 자료 (9편)

⚠️ **이 코퍼스의 파일에는 프론트매터에 `업로드일` 필드가 없다.** 실제 필드 구성은
`영상 링크 / 채널 / 검색 키워드 / 자막 언어 / 단어 수`다. 아래 표의 날짜는 **수집일 폴더명**이며
**게시일이 아니다.** 논문에서 폴더명을 게시일로 쓰면 안 된다.

| 수집일 폴더 | 영상 | 성격 |
|---|---|---|
| 2026-07-18 | [제조업 AX의 골든 타임 (IT슈다)](https://www.youtube.com/watch?v=iAbE9YXnbqA) | 삼성SDS×KASMO 공동 토크쇼 |
| 2026-07-21 | [2024 AI 트렌드 총정리 2](https://www.youtube.com/watch?v=_FfB0sPuhr8) | 자사 채널 대담 |
| 2026-07-21 | [AI&CLOUD2026 세션1 (IT조선 주최)](https://www.youtube.com/watch?v=mHbsngztlHw) | 외부 컨퍼런스 발표 |
| 2026-07-21 | [LG CNS: Leading the Future of Chemical Industry with AX](https://www.youtube.com/watch?v=tdUBajpHiGY) | 396단어 브랜드 필름 |
| 2026-07-21 | [SK AX, a new partner for AX innovation](https://www.youtube.com/watch?v=IIUd_CB4azI) | 192단어 브랜드 필름 |
| 2026-07-23 | [AX Summit 키노트 2 (신계영)](https://www.youtube.com/watch?v=PsfnMJwSoXs) | 자사 주최 서밋 |
| 2026-07-26 | [AI-Native 기업으로 전환 전략과 사례](https://www.youtube.com/watch?v=Y-ApGj-9ceI) | 확장판 키노트(5,546단어) |
| 2026-07-26 | [ChatGPT Enterprise 도입전략](https://www.youtube.com/watch?v=oXxq-xeAoJQ) | OpenAI 공동 웨비나 |
| 2026-07-26 | [AI for AI: Building the Transformation Office (Tigerhall)](https://www.youtube.com/watch?v=OJwpw-8SkBM) | 글로벌 SaaS 웨비나 |

## 11-2. 우리은행 사례의 3중 구조

> "우리 은행은... 작년 한 해 동안 회사를 AX로 전환하겠다. **우리는 금융 회사지만 우리는 앞으로 AX 회사다**라고 선언을 어 대표님께서 선언을 하시면서 1년 동안 5대 업무를 선정을 하고 5대 업무에이 **27개 핵심 업무에 175개 이상의 에이전트**를 만들겠다라고..."
> — 신계영(삼성SDS AX센터 AI사업팀장 부사장), [AX Summit](https://www.youtube.com/watch?v=PsfnMJwSoXs)

**주목할 점은 삼성SDS가 (1)선언과 (2)설계의 저자가 아니라는 것이다.** 선언은 은행장이, 설계는 외부
컨설팅사가 했다. 그런데 키노트에서 이 세 겹은 하나의 매끄러운 '고객 여정'으로 봉합되고, 마지막에
**"이 여정은 저희 패브릭스 기반으로"**가 붙는다.

## 11-3. 이 사례의 결정적 발견 — 숫자의 유동성

**외부 컨퍼런스에서는 상향 판정이 명시적으로 발화된다.**

> "다섯 개 업무에 175개 에이전트가 들어가서... AX를 전환하겠다라고 했는데 **저희가 들어가서 이제 판단을 해 보니까 175개가 아니라 최소 300개 그 이상의 에이전트들이** 어 실제로 어 구축이 되고 운영이 되고..."
> — 신계영, [AI&CLOUD2026](https://www.youtube.com/watch?v=mHbsngztlHw)

**즉 고객이 1년간 컨설팅으로 만든 설계도가, 벤더가 들어간 순간 부족한 것으로 재분류된다. 그리고 그
격차 125개 이상이 곧 추가 수주 범위다.**

자사 주최 서밋에서는 **상향의 근거가 사라지고 두 숫자가 나란히 놓인다.**

> "이 여정은 저희 패브릭스 기반으로... 그 플랫폼 기반에 다양한 어 **300여개 이상의 에이전트들**을 만들어 나가고요."
> — 신계영, [AX Summit](https://www.youtube.com/watch?v=PsfnMJwSoXs)

**핵심업무 수도 자리마다 흔들린다.**

> "올해 5월부터는 저희 SS와 함께 어 이렇게 **29개 핵심 업무에 175개 에이전트**를 올해 연말 내년 상반기까지 두 차례로 끊어가면서..."
> — 신계영, [확장판 키노트](https://www.youtube.com/watch?v=Y-ApGj-9ceI)

27개(AX Summit) ↔ 29개(확장판). **사례는 고정된 사실이 아니라 발표 자리에 따라 재조정되는 서사
자원이다.**

## 11-4. 조직 서사 — 벤더가 자기 자신을 첫 레퍼런스로 삼는다

> "**이건 저희 SDS의 실제 사례입니다.** 저희 SDS에서는 어 작년만 조직 개표를 통해서 전사적으로 에이전트를 만들고 개발하고 운영하시는 분들을 하나의 조직으로 만들어서 AX 센터를 만들고 CAIO를 선임을 해서..."
> — 신계영, [AX Summit](https://www.youtube.com/watch?v=PsfnMJwSoXs)

> "현재 AI 크루가 **107명**이 활동을 하고 있고 어 연말에 AI 서밋을... 잘 선정이 된 분들한테는 좀 꽤 큰 좀 어 상금 또 해외 연수기회 이런 것들을 제공을 하고 있습니다."
> — 신계영, [확장판 키노트](https://www.youtube.com/watch?v=Y-ApGj-9ceI)

**그런데 같은 발표자가 후발주자임을 인정한다.**

> "저희도 **다른 회사 IT 회사보다 좀 늦게** 좀 AX센터 출범을 했습니다. 작년 12월에..."
> — 신계영, [확장판 키노트](https://www.youtube.com/watch?v=Y-ApGj-9ceI)

**방법론의 권위가 선행 성과가 아니라 '우리도 겪고 있다'는 동병상련에서 나온다.**

## 11-5. 탑다운의 정의 — 이 코퍼스에서 가장 직설적인 발화

> "근데 반대로 탑다운 오프로치는 저희는 좀 되게 과격하게 생각을 해요. 그래서 야 **특정이 부서 없어지면 큰일 나. AI가 들어와서 한번 없애 보자. AI로 한번 없애 볼까? 이 업무 프로세스 한번 전체를 사람 한번 빼 볼까?** 이런 어프로치가 저희는 탑 어프로치 생각을 하거든요."
> — 신계영, [확장판 키노트](https://www.youtube.com/watch?v=Y-ApGj-9ceI)

**ROI 측정 가능성이 곧 인력 감축 가능성과 등치된다.**

## 11-6. 균열 — 같은 회사, 다른 무대, 반대 처방

**자사 키노트는 '과격한 탑다운'을, 공공기관 공동 토크쇼는 '바텀업'을 처방한다.**

> "그래서 하나 또 강조드리는 것은 이렇게 **탑다운 방식으로 뭐 AI 이런 거 써 이게 아니라 정말 바텀업 방식으로** 그 현장의 어 인직원들이 겪고 있는 그런 고충 고층에서 출발을 해야 된다."
> — 김지현(삼성SDS 컨설팅팀 제조컨설팅그룹), [IT슈다](https://www.youtube.com/watch?v=iAbE9YXnbqA)

**같은 인물이 키노트의 성공 서사와 정면으로 어긋나는 실측 증언을 한다.**

> "근데 만나본 **대부분의 고객들이** P나 파일럿 이런 것들은 이제 진행을 다해 본 상태고 그리고 현재는 **AX 전담 조직까지 이제 구성을 해서 좀 확산을 하려고 하고 있는데 이게 잘 확산이 잘 안 되고 있어요.**"
> — 김지현, [IT슈다](https://www.youtube.com/watch?v=iAbE9YXnbqA)

**즉 키노트가 파는 처방(조직 신설 + 크루 선정) 자체의 유효성이 같은 회사 현장 인력에게 흔들린다.**

**탑다운 AX의 전제도 자기 발화로 부정된다.**

> "최근에는 어 전체 삼성에 있는 **CEO 또 임원 레벨에도 AR 리터리시가 생각보다 높지 않다**라는게 저희 이제 그룹사에서 오프타 리코드를 말씀드립니다만 반달 진단한 어 그런 결과가 나와서 임원들도 어 뭐 2박 3일씩 이제 합숙을 해서 교육을..."
> — 신계영, [AI&CLOUD2026](https://www.youtube.com/watch?v=mHbsngztlHw)

**그리고 벤더 채널에 실린 가장 강한 반증 데이터.**

> "실제로 최근에 해외 보고서들 보면이 **AI 프로젝트의 실패율이 80%**라는 얘기가 나와요 이게 실제 it 일반적인 프로젝트의 실패율이 두 배가 넘습니다... **장님이 장님을 인도해서 그런다** 이런 표을 쓰더라고요"
> — 대담 진행자(외부 '소장'), [2024 AI 트렌드](https://www.youtube.com/watch?v=_FfB0sPuhr8)

**포지션 전환**도 잡힌다. "자체 LLM 만들면 사단난다"던 회사가 "국내기업 최초 ChatGPT Enterprise
리셀러"로 이동하고, 그러면서 **자사 제품의 결정적 한계를 인정한다.**

> "하지만 채 GPT 엔터프라이즈는 클라우드 기반 사스 서비스입니다. 따라서 **완전한 폐쇄망에서의 직접 사용은 불과합니다.**"
> — [ChatGPT Enterprise 도입전략](https://www.youtube.com/watch?v=oXxq-xeAoJQ)

보안·온프레미스를 최대 차별점으로 내세우던 회사가 리셀링 제품에서는 정반대를 말한다.

## 11-7. 비교축 — 한국 벤더와 글로벌 SaaS의 신뢰 조달 방식

| | 신뢰를 어떻게 조달하는가 | 분량 |
|---|---|---|
| **삼성SDS** | 고유명사(우리은행·삼성전자·삼성바이오로직스·첼로스퀘어) + 수치(175/300, 107명, 만여 개) | 3,000~5,500단어 |
| **LG CNS** | "AX leader"라는 자기 라벨만. 고객사명·수치·발표자 **전무** | 396단어 |
| **SK AX** | 사명 변경 알림. "AX를 상상해 보세요" | 192단어 |
| **Tigerhall** | 고객사명을 지우고 **메커니즘**만(컨텍스트 레이어, 데이터 플라이휠, 60:40 거버넌스, 90일 91% 도입률) | 웨비나 |

**한국 벤더는 '누가 했는가'로, 글로벌 SaaS는 '어떻게 작동하는가'로 신뢰를 조달한다.**

## 11-8. 인용 시 주의 (⚠️ 중대)

- **업로드일 부재.** 9개 파일 전부에 업로드일 필드가 없다(`transcripts/2026-07-18·21·23·26` 전체 grep
  확인, 매치 0건). 인용 시 **원 영상에서 게시일을 별도 확인**해야 한다.
- **타임라인은 추정이다.** 위 순서는 수집일 폴더 + 스크립트 내부 시점 단서("작년 12월", "올해 5월부터",
  "25년 11월", 행사명)로 재구성했으며 실제 게시 순서가 뒤바뀔 수 있다.
- **수요기업 당사자의 직접 발화는 이 코퍼스에 없다.** AX Summit에 "김수현 전문님 발표해 주셨는데"라는
  언급이 있어 우리은행 실무자의 별도 세션이 존재하지만 그 트랜스크립트는 수집되지 않았다.
  **따라서 이 사례가 다루는 것은 '우리은행이 무엇을 했는가'가 아니라 '삼성SDS가 우리은행을 어떻게
  이야기하는가'다.**
- 자막 오염: "채치T/최치피/제치피트"(ChatGPT), "이i 컨설팅"(우리은행 컨설팅사, **사명 판독 불가**),
  "AS SDS/SS/STS"(삼성SDS), "안목지/암목지"(암묵지).

---

# 12. 이 문서가 앞선 문서에서 교정한 것

원본 스크립트를 정독한 결과, `CASE_PROFILES.md`의 다음 서술을 교정한다.

| 위치 | 기존 서술 | 교정 |
|---|---|---|
| Palantir | 관세 "연 $88,000 절감"을 성과로 인용 | `Chad & X` 시리즈는 **가상 고객 'Onyx Inc.'의 시연용 설정값**이다. 성과 증거로 쓸 수 없다 |
| Zapier | "8명이 $5B 운영" | **스크립트 본문에 없다.** "5B"는 **영상 제목 줄에만** 존재한다. '제목의 주장'으로만 표기할 것 |
| Huawei | anti_washing 0건 = 자기반증 부재 | **포맷 부재**다. 임원이 논쟁적 주제로 장시간 발화하는 형식 자체가 이 채널에 없다. 인과 과잉 귀속 금지 |
| AMD | "AMD 96% 도입 준비" | 출처는 **레노버 자체 설문**이고 내용은 **의향**이다. AMD 발화가 아니다 |
| Zoox | "조건부·점진 채택" | 방향은 맞으나 불충분. 거부 이유 3가지(안전 미달·설명 불가·수정 곤란), VLA는 **조언자**, 대형 모델은 **오프라인 전용** |
| 삼성SDS | 수집일을 시점으로 사용 | **업로드일 필드가 존재하지 않는다.** 폴더명은 수집일이다 |
| 삼성SDS | "175개 이상 에이전트" | 벤더가 **"최소 300개 이상"으로 상향 판정**했고, 자리마다 27개/29개로 흔들린다 |

## 새로 확인된 사실

- **NVIDIA에는 토큰 경제학 전용 영상군이 존재한다** — `Extreme Co-Design for Efficient Tokenomics`,
  `How AI Factories Maximize Tokens, Power, and Profit`, `Why Cost Per Token Is the Only Metric You
  Need for AI TCO`, `Inside AI Tokenomics`. 분모=토큰 주장의 근거는 계량표가 아니라 이 영상군이다.
- **Siemens 서사는 2025-12-30과 2026-01-07 사이 8일 만에 뒤집힌다.** 자기 데이터 품질 부정 →
  "산업 AI 혁명을 주도하고 있습니다".
- **IQVIA에는 예외 기반 모델 전용 제품 영상군이 있다** — Vigilance Platform, IVP Collect,
  Detect+Extract, The Future of Work. 임계값을 **고객사가 코드 없이 조정**한다는 것이 핵심이다.
- **Unilever의 IR 자료는 AI 주장이 재무 검증선 앞에서 멈추는 지점을 반복적으로 기록한다.**
  2024-11의 '4%' 이후 새로운 실측 수치는 2026-07까지 제시되지 않는다.
