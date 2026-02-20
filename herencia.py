class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El {self.marca} {self.modelo} esta encendido. "

class Coche(Vehiculo):
    def tocar_claxon(self):
        return "Beep beep"

mi_coche = Coche("Honda", "Civic")

print(mi_coche.arrancar())
print(mi_coche.tocar_claxon())