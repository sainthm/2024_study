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
- 리소스 타입과 이름은 모듈 내에서 unique 해야함! → 이거 자체로 identifier 가 되므로
- 블럭 { } 안에는 특정 리소스 자체가 갖고 있는 인자(argument)값이 옴
  - 당연히 인자값은 리소스 타입에 의존성을 갖고 있음

```hcl
resource "aws_instance" "web" {     # aws_instance 리소스 타입!
  ami           = "ami-a1b2c3d4"    # ami, instance_type 인자값은 리소스 타입(aws_instance)에 의존성!
  instance_type = "t2.micro"
}
```


