class Counter():
    __hidden_count = 0
    def count(self):
        self.__hidden_count += 1
    def counter_to_zero (self):
        self.__hidden_count = 0
    def get(self):
        return self.__hidden_count
    def set(self,n):
        self.__hidden_count = n
c=Counter()
c.count()
print(c.get)