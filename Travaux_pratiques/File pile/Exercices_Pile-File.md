## **Exercice 0 : calculatrice polonaise inverse**

L'écriture polonaise inverse des expressions arithmétiques place l'opérateur après ses opérandes. Cette notation ne nécessite aucune parenthèse ni aucune règle de priorité.

Ainsi l'expression polonaise inverse décrite par la chaîne de caractères: `'1 2 3 * + 4 *'` désigne l'expression traditionnellement notée .

Écrire une fonction `eval_pol_inv` prenant en paramètre une chaîne de caractères représentant une expression en notation polonaise inverse composée d'additions et de multiplications de nombres entiers et renvoyant la valeur de cette expression. On supposera que les éléments de l'expression sont séparés par des espaces.

Attention: cette fonction ne doit pas renvoyer de résultat (ou `None`) si l'expression est mal écrite.

**Quelques tests:**

```python
assert eval_pol_inv('2 1 7 + 5 * +') == 42
assert eval_pol_inv('1 + 2') == None
```

---

## **Exercice 1**

Dans cet exercice, on utilise une classe `Pile` implémentée avec une liste de Python et possédant ses quatre éléments d'interface usuels:

- Un constructeur qui permet de créer une pile vide, représentée par `[]` ;
- La méthode `est_vide()` qui renvoie `True` si l'objet est une pile ne contenant aucun élément, et `False` sinon ;
- La méthode `empiler` qui prend un objet quelconque en paramètre et ajoute cet objet au sommet de la pile. Dans la représentation de la pile dans la console, cet objet apparaît à droite des autres éléments de la pile ;
- La méthode `depiler` qui renvoie l'objet présent au sommet de la pile et le retire de la pile.

**Exemples:**

```python
>>> mapile = Pile()
>>> mapile.empiler(2)
>>> mapile
[2]
>>> mapile.empiler(3)
>>> mapile.empiler(50)
>>> mapile
[2, 3, 50]
>>> mapile.depiler()
50
>>> mapile
[2, 3]
```

1. La méthode `est_triee` ci-dessous renvoie `True` si, en dépilant tous les éléments un par un , ils sont traités dans l'ordre croissant, et `False` sinon. Compléter les lignes 6 et 8.
    
    ```python
    def est_triee(self):
        if not self.est_vide() :
            e1 = self.depiler()
            while not self.est_vide():
                e2 = self.depiler()
                if e1 ... e2 :
                    return False
                e1 = ...
        return True
    ```
    
    
2. On crée dans la console la pile `A` représentée par `[1, 2, 3, 4]`.
    
    **a.** Donner la valeur renvoyée par l'appel `A.est_triee()`.
    
    **b.** Donner le contenu de la pile `A` après l'exécution de cette instruction.
    
3. On souhaite maintenant écrire le code d'une méthode `depileMax` d'une pile non vide ne contenant que des nombres entiers et renvoyant le plus grand élément de cette pile en le retirant de la pile.
    
    Après l'exécution de `p.depileMax()`, le nombre d'éléments de la pile `p` diminue donc de 1.
    
    Compléter les lignes 9 et 11 :
    
    ```python
    def depileMax(self):
        assert not self.est_vide(), "Pile vide"
        q = Pile()
        maxi = self.depiler()
        while not self.est_vide() :
            elt = self.depiler()
            if maxi < elt :
                q.empiler(maxi)
                maxi = ...
            else :
                ...
        while not q.est_vide():
            self.empiler(q.depiler())
        return maxi
    ```
    
    
4. On crée la pile `B` représentée par `[9, -7, 8, 12, 4]` et on effectue l’appel `B.depileMax()`.
    
    **a.** Donner le contenu des piles `B` et `q` à la fin de chaque itération de la boucle `while` de la ligne 5.
    
    **b.** Donner le contenu des piles `B` et `q` avant l’exécution de la ligne 14.
    
    **c.** Donner un exemple de pile qui montre que l'ordre des éléments restants n’est pas préservé après l’exécution de `depileMax`.
    
5. On donne le code de la fonction `traite` :
    
    ```python
    def traite(self):
        q = Pile()
        while not self.est_vide():
            q.empile(self.depile_max())
        while not q.est_vide():
            self.empile(q.depile())
    ```
    
    
    **a.** Donner les contenus successifs des piles `B` et `q`
    
    - avant la ligne 3,
    - avant la ligne 5,
    - à la fin de l'exécution de la fonction `traite`
    
    lorsque la fonction `traite` est appelée avec la pile `B` contenant `[1, 6, 4, 3, 7, 2]`.
    
    **b.** Expliquer le traitement effectué par cette fonction.
    

---


## **Exercice 2**

> D'après 2022, Centres étrangers, J1, Ex. 2
> 

Un supermarché met en place un système de passage automatique en caisse. Un client scanne les articles à l'aide d'un scanner de code-barres au fur et à mesure qu'il les ajoute dans son panier.

Les articles s'enregistrent alors dans une structure de données. La structure de données utilisée est une file définie par la classe `Panier`, avec les primitives habituelles sur la structure de file.

Pour faciliter la lecture, le code de la classe `Panier` n'est pas écrit.

```python
class Panier():
    def __init__(self):
        "Initialise la file comme une file vide."

    def est_vide(self):
        "Renvoie True si la file est vide, False sinon."

    def enfile(self, e):
        "Ajoute l'élément e en dernière position de la file, ne renvoie rien."

    def defile(self):
        "Retire le premier élément de la file et le renvoie."
```

Les articles sont représentés par des tuples `(code_barre, designation, prix, horaire_scan)` où

- `code_barre` est un nombre entier identifiant l'article ;
- `designation` est une chaine de caractères qui pourra être affichée sur le ticket de caisse ;
- `prix` est un nombre décimal donnant le prix d'une unité de cet article ;
- `horaire_scan` est un nombre entier de secondes permettant de connaitre l'heure où l'article a été scanné.

Le panier d'un client sera donc représenté par une file contenant les articles scannés.

1. On souhaite ajouter un article dont le tuple est le suivant `(31002, "café noir", 1.50, 50525)`.
    
    Écrire le code utilisant une des quatre méthodes ci-dessus permettant d'ajouter l'article à l'objet de classe `Panier` appelé `panier_1`.
    
2. On souhaite définir une méthode `remplir` de paramètre `panier_temp` dans la classe `Panier` permettant de transférer vers la file tout le contenu d'un autre panier `panier_temp` qui est aussi un objet de type `Panier`. Recopier et compléter le code de la méthode `remplir`.
    
    ```python
    def remplir(self, panier_temp):
        while not panier_temp. ... :
            article = panier_temp. ...
            self. ... (article)
    ```
    
3. Pour que le client puisse connaitre à tout moment le montant de son panier, on souhaite ajouter une méthode `prix_total` (sans paramètres) à la classe `Panier` qui renvoie la somme des prix de tous les articles présents dans le panier.
    
    Écrire le code de la méthode `prix_total`.
    
    /!\ Attention, après l'appel de cette méthode, le panier devra toujours contenir ses articles.
    
4. Le magasin souhaite connaitre pour chaque client la durée du passage en caisse. Cette durée sera obtenue en faisant la différence entre le champ `horaire_scan` du dernier article scanné et le champ `horaire_scan` du premier article scanné dans le panier du client. Un panier vide renverra une durée égale à `None`. On pourra accepter que le panier soit vide après l'appel de cette méthode.
    
    Écrire une méthode `duree_passage_en_caisse` de la classe `Panier` qui renvoie cette durée.
    

---


## **Exercice 3 : files d'attente**

Dans cet exercice, on se propose d'évaluer le temps d'attente de clients à des guichets, en comparant la solution d'une unique file d'attente et la solution d'une file d'attente par guichet.

Pour cela, on modélise le temps par une variable globale, qui est incrémentée à chaque tour de boucle. Lorsqu'un nouveau client arrive, il est placé dans une file sous la forme d'un entier égal à la valeur de l'horloge, c'est-à-dire égal à son heure d'arrivée. Lorsqu'un client est servi, c'est-à-dire lorsqu'il sort de sa file d'attente, on obtient son temps d'attente en faisant la soustraction de la valeur courante de l'horloge et de la valeur qui vient d'être retirée de la file.

L'idée est de faire tourner une telle simulation relativement longtemps, tout en totalisant le nombre de clients servis et le temps d'attente cumulé sur tous les clients. Le rapport de ces deux quantités nous donne le temps d'attente moyen. On peut alors comparer plusieurs stratégies (une ou plusieurs files, choix d'une file au hasard quand il y en a plusieurs, choix de la file où il y a le moins de clients, etc.).

On se donne un nombre N de guichets (par exemple, N = 5). Pour simuler la disponibilité d'un guichet, on peut se donner un tableau d'entiers `dispo` de taille N. La valeur de `dispo[i]` indique le nombre de tours d'horloge où le guichet `i` sera occupé. En particulier, lorsque cette valeur vaut 0, cela veut dire que le guichet est libre et peut donc servir un nouveau client. Lorsqu'un client est servi par le guichet 1, on choisit un temps de traitement pour ce client, au hasard entre 0 et N, et on l'affecte à `dispo[i]`.

À chaque tour d'horloge, on réalise deux opérations:

- on fait apparaître un nouveau client;
- pour chaque guichet `i`:
    - s'il est disponible, il sert un nouveau client (pris dans sa propre file ou dans l'unique file, selon le modèle), le cas échéant;
    - sinon, on décrémente `dispo[i]`.

Écrire un programme qui effectue une telle simulation, sur 100 tours d'horloge, et affiche au final le temps d'attente moyen. Comparer avec différentes stratégies.

--- 

## **Exercice 4**

https://adventofcode.com/2018/day/5

--- 


## **Exercice 5**

https://adventofcode.com/2022/day/5

On travaillera avec la situation de départ suivante :

![](https://cgouygou.github.io/TNSI/T01_StructuresDonnees/images/aoc22_day5_input.png)

Et ce fichier d'instructions.
