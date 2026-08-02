# How GPUs and RDUs work together | SambaNova at COMPUTEX 2026

- 영상 링크: https://www.youtube.com/watch?v=bxjLJtwOxo0
- 채널: SambaNova
- 업로드일: 2026-06-29
- 자막 언어: en
- 단어 수: 약 138개

---

## 스크립트

Same prompt, same [music] model, but two different stacks. The right shows just GPU only [music] inference. The left adds SambaNova's SN40RDU. GPU [music] runs prefill, RDU runs decode. Watch the disaggregated stack. The agent thinks, plans, and acts. &gt;&gt; [music] &gt;&gt; Each step a fresh trip through the model. Code execution moves to the Intel Xeon CPU. Here's [music] where it adds up. The RDU decodes fast, so the gap between steps shrinks, and an agent [music] runs many of them per task. As the report grows, the context [music] balloons. Prompt caching and GPU compute keep prefill time low. It's [music] done in 32 seconds. Three chips, each doing what it's best at. [music] Live trace shows exactly how the work splits. The recap. Disaggregated finished three times faster. [music] For agents, decode is the bottleneck.
