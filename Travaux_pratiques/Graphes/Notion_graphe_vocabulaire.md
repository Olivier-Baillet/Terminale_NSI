# 1. Notion de graphe et vocabulaire

Le concept de graphe permet de résoudre de nombreux problèmes en mathématiques comme en informatique. C'est un outil de représentation très courant, et nous l'avons déjà rencontré à plusieurs reprises, en particulier lors de l'étude de réseaux.

## 1.1 Exemples de situations

### **1.1.1 Réseau informatique**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/22J2AS1_ex2.png)

### **1.1.2 Réseau de transport**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/carte-metro-parisien-768x890.jpg)

### **1.1.3 Réseau social**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/graphe_RS.png)

### **1.1.4 Généralisation**

Une multitude de problèmes concrets d'origines très diverses peuvent donner lieu à des modélisations par des graphes : c'est donc une structure essentielle en sciences, qui requiert un formalisme mathématique particulier que nous allons découvrir.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/graph_math.png)

L'étude de la théorie des graphes est un champ très vaste des mathématiques : nous allons surtout nous intéresser à l'implémentation en Python d'un graphe et à différents problèmes algorithmiques qui se posent dans les graphes.

## 1.2 Vocabulaire

En général, un graphe est un ensemble d'objets, appelés *sommets* ou parfois *nœuds* (*vertex* or *nodes* en anglais) reliés par des *arêtes* ou *arcs* ((*edges* en anglais)). Ce graphe peut être **non-orienté** ou **orienté** .

### **1.2.1 Graphe non-orienté**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/exemple_graphe.png)

Dans un graphe **non-orienté**, les *arêtes* peuvent être empruntées dans les deux sens, et une *chaîne* est une suite de sommets reliés par des arêtes, comme C - B - A - E par exemple. La *longueur* de cette chaîne est alors 3, soit le nombre d'arêtes.

Les sommets B et E sont *adjacents* au sommet A, ce sont les *voisins* de A.

**Exemple de graphe non-orienté** : le graphe des relations d'un individu sur Facebook est non-orienté, car si on est «ami» avec quelqu'un la réciproque est vraie.

### **1.2.2 Graphe orienté**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/exemple_graphe_oriente.png)

Dans un graphe **orienté**, les *arcs* ne peuvent être empruntés que dans le sens de la flèche, et un *chemin* est une suite de sommets reliés par des arcs, comme B → C → D → E par exemple.

Les sommets C et D sont *adjacents* au sommet B (mais pas A !), ce sont les *voisins* de B.

**Exemple de graphe orienté** : le graphe des relations d'un individu sur Instagram est orienté, car on peut «suivre» quelqu'un sans que cela soit réciproque.

### **1.2.3 Graphe pondéré**

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/exemple_graphe_pondere.png)

Un graphe est **pondéré** (ou valué) si on attribue à chaque arête une valeur numérique (la plupart du temps positive), qu'on appelle *mesure*, *poids*, *coût* ou *valuation*.

Par exemple:

- dans le protocole OSPF, on pondère les liaisons entre routeurs par le coût;
- dans un réseau routier entre plusieurs villes, on pondère par les distances.

### **1.2.4 Connexité**

Un graphe est **connexe** s'il est d'un seul tenant: c'est-à-dire si n'importe quelle paire de sommets peut toujours être reliée par une chaîne. Autrement un graphe est connexe s'il est «en un seul morceau».

Par exemple, le graphe précédent est connexe. Mais le suivant ne l'est pas: il n'existe pas de chaîne entre les sommets A et F par exemple.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.4_Graphes/data/exemple_graphe_non_connexe.png)

Il possède cependant deux **composantes connexes** : le sous-graphe composé des sommets A, B, C, D et E d'une part et le sous-graphe composé des sommets F, G et H.