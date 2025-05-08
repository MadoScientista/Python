"""
 Crea un algoritmo que a partir de un número ingresado
 por el usuario, se muestre en pantalla si el número ingresado
 es par o impar, seguido de los números pares e impares
"""

num = int(input("Ingresa un número: "))

if not num % 2:
    print(f"{num} es par")
else:
    print(f"{num} es impar")

pares = ""
impares = ""

for n in range(1, num+1):
    if not n % 2:
        pares += " " + str(n)
    else:
        impares += " " + str(n)

print(f"Son pares:{pares}")
print(f"Son impares:{impares}")
