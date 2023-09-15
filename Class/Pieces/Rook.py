from Class.Pieces.Piece import *

class Rook(Piece):
    """Permet de créer une tour enfante de Piece"""

    def __init__(self, color):

        super().__init__("R", color)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass