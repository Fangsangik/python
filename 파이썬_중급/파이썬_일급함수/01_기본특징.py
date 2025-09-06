"""
일급 함수 (First-Class Function) 란?
함수를 숫자나 문자열 같은 일반 값(value)처럼 다룰 수 있다는 의미
순수 함수를 지향 & 기존 기능을 개선하기도 쉬움
동시에 여러 스레드에서 작업 할 수 있음

파이썬 함수 특징
1. Runtime 초기화
2. 함수를 변수에 할당
3. 함수의 인수 전달 가능
4. 함수 결과 반환 가능 (return)
"""
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    """재귀 함수로 구현한 팩토리얼"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

class A :
    pass

print(factorial(5))
# 일급 객체 => 함수로 처리
print(type(factorial), type(A))  # <class 'function'> <class 'type'>
print(dir(factorial)) # 함수 -> __repr__, __init__, __call__ ...
# 함수 안에 갖고 있는 성질들만 확인
print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수만의 고유한 속성 확인
print(factorial.__name__) # factorial
print(factorial.__code__) # 파일 위치와, 코드 내용

# 변수 할당 가능
var_func = factorial
print(var_func) # <function factorial at 0x0000020C8F1B3EE0>
print(var_func(10)) # 3628800
print(list(map(var_func, range(1, 10)))) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 함수 인수 전달 및 함수로 결과 반환 (고위 함수 - Higher Order Function)
# map, filter, reduce
# 함수를 결과값으로 반환
print([var_func(i) for i in range(1, 10) if i % 2])

# map
print(list(map(var_func, filter(lambda x: x % 2, range(1, 10)))))

# reduce
from functools import reduce
from operator import add
print(sum(range(1, 10)))
# 감소 시키면서 합을 구함 (누적 합)
print(reduce(add, range(1, 10))) # 누적 합

# 익명함수 (lambda)
# 가급적 주석이나, 함수로 구현하는 것을 권장
# 일반 함수 형태로 refactoring
# add == lambda x, y: x + y
print(reduce(lambda x, t: x + t, range(1, 10))) # 누적 합

# callable (메서드 형태로 호출 가능 함수)
# 호출 가능 확인
# 상수 자체로는 호출 불가능
print(callable(str), callable(list), callable(var_func), callable(3.14), callable(factorial))

# partial 사용법 : 인수 고정 -> callback 함수로 사용
from operator import mul
from functools import partial

print(mul(10, 10)) # 100

# 인수 고정 (한쪽 값 고정)
# 함수로 인자 전달 가능, 변수 할당
# 고정 해놓고 호출만 하면 됨 -> partial
ten = partial(mul, 10)
print(ten(10)) # 100

# 고정 추가
six = partial(ten, 6)
print(six())
print([ten(i) for i in range(1, 10)]) # [6, 12, 18, 24, 30, 36, 42, 48, 54]
print(list(map(ten, range(1, 10)))) # [10, 20, 30, 40, 50, 60, 70, 80, 90]