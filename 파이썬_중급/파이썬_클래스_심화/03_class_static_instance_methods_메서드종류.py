"""
클래스 메서드
인스턴스 메서드
static 메서드
"""
class Car() :

    """
    Car class
    Author : Hwang
    Date : 2025.09.04
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.2

    # class method
    @classmethod
        # cls : class 자기 자신
        # class 변수를 controlling 할 때 사용
        # 모두가 참조 하기 때문 -> 값이 변경될 때 모두에게 영향을 미침
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
        elif per > 1:
            cls.price_per_raise = per
            print("Succeed! price increased.")

    # 생성자
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 인스턴스 메소드
    # 사용자 입장
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 레프리젠테이션 메서드
    # 자료형 타입에 따른 출력 (개발자 입장) / 엄격한 타입
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # instance method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get("price")))

    # instance method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get("price"))

    # instance method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get("price") * Car.price_per_raise)

    # static method
    # self, cls 둘 다 안받음
    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return "Ok! This car is BMW".format(inst._company)
        return "Sorry. This car is not BMW"

car1 = Car("현대", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("기아", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("쌍용", {"color": "silver", "horsepower": 300, "price": 6000})

# 전체정보
car1.detail_info()

# 가격정보
# 클래스 메서드 미사용
print(car1._details.get("price")) # 인스턴스 변수에 직접 접근하는 것은 좋지 않음
print(car1.get_price())
print(car1.get_price_culc())

# 가격 인상(클래스 메서드 사용)
Car.raise_price(1.5)
print(car1.get_price())
print(car1.get_price_culc())

# static method
# 클래스를 호출해서 사용하던, 인스턴스를 호출해서 사용하던 상관 없음
# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

# 인스턴스로 호출
print(Car.is_bmw(car3))
print(car1.is_bmw(car1))