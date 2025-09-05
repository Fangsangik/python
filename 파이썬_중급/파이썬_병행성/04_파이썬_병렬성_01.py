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
# concurrent.futures 사용법 1
# concurrent.futures 사용법 2

import os
import time
from concurrent import futures

WORK_LIST =[10000, 200000, 3000000, 40000000, 500000000]

# 동시성 합계 메인 함수
# 누적 합계 합수 (제너레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))

def main():
    # worker count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor, ThreadPoolExecutor
    # 수치 연산의 경우 CPU가 더 빠름 / Deep Learning, AI -> GPU

    # with futures.ThreadPoolExecutor() as executor:  # Thread
    with futures.ProcessPoolExecutor() as executor: # Process

        # map은 작업 순서를 유지 -> 직시 실행
        result = executor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 format
    msg = '\n Result -> {} time : {:.2f} seconds'

    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 실행
# 첫 시작점
if __name__ == '__main__':
    main()
    