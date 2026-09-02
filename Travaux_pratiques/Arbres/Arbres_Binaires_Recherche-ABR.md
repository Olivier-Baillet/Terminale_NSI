# Arbres Binaires de Recherche (ABR)

### **Définition**

Un arbre binaire de recherche (ABR en abrégé) est un cas particulier d'arbre binaire, où les valeurs des nœuds (appelées plutôt *clés*) sont nécessairement ordonnables entre elles: elles sont toutes de même type `int` ou `str` par exemple.

De plus, **pour tous** les nœuds de l'arbre, la clé est :

- strictement supérieure à toutes les clés du sous-arbre gauche;
- inférieure ou égale à toutes les clés du sous-arbre droit;

### **ABR or not ABR ?**

![Exemple 1](Arbres%20Binaires%20de%20Recherche%20(ABR)/image.png)

Exemple 1

![Exemple 2](Arbres%20Binaires%20de%20Recherche%20(ABR)/image%201.png)

Exemple 2

![Exemple 3](Arbres%20Binaires%20de%20Recherche%20(ABR)/image%202.png)

Exemple 3

![Exemple 4](https://cgouygou.github.io/TNSI/T01_StructuresDonnees/images/ABR4.png)

Exemple 4

- **Important: parcours et ordre croissant**
    
    **Quel parcours d'un ABR donne un tri des clés dans l'ordre croissant.**
    

## 1. Recherche dans un ABR

La structure d'ABR va permettre de rechercher efficacement une clé. En effet, en fonction du résultat de la comparaison d'une clé avec la valeur recherchée, on sait dans quel sous-arbre poursuivre récursivement la recherche...

### **Classe `ABR`**

Un ABR étant un cas particulier d'un arbre binaire, on peut reprendre l'implémentation déjà existante de la classe `Noeud` en adaptant seulement le constructeur de la classe:

```python
class Noeud:
		def __init__(self, valeur, g=None, d=None):
				self.valeur = valeur
				self.fils_gauche = g
				self.fils_droit = d
```

Une autre manière de gérer l’arbre, quelle serait son aventage ?

```python
class ABR:
    def __init__(self, cle=None):
        self.cle = cle
        if self.cle is not None:
            self.fils_gauche = ABR()
            self.fils_droit = ABR()
```

Ainsi que la méthode  `rechercher` :

<aside>
💡

### **À compléter :**

```python
    def rechercher(self, valeur):
        if ... :
            return False
        elif ... :
            return True
        elif valeur < self.cle:
            return ...
        else:
            return ...
```

</aside>

## 2. Ajout dans un ABR

L'insertion d'un nœud dans un ABR va permettre de *construire* un ABR. Mais il faut bien évidemment conserver la cohérence des clés des nœuds: on doit insérer un nœud en construisant des sous-arbres qui sont aussi des ABR.

Pour cela, on va construire uniquement un ABR vide, puis insérer un nœud/sous-arbre sur les feuilles, c'est-à-dire uniquement sur un sous-arbre vide: le fils_gauche ou le fils_droit, selon la valeur de la clé à insérer.

### **Exemple**

Dessiner l'ABR obtenu en partant d'un arbre vide, puis en insérant successivement les clés 12, 10, 15, 5, 20, 4, 8, 11, 17.

### **Implémentation de la méthode**

Compléter les deux méthodes ci-dessous:

```python
    def inserer_cle(self, cle):
        if self.est_vide():
            self.cle = ...
            self.fils_gauche = ...
            self.fils_droit = ...
        elif ...
            self.fils_droit.inserer_cle(cle)
        else:
            ...

    def inserer_cles(self, liste_cles):
        ...
```

## 3. Exercices

### **Exercice 1**

Dans un ABR, où se trouve le plus petit élément? En déduire une méthode `minimum` qui renvoie le plus petit élément de l'ABR, et `None` si l'ABR est vide.

### **Exercice 2**

Écrire une fonction qui prend en paramètre un arbre binaire et qui renvoie `True` si l'arbre est un ABR et `False` sinon.

### **Exercice 3**

Écrire une méthode `compte` qui renvoie le nombre d'occurrences d'une clé dans un ABR.

---

## Annexe :

### Exemple d’utilisation

```python
abr = Noeud(12)
for v in [10, 15, 5, 20, 4, 8, 11, 17]:
	abr.inserer(v)

print(abr.contient(5))    # True
print(abr.contient(20))   # False
print(abr.taille())       
print(abr.hauteur())      # dépend de la forme de l'arbre
```

---

### Recherche récursive

```python
    def contient(self, valeur):
        if self.valeur == valeur:
            return True
        elif valeur < self.valeur:
            if self.fils_gauche is None:
                return False
            return self.fils_gauche.contient(valeur)
        else:
            if self.fils_droit is None:
                return False
            return self.fils_droit.contient(valeur)

```

### Insertion récursive dans un ABR

```python
    def inserer(self, valeur):
        if valeur < self.valeur:
            if self.fils_gauche is None:
                self.fils_gauche = Arbre(valeur)
            else:
                self.fils_gauche.inserer(valeur)
        elif valeur > self.valeur:
            if self.fils_droit is None:
                self.fils_droit = Arbre(valeur)
            else:
                self.fils_droit.inserer(valeur)

```

### Taille récursive

```python
    def taille(self):
        if self.fils_gauche is not None:
	        taille_g = self.fils_gauche.taille()
        else:
	        taille_g = 0
        
        if self.fils_droit is not None:
	        taille_d = self.fils_droit.taille()
	      else 
		      taille_d = 0
        return 1 + taille_g + taille_d

```

### Hauteur récursive

```python
    def hauteur(self):
        if self.fils_gauche:
	        h_g = self.fils_gauche.hauteur() 
        else:
	        h_g = 0
        
        if self.fils_droit:
	        h_d = self.fils_droit.hauteur() 
	      else 
		      hd = 0
		      
        return 1 + max(h_g, h_d)

```

Est arbre

```python
def est_abr(arbre, min_val=float("-inf"), max_val=float("inf")):
	if arbre is None:
			return True
	
	if not (min_val < arbre.valeur < max_val):
	    return False
	
	return (
	    est_abr(arbre.gauche, min_val, arbre.valeur)
	    and est_abr(arbre.droite, arbre.valeur, max_val)
	)

```

Compte occurence :

```python
def compte(self, valeur):
    if self.cle is None:
        return 0

    if valeur == self.cle:
        return 1 + self.droit.compte(valeur)

    if valeur < self.cle:
        return self.gauche.compte(valeur)
    else:
        return self.droit.compte(valeur)

```