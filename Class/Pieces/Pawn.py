from Class.Pieces.Piece import *


class Pawn(Piece):
    """Permet de créer un pion enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("P", color) #Attention les notations ne contiennent pas le "P" !

    def LegalMoves(self, Board, x, y):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        pass