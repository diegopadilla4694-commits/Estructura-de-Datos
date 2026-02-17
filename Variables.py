'''variable = "Hola Mundo"
numero = 42
decimal = 10.5
verdadero = True
falso = False'''

palabra = input("Ingrese una palabra por favor \ntienes de 10 intentos ")
cont = 10

while palabra != "chupacabras":
    
    print("JUAJUAJUAJUA palabra incorrecta")
    cont -= 1
    print(f"te quedan {cont} intentos")

    
    palabra = input("Ingrese otra palabra de nuevo juajua ")
    
    if cont == 1:
        print("Perdiste mi juego nimodo juajua")
        break


if palabra == "chupacabras":
    print("......")
    print("Has dejado el con bucle exito")
       



    

       
    