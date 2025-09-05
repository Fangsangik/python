"""
람다
장점 : 메모리 절역, 가독성, 코드 간결 해진다
함수는 객체 생성 -> 리소스(메모리) 할당
람다는 즉시 실행 함수(HEAP 초기화) -> 메모리 초기화 (효율적으로 메모리를 사용)
단점 : 가독성이 떨어진다, 디버깅이 어렵다, 재사용성이 떨어진다
"""


# 일반 함수 vs 람다 함수
# 일반 함수
# 일반 함수의 경우 객체가 생성이 되고, 메모리 할당이 된다.
def mul_func(x, y):
    return x * y


result = mul_func(10, 50)
print(result)

# 람다함수
# 람다 함수의 경우 즉시 실행 함수로 메모리 할당이 되지 않는다.
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))


# 일시적으로 즉시 값이 나와야 할때 람다 함수 사용
# 함수 안에서 함수를 인자로 받을때는 람다로 받아도 되고, 이미 변수로 할당한 값을 넣어도 됨
def func_final(x, y, func):
    print(x * y * func(100, 200))
func_final(10, 20, lambda_mul_func)
