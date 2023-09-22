from Class.Game import *
from Class.Pieces.Bishop import *
from Class.Pieces.King import *
from Class.Pieces.Knight import *
from Class.Pieces.Pawn import *
from Class.Pieces.Piece import *
from Class.Pieces.Queen import *
from Class.Pieces.Rook import *


def Game_Page(game : Game()):
    case_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    while game.gameStatus == "Playing":

        #Mettre dans une méthode de Game après
        if game.turn == "White":
            moveName = str(input("Move (piece pos + space + new pos): "))

            #Remplace le première caractère du coup par sa valeur
            moveName[0] == str(case_letters.index(moveName[0] + 1))

            #Verifie si la case est dans la matrice
            if moveName[0] in case_letters and int(moveName[1]) in range(1, 8):
                if game.board[int(moveName[0]), int(moveName[1])] != None:
                    break