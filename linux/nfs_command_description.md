
# RHEL/CentOS 기반 NFS 설정 명령어 설명

## 1. 명령어 설명

### 1.1 `sudo yum install nfs-utils`
- **`sudo`**: 관리자 권한으로 명령어를 실행합니다. 시스템에 소프트웨어를 설치하거나 중요한 설정을 변경할 때 사용됩니다.
- **`yum`**: RHEL/CentOS에서 패키지를 관리하기 위한 기본 패키지 관리 도구입니다. 소프트웨어 패키지를 설치, 업데이트, 제거할 때 사용됩니다.
- **`install`**: `yum` 명령어의 옵션으로, 지정된 패키지를 설치합니다.
- **`nfs-utils`**: NFS(Network File System) 서버와 클라이언트 운영에 필요한 유틸리티 모음입니다. 이 패키지를 설치하면 NFS를 통해 파일 공유를 설정할 수 있습니다.

### 1.2 `sudo vim /etc/fstab`
- **`sudo`**: 관리자 권한으로 명령어를 실행합니다.
- **`vim`**: 텍스트 편집기입니다. 이 명령어는 `vim`을 사용해 특정 파일을 편집할 수 있게 해줍니다.
- **`/etc/fstab`**: 파일 시스템 탑재 정보를 담고 있는 설정 파일입니다. 이 파일은 시스템 부팅 시 자동으로 파일 시스템을 마운트하는 데 사용됩니다.

### 1.3 `ip-address:/file-share mount-point-directory nfs options,_netdev 0 0`
- **`ip-address:/file-share`**: NFS 서버의 IP 주소와 공유 디렉터리 경로를 지정합니다. 예를 들어, `192.168.1.100:/export/shared`와 같은 형식입니다.
- **`mount-point-directory`**: NFS 공유를 마운트할 클라이언트 시스템의 디렉터리 경로를 지정합니다. 예: `/mnt/shared`.
- **`nfs`**: 파일 시스템 타입을 나타내며, 이 경우 NFS로 설정되어 있습니다.
- **`options`**: NFS 마운트에 적용할 옵션을 지정합니다. 여러 옵션을 쉼표로 구분하여 사용할 수 있습니다.
- **`_netdev`**: 네트워크 장치가 준비된 후에 파일 시스템을 마운트하도록 지시하는 옵션입니다. 이 옵션은 네트워크 기반 파일 시스템에서 중요합니다.
- **`0 0`**:
  - 첫 번째 `0`: 덤프 백업을 설정하지 않음을 의미합니다. 일반적으로 0으로 설정됩니다.
  - 두 번째 `0`: 파일 시스템을 부팅 시 검사하지 않음을 의미합니다. NFS 마운트에서는 보통 0으로 설정됩니다.

## 옵션
### 1. 덤프 백업 설정 옵션 (첫 번째 숫자)
- 0: 덤프 백업을 하지 않도록 설정합니다. 기본값으로, 대부분의 경우 0으로 설정되어 있습니다.
- 1: 덤프 백업을 하도록 설정합니다. 이 값을 설정하면 dump 명령어를 사용하여 해당 파일 시스템을 백업할 수 있습니다.

### 2. 파일 시스템 부팅 검사 옵션 (두 번째 숫자)
- 0: 부팅 시 파일 시스템을 검사하지 않도록 설정합니다. NFS와 같은 원격 파일 시스템에서는 일반적으로 0으로 설정합니다.
- 1: 루트 파일 시스템을 먼저 검사하도록 설정합니다. 이 값은 시스템이 부팅될 때 루트 파일 시스템의 무결성을 검사하기 위해 사용됩니다.
- 2: 루트 파일 시스템이 아닌 다른 파일 시스템을 부팅 시 검사하도록 설정합니다. 루트 파일 시스템 다음 순서로 검사됩니다.

### 사용 예시
- 1 1: 덤프 백업을 설정하고, 부팅 시 루트 파일 시스템 검사를 수행하도록 설정합니다.
- 1 2: 덤프 백업을 설정하고, 부팅 시 루트 파일 시스템 외의 다른 파일 시스템 검사를 수행하도록 설정합니다.

이 값을 통해 /etc/fstab에서 파일 시스템의 덤프 백업과 부팅 시 검사를 세밀하게 설정할 수 있습니다.