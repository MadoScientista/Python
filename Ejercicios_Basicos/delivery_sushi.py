import os


def mostrar_opciones_de_sushi():
    """Muestra las opciones de sushi"""

    print("¿Cuál roll desea agregar?")
    print("-"*34)
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5. Terminar compra")
    print("-"*34)


def aplica_descuento(total):
    """Retorna valor del descuento y la desición del cliente
    de seguir comprando o pedir boleta"""

    descuento = 0
    while True:
        print("¿Tiene código de descuento?")
        print("1. Sí tengo")
        print("2. No tengo")
        print("-"*34)

        tiene_codigo = input()
        os.system('cls')

        match tiene_codigo:
            case "1":
                codigo_descuento = input("Ingrese su código de descuento: ")
                os.system('cls')

                if codigo_descuento == "soyotaku":
                    descuento = total*0.1
                    return descuento, False

                print("Código de descuento no válido")
                print('Para seguir comprando ingrese "X"')
                print("Presione enter para intentarlo de nuevo")

                sigue_comprando = input()
                os.system('cls')

                if sigue_comprando == "X":
                    return descuento, True

            case "2":
                return descuento, False

            case _:
                print("Opción no válida")
                print("Ingrese solo 1 o 2")


def ordena_de_nuevo():
    while True:
        print("¿Desea realizar un nuevo pedido?")
        print("1. Sí")
        print("2. No")
        print("-"*34)

        respuesta = input("Desea realizar un nuevo pedido?")
        os.system('cls')

        match respuesta:
            case "1":
                return True
            case "2":
                return False
            case _:
                print("Opción no válida, ingrese solo 1 o 2")


# Inicializa variables
n_pikachu = 0
n_otaku = 0
n_pulpo = 0
n_anguila = 0
n_productos = 0
total_compra = 0
monto_descuento = 0

# Mientras el cliente esté en local
cliente_en_local = True
cliente_comprando = True

os.system('cls')
while cliente_en_local:

    while cliente_comprando:

        while True:
            mostrar_opciones_de_sushi()

            roll_agregado = input("Ingrese la opción que desea: ")
            os.system('cls')

            match roll_agregado:
                case "1":
                    print("Ha agregado un Pikachu Roll")
                    total_compra += 4500
                    n_pikachu += 1
                case "2":
                    print("Ha agregado un Otaku Roll")
                    total_compra += 5000
                    n_otaku += 1
                case "3":
                    print("Ha agregado un Pulpo Venenoso Roll")
                    total_compra += 5200
                    n_pulpo += 1
                case "4":
                    print("Ha agregado un Anguila Eléctrica Roll")
                    total_compra += 4800
                    n_anguila += 1
                case "5":
                    break
                case _:
                    print("Opción no válida")
                    print("Ingrese solo 1, 2, 3 o 4")

        monto_descuento, cliente_comprando = aplica_descuento(total_compra)

    os.system('cls')

    # Entrega boleta
    n_productos = n_pikachu + n_otaku + n_pulpo + n_anguila
    print("-"*34)
    print(f"TOTAL PRODUCTOS: {n_productos}")
    print("-"*34)
    print(f"Pikachu Roll: {n_pikachu}")
    print(f"Otaku Roll: {n_otaku}")
    print(f"Pulpo Venenoso Roll: {n_pulpo}")
    print(f"Anguila Eléctrica Roll: {n_anguila}")
    print("-"*34)
    print(f"Subtotal por pagar: ${total_compra}")
    print(f"DEscuento por código: ${monto_descuento}")
    print(f"TOTAL: {total_compra-monto_descuento}")

    if ordena_de_nuevo():
        n_pikachu = 0
        n_otaku = 0
        n_pulpo = 0
        n_anguila = 0
        n_productos = 0
        total_compra = 0
        monto_descuento = 0

        cliente_comprando = True

    else:
        cliente_en_local = False
