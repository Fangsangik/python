"""
`아래` **`Dict 데이터`** `에서` **`사용자 입력`** `으로` **`키(Key)`** `로` **`검색`** `후` **`값`** `을 반환하세요.` `아래와 같이 출력하세요.`
d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

# 사용자 입력1(정상 값)
France

# 출력1
'32'

# 사용자 입력2(잘못된 값)
Canada

# 출력2
'No results were found for your search.'

# input 함수 기억하시죠?
# 사용자 입력 기능을 구현 할 경우에는 다양한 입력 변수를 고려해야해요.(대소문자, 특수문자 등)

# 함수 형태로도 구현해 보세요.

# 예외 처리 기능을 사용하시면 기능적으로 견고하게 동작할 수 있어요.

# 참고
# https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions
"""

d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

"""# 방법 1
def search_dict():
    key = input("Enter a country name: ").upper()
    upper_dict = {k.upper(): v for k, v in d.items()}

    if key in upper_dict:
        print(f"'{upper_dict[key]}'")
    else:
        print("'No results were found for your search.'")
search_dict()

# 방법 2
txt = input("Enter a country name: ").lower()
for i in d.keys():
    if i.lower() == txt:
        print(f"'{d[i]}'")
        break
else:
    print("'No results were found for your search.'")

# 방법 3
def search_dict_v2(word):
    try :
        c = dict((k.lower(), v) for k, v in d.items())
        return c.get(word)
    except KeyError:
        return 'No results were found for your search.'

txt = input("Enter a country name: ").lower()
print(search_dict_v2(txt))

# 방법 4
def search_dict_v3(word):
    c = dict((k.lower(), v) for k, v in d.items())
    # get을 사용해서 catch문 없이 처리
    return c.get(word, 'No results were found for your search.')
"""


"""
**`datetime 패키지`** `와` **`strftime 함수`** `를 사용해서` **`하단 포멧`** 
`결과와 ` **`똑같이`** `출력하세요.` **`힌트 링크를 활용하세요.`**

t = datetime.now()

# 날짜 및 시간은 실행 시간에 따라 변경

# 출력 포맷1
# 2022-08-04 12:28:23

# 출력 포맷2
# 2022-08-04 12:28:23 PM Thursday August

# 출력 포맷3
# Thursday, August 04, 2022 12:28:57

# 출력 포맷4
# Thursday, Aug 08/04/22 12:28:57 PM

# 다양한 형식의 시간 관련 출력 방법은 정말 중요해요.
# 시, 분, 초, 일, 월, 년 간의 계산 방법도 꼭 알아두셔야 합니다.
# 날짜 계산, 수행시간 계산, 로그 출력 포멧 규정 등 프로그래밍에서 많이 활용됩니다.

# UTC 기준 시간대 표현은 timezone 내장 모듈을 사용합니다.
    
# datetime.date.today() : 자주 사용
# datetime.now() : 자주 사용

# time.strptime(string[, format])
    
# 참고1
# https://docs.python.org/3/library/time.html#time.strptime
# https://strftime.org/
    
# 참고2
# https://docs.python.org/3/library/datetime.html
"""

from datetime import datetime, timezone

# %Y-%m-%d %H:%M:%S -> 년-월-일 시:분:초
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# %p %A %B -> AM/PM, 요일, 월
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S %p %A %B"))
# "%A, %B %d, %Y %H:%M:%S" -> 요일, 월 일, 년 시:분:초
print(datetime.now().strftime("%A, %B %d, %Y %H:%M:%S"))
# "%A, %b %m/%d/%y %I:%M:%S %p" -> 요일, 월(약어) 월/일/년(약어) 시:분:초 AM/PM
print(datetime.now().strftime("%A, %b %m/%d/%y %I:%M:%S %p"))

"""
`주어진` **`문자열`** `에서` **`6자리`** `의` **`무작위의 코드`** `를 ` **`중복없이 5개`** `생성하세요.(리스트)` **`출력 결과를 확인하세요.`**

# 출력 결과
['ihv)jW', 'KFGN@o', 'L?w0yv', 'Y4hJ$O', 'K*bypg']

# 랜덤으로 숫자 문자를 조합 후 중복없이 처리하는 방법도 중요합니다.
# 실행 시 시간복잡도도 생각하셔야 해요.

# UTC 기준 시간대 표현은 timezone 내장 모듈을 사용합니다.
    
# random.choice : 1개 생성
# random.choices : 다수 생성(중복 없음) python 3.6+ 
# random.sample : 다수 생성(중복 있음)

# random.choice(seq)
# random.choices(population, weights=None, *, cum_weights=None, k=1)
# random.sample(population, k, *, counts=None)
    
# 참고
# https://docs.python.org/3/library/random.html
```
"""
import random
from datetime import datetime

# 문자열 선언
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# 중복 제거에 대한 고려
# 1. seed 사용
# 2. set 사용
# 3. 반복문 체크

# 방법 1
def generate_codes(n) :
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    code_list = []
    # 값이 바뀌면 안되고, 고정 시킨 상태에서 test -> 고정 값을 주면 된다.
    random.seed()

    for i in range(0, n):
        chosen = random.sample(characters, 5)
        code = ''.join(chosen)
        code_list.append(code)
    return code_list
print(generate_codes(5))

"""
`아래` **`조건`** `과 같이` **`사용자 입력 문자열(비밀번호)`** `를` **`체크하세요.`
** **`아래 조건 참조`** **`while, input 사용`**

# 사용자 비밀번호 입력
# 조건1 : 비밀번호는 반드시 8자 이상이어야 합니다.
# 조건2 : 반드시 1개 이상의 대문자는 포함되어 있어야 합니다.
# 조건3 : 반드시 1개 이상의 숫자를 포함해야 합니다.

# 사용자 입력1
password1 = input() # a1234!! 

# 출력 결과1
# 8자 이하, 대문자 미포함
비밀번호 조건이 맞지 않습니다.


# 사용자 입력2
password2 = input() # A777abcd!

# 출력 결과2
비밀번호 형식이 맞습니다.


# 주어진 문자열에 대해 조건을 체크하는 문제 해결 능력은 중요합니다.
# 정규표현식을 사용해도 됩니다.

# while 문을 활용해서 프로그램 흐름이 끊기지 않게 작성해 주세요.
    
# any 함수 : 한 개라도 참(True)일 경우 True 반환(일부 만족)
# all 함수 : 전체가 참(True)일 경우 True 반환(모두 만족)

# 내부 문자열 함수 isdigit(), isupper() 함수 등을 활용하세요.
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
"""

"""def check_password():
    password = input("비밀번호를 입력하세요 : ")
    while True :
        if len(password) < 8:
            print("8자 이하, 대문자 미포함")
            password = input("비밀번호를 입력하세요 : ")
        elif not any(char.isupper() for char in password):
            print("대문자 미포함")
            password = input("비밀번호를 입력하세요 : ")
        elif not any(char.isdigit() for char in password):
            print("숫자 미포함")
            password = input("비밀번호를 입력하세요 : ")
        else :
            print("비밀번호 형식이 맞습니다.")
            break
check_password()

# 방법 2
def check_password_v2():
    while True:
        results = []
        password = input("비밀번호를 입력하세요 : ")
        if not any(i.isdigit() for i in password):
            results.append("최소 한개 이상의 숫자를 포함해야 합니다.")
        elif not any(i.isupper() for i in password):
            results.append("최소 한개 이상의 대문자를 포함해야 합니다.")
        elif len(password) < 8:
            results.append("비밀번호는 반드시 8자 이상이어야 합니다.")

        if len(results) == 0:
            print("비밀번호 형식이 맞습니다.")
            break
        else:
            print("아래와 같이 비밀번호 조건이 맞지 않습니다.")
            for txt in results:
                print("--->", txt)
check_password_v2()
"""

"""
**`41-1.txt`** **`텍스트`** `파일을 불러온 후` **`알파벳 C로`** `시작하는` **`나라`** `의` **`지표의 합`** `을 출력하세요.` **`다양한 방법으로 해결해보세요.`**

# 41-1.txt 파일을 열어보세요.

# C로 시작하는 나라 이름
# Canada, China, Chad ...

# 결과 값
1546447728

# 지금까지 배운 내용으로 충분히 문제 해결이 가능해요.

# 다양한 포멧 형식(excel, txt, xml, html, json 등) 파일 데이터를 읽어오는 방법은 매우 중요합니다.
    
# 사용자가 원하는 데이터의 합, 평균, 최대값, 최소값, 랭킹(정렬) 등 가공 능력은 정말 중요해요.
    
# 주로 pandas를 사용합니다.
# 참고 : https://pandas.pydata.org/docs/reference/index.html
"""

# 방법 1
def file_open(filepath):
    count = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            country, value = line.strip().split(",")
            if country.startswith('C' or country.startswith('c')):
                count += int(value)
    return count
print(file_open('/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/41-1.txt'))

# 방법 2
def file_open_v2(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readline()
        count = sum(int(lines.split(",")[1]) for lines in f if lines.startswith("C" or lines.startswith("c")))
    return count
print(file_open_v2('/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/41-1.txt'))

# 방법 3
def file_open_v3(filepath):
    total = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for i in f :
            lines = i.strip().split(",")
            if not lines : 
                continue
            country, value = lines[0].strip(), lines[1].strip() 
            if country.lower().startswith('c'):
                total += int(value)
    return total
print(file_open_v3('/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/41-1.txt'))

# 방법 4
def file_open_v4(filepath):
    value_list = []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            country, value = line.rstrip().split(",")
            if country.lower().startswith('c'):
                value_list.append(int(value))

    return value_list

result = file_open_v4('/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/41-1.txt')
print(sum(result))

"""
`폴더` **`42-1`** `에 존재하는` **`파일`** `중에서` **`확장자`** `가` **`*.py 및 *.png`** 
`파일을` **`분류하세요.`** **`다양한 방법으로 프로그래밍 해보세요.`**

# 폴더 경로
# ../source/42-1
# 조건1 : 파이썬 실행 형식(*.py) 개수 및 파일명
# 조건2 : 이미지 파일 형식(*.png) 개수 및 파일명


# 출력 결과
PNG file info :  ['file10.png', 'file11.png', 'file19.png', 'file6.png']  Count :  4
PY file info :  ['file12.py', 'file13.py', 'file17.py', 'file3.py', 'file4.py', 'file8.py']  Count :  6
```

# os 패키지의 listdir() 함수를 사용해보세요.
# glob 패키지의 glob1()함수를 사용해보세요.

# listdir() : os.listdir(path of the directory) 
# glob1() : glob.glob1(pathname)
    
# 참고1 : https://docs.python.org/3/library/os.html#os.listdir
# 참고2 : https://thomas-cokelaer.info/tutorials/python/module_glob.html
"""

import os

# 방법 1
py_list = []
png_list = []

for files in os.listdir("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/42-1"):

    # splitext -> 파일명과 확장자 분리 (튜플 형태로 반환)
    # print(os.path.splitext(files))

    # 확장자 검사
    ex = files.split(".")[-1]

    if ex == "py":
        py_list.append(files)
    elif ex == "png":
        png_list.append(files)
print("PNG file info : ", png_list, " Count : ", len(png_list))
print("PY file info : ", py_list, " Count : ", len(py_list))

# 방법 2
import glob

png_list1 = glob.glob1("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/42-1", "*.png")
py_list1 = glob.glob1("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/42-1", "*.py")
print("PNG file info : ", png_list1, " Count : ", len(png_list1))
print("PY file info : ", py_list1, " Count : ", len(py_list1))

"""
`폴더` ** `43 - 1` ** `에 존재하는` ** `파일 및 하위 폴더
` ** `전체에서` ** `확장자` ** `가` ** ` *.txt 및 *.png
` ** `파일을` ** `분류하세요.` ** ** `다양한 방법으로 프로그래밍 해보세요.

# 폴더 경로
# ../source/43-1
# 조건1 : 텍스트 실행 형식(*.txt) 개수 및 파일명
# 조건2 : 이미지 파일 형식(*.png) 개수 및 파일명

# 출력 결과
TXT
file
info: ['file1.txt', 'file14.txt', 'file15.txt', 'file2.txt', 'file20.txt', 'file5.txt', 'file7.txt', 'file9.txt',
       'file1.txt', 'file6.txt', 'file7.txt', 'file8.txt']
Count: 12

PNG
file
info: ['file10.png', 'file11.png', 'file19.png', 'file6.png', 'file3.png', 'file7.png', 'file3.png', 'file4.png']
Count: 8

# os 패키지의 os.walk(), os.path.join(), listdir() 에서 필요한 함수를 사용해보세요.
# glob 패키지의 glob()함수를 사용해보세요.

# listdir() : os.listdir(path of the directory) 
# walk() : os.walk(top, topdown=True, onerror=None, followlinks=False)
# glob() : glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False)
    
# 참고1 : https://docs.python.org/3/library/os.html#os.listdir
# 참고2 : https://docs.python.org/3/library/os.html#os.walk
# 참고3 : https://docs.python.org/3/library/os.html#os.DirEntry.path
# 참고4 : https://docs.python.org/3/library/glob.html#glob.glob
"""

import os
import glob

# 방법 1
txt_list = []
png_list = []

# os.walk : 상위 폴더 부터 하위 폴더까지 탐색 (재귀)
a = os.walk("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/43-1")

for x, y, z in a:
    for f in z :
        ex = f.split(".")[-1]
        if ex == "txt":
            txt_list.append(f)
        elif ex == "png":
            png_list.append(f)
print("TXT file info: ", txt_list, " Count: ", len(txt_list))
print("PNG file info: ", png_list, " Count: ", len(png_list))

# 방법 2
# recursive=True -> 하위 폴더까지 탐색 (재귀)
txt_list1 = glob.glob("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/43-1/**/*.txt", recursive=True)
png_list1 = glob.glob("/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/43-1/**/*.png", recursive=True)
print("TXT file info: ", [os.path.basename(f) for f in txt_list1], " Count: ", len(txt_list1))
print("PNG file info: ", [os.path.basename(f) for f in png_list1], " Count: ", len(png_list1))