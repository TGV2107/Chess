from Class.Pieces.Piece import *

class Queen(Piece):
    """Permet de créer une dame enfante de Piece"""

    def __init__(self, color, x, y):

        super().__init__("Q", color, x, y)

    def LegalMoves(self, Board):
        y,x = self.posy,self.posx
        legalmoves = []

        #copie légalMoves fou
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
        
        #copie legalmoves tour
        for i in range(7):

            if Board[y + i][x] == None or Board[y + i][x] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] == Piece:
                    break
        
        for i in range(7):
            if Board[y][x + i] == None or Board[y][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] == Piece:
                    break
        
        for i in range(-7,0):

            if Board[y + i][x] == None or Board[y + i][x] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] == Piece:
                    break
        
        for i in range(-7,0):
            if Board[y][x + i] == None or Board[y][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] == Piece:
                    break

        return legalmoves

        

