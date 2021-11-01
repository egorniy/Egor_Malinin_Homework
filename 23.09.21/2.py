class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Parent(Person):
    def __init__(self, name, age, hair, eyes):
        super().__init__(name, age)
        self.hair = hair
        self.eyes = eyes
import random
class Children(Person):
    def __init__(self, name, age, p1, p2):
        super().__init__(name, age)
        hair_1,eyes_1 = p1.hair,p1.eyes
        hair_2,eyes_2 = p2.hair,p2.eyes
        self.hair  = random.choice([hair_1, hair_2])
        self.eyes = random.choice([eyes_1, eyes_2])
p1 = Parent('Dorian', 84, 'brown', 'blue')
p2 = Parent('Grey', 12, 'black', 'grey')
c = Children('Cristian-akakiy', 11, p1, p2)
print(c.eyes)