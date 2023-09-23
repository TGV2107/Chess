from Class.Pieces.Piece import *


class King(Piece):
    """Permet de créer un roi enfant de Piece"""

    def __init__(self, color):

        super().__init__("K", color)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        #penser a vérifier si le roi n'est pas en echec
        y,x = self.posy,self.posx
        legalmoves = []
        move = [(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]

        for i in move:
            movey,movex = move
            if Board[y + movey][x + movex] == None or Board[y + movey][x + movex] == Piece.Color:
                legalmoves.append(Board[y + movey][x + movex])
        return legalmoves
