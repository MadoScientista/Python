"""------------------------------------------------------------------------------------------------
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
*------------------------------------------------------------------------------------------------"""


nav_menu = [
    "Inicio",
    "Blog",
    "Compras",
    "Contactanos",
    "Sobre nosotros"
]

actual_pag = 0

title = f"--------|{nav_menu[actual_pag]}|----------"
back = "1. atrás|"
forward = "|2. adelante"

print()
