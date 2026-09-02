# la Py rinthe

# Génération d'un labyrinthe

Dans ce problème, on considèrera qu'un labyrinthe est composé initialement d'une grille de cellules possédant chacune quatre murs. La cellule en haut à gauche est de coordonnées $(0,0)$.

![](https://cgouygou.github.io/TNSI/T03_Algorithmique/images/TP_maze1.png)

Pour créer un labyrinthe à partir de cette grille, on va utiliser la méthode *diviser pour régner* en appliquant récursivement une méthode `creer_labyrinthe` sur des sous-grilles en coupant la grille en deux puis en reliant les deux sous-labyrinthes en créant un passage entre eux.

![](https://cgouygou.github.io/TNSI/T03_Algorithmique/images/TP_maze2.png)

## **Algorithme de génération**

Plus précisément, voici l'algorithme à utiliser:

```python
creer_labyrinthe(i, j, di, dj):
    ''' génère un labyrinthe de dimension (di, dj) à partir de la case (i, j) en haut à gauche '''
    Si di = 1 ou dj = 1:
        enlever tous les murs reliant les cases situées sur la ligne droite entre (i, j) et (i+di−1, j+dj−1)
    Sinon
        Si di >= dj:
            tirer au hasard c entre 1 et di−1
            appeler creer_labyrinthe(i, j, c, dj)
            appeler creer_labyrinthe(i+c, j, di−c, dj).
        Sinon
            tirer au hasard c entre 1 et dj−1
            appeler creer_labyrinthe(i, j, di, c)
            creer_labyrinthe(i, j+c, di, dj−c).
        Enlever un mur aléatoirement entre les deux sous-labyrinthes créés.
```

## **Partie 1: Mise en place**

On modélise le labyrinthe à l'aide de deux classes:

- une classe `Cellule` qui contient un unique attribut `murs` de type `dict` dont les clés sont `'N'`, `'E'`, `'S'` et `'O'` et dont les valeurs sont des booléens;
- une classe `Labyrinthe` qui contient un unique attribut `grille` de type `list` qui contient des cellules et dont il faut compléter la méthode `construire_grille`.

```python
class Cellule:
    def __init__(self, mur_nord, mur_est, mur_sud, mur_ouest):
        self.murs = {'N':mur_nord, 'E':mur_est, 'S':mur_sud, 'O':mur_ouest}

class Labyrinthe:
    def __init__(self, hauteur, largeur):
        self.grille = self.construire_grille(hauteur, largeur)

    def construire_grille(self, h, l):
        grille = 
        return grille
```

---

Pour contrôler notre travail, il faut un outil graphique pour dessiner les labyrinthes. On utilisera naturellement le module `pygame`.

<aside>
💡

Modèle à utiliser et à compléter au fur et à mesure

```python
import pygame
from pygame.locals import *

## Classes

## Constantes
hauteur_laby, largeur_laby, cote_cellule = 10, 10, 10
taille_ecran = (largeur_laby*cote_cellule, hauteur_laby*cote_cellule)

## Instanciation d'un labyrinthe et génération

## Initialisation de Pygame
pygame.init()

## Écran
screen = pygame.display.set_mode(taille_ecran)
screen.fill([255, 255, 255])
pygame.display.set_caption("Génération d'un labyrinthe")

## Boucle des événements

# affichage du labyrinthe

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()

## Fermeture de la fenêtre
pygame.quit()
```

</aside>

---

## **Partie 2: Affichage**

Pour chaque cellule de la grille du labyrinthe, il faut tracer un segment pour chaque mur existant (valeur `True` pour les clés du dictionnaire).

Pour passer des coordonnées  d'une cellule dans la grille aux coordonnées de dessin dans la fenêtre `pygame`, il faut multiplier par la longueur choisie pour le côté des cellules (nommée `cote_cellule` dans le code précédent).

L'indice de ligne `i`correspond aux ordonnées de la fenêtre de dessin et l'indice de colonne `j`aux abscisses...

Par exemple pour tracer le mur nord d'une cellule de coordonnées  dans la grille, il faut tracer un segment entre les points de coordonnées `[cote_cellule*j, cote_cellule*i]` et `[cote_cellule*(j+1), cote_cellule*i]`.

Compléter la méthode `afficher` (de `Labyrinthe`):

```python
def afficher(self, c):
    '''
    affiche le labyrinthe, avec c qui désigne la longueur du côté d'une cellule
    '''
    for i in range(...):
        for j in range(...):
            if self.grille[i][j].murs[...]:
                pygame.draw.line(screen, [0, 0, 0], [..., ...], [..., ...], 2)
            ...
```

---

## **Partie 3: création d'un passage**

Il s'agit de passer les valeurs à `False` pour les murs correspondant au passage entre deux cellules. Tout d'abord il faut repérer si le passage est horizontal ou vertical...

Compléter la méthode `creer_passsage` (de `Labyrinthe`) :

```python
def creer_passage(self, i1, j1, i2, j2):
    '''
    crée une ouverture entre les cellules d'adresses (i1, j1) et (i2, j2)
    '''
    if ... : #ouverture horizontale
        if ... :
            self.grille[i1][j1].murs['E'] = False
            self.grille[i2][j2].murs['O'] = False
        else:
            ...
    else:
        ...
```

---

## **Partie 4: création du labyrinthe**

Utiliser l'algorithme établi en début d'activité pour écrire la méthode `creer_labyrinthe`.

```python
def creer_labyrinthe(self, i, j, di, dj):
    '''
    générère un labyrinthe de dimension (di, dj) à partir de la case (i, j) en haut à gauche.
    '''
```

---

# Résultats

```python
import pygame
from pygame.locals import *
import random

# -----------------------------
# Classe Cellule
# -----------------------------
class Cellule:
    def __init__(self, mur_nord=True, mur_est=True, mur_sud=True, mur_ouest=True):
        self.murs = {'N': mur_nord, 'E': mur_est, 'S': mur_sud, 'O': mur_ouest}

# -----------------------------
# Classe Labyrinthe
# -----------------------------
class Labyrinthe:

    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.grille = self.construire_grille(hauteur, largeur)

    # construction de la grille initiale (tous les murs)
    def construire_grille(self, h, l):
        grille = []
        for i in range(h):
            ligne = []
            for j in range(l):
                ligne.append(Cellule(True, True, True, True))
            grille.append(ligne)
        return grille

    # ---------------------------------
    # affichage graphique
    # ---------------------------------
    def afficher(self, c):
        for i in range(self.hauteur):
            for j in range(self.largeur):

                cellule = self.grille[i][j]

                # mur nord
                if cellule.murs['N']:
                    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        (c*j, c*i),
                        (c*(j+1), c*i),
                        2
                    )

                # mur est
                if cellule.murs['E']:
                    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        (c*(j+1), c*i),
                        (c*(j+1), c*(i+1)),
                        2
                    )

                # mur sud
                if cellule.murs['S']:
                    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        (c*j, c*(i+1)),
                        (c*(j+1), c*(i+1)),
                        2
                    )

                # mur ouest
                if cellule.murs['O']:
                    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        (c*j, c*i),
                        (c*j, c*(i+1)),
                        2
                    )

    # ---------------------------------
    # création d'un passage
    # ---------------------------------
    def creer_passage(self, i1, j1, i2, j2):

        # passage horizontal
        if i1 == i2:
            if j1 < j2:
                self.grille[i1][j1].murs['E'] = False
                self.grille[i2][j2].murs['O'] = False
            else:
                self.grille[i1][j1].murs['O'] = False
                self.grille[i2][j2].murs['E'] = False

        # passage vertical
        else:
            if i1 < i2:
                self.grille[i1][j1].murs['S'] = False
                self.grille[i2][j2].murs['N'] = False
            else:
                self.grille[i1][j1].murs['N'] = False
                self.grille[i2][j2].murs['S'] = False

    # ---------------------------------
    # génération récursive
    # ---------------------------------
    def creer_labyrinthe(self, i, j, di, dj):

        # cas de base : ligne ou colonne
        if di == 1:
            for k in range(dj - 1):
                self.creer_passage(i, j+k, i, j+k+1)
            return

        if dj == 1:
            for k in range(di - 1):
                self.creer_passage(i+k, j, i+k+1, j)
            return

        # division verticale
        if di >= dj:

            c = random.randint(1, di-1)

            self.creer_labyrinthe(i, j, c, dj)
            self.creer_labyrinthe(i+c, j, di-c, dj)

            passage = random.randint(0, dj-1)
            self.creer_passage(i+c-1, j+passage, i+c, j+passage)

        # division horizontale
        else:

            c = random.randint(1, dj-1)

            self.creer_labyrinthe(i, j, di, c)
            self.creer_labyrinthe(i, j+c, di, dj-c)

            passage = random.randint(0, di-1)
            self.creer_passage(i+passage, j+c-1, i+passage, j+c)

# -----------------------------
# Constantes
# -----------------------------
hauteur_laby = 20
largeur_laby = 20
cote_cellule = 20

taille_ecran = (
    largeur_laby * cote_cellule,
    hauteur_laby * cote_cellule
)

# -----------------------------
# Instanciation d'un labyrinthe et génération
# -----------------------------
laby = Labyrinthe(hauteur_laby, largeur_laby)
laby.creer_labyrinthe(0, 0, hauteur_laby, largeur_laby)

# -----------------------------
# Initialisation pygame
# -----------------------------
pygame.init()

screen = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Génération d'un labyrinthe")
screen.fill((255, 255, 255))

laby.afficher(cote_cellule)

# -----------------------------
# Boucle principale
# -----------------------------
continuer = True

while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()

pygame.quit()
```