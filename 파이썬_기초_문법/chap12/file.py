"""
파일 write & read 함수 실습

읽기 모드 : r / 쓰기 모드 : w / 추가 모드 : a, t(text), b(binary)
상대 경로 : .. / ./
절대 경로 : /home/user/file.txt (root부터 시작하는 경로) -> 코드가 어디서든 실행 가능
"""

# 파일 읽기 (open 함수 사용)
f = open('resource/it_news.txt', 'r', encoding='UTF-8')  # r + t (단 text는 기본값)
print(dir(f))
print(f.encoding)  # 파일 인코딩 확인
print(f.name)  # 파일 이름
print(f.mode)  # 파일 모드 확인 (r, w, a 등)
cts = f.read()
print(cts)  # 파일 내용 출력
f.close()  # 파일 닫기 (열었으면 닫아줘야 함)

# 파일 읽기2 (with 구문 사용 = 자동으로 파일 닫기)
# 들여쓰기 딱딱 되어 있음
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)  # 파일 내용 출력
    print(iter(c))
    print(list(c))  # 파일 내용을 리스트로 출력
print()

# read() -> 전체를 읽어오지만 / read(n) -> n바이트 까지만 읽어옴
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)  # 파일 내용 출력
    c = f.read(20)  # 내부적으로 내가 어디 까지 읽어 왔는지 기억함 / 다음 20바이트 읽기
    print(c)  # 파일 내용 출력
    c = f.seek(0, 0) # 파일 포인터를 처음으로 이동
    print(c)
print()

# readline() : 한 줄씩 읽기
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline() # 한 줄 읽기
    print(line)
    line = f.readline() # 다음 줄 읽기
    print(line)
print()

# readlines() : 모든 줄을 읽어 리스트로 반환
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()  # 모든 줄을 읽어 리스트로 반환
    print(lines)  # 리스트 형태로 출력
    for line in lines:  # 각 줄을 출력
        print(line.strip())  # 줄바꿈 문자 제거하고 출력
print()

# 파일 쓰기 (open 함수 사용)
with open('resource/it_news2.txt', 'w', encoding='UTF-8') as f:
    f.write('Hello, World!\n')  # 파일에 문자열 쓰기
    f.write('This is a test file.\n')  # 다음 줄에 문자열 쓰기
    f.writelines(['Line 1\n', 'Line 2\n', 'Line 3\n'])  # 여러 줄 쓰기

# 파일 쓰기 2
with open('resource/it_news2.txt', 'a', encoding='UTF-8') as f:
    f.write('Hello, World!\n')  # 파일에 문자열 쓰기

# writeLines() : 리스트 -> 파일
with open('resource/it_news2.txt', 'w', encoding='UTF-8') as f:
    lines = ['Apple\n', 'Banana\n', 'Cherry\n']  # 리스트 형태로 저장
    f.writelines(lines)  # 리스트의 각 요소를 파일에 씀

# 파일 읽기
# print문이 console에 출력 x -> 파일에 출력
with open('resource/it_news2.txt', 'w', encoding='UTF-8') as f:
    print('Test text write!', file = f)  # 파일 내용 출력
    print('Test text write!', file = f)  # 파일 내용 출력
    print('Test text write!', file = f)  # 파일 내용 출력