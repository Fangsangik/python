"""
class of class
type, meta class
custom meta class

메타 클래스
1. 클래스를 만드는 역할
    - 의도한는 방향으로 클래스르 커스텀 하겠다
2. 프레임워크 작성시 필수
3. 동적 생성을 가능하게 해줌, 커스텀 생성 함수
4. 커스텀 클래스 -> 검증 클래스
5. 엄격한 클래스 사용 요구, 메서드 오버라이드 요구
"""

# ex1
# type
# 모든 클래스의 원형이 되는 것은 type
class SampleA:
    pass

# 현실에 있는 obj을 코딩 형식으로 옮기는 것 -> 객체지향
# 파이썬에서는 클래스와 객체를 동일하게 취급 (class == object)
# 클래스를 인스턴스화 했다
# 변수에 할당, 복사, 새로운 속성 추가, 함수의 인자로 넘기기 가능
obj1 = SampleA()
obj2 = SampleA()

# obj1 -> SampleA
# SampleA -> type meta class
# type -> type meta class
print(obj1.__class__) # <class '__main__.SampleA'> 만들어진 원형을 알려줌
print(type(obj1))  # <class '__main__.SampleA'> 자료형이 뭐인지 알려줌
print(obj1.__class__ is type(obj1)) # True
print(obj1.__class__.__class__ is type(obj1).__class__) # <class 'type'>
print(type.__class__) # <class 'type'>

# ex2
# 메타 클래스
# int, dict
n = 10
d = {'a' : 10, 'b' :20}

class SampleB() :
    pass

obj3 = SampleB()

# 모든 클래스의 원형이 type
for o in (n, d, obj3) :
    print('Ex - {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))

for t in int, float, list, tuple:
    print('Ex - {} {}'.format(t, isinstance(t, type))) # True

