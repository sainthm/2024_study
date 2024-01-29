# Files and Directories

### File Extension

- .tf 확장자
- Plain text
- JSON based 도 가능 → .tf.json 확장자
- 가이드 내, Terraform code 는 **configuration files**

### Text Encoding

- UTF-8 인코딩

### Directories and Modules

- 모듈은 .tf 파일의 모음들이 한 디렉토리 안에 들어있는 것으로 이해하자
- 테라폼 모듈은 디렉토리 내, Top-level 설정 파일로만 구성!!
  - 중첩된 디렉토리들은 완전 별개의 모듈로 취급
  - 자동으로 모듈에 포함되지도 않음
- 테라폼은 모듈 내, 설정 파일들을 검사하고 전체 모듈을 하나의 문서로 취급!
  - 다른 파일의 분리된 various 블럭 등은 작성자나 관리자의 편의를 위한 것이며, 모듈의 행동에는 전혀 영향이 없음!