class Livre:

    def __init__(self, titre, auteur, emprunte = False):
        self.titre = titre
        self.auteur = auteur
        self.emprunte = emprunte

    def emprunter(self):
        self.emprunte = True
        return self.emprunte

    def retourner(self):
        self.emprunte = False
        return self.emprunte


    def afficher(self):
        print(f" auteur : {self.auteur}, titre = {self.titre}, emprunté : {self.emprunte}")
