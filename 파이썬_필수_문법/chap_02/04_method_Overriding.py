"""
Overriding(오버라이딩)
- 1. subClass에서 superClass의 Method를 호출 후 사용
- 2. superClass의 Method를 재정의
- 3. 부모 클래스의 메소드를 추상화 후 사용가능 (구조적 접근)
- 4. 확장 가능, 다형성 (다양한 방식으로 동작)
- 5. 가독성 증가, 오류 가능성 감소, 메서드 이름 절약, 유지보수성 증가

OOP

다형성
"""
# ex 1
# 기본 Method Overriding

class ParentEx1 :
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

# 상속
class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

# 부모 클래스 메서드 호출
print(c1.get_value())  # 5
print(p1.get_value())  # 5

# c1의 모든 속성 출력
print(dir(c1)) # 'get_value', 'value' 포함
print()

# 부모와 자식의 모든 속성 값 출력
print(dir(ParentEx1))
print(dir(ChildEx1))
print()

# 자식의 NameSpace에는 뭐 없음
# 인스턴스화 될떄 NameSpace가 생성됨
print(ParentEx1.__dict__)
print(ChildEx1.__dict__)

# ex 2
# 기본 Overriding 메서드 재정의
class ParentEx2 :
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

# 부모꺼를 재정의
class ChildEx2(ParentEx2):
    # 메서드 재정의
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()
print(c2.get_value())

# 다형성
import datetime

class Logger :
    def log(self, msg):
        # 출력은 내가
        print(msg)

# 기록
class TimestampLogger(Logger) :
    def log(self, msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now(), msg = "{msg}")
        # super().log(message)
        # 정확한 자식 클래스, 인스턴스
        super(TimestampLogger, self).log(message)

class DateTimeLogger(Logger) :
    def log(self, msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now().strftime('%Y-%m-%d'), msg = "{msg}")
        # super().log(message)
        # 정확한 자식 클래스, 인스턴스
        super(DateTimeLogger, self).log(message)

l1 = Logger()
t1 = TimestampLogger()
d1 = DateTimeLogger()

l1.log("Hello")
t1.log("Hello")
d1.log("Hello")