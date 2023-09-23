from Class.Pieces.Piece import *


class Bishop(Piece):
    """Permet de créer un fou enfant de Piece"""

    def __init__(self, color):

        super().__init__("B", color)

    def LegalMoves(self, Board):
        y,x = self.posy,self.posx
        legalmoves = []
    

