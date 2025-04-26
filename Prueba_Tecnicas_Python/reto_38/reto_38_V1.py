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


class SumList():
    """Objeto que gestiona listas"""

    def __init__(self, number_list: list, target_sum: int):
        self.numbers = sorted(number_list)
        self.target = target_sum
        self.target_list = []
        self.partial_list = []
        self.actual_numbers = []
        self.list_numbers()

    def list_numbers(self):
        """Encuentre listas"""

        while len(self.numbers):

            # Copia la lista numbers
            self.actual_numbers = self.numbers[:]

            # Busca todas las posibles soluciones
            self.find_list_target()

            # Elimina el elemento de numbers
            self.numbers.pop(0)

    def find_list_target(self):
        "Encuentra soluciones en actual_numbers"

        while len(self.actual_numbers) > 0:
            self.partial_list = []
            nums = 0

            # Itera todas las combinaciones con el primer número
            for num in self.actual_numbers:

                # Identifica si los números pueden entrar a la lista
                nums += num

                if nums <= self.target:
                    # Se agregan a una potencial lista solución
                    self.partial_list.append(num)

                    # Si se logra el target se agrega como una solución
                    if nums == self.target and self.partial_list not in self.target_list:
                        self.target_list.append(self.partial_list)

                        # Elimina el segundo elemento de la lista
                        if len(self.actual_numbers) > 1:
                            self.actual_numbers.pop(1)
                        break

                    if len(self.actual_numbers) == 1:
                        self.actual_numbers.pop()

                # Elimina el segundo elemento de la lista
                elif len(self.actual_numbers) > 1:
                    self.actual_numbers.pop(1)
                    break


Lista = [1, 5, 3, 3, 2, 6]
my_list = SumList(Lista, 6)
print(my_list.target_list)
