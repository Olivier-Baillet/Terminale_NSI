# 2. Modélisations d'un graphe

Pour modéliser un graphe, il faut établir par convention une manière de donner les renseignements suivants :

- qui sont les sommets ?
- pour chaque sommet, quels sont ses voisins ? (et éventuellement quel poids porte l'arête qui les relie)

# 2.1 Représentation par matrice d'adjacence

<aside>
💡

**Principe**

- On classe les sommets (en les numérotant, ou par ordre alphabétique).
- on représente les arêtes (ou les arcs) dans une matrice, c'est-à-dire un tableau à deux dimensions où on inscrit un 1 en ligne `i` et colonne `j` si les sommets de rang `i` et de rang `j` sont **voisins** (dits aussi *adjacents*).

Ce tableau s'appelle une **matrice d'adjacence** (on aurait très bien pu l'appeler aussi *matrice de voisinage*).

</aside>

## **2.1.1 Graphe non orienté**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/matgraph_1.png)

Dans ce graphe non orienté, comme B est voisin de C, C est aussi voisin de B, ce qui signifie que l'arête qui relie B et C va donner lieu à deux "1" dans la matrice, situé de part et d'autre de la diagonale descendante (un mathématicien parlera de matrice *symétrique*).

## **2.1.2 Graphe orienté**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/matgraph_2.png)

Comme le graphe est orienté, la matrice n'est pas forcément symétrique (il faudrait que tous les liens soient réciproques pour qu'elle le soit).

## **2.1.3 Graphe pondéré**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/matgraph_3.png)

Il peut exister de la même manière des graphes pondérés **et** orientés.

## **2.1.4 Exercices**

### **Exercice 1**

Soit un ensemble d'amis connectés sur un réseau social quelconque. Voici les interactions qu'on a recensées :

- André est ami avec Béa, Charles, Estelle et Fabrice,
- Béa est amie avec André, Charles, Denise et Héloïse,
- Charles est ami avec André, Béa, Denise, Estelle, Fabrice et Gilbert,
- Denise est amie avec Béa, Charles et Estelle,
- Estelle est amie avec André, Charles et Denise,
- Fabrice est ami avec André, Charles et Gilbert,
- Gilbert est ami avec Charles et Fabrice,
- Héloïse est amie avec Béa.

**Q1.** Représenter le graphe des relations dans ce réseau social (on désignera chaque individu par l'initiale de son prénom). Il est possible de faire en sorte que les arêtes ne se croisent pas !

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/grapheRS.png)
    

**Q2.** Donner la matrice d'adjacence de ce graphe.

![image.png](2%20Mod%C3%A9lisations%20d'un%20graphe/image.png)

### **Exercice 2**

Construire les graphes correspondants aux matrices d'adjacence suivantes:

**Q1.**  $M1 = \begin{pmatrix}
0 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0
\end{pmatrix}$

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q1.png)
    

**Q2.** $M2 = \begin{pmatrix}
0 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}$

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q2.png)
    

**Q3.**  $M3 = \begin{pmatrix}
0 & 5 & 10 & 50 & 12 \\
5 & 0 & 10 & 0  & 0 \\
10 & 10 & 0 & 8 & 0 \\
50 & 0 & 8 & 0 & 100 \\
12 & 0 & 0 & 100 & 0
\end{pmatrix}$

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q3.png)
    

## **2.1.5 Implémentation Python des matrices d'adjacence**

**Matrices d'adjacence en Python**

Une matrice se représente naturellement par une liste de listes.

**Exemple:** 

$M1 = \begin{pmatrix}
0 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}$

La matrice , associée au graphe

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q1.png)

sera représentée par la variable `G` suivante :

```python
G = [[0, 1, 1, 1, 1],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 1, 0],
      [1, 0, 1, 0, 1],
      [1, 0, 0, 1, 0]]
```

<aside>
💡

**Complexité en mémoire et temps d'accès :**

- Pour un graphe à sommets, la complexité en mémoire (appelée aussi *complexité spatiale*) de la représentation matricielle est en .
- Tester si un sommet est isolé (ou connaître ses voisins) est en puisqu'il faut parcourir une ligne, mais tester si deux sommets sont adjacents (voisins) est en , c'est un simple accès au tableau.

La modélisation d'un graphe par sa matrice d'adjacence est loin d'être la seule manière de représenter un graphe : nous allons voir une autre modélisation, par **liste d'adjacence**.

</aside>

### 2.2 Représentation par listes d'adjacence

**Principe**

- On associe à chaque sommet sa liste des voisins (c'est-à-dire les sommets adjacents). On utilise pour cela un dictionnaire dont les clés sont les sommets et les valeurs les listes des voisins.
- Dans le cas d'un graphe orienté on associe à chaque sommet la liste des *successeurs* (ou bien des *prédécesseurs*, au choix).

Par exemple, le graphe

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex2_Q1.png)

sera représenté par le dictionnaire :

```python
G = {'A': ['B', 'C', 'D', 'E'],
     'B': ['A', 'C'],
     'C': ['A', 'B', 'D'],
     'D': ['A', 'C', 'E'],
     'E': ['A', 'D']
    }
```

---

<aside>
💡

**Complexité en mémoire et temps d'accès :**

- Pour un graphe à sommets et arêtes, la complexité spatiale de la représentation en liste d'adjacence est en . C'est beaucoup mieux qu'une matrice d'adjacence lorsque le graphe comporte peu d'arêtes (i.e. beaucoup de 0 dans la matrice, non stockés avec des listes).
- Tester si un sommet est isolé (ou connaître ses voisins) est en puisqu'on y accède immédiatement, mais tester si deux sommets sont adjacents (voisins) est en car il faut parcourir la liste.
</aside>

## **2.2.1 Exercices**

### **Exercice 3**

Construire les graphes correspondants aux listes d'adjacence suivantes.

**Q1.**

```python
G1 = {
'A': ['B', 'C'],
'B': ['A', 'C', 'E', 'F'],
'C': ['A', 'B', 'D'],
'D': ['C', 'E'],
'E': ['B', 'D', 'F'],
'F': ['B', 'E']
     }
```

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex3_Q1.png)
    

**Q2.**

```python
G2 = {
'A': ['B'],
'B': ['C', 'E'],
'C': ['B', 'D'],
'D': [],
'E': ['A']
     }
```

- **Correction**
    
    ![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/ex3_Q2.png)
    

# 2.3 Représentation uniquement avec des listes.

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/graphEP.png)

Ainsi qu'il est fait dans un sujet du bac, le graphe ci-dessus peut être représenté par la liste de listes suivante :

```python
adj = [[1, 2], [0, 3], [0], [1], [5], [4]]
```