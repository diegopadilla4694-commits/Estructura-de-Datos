class Stack:
    def __init__ (self):
        print("¡Hola!")
 
 
stack_object = Stack()
 
class Perro:
    def __init__(self, nom, ra, col, age):
        print("GUAU")
        self.__nombre = nom
        self.__raza = ra
        self.__color = col
        self.__edad = age
    
    def obtener_nombre(self):
        return f"{self.__nombre},{self.__raza},{self.__color},{self.__edad}" 


animal = Perro("Candy", "Freish Maltes", "Blanco", 10) 

#print(animal.__nombre, animal.__raza, animal.__color, animal.__edad) 
"""este solo se utiliza cuando es publico o protegido """

print(animal.obtener_nombre())