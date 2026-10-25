from personne import Personne
from fermier import Fermier
from taches import Tache, Eau_animaux

personne1 = Personne("Gudra mak", 19, "Noir")
personne1.self_introduction()

tache1 = Tache("Faire manger les cheveaux", "dans la ferme")
fermier1 = Fermier("Gudra mak", 19, "Negro", "licencie", "les cheveaux", "les oiseaux", tache1)
fermier1.know_year()
fermier1.points()
fermier1.tache()

tache2 = Eau_animaux("Donner a boire aux animaux", "Au Sud-Est de la ferme")
fermier2 = Fermier("Isma", "Ange", "Black", "licencie", "la fone", "la flore", tache2)
fermier2.tache()
tache2.etat()

