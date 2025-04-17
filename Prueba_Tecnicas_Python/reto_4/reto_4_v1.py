"""---------------------------------------|RETO 4|------------------------------------------
* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
* Ejemplos:
* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*
*--------------------------------------|NECESITA SABER|-------------------------------------
* Ciclo for y while
* if
* return
* range()
* ------------------------------------|CONSIDERACIONES|-------------------------------------
* 1. Un número "n" es par si el resto de la división entre 2 es cero -> n % 2 == 0
* 2. Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores 
*    positivos distintos: 1 y sí mismo
* 3. La secuencia de Fibonacci comienza con 0 y 1, los siguientes números de la secuencia
*    se calculan sumando los dos últimos números -> 0,1,1,2,3,5,8,13,21,34...
* 4. Es útil crear funciones para reciclar código
*-----------------------------------------------------------------------------------------"""


def isPrime(num):

    if num <= 1:
        return False

    for n in range(2, num):   # Para todos los enteros entre 2 y num-1
        if num % n == 0:
            return False      # Falso si hay un divisor

    return True               # Verdadero si no los hay


def isFibonacci(num):

    if num in range(2):      # True si num es 0,1
        return True

    n_1 = 0                  # Inicia la secuencia de fibonacci
    n_2 = 1
    n_th = 1

    while n_th < num:
        n_th = n_1 + n_2     # El siguiente número de la secuencia es la suma de los dos anteriores
        n_1 = n_2
        n_2 = n_th

        if n_th == num:
            return True

    return False


def isEven(num):
    if num % 2 == 0:
        return True
    return False


def categorize(num_input):

    num = int(num_input)
    prime = "no es primo"
    fibonacci = "no es fibonacci"
    even = "es impar"

    if isPrime(num):
        prime = "es primo"
    if isFibonacci(num):
        fibonacci = "es fibonacci"
    if isEven(num):
        even = "es par"

    return f'{num} {prime}, {fibonacci} y {even}'


user_num = input("ingresa un número natural: ")
print(categorize(user_num))
