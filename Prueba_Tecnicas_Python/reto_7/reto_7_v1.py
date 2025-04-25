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


def begin_test():
    """Muesta un test de casas de Howarts"""

    # Diccionario con puntajes de cada casa
    houses = {"Griffindor": 0,
              "Slytherin": 0,
              "Hufflepuff": 0,
              "Ravenclaw": 0}

    # Lista de reguntas
    questions = [
        """ ¿Qué cualidad valoras más en ti mismo?
        
        a) Valentía y osadía
        b) Ambición y astucia
        c) Lealtad y trabajo duro
        d) Inteligencia y curiosidad
         """,

        """ ¿Qué tipo de desafío te atrae más?

        a) Enfrentar un peligro por una buena causa
        b) Superar a mis rivales para alcanzar mis metas
        c) Colaborar con otros para lograr un objetivo común
        d) Resolver un enigma complejo o aprender algo nuevo
          """,

        """¿Cómo reaccionarías ante una injusticia?

        a) Me levantaría para defender a los oprimidos, sin importar el riesgo.
        b) Buscaría la manera más estratégica para sacar provecho de la situación.
        c) Trabajaría diligentemente para restaurar la armonía y el equilibrio.
        d) Investigaría a fondo la situación para entenderla completamente antes de actuar.
          """,

        """¿Qué entorno de aprendizaje prefieres?

        a) Uno donde pueda demostrar mi coraje y liderazgo.
        b) Uno donde pueda poner a prueba mi ingenio y estrategia.
        c) Uno donde haya un fuerte sentido de comunidad y apoyo mutuo.
        d) Uno que estimule mi mente con ideas y debates interesantes.
          """,

        """¿Qué tipo de criatura mágica te inspira más respeto?

        a) Un grifo, por su nobleza y valentía.
        b) Una serpiente, por su astucia y poder.
        c) Un tejón, por su lealtad y dedicación.
        d) Un águila, por su visión y sabiduría.
          """]

    # Recorre la lista de preguntas
    for i, question in enumerate(questions):

        # Establece la cadena de texto de cada pregunta
        ask = f'\nPregunta n°{i+1} {question} \nIngrese a, b, c, d o salir: '
        answer = input(ask).lower()

        # Si la respuesta no es válida, se pregunta nuevamente
        while answer not in ("a", "b", "c", "d", "salir"):
            answer = input("Ingrese a, b, c, d o salir: ")

        # Asigna puntos segun la respuesta
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

    # Ordena las casas según el puntaje obtenido
    houses = sorted(houses.items(), reverse=True,
                    key=lambda item: item[1])

    # Establece la cadena de texto y muestra el resultado
    your_house = f"El sombrero seleccionador ha hablado, tu casa es: ¡¡¡{houses[0][0]}!!!"
    return print(your_house)


begin_test()  # Llama a la función para comenzar el test
