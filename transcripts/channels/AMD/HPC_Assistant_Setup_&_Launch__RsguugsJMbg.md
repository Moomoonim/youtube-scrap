# HPC Assistant: Setup & Launch

- 영상 링크: https://www.youtube.com/watch?v=RsguugsJMbg
- 채널: AMD
- 업로드일: 2026-06-05
- 자막 언어: en
- 단어 수: 약 132개

---

## 스크립트

HPC assistant setup wizard starts by asking a few configuration questions. Which HPC site are we installing it for? Which inference service should be used as a backbone of the agentic framework and which agentic framework the user has installed in their workspace? For the setup, the user needs to provide the required CIF files for building the database and running the Chroma MCP. Next, user selects the directories where the documentation should be cloned and where the persistent Chroma database should be stored. The wizard then builds the knowledge base. It clones the documentation into the selected path, splits the documents into chunks, embeds those chunks and stores them in the Chroma database. At the end, it starts the Chroma MCP instance. And that's it. The assistant is ready to use.
