"""`아래와 같은` **`문장을 공백`** `으로` **`구분 후`** `
단어 개수를 출력하는` **`함수`** `를 작성 후 실행하세요.` **`input 함수 가능`**
출력 결과 : 10

# Python split() 함수는 자주사용해요.
# string.split(separator, maxsplit) : 구분자, 분할 수
# 기본 분리 지정자는 공백
# 문자열을 구분 후 리스트로 변환
"""
from traceback import format_list

in_str = "Suppose we have few words that are separated by spaces."

a = in_str.split(" ")  # 공백으로 구분
print(a)

"""txt2 = input()
b = txt2.split("&")
print(b)"""

count = 0
for i in in_str.split(" "):
    count += 1
print(count)

"""def word_count():
    in_str = input("문장을 입력하세요: ")
    count = 0
    for i in in_str.split(" "):
        count += 1
    return count
print(word_count())"""
print()

"""
**`/source`** **`폴더의 22-2.txt`** `파일을` **`공백 구분 후`** `단어 개수를 출력하는` **`함수`** `를 작성 후 실행하세요.` **`*콤마의 경우 두 단어로 취급*`**
출력 결과 : 72

# string.split(separator, maxsplit) : 구분자, 분할 수
# string.replace(oldvalue, newvalue, count) : 타겟, 변환 값, 개수
# 콤마를 공백으로 치환 -> 문자열을 구분 후 리스트로 변환
# python re(Regular Expression) 사용가능(정규표현식)
"""
# Hi! Kim,Eun 의 경우 -> 3개

in_str = "/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/22-1.txt"


def cnt_word1(filePath):
    with open(filePath, 'r') as file:
        txt = file.read()
    txt = txt.replace(",", " ")
    txt_list = txt.split(" ")
    return len(txt_list)


print(cnt_word1(in_str))

import re


def cnt_word2(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()

    # 정규 표현식
    txt_list = re.split(" | ", txt)  # 공백과 콤마로 구분
    return len(txt_list)


print(cnt_word2(in_str))
print()

"""**`/source`** **`폴더에 23-1.txt`** `파일이름으로` **`대문자 알파벳(A-Z)을`**  
**`공백`** `으로 구분 후 파일로 쓰세요.` **`*아래 조건을 참고하세요*`**
# 아래 조건 참조

파일명 & 경로 = "../source/23-1.txt"
파일 출력 결과 : "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

# 방법1 : 알파벳 리스트를 선언 후 파일로 쓰기
# 방법2 : string 패키지를 사용 후 쉽게 파일로 쓰기
# 파이썬 *유니코드*의 이해는 정말 중요해요.
# 유니코드(Unicode) : 전세계에 존재하는 문자의 출력을 위한 인코딩 표준 -> 유니코드 코드값의 테이블 형태 
# ord(), chr() 함수 사용법 중요해요.
# python string package : https://docs.python.org/3/library/string.html
```"""


def write_alphabet1(filepath):
    with open(filepath, 'w') as file:
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # str은 시퀀스형 -> 반복문 사용 가능
            file.write(i + " ")
    print("파일 쓰기 완료")


write_alphabet1("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/23-1.txt")


def write_alphabet1_1(filepath):
    with open(filepath, 'w') as file:
        for i in range(65, 91):
            file.write(chr(i) + " ")
    print("파일 쓰기 완료")


write_alphabet1_1("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/23-1_2.txt")

import string  # Built-in 함수


def write_alphabet2(filepath):
    with open(filepath, 'w') as file:
        file.write(string.ascii_uppercase.replace("", " ").strip())  # ascii_uppercase -> 대문자 알파벳
    print("파일 쓰기 완료")


write_alphabet2("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/23-1_3.txt")
print()

"""
아래 **`3개의 리스트`** 를 **`{key : a , value : b * c}`** `형태의 
` **`Dict(딕셔너리)`**  **`구조`** `로 변경하세요.` **`*다양한 방법 활용*`**
출력 결과 : "{'one': 156.0, 'two': 148.0, 'three': 54.0, 'four': 315.0}"

# 다양한 Iterable 그룹을 묶어 연산하는 과정은 중요해요.
# zip : 다중 그룹의 반복가능한 자료형을 묶는 기능
# usage : zip(*iterables, strict=False) # Changed in version 3.10: Added the strict argument.
# python string package : https://www.oulub.com/en-US/Python/library.functions-zip
"""
a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# zip 활용
result1 = {}
for x, y, z in zip(a, b, c):
    result1[x] = y * z
print(result1)

# for문 활용
for i in range(len(a)):
    a[i] = (a[i], b[i] * c[i])
print(dict(a))

print({x: y * z for x, y, z in zip(a, b, c)})

# dict 함수 활용
print(dict((x, y * z) for x, y, z in zip(a, b, c)))

"""`
아래와 같이` **`주어진 리스트`** `를` **`N개 단위로`** **`출력 결과`** `와 같이` **`리스트`** `로 생성 & 출력 하세요.` 
**`*함수 가능*`**

# N -> 3
출력
결과: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'],
     ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z']]

# N -> 5
출력
결과: [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J'], ['K', 'L', 'M', 'N', 'O'], ['P', 'Q', 'R', 'S', 'T'],
     ['U', 'V', 'W', 'X', 'Y'], ['Z']]
     
# List slicing : https://www.geeksforgeeks.org/python-list-slicing/
# List Comprehension : https://www.w3schools.com/python/python_lists_comprehension.asp
# 추천1 : for loop 
# 추천2 : List Comprehension
```"""

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']


def split_list1(input_list, n):
    result = []
    for i in range(0, len(input_list), n):
        result.append(input_list[i:i + n])
    return result


print(split_list1(x, 3))
print(split_list1(x, 5))


def spilt_list2(spilt_size=3):  # default 값 설정
    spilt_list_1 = list()
    for i in range(0, len(x), spilt_size):
        spilt_list_1.append(x[i:i + spilt_size])  # i부터 i+spilt_size 전까지
    return spilt_list_1


print(spilt_list2(3))
print(spilt_list2(5))

spilt_size = 3
output = [x[i:i + spilt_size] for i in range(0, len(x), spilt_size)]
print(output)

"""
**`/source/26-1/`** `경로에서` **`아래 조건`** `으로` **`name = 파일명`**  **`contents = 내용`** `으로 파일로 쓰세요.`

파일명 & 경로 = "../source/26-1/파일명.txt"
파일명 리스트 = ["A", "B", "C", "D", "F", "G"]
컨텐츠 리스트 = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
```

# 다중 리스트 형태의 파일 쓰기 패턴은 정말 많이 사용해요.
# Python Open 함수의 쓰기 모드를 기억해야 해요.
    
# 'w' : Open a text file for writing text (덮어쓰기) / 일정 주기적으로 파일을 덮어써야 하는 경우
# 'a' : Open a text file for appending text (추가) / 하나의 파일의 용량이 찰때 까지 사용 
# f.write :  writes a string to a text file 
# f.writelines : write a list of strings to a file at once.

I/O 작업 -> os와 관련 
"""

import os

filenames = ["A", "B", "C", "D", "F", "G"]
contents1 = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
contents2 = [["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],
             ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],
             ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]]


def write_files(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # loop write
    # for문 안에서 파일을 열고 쓰고 닫고 반복
    for n, c in zip(filenames, contents1):
        with open(filepath + n + ' .txt', 'w') as file:
            file.write(c)
    print("파일 쓰기 완료")


write_files("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/26-1")


def write_files2(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # loop write
    # for문 안에서 파일을 열고 쓰고 닫고 반복
    for n, c in zip(filenames, contents2):
        with open(filepath + n + ' .txt', 'w') as file:
            file.writelines(c + '\n' for c in c)  # 안에 있는 리스트를 iteration 하면서 적어줌
    print("파일 쓰기 완료")


write_files2("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/26-2")

""""**`/source/27-1/`** `경로에` **`모든 텍스트 파일(txt)`** `을` **`읽은 후`** **
`리스트`** `로 출력하세요.` **`*아래 조건 참조*`**
파일명 & 경로 = "../source/27-1/*.txt"

출력 = ['Python', 'JavaScript', 'PHP', 'Rust', 'elite', 'Solidity', 'Assembly', 'hamster', 'india', 'january', 'kibana', 'lamada', 'monster', 'notion', 'orange', 'pokemon', 'query', 'range', 'sonic', 'telegram', 'urban', 'village', 'world', 'x-ray', 'yellow', 'zigzag']

# 다양한 확장자 형식 파일 읽기는 중요해요.
# Python OS 패키지 사용은 능숙해야 해요.
    
# 참조 : https://docs.python.org/3/library/os.html
# getcwd() : 현재 작업 경로를 반환
# listdir() : 지정한 경로의 파일 & 디렉토리 전부 반환

# glob 패키지도 사용 가능해요.
# 참조 : https://docs.python.org/3/library/glob.html
"""

import os


# 방법 1
def read_txt_file(filepath):
    output = []

    # iterate through all files
    for file in os.listdir(filepath):
        if file.endswith(".txt"):
            target_path = os.path.join(filepath, file)

            with open(target_path, 'r', encoding="utf-8") as f:
                output.append(f.read().strip())
    return output


print(read_txt_file("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/27-1"))

import glob


def read_txt_file2(filepath):
    output = []
    for file in glob.glob(filepath + "/*.txt"):  # 경로 내의 모든 txt 파일
        with open(file, 'r', encoding="utf-8") as f:
            output.append(f.read().strip())
    return output


print(read_txt_file2("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/27-1"))

"""`
사용자에게` **`정수를 3회`** **`입력 받은 후`** `으로` **`평균 값`**  `을 출력하세요.` 
**`*다양한 방법으로 시도해 보세요*`**
x = 사용자 입력 -> 15
y = 사용자 입력 -> 25
z = 사용자 입력 -> 45

# 출력
28.3333333333 # (15 + 25 + 45) / 3

# Input 함수는 기본 입력 타입은 Str 자료형인 부분을 꼭 기억하세요.
# 연속적으로 편하게 입력받을 수 있는 방법을 생각해보세요.
    
# 평균, 합계는 리스트로 변환해서 계산하면 매우 편해요!
    
# 참고 : https://docs.python.org/3/library/functions.html#input
"""

"""# 방법 1
# a = int(input("정수 1 입력: "))
# b = int(input("정수 2 입력: "))
# c = int(input("정수 3 입력: "))
# print((a + b + c) / 3)

# 방법 2
x, y, z = input("enter three integers: ").split()
print((int(x) + int(y) + int(z)) / 3) 

# 방법 3
list_num = []
for i in range(3):
    num = int(input("정수 입력: "))
    list_num.append(num)
print(round(sum(list_num) / len(list_num), 2)) # 소수점 둘째자리까지"""

"""
`아래` **`String 포멧`** **`출력문`** `에서` **`결과 값`**  `이` **`다른 것`** `은 무엇일까요?` 
**`*꼭 코딩 후 확인하세요`**

# 파이썬 문자 출력(서식)은 여러가지 방법이 있어요.
    
# 1. % Operator(Old Style)
# 2. str.format(New Style)
# 3. f-Strings (Python 3.6+)
# 4. Template String(from string import Template)
# 참고 : https://docs.python.org/3/library/string.html#template-strings
# 참고 : https://realpython.com/python-f-strings/
"""

# 공통 변수 선언
x = 10
y = 20
serialno = 308276567
n = 'Kim'

# Operator
# 출력1
# %x -> 16진수, %d -> 10진수
ex1 = 'n = %s, s = %x, sum = %d' % (n, serialno, x + y)
print(ex1)

# str.format
# 출력2
ex2 = f'n = {n}, s = {serialno}, sum = {sum}'.format(n=n, serialno=serialno, sum=x + y)
print(ex2)

# f-Strings
# 출력3
ex3 = f'n = {n}, s = {serialno}, sum = {x + y}'
print(ex3)

# 출력 4
"""
string.Template 클래스 사용.
문자열 안에 $변수명 문법.
단순 치환만 하기 때문에 외부 입력 처리에 보안상 안전.
print문 없이도 출력 가능 -> 변수에 담긴 문자열이 출력됨
"""
from string import Template

ex4 = 'n = $n, s= $serialno, sum = $sum'
t = Template(ex4)

# f-String 연습
# 진수
# b : 2진수, o : 8진수, x or X : 16진수
k = 77
print(f"k 2: {k : b}, k 8 {k : o}")
print(f"k 16 : {k : x}, K 16 : {k : X}")  # 16진수 대문자 / 소문자 구분
print()

# 구분기호
num = 1000000000
print(f"m : {num : ,}")

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
g = 20
print(f'g: {g : 10}')  # 10자리
print(f'g: {g : <10}')  # 왼쪽 정렬
print(f'g: {g : >10}')  # 오른쪽 정렬
print(f'g: {g : ^10}')  # 가운데 정렬
print(f'g: {g :*^10}')  # 가운데 정렬, 빈칸 *로 채우기

"""
`아래` **`딕셔너리(Dict)`** `에서` **`출력결과`** `와 같이` **`값을`** `추출하세요.` **`*가능한 방법 모두 코딩해보세요.*`**
# 출력결과
Name : Kim, Age : 23, Type : officer
"""
# 중첩 Dict 선언
d = {"group1": [
    {'name': 'Park', 'age': '32', 'sex': 'Male'},
    {'name': 'Cho', 'age': '44', 'sex': 'Female'},
    {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
],
    "group2": [
        {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
        {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
    ],
    "type": {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
}

# 방법 1
for i in d['group2']:
    if i['name'] == 'Kim':
        name = i['name']
        age = i['age']
        type_ = d['type']['b']
        print(f"Name : {name}, Age : {age}, Type : {type_}")

# 방법 2
keys = list(d.keys())
i = 0

while i < len(keys):
    key = keys[i]
    value = d[key]

    if isinstance(value, list):
        if key == 'group2':
            for item in value:
                if item['name'] == 'Kim':
                    name = item['name']
                    age = item['age']
                    type_ = d['type']['b']
                    print(f"Name : {name}, Age : {age}, Type : {type_}")

                    break
    i += 1

# 방법 3
ex_1 = 'Name : {0}, Age : {1}, Type : {2}'.format(d['group2'][0]['name'], d['group2'][0]['age'], d["type"]["b"])
print(ex_1)

# 방법 4
ex_2 = 'Name : {0}, Age : {1}, Type : {2}'.format(d.get('group2')[0].get('name'), d.get('group2')[0].get('age'),
                                                  d.get("type").get("b"))

"""
`아래` **`딕셔너리(Dict)`** `에` **`두 개`** `의` **`요소를`** `추가하세요.` **`*가능한 방법 모두 코딩해보세요.*`**

# Dict 선언
d = {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }


# 추가1
"group1" : {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}
    
    
# 추가2
"type" : {"f": "engineer"}
    

# 출력 결과
 {  "group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'},
                {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider", "f": "engineer"}
  }
```
"""
d = {"group1": [
    {'name': 'Park', 'age': '32', 'sex': 'Male'},
    {'name': 'Cho', 'age': '44', 'sex': 'Female'},
    {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
],
    "group2": [
        {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
        {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
    ],
    "type": {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
}

# 방법 1
d['group1'].append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
d['type']['f'] = 'engineer'
print(d)

# 방법 2
d.get('group1').append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
d.get('type')['f'] = 'engineer'
print(d)

"""
`아래` **`딕셔너리(Dict)`** `을` **`JSON`**  **`형식`** `으로 변환하세요.` **`*힌트를 참고하세요.*`**

# Dict 선언
d = {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }

# 결과
{
    "group1": [
        {
            "name": "Park",
            "age": "32",
            "sex": "Male"
        },
        {
            "name": "Cho",
            "age": "44",
            "sex": "Female"
        },
        {
            "name": "Kang",
            "age": "39",
            "sex": "Female",
            "married": "No"
        }
    ],
    "group2": [
        {
            "name": "Kim",
            "age": "23",
            "sex": "Male",
            "married": "Yes"
        },
        {
            "name": "Lee",
            "age": "37",
            "sex": "Male",
            "married": "No"
        }
    ],
    "type": {
        "a": "employee",
        "b": "officer",
        "c": "director",
        "d": "manager",
        "e": "service provider"
    }
}


# Dictionary 를 JSON으로 변환하는 기능은 정말 많이 사용해요.
# 데이터 송수신 부분에서 표준화된 데이터 포멧이기 때문이예요.(JavaScript Object Notation)

# json 내장 패키지를 통해 쉽게 변환 가능해요.
# json.dumps() vs json.dump() 차이점을 꼭 이해해야 해요.

# json.dumps(dict, indent) -> 화면상 출력 가능
# json.dump(dict, file_pointer) -> 파일을 쓸 수 있음 
    
# 참고
# https://docs.python.org/3/library/json.html
"""

import json

d = {"group1": [
    {'name': 'Park', 'age': '32', 'sex': 'Male'},
    {'name': 'Cho', 'age': '44', 'sex': 'Female'},
    {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
],
    "group2": [
        {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
        {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
    ],
    "type": {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
}

json_obj = json.dumps(d, indent=4)  # dict -> json string
print(json_obj)

with open("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/dict_to_json.json", 'w') as out:
    json.dump(d, out)  # dict -> json file
print("파일 쓰기 완료")

"""
`아래` **`문자열(JSON 구조)`** `를` **`딕셔너리(Dict)`**  **`형식`** `으로 변환하세요.` **`*힌트를 참고하세요.*`**

# Dict 선언
d = 
    {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    


# 결과
{'group1': 
 [{'name': 'Park', 'age': '32', 'sex': 'Male'}, 
  {'name': 'Cho', 'age': '44', 'sex': 'Female'}, 
  {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
 ], 
 'group2': 
 [{'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'}, 
  {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
 ], 
 'type': {
     'a': 'employee', 'b': 'officer', 'c': 'director', 'd': 'manager', 'e': 'service provider'}
  }
```
"""

d = """
    {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    """
# 문자열을(텍스트파일) Dictionary 구조로 변환하는 방법도 잘 익혀두어야 해요.
# 데이터 송수신 부분에서 표준화된 데이터 포멧이기 때문이예요.(JavaScript Object Notation)

# json 내장 패키지를 통해 쉽게 변환 가능해요.
# (json.load() => 파일 읽어올때)  vs (json.loads() => 출력 확인)  차이점을 꼭 이해해야 해요.

# json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

# 참고
# https://docs.python.org/3/library/json.html#json.load


import json

json_read = json.loads(d.replace("'", "\""))
print(json_read)

with open("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/dict_to_json.json", 'r') as infile:
    json_obj = json.load(infile)
    print(json_obj)

"""
`아래` **`한 개의`** **`리스트(List)`** `를` **`딕셔너리(Dict)`**  **`형식`** `으로 변환하세요.` 
**`*다양한 방법으로 시도하세요.*`**

# 리스트
l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]


# 변환 결과1
{ 0: "Red", 1: "Green", 2: "Black", 3: "Blue", 4: "Orange", 5: "Purple" }

# 변환 결과2
{ 100: "Red", 101: "Green", 102: "Black", 103: "Blue", 104: "Orange", 105: "Purple" }

# 파이썬 내장함수인 enumerate()는 열거형 객체를 반환 하고 카운터 변수도 추가 해요.
# 인덱스 생성 포함 출력 및 Dictionary 변환해도 자주 사용해요.
# 반드시 알아두어야 하는 함수입니다.
# enumerate(iterable, start=0)
"""

l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]
print(dict(enumerate(l, start=0)))

"""
**`1`** `부터` **`10`** `까지` **`1초`** `간격으로` **`숫자`** `를` **`출력 후 종료하세요.`**  **`*(while)문 사용 후 다양한 방법으로 시도하세요.*`**
# 출력 결과
1
2
3
4
5
6
7
8
9
10

# 일정 딜레이(시간) 간격 프로그램 실행 패턴 구현은 정말 중요해요.
# 반복문 외 sleep 함수를 꼭 알아두셔야 해요
# while 문을 사용해서 작성해보세요.
# break, continue 문도 기억하시죠?
# time.sleep(secs)

# 참고
# https://docs.python.org/3/library/time.html#time.sleep
"""
# 방법 1
import time

"""while True:
    for i in range(1, 11):
        print(i)
        # time.sleep(1)
    break
print("종료")
print()

# 방법 2
# 비동기로 하는 작업 -> sleep 이 걸렸을때 고려
n = 0
while n < 10:
    n += 1
    # time.sleep(1)
    print(n)
print("종료")

# 방법 3
n = 1
while True:
    if n > 10:
        # time.sleep(1)
        print(n)
        n += 1
        break"""

"""
**`0.5`** `부터` **`3`** `까지` **`0.5초`** `간격으로` **`딜레이`** `를` **`증가`** `하면서` `아래와 같이 출력하세요.`

# 출력 결과
Delayed for 0.5 seconds
Delayed for 1 seconds
Delayed for 1.5 seconds
Delayed for 2 seconds
Delayed for 2.5 seconds
Delayed for 3 seconds

# 일정 딜레이(시간) 간격 프로그램 실행 패턴 구현은 정말 중요해요.
# 반복문 외 sleep 함수를 꼭 알아두셔야 해요.

# sleep 구문이 포함된 
1.함수 형태 또는 
2.리스트 & 반복문을 사용해서 작성해보세요.
    
# time.sleep(secs)
"""

import time

# 방법 1
for i in [0.5, 1, 1.5, 2, 2.5, 3]:
    time.sleep(i)
    print(f"Delayed for {i} seconds")
print("종료")

# 방법 2
n = 0.5
while True:
    if n > 3:
        time.sleep(n)
        break
    n += 0.5
    print(f"Delayed for {n} seconds")
print("종료")

# 방법 3
def sleep_out(n = 1):
    print(f"delayed for {n} seconds")
    time.sleep(n)

for n in [0.5, 1, 1.5, 2, 2.5, 3]:
    sleep_out(n)
print("종료")
