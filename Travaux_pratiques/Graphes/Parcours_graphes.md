# 4. Parcours de graphes

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/toutgraphe.jpeg)

### **Algorithme de parcours**

Un parcours de graphe est un algorithme consistant à explorer **tous** les sommets d'un graphe de proche en proche à partir d'un sommet initial. Ces parcours sont notamment utilisés pour rechercher un plus court chemin (et donc dans les GPS) ou pour trouver la sortie d'un labyrinthe...

Parcourir simplement le dictionnaire ou la matrice d’un graphe n’est pas considéré comme un parcours de graphe.

Tous les parcours suivent plus ou moins le même algorithme de base :

- On visite un sommet `A` . On crée une structure `S` qui contiendra au départ uniquement le sommet `A` .
- Tant que `S` n’est pas vide :
    - on choisit un sommet `s` de `S` (on dit qu'on «visite» `s`);
    - on ajoute à `S` tous les voisins de `s` **pas encore visités**.

### **Sommets visités**

Contrairement à un parcours d'arbre, où un nœud ne peut pas être fils de deux nœuds différents, un sommet **peut** être voisin de deux sommets différents.

Il est donc nécessaire de mémoriser les sommets déja visités ou découverts (on dira qu'un sommet est découvert lorsqu'on l'ajoute à `S`).

Le choix de la structure de l'ensemble `S` est prépondérant:

- Si on choisit une **file** (FIFO): on visitera les sommets dans l'ordre d'arrivée, donc les plus proches du sommet précédent. On obtient donc un *parcours en largeur*  **BFS**.
- Si on choisit une **pile** (LIFO): on visitera d'abord les derniers sommets arrivés, donc on parcourt le graphe en visitant à chaque étape un voisin du précédent. On obtient donc un *parcours en profondeur*  **DFS**.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/dfs_or_bfs_meme.jpg)

# 4.1 Le parcours en largeur (BFS, Breadth First Search)

## **4.1.1 Principe**

**Exemple de parcours en largeur, avec B comme sommet de départ:**

**Codes couleur :**

- **vert** : les sommets non encore traités.
- **rouge** : le sommet en cours de traitement.
- **orange** : la file d'attente des sommets qui seront bientôt traités. On y rajoute à chaque fois les voisins du sommet en cours de traitement, uniquement **si ils n'ont pas encore été découverts**.
- **noir** : les sommets traités.

## **4.1.2 Algorithme BFS**

On utilise :

- une liste `traites` qui recueille les sommets visités (c'est-à-dire qu'on a fini de traiter, après avoir ajouté ses voisins dans la file d'attente) et qui sera renvoyée à la fin de l'algorithme;
- une liste `decouverts` qui contient les sommets découverts au fur et à mesure du parcours;
- une **file** `en_attente` qui contient les sommets découverts mais non encore visités. On utilisera au choix une classe `File` écrite plus tôt dans l'année ou tout simplement une `list` en utilisant `pop(0)` (pour défiler) et `append()` (pour enfiler).

En début d'algorithme, seul le sommet de départ `depart` donné en paramètre est découvert. La fonction `BFS` renvoie la liste des sommets dans l'ordre de visite lors du parcours en largeur.

### **Parcours en largeur - BFS**

```python
def BFS(g, depart):
    '''
    Effectue un parcours en largeur du graphe g en partant du sommet depart,
    et renvoie la liste des sommets visités dans l'ordre du parcours.
    '''
    traites = []
    decouverts = [depart]
    en_attente = [depart]
    while en_attente != [] :
        sommet = en_attente.pop(0)
        voisins = g.voisins(sommet)
        for voisin in voisins:
            if voisin not in decouverts:
                decouverts.append(voisin)
                en_attente.append(voisin)
        traites.append(sommet)
    return traites
```

---

**Intérêt de la liste `decouverts`**

La liste `decouverts` contient tous les sommets qui ont été :

- soit traités (auquel cas ils sont dans la liste `traites`)
- soit en attente (auquel cas ils sont dans la liste `en_attente`)

Le test de la ligne 13 `if voisin not in decouverts:` permet donc de ne pas mettre en file d'attente un voisin qui est (ou a été) déjà en file d'attente.

**Que contient la file `en_attente` ?**

À chaque instant, la file `en_attente` contient des sommets à la distance `k+1` et à la distance `k` du point de départ :

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/en_attente.png)

### **Exercice 4**

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/BFS_ex1.png)

Grâce à la classe `Graphe` du 3.3, ce graphe s'implémente par :

```python
g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
g.ajoute_arete('A', 'B')
g.ajoute_arete('A', 'C')
g.ajoute_arete('B', 'D')
g.ajoute_arete('D', 'C')
g.ajoute_arete('B', 'E')
g.ajoute_arete('D', 'E')
g.ajoute_arete('E', 'F')
g.ajoute_arete('E', 'G')
g.ajoute_arete('F', 'G')
g.ajoute_arete('G', 'H')
```

---

**Q1.** Donner le parcours en largeur de `g` grâce à l'algorithme BFS, si le sommet de départ est B. Cela correspond au parcours présenté par le gif de début de paragraphe.

- **Correction**
    
    ```python
    >>> BFS(g, 'B')
    ['B', 'A', 'D', 'E', 'C', 'F', 'G', 'H']
    ```
    

**Q2.** Deviner le parcours en largeur de départ D, puis de départ G. Vérifier grâce à votre algorithme.

- **Correction**
    
    ```python
    >>> BFS(g, 'D')
    ['D', 'B', 'C', 'E', 'A', 'F', 'G', 'H']
    >>> BFS(g, 'G')
    ['G', 'E', 'F', 'H', 'B', 'D', 'A', 'C']
    ```
    

## 4.1.3 Application du BFS : recherche du plus court chemin

L'algorithme BFS découvre les sommets «par cercles concentriques» autour du point de départ (ainsi que le montre la structure de la file d'attente). On découvre d'abord tous les sommets à la distance 1 du point de départ, puis à la distance 2, puis 3, etc.

Un sommet situé à la distance 5 sera découvert en tant que voisin d'un sommet à la distance 4, qui lui-même aura été découvert grâce à un sommet à la distance 3, qui lui-même...

On comprend donc que si on arrive à se souvenir du sommet «parent» de chaque sommet (celui qui lui a permis d'être découvert), on pourra alors reconstituer un chemin permettant de remonter au point de départ.

Nous allons pour cela nous servir d'une structure de dictionnaire pour associer à chaque sommet son sommet-parent.

Il faudra ensuite une fonction pour recréer le chemin.

### **Pourquoi le plus court chemin ?**

- Comment est-on sûr qu'un chemin va être trouvé entre deux sommets A et B ?

Si le graphe est connexe, tout parcours BFS au départ de A va parcourir l'intégralité du graphe, et donc passera par B à un moment. Un chemin sera donc forcément trouvé entre A et B.

- Comment est-on sûr que ce chemin trouvé est **le plus court** ?

La découverte des sommets par cercles concentriques entre A et B nous assure qu'on ne peut pas rater le point B : s'il est à la distance `k` de A, il sera forcément visité puisque tous les sommets à la distance `k` vont passer par la liste d'attente, après les sommets de distance `k-1` et avant les sommets de distance `k+1`.

Lorsqu'on remontera de B vers A en passant par les sommets parents successifs, il ne peut y avoir qu'un seul sommet par «couche» : le chemin sera donc exactement de longueur `k`, il sera donc minimal.

```python
def recherche_chemin(g, depart, arrivee):
    '''
    Parcours en largeur du graphe g en partant du sommet depart,
    qui s'arrête dès que le sommet arrivee est atteint.
    Renvoie alors le chemin du depart vers arrivee.
    '''
    traites = []
    decouverts = [depart]
    en_attente = [depart]
    parent = {}
    while en_attente != [] :
        sommet = en_attente.pop(0)
        voisins = g.voisins(sommet)
        for voisin in voisins:
            if voisin not in decouverts:
                decouverts.append(voisin)
                en_attente.append(voisin)
                parent[voisin] = sommet
                if voisin == arrivee:
                    return remonte_chemin(depart, arrivee, parent)
        traites.append(sommet)
    return "non trouvé"  

def remonte_chemin(depart, arrivee, parent):
    sommet = arrivee
    chemin = arrivee
    while sommet != depart:
        sommet = parent[sommet]
        chemin = sommet + chemin
    return chemin
```

---

### **Exercice 5**

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/BFS_ex1.png)

Tester le code précédent pour trouver le plus court chemin entre A et G, entre H et C, entre B et G...

# 4.2 Le parcours en profondeur (DFS, Depth First Search)

## **4.2.1 Parcours DFS récursif**

Le parcours en profondeur est un parcours où on va aller «le plus loin possible» sans se préoccuper des autres voisins non visités : on va visiter le premier de ses voisins non traités, qui va faire de même, etc. Lorsqu'il n'y a plus de voisin, on revient en arrière pour aller voir le dernier voisin non visité.

Dans un labyrinthe, ce parcours s'explique très bien : on prend tous les chemins sur la droite jusqu'à rencontrer un mur, auquel cas on revient au dernier embranchement et on prend un autre chemin, puis on repart à droite, etc.

C'est un parcours qui s'écrit naturellement de manière **récursive** :

**Parcours en profondeur - DFS**  

```python
def DFSrec(g, traites, actuel):
    traites.append(actuel)
    for voisin in g.voisins(actuel):
        if voisin not in traites:
            DFSrec(g, traites, voisin)
    return traites
```

---

### **Exercice 6**

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/BFS_ex1.png)

**Q1.** Donner (de tête) le parcours DFS de ce graphe en partant de A.

Rappel : les voisins sont donnés par ordre alphabétique. Le premier voisin de A est donc B.

**Q2.** Vérifier avec le code précédent.

- **Correction**
    
    ```python
    class Graphe:
        def __init__(self, liste_sommets):
            self.liste_sommets = liste_sommets
            self.adjacents = {sommet : [] for sommet in liste_sommets}
    
        def ajoute_arete(self, sommetA, sommetB):
            self.adjacents[sommetA].append(sommetB)
            self.adjacents[sommetB].append(sommetA)
    
        def voisins(self, sommet):
            return self.adjacents[sommet]
    
        def sont_voisins(self, sommetA, sommetB):
            return sommetB in self.adjacents[sommetA]
    
    g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    g.ajoute_arete('A', 'B')
    g.ajoute_arete('A', 'C')
    g.ajoute_arete('B', 'D')
    g.ajoute_arete('D', 'C')
    g.ajoute_arete('B', 'E')
    g.ajoute_arete('D', 'E')
    g.ajoute_arete('E', 'F')
    g.ajoute_arete('E', 'G')
    g.ajoute_arete('F', 'G')
    g.ajoute_arete('G', 'H')
    
    def DFSrec(g, traites, actuel):
        traites.append(actuel)
        for voisin in g.voisins(actuel):
            if voisin not in traites:
                DFSrec(g, traites, voisin)
        return traites
    ```
    
    ---
    
    ```python
    >>> DFSrec(g, [], 'A')
    ['A', 'B', 'D', 'C', 'E', 'F', 'G', 'H']
    ```
    

**Q3.** Reprendre les questions précédentes en changeant le sommet de départ.

## **4.2.2 Parcours DFS itératif**

Il «suffit» de remplacer la file du parcours BFS par une **pile**. Ainsi, on partira visiter le voisin tout juste ajouté à la *file d'attente* (qui porte maintenant très mal son nom, puisque c'est devenu une pile).

### **Parcours en profondeur itératif - DFS**

```python
def DFS_iteratif(graphe, start):
    traites = []
    en_attente = [start]
    while en_attente != []:
        actuel = en_attente.pop()
        if actuel not in traites:
            voisins = g.voisins(actuel)[::-1]
            for voisin in voisins:
                if voisin not in traites:
                    en_attente.append(voisin)
            traites.append(actuel)
    return traites
```

---

### **Remarques :**

- À la ligne 7, on inverse l'ordre des voisins (avec l'astuce `[::-1]`) pour que ce code renvoie le même parcours que le parcours récursif (sinon c'est le dernier voisin ajouté qui sera dépilé). Cela n'est pas obligatoire : il n'y a pas «un seul» parcours DFS (tout comme il n'y a pas qu'un seul BFS). Ce qui les caractérise est la **méthode de découverte**, plus que l'implémentation proprement dite.
- Contrairement au BFS, il est possible d'empiler un sommet déjà découvert (on vérifie juste qu'il n'ait pas déjà été traité). Vous pouvez vous en apercevoir en écrivant l'état de la pile lors du parcours DFS itératif du graphe de l'exercice 6.