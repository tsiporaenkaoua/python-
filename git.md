##########   GIT

Gestion de git lorsqu'on travaille seul sur 2 ordis :
    CREER MON REPO:
        git init
        git add .
        git commit -m"detail du commit"
        git remote add origin URL_DU_REPO
        git push -u origin master

    2eme ordi  - premiere fois
        git clone URL_DU_REPO
    
    Travail sur ordi 1:
        git add .
        git commit -m "Ajout de fonctionnalité X"
        git push

    Tu passes sur l'ordinateur 2 , mise a jour puis push du travail:
        git pull

        #pusher le code sur le depot distant
        git add .
        git commit -m "Ajout de fonctionnalité X"
        git push


######### LIGNE DE COMMANDE

cd .. revenir dans le dossier parent
cd "dossier" alles dans un dossier enfant
dir "dossier" voir ce que le dossier contient