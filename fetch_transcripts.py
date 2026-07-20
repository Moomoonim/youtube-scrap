"""
유튜브에서 AX(AI 전환) 관련 영상의 스크립트(자막)를 가져와 저장하는 스크립트.

동작 순서:
1. config.py 의 키워드로 유튜브를 검색한다 (yt-dlp 사용)
2. 각 영상의 자막을 yt-dlp 로 받아온다 (클라우드 IP 차단에 강함)
3. 이미 받은 영상은 건너뛴다 (transcripts/_seen.json 으로 중복 관리)
4. 오늘 날짜 폴더에 영상별 .md 파일과 요약 목록을 저장한다

직접 실행: python fetch_transcripts.py
"""

import glob
import json
import os
import re
import tempfile
from datetime import datetime, timedelta, timezone

import yt_dlp

import config


def log(message):
    """진행 상황을 화면에 출력한다."""
    print(f"[fetch] {message}", flush=True)


def slugify(text, max_length=60):
    """파일 이름으로 쓸 수 있게 제목을 안전한 문자열로 바꾼다."""
    text = re.sub(r"[\\/:*?\"<>|]", "", text)  # 파일명에 못 쓰는 문자 제거
    text = re.sub(r"\s+", "_", text.strip())
    return text[:max_length] or "untitled"


_cookie_logged = False


def cookie_opts():
    """쿠키 파일이 있으면 yt-dlp 옵션으로 돌려준다.

    유튜브가 서버 IP를 봇으로 차단할 때, 로그인 쿠키를 쓰면 우회된다.
    워크플로우가 COOKIES_FILE 환경변수에 쿠키 파일 경로를 넣어준다.
    """
    global _cookie_logged
    path = os.environ.get("COOKIES_FILE", "cookies.txt")
    if path and os.path.exists(path) and os.path.getsize(path) > 0:
        if not _cookie_logged:
            log(f"쿠키 파일 사용: {path}")
            _cookie_logged = True
        return {"cookiefile": path}
    return {}


def search_videos():
    """키워드로 유튜브를 검색해 영상 목록(중복 제거)을 돌려준다."""
    seen_in_search = set()
    videos = []

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,  # 빠르게 검색 결과 목록만 가져오기
        "skip_download": True,
        "ignoreerrors": True,
        "socket_timeout": config.SOCKET_TIMEOUT_SEC,
        **cookie_opts(),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for keyword in config.KEYWORDS:
            query = f"ytsearch{config.RESULTS_PER_KEYWORD}:{keyword}"
            log(f"검색 중: '{keyword}'")
            try:
                info = ydl.extract_info(query, download=False)
            except Exception as exc:  # 네트워크 등 일시적 오류는 건너뜀
                log(f"  검색 실패({keyword}): {exc}")
                continue

            for entry in (info or {}).get("entries", []) or []:
                if not entry:
                    continue
                video_id = entry.get("id")
                if not video_id or video_id in seen_in_search:
                    continue
                seen_in_search.add(video_id)
                videos.append(
                    {
                        "id": video_id,
                        "title": entry.get("title") or video_id,
                        "url": entry.get("url")
                        or f"https://www.youtube.com/watch?v={video_id}",
                        "channel": entry.get("channel")
                        or entry.get("uploader")
                        or "",
                        "keyword": keyword,
                    }
                )

    log(f"검색 결과 총 {len(videos)}개 영상(중복 제거 후)")
    return videos


def parse_vtt(path):
    """VTT 자막 파일을 깔끔한 한 줄 텍스트로 바꾼다."""
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    text_lines = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:  # 타임스탬프 줄
            continue
        if re.match(r"^\d+$", line):  # 큐 번호
            continue
        line = re.sub(r"<[^>]+>", "", line)  # <00:00:00.000>, <c> 등 태그 제거
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            text_lines.append(line)

    # 자동 자막은 줄이 겹쳐 반복되므로 연속 중복을 제거
    deduped = []
    for line in text_lines:
        if not deduped or deduped[-1] != line:
            deduped.append(line)

    text = " ".join(deduped)
    return re.sub(r"\s+", " ", text).strip()


def get_transcript_text(video_id):
    """yt-dlp 로 자막을 받아 (언어코드, 본문텍스트) 로 돌려준다.

    실패하면 (None, None) 을 돌려준다. (실패 사유는 yt-dlp 가 로그에 직접 출력)
    """
    url = f"https://www.youtube.com/watch?v={video_id}"

    with tempfile.TemporaryDirectory() as tmp:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,            # 영상은 받지 않음
            "writesubtitles": True,           # 사람이 단 자막
            "writeautomaticsub": True,        # 자동 생성 자막
            "subtitleslangs": config.LANGUAGES,
            "subtitlesformat": "vtt",
            "outtmpl": os.path.join(tmp, "%(id)s.%(ext)s"),
            "ignoreerrors": True,
            "retries": 2,
            "socket_timeout": config.SOCKET_TIMEOUT_SEC,
            "sleep_interval_requests": config.SLEEP_BETWEEN_REQUESTS_SEC,
            "sleep_interval_subtitles": config.SLEEP_BETWEEN_SUBTITLES_SEC,
            # 자막만 필요하므로 영상 화질(format) 정보가 없어도 계속 진행
            "ignore_no_formats_error": True,
            **cookie_opts(),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception:
            return None, None  # 다운로드 자체 실패

        vtts = glob.glob(os.path.join(tmp, "*.vtt"))
        if not vtts:
            return None, None  # 자막 파일이 만들어지지 않음 (차단/자막없음 등)

        # 설정한 언어 우선순위대로 자막 파일 선택
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
            return None, None  # 자막 내용이 비어 있음
        return lang, text


def load_seen(seen_path):
    """지금까지 받은 영상 ID 기록을 불러온다."""
    if os.path.exists(seen_path):
        try:
            with open(seen_path, "r", encoding="utf-8") as fp:
                return json.load(fp)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_seen(seen_path, seen):
    with open(seen_path, "w", encoding="utf-8") as fp:
        json.dump(seen, fp, ensure_ascii=False, indent=2)


def write_transcript_file(day_dir, video, lang, text):
    """영상 한 개의 스크립트를 마크다운 파일로 저장한다."""
    filename = f"{slugify(video['title'])}__{video['id']}.md"
    path = os.path.join(day_dir, filename)
    word_count = len(text.split())
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(f"# {video['title']}\n\n")
        fp.write(f"- 영상 링크: {video['url']}\n")
        fp.write(f"- 채널: {video['channel']}\n")
        fp.write(f"- 검색 키워드: {video['keyword']}\n")
        fp.write(f"- 자막 언어: {lang}\n")
        fp.write(f"- 단어 수: 약 {word_count}개\n\n")
        fp.write("---\n\n")
        fp.write("## 스크립트\n\n")
        fp.write(text + "\n")
    return filename


def main():
    # 날짜/시각은 한국시간(KST) 기준 — 하루 여러 회 실행이 같은 날짜 폴더에 모이도록
    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst)
    today = now.strftime("%Y-%m-%d")
    run_time = now.strftime("%H:%M")
    output_dir = config.OUTPUT_DIR
    day_dir = os.path.join(output_dir, today)
    os.makedirs(day_dir, exist_ok=True)

    seen_path = os.path.join(output_dir, "_seen.json")
    seen = load_seen(seen_path)

    videos = search_videos()

    saved = []
    for video in videos:
        if len(saved) >= config.MAX_VIDEOS_PER_DAY:
            break
        if video["id"] in seen:
            continue  # 이미 받은 영상은 건너뛰기

        lang, text = get_transcript_text(video["id"])
        if not text:
            log(f"  자막 없음/실패, 건너뜀: {video['title']}")
            continue

        filename = write_transcript_file(day_dir, video, lang, text)
        seen[video["id"]] = {
            "title": video["title"],
            "url": video["url"],
            "fetched_at": today,
            "lang": lang,
        }
        saved.append({**video, "lang": lang, "filename": filename})
        log(f"  저장 완료({lang}): {video['title']}")

    # 오늘 수집한 영상 목록(요약) 파일 작성
    # 하루 여러 회 실행되므로, 기존 목록을 덮어쓰지 않고 회차별로 이어 쓴다
    if saved:
        index_path = os.path.join(day_dir, "README.md")
        is_new = not os.path.exists(index_path)
        with open(index_path, "a", encoding="utf-8") as fp:
            if is_new:
                fp.write(f"# {today} AX 스크립트 수집 결과\n")
            fp.write(f"\n## {run_time} 수집 ({len(saved)}개)\n\n")
            for item in saved:
                fp.write(
                    f"- [{item['title']}]({item['filename']}) "
                    f"({item['lang']}) — [원본]({item['url']})\n"
                )

    save_seen(seen_path, seen)
    log(f"완료: 오늘 {len(saved)}개 영상 스크립트 저장 (폴더: {day_dir})")


if __name__ == "__main__":
    main()
