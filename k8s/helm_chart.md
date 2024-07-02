
# Kubernetes에서 Helm 차트 이해하기

## Helm 차트 소개

Helm은 Kubernetes의 패키지 매니저로, 컨테이너화된 애플리케이션의 배포, 확장 및 관리를 자동화하는 오픈 소스 시스템입니다. Helm은 차트라는 패키징 형식을 사용합니다. Helm 차트는 관련된 Kubernetes 리소스 집합을 설명하는 파일 모음입니다.

차트를 사용하면 단순한 단일 컨테이너 애플리케이션에서부터 많은 마이크로서비스로 구성된 복잡한 시스템에 이르기까지 모든 것을 배포할 수 있습니다. Helm은 Kubernetes 애플리케이션을 관리하는 데 도움을 주며, Helm 차트는 가장 복잡한 Kubernetes 애플리케이션조차도 정의, 설치 및 업그레이드하는 데 도움을 줍니다.

## Helm 차트의 주요 구성 요소

1. **Chart.yaml**: 차트에 대한 메타데이터를 포함한 주요 파일로, 차트의 이름, 버전 및 설명을 포함합니다.
2. **Values.yaml**: 차트의 기본 구성 값을 포함하는 파일입니다. 사용자는 이 값을 재정의하여 자신만의 값을 제공할 수 있습니다.
3. **Templates**: 템플릿 디렉토리에는 Kubernetes 매니페스트 템플릿이 포함되어 있으며, 이는 Values.yaml 파일의 값과 결합되어 최종 Kubernetes 매니페스트 파일을 생성합니다.
4. **Charts**: 종속 차트를 포함할 수 있는 디렉토리입니다.
5. **README.md**: 차트에 대한 정보, 사용법 설명 및 기타 관련 세부 정보를 제공하는 파일입니다.

## 예시: 간단한 Helm 차트 생성

간단한 웹 애플리케이션에 대한 Helm 차트를 만들어 보겠습니다. 이 애플리케이션은 Deployment와 Service로 구성됩니다.

### 1단계: Helm 차트 생성

먼저 Helm CLI를 사용하여 새 Helm 차트를 생성합니다:

```bash
helm create mywebapp
```

이 명령은 기본 디렉토리 구조와 Helm 차트 파일을 포함하는 `mywebapp`이라는 디렉토리를 생성합니다.

### 2단계: 차트 커스터마이징

`mywebapp` 디렉토리로 이동합니다:

```bash
cd mywebapp
```

다음과 같은 디렉토리 구조를 볼 수 있습니다:

```
mywebapp/
  ├── charts/
  ├── templates/
  │   ├── deployment.yaml
  │   ├── _helpers.tpl
  │   ├── hpa.yaml
  │   ├── ingress.yaml
  │   ├── NOTES.txt
  │   ├── service.yaml
  │   ├── serviceaccount.yaml
  │   └── tests/
  ├── Chart.yaml
  └── values.yaml
```

`values.yaml` 파일을 편집하여 기본 값을 설정합니다:

```yaml
# values.yaml
replicaCount: 2

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: stable

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false

resources: {}

nodeSelector: {}

tolerations: []

affinity: {}
```

`templates/deployment.yaml` 파일을 편집하여 배포를 구성합니다:

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mywebapp.fullname" . }}
  labels:
    app: {{ include "mywebapp.name" . }}
    chart: {{ include "mywebapp.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "mywebapp.name" . }}
      release: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ include "mywebapp.name" . }}
        release: {{ .Release.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - containerPort: 80
```

### 3단계: Helm 차트 설치

이 애플리케이션을 Kubernetes 클러스터에 배포하려면 `helm install` 명령을 사용합니다:

```bash
helm install mywebapp ./mywebapp
```

이 명령은 Helm 차트에 정의된 필요한 Kubernetes 리소스를 생성합니다.

### 4단계: 배포 확인

`kubectl` 명령을 사용하여 애플리케이션이 실행 중인지 확인할 수 있습니다:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## 결론

Helm 차트는 Kubernetes 애플리케이션을 관리하는 강력한 도구입니다. 애플리케이션의 리소스를 Helm 차트에 정의함으로써 애플리케이션을 쉽게 배포, 관리 및 업그레이드할 수 있습니다. 제공된 예시는 Helm 차트를 사용하여 간단한 웹 애플리케이션을 생성하고 배포하는 기본 구조와 단계를 설명합니다.

더 복잡한 사용법을 위해서는 Helm의 차트 종속성, 후크, 차트 저장소 등의 기능을 탐구해보세요.

