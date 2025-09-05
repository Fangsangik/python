"""
If 구문 실습
관계 연산자
논리 연산자
일반 조건문
다중 조건문
중첩 조건문
"""

# 기본 형식
# 0이 아닌 수, 'abc', [1, 2, 3] 등은 True
# 0, '', [], {}, 빈 집합, 값이 없을 경우 False
print(type(True))
print(type(False))
print()

# 예 1
if True:
    print('Good')

# 예 2
# False익기 때문에 하위 구문 실행 X
if False:
    print('Bad')
else:
    print('Good')
print()

# 관계 연산자
# > , <, >=, <=, ==, !=
x = 15
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print()

city = ''
if city:
    print('you ar in', city)
else:
    print('plz input city')
print()

city2 = 'seoul'
if city2:
    print('you ar in', city2)
else:
    print('plz input city')
print()

# 논리 연산자
# and, or, not
a = 75
b = 40
c = 10

print('and - ', a > b and b > c)  # True
print('or - ', a > b or b > c)  # True
print('not - ', not (a > b))  # False
print('not - ', not (b > c))  # False
print(not True)
print(not False)
print()

# 산술, 관계, 논리 연산자 우선순위
# 산술 > 관계 > 논리
# 산술 연산자 우선순위는 * / % > + -
print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 3 + 12 > 7 + 3 and 5 < 10)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)
print()

# 복수의 조건이 모두 참일 때
score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('Welcome admin')
if id2 == 'admin' and grade == 'platinum':
    print('Welcome platinum admin')
print()

# 다중 조건문
num = 90
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('Grade : D')
print()

# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100 %')
    elif total >= 80:
        print('장학금 80 %')
    else:
        print('장학금 X')
print()

# in, not in
q = [10, 20, 30, 40, 50]
w = [70, 80, 90, 100]
e = {'name': 'Lee', 'city': 'Seoul', 'Grade': 'A'}
r = (10, 12, 14, 16, 18)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values())