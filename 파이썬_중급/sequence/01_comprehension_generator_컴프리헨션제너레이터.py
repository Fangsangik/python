"""
순서가 있고, List 같은 경우 = mutable = 변경 가능, 제힐딩, 추가, 삭제 가능

1. container : 서로 다른 자료형을 담을 수 있음 (ex. list, tuple, collections.deque)
2. flat : 한 가지 자료형만 담을 수 있음 (ex. str, bytes, bytearray(메모리 효율성 (자연어 처리), array.array, memoryview)
가변형 : list, bytearray, array.array, collections.deque
불변형 : tuple, str, bytes, memoryview
"""
import array

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!~?><:'
code_list1 = []

for s in chars:
    # ord() : 문자의 유니코드 값을 반환
    code_list1.append(ord(s))
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
# filter
code_list3 = [ord(s) for s in chars
              if ord(s) > 40]
print(code_list3)

# filter + map
code_list4 = list(filter
                  (lambda x : x > 40, map(ord, chars)))

# map
code_list5 = list(map(ord, chars))
print(code_list5)

# 유니코드 -> 문자얄
print([chr(s) for s in code_list1])
print()

# Generator (local 상태를 유지, 값을 반환) / (한번에 한개의 반환할 값만 갖고 있음) / (메모리 유지 X)
# 제너레이터는 전체 데이터를 한 번에 메모리에 로드하지 않고 요청이 있을 때마다(yield) 값을 생성
# 대량의 데이터를 다룰 때 메모리를 매우 효율적으로 사용
# 메모리 소비
tuple_x = [ord(s) for s in chars]
print(tuple_x)

tuple_x1 = (ord(s) for s in chars)
print(tuple_x1)
print(type(tuple_x1))
print(next(tuple_x1)) # next -> 다음 값 반환
print(next(tuple_x1)) # next -> 다음 값 반환

array_g = array.array('I', (ord(s) for s in chars))
print(type(array_g))
print(array_g)
print(array_g.tolist()) # tolist() : array -> list
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s, end=' ')
print()
print()

# 리스트 사용시 주의
# 깊은 복사, 얕은 복사
mark1 = [['~'] * 5 for s in range(3)] # id 값이 각각 다름
mark2 = [['~'] * 5] * 3 # 하나의 주소 값이 복사됨 -> id 값이 모두 같음

print(mark1)
print(mark2)

# 수정
mark1[0][1] = 'X'
mark2[0][1] = 'O'
print(mark1)
print(mark2)

# 증명
print([id(i) for i in mark1]) # id 값이 각각 다름
print([id(i) for i in mark2]) # 하나의 주소 값이 복사됨 -> id 값이 모두 같음
