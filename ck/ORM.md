# ORM (Object-Relational Mapping)

## 개요
ORM은 `Object-Relational Mapping`의 약자로, `객체와 관계형 데이터베이스 간의 매핑을 자동화하는 기술`입니다. 이를 통해 데이터베이스 테이블의 레코드를 객체로 취급하고, 객체 간의 관계를 이용하여 데이터베이스 조작을 추상화할 수 있습니다.

## 기능
1. 객체와 데이터베이스 테이블 간의 매핑 관리
2. 객체 간의 관계 표현
3. 데이터베이스 조작을 객체 지향적으로 처리

## 장점
1. 개발 생산성 향상: SQL 쿼리 작성에 필요한 시간을 절약하고, 객체 지향적인 코드 작성에 집중할 수 있습니다.
2. 유지보수성 향상: 객체를 이용하여 데이터베이스 조작을 추상화하므로, 변경이 필요한 경우 관련 로직을 한 곳에서 수정할 수 있습니다.
3. 데이터베이스 독립성: ORM을 사용하면 데이터베이스 종류에 관계없이 동일한 코드로 작업할 수 있습니다.

## 단점
1. 성능 문제: 복잡한 쿼리나 대량의 데이터를 다룰 때 원본 SQL에 비해 성능 저하가 발생할 수 있습니다.
2. 학습 곡선: ORM을 사용하기 위해서는 ORM 프레임워크의 학습이 필요하며, 초보자에게는 처음에는 이해하기 어려울 수 있습니다.
3. 제약 사항: ORM은 데이터베이스의 모든 기능을 완벽하게 대체하지 못할 수 있으며, 특정 데이터베이스의 고급 기능을 활용하기 어려울 수 있습니다.
4. 오버헤드: ORM은 객체와 데이터베이스 간의 매핑을 위한 추가적인 오버헤드가 발생할 수 있습니다. 특히, 간단한 쿼리의 경우에도 ORM을 사용하면 오버헤드가 발생할 수 있습니다.

## 대표적인 ORM 프레임워크
1. Hibernate (Java)
2. Entity Framework (.NET)
3. SQLAlchemy (Python)
4. Django ORM (Python)
5. Sequelize (Node.js)

## ORM 사용 예시 (Python의 SQLAlchemy를 기준으로)
```python
# SQLAlchemy를 사용하여 간단한 ORM 기능 구현
# 객체를 통해 데이터베이스 조작을 추상화

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 연결 설정
engine = create_engine('sqlite:///:memory:', echo=True)

# 객체와 테이블 간의 매핑을 위한 베이스 클래스 정의
Base = declarative_base()

# 객체 정의
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 테이블 생성
Base.metadata.create_all(engine)

# Session 생성
Session = sessionmaker(bind=engine)
session = Session()

# 데이터 조작
user = User(name='John', age=30)
session.add(user)
session.commit()

# 쿼리 실행
user = session.query(User).filter_by(name='John').first()
print(user.name, user.age)
```

