from Class.Pieces.Piece import *

class Knight(Piece):
    """Permet de créer un cavalier enfant de Piece"""

    def __init__(self, color):

        super().__init__("N", color)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass