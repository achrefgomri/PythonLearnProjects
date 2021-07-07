class Caisse:

    def __init__(self,id=-1,nom='NULL',valeur='NULL',date_creation='NULL',commentaire='NULL'):
        self.id=id
        self.nom=nom
        self.valeur=valeur
        self.date_creation=date_creation
        self.commentaire=commentaire
	
class Mouvement:
	
    def __init__(self,id=-1,id_caisse=-1,nature='NULL',type='NULL',valeur='NULL',motif='NULL',date_valeur='NULL'):
        self.id=id
        self.id_caisse=id_caisse
        self.nature=nature
        self.type=type
        self.valeur=valeur
        self.motif=motif
        self.date_valeur=date_valeur
		
	


def main():
	
    return

if __name__=='__main__':
	main()
