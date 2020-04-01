from fonctions import *
from donnees import *
from random import randrange

nom_joueur=input("bonjour cher joueur, veuillez saisir votre nom à fin de vous identifier.")
score_joueur=joueur(nom_joueur)
while(True):
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
                    if 'a' <= lettre <= 'z':
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
            if i<=nombre_tentative:
                score_joueur+=nombre_tentative-i+1
                print("bravo vous l'avez trouvé dès la tentative numero: ",i,"\nvotre score devient donc: ",score_joueur)
            else:
                print("malheureusement vous avez perdu, votre score reste: ",score_joueur)
        else:
            break
    except:
        break
print("\n au revoir")
    