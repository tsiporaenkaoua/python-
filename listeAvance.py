
nombres = [1, 2, 3, 4, 5]
print(sum(nombres))
print(max(nombres))
print(min(nombres))


#parcourir une liste
chiffres = [1, 2, 3, 4, 5]
carres = []

for n in chiffres:
    carres.append(n * n)
print(carres)

# version moderne du for
carres = [n * n for n in chiffres]
print(carres)

# exo : notes = [12, 15, 8, 19, 10] Affiche uniquement les notes ≥ 10
notes = [12, 15, 8, 19, 10]
bonnesNotes = []

for n in notes:
    if n >= 10:
        bonnesNotes.append(n)
print (bonnesNotes)