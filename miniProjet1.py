# Crée un programme qui affiche un menu :
# 1 - Dire bonjour
# 2 - Addition
# 3 - Afficher une liste
# 4 - Quitter

#Le programme doit :
# demander le choix de l'utilisateur ;
# appeler la fonction correspondante ;
# afficher le résultat.

print("Choisissez une option : 1 - Dire bonjour 2 - Addition 3 - Afficher une liste  4 - Quitter ")
choix = input("Numéro de votre choix : ")

def direBonjour():
    print("Bonjour")

match choix:
    case "1":
        direBonjour()
    case "2":
        nb1 = int(input("Entrez un premier chiffre : "))
        nb2 = int(input("Entrez un second chiffre : "))
        print(nb1 + nb2)
    case "3":
        print(["peche","pomme","poire"])
    case  "4":
        print("Vous quittez le jeu")
    case _:
        print("Choix invalide.")
    