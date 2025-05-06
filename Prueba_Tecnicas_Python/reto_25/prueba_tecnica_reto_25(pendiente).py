"""
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 *
 * Código Konami para Contra
 * 30 vidas
 ↑ ↑ ↓ ↓ ← → ← → a b
"""

import keyboard as kb
import time

extra_life_30 = ["flecha arriba", "flecha arriba", "flecha abajo", "flecha abajo",
                 "flecha izquierda", "flecha derecha", "flecha izquierda", "flecha derecha",
                 "a", "b"]

while True:
    if kb.read_key() == "q" or kb.read_key() == "flecha derecha":
        break

    print(kb.read_key())

print("fin")