import random

from Class.Elements.Button import *


def Main_Menu(screen):

    #list des éléments
    elements_list = []

    #bouton "Partie à deux joueurs"
    button_TwoPlayer = Button("yo",(0,0),(100,100),pygame.image.load("Assets/IMG/bouton_collection.png"), "Main_Menu")
    elements_list.append(button_TwoPlayer)

    #bouton test 2
    button_test = Button("yo",(200,200),(50,50),pygame.image.load("Assets/IMG/bouton_collection.png"), "Main_Menu")
    elements_list.append(button_test)

    return elements_list

def Main_Page_Relayeur(element, button):

    if element.name == "yo" and button == 1:

        print("izapedj")