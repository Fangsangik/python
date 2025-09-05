"""
파이썬 외장 함수
실제 프로그램 개발 중 자주 사용
종류 : sys, pickle, shutil, temfile, time, random ...
"""

# 예제
# sys 모듈을 사용하여 명령행 인자 출력
import sys
print(sys.argv)

# 예제2
# 강제 종료
# sys.exit()

# 예제3
# python package 위치
print(sys.path)

# 예제4
# pickle : 객체 파일 쓰기
# 클래스나, 변수, 메서드 파이썬의 자료형을 쓸때 -> 객체 자체를 컴퓨터에 저장
import pickle

# 예제 4
# 쓰기
f = open('text.obj', 'wb') # 바이너리 모드로 파일 열기
obj = {1 : 'one', 2 : 'two', 3 : 'three'}
pickle.dump(obj, f)  # 객체를 파일에 저장 / dump : 객체를 파일에 저장하는 함수
f.close()  # 파일 닫기 (열었으면 닫아줘야 함)

# 열기
f = open('text.obj', 'rb')  # 바이너리 모드로 파일 열기
data = pickle.load(f)  # 파일에서 객체를 읽어오기 / load : 파일에서 객체를 읽어오는 함수
print(data, type(data))  # {1: 'one', 2: 'two', 3: 'three'} <class 'dict'>
f.close()  # 파일 닫기 (열었으면 닫아줘야 함)

# OS : 환경변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename
# 예제
import os
print(os.environ)
print(os.environ['HOMEBREW_PREFIX'])  # 환경변수 출력

# 현제 경로
print(os.getcwd())  # 현재 작업 디렉토리 출력

# time : 시간 관련 함수
import time
print(time.time())
# 현재 시간을 출력
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 현재 시간을 'YYYY-MM-DD HH:MM:SS' 형식으로 출력))
# 시간 간격 발생
for i in range(5):
    print(i)
    time.sleep(0)  # 5초 대기 -> 프로그램이 5초 동안 멈춤

# random : 난수 생성
import random
print(random.random()) # 0 ~ 1 사이의 난수 생성
print(random.randint(1, 45))  # 1 ~ 45 사이의 정수 난수 생성
print(random.randrange(1, 46))  # 1 ~ 46 사이의 정수 난수 생성 (46는 포함되지 않음)

# shuffle : 리스트의 요소를 무작위로 섞기
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)  # 리스트의 요소를 무작위로 섞기
print(lst)  # 섞인 리스트 출력

# choice : 리스트에서 무작위로 요소 선택
print(random.choice(lst))  # 리스트에서 무작위로 요소 선택

# webbrowser : 웹 브라우저 관련 함수
import webbrowser
webbrowser.open('https://www.python.org')  # 파이썬 공식 웹사이트 열기