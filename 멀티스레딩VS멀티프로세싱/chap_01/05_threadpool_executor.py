"""
Many Threads,
concurrent.futures,
(xxx)PoolExecutor

Group Thread
1. 파이썬 3.2 이상에서 사용 가능
2. concurrent.futures 모듈 사용
3. .with 사용으로 스레드를 생성하거나 소멸, lifeCycle 관리
     - Debugging 어려움
4. 대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 반환 -> 단일화(capsulation)
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    logging.info("Sub Thread %s: starting", name)
    result = 0
    for i in range(1, 10000):
        result += i
    logging.info("sub_thread %s : finishing result %d", name, result)
    return result

def main() :
    # Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main Thread : before creating and running thread")

    # 실행 방법 1
    # max_workers : 작업의 개수가 넘어가면, 작업 설정이 유리
    """    
    executor = ThreadPoolExecutor(max_workers=3)
        for task_name, i in zip(["A", "B", "C", "D", "E"], range(5)):
            executor.submit(task, task_name)
    """

    # 실행 방법 2
    # with 구문 사용
    with ThreadPoolExecutor(max_workers=3) as executor :
        tasks = executor.map(task, ["A", "B", "C", "D", "E"])
        logging.info("Main Thread : wait for the results %s", tasks)

if __name__ == "__main__" :
    main()