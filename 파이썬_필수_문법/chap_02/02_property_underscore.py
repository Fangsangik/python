"""
class형 코딩 -> property, underscore
access modifier, underscore
"""

# ex1
# 1. interpreter, 값 무시, 네이밍(국제화, 자리수)

# unpacking
# _ : 값 무시
x, _, y = (1, 2, 3)
print(x, y)

# packing 처리 되면서 값 무시
a, *_, b = (1, 2, 3, 4, 5)
print(a, b)

for _ in range(1, 10) :
    pass

# enumerate :
for _, val in enumerate(range(20)):
    pass

# ex2
"""
접근 지정자
name : public
_name : protected
__name : private
파이썬 -> public 강제 X , 약속된 규약에 따라 코딩 장려(자유도, 책임감)
타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함) -> Naming Mangling
타 클래스 __ 접근하지 않는 것이 원칙 
"""

class sampleA :
    def __init__(self):
        self.x = 10          # public
        self._y = 20         # protected
        self.__z = 30        # private

a = sampleA()
a.x = 1
print(a.x)
# protected와 private는 직접 접근하지 않는 것이 원칙 / 수정은 가능 그리고 강제성은 없음
a._y = 2
print(a._y)
# a.__z = 3
# print(a.__z)  # AttributeError: 'sampleA' object has no attribute '__z'
print(dir(a))

# ex3
# 메서드 활용 Getter, Setter
class SampleB :
    def __init__(self):
        self.x = 0
        self.__y = 0 # SampleB__y

    # Getter
    def get_y(self):
        return self.__y

    # Setter
    def set_y(self, value):
        self.__y = value

# b._SampleB__y = value 직접 접근 가능은 하지만 권장하지 않음

b = SampleB()
b.x = 1
b.set_y(2)
print(b.x)
print(b.get_y())

# 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락
# b._SampleB__y = 3
print(dir(b))