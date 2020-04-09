class tier():
    def __init__(self,id_tier,titre,id_client,id_fournisseur,adresse):
        self.id_tier=id_tier
        self.titre=titre
        self.id_client=id_client
        self.id_fournisseur=id_fournisseur
        self.adresse=adresse
    def changer_addresse(self,adresse):
        self.adresse=adresse
    def get(self):
        return
    
        
class client():
    def __init__(self,id_client):
        self.id_client=id_client
        
        
class fournisseur():
    def __init__(self,fournisseur):
        self.fournisseur=fournisseur
        
        
class contact():
        def __init__(self,id_contact,id_tier,types,valeur):
            self.id_client=id_client
            self.id_tier=id_tier
            self.types=types
            self.valeur=valeur
        
def main():


if __name__==__main__:
    main()