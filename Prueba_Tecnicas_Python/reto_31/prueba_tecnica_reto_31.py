"""
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
"""


def abacoToNumber(abaco):
    number = 0

    for index, row in enumerate(abaco):
        if len(row) == 12:
            digit = 0
            separator = 0
            count_O = 0

            for element in row:
                if element == "O":
                    if separator == 0:
                        digit += 1

                    count_O += 1
                    if count_O > 9:
                        return f'La fila {index + 1 } tiene demasiados "O"'

                elif element == "-":
                    separator += 1
                    if separator > 3:
                        return f'La fila {index + 1 } tiene demasiados "-"'
                else:
                    return f'La fila {index} solo debe contener 9 "O" separados por 3 "-"'

            number += digit * pow(10, 6-index)

        else:
            return f'La fila {index + 1} tiene errores -> {row}'

    return '{:,}'.format(number)


numero = abacoToNumber(["O---OOOOOOOO",
                        "OOO---OOOOOO",
                        "---OOOOOOOOO",
                        "OO---OOOOOOO",
                        "OOOOOOO---OO",
                        "OOOOOOOOO---",
                        "---OOOOOOOOO"])
print(numero)
