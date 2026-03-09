class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)
