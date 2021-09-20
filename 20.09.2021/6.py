import math
class Circle():
    def __init__(self, d, r ):
        self.d = d
        self.r = r
    def get_l(self):
        return math.pi*self.d
    def get_pl(self):
        return math.pi*self.r**2

c = Circle(5, 3)
print(c.get_l())
print(c.get_pl())