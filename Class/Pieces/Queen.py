from Class.Pieces.Piece import *

class Queen(Piece):
    """Permet de créer une dame enfante de Piece"""

    def __init__(self, color):

        super().__init__("Q", color)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass