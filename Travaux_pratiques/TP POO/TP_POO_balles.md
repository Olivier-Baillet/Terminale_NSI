# TP : balles rebondissantes

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.1_Programmation_Orientee_Objet/data/balles1.png)

## 1. Prise en main de Pygame

```python
import pygame,sys
import time
from pygame.locals import *

LARGEUR = 640
HAUTEUR = 480
RAYON = 20

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])

x = 300
y = 200
dx = 4
dy = -3
couleur = (45, 170, 250)

while True:
    fenetre.fill([0, 0, 0])
    pygame.draw.circle(fenetre, couleur, (x, y), RAYON)

    x += dx
    y += dy

    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    time.sleep(0.1)
```

---

### 1.1 Rajout d'un rebond sur les parois

Modifiez le code précédent afin que la balle rebondisse sur chaque paroi (il suffit de modifier intelligemment les variables de vitesse `dx` et `dy`).


    ---
    

### 1.2 Rajout d'une deuxième balle

Attention au nommage des variables...


    ---
    

### 1.3 Gestion de la collision entre les deux balles

**Q1.** À l'aide d'un schéma (papier-crayon !), mettez en évidence le test devant être réalisé pour détecter une collision.

- **indice**
    
    ![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.1_Programmation_Orientee_Objet/data/TP_dist.png)
    

**Q2.** Implémentez ce test (en créant pour cela une fonction `distance` ) et affichez "collision" en console lorsque les deux balles se touchent.


    ---
    

**Q3.** Pour donner l'illusion physique du rebond, échangez les valeurs respectives de `dx` et `dy` pour les deux balles.


    ---
    

### 1.4 Rajout d'une troisième balle et gestion du rebond avec les deux autres.

... vraiment ? Peut-on continuer comme précédemment ?

![image](https://glassus.github.io/terminale_nsi/T2_Programmation/2.1_Programmation_Orientee_Objet/data/meme_doubt.png)

## 2. La POO à la rescousse : création d'une classe Balle

### 2.1 la classe Balle

L'objectif est que la méthode constructeur dote chaque nouvelle balle de valeurs aléatoires : abscisse, ordonnée, vitesse, couleur...

- Pour l'aléatoire, on pourra utiliser `randint(a, b)` qui renvoie un nombre pseudo-aléatoire entre `a` et `b`. Il faut pour cela importer la fonction, par `from random import randint`
- Vous pouvez aussi doter votre classe `Balle` d'une méthode `dessine` (qui affiche la balle), ainsi qu'une méthode `bouge` qui la fait bouger.

Créez cette classe et instanciez une balle.


    ---
    

### 2.2 Plusieurs balles

L'idée est de stocker dans une liste `sac_a_balles` un nombre déterminé de balles...


    ---
    

### 2.3 Collision de toutes les balles

Il «suffit» , dans la méthode constructeur, de tester la collision de la balle `self` avec chacune des balles de notre `sac_a_balles`.


    ---
    

## 3. Extensions

- Vous pouvez créer des balles de couleurs identiques, sauf une. Cette balle diffusera sa couleur à toutes les balles avec qui elle rentrera en collision.
- En la supprimant de la liste `sac_a_balles`, vous pouvez faire disparaitre une balle.
- Vous pouvez créer une balle que vous déplacerez au clavier (voir [ici](https://glassus.github.io/premiere_nsi/T6_Mini-projets/05_Initiation_Pygame/) pour la gestion des déplacements)
- ...
- Ce que je ne veux pas voir :
    
    ![](https://glassus.github.io/terminale_nsi/T2_Programmation/2.1_Programmation_Orientee_Objet/data/paste.png)
