"""---------------------------|RETO 1|---------------------------------
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
* 
*-------------------------|NECESITA SABER|-----------------------------
* Ciclo for
* if, elif y else
* range()
* ------------------------|CONSIDERACIONES|----------------------------
* 
* 1. Un número  "n" es divisible entre 3 si el resto de la división 
*    entre "n" y 3 es cero --> n % 3 == 0. Lo mismo para números 
*    divisibles entre 5 --> n % 5 == 0
*
* -------------------------------------------------------------------"""


for n in range(1, 101):             # Para cada número n dentro del rango

    if n % 3 == 0:
        if n % 5 == 0:
            print("fizzbuzz")       # fizzbuzz si "n" es múltiplo de 3 y 5
        else:
            print("fizz")           # fizz cuando "n" solo es múltiplo de 3
    elif n % 5 == 0:
        print("buzz")               # buzz cuando "n" solo es múltiplo de 5
    else:
        print(n)                    # "n" cuando "n" no es múltiplo de 3 ni de 5
