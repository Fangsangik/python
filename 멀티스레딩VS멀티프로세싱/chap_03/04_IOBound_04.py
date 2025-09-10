"""
예제 3-4. Sync / Async
"""

# 서버에 접속해서 관련 정보를 가져옴
import time
import asyncio

"""
동시 프로그래밍 페러다임이 변화 
싱글 코어 : 처리 향상 미미, 저하 -> 비동기 프로그래밍 -> CPU 연산이나, DB 연동, API 호출 대기시간 늘어남 
파이썬 3.4 -> 비동기 asyncio 등장 

def -> 동기 
async def -> 비동기 -> 다른 비동기 함수에서 다른 비동기 함수 call -> await
async + await -> coroutine
"""

# 비동기 처리
async def exe_calculate_sync(name, n):
    for i in range(n, n + 1):
        print(f"{name} -> {i} of {n} is calculating...")
        await asyncio.sleep(1)
    print(f"{name} done...")


async def proc_sync():
    start = time.time()

    await asyncio.wait([asyncio.create_task(exe_calculate_sync('A', 3)),
                        asyncio.create_task(exe_calculate_sync('B', 2)),
                        asyncio.create_task(exe_calculate_sync('C', 1))])

    end = time.time()
    print("Total Time : ", end - start)

# 동기처리
"""def exe_calculate_sync(name, n):
    for i in range(n, n + 1):
        print(f"{name} -> {i} of {n} is calculating...")
        time.sleep(1)
    print(f"{name} done...")


def proc_sync():
    start = time.time()
    exe_calculate_sync('A', 3)
    exe_calculate_sync('B', 2)
    exe_calculate_sync('C', 1)
    end = time.time()
    print("Total Time : ", end - start)"""


if __name__ == "__main__":
    # sync
    # proc_sync()

    # async
    # 3.7 이상에서는 실행 방법이 쫌더 쉬움
    asyncio.run(proc_sync())
    # asyncio.get_event_loop().run_until_complete(proc_sync())
