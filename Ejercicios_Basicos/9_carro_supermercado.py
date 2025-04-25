'''
* Preguntar al usuario cuantos productos llevará
* Escribir listado de 3 productos y sus precios
" Mostrar el total neto de la compra
* Mostrar el total más iva (19%)
'''


import os


# Lista de productos
products = [
    ("Mantequilla", 1000),
    ("Arroz", 1200),
    ("Aceite", 1800),
    ("Azúcar", 1100),
    ("Pan", 1000),
    ("Té", 800),
    ("Sal", 850)
]

# Inicialización variables
total_neto = 0
total_iva = 0
prod_select = 0
n_products = 0

# Limpia pantalla y da la bienvenida
os.system('cls')

print("-"*40)
print("Bienvenido al carrito de compras")
print("-"*40)


# Solicita número de productos
n_products = int(input("¿Cuántos productos llevará? "))


for i in range(n_products):

    os.system('cls')

    # Muestra lisata de productos
    print("-"*40)
    for idx, product in enumerate(products):
        print(f"{idx+1}. {product[0]}: ${product[1]}")
    print("-"*40)

    # Muestra total parcial neto y con iva
    print(f"El total parcial neto es: {total_neto}")
    print(f"El total parcial con iva es: {total_iva}")
    print("-"*40)

    # Solicita número de producto
    prod_select = int(input("¿Qué producto llevará? ")) - 1

    # Si el número no está en la lista, vuelve a preguntar
    while prod_select not in range(len(products)):
        print("Producto no está dentro de la lista")
        prod_select = int(input("¿Qué producto llevará? ")) - 1

    # Suma el producto
    total_neto += products[prod_select][1]
    total_iva = total_neto*1.19

# Limpia pantalla y muestra el total neto y con iva de la compra
os.system('cls')

print("-"*40)
print(f"El total neto de su compra es de: {total_neto}")
print(f"El total con iva de su compra es de: {total_iva}")
print("-"*40)
