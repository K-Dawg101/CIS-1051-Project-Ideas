from typing import List
import pygame as pyg
from Square import Square


class ChessGame:

    def __init__(self):
        pyg.init()
        self.board = None
        self.screen = pyg.display.set_mode((800, 800))
        self.darkSquareColor = "#B78962"
        self.lightSquareColor = "#EFD9B5"
        self.gameRunning = True

    def start_game(self):
        self.draw_board()
        pyg.display.flip()
        self.play_game()

    def draw_board(self):
        self.screen.fill((0, 0, 0))
        self.board = [["  " for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                color = self.lightSquareColor
                is_dark_colored_spot = (i + (j + 1)) % 2 == 0
                if is_dark_colored_spot:
                    color = self.darkSquareColor
                self.board[i][j] = Square(i, j, pyg.draw.rect(self.screen, color, [i * 100, j * 100, 100, 100]))

    def play_game(self):
        while self.gameRunning:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.gameRunning = False
                    return
