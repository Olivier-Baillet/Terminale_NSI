# Récursivité

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/BO.png)

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/infini.jpeg)

# 1. Première approche

## 1.1. Définition

<aside>

**Fonction récursive**

Une fonction est dite récursive lorsqu'elle fait appel à elle-même dans sa propre définition.

</aside>

### 1.2 La mauvaise réputation

Dans la culture informatique, la récursivité est (trop) souvent abordée par le biais de l'auto-référence, le puits sans fin de la boucle infinie.

On trouve d'ailleurs fréquemment cette définition de la récursivité :

> **Fonction récursive** : fonction qui fait appel à la récursivité. Voir *fonction récursive*.
> 

Google fait aussi (dans toutes les langues) la même blague lors d'une recherche sur le terme «récursivité» :

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/google.png)

Les [acronymes récursifs](https://fr.wikipedia.org/wiki/Sigles_auto-r%C3%A9f%C3%A9rentiels) sont aussi très fréquents... et véhiculent avec eux le même piège : une fonction récursive ne serait *jamais vraiment définie* (c'est faux, nous le verrons)

Par exemple :

- GNU (dans GNU/Linux) signifie GNU is Not Unix. On ne sait jamais vraiment ce que signifie GNU...
- PHP (le langage serveur) sigifie PHP: Hypertext Preprocessor
- VISA (les cartes bancaires) signifie VISA International Service Association.

# 2. La récursivité, ça marche !

Disons-le clairement : au-delà de la blague pour initiés (dont vous faites partie maintenant) la récursivité ne DOIT PAS être associée à une auto-référence vertigineuse : c'est en algorithmique une méthode (parfois) très efficace, à condition de respecter une règle cruciale :

> **L'existence d'un CAS DE BASE**.
> 

Ce «cas de base» sera aussi appelé «condition d'arrêt», puisque la très grande majorité des algorithmes récursifs peuvent être perçus comme des escaliers qu'on descend marche par marche, jusqu'au sol qui assure notre arrêt.

<aside>

**Terminaison possible**

Pour s'assurer qu'une fonction récursive se termine, il faut **absolument** que la chaîne d'appel conduise au cas de base.

- si le paramètre de la fonction est un entier, alors l'appel doit se faire avec un **entier strictement inférieur**;
- si le paramètre de la fonction est une liste, alors l'appel doit se faire avec une liste de **longueur strictement inférieure**;
- etc.
</aside>

## 2.1 La récursivité en BD

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.2_Recursivite/data/bd.png)

Observez bien la descente puis la remontée de notre vendeur de livre. Le cas de base est ici l'étage 0. Il empêche une descente infinie.

Nous coderons bientôt la fonction donnant le prix du livre en fonction de l'étage.

Pour l'instant, découvrons enfin à quoi ressemble une fonction récursive «bien écrite» :

## 2.2 Enfin un bon exemple

**Exemple fondateur n°1**

```python
def mystere(n):
    if n == 0 :
        return 0
    else :
        return n + mystere(n-1)
```

---

Trois choses sont essentielles et doivent se retrouver dans tout programme récursif :

- `lignes 2 et 3` : le cas de base (si `n` vaut 0 on renvoie *vraiment* une valeur, en l'occurrence 0)
- `ligne 5` : l'appel récursif
- `ligne 5` : la décrémentation du paramètre d'appel

## **2.3 Premiers exemples et précautions d'usage**

Voici trois premiers exemples de fonctions récursives. Dans chaque cas, repérer l'appel récursif à la fonction.

Une seule de ces 3 fonctions est correcte, laquelle?

```python
def f(n):
    print(n)
    f(n-1)
    print("Hello world!")
```

```python
def f(n):
		if n == 0:
				print("Hello world!")
		else:
				print(n)
				f(n)
```

```python
def f(n):
		if n == 0:
				print("Hello world!")
		else:
				print(n)
				f(n-1)
```

## **2.4 Exemples à connaître**

### **2.4.1 Somme des n premiers entiers**

On souhaite calculer la somme suivante : $S= 0+1+2+3+ … + (n-1)+n$

En première, on a vu comment construire une fonction *itérative* le permettant, à l'aide d'une boucle `for` (d'où le terme *itératif*) et d'une variable accumulatrice:

```python
def somme(n):
    s = 0
    for k in range(n+1):
        s += k
    return s
```

---

Une autre façon de voir le problème, c'est de se dire que cette somme peut s'écrire
 $S= n +1(n-1)+ … + 3+2+1+0$ 
Et que c'est la somme de $n$ et **de la somme des**  $n-1$ **premiers entiers.**

On écrit alors de façon «assez naturelle» la fonction récursive suivante:

```python
def somme(n):
    if n == 0:
        return 0
    else:
        return n + somme(n-1)
```

---

### **2.4.2 Factorielle**

En mathématiques, la factorielle d'un nombre entier , notée , est le produit de tous les entiers positifs non nuls inférieurs ou égaux à .

Autrement dit, $n! = 1*2*3*…*(n-1)*n = n*(n-1)* … * 3*2*1$

#### **Exercice 1**

S'inspirer des fonctions `somme` précédentes pour écrire deux fonctions `facto_iter` (itérative) et `facto_rec` (récursive) renvoyant la factorielle d'un nombre entier `n` strictement positif.

# 3 Mécanisme

Maintenant qu'on a vu le principe d'une fonction récursive, il faut comprendre comment se passent les appels successifs à la fonction, pour un paramètre différent.

Reprenons l'exemple de la fonction récursive `somme`. Si on appelle cette fonction:

```python
>>> somme(5)
```

Puisque l'argument `5` ne correspond pas au cas de base, la fonction va faire appel à `somme(4)` . Il faut retenir que l'exécution de la fonction `somme` est interrompue (avec l'argument `5` ) pour rappeler la fonction `somme` (avec l'argument `4` )...

Pour gérer ces différents appels, le système utilise une **pile d'exécution**:

- On parle de pile, car les exécutions successives «s'empilent» les unes sur les autres.
- Lorsque le cas de base est atteint, on «dépile» les instructions.

D'où l'importance de l'existence du cas de base, et de s'assurer qu'il sera bien atteint...

<aside>

**Limitation de la taille de la pile**

Dans l'exemple précédent, la pile a une *profondeur* de 6. La profondeur de la pile n'est pas illimitée:

```python
>>> somme(1000)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "<tmp 1>", line 5, in somme
    return n + somme(n-1)
  File "<tmp 1>", line 5, in somme
    return n + somme(n-1)
  File "<tmp 1>", line 5, in somme
    return n + somme(n-1)
  [Previous line repeated 984 more times]
  File "<tmp 1>", line 2, in somme
    if n == 0:
RecursionError: maximum recursion depth exceeded in comparison
```

---

Vous venons de provoquer un «débordement de pile», le célèbre **stack overflow.**

</aside>

De manière générale, les programmes récursifs sont souvent proches de la définition du problème à résoudre et assez naturels à écrire, mais ils sont susceptibles de générer un trop grand nombre d'appels à eux-mêmes et de nécessiter un temps d'exécution trop grand ou un débordement de pile.
Il est parfois possible de les optimiser, comme nous le verrons dans le cours concernant la **programmation dynamique**.