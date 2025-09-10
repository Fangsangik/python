"""
Queue and Pipe
"""

# Pipe
from multiprocessing import Process, Pipe, current_process
import time
import os


# 실행함수
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0
    for i in range(baseNum):
        sub_total += i

    # Produce
    conn.send(sub_total)
    conn.close()

    print("id : {}, name : {}, pid : {}, sub_total : {}".format(id, process_name, process_id, sub_total))
    print("Result : ", sub_total)

def main():
    parent_process_id = os.getpid()
    print("Parent process id : ", parent_process_id)
    process_list = []

    # 시작 시간
    start_time = time.time()

    """
    프로세스가 실행되는 동시에, Join은 완료 될 때까지 대기 
    while True에서 get으로 가져오고, 
    kill이면 종료 / 아니면 total에 더해준다.
    """

    # Pipe 선언
    # 부모와 자식 양방향 통신
    # send / recv
    parent_conn, child_conn = Pipe()

        # 생성
    p = Process(name= str(1), target=worker, args=(1, 100000000, child_conn))

    # 시작
    p.start()

    # Join
    p.join()

    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))
    print()

    print("Main processing total cnt ={}".format(parent_conn.recv()))
    print("Main processing end")

# Main 시작
if __name__ == "__main__":
    main()