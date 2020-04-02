from donnees import *
from random import randrange
import os
import pickle
def ScoreJoueur(nom_joueur):
    if os.path.exists('scores'): # Le fichier existe
        with open ('scores','rb') as fichier_scores:
            mon_pickler = pickle.Unpickler(fichier_scores)
            liste_joueurs = mon_pickler.load()
    else:
        liste_joueurs = {}
    if nom_joueur not in liste_joueurs:
        liste_joueurs[nom_joueur]=0
    
    Score_joueur=liste_joueurs[nom_joueur]
#    print("le score de {} est {}".format(nom_joueur,Score_joueur))
    return Score_joueur
def joueur (x):
    nom_joueur=''
    try:
        while len(nom_joueur)<3:
            nom_joueur=input("bonjour cher joueur, veuillez saisir votre nom à fin de vous identifier.")
            score_joueur=ScoreJoueur(nom_joueur)
    except:
        x=0
    if x==1:
        print("le score de {} est {}".format(nom_joueur,score_joueur))
    return nom_joueur,x

def affiche(tab,mot_saisi):
    mot_resultat=''
    for i in mot_saisi:
        if i in tab:
            mot_resultat += i
        else:
            mot_resultat += '*'
    return mot_resultat
    
def tour(nom_joueur,score_joueur,x):
    try:
        reponse=input("Bonjour monsieur {}, votre dernier score est {},voulez vous commencer une partie ?. (y/N)\n".format(nom_joueur,score_joueur))
        if reponse in ['y','Y']:
            i=1
            tab=[]
            x=randrange(len(liste_mots))
            mot_choisi=liste_mots[x]
            while(i<=nombre_tentative):
                while (True):
                    lettre=input("c'est la tentative numéro {}, entrez un caractère miniscule".format(i))
                    if 'a' <= lettre <= 'z' and len(lettre)==1:
                        if lettre in tab:
                            print("Vous avez déjà esseyer ce caractère")
                        else:
                            break
                    else:
                        print ("entrée non valide !")
                
                tab+=lettre
                mot_trouve=affiche(tab,mot_choisi)
                if mot_choisi==mot_trouve:
                    break
                print(mot_trouve)
                i+=1
            x=1
            if i<=nombre_tentative:
                score_joueur+=nombre_tentative-i+1
                print("bravo vous l'avez trouvé dès la tentative numero: ",i,"\nvotre score devient donc: ",score_joueur)
                
            else:
                print("malheureusement vous avez perdu, votre score reste: ",score_joueur)
                
        else:
            x=0
            return score_joueur,x
    except :
        x=0
        return score_joueur,x  
    return score_joueur,x
    
def SauvScore(nom_joueur,score_joueur):
    if os.path.exists('scores'): # Le fichier existe
        with open ('scores','rb') as fichier_scores:
            mon_pickler = pickle.Unpickler(fichier_scores)
            liste_joueurs = mon_pickler.load()
    else:
        liste_joueurs = {}
    liste_joueurs[nom_joueur]=score_joueur
    with open ('scores','wb') as fichier_scores:
        mon_pickler = pickle.Pickler(fichier_scores)
        mon_pickler.dump(liste_joueurs)