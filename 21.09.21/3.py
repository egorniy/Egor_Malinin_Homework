class Field():
    __pos_hare=0
    __pos_tort=0
    
    def __init__(self, n, m, x):
        self.__step_hare = n
        self.__step_tort = m
        if n<=m:
            print('fghjk')
            return
        self.__pos_hare=n
        self.__pos_tort=m
        self.__lenght=x
    def get_pos_hare(self):
        return self.__pos_hare
    def get_pos_tort(self):
        return self.__pos_tort
    def step(self):
        hare_new_pos = self.pos_hare+self.step_hare
        if hare_new_pos>self.__lenght:
            hare_new_pos-=self.__lenght
        self.__pos_hare=hare_new_pos
    def step(self):
        tort_new_pos = self.__pos_tort+self.__step_tort
        if tort_new_pos>self.__lenght:
            tort_new_pos-=self.__lenght
        self.__pos_tort=tort_new_pos


f = Field(5, 2, 11)
i = 0
first_meet = 0
while(i<100):
    f.step()
    i += 1
    if f.get_pos_hare() == f.get_pos_tort():
        print('meet', i- first_meet)
        first_meet = i