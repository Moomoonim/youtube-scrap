# 수집 콘텐츠 검토 보고서 (2026-07-21)

> 342건(키워드 56 + 채널 286) 전수 정독 기반. 다음 회귀분석·코딩 작업 전에 읽을 것.

---

## 1. 코퍼스 지도 — AI/AX 담론 밀도 순

| 밀도 | 채널 | 성격 |
|---|---|---|
| ★★★ | NVIDIA·NVIDIA Developer, Arm | "AI 팩토리"·에이전트 시대 담론의 발원지. 수치 가장 풍부 |
| ★★★ | LG AI Research, IBM, Salesforce, W&B·Qdrant·Pinecone·Weaviate·Snowflake | AI가 곧 제품. 도입 방법론·평가·거버넌스 담론 |
| ★★☆ | Meta(Boz 팟캐스트), Boston Dynamics, Microsoft Azure, Google Developers, Meta Developers, SK하이닉스, GE HealthCare, Accenture | AI 전환을 자사 제품/비전에 접합 |
| ★☆☆ | SK텔레콤, Telenor, Amazon, Waymo, Mayo Clinic | AI가 마케팅 소재(보안·안전·감성) |
| ☆ | Swisscom(축구 광고 15개), Reckitt, Schneider(채용 영상 6개), NTT DATA(채용), LinkedIn(광고), Luma·Suno, Philips(제모기 광고) | AI 담론 거의 없음 — 그 자체가 신호 |

키워드 수집분(56건, `transcripts/2026-*/`)은 한국어 AX 강의·컨설팅·정책·언론 콘텐츠가 주력이며, 연구 주제에 가장 밀도 높은 그룹.

---

## 2. 주요 발화자·패널

**한국 AX 담론**
- **김건우**(『AI 전환 절대공식』 저자, 가톨릭대 겸임) — 코퍼스 최다 등장. 3S 공식(Small Start→Solid Success→Smart Scaling), "AX=업무 재설계", "에이전트 워싱" 경고
- **김유신 상무**(티타임즈TV) — 데이터 거버넌스, AI+X vs AX 구분, MLOps
- **신계영 부사장**(삼성SDS AX센터) — 우리은행 "AX 회사 선언"(에이전트 175→300개), 삼성전자 에이전트 1만 개+
- **장진석**(BCG 파트너) — "1,200개사 조사: 선도 5%가 매출·이익 60~70% 개선"
- **윤병동**(서울대 교수·원프레딕트 대표) — "DX=자동화, AX=자율화" 공식화
- 이세돌×이홍락(LG AI Research) 대담, 신재인(Vibers.AI), 남대현(TreeSoop) 등

**글로벌**
- 젠슨 황(NVIDIA), Kevin Deierling(NVIDIA 네트워킹 SVP), Will Abbey(Arm CRO/COO)
- Boz(Meta CTO)와 대담 게스트 Shyam Sankar(Palantir CTO)·Ed Catmull(픽사)·Dylan Field(Figma CEO)
- Aaron Levie(Box CEO), Cohere CEO, Peter Arduini(GE헬스케어 CEO), Dave Fredrickson(아스트라제네카 EVP)
- McKinsey Rewired 저자 3인, INSEAD·Wharton 교수진

---

## 3. AX·DX·AI 개념 정의 (코퍼스 합의)

| 개념 | 정의 |
|---|---|
| DX | 아날로그→디지털, 프로세스 **자동화**(정해진 패턴) |
| AX | **자율화**(AI가 판단·의사결정·실행). 도구 도입이 아니라 워크플로 재설계 |
| 관계 | "DX가 먼저 돼야 AX가 가능"(삼성SDS·SK하이닉스·INSEAD 공통 견해) |
| 실체 | 2026년 시점 AX는 사실상 **에이전틱 AI**(오케스트레이션)로 수렴 |

⚠️ **용어 이중성**: 한국·기업 담론 = AI Transformation. 해외 UX 계열(Microsoft Developer, Brave Achievers) = **Agent Experience**(에이전트를 사용자로 보는 설계론). 분류 라벨에 반드시 구분 반영.

---

## 4. 핵심 이슈 6가지

1. **"도입 ≠ 성과"** — MIT "95% 실패", 맥킨지 "88% 사용 vs 수익화 39%", "AI 프로젝트 실패율 80%(일반 IT의 2배)", "직원 78% 섀도 AI(70% 은닉)". 처방: 문제 정의 → 스몰 스타트 → 거버넌스 → 경영진 스폰서십.
2. **"AI 팩토리·토큰 경제학"**(NVIDIA·Arm) — "데이터센터=비용센터→AI공장=토큰 수익원", 전력이 절대 제약. 자사 유리한 KPI로 측정 프레임 재정의(동시 에이전트 수, 와트당 성능).
3. **비용 담론 양면** — 판매측 "온디바이스=데이터센터 비용 소멸"(Google·Qualcomm), "소프트웨어가 싸지면 프로세스가 비싸진다"(Sankar) / 리스크측 토큰 비용 폭증, SBS "클로드 251억 원 오청구" 사건.
4. **노동** — "대체 아닌 증강"이 공식 프레임이나 수치는 양방향("동일 급여로 인력 2배", "시설관리 인력 65% 감축").
5. **AI 워싱 스펙트럼** — 강함: 스포츠 스폰서십+AI buzzword(Accenture WTA·골프), 자막 없는 "Gemini Robotics" 제목(Boston Dynamics), 수치 전무 플랫폼 홍보(Schneider Foresight). 反워싱 발언도 공존("AI는 틀렸을 때조차 확신에 차 있다" — GE). 판별 지표: **AI를 전면에 내세울수록 정량 성과 부재**(정량성의 역설).
6. **한국 특유 담론** — 정부 주도(M.AX/MX 얼라이언스 1,300개 단체, AI 기본법), DX 실패 트라우마, AX 컨설팅 시장 급속 상업화, 주권 AI("미국 10 vs 한국 7" — 이홍락).

---

## 5. 대표 수치·사례 (인용 가치 높음)

| 사례 | 수치 | 출처 |
|---|---|---|
| JP모건 | 32만 명 중 20만 명 LLM 사용 | 김건우 강연 |
| 월마트 | 150만 명 대상 AI 도구 | 〃 |
| 모더나 | GPT 750종, 직원 40% 직접 제작 | 〃 |
| 우리은행 | "AX 회사" 선언, 에이전트 175→300개 | 삼성SDS 신계영 |
| 삼성전자 | 에이전트 1만 개+, 시장조사 에이전트가 연 100억 조사비 대체 | 〃 |
| NVIDIA 내부 | 월 4조 토큰, 일 2억 추론, 수요 월 40%↑ | AI Factory Insider |
| ServiceNow | L1 티켓 90% 자율 해결 | NVIDIA Developer |
| BCG 조사 | 선도 5% 기업 매출·이익 60~70% 개선 | 장진석 |
| Harvard×BCG | AI 쓴 컨설턴트 과제 +12%, 속도 +25%, 품질 +40% | Cole Medin 워크숍 |
| Klarna | AI 퍼스트 → 실패 후 재고용 | 김건우 |
| 에어캐나다 | 챗봇 오안내 배상 판례(2024) | 〃 |
| Stanford 의료 | EKG 모델 1개 10년·$2,800만 / LLM 오류율 35% | Stanford Health Care |

---

## 6. 데이터 품질 이슈 및 조치 내역

1. 🔴 **TCS 채널 오수집 → 수정 완료(2026-07-21)**: `config.py`의 `@TCS` 핸들이 Tata Consultancy Services가 아니라 스위스 자동차클럽(Touring Club Schweiz)을 가리키고 있었음.
   - `config.py`: 핸들을 `@TCSGlobal`(확인된 정식 TCS 핸들)로 교정
   - 기존 오수집분 7건: `transcripts/channels/TCS/` → `transcripts/channels/Touring_Club_Schweiz/`로 이동, `_seen.json` 및 각 md 메타데이터의 채널명도 정정
   - 다음 회차부터 `Touring_Club_Schweiz`와 별개로 진짜 TCS 콘텐츠가 `channels/TCS/`에 새로 쌓임
2. **노이즈 채널** — Swisscom(동일 축구광고 15개), Philips(제모기 광고), Suno(음악), NTT DATA(채용 홍보): AX 분석 코퍼스에서 별도 분류 권장. 분석에서 자동 제외하려면 `classify.py`/`extract_cases.py`에 채널 화이트/블랙리스트 추가 검토.
3. **자동번역 오류 체계적** — "humanities→music", "BEIR→맥주", "Nemotron→네마트론" 등. 인용 전 원문 확인 필수(HANDOVER 원칙과 동일).
4. **빈 자막 파일** — "[음악] 우." 등 실질 내용 없는 파일 다수(Boston Dynamics 티저 6개 등). 텍스트 분석 시 단어 수 임계값(예: 50단어 미만) 필터링 권장.
5. **AX 용어 이중성**(§3) — 분류 라벨에 반영 필요.

---

## 7. 연구(AX 담론→기업 비용구조) 최우선 자료 10선

1. NVIDIA COMPUTEX 기조 — "비용센터→토큰 수익원" 담론의 정점
2. Meta Boz×Shyam Sankar(Palantir) — "소프트웨어가 싸지면 프로세스가 비싸진다"
3. 삼성SDS 신계영 발표 — 한국 대기업 KPI 3층·에이전트 거버넌스 실무
4. 김건우 시리즈(6편+) — 한국 AX 담론의 표준 문법
5. Arm Will Abbey 대담 — "토큰은 산출이 아니라 투입" AX 회의론
6. Meta WhatsApp Max Pricing — AI 최적화 명목의 과금구조 재설계
7. Google 온디바이스 AI 워크숍 — "데이터센터 비용 소멸" 프레임
8. Boston Dynamics 웨비나 — "자동화 통합 1건=1년·$100만" 휴머노이드 경제학
9. 맥킨지 State of AI + BCG 장진석 — 도입-성과 괴리의 정량 기준선
10. GE 심박출량 강연 — "미충족 수요를 수치로 제시해 도입을 정당화"하는 담론 구조
