"""
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 """


def findSumList(list_numbers: list, target_number: int):

    numbers = list_numbers.sort()
    current_list = []
    results = []

    def findSum(start: int, target: int, sum_combination: list):
        # Solución encontrada
        if target == 0:
            current_list = sum_combination
            results.append(current_list)

        # Sin solución
        if start > len(list_numbers):
            return

        findSum()

    findSum(0, target_number, [])
    for number in numbers:
        if number <= current_target:
            current_list.append(number)
            current_target -= number

    return results
