class Person():
    def init(self,name):
        self.name = name
class Student(Person):
    homework = 0
    kn = 0
    def get_kn(self):
        self.kn +=1
    def get_homework(self, n):
        self.homework += n
    def do_homework(self):
        if self.homework > 0:
            self.homework-=1
        else:
            print("Ну вот и все")
class Teacher(Person):
    work=0
    def give_kn(self,pupils):
        for pupil in pupils:
            pupil.get_kn()
            self.work +=1
def give_homework(self,*pupils,n):
    for pupil in pupils:
        pupil.get_homework(n)
        self.work+=1
s=Student('Грыша')
p=Teacher('Лади Гагалина')
s.give_kn(s) 
p.give_kn(p.kn)

