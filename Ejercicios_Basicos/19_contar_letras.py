# -------🔥🔥🏠La aldea se incendia 🏠🔥🔥-----------
# Crea un programa que simule una aldea incendiándose
# Tu deber es extinguir los 4 puntos de incendio 🔥
# antes que este se propague a 10 puntos de 🔥
# Puedes elegir llevar entre 1 a 3 cantidades de agua 💧
# que permita extinguir una cantidad igual de 🔥
# Mientras más alta sea la cantidad de 💧 que elijas
# mayor será la probabildiad de que esta se derrame
# y el fuego termine propagándose aleatoriamente entre
# 1 a 3 focos más
# ------------------------------------------------------

from random import randint
import os

# Inicializamos variables necesarias
fuego = 4
agua = 0
derrame = 0

# Limpiamos la consola
os.system('cls')

# El código se ejecuta mientras la aldea
# todavía se pueda salvar o quemar
while 0 < fuego < 10:

    # Mostramos el estado de la aldea
    print("-"*35)
    print("🏠¡La aldea se incendia!🏠")
    print("🔥"*fuego)
    print("-"*35)

    # El usuario elije la cantidad de agua a llevar
    agua = int(input("¿Cuánta agua llevarás? ¿1,2 o 3?\n"))
    os.system('cls')

    # La probabilidad de derramar el agua será
    # 20%, 40% o 60% dependiendo de la elección del usuario
    derrame = randint(1, 10)
    if derrame <= agua*2:
        print("¡¡EL AGUA SE HA DERRAMADO!!")
        fuego += randint(1, 3)
    else:
        print("Logras llevar " + "💧"*agua)
        fuego -= agua

# Evalúa si la aldea se salva o quema
print("-"*35)
if fuego < 1:
    print("💧🏠¡Has salvado a la aldea!🏠💧")

else:
    print("🔥🔥🏠RIP aldea🏠🔥🔥")
print("-"*35)
