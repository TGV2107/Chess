from Class.Pieces.Piece import *


class Rook(Piece):
    """Permet de créer une tour enfante de Piece"""

    def __init__(self, color, x, y):
        self.color = color

        super().__init__("R", x, y)

    def __str__(self) -> str:
        return "Ceci est une tour"

    def LegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        
        legalmoves = []
        y,x = self.posy,self.posx
        # penser a faire le systeme pour interdir de faire bouger la pièce si on risque d'etre en échec
        
        for i in range(1,8):
            if y + i < 0 or y + i > 7:
                break
            if Board[y + i][x] == None or Board[y + i][x].color != self.color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] != None:
                    break
        
        for i in range(1,8):
            if x + i < 0 or x + i > 7:
                break
            if Board[y][x + i] == None or Board[y][x + i].color != self.color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] != None:
                    break
        
        for i in range(1,8):
            if Board[y - i][x] == None or Board[y - i][x].color != self.color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] != None:
                    break
        
        for i in range(1,8):
            if Board[y][x - i] == None or Board[y][x - i].color != self.color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] != None:
                    break

        return legalmoves