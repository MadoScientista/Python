"""
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 * https://pokeapi.co/api/v2/pokemon/ditto
"""

import requests


# Pide el nombre de un pokemon
pokemon = input("Ingrese el nombre de un pokemon: ").lower()

# Agrega el nombre del pokemon a la URL y realiza llamada
URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
poke_info = requests.get(URL, timeout=5)

# Convierte la respuesta a Json y busca tipos de pokemon
poke_info_json = poke_info.json()
types_found = poke_info_json["types"]

# Concatena los tipos disponibles (pueden ser 1 o 2)
types_pokemon = f"El tipo de {pokemon} es: "

for types in types_found:
    types_pokemon += types["type"]["name"] + " "

# Muestra los tipos del pokemon
print(types_pokemon)
