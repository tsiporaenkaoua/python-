class Livre:

    def __init__(self, titre, auteur, emprunte=False):
        self.titre = titre
        self.auteur = auteur
        self.emprunte = emprunte

    def emprunter(self):
        if self.emprunte:
            return "Le livre est déjà emprunté"
        self.emprunte = True
        return "Le livre est maintenant emprunté"

    def __str__(self):
        return f"{self.titre} par {self.auteur}"


livre1 = Livre("Harry Potter", "J.K. Rowling")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre3 = Livre("1984", "George Orwell")

bibliotheque = [livre1, livre2, livre3]


def afficherLivres(bibliotheque):
    for i, livre in enumerate(bibliotheque, start=1):
        print(i, "-", livre.titre)


def choisirLivre(bibliotheque):
    afficherLivres(bibliotheque)

    choix = int(input("Choisis un livre : "))-1

    return bibliotheque[choix]


print("Bienvenue dans la bibliothèque")

livre = choisirLivre(bibliotheque)

print(livre)

print(livre.emprunter())

print("Fin du programme")