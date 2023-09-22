from Class.Game import *
from Class.Pieces.Piece import *
from Class.Pieces.Pawn import *
from Class.Pieces.Rook import *
from Class.Pieces.Knight import *
from Class.Pieces.Bishop import *
from Class.Pieces.Queen import *
from Class.Pieces.King import *

def Game_Page(game : Game()):
    case_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    while game.gameStatus == "Playing":

        #Mettre dans une méthode de Game après
        if game.turn == "White":
            moveName = str(input("Move (piece pos + space + new pos): "))

            #Remplace le première caractère du coup par sa valeur
            moveName[0] == case_letters.find(moveName[0])

            if moveName[0] in case_letters and moveName[1]:
                
