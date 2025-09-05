"""
while 기본 사용법
Break, Continue
While-else
무한 반복 구문
기본 패턴 실습
"""

# While <expr> :
#       <statement>:
n = 5
while n > 0:
    n = n - 1
    print(n, end=' ')
print()

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1), end=' ')
print()

# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended')
print()

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop ended')
print()

# if 중첩
i = 1
while i <= 10 :
    print('i : ', i)
    if i == 6:
        break
    i += 1
print()

# while-else
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')
print()

a = ['foo', 'bar', 'baz', 'qwer']
s = 'qwer'
i = 0

while i < len(a) :
    if a[i] == s :
        print('Found it')
        break
    i += 1
else:
    print('Not found')
print()

# 무한반복 조심
# while True:
a = ['foo', 'bar', 'baz']
s = 'bar'

while True:
    # a가 비어있다면
    if not a :
        break
    print(a.pop())

