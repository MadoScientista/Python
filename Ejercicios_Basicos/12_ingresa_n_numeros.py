"""
Pide al usuario ingresar números de uno en uno,
puede ingresar "salir" para terminar. Al terminar
se debe informar la cantidad de números ingresados
y la suma total de ellos
"""

from os import system

system('cls')

n = 0
total = 0
num = 0

while num != "salir":

    if n == 0:
        num = input(
            'Ingresa un número.\n'
            'Ingresa "salir" para terminar:\n'
            ''
        )
    else:
        num = input(
            'Ingresa otro número.\n'
            'Ingresa "salir" para terminar:\n'
            ''
        )
    system('cls')

    try:
        num = float(num)
        n += 1
        total += num
        print(f"Has ingresado {n} números")
        print("-"*30)
    except ValueError:
        if num != "salir":
            print(f"- {num} - no es una entrada válida")
            print("-"*30)

print(f'Has ingresado un total de {n} números')
print(f'La suma total de los números ingresados es: {total}')
