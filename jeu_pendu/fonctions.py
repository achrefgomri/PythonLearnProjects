from donnees import *

def joueur(nom_joueur):
    if nom_joueur not in liste_joueurs:
        liste_joueurs[nom_joueur]=0
    
    Score_joueur=liste_joueurs[nom_joueur]
    print("le score de {} est {}".format(nom_joueur,Score_joueur))
    return Score_joueur

def affiche(tab,mot_saisi):
    mot_resultat=''
    for i in mot_saisi:
        if i in tab:
            mot_resultat += i
        else:
            mot_resultat += '*'
    return mot_resultat