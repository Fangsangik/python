"""
다양한 변수 선언
변수 할당 설명
Object Identity 설명
변수 네이밍 규칙
예약어
"""

# 기본선언
# n이 할당되어 있는 주소로 n의 할당 값을 확인 가능
n = 700
print(n * 700)
# n이 할당 되어 있는 자료형 확인
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75
# 재선언
var = 'change value'
# 마지막에 선언된 값이 새로운 값으로 대체
print(var)
print(type(var))
print()

# Object reference
# 변수의 값이 할당 상태 일때
# 1. 타입에 맞는 오브젝트 생성
# 2. 값을 생성
# 3. 콘솔 출력
# 예 1)
print(300)
print(int(300))
print()

# 예 2)
# n -> 777
n = 777
print(n , "=",  type(n))

# m -> 777
m = n
print(m , "=", type(m))

m = 400
print(m , "=", type(m))
print()

# id(identity) 객체의 고유 값
m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))  # False
print()

# 파이썬 입장에서는 같은 값을 여러번 생성 하는 것이 비효율적이라고 판단
# 그래서 같은 값을 할당할 때는 주소값을 공유한다.
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))  # True
print()

# 다양한 변수 선언
student1 = 'John'
student2 = 'Jane'

# CarmelCase : nuberOfStudents -> Method
# PascalCase : NumberOfStudents -> Class
# snake_case : number_of_students
# 특수문자 허용 X & 숫자로 시작 X / 단 _, $ 허용
# 예약어(Reserved Words) 사용 불가
# 허용하는 변수 선언 법
age = 1
Age = 2
AGE = 3
aGe = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8



