import os

n_pasajes = 0
total_ventas = 0
valor_pasaje = 0

a = ""
os.system('cls')
while n_pasajes <= 0:
    print("─"*50)
    print("Venta de pasajes".center(50))
    print("─"*50)

    try:
        n_pasajes = int(input("Ingrese la cantidad de pasajes: "))
        os.system('cls')
    except ValueError:
        os.system('cls')
        print("Debe ingresar un número mayor a cero")


for pasaje in range(n_pasajes):

    valor_pasaje = 0

    while valor_pasaje <= 0:
        print("─"*50)
        print(f"Ingrese el valor del {pasaje+1}° pasaje".center(50))
        print("─"*50)

        try:
            valor_pasaje = int(input())
            total_ventas += valor_pasaje
            os.system('cls')
        except ValueError:
            os.system('cls')
            print("Debe ingresar un número mayor a cero")

        print(f"Total parcial de ventas: {total_ventas}")

os.system('cls')
print("─"*50)
print(f"Total Ventas: {total_ventas}".center(50))
print("─"*50)
