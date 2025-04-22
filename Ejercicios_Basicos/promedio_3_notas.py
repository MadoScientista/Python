# Ingresa 3 notas
# Calcula promedio
# Informa si aprobó


# Bienvenida
print("-"*40)
print("Bienvenido a la calculadora de promedios")
print("-"*40)

# Solicita datos
# input recibe String y float() convierte a decimal (float)
num1 = float(input("Ingresa la primera nota: "))
num2 = float(input("Ingresa la segunda nota: "))
num3 = float(input("Ingresa la tercera nota: "))

# Calcula el promedio
avg = (num1+num2+num3)/3

# Informa al usuario el promedio
print("-"*30)
print(f"El promedio entre {num1}, {num2}, {num3} es: {avg}")

# Evalúa si aprobó e informa el resultado
if avg >= 4.0:
    print("El/La estudiante ha aprobado")
else:
    print("El/La estudiante no ha aprobado")
print("-"*40)



