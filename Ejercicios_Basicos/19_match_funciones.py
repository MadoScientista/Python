# Uso y explicación de match

msj_options = '''Ingrese una operación
1.- Suma
2.- Resta
3._ Multiplicación
4.- División
5.- Salir
'''
def suma():
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    print(f"La suma de {n1} y {n2} es {n1+n2}")

def resta():
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    print(f"La resta de {n1} y {n2} es {n1-n2}")

def multiplicar():
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    print(f"La la multiplicación de {n1} y {n2} es {n1*n2}")

def division():
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    print(f"La la división de {n1} y {n2} es {n1/n2}")

def calculadora():
    while True:
        option = int(input(msj_options))

        match option:
            case 1:
                print("Ha seleccionado suma")
                suma()
            case 2:
                print("Ha seleccionado resta")
                resta()
            case 3:
                print("Ha seleccionado multiplicación")
                multiplicar()
            case 4:
                print("Ha seleccionado división")
                division()
            case 5:
                print("Saliendo del programa")
                break
            case _:
                print("opción inválida")

calculadora()