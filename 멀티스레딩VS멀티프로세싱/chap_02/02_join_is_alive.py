"""
multi-processing
join, is_alive
"""

from multiprocessing import Process
import time
import logging


def proc_func(name):
    logging.info("sub process starting % s", name)
    time.sleep(5)
    logging.info("sub process ending % s", name)


def main():
    # Logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))

    logging.info("Main Process : before creating Process")

    p.start()
    logging.info("Main Process : during Process")

    logging.info("Main Process : Terminated")
    # p.terminate()

    logging.info("Main Process : joined Process")
    p.join()

    # 프로세스 상태 확인
    logging.info("Process is alive %s", p)


# Main 시작
if __name__ == "__main__":
    pass
