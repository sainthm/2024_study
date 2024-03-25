# 객체의 속성 (Attributes)

객체의 속성이란 `객체가 가지고 있는 데이터`를 의미합니다. `객체의 상태를 나타내며, 객체의 속성은 해당 객체의 특징과 특성을 정의`합니다. `객체의 속성은 클래스에 의해 정의되며, 각 객체는 해당 클래스의 속성을 가집니다.`

## 속성의 특징
1. **데이터 보유**: 속성은 객체가 가지고 있는 데이터를 의미합니다. 이 데이터는 객체의 상태를 나타내며, 객체가 존재하는 동안에 변할 수 있습니다.
2. **접근 제어**: 속성은 객체 내부에서 사용되는데, 이 속성에 대한 접근을 제어할 수 있습니다. 일부 속성은 외부에서 직접 접근이 가능하고(public), 일부는 객체 내부에서만 접근이 가능하고(private)할 수 있습니다.
3. **다양한 데이터 타입**: 속성은 다양한 데이터 타입을 가질 수 있습니다. 정수, 실수, 문자열, 리스트, 객체 등 어떠한 데이터 타입도 속성으로 사용될 수 있습니다.

## 속성의 예시 (Python으로 작성)
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make            # 제조사
        self.model = model          # 모델명
        self.year = year            # 출시년도
        self.odometer_reading = 0   # 주행거리 (기본값 0)

    def get_description(self):
        description = f"{self.year}년에 출시된 {self.make} {self.model}"
        return description

    def read_odometer(self):
        print(f"현재 주행거리: {self.odometer_reading}km")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행거리를 역으로 감소시킬 수 없습니다!")
```

위의 예시에서 `Car` 클래스는 자동차를 나타내며, `make`, `model`, `year`, `odometer_reading` 등의 속성을 가지고 있습니다. `make`, `model`, `year` 속성은 자동차의 제조사, 모델명, 출시년도를 나타내고, `odometer_reading` 속성은 자동차의 주행거리를 나타냅니다. 이러한 속성들은 각각의 객체가 가지고 있으며, 객체마다 속성의 값이 다를 수 있습니다.

