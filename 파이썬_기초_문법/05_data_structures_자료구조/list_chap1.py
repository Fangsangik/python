"""
리스트 : 순서, 중복, 삭제, 수정 모두 가능

리스트 사용법
리스트 선언
리스트 특징
리스트 인덱싱
리스트 슬라이싱
리스트 함수
리스트 삭제
"""

# List
a = []
b = list()
c = [1, 2, 3, 4]
d = [1000, 10000, 'Ace', 'Base', 'Captin']
e = [1, 2, 3, ['a', 'b', 'c']]
f = [21.42, 'foobar', 3, 4, False, 3.141592]

# indexing
print('>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
# 리스트 내부에 리스트의 경우 첫 리스트는 그냥 원소, 내부에 리스트는 인덱싱으로 접근
print('e - ', e[-1][1])
print('e - ', type(e[-1][1]))
print('e - ', type(list(e[-1][1])))
print()

# 슬라이싱
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[-1][1:3])
print()

# 리스트 연산
print('>>>>')
print(c + d)
print(c * 3)  # 순서는 유지
print(c + e[-1])
print('test' + str(c[1]))
print()

# 값 비교
print(c == c[:3] + c[3:])
print()

# Identity (Id)
print('>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

# 리스트 수정, 삭제
print('>>>>')
c[0] = 4
print('c - ', c)
# 슬라이싱 자리에는 원소
c[1:2] = [5, 6, 7]
print('c - ', c)
c[1:2] = [[5, 6, 7]]
print('c - ', c)
# 특정 자리에는 리스트
c[1] = [5, 6, 7]
print('c - ', c)
# 리스트 삭제 -> 이렇게 쓰지는 않음 / del
c[1:3] = []
print('c - ', c)
# 삭제
del c[2]
print('c - ', c)
print()

# 리스트 함수
# 데이터의 양이 많을 경우 sort, reverse는 시간이 많이 걸림
print('>>>>')
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b1 = [4, 8, 9, 3, 1, 7, 8, 9, 1, 5, 6]
print('a1 = ', a1)
print('a1 - ', len(a1))  # 길이
a1.append(11)
print(a1)
b1.sort()
print(b1)
a1.reverse()
print(a1)
print('a1 = ', a1.index(3), a1[3])
# 위치 + 추가 할 값
a1.insert(10, 7)
print('a1 - ', a1)
a1.reverse()
print('a1 - ', a1)
a1.remove(11)
print('a1 - ', a1)
# 기존에 마지막에 해당하는 원소를 가져오고 해당 원소 삭제
print('a1 - ', a1.pop())
print('a1 - ', a1)
# count
print('a1 - ', a1.count(7))  # 7의 개수

# extend (리스트 확장)
ex = [8, 9]
a1.extend(ex)
print('a1 - ', a1)

# 삭제 -> pop, remove, del
while a1 :
    data = a1.pop()
    if data == 2:
        break
    print(data)
print('a1 - ', a1)
