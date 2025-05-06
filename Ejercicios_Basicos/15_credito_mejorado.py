# Calcular el puntaje de credito
# Debe calcular que tanto crédito tiene una persona 
# en cierta entidad financiera, debe considerar
# cantidad de ingresos, nivel educacional, nacionalidad
#
# Cantidad de ingresos:
# 500.000 a 1.000.000: 300.000
# 1.000.001 a 1.500.000: 650.000
# 1.500.001 o más: 1.000.000
#
# Nivel Educacional:
# Básico: x1 Medio: x1.3, Superior: x1.5
#
# Nacionalidad:
# Chilena: +300.000, Extranjero: +0

import os

credito = 0
ingreso = 0
educacion = 0
nacionalidad = 0

mensaje_ingreso = """¿En qué rango se encuentra su ingreso mensual?
1. Menos de 500.000
2. Entre 500.000 a 1.000.000
3. Entre 1.000.001 a 1.500.000
4. Más de 1.500.000
"""

mensaje_educacion = """¿Cuál es su nivel educacional?

1. Básica completa
2. Media completa
3. Superior completa\n"""

mensaje_nacionalidad = """¿Cuál es su nacionalidad?
1. Chileno/a
2. Extranjero/a\n"""


def evaluarEntrada(mensaje, opciones):
    entrada = input(mensaje)
    while True:
        try:
            entrada = int(entrada)
            if entrada in opciones:
                break

            os.system('cls')
            print("-"*20)
            print("Opción no valida")
            print("-"*20)

        except ValueError:
            os.system('cls')
            print("-"*20)
            print("Ingrese solo números")
            print("-"*20)
        entrada = input(mensaje)
        
    return entrada



# Limpia pantalla y pregunta ingresos
os.system('cls')
ingreso = evaluarEntrada(mensaje_ingreso, (1,2,3,4))


# Si el ingreso es menor a 500.000
if ingreso == 1:
    print("Sus ingresos no califican para un crédito")

else:
    if ingreso == 2:
        credito += 300000
    elif ingreso == 3:
        credito += 650000
    else:
        credito += 1000000
    
    # Limpia pantalla y pregunta educación
    os.system('cls')
    educacion = evaluarEntrada(mensaje_educacion, (1,2,3))

    if educacion == 1:
        credito *=1
    elif educacion == 2:
        credito *= 1.3
    elif credito == 3:
        credito *=1.5

    # Limpia pantalla y pregunta nacionalidad
    os.system('cls')
    nacionalidad = evaluarEntrada(mensaje_nacionalidad, (1,2))

    if nacionalidad == 1:
        credito += 300000

    os.system('cls')
    print(f"Le ofrecemos un crédito máximo de: {credito}")


