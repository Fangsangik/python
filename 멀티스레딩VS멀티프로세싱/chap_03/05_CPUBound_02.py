"""
CPU Bound Multi Processing
Manager Shared Memory

CPU 바운드 작업은 대부분의 시간을 계산에 사용하며,
파일 압축은 CPU 성능에 크게 좌우되는 대표적인 계산 작업.
"""
import os
import time
from multiprocessing import current_process, Array, Manager, Process, freeze_support

def cpu_bound(n, total_list) :
    process_id = os.getpid()
    process_name = current_process().name

    # 결과
    print(f"process id : {process_id}, name : {process_name} -> {n}")

    total_list.append(sum(i * i for i in range(n)))

def main() :
    numbers = [1000000 + x for x in range(20)]
    print(numbers)

    # 프로세스 리스트 선언
    processes = list()

    # process 공유 메니저
    manager = Manager()

    # 리스트 획득 (프로세스 공유)
    total_list = manager.list()

    # 살행 시간
    start_time = time.time()

    # 프로세스 생성 & 실행
    for i in numbers : # 1 ~ 100
        # 생성
        p = Process(name = str(i), target= cpu_bound, args = (i, total_list,))
        processes.append(p)

        # 시작
        p.start()

    # Join
    for p in processes :
        p.join()

    print()

    print(f"total list : {total_list}")
    print(f"sum : {sum(total_list)}")

    # 실행시간 종료
    duration = time.time() - start_time
    print()

    # 수행 시간
    print(f"수행 시간 : {duration}")

if __name__ == "__main__":
    main()





