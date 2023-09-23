from Class.Pieces.Piece import *


class Rook(Piece):
    """Permet de créer une tour enfante de Piece"""

    def __init__(self, color):

        super().__init__("R", color)

    def LegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        
        legalmoves = []
        y,x = self.posy,self.posx
        # penser a faire le systeme pour interdir de faire bouger la pièce si on risque d'etre en échec
        for i in range(-7,7):

            if Board[y + i][x] == None or Board[y + i][x] == Piece.Color != self.Color:
                legalmoves.append(Board[y + i][x])
                if Board[y + i][x] == Piece.Color != self.Color:
                    break
        
        for i in range(-7,7):
            if Board[y][x + i] == None or Board[y][x + i] == Piece.Color != self.Color:
                legalmoves.append(Board[y][x + i])
                if Board[y][x + y] == Piece.Color != self.Color:
                    break

        return legalmoves