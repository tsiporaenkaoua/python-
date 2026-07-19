# Un compte possède :
# un propriétaire
# un solde

# Il peut :
# déposer
# retirer

class Compte :
    #constructeur
    def __init__(self, proprietaire, solde):
        self.proprietaire =proprietaire
        self.solde =solde

    def retirer(self, montant):
        if self.solde - montant < 0:
            return False
        else:
            self.solde -= montant
            return True

    
    def deposer(self, montant):
        self.solde += montant
        return self.solde
    
    def __str__(self):
        return f"proprietaire = {self.proprietaire} , solde = {self.solde}"
  
    

compte1= Compte("Lea", 500)
print(compte1.__dict__)
#grace a str
print(compte1)
print(dir(compte1))
print(compte1.retirer(600))
print(compte1.deposer(300))


#pas besoin de déclarer les attributs de la classe avant le constructeur
#self dans les parametres du constructeur et des méthodes : self → l'objet qui vient d'être créé, Python ajoute automatiquement l'objet concerné comme premier argument quand il appelle une méthode.
# visualiser les attributs d'une instance en python : instance.__dict__ OU fonction str (a privilegier)
# | Besoin                            | Outil            |
# | --------------------------------- | ---------------- |
# | Voir rapidement le contenu        | `objet.__dict__` |
# | Afficher proprement un objet      | `__str__()`      |
# | Voir tout ce que possède un objet | `dir(objet)`     |
# | Voir le type                      | `type(objet)`    |



#Listes d'objets
c1 = Compte("Georges", 400)
c2 = Compte("Amandine", 700)
c3 = Compte("Loris", 200)
c4 = Compte("Emma", 1400)

comptes = [c1, c2, c3, c4]

for c in comptes :
    print(c)