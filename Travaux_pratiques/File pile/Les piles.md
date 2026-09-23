# Les piles

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/gifpile.webp)

Comme expliqué précédemment, une pile travaille en mode LIFO (Last In First Out). Pour être utilisée, l'interface d'une pile doit permettre a minima :

- la création d'une pile vide
- l'ajout d'un élément dans la pile (qui sera forcément au dessus). On dira qu'on **empile**.
- le retrait d'un élément de la pile (qui sera forcément celui du dessus) et le renvoi de sa valeur. On dira qu'on **dépile**.

## **3.1 Utilisation d'une interface de pile**

### **Exercice 3**

On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la pile `p` et la valeur éventuellement renvoyée.
Bien comprendre que la classe `Pile()` et ses méthodes n'existent pas vraiment. Nous *jouons* avec son interface.

```python
On prendra pour convention que la tête de la pile est à droite.

1. p = Pile() 
2. p.empile(3)   
3. p.empile(5)  
4. p.est_vide()  
5. p.empile(1)  
6. p.depile()  
7. p.depile() 
8. p.empile(9)  
9. p.depile()  
10. p.depile() 
11. p.est_vide()
```

## **3.2 Implémentation(s) d'une pile**

L'objectif est de créer une classe `Pile`. L'instruction `Pile()` créera une pile vide. Chaque objet `Pile` disposera des méthodes suivantes :
- `est_vide` : indique si la pile est vide (renvoie un booléen)
- `empile` : insère un élément (passé en paramètre) en haut de la pile. Ne renvoie rien.
- `depile` : renvoie la valeur de l'élément en haut de la pile ET le supprime de la pile.

Ces 3 méthodes sont essentielles et se retrouveront systématiquement dans chaque interface. Nous y ajouterons, uniquement par commodité, la méthode suivante :

- `__repr__` : permet d'afficher la pile sous forme agréable (par ex : `|3|6|2|5|`)

### **3.2.1 À l'aide du type `list` de Python**

### **Exercice 4**

Créer la classe `Pile` ci-dessus.
Le type `list` de Python est parfaitement adapté. Des renseignements intéressants à son sujet peuvent être trouvés [ici](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists).

Test de l'implémentation :

```python
>>> p = Pile()
>>> p.empile(5)
>>> p.empile(3)
>>> p.empile(7)
>>> p
|5|3|7|

```

### **3.2.2 À l'aide d'une liste chaînée et de la classe `Cellule`**

Nous avons créé la classe `Cellule` :

```python
class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante
```

### **Exercice 5**

À l'aide cette classe, re-créer une classe `Pile` disposant exactement de la même interface que dans l'exercice précédent.

Test de l'implémentation :

```python
>>> p = Pile()
>>> p.empile(5)
>>> p.empile(3)
>>> p.empile(7)
>>> p
|7|3|5|
```

**À retenir :** pour l'utilisateur, les interfaces du 3.2.1 et 3.2.2 sont strictement identiques. Il ne peut pas savoir, en les utilisant, quelle est l'implémentation qui est derrière.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/xkcd.png)

## **3.3 Application des piles**

### **Exercice 6**

Simulez une gestion de l'historique de navigation internet, en créant une classe `Nav` qui utilisera une pile. Attention, il ne faut pas réinventer la classe `Pile`, mais uniquement s'en servir !

Exemple d'utilisation :

```python
>>> n = Nav()
>>> n.visite('lemonde.fr')
page actuelle : lemonde.fr
>>> n.visite('google.fr')
page actuelle : google.fr
>>> n.visite('lyceemousseron.fr')
page actuelle : lyceemousseron.fr
>>> n.back()
page quittée : lyceemousseron.fr
>>> n.back()
page quittée : google.fr
```
