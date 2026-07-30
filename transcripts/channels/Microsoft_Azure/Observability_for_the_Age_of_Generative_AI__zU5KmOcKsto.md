# Observability for the Age of Generative AI

- 영상 링크: https://www.youtube.com/watch?v=zU5KmOcKsto
- 채널: Microsoft Azure
- 업로드일: 2026-04-09
- 자막 언어: en
- 단어 수: 약 393개

---

## 스크립트

Here is an e-commerce app, Zava, with several agentic components. As a manager at Zaver, I need to restock my inventory and I have a multi-agent workflow to help me. You can see the three agents hand off to each other and make a recommendation for restocking. As a customer at Zaver, I have an agent to assist me too. Here, I ask it to tell me my last order. Over in AI Foundry, I see the Customer Assistant agent. The other restocking agents were created with Agent Framework. I have not registered them in Foundry, but the data is still flowing to Azure Monitor. Whether I use Foundry, Agent Framework, OpenAI, or even LangChain or Copilot Studio, I can see it all in Azure Monitor. For the agents registered in Foundry, I can easily hop over to Azure Monitor from the Monitor view. This lands me in a new agents view where I can see agent runs, errors, tool calls, issues, model issues, tokens, and evals. It's a central pane of glass for your agentic apps. I can filter on that restocking agent, drill in a tool call, and click on the most recent trace. Here you can see the new simple mode, optimized, to see the flow of your multi-agent system. You can see all three of our agents with the brown meta tags handing off to each other and getting rich attributes on each span with prompts broken out and easy to read panes. Let's say you want to troubleshoot an error. I see the errors in my tool calls and scan my traces to find one with errors. I click on a trace with errors. Here I can see tool call exceptions, including the call stack, which lets me know where to look further. If I suspect an issue with my pod, I can switch over to Ask Insights right here. In context, when I search for the controller that my agent is running on, I see a couple instances of it in the last hour. Sure enough, I'm able to find that the container that's running my agent is in a warned state, and I'm able to view the logs and investigate further. I hope you'll find these new experiences useful, and there's more to come. Please feel free to share your feedback directly from within the product.
