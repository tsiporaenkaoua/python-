# Permet d'isoler les dépendances parce que d'un projet à l'autre les dépendances utilisent des versions differentes
# 1. Création du dossier projet
# 2. Création de l'environnement virtuel à la racine du projet
# Commandes :
# python -m venv .venv
# .venv\Scripts\activate
# 3.Installation des dépendances
#(.venv) dans le terminal sil n'y a pas ca on peut le reactiver avec .venv\Scripts\activate
#4. ajouter un fichier requirements.txt à la racine du projet et y mettre les dépendances
#pip freeze > requirements.txt

from pathlib import Path

p = Path("mon_dossier")
print(p.exists())



