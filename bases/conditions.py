
# 2 conditions
age = 17

if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# 3 conditions
note = 15

if note >= 16:
    print("Très bien")
elif note >= 10:
    print("Admis")
else:
    print("Échec")

#equivalent de switch/case de php
jour = "lundi"

match jour:
    case "lundi":
        print("Début de semaine")

    case "vendredi":
        print("Bientôt le week-end")

    case _: #correspond au default
        print("Jour inconnu")


#pattern matching : reconnaître la structure d'un objet.
point = (3, 5)

match point:
    case (0, 0):
        print("Origine")
    case (0, y):
        print(f"Sur l'axe Y : {y}")
    case (x, 0):
        print(f"Sur l'axe X : {x}")
    case (x, y):
        print(f"Point ({x}, {y})")