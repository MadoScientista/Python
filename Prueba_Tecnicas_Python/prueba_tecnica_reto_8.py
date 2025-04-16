""" Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de 
programación seleccionado.
 
- Es más complicado de lo que parece...

Atributos datetime now: year, month, day, hour, minute, second,
microsecond , y tzinfo.

"""


from datetime import datetime


def randomNum():
    seed = datetime.now().microsecond
    seed = list(str(seed))
    random_number = int(seed[0]) + int(seed[1])

    if int(seed[4]) < 3:
        random_number = int(seed[0])
    elif int(seed[4]) < 8:
        random_number = int(seed[0]+seed[1])
    elif int(seed[3]) < 2:
        random_number = 100

    return random_number
