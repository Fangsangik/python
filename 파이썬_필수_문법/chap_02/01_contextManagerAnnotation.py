"""
Decorator
contextlib.contextmanager
@contextlib.contextmanager, __enter__, __exit__
"""

"""
가장 대표적인 with 구문 이해 
contextlib decorator 
코드 직관적, 예외 처리 
"""
import time
import contextlib

# ex1
# Use Decorator
# enter, exit가 어딘지
# @contextlib.contextmanager : 따로 __enter__, __exit__를 만들지 않아도 됨, 이미 클래스로 구현 되어 있음
@contextlib.contextmanager
def my_file_writer(file_name, method) :
    f = open(file_name, method)
    yield f # __enter__ -> f return
    f.close() # __exit__ -> close

with my_file_writer('testfile4.txt', 'w') as f:
    f.write("Context Manager Test4")

# ex2
# Use Decorator
@contextlib.contextmanager
def my_timer(msg):
    start = time.monotonic()
    try:
        yield start # __enter__ -> start return

    except BaseException as e:
        print(f"Error Occurred: {e}")
        raise

    else :
        print('{} : {}s'.format(msg, time.monotonic() - start))

with my_timer("Start Job2") as v:
    print("do something : {}".format(v) )
    for i in range(1000000000):
        pass
    raise Exception("raise error")
