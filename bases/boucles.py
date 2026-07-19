#for pour repeter un certain nombre de fois
for i in range(5):
    print(i)

#for pour parcourir un tableau
fruits = ["pomme", "banane", "kiwi"]
for fruit in fruits:
    print(fruit)

#while pour répéter tant que la condition est vraie
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

#continue sert à arrêter l'itération actuelle d'une boucle et passer directement à l'itération suivante.
while True:
    nombre = int(input("Donne un nombre positif : "))

    if nombre < 0:
        print("Nombre invalide")
        continue

    print("Ton nombre est :", nombre)