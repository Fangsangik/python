"""
다양한 Print 출력
Separator, End, Python Format 사용

Escape Code
/n -> 개행
/t -> 탭
\\ -> 문자
\' -> 문자
\" -> 문자
\000 -> 널 문자 (아무것도 없는 문자)

파이썬 3가지 Formating 방법
"""

# 3가지 Formating 방법
x =50
y = 100
text = 308276767
n = 'Fang'

# 출력 1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력 2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=(x + y))
print(ex2)

# 출력 3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)
print()

# 구분기호
m = 100000000
print(f'm : {m:,}')

# 정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬
t = 20
print(f't : {t:<10}')  # 왼쪽 정렬
print(f't : {t:>10}')  # 오른쪽 정렬
print(f't : {t:^10}')  # 가운데 정렬
print()

print(f't center : {t:-^10}')  # 가운데 정렬


