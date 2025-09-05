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
"""

# Print

# 기본 출력
print("Hello Python Basic1")
# 작은 따음표를 많이 사용
print('Python start')
print('''Python Start''')
print("""Python Start""")
print() # 개행

# Separator
# sep -> 출력 사이에 넣을 문자열
print('p', 'y', 't', 'h', 'o', 'n')
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '8888', sep='-')
print('python', 'gmail.com', sep='@')
print()

# End
# end 옵션이 들어가면 다음 프린트 문에 이어줄 수 있음
print('welcome to', end=' ')
print('IT News', end=' ')
print('web site')
print()

# File
# import -> 파일을 불러오는 명령어
import sys

# 현재 내용을 내부 파일에 쓸 것이다. 콘솔 창에는 안나와도 됨
#sys.stdout -> 콘솔 out
print('learn python', file=sys.stdout)  # 표준 출력
print()

# format (d, s, f)
# d -> 정수, s -> 문자열, f -> 실수
# s를 제외한 d, f는 명시적으로 d, f를 사용해야 함
# %가 연결해주는 다리 같은 것, 첫번째 s -> one 두번째 s -> two
print('%s %s' % ('one', 'two'))
# format 함수를 사용한 방법
print('{} {}'.format('one', 'two'))
# 순서를 지정해서 사용 가능
print('{1} {0}'.format('one', 'two'))
print()

# %s
# 양수일때는 오른쪽, 음수는 왼쪽 정렬 / > 오른쪽, 아무것도 붙지 않았을 때는 왼쪽 정렬
# 정수, 리스트, 객체 모두 가능.
# 10칸을 확보하고 오른쪽 정렬
print('%10s' % ('python'))
print('{:>10}'.format('nice'))

# 왼쪽으로 정렬
print('%-10s' % ('python'))
print('{:10}'.format('nice'))

# 공백을 다른 문자로 채우기
print('{:_>10}'.format('nice'))

# 중양 정렬
print('{:_^10}'.format('nice'))

# .이 붙으면 문자열의 길이를 제한
print('%.5s' % ('nice'))
print('%.5s' % ('pythonStudy'))
# 공간은 있고, 5글자 까지만 나오는 것
print('{:10.5}'.format('pythonStudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%f' % (3.141592))
print('{:f}'.format(3.141592))
# 정수 & 소수 둘다 출력
print('%1.2f' % (3.141592))
# 소수점 2자리 까지만 출력
print('%.2f' % (3.141592))
print('{:.2f}'.format(3.141592))
# 6자리 까지 출력 하는데 소수점 2자리 까지 출력, 정수부 한자리만 있기 때문에 나머지 부분은 0으로 채움
print('%06.2f' % (3.141592))
print('{:06.2f}'.format(3.141592))
