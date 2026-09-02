# 3. Création d'une classe Graphe

Dans cette partie, nous ne traiterons que des graphes **non-orientés**.

# 3.1 Interface souhaitée

Nous voulons que le graphe

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q1.png)

puisse être créé grâce aux instructions suivantes :

```python
g = Graphe(['A', 'B', 'C', 'D', 'E'])
g.ajoute_arete('A', 'B')
g.ajoute_arete('A', 'C')
g.ajoute_arete('A', 'D')
g.ajoute_arete('A', 'E')
g.ajoute_arete('B', 'C')
g.ajoute_arete('C', 'D')
g.ajoute_arete('D', 'E')
```

Nous souhaitons aussi pouvoir tester si deux sommets sont voisins avec la méthode `sont_voisins` :

```python
>>> g.sont_voisins('E', 'A')
True
>>> g.sont_voisins('E', 'B')
False
```

Enfin, nous voulons pouvoir obtenir facilement la liste de tous les voisins d'un sommet avec la méthode `voisins`:

```python
>>> g.voisins('C')
['A', 'B', 'D']
```

# 3.2 Conseils d'implémentation

L'objet de type `Graphe` aura comme attributs :

- une liste `liste_sommets` (donnée en paramètre dans la liste `liste_sommets`)
- un dictionnaire `adjacents`, où chaque sommet se verra attribuer une liste vide `[]`.

# 3.3 Implémentation

**Implémentation d'une classe `Graphe`**  

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
```

### **Remarques**

- Pour un graphe pondéré, on associera un dictionnaire (d'associations `voisin: valuation`).
- Pour un graphe à sommets et arêtes, la complexité spatiale (place en mémoire) est en $O(n)$. C'est beaucoup mieux qu'une matrice d'adjacence lorsque le graphe comporte peu d'arêtes (i.e. beaucoup de 0 dans la matrice, non stockés avec des listes).
- Tester si un sommet est isolé (ou connaître ses voisins) est en puisqu'on y accède immédiatement, mais tester si deux sommets sont adjacents (voisins) est en car il faut parcourir la liste.