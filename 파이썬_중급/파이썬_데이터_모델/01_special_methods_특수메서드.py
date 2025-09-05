"""
Special Methods in Python
파이썬 핵심 -> sequence, iterator, function, class... etc

클래스 안에 정의 할 수 있는 특별한(Built_in) 메서드들
"""

# 기본형
print(int)
print(float)

# 모든 속성 및 메서드 설계
print(dir(int))
print(dir(float))

n = 10
print(type(n))

# n.__add__ 더하기
print(n + 100) # Wrapping 된 상태
print(n.__add__(100)) # 내부적으로 호출되는 메서드

# n.__doc__  Docstring 출력
print(n.__bool__(), bool(n)) # True
# n.__mul__  곱셈
print(n * 100, n.__mul__(100)) # 1000
print()

