"""
type inheritance
custom meta class
메타 클래스 상속 실습

메타클래스 상속
1. type 클래스 상속
2. metaclass 속성 사용
3. custom meta class 생성
    - 클래스 생성 가로체기 = intercept
    - 클래스 수정 하기 (modify)
    - 클래스 개선 (기능 추가)
    - 수정된 클래스 반환 
"""


# ex1
# custom meta class (type 클래스 상솟 X)
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list를 상속 받음, 메서드 2개 추가
# 형태는 여기서 정의
Custom_list = type('Custom_list', (list,),
                   {'desc': 'custom list',
                    'cus_mul': cus_mul,
                    'cus_replace': cus_replace})

# 초기화 할때 list를 넣어주고,
# 클래스 안에 self를 호출 하는 것은 초기화 값이 나온다.
# list 클래스를 상속받았기 때문에 list가 갖고 있는 메서드도 사용 가능
c1 = Custom_list(range(11))  # 초기화
c1.cus_mul(10)
c1.cus_replace(0, 90)
c1.cus_replace(10, "hello")  # 없는 값이기 때문에 변화 없음
print(c1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 90, 100]
print(c1.desc)  # custom list
print(dir(c1))  # list가 갖고 있는 메서드도 사용 가능 (기본 메서드 + 커스텀 메서드)
print()

# ex2
"""
메타 클래스는 사용자가 고려할 필요 없음 
굳이 필요하지는 않음 

# custom meta class 생성 예제 (type 상속 O)
class MetaClassName(type) :
    def __new__(metacls, name, bases, namespace):
"""


# new -> list -> call
# type을 사용하긴 하는데 type을 사용한 meta
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __new__(metacls, name, bases, namespace):
        print("__new__ -> ", metacls, name, bases, namespace)
        namespace['desc'] = 'custom list2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespace)

    # 클래스 인스턴스 생성 (메모리 초기화)
    def __init__(self, obj_or_name, bases, dict):
        print("__init__ -> ", self, obj_or_name, bases, dict)
        super().__init__(obj_or_name, bases, dict)


    # 인스턴스 실행
    # 메타클래스에서 __call__을 오버라이딩하면 인스턴스 생성 과정 전체를 직접 컨트롤하는 거라 return이 필수.
    def __call__(self, *args, **kwargs):
        print("__call__ -> ", self, *args, **kwargs)
        return super().__call__(*args, **kwargs)


CustomList2 = CustomListMeta('CustomList2',
                             (list,),
                             {})

c2 = CustomList2(range(11))
c2.cus_mul(10)
c2.cus_replace(0, 90)
print(c2)  # [90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 상속 확인
print(CustomList2.__mro__)