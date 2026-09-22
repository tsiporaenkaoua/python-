from miniProjets.miniProjet3 import Livre

livre1 = Livre("Harry Potter", "J. K. Royling")
livre2 = Livre("Le petit prince", "Antoine de St Exupery")
livre3 = Livre("Les 3 mousquetaires", "Alexandre Dumas")
livre4 = Livre("Les 10 petits negres", "Agatha Christie")

bibliotheque = [livre1, livre2, livre3, livre4]
def afficherLivres(bibliotheque):
    for livre in bibliotheque:
        return livre
    
print(afficherLivres(bibliotheque))


#dans les import Pas .py à la fin
#REGLES IMPORTS :
# importer un module entier : import math
# importer des fonctions précises d'un module : from math import sqrt, pi
# importer avec un alias : import numpy as np
# importer depuis un fichier local : import mon_module ou from mon_module import ma_fonction
# Import de sous dossiers : from dossier_meme_niveau.sous_dossier import mon_module



