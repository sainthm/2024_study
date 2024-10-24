# Software Composition Analysis (SCA)

## 1. 개요
- Software Composition Analysis(SCA)는 오픈 소스 및 서드파티 라이브러리 같은 소프트웨어 구성 요소의 보안 취약점을 식별하고 관리하는 방법입니다.
- 현대 소프트웨어 개발에서는 많은 오픈 소스 라이브러리와 패키지를 사용하기 때문에, 이러한 구성 요소에 대한 보안 검토가 매우 중요합니다.
- SCA 도구는 코드베이스 내에서 사용되는 오픈 소스 라이브러리 및 종속성을 분석하여 다음과 같은 사항을 검토합니다:

<br>

- **라이선스 준수**: 사용 중인 라이브러리의 라이선스 조건이 프로젝트에 적합한지 확인.
- **보안 취약점**: 알려진 보안 취약점이 포함된 라이브러리 식별.
- **버전 관리**: 오래된 버전이나 보안 패치가 적용되지 않은 구성 요소 파악.

<br>

SCA는 DevSecOps 파이프라인의 중요한 부분으로, 소프트웨어 개발 초기 단계에서부터 지속적으로 보안 리스크를 모니터링하고 해결하는 데 도움을 줍니다.

<br>

## 2. SCA의 중요성
- **취약점 식별**: 오픈 소스 구성 요소의 알려진 취약점을 신속히 파악할 수 있습니다.
- **자동화된 보안 검토**: SCA 도구는 소프트웨어의 보안성을 자동으로 평가하여 개발자의 수고를 덜어줍니다.
- **라이선스 리스크 관리**: 잘못된 라이선스를 사용하면 법적 문제가 발생할 수 있기 때문에, SCA는 올바른 라이선스 사용을 보장합니다.
- **지속적인 모니터링**: SCA 도구는 최신 취약점 데이터베이스를 참고하여 지속적으로 취약점을 모니터링합니다.

<br>

## 3. 대표적인 SCA 도구

### 3.1 **Snyk**
- **특징**: 오픈 소스 라이브러리의 보안 취약점을 탐지하고 자동으로 패치를 제안합니다. 라이브러리 취약점과 라이선스 문제를 모두 모니터링합니다.
- **장점**:
  - CI/CD 파이프라인과 통합 가능.
  - 실시간으로 취약점 데이터베이스 업데이트.
  - 다양한 언어와 프레임워크 지원.
  
### 3.2 **WhiteSource (Renamed to Mend)**
- **특징**: 코드 내 오픈 소스 라이브러리를 분석하고, 라이선스 문제와 보안 취약점을 감지합니다. WhiteSource는 모든 오픈 소스 라이브러리를 중앙에서 관리하고 정책 기반으로 허용되는 라이브러리만 사용할 수 있게 제어합니다.
- **장점**:
  - 광범위한 라이브러리 및 패키지 지원.
  - 자동화된 보안 및 라이선스 관리 기능 제공.
  - DevOps 툴체인에 쉽게 통합 가능.

### 3.3 **Black Duck by Synopsys**
- **특징**: 오픈 소스 및 서드파티 라이브러리에 대한 종합적인 보안 분석 및 관리 기능을 제공합니다. Black Duck은 보안, 라이선스 컴플라이언스, 코드 품질 문제를 모두 해결할 수 있는 포괄적인 솔루션입니다.
- **장점**:
  - 라이선스 및 보안 정책을 자동으로 적용 가능.
  - 통합된 보안 취약점 및 컴플라이언스 리포트.
  - 소프트웨어 공급망 전반에 걸친 리스크 관리 제공.

### 3.4 **JFrog Xray**
- **특징**: JFrog Xray는 바이너리 파일까지 분석하는 SCA 도구로, 아티팩트 저장소에 있는 모든 종속성에 대해 심층적인 보안 스캔을 제공합니다. 개발자 워크플로우 내에서 실시간 피드백을 제공합니다.
- **장점**:
  - 모든 아티팩트와 종속성의 심층 분석 제공.
  - JFrog 아티팩트리와 통합하여 아티팩트의 보안성을 강화.
  - CVE 데이터베이스와 실시간으로 연동.

### 3.5 **OWASP Dependency-Check**
- **특징**: 오픈 소스 라이브러리에서 알려진 보안 취약점을 검색하는 도구로, OWASP에서 제공하는 무료 도구입니다. Maven, Gradle, Python, .NET 등의 환경을 지원합니다.
- **장점**:
  - 무료로 사용할 수 있는 오픈 소스 도구.
  - 다양한 언어와 빌드 시스템을 지원.
  - 정기적인 CVE 데이터베이스 업데이트.

<br>

## 4. 결론
SCA 도구는 현대 소프트웨어 개발에서 필수적인 보안 관리 도구입니다. 오픈 소스 소프트웨어의 사용이 증가함에 따라, 이들 라이브러리의 보안 리스크를 효과적으로 관리하는 것은 기업의 전반적인 보안 수준을 높이는 중요한 요소입니다. 적절한 SCA 도구를 선택하고 개발 파이프라인에 통합함으로써, 오픈 소스 소프트웨어의 보안 및 라이선스 리스크를 줄이고 소프트웨어의 신뢰성을 강화할 수 있습니다.

<br>

## 5. 참고 자료
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [Snyk](https://snyk.io/)
- [WhiteSource (Mend)](https://www.mend.io/)
- [Black Duck by Synopsys](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html)
- [JFrog Xray](https://jfrog.com/xray/)