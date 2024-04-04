# top command

# Linux `top` 명령어

`top` 명령어는 리눅스 시스템에서 현재 실행 중인 프로세스와 시스템 리소스 사용량을 모니터링하는 데 사용됩니다. 이 명령어는 시스템 상태를 실시간으로 확인하고, 리소스 사용이 높은 프로세스를 식별하여 시스템 성능 문제를 해결하는 데 도움을 줍니다.

## 사용법

`top` 명령어를 실행하면 기본적으로 프로세스 목록과 시스템 리소스 사용량이 실시간으로 업데이트되어 화면에 표시됩니다. 일부 옵션을 사용하여 표시되는 정보를 변경하거나 정렬 순서를 조정할 수 있습니다.

### 기본 사용법

```bash
top
```

### 자주 사용하는 옵션

- `-i`: 업데이트 간격을 지정합니다. 예를 들어, `-i 5`는 5초마다 업데이트합니다.
- `-u`: 특정 사용자의 프로세스만 표시합니다.
- `-p`: 특정 프로세스 ID(PID)의 정보를 표시합니다.
- `-c`: 명령어 이름을 보여줍니다.
- `-o`: 특정 열을 기준으로 정렬합니다.

## 화면 구성 요소

`top` 명령어의 출력 화면은 다음과 같이 구성됩니다.

1. **첫 번째 행**: 시스템 부하, 실행 중인 프로세스 수, 스왑 사용량 등의 요약 정보를 표시합니다.
2. **두 번째 행**: 프로세스 관련 정보의 열 제목을 표시합니다.
3. **프로세스 목록**: 실행 중인 각 프로세스의 정보를 표시합니다.
   - PID: 프로세스 ID
   - USER: 프로세스를 실행한 사용자
   - %CPU: CPU 사용량
   - %MEM: 메모리 사용량
   - COMMAND: 실행 중인 명령어

## 단축키

- `q`: `top` 명령어를 종료합니다.
- `k`: 선택한 프로세스를 종료합니다.
- `1`: 다중 CPU 코어가 있는 시스템에서 각 CPU 코어별 사용량을 표시합니다.

## 예시

```bash
top -i 5
```

이 명령어는 5초마다 시스템 상태를 업데이트하여 표시합니다.

```bash
top -u username
```

이 명령어는 특정 사용자가 실행한 프로세스만 표시합니다.

## 참고

`top` 명령어는 시스템 관리자와 개발자들이 시스템 리소스 사용량을 추적하고 성능 문제를 해결하는 데 유용한 도구입니다. 또한, 프로세스 우선 순위를 변경하거나 응답하지 않는 프로세스를 종료하는 등의 작업을 수행할 수 있습니다.

이상으로 `top` 명령어에 대한 상세한 설명을 마칩니다. 부가적인 정보가 필요하다면 `man top` 명령어를 사용하여 더 자세한 내용을 확인할 수 있습니다.