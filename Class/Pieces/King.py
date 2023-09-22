from Class.Pieces.Piece import *


class King(Piece):
    """Permet de créer un roi enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("K", color, x, y)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass