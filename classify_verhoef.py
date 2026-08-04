"""
Verhoef 3단계(digitization / digitalization / digital transformation) 사례 태거.

이론틀:
  Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q.,
  Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary
  reflection and research agenda. Journal of Business Research, 122, 889-901.

무엇을 하나:
  수집된 유튜브 스크립트 전량을 훑어 각 영상이 말하는 사례가 Verhoef의
  3단계 중 **어디에 해당하는 담론인지**를 규칙 기반으로 태깅하고, 단계별
  근거 문장(사례 주장)을 뽑아낸다. 여기에 Table 1의 네 가지 전략 요소
  (디지털 자원 · 조직구조 · 성장전략 · 지표)를 보조 축으로 함께 코딩한다.

  단계 정의(논문 그대로):
    S1 digitization   아날로그 정보의 디지털 변환. 가치창출 활동 자체는 불변.
                      목표는 비용 절감. (종이→디지털, 스캔·OCR·전산화)
    S2 digitalization 디지털 기술로 **기존 프로세스**를 변경·최적화.
                      비용 절감 + 고객경험 개선. (자동화·워크플로·ERP/CRM·챗봇)
    S3 digital        전사적 차원의 **새로운 비즈니스 모델**과 가치창출·전유
       transformation 로직 도입. 사업 논리 자체의 재구성. (플랫폼·생태계·
                      수익모델 전환·사업구조 재편)

  + S4c 는 논문에 없는 **AX 위치 판별용 보조 축**이다. 의사결정의 알고리즘화·
    자율 에이전트·AI 인력화처럼 "AX가 DX의 연장인가, 질적으로 다른 전환인가"를
    논증할 때 쓸 후보 사례를 따로 표시한다(본 저장소의 AT 축과 연결).

산출:
  analysis/verhoef_stages.csv  — 영상별 단계 점수·라벨·근거(기계 판독용)
  docs/VERHOEF_CASES.md        — 단계별·회사별 사례집(사람이 읽는 정리본)

직접 실행: python classify_verhoef.py

한계(정직한 고지): 규칙 기반이라 문맥·반어·부정을 완벽히 잡지 못하고,
발화 주체(벤더 홍보 vs 도입 기업 증언)를 자동으로는 vendor/media까지만
구분한다. 인용 전 원문 스크립트 확인이 필수다.
"""

import collections
import csv
import glob
import os
import re

import config
from classify import parse_transcript, doc_month, score_text, AT_PATTERNS
from classify_v2 import classify_relevance, classify_stance
from extract_cases import ACTION_RE, METRIC_RE, AI_RE, NOISE_RE, split_sentences
from build_catalog import CH2LAYER, CH2HQ


def rx(*pats):
    """여러 패턴을 **하나의 합집합 정규식**으로 컴파일한다.

    코퍼스가 1만 건 규모라 패턴을 하나씩 돌리면(사전당 수십 개 × 문장 수백 개)
    실행 시간이 폭발한다. 합집합 1회 스캔으로 같은 결과를 얻는다.
    (같은 위치에서 여러 대안이 겹치면 1회로 세므로 과대집계도 줄어든다.)
    """
    return re.compile("|".join(f"(?:{p})" for p in pats), re.IGNORECASE)


# ══════════════════════════════════════════════════════════════
# 1. 단계 사전 — Verhoef Table 1의 단계 정의를 담론 마커로 번역
# ══════════════════════════════════════════════════════════════

# ── S1 digitization: 아날로그 → 디지털 (가치창출 활동 불변, 비용 절감) ──
S1_DIGITIZATION = rx(
    r"전산화", r"디지털화\s*(작업|사업)?", r"전자\s*문서(화)?", r"문서\s*(전자화|디지털화|디지타이)",
    r"종이\s*(문서|서류|장부|기반)", r"페이퍼\s*리스", r"paperless",
    r"수기\s*(작성|입력|기록|관리)", r"손으로\s*(적|입력)", r"엑셀(로)?\s*(정리|관리|입력)",
    # '스캔' 단독은 의료 영상(초음파·CT) 담론에서 대량 오탐된다 — 문서 맥락일 때만 센다.
    r"(문서|서류|자료|장부|도면|영수증)(를|을)?\s*스캔",
    r"스캔(해서|하여|한)\s*(저장|보관|디지털|업로드|보관)",
    r"\bOCR\b", r"광학\s*문자",
    r"digiti[sz](e|ed|ing|ation)", r"scan(ned|ning)?\s+(document|paper|record)",
    r"paper[-\s]?based", r"data\s+entry", r"수작업\s*(입력|처리)",
    r"아날로그\s*(정보|자료|데이터|방식)", r"analog(ue)?\s+(data|information|process)",
    r"디지털\s*(아카이브|자료화)", r"데이터베이스(로)?\s*(구축|이관|옮)",
    r"자료(를)?\s*디지털(로)?", r"convert.{0,12}(to\s+digital|into\s+digital)",
    r"디지털\s*형태로\s*(바꾸|전환|변환)", r"전자\s*결재",
)

# ── S2 digitalization: 기존 프로세스의 변경·최적화 (비용 + 고객경험) ──
S2_DIGITALIZATION = rx(
    r"프로세스\s*(자동화|최적화|개선|효율화|혁신|재설계)", r"process\s+(automation|optimi[sz]ation|improvement|redesign)",
    r"업무\s*(자동화|효율화|개선|간소화|디지털화)", r"work(flow)?\s+automation",
    r"워크플로\w*\s*(자동화|개선|최적화|재설계)?", r"streamlin",
    r"\bRPA\b", r"로봇\s*프로세스", r"업무\s*프로세스",
    r"\bERP\b", r"\bCRM\b", r"\bSCM\b", r"\bMES\b", r"그룹웨어",
    r"레거시\s*(시스템|전환|현대화)", r"legacy\s+(system|modernization)", r"시스템\s*(통합|현대화|고도화)",
    r"클라우드\s*(전환|이전|마이그레이션|도입)", r"cloud\s+(migration|adoption)",
    r"고객\s*경험\s*(개선|향상|혁신)?", r"customer\s+experience", r"\bCX\b",
    r"고객\s*(응대|상담|서비스)\s*(자동화|개선)?", r"contact\s+center|콜센터|상담(원|사)",
    r"챗봇|chatbot", r"셀프\s*서비스|self[-\s]?service",
    r"옴니\s*채널|omni[-\s]?channel|온라인\s*채널|모바일\s*앱\s*(출시|도입)",
    r"리드\s*타임\s*(단축|절감)", r"lead\s+time", r"공정\s*(자동화|최적화)",
    r"재고\s*(최적화|관리\s*자동화)", r"수요\s*예측", r"demand\s+forecast",
    r"예지\s*정비|predictive\s+maintenance", r"품질\s*검사\s*자동화|visual\s+inspection",
    r"코파일럿\s*(도입|배포|적용)|copilot\s+(rollout|deployment|for\s+employees)",
    r"사내\s*(툴|시스템|도구)\s*(도입|배포)", r"생산성\s*(향상|개선|도구)",
    r"back[-\s]?office\s+automation|백오피스",
    r"기존\s*(업무|프로세스|시스템)(를|을)?\s*(바꾸|개선|자동화|최적화)",
)

# ── S3 digital transformation: 전사적 BM·가치창출/전유 로직 재구성 ──
# (일반 명사 '플랫폼/생태계'는 벤더 기술 담론에서 남발되므로 사업 맥락 한정)
S3_TRANSFORMATION = rx(
    r"비즈니스\s*모델\s*(혁신|전환|변화|재편|재설계|구축|바꾸|자체)?", r"business\s+model(\s+(innovation|change|shift|transformation))?",
    r"사업\s*(모델|구조|포트폴리오)\s*(전환|재편|개편|바꾸|다각화)", r"수익\s*(모델|구조)\s*(전환|변화|재편|바꾸)?",
    r"신규\s*(사업|수익원|매출원)", r"new\s+(business|revenue)\s+(model|stream|source)",
    r"전사(적)?\s*(전환|혁신|재편|차원)", r"company[-\s]?wide|enterprise[-\s]?wide\s+transformation",
    r"플랫폼\s*(비즈니스|사업|기업|모델|전략|경제|전환)", r"platform\s+(business|company|model|strategy|economy|play)",
    # 'marketplace' 단독은 AWS/Azure 마켓플레이스 조달 이야기에서 남발되므로
    # (BM 전환이 아니다) 사업 맥락이 붙을 때만 센다.
    r"양면\s*시장|two[-\s]?sided\s+market",
    r"마켓\s*플레이스\s*(비즈니스|사업|모델|전략|경제)",
    r"marketplace\s+(business|model|strategy|economy|play)",
    r"네트워크\s*효과|network\s+effect", r"생태계\s*(구축|조성|전략|참여자)|business\s+ecosystem",
    r"구독\s*(모델|경제|전환)|subscription\s+(model|business)",
    r"서비스화|servitization|as[-\s]?a[-\s]?service\s+(model|business)|\bXaaS\b",
    # '가치 사슬/창출'은 IR·컨설팅 화법에서 상투어라, **바뀐다는 서술이 붙을 때만** 센다
    r"가치\s*(사슬|창출|제안)(을|를|이|가)?\s*(재편|재설계|재정의|바꾸|변화|전환|혁신)",
    r"value\s+(chain|creation|proposition)\s+(redesign|reshap|shift|change|transformation)",
    r"value\s+(capture|appropriation)", r"가치\s*전유",
    r"디지털\s*(네이티브|퍼스트)\s*(기업|조직|전환)?|digital[-\s]?(native|first)\s+(company|organization)",
    r"업(의)?\s*본질|사업의\s*정의(를)?\s*(바꾸|다시)", r"redefin(e|ing)\s+(the\s+)?(business|industry|company)",
    r"D2C|direct[-\s]?to[-\s]?consumer", r"공동\s*창출|co[-\s]?creation",
    r"파괴적\s*혁신|disrupt(ion|ive|ing|s|ed)?\s+(the\s+)?(industry|market|business|value\s+chain)",
    r"피벗|pivot(ed|ing)?\s+(the\s+)?(company|business)",
    r"AI\s*(퍼스트|first)\s*(회사|기업|company|organization)",
)

# ── S4c(보조): AX가 DX의 연장인가 별개인가를 논증할 후보 신호 ──
S4_ALGORITHMIC = rx(
    *[p for p in [
        r"의사\s*결정(을|의)?\s*(자동화|알고리즘|위임|맡기)",
        r"automated?\s+decision[-\s]?making", r"알고리즘(이|에\s*의해)\s*(결정|판단|배분|운영)",
        r"자율\s*(에이전트|운영|기업)|autonomous\s+(agent|operation|enterprise)",
        r"agentic\s+(enterprise|organization|workforce|company)",
        r"AI\s*직원|AI\s+(employee|coworker|worker)|디지털\s*워커|digital\s+worker",
        r"에이전트(가|를)?\s*(업무|일)(를)?\s*(수행|처리|대신)",
        r"self[-\s]?driving\s+(company|business|enterprise|operation)",
        r"인력(을)?\s*(대체|재배치|감축)|headcount|\bFTE\b",
        # ⚠️ 'AI 전환/AX/AI transformation' 같은 **명칭**은 넣지 않는다.
        #    구성개념(결정권의 알고리즘 이전)이 아니라 호칭일 뿐이라, 넣으면
        #    이 축이 "AX라는 단어를 썼는가"로 변질된다.
    ]],
    *AT_PATTERNS,
)

STAGES = [
    ("s1_digitization", S1_DIGITIZATION),
    ("s2_digitalization", S2_DIGITALIZATION),
    ("s3_transformation", S3_TRANSFORMATION),
    ("s4c_algorithmic", S4_ALGORITHMIC),
]

STAGE_LABEL = {
    "s1_digitization": "S1 digitization(전산화)",
    "s2_digitalization": "S2 digitalization(디지털화)",
    "s3_transformation": "S3 digital transformation(디지털 전환)",
    "s4c_algorithmic": "S4c 알고리즘 전환 후보(AX 위치 논쟁용)",
}

# 단계 인정 최소 등장 횟수 (classify.py MIN_HITS=2 관행과 동일)
MIN_STAGE_HITS = 2


# ══════════════════════════════════════════════════════════════
# 2. Table 1 — 단계별 전략 요소 네 가지를 보조 축으로 코딩
# ══════════════════════════════════════════════════════════════
ELEMENTS = {
    # (1) 디지털 자원: 디지털 자산 → 민첩성·네트워킹 → 빅데이터 분석 역량
    "res_asset": rx(r"디지털\s*(자산|인프라|기반)", r"digital\s+(asset|infrastructure)",
                    r"데이터\s*(자산|축적|보유)", r"proprietary\s+data|자체\s*데이터"),
    "res_agility": rx(r"민첩(성|하게)|agility|agile|애자일", r"빠르게\s*(실험|반복|출시)",
                      r"실험\s*(문화|속도)|rapid\s+(experimentation|iteration)", r"스쿼드|스프린트"),
    "res_networking": rx(r"파트너(십|사)|partnership|얼라이언스|alliance",
                         r"생태계\s*(파트너|참여)|ecosystem\s+partner", r"공동\s*(개발|연구|창출)|co[-\s]?(develop|creat)",
                         r"\bAPI\b\s*(개방|공개)|open\s+API|외부\s*(개발자|연동)"),
    "res_bigdata": rx(r"빅\s*데이터|big\s+data", r"데이터\s*(분석|사이언스|레이크|플랫폼|웨어하우스)",
                      r"data\s+(analytics|science|lake|platform|warehouse)", r"분석\s*역량|analytics\s+capabilit"),
    # (2) 조직구조: 표준 위계 → 분리된 애자일 유닛 → 내재화된 유연 조직
    "org_hierarchy": rx(r"위계|hierarch", r"기존\s*조직(을|은|에서)?\s*(유지|그대로)",
                        r"부서\s*(별|간)\s*(칸막이|사일로)|사일로|silo", r"top[-\s]?down|하향식"),
    "org_separate_unit": rx(r"(전담|별도|신설)\s*(조직|팀|부서|센터|본부)", r"AX\s*(센터|추진단|조직|본부)",
                            r"디지털\s*(추진|혁신)\s*(단|팀|실|본부)", r"\bCoE\b|센터\s*오브\s*엑설런스",
                            r"\bCDO\b|\bCAIO\b|최고\s*(디지털|AI)\s*책임자", r"(separate|dedicated)\s+(unit|team|organization)",
                            r"transformation\s+office|innovation\s+lab|사내\s*벤처"),
    "org_embedded": rx(r"전사(적)?(으로)?\s*(확산|내재화|적용|배포)", r"내재화|in[-\s]?hous",
                       r"현업\s*(부서|팀)(이|에)?\s*(직접|주도)", r"embed(ded|ding)?\s+(analytics|AI|IT)",
                       r"cross[-\s]?functional|교차\s*기능|융합\s*조직",
                       r"모든\s*(직원|임직원)(이|에게)", r"every\s+employee"),
    # (3) 성장전략: 플랫폼 기반 침투 · 공동창출 플랫폼 · 플랫폼 다각화
    "growth_penetration": rx(r"시장\s*(점유|침투|확대)", r"market\s+(penetration|share)",
                             r"기존\s*고객(에게|의)?\s*(더|추가|확대)", r"cross[-\s]?sell|up[-\s]?sell|교차\s*판매"),
    "growth_cocreation": rx(r"공동\s*창출|co[-\s]?creation", r"사용자(가|의)?\s*(참여|기여|생성)",
                            r"user[-\s]?generated|커뮤니티\s*(기여|참여)", r"개발자\s*생태계|developer\s+ecosystem",
                            r"오픈\s*소스\s*(생태계|커뮤니티|전략)"),
    "growth_diversification": rx(r"다각화|diversif", r"신규\s*(시장|영역|카테고리)\s*(진출|확장)",
                                 r"new\s+market\s+entry", r"인접\s*(사업|영역)|adjacen(t|cy)",
                                 r"\bM&A\b|인수\s*합병|인수했"),
    # (4) 지표: 전통 KPI(ROI·ROA) → 디지털 KPI(활성 사용자·digital share·감성)
    "kpi_traditional": rx(r"\bROI\b|\bROA\b|\bROE\b|투자\s*수익(률)?", r"영업\s*이익|순이익|매출\s*(총)?이익",
                          r"원가\s*(절감|구조)|비용\s*절감", r"profit\s+margin|EBITDA|payback"),
    "kpi_digital": rx(r"활성\s*(사용자|이용자)|\bMAU\b|\bDAU\b|active\s+users?",
                      r"디지털\s*(매출|비중|채널)\s*(비중|비율)?|digital\s+(share|revenue|sales)",
                      r"체류\s*시간|engagement|이탈률|churn|리텐션|retention",
                      r"\bNPS\b|고객\s*만족도|customer\s+satisfaction|감성\s*분석|sentiment",
                      r"전환율|conversion\s+rate|채택률|adoption\s+rate|사용률"),
}


def count(pattern, text):
    return sum(1 for _ in pattern.finditer(text))


def any_hit(pattern, text):
    return 1 if pattern.search(text) else 0


def best_evidence(sentences, pattern, max_len=300):
    """단계 마커가 든 문장 중 '사례 주장'으로 가장 좋은 한 문장을 고른다.

    extract_cases.py와 같은 기준: **행동(무엇을 했다)** 신호가 없는 문장은
    사례가 아니라 일반론이므로 버린다(수치만 든 잡문 배제).
    """
    best, best_score = "", 0
    for sent in sentences:
        if not pattern.search(sent):
            continue
        if NOISE_RE.search(sent):
            continue
        if not ACTION_RE.search(sent):
            continue                      # 행동 없는 일반론은 사례 근거로 보지 않는다
        score = 3
        if METRIC_RE.search(sent):
            score += 3
        if AI_RE.search(sent):
            score += 1
        if score > best_score:
            best, best_score = sent, score
    if len(best) > max_len:
        best = best[:max_len] + "…"
    return best, best_score


def assign_stage(scores):
    """가장 높은 단계부터 내려오며 최소 기준을 넘는 단계를 배정한다.

    Verhoef의 3단계는 누적·위계적이다(전환은 디지털화를 포함한다). 따라서
    상위 단계 근거가 충분하면 그 단계로 본다. 어느 단계도 기준 미달이면
    unassigned(사례로 볼 근거 부족).
    """
    for key in ("s3_transformation", "s2_digitalization", "s1_digitization"):
        if scores[key] >= MIN_STAGE_HITS:
            return key
    return "unassigned"


def stage_mix(scores):
    hit = [k.split("_")[0].upper() for k, _ in STAGES[:3] if scores[k] >= MIN_STAGE_HITS]
    return "+".join(hit) if hit else "-"


def collect():
    files = sorted(glob.glob(os.path.join(config.OUTPUT_DIR, "**", "*.md"), recursive=True))
    files = [f for f in files if os.path.basename(f) != "README.md"]

    rows = []
    for path in files:
        meta, text = parse_transcript(path)
        _hits, _density, words = score_text(text)
        rel = path.replace(os.sep, "/")
        source = "channel" if "/channels/" in rel else "keyword"
        relevance = classify_relevance(text, words)
        sentences = split_sentences(text)

        scores = {key: count(pats, text) for key, pats in STAGES}
        stage = assign_stage(scores)

        row = {
            "file": rel,
            "url": meta["url"],
            "title": meta["title"],
            "channel": meta["channel"] or "(미상)",
            "layer": CH2LAYER.get(meta["channel"], "" if source == "channel" else "키워드검색"),
            "hq_country": CH2HQ.get(meta["channel"], ""),
            "date": meta.get("upload_date", ""),
            "month": doc_month(path, meta),
            "source": source,
            "lang": meta["lang"],
            "words": words,
            "relevance": relevance,
            "stance": classify_stance(text) if relevance in ("ax_core", "ax_adjacent") else "neutral",
            "verhoef_stage": stage,
            "stage_mix": stage_mix(scores),
        }
        row.update(scores)
        for name, pats in ELEMENTS.items():
            row[name] = any_hit(pats, text)

        ev_total = 0
        for key, pats in STAGES:
            # 신호가 없는 단계는 문장 스캔 자체를 건너뛴다(속도)
            ev, sc = best_evidence(sentences, pats) if scores[key] else ("", 0)
            row[f"evidence_{key.split('_')[0]}"] = ev
            ev_total += sc
        row["evidence_strength"] = ev_total
        rows.append(row)
    return rows


def write_csv(rows):
    os.makedirs("analysis", exist_ok=True)
    path = os.path.join("analysis", "verhoef_stages.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return path


# ══════════════════════════════════════════════════════════════
# 3. 사람이 읽는 사례집
# ══════════════════════════════════════════════════════════════
HEADER = """# Verhoef 3단계 프레임으로 본 코퍼스 사례집

> **이론틀**: Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q.,
> Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary
> reflection and research agenda. *Journal of Business Research, 122*, 889–901.
> https://doi.org/10.1016/j.jbusres.2019.09.022
>
> 생성: `python classify_verhoef.py` · 원자료: `analysis/verhoef_stages.csv`
>
> 사례 **상세 카드**: [`VERHOEF_DOSSIER_S3.md`](VERHOEF_DOSSIER_S3.md) ·
> [`S2`](VERHOEF_DOSSIER_S2.md) · [`S1`](VERHOEF_DOSSIER_S1.md) · [`S4c`](VERHOEF_DOSSIER_S4c.md)
> (`build_verhoef_dossier.py`) — 사례별 판정 근거·주장·수치·언급 기업까지 펼친 카드.
> 상위 S3 사례를 원문으로 검증한 서술은 [`VERHOEF_S3_PROFILES.md`](VERHOEF_S3_PROFILES.md).

## 이 문서는 무엇인가

수집된 유튜브 AX 담론 전량을 Verhoef et al.(2021)의 **디지털 변화 3단계**로
태깅하고, 단계별로 **어떤 회사의 어떤 사례가 그 단계에 해당하는지**를
근거 문장과 함께 모은 것이다. 논문이 개념적 리뷰(스코핑 리뷰)라 사례가 없는
자리에, 이 코퍼스가 **2020–2026년 AI 국면의 사례 증거**를 채워 넣는 구조다.

| 단계 | 논문 정의 | 목표 | 이 코퍼스에서의 판별 신호 |
|---|---|---|---|
| **S1 digitization**(전산화) | 아날로그 정보의 디지털 변환. 가치창출 활동 자체는 불변 | 비용 절감 | 종이·수기·스캔·OCR·전산화·전자문서·데이터 입력 |
| **S2 digitalization**(디지털화) | 디지털 기술로 **기존 프로세스**를 변경·최적화 | 비용 절감 + 고객경험 | 프로세스/업무 자동화·RPA·ERP/CRM·클라우드 전환·챗봇·콜센터·리드타임 |
| **S3 digital transformation**(디지털 전환) | 전사적 차원의 **새 비즈니스 모델**과 가치창출·전유 로직 | 사업 논리 재구성 | 비즈니스 모델·수익구조 전환·플랫폼 비즈니스·생태계·구독/서비스화·가치사슬 재편 |
| **S4c**(보조축, 논문 밖) | AX가 DX의 연장(제4단계)인지 질적으로 다른 전환인지 논증할 후보 | — | 의사결정 알고리즘화·자율 에이전트·AI 인력화 |

**S4c는 Verhoef의 프레임이 아니다.** 논문은 AI를 IoT·블록체인과 함께 외부
동인의 하나로만 다루고, 2018년까지의 문헌만 포괄한다(생성형 AI 이전).
따라서 이 축은 "이 담론이 3단계 중 어디를 말하는가"를 판별한 뒤,
**3단계로 담기지 않는 잔여**를 표시하기 위한 것이다 — AX를 제4단계로 볼지
별개 전환으로 볼지는 이 잔여를 근거로 논증해야 한다.

## 방법 (재현 가능)

1. `transcripts/**/*.md` 전량(자막 스크립트)을 읽는다.
2. 단계별 정규식 사전(`classify_verhoef.py` 상단)의 **등장 횟수**를 센다.
3. 단계 배정: 3단계는 **누적·위계적**(전환은 디지털화를 포함)이므로
   **상위 단계부터** 최소 {min_hits}회 기준을 넘는 첫 단계로 배정한다.
   어느 단계도 미달이면 `unassigned`(사례로 볼 근거 부족).
4. 근거 문장: 단계 마커가 든 문장 중 **수치·행동 동사·AI 문맥** 점수가
   가장 높은 한 문장을 발췌한다.
5. Table 1의 네 전략 요소(디지털 자원·조직구조·성장전략·지표)를 보조 축으로
   0/1 코딩한다.

> ⚠️ 규칙 기반 1차 태깅이다. 발화 주체(벤더 홍보 vs 도입 기업 증언)와 맥락은
> 자동으로 완전히 가려지지 않는다. **인용 전 원문 스크립트·영상 확인 필수.**

## 기존 코드북(DX/AX/AT)과의 관계

이 저장소의 `docs/CODEBOOK.md`는 DX → AX → AT를 심화 스펙트럼으로 본다.
Verhoef 프레임은 그중 **DX 한 칸을 셋으로 쪼갠다**:

```
CODEBOOK:   DX ─────────────────────▶ AX ────────▶ AT
Verhoef:    S1 ─▶ S2 ─▶ S3           (논문 밖: S4c 보조축)
            전산화  디지털화  전환
```

즉 기존 `DX_hits`는 S1(전산화)·S2(프로세스 최적화)·S3(BM 재구성)을 **하나로
뭉뚱그린 지표**였다. 이 태깅의 실익은 "DX를 말한다"는 담론이 실제로는 대부분
**S2에 머문다**는 것을 분리해 보여주는 데 있다 — AX 담론이 S2의 반복인지
S3의 재구성인지를 가르는 것이 AX 연구의 핵심 질문이기 때문이다.
"""


def write_md(rows):
    os.makedirs("docs", exist_ok=True)
    path = os.path.join("docs", "VERHOEF_CASES.md")

    core = [r for r in rows if r["relevance"] == "ax_core"]

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(HEADER.format(min_hits=MIN_STAGE_HITS))

        # ── 분포 ──
        fp.write("\n## 1. 단계 분포\n\n")
        fp.write(f"전체 {len(rows):,}건 · 연구용 주 표본(`relevance=ax_core`) {len(core):,}건\n\n")
        fp.write("| 단계 | 전체 | 비율 | ax_core | 비율(ax_core) |\n|---|---:|---:|---:|---:|\n")
        all_c = collections.Counter(r["verhoef_stage"] for r in rows)
        core_c = collections.Counter(r["verhoef_stage"] for r in core)
        for key in ("s1_digitization", "s2_digitalization", "s3_transformation", "unassigned"):
            label = STAGE_LABEL.get(key, "unassigned(근거 부족)")
            fp.write(f"| {label} | {all_c[key]:,} | {100*all_c[key]/max(len(rows),1):.1f}% "
                     f"| {core_c[key]:,} | {100*core_c[key]/max(len(core),1):.1f}% |\n")
        s4 = sum(1 for r in core if r["s4c_algorithmic"] >= MIN_STAGE_HITS)
        fp.write(f"\n> S4c(알고리즘 전환 후보) 신호는 ax_core {s4:,}건"
                 f"({100*s4/max(len(core),1):.1f}%)에서 관측된다 — 단계 배정과 별개의 보조 축이다.\n")

        # 중첩(단계 혼합)
        fp.write("\n**단계 혼합**(한 영상이 여러 단계 기준을 동시에 넘는 경우) — "
                 "3단계가 누적적이라는 논문의 주장과 대조할 지점:\n\n")
        fp.write("| 혼합 유형 | ax_core 건수 |\n|---|---:|\n")
        mixes = collections.Counter(r["stage_mix"] for r in core)
        for mix, n in mixes.most_common(8):
            fp.write(f"| {mix} | {n:,} |\n")

        s2, s3 = core_c["s2_digitalization"], core_c["s3_transformation"]
        ratio = f"{s2/s3:.1f}배" if s3 else "—"
        fp.write(f"""
**읽는 법.** 단계가 배정된 {s2+s3+core_c['s1_digitization']:,}건 중 **S2가 {s2:,}건으로
S3({s3:,}건)의 {ratio}**다. 즉 이 코퍼스의 AX 담론은 압도적으로 **기존 프로세스의
자동화·최적화**(Verhoef의 digitalization)를 말하고 있고, **비즈니스 모델과 가치창출
로직을 바꾸는 이야기**(digital transformation)는 소수다. Verhoef et al.(2021)이
"기술 도입 문제가 아니라 비즈니스 모델 혁신 문제"라고 재정의한 지점과 대조하면,
현재 AX 담론의 대부분은 **S2 언어로 S3를 자칭**하고 있다는 가설을 세울 수 있다.
S1(전산화)이 {core_c['s1_digitization']:,}건으로 희소한 것은 2020년대 코퍼스로서 자연스럽다 —
아날로그→디지털 변환은 이미 지나온 단계이기 때문이다.

`unassigned` {core_c['unassigned']:,}건은 "AX 담론이지만 **단계 언어를 쓰지 않는**"
경우다(모델·에이전트 기술 소개, 전략 일반론 등). 3단계 프레임이 AI 국면의 담론을
얼마나 담아내지 못하는지를 보여주는 수치이기도 하다.
""")

        # 월별 추이
        fp.write("\n### 월별 추이 (ax_core, 단계별 건수)\n\n")
        months = sorted({r["month"] for r in core if re.match(r"\d{4}-\d{2}", r["month"])})
        fp.write("| 월 | S1 | S2 | S3 | unassigned |\n|---|---:|---:|---:|---:|\n")
        for m in months:
            sub = [r for r in core if r["month"] == m]
            c = collections.Counter(r["verhoef_stage"] for r in sub)
            fp.write(f"| {m} | {c['s1_digitization']} | {c['s2_digitalization']} "
                     f"| {c['s3_transformation']} | {c['unassigned']} |\n")

        # ── Table 1 매핑 ──
        fp.write("\n## 2. Table 1 전략 요소 × 단계 (ax_core 기준 출현율)\n\n")
        fp.write("논문 Table 1은 단계가 올라갈수록 (1) 디지털 자원이 자산→민첩성·네트워킹→"
                 "빅데이터 분석 역량으로 누적되고, (2) 조직이 표준 위계→분리된 애자일 유닛→"
                 "내재화된 유연 조직으로 이동하며, (3) 성장전략이 플랫폼 기반으로 확장되고, "
                 "(4) 지표가 전통 KPI→디지털 KPI로 옮겨간다고 본다. 코퍼스에서 그 패턴이 "
                 "실제로 관측되는지 대조한 표다.\n\n")
        groups = [
            ("(1) 디지털 자원", ["res_asset", "res_agility", "res_networking", "res_bigdata"]),
            ("(2) 조직구조", ["org_hierarchy", "org_separate_unit", "org_embedded"]),
            ("(3) 성장전략", ["growth_penetration", "growth_cocreation", "growth_diversification"]),
            ("(4) 지표", ["kpi_traditional", "kpi_digital"]),
        ]
        fp.write("| 요소 | S1 | S2 | S3 |\n|---|---:|---:|---:|\n")
        for gname, keys in groups:
            fp.write(f"| **{gname}** | | | |\n")
            for k in keys:
                cells = []
                for st in ("s1_digitization", "s2_digitalization", "s3_transformation"):
                    sub = [r for r in core if r["verhoef_stage"] == st]
                    n = sum(r[k] for r in sub)
                    cells.append(f"{100*n/max(len(sub),1):.0f}%")
                fp.write(f"| {k} | {cells[0]} | {cells[1]} | {cells[2]} |\n")

        # ── 단계별 사례 ──
        for sec, key in enumerate(("s3_transformation", "s2_digitalization", "s1_digitization"), 3):
            sub = [r for r in core if r["verhoef_stage"] == key]
            ev_key = "evidence_" + key.split("_")[0]
            sub = [r for r in sub if r[ev_key]]
            sub.sort(key=lambda r: (-r[key], -r["evidence_strength"]))
            by_company = collections.defaultdict(list)
            for r in sub:
                by_company[r["channel"]].append(r)

            fp.write(f"\n## {sec}. {STAGE_LABEL[key]} — 사례 {len(sub):,}건 / "
                     f"{len(by_company):,}개 회사·채널\n\n")
            fp.write("회사(채널)별로 단계 신호가 강한 순으로 최대 3건씩. "
                     "근거 문장은 **행동 동사가 든 문장**만 뽑았다(일반론 배제). "
                     "전량은 `analysis/verhoef_stages.csv` 참조.\n\n")
            for company in sorted(by_company, key=lambda c: -len(by_company[c])):
                items = by_company[company][:3]
                meta = items[0]
                tag = " · ".join(x for x in [meta["layer"], meta["hq_country"]] if x)
                fp.write(f"### {company} ({len(by_company[company])}건{' · ' + tag if tag else ''})\n\n")
                fp.write("| 월 | 톤 | 근거 문장 (스크립트 발췌) | 신호 | 출처 |\n|---|---|---|---:|---|\n")
                for r in items:
                    ev = r[ev_key].replace("|", "／").replace("\n", " ")
                    fp.write(f"| {r['month']} | {r['stance']} | {ev} | {r[key]} "
                             f"| [영상]({r['url']}) · [script](../{r['file']}) |\n")
                fp.write("\n")

        # ── S4c 보조 축 ──
        s4rows = [r for r in core if r["s4c_algorithmic"] >= MIN_STAGE_HITS and r["evidence_s4c"]]
        s4rows.sort(key=lambda r: (-r["s4c_algorithmic"], -r["evidence_strength"]))
        fp.write(f"\n## 6. S4c — 3단계로 담기지 않는 잔여 (AX 위치 논쟁용) · {len(s4rows):,}건\n\n")
        fp.write("의사결정의 알고리즘화·자율 에이전트·AI 인력화를 말하는 사례다. "
                 "Verhoef의 S3(비즈니스 모델 전환)와 **겹치는지 남는지**가 "
                 "'AX = DX의 제4단계인가, 질적으로 다른 전환인가' 논증의 경험적 근거가 된다. "
                 + ("아래는 신호가 강한 상위 120건.\n\n" if len(s4rows) > 120 else "아래가 전량이다.\n\n"))
        fp.write("| 회사·채널 | 월 | 배정 단계 | 톤 | 근거 문장 | 신호 | 출처 |\n|---|---|---|---|---|---:|---|\n")
        for r in s4rows[:120]:
            ev = r["evidence_s4c"].replace("|", "／").replace("\n", " ")
            fp.write(f"| {r['channel']} | {r['month']} | {STAGE_LABEL.get(r['verhoef_stage'], 'unassigned')} "
                     f"| {r['stance']} | {ev} | {r['s4c_algorithmic']} "
                     f"| [영상]({r['url']}) · [script](../{r['file']}) |\n")

        # ── 한계 ──
        fp.write("""
## 7. 한계와 사용법

1. **규칙 기반 1차 태깅**이다. 문맥·반어·부정을 완전히 잡지 못하고, 자동자막
   오인식('음악' 치환 등)이 마커를 훼손할 수 있다. 신호는 대리지표로만 쓴다.
2. **발화 주체**가 벤더 홍보인지 도입 기업 증언인지는 `source`(channel=vendor /
   keyword=media)까지만 자동 구분된다. 사례로 인용하려면 원문 확인이 필요하다.
3. **담론이지 실제 비용구조가 아니다.** "했다고 말한 것"의 집계이므로, K1(기업
   공개 자료)·인터뷰와의 삼각검증 없이는 성과 주장으로 읽을 수 없다.
4. **Verhoef의 프레임 자체가 2018년까지의 문헌**에 기반한다(생성형 AI 이전).
   이 코퍼스(2020–2026)를 그 프레임으로 읽을 때는 시점 한계를 명시해야 한다 —
   S4c 축을 따로 둔 이유다.
5. 단계 배정은 **상위 우선**이라 S3 신호가 2회 이상이면 S2/S1 신호가 더 많아도
   S3로 간다. 누적성 가정을 검증하려면 `stage_mix`와 원점수(`s1_*`·`s2_*`·`s3_*`)를
   직접 보라.
""")
    return path


def main():
    rows = collect()
    if not rows:
        print("[verhoef] 스크립트가 없습니다.")
        return
    csv_path = write_csv(rows)
    md_path = write_md(rows)

    core = [r for r in rows if r["relevance"] == "ax_core"]
    c = collections.Counter(r["verhoef_stage"] for r in core)
    print(f"[verhoef] 총 {len(rows):,}건 태깅 (ax_core {len(core):,}건) → {csv_path}, {md_path}")
    for key in ("s1_digitization", "s2_digitalization", "s3_transformation", "unassigned"):
        print(f"  {STAGE_LABEL.get(key, 'unassigned')}: {c[key]:,}건")
    s4 = sum(1 for r in core if r["s4c_algorithmic"] >= MIN_STAGE_HITS)
    print(f"  S4c 후보 신호: {s4:,}건")


if __name__ == "__main__":
    main()
