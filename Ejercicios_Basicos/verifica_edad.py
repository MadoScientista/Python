# Pide al usuario nombre y edad
# Verifica si el usuario es mayor de edad
# Informa el resultado al usuario

nombre = input("Ingresa tu nombre: ")    # Input recibe String
edad = int(input("Ingresa tu edad: "))   # int() convierte String a Integer


# Evalúa si su edad es igual o mayor de 18
if edad >= 18:                           
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")