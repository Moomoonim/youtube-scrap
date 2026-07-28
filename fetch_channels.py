"""
config.CHANNELS 에 등록된 공식 유튜브 채널의 영상 스크립트를 수집한다.

동작 방식:
1. 각 채널의 '동영상' 탭에서 영상 목록을 최신순으로 가져온다
2. 아직 안 받은 영상의 자막을 받아 transcripts/channels/<채널명>/ 에 저장한다
3. 업로드일이 config.CHANNEL_SINCE(기본 2020-01-01) 이전이면 그 채널은 중단
4. 실행 1회당 채널별/전체 상한이 있어, 매 회차 조금씩 과거로 백필된다
   (이미 받은 영상은 _seen.json 으로 건너뛰므로 여러 번 돌수록 완성됨)

직접 실행: python fetch_channels.py
"""

import glob
import os
import random
import tempfile
import time
from datetime import datetime, timedelta, timezone

import yt_dlp

import config
from fetch_transcripts import (
    cookie_opts,
    load_seen,
    log,
    parse_vtt,
    save_seen,
    slugify,
)


def list_channel_videos(handle):
    """채널의 동영상 탭에서 (최신순) 영상 목록을 가져온다."""
    url = f"https://www.youtube.com/{handle}/videos"
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",  # 목록만 빠르게
        "skip_download": True,
        "playlistend": 1200,            # 목록 조회 시간 상한 (백필 진행되면 상향)
        "socket_timeout": config.SOCKET_TIMEOUT_SEC,
        "sleep_interval_requests": config.SLEEP_BETWEEN_REQUESTS_SEC,
        **cookie_opts(),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return [e for e in (info or {}).get("entries") or [] if e and e.get("id")]


def captions_advertised(info):
    """영상 메타데이터에 우리가 원하는 언어의 자막이 '있다고 표시'되는지 확인."""
    if not info:
        return False
    subs = set((info.get("subtitles") or {}).keys())
    autos = set((info.get("automatic_captions") or {}).keys())
    available = subs | autos
    return any(
        lang == want or lang.startswith(f"{want}-")
        for want in config.LANGUAGES
        for lang in available
    )


def fetch_video(video_id):
    """영상 정보와 자막을 받아 (info, 언어, 본문) 을 돌려준다.

    실패 시 (info, None, None). info의 자막 목록으로 '진짜 자막 없음'과
    '다운로드 실패(쿠키 만료 등)'를 호출부에서 구분할 수 있다.
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    with tempfile.TemporaryDirectory() as tmp:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": config.LANGUAGES,
            "subtitlesformat": "vtt",
            "outtmpl": os.path.join(tmp, "%(id)s.%(ext)s"),
            "ignoreerrors": True,
            "ignore_no_formats_error": True,
            "retries": 2,
            "socket_timeout": config.SOCKET_TIMEOUT_SEC,
            # 유튜브 세션 속도 제한(rate limit) 방지용 요청 간 지연
            "sleep_interval_requests": config.SLEEP_BETWEEN_REQUESTS_SEC,
            "sleep_interval_subtitles": config.SLEEP_BETWEEN_SUBTITLES_SEC,
            **cookie_opts(),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
        except Exception:
            return None, None, None

        vtts = glob.glob(os.path.join(tmp, "*.vtt"))
        if not vtts:
            return info, None, None

        chosen, lang = None, None
        for want in config.LANGUAGES:
            for path in vtts:
                if f".{want}." in os.path.basename(path):
                    chosen, lang = path, want
                    break
            if chosen:
                break
        if not chosen:
            chosen, lang = vtts[0], "unknown"

        text = parse_vtt(chosen)
        if not text:
            return info, None, None
        return info, lang, text


def write_channel_file(ch_dir, video_id, title, channel, upload_date, lang, text):
    """채널 영상 스크립트를 마크다운 파일로 저장한다."""
    date_str = "미상"
    if upload_date and len(upload_date) == 8:
        date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    filename = f"{slugify(title)}__{video_id}.md"
    path = os.path.join(ch_dir, filename)
    word_count = len(text.split())
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(f"# {title}\n\n")
        fp.write(f"- 영상 링크: https://www.youtube.com/watch?v={video_id}\n")
        fp.write(f"- 채널: {channel}\n")
        fp.write(f"- 업로드일: {date_str}\n")
        fp.write(f"- 자막 언어: {lang}\n")
        fp.write(f"- 단어 수: 약 {word_count}개\n\n")
        fp.write("---\n\n")
        fp.write("## 스크립트\n\n")
        fp.write(text + "\n")


def title_allowed(title):
    """제목 필터가 설정돼 있으면 해당 단어 포함 여부를 검사한다."""
    if not config.CHANNEL_TITLE_KEYWORDS:
        return True
    low = (title or "").lower()
    return any(k.lower() in low for k in config.CHANNEL_TITLE_KEYWORDS)


def main():
    kst = timezone(timedelta(hours=9))
    today = datetime.now(kst).strftime("%Y-%m-%d")
    started = time.monotonic()

    def over_budget():
        return (time.monotonic() - started) > config.CHANNEL_TIME_BUDGET_MIN * 60

    seen_path = os.path.join(config.OUTPUT_DIR, "_seen.json")
    seen = load_seen(seen_path)

    total_saved = 0
    summary = []       # (채널, 저장 수)
    failed_channels = []
    # 자막이 '있다고 표시'되는데 다운로드가 실패한 횟수 — 연속되면 쿠키 만료 의심
    suspect_failures = 0
    SUSPECT_LIMIT = 12

    # 매 회차 채널 순서를 섞어, 상한에 걸려도 모든 채널이 고르게 진행되게 한다
    channels = list(config.CHANNELS.items())
    random.shuffle(channels)

    for name, handle in channels:
        if total_saved >= config.MAX_CHANNEL_TOTAL_PER_RUN:
            log(f"이번 회차 총 상한({config.MAX_CHANNEL_TOTAL_PER_RUN}개) 도달 — 다음 회차에 계속")
            break
        if over_budget():
            log(f"시간 예산({config.CHANNEL_TIME_BUDGET_MIN}분) 도달 — 지금까지 결과를 저장하고 종료")
            break

        try:
            entries = list_channel_videos(handle)
        except Exception as exc:
            log(f"채널 접속 실패: {name} ({handle}) — {exc}")
            failed_channels.append(name)
            continue
        if not entries:
            log(f"채널 영상 없음/접속 실패: {name} ({handle})")
            failed_channels.append(name)
            continue

        ch_dir = os.path.join(config.OUTPUT_DIR, "channels", slugify(name, 40))
        saved_ch = 0
        attempts_ch = 0

        for entry in entries:
            if saved_ch >= config.MAX_PER_CHANNEL_PER_RUN:
                break
            if attempts_ch >= config.MAX_ATTEMPTS_PER_CHANNEL_PER_RUN:
                log(f"  {name}: 이번 회차 시도 상한 도달 — 다음 회차에 계속")
                break
            if total_saved >= config.MAX_CHANNEL_TOTAL_PER_RUN:
                break
            if over_budget():
                break

            vid = entry["id"]
            if vid in seen:
                continue
            if not title_allowed(entry.get("title")):
                continue

            attempts_ch += 1
            info, lang, text = fetch_video(vid)
            if info is None:
                # 추출 자체 실패(봇 차단/네트워크). 기록하지 않고 재시도하되,
                # 연쇄되면 세션 문제로 보고 조기 중단해 쿠키 소모를 막는다.
                suspect_failures += 1
                if suspect_failures >= SUSPECT_LIMIT:
                    log("🔴 영상 추출이 연쇄 실패 중 — 쿠키 무효화/봇 차단 의심. "
                        "이번 회차 채널 수집을 중단합니다. "
                        "(YOUTUBE_COOKIES 비밀값을 새 쿠키로 교체하세요)")
                    save_seen(seen_path, seen)
                    return
                continue

            upload_date = info.get("upload_date") or ""
            if upload_date and upload_date < config.CHANNEL_SINCE:
                # 최신순 목록에서 2020년 이전 영상을 만나면 이 채널은 백필 완료
                log(f"  {name}: {config.CHANNEL_SINCE[:4]}년 이전 도달 — 백필 완료")
                break

            title = info.get("title") or entry.get("title") or vid
            if not text:
                # 추출이 '건강한' 상태(화질 정보 존재)에서 자막 목록도 없을 때만
                # 진짜 '자막 없음'으로 기록한다. 화질 정보까지 비어 있으면
                # 유튜브가 응답을 제한한 것(PO토큰/차단/제한)이므로 재시도 대상.
                extraction_healthy = bool(info.get("formats"))
                if extraction_healthy and not captions_advertised(info):
                    seen[vid] = {
                        "title": title, "channel": name,
                        "status": "no_subs", "fetched_at": today,
                    }
                else:
                    suspect_failures += 1
                    log(f"  자막 취득 실패(재시도 예정): {title}")
                    if suspect_failures >= SUSPECT_LIMIT:
                        log("🔴 자막 취득이 연쇄 실패 중 — PO토큰/쿠키/차단 문제 의심. "
                            "이번 회차 채널 수집을 중단합니다.")
                        save_seen(seen_path, seen)
                        return
                continue

            suspect_failures = 0  # 성공하면 연쇄 실패 카운터 초기화

            os.makedirs(ch_dir, exist_ok=True)
            write_channel_file(ch_dir, vid, title, name, upload_date, lang, text)
            seen[vid] = {
                "title": title, "channel": name, "lang": lang,
                "upload_date": upload_date, "fetched_at": today,
            }
            saved_ch += 1
            total_saved += 1
            log(f"  저장({lang}): [{name}] {title}")

        if saved_ch:
            summary.append((name, saved_ch))
        save_seen(seen_path, seen)  # 채널마다 저장해 중단돼도 진행분 보존

    log("=== 채널 수집 요약 ===")
    for name, cnt in sorted(summary, key=lambda x: -x[1]):
        log(f"  {name}: {cnt}개")
    if failed_channels:
        log(f"접속 실패 채널({len(failed_channels)}): {', '.join(failed_channels)}")
    log(f"채널 수집 완료: 총 {total_saved}개 저장")


if __name__ == "__main__":
    main()
