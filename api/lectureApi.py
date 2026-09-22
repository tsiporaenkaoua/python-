import json

# Lecture
with open("utilisateur.json", "r", encoding="utf-8") as fichier:
    utilisateur = json.load(fichier)

print(utilisateur)
print(utilisateur["nom"])

# Ecriture

#Modification
utilisateur["prenom"] = "Georges" 
utilisateur["ville"] = "Paris"

#avec w on va supprimer l'ancien json et on en crée un nouveau qu'on va remplir avec notre objet utilisateur
with open("utilisateur.json", "w", encoding="utf-8") as fichier: 
    json.dump(utilisateur, fichier, indent=4)
