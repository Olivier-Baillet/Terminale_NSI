## À retenir

- Dans une méthode, `self` désigne l’objet sur lequel on appelle la méthode. Un **attribut** se crée et se lit avec `self.`.
- Une **variable définie dans une méthode** sans `self.` est locale : elle disparaît à la fin de l’appel et n’est pas un attribut.
- Depuis l’extérieur de la classe, un attribut se lit avec un objet : `objet.attribut`.
- Une méthode qui **renvoie** une valeur (`return`) n’**affiche** rien.
- `b = a` ne copie pas un objet : `a` et `b` désignent le même objet.

---

## Exercice 1 – Vrai ou faux ?

Pour chaque affirmation, indiquer si elle est vraie ou fausse. Quand elle est fausse, la corriger en une phrase.

1. Il faut écrire `obj.methode(obj)` pour que le paramètre `self` reçoive l’objet.
2. La méthode `__init__` est appelée automatiquement lors de la création d’un objet.
3. Une variable créée dans une méthode, sans `self.`, devient un attribut de l’objet.
4. Deux objets de la même classe ont chacun leurs propres attributs.
5. Une méthode qui ne contient aucun `return` renvoie `None`.
6. Si `a` est un objet et qu’on écrit `b = a`, modifier un attribut de `b` ne modifie pas `a`.
7. Depuis l’extérieur de la classe, on peut lire l’attribut `x` d’un objet `o` en écrivant simplement `x`.
8. Dans une méthode, `print(valeur)` et `return valeur` produisent le même effet.

---

## Exercice 2 – Chasse aux erreurs

La classe suivante contient **cinq erreurs**. Elle est censée représenter un thermomètre.

```python
class Thermometre:
    def __init__(temperature):
        temperature = temperature

    def chauffer(self, degres):
        self.temperature + degres

    def est_gele(self):
        self.temperature <= 0

    def afficher(self):
        print("Il fait", temperature, "degrés")
```

1. Repérer les cinq erreurs et, pour chacune, dire ce qui se passerait à l’exécution (message d’erreur ou comportement incorrect).
2. Réécrire la classe corrigée.
3. Donner ce qu’affiche le script suivant avec la classe corrigée :

```python
t = Thermometre(-3)
t.chauffer(5)
print(t.est_gele())
t.afficher()
```

---

## Exercice 3 – Un ascenseur

On modélise un ascenseur d’immeuble. Il dessert les étages de `0` (rez-de-chaussée) à `etage_max`. Il démarre au rez-de-chaussée.

1. Recopier et compléter les points de suspension :

```python
class Ascenseur:
    def __init__(self, etage_max):
        self.etage_max = ...
        self.etage = ...

    def monter(self):
        if self.etage ... self.etage_max:
            self.etage = ...
            return True
        return ...

    def est_au_rez(self):
        return ...
```

La méthode `monter` fait monter l’ascenseur d’un étage et renvoie `True` ; si l’ascenseur est déjà à l’étage maximum, elle ne fait rien et renvoie `False`.

1. Écrire la méthode `descendre(self)`, qui fonctionne de la même manière en descendant, sans jamais passer sous le rez-de-chaussée.
2. Écrire la méthode `aller_a(self, destination)` qui amène l’ascenseur à l’étage `destination`, en **utilisant les méthodes `monter` et `descendre`** de la classe. On suppose que `destination` est un étage valide. Cette méthode ne renvoie rien.
3. Écrire la méthode spéciale `__str__(self)` qui renvoie une chaîne de la forme `"Ascenseur à l’étage 2/5"` (étage actuel, puis étage maximum).
4. Donner ce qu’affiche le script suivant :

```python
a = Ascenseur(3)
a.monter()
a.monter()
print(a.monter())
print(a.monter())
print(a)
a.aller_a(1)
print(a)
```

---

## Exercice 4 – Une playlist

On dispose de la classe suivante, où la durée est donnée en secondes :

```python
class Morceau:
    def __init__(self, titre, artiste, duree):
        self.titre = titre
        self.artiste = artiste
        self.duree = duree

    def est_long(self):
        return self.duree > 240
```

1. Écrire les instructions qui créent une liste `playlist` contenant, dans cet ordre, ces trois morceaux : *Alpha* de *Lune* (200 s), *Bravo* de *Lune* (260 s) et *Charlie* de *Soleil* (180 s).
2. Écrire une fonction `duree_totale(morceaux)` qui renvoie la durée totale, en secondes, d’une liste de morceaux.
3. Écrire une fonction `de_artiste(morceaux, artiste)` qui renvoie la **liste des titres** des morceaux de cet artiste. Elle renvoie une liste vide si l’artiste n’apparaît pas.
4. Avec la liste `playlist` de la question 1, donner la valeur de chacune des expressions suivantes :

```python
playlist[0].duree
playlist[1].est_long()
duree_totale(playlist)
de_artiste(playlist, "Lune")
de_artiste(playlist, "Terre")
```

---

## Exercice bonus – Références et objets

On utilise la classe `Morceau` de l’exercice 4. Donner ce qu’affiche le programme suivant et expliquer.

```python
m1 = Morceau("Alpha", "Lune", 200)
m2 = m1
m3 = Morceau("Alpha", "Lune", 200)
m2.duree = 300
print(m1.duree, m3.duree)
print(m1 is m2, m1 is m3)
```

---

# Corrigé

*À distribuer après la séance.*

## Exercice 1

1. Faux. Python transmet l’objet automatiquement comme premier argument : on écrit `obj.methode()`.
2. Vrai.
3. Faux. Une variable locale n’existe que pendant l’appel de la méthode ; pour créer un attribut, il faut écrire `self.nom = ...`.
4. Vrai.
5. Vrai.
6. Faux. `a` et `b` désignent le même objet, donc la modification est visible par les deux.
7. Faux. Il faut passer par l’objet : `o.x`.
8. Faux. `print` affiche à l’écran, tandis que `return` renvoie une valeur que l’appelant peut utiliser. Sans `return`, la méthode renvoie `None`.

## Exercice 2

1. Les cinq erreurs :
    - `__init__(temperature)` : le paramètre `self` manque ; `Thermometre(-3)` lève une erreur car le constructeur reçoit un argument de trop.
    - `temperature = temperature` : variable locale qui ne crée aucun attribut ; il faut `self.temperature = temperature`.
    - `self.temperature + degres` : le calcul est fait mais jamais stocké, la température ne change pas.
    - `self.temperature <= 0` dans `est_gele` : il manque `return`, la méthode renvoie `None`.
    - `temperature` dans `afficher` : variable inconnue (erreur de nom) ; il faut `self.temperature`.
2. Classe corrigée :

```python
class Thermometre:
    def __init__(self, temperature):
        self.temperature = temperature

    def chauffer(self, degres):
        self.temperature = self.temperature + degres

    def est_gele(self):
        return self.temperature <= 0

    def afficher(self):
        print("Il fait", self.temperature, "degrés")
```

1. Affichage : `False`, puis `Il fait 2 degrés`.

## Exercice 3

```python
class Ascenseur:
    def __init__(self, etage_max):
        self.etage_max = etage_max
        self.etage = 0

    def monter(self):
        if self.etage < self.etage_max:
            self.etage = self.etage + 1
            return True
        return False

    def est_au_rez(self):
        return self.etage == 0

    def descendre(self):
        if self.etage > 0:
            self.etage = self.etage - 1
            return True
        return False

    def aller_a(self, destination):
        while self.etage < destination:
            self.monter()
        while self.etage > destination:
            self.descendre()

    def __str__(self):
        return f"Ascenseur à l’étage {self.etage}/{self.etage_max}"
```

Question 5 : affichages `True`, `False`, `Ascenseur à l’étage 3/3`, puis `Ascenseur à l’étage 1/3`. Les deux premiers `monter()` portent l’ascenseur à l’étage 2 ; le troisième le fait passer à 3 et renvoie `True` ; le suivant échoue car l’étage maximum est atteint.

## Exercice 4

```python
playlist = [
    Morceau("Alpha", "Lune", 200),
    Morceau("Bravo", "Lune", 260),
    Morceau("Charlie", "Soleil", 180)
]

def duree_totale(morceaux):
    total = 0
    for m in morceaux:
        total = total + m.duree
    return total

def de_artiste(morceaux, artiste):
    titres = []
    for m in morceaux:
        if m.artiste == artiste:
            titres.append(m.titre)
    return titres
```

Question 4 : `200`, `True` (260 > 240), `640`, `['Alpha', 'Bravo']` et `[]`.

## Exercice bonus

Affichages : `300 200`, puis `True False`. `m2 = m1` ne copie pas l’objet : `m1` et `m2` désignent le même objet, donc changer `m2.duree` change aussi `m1.duree`. `m3` est un objet distinct, créé avec les mêmes valeurs : il n’est pas modifié, et `m1 is m3` vaut `False`.
