from Class.Pieces.Piece import *
from Class.Pieces.Bishop import*
from Class.Pieces.Rook import*


class King(Piece):
    """Permet de créer un roi enfant de Piece"""

    def __init__(self, color, x, y):
        self.color = color
    
    def __str__(self) -> str:
        return "Ceci est un roi"

        super().__init__("K", x, y)

    def LegalMoves(self, Board):

        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        #penser a vérifier si le roi n'est pas en echec
        y,x = self.posy,self.posx
        legalmoves = []
        move = [(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]

        for i in move:
            movey,movex = i
            if x + i < 0 or x + i > 7 or y + i < 0 or y + i > 7:
                break
            if Board[y + movey][x + movex] == None or Board[y + movey][x + movex] == [y + movey][x + movex].color:
                legalmoves.append((y + movey,x + movex))
        return legalmoves
    
    def ischess(self, Board)-> bool:
        """verifie si le roi est en echec en remplaçant le roi par une tour et un fou et verifie si dans ses mouvements il peux avoir un fou ou une tour ou dame renvoie true si il est en echec et False sinon"""
        x,y = self.posx, self.posy
        fou = Bishop(self.color,x,y)
        tour = Rook(self.color,x,y)
        for i in fou.LegalMoves(Board):
            if i == Bishop(not(self.color)):
                return True
        for i in tour.LegalMoves(self.color):
            if Board(i) == Rook(not(self.color)):
                return True
        return False

        
