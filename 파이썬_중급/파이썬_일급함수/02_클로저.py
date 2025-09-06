"""
closer (클로저)
외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(access) 가능

# scope가 닫쳐도 함수가 실행이 끝나면, 변수의 값을 유지하는 것 (기억)
# 서버 프로그래밍에서 동시성 제어 (Concurrency Control) -> 메모리 공간에 여러 자원이 접근 / 교착 상태 (Dead Lock)
# dead lock 회피 하기 위해 메시지 전달로 처리하기 위한 -> Erlang, Elixir, Go
# 클로저는 공유는 하되, 변경되지 않는(immutable, readOnly)
# 콜로저는 불변자료 구조 및 atom, STM -> 멀티스레드 프로그래밍 강점 (Coroutine)
"""
# 파이썬 변수 범위
# ex1
def func_v1(a) :
    print(a)
    print(b)

# 외부에 선언 되어 있음 (global)
b = 20

# ex2
def func_v2(a) :
    print(a)
    print(b)

func_v2(10)

c = 30

# ex3
def func_v3(a) :
    global c # 전역 변수 참조
    print(a) # 10
    print(c) # 30
    c = 40 # 전역 변수 변경

print('c :', c) # 30
func_v3(10) # 10 30 / 내부 함수 실행 시작
print('c :', c) # 40
print()

# Closure (클로저)
a = 100
print(a + 100)
print(a + 1000)

# 누적
print(sum(range(1, 51))) # 1 ~ 50
print(sum(range(51, 101))) # 51 ~ 100

# 클래스 이용
# 값의 상태를 유지 (계속 누적)
class Averager ():
    def __init__(self):
        self.series = []

    def __call__(self, v):
        self.series.append(v)
        print('inner >>', self.series, len(self.series))
        return sum(self.series) / len(self.series)

# 인스턴스 생성
averager_cls = Averager()
print(dir(averager_cls))
print(averager_cls(10)) # 10.0
print(averager_cls(30)) # 20.0

# 클로저 (Closure) 구현
def closure_ex1 ():
    # free variable
    # 클로저 영역의 자유 영역은 -> 내가 사용하려고 하는 함수 바깥에 있는 변수
    # 클로저 영역 (임시)
    series = []

    def averager(v):
        # 원래대로 라면 series 함수 호출 된 후 소멸
        series.append(v)
        print('inner >>', series, len(series))
        return sum(series) / len(series)

    # 함수 결과 반환 가능 (함수 반환)
    return averager # 함수 반환

avg_closure1 = closure_ex1() # 클로저 영역에 있는 함수 반환
# 함수가 return -> closure_ex1.<locals>.averager
# 누적해서 값을 유지
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print()

# function inspection
print(dir(avg_closure1)) # __closure__
print(avg_closure1.__code__) # co_freevars
print(avg_closure1.__code__.co_freevars) # ('series',)
print(avg_closure1.__closure__[0].cell_contents) # [10, 30, 50]
print()

# 잘못된 closure 사용 예
# cnt, total => 외부 함수의 지역 변수
# averager 함수 안에서 cnt += 1 , total += v 문장 사용시, 파이썬은 그 변수를 지역변수로 재정의 시도
# cnt 가 아직 averager 내부에서 정의되지 않았으니 → "참조하려고 했는데 할당 전이다!" → UnboundLocalError 발생.
def closure_ex2 ():
    # free variable
    cnt = 0
    total = 0

    # UnboundLocalError: local variable 'cnt' referenced before assignment
    def averager(v):
        # cnt += 1  윗 부분을 참조 하지 못하고 있음
        # total += v
        return total / cnt

    return averager


def closure_ex3 ():
    # free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total # free 변수로 선언 -> 지역변수로 사용하지 않겠다.
        cnt += 1
        total += v
        return total / cnt

    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10))