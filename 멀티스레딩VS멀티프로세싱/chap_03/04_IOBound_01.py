"""
synchronous I/O-bound
"""

# 서버에 접속해서 관련 정보를 가져옴
import requests
import time


# download
def request_site(url, session):
    print(session)
    print(session.headers)

    with session.get(url) as response:
        print(f"Read : {len(response.content)}, status code : {response.status_code} from {url}")


# 실행 함수
# request session이 살아있는 동안 처리
def request_all_sites(urls):
    with requests.session() as session:
        for url in urls:
            request_site(url, session)


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