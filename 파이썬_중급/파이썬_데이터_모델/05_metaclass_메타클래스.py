# namedTuple 실사용
# 반 20명 / 4개의 반 (A, B, C, D)
from collections import namedtuple

Classes = namedtuple('Classes', ['rank', 'number'])

# 리스트 준비
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
# 기존 리스트(또는 이터러블)를 한 줄로 가공해 새 리스트를 만드는 파이썬 구문.
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in
                    [str(n) for n in range(1, 21)]]
print(len(students2))
print(students2)
