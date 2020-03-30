import random
from os import system, name 
#print("Bonjour joueur et bienvenue au Zcasino! ton solde initial est de 500$")
#solde=int(500)
#montant=''
#numero_mise=''
i=0
while(True):
    i+=1
    print("c'est le tour numéro: {}".format(i))
    while(True):
        try:
            montant=input("veuiller saisir le montant à miser, q pour quiter")
            montant=int(montant)
            numero_mise=input("saisissez le numero de la mise, q pour quiter")
            numero_mise=int(numero_mise)
            if(not (montant < 1 or montant > solde or numero_mise<0 or numero_mise>49)):
                solde=solde-montant
                break
            else:
                print("le numero est erronée,veuiller reessayer")
        except:
            print("le numero est erronée,veuiller reessayer")
            if montant=='q' or numero_mise=='q':
                break
    if montant=='q' or numero_mise=='q':
        break
    numGagnant=random.randrange(50)
    if numGagnant==numero_mise :
        solde=solde+(montant*3)
        print ("bravo joueur, le numéro gagnant est bien le {}, vous avez gagné {}$, votre nouveau solde est de {}$".format(numGagnant,montant*3,solde)) 
    elif numGagnant%2==numero_mise%2:
        solde=solde+(montant*1.5)
        print ("le numéro gagnant est le {}, vous avez gagné {}$, votre nouveau solde est de {}$".format(numGagnant,montant*1.5,solde))
    else:
        print ("dommage que vous avez rien gagné, le numéro gagnant est le {}, solde restant est de {} en revenche vous pouvez toujours reesseyer".format(numGagnant,solde))
    print("Votre solde est de {}$, q pour quiter".format(solde))
print("au revoir et à trés bientôt")        
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def initialiser():
    print("Bonjour joueur et bienvenue au Zcasino! ton solde initial est de 500$")
    solde=int(500)
    montant=''
    numero_mise=''
def transformer():
    