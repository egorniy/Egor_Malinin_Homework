class Summator(): #Объявляем класс и называем
    def init(self, a, b): #Объявляем функцию
        self.a = a  #Пишем, что а=а
        self.b = b #а б=б
    def return_sum(self): #объявляем еще одну функцию, которая вернет сумму а и б

        return self.a  + self.b

s = Summator(1,3) #Пишем из чего состоит класс сумматор, а =1, б=3

print(s.return_sum()) #Применяем функцию и возвращаем ее значение от s