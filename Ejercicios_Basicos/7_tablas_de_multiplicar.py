"""---------|Tablas de multiplicar|-----------
* - Pide al usuario un número
* - Muestra en consola la tabla del 1 al 10 del
*   número que ingresó el usuario
*----------------------------------------------"""
num = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

