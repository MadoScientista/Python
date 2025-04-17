"""
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
"""

from calendar import weekday
import pytest


def friday_13(year, month):
    if weekday(year, month, 13) == 4:
        return True
    return False


@pytest.mark.parametrize(
    "year_input, month_input, expected",
    [
        (2023, 1, True),
        (2023, 2, False),
        (2023, 3, False),
        (2023, 4, False),
    ]
)
def test_friday_13(year_input, month_input, expected):
    assert friday_13(year_input, month_input) == expected
