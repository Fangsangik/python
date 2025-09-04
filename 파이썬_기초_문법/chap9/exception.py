"""
예외 개념 처리
SyntaxError, NameError, TypeError, ValueError, IndexError, KeyError....
문법적으로는 예외는 없지만, 코드 실행 중에 발생하는 오류를 예외라고 한다.

1. 예외는 반드시 처리
2. 로그는 반드시 남김
3. 예외는 던져진다. -> 다른 곳으로 처리 위임
4. 예외 무시
"""

# SyntaxError -> 문법 오류
# print("SyntaxError 예시)
#print('error'))
# if True
#     print("SyntaxError 예시) 문법 오류가 발생합니다.")  # SyntaxError: invalid syntax

# NameError -> 참조 없음
a = 10
# print(b)  # NameError: name 'b' is not defined

# TypeError -> 타입 오류
# a = 10
# b = "20"
# print(a + b)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ZeroDivisionError -> 0으로 나누기
# a = 10
# b = 0
# print(a / b)  # ZeroDivisionError: division by zero

# IndexError -> 인덱스 범위 초과
my_list = [1, 2, 3]
# print(my_list[5])  # IndexError: list index out of range

# KeyError -> 딕셔너리 키 오류
# my_dict = {"a": 1, "b": 2}
# print(my_dict["c"])  # KeyError: 'c'

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외 처리 권장

# attributeError -> 모듈, 클래스에 있는 잘못된 송성 사용 예외
# import time
# print(time.time2())

# ValueError -> 값이 잘못된 경우
# x = [1, 2, 3]
# x.remove(1)
# print(x)
# x.remove(5)

# FileNotFoundError -> 파일이 없는 경우
# f = open("non_existent_file.txt", "r")  # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'

# typeError -> 자료형에 맞지 않는 연산을 수행
x = [1, 2, 3]
y = (4, 5, 6)
# print(x + y)  # TypeError: can only concatenate list (not "tuple") to list

# 예외 처리
# try -> 에러가 발생할 가능성이 있는 코드
# except -> 에러가 발생했을 때 처리하는 코드 / 여러개 가능
# except -> 에러명2
# else -> try 블록에서 에러가 발생하지 않았을 때 실행되는 코드

name = ["홍길동", "김철수", "이영희"]
try:
    z = '황상익'
    x = name.index(z)
    print('{} found it {} in name'.format(z, x + 1))
except ValueError as e:
    print('ValueError: {}'.format(e))
else:
    print('No error occurred, index found successfully.')
print()

try:
    z = '터진입'
    x = name.index(z)
    print('{} found it {} in name'.format(z, x + 1))
except Exception as e: # 모든 예외를 처리
    print('ValueError: {}'.format(e))
else:
    print('No error occurred, index found successfully.')
print()

try:
    z = '터진입'
    x = name.index(z)
    print('{} found it {} in name'.format(z, x + 1))
except Exception as e: # 모든 예외를 처리
    print('ValueError: {}'.format(e))
else:
    print('No error occurred, index found successfully.')
finally: # 예외 발생 여부와 상관없이 항상 실행되는 블록
    print('This block always executes, regardless of error.')
print()

# 예외 발생시키기
# raise 키워드 사용
try :
    a = '홍길동'
    if a == '홍길동':
        print("Hello, 홍!")
    else:
        raise ValueError
except ValueError:
    print("ValueError: 이름이 홍길동이 아닙니다. 예외가 발생했습니다.")
finally:
    print("OK PASS")