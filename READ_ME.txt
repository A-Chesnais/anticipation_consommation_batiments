
*** Que contient ce r�pertoire de travail ? ***

- Un dossier "donn�es", qui contient les donn�es d'origine et
  le script pour assembler les sets de 2015 et 2016

Sous la racine on trouve :

- Le notebook de nettoyage (Nettoyage)
- Le notebook de l'analyse exploratoire (EDA)
- Le notebook contenant le feature engineering et la mod�lisation (synthe�se - VF)
- Un fichier 'functions' qui contient des fonctions additionnelles



*** Comment utiliser ce r�pertoire ? ***

- T�l�charger les deux set de donn�es 2015 et 2016 � l'adresse suivante : https://www.kaggle.com/city-of-seattle/sea-building-energy-benchmarking
- Les placer dans le r�pertoire 'donn�es'
- Ex�cuter le notebook 'Assemblage' disponible dans le dossier 'donn�es'
- R�cup�rer le .csv qui en r�sulte (Dataset) et le placer � la racine du r�pertoire
- Lancer le notebook de nettoyage des donn�es (Nettoyage) qui va g�n�rer le .csv 'cleaned_dataset'
- Visualiser l'EDA en lan��ant le notebook 'EDA'
- Visualiser la partie mod�lisation en lan�ant le notebook 'synthe�se - VF'



*** Quelles librairies sont n�cessaires ? ***

Le code a �t� r�dig� en Python, les librairies suivantes doivent �tre install�es :

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Bokeh
- Sklearn
- XGBoost

A l'exception de XGBoost, les autres librairies sont install�es de base avec la distribution Anaconda.
Les instructions pour installer XGBoost depuis Anaconda sont disponibles au lien suivant : https://anaconda.org/anaconda/py-xgboost
A noter qu'il est �galement n�cessaire que le fichier 'functions' soit dans le m�me r�pertoire que le notebook 'synthe�se - VF'

Jupiter Notebook est n�cessaire pour l'ouverture des Notebook.