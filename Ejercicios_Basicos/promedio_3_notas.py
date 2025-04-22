# Ingresa 3 notas
# Calcula promedio
# Informa si aprobó

print("-"*40)
print("Bienvenido a la calculadora de promedios")
print("-"*40)

num1 = float(input("Ingresa la primera nota: "))
num2 = float(input("Ingresa la segunda nota: "))
num3 = float(input("Ingresa la tercera nota: "))

avg = (num1+num2+num3)/3

print("-"*30)
print(f"El promedio entre {num1}, {num2}, {num3} es: {avg}")

if avg >= 4.0:
    print("El/La estudiante ha aprobado")
else:
    print("El/La estudiante no ha aprobado")
print("-"*40)



