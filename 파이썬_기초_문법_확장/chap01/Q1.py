"""```다음 중 변수로 사용할 수 없는 이름은 무엇일까요? 생각해보세요.(실행까지 해보세요.)```"""
from 파이썬_기초_문법.chap7.function_1 import result

a = 15
_b = 3.14
#2c = int(77)
_7d = float(5.14)
"""
# 영문 문자와 숫자를 사용 가능
# 대소문자를 구분
# 문자부터 시작, 숫자는 불가
# _(언더스코어)가능, 
# 특수문자(+, _, *, /, $, @, &, %)불가
이중 밑줄(__)로 시작하는 이름은 파이썬에서 특별한 용도로 사용.
"""

"""`아래 파이썬 코드의 결과 값을` **`True or False`**  `값을 예상하고 아래 코딩영역에 작성하세요.`

```python"""
x = 15
y = 25

print(f'x == y : {x == y}') # False
print(f'x is y : {x is y}') # False

print(f'x value, id : {x}, {hex(id(x))}')
print(f'y value, id : {y}, {hex(id(y))}')
print()


"""
is의 경우 참조, 객체(same object, 오브젝트)비교
"""

"""`아래 파이썬 코드의 결과 값을` **`True or False`**  `값을 예상하고 아래 코딩영역에 작성하세요.`

```python"""
x = ['orange', 'banana', 'apple']
y = x

print(f'x == y : {x == y}') # True
print(f'x is y : {x is y}') # True

print(f'x value, id : {x}, {hex(id(x))}')
print(f'y value, id : {y}, {hex(id(y))}')
print()


"""`아래 파이썬 코드의 결과 값을` **`True or False`**  `값을 예상하고 아래 코딩영역에 작성하세요.`

```python"""
x = ['orange', 'banana', 'apple']
y = ['orange', 'banana', 'apple']

print(f'x == y : {x == y}') # True
print(f'x is y : {x is y}') # False -> 주소값이 다름
print()

"""
# is , not is -> 참조, 객체(same object, 오브젝트)비교 
# == , != -> 값 비교
# 값, 참조가 같은 비교는 is 사용(중요)
"""

"""`아래 파이썬 코드가 왜` **`에러(예외)`**  `가 발생하는지 생각해보고` **`동작하도록 수정`** `후 코딩영역에 작성하세요.`

```python"""
x = "Seoul"
y = 25
y = str(y)
z = x + y

print(f'x + y : {z}')
print()
"""
# 기존에 타입이 맞지 않아서 에러 발생
# 문자열 <-> 정수 연산은 형변환(Type Casting)이 필요
# Calling a non-callable 인 경우 
# 리스트 인덱스 타입 에러인 경우
# 기타 타입 에러
"""


"""`아래 리스트(List)에서` **`index 함수`** `를 포함한 다양한 방법으로` **`"Banana"`** `를 인덱싱(추출) 해보세요.` `출력 결과와 같아야 되요.`"""

# 직접 접근, index함수 사용 가능
x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']
print(x[4])
print(x[-2])
print('Banana' in x) # 포함 여부 확인
print(x.index('Banana')) # 인덱스 위치 반환
print(x[x.index('Banana')]) # 인덱스 값 반환
print(x[x.index('Banana', 4, len(x))]) # 인덱스 시작점 부터 끝까지

for i in x :
    if i == 'Banana' :
        print(i)
# 출력 결과 : Banana
print()

"""
# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# List 관련 함수는 중요!
# cmp, len, max, min, list, append, count, extend, index, insert, pop, remove, reverse, sort..
# index 함수 대소문자 구분
# sort, sorted 함수 차이도 중요
"""


"""`아래 리스트(List)에서` **`슬라이싱을 사용`** `해서` **`[e,f,g]`** `값을 출력해보세요. 다양한 슬라이싱 방법으로 시도해보세요.`"""

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
print(x[4 : 7])
print(x[-9 : -6])
print(x[-9 : 7])
print(x[-9: -6 : 1]) # step을 1씩 증가
print(list(reversed(x[6 : 3 : -1]))) # step을 -1씩 감소
for i in range(4, 7) :
    print(x[i], end=' ')
print()
print()

"""`아래 리스트(List)에서` **`apple, kiwi`** `를 추출해서` **`대문자`** `리스트로 출력하세요.` **`가능한 다양한`** `방법으로 코딩해보세요.`"""
# 출력 결과 : [APPLE, KIWI]
x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]

print([x[4].upper(), x[9].upper()])
print(list(map(str.upper, [x[4], x[9]])))

# 방법 1
ex1 = []
for i in range(len(x)) :
    if x[i] == 'apple' or x[i] == 'kiwi':
       ex1.append(x[i].upper())
print(ex1)

# 방법 2
ex2 = list(map(lambda b : b.upper(), filter(lambda a : a == 'apple' or a == 'kiwi', x)))
print(ex2)

# 방법 3
ex3 = [a.upper() for a in x
       if a == 'apple' or a == 'kiwi']
print(ex3)
print()

"""
`다음과 같이` **`30 ~ -10`** `까지` **`-2씩 감소한 결과를`** `리스트로 출력하세요.`
출력 결과 : [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]
"""

# range 함수(내장) : 주어진 범위 사이의 숫자형 시퀀스 반환
# loop 관점에서 핵심적인 함수(주로 for, while 함께 사용)
# range(stop) takes one argument.
# range(start, stop) takes two arguments.
# range(start, stop, step) takes three arguments.

x = []
for i in range(30, -12, -2) :
    x.append(i)
print(x)

x = list(filter(lambda a : a % 2 == 0, range(30, -12, -2)))
print(x)
print()



"""
`아래와 같이` **`1부터 20`** `까지` **`홀수 * 10, 짝수는 그대로`** `리스트로 출력하세요.`
출력 결과 : [10, 2, 30, 4, 50, 6, 70, 8, 90, 10, 110, 12, 130, 14, 150, 16, 170, 18, 190, 20]
"""

x = []
for i in range(1, 21) :
    if i % 2 == 0 :
        x.append(i)
    else :
        x.append(i * 10)
print(x)
print()

print([[j for j in range(5)] for i in range(5)]) # 2중 리스트 컴프리헨션
"""
j가 0부터 4까지 돌면서 리스트를 만든다.
즉, 결과는 항상 [0, 1, 2, 3, 4].
i가 0부터 4까지 총 5번 반복하면서,
안쪽 리스트 [0, 1, 2, 3, 4]를 그대로 넣는다.
"""

"""
`아래와 같이` **`1부터 15`** `까지` **`원소 * 10`** `결과는` **`문자열`** `리스트로 출력하세요.`  **`range, map, lambda 사용`**
출력 결과 : ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150"]
"""

x = []
for i in range(1, 16) :
    x.append(str(i * 10))
print(str(x))
print()

x = list(map(lambda a : str(a * 10), range(1, 16)))
print(x)

print(str(x * 10) for x in range(1, 16))
print()
# 람다함수 : 인라인 작성으로 인해 가독성 증가(함수 표현식 내용이 적을 때 람다 사용 권장)
#            함수 객체 반환 -> 함수 객체 인수로 받는 map, filter 등과 연계 사용
# lambda : https://www.w3schools.com/python/python_lambda.asp
# map : https://www.geeksforgeeks.org/python-map-function/

"""
`아래와 리스트에서` **`중복`** `되는` **`원소`** `를` `제거 후 출력하세요.`  **`다양한 방법`** `코딩하세요.`
출력 결과 : [1, 2, 3, 4, 5, 'a', 'b']

# Set(집합 자료형) : 중복 허용 하지 않음, 순서 없음
# List, Tuple : 순서 있음, 중복 허용
# OrderedDict : Dict 순서 보장 받을 수 있음(python 3.6 부터는 기본값)
"""

x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]
print(list(set(x)))

num = []
chars = []

from collections import OrderedDict
ex2 = list(OrderedDict.fromkeys(x))
print(ex2)

print([j for idx, j in enumerate(x) if j not in x[:idx]])

ex3 = []
for i in x :
    if i not in ex3:
        ex3.append(i)
print(ex3)

while x :
    element = x.pop(0)
    if isinstance(element, int) and element not in num:
        num.append(element)
    if isinstance(element, str) and element not in chars:
        chars.append(element)
result = num + chars
print(result)
print()


"""
`아래와 같은 Dict 구조에서` **`모든 value`** `값의` **`합(Sum)`** `을 구하세요.` **`*가능한 모든 방법*`** `으로 코딩하세요.` 
출력 결과 : 2327

# Dict : Key와 value의 대응관계를 갖는 자료형(해시테이블, 가변적-수정가능)

# 자주 사용하는 함수 : get(), values(), keys() 

# 다양한 Dict 선언 방법에 대해서 알아둬야 해요!
# 빈 딕셔너리
"""
d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

print(sum(d.values()))
print(sum(d[item] for item in d))

total = 0
for i in d.values():
    total += i
print(total)
print()

"""
`아래와 같이` **`Dictionary`** `에` **`{'c': 'banana', 'd': 'kiwi'}`** `를` **`추가하세요.`**  **`*가능한 방법 모두`** `구현`
d = {'a': 'apple', 'b': 'grape'}
출력 결과 : {'a': 'apple', 'b': 'grape', 'c': 'banana', 'd': 'kiwi'}
```"""

d = {'a': 'apple', 'b': 'grape'}
d.update({'c': 'banana', 'd': 'kiwi'})
print(d)

d['c'] = 'banana'
d['d'] = 'kiwi'
print(d)
print()


"""
`아래와 같은` **`딕셔너리`** `구조에서` **`Value 값이 25 이상`** `필터링 후 출력하세요.` **`다양한 방법`** `으로 코딩하세요.`

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}
출력 결과 : {'b': 33, 'd': 26, 'f': 120}
```
"""
d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

ex1 = {}
for k, v in d.items():
    if v >= 25 :
        ex1[k] = v
print(ex1)

print({k : v for k, v in d.items() if v >= 25})
print(dict((k, v) for k, v in d.items() if v >= 25))
print(dict(filter
           (lambda v : v[1] >= 25, d.items()))) # lambda v : v[1] >= 25 -> V[0} : key, v[1] : value
print()

"""
`아래와 같이` **`코드를 작성 후 `** `실행하세요.` **`json 형식`** `을 구조에 맞게(예쁘게) ` **`출력하세요.(pprint)`**

# pprint : Python 데이터 구조를 예쁘게 인쇄할 때 사용하는 기능 제공
# depth(중첩 데이터), indent(들여쓰기), width(줄 길이 조정), sort_dicts(키 정렬), stream(파일에 출력) 옵션 제공
# 참고 : https://docs.python.org/3/library/pprint.html
"""

import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url, timeout=10)  # SSL 검증 자동 처리 (certifi 사용)
r.raise_for_status()

data = r.json()

print(data)        # 기본 출력
print()
pprint(data, depth=3, indent=4, width=200)       # 보기 좋은 출력
print()

"""
`아래와 같은 ` **`딕셔너리(Dict)`** `를` **`출력 결과`** `와 같이` **`완성 하세요.`** **`(반복문 사용)`**

key 'one' has values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> total : 10
key 'two' has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] -> total : 12
key 'three' has values [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] -> total : 14

# Iterator : 순서대로 다음에 값을 반환(리턴)할 수 있는 객체 또는 상태(자체적으로 next 메소드 내장)
#            반복가능한 객체, 순회하면서 처리
# dict 구조의 items(), keys(), get() 함수를 기억해야 되요.
# https://www.w3schools.com/python/python_ref_dictionary.asp
"""
print()

# Dict 선언
d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 37)))

for j, k in d.items() :
    print(f"key '{j}' has values {k} -> total : {len(k)}")
print()

"""
`아래와 같이 ** `N` ** `까지` ** `합(Sigma)` ** `을 구하는 공식을` ** `함수` ** `형태로 작성 후 출력하세요.

입력: 10

출력
결과: 55
"""

total = 0
for i in range (1, 11):
    total += i
print(f'결과: {total}')

def result1(n) :
    total1 = 0
    for i in range(1, n + 1):
        total1 += i
    return  total1
print(f'결과: {result1(10)}')

def result2(n) :
    return n * (n + 1) // 2
print(f'결과: {result2(10)}')
print()


"""
`아래` **`함수가 실행 시 에러가 발생하는 이유`** `를 생각해보세요.` **`함수 수정 후`** `정상적으로 실행해보세요.`

# 파이썬 함수 인자 실행 순서는 중요해요.
# 함수 정의시 가변인자, 기본값 등을 사용하면 활용도와 가독성이 높게 작성할 수 있어요.
# 참고 : https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29
"""

# 함수 선언
def greet(name, msg="Good morning!"):
    return "Hi! " + name + ', ' + msg

# 실행
print(greet("Kim"))
print(greet("Park", "How do u do?"))
print("-------")

def add1 (a, b=10, c=20):
    print(a, b, c)
    return a + b + c

print(add1(5))
print(add1(5, 7))
print(add1(5, 7, 9))

def add2 (*d):
    # *d는 "들어오는 인자들을 전부 tuple로 묶어라"
    tot = 0
    for i in d :
        tot += i
    return tot
print(add2(10, 20))
print()

"""
-> 모든 인자 default 값 있는 경우 / 없는 경우 / default 값 인자가 뒤로 
"""


"""
`아래` **`함수가 실행 시 에러가 발생하는 이유`** `를 생각해보세요.` **`함수 수정 후`** `정상적으로 실행해보세요.`  **`결과값 : 1000`**

# 변수 영역에 대한 이해 부족 시 잘못된 결과값, 프로그램 종료 등 문제가 발생할 수 있어요.
# 전역 변수 : 함수 내부가 아닌 외부에 정의되어 전체 범위를 갖는 변수(프로그램 영역 전체, 함수 내부 엑세스 가능)
# 전역 변수의 변경, 수정(출력, 엑세스 X)이 필요한 경우는 global 키워드 사용
"""
# 전역변수
x1 = 100 # 전체 범위 cover

def test():
    x = x1 * 10 # 지역변수
    return x
print(test())

def test1():
    return x1 * 10
print(test1())

y = 100
def test3():
    global y
    y = y * 10
    return y
print(test3())
print()

"""
`아래` **`함수 실행 후`** **`step1, step2, step3`** `결과를` **`예측`** `해보세요.`
# 변수 영역에 대한 이해 부족 시 잘못된 결과값, 프로그램 종료 등 문제가 발생할 수 있어요.
# 지역 변수 : 함수 내부에 정의되어 해당 함수 내에서만 유효한 변수(함수 내부에서만 엑세스 가능)
# 전역 변수 : 함수 내부가 아닌 외부에 정의되어 전체 범위를 갖는 변수(프로그램 영역 전체, 함수 내부 엑세스 가능)
# 전역 변수의 변경, 수정(출력, 엑세스 X)이 필요한 경우는 global 키워드 사용
"""
a = 20

def test():
    # 지역변수
    a = 35
    return a

print('step1 : ', a) # 20

a = 100

print('step2 : ', a) # 100
print('step3 : ', test()) # 35
print()

a = 20
def test1():
    global a # global 키워드로 전역변수 a를 사용 (2)
    print("step1 ", a) # 100으로 변경 되어 있기 때문에 100으로 나옴

    a = 35 # (3)
    return a
print(a)

a = 100 # 전역변수 재할당 (1)
print("step2 ",a)
print("step3 ", test1())
print()

"""
`아래` **`함수 실행 후`** **`Step1, Step2 -> a, b, x, y`** `결과를` **`예측`** `해보세요.`
"""

def test(x, y):
    global a
    a = 49 # 8 -> 49
    x,y = y,x
    b = 53
    b = 7
    a = 135 # 49 -> 135
    # 예상1
    print('Step1 : ', a, b, x, y) # a = 135, b = 7, 7, 23

a, b, x, y = 8, 13, 33, 44 # (1)

# 함수 실행
test(23, 7)

# 예상2
print('Step2 : ', a, b, x, y) # a = 49, b = 13, x = 33, y = 44
print()

"""
`아래와 같은` **`문장을 공백`** `으로` **`구분 후`** `단어 개수를 출력하는` **`함수`** `를 작성 후 실행하세요.` **`input 함수 가능`**
출력 결과 : 10
"""
in_str = "Suppose we have few words that are separated by spaces."

def word_count(s) :
    return len(s.split())
print(word_count(in_str))
