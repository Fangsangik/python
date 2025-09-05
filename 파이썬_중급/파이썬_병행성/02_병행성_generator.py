"""
병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시 실행  -> 단일 프로그램에서 여러일을 쉽게 해결
병렬성(Parallelism) : 여러 컴퓨터가 여러 일을 동시 실행 -> 속도
"""

# Generator ex1
# yield : return + 중간 상태 저장 (중간에 멈추고 다음 명령어가 나올 때 까지 대기)
def generator_ex1():
    print('Start')
    yield 'A point'
    print('Continue')
    yield 'B point'
    print('End')

temp = iter(generator_ex1()) # 제너레이터 객체 반환 / 중간 점을 기억해서 다음에 이어서 실행
print(next(temp)) # Start -> A point
print(next(temp))
# print(next(temp)) # StopIteration
print()

for v in generator_ex1():
    print(v)

# Generator ex2
# yield -> return
temp2 = [x * 3 for x in generator_ex1()]
temp3 = [x * 3 for x in generator_ex1()]

print(temp2)
print(temp3)
print()

for i in temp2:
    print(i)

for i in temp3:
    print(i)

# Generator function
# filterfalse : 조건에 맞지 않는 값 반환, accumulate : 누적 합계, chain : 연결, product : 데카르트 곱, groupby : 그룹화
import itertools
gen1 = itertools.count(1, 2.5) # 무한대
print(next(gen1))
print(next(gen1))

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5)) # 1000 미만
for v in gen2:
    print(v)
print()

# filterfalse : 반대 값
gen3 = itertools.filterfalse(lambda x : x < 1000, [10, 200, 3000, 400, 5000, 600, 7000])
for v in gen3:
    print(v)
print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
    print(v)
print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

# 연결2
# enumerate : 인덱스 + 값
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# product : 데카르트 곱 (개별 튜프를 각각 반환)
gen7 = itertools.product('ABCDE', range(1, 11, 2))
print(list(gen7))

# repeat : 반복
gen8 = itertools.product('A', repeat = 4) # A를 10번 반복
print(list(gen8))

# groupby : 그룹화 (반드시 정렬 후 사용)
gen9 = itertools.groupby('AAABBBCCCDDEEE') # 연속된 값만 그룹화
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))