# NGINX 소개

- NGINX는 고성능의 오픈 소스 웹 서버 소프트웨어로, 웹 서버, 리버스 프록시 및 로드 밸런서로 사용됩니다.
- 기본적으로 이벤트 기반 아키텍처를 사용하여 대규모 동시 연결을 처리할 수 있으며, 높은 성능과 안정성을 제공합니다.

<br>

## NGINX를 프록시로 사용하는 방법

- NGINX를 프록시로 사용하면 클라이언트 요청을 다른 서버로 전달하고 응답을 다시 클라이언트에게 반환할 수 있습니다.
- 이를 통해 부하 분산, 캐싱, SSL 종단점 등 다양한 기능을 구현할 수 있습니다.

### 설정 방법

1. **NGINX 설치**: 운영 체제에 맞는 NGINX를 설치합니다.

2. **설정 파일 수정**: NGINX의 설정 파일을 수정하여 프록시로 동작하도록 설정합니다. 일반적으로 `nginx.conf` 파일을 수정합니다.

    예를 들어, 다음은 NGINX를 프록시로 사용하여 요청을 백엔드 서버로 전달하는 설정 예시입니다.

    ```nginx
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://backend_server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

    이 설정은 클라이언트로부터의 모든 요청을 `http://backend_server`로 전달합니다. 여기서 `backend_server`는 프록시로 사용할 백엔드 서버의 주소입니다.

3. **NGINX 재시작**: 설정을 적용하기 위해 NGINX를 재시작합니다.

    ```bash
    sudo systemctl restart nginx
    ```

<br>

## 마무리

- NGINX는 유연하고 성능이 뛰어난 웹 서버 및 프록시로, 다양한 환경에서 사용됩니다.
- 프록시로 사용할 때는 적절한 설정을 통해 요청을 백엔드 서버로 전달하고 응답을 클라이언트에게 반환할 수 있습니다.
