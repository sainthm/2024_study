# OCI(Open Container Initiative) & CRD(Custom Resource Definition)

1. OCI(Open Container Initiative):
   OCI는 컨테이너 이미지와 런타임 사양의 개방형 표준을 정의하는 프로젝트입니다. 이러한 표준은 컨테이너 이미지 및 컨테이너 실행 환경과 관련된 기술적인 세부 사항을 명확히하고 표준화하여, 다양한 컨테이너화된 응용 프로그램을 다양한 환경에서 실행할 수 있도록 지원합니다. OCI는 Docker 및 Kubernetes와 같은 컨테이너 기술의 표준화와 호환성을 증진하기 위해 만들어졌습니다.

<br>

2. CRD(Custom Resource Definition):
   CRD는 Kubernetes에서 사용자가 정의한 리소스 유형을 생성하는 데 사용되는 Kubernetes API 개체입니다. 이를 통해 Kubernetes 클러스터의 상태를 확장하고 사용자 지정 리소스를 정의하여 애플리케이션의 요구 사항에 맞게 Kubernetes를 확장할 수 있습니다. CRD를 사용하면 사용자 지정 리소스 및 이러한 리소스를 조작하는 API 엔드포인트를 생성할 수 있습니다. CRD는 Kubernetes의 핵심 기능 중 하나로, Operator나 컨트롤러 등의 사용자 지정 컨트롤러를 만들거나 특정 애플리케이션에 필요한 리소스 유형을 정의하는 데 사용됩니다.