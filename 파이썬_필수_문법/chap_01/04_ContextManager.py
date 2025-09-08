"""
context manager(컨텍스트 매니저)
- contextlib
- __enter__, __exit__
- with
"""

# close
# close를 하지 않을 경우 I/O 리소스가 계속 낭비 될 수 있음
# context manger : 원하는 타이밍에, 정확하게 리소스를 할당 및 제공 / 반환
# 가장 대표적인게 with 구문 이해
# 정확한 이해 후 프로그래밍 개발 중요

# ex1
# open으로 파일 생성
file = open('testfile.txt', 'w')
try:
    file.write("Context Manager Test")
finally:
    # 할당 받은 리소스를 close
    file.close()

# ex2
# with 구문 사용 (with문 내부에 close가 있음)
with open('testfile1.txt', 'w') as f:
    f.write("Context Manager Test2")

# ex3
class ContextManger_with_exception_handling() :
    def __init__(self, filename, method):
        print("MyFileManager.__init__")
        # 파일 오픈
        self.file_obj = open(filename, method)

    def __enter__(self):
        print("MyFileManager.__enter__")
        return self.file_obj

    # exc_type : 예외 타입
    # exc_val : 예외 값
    # exc_tb : 트레이스백 객체
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MyFileManager.__exit__")
        if exc_type :
            print("Error Type : ", exc_type)
            print("Error Value : ", exc_val)
            print("Error Traceback : ", exc_tb)
        self.file_obj.close()

# 내부적으로 사용이 될때, with 구문이 사용됨
# 초기화 되면서 __init__ 호출 -> open
with ContextManger_with_exception_handling('testfile3.txt', 'w') as f:
    # enter 호출 -> file_obj return
    # 다쓰고 exit 호출 -> close / exception handling
    f.write("Context Manager Test3")

