"""
채널 핸들 일괄 검증 (GitHub Actions 러너에서 실행).

- config.CHANNELS 중 0건 수집 채널 + config.py에 주석 처리된 후보 핸들을
  yt-dlp 목록 조회(extract_flat)로 검사한다.
- 출력: OK(실제 채널명·영상 수) / FAIL(사유) — 로그를 보고 config.py를 교정한다.

직접 실행: python verify_handles.py
"""

import os
import yt_dlp

import config
from fetch_transcripts import slugify

# config.py에서 주석 처리돼 있던 후보 핸들 (재검증 대상)
COMMENTED = {
    "Mistral AI": "@MistralAI",
    "AWS": "@AmazonWebServices",
    "TSMC": "@tsmc",
    "Samsung Semiconductor": "@SamsungSemiconductor",
    "Cerebras": "@CerebrasSystems",
    "Tenstorrent": "@Tenstorrent",
    "Groq": "@GroqInc",
    "SambaNova": "@SambaNovaAI",
    "HeyGen": "@HeyGen",
    "1X": "@1XTechnologies",
    "Baidu": "@Baidu",
    "NAVER": "@naver",
    "NAVER D2": "@naverd2",
    "카카오": "@kakao",
    "KT": "@KT",
}

# 대안 핸들 후보 (1차 실패 시 시도)
ALTERNATIVES = {
    "AWS": ["@amazonwebservices", "@AWSEventsChannel"],
    "TSMC": ["@tsmc_official", "@TSMCglobal"],
    "Samsung Semiconductor": ["@SamsungSemiconductorGlobal", "@samsungsemiconductor7024"],
    "Groq": ["@groq", "@GroqCloud"],
    "SambaNova": ["@SambaNovaSystems"],
    "1X": ["@1x_tech", "@1xtechnologies"],
    "NAVER": ["@navercorp", "@NAVER_official"],
    "카카오": ["@kakao_official", "@kakaocorp"],
    "KT": ["@kt_corp", "@KTOfficialChannel"],
    "Cerebras": ["@Cerebras"],
    "Mistral AI": ["@mistralaiofficial"],
    "Cruise": ["@DriveCruise"],
    "Slack": ["@SlackHQ"],
    "Snap": ["@SnapInc"],
    "Cursor": ["@cursor_ai", "@anysphere"],
    "Eli Lilly": ["@EliLillyandCompany", "@lillypad"],
    "General Motors": ["@generalmotors"],
    "BYD": ["@BYDCompany", "@BYDGlobal"],
    "Boston Consulting Group": ["@BostonConsultingGroup", "@TheBostonConsultingGroup"],
    "Intuit": ["@IntuitInc"],
    "Netflix": ["@netflix"],
    "Adobe": ["@AdobeCreativeCloud", "@AdobeExperienceCloud"],
    "Tencent": ["@TencentGlobal"],
    "iRobot": ["@iRobotCorp"],
    "T-Mobile": ["@TMobileUS"],
}


def probe(handle):
    """핸들의 /videos 목록을 얕게 조회. (성공, 채널명, 영상수|사유) 반환."""
    url = f"https://www.youtube.com/{handle}/videos"
    opts = {
        "quiet": True, "no_warnings": True,
        "extract_flat": "in_playlist", "playlistend": 5,
        "skip_download": True, "socket_timeout": 20,
    }
    if os.path.exists("cookies.txt"):
        opts["cookiefile"] = "cookies.txt"
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
        entries = [e for e in (info.get("entries") or []) if e]
        return True, info.get("channel") or info.get("title") or "?", len(entries)
    except Exception as exc:
        msg = str(exc)[:120]
        return False, None, msg


def main():
    # 1) 0건 수집 채널 찾기
    zero = []
    for name, handle in config.CHANNELS.items():
        d = os.path.join("transcripts", "channels", slugify(name, 40))
        n = 0
        if os.path.isdir(d):
            n = len([f for f in os.listdir(d) if f.endswith(".md") and f != "README.md"])
        if n == 0:
            zero.append((name, handle))

    targets = [("ZERO", n, h) for n, h in zero] + [("CMT", n, h) for n, h in COMMENTED.items()]
    print(f"검증 대상: 0건 채널 {len(zero)}개 + 주석 후보 {len(COMMENTED)}개\n")

    for kind, name, handle in targets:
        ok, chname, extra = probe(handle)
        if ok:
            print(f"[{kind}] OK   {name}: {handle} → 실제 채널명='{chname}', 최근영상 {extra}개")
        else:
            print(f"[{kind}] FAIL {name}: {handle} → {extra}")
            for alt in ALTERNATIVES.get(name, []):
                ok2, chname2, extra2 = probe(alt)
                if ok2:
                    print(f"        ↳ 대안 OK  {alt} → '{chname2}', 최근영상 {extra2}개")
                    break
                else:
                    print(f"        ↳ 대안 FAIL {alt}")


if __name__ == "__main__":
    main()
