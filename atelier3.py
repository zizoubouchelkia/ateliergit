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