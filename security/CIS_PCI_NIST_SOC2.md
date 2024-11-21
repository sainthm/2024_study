
# IT 보안 업계에서 CIS, PCI, NIST, SOC 2 설명

- IT 보안 업계에서 **CIS**, **PCI**, **NIST**, **SOC 2**는 모두 정보 보안 및 규정 준수와 관련된 중요한 프레임워크 또는 표준입니다.
- 각각의 의미와 주요 내용을 살펴보겠습니다.

<br>

## 1. CIS (Center for Internet Security)

**CIS**는 인터넷 보안을 강화하기 위해 설립된 비영리 조직으로, 주로 **CIS Controls**와 **CIS Benchmarks**로 잘 알려져 있습니다.

### 주요 내용:
- **CIS Controls**:  
  - 18개의 핵심 보안 통제 항목으로 구성된 보안 프레임워크입니다.
  - 기업이 가장 효과적인 보안 전략을 수립하고 우선순위를 정할 수 있도록 지원합니다.
  - 초보자부터 전문가까지 사용할 수 있는 실용적인 보안 가이드를 제공합니다.
  - 예: 악성코드 방어, 사용자 계정 관리, 데이터 보호 등.
  
- **CIS Benchmarks**:  
  - 특정 소프트웨어, 하드웨어, 운영체제에 대한 **구성 가이드라인**입니다.
  - 벤치마크는 시스템을 보안 강화하는 데 필요한 권장 설정을 명시합니다.
  - 클라우드 환경(AWS, Azure), 데이터베이스, 네트워크 장비 등에 적용됩니다.

### 활용:
기업이 IT 자산을 효율적으로 보호하고, 규정 준수를 달성할 수 있도록 도움.

<br>

## 2. PCI (Payment Card Industry)

**PCI DSS (Payment Card Industry Data Security Standard)** 는 카드 결제 보안 강화를 위해 만들어진 국제 표준입니다.

### 주요 내용:
- **카드 결제 정보**를 안전하게 보호하기 위한 요구사항
- 신용카드 결제 정보를 처리, 저장, 전송하는 모든 조직이 준수해야 함
- 12가지 주요 요구사항으로 구성
  - 예: 방화벽 설치, 데이터 암호화, 취약점 관리, 접근 통제, 보안 정책 유지 등

### 활용:
- **비즈니스 대상**: 전자 상거래, POS 시스템, 결제 게이트웨이 등
- 준수 여부는 결제 처리 업체(Visa, MasterCard, American Express 등)에서 확인
- PCI DSS 준수는 고객 정보 유출 사고를 예방하고, 규정 위반으로 인한 벌금을 피하는 데 중요

<br>

## 3. NIST (National Institute of Standards and Technology)

**NIST**는 미국 국립 표준 기술 연구소로, 정보 보안을 위한 다양한 프레임워크와 가이드를 제공합니다.

### 주요 내용:
- **NIST Cybersecurity Framework (NIST CSF)**:  
  - 보안 위험을 식별하고 대응할 수 있도록 설계된 가이드라인
  - Identify(식별), Protect(보호), Detect(탐지), Respond(대응), Recover(복구) 5단계로 구성
  
- **NIST 800 시리즈**:  
  - 보안 통제(800-53), 리스크 관리(800-37), 클라우드 보안(800-144) 등 IT 보안에 관련된 문서 시리즈
  - 다양한 보안 요구사항 및 기술적 지침을 제공

### 활용:
- 주로 **정부 기관**과 **대기업**이 채택
- 사이버 보안 정책 수립 및 기술적 구현 시 필수 참고 자료

<br>

## 4. SOC 2 (System and Organization Controls 2)

**SOC 2**는 데이터 보안을 다루는 감사 프레임워크로, 주로 클라우드 기반 서비스 제공업체의 **보안, 가용성, 무결성** 등을 평가합니다.

### 주요 내용:
- **Trust Service Criteria (신뢰 서비스 기준)**:
  1. **Security**: 시스템 보호 여부
  2. **Availability**: 서비스의 가용성
  3. **Processing Integrity**: 데이터 처리의 무결성
  4. **Confidentiality**: 기밀 데이터 보호
  5. **Privacy**: 개인정보 처리의 적합성
  
- SOC 2 보고서:  
  - **Type I**: 시스템 설계가 신뢰 기준을 충족하는지 확인
  - **Type II**: 설계 및 운영이 일정 기간 동안 기준을 충족했는지 평가

### 활용:
- SaaS(Software as a Service) 업체, 클라우드 서비스 제공업체 등이 고객 및 파트너에게 신뢰를 제공하기 위해 준수.

<br>

---

<br>

## 요약 비교

| **항목**   | **CIS** | **PCI**                 | **NIST**            | **SOC 2**          |
|------------|---------|-------------------------|---------------------|--------------------|
| **초점**    | 보안 강화 가이드 | 카드 결제 정보 보안 | 보안 프레임워크와 표준 | 서비스 데이터 보안 |
| **적용 대상** | IT 자산 전반 | 카드 결제 정보 처리 기업 | 정부 기관, 대기업 | 클라우드, SaaS |
| **주요 문서** | CIS Controls, Benchmarks | PCI DSS             | NIST CSF, 800 시리즈 | SOC 2 보고서 |


<br>

각 프레임워크는 상호 보완적으로 활용될 수 있으며, 기업의 보안 요구사항과 산업 규정에 따라 적절히 선택 및 적용해야 합니다.