"""
Descriptor vs Property
Low Level (descriptor) vs High Level (property)
Descriptor 예제 심화

디스크립터
1. 상황에 맞는 메서드 구현을 통한 객체지향 프로그래밍 구현
2. Property와 달리 reuse 가능
3. ORM framework 사용
"""

# ex1
# Descriptor 예제(1)
import os

class DirectoryFileCount :
    def __get__(self, obj, objType = None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    # Discriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname

# 현재 경로
s = DirectoryPath('./')
# 이전 경로
g = DirectoryPath('../')
print(s.size)
print(g.size)

# 출력 용도
print(dir(DirectoryPath))
print(DirectoryPath.__dict__)
print(dir(s))
print(s.__dict__)

# ex2
# Descriptor 예제(2)
import logging
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objType=None):
        logging.info("Accessing %r giving %r", 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info("updating %r giving %r", 'score', value)
        self.value = value

"""
가장 중요한 Descript 할 필드 
변수와 메서드 따로 정리 
"""
class Student:
    # Descriptor instance
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        self.name = name
        self._score = 0

s1 = Student('Kim')
s2 = Student('Park')

print(s1.score)
s1.score = 100
print(s1.score)

print(s2.score)
s2.score += 30
print(s2.score)

print(vars(s1))
print(vars(s2))
print(s1.__dict__)
print(s2.__dict__)

