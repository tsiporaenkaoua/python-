# Créer un programme avec menu :
# 1 - Addition
# 2 - Soustraction
# 3 - Multiplication
# 4 - Division
# 5 - Quitter

# Contraintes :
# utiliser des fonctions - ok
# utiliser input() - ok
# gérer les erreurs (division par 0)
# boucle while pour rester dans le menu - ok

def additionner(nb1, nb2):
    return nb1+nb2

def soustraire(nb1, nb2):
    return nb1-nb2

def multiplier(nb1, nb2):
    return nb1*nb2

def diviser(nb1, nb2):
    if (nb2 ==0):
            return "On ne peut pas diviser par 0"
    return nb1 / nb2

tab = ["1-Addition", "2-Soustraction", "3-Multiplication", "4-Division", "5-Quitter"]
number=0

while(number!=5):
    
    for element in tab:
        print(element)

    try:
        number = int(input("Choisis une operation du menu et saisis son chiffre :"))
    except ValueError:
        print("Vous devez entrer un chiffre")
        continue

    if(number==5):
        break

    if number < 1 or number > 5:
        print("Il faut choisir un chiffre entre 1 et 5")
        continue

    print(f"Vous avez choisi :{tab[number-1]} ")

    try:
        nb1 = float(input("Entrez un premier nombre : "))
        nb2 = float(input("Entrer un second nombre : "))
    except ValueError:
        print("Vous devez entrer un chiffre")
        continue


    match number:
        case 1: 
            print(additionner(nb1, nb2))
        case 2: 
            print(soustraire(nb1, nb2))
        case 3: 
            print(multiplier(nb1, nb2))
        case 4: 
            print(diviser(nb1, nb2))
       

