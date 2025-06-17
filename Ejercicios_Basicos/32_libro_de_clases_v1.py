'''
Tarea
Crear programa de manejo de notas
1.- Ingresar nota
2.- Borrar nota
3.- Mostar notas
4.- Sacar promedio, nota mayor y nota menor
5.- Limpiar todas las notas
6.- Salir
'''

import os

def mostrar_menu():
    print("Libro de clases".center(60))
    print("-"*60)
    print("1.- Ingresar nota")
    print("2.- Borrar nota")
    print("3.- Mostar notas")
    print("4.- Sacar promedio, nota mayor y nota menor")
    print("5.- Limpiar todas las notas")
    print("6.- Salir")
    print("-"*60)

def mostrar_notas(notas:list):
    for numero, nota in enumerate(notas):
        print(f"Nota {numero+1}: {nota}")

def mostrar_nota_y_promedio(notas:list):
    nota_alta = max(notas)
    nota_baja = min(notas)

    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma/len(notas)

    print("Notas".center(60))
    print("-"*60)
    mostrar_notas(notas)
    print("-"*60)
    print(f"Nota más alta: {nota_alta}")
    print(f"Nota más baja: {nota_baja}")
    print("-"*60)
    print(f"Promedio: {promedio}")
    print("-"*60)
    print("Presione enter para volver al menú principal")

    input()
    os.system('cls')

lista_de_notas = []
libro_abierto = True

os.system('cls')
while libro_abierto:

    # Mostrar menú y recibir opción del usuario
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese el número de la opción que desea: "))
            os.system('cls')
        
            if opcion in range(6):
                break
            print("Las opciones disponibles son (1-6)")

        except ValueError:
            print("Ingrese solo números enteros (1-6)")


    # Realizar acción según opción del usuario
    match opcion:

        case 1:  # 1.- Ingresar nota

            while True:
                print("Ingresando notas".center(60))
                print("-"*60)
                print("Ingrese la nota sin punto decimal")
                print("Ejemplo: Para un 6,5 ingrese 65")
                print("-"*60)

                try:
                    nota = int(input("Ingrese nota: "))
                    os.system('cls')

                    if 10 <= nota <= 70:
                        lista_de_notas.append(nota/10)
                        print(f"Se ha agregado {nota/10} a la lista de notas")
                        print("-"*60)
                        print('Presione enter para agregar otra nota')
                        otra_nota = input('ingrese "s" para volver al menú principal: ')
                        os.system('cls')

                        if otra_nota == "s":
                            break
                        
                    else:
                        print("La nota debe estar entre 10 y 70")

                except ValueError:
                    os.system('cls')
                    print("Error al ingersar nota")
                    print("Ingrese solo números entre 10 y 70")
                    print("-"*60)
                    print("Presione enter para continuar")
                    input()
                    os.system('cls')

        case 2:  # 2.- Borrar nota

            if lista_de_notas:
                while True:

                    if len(lista_de_notas) == 1:
                        print("solo existe una nota disponible")
                        print(f"Nota 1: {lista_de_notas[0]}")
                        print("-"*60)

                        eliminar_nota = input('Ingrese "s" si desea eliminar la nota: ')
                        os.system('cls')

                        if eliminar_nota == "s":
                            print("Se ha eliminado la nota con éxito")
                            print("-"*60)
                        break

                    print("Notas disponibles".center(60))
                    print("-"*60)
                    mostrar_notas(lista_de_notas)
                    print("-"*60)

                    try:
                        print(f"Ingrese el número de la nota que desea eliminar ({1}-{len(lista_de_notas)})")
                        nota = int(input()) - 1
                        os.system('cls')

                        if nota in range(len(lista_de_notas)):
                            print(f"Se ha eliminado {lista_de_notas[nota]} con éxito")
                            lista_de_notas.pop(nota)
                            break

                        print(f"Las opciones disponibles son 1-{len(lista_de_notas)}")
                    except:
                        os.system('cls')
                        print("Error al borrar nota")
                        print("Ingrese solo números enteros")
                        print("-"*60)
                        input("Presione enter para continuar\n")
                        os.system('cls')

        case 3:  # 3.- Mostar notas
            print("Notas disponibles".center(60))
            print("-"*60)
            mostrar_notas(lista_de_notas)
            print("-"*60)

            print("Presione enter para volver a menú principal")
            input()
            os.system('cls')

        case 4:  # 4.- Sacar promedio, nota mayor y nota menor

            mostrar_nota_y_promedio(lista_de_notas)

        case 5:  # 5.- Limpiar todas las notas
            lista_de_notas.clear()
            print("Se han limpiado todas las notas con éxito")
            print("-"*60)
            input("Presione enter para volver al menú principal\n")
            os.system('cls')

        case 6:  # Salir
            libro_abierto = False
            print("Cerrando libro de clases ¡Hasta luego!")


    
