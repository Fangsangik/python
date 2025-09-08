"""
Pythonic Code
@Property
- 장점 :
1. 파이써닉한 코드
2. 변수에 제약을 설정
3. Getter, Setter 효과 동등 (코드 일관성)
  - 캡슐화 & 유효성 검사 기능 추가 용이
  - 대체 표현 (속성 노출, 내부에 표현을 숨기기 가능)
  - 속성의 수명 및 메모리 관리 용이
  - 디버깅 용이
  - Getter, Setter 작동에 대해 설계된 라이브러리(오픈소스) 상호 운용성 증가

Getter & Setter
"""


# 파이썬 함수의 Getter Setter 표준
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        print("Called Get Method")
        return self.__y

    @y.setter
    def y(self, value):
        print("Called Set Method")
        self.__y = value

    @y.deleter
    def y(self):
        print("Called Delete Method")
        del self.__y


a = SampleA()
a.x = 10
a.y = 20
print(a.x)
print(a.y)

del a.y  # a_SampleA__y 객체가 있어야 하는데 없음
print(dir(a))


# property 활용
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private (제약 조건을 걸 수 있음)

    @property
    def y(self):
        # print("Called Get Method")
        return self.__y

    @y.setter
    def y(self, value):
        # print("Called Set Method")
        if value < 0:
            raise ValueError("0보다 작은 값은 허용하지 않습니다.")
        else:
            self.__y = value

    @y.deleter
    def y(self):
        # print("Called Delete Method")
        del self.__y


b = SampleB()
b.x = 1
b.y = -1