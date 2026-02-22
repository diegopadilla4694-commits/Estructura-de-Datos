class Num:
    def __init__(self, val = 1):
        if val % 2 != 0:
             self.numA = 1
        else:
             self.numB = 1

example = Num(float(input("ingrese un numero: ")))

try:
     print(example.numA)
except AttributeError:
    print("Digito no encontado")

try:
    print(example.numB)
except AttributeError:
    print("Digito no encontrado")