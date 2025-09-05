"""
HashTable
- key-value를 저장하는 구조
- key는 중복 불가, value는 중복 가능
- 파이썬 dict 해쉬 테이블 예)
- key 값에 연산 결과에 따라 직접 접근 가능한 구조
- key 값을 hashing 함수 -> 주소 -> 키에 대한 value 접근
"""

# dict 구조
print(__builtins__.__dict__)  # key-value 구조

# Hash값 확인 -> 고유
t1 = (10, 20, (30, 40, 50)) # 튜플은 변경 불가
t2 = (10, 20, [30, 40, 50]) # 리스트는 변경 가능

print(hash(t1))
# print(hash(t2)) # TypeError: unhashable type: 'list' -> 리스트는 mutable(변경 가능)해서 해쉬 불가

# Dict Setdefault 예제
# 대용량 데이터에서 많이 사용
# 키가 중복 되어있는 상황
source = (('k1', 'v1'),
          ('k1', 'v2'),
          ('k2', 'v3'),
          ('k2', 'v4'),
          ('k2', 'v5'))

new_dict1 = {}
new_dict2 = {}

# no use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

    if k in new_dict2:
        new_dict2[k].append(v)
    else:
        new_dict2[k] = [v]
print(new_dict1)
print(new_dict2)
print()

# use setdefault
# setdefault -> key 값이 있으면 해당 value 반환, 없으면 디폴트 값 세팅
for k, v in source:
    new_dict1.setdefault(k, []).append(v) # default로 k , 나머지 값들은 list
    new_dict2.setdefault(k, []).append(v)
print(new_dict1)
print(new_dict2)

# 주의사항
new_dict3 = {k : v for k, v in source} # dict comprehension
print(new_dict3) # {'k1': 'v2', 'k2': 'v5'} -> key 값이 중복되면 덮어 써버리기 때문에 주의