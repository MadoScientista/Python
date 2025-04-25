"""
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través 
 *   de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin, 
 *   Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el 
 *   algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 """


import os
from random import sample

# Importa lista de preguntas
from questions_v2 import questions


def begin_test():
    """Muesta un test de casas de Howarts"""

    # Diccionario con puntajes de cada casa
    houses = {"Gryffindor": 0,
              "Slytherin": 0,
              "Hufflepuff": 0,
              "Ravenclaw": 0}

    letters = ["a) ", "b) ", "c) ", "d) "]
    # Recorre la lista de preguntas
    for i, question in enumerate(questions):
        os.system('cls')

        # Establece la cadena de texto de cada pregunta
        ask = f'Pregunta n°{i+1} {question[0]}\n'
        ord_options = question[1]

        options = sample(ord_options, len(ord_options))

        for j, letter in enumerate(letters):
            ask = ask + f'{letter}{options[j][0]}\n'

        ask = ask + "Ingrese a, b, c, d o salir: "
        answer = input(ask).lower()

        # Si la respuesta no es válida, se pregunta nuevamente
        while answer not in ("a", "b", "c", "d", "salir"):
            answer = input("Ingrese a, b, c, d o salir: ")

        # Asigna puntos segun la respuesta
        if answer == "salir":
            break

        if answer == "a":
            houses[options[0][1]] += 1
        if answer == "b":
            houses[options[1][1]] += 1
        if answer == "c":
            houses[options[2][1]] += 1
        if answer == "d":
            houses[options[3][1]] += 1

    # Ordena las casas según el puntaje obtenido
    houses = sorted(houses.items(), reverse=True,
                    key=lambda item: item[1])
    
    

    os.system('cls')

    print("Afinidad con las casas")
    for house in houses:
        print(f"{house[0]}: {house[1]}")

    print("-"*80)
    # Establece la cadena de texto y muestra el resultado
    your_house = f"El sombrero seleccionador ha hablado, tu casa es: ¡¡¡{houses[0][0]}!!!"
    print(your_house)
    print("-"*80)


begin_test()  # Llama a la función para comenzar el test
