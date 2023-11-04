from Class.Pieces.Piece import *


class Knight(Piece):
    """Permet de créer un cavalier enfant de Piece"""

    def __init__(self, color, x, y):
        self.color = color

        super().__init__("N", x, y)
    
    def __str__(self) -> str:
        return "C'est un cavalier"

    def getLegalMoves(self, Board):
        #Ecrire la fonction de calcule des coups légaux grâce au plateau (Board)
        y, x = self.posy, self.posx
        print(x)
        print(y)
        legalmoves = []
        move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        for i in move:
            print(i)
            movey, movex = i
            
            if 0 <= x + movex < 8 and 0 <= y + movey < 8: 
                if Board[y + movey][x + movex] == None or self.color != Board[y + movey][x + movex].color:
                    legalmoves.append((y + movey, x + movex))
                    print((y + movey, x + movex))
            else:
                print(None)
        return legalmoves

