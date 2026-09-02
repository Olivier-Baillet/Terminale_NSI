# TP : Analyse de données avec Tableur

## **Téléchargement et Ouverture du fichier**

- Lancez un navigateur web et rendez vous sur la [plateforme ouverte des données publiques françaises](http://www.data.gouv.fr/).
- Recherchez *Films entrées* dans le champs de recherche.
- Téléchargez le fichier *Films ayant réalisé plus d'un million d'entrées* au format `.xlsx`.
- Ouvrir le logiciel *LibreOffice Calc*, et ouvrez le fichier que vous venez de télécharger avec ce logiciel.

### **Analyse sommaire du fichier**

*Justifier vos réponses*

1. Depuis combien de temps les données sont elles extraites ?
2. Les données comptabilisent-elles les entrées en salles dans un seul pays ou dans plusieurs pays ? Justifie ta réponse en t’appuyant sur la source des données.
3. Les nationalités de films présentes dans les données reflètent-elles la diversité des pays producteurs de films dans le monde ? Justifie.

### **Utilisation des filtres**

- Placez-vous dans l'onglet de l'année 2024.
- Cliquez sur la gauche de la ligne 7 (pour la sélectionner entièrement).
- Dans le menu, cliquez sur `Données` puis `AutoFiltre`.
- Filtrez par nationalité, décochez tous les éléments sauf `FRANCE`, puis validez avec le bouton `OK`.

![_primary](https://snt.ababsurdo.fr/les-donnees-structurees-et-leur-traitement/tableur/filtre-fr.png)

Vous ne devriez voir afficher que les films français de l'année 2024.

1. Quels sont les trois films français ayant fait le plus d'entrée en 2024 ?

### Fonction de tableur

- On souhaite connaître le nombre de films français de cette liste.
 Dans la cellule `B5`, écrivez `=SOUS.TOTAL(3;B8:B40)` (cette fonction permet de calculer le nombre de cellules de la colonne `B`, mais seulement pour les cellules filtrés). 
 La cellule devrait afficher `9`, soit 9 films dans cette liste.
- On souhaite connaître le nombre d'entrée réalisées par les films français de cette liste.
 Dans la cellule `E5`,
  écrivez `=SOUS.TOTAL(9;E8:E32)` (cette fonction permet de calculer la somme de la colonne `E`, mais seulement pour les films filtrés).
 La cellule devrait afficher environ 32,11 millions.
- Supprimez le filtre sur la nationalité (vous devez à nouveau voir toutes les nationalités),
 puis triez la colonne `sortie` par date.
    
    ![_primary](https://snt.ababsurdo.fr/les-donnees-structurees-et-leur-traitement/tableur/tri-croissant.png)
    
    *Les trois premiers films affichés devraient être `UN P'TIT TRUC EN PLUS`, `LE COMTE DE MONTE-CRISTO`, `VICE-VERSA 2`.*
    
1. Le 18 ème film est sorti en 2023. Pourquoi est-il affiché dans cette liste qui concerne l'année 2024 ?
2. On veut connaître, parmi les films des États-Unis sortis en 2024, quels sont les trois films ayant réalisé le moins d'entrée parmi ceux présents.
    1. Décrire sur votre compte-rendu votre démarche pour répondre à cette question : Quels filtres appliqués ? Quels tris ?
    2. Répondre à la question.

## **Tâche complexe**

Dans cette partie, les réponses seules aux questions ne rapporteront que peu de point. La **démarche** utilisée devra être expliquée.

- Retournez sur [data.gouv.fr](https://www.data.gouv.fr/), et recherchez `liste cinémas`, puis cliquez sur `Liste des établissements cinématographiques actifs`.
- Téléchargez le fichier, et ouvrez le avec *LibreOffice*.
- Utilisez ce fichier, et les filtres, tris, fonctions vus à la question précédente pour répondre aux questions suivantes, en regardant l'année la plus récente. Si nécessaire, vous pouvez consulter la [documentation pour la fonction `SOUS.TOTAL`](https://help.libreoffice.org/latest/fr/text/scalc/01/04060106.html?#Section12).
    
    Attention : Pour chaque question, préciser la démarche utilisée : Quels filtres avez-vous utilisé ? Quels tris ? Quelles fonctions (dans quelles cellules) ? Quelles analyses ou manipulations avez-vous effectuées « à la main » ? Votre démarche est clairement expliquée si en lisant votre compte-rendu, il est possible de l'appliquer sans hésitation et sans erreur.
    
    1. Quelle est la salle de cinéma en France ayant le plus de fauteuils ? Donner la ville, le nom de la salle, le nombre de fauteuils.
    2. Combien d'écrans et de fauteuils l'unique cinéma de Vienne a-t-il ?
    3. Combien y a-t-il en France de cinéma *« SALLE DES FETES»*  itinérants ? *Attention : il y a deux conditions.*
    4. Combien de fauteuils ont l'ensemble des dix plus gros cinémas français (en nombre de fauteuils) ?
    5. Combien les cinémas français ont-ils d'écrans, en moyenne (arrondir au dixième) ?

## **Rendu**

- Convertissez votre compte-rendu au format PDF.
- Vérifiez que votre nom apparait dans le nom du document.
- Rendez-moi le compte-rendu sur Moodle.
