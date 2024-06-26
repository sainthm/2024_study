# Linux 시스템 루트 디렉토리 (/) 구성

### 일반적인 루트 디렉토리 하위 폴더 구성

![스크린샷 2024-04-15 오후 3 07 28](https://github.com/sainthm/2024_study/assets/54525036/10265908-67d8-4026-8df7-29302ad56a88)

<br>

- **bin**: 바이너리(binary) 파일이 위치하는 디렉토리. 주로 실행 가능한 프로그램이 저장됨.
- **boot**: 부팅 관련 파일들이 위치하는 디렉토리. 부트로더와 커널 이미지 등이 여기에 저장됨.
- **dev**: 장치 파일들이 위치하는 디렉토리. 시스템에서 사용하는 하드웨어 디바이스들을 나타냄.
- **etc**: 시스템 설정 파일들이 위치하는 디렉토리. 주요 설정 파일들이 여기에 저장됨.
- **home**: 사용자 홈 디렉토리들이 담겨 있는 디렉토리. 각 사용자의 개인 파일과 디렉토리들이 여기에 위치함.
- **lib** 및 **lib64**: 공유 라이브러리 파일들이 위치하는 디렉토리. 프로그램들이 공유해서 사용하는 라이브러리 파일들이 저장됨.
- **media**: 이동식 미디어(USB 드라이브, CD-ROM 등)를 마운트할 때 사용되는 디렉토리.
- **mnt**: 일시적으로 파일 시스템을 마운트할 때 사용되는 디렉토리. 외부 장치를 임시로 연결할 때 사용됨.
- **opt**: 추가적인 소프트웨어 패키지들이 설치되는 디렉토리. 주로 사용자가 설치한 소프트웨어들이 여기에 위치함.
- **proc**: 가상 파일 시스템. 현재 실행 중인 프로세스와 커널 정보를 제공함.
- **root**: root 사용자의 홈 디렉토리. 일반적으로 /root에 위치함.
- **run**: 실행 중인 프로세스들의 임시 파일들이 위치하는 디렉토리.
- **sbin**: 시스템 관리용 바이너리 파일들이 위치하는 디렉토리. 시스템 설정이나 관리를 위한 실행 파일들이 저장됨.
- **srv**: 서버 데이터 디렉토리. 시스템에서 제공하는 서비스의 데이터들이 저장됨.
- **sys**: 커널과 관련된 파일들이 위치하는 가상 파일 시스템. 하드웨어 정보 등이 여기에 포함됨.
- **tmp**: 임시 파일들이 위치하는 디렉토리. 일시적으로 생성되는 파일들이 저장됨.
- **usr**: 사용자가 설치한 응용 프로그램, 라이브러리, 문서 등이 위치하는 디렉토리.
- **var**: 가변 데이터가 저장되는 디렉토리. 로그 파일이나 캐시 파일 등이 여기에 저장됨.
