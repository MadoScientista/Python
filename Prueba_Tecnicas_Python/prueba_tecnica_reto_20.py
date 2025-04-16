"""
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 """

from math import ceil


def drawTriForce(rows_one_force):

    base_one_force = 2*rows_one_force - 1
    base_tri_force = 2*base_one_force + 1

    for row in range(1, rows_one_force + 1):
        space = ceil((base_tri_force/2) - row)
        n_simbol = 2*row-1

        print(" "*space + "*"*n_simbol)

    for row in range(1, rows_one_force+1):
        space_1 = ceil((base_one_force/2) - row)

        space_2 = (base_one_force + 2) - 2*row
        n_simbol = 2*row-1

        print(" "*space_1 + "*"*n_simbol + " "*space_2 + "*"*n_simbol)


drawTriForce(2)
