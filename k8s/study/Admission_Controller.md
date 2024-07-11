# Kubernetes Admission Controller

## 개요
Kubernetes의 Admission Controller는 API 서버에 대한 요청을 가로채고 처리하여 클러스터에 적용되기 전에 이를 검증하고 수정하는 플러그인입니다. Admission Controller는 클러스터 보안, 정책 적용, 자원 관리 등의 다양한 목적을 위해 사용됩니다.

## 동작 원리
1. **API 요청 수신**: 클라이언트가 Kubernetes API 서버로 요청을 보냅니다.
2. **인증 및 권한 검사**: API 서버는 요청을 인증하고 권한을 확인합니다.
3. **Admission Controller 호출**: 요청이 유효한 경우, API 서버는 Admission Controller에 요청을 전달합니다.
4. **검증 및 수정**: Admission Controller는 요청을 검토하고, 필요한 경우 요청을 수정합니다. 검증에 실패하면 요청이 거부됩니다.
5. **저장 및 응답**: 요청이 성공적으로 처리되면, API 서버는 객체를 etcd에 저장하고 클라이언트에 응답을 반환합니다.

## 종류
Admission Controller는 두 가지 유형으로 나눌 수 있습니다:
- **Validating Admission Controller**: 요청을 검증하지만 수정하지 않습니다.
- **Mutating Admission Controller**: 요청을 검토하고 수정할 수 있습니다.

## 사용 사례
- **정책 적용**: 네임스페이스, 리소스 쿼터, 네트워크 정책 등 클러스터 정책을 강제합니다.
- **보안 강화**: PodSecurityPolicy를 사용하여 보안 설정을 강제합니다.
- **자원 관리**: 요청된 리소스가 클러스터의 제약 조건을 초과하지 않도록 합니다.

## 공식 문서 예시

Kubernetes 공식 문서에는 Mutating Admission Controller의 예시로 `MutatingWebhookConfiguration` 리소스를 사용하는 방법이 나와 있습니다.

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: example-mutating-webhook
webhooks:
  - name: example.com
    clientConfig:
      service:
        name: example-service
        namespace: example-namespace
        path: "/mutate"
      caBundle: "..."
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
    admissionReviewVersions: ["v1"]
    sideEffects: None
