"""
로컬(내 PC) 전용 저속 수집 실행기.

클라우드(GitHub Actions)는 데이터센터 IP라 유튜브 봇 차단이 잦다.
집(가정용) IP에서 이 스크립트를 **느린 간격(--pace)**으로 돌리면 차단이 훨씬 덜하다.

기존 fetch_channels.py / fetch_transcripts.py 의 함수를 그대로 재사용하므로
저장 형식·중복 관리(_seen.json)·백필 로직이 클라우드와 완전히 동일하다.
(이미 받은 영상은 자동으로 건너뛰므로, 언제 멈췄다 다시 켜도 이어서 받는다.)

예시:
  # 채널 백필을 20초 간격으로 최대 200개까지
  python fetch_local.py --pace 20 --limit 200

  # 특정 채널만(이름 일부 매칭), 채널당 최대 30개
  python fetch_local.py --channel "삼성" --per-channel 30 --pace 20

  # 키워드 검색분을 20초 간격으로
  python fetch_local.py --source keyword --pace 20 --limit 40

  # 쿠키 파일 지정(자동 자막 차단 우회에 도움)
  python fetch_local.py --cookies ./cookies.txt --pace 20

Ctrl+C 로 중단해도 그때까지 받은 것은 저장된다. 차단이 감지되면
안전하게 멈추므로, 30분쯤 뒤 같은 명령을 다시 실행하면 이어서 받는다.
"""

import argparse
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone

import config
from fetch_transcripts import (
    cookie_opts,
    get_transcript_text,
    load_seen,
    log,
    save_seen,
    search_videos,
    slugify,
    write_transcript_file,
)
from fetch_channels import (
    captions_advertised,
    fetch_video,
    list_channel_videos,
    rate_limited,
    title_allowed,
    write_channel_file,
)

SUSPECT_LIMIT = 12  # 연쇄 실패가 이만큼 쌓이면 봇 차단으로 보고 안전 중단


def human(sec):
    """초를 사람이 읽기 쉬운 시간 문자열로."""
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}시간 {m}분"
    if m:
        return f"{m}분 {s}초"
    return f"{s}초"


def collect_channels(args, seen, seen_path):
    """공식 채널 백필을 저속으로 수집한다."""
    since = args.since or config.CHANNEL_SINCE
    channels = list(config.CHANNELS.items())
    if args.channel:
        needle = args.channel.lower()
        channels = [(n, h) for n, h in channels if needle in n.lower()]
        if not channels:
            log(f"'{args.channel}' 와 매칭되는 채널이 없습니다.")
            return 0
        log(f"대상 채널 {len(channels)}개: {', '.join(n for n, _ in channels)}")
    random.shuffle(channels)

    total_saved = 0
    suspect = 0
    started = time.monotonic()

    for name, handle in channels:
        if args.limit and total_saved >= args.limit:
            break
        try:
            entries = list_channel_videos(handle)
        except Exception as exc:
            log(f"채널 접속 실패: {name} ({handle}) — {exc}")
            continue
        if not entries:
            log(f"채널 영상 없음/접속 실패: {name} ({handle})")
            continue

        ch_dir = os.path.join(config.OUTPUT_DIR, "channels", slugify(name, 40))
        saved_ch = 0
        attempts_ch = 0
        caption_fail_ch = 0  # 건강한 응답인데 자막만 실패한 연속 횟수(채널 단위)

        for entry in entries:
            if args.limit and total_saved >= args.limit:
                break
            if args.per_channel and saved_ch >= args.per_channel:
                break
            if attempts_ch >= args.max_attempts:
                log(f"  {name}: 시도 상한({args.max_attempts}) 도달 — 다음 채널로")
                break

            vid = entry["id"]
            if vid in seen:
                continue
            if not title_allowed(entry.get("title")):
                continue

            attempts_ch += 1
            info, lang, text = fetch_video(vid)

            # --- 봇 차단/네트워크로 추출 자체가 실패한 경우 ---
            if info is None:
                suspect += 1
                if suspect >= SUSPECT_LIMIT:
                    log("🔴 추출이 연쇄 실패 중 — 봇 차단/쿠키 만료 의심. 안전 중단합니다. "
                        "(30분쯤 뒤 같은 명령을 다시 실행하면 이어서 받습니다)")
                    save_seen(seen_path, seen)
                    return total_saved
                time.sleep(args.pace)
                continue

            # --- 최신순 목록에서 기준연도 이전 도달 = 이 채널 백필 완료 ---
            upload_date = info.get("upload_date") or ""
            if upload_date and upload_date < since:
                log(f"  {name}: {since[:4]}년 이전 도달 — 백필 완료")
                break

            title = info.get("title") or entry.get("title") or vid

            # --- 자막 취득 실패 ---
            if not text:
                # [2026-08-12 추가] 429(속도 제한)면 더 두드릴수록 제한만 길어진다.
                # 실패로 세지 말고 즉시 중단해서 나중에 이어받게 한다.
                if rate_limited():
                    log("🔴 유튜브 자막 요청이 속도 제한(HTTP 429)에 걸렸습니다 — 안전 중단합니다.")
                    log("   1~2시간 뒤 같은 명령을 다시 실행하면 이어서 받습니다. "
                        "(--pace 를 20~30 으로 올리면 재발이 줄어듭니다)")
                    save_seen(seen_path, seen)
                    return total_saved
                healthy = bool(info.get("formats"))
                if healthy and not captions_advertised(info):
                    # 진짜 '자막 없음' — 기록해 다시 시도하지 않음
                    seen[vid] = {"title": title, "channel": name,
                                 "status": "no_subs", "fetched_at": args.today}
                elif healthy:
                    # [2026-08-11 수정] 추출은 건강한데 자막만 실패 = 세션 문제가
                    # 아니라 이 채널 콘텐츠 특성일 가능성 — 채널 단위로만 세고,
                    # 연속되면 이 채널만 건너뛴다(전역 중단 금지).
                    # (기존엔 앞 채널의 자막 실패 12회가 표적 채널 도달 전에
                    #  실행 전체를 죽였음 — fetch_channels.py와 동일한 버그)
                    caption_fail_ch += 1
                    log(f"  자막 취득 실패(재시도 예정): {title}")
                    if caption_fail_ch >= 5:
                        log(f"  {name}: 자막 실패 연속 {caption_fail_ch}회 — 이 채널만 건너뛰고 다음 채널로")
                        break
                else:
                    # 화질 정보까지 비어 있으면 진짜 세션 문제(PO토큰/차단) 의심
                    suspect += 1
                    log(f"  자막 취득 실패(세션 의심): {title}")
                    if suspect >= SUSPECT_LIMIT:
                        log("🔴 자막 취득이 연쇄 실패 중 — 안전 중단합니다.")
                        save_seen(seen_path, seen)
                        return total_saved
                time.sleep(args.pace)
                continue

            # --- 성공 ---
            suspect = 0
            caption_fail_ch = 0
            os.makedirs(ch_dir, exist_ok=True)
            write_channel_file(ch_dir, vid, title, name, upload_date, lang, text)
            seen[vid] = {"title": title, "channel": name, "lang": lang,
                         "upload_date": upload_date, "fetched_at": args.today}
            saved_ch += 1
            total_saved += 1
            elapsed = time.monotonic() - started
            rate = elapsed / total_saved if total_saved else 0
            log(f"  저장({lang}) [{total_saved}{'/'+str(args.limit) if args.limit else ''}] "
                f"[{name}] {title}  (평균 {rate:.0f}s/개)")

            save_seen(seen_path, seen)  # 매 저장마다 보존 → 중단돼도 손실 없음
            time.sleep(args.pace)       # ★ IP 차단 완화의 핵심: 요청 간 저속 간격

    return total_saved


def collect_keywords(args, seen, seen_path):
    """키워드 검색분을 저속으로 수집한다."""
    kst = timezone(timedelta(hours=9))
    day_dir = os.path.join(config.OUTPUT_DIR, args.today)
    os.makedirs(day_dir, exist_ok=True)

    videos = search_videos()
    total_saved = 0
    suspect = 0
    started = time.monotonic()

    for video in videos:
        if args.limit and total_saved >= args.limit:
            break
        if video["id"] in seen:
            continue

        lang, text = get_transcript_text(video["id"])
        if not text:
            suspect += 1
            log(f"  자막 없음/실패, 건너뜀: {video['title']}")
            if suspect >= SUSPECT_LIMIT:
                log("🔴 연쇄 실패 — 봇 차단 의심. 안전 중단합니다.")
                save_seen(seen_path, seen)
                return total_saved
            time.sleep(args.pace)
            continue

        suspect = 0
        write_transcript_file(day_dir, video, lang, text)
        seen[video["id"]] = {"title": video["title"], "url": video["url"],
                             "fetched_at": args.today, "lang": lang}
        total_saved += 1
        elapsed = time.monotonic() - started
        rate = elapsed / total_saved if total_saved else 0
        log(f"  저장({lang}) [{total_saved}{'/'+str(args.limit) if args.limit else ''}] "
            f"{video['title']}  (평균 {rate:.0f}s/개)")
        save_seen(seen_path, seen)
        time.sleep(args.pace)

    return total_saved


def main():
    p = argparse.ArgumentParser(
        description="로컬 저속 수집 실행기 (IP 차단 완화용)")
    p.add_argument("--pace", type=float, default=20,
                   help="영상 사이 지연(초). 기본 20. 클수록 차단 위험↓ 속도↓")
    p.add_argument("--limit", type=int, default=None,
                   help="이번 실행에서 저장할 최대 개수(전체). 미지정=제한 없음")
    p.add_argument("--per-channel", type=int, default=None,
                   help="채널 하나당 저장할 최대 개수. 미지정=제한 없음")
    p.add_argument("--max-attempts", type=int, default=60,
                   help="채널 하나당 시도(성공+실패) 상한. 기본 60")
    p.add_argument("--channel", type=str, default=None,
                   help="이름 일부로 특정 채널만 대상(예: --channel 삼성)")
    p.add_argument("--source", choices=["channel", "keyword", "both"],
                   default="channel", help="수집 대상. 기본 channel")
    p.add_argument("--since", type=str, default=None,
                   help="이 날짜(YYYYMMDD) 이후만. 미지정=config 값(20200101)")
    p.add_argument("--cookies", type=str, default=None,
                   help="쿠키 파일 경로(자동 자막 차단 우회). COOKIES_FILE 로 설정됨")
    args = p.parse_args()

    if args.cookies:
        os.environ["COOKIES_FILE"] = args.cookies

    kst = timezone(timedelta(hours=9))
    args.today = datetime.now(kst).strftime("%Y-%m-%d")

    log(f"로컬 수집 시작 — 간격 {args.pace}s, 대상 {args.source}, "
        f"상한 {args.limit or '무제한'}")
    if args.pace < 5:
        log("⚠️ pace가 5초 미만입니다. 가정용 IP라도 차단 위험이 커집니다(권장 15~30초).")

    started = time.monotonic()
    seen_path = os.path.join(config.OUTPUT_DIR, "_seen.json")
    seen = load_seen(seen_path)
    total = 0
    try:
        if args.source in ("channel", "both"):
            total += collect_channels(args, seen, seen_path)
        if args.source in ("keyword", "both"):
            total += collect_keywords(args, seen, seen_path)
    except KeyboardInterrupt:
        log("\n⏹  중단됨(Ctrl+C). 지금까지 받은 것은 저장되었습니다.")
    finally:
        save_seen(seen_path, seen)

    dur = time.monotonic() - started
    log(f"완료: {total}개 저장, 소요 {human(dur)}. "
        f"분석 갱신은 `python classify.py && python summarize.py` 실행.")


if __name__ == "__main__":
    main()
