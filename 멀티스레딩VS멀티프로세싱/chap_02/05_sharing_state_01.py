"""
Memory Sharing
Share Array
Share Value
"""

from multiprocessing import Process, current_process
import os
from multiprocessing.process import parent_process


# 프로세스 Memory 공유 X

# 실행 함수
def generate_number(v: int) :
    for _ in range(50) :
        v += 1
    print(current_process().name, "data", v)

def main() :
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f"Parent Process ID : {parent_process_id}")

    # process list
    process_list = []

    # 프로세스 메모리 공유 변수
    shared_value = 0
    for _ in range(1, 9):
        # 생성
        p = Process(target=generate_number, args=(shared_value,))
        process_list.append(p)
        # 실행
        p.start()

        for p in process_list :
            p.join()

        # 최종 프로세스 부모 변수 확인
        # 공유가 안되는 상황 / 프로세스는 독립된 메모리 공간을 가지기 때문
        print("Final Parent Process Value : ", shared_value)

if __name__ == "__main__":
    main()

