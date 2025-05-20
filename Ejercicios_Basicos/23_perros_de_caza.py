# perros de caza
# Pida al usuario la cantidad de perro
# Muestra cual es la cuota mínima de conejos
# si el perro trajo la cantidad mínima 
# cumplió la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no.

from random import randint
import os

# Inicializa las variables necesarias
cuota_conejos = 0
n_perros = 0
conejos_atrapados = 0
perros_cumplieron = 0

# Limpia la consola
os.system('cls')

# Pide cantidad de perros
while n_perros < 1:
    try:
        n_perros = int(input("Ingrese la cantidad de perros: "))

        if n_perros < 0:
            print("-"*40)
            print("Ingrese solo números enteros positivos")
            print("-"*40)
            n_perros = 0
        
    except ValueError as error:
        # print(error)
        print("Ingrese solo números enteros positivos")


# Muestra cuota de conejos
cuota_conejos = randint(1, 5)
print("-"*40)
print(f"La cuota mínima de conejos es de {cuota_conejos}")
print("\n----------|Comienza la caza|------------\n")


# Calcula y muestra el resumen de cada perro
for i in range(n_perros):

    conejos_atrapados = randint(0,cuota_conejos+2)

    if conejos_atrapados >= cuota_conejos:
        print(f"El {i+1}° perro atrapó {conejos_atrapados}, ganó un filete")
        perros_cumplieron += 1

    else:
        print(f"El {i+1}° perro atrapó {conejos_atrapados}, NO gana filete")


# Muestra resumen de perros
print("-"*40)
print(f"De un total de {n_perros}")
print(f"{perros_cumplieron} perros cumplieron la cuota")
print(f"{n_perros - perros_cumplieron} perros NO cumplieron la cuota")


