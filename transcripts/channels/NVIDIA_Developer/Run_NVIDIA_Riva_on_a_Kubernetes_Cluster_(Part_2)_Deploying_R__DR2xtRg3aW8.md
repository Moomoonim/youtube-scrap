# Run NVIDIA Riva on a Kubernetes Cluster (Part 2): Deploying Riva on a Kubernetes cluster with Helm

- 영상 링크: https://www.youtube.com/watch?v=DR2xtRg3aW8
- 채널: NVIDIA Developer
- 업로드일: 2023-08-29
- 자막 언어: ko
- 단어 수: 약 442개

---

## 스크립트

GKE에서 Riva를 실행하는 두 번째 비디오에서는 Helm을 사용하여 Kubernetes 클러스터에 Riva를 배포하고, 해당 클러스터에서 실행 중인 Riva 서버를 통해 스페인어- 영어 음성-텍스트 변환 및 음성- 음성 변환을 실행합니다. 먼저 Riva Helm 차트를 다운로드해야 하는데, 저는 이미 화면 밖에서 다운로드했습니다. 직접 다운로드하려면 여기에 표시된 명령어를 사용하세요. Helm 차트가 포함된 Riva API 폴더에서 values.yaml과 templates/deployment.yaml 두 파일을 편집합니다. 먼저 values.yaml 파일을 수정하는 방법을 살펴보겠습니다. GCP에서 Riva를 실행한 데모 비디오와 동일한 스페인어-영어 음성-텍스트 변환 파이프라인을 실행하려면 모델 파일에서 다음과 같이 변경합니다. `repo generator.NGC model configs.Triton group zero field`, 그리고 ASR 모델의 언어 코드를 미국 영어에서 라틴 아메리카 스페인어로 변경합니다. 즉, `en`이 `ES`가 됩니다. 다음으로 미러 ` Megatron any en500m` 줄의 주석 처리를 해제합니다. 또한 이 Kubernetes 클러스터는 관리형 Kubernetes 플랫폼인 GKE에 배포되었으므로 `service.type`을 `cluster IP`에서 `load balancer`로 변경합니다. 이 변경 사항을 통해 외부에서 클러스터의 Riva 서버 로 추론 요청을 보내는 것이 훨씬 쉬워집니다. templates/deployment.yaml 파일에 spec.template.spec 아래에 노드 선택기 제약 조건을 추가하여 Riva가 올바른 GPU 리소스에만 배포되도록 합니다. 이 Riva Helm 차트를 GKE 클러스터에 적용하므로 노드 선택기 유형을 cloud.google.com GKE Dash 노드 풀로 지정합니다. 노드 풀 이름을 얻으려면 먼저 터미널에서 gcloud container clusters list 명령을 실행하여 해당 클러스터 이름을 복사합니다. 그런 다음 gcloud container node Dash pools list 명령을 실행하여 클러스터 이름을 빼고, GPU가 포함된 이름을 복사하여 deployments.yaml 파일의 gke dash 노드 풀 필드에 붙여넣습니다. Riva API 폴더가 있는 디렉터리의 deployments.yaml 파일에서 다음 명령을 실행하여 Riva Helm 차트를 GKE 클러스터에 적용합니다. Helm install을 실행했던 터미널은 다시 사용 가능해지지만, GKE 클러스터에서 Riva를 실제로 사용하려면 약 한 시간 정도 소요될 수 있습니다. 그동안 Cube Control에서 Pod 변수를 정의하여 배포를 모니터링할 수 있습니다. 다음은 Pod에 대한 설명입니다. Helm install을 실행한 후 약 13분이 경과했음을 알 수 있습니다. 마지막으로 Riva 모델 초기화 컨테이너 와 Riva 음성 API 컨테이너 모두에서 Cube Control 로그를 확인할 수 있습니다. 아마도 Riva 음성 API 컨테이너가 아직 실행되지 않았기 때문에 오류가 발생한 것 같습니다. Helm이 GKE 클러스터에 Riva를 설치하고 배포하는 데 약 1시간 30분이 걸렸습니다. 로드 밸런서 서비스 유형 덕분에 단일 노드 GCP VM 인스턴스에서 실행했던 것과 동일한 스페인어-영어, s에서 T, S에서 s 번역 데모를 동일한 환경에서 실행할 수 있습니다. 필요한 것은 추론 요청을 보내는 URI를 localhost에서 Riva API 서비스와 연결된 IP 주소로 변경하는 것뿐입니다. Cube Control get services를 실행하여 이름 열에서 Riva API를 찾고 외부 IP 열에서 연결된 IP 주소를 찾으면 됩니다. 그런 다음 해당 IP 주소를 riva.client.auth 호출의 URI 인수에 복사합니다. 이 설정에서는 포트 번호는 동일하게 유지됩니다. 이제 아래의 셀을 실행하고 결과를 확인해 보겠습니다. 삶 자체가 광기처럼 보일 때 번역은 꽤 괜찮아 보입니다. 그 광기가 어디에서 오는지 누가 알겠습니까? 최종 합성 오디오는 대략적으로 예상대로 들립니다. 이제 Terraform으로 GKE 클러스터를 설정 하고 Helm으로 해당 클러스터에 Riva를 배포하는 방법을 알게 되었습니다. 또한 해당 클러스터에서 실행 중인 Riva 서버에 추론 요청을 제출하는 한 가지 방법도 살펴보았습니다.
