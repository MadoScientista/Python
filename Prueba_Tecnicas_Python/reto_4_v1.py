"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


# Un número primo solo es divisible por 1 y si mismo
def isPrime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def isEven(num):
    if num % 2 == 0:
        return True
    return False


def isFibonacci(num):
    n_1 = 0
    n_2 = 1
    n_th = 1

    if num in range(3):
        return True

    while n_th < num:
        n_th = n_1 + n_2
        n_1 = n_2
        n_2 = n_th

        if n_th == num:
            return True

    return False


def categorize(num_input):
    num = int(num_input)
    fibonacci = "no es fibonacci"
    prime = "no es primo"
    even = "no es impar"

    if isPrime(num):
        prime = "es primo"
    if isFibonacci(num):
        fibonacci = "es fibonacci"
    if isEven(num):
        even = "es par"

    return f'{num} {prime}, {fibonacci} y {even}'


num_categorize = input("ingresa un número entero: ")
print(categorize(num_categorize))
