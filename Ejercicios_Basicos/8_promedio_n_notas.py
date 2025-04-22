"""------------------|Promedio n Notas|-----------------------
* - Pide al usuario ingresar la cantidad de notas a promediar
* - Usa el ciclo for para pedir una a una las notas
* - Calcula el promedio de notas
* - Informa si el estudiante ha aprobado
*----------------------------------------------------------"""

# Bienvenida
print("-"*40) # Escribe 40 veces el caracter "-""
print("Bienvenido a la calculadora de promedios")
print("-"*40)

n_Notas = int(input("Ingrese la cantidad de notas: "))
suma = 0

for i in range(n_Notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota

avg = suma/n_Notas
avg = round(avg, 1)
print(f"El promedio es {avg}")

# Evalúa si aprobó e informa el resultado
if avg >= 4.0:
    print("El/La estudiante ha aprobado")
else:
    print("El/La estudiante no ha aprobado")
print("-"*40)