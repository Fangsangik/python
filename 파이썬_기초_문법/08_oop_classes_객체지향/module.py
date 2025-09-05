"""
파이썬 모듈
Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
"""


def add(x, y):
    """두 수를 더하는 함수"""
    return x + y

def subtract(x, y):
    """두 수를 빼는 함수"""
    return x - y

def multiply(x, y):
    """두 수를 곱하는 함수"""
    return x * y

def divide(x, y):
    """두 수를 나누는 함수"""
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y

def power(x, y):
    """x의 y제곱을 계산하는 함수"""
    return x ** y


# print('-' * 15)
# print('called inner')
# print(add(5, 5))
# print(subtract(10, 5))
# print(multiply(2, 3))
# print(divide(10, 2))
# print(power(2, 3))
# print('-' * 15)

# __name__
# main은 실행 되는 대상
# main이 아니라면 실행이 되지 않는다. 
if __name__ == '__main__':
    print('-' * 15)
    print('called __main__')
    print(add(5, 5))
    print(subtract(10, 5))
    print(multiply(2, 3))
    print(divide(10, 2))
    print(power(2, 3))
    print('-' * 15)
