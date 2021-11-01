import random
class Car ():
    def __init__(self, speed, name, mark):
        self.speed = speed
        self.name = name
        self.mark = mark

c1 = Car(random.randint(1,50),'L666KJ','m.video')
c2 = Car(random.randint(1,50), 'L123DF','Audi')
pos1 = 0
pos2 =0
while True:
    if (pos1+c1.speed) > (pos2+c2.speed):
        print('Win ',c1.mark,c1.name)
        break
    else:
        print('Win ', c2.mark, c2.name)
        break