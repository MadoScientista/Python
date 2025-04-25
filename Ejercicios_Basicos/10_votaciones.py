"""-----------------|Votación infinita|------------------------
* - A partir de un diccionario de candidatos
* - Comienza una votación infinita donde el usuario
*   puede ingresar el número de candidato para votar
* - La votación termina cuando el usuario ingresa cualquier 
*   caracter que no sea un entero
* - Finalmente muestra al candidato electo
*--------------------------------------------------------------"""

import os

# Diccionario con candidatos
candidates = {
    "Matthei": 0,
    "Kaiser": 0,
    "Kast": 0,
    "Winter": 0,
    "Jara": 0
}


# Inicializa variables
voto = 0

# Comienza una votación infinita
while True:

    os.system('cls')

    print("-"*50)
    print("Votación en curso")
    print("-"*50)

    # Lista los candidatos
    list_candidates = list(candidates.items())
    for idx, candidate in enumerate(list_candidates):
        print(f"{idx+1}. {candidate[0]}")

    # Intenta convertir lo ingresado a integer
    try:
        print("Ingrese el número de su candidato, cualquier otro valor para salir")
        voto = int(input("¿Por cuál candidato desea votar?: ")) - 1

        # Suma el voto al candidato correspondiente
        if 0 < voto < len(list_candidates):
            candidates[list_candidates[voto][0]] += 1
        else:
            print("Número de candidato no válido")

    # Sino lo logra, sale del bucle
    except ValueError:
        os.system('cls')
        print("Saliendo de la votación")
        break


# Ordena la lista según la cantidad de votos en una lista
lista_ordenada = sorted(candidates.items(), reverse=True,
                        key=lambda item: item[1])


# Obtiene el nombre del candidato/a electo
electo = lista_ordenada[0][0]

# Muestra el resultado de la votación y el candidato electo
print("Resultado de la votación: ")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes}")
print(f"Es electo: {electo}")
