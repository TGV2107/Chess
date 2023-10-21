from Class.Pieces.Piece import *


class Rook(Piece):
    """Permet de créer une tour enfante de Piece"""

    def __init__(self, color, y, x):
        self.color = color

        super().__init__("R", y, x)

    def __str__(self) -> str:
        return "Ceci est une tour"

    def getLegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        
        legalmoves = []
        y,x = self.posy,self.posx
        # penser a faire le systeme pour interdir de faire bouger la pièce si on risque d'etre en échec
        
        for i in range(1,8):
            if y + i < 0 or y + i > 7:
                break
            if Board[y + i][x] == None or Board[y + i][x].color != self.color:
                legalmoves.append((y+i,x))
            if Board[y + i][x] != None: #si il s'agit d'une pièce on arrete d'avancer dans cette direction
                    break
        
        for i in range(1,8):
            if x + i < 0 or x + i > 7:
                break
            if Board[y][x + i] == None or Board[y][x + i].color != self.color:
                legalmoves.append((y,x+i))
                if Board[y][x + i] != None:
                    break
        
        for i in range(1,8):
            if y - i < 0 or y - i > 7:
                break
            if Board[y - i][x] == None or Board[y - i][x].color != self.color:
                legalmoves.append((y-i,x))
                if Board[y - i][x] != None:
                    break
        
        for i in range(1,8):
            if x - i < 0 or x - i > 7:
                break
            if Board[y][x - i] == None or Board[y][x - i].color != self.color:
                legalmoves.append((y,x-i))
                if Board[y][x - i] != None:
                    break

        return legalmoves