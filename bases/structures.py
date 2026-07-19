# STRUCTURES

#liste : 
    # ordonnés, les elements gardent leur position
    # modifiable, on peut ajouter, supprimer, modifier
    # accepte les doublons
    # éléments accessibles par leur indice
fruits = ["pomme", "banane", "orange"]
print(fruits)
print(fruits[0])
fruits.append("kiwi")
print(fruits)
print(type(fruits))

# tuple:
    #ordonnées
    #non modifiable
    #accepte les doublons
    # éléments accessibles par leur indice
    #utilisé pour représenter des données qui ne douvent pas changer (coordonnées GPS, couleurs RGB ...)
coordonnees = (48.85, 2.35)
print(coordonnees[0])
print(type(coordonnees))



#Dictionnaire:
    #  stockage sous forme clé : valeur
    # modifiable
    #les clés sont uniques
    # accés aux valeurs grace aux clés et non à l'indice
    #trés utilisé pour représenter un objet
utilisateur = {
    "nom": "Léa",
    "age": 25,
    "ville": "Paris"
}
print(utilisateur)
print(utilisateur["nom"])
print(type(utilisateur))




#set :
#  ordre non garanti 
# pas de doublons
# modifiable
#pratique pour supprimer automatiquement les doublons
#on ne peut pas accéder à un élément avec un indice
couleurs = {"rouge", "bleu", "vert", "jaune"}
print(couleurs)
couleurs.add("jaune")
print(couleurs)
print(type(couleurs))