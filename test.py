from Class.Pieces.Piece import *
from Class.Pieces.Bishop import *
from Class.Game import *

game = Game()

test = game.board[0][0]
print(test)

print(test.getLegalMoves(game.board))