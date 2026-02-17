# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))


cont = 5

while cont > 1:
    if number % 2:
        odd_numbers += 1
    else:
         even_numbers += 1
    cont -=1
    number = int(input("Introduce un número o escribe 0 para detener: "))
   
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

print("Salio del bucle")

