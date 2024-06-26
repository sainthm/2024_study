# Istio 및 Envoy 개요

## Istio란?

- Istio는 서비스 메시를 위한 오픈 소스 플랫폼으로, Kubernetes 클러스터에서 마이크로서비스 애플리케이션을 쉽게 연결, 보호, 제어 및 모니터링할 수 있게 해주는 기능을 제공합니다.
- Istio는 트래픽 관리, 보안, 모니터링 및 로깅 등의 서비스를 제공하여 마이크로서비스 아키텍처를 관리하는 데 도움이 됩니다.

### Istio의 주요 기능:
- **트래픽 관리**: 트래픽을 라우팅하고 분산시키는 데 사용됩니다.
- **폴리그랏 서비스 메시**: 서로 다른 언어 및 프레임워크로 작성된 서비스를 통합할 수 있습니다.
- **보안**: 서비스 간 통신을 보호하고 권한 부여 및 접근 제어를 제공합니다.
- **모니터링 및 추적**: 서비스의 성능을 모니터링하고 추적하는 데 사용됩니다.
- **로깅**: 서비스의 로그를 수집하고 분석하는 데 사용됩니다.

<br>

## Envoy란?

- Envoy는 클라우드 네이티브 환경에서 사용되는 고성능 프록시 및 서비스 메시 프록시입니다.
- Envoy는 서비스 간 통신을 위해 프록시 역할을 하며, 특히 Istio와 함께 사용되어 마이크로서비스 트래픽을 관리하는 데 중요한 역할을 합니다.

### Envoy의 주요 특징:
- **고성능**: C++로 개발되었으며, 네트워크 트래픽을 처리하는 데 뛰어난 성능을 제공합니다.
- **동적 구성**: 동적으로 구성이 가능하여 서비스 메시 환경에서 유연하게 사용할 수 있습니다.
- **로드 밸런싱**: 서버 간 부하 분산을 수행하여 서비스의 가용성을 향상시킵니다.
- **서비스 디스커버리**: 서비스 검색 및 탐지를 지원하여 서비스 간 통신을 용이하게 합니다.
- **강력한 보안 기능**: TLS(전송 계층 보안) 및 인증과 같은 보안 기능을 내장하고 있어 안전한 통신을 보장합니다.

Envoy는 서비스 메시 아키텍처에서 효율적인 트래픽 관리와 보안을 위해 사용되며, Istio와 같은 툴과 함께 사용될 때 가장 큰 효과를 발휘합니다.

<br>

## SNI (Server Name Indication)

- SNI는 TLS(Transport Layer Security) 프로토콜 확장으로, 클라이언트가 서버와의 TLS 연결을 설정할 때 사용되는 호스트 이름을 지정하는 데 사용됩니다.
- 이것은 하나의 IP 주소에 여러 개의 SSL 인증서를 호스팅할 수 있도록 하며, 특히 가상 호스팅(Virtual Hosting) 환경에서 유용합니다.
- Istio 및 Envoy와 같은 서비스 메시 플랫폼에서는 SNI를 사용하여 다중 호스트 서비스의 효율적인 관리를 가능케 합니다.
- Envoy는 SNI를 지원하여 서버로의 요청을 올바른 호스트로 라우팅하는 데 사용됩니다.
