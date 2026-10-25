class Tache:
    def __init__(self, type, lieu):
        self.type = type
        self.lieu = lieu
    def etat(self):
        print("Pas fait !")

class Eau_animaux(Tache):
    def etat(self):
        etat_work = str(input("As-tu fait cette tache ?"))
        verifier_answer = etat_work.lower()
        if verifier_answer == "oui":
            print("Bravo ! Tu as fait cette tache !")
        elif verifier_answer == "non":
            print("Tu n'as pas fait cette tache !")
        else:
            print("Repondre par oui ou non !")

        litre = int(input("Combien de litres d'eau as-tu donne aux animaux ?"))
        if (litre >= 0 and litre <= 5):
            print(f"{litre} litres d'eau c'est peu ! Tu dois donner plus d'eau aux animaux !")
        else :
            print(f"Tu as donne {litre} litres d'eau aux animaux ! C'est parfait")
