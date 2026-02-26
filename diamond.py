class Guerrero_legendario_mistico:
    def __init__(self):
        self.habilidades = []
        self.catalogos = {"Mago": ["Hechizo", "Alumbrar"], 
                          "Paladin_mistico": ["Estocada Suprema", "Escudazo Supremo"],
                          "Jinete_Mistico": ["Cabalgar", "Estocada", "Velocidad"]
                          }
        
        
class jinete_mistico(Guerrero_legendario_mistico):
     def movimientos_J(self, seleccion):
        self.habilidades.append(f"Poder jinete : {seleccion}")
        print("Fase Platino")
          


class Paladin_mistico(Guerrero_legendario_mistico):
    def movimientos_P(self, seleccion):
        self.habilidades.append(f"Poder espadachin : {seleccion}")
        print("Fase Dorada")


class mago(Guerrero_legendario_mistico):
    def movimientos_M(self, seleccion):
        self.habilidades.append(f"Poder mago : {seleccion}")
        print("Fase Plata")


class Personaje_Principal(mago, Paladin_mistico, jinete_mistico):
    def __init__(self, nombre):
         super().__init__()
         self.nombre = nombre

    def mostrar_habilidades(self):
        print(f"\n--- Personaje: {self.nombre} ---")        
        print(f"Habilidades aprendidas: {','.join(self.habilidades) if self.habilidades else 'Ninguna'}")


def menu():
    nombre = input("Ingrese el nombre de su personaje: ")
    heroe = Personaje_Principal(nombre)
        
    continuar = True
    while continuar:
        print("\n ===== Menu de aprendizaje =====")
        print("1. Habilidades del mago: ")
        print("2. Habilidades del Paladin mistico: ")
        print("3. Habilidades del Jinete Mistico: ")
        print("4. Mi personaje")

        opcion = input("Selecciona alguna de las siguentes opciones (1-4): ")

        if opcion == "4":
             continuar = False
             continue
        
        ramas = {"1": ("Mago", heroe.movimientos_M),
                 "2": ("Paladin_mistico", heroe.movimientos_P),
                 "3": ("Jinete_Mistico", heroe.movimientos_J)}
        
        if opcion in ramas:
             nombre_rama, metodo_aprender = ramas[opcion]
             habls = heroe.catalogos[nombre_rama]

             print(f"\nDisponibles: {habls}")
             eleccion = input(f"¿Cual quieres aprender? ").capitalize()


             if eleccion in habls:
                  metodo_aprender(eleccion)
                  print(f"Has aprendido {eleccion}!")
             else:
                print("Esa habilidad no existe en esta rama")
        else:
             print("Opcion no valida")

    heroe.mostrar_habilidades()

menu()
             
            
                  
    