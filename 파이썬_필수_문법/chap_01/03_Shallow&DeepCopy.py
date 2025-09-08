"""
겍체의 복사 종류 (ccpy, shallow copy, deep copy) - 정확하게 알고 사용 해야함

copy :
shallow copy :
deep copy :
"""
import copy

# copy
# call by value, call by reffernce, call by share
a_list = [4, 5, 6, [7, 8, 9]]
b_list = a_list

# 같은 id 값 참조
print(id(a_list))
print(id(b_list))

b_list[2] = 100
print(a_list)
print(b_list)

b_list[3][0] = 700
print(a_list)
print(b_list)
print()

# immutable : str, float, boolean, unicode, tuple
# mutable : list, set, dict, byte array

# ex2 - shallow copy
# 가변형 객체 list나 참조형에 대해 주소 값까지 다른 값으로 복사하지는 않는다.
# 중첩문의 경우 주소 값을 공유
c_list = [4, 5, 6, [7, 8, 9]]
# 데이터 보호 차원에서 사본을 만들어서 copy package 사용 -> 주소값 다르게 사용
d_list = copy.copy(c_list)
print(id(c_list))
print(id(d_list))

d_list[2] = 100
print(c_list)
print(d_list)

"""
1차 list의 경우 각각 다른 주소 값을 공유 하지만, list in list의 경우 같은 주소 값을 공유
"""
d_list[3].append(10000)
d_list[3][1] = 800
print(c_list)
print(d_list)
print()

# ex3 - deep copy
# 중첩된 객체나 list들은 모두 다른 객체로 복사
e_list = [4, 5, 6, [7, 8, 9]]
f_list = copy.deepcopy(e_list)
print(id(e_list))
print(id(f_list))
f_list[2] = 100
print(e_list)
print(f_list)
f_list[3].append(10000)
f_list[3][1] = 800
print(e_list)
print(f_list)


