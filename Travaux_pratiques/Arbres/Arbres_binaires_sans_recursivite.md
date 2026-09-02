# TP NSI – Arbres binaires sans récursivité

## **Objectifs du TP**

- Comprendre la structure d’un arbre binaire.
- Manipuler une représentation d’arbre en Python.
- Implémenter trois parcours **sans récursion** :
    - Parcours **préfixe** (DFS)
    - Parcours **en profondeur (DFS) avec pile**
    - Parcours **en largeur (BFS) avec file**

## **Pré-requis**

- Dictionnaires Python
- Piles (listes Python)
- Files (collections.deque)

---

# Mise en place : Représentation d’un arbre binaire

On utilisera la représentation suivante :

```python
arbre = {
    "val": 8,
    "gauche": {
        "val": 3,
        "gauche": {"val": 1, "gauche": None, "droite": None},
        "droite": {"val": 6, "gauche": None, "droite": None}
    },
    "droite": {
        "val": 10,
        "gauche": None,
        "droite": {"val": 14, "gauche": None, "droite": None}
    }
}

```

Arbre correspondant :

```
        8
      /   \
     3    10
    / \     \
   1   6     14

```

---

# Parcours préfixe

*Rappel du parcours préfixe* :

**noeud → gauche → droite**

## Implémentation Python sans récursion (pile)

Compléter :

```python
def parcours_prefixe(racine):
    pile = new objet pile (racine)    # pile contenant le prochain nœud à traiter

    while not pile.estVide() :

```

```python
def parcours_prefixe(racine):
    pile = new objet pile (racine)        # pile contenant le prochain nœud à traiter

    while not pile.estVide() :
			  noeud = pile.depiler()    # retirer le dernier élément ajouté

        # Ajouter les enfants : d’abord le droit pour traiter le gauche en premier
        if __________________________________:
            __________________________________
        if __________________________________:
            __________________________________

```

Test :

```python
parcours_prefixe(arbre)

```

---

```python
def dfs_pile(racine):
    pile = pile(racine)

    while not pile.est_vide():
        print("PILE =", [n["val"] for n in pile])
        noeud = pile.depiler()
        print("Visite :", noeud["val"])

        if noeud.fils_droit().est_vide() : # is not None:
            pile.empiler(noeud.fils_droit())
        if noeud.fils_gauche().est_vide() : # is not None:
            pile.empiler(noeud.fils_gauche())
```

---

# **Parcours en largeur des arbres**

<aside>
💡

**BFS**

- Ce parcours est parfois noté **BFS** pour **B**readth-**F**irst **S**earch
- Le parcours en largeur correspond à un parcours par niveau de noeuds de l'arbre. Un niveau est un ensemble de nœuds ou de feuilles situés à la même profondeur.

C'est un parcours étage par étage (de haut en bas) et de gauche à droite.

![largeur](https://mcoilhac.forge.apps.education.fr/term/arbres/images/largeur.png)

Dans cet exemple, on obtient successivement : 3, 1, 4, 5, 2, 0.

</aside>

Pour étudier cet algorithme de parcours en largeur, nous allons utiliser une file.

Utiliser l’implémentation faite en cours ou si vous ne l’avez pas, vous pouvez utiliser celle de Python : le module Queue

<aside>
💡

Les objets `Queue` (Queue, LifoQueue ou PriorityQueue) fournissent les méthodes publiques décrites ci-dessous.

- `f = Queue()` Créé une file vide nommée `f`.
- `f.qsize()` renvoie la taille de la file `f`.
- `f.empty()` renvoie `True` si la file `f` est vide, `False` sinon
- `f.put(item)` enfile `item` dans la file `f`
- `f.get()` défile (retire) et renvoie l'élément défilé de la file `f`.
</aside>

Compléter le script suivant : la fonction `parcours_BFS` doit renvoyer la liste des noeuds obtenue par le parcours en largeur de l'arbre.

```python
from queue import Queue

def parcours_BFS(arbre):
    file = Queue()
    file.put(arbre)
    solution = []
    ...

- - - - - 

def parcours_BFS(arbre):
    file = file()
    file.empiler(arbre)
    solution = []
    ...
```

<aside>
💡

Aide

```
f = File() # Création d'une file vide
f.enfiler(arbre)

tant que f non vide :
    arbre_au_sommet = f.defiler()
    si arbre_au_sommet n'est pas vide
        On garde son étiquette
        f.enfiler(son sous-arbre gauche)
        f.enfiler(son sous-arbre droit)
    fin si
fin tant que
```

</aside>

```python
f = File
f.enfiler(noeud) //on place la racine dans la file
tant que f non vide :
   n = f.defiler()
   visiter(n)
   si n.gauche n'est pas vide
      f.enfiler(n.gauche)
   fin si
   si n.droit n'est pas vide
      f.enfiler(n.droit)
   fin si
fin tant que
```

<aside>
💡

**Solution**

```python
def parcours_BFS(arbre):
    file = Queue()
    file.put(arbre)
    solution = []
    while not file.empty():
        a = file.get()
        if a is not None :
            solution.append(a.data)
            file.put(a.left)
            file.put(a.right)
    return solution
```

</aside>