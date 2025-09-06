"""
AsyncIO(비동기 입출력)
코루틴에서 확장
I/O 작업을 coroutine으로 처리
Generator -> 반복적 객체 / return 사용
non-blocking I/O -> 비동기 처리

Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때 까지 제어권을 갖고 있음 (다른 함수는 대기)
Non-Blocking I/O : 호출된 함수가  return 후 호출한 함수(main routine)의 제어권 전달 -> 타 함수는 일 지속

스레드 : 디버깅, 자원 접근시 race condition, 교착상태 발생 가능(dead lock) 고려 후 코딩
coroutine : 디버깅, 자원 접근시 위 사항 없음 -> 단일 스레드 기반 -> 사용 함수가 비동기로 구현 되어 있어야 함 or 직접 비동기로 구현
"""

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import ssl, certifi
from functools import partial

"""
신뢰 CA 컨텍스트 생성
파이썬 내장 ssl 모둘 함수
HTTPS 통신 시 사용할 SSLContext 객체를 생성.
SSLContext는 인증서 검증, 암호화 방식, 키 파일 같은 걸 관리하는 “TLS 설정 객체”라고 보면 됨.
create_default_context():  운영체제나 지정된 CA(인증서 발급기관) 목록을 불러와서 기본적으로 안전한 검증 규칙을 가진 컨텍스트를 만들어 줌
cafile=certifi.where() : 신뢰할 수 있는 CA 인증서 목록을 제공하는 certifi 패키지 사용
"""
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

# 실행 시작 시각
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트 실습
# 동시 실행 -> urlopen blocking I/O -> Thread를 사용 해 urlOpen을 따로 빼서 처리
urls = ["https://www.daum.net", "https://naver.com", "https://google.com"]


async def fetch(url, executor) :
    # thread 디버깅
    print('Thread Name : ', threading.current_thread(), 'Start', url)

    # 실행
    # loop는 main 영역에서 선언 했기 떄문에 사용 가능
    fn = partial(urlopen, url, timeout=10, context=SSL_CTX)
    res = await loop.run_in_executor(executor, fn)

    print('Thread Name : ', threading.current_thread(), 'Done', url)

    # 결과 반환
    return res.read()[0:6]

# 비동기 처리 함수
async def main() :
    # non-blocking I/O
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합 (future에 있는 값을 모아서, 끝날때 까지 unpacking)
    rst = await asyncio.gather(*futures)

    print('result : ', rst)

if __name__ == '__main__' :
    # loop 초기화
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Running Time : ', duration)

