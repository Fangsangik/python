"""
딕셔너리 (순서 X, 중복 X, 변경 O, 삭제 0 키:값 쌍)
범용적으로 가장 많이 사용

딕셔너리 -> List로 넣어줘서 많은 데이터 처리 가능

딕셔너리 선언
딕셔너리 특징
딕셔너리 수정
딕셔너리 함수
딕셔너리 중요성
"""

# 딕셔너리 선언 {}
# 키 중복을 허용 하지 않음
a = {'name': '홍길동', 'age': 30, 'city': '서울'}
b = {0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'name': '홍길동',
    'age': 30,
    'city': '서울',
    'hobby': ['영화', '독서', '여행'],
    'score': {'math': 90, 'english': 85}
}

# dict 내부에 튜플로 선언 후 -> key : value는 List로 묶어줘야 함
e = dict([
    ('name', '홍길동'),
    ('age', 30),
    ('city', '서울')
])

# dict 내부에 튜플로 선언 후 -> key = value
f = dict(
    Name='홍길동',
    Age=30,
    City='서울',
)
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
# get으로 접근 했을때 키가 없으면 None -> 더 안정적 운영 가능
# 그냥 가져왔을 경우 키가 존재 하지 않을때 -> KeyError 발생
print('>>>>>')
print('a - ', a['name'])
print('a - ', a.get('name0'))
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('city'))
print('f - ', f.get('age'))
print()

# 추가
# 속성 값으로 접근해서 넣으면 됨
# 같은 키 값을 넣으면 덮어 씌워짐
print('>>>>>')
a['Address'] = '서울시 강남구'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print('a -', len(a))
print('b - ', len(b))
print()

# 함수
# dict_keys() : 키만 가져옴, dict_values() : 값만 가져옴, dict_items() : 키와 값 쌍을 가져옴 -> 반복문에서 사용 (__iter__)
print('>>>>>')
print('a - ', a.keys())
print('a - ', a.values())
print('b - ', b.keys())
print('b - ', b.values())
print('c - ', c.keys())
print('c - ', c.values())
print('d - ', d.keys())
print('d - ', d.values())
print('e - ', list(e.keys()))
print('e - ', list(e.values()))
print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())
print('e - ', e.items())

print('a - ', a.pop('name'))  # 키를 통해서 삭제
print('a - ', a)
print()

# popitem() : 무작위 뽑아서 반환
print('>>>>>')
print('a - ', a.popitem())
print('a - ', a)
print('a - ', a.popitem())
print('a - ', a)
print()

# in 연산자
print('>>>>>')
print('a - ', 'name' in a)  # False
print('b - ', 'name' in b)  # False
print('a - ', 'name' not in a)  # True

# 수정 & 추가 -> 속성 값으로 접근
a['test'] = 'test_dict'
print('a - ', a)
a.update(age = 35)
print('a - ', a)
a.update({'city': '부산'})
print('a - ', a)