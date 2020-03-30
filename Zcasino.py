import random
while(True):
	try:
		montant=input("veuiller saisir le montant à miser")
		montant=int(montant)
		numero_mise=input("saisissez le numero de la mise")
		numero_mise=int(numero_mise)
		if(not (montant < 1 or numero_mise<0 or numero_mise>49)):
			break
		else:
			print("le numero est erronée,veuiller reessayer")
	except:
		print("le numero est erronée,veuiller reessayer")
		if montant=='q' or numero_mise=='q':
			break
random.randrange(50)
		
