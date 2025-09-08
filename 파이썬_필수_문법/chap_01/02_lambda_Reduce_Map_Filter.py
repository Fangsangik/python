"""
sequence형 데이터
lambda, map, filter, reduce

lambda : 익명, heqp 영역 사용, 즉시 소멸, pythonic, 파이썬 가비지 컬랙션
일반 함수 : 재사용성 위해 메모리 저장
스퀀스형 전처리에 : Reduce, Map, Filter  (call을 할때 메모리에 남김)
"""


# ex1
# lambda
def add(x, y, z):
    return x + y + z


print(add(10, 20, 30))

# 함수를 변수에 저장 할 수 도 있고,
# 함수를 인자로 받는 형태에 즉시 실행도 가능
print((lambda x, y, z: x + y + z)(10, 20, 30))

# ex2
# map(funcm iter1, iter2, ...)
# 각각 리스트에 있는 모든 원소드를, iterable 하게 객체로 넘겨줌 (내부적으로 next)
# list를 순회하면서 어떤 결과값을 도출 하겠다. -> map
digits1 = [x * 10 for x in range(1, 10)]
print(digits1)

result1 = map(lambda i: i ** 2, digits1)
result2 = list(map(lambda i: i ** 2, digits1))
print(result1)  # <map object at 0x10419fa90>
print(result2)  # list로 형변환


def also_square(i):
    def double(x):
        return x ** 2

    return map(double, i)


print(list(also_square(digits1)))

# ex3
# filter(func, iterable) -> 원하는 값만 뽑아내겠다.
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = filter(lambda x: x % 2 == 0, digits2) # TRUE인 값만 나온다.
print(list(result3))  # [2, 4, 6, 8, 10]

def also_even(i):
    def is_even(x):
        return x % 2 == 0
    # 실행 함수의 필터
    return filter(is_even, i)
print(list(also_even(digits2)))  # [2, 4, 6, 8, 10]

# ex4
# reduce(func, seq) -> 순회 가능한 누적으로 합계
# 내장 함수로 빠짐
from functools import reduce
digits3 = [x for x in range(1, 101)]
result4 = reduce(lambda x, y : x + y, digits3)
print(result4)  # 5050

def also_sum(i) :
    def add(x, y) :
        return x + y
    return reduce(add, i)
print(also_sum(digits3))  # 5050