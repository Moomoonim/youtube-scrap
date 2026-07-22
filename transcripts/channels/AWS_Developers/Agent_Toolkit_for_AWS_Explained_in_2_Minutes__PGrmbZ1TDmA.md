# Agent Toolkit for AWS Explained in 2 Minutes

- 영상 링크: https://www.youtube.com/watch?v=PGrmbZ1TDmA
- 채널: AWS Developers
- 업로드일: 2026-06-16
- 자막 언어: en
- 단어 수: 약 402개

---

## 스크립트

The toolkit has four parts. The AWS MCP server is a managed endpoint your agent connects to through the model context protocol. It gives your agent access to current AWS documentation, &gt;&gt; [music] &gt;&gt; not just training data, the actual docs searched in real time. And it lets your agent make authenticated AWS API calls using your IAM credentials. The calls go through the managed server, they get validated, and then they all land in CloudTrail. If you're on a team or if you're a platform engineer trying to figure out how to get developers to use coding agents without giving the agent full write access, there are IAM condition keys that let you write policies specific for agent initiated actions. So, you can give the agent read-only access through the MCP server even if the developer's own role can write. I'll come back to this after the demo. The second piece is agent skills. A skill is a runbook in markdown, step-by-step instructions for a specific AWS task written by someone who actually ran the workflow and found where agents get stuck. The Lambda plus API Gateway skill, for example, includes [music] the odds permission step. That's the step that grants API Gateway permission to invoke the function, and it's the [music] one agents most consistently miss. Without it, the API exists and the function exists, but they can't talk with each other. Skills are compact. It's a few thousand tokens, not the tens of thousands you'd get from pasting a full docs page into context. The agent discovers skills through the MCP server, loads the one it needs, follows it, and drops it when the task is done. Third piece, plugins. For Cloud Code and Code X, a plugin bundles the MCP server config and a set of skills [music] into one install. For every other agent, Corsa, Kiro, Windsurf, Klein, Cloud Code, or any other MCP compatible client, you add the AWS MCP server to your MCP config file directly. And the fourth piece is rules files, project level config that tells your agent how to use AWS in your project. [music] Things like use the MCP server for API calls or search for a skill before starting a task. [music] You drop them in your repo and they apply to every session. The toolkit itself is free. You just pay for whatever AWS resources the agent creates. [music]
