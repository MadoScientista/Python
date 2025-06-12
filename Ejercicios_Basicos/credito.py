import os

credito_maximo = 100000
deuda = 100000
salir = False


def enter_para_continuar():
    print("-"*40)
    print("Presione enter para continuar".center(40))
    print("-"*40)
    input()
    os.system('cls')


os.system('cls')
while not salir:

    print(f"Deuda actual: ${deuda}".center(40))
    print(f"Cupo máximo: ${credito_maximo-deuda}".center(40))
    print("-"*40)

    print("1. Pago de tarjeta de crédito")
    print("2. Comprar")
    print("3. Salir")
    print("-"*40)

    opcion = input("Ingrese el número de la opción que desea: ")
    os.system('cls')

    match opcion:
        case "1":

            while True:

                print("Pago de tarjeta de crédito".center(40))
                print("-"*40)

                if deuda == 0:
                    print("No tiene deuda pendiente")
                    enter_para_continuar()
                    break
                try:
                    monto_a_pagar = int(input("Ingrese monto a pagar: "))
                    os.system('cls')

                    if monto_a_pagar <= 0:
                        print("El monto debe ser mayor a cero".center(40))
                        enter_para_continuar()

                    elif monto_a_pagar <= deuda:
                        deuda -= monto_a_pagar
                        print("Pago exitoso".center(40))
                        enter_para_continuar()

                    else:
                        print(f"El pago máximo es de: {deuda}".center(40))
                        enter_para_continuar()

                    break
                except ValueError:
                    os.system('cls')
                    print("Ingrese solo números".center(40))
                    enter_para_continuar()

        case "2":
            en_tienda = True
            while en_tienda:
                try:
                    print("En tienda".center(40))
                    print("-"*40)

                    monto_compra = int(
                        input("Ingrese el monto de su compra: "))
                    os.system('cls')

                    if monto_compra <= 0:
                        print(
                            "El monto de la compra debe ser mayor a cero".center(40))
                        enter_para_continuar()
                    elif deuda + monto_compra > credito_maximo:
                        print("El monto excede el cupo máximo".center(40))
                        print(
                            f"El valor máximo de compra es de {credito_maximo - deuda}".center(40))
                        enter_para_continuar()
                    else:
                        deuda += monto_compra
                        print("Compra exitosa".center(40))
                        print(
                            f"Su cupo actual es de {credito_maximo - deuda}".center(40))
                        enter_para_continuar()

                    while True:
                        print("¿Qué desea hacer ahora?")
                        print("-"*40)
                        print("1. Seguir comprando")
                        print("2. Quiero volver al menú principal")
                        print("3. Salir")
                        print("-"*40)

                        seguir_comprando = input()
                        os.system('cls')

                        match seguir_comprando:
                            case "1":
                                break
                            case "2":
                                en_tienda = False
                                salir = False
                                break
                            case "3":
                                en_tienda = False
                                salir = True
                                break
                            case _:
                                print("Opción no válida")
                                enter_para_continuar()

                except ValueError:
                    print("Ingrese solo números".center(40))
                    enter_para_continuar()

        case "3":
            salir = True
        case _:
            print("Opción no válida".center(40))
            enter_para_continuar()
