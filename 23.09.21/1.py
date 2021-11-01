class Name():
    def __init__(self, name):
        self.__hidden_name = name
    

    def get_name(self):
        print("getter")
        return self.__hidden_name
    def set_name(self, name):
        print("setter")
        self.__hidden_name = name
    name = property(get_name, set_name)
n = Name("ya")
n.name = "oper"
print(n.name)
print(Name)