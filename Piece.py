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

    def __init__(self, color: PieceColor, piece_type: PieceType, position: Tuple['int'], rect=None) -> None:
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
    def get_moves(self, board):
        moves = []
        match self.piece_type:
            case PieceType.Pawn:
                moves = self.pawn_moves(board)
            case PieceType.King:
                moves = self.king_moves(board)
            case PieceType.Rook:
                moves = self.rook_moves(board)
            case PieceType.Bishop:
                moves = self.bishop_moves(board)
            case PieceType.Knight:
                moves = self.knight_moves(board)
            case PieceType.Queen:
                moves = self.queen_moves(board)


        return moves


    def pawn_moves(self, board):
        (row, col) = self.position
        moves = []
        take_moves = []
        final_moves = []

        # Find all the possible moves and take moves for black piece
        if self.color == PieceColor.Black:
            moves = [(row, col + 1)]  # can move one column up
            take_moves = [(row - 1, col + 1), (row + 1, col + 1)]  # can take pieces diagonally
            if self.position[1] == 1:
                moves.append((row, col + 2))  # can move two columns up, if it's the pawn's first move

        # Find all the possible moves and take moves for white piece
        else:
            moves = [(row, col - 1)]
            take_moves = [(row + 1, col - 1), (row - 1, col - 1)]
            if self.position[1] == 6:
                moves.append((row, col - 2))

        # Filter the take moves so that a piece isn't able to take self colored piece
        for move in take_moves:
            (row, col) = move
            if row not in range(0, 8) or col not in range(0, 8):
                continue
            square = board[row][col]
            if square.contains_piece() and square.chessPiece.color != self.color:
                final_moves.append(move)

        # Filter out blocked moves
        for move in moves:
            (row, col) = move
            if row not in range(0, 8) or col not in range(0, 8):
                continue
            square = board[row][col]
            if square.contains_piece():
                continue
            else:
                final_moves.append(move)
        return final_moves

    def king_moves(self, board):
        (row, col) = self.position

        moves = [
            (row + 1, col + 1), (row + 1, col), (row + 1, col - 1),
            (row, col + 1), (row, col - 1),
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1)
        ]
        final_moves = []

        # Filter out blocked moves
        for move in moves:
            (row, col) = move
            if row not in range(0, 8) or col not in range(0, 8):
                continue
            square = board[row][col]
            if square.contains_piece() and square.chessPiece.color == self.color:
                continue
            else:
                final_moves.append(move)

        return final_moves

    def rook_moves(self, board):
        axes = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        final_moves = []
        (row, col) = self.position

        for ax in axes:
            new_row = row + ax[0]
            new_col = col + ax[1]
            while new_row in range(0, 8) and new_col in range(0, 8):
                square = board[new_row][new_col]
                if square.contains_piece():
                    if square.chessPiece.color == self.color:
                        break
                    else:
                        final_moves.append((new_row, new_col))
                        break
                else:
                    final_moves.append((new_row, new_col))
                new_row += ax[0]
                new_col += ax[1]

        return final_moves

    def bishop_moves(self, board):
        axes = [
            (1, 1),
            (1, - 1),
            (- 1, -1),
            (-1, 1)
        ]
        final_moves = []
        (row, col) = self.position

        for ax in axes:
            new_row = row + ax[0]
            new_col = col + ax[1]
            while new_row in range(0, 8) and new_col in range(0, 8):
                square = board[new_row][new_col]
                if square.contains_piece():
                    if square.chessPiece.color == self.color:
                        break
                    else:
                        final_moves.append((new_row, new_col))
                        break
                else:
                    final_moves.append((new_row, new_col))
                new_row += ax[0]
                new_col += ax[1]

        return final_moves
    
    def knight_moves(self, board):
        (row, col) = self.position
        moves = [
            # row 2
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),

            # column 2
            (row + 1, col - 2), (row - 1, col - 2),
            (row + 1, col + 2), (row - 1, col + 2),
        ]
        final_moves = []
        for move in moves:
            (row, col) = move

            if row not in range(0, 8) or col not in range(0, 8):
                continue

            square = board[row][col]
            if square.contains_piece():
                if square.chessPiece.color == self.color:
                    continue
                else:
                    final_moves.append(move)
            else:
                final_moves.append(move)

        return final_moves
    
    def queen_moves(self, board):
        return self.bishop_moves(board) + self.rook_moves(board)
