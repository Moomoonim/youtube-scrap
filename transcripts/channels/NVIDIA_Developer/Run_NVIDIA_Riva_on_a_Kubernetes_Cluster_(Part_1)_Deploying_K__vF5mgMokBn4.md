# Run NVIDIA Riva on a Kubernetes Cluster (Part 1): Deploying Kubernetes Cluster to GKE with Terraform

- 영상 링크: https://www.youtube.com/watch?v=vF5mgMokBn4
- 채널: NVIDIA Developer
- 업로드일: 2023-08-29
- 자막 언어: ko
- 단어 수: 약 271개

---

## 스크립트

Google Kubernetes Engine에서 Riva를 실행하는 방법에 대한 두 편의 비디오 중 첫 번째 비디오에 오신 것을 환영합니다. 이 비디오에서는 Terraform을 사용하여 GKE에 Kubernetes 클러스터를 배포하는 방법을 다룹니다. 먼저 Terraform을 사용하여 GKE에 Kubernetes 클러스터를 배포하고, 그다음 Helm을 사용하여 해당 클러스터에 Riva를 배포합니다. 마지막으로 GCP에서 실행했던 것과 동일한 스페인어- 영어 음성 번역 데모를 실행하지만, 인증 URI를 변경하여 추론 요청을 GCP 노드 의 로컬 호스트가 아닌 GKE 클러스터로 보내도록 합니다. 오른쪽 상단 터미널에서 Terraform 모듈 저장소의 홈 디렉토리로 이동한 다음, 그 안에 있는 GKE 디렉토리로 이동했습니다. 해당 터미널에서 저장소의 출처도 확인할 수 있습니다. GKE 디렉토리에서 terraform.tf와 variables.tf 두 파일을 약간 수정해야 합니다. terraform.tfvars 파일에서 프로젝트 ID, 클러스터 이름, 지역 및 노드 영역 줄의 주석 처리를 해제하고 적절하게 수정합니다. variables.tf 파일에서 다음을 추가합니다. 기본 지역을 설정 하고 비용을 절감하기 위해 기본 GPU 유형을 수정하려면 터미널에서 `gcloud auth application Dash default login` 명령을 실행합니다. 이렇게 하면 Google 자격 증명을 Terraform 실행 파일에서 사용할 수 있게 됩니다. 생성된 링크를 클릭하여 브라우저 탭을 엽니다. 해당 탭에서 적절한 버튼을 클릭 하고 생성된 문자열을 터미널에 복사합니다. 다음으로 `terraform init` 명령을 실행하여 구성을 초기화합니다. Terraform이 성공적으로 초기화되면 `terraform plan` 명령을 실행하여 클러스터에 적용될 내용을 확인합니다. ` terraform plan`의 출력을 검사하여 모든 것이 정상적으로 보이면 ` terraform apply` 명령을 실행하여 GKE 환경에 코드를 적용합니다. 클러스터가 생성되고 배포되는 데 약 15분이 소요됩니다. ` terraform apply`가 완료되면 ` gcloud container clusters get Dash credentials` 명령을 실행하여 Cube Control로 클러스터에 연결합니다. 이 명령은 최소 하나의 인수( 클러스터 이름)를 필요로 합니다. 이 이름은 ` terraform.tf` 파일의 `vars` 섹션에 지정되어 있습니다. 이 비디오에서는 Terraform을 사용하여 Kubernetes 클러스터를 GKE에 배포했습니다. Riva를 배포하는 방법은 2부를 참조하세요. Helm을 사용하여 클러스터를 구성한 다음 스페인어-영어 음성-텍스트 변환 및 음성-음성 변환 추론을 실행합니다.
