# How to Deploy High-Performance Storage for AKS | Free, Open-Source Azure Container Storage

- 영상 링크: https://www.youtube.com/watch?v=DqabGLa_Hxo
- 채널: Microsoft Azure
- 업로드일: 2026-01-07
- 자막 언어: ko
- 단어 수: 약 408개

---

## 스크립트

이 데모에서는 Azure Container Storage를 설치, 배포 및 사용하는 방법을 보여줍니다. 먼저, 어떤 스토리지 드라이버가 여러분의 상황에 적합한지 파악해야 합니다. Azure의 CSI 드라이버는 대부분의 Azure 디스크, 파일 및 Blob 서비스에 대한 Kubernetes 지원을 제공합니다. Azure Container Storage는 Azure Discs CI 드라이버에서 지원하지 않는 고유한 스토리지 백엔드에 대한 Kubernetes 지원을 제공합니다 . 현재 Azure Container Storage는 로컬 NVMe 디스크만 지원합니다. Kubernetes 환경의 VM에 로컬 NVME 디스크가 있는지 확인해야 합니다. 예를 들어 스토리지에 최적화된 L 시리즈 VM이나 GPU 가속 VM을 선택하세요. Azure 컨테이너 스토리지를 설치하는 방법을 보여드리겠습니다 . 먼저 AKS 확장 프로그램을 통해 Azure Container Storage를 설치하는 방법을 보여드리겠습니다 . Azure CLI의 최신 버전을 사용하고 있는지, Azure CLI용 Kubernetes 확장 프로그램 과 Kubernetes 명령줄 클라이언트인 `coupube control`이 설치되어 있는지 확인하십시오. AKS 클러스터를 처음부터 새로 생성하는 경우 Azure 컨테이너 스토리지를 활성화하는 플래그를 사용할 수 있습니다. aks create 명령에서 플래그를 지정할 때 , 이미 존재하는 AKS 클러스터를 업데이트하는 경우에도 동일한 플래그를 사용하는 유사한 명령을 사용할 수 있습니다. 몇 분 후면 Azure Container Storage가 설치됩니다. Azure Container Storage의 오픈 소스 버전을 설치하려면 해당 CSI 드라이버의 GitHub 페이지를 방문하여 최신 릴리스 버전을 찾으세요. Helm을 통해 로컬 CSI 드라이버를 설치할 수 있습니다. 온라인에서 찾은 최신 릴리스 버전으로 버전 옵션을 반드시 교체하십시오. 몇 분 후면 로컬 CSI 드라이버가 설치됩니다. 이제 aks get credentials 명령어를 사용하여 클러스터에 연결해 보겠습니다 . Kubernetes 클러스터에 Azure 컨테이너 스토리지를 사용하는 방법을 보여드리겠습니다 . Azure 컨테이너 스토리지가 설치되었으니 이제 로컬 NVMe 디스크를 사용하도록 설정해 보겠습니다. 로컬 NVMe는 매우 빠른 성능을 제공하여 빠른 임시 저장소가 필요한 앱에 적합합니다. 이 데이터는 가상 머신이 중지되거나 삭제되면 유지되지 않는다는 점을 기억하세요. Azure 컨테이너 스토리지는 최상의 성능을 위해 지정된 노드의 모든 NVME 디스크에 데이터를 자동으로 스트라이핑합니다 . 먼저 스토리지 클래스를 만들어 보겠습니다. 터미널이나 에디터를 열고 YAML 파일을 생성하세요 . 클러스터에 적용하세요. 그런 다음 생성되었는지 확인하십시오. 다음으로, 해당 스토리지를 사용하여 Pod를 배포해 보겠습니다 . 이 Pod는 Pod가 실행되는 동안에만 존재하는 임시 볼륨을 사용합니다 . 배포가 완료되면 정상적으로 작동하는지 확인하겠습니다 . 다음으로 FIO를 사용하여 간단한 성능 테스트를 실행하겠습니다. 이제 임시 스토리지를 사용하여 영구 볼륨을 사용하는 방법을 살펴보겠습니다. 이 접근 방식은 앱에서 영구 볼륨 클레임을 기대하지만 로컬 임시 저장소도 사용하는 경우에 적합합니다. 각 복제본이 자체 MVME 기반 볼륨을 갖도록 상태 저장 세트를 배포하겠습니다. 최신 예제 코드는 문서에서 확인하실 수 있습니다. 적용이 완료되면 고속 로컬 스토리지를 갖춘 포드가 나타나는 것을 볼 수 있습니다. 이제 로컬 NVMe 디스크를 사용하여 Azure 컨테이너 스토리지를 구성, 배포 및 관리하는 방법을 살펴보았습니다. 이제 귀사의 워크로드는 임시 또는 고성능 요구 사항에 이상적인 초고속 스토리지를 이용할 수 있습니다 . 자세한 내용은 Microsoft Learn의 Azure Container Storage 설명서를 참조하세요.
