"""
CLASS
ex) 붕어빵 틀
OOP 객체지향 프로그래밍 -> self, instance 변수 / 메소드
class 와 인스턴스 차이
class 변수: 직접 접근이 가능, 공유
인스턴스 변수 : 객체마다 값이 다름
"""

# 예제
class Dog : # class (Object를 상속)
    # 클래스 속성 (클래스 변수)
    species = 'first Dog'

    # 초기화 인스턴스 속성 (자바에서의 생성자)
    def __init__(self, name, age) :
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('멍멍이', 3)
b = Dog('바둑이', 5)
c = Dog('멍멍이', 3)

# 비교
print(a == b) # False
print(a == b, id(a), id(b)) # False
print(a == c, id(a), id(c)) # 값은 같을 수 있지만 객체의 값은 다르다

# 네임스페이스 (class가 갖고 있는 속성을 확인 할 수 있음)
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'first Dog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print()

# 예제 2
# self 이해하기 : self가 붙으면 나만의 instance
class SelfTest :
    # TypeError: SelfTest.func1() takes 0 positional arguments but 1 was given
    # self는 인스턴스를 요구
    # 클래스 내부에 매개변수 X => 클래스 메소드 / 클래스로 바로 호출
    def func1():
        print('func1')

    # 인스턴스 매서드
    def func2(self):
        print(id(self))
        print('func2')

f = SelfTest()

print(dir(f))
print(id(f))
f.func2()
# 클래스에 바로 접근해서 호출 가능
SelfTest.func1()
print()

# 예제 3
# 클래스 변수와 인스턴스 변수
class Warehouse :
    # 클래스 변수
    stock_num = 0

    # 초기화
    def __init__(self, name) :
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Kim')
user2 = Warehouse('Lee')
user3 = Warehouse('Park')
print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user3.name)
print(user1.__dict__) # 클래스 변수가 확인 되지 않는 이유는 -> 모두 공유하기 때문에 굳이 표기 X
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__) # 'stock_num': 3, '
print(user1.stock_num)

del user1
print(Warehouse.__dict__) # 메모리에서 하나 지움
print()

# 예제 4
class Dog2 : # class (Object를 상속)
    # 클래스 속성 (클래스 변수)
    species = 'first Dog'

    # 초기화 인스턴스 속성 (자바에서의 생성자)
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def info (self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

# 인스턴스 생성
c = Dog2('Charlie', 4)
# 메소드 호출
print(c.info())
print(c.speak('멍멍')) 
