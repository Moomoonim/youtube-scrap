# Using an NVIDIA Launchable to Deploy the NVIDIA AI Blueprint for Video Search and Summarization

- 영상 링크: https://www.youtube.com/watch?v=lpB1wj2H79o
- 채널: NVIDIA Developer
- 업로드일: 2025-05-23
- 자막 언어: ko
- 단어 수: 약 136개

---

## 스크립트

Launchables를 통해 VSS를 매우 쉽게 체험해 볼 수 있습니다. Launchables는 AX L40S 인스턴스에 비주얼 에이전트를 배포하는 원클릭 스크립트입니다 . 실행 후 Jupyter 노트북을 열고 첫 번째 셀에 Nvidia NGC API 키를 입력한 다음 실행을 클릭하세요. 그러면 노트북은 설계도 에서 사용되는 각 Nvidia 추론 마이크로서비스(NIMS)를 다운로드하고 실행합니다 . 하나는 LLM용, 하나는 임베딩용, 그리고 하나는 재순위 지정용입니다. NIMS가 실행되면 VSS 엔진 컨테이너가 다운로드되어 배포됩니다. 여기에는 VLM(비전 언어 모델) 다운로드 및 TRT LLM 최적화 엔진 생성 작업이 포함되며, 이 과정은 약 15~20분 정도 소요됩니다. VSS 엔진이 배포되면 포트 포워딩을 통해 VSS 프런트엔드 인터페이스에 액세스할 수 있습니다 . 설계도를 숙지하셨다면 , 이제 직접 영상을 업로드하고 RTSP 스트림을 연결하여 그 기능을 더욱 자세히 살펴보세요. 그다음에는 담당자가 요약을 작성하고, 질의응답에 참여하고, 주요 내용을 담은 영상을 생성하도록 하여 창고 사례를 시도해 보세요. 작업이 완료되면 인스턴스를 중지하고 준비가 되면 다시 시작할 수 있습니다 .
