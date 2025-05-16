# Crear un menú de carrito con las siguientes opciones
# 1.- Ingrese nombre del usuario
# Será mostrado en la boleta, con un saludo
# 2.- comprar, poner productos para poder comprar
# con su precio correspondiente
# 3.- Sacar boleta, calcular el precio neto 
# y el precio más el IVA. Mostrar totales
#bonus: contar la cantidad de artículos
# 4.- Salir
# Consideraciones:
# Por lo menos 3 productos
# No hay límite de compra
# Se puede salir en cualquier momento

import os

msj_bienvenida = "-"*35 + "\nBienvenido al carrito de compras\n" + "-"*35

msj_opciones = """Elige una opción:
1.- Ingrese nombre de cliente
2.- Comprar
3.- Sacar boleta
4.- Salir
"""

lista_productos = [
    ("mantequilla", 1200),
    ("azúcar", 1000),
    ("arroz", 1200),
    ("fideos", 890),
    ("bebida 2L", 1800),
    ("galletas", 870),
]


boleta = {
    "Nombre Cliente" : "Cliente",
    "Total Neto": 0,
    "Total con IVA": 0,
    "Productos": {}
}

def listar_productos(mis_productos):
    for i, producto in enumerate(mis_productos):
        print(f"{i+1}.- {producto[0].capitalize()}")

def verifica_entero(num_int):
    try:
        num_int = int(num_int)
        return num_int
    except ValueError:
        print("Ingresa solo números")

def nombre_en_boleta():
    os.system('cls')
    name = input("Ingresa nombre de cliente: ")
    return name

def comprar(lista_de_productos):
    os.system('cls')
    productos_que_lleva = {}
    total = 0

    while True:
        # Lista los productos disponibles
        print("-"*30)
        print("Productos disponibles:")
        print("-"*30)

        listar_productos(lista_de_productos)
        print('Ingrese "q" para salir')

        # Pide número de producto
        producto_seleccionado = input("¿Qué producto llevará? ")

        # Verifica si desea salir
        if producto_seleccionado == "q":
            break

        # verifica número de producto
        try:
            os.system('cls')
            producto_seleccionado = int(producto_seleccionado) - 1

            if producto_seleccionado not in range(len(lista_de_productos)):
                print("Número de producto no está en la lista")
            else:
                nombre_producto = lista_de_productos[producto_seleccionado][0]
                precio_producto = lista_de_productos[producto_seleccionado][1]

                total += precio_producto
                print(f"Se ha agregado {nombre_producto} al carro")
                print(f"El total actual es: {total}")


                if nombre_producto not in productos_que_lleva:
                    productos_que_lleva[nombre_producto] = 1

                else:
                    productos_que_lleva[nombre_producto] += 1

                # print(productos_que_lleva)
                

        except ValueError:
            print("Ingresa solo números")


    
    return productos_que_lleva, total, total*1.19

def sacar_boleta(mi_boleta:dict):

    print("-"*30)
    print(f"Nombre de cliente: {mi_boleta["Nombre Cliente"]}")
    print("-"*30)

    print(f"Total neto: {mi_boleta["Total Neto"]}")
    print(f"Total con IVA: {mi_boleta["Total con IVA"]}")

    print("-"*30)
    print("Los productos que lleva son: ")
    print("-"*30)

    productos_en_boleta = mi_boleta["Productos"]
    for i, x in productos_en_boleta.items():
        print(x,i.capitalize())

    print("-"*30)

def carrito_supermercado():

    os.system('cls')
    print(msj_bienvenida)
   
    while True:
        try:
            option = int(input(msj_opciones))

            match option:
                case 1:
                    boleta["Nombre Cliente"] = nombre_en_boleta()

                case 2:
                    boleta["Productos"], boleta["Total Neto"], boleta["Total con IVA"] = comprar(lista_productos)
                    os.system('cls')

                case 3:
                    os.system('cls')
                    sacar_boleta(boleta)
                    break

                case 4:
                    break

                case _:
                    os.system('cls')
                    print("-"*30)
                    print("Opción no válida")
                    print("-"*30)
                    
        except ValueError:
            os.system('cls')
            print("-"*30)
            print("Ingrese sólo números")
            print("-"*30)


carrito_supermercado()