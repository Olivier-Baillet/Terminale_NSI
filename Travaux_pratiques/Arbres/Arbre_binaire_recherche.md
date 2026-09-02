# Arbre binaire de recherche

Objectifs :

- Construire un arbre binaire de recherche à partir d'une liste;
- Rechercher une clef dans un arbre binaire de recherche.

Rappel :

Un **arbre binaire de recherche** est un arbre défini comme suit :

- Les étiquettes des noeuds sont appelées des **clé**.
- Les clés de tous les noeuds d'un sous-arbre gauche d'un noeud X sont inférieures ou égales à la clé de X.
- Les clés de tous les noeuds d'un sous-arbre droit d'un noeud X sont strictement supérieures à la clé de X.

![Kiwi standing on oval](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/Exemple_arbre_binaire_de_recherche.svg)

### **Construction d'un arbre binaire de recherche à partir d'une liste de nombres**

On dispose d'une liste d'entiers. On souhaite construire un arbre binaire de recherche à partir de cette liste et en traitant les clefs à insérer dans l'arbre à partir de l'ordre de la liste.

Exemple : Pour la liste d'entiers suivante : `[59, 18, 44, 8, 57, 36, 52, 61]`, l'arbre binaire de recherche construit est celui-ci :

![](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/abr_exemple.PNG)

Dans le fichier squelette Python, deux méthodes (qui ne sont pas des méthodes de la classe `Arbre`) permettent de construire un arbre binaire complet avec des entiers consécutifs à partir de 1 :

- `construit_arbre_binaire_recherche(liste)` : permet de générer un arbre binaire de recherche à partir de la liste de nombres `liste`.
- `insere_arbre_binaire_recherche_recur(nombre,indice,racine,noeud)` : méthode récursive permettant d'insérer une clef (un nombre) au bon endroit dans l'arbre binaire de recherche en cours de construction.
    
    Description des paramètres de la méthode `insere_arbre_binaire_recherche_recur(nombre,racine,noeud)` :
    
    - `nombre` : la clef à insérer dans l'arbre binaire de recherche
    - `racine` : noeud racine de l'arbre binaire de recherche (variable de type `Arbre`)
    - `noeud` : noeud courant de l'arbre en cours de construction (variable de type `Arbre`)

**Ecrire le code de la méthode `insere_arbre_binaire_recherche_recur(nombre,racine,noeud)`.**

**Testez votre méthode à partir d'une liste d'entiers générés aléatoirement de taille comprise entre 5 et 10 et en affichant l'arbre binaire de recherche généré à l'aide de la méthode `affiche_arbre(self)` de la classe `Arbre`.**

### **Recherche d'une clef dans un arbre binaire de recherche**

**Ecrire le code de la méthode `recherche_clef_abr(self,clef,nb_etapes=1)` membre de la classe `Arbre` qui recherche si la clé `clef` est présente dans l'arbre binaire de recherche et retourne :**

- `True,nb_etapes` (nb_etapes étant le nombre d'étapes (cad d'appels récursifs de la méthode))
- `False,None` sinon.

Exemple : Pour l'arbre binaire de recherche de l'exemple ci-dessus :

![](https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_arbres/img/abr_exemple.PNG)

- L'appel à la méthode `recherche_clef_abr(self,57,nb_etapes=1)` doit retourner `True,4`;
- L'appel à la méthode `recherche_clef_abr(self,8,nb_etapes=1)` doit retourner `True,3`;
- L'appel à la méthode `recherche_clef_abr(self,59,nb_etapes=1)` doit retourner `True,1`;
- L'appel à la méthode `recherche_clef_abr(self,14,nb_etapes=1)` doit retourner `False,None`.

---