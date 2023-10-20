from Class.Pieces.Piece import *


class Pawn(Piece):
    """Permet de créer un pion enfant de Piece"""

    def __init__(self, color,x , y):
        self.color = color

        super().__init__("P", x, y) #Attention les notations ne contiennent pas le "P" !

    def __str__(self) -> str:
        return "Ceci est un piont"

    def LegalMoves(self, Board):
        y,x = self.posy,self.posx
        if Piece.Color == "Black":
            moveDirection = -1
        elif Piece.Color == "White":
            moveDirection = 1
        
        legalmoves = []
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        if Board[y + moveDirection][x] == None: #verifier si le roi n'est pas découvert
            legalmoves.append([y + moveDirection][x])

        if Board[y + moveDirection][x + moveDirection] == Piece.Color != self.Color: #verifier si le roi n'est pas découvert
            legalmoves[y + moveDirection][x + moveDirection]
        return legalmoves
