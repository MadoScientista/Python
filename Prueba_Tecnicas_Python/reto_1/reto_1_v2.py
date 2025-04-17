"""---------------------------|RETO 1|-------------------------------------------
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
* 
*--------------------------|NECESITA SABER|--------------------------------------
* Ciclo for
* if, elif y else
* range()
* def: Crear y llamar funciones
*--------------------------|CONSIDERACIONES|--------------------------------------
* 
* 1. Un número  "n" es divisible entre 3 si el resto de la división entre "n" y 3
* es cero --> n % 3 == 0. Lo mismo para números divisibles entre 5 --> n % 5 == 0
*
* 2. Las instrucciones dentro de un "if" se ejecutan solo si la condición
* a evaluar es verdadera (True o 1)
*
* 3. Una variable de tipo bool solo puede tener dos valores, "False" cuando es 0
* y "True" cuando es cualquier otro valor
*
* 4. Si se niega (not) un False este pasa a ser True -->  not False = True
*
* 5. Si se niega (not) un True este pasa a ser False --> not True = False
*
* 6. Siempre es útil crear funciones para reciclar código
*
* ---------------------------------------------------------------------------"""


def fizzBuzz(num):

    for n in range(1, num+1):        # Para cada número "n" dentro del rango
        multiplo_3 = not n % 3       # True si el resto es 0, False para otro valor
        multiplo_5 = not n % 5       # True si el resto es 0, False para otro valor

        if multiplo_3:
            if multiplo_5:
                print("fizzbuzz")    # fizzbuzz si "n" es múltiplo de 3 y 5
            else:
                print("fizz")        # fizz cuando "n" solo es múltiplo de 3
        elif multiplo_5:
            print("buzz")            # buzz cuando "n" solo es múltiplo de 5
        else:
            print(n)                 # "n" cuando "n" no es múltiplo de 3 ni de 5


# Ejecutamos fizzBuzz para 100
fizzBuzz(100)
