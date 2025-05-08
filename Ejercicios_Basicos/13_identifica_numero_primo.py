"""
Crea una función que informe si un número
ingresado por el usuario es primo
"""


def esPrimo(n):
    for i in range(2, n):
        if not n % i:
            print(f"{n} es divisible entre {i}")
            return False

    return True


num = int(input("Ingresa un número entero: "))

if esPrimo(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es primo")
