# crear un programa que pida la cantidad de asignaturas
# luego pida el promedio de cada asignatura
# basados en su promedio final, aplicar puntaje
# de beneficios
# 4.5 y 5: 300
# 5.1 y 6.0: 500
# 6.1 y 7.0: 800
# Agregar puntaje según carrera
# Técnico:+60
# Ingeniería: +40 
# Diplomado: +20

n_asignaturas = 0
promedio = 0
promedio_asignatura = 0
suma_parcial = 0
puntaje_nota = 0
puntaje_carrera = 0

n_asignaturas = int(input("Ingrese cantidad de asignaturas: "))

for i in range(n_asignaturas):
    promedio_asignatura = int(input(f"Ingrese promedio de la asignatura n°{i}: "))
    suma_parcial += promedio_asignatura

promedio = suma_parcial/n_asignaturas

if promedio < 4.5:
    puntaje_nota += 0
elif promedio >= 4.5 and promedio <= 5:
    puntaje_nota += 300
