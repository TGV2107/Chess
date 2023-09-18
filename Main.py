#importation des utilitaires

import pygame
import time

#importation des classes

from Class.Window import *
from Class.Game import *
from Class.Pieces.Piece import *
from Class.Pieces.Pawn import *
from Class.Pieces.Rook import *
from Class.Pieces.Knight import *
from Class.Pieces.Bishop import *
from Class.Pieces.Queen import *
from Class.Pieces.King import *

#importation des pages

from Pages.Main_Menu import *
from Pages.Game_Page import *

#page pygame
pygame.init()
pygame.font.init()

window = Window(pygame.display.set_mode((1080,720)))
pygame.display.set_caption("Chess")
running = True
window.ScreenName = "Main_Menu"


#boucle d'actualisation
while running:
    
    pygame.display.flip()
    window.Screen.fill((0,0,0))
    
    #affichage de chaque page
    
    if window.ScreenName == "Main_Menu": #affichage de main
        
        Main_Menu_button_TwoPlayer = Main_Menu(window.Screen)

    elif window.ScreenName == "Game_Page" : #affichage du jeu

        Game_Page(game)
    
    #détection des événements                          
    for event in pygame.event.get():
        
        #événement de fermeture de la page pygame
        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()

        #événement clic sur souris, event.button représente le bouton de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if Main_Menu_button_TwoPlayer.collidepoint(event.pos):
                
                game = Game()
                window.ScreenName = "Game_Page"

    #fps
    time.sleep(0.05)