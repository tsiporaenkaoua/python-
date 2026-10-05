from pathlib import Path
import json

chemin = Path("contacts.json")

# Charger les contacts au démarrage
with open(chemin, "r", encoding="utf-8") as fichier:
    contacts = json.load(fichier)

while True:#boucle infinie tant que l'utilisateur ne choisit pas de quitter
    print("1 - Afficher les contacts ")
    print("2 - Ajouter un contact")
    print("3 - Sauvegarder")
    print("4 - Quitter")

    choix = input("Choisis un chiffre du menu : ")

    while choix not in ["1", "2", "3", "4"]:
        print("Choix invalide")
        choix = input("Choisis un chiffre du menu : ")

    match choix:
        case "1":
            print(contacts)

        case "2":
            nom = input("Entrez le nom : ")
            tel = input("Entrez le num de telephone : ")

            nouveau_contact = {
                "nom": nom,
                "telephone": tel
            }

            contacts.append(nouveau_contact)
            print("Contact ajouté !")

        case "3":
            with open(chemin, "w", encoding="utf-8") as fichier:
                json.dump(contacts, fichier, indent=4)
            print("Sauvegarde effectuée !")

        case "4":
            print("Au revoir !")
            break
