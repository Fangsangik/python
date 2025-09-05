# 예제 (매직 메서드 실습)

class Fruit :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    def __str__(self) :
        return "fruit Class Info : {} , {}".format(self.name, self.price)

    """
    self : s1 / other : s2
    """
    def __add__(self, other):
        print('called add')
        return self.price + other.price

    def __sub__(self, other):
        print('called sub')
        return self.price - other.price

    # <=
    def __le__(self, other):
        print('called <= ')
        if self.price <= other.price :
            return True
        else :
            return False

    # >=
    def __ge__(self, other):
        print('called >= ')
        if self.price >= other.price :
            return True
        else :
            return False

    # <
    def __lt__(self, other):
        print('called < ')
        if self.price < other.price :
            return True
        else :
            return False

    # >
    def __gt__(self, other):
        print('called > ')
        if self.price > other.price :
            return True
        else :
            return False

    # *
    def __mul__(self, other):
        print('called * ')
        return self.price * other.price

s1 = Fruit("Apple", 1000)
s2 = Fruit("Banana", 2000)

print(s1 + s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)

