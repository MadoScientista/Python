"""---------------------------------------|RETO 4|------------------------------------------
* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
* Ejemplos:
* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*-----------------------------------------------------------------------------------------"""


def is_prime(num):
    """Un número primo es un número natural mayor que 1 que 
    tiene únicamente dos divisores positivos distintos: 1 y sí mismo"""

    if num <= 1:
        return False

    for n in range(2, num):   # Busca divisores de num entre 2 y num-1
        if num % n == 0:
            return False

    return True


def is_fibonacci(num):
    """La secuencia de Fibonacci comienza con 0 y 1, los siguientes 
    números de la secuencia se calculan sumando los dos últimos números 
    -> 0,1,1,2,3,5,8,13,21,34..."""

    if num in range(2):
        return True

    n_1 = 0
    n_2 = 1
    n_th = 1

    while n_th < num:
        n_th = n_1 + n_2
        n_1 = n_2
        n_2 = n_th

        if n_th == num:
            return True

    return False


def is_even(num):
    """Un número "n" es par si el resto de la 
    división entre 2 es cero -> n % 2 == 0"""

    if num % 2 == 0:
        return True
    return False


def categorize(num_input):
    """Por defecto la categorización es negativa, pero cambia
    dependiendo del resultado de las evaluaciones"""

    num = int(num_input)
    prime = "no es primo"
    fibonacci = "no es fibonacci"
    even = "es impar"

    if is_prime(num):
        prime = "es primo"
    if is_fibonacci(num):
        fibonacci = "es fibonacci"
    if is_even(num):
        even = "es par"

    return f'{num} {prime}, {fibonacci} y {even}'


user_num = input("ingresa un número natural: ")
print(categorize(user_num))
