"""
CPU Bound

프로세스에 i/o 대부분의 실행의 시간을 CPU에서 작업
"""

import time

def cpu_bound(n) :
    return sum(i * i for i in range(n))

def find_sums(n) :
    result = []
    for number in n:
        result.append(cpu_bound(number))

    return result

def main() :
    numbers = [10000000 + x for x in range(20)]
    print(numbers)

    # 살행 시간
    start_time = time.time()

    # 실행
    total = find_sums(numbers)
    print()

    print(f"total list : {total}")
    print(f"sum : {sum(total)}")

    # 실행시간 종료
    duration = time.time() - start_time
    print()

    # 수행 시간
    print(f"수행 시간 : {duration}")


if __name__ == "__main__":
    main()




