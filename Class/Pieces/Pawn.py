from Class.Pieces.Piece import *


class Pawn(Piece):
    """Permet de créer un pion enfant de Piece"""

    def __init__(self, color):

        super().__init__("P", color) #Attention les notations ne contiennent pas le "P" !

    def LegalMoves(self, Board, x, y):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        if Board[y + moveDirection][x] == None: #verifier si le roi n'est pas découvert
            legalmoves.append([y + moveDirection][x])
            
        if Board[y + moveDirection][x + moveDirection] == Piece.Color != self.Color: #verifier si le roi n'est pas découvert
            legalmoves[y + moveDirection][x + moveDirection]
        return legalmoves
