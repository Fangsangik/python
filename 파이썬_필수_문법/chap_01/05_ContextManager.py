"""
context manager2(컨텍스트 매니저)
타이머 클래스
contextlib 구현 : Measure execution time
"""

import time
from contextlib import contextmanager

# ex1
# with문 안에서 수행을 해도 실행 시간 측정 가능
class Timer :
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        # 들어가는 시점에 시작 시간을 기입
        self.start = time.monotonic()
        return self.start

    # exc_tb : traceback -> 오류가 발생했을 때 오류에 대한 정보를 담고 있음 (debugging)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.monotonic()
        print(f"{self.msg} : {self.end - self.start:.5f} sec")
        # 예외가 발생했을 때 처리
        if exc_type :
            print("Error Type : ", exc_type)
            print("Error Value : ", exc_val)
            print("Error Traceback : ", exc_tb)
        else:
            # 종료시간 - 시작시간 = 수행시간
            print("No Error", self.msg, time.monotonic() - self.start)

        return True

with Timer('start job') as v:
    print("do something")

    # execute job
    for i in range(10000):
        pass
    raise Exception("raise error")




