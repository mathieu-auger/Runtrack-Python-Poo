class Personne:
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    
    def se_presenter(self):
        __name__=self.nom
        __prenom__= self.prenom
        print(__name__)
        print(__prenom__)

nom=Personne('je suis john doe','je suis jean dupond')    
nom.se_presenter()
