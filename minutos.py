min = int(input("ingrese cantidad de minutos"))

horas = min//60  #// Esto funciona para redondear el valor
minutos = min % 60 # % El modulo divide a min y el residuo que es el decimal lo multiplica con 60

print(f'La cantidad de horas es {horas}')
print(f'La cantidad de minutos es {minutos}')
