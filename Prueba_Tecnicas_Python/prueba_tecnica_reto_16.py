"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
"""


def drawStair(steps):
    if steps < 0:
        print("_")
        for step in range(abs(steps)):
            print(" "*(2*step+1) + "|_")

    elif steps > 0:
        print("  "*steps + "_")

        for step in range(1, steps+1):
            print(((steps - step)) * "  " + "_|")

    else:
        print("__")


drawStair(3)
