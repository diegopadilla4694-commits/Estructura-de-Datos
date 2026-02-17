#Metodo Constructor
class Carreras():
     """nombre = "Ingeniera Civil"
     creditos = "100"
     Escuela = "CUCEI" 
     """

     def __init__(self, nom, cre, Esc):
         print("Asignacion de recursos")
         self.nombre = nom  
         self.creditos = cre
         self.Escuela = Esc
    
     #Metodo Destructor
     def __del__(self):
         print("La clase a sido destruida")
          

Carrera1 = Carreras("Ingenieria En ICCO", 120, "CUTonala")
print(Carrera1.Escuela)

Carrera2 = Carreras("Ingenieria de Ciberseguridad", 200, "CUTonala")
print(Carrera2.Escuela)

