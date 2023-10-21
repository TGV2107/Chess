from Class.Pieces.Piece import *


class Bishop(Piece):
    """Permet de créer un fou enfant de Piece"""

    def __init__(self, color, y, x):
        self.color = color

        super().__init__("B", x, y)

    def __str__(self) -> str:
        return "Ceci est un fou"

    def getLegalMoves(self, Board):
        y,x = self.posy,self.posx
        legalmoves = []
        for i in range (1,8):
            if x + i < 0 or x + i > 7 or y + i < 0 or y + i > 7:
                break
            if Board[y + i][x + i] == None or Board[y + i][x + i].color != self.color:
                legalmoves.append((y+i,x+i))
            if Board[y + i][x + i] != None:
                break
    
        for i in range (1,8):
            if x - i < 0 or x - i > 7 or y + i < 0 or y + i > 7:
                break
            if Board[y + i][x - i] == None or Board[y + i][x - i].color != self.color:
                legalmoves.append((y+i,x-i))
            if Board[y + i][x - i] != None:
                break

        for i in range (1,8):
            if x + i < 0 or x + i > 7 or y - i < 0 or y - i > 7:
                break
            if Board[y - i][x + i] == None or Board[y - i][x + i].color != self.color:
                legalmoves.append((y-i,x+i))
            if Board[y - i][x + i] != None:
                break

        for i in range (1,8):
            if x - i < 0 or x - i > 7 or y - i < 0 or y - i > 7:
                break
            if Board[y - i][x - i] == None or Board[y - i][x - i].color != self.color:
                legalmoves.append((y-i,x-i))
            if Board[y - i][x - i] != None:
                break

        return legalmoves

