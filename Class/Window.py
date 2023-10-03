import pygame

from Class.Game import *
from Pages.Game_Page import *
from Pages.Main_Menu import *


class Window:
    """Class générale étant la fenêtre affiché"""

    def __init__(self, screen) -> None:
        """Constructeur de la fenêtre"""
        
        self.ScreenName = "Main_Menu"
        self.Screen = screen

        self.elements_list = []
        self.button_list = []

        self.game = None

    
    def getElements(self):
        """Fonction permettant la récupération des éléments de chaque page"""
        #FAIRE GAME PAGE

        pygame.display.flip()
        self.Screen.fill((0,0,0))

        if self.ScreenName == "Main_Menu":

            self.elements_list = Main_Menu(self.Screen)

        elif self.ScreenName == "Game_Page" :

            Game_Page(self.game)


    def blit(self):
        """Permet l'affichague des éléments d'une page et le revoie aux fonctions en lien avec chaque boutons, permet également le traitement des événements"""

        running = True
        MOUSEBUTTONDOWN = False

        for event in pygame.event.get(): #récupération des événements de pygame
            
            if event.type == pygame.QUIT: #si la fenêtre a été fermée
                
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN: #si la souris a été cliquée

                MOUSEBUTTONDOWN = True
                button = event.button

        for element in self.elements_list: #traitement de chaque élément

            element.Blit(self.Screen) #affichage


            if element.type == "Button" and MOUSEBUTTONDOWN: #gestion des boutons


                if element.rect.collidepoint(event.pos): #appel des fonctions


                    if element.page == "Main_Menu":
                        
                        Main_Page_Relayeur(element, button)

        #return : running -> permet de stopper le programme (si False)
        return running