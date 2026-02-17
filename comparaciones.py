import math

def calculo(bloques):
    h = (-1 + math.sqrt(1 + 8*bloques)) / 2
    return int(h)


Bloques = int(input("Ingrese la cantidad de bloques: "))
resultado = calculo(Bloques)

print(f"La altura de la piramide con {Bloques} en la piramide es de {resultado} de alto")