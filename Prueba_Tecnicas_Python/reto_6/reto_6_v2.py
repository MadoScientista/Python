"""-------------------------------|RETO 6|---------------------------------------
* Crea un programa que calcule quien gana más partidas al piedra, papel, 
* tijera, lagarto, spock.
*
* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
* - La función recibe un listado que contiene pares, representando cada jugada.
* - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
*   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
* - Ej. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
* - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
*
* REGLAS DEL JUEGO 
*
* Tijeras cortan papel.
* Papel cubre piedra.
* Piedra aplasta a lagarto.
* Lagarto envenena a Spock.
* Spock aplasta tijeras.
* Tijeras decapitan a lagarto.
* Lagarto come papel.
* Papel refuta a Spock.
* Spock vaporiza piedra.
* Piedra rompe tijeras.
*-------------------------------------------------------------------------------"""


import random
import os


def random_hands(n_plays):
    """Devuelve una lista con pares de jugadas aleatorias"""

    hands = ["piedra", "papel", "tijeras", "lagarto", "spock"]
    p1_p2 = []

    while len(p1_p2) < n_plays:
        n1 = random.randint(0, 4)
        n2 = random.randint(0, 4)

        p1_p2.append((hands[n1], hands[n2]))

    return p1_p2


def start_game(hands):
    """Imprime partidas jugadas, resultados parciales y ganador"""

    os.system('cls')

    print("-"*30)
    print("Comienza el juego")
    print("-"*30)

    rules = {"tijeras": ("papel", "lagarto"),
             "papel": ("piedra", "spock"),
             "piedra": ("tijeras", "lagarto"),
             "lagarto": ("spock", "papel"),
             "spock": ("tijeras", "piedra")}

    player_1 = 0
    player_2 = 0
    tie = 0

    for hand in hands:
        print("-"*30)
        print(f'Player_1: {hand[0]} | Player_2: {hand[1]}')

        if hand[1] in rules[hand[0]]:
            player_1 += 1
        elif hand[0] in rules[hand[1]]:
            player_2 += 1
        else:
            tie += 1
        print(f'player_1: {player_1}, player_2: {player_2}, tie: {tie}')

    print("-"*30)
    if player_1 > player_2:
        return "player_1"
    if player_2 > player_1:
        return "player_2"
    return "tie"


games_plays = random_hands(5)
print(start_game(games_plays))
