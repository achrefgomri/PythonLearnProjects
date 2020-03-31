import random
from os import system, name
solde=float(500)
montant=''
numero_mise=''
i=1
x=0
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def titre():
    clear()
    b="c'est le tour numéro: ",i,",votre solde est de: ",solde
    b=str("\t\t\t\t\t "+b[0]+str(b[1])+b[2]+str(b[3])+"\n"+"\n")
    print(b.center(10))
titre()
print("Bonjour joueur et bienvenue au Zcasino! ton solde initial est de 500$")
while(True):
    while(True):
        try:
            montant=input("veuiller saisir le montant à miser, q pour quiter \n")
            montant=float(montant)
            titre()
            numero_mise=input("saisissez le numero de la mise, q pour quiter \n")
            numero_mise=int(numero_mise)
            titre()
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
        print ("dommage que vous avez rien gagné, le numéro gagnant est le {}, solde restant est de {}$".format(numGagnant,solde))
        x=1
    print("\n")
    if solde==0:
        print("Votre solde est de {}$".format(solde))
        a=input("jeux terminer, n importe pour sortir")
        break
    if x==1:    
        print("en revenche vous pouvez toujours reesseyer \n")
        x=0
    print("Votre solde est de {}$".format(solde))
    a=input("n importe pour continuer, q pour sortir")
    if a=='q':
        break
    i+=1
    titre()

clear()
print("au revoir et à trés bientôt")        