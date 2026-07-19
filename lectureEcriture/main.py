from pathlib import Path

#Path(__file__) cible le chemin du fichier present
chemin = Path(__file__).parent / "notes.txt"

with open(chemin, "w") as fichier:
    fichier.write("bonjour les amis \n")


with open(chemin, "r") as fichier:
    contenu = fichier.read()

print(contenu)




# | Code           | Si le fichier existe | Si le fichier n'existe pas |
# | -------------- | -------------------- | -------------------------- |
# | `"r"` (read)   | ouvre pour lire      | erreur                     |
# | `"w"` (write)  | ouvre et efface      | crée le fichier            |
# | `"a"` (append) | ajoute à la fin      | crée le fichier            |
# | `"x"` (create) | erreur               | crée le fichier            |


# le with = "Ouvre le fichier, utilise-le, puis ferme-le automatiquement quand tu as terminé."

nom = input("Entrez votre prenom : ")

with open(chemin, "a") as fichier:
    fichier.write(nom)

with open(chemin, "r") as fichier:
    print(fichier.read())
