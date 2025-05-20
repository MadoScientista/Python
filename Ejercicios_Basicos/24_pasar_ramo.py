# Quiere pasar el ramo?
# Preguntar la cantidad de rojos en el curso 
# Los talleres que hay en el semestre son 4
# Por cada taller asistido obtiene 0.3
# Si el alumno tiene más de 1 punto 
# tiene la bendición del rpofesor
# sino, no se le puede ayudar
# ingrese la nota final y la suma de las décimas cumuladas
# Muestre si aprueba o reprueba

from random import randint

# Inicializa variables necesarias
n_rojos = 0
asistencia = 0
nota = 0

# Pregunta la cantidad de rojos en el curso
while n_rojos < 1:
    try:
        n_rojos = int(input("Ingrese la cantidad de rojos: "))

        if n_rojos < 0:
            print("-"*40)
            print("Ingrese solo números enteros positivos")
            print("-"*40)
            n_rojos = 0
        
    except ValueError as error:
        # print(error)
        print("Ingrese solo números enteros positivos")



for i in range(n_rojos):
    nota = randint(10, 39)/10
    asistencia = randint(1, 4)

    print(f"Estudiante n°{i+1} obtuvo un {nota}")

    if asistencia == 4:
        nota += 1.2

    if nota >= 4:
        print(f"asistió a {asistencia} talleres, ha aprobado con un {nota}")
    else:
        print(f"asistió a {asistencia} talleres, ha reprobado con un {nota}")