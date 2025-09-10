"""
Daemon Thread
1. Background 실행
2. Main Thread 종료 시 즉시 종료
3. Background 무한 대기 이벤트 발생시 실행하는 부분 담당 -> GC(가비지 컬렉터) 역할, 자동 저장 등
4. 일반 스레드는 작업 종료시
"""

import logging
import threading
import time

def thread_func(name, d):
    logging.info("Sub Thread %s : starting", name)
    for i in d:
        print(i, "", end="")
    logging.info("Sub Thread %s : finishing", name)

# Main Thread
if __name__ == "__main__" :

    #Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main Thread : before creating thread")

    # 함수 인자 확인
    # daemon=True : 데몬 스레드로 설정 -> 메인 스레드 종료 시 즉시 종료 / daemon=False(기본값) : 일반 스레드
    x = threading.Thread(target=thread_func, args=('First',range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second',range(10000)), daemon=True)
    logging.info("Main Thread : before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # Daemon Thread인지 확인
    # print(x.isDaemon())

    # 서브 스레드 작업이 끝날 때까지 메인 스레드 대기
    # daemon Thread인데 join을 사용 하는 것은 권장하지 않음
    # daemon Thread는 메인 Thread가 종료되면 즉시 종료되기 때문에 join을 사용할 필요가 없음
    x.join()
    y.join()

    logging.info("Main Thread : waiting for thread to finish")

    logging.info("all done")
