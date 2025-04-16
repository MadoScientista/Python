"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 """
from random import randint
from math import ceil


def random_words():
    words = ["semana", "colegio", "almohada",
             "camarote", "perspicaz", "detalles",
             "celular", "computador", "telenovela",
             "escritorio", "conejo ambulante"]
    return words[randint(0, len(words)-1)]


def charToHide(word):
    word_no_space = word.replace(" ", "")
    min_show = ceil((len(word_no_space)*0.4))
    char_hide = []
    char_show = word_no_space

    while True:
        random_char = char_show[randint(0, len(char_show)-1)]
        char_show = char_show.replace(random_char, "")

        if len(char_show) >= min_show:
            char_hide.append(random_char)
        else:
            break

    return char_hide


def play(max_attempts, word_to_find, char_to_find):
    remaining_attempts = max_attempts
    char_list = char_to_find

    while len(char_list) > 0:

        word_in_play = word_to_find

        for char in char_list:
            word_in_play = word_in_play.replace(char, "_")

        print(f"\n{word_in_play}\n")
        print(f'Intentos restantes: {remaining_attempts}')
        char_possible = str((
            input("Ingresa una letra o la palabra completa: "))).lower()

        if len(char_possible) == 1:
            if char_possible in char_list:
                char_list.remove(char_possible)
            else:
                remaining_attempts -= 1
        elif char_possible == word_to_find:
            print("Excelente")
            break
        else:
            remaining_attempts -= 1

        if remaining_attempts == 0:
            print("Se acabaron los intentos")
            break

    print(f'La palabra era {word_to_find}')


def gameBegin():
    word_to_play = random_words()
    char_to_hide = charToHide(word_to_play)
    attepmts = 4

    play(attepmts, word_to_play, char_to_hide)


gameBegin()
