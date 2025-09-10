"""
예제 3-5. AsyncIO 예제
"""

# 서버에 접속해서 관련 정보를 가져옴
import time
import asyncio
import aiohttp
import threading  # multiprocessing 대신 threading 사용

"""
threading 보다는 asyncio가 코드 복잡도는 더 높음 + Async await
"""

# download
async def request_site(session, url):

    print(session.headers)

    # 세션 확인
    async with session.get(url) as response:  # async with 사용
        print(f"[Read {0}, from {1}".format(response.content_length, url))


# 실행 함수
# request session이 살아있는 동안 처리
async def request_all_sites(urls):  # async 함수로 변경
    async with aiohttp.ClientSession() as session:
        
        tasks = []
        for url in urls:
            task = asyncio.create_task(request_site(session, url))  # create_task 사용
            tasks.append(task)

        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)  # *tasks 사용


def main():
    # test URLS
    urls = [
               "https://www.jython.org",
               "http://olympus.realpython.org/dice",
               "https://www.python.org",
           ] * 3

    # 실행 시간
    start_time = time.time()

    # 실행
    asyncio.run(request_all_sites(urls))

    # 실행 종료
    duration = time.time() - start_time

    print()
    print(f"Downloaded: {len(urls)} sites in {duration:.2f} seconds")


if __name__ == "__main__":
    main()