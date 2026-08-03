# Demo: Using /delegate in the GitHub Copilot CLI

- 영상 링크: https://www.youtube.com/watch?v=P2qK2BCdi-w
- 채널: GitHub
- 업로드일: 2026-01-25
- 자막 언어: en
- 단어 수: 약 458개

---

## 스크립트

Hey friends, I'm Scott and I'm playing around with GitHub Copilot CLI. In this case, I'm in WSL on Windows, but I'm also on Windows proper inside of PowerShell that runs everywhere, including on Macs. I asked it to upgrade my Next.js15 application uh to Nex.js16. I had it make a plan for me. Did a formal plan uh and I was thinking I would go and run this work locally, but then I realized that I could go and delegate that work while I focus on other things. So, I'm going to go and do a slash command, and I'm going to say delegate uh execute on this plan in the cloud and upgrade the app. So, it's going to go and execute on that plan. It's going to take those local changes and it's going to put those into a different uh branch in the cloud. The logs are going to start streaming. So, it says delegating session to GitHub coding agent. It's taking the conversation, the context about what we already talked about. And if we switch back over to the browser, take a look at what's happening in the cloud here. All right, we've got these remote agents that can go and do work. We can put in a pull request. You can go and say make an issue, assign that issue to someone, which is cool. In this case, that pull request is going to be pull request number six. There it is. Just showed up. So, we just by saying /delegate have gone and pushed that up into the cloud right now. Look at that. There's that original prompt. It's got the chronological review of everything. That work is actually happening right now. We can see that work. The logs will go streaming here if we want to, but I can just go and say start a new session. And I'll go off and do my thing. And I'm going to go and continue to work locally while the co-pilot in the cloud does its thing. And then when that session is done here, I'm going to click view session and look at it. Now it's starting to implement that. It's firing up playright. It's going to go and talk to uh the browser, spin this whole thing up, and upgrade the app for me in the cloud while I continue to work in uh on my local machine. And it did that just by saying delegate, which is pretty cool. You can check it out. Go ahead and pick up the uh GitHub Copilot CLI in npm npm rather. You can see it in Windgget and you can see it in Brew or you can check it out at copilot.github.com. github.com
