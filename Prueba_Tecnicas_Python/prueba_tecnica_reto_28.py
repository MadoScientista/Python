"""
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
"""
import pytest


def checkSyntaxExpression(expression):
    """Comprueba sin la expresión matemática ingresada es correcta

    Operaciones soportadas: + - * / % 
    """

    supported_operations = ["+", "-", "*", "/", "%"]

    number_or_symbol = expression.split(" ")
    one_operation = False
    div_0 = False
    error = "La expresión no es válida"
    error_div_0 = "Expresión indefinida, no se puede dividir por 0"

    if len(number_or_symbol) > 2:

        for element in number_or_symbol:

            if element in supported_operations and not one_operation:
                one_operation = True
                if element == "/":
                    div_0 = True
            else:
                try:
                    element = float(element)

                    if element == 0 and div_0 == True:
                        return error_div_0

                    div_0 = False
                    one_operation = False

                except:
                    return error

        return f'La expresión {expression} es válida'

    return "La expresión debe contener al menos un número, una operación y otro número separados por espacios."


math_expression = input(
    "Verifica la sintaxis de tu expresión matemática \nIngresa una expresión: ")

print(checkSyntaxExpression(math_expression))


@pytest.mark.parametrize(
    "expression_input, expected",
    [
        ("2 + 2 - 2 / 6 * 12 % 15", f'La expresión 2 + 2 - 2 / 6 * 12 % 15 es válida'),
        ("4", "La expresión debe contener al menos un número, una operación y otro número separados por espacios."),
        ("12 + 2 - a", "La expresión no es válida"),
        ("12 +* 2 - a", "La expresión no es válida"),
        ("12 + 2-1", "La expresión no es válida"),
        ("2 % 2 + 6.6", f'La expresión 2 % 2 + 6.6 es válida'),
        ("2 % 2 + 6,6", "La expresión no es válida"),
        ("2 / 0 + 2", "Expresión indefinida, no se puede dividir por 0"),
        ("2 * 0 + 2", f'La expresión 2 * 0 + 2 es válida'),

    ]
)
def test_checkSyntaxExpression(expression_input, expected):
    assert checkSyntaxExpression(expression_input) == expected
