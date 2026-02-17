secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

num = int(input("ingrese un numero entero muajajaja "))

while num != 777:
    print("Te equivocastes de numero muggle, sigues atrapado en mi bucle infinito")
    num = int(input("ingrese un numero entero muajajaja "))

if num == 777:
   print("Lo Lograstes eres libre")
