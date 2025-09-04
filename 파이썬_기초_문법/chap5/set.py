"""
집합 자료형
set (중복 X, 순서 X, 변경 0, 삭제 O)
어떤 원소가 포함되어 있는지 확인하는 용도로 사용
"""

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 2, 'a', 'b', 'c'])
e = {'foo', 'bar', 'baz'}  # 키가 없이 사용 한다면 -> set으로 인식
f = {42, 'foo', (1, 2, 3), 3.141592}  # 튜플은 set에 포함 가능

print('a ->', type(a), a)
print('b ->', type(b), b)  # 중복된 원소는 제거됨
print('c ->', type(c), c)
print('e ->', type(e), e)
print('f ->', type(f), f)
print('a ->', a in b)

# 튜플 변환 set -> tuple
t = tuple(b)
print('t ->', type(t), t)
print('t ->', t[0], t[1:3])

# 리스트 변환 set -> list
l = list(c)
print('l ->', type(l), l)

# 길이
print('b의 길이 ->', len(b))
print('c의 길이 ->', len(c))
print('e의 길이 ->', len(e))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5])

# 교집합
print('s1 & s2 -> ', s1 & s2)
print('s1 & s2 -> ', s1.intersection(s2))

# 합집합
print('s1 | s2 -> ', s1 | s2)
print('s1 | s2 -> ', s1.union(s2))

# 차집합
print('s1 - s2 -> ', s1 - s2)
print('s1 - s2 -> ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 -> ', s1.isdisjoint(s2))  # 중복 원소가 없으면 True

# 부분집합
print('s1 & s2 -> ', s1.issubset(s2))  # s1이 s2의 부분집합이면 True
print('s1 & s2 -> ', s1.issuperset(s2))  # s1가 s2의 부분집합이면 True

# data 추가
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 ->', s1)

# data 삭제
# remove(6) -> 존재하지 않는 원소를 삭제하면 KeyError 발생
# discard는 존재하지 않는 원소를 삭제해도 에러가 발생하지 않음
# clear() -> 모든 원소 삭제
s1.remove(2)
print('s1 ->', s1)
s1.discard(3)
print('s1 ->', s1)
s1.discard(6)
print('s1 ->', s1)