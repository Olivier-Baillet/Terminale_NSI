# Cours NSI Terminale – Les arbres (sans récursivité)

# 1️⃣ Introduction : Qu’est-ce qu’un arbre ?

Un **arbre** est une structure de données hiérarchique composée de **nœuds**.

Chaque nœud peut contenir :

- une *valeur*
- des *références* vers d’autres nœuds (appelés **enfants**)

Dans un **arbre binaire** :

➡️ chaque nœud peut avoir **0, 1 ou 2 enfants**.

---

# 2️⃣ Vocabulaire indispensable

- **Racine** : nœud de départ, sans parent
- **Parent / enfant**
- **Feuille** : nœud sans enfant
- **Profondeur** : distance à la racine
- **Hauteur** : profondeur maximale
- **Sous-arbre** : arbre inclus dans un plus grand

---

# 3️⃣ Pourquoi étudier les arbres ?

Les arbres sont partout :

- structures de fichiers (répertoires)
- pages web (DOM)
- intelligence artificielle (arbres de décision)
- bases de données (B-Tree)
- recherche efficace (ABR)

---

# 4️⃣ Représentation d’un arbre en Python (non récursif)

## 🟦 A. Représentation par dictionnéaires imbriqués

Simple, lisible, idéale au lycée :

```python
arbre = {
    "val": 10,
    "gauche": {"val": 4, "gauche": None, "droite": None},
    "droite": {"val": 15, "gauche": None, "droite": None}
}

```

## 🟩 B. Représentation par liste de nœuds (style graphe)

Chaque nœud a un identifiant :

```python
noeuds = {
    0: {"val": 10, "g": 1, "d": 2},
    1: {"val": 4, "g": None, "d": None},
    2: {"val": 15, "g": None, "d": None}
}
racine = 0

```

---

# 5️⃣ Parcours d’un arbre *sans récursivité*

Les trois parcours classiques :

- **Préfixe** : noeud → gauche → droite
- **Infixe** : gauche → noeud → droite
- **Postfixe** : gauche → droite → noeud

Normalement on les fait avec de la récursion…

➡️ **Mais on peut les faire avec une pile !**

---

# 5.1 Parcours en profondeur (DFS) avec une pile

Objectif : afficher les valeurs dans un parcours **préfixe**.

### **Algorithme (stack)**

```
On affiche le noeud visité;
On visite le fils droit si il existe.
    dépiler un nœud N
    afficher N
    empiler son enfant droit
    empiler son enfant gauche

```

 On empile d’abord le droit pour traiter le gauche en premier.

### Implémentation en Python

```python
def parcours_prefixe(racine):
    if racine is None:
        return

    pile = [racine]

    while pile:
        noeud = pile.pop()
        print(noeud["val"])

        if noeud["droite"] is not None:
            pile.append(noeud["droite"])
        if noeud["gauche"] is not None:
            pile.append(noeud["gauche"])

```

---

# 🔵 5.2 Parcours en largeur (BFS) avec une file

Utilise une **file (queue)**.

### 🚀 Algorithme :

```
Créer une file
Enfiler la racine

Tant que la file n’est pas vide :
    défiler un nœud
    afficher sa valeur
    enfiler son enfant gauche
    enfiler son enfant droit

```

### Code Python :

```python
from collections import deque

def parcours_largeur(racine):
    if racine is None:
        return

    file = deque([racine])

    while file:
        noeud = file.popleft()
        print(noeud["val"])

        if noeud["gauche"] is not None:
            file.append(noeud["gauche"])
        if noeud["droite"] is not None:
            file.append(noeud["droite"])

```

---

# 6️⃣ Arbres binaires de recherche (ABR) – sans récursivité

Un ABR vérifie :

```
valeurs < nœud < valeurs >

```

## ✔ Rechercher une valeur

```
Tant que le nœud n’est pas None :
    si valeur == nœud.val → trouvé
    si valeur < nœud.val → aller à gauche
    sinon → aller à droite

```

### Code Python :

```python
def rechercher(racine, cible):
    noeud = racine
    while noeud is not None:
        if cible == noeud["val"]:
            return True
        elif cible < noeud["val"]:
            noeud = noeud["gauche"]
        else:
            noeud = noeud["droite"]
    return False

```

---

# 7️⃣ Activité débranchée 🧩 "Parcours d'arbre"

### Objectif

Comprendre le fonctionnement des parcours **préfixe, infixe, postfixe**.

### Matériel

- Cartes "nœuds"
- Flèches "gauche"/"droite"
- Une pile (verres rouges)
- Une file (verres bleus)

### Consigne

Les élèves simulent les parcours :

- un élève = la racine
- d’autres = les nœuds enfants
- une pile (verres) pour simuler le DFS
- une file pour simuler le BFS

🎯 Très concret → idéal pour comprendre les structures internes.

---

# 8️⃣ Exercices (progressifs)

## 🔹 Exercice 1 : Représenter cet arbre en Python

(on donne un dessin)

## 🔹 Exercice 2 : Parcours en largeur (papier)

```
        8
      /   \
     3    10
    / \     \
   1  6      14

```

Écrire l'ordre de visite en largeur.

## 🔹 Exercice 3 : Parcours préfixe avec pile (papier)

## 🔹 Exercice 4 : Programmer le parcours sans récursivité

## 🔹 Exercice 5 : Rechercher dans un ABR (non récursif)

---

# 9️⃣ Mini-projet (évaluable)

👉 **Construire un ABR non récursif**

avec :

- insertion
- recherche
- parcours en largeur

Puis afficher les valeurs triées (parcours infixe non récursif via pile).

---

# 🔟 Conclusion – Ce qu’il faut retenir

✔ Un arbre = structure hiérarchique

✔ On peut tout faire **sans récursivité**

✔ Pile = parcours en profondeur

✔ File = parcours en largeur

✔ ABR → recherche très efficace

---

Si tu veux, je peux aussi te produire :

✅ une fiche élève

✅ une fiche professeur

✅ une évaluation corrigée

✅ un TP complet (avec version arcade non récursive)

Souhaites-tu l’une de ces versions ?

[**TP NSI – Arbres binaires sans récursivité**](Cours%20NSI%20Terminale%20%E2%80%93%20Les%20arbres%20(sans%20r%C3%A9cursivit%C3%A9/TP%20NSI%20%E2%80%93%20Arbres%20binaires%20sans%20r%C3%A9cursivit%C3%A9%202b59d18941358074ba44f6c95e521cdc.md)