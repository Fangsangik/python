"""
Overloading,
- 1. 동일 메서드 재정의
- 2. 네이밍 기능 예측
- 3. 코드 절약과 가독성 향상
- 4. 메서드 파라미터 기반 호출 방식 (파라미터 개수에 따라서 자신에게 알맞는 메서드 호출)

oop, multipleDispatch
"""
# ex 1
# 동일 이름 메서드 사용 예제
# 동적 타입 검사 -> 런타임에 실행 (타입 에러가 실행시에 발견)
# 클래스 내에서 메서드 오버로딩 지원 X -> multiple Dispatch을 활용해 메서드 오버로딩 구현
class SampleA() :
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # packing
    # 묶어서 하나로 보내기 때문에
    # def add(self, *args):
        # 여기서 unpacking
    #    return sum(args)

a = SampleA()
# print(a.add(3, 3))
print(dir(a)) # -> add : 파라미터 3개 짜리

# ex 2
# 동일 이름 메서드 사용 예제
# 자료형에 따른 분기 처리
class SampleB() :
    def add(self, datatype, *args):
        if datatype == 'int' :
            return sum(args)

        if datatype == 'str' :
            return ''.join([x for x in args])

b = SampleB()
print(b.add('int', 3, 3))
print(b.add('str', 'hello', " " ,'world'))

# ex 3
# dispatch 활용
from multipledispatch import dispatch

class SampleC :
    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z

    @dispatch(str, str)
    def product(x, y):
        return x + y

c = SampleC()
print(c.product(3, 3))
print(c.product(3, 3, 3))
print(c.product(3.0, 3.0, 3.0))
print(c.product('hello', 'world'))
