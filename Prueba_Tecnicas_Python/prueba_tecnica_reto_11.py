"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
"""


def parameterUrl(url):
    parameters = {}

    if "?" in url:
        query = url.split("?")[1]
    else:
        return False

    while "=" in query:
        key = query[:query.index("=")]
        query = query[query.index("=")+1:]

        if "&" in query:
            value = query[:query.index("&")]
            query = query[query.index("&")+1:]
        else:
            value = query

        parameters[key] = value

    return parameters


print(parameterUrl("https://retosdeprogramacion.com?year=2023&challenge=0"))
print(parameterUrl("https://www.prueba.com?hola=2020&camlleo=12&solidicar=3&mouse=colegio"))
