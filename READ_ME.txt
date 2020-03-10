
*** Que contient ce répertoire de travail ? ***

- Un dossier "données", qui contient les données d'origine et
  le script pour assembler les sets de 2015 et 2016

Sous la racine on trouve :

- Le notebook de nettoyage (Nettoyage)
- Le notebook de l'analyse exploratoire (EDA)
- Le notebook contenant le feature engineering et la modélisation (synthese - VF)
- Un fichier 'functions' qui contient des fonctions additionnelles



*** Comment utiliser ce répertoire ? ***

- Télécharger les deux set de données 2015 et 2016 ˆ l'adresse suivante : https://www.kaggle.com/city-of-seattle/sea-building-energy-benchmarking
- Les placer dans le répertoire 'données'
- Exécuter le notebook 'Assemblage' disponible dans le dossier 'données'
- Récupérer le .csv qui en résulte (Dataset) et le placer à la racine du répertoire
- Lancer le notebook de nettoyage des données (Nettoyage) qui va générer le .csv 'cleaned_dataset'
- Visualiser l'EDA en lançant le notebook 'EDA'
- Visualiser la partie modélisation en lançant le notebook 'synthese - VF'



*** Quelles librairies sont nécessaires ? ***

Le code a été rédigé en Python, les librairies suivantes doivent être installées :

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Bokeh
- Sklearn
- XGBoost

A l'exception de XGBoost, les autres librairies sont installées de base avec la distribution Anaconda.
Les instructions pour installer XGBoost depuis Anaconda sont disponibles au lien suivant : https://anaconda.org/anaconda/py-xgboost
A noter qu'il est également nécessaire que le fichier 'functions' soit dans le même répertoire que le notebook 'synthese - VF'

Jupiter Notebook est nécessaire pour l'ouverture des Notebook.