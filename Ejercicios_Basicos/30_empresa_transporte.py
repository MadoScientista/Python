# Kilos Categoria Valor
# 1-5    Liviana   1000
# 6-10   Normal    2000

import os

cantidad_paquetes = 0

precios = [
    {"categoría": "Liviana", "min": 1, "max": 5, "valor": 1000},
    {"categoría": "Normal", "min": 6, "max": 10, "valor": 2000},
]

paquetes_de_cliente = {}

paquetes_livianos = 0
paquetes_normales = 0
no_clasificados = 0
precio_livianos = 1000
precio_normales = 2000
total = 0

os.system('cls')
while cantidad_paquetes <= 0:
    try:
        cantidad_paquetes = int(input("Ingrese la cantidad de paquetes: "))
        os.system('cls')
    except ValueError:
        os.system('cls')
        print("Ingrese un número mayor a cero")

for paquete in range(cantidad_paquetes):
    peso = 0
    while peso <= 0:
        try:
            peso = float(input("Ingrese peso: "))
            os.system('cls')
        except ValueError:
            os.system('cls')
            print("Debe ingresar un valor mayor a cero")

    if 1 <= peso <= 5:
        paquetes_livianos += 1
    elif 6 <= peso <= 10:
        paquetes_normales += 1
    else:
        no_clasificados += 1

total = paquetes_normales*precio_normales + paquetes_livianos*precio_livianos
print("-"*42)
print(f"Total de paquetes: {paquetes_normales + paquetes_livianos}")
print("-"*42)
print(f"{paquetes_livianos} Paquetes livianos: ${paquetes_livianos*precio_livianos}")
print(f"{paquetes_normales} Paquetes normales: ${paquetes_normales*precio_normales}")
print("-"*42)
if no_clasificados > 0:
    print(f"{no_clasificados} No clasificados")
    print("Verifique valor en servicio al cliente")
print("-"*42)
print(f"Total a pagar: ${total}")
