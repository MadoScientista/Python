import os

os.system('cls')


def atras_salir():
    print("Ingrese 1 para volver atrás, 2 para salir")
    op = input()
    os.system('cls')

    volver_atras = False
    salir = False

    if op == "1":
        volver_atras = True
    elif op == "2":
        print("Cierre de sesión exitoso, adiós")
        volver_atras = True
        salir = True
    else:
        os.system('cls')
        print("Opción no válida")

    return volver_atras, salir


saldo = 500000
cerrar_sesion = False

while not cerrar_sesion:
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Cargar $20.000")
    print("4. Salir")

    print("-"*40)

    opcion = input("Ingrese el número de la opción que desea: ")
    os.system('cls')

    match opcion:
        case "1":
            print("Tiene un saldo de $500000")

            atras = False
            while not atras:
                atras, cerrar_sesion = atras_salir()

        case "2":
            print("Transferencia realizada")
            atras = False
            while not atras:
                atras, cerrar_sesion = atras_salir()

        case "3":

            saldo += 20000
            print("Transferencia realizada")
            print(f"Su nuevo saldo es de {saldo}")
            atras = False
            while not atras:
                atras, cerrar_sesion = atras_salir()

        case "4":
            os.system('cls')
            print("Cierre de sesión exitoso, adiós")
            sesion_activa = False

        case _:
            os.system('cls')
            print("Opción no válida")
