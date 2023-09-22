class Piece:
    '''Permet de créer une pièce d'échec'''

    def __init__(self, type, color, x, y):

        self.Type = type

        self.Color = color

        self.posx = x

        self.posy = y

        self.LegalMoves = []

    def setLegalMoves(self, LegalMoves):

        self.LegalMoves = LegalMoves