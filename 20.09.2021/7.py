import math
class Triangle():
    def __init__(self, a, b,c,h ):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def get_s(self):
        return 1/2*self.a*self.h
    def get_p(self):
        return self.a+self.b+self.c

a = Triangle(5, 8,4,9)
print(a.get_s())
print(a.get_p())
