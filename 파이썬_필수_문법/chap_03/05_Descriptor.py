"""
Descriptor
1. 객체에서 서로 다른 객체를 속성 값으로 갖는 것
2. Read, Write, Delete 기능을 미리 정의 가능
3. data descriptor (set, del), non-data descriptor (get)
4. 일기 전요 객체 생성 장점, 클래스를 의도 하는 방향으로 생성 가능
"""


# ex1
# 기본적인 Descriptor 예제
class DescriptorEx1:
    def __init__(self, name='Object'):
        self.name = name

    def __get__(self, obj, objType):
        return "get method called -> self: {}, obj: {}, name: {}".format(self, obj, objType)

    def __set__(self, obj, name):
        print('Set method called')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name must be String type')

    def __delete__(self, obj):
        print('Delete method called')
        del self.name

class Sample1:
    # name을 handling 할때는 DescriptorEx1이 호출
    name = DescriptorEx1()

s1 = Sample1()
s1.name = 'Python'  # set method called
# s1.name = 100     TypeError: Name must be String type

# attr 확인
# __get__ 호출
print(s1.name)

# __delete__ 호출
del s1.name

# ex2
# Property 사용 + Descriptor
# class property(fget=None, fset=None, fdel=None, doc=None)
# DescriptorEx2 -> property 역할도 하고, class 역할도 함

"""
property는 데이터 디스크립터다(__get__/__set__/__delete__ 보유).
파이썬의 속성 조회/할당 규칙상, 데이터 디스크립터가 있으면 인스턴스 __dict__보다 우선한다.
→ 즉 self.name = value는 인스턴스 딕셔너리에 키를 만드는 게 아니라, 항상 setter(setVal)를 호출

setVal() 내부에서 다시 self.name = value를 하면?
→ 또 같은 setter가 호출됨 → 다시 self.name = value → … 무한 재귀 → RecursionError

__init__에서 self.name = value도 마찬가지로 첫 호출 트리거가 된다.
→ 결국 초기화 시점부터 같은 재귀가 시작.
"""
class DescriptorEx2:
    def __init__(self, value):
        self._name = value

    def getVal(self):
        print('get method called')
        return self._name

    def setVal(self, value):
        print('set method called')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name must be String type')

    def delVal(self):
        print('delete method called')
        self.name = None

    # property 함수로 get, set, del 기능 연결
    name = property(getVal, setVal, delVal, 'Property example')

# 값 확인
s2 = DescriptorEx2("Descriptor Test2")
print(s2.name)  # get method called -> Descriptor Test2
s2.name = "New Name"  # set method called
print(s2.name)  # get method called -> New Name


