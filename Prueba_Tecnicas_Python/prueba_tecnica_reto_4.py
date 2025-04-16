"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


def categorize(num_input):
    num = int(num_input)
    fibonacci = "no es fibonacci"
    prime = "no es primo"
    even = "es impar"

    if isPrime(num):
        prime = "es primo"
    if isFibonacci(num):
        fibonacci = "es fibonacci"
    if isEven(num):
        even = "es par"

    return f'{num} {prime}, {fibonacci} y {even}'


def isFibonacci(fib_input):
    n_1 = 0
    n_2 = 1
    n_th = 1

    if fib_input in range(3):
        return True

    while n_th < fib_input:
        n_th = n_1 + n_2
        n_1 = n_2
        n_2 = n_th

        if n_th == fib_input:
            return True

    return False


def isPrime(prime_input):
    for n in range(2, prime_input):
        if prime_input % n == 0:
            return False
    return True


def isEven(even_input):
    if even_input != 0:
        return not even_input % 2
    return False


num_categorize = input("ingresa un número entero: ")
print(categorize(num_categorize))
