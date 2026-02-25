class Nombre:
    def __init__(self, nom):
        self.__nombre = nom
    
    def complete_name(self, middle, first, last):
        self.__middle_name = middle
        self.__first_name = first
        self.__last_name = last
    
    def __str__ (self):
        return "Mi nombre es " + self.__nombre + self.__middle_name + self.__first_name + self.__last_name + "."
    

class Sub_Name(Nombre):
    def __init__(self, nom):
        super().__init__(nom)
        self.complete_name(" Fernando", " Padilla", " López")

obj = Sub_Name("Diego")
print(obj)