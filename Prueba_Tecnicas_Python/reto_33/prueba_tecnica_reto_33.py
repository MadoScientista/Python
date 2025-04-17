"""
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 """

import numpy as np
import os
import keyboard


class Tetris():

    def __init__(self, bg_width=10, bg_height=10, piece_pixel="🔳", bg_pixel="🔲"):
        self.bg_width = bg_width
        self.bg_height = bg_height
        self.piece_pixel = piece_pixel
        self.bg_pixel = bg_pixel
        self.background = np.zeros((10, 10))
        self.piece = Piece()
        self.keys = ['esc', 'a', 's', 'd', 'w']
        self.screen = self.createScreen()
        self.command_input = 0

    def createScreen(self):
        self.background = np.zeros((10, 10))
        row_0 = self.piece.row_0
        row_f = self.piece.row_f
        column_0 = self.piece.column_0
        column_f = self.piece.column_f

        self.background[row_0:row_f, column_0:column_f] = self.piece.form_piece
        return self.background

    def showScreen(self):
        os.system('cls')
        self.screen = self.createScreen()

        for row in self.screen:
            row_screen = ""
            for _ in row:
                if _:
                    row_screen += f'{self.piece_pixel} '
                else:
                    row_screen += f'{self.bg_pixel} '
            print(row_screen)

        print("Mueve la pieza con ASD y rota con W. Presiona esc para salir")

    def move_piece(self, key_input):
        if key_input == 'a' and self.piece.column_0 > 0:
            self.piece.move(0, -1)

        elif key_input == 's' and self.piece.row_f < self.bg_height:
            self.piece.move(1, 0)

        elif key_input == 'd' and self.piece.column_f < self.bg_width:
            self.piece.move(0, 1)

        elif key_input == 'w':
            self.piece.rotate()

    def waitKeys(self):
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name in self.keys:
            return event.name

    def gameBegin(self):

        while True:
            self.showScreen()
            key_pressed = self.waitKeys()
            self.move_piece(key_pressed)

            if key_pressed == 'esc':
                break

        print("Juego terminado")


class Piece():

    def __init__(self, piece_array=[[1, 0, 0], [1, 1, 1]]):
        self.form_piece = np.array(piece_array)
        self.row_0 = 0
        self.column_0 = 0
        self.row_f = self.form_piece.shape[0]
        self.column_f = self.form_piece.shape[1]

    def rotate(self):
        self.form_piece = np.rot90(self.form_piece, k=-1)
        self.row_f = self.row_0 + self.form_piece.shape[0]
        self.column_f = self.column_0 + self.form_piece.shape[1]

    def move(self, row, column):
        self.row_0 += row
        self.column_0 += column
        self.row_f = self.row_0 + self.form_piece.shape[0]
        self.column_f = self.column_0 + self.form_piece.shape[1]


tetris = Tetris()

tetris.gameBegin()
