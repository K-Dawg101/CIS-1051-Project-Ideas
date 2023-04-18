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