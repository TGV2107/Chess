from Class.Pieces.Piece import *
from Class.Pieces.Bishop import*
from Class.Pieces.Rook import*


class King(Piece):
    """Permet de créer un roi enfant de Piece"""

    def __init__(self, color, x, y):
        self.color = color

        super().__init__("K", x, y)

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
    
    def ischess(self, Board)-> bool:
        """verifie si le roi est en echec en remplaçant le roi par une tour et un fou et verifie si dans ses mouvements il peux avoir un fou ou une tour ou dame renvoie true si il est en echec et False sinon"""
        x,y = self.posx, self.posy
        fou = Bishop(self.Color,x,y)
        tour = Rook(self.Color,x,y)
        for i in fou.LegalMoves(Board):
            if i == Bishop(not(self.Color)):
                return True
        for i in tour.LegalMoves(self.Color):
            if Board(i) == Rook(not(self.Color)):
                return True
        return False

        
