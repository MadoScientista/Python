"""-------------------------------|RETO 6|----------------------------------------------
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.


Las tijeras cortan el papel.
El papel cubre la piedra.
La piedra aplasta el lagarto.
El lagarto envenena a Spock.
Spock aplasta las tijeras.
Las tijeras decapitan el lagarto.
El lagarto se come el papel.
El papel refuta a Spock.
Spock vaporiza la piedra.
La piedra aplasta a las tijeras.
"""

# juegos       player_1  Player_2
games_plays = [("spock", "lagarto"),
               ("papel", "piedra"),
               ("lagarto", "spock"),
               ("papel", "papel"),
               ("tijeras", "piedra")]


def ganador(games):
    wins = {"tijeras": ("papel", "lagarto"),
            "papel": ("piedra", "spock"),
            "piedra": ("tijeras", "lagarto"),
            "lagarto": ("spock", "papel"),
            "spock": ("tijeras", "piedra")}

    player_1 = 0
    player_2 = 0
    tie = 0

    for game in games:
        print(f'Player_1: {game[0]} | Player_2: {game[1]}')

        if game[1] in wins[game[0]]:
            player_1 += 1
        elif game[0] != game[1]:
            player_2 += 1
        else:
            tie += 1
        print(f'player_1 :{player_1}, player_2 :{player_2}, tie :{tie}')
        print("-"*25)

    if player_1 > player_2:
        return "player_1"
    if player_2 > player_1:
        return "player_2"
    return "tie"


print(ganador(games_plays))
