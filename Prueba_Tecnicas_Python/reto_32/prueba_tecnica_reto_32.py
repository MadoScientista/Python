"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 """


def numberColumn(name):
    name_list = list(name)
    char_list = list(name.lower())
    number_column = 0

    for index, char in enumerate(char_list):
        if 'a' <= char <= 'z':
            pos = ord(char) - ord('a') + 1
        else:
            return f'El caracter {name_list[index]} no es válido'

        number_column += pos * pow(26, len(char_list)-index-1)

    return number_column


print(numberColumn("CA"))
