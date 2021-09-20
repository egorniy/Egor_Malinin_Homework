class Person():
    def __init__(self, name):
        self.name = name
    def exclaim(self):
        print("I'm a person with name ", self.name)

class Student():
    def __init__(self, name):
        self.name = name
    def exclaim(self):
        print("I'm a person with name ", self.name, "but i want to sleep more")
p = Person ('Лана дель рэй')
s = Student ('Алевтина')
p.exclaim()
s.exclaim()

isinstance(s,Student)

