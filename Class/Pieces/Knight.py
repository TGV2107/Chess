from Class.Pieces.Piece import *


class Knight(Piece):
    """Permet de créer un cavalier enfant de Piece"""

    def __init__(self, color, x, y):

        super().__init__("N", color, x, y)

    def LegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        y,x = self.posy, self.posx
        legalmoves = []
        move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        for i in move:
            movey,movex = i
            if Board[y + movey][x + movey] == None or Board[y + movey][x + movey] == self.Color != self.Color:
                legalmoves.append(Board[y + movey, x + movex])
        return legalmoves

