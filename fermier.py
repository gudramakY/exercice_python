from personne import Personne
from taches import Tache

class Fermier(Personne):
    def __init__(self, nom_complet, age, race, niveau_etude, points_forts, points_faibles, tache:Tache):
        super().__init__(nom_complet, age, race)
        self.niveau = niveau_etude
        self.forts = points_forts
        self.faibles = points_faibles
        self.work = tache

    def know_year(self):
        date_debut = int(input("Vous etes arrive dans la ferme dans quelle annee ?"))
        if len(str(date_debut)) > 4 :
            print("annee invalide ! Verifiez si votre annee contient bien 4 chiffres")
            return
        
        years = 2026 - date_debut
        
        if (years > 5):
            print(f"Bravo pour vos {years} ans d'experience dans notre ferme !")
        elif (years >= 0 and years <= 2):
            print(f"Vous etes dans la ferme depuis {years} ans ! Vous etes encore tout nouveau ! Courage !")
        else:
            print(f"Vous etes dans la ferme depuis {years} ans !")

    def points(self):
        print(f"Ton point fort est : {self.forts} et ton point faible est : {self.faibles}.")

    def tache(self):
        print(f"Vous faites '{self.work.type}' comme tache ?")

    
        

    