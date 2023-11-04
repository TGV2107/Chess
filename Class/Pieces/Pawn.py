from Class.Pieces.Piece import *


class Pawn(Piece):
    """Permet de créer un pion enfant de Piece"""

    def __init__(self, color,x , y):
        self.color = color

        super().__init__("P", x, y) #Attention les notations ne contiennent pas le "P" !

    def __str__(self) -> str:
        return "Ceci est un pion"

    def getLegalMoves(self, Board):
        y,x = self.posy,self.posx
        if self.color == "White":
            moveDirection = -1
        elif self.color == "Black":
            moveDirection = 1
        print(moveDirection)

        if y == 1 and self.color == "Black" or y == 6 and self.color == "White":
            firstmove = 2*moveDirection
        
        
        legalmoves = []
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        if 0 <= y + moveDirection < 8 and 0 <= x + moveDirection < 8:  
            if Board[y + moveDirection][x] == None: #verifier si le roi n'est pas découvert
                legalmoves.append([y + moveDirection,x])
            if Board[y + firstmove][x] == None:
                legalmoves.append([y + firstmove,x])


            if Board[y + moveDirection][x + moveDirection] != None and Board[y + moveDirection][x + moveDirection].color != self.color: #verifier si le roi n'est pas découvert
                legalmoves[y + moveDirection, x + moveDirection]
            if Board[y + moveDirection][x + moveDirection] != None and Board[y + moveDirection][x - moveDirection].color != self.color: #verifier si le roi n'est pas découvert
                legalmoves[y + moveDirection, x - moveDirection]
            return legalmoves
