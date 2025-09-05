# advanced tuple
# unpacking
# b, a = a, b

# divmod -> 몫과 나머지 반환
print(divmod(100, 9))
# *를 붙이면 unpacking
print(divmod(*(100, 9)))  # unpacking
print(*(divmod(100, 9)))  # unpacking
print()

# rest
# x, y, rest = range(10) # Error -> ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)  # 나머지 값들은 리스트로 반환
print(x, y, rest)

x, y, *rest = range(2)  # 나머지 값들은 리스트로 반환
print(x, y, rest)

x, y, *rest = [1, 2, 3, 4, 5]  # 나머지 값들은 리스트로 반환
print(x, y, rest)
print()

# mutable -> 변경 가능 / immutable -> 변경 불가
l = (15, 20, 25) # tuple -> immutable
m = [15, 20, 25] # list -> mutable
print(l, id(l))
print(m, id(m))

# 곱해서 새로운 변수에 재할당
l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2 # 불변형이기 때문에 새로운 객체 생성
m *= 2 # 가변형이기 때문에 기존 객체에 값만 변경
print(l, id(l))
print(m, id(m))
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...
# sorted -> 정렬 후 새로운 객체로 반환 (원본은 그대로 유지)  / sort -> 정렬 후 객체를 직접 변경 (원본 변경)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('original - ', f_list)
print('sorted - ', sorted(f_list)) # 정렬 후 새로운 객체로 반환
print('reversed sorted - ', sorted(f_list, reverse=True)) # 정렬 후 새로운 객체로 반환
print('key=len - ', sorted(f_list, key=len)) # 단어 길이 장렬
print('key=len - ', sorted(f_list, key=lambda x: x[-1], reverse=True)) # 단어 마지막 글자 기준 정렬
print()

# sort
print('sort - ', f_list.sort(), f_list) # None 반환 -> 객체 직접 변경 (원본 변경)
print('sort - ', f_list.sort(reverse=True), f_list) # None 반환 -> 객체 직접 변경 (원본 변경)
print('sort - ', f_list.sort(key=len), f_list) # 단어 길이 정렬
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list) # 단어 마지막 글자 기준 정렬
print()

# List vs Array
# List -> 융통상, 다양한 data type, 범용적 사용
# 숫자 기반 -> Array (고성능 연산), 리스트와 호환 
