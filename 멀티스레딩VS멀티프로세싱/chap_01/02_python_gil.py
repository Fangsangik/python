"""
python's GIL (Global Interpreter Lock) 설명
cPython
gil vs thread
gil details

1. GIL(Global Interpreter Lock)
- CPython이 Code를 해석 -> Python(bytecode) 실행시 여러 스레드를 사용 할 경우, 멀티스레드에 접근 해도 하나의 스레드가 Python object 접근하게 제한하는 mutex
- CPython 메모리 관리가 취약 (Thread safe)
- 단인 스레드로 충분히 빠르다
- 프로세스 사용 가능 (Numpy, Scipy)등 Gil 외부 영역에서 효율적 코딩
- 병렬 처리는 MultiProcessing 사용 권장, Asyncio (비동기 처리) 권장
- Thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python
"""