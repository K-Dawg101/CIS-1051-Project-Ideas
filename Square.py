class Square:
    def __init__(self, row: int, col: int, rectangle=None, chessPiece=None):
        self.hasPiece = chessPiece is not None
        self.chessPiece = chessPiece
        self.col = col
        self.row = row
        self.position = (row, col)
        self.rectangle = rectangle

    def place_chess_piece(self, chessPiece):
        if not chessPiece:
            return
        self.chessPiece = chessPiece
        self.hasPiece = True

    def contains_piece(self):
        return self.chessPiece is not None

