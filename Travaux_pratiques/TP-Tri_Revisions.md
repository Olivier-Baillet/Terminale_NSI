# TP : Tri Révisions

## **Tri par sélection**

Autant ne pas le cacher, ces algorithmes sont déjà implémentés (quelque soit le langage) dans des fonctions très performantes.

En Python, on utilise la fonction `sort()`:

```python
>>> tab = [4, 8, 1, 2, 6]
>>> tab.sort()
>>> tab
[1, 2, 4, 6, 8]
```

Le tri par sélection est le premier des deux algorithmes de tri que nous allons réétudier (le deuxième sera le tri par insertion).

Ces deux algorithmes ont pour particularité de :

- ne pas nécessiter la création d'une nouvelle liste. Ils modifient la liste à trier **sur place**.
- ne pas faire intervenir de fonctions complexes.

## Principe du tri

![](https://cgouygou.github.io/1NSI/T07_Algorithmes/images/Selection_sort_numbers.gif)

On cherche à trier un tableau de  valeurs différentes, en général les entiers de $0$ à $n-1$ .

- En partant de l'indice 0, on cherche l'indice du plus petit élément en parcourant le tableau;
- on l'échange avec l'élément d'indice 0;
- On recommence en partant de l'indice 1, puis 2, etc. jusqu'à ce que le tableau soit trié.

---

### Exercice I

On veut écrire une fonction `tri_selection` qui prend en paramètre une liste et qui trie cette liste par l'algorithme du tri par sélection.

1. Écrire un jeu de tests pour cette fonction.
2. Compléter puis tester la fonction ci-dessous.

```python
def tri_selection(tab: list) -> None:
```

*Vérification :*

```python
ma_liste = [7, 5, 2, 8, 1, 4]
tri_selection(ma_liste)
print(ma_liste)
# Résultat attendu :
[1, 2, 4, 5, 7, 8]
```

### Exercice II

On va s'intéresser au temps d'éxécution de ce tri, et plus particulièrement au lien entre la taille de la liste donnée en entrée et ce temps d'éxécution.

On définit donc :

- une fonction `alea` qui renvoie une liste de taille `n` créée aléatoirement;
- une fonction `chrono` qui prend en paramètre un entier `n` et qui renvoie le temps d'éxécution de la fonction `tri_selection` pour la liste construite à partir de la fonction `alea`.

1. Compléter les fonctions dont les extraits sont fournis ci-dessous.
2. Construire une liste (en compréhension si possible) des temps obtenus pour les valeurs de `n` suivantes : 10, 100, 1000, 10000.
3. Quel semble être le lien entre `n` et le temps d'éxécution?

```python
import time
import random as rd

def alea(n):
    lst_alea = list(range(n))
    rd.shuffle(lst_alea)
    return lst_alea

def chrono(n):
    t0 = time.time()
    tri_selection(...)
    t1 = time.time()
    return 

tailles = [10, 100, 1000, 10000]
temps = [...]
```

1. On va visualiser tout ça...

```python
import matplotlib.pyplot as plt

plt.plot(tailles, temps)
plt.show()
```

<aside markdown="1">
💡

Debian / Ubuntu: `sudo apt-get install python3-matplotlib`

Windows :  `python -m pip install -U pip 
python -m pip install -U matplotlib`

</aside>

---

## Tri par insertion

Après le tri par sélection, nous allons étudier un deuxième algorithme de tri: le tri par insertion. C'est le «tri du joueur de cartes».

Il consiste à choisir un élément et de l'insérer à la bonne position en faisant «remonter» les éléments plus grands que lui.

![](https://cgouygou.github.io/1NSI/T07_Algorithmes/images/Insertion_sort_example.gif)

**Quelques remarques:**

- on commence à l'indice 1;
- pour chaque indice de travail `i`, on appelle clé l'élément de la liste d'indice `i`;
- on examine ensuite les éléments à gauche, c'est-à-dire les élements d'indice `j < i`;
- tant que l'élément d'indice `j` est supérieur à la clé, on le décale d'une position vers la droite;
- une fois que ce n'est plus possible, on insère la clé.

---

### Exercice I

Implémenter l'algorithme du tri par insertion sous la forme d'une fonction:

```python
def tri_insertion(tab: list) -> None:
    '''
    Trie en place le tableau tab donné en paramètre
    '''
```

*Vérification :*

```python
ma_liste = [7, 5, 2, 8, 1, 4]
tri_insertion(ma_liste)
print(ma_liste)
# Résultat attendu :
[1, 2, 4, 5, 7, 8]
```

### Exercice II

Il s'agit d'étudier la complexité de cet algorithme de façon expérimentale.

Pour cela:

1. Reprendre les fonctions `chrono` et `pire_cas` de l'exercice 2 sur le tri par sélection et afficher le graphique des temps d'exécution.
2. Faire de même avec une liste déjà triée. Que remarquez-vous?

---

Visualiser les Tris dans différents cas :

[https://www.toptal.com/developers/sorting-algorithms](https://www.toptal.com/developers/sorting-algorithms)

---

### Indice Selection Exercice I

```python

def tri_selection(tab: list) -> None:
    n = len(tab)
    for i in range(...):
        indice_min =
        for j in range( , ):
            if tab[j] < tab[indice_min]:
                ...
        #il reste à échanger les valeurs d'indice i et indice_min
        ...
        ...
        ...
```

### Indice Insertion Exercice I

```python
def tri_insertion(tab: list) -> None:
    '''
    Trie en place le tableau tab donné en paramètre
    '''
    for i in range():
        cle =
        j =
        #décalage des éléments du tableau
        while  and :
            tab[ ] = tab[ ]
            j =
        #on insère l'élément à sa place
        tab[] =
```
