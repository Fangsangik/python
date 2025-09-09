"""
type(name, base, dct)
Dynamic Metaclass
메타 클래스 코딩 이점

type이 class를 만들어 내고, class의 meta는 type이다

메타 클래스
1. 메타클래스 동적 생성
2. 동적 생성한 메타 클레스 -> 커스텀 메타 클래스 생성
3. 의도하는 방형으로 직접 클래스 생성에 관여 할 수 있는 큰 장점
"""

# ex1
# type 동적 클래스 생성
# type(name(이름), bases(상속), dict(속성, 메서드))
# 이 코드 자체가 클래스르 만든 것
s1 = type('sample1', (), {}) # class sample1 : pass
print(s1) # <class '__main__.sample1'
print(type(s1))
print(s1.__bases__) # (<class 'object'>, )
print(s1.__dict__)
print()

# 동적 생성 + 상속
class Parent1:
    pass

# Sample2를 만들고 attr1, attr2 속성을 추가
# 동적으로 활용 할 수 있기 때문에 for문이나 다른 코드드로 클래스 생성 가능
s2 = type('sample2',
          (Parent1,),
          dict(attr1 = 100, attr2 = 'hi'))
print(s2) # <class '__main__.sample2'>
print(type(s2))
print(s2.__bases__)
print(s2.__dict__)
print(s2.attr1, s2.attr2) # 접근 가능
print()

# type 동적 클래스 생성 + 메서드 동적 생성
class SampleEx:
    attr1 = 30
    attr2 = 100

    # 정적
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

ex = SampleEx()
print(ex.attr1)
print(ex.attr2)
print(ex.add(100, 200))
print(ex.mul(100, 200))
print()

s3 = type('sample3',
          (object, ),
          dict(attr1 = 30, attr2 = 100, add = lambda x, y : x + y, mul = lambda x, y : x * y))
          # {'attr1' : 30, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y}
print(s3)
print(s3.attr1)
print(s3.attr2)
print(s3.add(100, 200))
print(s3.mul(100, 200))
