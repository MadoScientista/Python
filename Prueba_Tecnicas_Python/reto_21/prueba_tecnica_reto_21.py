"""
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
"""


def twinPrime(num_max):
    possible_pair = []
    twin_prime = []

    for num in range(3, num_max+1):
        if isPrime(num):
            possible_pair.append(num)

        if len(possible_pair) == 2:
            if possible_pair[1] - possible_pair[0] == 2:
                twin_prime.append((possible_pair[0], possible_pair[1]))
            possible_pair = [possible_pair[1]]

    return twin_prime


def isPrime(num_prime):

    for num in range(2, num_prime):
        if num_prime % num == 0:
            return False

    return True


print("---- Encontrar pares de primos gemelos desde 0 hasta un número ----")
number = input("Ingrese un número: ")

twins_prime = twinPrime(int(number))

for pair in twins_prime:
    print(pair)
