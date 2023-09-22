from Class.Pieces.Piece import *


class Knight(Piece):
    """Permet de créer un cavalier enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("N", color, x, y)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass