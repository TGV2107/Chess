from Class.Pieces.Piece import *
from Class.Pieces.Bishop import *
from Class.Pieces.Rook import *
from Class.Game import *

class Queen(Piece):
    """Permet de créer une dame enfante de Piece"""

    def __init__(self, color, x, y):
        self.color = color

        super().__init__("Q", x, y)
    
    def __str__(self) -> str:
        return "Ceci est une Dame"

    def getLegalMoves(self, Board):
        y, x = self.posy, self.posx
        legalmoves = []

        # Ajouter les mouvements de la tour (rook)
        legalmoves.extend(Rook(self.color, y, x).getLegalMoves(Board))

        # Ajouter les mouvements du fou (bishop)
        legalmoves.extend(Bishop(self.color, y, x).getLegalMoves(Board))

        return legalmoves

        

