beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon") 
beatles.append("Paul McCartney"), 
beatles.append("George Harrison")
print("Paso 2:", beatles)

for i in range(2):
     miembros = input("agregue los miembros faltantes de la banda ")
     beatles.append(miembros)
     
print("Paso 3:", beatles)

del beatles [3:]
print("Paso 4:", beatles)

beatles.insert( 0, "Ringo Starr")
print("Paso 5:", len(beatles), beatles)

