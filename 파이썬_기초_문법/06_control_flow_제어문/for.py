"""
For 흐름 제어 실습
반복문 중요성
기본 For 사용
For문 패턴 실습
For-Else 사용
"""
from itertools import count

from prompt_toolkit.input.vt100 import raw_mode

# for in collection
#  <loop body>
for v1 in range(10) : # -> 0 to 9
    print('v1 is : ', v1)
print()

for v2 in range(1, 11) :
    print('v2 is : ', v2)
print()

for v3 in range(1, 11, 2) : # -> 1 to 10, 2개씩 증가
    print('v3 is : ', v3)
print()

# 1 ~ 1000
sum1 = 0
for v4 in range(1, 1001) :
    sum1 += v4
print('1 ~ 1000 sum is : ', sum1)
print('1 ~ 1000 sum :', sum(range(1, 1001))) # sum() 함수 사용
print(type(range(1, 11)))
print('1 ~ 1000 까지의 4의 배수의 합 :', sum(range(4, 1001, 4)))
print()

# iterables
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range(), reversed(), enumerate(), filter(), map(), zip()
names = ['Kim', 'Park', 'Lee', 'Choi', 'Jeong']
for name in names :
    print('U r name is : ', name)
print()

# Lotto
lotto_numbers = [1, 3, 5, 7, 9, 11]
for number in lotto_numbers :
    print('Lotto number is : ', number)
print()

word = "Beautiful"
for n in word :
    print('Word letter is : ', n)
print()

my_info = {
    "name": "Kim",
    "age": 30,
    "city": "Seoul"
}

for key in my_info :
    print('My info key is : ', key)

for values in my_info.values() :
    print('My info value is : ', values)
print()

name = "FineApple"

for index in name :
    if index.isupper():
        print(index, end= '')
    else:
        print(index.upper(), end= '')
print()

for index in name :
    if index.islower():
        print(index, end= '')
    else:
        print(index.lower(), end= '')
print()

# break, continue
score = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
count = 0

for s in score :
    count += 1
    if s == 18 :
        print('18점이 나왔습니다. 반복문을 종료합니다.')
        print('18점이 나올 때까지 반복한 횟수는 : ', count)
        break

for s in score :
    if s == 21:
        print("21점이 나왔습니다. 반복문을 종료합니다.")
        break
    else:
        print("NOT FOUND")

lt = ["1", 2, 5, True, 3.14, complex(4)]
print()

for l in lt :
    if type(lt) is bool:
        continue
    print("current type is :", type(lt))
    print('multiply by 3 : ', l * 3)
print()

# for-else
# 모든 원소를 반복 한 후 없다면 else문 실행
score = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
for num in score :
    if num == 20:
        print("Found 20, exiting loop.")
        break
else :
    print("Not Found 24")

for num in score :
    if num == 49:
        print("Found 49, exiting loop.")
        break
else :
    print("Not Found 49")
print()

# 구구단
for i in range(2, 11):
    for j in range (1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제
name2 = 'Aceman'
print('Reversed name is : ', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
