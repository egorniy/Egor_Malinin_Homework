class Field():
    __pos_hare=0
    __pos_tort=0
    def __init__(self,n,m,x):
        if n<=m:
            print('PLOXO')
            return
        self.__step_hare =n
        self.__step_tort=m
        self.__length=x
    def get_pos_hare(self):
        return self.__pos_hare
    def get_pos_tort(self):
        return self.__pos_tort 
    def step(self):
        hare_new_pos =self.__pos_hare + step.__step_hare

f=Field(5,2,1)
first_meet +=0

