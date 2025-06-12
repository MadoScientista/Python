import os


def mostrar_opciones_de_sushi():
    print("*"*42)
    print("¿Qué roll desea agregar?".center(42))
    print("*"*42)

    print("1. Pikachu Roll $4.500")
    print("2. Otaku Roll $5.000")
    print("3. Pulpo Venenoso Roll $5.200")
    print("4. Anguila Eléctrica Roll $4.800")
    print("5. Terminar pedido")
    print("*"*42)


def aplicar_descuento(total):
    monto_descuento = 0
    descuento_aplicado = True

    while True:

        print("*"*42)
        print("¿Tiene código de descuento?".center(42))
        print("*"*42)

        print("1. Si tengo")
        print("2. No tengo")

        opcion_descuento = input()
        os.system('cls')

        match opcion_descuento:
            case "1":
                codigo_descuento = input("Ingrese código de descuento: ")
                os.system('cls')

                if codigo_descuento == "soyotaku":
                    monto_descuento = total * 0.1
                else:
                    print("Código no válido")
                    seguir_comprando = input(
                        "Para seguir comprando ingrese x: ")
                    os.system('cls')

                    if seguir_comprando == "x":
                        descuento_aplicado = False

            case "2":
                descuento_aplicado = True
            case _:
                print("Opción no válida")
                continue

        return monto_descuento, descuento_aplicado


def realizar_otro_pedido():
    while True:
        print("¿Desea realizar otro pedido?")
        print("1. Si")
        print("2. No")

        opcion = input()
        os.system('cls')

        match opcion:
            case "1":
                return True
            case "2":
                return False
            case _:
                print("Opción no válida")


cliente_en_local = True

# Mientras el cliente esté en el local
# Se tomarán las órdenes que quiera con boletas separadas

sub_total = 0
descuento = 0
n_productos = 0
n_pikachu = 0
n_otaku = 0
n_pulpo = 0
n_anguila = 0

while cliente_en_local:
    os.system('cls')
    # Toma el pedido del cliente
    while True:
        mostrar_opciones_de_sushi()

        lleva = input("Ingrese el número del roll que quiere agregar: ")
        os.system('cls')

        match lleva:
            case "1":
                print("Ha agregado Pikachu Roll")
                sub_total += 4500
                n_pikachu += 1
            case "2":
                print("Ha agregado Otaku roll")
                sub_total += 5000
                n_otaku += 1
            case "3":
                print("Ha agregado Pulpo Venenoso Roll")
                sub_total += 5200
                n_pulpo += 1
            case "4":
                print("Ha agregado Anguila Eléctrica Roll")
                sub_total += 4800
                n_anguila += 1
            case "5":
                break
            case _:
                print("Opción no válida")
                print("Las opciones disponibles son 1, 2, 3 y 4")

    # Pregunta por el descuento
    descuento, terminar_pedido = aplicar_descuento(sub_total)

    if terminar_pedido:
        # Entrega boleta
        print("*"*42)
        print(f"Total Productos: {n_pikachu+n_otaku+n_anguila+n_pulpo}")
        print("*"*42)
        print(f"Pikachu Roll: {n_pikachu}")
        print(f"Otaku Roll: {n_otaku}")
        print(f"Pulpo Venenoso Roll: {n_pulpo}")
        print(f"Anguila eléctrica Roll: {n_anguila}")
        print("*"*42)
        print(f"Sub total a pagar {sub_total}")
        print(f"Descuento por código: {descuento}")
        print(f"TOTAL: {sub_total - descuento}")
        print("*"*42)

        # Reinicia datos para comenzar nuevo pedido o se despide
        if realizar_otro_pedido():
            sub_total = 0
            descuento = 0
            n_productos = 0
            n_pikachu = 0
            n_otaku = 0
            n_pulpo = 0
            n_anguila = 0
        else:
            print("Gracias por su compra")
            cliente_en_local = False
            break
