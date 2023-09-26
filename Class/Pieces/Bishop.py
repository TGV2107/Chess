from Class.Pieces.Piece import *


class Bishop(Piece):
    """Permet de créer un fou enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("B", color)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass