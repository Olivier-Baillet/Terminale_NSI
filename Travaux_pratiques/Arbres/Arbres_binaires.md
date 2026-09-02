# TP : Arbres binaires

### **Objectifs**

- Etre capable de modéliser en Python un arbre binaire en utilisant une classe objet;
- Implémenter en Python des algorithmes récursifs de parcours d'arbres binaires;
- Calculer la hauteur d'un arbre binaire;
- Construire un arbre binaire complet;

Le squelette du fichier Python source avec les méthodes à compléter est accessible en annexe : Squelette Python

### **Classe objet pour représenter un arbre binaire**

Un arbre binaire peut être représenté par les attributs suivants :

- le nom de sa racine : `nom`
- son sous-arbre gauche (ou None si l'arbre ne possède pas de sous-arbre gauche) : `fils_gauche`
- son sous-arbre droit (ou None si l'arbre ne possède pas de sous-arbre droit) : `fils_droit`

**Complétez le corps du constructeur de la classe `Arbre` afin de construire un arbre dont la racine a pour nom `nom`, avec un sous-arbre gauche vide (`fils_gauche = None`) et un sous-arbre droit vide (`fils_droit = None`)**

```python
class Arbre():

    def __init__(self,nom):
        pass
```

**Complétez les corps des méthodes suivantes de la classe `Arbre` :**

- `set_nom(self,nom)` : renseigne le nom de la racine de l'arbre avec le paramètre `nom` de la méthode;
- `insere_fils_gauche(self, fils_gauche)` : renseigne le sous-arbre gauche de l'arbre avec le paramètre `fils_gauche` (de type `Arbre`) de la méthode;
- `insere_fils_droit(self, fils_droit)` : renseigne le sous-arbre droit de l'arbre avec le paramètre `fils_droit` (de type `Arbre`) de la méthode.

On considère l'arbre binaire suivant :

![](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/arbre1.svg)

**En utilisant les méthodes précédentes de la classe `Arbre`, compléter le corps de la fonction `construit_arbre_exemple()` (qui n'est pas une méthode membre de la classe `Arbre`) qui permet de créer et de retourner une instance de cette classe qui permet de représenter cet arbre.**

### **Représentation graphique d'un arbre binaire en mode texte**

Vous trouverez dans le squelette Python du TP, une méthode de la classe `Arbre` nommée `affiche_arbre(self)` qui permet de visualiser graphique en mode texte un arbre binaire.

La bibliothèque Python utilisée se nomme `binarytree` et la classe Python utilisée permettant de représenter graphiquement un arbre se nomme `Node`.

**Testez cette méthode avec l'arbre de l'exemple et vérifiez que vous devez obtenir l'affichage suivant dans la console Python :**

![](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/Binarytree_example.PNG)

### **Hauteur d'un arbre binaire**

**Dans le fichier squelette Python, la méthode de la classe `Arbre` nommée `hauteur(self)` comporte des lignes mises en commentaire avec des parties de code à compléter. Décommentez les lignes du corps de cette méthode et complétez les parties en pointillés.**

Indication : le principe de l'algorithme récursif de cette méthode est basé sur le résultat suivant : la hauteur d'un arbre est égale au maximum des hauteurs de ces différentes branches.

### **Parcours d'un arbre binaire**

Il existe principalement 3 méthodes récursives de parcours d'un arbre binaire :

- Ordre **préfixe**
    1. On affiche le noeud visité;
    2. On visite le fils gauche si il existe;
    3. On visite le fils droit si il existe.
- Ordre **infixe**
    1. On visite le fils gauche si il existe;
    2. On affiche le noeud visité;
    3. On visite le fils droit si il existe.
- Ordre **postfixe**
    1. On visite le fils gauche si il existe;
    2. On visite le fils droit si il existe;
    3. On affiche le noeud visité.

Ainsi pour l'arbre binaire ci-dessus, voici les 3 parcours :

- Ordre préfixe : 10 - 8 - 3 - 15 - 20 - 5 - 4
- Ordre infixe : 3 - 8 - 20 - 15 - 10 - 4 - 5
- Ordre postfixe : 3 - 20 - 15 - 8 - 4 - 5 - 10

**Complétez le corps des 3 méthodes de la classe `Arbre` pour parcourir un arbre binaire qui retournent chacune sous la forme d'une liste le parcours correspondant.**

**Vérifiez que vos méthodes donnent bien les bons résultats pour les 3 parcours de l'arbre de l'exemple.**

- `parcours_prefixe(self)`
- `parcours_infixe(self)`
- `parcours_postfixe(self)`

### **Arbre binaire complet**

Un arbre binaire complet est un arbre binaire dont chaque noeud possède 2 fils sauf pour le dernier niveau dont tous les noeuds n'ont aucun fils.

On utilisera la convention suivante : la hauteur d’un arbre binaire ne comportant qu’un noeud est 1.

Voici un exemple d'arbre binaire complet

![](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/arbre_complet.svg)

**Donner la hauteur et la taille de cet arbre.**

**Donner le nombre de noeuds d'un arbre de hauteur `h` (h étant un entier supérieur ou égal à 1).**

### **Génération d'un arbre binaire complet dont les noeuds sont des entiers naturels consécutifs à partir de 1**

Dans le fichier squelette Python, deux méthodes (qui ne sont pas des méthodes de la classe `Arbre`) permettent de construire un arbre binaire complet avec des entiers consécutifs à partir de 1 :

- `genere_arbre_binaire_complet(hauteur)` : permet de générer un arbre binaire complet de hauteur `hauteur`.
- `genere_arbre_binaire_complet_recur(hauteur,racine,noeud_courant,h=1,no=1)` : méthode récursive permettant de construire l'arbre binaire complet.
    
    Description des paramètres de la méthode `genere_arbre_binaire_complet_recur(hauteur,racine,noeud_courant,h=1,no=1)` :
    
    - `hauteur` : hauteur de l'arbre binaire complet
    - `racine` : noeud racine de l'arbre binaire complet (son étiquette est le nombre 1) : de type `Arbre`
    - `noeud_courant` : noeud courant de l'arbre en cours de construction (variable de type `Arbre`)
    - `h` : hauteur courante de l'arbre en cours de construction (valeur 1 lors du premier appel de la méthode)
    - `no` : valeur courante de l'étiquette du noeud courant de l'arbre en cours de construction (valeur 1 lors du premier appel de la méthode)

**Ecrire le code de la méthode `genere_arbre_binaire_complet_recur(hauteur,racine,noeud_courant,h=1,no=1)`.**

[Annexe : arbres binaires](TP%20Arbres%20binaires/Annexe%20arbres%20binaires%202ae9d189413580cba4fde917753aa7e2.md)