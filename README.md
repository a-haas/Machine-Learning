# Apprentissage statistique

## Datahandler

Le fichier datahandler.py est un ensemble de fonction qui a pour objectif de formaliser les datasets afin qu'ils puissent être utilisés au sein des algorithmes de machine learning ci-dessous.

### Liste des fonctions

* csvtolist (filename) : Lis un csv nommé filename et le transforme en liste
* csvtoheader(filename) : récupère un tableau 1D d'un fichier csv nommé filename
* csvtoattributearray(filename, headerfilename) : Créé un dictionnaire avec comme clé les attributs et comme valeur le tableau de cet attribut pour chaque ligne du dataset (ex : datasetdict["attribute1"] donne [0.1, 0.2, ...])
* splitio(inputname, outputname, matrix) : Prend le data set nommé matrix et sépare les inputs des outputs pour les mettre dans les fichiers nommés, respectivement, inputname et outputname.
* normalise(matrix, max, min) : Fonction qui permet de normaliser une matrice entre 0 et 1 


## Naive Bayes Classifier

Le Naive Bayes Classifier est un algorithme de classification supervisé. Son interet, malgré ses quelques restrictions, se trouve dans sa rapidité. On peut citer comme restriction forte le fait que les attributs du dataset sont tous indépendants. Cependant même si l'indépendance n'est pas respectée, l'algorithme peut toujours fonctionné.

### Algorithme

1. Séparer les données par classes
2. Calculer la moyenne et l'écart-type pour chacun des attributs en fonction des classes (dans un cadre continu)
3. Calculer la probabilité d'apparition de chacune des classes
4. Ensuite on multiplie les probabilités des attributs en fonction du vecteur à tester pour chacune des classes
5. On prend la valeur la plus élevée

### Démo

Une démo est disponible (cf. naivebayesdemo.py) et permet de tester le classifier sur le dataset iris

### Limitations

Cette implémentation nécessite un fichier csv d'input et un autre d'output. Le vecteur d'entrée ne contient que des valeurs continues et le vecteur de sortie ne doit contenir qu'une seule valeur.

### Sources

* http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
* https://en.wikipedia.org/wiki/Naive_Bayes_classifier
* https://www.youtube.com/watch?v=IlVINQDk4o8