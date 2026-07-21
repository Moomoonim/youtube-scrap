"""
수집 설정 파일.

여기 값만 바꾸면 검색어/언어/개수 등을 손쉽게 조정할 수 있어요.
(코드를 몰라도 따옴표 안의 글자만 고치면 됩니다.)
"""

# 검색할 키워드 목록 (AX = AI 전환 / AI Transformation)
# 한국어 + 영어 키워드를 함께 넣어두었습니다.
KEYWORDS = [
    # 한국어
    "AX AI 전환",
    "AI 전환 사례",
    "기업 AI 도입",
    "AX 인공지능 전환",
    # 영어
    "AI Transformation",
    "Enterprise AI adoption",
    "AX AI transformation business",
]

# 자막을 받아올 언어 (우선순위 순서). ko=한국어, en=영어
LANGUAGES = ["ko", "en"]

# 키워드 하나당 검색해볼 영상 개수
RESULTS_PER_KEYWORD = 8

# 실행 1회당 저장할 최대 영상 개수 (중복 제거 후 기준)
# 하루 5회 실행되므로 하루 최대 = 이 값 × 5
MAX_VIDEOS_PER_DAY = 30

# 결과를 저장할 폴더 이름
OUTPUT_DIR = "transcripts"


# ──────────────────────────────────────────────
# 공식 채널 수집 설정 (키워드 검색과 별도로 동작)
# ──────────────────────────────────────────────

# 이 날짜 이후 업로드된 영상만 수집 (YYYYMMDD)
CHANNEL_SINCE = "20200101"

# 실행 1회당 채널 하나에서 새로 수집할 최대 영상 수
MAX_PER_CHANNEL_PER_RUN = 8

# 실행 1회당 전체 채널에서 수집할 총 상한 (실행 시간 관리용)
# 하루 5회 실행 → 하루 최대 = 이 값 × 5
MAX_CHANNEL_TOTAL_PER_RUN = 150

# 실행 1회당 채널 하나에서 시도(성공+실패 포함)할 최대 영상 수
# — 자막 없는 영상이 많은 채널이 실행 시간을 독식하는 것을 방지
MAX_ATTEMPTS_PER_CHANNEL_PER_RUN = 15

# 채널 수집 단계의 시간 예산(분) — 초과하면 하던 것까지 저장하고 정상 종료
# (GitHub Actions 6시간 강제 취소로 결과를 통째로 잃는 사고 방지)
CHANNEL_TIME_BUDGET_MIN = 90

# 네트워크 응답 대기 한도(초) — 개별 요청이 무한정 매달리는 것 방지
SOCKET_TIMEOUT_SEC = 20

# 유튜브 세션 속도 제한(rate limit) 방지: 요청/자막 다운로드 사이 지연(초)
SLEEP_BETWEEN_REQUESTS_SEC = 1
SLEEP_BETWEEN_SUBTITLES_SEC = 2

# 제목 필터 (None이면 전체 수집, 예: ["AI", "GPT"]로 지정 시 해당 단어 포함 영상만)
CHANNEL_TITLE_KEYWORDS = None

# 수집할 공식 채널 목록: 이름 → 유튜브 핸들
# ※ '추정'이 붙은 핸들은 알려진 공식 핸들 기준 추정치 — 실행 로그의
#   '채널 접속 실패' 목록을 보고 잘못된 것은 수정/삭제하면 된다.
CHANNELS = {
    # 1. 파운데이션 모델 랩
    "OpenAI": "@OpenAI",
    "Anthropic": "@anthropic-ai",
    "Google DeepMind": "@googledeepmind",
    "xAI": "@xAI",
    "Cohere": "@CohereAI",                     # 수정(1차 @Cohere 404)
    # [핸들 검증 필요 — 404로 수집 제외] "Mistral AI": "@MistralAI",                # 소규모/추정
    # 2. 하이퍼스케일러 · 클라우드
    "Microsoft": "@Microsoft",
    "Microsoft Developer": "@MicrosoftDeveloper",
    "Microsoft Azure": "@MicrosoftAzure",
    "Google": "@Google",
    "Google Developers": "@GoogleDevelopers",
    "Google Cloud Tech": "@googlecloudtech",
    # [핸들 검증 필요 — 404로 수집 제외] "AWS": "@AmazonWebServices",
    "AWS Developers": "@awsdevelopers",
    "Meta": "@Meta",
    "Meta Developers": "@MetaDevelopers",
    "Apple": "@Apple",
    "Apple Developer": "@AppleDeveloper",
    "IBM Technology": "@IBMTechnology",
    "Oracle": "@Oracle",
    "Salesforce": "@Salesforce",
    "SAP": "@SAP",
    # 3. AI 반도체 · 하드웨어
    "NVIDIA": "@NVIDIA",
    "NVIDIA Developer": "@NVIDIADeveloper",
    "AMD": "@amd",
    "Intel": "@intel",
    "Arm": "@Arm",                             # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "TSMC": "@tsmc",                           # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "Samsung Semiconductor": "@SamsungSemiconductor",  # 추정
    "SK hynix": "@SKhynix",                    # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "Cerebras": "@CerebrasSystems",            # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "Tenstorrent": "@Tenstorrent",
    # [핸들 검증 필요 — 404로 수집 제외] "Groq": "@GroqInc",                        # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "SambaNova": "@SambaNovaAI",               # 추정
    # 4. 인프라 · MLOps
    "Databricks": "@Databricks",
    "Snowflake": "@SnowflakeInc",              # 추정
    "Hugging Face": "@HuggingFace",
    "Weights & Biases": "@WeightsBiases",
    # 5. 데이터 · 벡터 DB
    "Weaviate": "@Weaviate",                   # 추정
    "Pinecone": "@pinecone-io",                # 추정
    "Qdrant": "@qdrant",                       # 추정
    "Scale AI": "@ScaleAI",                    # 추정
    # 6. 생성형 미디어 (Midjourney: 공식 채널 없음 → 제외)
    "Runway": "@RunwayML",
    "Stability AI": "@StabilityAI",            # 추정
    "Synthesia": "@Synthesia",                 # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "HeyGen": "@HeyGen",                       # 추정
    "Luma AI": "@LumaLabsAI",                  # 추정
    "ElevenLabs": "@ElevenLabs",               # 수정(1차 404)
    "Suno": "@SunoMusic",                      # 추정
    # 7. AI 코딩 · 개발자 도구 (Cursor: 공식 채널 콘텐츠 미미 → 제외)
    "GitHub": "@GitHub",
    "Replit": "@Replit",
    # 8. AI 검색 · 어시스턴트
    "Perplexity": "@PerplexityAI",             # 추정
    # 9. 자율주행 · 로보틱스
    "Boston Dynamics": "@BostonDynamics",
    "Tesla": "@Tesla",
    "Waymo": "@Waymo",
    "Figure": "@figureai",                     # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "1X": "@1XTechnologies",                   # 추정
    "Wayve": "@wayve",                         # 추정
    "Aurora": "@AuroraInnovation",             # 추정
    # 10. 버티컬 · 방산
    "Palantir": "@palantirtech",               # 추정
    "Anduril": "@anduriltech",                 # 수정(1차 404)
    # 11. 중국 (DeepSeek: 공식 채널 없음 → 제외)
    "Alibaba Cloud": "@AlibabaCloud",
    "Huawei": "@Huawei",
    "Tencent": "@Tencent",                     # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "Baidu": "@Baidu",                         # 추정
    # 12. 한국
    # [핸들 검증 필요 — 404로 수집 제외] "NAVER": "@naver",                         # 추정
    "NAVER Cloud": "@navercloudplatform",
    # [핸들 검증 필요 — 404로 수집 제외] "NAVER D2": "@naverd2",                    # 추정
    "LG AI Research": "@LGAIResearch",         # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "카카오": "@kakao",                         # 추정
    "kakao tech": "@kakaotech",                # 추정
    "SK텔레콤": "@SKtelecom",                   # 추정
    # [핸들 검증 필요 — 404로 수집 제외] "KT": "@KT",                               # 추정
    "Upstage": "@upstageai",                   # 추정

    # ══════════════════════════════════════════════════
    # HBR·NVIDIA GTC 사례 문서에서 추출한 AX 도입 기업들
    # (핸들은 추정 — 실행 로그의 '접속 실패' 목록으로 검증/수정)
    # ══════════════════════════════════════════════════

    # 13. 소비재 · 리테일 · 마케팅
    "L'Oréal": "@loreal",                      # 추정
    "IKEA": "@IKEA",                           # 추정
    "Amazon": "@amazon",                       # 추정
    "Nike": "@nike",                           # 추정
    "Unilever": "@unilever",                   # 추정
    "Reckitt": "@Reckitt",                     # 추정
    "Adobe": "@Adobe",                         # 추정
    "Netflix": "@Netflix",                     # 추정
    "Chegg": "@chegg",                         # 추정

    # 14. 금융 · 컨설팅 · 전문 서비스
    "McKinsey & Company": "@McKinsey",         # 추정
    "Boston Consulting Group": "@bcg",         # 확인(수집분에 등장)
    "Deloitte": "@Deloitte",                   # 추정
    "Accenture": "@Accenture",                 # 추정
    "Genpact": "@Genpact",                     # 추정
    "Intuit": "@Intuit",                       # 추정
    "LinkedIn": "@LinkedIn",                   # 추정
    "IQVIA": "@IQVIA",                         # 추정

    # 15. 산업 · 자동차 · 로보틱스
    "Caterpillar": "@Caterpillar",             # 추정
    "Mercedes-Benz": "@MercedesBenz",          # 추정
    "BMW": "@BMW",                             # 추정
    "General Motors": "@GM",                   # 추정
    "Volvo Cars": "@VolvoCars",                # 추정
    "Nissan": "@Nissan",                       # 추정
    "Siemens": "@Siemens",                     # 추정
    "Rockwell Automation": "@ROKAutomation",   # 추정
    "BYD": "@BYD",                             # 추정

    # 16. 헬스케어 · 제약 · 바이오
    "Eli Lilly": "@lilly",                     # 추정
    "Novo Nordisk": "@novonordisk",            # 추정
    "Johnson & Johnson": "@johnsonandjohnson", # 추정
    "Philips": "@philips",                     # 추정
    "GE HealthCare": "@gehealthcare",          # 추정
    "Mayo Clinic": "@MayoClinic",              # 추정
    "ZEISS": "@ZEISS",                         # 추정
    "Chan Zuckerberg Initiative": "@ChanZuckerbergInitiative",  # 추정

    # 17. 엔터프라이즈 SW · AI 인프라
    "Nokia": "@nokia",                         # 추정
    "ServiceNow": "@servicenow",               # 추정
    "Schneider Electric": "@SchneiderElectric",# 추정
    "Vertiv": "@Vertiv",                       # 추정
    "Cadence": "@cadence",                     # 추정
    "Together AI": "@togetherai",              # 추정
    "Intercom": "@intercom",                   # 추정
    "Zapier": "@zapier",                       # 추정
    "Slack": "@Slack",                         # 추정
    "Cursor": "@cursor",                       # 추정(콘텐츠 적음)

    # 18. 텔레콤
    "T-Mobile": "@TMobile",                    # 추정
    "Orange": "@Orange",                       # 추정
    "Telefónica": "@telefonica",               # 추정
    "Swisscom": "@Swisscom",                   # 추정
    "Telenor": "@TelenorGroup",                # 추정
    "SoftBank": "@softbank",                   # 추정
    "TCS": "@TCSGlobal",                       # [핸들 수정 2026-07-21] @TCS는 스위스 자동차클럽(Touring Club Schweiz)으로 오수집됨 — 확인된 정식 핸들로 교체
    "Infosys": "@Infosys",                     # 추정
    "Capgemini": "@Capgemini",                 # 추정
    "NTT DATA": "@NTTDATA",                    # 추정

    # 19. 미디어 · 소셜 · 자율주행 · 기타
    "Snap": "@Snap",                           # 추정
    "DuckDuckGo": "@DuckDuckGo",               # 추정
    "iRobot": "@iRobot",                       # 추정
    "Cruise": "@Cruise",                       # 추정
    "Zoox": "@ZooxYouTube",                    # [핸들 수정 2026-07-21] @zoox는 동명의 게임 유튜버로 오수집됨 — 확인된 로보택시 채널로 교체
}
