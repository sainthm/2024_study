# Spring Boot 및 Spring Boot로 만든 애플리케이션 설명

## Spring Boot

**Spring Boot**는 Spring Framework를 기반으로 한 자바 기반 프레임워크로, 스프링 애플리케이션을 쉽고 빠르게 개발할 수 있게 해줍니다. Spring Boot는 특히 설정을 간소화하고, 시작 프로젝트의 구성을 자동화하며, 개발자가 핵심 비즈니스 로직에 집중할 수 있게 하는 데 중점을 둡니다.

### 주요 특징

1. **자동 설정(Auto-Configuration)**:
   Spring Boot는 다양한 설정을 자동으로 해줍니다. 예를 들어, 데이터베이스 연결 설정, 웹 서버 설정 등 대부분의 설정이 자동으로 처리됩니다.

2. **스타터 종속성(Starter Dependencies)**:
   특정 기능을 쉽게 사용할 수 있도록 미리 구성된 종속성 모음을 제공합니다. 예를 들어, 웹 애플리케이션 개발을 위한 `spring-boot-starter-web`, 데이터 접근을 위한 `spring-boot-starter-data-jpa` 등이 있습니다.

3. **내장 웹 서버(Embedded Web Server)**:
   Tomcat, Jetty, Undertow와 같은 내장 웹 서버를 제공하여 별도의 외부 서버 없이도 애플리케이션을 실행할 수 있습니다.

4. **스프링 CLI(Spring CLI)**:
   Groovy를 사용하여 애플리케이션을 빠르게 개발하고 실행할 수 있는 커맨드라인 도구를 제공합니다.

5. **운영 환경 모니터링 및 관리**:
   애플리케이션의 상태를 모니터링하고, 관리할 수 있는 다양한 엔드포인트와 툴을 제공합니다. Spring Boot Actuator가 대표적입니다.

## Spring Boot로 만든 애플리케이션

Spring Boot로 만든 애플리케이션은 Spring Boot의 모든 장점을 활용하여 다양한 형태로 개발될 수 있습니다. 다음은 Spring Boot로 만든 애플리케이션의 주요 특성입니다.

1. **빠른 시작**:
   Spring Initializr를 통해 프로젝트를 생성하면 필요한 의존성이 미리 설정된 상태로 프로젝트가 생성됩니다. 이를 통해 개발자는 곧바로 애플리케이션 로직 구현에 집중할 수 있습니다.

2. **경량화된 애플리케이션**:
   필요 없는 설정을 최소화하고, 내장 서버를 사용하여 외부 의존성을 줄임으로써 경량화된 애플리케이션을 만들 수 있습니다.

3. **확장성**:
   Spring Boot의 모듈화된 구조 덕분에 필요한 기능만 선택적으로 사용하고, 쉽게 확장할 수 있습니다. 예를 들어, RESTful API 서버, 웹 애플리케이션, 배치 프로세스 등을 쉽게 개발할 수 있습니다.

4. **유연한 구성**:
   `application.properties` 또는 `application.yml` 파일을 통해 설정을 관리하고, 프로파일을 사용하여 환경별 설정을 쉽게 전환할 수 있습니다.

5. **생산성 향상**:
   자동 설정과 다양한 내장 도구 덕분에 개발 생산성을 크게 향상시킬 수 있습니다. 또한, 스프링의 강력한 생태계를 활용하여 다양한 기능을 쉽게 추가할 수 있습니다.

## 예시 코드

다음은 간단한 Spring Boot 애플리케이션의 예제 코드입니다.

### Main 클래스 (Application Entry Point)

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
