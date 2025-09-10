"""
process id
process Naming
process parallelism
"""

from multiprocessing import Process, current_process
import os
import time
import random
from multiprocessing.process import parent_process


# 실행
def square(n):
    # random sleep
    time.sleep(random.randint(1, 5))
    process_id = os.getpid()
    process_name = current_process().name
    result = n * n
    print(f"process id : {process_id}, process name : {process_name}, input : {n}, result : {result}")


# main 함수
if __name__ == "__main__":
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent process id : {parent_process_id}")

    # 프로세스 리스트
    processes = []
    # 10개의 프로세스 생성
    for i in range(1, 10):
        # 프로세스 생성
        p = Process(target=square, args=(i,), name=str(i))
        # 프로세스 리스트에 추가
        # 한번에 담았다가 join
        processes.append(p)
        # 프로세스 시작
        p.start()

    for process in processes:
        process.join()

    # 종료
    print("Main process end")
