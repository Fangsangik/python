"""
예제 3-4. I/O 바운드 Multiprocessing 예제
"""

# 서버에 접속해서 관련 정보를 가져옴
import requests
import time
import multiprocessing


"""
프로세스에서 어떤 객체를 생성하는 것은 비용이 많이 듬
미리 생성을 해서 할당 -> 공유되는 것과는 다름 
"""
# 객체를 미리 생성
session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

# download
def request_site(url):

    # 세션 확인
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"[{name} -> Read : {len(response.content)}, status code : {response.status_code} from {url}]")

# 실행 함수
# request session이 살아있는 동안 처리
def request_all_sites(urls):
    # 멀티 프로세싱 실행  (많아도 적어도 문제)
    # Process 개수 조절 . Session 객체 및 실행시간 확인
    # 동시성에서 순서를 보장 받을 수 없음
    # 초기화 할때 이미 함수를 만들고 실행흘 하기 때문에 각각의 프로세스가 돌아감
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool :
        pool.map(request_site, urls)


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
