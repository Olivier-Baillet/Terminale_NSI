## **Exercice 1**

Utiliser la fonction `construire` pour créer la liste `lst` de l'exemple:

![](https://cgouygou.github.io/TNSI/T01_StructuresDonnees/images/llist3.png)

Vous devez avoir ensuite:

```python
>>> print(l)
3 -> 5 -> 1
>>> l.tete()
3
>>> l.queue()
<__main__.Liste object at 0x...>
>>> print(l.queue())
5 -> 1
>>> l.queue().tete()
5
>>> l.queue().queue().tete()
1
```

## **Exercice 2**

Écrire une fonction `longueur` qui renvoie la longueur d'une liste en paramètre (ou ajouter la méthode spéciale `__len__` à la classe `Liste`)

Quelle est la complexité de cette fonction?

## **Exercice 3**

Ajouter la méthode `insert` à la classe `Liste`, qui insère une valeur **en tête** de liste.

---

## **Exercice 4**

Écrire les fonctions suivantes (récursivement si possible):

1. `concatener(lst1, lst2)` : fonction qui opère une concaténation de deux listes, c'est-à-dire les mettre bout à bout.
2. `nieme(lst, n)` : fonction qui renvoie le n-ième élément de la liste (sashant que la tête est le «0-ième»).
3. `occurences(x, lst)` : fonction qui renvoie le nombre d'occurences de la valeur `x` dans `lst`.

Quelle est la complexité de ces fonctions?
