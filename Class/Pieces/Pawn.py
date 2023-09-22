from Class.Pieces.Piece import *


class Pawn(Piece):
    """Permet de créer un pion enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("P", color) #Attention les notations ne contiennent pas le "P" !

    def LegalMoves(self, Board)->list:
        y,x = self.posy, self.posx

        if self.Color == "White":
            moveDirection = 1
        
        elif self.Color == "Black":
            moveDirection = -1

        legalmoves = []

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        if Board[y + moveDirection][x] == None: #verifier si le roi n'est pas découvert
            legalmoves.append([y + moveDirection][x])
        if Board[y + moveDirection][x + moveDirection] == Piece.Color != self.Color: #verifier si le roi n'est pas découvert
            legalmoves[y + moveDirection][x + moveDirection]
        return legalmoves
