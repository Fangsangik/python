"""
프로그래머가 이름을 통해서 정의 후 필요할 때마다 호출
반복되는 코드를 한번 구현 후, 재사용 가능한 코드의 집합
함수 구현 -> 재사용 가능, 루틴(프로시저, 서브루틴)

종류
1. 매개변수가 필요한 함수
2. 매개변수가 필요 없는 함수
3. 결과값을 반환하는 함수 (return)
4. 결과값을 반환하지 않는 함수 (return 없음)

"""
# 예제 1. 매개변수가 필요하지 않은 함수 (return 없음)
def function1():
    print('Hello, World!')

# 예제 2. 매개변수가 필요한 함수 결과값을 리턴하지 않는 함수
def function2(a, b):
    print('Hello,', a, b)

def function3(x, y):
    print('Sum:', x + y)

# 예제 3. 결과값 반환 하는 함수
# return이 있기 때문에 변수로 받을 수 있음
def function4(x, y):
    return x + y

# 실행
function1()
function2('Python', 'World!')
function3(100, 200)
result = function4(100, 200)
print('Result of function4:', result)
