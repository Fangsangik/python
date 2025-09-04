# Vector

class Vector:

    # packing을 한다고 가정 하고 -> unpacking
    def __init__(self, *args):
        '''
        Create a Vector, example : v = Vector(2,3)
        '''

        # 0을 대입 할 경우 error 방지
        if len(args) == 0 :
            self.x = 0
            self.y = 0
        else :
            self.x, self.y = args

    def __repr__(self):
        '''
        return the Vector information
        '''
        # %r : repr
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        '''
        return the vector addtion of self and other
        '''
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        '''
        return the vector multiplication of self and other
        '''
        return Vector(self.x * other.x, self.y * other.y)

    def __bool__(self):
        '''
        return the vector truth value
        max(self.x, self.y) -> 둘 중 큰 값을 반환
        (0, 0) 이면 False, 그 외는 True
        '''
        return bool(max(self.x, self.y))

# 메서드 내 주석 설명
print(Vector.__init__.__doc__)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector() # (0, 0)

print(v1, v2) # __repr__ 호출
print(v1 + v2) # __add__ 호출
print(v1 * v2) # __mul__ 호출
print(v1.x, v2.y) # 각각의 x, y 값 접근
print(bool(v1), bool(v2), bool(v3)) # __bool__ 호출