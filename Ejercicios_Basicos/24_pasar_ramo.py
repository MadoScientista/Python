# Quiere pasar el ramo?
# Preguntar la cantidad de rojos en el curso 
# Los talleres que hay en el semestre son 4
# Por cada taller asistido obtiene 0.3
# Si el alumno tiene más de 1 punto 
# tiene la bendición del rpofesor
# sino, no se le puede ayudar
# ingrese la nota final y la suma de las décimas cumuladas
# Muestre si aprueba o reprueba


while n_perros < 1:
    try:
        n_perros = int(input("Ingrese la cantidad de perros: "))
        
        if n_perros < 0:
            print("-"*40)
            print("Ingrese solo números enteros positivos")
            print("-"*40)
            n_perros = 0
        
    except ValueError as error:
        # print(error)
        print("Ingrese solo números enteros positivos")