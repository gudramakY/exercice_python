class Personne :
    def __init__(self, nom_complet:str, age:int, race:str):
        self.nom = nom_complet
        self.age = age
        self.race = race

    def self_introduction(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans et je suis de la race {self.race}. Merci !")

    