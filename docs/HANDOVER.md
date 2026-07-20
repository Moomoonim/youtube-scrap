# AX 유튜브 스크립트 수집 시스템 — 인수인계 문서 (HANDOVER)

> 새 세션/새 저장소에서 이 프로젝트를 이어받기 위한 완전한 정리본.
> 작성: 2026-07-20 (마지막 코드 커밋 기준: `6d3efd1`)

---

## 1. 프로젝트 개요

**목표**: 유튜브에서 AX(AI Transformation) 관련 담론을 대규모 수집하여
DX/AX/AT로 분류하고, K1(기업 공개 자료)과 병합해 **AX 담론 → 기업 비용 구조
변화**를 분석하는 연구 데이터 기반 구축. (궁극 프레임: Algorithmic
Transformation — 의사결정의 알고리즘화)

**수집 대상**:
1. **키워드 검색**: AX 관련 한/영 키워드 7개, 검색 상위 영상의 자막
2. **공식 채널 118개**: OpenAI·NVIDIA·Microsoft·로레알·Eli Lilly·네이버클라우드 등
   12+개 도메인 (HBR·NVIDIA GTC 사례 기업 포함), **2020-01-01 이후 전체 영상 백필**

**현재 저장소**: `Moomoonim/Moomoonim` (기본 브랜치 `claude/vibe-coding-usage-fpm7ei`)
→ **`Moomoonim/youtube-scrap`으로 이사 예정** (아래 §7)

---

## 2. 수집 방법 (핵심 아키텍처)

```
GitHub Actions cron (하루 5회, KST 06/10/14/18/22시)
  └─ .github/workflows/daily-fetch.yml
      1. 저장소 클론 (외부 action 금지 정책 → git 직접 사용)
      2. YOUTUBE_COOKIES Secret → cookies.txt 복원   ← 봇차단 우회 (필수!)
      3. PO 토큰 제공기 실행 (docker: brainicism/bgutil-ytdlp-pot-provider
         + pip: bgutil-ytdlp-pot-provider)           ← 자동자막 인증 (필수!)
      4. fetch_transcripts.py  — 키워드 검색 수집 (회당 최대 30건)
      5. fetch_channels.py     — 채널 백필 수집 (회당 최대 150건, 채널당 8건)
      6. classify.py           — DX/AX/AT 사전 기반 분류
      7. summarize.py          — 메타데이터별 발췌 요약
      8. extract_cases.py      — 회사별 사례 주장 추출 (근거 발췌)
      9. git commit & push (rebase 재시도 3회 — 동시 커밋 충돌 방지)
```

**도구**: `yt-dlp` (API 키 불필요) — 검색·채널 목록·자막(vtt) 취득 → 자체 파서로
타임스탬프/태그/중복 제거 후 마크다운 저장.

**핵심 파라미터** (`config.py`):
| 항목 | 값 | 이유 |
|---|---|---|
| `SLEEP_BETWEEN_REQUESTS_SEC` = 1, `SUBTITLES` = 2 | 요청 간 지연 | 🔴 rate limit 방지 (무지연 시 세션 차단됨 — 실증) |
| `MAX_CHANNEL_TOTAL_PER_RUN` = 150 | 회당 총 상한 | 실행 시간 관리 |
| `MAX_ATTEMPTS_PER_CHANNEL_PER_RUN` = 15 | 채널당 시도 상한 | 자막 없는 채널의 시간 독식 방지 |
| `CHANNEL_TIME_BUDGET_MIN` = 90 | 시간 예산 | 🔴 6시간 강제취소 사고 재발 방지 — 초과 시 저장 후 정상 종료 |
| `SOCKET_TIMEOUT_SEC` = 20 | 요청 타임아웃 | 무한 대기 방지 |
| `CHANNEL_SINCE` = "20200101" | 백필 하한 | 최신순으로 걷다가 2020 이전 도달 시 그 채널 완료 |

**중복/상태 관리**: `transcripts/_seen.json`
- 수집 성공: `{title, channel, lang, upload_date, fetched_at}`
- 자막 없음(`status: no_subs`): **추출이 건강(formats 존재)할 때만** 기록 — 아니면 재시도
- 🔴 연쇄 실패 12회 → 즉시 중단 (죽은 쿠키/차단 상태에서 세션 소모 방지)

**저장 구조**:
```
transcripts/
├── _seen.json                 # 중복 방지 원장
├── 2026-07-18/                # 키워드 수집 (KST 날짜별)
│   ├── README.md              # 회차별 목록
│   └── 제목__영상ID.md         # 제목/채널/키워드/언어/단어수 + 전문
└── channels/채널명/제목__ID.md  # 채널 수집 (업로드일 포함)
analysis/                      # 매 회차 자동 갱신
├── classified.csv / monthly_summary.csv     # DX/AX/AT 분류 (월×라벨 시계열)
├── summaries.csv / SUMMARY_BY_CHANNEL.md / SUMMARY_BY_MONTH.md
└── cases.csv / CASES_BY_COMPANY.md          # 회사별 사례 주장 + 근거 발췌
docs/
├── CODEBOOK.md                # DX→AX→AT 분류 기준 (다중라벨, 검증 절차)
├── DIARY.md                   # 연구 다이어리 (DSL protocol)
└── HANDOVER.md                # 본 문서
```

---

## 3. 필수 설정 (새 저장소에서 반드시 재설정)

1. **GitHub Actions 켜기**: 저장소 Settings → Actions →
   "Allow all actions" + Workflow permissions "Read and write"
2. **`YOUTUBE_COOKIES` Secret**: Settings → Secrets and variables → Actions
   - 크롬 확장 "Get cookies.txt LOCALLY"로 유튜브 로그인 쿠키 내보내기 → 전체 붙여넣기
   - 🔴 **부계정 사용 강력 권장** (본계정 세션이 차단된 전례 있음)
   - 🔴 내보내기 후 해당 브라우저 창에서 유튜브를 더 탐색하지 말 것 (쿠키 회전으로 무효화)
3. (저장소 정책이 SHA 고정을 요구하지 않으면 워크플로우의 "외부 action 금지"
   구조는 그대로 둬도 무방 — 이미 자립형)

---

## 4. 🔴 겪은 문제와 해법 (같은 함정에 빠지지 말 것)

| # | 증상 | 원인 | 해법 (적용됨) |
|---|---|---|---|
| 1 | 자막 0건 + "Sign in to confirm you're not a bot" | GitHub 서버 IP 봇차단 | 로그인 쿠키를 Secret으로 주입 |
| 2 | "Requested format is not available" | 자막만 필요한데 화질 정보 요구 | `ignore_no_formats_error: True` |
| 3 | 실행이 6시간 만에 강제취소, 결과 유실 | 시간 제한 장치 부재 | 시간 예산 90분 + job timeout 150분 + socket timeout |
| 4 | "rate-limited for up to an hour" | 무지연 대량 요청(1,300건/30분) | 요청 간 1~2초 지연 + 회당 상한 하향 |
| 5 | 자동자막 영상 전멸 (수동자막만 성공) | 유튜브가 자동자막에 **PO 토큰** 요구 | bgutil PO 토큰 제공기 (docker+plugin) |
| 6 | 쿠키 넣어도 봇차단 재발 | **쿠키(세션) 무효화** — 수천 요청 후 차단 | 새 쿠키 교체(부계정) + 연쇄실패 조기중단 |
| 7 | `_seen.json`에 no_subs 수천 건 오기록 | 실패를 "자막 없음"으로 오판 | 건강 판정(formats 존재) 시에만 기록; 오염분 3회 복구 |
| 8 | 워크플로우 푸시 충돌 (rejected) | 수집 중 다른 커밋 발생 | push 전 rebase 재시도 3회 |
| 9 | 채널 핸들 404 다수 | 추정 핸들 오류 | 로그의 '접속 실패' 목록으로 검증, 오류는 주석 처리 |

**운영 규칙 요약**: <u>수집이 갑자기 0건이 되면 90%는 쿠키 문제</u> —
diagnose.yml 수동 실행 → "Sign in to confirm" 보이면 쿠키 교체.

---

## 5. 진단 도구 (diagnose.yml)

- Actions 탭 → "Subtitle Diagnose" → Run workflow (약 1분)
- 출력: `[원본진단]` 실제 에러 + 클라이언트별(web/tv/mweb/android...) 자동자막
  수·VTT 생성 여부
- 판독: `VTT생성 ≥ 1` = 정상 / `예외: Sign in...` = 쿠키 교체 필요 /
  `rate-limited` = 몇 시간 대기

---

## 6. 현재 상태 (2026-07-20 기준)

- **수집 누적: 38건** (키워드 34 + 채널 4) — 분류: AX 25 / DX 4 / AT 0 / 미분류 5
- 🔴 **수집 중단 상태**: 쿠키 무효화. **새(부계정) 쿠키 등록이 재개 조건**
- 채널 118개 중 **핸들 검증 필요 15개는 주석 처리**됨 (`config.py`에서
  `[핸들 검증 필요]` 검색) — NAVER, 카카오, KT, TSMC, Cerebras, AWS 등
- PO 토큰 해법은 장착됐으나 **쿠키가 죽어 있어 아직 실효성 미검증** —
  새 쿠키 등록 후 diagnose로 확인할 것
- 사례 추출은 1차 규칙 기반 — 인용 전 원문 확인 필요. LLM 2차 정제는
  API 키 등록 시 `extract_cases.extract_claims()` / `summarize.summarize_text()`
  교체로 업그레이드 가능

---

## 7. 새 저장소(youtube-scrap)에서 시작하는 법

새 세션(저장소: `Moomoonim/youtube-scrap`)에서 아래를 붙여넣기:

> 공개 저장소 https://github.com/Moomoonim/Moomoonim 의 파일 전체(.github/workflows
> 포함, .git 제외)를 이 저장소 main 브랜치로 복사해서 커밋·푸시해줘. 유튜브에서
> AX(AI 전환) 스크립트를 하루 5회 자동 수집·분류하는 시스템이야. 자세한 구조와
> 주의사항은 docs/HANDOVER.md 를 먼저 읽어줘.

그다음: §3의 필수 설정 2가지(Actions 켜기 + 새 쿠키 Secret) → diagnose.yml 실행으로
검증 → daily-fetch.yml 수동 실행 1회 → 이후 자동.

이사 완료 후 원본(프로필 저장소)의 워크플로우를 삭제해 이중 수집을 방지할 것.

---

## 8. 연구 로드맵 (다음 단계)

1. **수집 재개** (새 쿠키) → 채널 백필 진행: 회당 150 × 하루 5회 = 최대 750건/일,
   2020년~ 전체(수만 건)는 수 주 소요
2. **핸들 검증**: 실행 로그 '접속 실패' 목록 기반으로 15개 채널 복원
3. **LLM 2차 처리**: 분류 정밀화 + 사례 구조화(전략/실행/성과) — 비용 수십 달러 수준
4. **사람 코딩 검증**: 표본 100~200건 → Cohen's κ 보고 (방법론 방어)
5. **K1 병합**: [월×산업×기술유형] 담론 지수 ↔ K1 기업 공개 자료 (산업코드·시점 키)
   → AX 담론 급증 이후 비용 구조 변화 (이벤트 스터디/DiD), 'AI 워싱' 측정
6. 연구 기록은 `docs/DIARY.md` (DSL protocol) 계속 갱신

---

## 부록: 파일별 한 줄 설명

| 파일 | 역할 |
|---|---|
| `config.py` | 모든 설정 (키워드·채널 118개·상한·지연·시간예산) |
| `fetch_transcripts.py` | 키워드 검색 수집 + 공용 유틸(쿠키/파서/저장) |
| `fetch_channels.py` | 채널 백필 수집 (최신순, 2020 하한, 셔플, 조기중단 가드) |
| `classify.py` | DX/AX/AT 사전 분류 → classified.csv, monthly_summary.csv |
| `summarize.py` | 발췌 요약 → summaries.csv, SUMMARY_BY_*.md |
| `extract_cases.py` | 사례 주장 추출(행동+수치/AI 문맥, 타기업 언급 감지) → cases.csv |
| `.github/workflows/daily-fetch.yml` | 하루 5회 자동 파이프라인 |
| `.github/workflows/diagnose.yml` | 자막 취득 가능 여부 1분 진단 |
