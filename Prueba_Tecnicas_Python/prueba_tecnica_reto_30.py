"""
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV

 """
import pytest


class T9Keyboard():
    def __init__(self):
        self.number_converter = {
            "1": (".", ",", "?"),
            "2": ("A", "B", "C"),
            "3": ("D", "E", "F"),
            "4": ("G", "H", "I"),
            "5": ("J", "K", "L"),
            "6": ("M", "N", "O"),
            "7": ("P", "Q", "R", "S"),
            "8": ("T", "U", "V"),
            "9": ("W", "X", "Y", "Z"),
            "0": (" "),
        }

        self.error_len = "No se ha encontrado coincidencias con: "
        self.error_number = "Cada bloque solo puede contener un mismo número, por ejemplo: 44-666-555-2"
        self.error = "Solo puede contener números separados por guiones,por ejemplo: 44-666-555-2"

    def converter(self, number_pattern):
        elements = number_pattern.split("-")
        converted_text = ""

        if (self.check_syntax_elements(elements)):

            for block in elements:
                if len(block) <= len(self.number_converter[block[0]]):
                    converted_text += self.number_converter[block[0]][len(
                        block)-1]
                else:
                    return f'{self.error_len}{block}'

            return converted_text
        else:
            return self.error

    def check_syntax_elements(self, elements):

        for block in elements:
            for char in block:
                try:
                    int(char)
                except:
                    print(self.error)
                    return False

                if block[0] != char:
                    print(self.error_number)
                    return False
        return True


@pytest.mark.parametrize(
    "pattern_input, expected",
    [
        ("6-666-88-777-33-3-33-888", "MOUREDEV"),
        ("44-666-555-2", "HOLA"),
        ("44 33 44 55", "Solo puede contener números separados por guiones,por ejemplo: 44-666-555-2"),
        ("44 33 44 as55", "Solo puede contener números separados por guiones,por ejemplo: 44-666-555-2"),
        ("44-3-44-55555", "No se ha encontrado coincidencias con: 55555")
    ]

)
def test_T9Keyboard(pattern_input, expected):
    teclado = T9Keyboard()
    texto_convertido = teclado.converter(pattern_input)
    assert texto_convertido == expected
