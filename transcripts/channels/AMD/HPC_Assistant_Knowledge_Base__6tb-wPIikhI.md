# HPC Assistant: Knowledge Base

- 영상 링크: https://www.youtube.com/watch?v=6tb-wPIikhI
- 채널: AMD
- 업로드일: 2026-06-05
- 자막 언어: en
- 단어 수: 약 132개

---

## 스크립트

HPC Assistant also has access to the knowledge base. For example, we can ask about different storage types on Moomi and their corresponding quotas. To answer this, the agent needs to refer to the documentation. Using the Chrome IAMCP, it can search the knowledge base, retrieve the relevant pages, and ground its answer in the documentation. This is useful when deciding where to store large training datasets, where to keep the code, and which storage option fits each part of the workflow. Some questions require the Assistant to combine multiple capabilities. For example, if we ask how to pull a Docker container from Docker Hub and convert it to a CIF file that can run on Moomi, the Assistant can use both the SLARM skill and Chrome IAMCP to produce an answer.
