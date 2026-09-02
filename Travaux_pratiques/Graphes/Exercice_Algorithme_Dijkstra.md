# Exercice : Algorithme de Dijkstra

L'algorithme de Dijkstra repose sur un parcours en largeur où l'on sélectionne parmi les sommets déjà découverts celui qui a la plus petite distance au sommet *source*.

Dans cet algorithme, on va construire un dictionnaire `distances` où:

- les clés sont les sommets du graphe;
- les valeurs sont un couple (une liste) de deux élements: la distance au sommet *source* et le sommet «père».
    
    Initialement, toutes les valeurs seront initialisés à `[inf, None]` (importer `inf` du module `math` qui permet d'avoir un nombre plus grand que tous les autres), sauf pour la clé du sommet *source* dont la valeur sera `[0, None]`.
    

On manipulera également deux listes:

- une liste `visites`, initialement vide, qui contiendra au fur et à mesure les sommets visités (c'est-à-dire finis d'être traités);
- une liste `decouverts`, qui contient initialement le sommet *source* seulement, et qui contiendra les sommets accessibles par un sommet déjà traité mais non encore visités.

On suit ensuite l'algorithme suivant:

- Tant que la liste `decouverts` n'est pas vide:
    - on sélectionne le sommet `s_min` de `decouverts` qui a la plus petite distance au sommet *source*;
    - on supprime ce sommet `s_min` de `decouverts` et on l'ajoute à `visites`.
    - pour chaque voisin `voisin` **qui n'est pas visité** de `s_min` , on actualise sa distance:
        - s'il n'est pas dans `decouvert`, on l'y ajoute et sa distance est la somme de la distance de `s_min` à la *source* et du poids de l'arête reliant `s_min` à `voisin`
        - sinon on remplace sa distance actuelle par cette somme si elle est plus petite.
        - dans les deux cas on actualise (éventuellement) le sommet père à `s_min`
- On renvoie le dictionnaire.

**Remarque:** on manipule un graphe de classe `Graphe`...

#### Algorithme de Dijkstra - à compléter

---

```python
def dijkstra(g:Graphe, source:str) -> dict:
    '''
    Détermine et renvoie le plus court chemin entre le sommet source et les
    autres sommets du graphe g.
    Renvoie un dictionnaire dont les clés sont les sommets du graphe et les
    valeurs une liste [d, p] où d est la distance la plus courte depuis le
    sommet source et p le sommet «père».
    '''
    distances = {s: [inf, None] for s in ...}
    distances[source] = ...
    visites = []
    decouverts = [source]
    while decouverts != []:
        # On détermine le sommet de la liste decouverts qui a la plus petite
        # distance au sommet source
        d_min = inf
        ...

        decouverts.remove(s_min)
        visites.append(s_min)

        for voisin in [v for v in ... if ...]:
            if ...:
                decouverts.append(voisin)
                distances[voisin] = ...
            else:
                if ... :
                    distances[voisin] = ...

    return distances
```

---

On pourra vérifier à l'aide de l'exemple sur le graphe suivant :

![image.png](Exercice%20Algorithme%20de%20Dijkstra/image.png)

```python
g = Graphe([])

g.ajoute_arete('A', 'B', 12)
g.ajoute_arete('A', 'D', 14)
g.ajoute_arete('B', 'F', 9)
g.ajoute_arete('B', 'G', 16)
g.ajoute_arete('B', 'H', 21)
g.ajoute_arete('D', 'E', 10)
g.ajoute_arete('C', 'E', 13)
g.ajoute_arete('C', 'F', 10)
g.ajoute_arete('E', 'F', 16)
g.ajoute_arete('E', 'H', 10)
g.ajoute_arete('F', 'H', 11)
g.ajoute_arete('G', 'H', 11)
```

---