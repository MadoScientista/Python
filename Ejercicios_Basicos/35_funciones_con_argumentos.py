# 1. Construya una función que calcule el IVA
#
# 2. Construya una función que al pasarle un precio
# y un número como porcentaje calcule el descuento
# y muestre el valor final
#


def calcula_iva(valor):
    iva = valor*0.19
    return iva

def calcula_descuento(valor, porcentaje):
    descuento = valor*porcentaje/100
    total_final = valor - descuento
    return total_final


precio = 2000
porcentaje_descuento = 10
iva = calcula_iva(precio)
precio_con_iva = precio + iva
precio_final = calcula_descuento(precio_con_iva, porcentaje_descuento)

print(f"Para un artículo cuyo valor neto es de {precio}")
print(f"El iva sería de {iva}")
print(f"El precio con iva sería {precio_con_iva}")
print(f"Si aplicamos un descuenti de {porcentaje_descuento}%")
print(f"El precio final del artículo sería de {precio_final}")