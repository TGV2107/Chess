from Class.Pieces.Piece import *
from Class.Pieces.Knight import *
from Class.Game import *

game = Game()

test = game.board[0][1]
print(test)

print(test.getLegalMoves(game.board))
