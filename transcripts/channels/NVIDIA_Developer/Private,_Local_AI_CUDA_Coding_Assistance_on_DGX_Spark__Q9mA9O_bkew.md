# Private, Local AI CUDA Coding Assistance on DGX Spark

- 영상 링크: https://www.youtube.com/watch?v=Q9mA9O_bkew
- 채널: NVIDIA Developer
- 업로드일: 2026-05-29
- 자막 언어: ko
- 단어 수: 약 243개

---

## 스크립트

CUDA는 비디오 병렬 컴퓨팅 플랫폼이며, NSIGHT Co-Pilot은 CUDA 개발자의 성공을 돕기 위해 맞춤 제작된 AI 코딩 도우미입니다 . 여기서는 DGX Spark 에서 로컬로 실행되는 LLM 및 백엔드 NIM을 포함하는 NSIGHT Co-Pilot 설계도를 시연해 보겠습니다 . 이는 데이터가 절대 통제권을 벗어나지 않도록 개인 정보 보호를 필요로 하고 클라우드 추론 비용을 피하고자 하는 개발자 및 조직을 위한 것입니다. 보시는 바와 같이 인터넷 연결 없이 VS Code에서 NSIGHT Co-Pilot [음악] 확장 프로그램을 실행했습니다 . 채팅 모델이 CUDA 관련 질문에 답하고 코드를 생성하도록 유도할 것입니다. 해당 채팅은 CUDA 인텔리전스 래그 파이프라인에서 GPT-OSS 120B NIM을 사용하여 CUDA에 특화된 응답을 제공합니다. 잠시 한발 물러서서 생각해 보면 , 오늘날 가장 인기 있는 AI 코딩 도구들은 고품질 CUDA 코딩 지원 기능을 제공하지 않습니다. [음악] VS Code용 NSIGHT Co-Pilot은 VS Code 마켓플레이스와 Open VSX에서 사용할 수 있으며 DGX 클라우드를 기반으로 개발자가 CUDA 애플리케이션을 작성하는 데 도움을 받을 수 있도록 지원합니다 . NSIGHT Co-Pilot의 온라인 버전은 CUDA 코딩 지원에는 훌륭하지만 , 보안이나 지적 재산권 보호 등의 이유로 클라우드 기반 도구(음악)를 사용할 수 없는 사람들의 요구를 충족시키지는 못합니다 . 편집기 내 지원을 위해 NSIGHT Co-Pilot에는 CUDA에 맞춰 자체적으로 학습시킨 자동 완성 모델이 있습니다. [음악] 그리고 Spark의 128GB 메모리 덕분에 이 모든 것을 로컬에서 실행할 수 있습니다 . NSIGHT Co-Pilot은 CUDA용 최신 개발자 도구이며, 최신 CUDA 라이브러리와 기술에 맞춰 지속적으로 업데이트할 예정입니다. DGX Spark 덕분에 NSIGHT Co-Pilot 설계도를 오프라인에서 실행할 수 있게 되어, 더 높은 수준의 개인 정보 보호가 필요하거나 클라우드 추론 비용을 없애고자 하는 음악 팀이 CUDA를 성공적으로 활용할 수 있도록 지원할 수 있습니다.
