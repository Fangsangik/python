"""
Closure -> Decorator
1. 클로저
2. 함수를 일급 인자로 활용
3. 가변 인자
4. 인자 풀기
5. 파이썬이 소스코드를 불러오는 자세한 과정

데코레이터 장점
1. 중복 제거, 코드 간결, 공통 함수 작성
2. 로깅, 프레임워크, 유요성 체크 -> 공통 함수 기능
3. 조합해서 사용 가능

데코레이터 단점
1. 가독성 떨어짐
2. 디버깅 어려움
3. 특정 어떤 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
"""

# 데코레이터 (Decorator)
import time


# 클로저는 외부 함수의 지역 변수(혹은 매개변수) 를 내부 함수가 참조하고 있을 때 형성
# func는 perf_clock의 매개변수인데, perf_clocked 안에서 참조되고 있으므로 자유 변수(free variable) 가 됨
# perf_clocked는 클로저 함수가 되고, func는 그 클로저가 캡처(capture)한 변수
def perf_clock(func):  # 외부 함수
    def perf_clocked(*args):  # 내부함수

        # 함수 시작 시간
        start_time = time.perf_counter()

        # 함수 실행
        # 부모에서 넘어온 func -> 자유변수로서 사용 가능
        result = func(*args)

        # 함수 종료 시간
        end_time = time.perf_counter() - start_time

        # 함수명
        name = func.__name__

        # 함수 매개 변수
        arg_str = ','.join(repr(arg) for arg in args)

        print('[%0.5fs] %s(%s) -> %r' % (end_time, name, arg_str, result))
        return result

    return perf_clocked


# 서로 다른 함수가 많더라도 decorator 하나로 모두 적용 가능
@perf_clock # 데코레이터 적용
def time_func(seconds):
    time.sleep(seconds)

@perf_clock # 데코레이터 적용
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
# 외부 함수를 실행해야 내부 함수가 실행됨
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)

print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)
print('-' * 40, "called Non Decorator -> time func")
print(non_deco1)
print('-' * 40, "called Non Decorator -> sum func")
non_deco2(100, 200, 300)
print()

# 데코레이터 사용
print('-' * 40, "called Decorator -> time func")
print()
time_func(2)
print('-' * 40, "called Decorator -> sum func")
print()
sum_func(100, 200, 300)

