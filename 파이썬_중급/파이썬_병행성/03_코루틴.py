"""
코루틴 (Coroutine) : 단일(싱글) 쓰레드, stack을 기반으로 동작하는 비동기 작업
yield, send : 통해서 main <-> sub 상호작용
Thread : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 쓰레드
코루틴을 제어 할때 yield를 통해서 제어 / 양방향 전송
subRoutine -> Main Routine 호출 -> subRoutine에서 수행 (흐름 제어)
Coroutine : Routine 실행 중 중지 -> 동시성 프로그래밍
Coroutine : Thread에 비해 오버헤드 감소
Thread : 싱글 쓰레드 -> 멀티 쓰레드 -> 복잡 -> 공유되는 자원 -> 교착상태 발생 가능성 -> Context Switching 비용 큼, 자원 소비 발생 가능성
def : async, yield : await
"""

# Coroutine
def coroutine_ex1():
    print(">>> coroutine started.")
    print("--- subroutine ---")
    # i에서 yield 할당 / yield가 들어 가면 generator / coroutune은 generator에서 파생 되었다고 볼 수도 있다.
    i = yield
    print(">>> coroutine received : {}".format(i))

# 제너레이터 선언
"""
코루틴: 실행하다가 yield에서 멈춤 → 원할 때 다시 이어서 실행 가능.
중간에 "멈췄다가 다시 시작"할 수 있으니까 동시성 프로그래밍에 활용 가능.
"""
print("--- Main ---")
cr1 = coroutine_ex1()
print(cr1, type(cr1))
# yield 지점 까지 subroutine 수행
# next(cr1) # yield 지점까지 수행
next(cr1)

# >>> coroutine received : 100 -> (Main -> Sub)
# send라는 명령어로 인해 Main <-> Sub 상호작용
# 기본 전달 값 (값 전송)
# cr1.send(100)
print()

# 잘못된 사용
# cr2 = coroutine_ex1()
# 예외 발생 -> next(cr2)로 yield 지점까지 수행 후 send로 값 전달 / generator가 시작 단계에서 send로 전달 할 수 없음
# cr2.send(100)
# 코루틴은 처음엔 무조건 next()로 yield까지 가야 send()로 값을 보낼 수 있음.
# 즉, yield라는 "받는 지점"이 준비되기 전에 값을 던져서 에러

# coroutine_ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 종료 상태
def coroutine_ex2(x) :
    print(">>> coroutine started : {}".format(x))
    # x를 Main에서 받아서 출력 & y를 Main에서 받아서 출력 -> x를 sub -> Main
    # 왼쪽은 받는 부분, 오른쪽은 보내는 부분
    y = yield x
    print(">>> coroutine received : {}".format(y))
    z = yield x + y
    print(">>> coroutine received : {}".format(z))

cr3 = coroutine_ex2(10)

from inspect import getgeneratorstate # 제너레이터 상태 확인

# coroutine 상태 확인
print(getgeneratorstate(cr3)) # GEN_CREATED

print(next(cr3)) # y 값을 받을 대기
print(cr3.send(15)) # x + y 값을 보냄
#print(cr3.send(20)) # z 값을 보냄
print()

# coroutine_ex3
# StopIteration 예외 발생 자동 처리
# 중첩 coroutine 처리
def coroutine_ex3(x) :
    # A, B return -> 두번 바등ㅁ
    for i in 'AB' :
        yield x
    # A -> 1, 2 / B -> 1, 2
    for y in range(1, 3) :
        yield y

t1 = coroutine_ex3(10)
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
#print(next(t1))

t2 = coroutine_ex3(20)
print(list(t2))  # list
print()

# yield from
def coroutine_ex4 ():
    # yield from -> iterable한 generator를 순차적으로 끝날때 까지 반환
    # yield from coroutine_ex3(x)
    # for v in coroutine_ex3(x) :
    #     yield v
    yield from 'AB'
    yield from range(1, 3)

t3 = coroutine_ex4()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
