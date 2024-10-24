# 쿠버네티스 데몬셋 (DaemonSet)

## 1. 데몬셋(DaemonSet)이란?

데몬셋(DaemonSet)은 쿠버네티스(Kubernetes)에서 사용되는 컨트롤러의 일종으로, 클러스터 내의 각 노드에서 단일 파드(Pod)를 실행하기 위해 사용됩니다. 즉, 데몬셋을 생성하면 클러스터의 모든 (또는 특정 레이블이 있는) 노드에서 지정된 파드를 자동으로 배포하고 관리합니다.

데몬셋을 사용하면 노드가 추가되거나 삭제될 때 자동으로 파드가 추가되거나 삭제됩니다. 이는 로그 수집기, 모니터링 에이전트, 네트워크 플러그인 등의 데몬형 애플리케이션을 노드마다 배포할 때 유용합니다.

## 2. 데몬셋의 활용 사례

데몬셋은 다음과 같은 상황에서 주로 사용됩니다:

- **로그 수집기:** 각 노드에서 실행되는 로그 수집기를 배포하여, 노드의 로그 데이터를 중앙화된 로그 시스템으로 전송.
- **모니터링 에이전트:** 시스템 상태를 모니터링하고 메트릭을 수집하기 위한 에이전트를 각 노드에 배포.
- **네트워크 플러그인:** 네트워크 플러그인(예: Calico, Flannel)을 각 노드에 배포하여 쿠버네티스 네트워크를 구성.
- **스토리지 드라이버:** 각 노드에서 스토리지와 상호작용하는 드라이버를 배포하여 스토리지 리소스를 관리.

## 3. 데몬셋 예시

아래는 NGINX를 각 노드에서 실행하기 위한 데몬셋의 예시 YAML 파일입니다:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-daemonset
  labels:
    app: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

이 예시는 클러스터의 모든 노드에서 NGINX 컨테이너를 실행하는 데몬셋을 정의합니다. 각 노드에는 `nginx:latest` 이미지를 기반으로 하는 파드가 하나씩 배포됩니다.

## 4. 데몬셋의 특징

- **모든 노드에서 실행:** 데몬셋은 기본적으로 클러스터의 모든 노드에서 파드를 실행합니다. 특정 노드에서만 실행되도록 설정할 수도 있습니다(예: 노드 셀렉터 또는 테인트/톨러레이션 사용).
- **자동 업데이트:** 데몬셋은 노드가 클러스터에 추가되거나 제거될 때 자동으로 파드를 추가 또는 제거합니다.
- **파드 관리:** 데몬셋에 의해 생성된 파드는 쿠버네티스가 자동으로 관리하며, 파드가 종료되면 새로운 파드를 자동으로 생성합니다.
- **롤링 업데이트 지원:** 쿠버네티스는 데몬셋의 롤링 업데이트를 지원하여, 다운타임 없이 파드를 업데이트할 수 있습니다.
- **리소스 효율성:** 데몬셋은 각 노드에서 단일 파드만 실행되도록 하여 리소스 사용을 효율적으로 관리합니다.

## 5. 데몬셋 관리 명령어

- 데몬셋 생성: `kubectl apply -f <daemonset.yaml>`
- 데몬셋 조회: `kubectl get daemonsets`
- 특정 데몬셋 조회: `kubectl describe daemonset <daemonset-name>`
- 데몬셋 삭제: `kubectl delete daemonset <daemonset-name>`

## 6. 결론

데몬셋은 클러스터 내 모든 노드에서 특정 애플리케이션을 실행해야 하는 경우에 매우 유용한 쿠버네티스 오브젝트입니다. 특히 로그 수집기, 모니터링 에이전트, 네트워크 플러그인 등의 시스템 레벨 데몬을 관리할 때 필수적인 도구입니다.

