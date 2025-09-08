"""
Variable Scope, global, nonlocal, locals, globals

- Variable Scope
    - 전역 변수 (global variable) : 변하지 않는 고정 값으로 사용 (모듈 전체에서 접근 가능)
    - 지역 변수 (local variable) : 함수 내에서만 접근 가능 (함수 호출시 생성, 함수 종료시 소멸)

- global 예약어 : 전역 변수 읽기, 수정 가능
- nonlocal 예약어 : 지역 변수 안에 하위에 지역 scope가 있을때 상위 지역 변수를 수정
- locals() : 현재 지역 변수 확인
- globals() : 현재 전역 변수 확인
"""

# ex1
a = 10  # 전역 변수 (global variable)
def func1():
    # 지역 scope (local scope)
    print(a)  # 전역 변수 a에 접근 가능
func1()  # 10 출력

# Read global variable
print(a)  # 10 출력

# ex2
b = 20
# 파이썬은 영역에서 변수를 찾을때 scope에서 우선 찾고 없으면 상위에서 찾는다
def func2():
    b = 30  # 지역 변수 (local variable)
    print(b)  # 지역 변수 b에 접근
func2()  # 30 출력

# ex3
# 지역에서는 어떤 특정한 예약어 없이 수정 가능
c = 40
def func3():
    # c = c + 10
    print(c)
# func3()  # UnboundLocalError: local variable 'c' referenced before assignment

# ex4
# global 예약어 사용
d = 50
def func4():
    global d  # global로 선언이 되어 있으면 전역 함수를 -> 읽기, 수정 가능
    d = d + 10  # 전역 변수 d 수정
    print(d)
func4()  # 60 출력

# ex5
# closure, decorator
def outer() :
    # 함수 영역에 있는 scope에 있는 변수를 기억 해놓음 (closure)
    e = 70

    def inner():
        nonlocal e # 지역 변수 안에 하위에 지역 scope가 있을때 상위 지역 변수를 수정 -> nonlocal 예약어 사용
        e += 10
        print(e)
    return inner
inner_func = outer() # closure
# UnboundLocalError: local variable 'e' referenced before assignment (nonlocal 없을때)
inner_func()

# ex6
# 파이썬의 지역 scope와 전역 scope를 갖고 있는지 확인
def func5(var) :
    x = 10
    # var => 지역 변수가 됨
    def printer() :
        print('ex6' , 'printer inner function')
    print('locals', locals())
func5("test")

# ex7
# globals() : 전역 변수 확인
# 선연한 모든 지역 변수 확인 가능
print('globals', globals())

# ex8 (지역 -> 전역 변수 만들기)
for i in range(1, 5):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k
print(globals())
print(plus_3_7)# 10
print(plus_4_9)# 13
