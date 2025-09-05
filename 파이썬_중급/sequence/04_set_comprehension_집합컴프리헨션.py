"""
HashTable -> 적은 resource로 많은 데이터를 효율적으로 저장하고 검색하는 자료구조
Dict -> key 중복 허용 X, Set -> 중복 허용 X, 순서 없음
"""

# Dict & Set
# immutable Dict
# 읽기 전용의 Dict

from types import MappingProxyType  # 읽기 전용의 Dict
d = {'key1': 'value1'}
d_frozen = MappingProxyType(d)  # 읽기 전용의 Dict / 표면상으로 읽기 전용이지만, 원본 Dict가 변경되면 반영됨
print(d, id(d)) # hash는 불가능
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'
print(d, id(d))
print()

# 수정 불가
# d_frozen['key2'] = 'value2' TypeError: 'mappingproxy' object does not support item assignment / 읽기 전용이므로 수정 불가

# Set
s1 = {'Apple', 'Banana', 'Orange', 'Apple', 'Orange'}  # 중복 허용 X, 순서 없음
print(s1, type(s1), len(s1), id(s1))  # {'Apple', 'Banana', 'Orange'} <class 'set'> 3
s2 = set(['Apple', 'Banana', 'Orange', 'Apple', 'Orange'])  # set() 생성자
print(s2, type(s2), len(s2), id(s2))  # {'Apple', 'Banana', 'Orange'} <class 'set'> 3
s3 = {2}
print(s3, type(s3), len(s3), id(s3))  # {2} <class 'set'> 1
s4 = {} # dict로 인식
print(s4, type(s4), len(s4), id(s4))  # {} <class 'dict'> 0 / dict로 인식
s5 = set() # set 생성
print(s5, type(s5), len(s5), id(s5))  # set() <class 'set'> 0
s6 = frozenset({'Apple', 'Banana', 'Orange', 'Apple', 'Orange'})  # frozenset: 읽기 전용의 set
print(s6, type(s6), len(s6), id(s6))  # frozenset({'Apple', 'Banana', 'Orange'}) <class 'frozenset'> 3
print()

# 추가 & 제거
s1.add('Melon')  # 추가
print(s1, id(s1))
# s6.add('Melon') AttributeError: 'frozenset' object has no attribute 'add' / frozenset는 읽기 전용이므로 추가 불가 / 메서드 자체가 없음

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터가 실행하는 코드
from dis import dis # 바이트 코드 생성 순서 확인 가능
print('-------') # 과정이 적음
print(dis('{10}'))
print('-------') # 과정이 더 많음 -> stack이 더 많은 상황
print(dis('set([10])'))
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name
# 없을 경우 name 함수를 사용해서 ''로 처리
print({name(chr(i), '') for i in range(65, 91)})  # A-Z
