"""
csv file -> csv.reader / csv.writer
xml / json / csv -> record set

CSV : MEME - text/csv
"""

import csv

# CSV 파일 읽기
with open('resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # header 빼고 출력

    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))  # __iter__() -> 반복 가능한 객체
    print()

    for c in reader:
        # print(c)
        # 타입 확인 (list -> str
        print(''.join(c))

# 예제 2
with open('resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 지정 (잘못된 구분자 사용시) -> 하나로 묶여서 가져와짐

    for c in reader:
        print(c)

# 예제 3
with open('resource/test2.csv', 'r') as f:
    reader = csv.DictReader(f)  # 정렬로 된 딕셔너리 형태로 읽기

    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__() -> 반복 가능한 객체
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------------')

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] # [10, 11, 12]를 하나의 record로 묶어서 출력
with open('resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    print(dir(wt))

    for v in w:
        wt.writerow(v) # 각 리스트를 한 줄로 출력

# dictionary key 값을 이용한 csv 파일 쓰기
with open('resource/write1.csv', 'w', encoding='UTF-8') as f:
    # 필드 명
    fields = ['One', 'Two', 'Three']

    # Dict writer
    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader() # 헤더 작성

    for v in w :
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})  # 딕셔너리 형태로 작성
