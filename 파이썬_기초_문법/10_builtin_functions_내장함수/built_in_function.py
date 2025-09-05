"""
파이썬 내장함수 : Built in
자주 사용 하는 함수
str(), int(), tuple() -> 형변환 이미 학습
"""

# 절대값
# abs() : 절대값을 반환하는 함수
print(abs(-10))  # 10

# all() : iterable 객체의 모든 요소가 참인지 확인 (and)
print(all([1, 2, 3]))  # True
print(all([1, 2, '']))  # false => 하나라도 빈 값이 있으면 false

# any() : iterable 객체의 요소 중 하나라도 참인지 확인 (or)
print(any([0, 1, 2]))  # True => 하나라도 참이면 True
print(any([0, '', None]))  # False => 모두 거짓이면 False

# chr : 아스키 -> 문자 / ord : 문자 -> 아스키
print(chr(65))  # 'A'
print(ord('A'))  # 65

# enumerate : index + iterable 객체 생성
for i, name in enumerate(['a', 'b', 'c']):
    print(i + 1, name)  # 0 a, 1 b, 2 c


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값을 추출
def conv_pos(x):
    return abs(x) > 2


# fiter 자체로 print 할 경우 주소값 나옴 / 원하는 값을 얻으려면 list로 변환
print(list(filter(conv_pos, [-1, 0, 1, 2, 3, 4])))
print(list(filter(lambda x: abs(x) > 2, [-1, 0, 1, 2, 3, 4])))  # 람다 함수로도 가능

# id : 객체의 고유한 주소값을 반환
print(id(int(1)))
print(id(4))

# len : 객체의 길이 반환 -> iterable 가능한 객체의 길이
print(len('hello'))  # 5
print(len([1, 2, 3, 4]))  # 4

# max / min : 최대값 / 최소값 반환 -> iterable 가능한 객체의 최대값 / 최소값
print(max([1, 2, 3, 4]))  # 4
print(max('hello'))  # 'o' => 알파벳 순서로 최대값
print(min([1, 2, 3, 4]))  # 1
print(min('hello'))  # 'e' => 알파벳 순서로 최소값


# map : iterable 객체의 요소를 지정한 함수 실행 후 추출
# filter는 걸러주지만 map은 변환해서 모든 값을 반환
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [-1, 0, 1, 2, 3, 4])))  # [1, 0, 1, 2, 3, 4]
print(list(map(lambda x: abs(x), [-1, 0, 1, 2, 3, 4])))  # [1, 0, 1, 2, 3, 4] 람다 함수로도 가능

# pow : 거듭제곱 계산
print(pow(2, 3))  # 8 => 2^3

# range : 지정한 범위의 숫자 생성
for i in range(5):
    print(i)  # 0 1 2 3 4

# round : 반올림
print(round(3.14159, 2))  # 3.14 => 소수점 둘째 자리까지 반올림
print(round(5.6))  # 6 => 소수점 첫째 자리까지 반올림

# sorted : 반복 가능한 객체 (iterable)
# 정렬된 리스트 반환 -> 기본적으로 오름차순 정렬
print(sorted([3, 1, 4, 2]))  # [1, 2, 3, 4] => 오름차순 정렬
a = sorted(['banana', 'apple', 'cherry'])
print(a)  # ['apple', 'banana', 'cherry'] => 알파벳 순서로 정렬

# sum : 반복 가능한 객체의 합을 반환
print(sum([6, 7, 8, 9]))  # 30 => 리스트의 합
print(sum(range(1, 101)))

# type : 객체의 타입을 반환
print(type(1))  # <class 'int'>
print(type('hello'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({'a': 1, 'b': 2}))  # <class 'dict'> => 딕셔너리 타입

# zip : 반복 가능한 객체를 묶어서 반환 -> 튜플로 묶음
print(list(zip([10, 20, 30], [20, 30, 40])))  # [(10, 'a'), (20, 'b'), (30, 'c')]
