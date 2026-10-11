# Exercices

## **Exercice 1**

Écrire une fonction récursive `puissance` qui prend en paramètres deux nombres `x` et `n` qui renvoie le nombre .
    

## **Exercice 2**

Écrire une fonction `somme_tab` qui prend en paramètre:

- un tableau d'entiers `tab`
- un indice `i`

et qui renvoie la somme des éléments du tableau à partir de l'indice donné.

**Conseil:** Bien réfléchir au cas d'arrêt et à l'appel récursif avant de se lancer dans l'écriture de la fonction...

## **Exercice 3**

La [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) (ou de Collatz) postule ceci :

*Prenons un nombre  : si  est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.*

**Q1.** Écrire une fonction récursive `syracuse` qui prend en paramètres une entier `n` et qui écrivant tous les termes de la suite de Syracuse commençant à `n` , et s'arrêtant (on l'espère...) à la valeur 1.    
    
Remarque : comme notre fonction `syracuse` ne renvoie pas de valeur numérique (elle ne fait qu'afficher une valeur), le `return` du test de parité est en fait inutile.

Mais le `return` du cas de base est lui primordial pour que le code s'arrête !

```python
def syracuse(n):
    print(n)
    if n == 1:
        return None
    if n % 2 == 0:
        syracuse(n // 2)
    else:
        syracuse(3*n + 1)
```

    

**Q2.** On appelle «temps de vol» le nombre d'étapes nécessaires avant de retomber sur 1. Modifier la fonction précédente afin qu'elle affiche le temps de vol pour tout nombre `n`.
    
    

## **Exercice 4**

Reproduire le dessin suivant, à l'aide du module `turtle`.

`turtle` est un hommage au langage LOGO inventé par [Seymour Papert](https://fr.wikipedia.org/wiki/Seymour_Papert) au MIT à la fin des années 60.

![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/carres_turtle.png)

    

## **Exercice 5**

Proposer une nouvelle fonction récursive `puissance_mod` qui prend en paramètres deux nombres `x` et `n` et qui renvoie le nombre . Pour optimiser la fonction déjà construite à l'exercice 1, utiliser le fait que :

- si est pair,
- sinon

    

## **Exercice 6**

Écrire un algorithme récursif `dicho_recursive` qui prend en paramètres une liste **triée** (par ordre croissant) `lst` et une valeur `val` et qui renvoie un booléen indiquant la présence ou non de la valeur `val` dans une liste `lst`.

*Exemple d'utilisation :*

```python
>>> lst = [2,4,5,5,7,9,11,15,16,18,19]
>>> dicho_recursive(lst, 16)
[2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
[9, 11, 15, 16, 18, 19]
[16, 18, 19]
[16]
True
>>> dicho_recursive(lst, 6)
[2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
[2, 4, 5, 5, 7]
[5, 5, 7]
[5, 7]
[5]
False
```

*Aide :*

Les techniques de *slicing* (hors-programme) permettent de couper une liste en deux :

```python
>>> lst = [10, 12, 15, 17, 18, 20, 22]
>>> lst[:3]
[10, 12, 15]
>>> lst[3:]
[17, 18, 20, 22]
```

    

## **Exercice 7**

On considère le jeu des **Tours de Hanoï**. Le but est de faire passer toutes les assiettes de A vers C, sachant qu'une assiette ne peut être déposée que sur une assiette de diamètre inférieur.

![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/hanoi0.png)

Une version jouable en ligne peut être trouvée [ici](https://www.mathsisfun.com/games/towerofhanoi.html).

1. S'entraîner et essayer d'établir une stratégie de victoire.
2. Observer les images ci-dessous :
    
    ![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/hanoi1.png)
    
    ![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/hanoi2.png)
    
    ![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/hanoi3.png)
    
    ![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/hanoi4.png)
    

Écrire une fonction récursive `hanoi(n, depart, inter, arrivee)` qui donnera la suite d'instructions (sous la forme " A vers C") pour faire passer une pile de taille n de `depart` vers `arrivee` en prenant `inter` comme intermédiaire.


    

## **Exercice 8**

Cet exercice a pour objectif le tracé du flocon de Von Koch.

![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/floc.png)

**Les fractales**

Ce flocon est une structure [fractale](https://fr.wikipedia.org/wiki/Fractale), au même titre que le superbe [ensemble de Mandelbrot](https://mandelbrot.site/), dont vous pouvez trouver une implémentation en Pygame [ici](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/mandelbrot_pygame.py).

L'idée est de répéter de manière récursive la transformation ci-dessous : chaque segment de longueur `l` donne naissance à 4 segments de longueur `l/3`, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/ex2.png)

**Q1.** Créer une fonction récursive `floc(n, l)` qui trace à une «profondeur» `n` un segment de longueur `l` .

![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/ex3b.png)

**Indications**

- l'instruction de tracé n'a lieu que quand `n` vaut 0.
- l'étape `n` fait 4 appels successifs à l'étape `n-1`.

    
    

**Q2.** Créer une fonction `triangle(n, l)` qui trace le flocon complet.


    

## **Exercice 9**

1. [Exercice 43.2 de la BNS 2025](https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2025/#exercice-432)
2. Application sur Capytale à retrouver [ici](https://capytale2.ac-paris.fr/web/c/ffb5-785788/mlc)

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/diffusion.png)


    

## **Exercice 10**

Exercice 4 du sujet [Amérique du Nord J1 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Amerique_Nord_J1.pdf)

## **Exercice 11**

Exercice 1 du sujet [Centres Étrangers J2 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Centres_Etrangers_J2.pdf)

## **Exercice 12**

Exercice 1 du [sujet Amérique du Nord J2 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ2AN1.pdf)

## **Exercice 13**

Le [flocon de Koch](https://fr.wikipedia.org/wiki/Flocon_de_Koch) est une [figure fractale](https://fr.wikipedia.org/wiki/Fractale) obtenue par itérations successives d'une même transformation sur chacun de ses segments.

La transformation est la suivante: chaque segment de longueur `l` donne naissance à 4 segments de longueur `l/3`, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

![](https://cgouygou.github.io/TNSI/T02_Programmation/images/segmentkoch.png)

**Animation des premières étapes:**

![](https://cgouygou.github.io/TNSI/T02_Programmation/images/Von_Koch_curve.gif)

**Consignes :**

1. Écrire une fonction récursive `segment` qui prend un entier `n` et un entier `l` et qui trace le segment de longueur `l` correspondant à l'étape `n`.
2. Écrire une fonction `flocon` qui trace le flocon entier (mêmes paramètres).

**Indications :**

- Le tracé ne se fait qu'à l'étape 0;
- l'étape `n` fait 4 appels récursifs à l'étape `n1` .
