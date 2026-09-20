# Les listes

## **2.1 Définition générale**

Une liste est un ensemble ordonné d'objets. Généralement, ces données seront de même type, mais ce n'est pas structurellement obligatoire.

## **2.2 Les listes chaînées *(linked lists)***

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/linked.png)

Lorsque l'implémentation de la liste fait apparaître une chaîne de valeurs, chacune pointant vers la suivante, on dit que la liste est une liste **chaînée**.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/listechainee.png)

**Implémentation choisie :**

- Une liste est caractérisée par un ensemble de cellules.
- Le lien (on dira souvent le «pointeur») de la variable est un lien vers la première cellule, qui renverra elle-même sur la deuxième, etc.
- Chaque cellule contient donc une valeur et un lien vers la cellule suivante.
- Une liste peut être vide (la liste vide est notée `x` ou bien `None` sur les schémas)

Une conséquence de cette implémentation sous forme de liste chaînée est la non-constance du temps d'accès à un élément de liste : pour accéder au 3ème élément, il faut obligatoirement passer par les deux précédents.

**À retenir :** dans une liste chaînée, le temps d'accès aux éléments n'est pas constant.

## **2.3 Exemple d'implémentation minimale d'une liste chaînée**

```python
**#Exemple fondateur : implémentation d'une liste chainée en POO** 

class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante

```

Cette implémentation rudimentaire permet bien la création d'une liste :

```python

>>> lst = Cellule(3, Cellule(5, Cellule(1,None)))
```

La liste créée est donc : 

```python
[ 3, 5, 1 ]
```

Mais plus précisément, on a :

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/ex2.png)

### **Exercice 1**

Retrouvez comment accéder aux éléments 3, 5 et 1.

## **2.4 Et les listes de Python ???**

Nous connaissons déjà les listes de Python :

```python
>>> maliste = [3, 1, -1, 42]
```

Et nous connaissons aussi (un peu) l'interface de ce type `list`, notamment avec les méthodes `append()` ou `reverse()`.

Néanmoins, l'implémentation qui a été choisie par les concepteurs de Python de ce type `list` fait que le celui-ci se rapproche plus d'un **tableau dynamique**.

**Dans un tableau dynamique :**

- le temps d'accès à n'importe quel élément est rapide. Ce temps d'accès est constant quelque soit l'élément : on dit que l'accès est en $O(1)$.
- l'insertion d'un élément au début ou au milieu de la liste est lente : cela oblige à décaler tous les éléments à droite de celui-ci. Le temps pris par l'insertion est proportionnel au nombre d'éléments à déplacer : on dit que l'insertion est en $O(n)$.

**Dans une liste chaînée :**

- le temps d'accès à n'importe quel élément peut être lent (proportionnel à la position de l'élément dans la liste). Le temps d'accès est en $O(n)$ .
- l'insertion d'un élément à l'intérieur de la liste est rapide : il y a simplement à modifier la valeur du lien de la cellule à gauche de l'endroit d'insertion. L'action d'insérer est donc en $O(1)$ . Toutefois, avant d'arriver à l'endroit d'insertion, il faut avoir parcouru toutes les cellules précédentes ! Le temps total d'insertion est donc lui aussi linéaire, en  .

Nous nous servirons parfois du type `list` de Python dans la suite de ce cours, mais il ne faut pas oublier qu'il n'est pas un «vrai» type `list`.

## **2.5 Un exemple d'interface pour les listes**

Imaginons que nous possédons une interface offrant les fonctionnalités suivantes :
• `Liste()` : crée une liste vide.
• `est_vide` : indique si la liste est vide. (renvoie un booléen)
• `ajoute_tete` : insère un élément (passé en paramètre) en tête de liste. (ne renvoie rien)
• `renvoie_tete` : renvoie la valeur de l'élément en tête de liste ET le supprime de la liste.

### **Exercice 2**

On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la liste `lst` et la valeur éventuellement renvoyée. On considèrera que la tête de la liste est à gauche.

```python
1. lst = Liste()      
2. lst.ajoute_tete(3)
3. lst.ajoute_tete(5) 
4. lst.ajoute_tete(1) 
5. lst.renvoie_tete() 
6. lst.est_vide()     
7. lst.ajoute_tete(2) 
8. lst.renvoie_tete() 
9. lst.renvoie_tete() 
10. lst.renvoie_tete()
11. lst.est_vide()
```