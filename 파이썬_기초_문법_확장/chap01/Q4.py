"""`
아래 조건과 같이` **`../source/44-1.txt`** `에` **`파일 읽기 및 쓰기`** `기능을` **`while`** `문을 사용후 구현하세요.`

# 구현내용
# 조건1 : 파일명 및 위치 ../source/44-1.txt
# 조건2 : 사용자 입력 (쓰기, 읽기, 종료)
# 조건3 : 기존 내용에 추가해서 쓰기 수행
# 조건4 : "종료" 명령어 입력 전까지는 프로그램이 종료 불가
# 조건5 : 파일 내용은 \n(줄바꿈) 해서 출력 수행


# 프로그램 구현 화면
# 강의 영상 참조

# Python File I/O Mode 이해는 정말 중요해요.
# 지금 까지 배운 내용을 활용해 보세요.

# open("source", a+) : write in text mode(appending, reading and writing) -> append + read/write
# open("source", w+) : write in text mode(reading and writing) -> write + read/write
# open("source", r+b) : read and write in binary mode -> read + write in binary
# +가 있으면 : 읽기 기능 + 다른 기능 수행

# 참고 : https://docs.python.org/3/library/functions.html#open
"""

"""
def file_read_write():
    file_path = "/Users/hwangsang-ik/PythonLecture/파이썬_기초_문법_확장/chap01/source/44-1.txt"
    while True :
        user_input = input("명령어를 입력하세요 (쓰기, 읽기, 종료): ")
        if user_input == "쓰기" :
            content = input("파일에 추가할 내용을 입력하세요: ")
            with open(file_path, "a+", encoding="utf-8") as file :
                file.write(content + "\n")
            print("내용이 파일에 추가되었습니다.")
        elif user_input == "읽기" :
            with open(file_path, "r", encoding="utf-8") as file :
                print("파일 내용:")
                print(file.read())
        elif user_input == "종료" :
            file.close()
            print("프로그램을 종료합니다.")
            break
        else :
            print("올바른 명령어를 입력하세요.")
file_read_write()
"""

"""
**`지금 까지 배운 내용을 기반으로`** `아래 조건과 같이` **`전화번호부`** `를` **`while`** `문을 사용후 구현하세요.` **`44번 예제를 참고하세요.`**

# 구현내용
# 조건1 : 전화번호부 확인
# 조건2 : 전화번호부 멤버 추가
# 조건3 : 전화번호부 멤버 삭제
# 조건4 : 프로그램 종료
# 조건5 : 전화번호 전체 데이터는 아래와 같이 json 형식으로 가정
# 조건6 : (가능한경우) 파일 쓰기, 읽기 기능 추가


# 프로그램 구현 화면
# 강의 영상 참조

# 기본 제공 데이터
phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }
```
"""

# 방법 1
"""phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }

def phonebook_manager():
    while True :
        command = input("명령어를 입력하세요 (확인, 추가, 삭제, 종료): ")
        if command == "확인" :
            print("전화번호부 : ")
            for key, value in phonebook.items():
                print(f"{key}: Name: {value['Name']}, Phone: {value['Phone']}")
        elif command == "추가" :
            name = input("추가할 이름을 입력하세요: ")
            phone = input("추가할 전화번호를 입력하세요: ")
            new_key = max(phonebook.keys()) + 1 if phonebook else 0
            phonebook[new_key] = {'Name': name, 'Phone': phone}
            print(f"{name}이(가) 전화번호부에 추가되었습니다.")
        elif command == "삭제" :
            key_to_delete = int(input("삭제할 멤버의 키를 입력하세요: "))
            if key_to_delete in phonebook :
                deleted_member = phonebook.pop(key_to_delete)
                print(f"{deleted_member['Name']}이(가) 전화번호부에서 삭제되었습니다.")
            else :
                print("해당 키의 멤버가 존재하지 않습니다.")
        elif command == "종료" :
            print("프로그램을 종료합니다.")
            break
        else :
            print("올바른 명령어를 입력하세요.")
phonebook_manager()"""

# 방법 2
phonebook2 = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }

# 전화번호부 확인
def confirm_phonebook():
    if not phonebook2:
        print("전화번호부가 비어 있습니다.\n")
        return
    for key, value in phonebook2.items():
        print(f"{key}: Name: {value['Name']}, Phone: {value['Phone']}")
    print()

# 전화번호부 멤버 추가
def add_phonebook_member():
    name = input("추가할 이름을 입력하세요: ")
    name_check = False

    for member in phonebook2.values():
        if member['Name'] == name:
            name_check = True
            break

    if name_check is True:
        print("이미 존재하는 이름입니다. 다른 이름을 입력하세요.\n")
        return

    phone = input("추가할 전화번호를 입력하세요: ")
    # 신규 전화번호 생성시, 마지막 키값 + 1 / 없으면 키 0부터 시작
    new_key = max(phonebook2.keys()) + 1 if phonebook2 else 0
    phonebook2[new_key] = {'Name': name, 'Phone': phone}
    print(f"{name}이(가) 전화번호부에 추가되었습니다.\n")

# 전화번호부 멤버 삭제
def delete_phonebook_member():
    key_to_delete = int(input("삭제할 멤버의 키를 입력하세요: "))
    if key_to_delete in phonebook2:
        deleted_member = phonebook2.pop(key_to_delete)
        print(f"{deleted_member['Name']}이(가) 전화번호부에서 삭제되었습니다.\n")
    else:
        print("해당 키의 멤버가 존재하지 않습니다.\n")


def phonebook_manager2():
    while True:
        menu = input("명령어를 입력하세요 (확인, 추가, 삭제, 종료): ")
        if menu == "확인":
            confirm_phonebook()
        elif menu == "추가":
            add_phonebook_member()
        elif menu == "삭제":
            delete_phonebook_member()
        elif menu == "종료":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 명령어를 입력하세요.")
phonebook_manager2()
