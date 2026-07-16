try:
    x = int(input("Nombre : "))
    print(10 / x)

except ValueError:
    print("Tu dois entrer un nombre")

except ZeroDivisionError:
    print("Division par zéro impossible")
    
finally:
    print("Fin du programme")


# #| Exception           | Quand se produit-elle ?                          |
# | ------------------- | ------------------------------------------------- |
# | `ValueError`        | Mauvaise valeur (ex. `"abc"` au lieu d'un entier) |
# | `TypeError`         | Types incompatibles (ex. `"5" + 3`)               |
# | `ZeroDivisionError` | Division par zéro                                 |
# | `IndexError`        | Indice de liste inexistant                        |
# | `KeyError`          | Clé absente dans un dictionnaire                  |
# | `NameError`         | Variable non définie                              |
# | `FileNotFoundError` | Fichier introuvable                               |


# demande un nombre
# affiche son carré
# gère les erreurs

try:
    nb = int(input("Entrez un nombre : ")) 
    print(nb*nb)  
except ValueError:
    print("Il faut entrer un nombre")

