"""------|Promedio de 3 notas|-------------
* Solicita al usuario ingresar 3 notas
* Convierte los Strings ingresados a Float
* Calcula el promedio de notas
* Informa el promedio en pantalla
*---------------------------------------"""


# Bienvenida
print("-"*40) # Escribe 40 veces el caracter "-""
print("Bienvenido a la calculadora de promedios")
print("-"*40)

# Solicita datos
# input recibe String y float() convierte a decimal (float)
num1 = float(input("Ingresa la primera nota: "))
num2 = float(input("Ingresa la segunda nota: "))
num3 = float(input("Ingresa la tercera nota: "))

# Calcula el promedio
avg = (num1+num2+num3)/3

# Redondeamos a 1 decimal
avg = round(avg, 1)

# Informa al usuario el promedio
print("-"*30)
print(f"El promedio entre {num1}, {num2}, {num3} es: {avg}")

# Evalúa si aprobó e informa el resultado
if avg >= 4.0:
    print("El/La estudiante ha aprobado")
else:
    print("El/La estudiante no ha aprobado")
print("-"*40)



