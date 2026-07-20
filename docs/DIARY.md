# Research Diary — AX 유튜브 담론 데이터 구축

> 표기 규약(DSL protocol): 중요 keyword/phrase는 **굵게**, 중요 문구/문장은 <u>밑줄</u>,
> 그중 더욱 중요한 내용은 🔴 표시 (Google Docs로 옮길 때 붉은 글씨로 변환).

---

## 260719 수집 대상 확장: HBR·NVIDIA GTC 사례 기업 추가 (59→118 채널)

### 1) 주요 키워드
**산업별(도메인) 사례 기업**, HBR 케이스, NVIDIA GTC 세션, 채널 목록 확장

### 2) 작업 내용
- HBR AX 사례 문서 + NVIDIA GTC(헬스케어·텔레콤·자율주행·산업·추론·물리) 세션 정리본에
  등장한 **AX 도입 기업들을 수집 채널 목록에 추가** — 59개 → **118개**
- 도메인 6개 신설: 소비재/리테일, 금융/컨설팅, 산업/자동차/로보틱스, 헬스케어/제약,
  엔터프라이즈SW/AI인프라, 텔레콤, 미디어/소셜
- 대표 추가: L'Oréal, IKEA, Amazon, Nike, Unilever, McKinsey, BCG, Accenture,
  Eli Lilly, Novo Nordisk, J&J, GE HealthCare, Mayo Clinic, Nokia, ServiceNow,
  Mercedes-Benz, BMW, GM, Siemens, Caterpillar, T-Mobile, Orange, TCS, Infosys 등

### 3) 의의 (AX 연구 관점)
- <u>공식 채널 = 공급자(벤더) 담론 vs 도입 기업(adopter) 담론을 산업별로 대비 가능해짐</u>
- 🔴 <u>**도메인별 AX 사례 코퍼스**가 K1 기업 공개 자료와 산업코드로 병합할 때
  기업 단위 매칭률을 높이는 기반이 됨</u>

### 4) 이슈
- 신규 핸들은 대부분 **추정값** — 다음 실행 로그의 '접속 실패' 목록으로 검증·수정 예정
  (틀린 핸들은 자동 스킵되어 안전)
- 채널 급증으로 채널별 백필 속도는 느려지나, 하루 5회·회당 150건 상한 내에서 순환 수집

### 5) 제외한 항목
- 가명(Acme Bank), 공식 채널 부재(Midjourney·DeepSeek), 소규모 스타트업 다수
  (Nablo Bio, CytoReason, Corti, Basecamp Research, Proda 등)

---

## 260628 시스템 구축: AX 유튜브 스크립트 자동 수집기 착수

### 1) 주요 키워드
**AI Transformation(AX)**, **YouTube 스크립트 수집**, **yt-dlp**, **GitHub Actions 자동화**, 바이브코딩

### 2) 작업 내용
- 유튜브에서 **AX 관련 영상의 자막(스크립트)을 매일 자동 수집**하는 시스템 구축 착수
- 검색 키워드: 한국어 4개 + 영어 3개 (AX AI 전환, AI Transformation, Enterprise AI adoption 등)
- <u>수집물은 날짜별 폴더에 영상별 마크다운 파일로 저장, 중복은 `_seen.json`으로 영구 관리</u>

### 3) 작업 방식
- **바이브코딩**(Claude Code): 자연어 지시로 코드 작성·실행·배포 전 과정 진행
- **yt-dlp** 사용 — <u>YouTube 공식 API 키 없이 검색·자막 추출 가능, 쿼터 제약 없음</u>
- **GitHub Actions cron**으로 서버리스 자동 실행 (개인 PC 불필요, 공개 저장소는 무료)

### 4) 진도
- 저장소 연결·쓰기 권한·Actions 활성화 설정 완료 (GitHub App 권한, Workflow permissions)
- 저장소 보안 정책(모든 action의 커밋 SHA 고정 요구) 대응 — 외부 action 없이 러너 기본 git/python만 사용하도록 재작성
- 첫 실행 성공: **검색 단계는 정상 작동** (AX 관련 한/영 영상 30여 개 탐지 확인)

### 5) 이슈
- 🔴 **유튜브 봇 차단**: <u>GitHub Actions 서버 IP를 유튜브가 "Sign in to confirm you're not a bot"으로 차단하여 자막 수집 0건</u> — 클라우드 서버에서 흔한 문제로 확인
- 실패 시 에러 문구가 자막처럼 저장되는 버그 발견 → 수정 완료

---

## 260718 수집 정상화: 쿠키 인증으로 봇 차단 해소, 첫 실수집 성공

### 1) 주요 키워드
**쿠키 인증(YOUTUBE_COOKIES Secret)**, 봇 차단 우회, 첫 실수집

### 2) 작업 내용
- <u>유튜브 로그인 쿠키를 GitHub Secret으로 등록하여 봇 차단 우회</u> — 브라우저 확장(Get cookies.txt LOCALLY)으로 내보낸 쿠키를 `YOUTUBE_COOKIES`에 저장, 워크플로우가 실행 시 파일로 복원
- 자막 전용 수집 시 발생한 format 오류(`Requested format is not available`)를 `ignore_no_formats_error` 옵션으로 해결

### 3) 진도
- 🔴 **첫 실수집 성공: 30개 영상의 실제 자막 확보** (한국어: KBS 'AX 인공지능 전환' 등 / 영어: BCG 'Leading an AI Transformation' 등, 최대 6,271단어)
- 수동 자막·자동 생성 자막 모두 수집, 한국어 우선·영어 차선 언어 선택 로직 검증

### 4) 이슈
- 🔴 <u>**쿠키는 수 주 단위로 만료됨** — 수집이 0건으로 떨어지면 쿠키 재발급·Secret 값 교체 필요 (유지관리 포인트)</u>

---

## 260719 수집 확장: 하루 3회 실행 + 공식 채널 74개 백필(2020~) 설계

### 1) 주요 키워드
**하루 3회 수집**, **공식 채널 74개**, **2020년~ 백필**, 시간 예산(time budget)

### 2) 작업 내용
- 실행 주기를 **매일 3회(한국시간 06/14/22시)**로 확대, 날짜·회차 기록을 KST 기준으로 정리
- <u>AI 생태계 공식 유튜브 채널 74개(파운데이션 랩·하이퍼스케일러·반도체·인프라·생성미디어·로보틱스·중국·한국 12개 분야) 목록화</u> — OpenAI, Anthropic, Google DeepMind, NVIDIA, 네이버클라우드, LG AI Research 등
- **2020년 1월 이후 전체 영상**을 대상으로 하는 채널 백필 수집기(`fetch_channels.py`) 구축

### 3) 작업 방식
- <u>회당 최대 250개(채널당 8개)씩 최신순으로 점진 백필 — 하루 최대 750개, 수만 개 규모 전체 완성까지 수 주 소요 예상</u>
- 채널 순서 셔플로 회차 간 고른 진행, 자막 없는 영상은 기록 후 재시도 방지

### 4) 진도
- 채널 수집기 구축·배포 완료, 첫 백필 실행 진행 중

### 5) 이슈
- 🔴 **6시간 강제취소 사고**: <u>첫 채널 수집 실행이 시간 제한 장치 부재로 GitHub 작업 한도(6시간)에 걸려 강제 취소, 수집분 유실</u>
- 재발 방지 조치 완료: **시간 예산 90분**(초과 시 저장 후 정상 종료), **요청당 타임아웃 20초**, **채널당 시도 상한 25개**, 작업 한도 150분
- 일부 채널 핸들은 추정치 — 실행 로그의 '접속 실패' 목록으로 검증·수정 예정

---

## 260719 분석 파이프라인: DX/AX/AT 분류·요약 자동화, K1 연계 설계

### 1) 주요 키워드
**DX/AX/AT 분류**, **코드북**, **담론 지수**, **K1 기업 공개 자료 연계**, Algorithmic Transformation

### 2) 작업 내용
- **분류 코드북**(`docs/CODEBOOK.md`) 작성 — <u>DX(디지털 전환) → AX(AI 전환) → AT(알고리즘 전환)를 배타적 범주가 아닌 **심화 스펙트럼**으로 정의</u>
  - 🔴 <u>**연구의 궁극 프레임은 Algorithmic Transformation** — 의사결정 권한이 알고리즘으로 이동하는 단계 (cf. algorithmic management, Kellogg et al. 2020)</u>
- **사전(dictionary) 기반 자동 분류기**(`classify.py`): 한/영 키워드 패턴, 다중 라벨 점수 + 지배 라벨, 최소 등장 규칙
- **메타데이터별 요약 정리**(`summarize.py`): 영상별 발췌 요약(문장 경계 인식)을 채널별·월×라벨별로 정리
- 매 수집마다 자동 갱신: `analysis/classified.csv`, `monthly_summary.csv`, `summaries.csv`, `SUMMARY_BY_CHANNEL.md`, `SUMMARY_BY_MONTH.md`

### 3) 진도
- 초기 34건 분류 결과: **AX 25 / DX 4 / AT 0 / 미분류 5** — <u>AT(알고리즘 전환) 담론이 아직 희소하다는 것 자체가 첫 관찰</u>

### 4) K1 연계 설계 (계획)
- K1 = **기업 공개 자료** (별도 채널에서 수집 진행 중)
- 설계: <u>유튜브 코퍼스 → 분류 → **[월 × 산업 × 기술유형] 담론 강도 지수** → K1 재무·공시 패널과 산업코드·시점으로 병합</u>
- 분석 방향: 🔴 <u>**AX 담론 급증 이후 t+k 시점의 비용 구조 변화**(인건비 비중, 판관비율, IT 투자) — 이벤트 스터디/DiD; 담론 선행 vs 실적 후행 격차는 'AI 워싱' 측정치로 활용 가능</u>
- 기대 가설: AT(자동화)→직접 인건비 절감 / DX→IT 자본지출 후 판관비 효율화 / AX→<u>초기 비용 증가 후 생산성 효과</u>

### 5) 문헌 기반 (lit review 닻)
- DX: Vial (2019, JSIS); Verhoef et al. (2021)
- AI 도입: Babina et al. (2024, JFE); Brynjolfsson & McElheran; Eloundou et al. (2023)
- 자동화·태스크: Acemoglu & Restrepo (2019; 2020)
- 텍스트 방법론: Gentzkow, Kelly & Taddy (2019, JEL); Bloom, Hassan et al. (기술 확산의 텍스트 측정)
- **포지셔닝**: <u>어닝콜·채용공고·특허 중심의 기존 AI 확산 측정과 달리, **기업 공식 유튜브 담론**은 미개척 소스 — 한/영 동시 수집으로 한국 vs 글로벌 비교 내장</u>

### 6) 이슈 및 다음 단계
- LLM 기반 2차 분류(정확도 향상) 도입 여부 — API 비용 발생, 수만 건 기준 수십 달러 수준부터
- <u>사람 코딩 표본(100~200건)으로 자동 분류 검증(Cohen's κ) — 방법론 방어용</u>
- 채널 핸들 오류 수정, 백필 진행률 모니터링
- K1 자료 스펙 확정 후 병합 키·집계 단위 확정
