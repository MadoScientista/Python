"""----|Califica edad|-------
* Menor de 12 niño/a
* Entre 12 y 17 adolescente
* Mayor o igual a 18 adulto
*-------------------------"""


# Solicita edad
edad = int(input("Ingrese edad: "))

# Califica edad
if edad < 12:
    print("Es un niño/a")
elif edad >= 12 and edad < 18:    # elif es lo mismo que else -if
    print("Es un adolescente")
else:
    print("Es un adulto")




