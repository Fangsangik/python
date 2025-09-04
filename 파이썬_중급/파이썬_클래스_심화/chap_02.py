"""
쿨래스 상세 설명
"""
class Car() :

    """
    Car class
    Author : Hwang
    Date : 2025.09.04
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0

    """
    self -> 인스터스 메서드 
    self가 있어야 자기 인스턴스의 값의 attribute에 value 값 가져올 수 있음 
    """
    # 생성자
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    # 인스턴스 메소드
    # 사용자 입장
    """
    __str__, __repr__ 같은 건 private이 아니라 스페셜 메서드
    __ 시작만 하고 끝에는 없는(__secret) 건 네임 맹글링으로 은닉용
    _name은 그냥 “내부용이니 건들지 마라”는 관례
    언더 스코어가 없는 경우는 직접 호출 가능
    """
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 레프리젠테이션 메서드
    # 자료형 타입에 따른 출력 (개발자 입장) / 엄격한 타입
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get("price")))

    def __del__(self):
        Car.car_count -= 1

car1 = Car("현대", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("기아", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("쌍용", {"color": "silver", "horsepower": 300, "price": 6000})

print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # 값 비교
print(car1 is car2) # 안스턴스 자체 비교

# dir & __dict__ 확인
# dir -> 해당 메서드가 갖고 있는 모든 속성을 보여줌
# __dict__ -> 해당 메서드가 key, value로 갖고 있는 속성을 보여줌
print(dir(car1))
print(dir(car2))
print(car1.__dict__)
print(car2.__dict__)

# Doctring
# """ """의 값을 볼 수 있음
print(Car.__doc__)
print()

car1.detail_info()
car2.detail_info()
print()

print(car1.__class__)
print(car2.__class__)
print(id(car1.__class__) == id(car2.__class__)) # 하나의 클래스에서 생성된 인스턴스이기 때문에 True

# 에러
# Car.detail_info() -> self가 없기 때문에 에러 / 직접 값을 넣어줘야 함

# 공유
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print(dir(car1))

del car1
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 생성자에 동일한 이름으로 변수 생성 가능 / 인스턴스 검색후 -> 상위(클래스 변수, 부모 클래스 변수)
# 생성자에 없을 경우에만, 클래스 변수에서 찾아본 후 접근 