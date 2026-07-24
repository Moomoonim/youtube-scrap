# How to Move Data to an Autonomous AI Lakehouse Using a Data Flow in Oracle FDI

- 영상 링크: https://www.youtube.com/watch?v=3Pr5anuLheI
- 채널: Oracle
- 업로드일: 2026-07-21
- 자막 언어: ko
- 단어 수: 약 315개

---

## 스크립트

이 튜토리얼에서는 Oracle Fusion Data Intelligence 데이터 흐름에서 선별된 데이터를 Oracle Autonomous AI Lakehouse 외부 데이터 소스에 저장하는 방법을 알아봅니다. 데이터 흐름을 사용하면 선별 및 변환된 데이터를 내보낼 수 있으므로 동일한 Oracle Autonomous AI Lakehouse 데이터 소스에 연결할 수 있는 다른 사람들과 데이터 세트를 쉽게 공유할 수 있습니다. 이 시나리오에서는 두 주제 영역의 통합 데이터를 외부 Autonomous AI Lakehouse 데이터 소스에 로드하려고 합니다. 두 가지 주제 영역을 중심으로 데이터 흐름도를 제시하며 시작하겠습니다 . HCM 인력 핵심 주제 영역에서는 부서, 인력, 위치 및 성과 평가 열을 추출합니다. HCM 성과 관리 주제 영역에서는 개인 식별자, 목표 등급, 관리자 이름, 평가 기간 및 성과 작업 상태 열을 추출합니다. 두 주제 영역에서 선택한 데이터를 결합하기 위해 두 주제 영역 사이에 간단한 조인을 추가했습니다. 저는 일치하는 행만 유지하고, 개인 식별자 열을 사용하여 주제 영역을 결합하도록 지정했습니다 . 데이터를 저장할게요. 데이터 흐름 기능에는 데이터를 변환할 수 있는 다양한 옵션이 있습니다 . 예를 들어, 필요에 따라 열을 추가, 선택, 이름 변경 및 변환할 수 있습니다. 이 예시에서는 두 가지 주제 영역의 데이터를 결합했지만, 필요한 경우 다른 연결이나 로컬 파일의 데이터 세트를 추가할 수도 있습니다 . 선별된 데이터를 Oracle Fusion Data Intelligence의 데이터 세트로 저장하거나 데이터베이스 연결을 통해 저장할 수 있습니다. 이 경우, 저는 해당 데이터를 Oracle Autonomous AI Lakehouse 데이터베이스 연결에 저장하겠습니다. 제 인스턴스에 이미 생성된 Oracle Autonomous AI Lakehouse 연결을 선택하겠습니다. 출력 테이블 이름이 ' 인력 성과 평가'인지 확인하겠습니다. 기존 데이터를 바꾸거나 기존 테이블에 새 데이터를 추가할 수 있습니다. Oracle Autonomous AI Lakehouse 연결에서 기존 테이블의 데이터를 교체하도록 선택하겠습니다. 컬럼 특성이 제대로 설정되어 있는지 확인하겠습니다. 이 데이터 흐름에서는 개인 식별자 데이터 형식을 속성으로 변경하겠습니다. 이제 데이터 흐름을 저장하고 실행하겠습니다. 이 과정이 완료되면 두 주제 영역에서 선별된 데이터가 Oracle Autonomous AI Lakehouse 외부 데이터 소스에 새 테이블로 저장됩니다. Oracle Fusion Data Intelligence 데이터를 선별하고 변환하는 데이터 흐름을 구축했으므로 이제 팀에서 해당 데이터 세트를 분석에 재사용할 수 있습니다. 아래 링크에서 이 시리즈의 다른 비디오와 Oracle Fusion Data Intelligence 사용에 대한 추가 자료를 찾아보세요.
