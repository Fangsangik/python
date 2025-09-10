"""
Queue and Pipe
"""

# Queue
from multiprocessing import Process, Queue, current_process
import time
import os


# 실행함수
def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0
    for i in range(baseNum):
        sub_total += i

    # Produce
    q.put(sub_total)

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
    # Queue 선언
    q = Queue()
    for i in range(5):
        # 생성
        p = Process(target=worker, args=(i, 100000000, q))

        # 배열에 담기
        process_list.append(p)

        # 시작
        p.start()

    # Join
    for process in process_list:
        process.join()

    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))

    # 종료 flag
    q.put("kill")

    # 대기
    # 하나의 프로세스가 종료되면 q에 값을 넣어주고
    # Join은 Join대로 기다린다.
    # 완료 되면 q에서 값을 꺼내서 total에 더해준다.

    total = 0

    while True:
        tmp = q.get()
        if tmp == "kill":
            break
        else:
            total += tmp
    print()

    print("Main processing total cnt ={}".format(total))
    print("Main processing end")

# Main 시작
if __name__ == "__main__":
    main()