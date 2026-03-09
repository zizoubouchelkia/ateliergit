class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)


class Parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.listeVoitures)

    def entrerVoiture(self, voiture):
        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                print("La voiture existe deja dans le parc.")
                return

        if len(self.listeVoitures) >= self.capacite:
            print("Le parc est plein.")
            return

        self.listeVoitures.append(voiture)
        print("Voiture ajoutee avec succes.")

    def sortirVoiture(self, voiture):
        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                self.listeVoitures.remove(v)
                print("Voiture retiree avec succes.")
                print("Nombre de places libres :", self.calculerNbrPlacesLibres())
                return

        print("Cette voiture n'existe pas dans le parc.")


v1 = Voiture("123AA", "Toyota", "Rouge")
v2 = Voiture("456BB", "Honda", "Noire")
v3 = Voiture("789CC", "Ford", "Blanche")
v4 = Voiture("999DD", "BMW", "Grise")

parc1 = Parc(1, "Toronto", 3)

v1.afficherInformations()

parc1.entrerVoiture(v1)
parc1.entrerVoiture(v2)
parc1.entrerVoiture(v3)

parc1.entrerVoiture(v4)
parc1.entrerVoiture(v1)