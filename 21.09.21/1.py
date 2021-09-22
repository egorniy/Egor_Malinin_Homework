class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age  
    def getname (self):
        return self.__name
    def getage (self):
        return self.__age

    def set_name (self, new_name, new_age):
        self.__name = new_name
    def set_age (self, new_age):
        self.__age = new_age



st= Person('Гордон', 23)
print(st.getname(),st.getage())