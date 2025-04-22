"""------|Califica edad|---------
* Menor de 12 niño/a
* Entre 12 y 17 adolescente
* Entre o igual a 17 y 64 adulto
* Mayor de 65 adulto mayor
*----------------------------"""


# Solicita edad
edad = int(input("Ingrese edad: "))

# Califica edad
if edad < 12:
    print("Es un niño/a")

elif edad >= 12 and edad < 18:    
    print("Es un adolescente")

elif edad >= 18 and edad <= 65:
    print("Es un adulto")
    
else:
    print("Es un adulto mayor")
