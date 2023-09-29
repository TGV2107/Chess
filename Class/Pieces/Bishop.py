from Class.Pieces.Piece import *


class Bishop(Piece):
    """Permet de créer un fou enfant de Piece"""

    def __init__(self, color):

        super().__init__("B", color)

    def LegalMoves(self, Board):
        y,x = self.posy,self.posx
        legalmoves = []
        for i in range (7):
            if Board[y + i][x + i] == None or Board[y + i][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x + i])
            if Board[y + i][x + i] == Piece:
                break
    
        for i in range (7):
            if Board[y + i][x - i] == None or Board[y + i][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x + i])
            if Board[y + i][x - i] == Piece:
                break

        for i in range (7):
            if Board[y - i][x + i] == None or Board[y + i][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x + i])
            if Board[y - i][x + i] == Piece:
                break

        for i in range (7):
            if Board[y + i][x - i] == None or Board[y + i][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x + i])
            if Board[y + i][x - i] == Piece:
                break

        return legalmoves
    

