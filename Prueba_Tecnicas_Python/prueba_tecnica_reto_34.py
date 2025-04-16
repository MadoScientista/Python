"""
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 """

import os


def showText():
    os.system("cls")
    with open("text.txt", "r") as file:
        print("Actualemente el archivo text.txt contiene lo siguiente:\n")
        print(file.read()+"\n")


os.system("cls")
print("---Gestión de archivo text.txt---\n\n")

if not os.path.exists("text.txt"):
    with open("text.txt", "r") as file:
        print("Se ha creado el archivo text.txt\n")

else:
    print("Se ha encontrado el archivo text.txt\n")


def gestionTxt():
    while True:
        option = input("\n¿Qué desea hacer con el archivo?\n \
                        \n(1) Escribir una nueva línea \
                        \n(2) Borrar todo y volver a escribir \
                        \n(3) Salir \
                    \n\nOpción: ")

        os.system('cls')

        if option == "1":

            showText()

            with open("text.txt", "a") as file:
                text_line = input("Ingresa una nueva línea de texto: \n")
                file.write("\n"+text_line)

            showText()

        if option == "2":
            with open("text.txt", "w") as file:
                text_line = input("Ingresa una nueva línea de texto: \n")
                file.write(text_line)

            showText()

        if option == "3":
            os.system('cls')
            print("Has salido del programa")
            break


gestionTxt()
