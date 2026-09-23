# Les files

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/giffile.webp)

Comme expliqué précédemment, une file travaille en mode FIFO (First In First Out). Pour être utilisée, une interface de file doit proposer a minima :

- la création d'une file vide
- l'ajout d'un élément dans la file. On dira qu'on **enfile**.
- le retrait d'un élément de la file et le renvoi de sa valeur. On dira qu'on **défile**.

La représentation la plus courante d'une file se fait horizontalement, en enfilant par la gauche et en défilant par la droite :

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/repfile.png)

## **4.1 Utilisation d'une interface de file**

### **Exercice 7**

On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la file `f` et la valeur éventuellement renvoyée. Par convention, on enfilera **à gauche** et on défilera **à droite**.

```python
1. f = File()
2. f.enfile(3) 
3. f.enfile(5)
4. f.est_vide()
5. f.enfile(1) 
6. f.defile() 
7. f.defile()
8. f.enfile(9) 
9. f.defile() 
10. f.defile()
11. f.est_vide() 
```

## **4.2 Implémentation d'une file**

L'objectif est de créer une classe `File`, disposant des méthodes suivantes :

- `est_vide` : indique si la file est vide. (renvoie un booléen)
- `enfile` : insère un élément (passé en paramètre) en queue de file. (ne renvoie rien)
- `defile` : renvoie la valeur de l'élément en tête de la file ET le supprime de la file.

Nous y ajouterons comme précédemment la méthode facultative suivante :
- `__repr__` : permet d'afficher la file sous forme agréable (par ex : `|3|6|2|5|`)

### **Exercice 8**

Créer la classe ci-dessus. Là encore, le type `list` de Python est peut être utilisé.
Penser à aller voir [ici](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists) les méthodes des objets de types `list`, notamment la méthode `insert`.


**Remarque :**

Notre implémentation répond parfaitement à l'interface qui était demandée. Mais si le «cahier des charges» obligeait à ce que les opérations `enfile()` et `defile()` aient lieu en temps constant (en ), notre implémentation ne conviendrait pas.

En cause : notre méthode `enfile()` agit en temps linéaire () et non pas en temps constant. L'utilisation de la structure de «liste» de Python (les *tableaux dynamiques*) provoque, lors de l'instruction `self.data.insert(0, x)` un redimensionnement de la liste. Le tableau doit être agrandi et chaque élément doit être recopié dans la case suivante. Ceci nous coûte un temps linéaire.

## **4.3 Implémentation d'une file avec deux piles**

Comment créer une file avec 2 piles ?

L'idée est la suivante : on crée une pile d'entrée et une pile de sortie.

- quand on veut enfiler, on empile sur la pile d'entrée.
- quand on veut défiler, on dépile sur la pile de sortie.
- si celle-ci est vide, on dépile entièrement la pile d'entrée dans la pile de sortie.

### **Exercice 9**

Créer une file avec deux piles.
