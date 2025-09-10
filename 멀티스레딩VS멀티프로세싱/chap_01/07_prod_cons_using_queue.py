"""
Queue
Python Event
Producer / Consumer Pattern (생산자 소지바 pattern)

Producer / Consumer Pattern (생산자 소비자 패턴)
1. MultiThreading, MultiProcessing 디자인 페턴의 정석
2. 서버 프로그래밍의 핵심
4. 주로 허리 역할

-> Python의 Event 객체
- Flag 초기 값(0)
- set() -> 1, clear() -> 0, wait() -> 0이면 대기, 1이면 진행, is_set() -> 현 Flag 상태 반환
"""

import concurrent.futures
import logging
import queue
import random
import threading
import time
from pyexpat.errors import messages


# 생산자
def producer(queue, event) :
    """
    네트워크 대기 상태라 가정 (서버)
    """
    # is_set() 기본 값 0 -> 생산을 하지 않는다
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info("Producer: 생산자 생성한 데이터 %s", message)
        queue.put(message)
        logging.info("Producer: 생산자 받은 데이터 %s", message)

    logging.info("Consumer: 소비자 종료")

# 소비자
def consumer(queue, event) :
    """
    응답 받고 소비하는 것으로 가정 or DB 저장
    """
    # 큐가 비어있으면 & event flag가 0이면 while문 돌지 않는다
    while not event.is_set() or not queue.empty() :
        message = queue.get()
        logging.info("Consumer: 소비자 받은 데이터 %s (size = %d)", message, queue.qsize())
    logging.info("Consumer: 소비자 종료")

# 큐 생성
if __name__ == "__main__" :
    # Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    # maxsize= x (큐의 사이즈가 운영하고자 하는 환경에 맞춰서 설정)
    # 제대로 활용 하지 못하면 -> 병목 현상 발생 or 소비자 측에서 제대로 소비하지 못함
    q_buffer = queue.Queue(maxsize=10)

    # event flag -> 초기값 0으로 setting이 되어 있음
    # Thread -> Consumer, Producer
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, q_buffer, event)
        executor.submit(consumer, q_buffer, event)

        while True :
            time.sleep(0.1)
            if q_buffer.empty() :
                logging.info("Main: 큐가 비었습니다")
                # set을 날리면 producer, consumer -> 1로 변경 되면서, program 종료
                event.set()
                break
            else :
                logging.info("Main: 큐에 데이터가 남아 있습니다. 소비자가 데이터를 소비할 때까지 기다립니다")
            if event.is_set() :
                break
    logging.info("Main: 프로그램 종료")

