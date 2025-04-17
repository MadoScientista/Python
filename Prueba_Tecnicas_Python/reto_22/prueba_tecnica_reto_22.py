"""
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
"""
from math import ceil, floor


def drawSpiral(len_spiral):
    """
    Symbols ═ ║ ╗ ╔ ╝ ╚
    """
    if len_spiral % 2:
        top = ceil(len_spiral/2)
        for row in range(top):
            line = "║"*(row-1) + "╔"*(ceil(1 % (row+1))) + "═" * \
                (len_spiral-(2*(row))-1) + "╗" + "║"*row
            print(line)

        bottom = len_spiral - top
        for row in range(bottom):
            line = "║"*(bottom-row-1) + "╚" + "═" * \
                ((2*row+1)) + "╝" + "║"*(bottom-row-1)

            print(line)

    else:
        top = ceil(len_spiral/2)
        for row in range(top):
            line = "║"*row + "╔" + "═" * \
                ((len_spiral)-(2*(row+1))) + "╗" + "║"*row
            print(line)

        bottom = len_spiral - top
        for row in range(bottom):
            line = "║"*(bottom - row-1) + "╚" + "═"*((2*row+1)) + \
                "╝"*(1-floor((row+1)/(bottom))) + "║"*(bottom - 2 - row)
            print(line)


drawSpiral(5)
