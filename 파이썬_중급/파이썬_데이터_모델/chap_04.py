"""
파이썬 데이터 모델 추상화
- 데이터 모델
- namedtuple
- model unpacking
- 네임드 튜플 실습 코딩
"""

# 객체 -> 파이썬의 데이터를 추상화 한다.
# 모든 객체 -> id / type -> value

# 일반적 튜플
x1 = (1.0, 2.0)
y1 = (3.0, 4.0)

from math import sqrt

result1 = sqrt((x1[0] - y1[0]) ** 2 + (x1[1] - y1[1]) ** 2)
print(result1)
print(f"{result1:.2f}")

from collections import namedtuple
"""
collection module 하위에 있고, key or index로 접근 가능 
"""
# namedtuple 선언
# namedtuple(typename, field_names)
# tuple형식으로 나오는데 -> 내부 데이터가 무엇을 의미하는지 알 수 있음
Point1 = namedtuple('Point', 'x y')
x2 = Point1(1.0, 2.0)
y2 = Point1(3.0, 4.0)

result2 = sqrt((x2.x - y2.x) ** 2 + (x2.y - y2.y) ** 2)
print(result2)
print(f"{result2:.2f}")

# namedtuple 선언 방법
Point2 = namedtuple('Point', ['x', 'y'])
Point3 = namedtuple('Point', 'x, y')
Point4 = namedtuple('Point', 'x y')
# x 중복 -> rename=True 옵션 사용 / rename = default False
Point5 = namedtuple('Point', 'x y x class', rename=True)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
x3 = Point2(x = 1.0, y = 2.0)
y3 = Point2(x = 3.0, y = 4.0)

# Point(x=1.0, y=2.0, _2=3.0, _3=4.0) -> under 난수로 표기
# rename=True 옵션으로 인해 => _1, _2로 변경
# rename=False 일 경우 작동 안함
x4 = Point5(1.0, 2.0, 3.0, 4.0)
y4 = Point5(3.0, 4.0, 5.0, 6.0)

# dict unpacking -> 알아서 unpacking
# ** -> dict unpacking
# * -> list, tuple unpacking
x5 = Point3(**temp_dict)  # dict unpacking -> 알아서 unpacking
print(x3, x4)
print(x5)

# 사용
print(x3.x + y3.x)
x, y = y3  # unpacking
print(x, y)

# 네임드 튜플 메소드
# ._make -> 리스트를 namedtuple로 만들어 준다.
temp = [52, 38]
p = Point1._make(temp)
print(p)

# ._fields -> 필드 네임 확인
print(p._fields)

# ._asdict() -> OrderedDict로 반환 (정렬된 딕셔너리)
print(p._asdict())