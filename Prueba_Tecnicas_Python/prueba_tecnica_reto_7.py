"""
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 """


def beginTest():

    houses = {"Griffindor": 0,
              "Slytherin": 0,
              "Hufflepuff": 0,
              "Ravenclaw": 0}

    questions = [
        ("Pregunta 1",
         ("""
    a) 
    b) 
    c)
    d)
    """)),
        ("Pregunta 2",
         ("""
    a) 
    b) 
    c)
    d)
    """)),
        ("Pregunta 3",
         ("""
    a) 
    b) 
    c)
    d)
    """)),
        ("Pregunta 4",
         ("""
    a) 
    b) 
    c)
    d)
    """)),
        ("Pregunta 5",
         ("""
    a) 
    b) 
    c)
    d)
    """))]

    for question in questions:

        ask = f'\n{question[0]} {question[1]} \nIngrese a, b, c, d o salir: '
        answer = input(ask).lower()
        while answer not in ("a", "b", "c", "d", "salir"):
            answer = input("Ingrese a, b, c, d o salir: ")

        if answer == "a":
            houses["Griffindor"] += 1
        elif answer == "b":
            houses["Slytherin"] += 1
        elif answer == "c":
            houses["Hufflepuff"] += 1
        elif answer == "d":
            houses["Ravenclaw"] += 1
        else:
            print("Has salido del test")
            break

    houses = sorted(houses.items(), reverse=True,
                    key=lambda item: item[1])
    print(houses)
    your_house = houses[0][0]
    return print(your_house)


beginTest()
