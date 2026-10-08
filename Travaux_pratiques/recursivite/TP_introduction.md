# TP Turtle

## **Exercice 1 : Familiariser vous avec Turtle**

```python
from turtle import *

reset() # effacer le dessin
forward(200) # déplace la tortue vers l'avant de 20 pixel
left(90) # tourne la tortue vers la gauche de 90 degrée
color('blue') # change la couleur du trait en bleue
width(3) # change l'épaiseur du trait à 3

#Pour garder la fenêtre ouverte on utilise une boucle infinie
continuer = True
while(continuer):
	mouvement = input("Quel mouvement ?\n")
	if(mouvement == "carre"):
		carre()

	if(mouvement == "stop"):
		continuer = False
	if(mouvement == "reset"):
		clearscreen()
		home()
```

Plus de commande et de description sont disponibles sur la [documentation officielle de Turtle](https://docs.python.org/fr/3/library/turtle.html).

## **Exercice 2 : Des dessins plus concrets**

Après avoir joué avec Turtle commencez, vous pouvez essayer de dessiner des formes géométriques simples :

- [ ]  Carré
- [ ]  Triangle
- [ ]  Hexagone
- [ ]  Pentagone
- [ ]  Étoile
- [ ]  Sablier
- [ ]  Maison
- [ ]  Grande ourse (constellation)

*(Il est inutile de réaliser toutes les formes. Je vous conseille de faire Carré, Triangle et Étoiles (utiles pour la suite) et une ou deux que vous apprécierez faire.)*

<aside markdown="1">


💡 **Astuce**
Essayer de créer une nouvelle fonction à chaque fois pour garder une trace de ce que vous avez fait. Ainsi il suffit d’appeler ou pas la fonction pour dessiner.

</aside>

Vous pouvez même utiliser des arguments pour gérer la taille.

```python
def carre(taille):
    forward(taille)
    left(90)
    #...
```

## **Exercice 3 : Des frises triangulaires**

### **Frise triangulaire simple**

Réaliser une frise comme celle-ci :

Frise simple à réaliser

![](https://www.penning.fr/materials/SNT/Turtle/frise_trig_simple.drawio.svg)

### **Frise triangulaire alterné**

Réaliser la frise suivante :

Frise triangulaire alternée

![](https://www.penning.fr/materials/SNT/Turtle/frise_trig_alt.drawio.svg)

### **Frise triangulaire grandissante**

Réaliser la frise (potentiellement infinie) suivante :

Frise grandissante triangulaire

![](https://www.penning.fr/materials/SNT/Turtle/frise_trig_grand.drawio.svg)

## **Exercice 4 :** Dessiner plusieurs carrés

Proposez une fonction `cinq_carres()` qui dessine cinq carrés emboîtés ayant comme
sommet commun la position initiale de la tortue.
Les longueurs des carrés sont comprises entre 10 à 50 (inclus).
Les longueurs de chacun des carrés varient de 10 en 10.

![image.png](Turtle/image.png)

Vous pouvez également proposer une variante `vingt_carres()` qui dessine cinquante carrés de longueurs comprises entre 10 et 200 inclus.
C’est plus joli, mais il est plus difficile de vérifier qu’il y a bien 20 carrés dessinés.

## **Exercice 5 :** Dessiner des polygones

Proposez une fonction pour dessiner un polygone régulier. Cette procédure acceptera un paramètre entier indiquant le nombre de côtés n, et un paramètre correspondant à la longueur l de la figure à tracer.
Par exemple

```python
dessine_un_polygone(3,100) 	 	 
```

…produira le dessin suivant:

![image.png](Turtle/image%201.png)

## **Exercice 6 : Des frises carrées**

### **Frise carrée simple**

Réaliser la frise suivante :

Frise carrée simple

![](https://www.penning.fr/materials/SNT/Turtle/frise_carre_simple.drawio.svg)

### **Frise carrée alternante**

Réaliser la frise suivante :

Frise carrée alternante

![](https://www.penning.fr/materials/SNT/Turtle/frise_carre_alt.drawio.svg)

## **Exercice 7 : Frise d’étoile**

### **Frise d’étoile simple**

Réaliser la frise suivante :

Frise d’étoile simple

![](https://www.penning.fr/materials/SNT/Turtle/frise_et_simple.drawio.svg)

### **Frise d’étoile alternante**

Réaliser la frise suivante :

Frise d’étoile alternante

![](https://www.penning.fr/materials/SNT/Turtle/frise_et_alt.drawio.svg)
