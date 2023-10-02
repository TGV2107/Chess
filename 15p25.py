def creer_tableau(taille: int) -> list:
    return [None]*taille

def set(tableau: list, value, index: int) -> list:
    if index <= taille(tableau) - 1:
        tableau[index] = value
        return tableau
    
    print("Erreur: l'indice dépasse la taille du tableau")
    return None

def get(tableau: list, index: int):

    if index <= taille(tableau) - 1:
        return tableau[index]
    
    print("Erreur: l'indice dépasse la taille du tableau")
    return None

def elements_tableau(tableau: list) -> list:
    return tableau

def tableau_vide(tableau: list) -> bool:
    for elements in tableau:

        if elements != None:
            return False
        
    return True

def taille(tableau: list) -> int:
    return len(tableau)