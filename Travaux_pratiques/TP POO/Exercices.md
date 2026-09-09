# Exercices

# **Exercice 1**

**Q1.** Écrire une classe `Eleve` qui contiendra les attributs `nom`, `classe` et `note`.

- **Correction**
    
    ```python
    class Eleve:
        def __init__(self, nom, classe, note):
            self.nom = nom
            self.classe = classe
            self.note = note
    ```
    
    ---
    

**Q2.** Instancier trois élèves de cette classe.

- **Correction**
    
    ```python
    riri = Eleve('Henri', 'TG2', 12)
    fifi = Eleve('Philippe', 'TG6', 15)
    loulou = Eleve('Louis', 'TG1', 8)
    ```
    

**Q3.** Écrire une fonction `compare` qui prend en paramètres deux élèves `eleve1` et `eleve2` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).

- **Correction**
    
    ```python
    class Eleve:
        def __init__(self, nom, classe, note):
            self.nom = nom
            self.classe = classe
            self.note = note
    
    def compare(eleve1, eleve2):
        if eleve1.note > eleve2.note:
            return eleve1.nom
        else:
            return eleve2.nom
    ```
    

**Exemple d'utilisation de la classe**

```python
>>> riri = Eleve("Henri", "TG2", 12)
>>> fifi = Eleve("Philippe", "TG6", 15)
>>> loulou = Eleve("Louis", "TG1", 8)
>>> compare(riri, fifi)
'Philippe'
```

# **Exercice 2**

Écrire une classe `TriangleRect` qui contiendra les attributs `cote1`, `cote2` et `hypotenuse`.

La méthode constructeur ne prendra en paramètres que `cote1` et `cote2`, l'attribut `hypotenuse` se calculera automatiquement.

**Exemple d'utilisation de la classe**

```python
>>> mon_triangle = TriangleRect(3,4)
>>> mon_triangle.cote1
3
>>> mon_triangle.cote2
4
>>> mon_triangle.hypotenuse
5.0
```

- **Correction**
    
    ```python
    classTriangleRect:
        def__init__(self, c1, c2):
            self.cote1 = c1
            self.cote2 = c2
            self.hypotenuse = (self.cote1**2 + self.cote2**2)**0.5
    ```
    
    ---
    

# **Exercice 3**

**Q1.** Écrire une classe `Chrono` qui contiendra les attributs `heures`, `minutes` et `secondes`.

**Q2.** Doter la classe d'une méthode `affiche` qui affichera le temps `t`.

**Q3.** Doter la classe d'une méthode `avance` qui prend en paramètre un temps `s` en secondes et qui fait avancer le temps `t` de `s` secondes.

**Exemple d'utilisation de la classe**

```python
>>> t = Chrono(17, 25, 38)
>>> t.heures
17
>>> t.minutes
25
>>> t.secondes
38
>>> t.affiche()
'Il est 17 heures, 25 minutes et 38 secondes'
>>> t.avance(27)
>>> t.affiche()
'Il est 17 heures, 26 minutes et 5 secondes'
```

- **Aide**
    
    On pourra utiliser les opérateurs :
    
    - `%`, qui calcule le reste d'une division euclidienne.
    - `//`, qui calcule le quotient d'une division euclidienne.

# **Exercice 5**

Créer une classe `CompteBancaire` dont la méthode constructeur recevra en paramètres :

- un attribut `titulaire` stockant le nom du propriétaire.
- un attribut `solde` contenant le solde disponible sur le compte.

Cette classe contiendra deux méthodes `retrait` et `depot` qui permettront de retirer ou de déposer de l'argent sur le compte.

#### **Exemple d'utilisation de la classe**

```python
>>> compteGL = CompteBancaire("G.Lassus", 1000)
>>> compteGL.retrait(50)
Vous avez retiré 50 euros
Solde actuel du compte : 950 euros
>>> compteGL.retrait(40000)
Retrait impossible
>>> compteGL.depot(10000000)
Vous avez déposé 10000000 euros
Solde actuel du compte : 10000950 euros
```

# **Exercice 6**

[Exercice 14.2](https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2024/#exercice-142) de la BNS 2024.

# **Exercice 7**

Exercice 2 Partie A du sujet [Métropole Septembre 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Metropole_Septembre.pdf)

# **Exercice 8**

Exercice 5 du sujet [Métropole J1 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Metropole_J1.pdf)

# **Exercice 9**

Exercice 2 du sujet [La Réunion J1 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_LeReunion_J1.pdf)

# **Exercice 10**

Exercice 3 (partie A et B) du [sujet Métropole J1 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ1ME.pdf)

# **Exercice 11**

Exercice 1 du [sujet Centres Étrangers J2 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ2G1.pdf)

```python
classChemin:

    def __init__(self, itineraire):
        self.itineraire = itineraire
        longueur, largeur = 0, 0
        for direction in self.itineraire:
            if direction == "D":
                longueur = longueur + 1
            if direction == "B":
                largeur = largeur +1
        self.longueur = longueur
        self.largeur = largeur
        self.grille = [['.' for i in range(longueur+1)] for j in range(largeur+1)]

    def remplir_grille(self):
        i, j = 0, 0
        self.grille[0][0] = 'S'
        for direction in ...:
            if direction == 'D':
                ... = ...
            elif direction == 'B':
                ... = ...
            self.grille[i][j] = '*'
        self.grille[self.largeur][self.longueur] = 'E'
```

---

Pour la question 6 :

```python
from random import choice

def itineraire_aleatoire(m, n):
    itineraire = ''
    i, j = 0, 0
    while i != m and j != n:
        ...
        ...
        ...
        ...
        ...
        ...
    if i == m:
        itineraire = itineraire + 'D'*(n-j)
    if j == n:
        itineraire = itineraire + 'B'*(m-i)
    return itineraire
```

---

# **Exercice 12**

Exercice 2 du [sujet Amérique du Nord J1 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25_NSIJ1AN1.pdf)

```python
class Colis:
    def __init__(self, id, poids, adresse):
        self.id = id
        self.poids = poids
        self.adresse = adresse
        self.etat = 'préparé'

colisA = Colis('AC12', 5.0, '20 rue de la paix 57000 Metz')
colisB = Colis('AF34', 10.25, '32 rue du centre 57000 Metz')
```

```python
def ajouter_colis(liste, colis):
    # ajoute le colis à la fin de la liste
    liste.append(colis)
```

```python
def poids_total(liste):
    total = ...
    for c in liste :
        total = ...
    return total
```

```python
def tri_decroissant(liste):
    n = len(liste)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if liste[j].poids > liste[min_pos].poids:
                min_pos = j
        # Échanger les éléments
        temp = liste[i]
        liste[i] = liste[min_pos]
        liste[min_pos] = temp
    return liste
```

```python
def chargement_glouton(liste, rang, capacite):
    if rang == len(liste):
        return ...
    elif liste[rang].poids <= ...:
        return ... + chargement_glouton(liste, ..., ...)
    else:
        return chargement_glouton(liste, ..., ...)
```

Pour faire des tests :

```python
colisA = Colis('AC12', 5.0, '20 rue de la paix 57000 Metz')
colisB = Colis('AF34', 10.25, '32 rue du centre 57000 Metz')
colisC = Colis('AZ14', 12, '33 rue des 3 bornes 75011 Paris')
colisD = Colis('AB56', 15, '18 rue des feuillantines 75005 Paris')
colisE = Colis('BF22', 17, '49 avenue Alsace-Lorraine 38000 Grenoble')
colisF = Colis('KV12', 11, '155 rue du Molinel 59000 Lille')

lst = []
ajouter_colis(lst, colisA)
ajouter_colis(lst, colisB)
ajouter_colis(lst, colisC)
ajouter_colis(lst, colisD)
ajouter_colis(lst, colisE)
ajouter_colis(lst, colisF)

lst = tri_decroissant(lst)
```

# **Exercice 13**

Exercice 3 du [sujet Asie J1 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ1JA1.pdf)

```python
class Personne():
    def __init__(self, num, n , p , a_naiss, a_entree):
        self.num_badge = num
        self.nom = n
        self.prenom = p
        self.annee_naissance = a_naiss
        self.annee_entree = a_entree
```

```python
class Personnel:
    def __init__(self):
        self.liste = []
```

```python
def donne_nom(..., num):
    for elt in self.liste:
        if ... == num:
            return ...
    return ...
```

# **Exercice 14**

Exercice 3 du [sujet Métropole J1 2023](https://glassus.github.io/terminale_nsi/T6_Annales/data/2023/2023_Metropole_J1.pdf)

```python
class Region:
'''Modélise une région d'un pays sur une carte.'''
    def __init__(self, nom_region):
'''
        initialise une région
        : param nom_region (str) le nom de la région
        '''
        self.nom = nom_region
        # tableau des régions voisines, vide au départ
        self.tab_voisines = []
        # tableau des couleurs disponibles pour colorier la région
        self.tab_couleurs_disponibles = ['rouge', 'vert', 'bleu', 'jaune', 'orange', 'marron']
        # couleur attribuée à la région et non encore choisie au départ
        self.couleur_attribuee = None
```

# **Exercice 15**

Exercice 3 du [sujet Amérique du Nord J2 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ2AN1.pdf)

- **Blockchain**
    
    ![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.1_Programmation_Orientee_Objet/data/blockchain.jpg)
    

```python
class Transaction:
    def __init__(self, expediteur, destinataire, montant):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant

class Bloc:
    def __init__(self, liste_transactions, bloc_precedent):
        self.liste_transactions = liste_transactions
        self.bloc_precedent = bloc_precedent # de type Bloc

class Blockchain:
    def __init__(self):
        self.tete = self.creer_bloc_0()

    def creer_bloc_0(self):
'''
        Crée le premier bloc qui distribue 100 nsicoin à tous les
        utilisateurs (un pseudo-utilisateur Genesis est utilisé comme
        expéditeur)
        '''
        liste_transactions = [
        Transaction('Genesis', 'Alice', 100),
        Transaction('Genesis', 'Bob', 100),
        Transaction('Genesis', 'Charlie', 100)
        ]
        return Bloc(liste_transactions, None)
```

À la question 9, le code à utiliser est celui-ci (erreur d'énoncé à la ligne 6):

```python
def calculer_solde(self, utilisateur):
    if self.bloc_precedent is None:
        solde = 0
    else:
        solde = ...
        for transaction in self.liste_transactions:
            if ... == utilisateur:
                solde = solde - ...
            elif ...:
                ...
        return solde
```

---

# **Exercice 16**

Exercice 1 du [sujet Centre Étrangers J1 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25_NSIJ1G11.pdf)

```python
class Balise:
    def __init__(self, numero, couleurs):
        self.num_balise = numero
        self.couleurs_balise = couleurs
        self.voisines = []
        self.visitee = False

    def methode1(self):
        return [b.num_balise for b in self.voisines]

    def methode2(self, couleur):
        self.couleurs_balise = [c for c in self.couleurs_balise if c != couleur]

    def methode3(self, couleur):
        self.couleurs_balise.append(couleur)

balise1 = Balise(1, ['vert', 'rouge', 'noir'])
balise2 = Balise(2, ['rouge'])
balise3 = Balise(3, ['vert', 'noir'])
balise4 = Balise(4, ['rouge', 'noir'])
balise5 = Balise(5, ['noir'])
balise6 = Balise(6, ['vert', 'rouge', 'noir'])
balise7 = Balise(7, ['vert'])
balise8 = Balise(8, ['rouge'])
balise9 = Balise(9, ['rouge'])
balise10 = Balise(10, ['vert', 'noir'])
balise11 = Balise(11, ['rouge'])
balise12 = ...

balise1.voisines = [balise2, balise3]
balise2.voisines = [balise1, balise4]
balise3.voisines = [balise1, balise6]
balise4.voisines = [balise2, balise5, balise6]
balise5.voisines = [balise4, balise10]
balise6.voisines = [balise3, balise4, balise7, balise11]
balise7.voisines = [balise6, balise10]
balise8.voisines = [balise9]
...
balise10.voisines = [balise5, balise7, balise12]
balise11.voisines = [balise6, balise9]
balise12.voisines = [balise9, balise10]
```

---

```python
def itineraire(balise_debut, balise_fin, couleur):
    assert couleur in balise_debut.couleurs_balise
    assert couleur in balise_fin.couleurs_balise
    balise = balise_debut
    chemin = [balise]
    while balise.num_balise != ...:
        for b in balise.voisines:
            if (couleur in ...) and (b not in ...):
                balise = ...
                chemin.append(balise)
    return [b.num_balise for b in chemin]
```

```python
def mystere(balise):
    meilleure_balise = None
    mini = -1
    for b, t in balise.voisines:
        if (b.visitee == False) and (mini == -1 or t < mini):
            meilleure_balise, mini = b, t
    return meilleure_balise
```

```python
def itineraire_trail(balise_debut, balise_fin):
    balise_debut.visitee = True
    balise = balise_debut
    chemin = [balise]
    while balise_fin not in chemin:
        prochaine = ...
        if prochaine != None:
            ...
        else:
            return None
    return [b.num_balise for b in chemin]
```

---