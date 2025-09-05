"""
튜플 (순서, 중복은 가능, 수정 삭제는 불가능) = immutable
리스트와 비교 중요

튜플 선언
튜플 특징
튜플 슬라이싱
튜플 함수
패킹 & 언팩킹
"""
# 튜플 선언 ()
a = (1, 2, 3)
# 원소가 하나일때는 콤마를 붙여야 함
# 붙이지 않을 경우 int로 인식
b = (1)
c = (1,)
d = (100, 10000, 100000, 'ACE', 'BDF', 'GHI')
e = (100, 10000, 100000, ('ACE', 'BDF', 'GHI'))
print(type(a), type(b), type(c))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[2])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][0])
# 튜플 -> 리스트
print('e - ', list(e[-1][0]))

# 수정 X
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[1:])
print('d - ', d[:3])

# 연산
# 튜플의 내부의 원소가 변경 되지 않고 늘어나는 것은 허용
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)

# 튜플 함수
print('>>>>>')
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))  # 3의 위치
print('a - ', a.count(3))  # 3의 개수

# 패킹 & 언팩킹
# 패킹
# 묶었기 떄문에 패킹
t = ('a', 'b', 'c', 'd')
print(t)
print(t[0])

# 언팩킹
# 묶여 있던 것을 풀어서 각각의 순서에 맞게 하나씩 배치
# 괄호가 없더라도 언팩킹이 가능 하지만 관습상 괄호를 사용
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹과 언패킹
# 괄호가 없어도 튜플
t2 = 1, 2, 3, 4, 5
t3 = 1,
x0, x1, x2, x3, x4 = t2  # 언패킹
x5, x6, x7 = (4, 5, 6)

print(t2)
print(t3)
print(x0, x1, x2, x3, x4)
print(x5, x6, x7)
