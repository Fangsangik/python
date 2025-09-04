"""
숫자형 사용법
파이썬 모든 자료형
데이터 타입 선언
연산자 활용
형변환
외부 모둘 사용법
"""

# 숫자형
"""
int, float, complex(복소수), bool(참과 거짓), str(문자열 = 시퀀스), list(리스트 = 시퀀스), tuple(튜플 = 시퀀스), set(집합), dict(딕셔너리)
"""
# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0
int1 = 7
list1 = [str1, str2]
# Key Value 쌍으로 이루어진 딕셔너리
dict1 = {'name': 'Machine Learning', 'version': 3.0}
tuple1 = (7, 8, 9)
set1 = {1, 2, 3}

# 데이터 타입 출력
print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict1))
print(type(tuple1))
print(type(set1))
print()

# 슷자형 연산자
"""
+, - * , /, //, %, abs(x), pow(x, y) -> x의 y제곱 = x ** y
"""

# 정수
i = 77
i2 = -14
big_int = 777777777777999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수
f = 0.9999999999
f2 = 3.141592
f3 = -2.718281828459045
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산
i1 = 39
i2 = 939
big_inti = 77777777777777779979797997979
big_inti2 = 99999999999999999999999999999
f1 = 1.234
f2 = 3.999

print(i1 + i2) # 덧셈
print(big_inti + big_inti2) # 큰 정수 덧셈
print(f1 + f2) # 실수 덧셈
print()

print(i1 - i2) # 뺄셈
print(big_inti - big_inti2) # 큰 정수 뺄셈
print(f1 - f2) # 실수 뺄셈
print()

print(i1 * i2) # 곱셈
print(f1 * f2) # 실수 곱셈
#print(big_inti * big_inti2) # 큰 정수 곱셈
print()

print(i1 / i2) # 나눗셈
print(f1 / f2) # 실수 나눗셈
print(big_inti / big_inti2) # 큰 정수 나눗셈
print()

print(i1 // i2) # 몫
print(f1 // f2) # 실수 몫
print(big_inti // big_inti2) # 큰 정수 몫
print()

print(i1 % i2) # 나머지
print(f1 % f2) # 실수 나머지
print(big_inti % big_inti2) # 큰 정수 나머지
print()

print(i1 ** i2) # 거듭제곱
print(f1 ** f2) # 실수 거듭제곱
#print(big_inti ** big_inti2) # 큰 정수 거듭제곱
print()

# 형변환
a = 3.
b = 6
c = .7
d = 12.7
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True -> 1
print(float(False)) # False -> 0.0 (실수형)
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))
print()

# 수치 연산 함수
print(abs(-100)) # 절대값
x, y= divmod(100, 8) # 몫과 나머지
print(x, y) # 몫과 나머지
print(pow(2, 3)) # 거듭제곱
print(2 **3)
print()

# 외부 모듈 사용
import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수에서 가장 작은 정수 