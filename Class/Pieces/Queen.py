from Class.Pieces.Piece import *

class Queen(Piece):
    """Permet de créer une dame enfante de Piece"""

    def __init__(self, color, x, y):

        super().__init__("Q", color, x, y)

    def LegalMoves(self, Board):

        self.get