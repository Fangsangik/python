"""
예제 I/O 바운드 Threading 예제
"""

# 서버에 접속해서 관련 정보를 가져옴
import requests
import time
import concurrent.futures
import threading

# 각 스레드에 생성되는 객체
# 독립적인 변수를 생성 가능
thread_local = threading.local()

"""
첫번째 thread 도착 후 -> 독립된 nameThread에 어떤 값을 저장하는 변수 
"""
def get_session():
    if not hasattr(thread_local, "session"):
        # session에 request session을 담아서 -> 반환
        # 두번째 스레드도 접근 시 새로 만들지 않고 반환 하면 됨
        thread_local.session = requests.Session()
    return thread_local.session

# download
def request_site(url):

    # 세션 획득
    # 별도에 header 값을 요청 해야 하는 경우
    session = get_session()

    # 세션 확인
    with session.get(url) as response:
        print(f"Read : {len(response.content)}, status code : {response.status_code} from {url}")

# 실행 함수
# request session이 살아있는 동안 처리
def request_all_sites(urls):
    # 멀티 스레드 실행 (많아도 적어도 문제)
    # 반드시 max_workers 조절 필요
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor :
        executor.map(request_site, urls)


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
    request_all_sites(urls)

    # 실행 종료
    duration = time.time() - start_time

    print()
    print(f"Downloaded: {len(urls)} sites in {duration:.2f} seconds")


if __name__ == "__main__":
    main()
