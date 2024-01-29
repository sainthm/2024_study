# Resources

> Resources are the most important element in the Terraform language

- 테라폼에서 가장 중요한 엘리먼트
  - 테라폼을 통해, 리소스를 생성하므로 당연할지도?
- 각각의 리소스 블럭은 하나 이상의 오브젝트를 정의 → 리소스 생성!

## Resource blocks

- 리소스 블럭을 통해, 인프라스트럭처의 오브젝트를 생성

### Resource syntax

- 리소스 블럭은 특정한 로컬 이름에 대해, 특정한 타입의 리소스를 **선언**
  - 말이 복잡해보이지만 생각할 건, 선언한다는 점!
  - 그리고 specific local name 이라는 점! → 같은 모듈에서는 참조하지만 모듈 밖에서는 남남사이
