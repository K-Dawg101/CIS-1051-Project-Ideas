from typing import List
import pygame as pyg
from Piece import Piece
from Square import Square


class ChessGame:

    def __init__(self):
        pyg.init()
        self.board = None
        self.screen = pyg.display.set_mode((800, 800))
        self.darkSquareColor = "#B78962"
        self.lightSquareColor = "#EFD9B5"
        self.board: List['Square']
        self.startingPosition = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
        ]
        self.gameRunning = True

    def start_game(self):
        self.draw_board()
        self.add_pieces()
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

    def add_pieces(self, pos=None):
        # TODO: position reading
        if pos:
            return

        for i in range(8):
            for j in range(8):
                if self.startingPosition[i][j].strip():
                    self.board[j][i].place_chess_piece(
                        Piece.from_short_anotation(self.startingPosition[i][j], (j, i))
                    )
                    if self.startingPosition[i][j] == "wk":
                        self.white_king = self.board[j][i]
                    elif self.startingPosition[i][j] == "bk":
                        self.black_king = self.board[j][i]
        self.draw_pieces()

    def draw_pieces(self):
        # self.images = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j].contains_piece():
                    img = pyg.image.load(self.board[i][j].chessPiece.image)
                    img = pyg.transform.scale(img, (100, 100))
                    rect = img.get_rect()
                    rect.topleft = (i * 100, j * 100)
                    self.board[i][j].chessPiece.rect = rect
                    self.board[i][j].chessPiece.blit_image = img

                    self.screen.blit(img, (i * 100, j * 100))