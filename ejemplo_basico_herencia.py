class Guerrero:
    def atacar(self):
        print("Ataca con espada ⚔️")

class Mago:
    def lanzar_hechizo(self):
        print("Lanza una bola de fuego 🔥")

# Herencia Múltiple: Esta clase hereda de DOS padres
class CaballeroMistico(Guerrero, Mago):
    pass

personaje = CaballeroMistico()
personaje.atacar()          # Viene de Guerrero
personaje.lanzar_hechizo()  # Viene de Mago