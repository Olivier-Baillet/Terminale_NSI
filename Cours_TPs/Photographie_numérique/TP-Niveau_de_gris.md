# TP Niveau de gris

## Introduction

Dans ce paragraphe, nous allons décrire comment transformer une image en couleurs en une image en niveaux de gris.

![pixels](https://www.monlyceenumerique.fr/snt_seconde/photographie_numerique/partie3/img/ImageCouleurGris.jpg)

Pour cela, il est nécessaire d’agir sur tous les pixels, les uns après les autres :
Nous allons utiliser ce qu’on appelle en informatique des boucles “for”, qui permettront de parcourir chaque pixel de l’image (le premier étant pour les lignes et le second pour les colonnes ).

```python
for y in range (largeur) :
	for x in range (hauteur) :
```

Pour chaque pixel, on calcule d’abord la valeur en niveau de gris en fonction de ses trois composantes par la formule suivante :

$g=0,11×r+0,83×v+0,06×b$

On remplace ensuite, pour ce pixel, la couleur (r, v, b) par la couleur (g, g, g).

Nous allons voir pas à pas comment procéder pour transformer l’image suivante :

![image.png](TP%20Niveau%20de%20gris/image.png)

pour aboutir à celle-ci :

![image.png](TP%20Niveau%20de%20gris/image%201.png)

## I. Préparation

- Crée un dossier nommé `Noir&Blanc` dans ton dossier SNT.
- Télécharge l’image du **perroquet couleur** ci-dessus.
    - Enregistre-la dans ton dossier `Noir&Blanc`.

## II. Création du programme

Ouvre **EduPython** et crée un nouveau fichier python.

Enregistre-le dans le même dossier que votre image et sous le nom :

→**`Prenom-Nom-niveau_Gris.py`**

---

## III. Code complet à copier

Copie **le code ci-dessous** dans ton fichier **à partir de la première ligne !**

```python
# Importation de la partie de la bibliothèque PIL utile pour le traitement de l'image :
from PIL import Image

# Ouverture de l'image perroquet et stockage dans une variable nommée imageSource :
imageSource = Image.open( "image.png" )

# récupération des dimensions de l'image (source) du perroquet :
tailleX , TailleY = ... .size # 4.1 Instruction size

# création d'une nouvelle image de même dimension que celle du perroquet :
imageGris = Image.new("RGB" , ( ... , ... )) # 4.2 Nouvelle image

# balayage de toute l'image du perroquet pixel par pixel :
for y in range (TailleY ) : # balayage de chacune des lignes de l'image
    for x in range (tailleX ) :  # balayage de chacune des colonnes de l'image

		# À compléter :
		# 4.3 Lire les composantes Rouge, Vert, Bleu du pixel (x, y)
        r,v,b = ... .getpixel (( x , y ))

        # 4.4 Calculer le niveau de gris (moyenne des 3 valeurs)
        g=int( ... )

        # 4.5 Écrire le pixel (x, y) dans la nouvelle image en gris
        ... .putpixel((x, y),( ... , ... , ... ))

        pass  # à supprimer ensuite

# enregistrement de l'image créée dans le même répertoire que celui contenant ce programme (et l'image initiale) :
imageGris.save("image_couleur_gris.jpg" )

# ouverture de l'image créée par un logiciel adapté de votre ordinateur
imageGris.show( )
```

> ⚠️ Attention : copie le code **à partir de la première ligne** et colle sans laisser de ligne ou d’instructions avant :
 `# Importation de la partie de la...`
> 

### Rappel :

<aside markdown="1">


### 💡 Variable

En python nous pouvons stocker des valeurs dans ce qu’on appelle des variables.
Dans le TP précédent nous avons utilisée la variable `bleue`.

```python
bleue = (0, 0, 255)
```

- A droite du égale, des valeurs, ici notre correspondance aux composantes RGB.
- A gauche du égale, le nom de la variable, qui pourra être réutilisée par la suite, comme par exemple :
    
    ```python
    image.putpixel((0, 0), **bleue** )
    ```
    

Autre exemple :

```python
imageSource = Image.open( "image.png" )
```

Ici `imageSource` est une variable également, est correspond à l’image initiale du perroquet.

> /!\ Attention : “image.png” correspond au nom de fichier que vous avez sauvegarder dans le dossier du TP. Si vous l’avez changé il faut modifier ce nom également.
> 
</aside>

## IV. Questions

Pendant ce TP, nous utiliserons deux variables images différentes :

- imageSource : Correspond à l’image du d’origine en couleur.
- imageGris :  Correspond à la nouvelle image qu’on souhaite modifier.

1. Remplacer les “…” de la ligne 8 du programme par une variable image, qui utilisera l’instruction `.size` afin de stocker dans les variables `largeur` et `longueur` les valeurs correspondantes aux deux dimensions de l'image initiale du perroquet.

<aside markdown="1">


### 💡 Instruction size

Pour récupérer les deux valeurs des dimensions de l'image photo, on utilise l'instruction :

```python
tailleX , TailleY = photo.size
```

Les variables `largeur` et `longueur` vont ainsi contenir les valeurs numériques correspondantes aux deux dimensions de l'image initiale du perroquet.

Si on souhaite récupérer les valeurs pour une autre image, il faut dans ce cas changer la variable `photo` par la variable de l’image souhaitée.

Par exemple si on crée une nouvelle image :

```python
imageExemple = Image.new("RGB" , ( 10, 20 ))
tailleX , TailleY = imageExemple.size
```

Pour la variable `imageExemple`, cela donne une variable `tailleX` égale à 10 et une variable `TailleY` égale à 20.

</aside>

2. Compléter les “…” de la ligne 11 du programme afin de créer une nouvelle image nommée `imageSource`, dont les dimensions seront les mêmes que notre image de couleur initial.
Donc les variables `largeur` et `hauteur` de l’image d’origine.

<aside markdown="1">


### 💡 Nouvelle image

On a déjà vu dans le TP précédent comment créer une nouvelle image de largeur L et de hauteur H :

```python
imageGris = Image.new("RGB" , ( L, H ))
```

Ici, `L` et `H` doivent être remplacés par des variables qui s’adapteront aux dimensions de l’image.

</aside>

3. Compléter la ligne 19 du programme avec getpixel(), afin de stocker dans les variables nommées `r`, `v` et `b` les composantes RVB du pixel de coordonnées (x,y) de l'image du perroquet initiale.
    
    Penser à utiliser la variable image déjà créée dans ce programme qui stocke l'image initiale du perroquet.
    

<aside markdown="1">


### 💡 Récupérer les pixels

Pour lire les informations (r, v, b) du pixel de coordonnées (x, y) de la variable d’une image nommée `photo`, on utilise l’instruction :

```python
r,v,b = photo.getpixel (( x , y ))
```

S’ils ont souhaite récupérer les valeurs des trois composantes d’un pixel pour une autre image, il faudra dans ce cas changer la variable `photo` par la variable de l’image souhaitée.

</aside>

4. Compléter la ligne 22 du programme en utilisant la formule de niveau de gris afin de stocker dans la variable nommée `g` le niveau de gris calculé.

<aside markdown="1">


### 💡 Formule niveau de gris

Pour chaque pixel, on calcule d’abord la valeur en niveau de gris en fonction de ses trois composantes par la formule suivante :

> $g = 0,11 × r + 0,83 × v + 0,06 × b$
> 

En le simplifiant en python cela donne :

```python
g = int((r + v + b) / 3)
```

L'instruction `int` permet de ne garder que la partie entière (c'est-à-dire celle devant la virgule) du résultat du calcul.

</aside>

5. Compléter la ligne 25 du programme en utilisant l’instruction `putpixel` afin de mettre le pixel de coordonnées (x,y) de l'image nouvellement construite au niveau de gris calculé.
    
    Penser à utiliser une variable déjà créée dans ce programme.
    

<aside markdown="1">


### 💡 Instruction putpixel

Pour affecter les informations (r, v, b) au pixel de coordonnées (x, y) de la variable image `photo`, on utilise l’instruction :

```python
photo.putpixel((x,y),(r,v,b))
```

On remplace ensuite, pour ce pixel, la couleur (r, v, b) par la couleur nouvellement créé `g` pour chacune des composantes.

</aside>

## Vérification

6. Vérifiez que l’image obtenue est similaire à celle attendue.
7. Si tout fonctionne, déplacez le fichier **.png** contenant votre image *pixel art* du dernier TP dans le dossier **Noir&Blanc** (exécuter le code Python du TP *Pixel art* recréera l’image si vous ne l’avez plus).
    
    Modifiez ensuite l’instruction suivante de votre code afin de récupérer le bon nom pour votre fichier image.
    Et ainsi transformer votre *pixel art* couleur en nuances de gris.
    

```python
imageSource = Image.open( "image.png" )
```

## Rendu

8. Rendre votre fichier Python dans Moodle.
Pas de pdf avec le code à l’intérieur, ni l’image résultat, mais bien le code que vous avez enregistré puis modifié à partir de l’étape : **2. Création du programme**





## **V. Le négatif d'une image**

Crée un nouveau fichier python.

Enregistre-le sous le nom :

→**`Prenom-Nom-négatif.py`**

- Télécharger l’image du loup ci-dessous.
    - Enregistrer là dans le dossier `Noir&Blanc`.
    - Renommer là en : loup.png

![image.png](TP%20Niveau%20de%20gris/image%202.png)

---

### Code complet à copier

1. Copie **le code ci-dessous** dans ton fichier **à partir de la première ligne !**

```python
# Importation de la partie de la bibliothèque PIL utile pour le traitement de l'image :
from PIL import Image

# Ouverture de l'image loup et stockage dans une variable nommée imageSource :
imageSource=Image.open( "loup.png" )  # si le programme n'est pas dans le même fichier que l'image loup, il faut rajouter un chemin d'accès

# récupération des dimensions de l'image du loup :
largeur , hauteur = ...

# création d'une nouvelle image de même dimension que celle du loup :
imageBut=Image.new("RGB" , ( ... , ... ))

# balayage de toute l'image du loup pixel par pixel :
for y in range (hauteur) : # balayage de chacune des lignes de l'image
    for x in range (largeur) :  # balayage de chacune des colonnes de l'image

        # Obtenir les informations RVB du pixel de coordonnées (x,y) de l'image (source) du loup :
        r, v, b = ...       # composante rouge, verte et bleue

        # Passage au négatif :
        ... .putpixel((x,y),( ... , ... , ... ))

# enregistrement de l'image créée dans le même répertoire que celui contenant ce programme (et l'image initiale) :
imageBut.save("negatif_loup.png" )

# ouverture de l'image créée par un logiciel adapté de votre ordinateur
imageBut.show( )

```

2. Reprendre et refaire les questions 4.1, 4.2 et 4.3 (même réponses) pour ce code.

3. Compléter la ligne 21 du programme en utilisant :
    - La formule donnant le négatif d'un pixel
    - L'instruction `putpixel`  afin de mettre le pixel de coordonnées (x,y) de l'image nouvellement construite à niveau de la couleur RVB correspondant au négatif.  

<aside markdown="1">
💡 Le négatif d'une image est une image dont les couleurs sont inversées par rapport à l'originale c'est-à-dire :

- Quand l'image originale est en RVB alors si $$(r,v,b)$$ sont les trois composantes d'un pixel de l'image d'origine alors les composantes du pixel négatif correspondant sont $$(255-r, 255-v, 255-b)$$.
</aside>
    
4. Vérifier que l'image obtenue est la suivante :

![image.png](TP%20Niveau%20de%20gris/image%203.png)

5. Rendre votre fichier Python dans Moodle.
