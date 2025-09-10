"""
ProcessPoolExecutor
as_completed
Futures Object
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS = [
    'http://www.foxnews.com',
    'http://www.cnn.com',
    'http://europe.wsj.com',
    'http://www.bbc.co.uk',
    'http://some-made-up-domain.com/'
]


# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        # 읽어서 전체를 return
        return conn.read()


def main():
    # 프로세스풀 context 영역
    with ProcessPoolExecutor(max_workers=5) as executor :
        # Future 로드 (실행X)
        # key : executor.submit(load_url, url, 60)
        # value : url
        future_to_url = {executor.submit(load_url, url, 60) : url for url in URLS}

        # 실행
        for future in as_completed(future_to_url) :
            # key값이 Future 객체
            url = future_to_url[future]

            try:
                # 결과
                data = future.result()
            except Exception as e:
                print(f"{url} generated an exception : {e}")
            else :
                print(f"{url} page is {len(data)} bytes")

if __name__ == "__main__":
    main()
