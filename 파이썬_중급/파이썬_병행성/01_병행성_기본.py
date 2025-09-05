"""
병행성 (Concurrency)
iterator :  반복 가능한 객체
generator : 반복 가능한 객체를 return 하는 함수

파이썬에서 반복 가능한 함수 : collections, text file, list, dict, set, tuple, unpacking, *args...-> iterator
"""

# 반복 가능한 이유 -> __iter__() 함수가 있으면 반복 가능한 객체
t = 'ABCDEFGOPQRSTUVWXYZ'
print(dir(t))  # __iter__ 있음 -> 반복 가능한 객체

for i in t:
    print(i)
print()

# 증명
# while
w = iter(t)
print(dir(w))  # __next__ 있음 -> iterator

# for문에서 돌아가는 것과 같음 (for 문에 내부적 원리)
while True:
    try:
        print(next(w))
    except StopIteration: # 예외 처리
        break
print()

# 반복형 확인
# hasattr : 속성 확인
print(hasattr(t, '__iter__')) # True
print(hasattr(t, '__next__')) # False
print()

from collections import abc
print(isinstance(t, abc.Iterable))
print()

# next pattern
class WordSplitter :
    def __init__(self, text) :
        self._idx = 0 # 0 idx 부터 시작
        self._text = text.split(' ')

    def __next__(self) :
        try:
            word = self._text[self._idx] # 현재 인덱스 단어
        except IndexError :
            raise StopIteration('stop iteration')
        self._idx += 1
        return word

    def __repr__(self) :
        return 'WordSplitter(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

# generator pattern
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양이 방대 할 경우 메모리 효울성
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각을 처리하는 파이프라인 구현에 적합

class WordSplitGenerator :
    # idx 없어도 됨
    def __init__(self, text) :
        self._text = text.split(' ')

    def __iter__(self) :
        for w in self._text :
            yield w # 제너레이터 / return 없어도 됨

    def __repr__(self) :
        return 'WordSpiltGenerator(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg) # iter로 감싸야함
print(wt)
print(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))