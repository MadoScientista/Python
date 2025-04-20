"""---------------------------|RETO 1|-------------------------------------------
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
* 
*--------------------------|CONSIDERACIONES|--------------------------------------
* 1. Las instrucciones dentro de un "if" se ejecutan solo si la condición
*    a evaluar es verdadera (True o 1)
* 2. Una variable de tipo bool solo puede tener dos valores, "False" cuando es 0
*    y "True" cuando es cualquier otro valor
* 3. Si se niega un False este pasa a ser True --> not False = True
* 5. Si se niega un True este pasa a ser False --> not True = False
* ---------------------------------------------------------------------------"""


def fizz_buzz(num):
    """
    Imprime números desde el 1 hasta "num", reemplazando múltiplos de 3 por
    "fizz", múltiplos de 5 por "buzz", y múltiplos de 3 y 5 por "fizzbuzz"
    """
    for n in range(1, num+1):
        multiplo_3 = not n % 3
        multiplo_5 = not n % 5

        if multiplo_3:
            if multiplo_5:
                print("fizzbuzz")
            else:
                print("fizz")
        elif multiplo_5:
            print("buzz")
        else:
            print(n)


# Ejecutamos fizz_buzz para 100
fizz_buzz(100)
