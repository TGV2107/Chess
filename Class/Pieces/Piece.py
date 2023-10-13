class Piece:
    '''Permet de créer une pièce d'échec'''

    def __init__(self, type, x, y):

        self.Type = type

        self.posx = x

        self.posy = y

        self.LegalMoves = []

    def setLegalMoves(self, LegalMoves):

        self.LegalMoves = LegalMoves