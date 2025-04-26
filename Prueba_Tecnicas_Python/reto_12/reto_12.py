"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""
from calendar import weekday


def friday_13(year, month):
    if weekday(year, month, 13) == 4:
        return True
    return False


for i in range(1, 13, 1):
    print(friday_13(2023, i))
