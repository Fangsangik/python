"""
파이썬 함수식 및 람다

함수의 정의 방법
def function_name(parameter1, parameter2, ...):
     code
"""

# 예제 1
def first_function(w):
    print("Hello", w)

word = "Python"
first_function(word)

# 예제 2
def return_function(w1):
    value = "bye, " + str(w1)
    return value
result = return_function("Python")
print(result)

# 예제 3 (다중 반환)
def func_mul(x):
    y1 = x * 2
    y2 = x * 3
    y3 = x * 4
    return y1, y2, y3
result1, result2, result3 = func_mul(3)
print(result1, result2, result3)

# 튜플 리턴
def func_mul_2(x):
    y1 = x * 2
    y2 = x * 3
    y3 = x * 4
    return (y1, y2, y3)
result = func_mul_2(3)
print(type(result), result, list(result))

# 리스트 리턴
def func_mul_3(x):
    y1 = x * 2
    y2 = x * 3
    y3 = x * 4
    return [y1, y2, y3]
result = func_mul_3(3)
print(type(result), result, set(result))

# 딕셔너리
def func_mul_3(x):
    y1 = x * 2
    y2 = x * 3
    y3 = x * 4
    return {'y1': y1, 'y2': y2, 'y3': y3}
result = func_mul_3(3)
print(type(result), result, result.keys(), result.values())

# *args **kwargs
# 언패킹
# *args
# * -> 튜플 형태 / ** -> 딕셔너리 형태
def args_func(*args):
    # 어떤 매개변수가 오더라도 풀어서 처리
    # 매개변수의 개수 만큼 해당 변수에도 값이 할당 되어야 하는 것이 맞음
    # unpacking -> 넘기는 것들을 묶어서 처리 -> 풀어서 처리 해줄께
    # 즉 하나의 튜플로 인식해서 처리
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-------')

args_func("Lee")
args_func("Lee", "Kim")
args_func("Lee", "Kim", "Park")

# **kwargs
def kwargs_func(**kwargs):
    # 매개변수의 이름과 값을 딕셔너리로 처리
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-------')
kwargs_func(name1 = "Lee")
kwargs_func(name1 = "Lee", name2 = "Kim")
kwargs_func(name1 = "Lee", name2 = "Kim", name3 = "Park" , sendSMS = True)

# 전체 혼합
def ex_func(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

ex_func(10, 20, 30, "Lee", "Kim", "Park", name1 = "Park", name2 = "Choi")
print()

# 함수의 중첩
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 10)

nested_func(100)