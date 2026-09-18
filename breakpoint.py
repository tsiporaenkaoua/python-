notes = [12, 15, 8, 17, 10]

total = 0

for note in notes:
    total = total + note

moyenne = total / len(notes)

if moyenne >= 10:
    resultat = "Admis"
else:
    resultat = "Non admis"

print("Total :", total)
print("Moyenne :", moyenne)
print("Résultat :", resultat)


# -Breakpoint (bouton rouge en tete de ligne )
# -debugger (F5 ou bouton run > debug)
# - Observer la section variable
    
# - F5 : Continue = normalement jusqu'au prochain breakpoint.
# -F10: Step Over = Il exécute la ligne actuelle, puis passe à la suivante.
# - F11 : Step Into = Il entre dans la fonction appelée à la ligne actuelle et s'arrête à la première ligne de cette fonction. Cela vous permet de déboguer le code à l'intérieur de la fonction. 
# - F9: Step Out = Il sort de la fonction appelée à la ligne actuelle et s'arrête au niveau de la fonction appelante.