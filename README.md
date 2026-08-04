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

**⑤ Verhoef 3단계 사례 태깅** (`classify_verhoef.py`, 수동 실행)
- Verhoef et al.(2021)의 **digitization(전산화) → digitalization(디지털화) →
  digital transformation(디지털 전환)** 3단계로 코퍼스 전량을 태깅하고,
  단계별 근거 문장(사례 주장)을 회사별로 모읍니다. Table 1의 네 전략 요소
  (디지털 자원·조직구조·성장전략·지표)도 보조 축으로 함께 코딩합니다.
- 결과: `analysis/verhoef_stages.csv` (기계 판독용), `docs/VERHOEF_CASES.md`
  (단계별·회사별 사례집)

**⑥ 사례 상세 카드** (`build_verhoef_dossier.py`, 수동 실행)
- ⑤에서 배정된 사례를 하나씩 펼칩니다 — **판정 근거가 된 실제 어휘와 횟수**, "무엇을 했다"는
  주장 문장(최대 5개), 성과 수치, 언급된 다른 기업, Table 1 좌표, 원본 링크.
  한 단어가 점수의 70% 이상을 차지하면 **⚠️ 단일 마커 지배** 경고가 붙습니다.
- 결과: `docs/VERHOEF_DOSSIER_S3.md` · `S2` · `S1` · `S4c` (총 1,142장)
- 이와 별도로 `docs/VERHOEF_S3_PROFILES.md` 는 S3 상위 사례를 **원문으로 직접 검증한**
  서술형 프로파일입니다(사람이 작성, 오탐 분석 포함).

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

## 로컬에서 저속 수집 (IP 차단 완화)

클라우드(GitHub Actions)는 데이터센터 IP라 유튜브 봇 차단이 잦습니다.
집(가정용) IP에서 아래 스크립트를 **느린 간격**으로 돌리면 차단이 훨씬 덜합니다.

```bash
pip install -r requirements.txt          # 최초 1회 (yt-dlp 설치)

# 채널 백필을 20초 간격으로 최대 200개
python fetch_local.py --pace 20 --limit 200

# 특정 채널만, 채널당 30개
python fetch_local.py --channel "삼성" --per-channel 30 --pace 20

# 키워드 검색분
python fetch_local.py --source keyword --pace 20 --limit 40

# 쿠키 파일 지정(자동 자막 차단 우회)
python fetch_local.py --cookies ./cookies.txt --pace 20
```

- 이미 받은 영상은 `_seen.json` 으로 **자동 건너뜀** → 언제 멈췄다 다시 켜도 이어서 받습니다.
- **Ctrl+C** 로 중단해도 그때까지 받은 것은 저장됩니다.
- 차단이 감지되면 안전하게 멈춥니다. **30분쯤 뒤 같은 명령**을 다시 실행하면 이어서 받습니다.
- 참고 처리량: 20초 간격 = 시간당 약 180개, 하루 이론상 ~4,000개(실제 ~2,500~3,500개). 단 백필은 유한하니 몇 시간씩 나눠 돌리는 것을 권장.
- 수집 후 분석 갱신: `python classify.py && python summarize.py`
