# Coding agents for the hardest bugs

- 영상 링크: https://www.youtube.com/watch?v=UVTh8af8uy4
- 채널: Cursor
- 업로드일: 2025-12-10
- 자막 언어: en
- 단어 수: 약 356개

---

## 스크립트

The bug mode is actually an agent that can help you with the most challenging parts of this process. And go to demo. I'm Albert, and before joining Cursor, I spent time doing kernel development work, including Linux optimizations and working on low-level USB drivers. I'm Alexey. Before Cursor, I was working on Chrome DevTools JavaScript debugging. And here at Cursor, my team usually deal with most challenging bugs. And today, we're excited to show you debug mode, a new way to interact with the agent to systematically approach the most complex bugs. First, you need to define an issue to an agent. You need to select the bug mode, and you need to submit your prompt. The agent will then generate hypotheses about what could be going wrong and insert runtime logs to try to prove or disprove them. The ideas that they have is like some of them you're going to come up with on your own, but some of them are like very cool and novel. Then it's going to give you a nice list of reproduction steps for me to go and manually test and reproduce the bug. The agent will have access to all of the runtime logs that it placed earlier and be able to pinpoint the root cause of the bug, leading to a much more precise and targeted solution. In this case, agent added a bunch of logs to get like very good understanding of what exactly is happening in your runtime. So, instead of fighting with the agent, you actually feel very included in the whole loop, and you work with the agent to solve the most complex bugs. As you can see, the issue has now been resolved, and you can click mark fixed. The agent will then remove all of the logs, leaving you with a nice and concise solution that you can now ship 100% reliably. Bug fixing, especially some very tricky bugs that sometimes you just get lost, you like try every other any ideas that you can come up with, and it's very like like almost sometimes I want to quit engineering.
