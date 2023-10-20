from Class.Pieces.Piece import *


class Rook(Piece):
    """Permet de créer une tour enfante de Piece"""

    def __init__(self, color, x, y):
        self.color = color

        super().__init__("R", x, y)

    def LegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        
        legalmoves = []
        y,x = self.posy,self.posx
        # penser a faire le systeme pour interdir de faire bouger la pièce si on risque d'etre en échec
        for i in range(7):

            if Board[y + i][x] == None or Board[y + i][x] and [y + i][x].Color != self.Color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] == Piece():
                    break
        
        for i in range(7):
            if Board[y][x + i] == None or Board[y][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] == Piece():
                    break
        
        for i in range(-7,0):

            if Board[y + i][x] == None or Board[y + i][x] and Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] == Piece():
                    break
        
        for i in range(-7,0):
            if Board[y][x + i] == None or Board[y][x + i] and Piece.Color != self.Color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] == Piece():
                    break

        return legalmoves