"""
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
"""
import pytest


def compare_string(text_1, text_2):

    text_1 = list(text_1)
    text_2 = list(text_2)
    char_different = []
    error_len = "Los dos textos tienen diferente longitud"
    error_content = "Los dos textos no tienen los mismos elementos"

    if len(text_1) == len(text_2):

        for index, char in enumerate(text_2):

            if char in text_1:
                if text_1[index] != text_2[index]:
                    char_different.append(char)
            else:
                return error_content

        return char_different

    return error_len


@pytest.mark.parametrize(
    "text_1_input, text_2_input, expected",
    [
        ("hola soy samuel", "hola soy samuel", []),
        ("hola soy samuel", "hola soy sameul", ["e", "u"]),
        ("hola soy samuel", "hola soy samuel cortes ",
         "Los dos textos tienen diferente longitud"),
        ("hola soy samuel", "hola soy camila",
         "Los dos textos no tienen los mismos elementos"),
        ("hola soy samuel", "ahlo  oy samuel", ["a", "h", "o", " "])

    ]

)
def test_compare_string(text_1_input, text_2_input, expected):
    assert compare_string(text_1_input, text_2_input) == expected
