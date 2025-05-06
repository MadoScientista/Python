# Pide al usuario 2 dígitos verificando que 
# el segundo sea mayor
# Genere un número aleatorio entre esos dos dígitos
# e imprima la cantidad de veces elifsímbolo ▄ (alt+220)

from random import randint
import os

num1 = 0
num2 = 0
n_aleatorio = 0

os.system('cls')
num1 = int(input("Ingrese un número: "))
num2 = int(input(f"Ingrese un número mayor que {num1}"))

while num1 >= num2:
    print(f"{num1} no es mayor que {num2}, vuelva a intentarlo")

    num1 = int(input("Ingrese un número: "))
    num2 = int(input(f"Ingrese un número mayor que {num1}"))
    os.system('cls')

n_aleatorio = randint(num1, num2)

print("▄"*n_aleatorio)

