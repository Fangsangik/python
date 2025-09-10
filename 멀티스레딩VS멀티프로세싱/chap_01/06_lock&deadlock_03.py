"""
lock, deadlock, race condition, synchronization

1. Semaphore
- 프로세스간 공유된 자원 접근시, 문제 발생 가능성
    - 한개의 프로세스만 접근 처리 고민(경쟁상태 예방)
2. Mutex
- 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막음 -> 경쟁 상태 예방
3. Lock
- 상호 배제를 위한 잠금 처리 -> 데이터 경쟁
4. Deadlock
- 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상태(교착 상태)
5. Thread Synchronization
- 스레드 동기화를 통해서 안정적으로 동작하게 처리한다 (동기화 메서드, 동기화 블럭)
6. semaphore vs mutex
- 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
- semaphore : 여러 스레드가 공유 자원에 접근 가능 (semaphore는 mutex가 가능)
- mutex : 한개의 스레드만 공유 자원에 접근 가능 (mutex는 semaphore가 불가능)
"""

import logging
import time
from concurrent.futures import ThreadPoolExecutor
import threading


class FakeDataStore:

    # 공유변수 (value)
    # Stack 영역 -> Data나 Heap 영역으로 data를 옮겨서 공유
    def __init__(self):
        # 공유되는 변수
        self.value = 0
        self._lock = threading.Lock()  # Lock 객체 생성

    # 변수 update
    # update 메서드를 실행하기 위해서는 stack 영역이 필요 -> 함수를 호출, 돌아가야 할 주소값 알아야 하고, 인자 값을 가져가야 하기 때문
    def update(self, n):
        logging.info('Thread %s: starting update', n)

        # 뮤택스 & Lock 동기화(synchronization 필요)
        # Lock 객체 생성

        # lock 획득 방법 2
        with self._lock:
            logging.info("Thread %s: has lock", n)

            local_copy = self.value  # local copy가 stack 영역에 저장
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info("Thread %s: has release lock", n)
        logging.info('Thread %s: finishing update', n)



if __name__ == "__main__":
    # Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # class instance
    store = FakeDataStore()
    logging.info("Tasking update. starting value is %d", store.value)

    # with context
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in ['First', 'Second', 'Third', 'Fourth', 'Fifth']:
            executor.submit(store.update, i)
    logging.info("Tasking update. Ending value is %d", store.value)
