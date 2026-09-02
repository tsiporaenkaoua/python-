class Livre:

    def __init__(self, titre, auteur, emprunte = False):
        self.titre = titre
        self.auteur = auteur
        self.emprunte = emprunte

    def emprunter(self): 
        if self.emprunte:
            return "le livre est déjà emprunté"
        else:
            self.emprunte = True
            return "Action prise en compte. Le livre est emprunté"

    def retourner(self):
        if not self.emprunte:
             return "le livre est déjà retourné"
        else:
            self.emprunte = False
            return "Action prise en compte. Le livre est retourné"


    def __str__(self):
        return(f" auteur : {self.auteur}, titre = {self.titre}, emprunté : {self.emprunte}")


livre1 = Livre("Harry Potter", "J. K. Royling")
livre2 = Livre("Le petit prince", "Antoine de St Exupery")
livre3 = Livre("Les 3 mousquetaires", "Alexandre Dumas")
livre4 = Livre("Les 10 petits negres", "Agatha Christie")

bibliotheque = [livre1, livre2, livre3, livre4]
#print(bibliotheque)

def afficherLivres(bibliotheque):
    for i, livre in enumerate(bibliotheque, start=1):
        print( i, "-", livre)

def choisirLivre(bibliotheque):
    afficherLivres(bibliotheque)
    nb = input("Selectionne un livre par son numéro :")
    return bibliotheque[int(nb) - 1]


number = ""
while number != "4":
    print("1 - Voir les livres")
    print("2 - Emprunter ")
    print("3 - Retourner ")
    print("4 - Quitter ")
    number = input("Selectionne un chiffre du menu : ") #verif chiffre, verif entre 1 et 4

    if number not in ["1", "2", "3", "4"]:
        print("Choix invalide")

    match number:
        case "1":
            afficherLivres(bibliotheque)
        case "2":
            livre = choisirLivre(bibliotheque)
            print(livre.emprunter())
        case "3":
            livre = choisirLivre(bibliotheque)
            print(livre.retourner())
        case "4":
            print("quitter")
        

# le not remplace le ! dans les conditions

####Ajouter une verif au niv de la fonction choisirLivre()
