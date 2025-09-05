"""
future : 동시성
- concurrent.futures : 병렬 작업
비동기 작업 실행
지연시간(block) CPU 및 리소스 낭비 방지 -> file I/O, 네트워크 I/O, 웹 크롤링, 빅데이터 처리, 머신러닝 -> 동시성 활용 권장
비동기 작업과 적합한 프로그래밍일 경우 압도적으로 성능 향상

futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
concurrent.futures

멀티 스레딩 / 멀티 프로세싱 API 통일 -> 사용하기 쉬움
실행중인 작업 취소, 완료 여부 체크, 타입아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> promise 개념

GIL : Global Interface Lock -> 두개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점 방지
    / 즉 리소스 전체에 락 & Context Switching 비용 발생

GIL 우화 : 멀티 프로세싱, CPython
"""

# 2가지 pattern 학습
# concurrent.futures map
# concurrent.futures wait, as_completed

"""
하나의 작업으로 인해 다른 작업이 밀리면 안됨 -> wait
작업의 실패 했을때 실패한 값을 일일히 확인 
"""
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST =[1000, 20000, 300000, 400000, 5000000000]

# 동시성 합계 메인 함수
# 누적 합계 합수 (제너레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))

# wait : 시간을 제어하는데 사용 가능
# as completed : 먼저 끝나는대로 반환 / as completed 호출 되기 전에 완료한 모든 퓨처들이 먼저 yield 됨
def main():
    # worker count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # future
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor, ThreadPoolExecutor
    # 수치 연산의 경우 CPU가 더 빠름 / Deep Learning, AI -> GPU

    # with futures.ThreadPoolExecutor() as executor:  # Thread
    with ProcessPoolExecutor() as executor: # Process
        for work in WORK_LIST :
            # future 반환
            future = executor.submit(sum_generator, work)

            # scheduling
            futures_list.append(future)

            # scheduling 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # wait 결과 출력
        # 7초가 over가 되면 Timeout
        result = wait(futures_list, timeout = 7)

        # 성공
        print('Completed Tasks : {}' + str(result.done))

        # 실패
        print('Pending ones : {}' + str(result.not_done))

        # 결과값 출력
        print([future.result() for future in result.done])

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 format
    msg = '\n time : {:.2f} seconds'

    # 최종 결과 출력
    print(msg.format(end_tm))

# 실행
# 첫 시작점
if __name__ == '__main__':
    main()