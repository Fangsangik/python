"""
퍼아썬 패키지
파이썬은 패키지로 분할 된 개별적인 모듈로 구성
상대경로 : .. -> 상위 디렉토리로 이동 / . -> 현재 디렉토리 (생략 가능)
패키지 : __init__.py 파일이 있는 디렉토리

__init__.py : python 3.3 이후로는 없어도 패키지로 인식 단 하위 호환을 위해서는 만드는 것을 추천 / 빈 파일이 없으면 import 시 에러 발생
__all__ : 외부에서 import 할때 허가 해주는 기능 / __all__ = ['mod1_test1', 'mod1_test2'] -> test1, test2만 허용
"""

# 예제 1

# 사용
파이썬_기초_문법.chap8.sub.sub1.module1.mod1_test1()
파이썬_기초_문법.chap8.sub.sub1.module1.mod1_test2()
파이썬_기초_문법.chap8.sub.sub2.module2.mod2_test1()
파이썬_기초_문법.chap8.sub.sub2.module2.mod2_test2()
print()

# 예제 2
# 길어질 경우 불편 -> from 키워드로 모듈을 가져오기 (간단하게)
from sub1 import module1
from sub2 import module2 as m2 # as 키워드로 모듈 이름 변경 가능

# 사용
module1.mod1_test1()
module1.mod1_test2()
m2.mod2_test1()
m2.mod2_test2()
print()

# 예제 3
# 전부 사용 할 것이라면 나이스
# 너무 전체를 계속 가져올 경우 메모리 성능 저하 가능성
from sub1.module1 import *
from sub2.module2 import *

# 사용
mod1_test1()
mod1_test2()
mod2_test1()
mod2_test2()