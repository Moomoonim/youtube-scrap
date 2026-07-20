# Moomoonim — AX(AI 전환) 유튜브 스크립트 수집기

유튜브에서 **AX(AI 전환 / AI Transformation)** 관련 영상의 자막(스크립트)을
**매일 자동으로** 가져와 저장하는 도구입니다. 한국어·영어 영상을 모두 수집합니다.

## 어떻게 동작하나요?

두 가지 방식으로 수집합니다 (모두 `yt-dlp` 사용, API 키 불필요):

**① 키워드 검색** (`fetch_transcripts.py`)
1. `config.py` 의 AX 관련 키워드로 유튜브를 검색합니다
2. 각 영상의 자막을 받아 날짜별 폴더에 저장 → `transcripts/2026-07-18/...`

**② 공식 채널 수집** (`fetch_channels.py`)
1. `config.py` 의 `CHANNELS` 목록(OpenAI, Anthropic, NVIDIA, 네이버클라우드 등
   약 70개 공식 채널)의 영상을 최신순으로 수집합니다
2. **2020년 1월 이후** 영상까지 거슬러 올라가며, 실행 1회당 최대 250개씩
   점진적으로 백필합니다 (수만 개 규모라 몇 주에 걸쳐 완성됨)
3. 채널별 폴더에 저장 → `transcripts/channels/OpenAI/...`

공통: 이미 받은 영상은 `transcripts/_seen.json` 으로 건너뛰고(중복 방지),
자막이 없는 영상도 기록해 다시 시도하지 않습니다.

**③ 자동 분류** (`classify.py`)
- 매 수집 후 전체 스크립트를 **DX / AX / AT** 축으로 사전(dictionary) 기반
  분류합니다 — 기준은 `docs/CODEBOOK.md`
- 결과: `analysis/classified.csv` (영상별 점수), `analysis/monthly_summary.csv`
  (월×라벨 시계열 집계 — K1 기업 공개 자료와의 병합용 기초 지수)

**④ 메타데이터별 요약 정리** (`summarize.py`)
- 영상별 **발췌 요약**(문장 경계 인식, 최대 약 70단어)을 만들고, 채널/출처별·
  월×분류라벨별로 정리합니다. (LLM 비용 없이 대량 처리하기 위한 방식이며,
  추상 요약이 필요해지면 `summarize_text()` 함수만 교체하면 됩니다.)
- 결과: `analysis/summaries.csv` (기계 판독용), `analysis/SUMMARY_BY_CHANNEL.md`,
  `analysis/SUMMARY_BY_MONTH.md` (사람이 읽는 정리본)

## 자동 실행 (하루 5회)

`.github/workflows/daily-fetch.yml` 이 **매일 한국시간 06시 / 10시 / 14시 /
18시 / 22시**에 자동으로 실행되어 새 스크립트를 수집하고 저장소에 커밋합니다.
이미 받은 영상은 건너뛰므로 매 회차 새 영상만 추가됩니다.
컴퓨터를 켜둘 필요가 없습니다.

> 유튜브 봇 차단 우회를 위해 `YOUTUBE_COOKIES` 비밀값(Secret)에 로그인
> 쿠키가 등록되어 있어야 합니다. 쿠키가 만료되어 수집이 0개가 되면
> cookies.txt를 다시 내보내 Secret 값만 교체하면 됩니다.

> GitHub 저장소의 **Actions** 탭에서 `Daily AX Transcript Fetch` 워크플로우를
> 선택하고 **Run workflow** 버튼을 누르면 지금 바로 한 번 실행해 볼 수도 있습니다.

## 직접 실행해 보기 (선택)

```bash
pip install -r requirements.txt
python fetch_transcripts.py
```

실행하면 `transcripts/오늘날짜/` 폴더에 영상별 `.md` 파일과
요약 목록(`README.md`)이 생깁니다.

## 설정 바꾸기

`config.py` 파일의 값만 고치면 됩니다 (코드를 몰라도 따옴표 안 글자만 수정):

| 설정 | 설명 |
|------|------|
| `KEYWORDS` | 검색할 키워드 목록 |
| `LANGUAGES` | 자막 언어 (`ko`=한국어, `en`=영어) |
| `RESULTS_PER_KEYWORD` | 키워드당 검색할 영상 수 |
| `MAX_VIDEOS_PER_DAY` | 하루 최대 저장 개수 |

## 폴더 구조

```
transcripts/
├── _seen.json              # 이미 받은 영상 기록 (중복 방지)
└── 2026-06-28/
    ├── README.md           # 그날 수집한 영상 목록
    ├── 영상제목__abc123.md  # 영상별 스크립트
    └── ...
```
