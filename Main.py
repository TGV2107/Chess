#importation des utilitaires

import time

import pygame

from Class.Game import *
from Class.Pieces.Bishop import *
from Class.Pieces.King import *
from Class.Pieces.Knight import *
from Class.Pieces.Pawn import *
from Class.Pieces.Piece import *
from Class.Pieces.Queen import *
from Class.Pieces.Rook import *
from Class.Window import *
from Pages.Game_Page import *
from Pages.Main_Menu import *

#importation des classes


#importation des pages


#page pygame
pygame.init()
pygame.font.init()

window = Window(pygame.display.set_mode((1080,720)))
pygame.display.set_caption("Chess")
running = True
window.ScreenName = "Main_Menu"


#boucle d'actualisation
while running:
    
    window.getElements()

    running = window.blit()

pygame.quit()