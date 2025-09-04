"""
객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지, 유지 보수, 대형 프로젝트에 용이
규모가 큰 프로젝트 -> 과거 = 함수 중심 (data가 방대해지고, 복잡성 증가) -> 복잡

클래스 중심 -> data 중심 -> 객체로 관리된다.
"""

# 일반적 코딩
car_company_1 = "현대"
car_detail_1 = [
    {"color": "white"},
    {"horsepower": 400},
    {"price": 8000},
]

car_company_2 = "기아"
car_detail_2 = [
    {"color": "black"},
    {"horsepower": 270},
    {"price": 5000},
]

car_company_3 = "쌍용"
car_detail_3 = [
    {"color": "silver"},
    {"horsepower": 300},
    {"price": 6000},
]

# 리스트 구조
# 관리하기 어려움
# 인덱스 접근시 실수 가능성, 삭제 접근 불편 (번호를 알아야 하기 때문)
car_company_list = ["현대", "기아", "쌍용"]
car_detail_list = [
    {"color": "white", "horsepower": 400, "price": 8000},
    {"color": "black", "horsepower": 270, "price": 5000},
    {"color": "silver", "horsepower": 300, "price": 6000},
]

# 삭제
del car_company_list[1]
del car_detail_list[1]
print(car_company_list, "\n", car_detail_list)
print()

# 딕셔너리 구조 (코드 반복, 중첩 문제 있음)
# key로 접근 가능, 삭제 편리
car_details = [
    {'car_company': "현대", 'car_detail': {"color": "white", "horsepower": 400, "price": 8000}},
    {'car_company': "기아", 'car_detail': {"color": "black", "horsepower": 270, "price": 5000}},
    {'car_company': "쌍용", 'car_detail': {"color": "silver", "horsepower": 300, "price": 6000}},
]

del car_details[1]
# pop -> key
car_details[0].pop("car_company")
print(car_details)

# 클래스 구조 (객체 지향 프로그래밍)
# 코드의 재사용, 코드 중복 방지, 유지 보수, 메소드를 활용
class Car() :

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

car1 = Car("현대", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("기아", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("쌍용", {"color": "silver", "horsepower": 300, "price": 6000})

print(car1)
print(car2)
print(car3)
# 속성 정보를 볼 수 있음
print(car1.__dict__)
# 내부 meta 정보
print(dir(car1))
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
print(car_list)
print()

# 반복문에서는 상황에 때라 __str__, __repr__ 구분해서 출력
for i in car_list:
    # 리프레젠테이션 메서드 호출
    print(repr(i))
    print(i)


