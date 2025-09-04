# 모듈 사용 실습
# 기본적 파이썬 엔진

import sys
import module

# import module 시 원하지 않게 나오는 문제
print(module.add(1, 2))  # 모듈 내 함수 호출
print("=" * 15)
print()

print(sys) # <module 'sys' (built-in)>
print(sys.path)
print(type(sys.path)) # <class 'module'>
sys.path.append('chap8')  # 모듈 경로 추가
print(sys.path)
print()
