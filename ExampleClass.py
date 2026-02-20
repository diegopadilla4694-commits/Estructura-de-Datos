class My_clase:
    def __init__(self, name = "Diego"):
        self.__Name = name
    
    def first_name(self, fst = "Padilla"):
        self.__Fst = fst

object_1 = My_clase()
object_2 = My_clase("Padilla")

object_2.first_name("López")

object_3 = My_clase("Fernando")
object_3. __lst = "Fer"

print(object_1.__dict__)
print(object_2.__dict__)
print(object_3.__dict__)