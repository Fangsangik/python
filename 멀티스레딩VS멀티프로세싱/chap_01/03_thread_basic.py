"""
기초 Thread
Main Thread vs Sub(Child) Thread

Main Thread 작업은 끝났지만 Sub Thread 작업이 끝나지 않으면 Sub Thread는 본인의 작업이 끝날 때까지 종료되지 않는다.

10:41:39: Main Thread : before creating thread
10:41:39: Main Thread : before running thread
10:41:39: Sub Thread First : starting
10:41:39: Main Thread : waiting for thread to finish
10:41:39: all done
10:41:42: Sub Thread First : finishing

"""

import logging
import threading
import time

def thread_func(name):
    logging.info("Sub Thread %s : starting", name)
    time.sleep(3)
    logging.info("Sub Thread %s : finishing", name)

# Main Thread
if __name__ == "__main__" :

    #Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main Thread : before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))
    logging.info("Main Thread : before running thread")

    # 서브 스레드 시작
    # 서브 스레드 작업이 끝날 때까지 메인 스레드 대기
    x.start()
    x.join()
    logging.info("Main Thread : waiting for thread to finish")

    logging.info("all done")
