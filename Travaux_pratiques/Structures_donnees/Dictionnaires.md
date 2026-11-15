# Dictionnaires
Au préalable, on peut relire le [chapitre de Première](https://olivier-baillet.github.io/Premiere_NSI/Progression/Types_construits/Dictionnaires).

# 1. Retour sur les dictionnaires

En Python, un dictionnaire (`<class 'dict'>`) est une structure de données native qui permet de représenter le type abstrait de données appelé *tableau associatif* ou *p-uplet nommé* qui correspond à un tableau dont les valeurs sont indexées par des clés, et dont l'interface contient généralement les opérations:

- **ajout** : association d'une nouvelle valeur à une nouvelle clé ;
- **modification** : association d'une nouvelle valeur à une ancienne clé ;
- **suppression** : suppression d'une clé (et donc de la valeur);
- **recherche** : détermination de la valeur associée à une clé, si elle existe.

Puisqu'un tableau associatif est un ensemble de couples *clé:valeur*, on pourrait penser l'implémenter simplement avec une simple liste de couples. Mais ainsi la recherche d'une clé (pour modification, suppression ou recherche) ne correspondrait plus à l'indice du couple dans la liste. Il faudrait donc pour chaque clé faire une recherche dans la liste.

# 2. Table de hachage

Puisqu'un tableau classique ne convient pas, il existe principalement deux méthodes pour implémenter **correctement** un tableau associatif:

- un arbre binaire de recherche;
- une table de hachage.

Python, avec le type `dict`, utilise une table de hachage.

### **Principe d'une table de hachage**

Une table de hachage est un **tableau couplé à une [fonction de hachage](https://cgouygou.github.io/TNSI/T09_Extras/Hachage/)**.

Le dictionnaire `d = {"pommes":3, "poires":0, "bananes":5}` sera implémenté dans un tableau comme celui-ci:

![](https://cgouygou.github.io/TNSI/T01_StructuresDonnees/images/hashdico.png)

- À chaque nouvelle clé, la fonction de hachage calcule un nombre entier (le «haché», ou «condensé»): par exemple `"pommes"` sera haché en `7e1fd3345`;
- un calcul sur cet entier donne un indice correspondant à la clé dans le tableau, généralement en prenant le reste de la division euclidienne de la valeur de hachage par la taille du tableau: `7e1fd3345` devient l'indice `4`;
- On obtient ainsi la position du couple (clé, valeur) dans le tableau, pour l’ajout ou pour la recherche.

Le calcul de l’indice à partir de la clé s’effectue donc en temps constant. Et Python sait où chercher une clé: soit il la trouve à l'indice calculé, soit il n'y a rien et la clé n'appartient pas au dictionnaire.

### **Collisions**

En théorie, toutes les clés peuvent être associées au même indice et terminer dans la même alvéole (case du tableau, bucket en anglais). La recherche d’une clé s’effectue alors en . C’est le pire des cas.

En pratique, le semblant d’aléatoire de la fonction de hachage permet généralement une répartition équilibrée dans le tableau avec un petit nombre de couples dans chaque alvéole. Si le nombre de collisions (couples dans chaque alvéole) est majoré par une constante (au plus quatre couples dans chaque alvéole par exemple), l’ajout ou la recherche d’une clé sont en temps constant.

En résumé, avec une table de hachage, l’ajout ou la recherche d’une valeur sont généralement en temps constant, en , mais peuvent être en  dans le pire des cas. Cela dépend des collisions.

### **Clé non mutables**

On ne peut pas utiliser un objet mutable comme clé: un dictionnaire a besoin d'avoir des clés dont les hachés sont définitifs.

Or si on prend une liste par exemple comme clé, on pourrait la modifier en dehors et donc ne plus la trouver dans le dictionnaire puisque son haché (et donc son indice dans le tableau) aurait changé!

On dit également que le type `list` n'est pas hachable.

```python
>>> lst = ["non", "hachable"]
>>> dico = {lst : "non non non"}
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: unhashable type: 'list'
```
