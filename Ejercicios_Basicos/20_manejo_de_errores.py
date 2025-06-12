# uso y explicacion de match
import os

# Mensaje de menú
msj_options = '''Ingrese una operación
1.- Suma
2.- Resta
3._ Multiplicación
4.- División
5.- Salir
'''

# Manejo de errores de ingreso de texto en vez de números


def verifica_numero(num):
    try:
        num = float(num)
    except ValueError as error_valor:
        print(f"Ingresa solo números - {error_valor}")

# Verifica número entero


def verifica_entero(num_int):
    try:
        num_int = int(num_int)
        return num_int
    except ValueError:
        print("Ingresa solo números")

# Muestra resultado entre guiones


def mostrar_resultado(mensaje_resultado):
    os.system('cls')
    print("-"*30)
    print(mensaje_resultado)
    print("-"*30)

# Suma dos números


def suma():

    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    n1 = 0
    n2 = 0

    resultado_suma = f"El resultado de la suma es {n1+n2}"
    mostrar_resultado(resultado_suma)

# Resta dos números


def resta():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    resultado_resta = f"El resultado de la resta es: {n1-n2}"
    mostrar_resultado(resultado_resta)

# multiplica dos números


def multiplicacion():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("El resultado de la suma es", n1*n2)

# Divide dos números


def division():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    # Manejo de errores de división entre cero
    try:
        resultado_division = f"El resultado de la division es: {n1/n2}"
    except ZeroDivisionError:
        resultado_division = f"{n1} dividido entre 0 es indefinido"

    mostrar_resultado(resultado_division)


# En un ciclo while ofrece opciones
# de operaciones básicas entre dos números
def calculadora():
    os.system('cls')
    while True:
        option = input(msj_options)
        option = verifica_entero(option)
        os.system('cls')

        # while

        match option:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Mutltiplicacion")
                multiplicacion()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("-"*30)
                print("Opcion INVALIDA")
                print("-"*30)


calculadora()
