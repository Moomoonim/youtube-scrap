# The Rise of Dawn for Science - A Scalable System Powered by Intel® | Intel

- 영상 링크: https://www.youtube.com/watch?v=ChcHZDE21Ts
- 채널: Intel
- 업로드일: 2024-05-28
- 자막 언어: ko
- 단어 수: 약 161개

---

## 스크립트

[음악] 안녕하세요 여러분, 저는 이탈리아 Inter Comparation의 Ja Morosi입니다. 저는 애플리케이션 엔지니어이고, 캠브리지 대학교의 Dome 슈퍼컴퓨터에서 진행 중인 라이브 데모를 보여드리고 싶습니다. Streams 2는 압축성 난류 유동을 계산하기 위해 압축성 NAVAT 스톡 방정식을 풀 수 있는 CFD 솔버입니다. 이 코드는 원래 CUDA Fortran Paradigm을 사용하여 작성되었지만, Intel 컴파일러가 최신 Fortran 표준과 OpenMP 오프로드 Paradigm을 훌륭하게 지원했기 때문에 단 일주일 만에 Intel 1 API를 사용하여 CUDA Fortran에서 OpenMP로 변환하는 데 성공했습니다. 보시 다시피, Leonardo Class AA의 NVIDIA 800 GPU와 비슷한 성능을 보였고, Lumi 슈퍼컴퓨터의 MD Mi 250X GPU보다 훨씬 뛰어난 성능을 보여주었습니다. 총 64개의 노드, 즉 512개의 GPU를 사용했는데도 코드의 이상적인 스케일링을 항상 유지했습니다. 우리가 모든 리소스를 최대한 활용하여 첫 번째 노드에서 64번째 노드 실행까지 예상되는 속도 향상을 얻을 수 있다고 가정해 보겠습니다. 여기에서 실제 시뮬레이션을 볼 수 있습니다. 이것은 상호작용하는 충격파 경계층입니다. 여기서는 벽면에서 오는 경계층과 상호작용하는 충돌 충격파를 볼 수 있습니다. 또한 반사 충격파가 경계층과 상호작용하는 것을 볼 수 있습니다. 따라서 반사 충격파에서 나타나는 이러한 진동은 경계층과의 상호작용으로 인해 발생합니다.
