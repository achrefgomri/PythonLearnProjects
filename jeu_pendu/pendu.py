from fonctions import *
from donnees import *
x=1
nom_joueur,x=joueur(x)
score_joueur=ScoreJoueur(nom_joueur)
#SauvListeMots()
while(x==1): 
    score_joueur,x=tour(nom_joueur,score_joueur,x)

SauvScore(nom_joueur,score_joueur)
print("\n au revoir")
    