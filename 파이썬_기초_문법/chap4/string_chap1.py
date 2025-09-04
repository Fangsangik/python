"""
파이썬 문자형

문자형 사용법
문자형 중요성
문자형 출력
이스케이프
멀티 라인
문자형 연산
문자형 형 반환
인덱싱
문자열 함수
슬라이싱
"""

# 문자형 생성
str1 = "I am a Python"
str2 = 'Python'
str3 = """Python is a programming language"""
str4 = '''Python is a programming language'''
print(type(str1), type(str2), type(str3), type(str4))

# 문자열 길이 (공백 포함)
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str5 = ""
str6 = str()
print(type(str5), len(str5))
print(type(str6), len(str6))
print()

# escape
# 작은 따음표 있을 경우 \로 이스케이프 하면 그냥 문자열로 인식
print('I\'m a boy')

escape_str1 = "Do you want to \"build a snowman?\""
print(escape_str1)
escape_str2 = 'What\'s your name?'
print(escape_str2)
print()

# \t 탭 & \n 줄바꿈
# 키보드의 Tab 키와 동일한 기능
print('a\t b')
print('a\n b')

t_s1 = "click \t Start!"
t_s2 = "New Line \n Check"
print(t_s1)
print(t_s2)
print()

# Raw String (r)
# 역슬래쉬 자체를 신경쓰지 않는다
# 파일 경로 같은거 지정 해줄때 유용
raw_s1 = r'D:\Python\test'
print(raw_s1)
print()

# 멀티라인 문자열
# 내부에 많은 문자열이 있을 때
# \""" """ 또는 \''' ''' 사용
multi_line_str1 = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
multi_line_str2 = """String Multi Line test"""
# \로 시작 하면 그 다음에 바인딩을 하는 것으로 파이썬은 인식
multi_line_str3 = \
    """String Multi Line test"""
print(multi_line_str2)
print(multi_line_str3)
print()

# 문자열 연산
str_01 = "hello"
str_02 = "World"
str_03 = "Python"
str_04 = "Programming"
print(str_01 * 3)
print(str_01 + str_02 + str_03 + str_04)
print(str_01 + " " + str_02 + " " + str_03 + " " + str_04)
# 문자가 문자열 안에 있는지 확인
print('y' in str_03)
print('z' in str_03)
print('y' not in str_03)
print('z' not in str_03)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(3.14), type(str(3.14)))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha, .....)
# 대문자로 변환
print('Capitalize:', str_01.capitalize())
# 소문자 변환
print('Lower:', str_02.lower())
# endswith (끝 글자가 특정 문자열로 끝나는지 확인)
print('Endswith:', str_04.endswith('ing'))
# replace (문자열 치환)
print('Replace:', str_04.replace("Programming", "Coding"))
# sorts (문자열 정렬)
print('Sorted:', sorted(str_04))
# split (특정 단어 또는 문자로 문자열을 나누기)
print('Split:', str_04.split('g'))
print()

# sequence (문자열은 시퀀스 자료형)
# __iter__ (iter가 있다면 반복 할 수 있다)
# 자르는 처리를 할 수 있다.
im_str = "Good Boy!"
print(dir(im_str))
for i in im_str:
    print(i)
print()

# slicing (문자열 자르기)
sl = "Nice Python"
# 첫번째 문자
print(sl[0])
# 0부터 4까지 (0, 1, 2, 3)
print(sl[0:4])
# 5 ~ 11
print(sl[5:11])
# 0부터 끝까지
print(sl[0:])
print(sl[:len(sl)])
# 0부터 마지막 단어 전까지
print(sl[:len(sl) - 1])
# 1부터 9까지 가져오는데 2칸씩 건너뛰기
print(sl[1:9:2])
# 끝에서 부터 0까지
print(sl[:11])
print(sl[-5:])
print(sl[1:-2])
# 처음부터 끝까지 두칸 간격을 갖고 가져오는 것
print(sl[::2])
# 슬라이싱을 이용한 역순
print(sl[::-1])
print()

# ASCII 코드
a = 'z'
b = 'A'
# 문자를 ASCII 코드로 변환
print(ord(a))
print(ord(b))
# ASCII 코드를 문자로 변환
print(chr(122))
print(chr(65))

