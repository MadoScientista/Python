from random import randint
import os

# Inicialización de variables
limite_inferior = 0
limite_superior = 0
num_aleatorio = 0

intentos = 3

num_usuario = 0
num_anterior = 0

# Bienvenida
os.system('cls')
print("-"*30)
print("Bienvenido al juego de adivinar")
print("-"*30)

# Consulta límites
limite_inferior = int(input("Ingrese límite inferior: "))
limite_superior = int(input("Ingrese límite superior: "))

while limite_superior < limite_inferior:
    os.system('cls')
    print(f"El límite superior debe ser mayor a {limite_inferior}")
    limite_superior = int(input("Ingrese límite superior: "))
    
num_aleatorio = randint(limite_inferior, limite_superior)


while True:

    # Intentos del usuario
    print("-"*50)
    print(f"Estoy pensando en un número entero entre {limite_inferior} y {limite_superior}")
    print("Cuál podría ser?")
    num_usuario = int(input("Ingresa solo números enteros: "))

    # Evalúa si ha acertado
    os.system('cls')
    if num_usuario == num_aleatorio:
        if intentos == 3:
            print(f"Felicitaciones, pudiste adivinar en tu primer intento")
        elif intentos == 2:
            print(f"Felicitaciones, pudiste adivinar en tu segundo intento")
        else:
            print(f"Felicitaciones, pudiste adivinar en tu tercer intento")

        print(f"El número era {num_aleatorio}")
        break

    # Evalúa si el número es mayor o menor
    if num_usuario > num_aleatorio:
        print(f"El número es menor a {num_usuario}")
    else:
        print(f"El número es mayor a {num_usuario}")

    # Da una pista en el intento 2
    if intentos == 2:
        print("-"*50)
        print("Pista:")

        # Evalúa cuál diferencia es mayor
        if abs(num_aleatorio - num_usuario) > abs(num_aleatorio - num_anterior):
            print(f"El número está más cerca de {num_anterior} que de {num_usuario}")
        elif abs(num_aleatorio - num_usuario) == abs(num_aleatorio - num_anterior):
            print(f"La distancia entre {num_usuario} y {num_anterior} es la misma")
        else:
            print(f"El número está más cerca de {num_usuario} que de {num_anterior}")

    intentos -= 1

    # Guarda el número del usuario
    num_anterior = num_usuario

    # Si el usuario se queda sin intentos se acaba el juego
    if intentos == 0:
        print("Ya no quedan más intentos")
        print(f"Perdiste, el número era {num_aleatorio}")
        break