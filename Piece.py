from enum import Enum
from typing import Tuple
from Square import Square


class PieceType(Enum):
    Rook = 0
    Bishop = 1
    Knight = 2
    King = 3
    Queen = 4
    Pawn = 5


class PieceColor(Enum):
    Black = 0
    White = 1


class Piece:

    def __init__(self, color: PieceColor, piece_type: PieceType, position: Tuple['int'],  rect=None) -> None:
        self.color = color
        self.piece_type = piece_type
        self.short_annotation = "w" if self.color == PieceColor.White else "b"
        self.rect = rect
        self.position: Tuple['int'] = position

        match piece_type:
            case PieceType.Rook:
                self.short_annotation += 'r'
            case PieceType.Bishop:
                self.short_annotation += 'b'
            case PieceType.Knight:
                self.short_annotation += 'n'
            case PieceType.Queen:
                self.short_annotation += 'q'
            case PieceType.Pawn:
                self.short_annotation += 'p'
            case PieceType.King:
                self.short_annotation += 'k'
        self.image = f'images/pieces/{self.short_annotation}.png'

        self.alive = True

    def from_short_anotation(short_annotation: str, position):
        if len(short_annotation) != 2:
            return

        piece_type = None
        color = PieceColor.White if short_annotation[0] == 'w' else PieceColor.Black

        match short_annotation[1]:
            case 'b':
                piece_type = PieceType.Bishop
            case 'r':
                piece_type = PieceType.Rook
            case 'n':
                piece_type = PieceType.Knight
            case 'k':
                piece_type = PieceType.King
            case 'q':
                piece_type = PieceType.Queen
            case 'p':
                piece_type = PieceType.Pawn
        piece = Piece(color, piece_type, position)

        return piece
    def get_pawn_moves(self, board):
        (row, col) = self.position
        possible_moves = []
        take_moves = []
        final_moves = []

        # Find all the possible moves and take moves for black piece
        if self.color == PieceColor.Black:
            possible_moves = [(row, col + 1)] # can move one column up
            take_moves = [(row - 1, col + 1), (row + 1, col + 1)] # can take pieces diagonally
            if self.position[1] == 1:
                possible_moves.append((row, col + 2)) # can move two columns up, if it's the pawn's first move

        # Find all the possible moves and take moves for white piece
        else:
            possible_moves = [(row, col - 1)]
            take_moves = [(row + 1, col - 1), (row - 1, col - 1)]
            if self.position[1] == 6:
                possible_moves.append((row, col - 2))

        # Filter the take moves so that a piece isn't able to take self colored piece
        for move in take_moves:
            (move_row, move_col) = move
            if move_row not in range(0, 8) or move_col not in range(0, 8):
                continue
            square = board[move_row][move_col]
            if square.containsChessPiece() and square.chessPiece.color != self.color:
                final_moves.append(move)

        # Filter the possible moves so that a piece may not move when blocked
        for move in possible_moves:
            (move_row, move_row) = move
            if move_row not in range(0, 8) or col not in range(0, 8):
                continue
            square = board[move_row][move_col]
            if square.containsChessPiece:
                continue
            else:
                final_moves.append(move)
        return final_moves