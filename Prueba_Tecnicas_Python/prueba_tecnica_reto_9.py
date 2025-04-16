"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""


def isPangram(word_pangram):
    """Pangrama: Es un texto que usa todas las letras posibles del alfabeto de un idioma"""

    alfabet = "abcdefghijklmnñopqrstuvwxyz"

    for char in alfabet:
        if char not in word_pangram.lower():
            return False

    return True


def isIsogram(word_isogram):
    """Isograma: Es una palabra o frase en la que cada letra aparece el mismo número de veces."""

    word_clean = word_isogram.replace(" ", "")
    char_dict = {}

    for char in word_clean.lower():
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    values = list(char_dict.values())

    for count in values:
        if count != values[0]:
            return False

    return True


def isHeterogram(word_heterogram):
    """Heterograma: Un heterograma es una palabra o frase que no contiene ninguna letra repetida."""

    word_clean = word_heterogram.replace(" ", "")
    char_list = ""

    for char in word_clean.lower():
        if char not in char_list:
            char_list += char
        else:
            return False

    return True
