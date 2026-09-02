# TP : Pixel art

# Introduction

Dans les travaux sur les images, on utilisera la bibliothèque PIL qui permet de manipuler, pixel par pixel, des images en Python.

Chaque image est considérée comme un tableau, dont chaque case contient notre triplet de nombres `(R, G, B)`.

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/matrice-rgb-france.png)

Par exemple, l'image ci-dessus représente une image de 3×2 pixels. Deux choses sont à noter sur les coordonnées :

- les coordonnées commencent à 0 (comme dans les ascenseurs, ce qui est courant en informatique) ;
- l'axe vertical est gradué de haut en bas (alors qu'habituellement en mathématiques, il est gradué de bas en haut).

Ainsi, la couleur du pixel de coordonnées `(2, 0)` (en haut à droite) est `(236, 25, 32)` (rouge).

Le programme Python suivant permet de dessiner le drapeau français de l'exemple ci-dessus.

```python
from PIL import Image

bleuFonce = (5, 20, 64)  
rouge = (255,0,0)
blanc = (255,255,255)

image = Image.new('RGB', (3, 2))

image.putpixel((0, 0), bleuFonce )
image.putpixel((0, 1), bleuFonce )
image.putpixel((1, 0), blanc )
image.putpixel((1, 1), blanc )
image.putpixel((2, 0), rouge )
image.putpixel((2, 1), rouge )

image.save("image.png")
image.show()
```

Voici l'explication de chaque ligne :

- Chargement de la bibliothèques `pillow`, qui permet à Python de manipuler des images.
    
    **`from** PIL **import** Image`
    
- Création de la couleur `bleuFonce` en utilisant le format RGB.
    
    `bleuFonce = (5, 20, 64)` 
    
- Création d'une nouvelle image, utilisant le format `‘RGB’` de `3` pixels de large par `2` pixel de haut.
    
    `image **=** Image**.**new**(**'RGB'**,** **(3,** **2))**`
    
- Tracé d'un pixel de couleur `bleuFonce` aux coordonnées `(0, 1)`.
    
    `image**.**putpixel**((0,** **1),** bleuFonce **)**`
    
- Écriture de l'image dans le fichier `image.png`, puis affichage de l'image.
    
    `image**.**save**(**"image.png"**)**
     image**.**show**()**`
    

---

# **I) Pixel par pixel**

1. Dans le dossier "SNT" de votre bureau, créer un dossier et appeler le "Pixel_Art", ensuite créer, sous EduPython, un fichier nommé drapeau.py et l’enregistrer dans ce dossier.
Le `.py` va transformer le fichier en script python.
2. Dans ce fichier, recopier le script donné ci-dessus et l’exécuter.
3. Modifier ce programme de sorte que les couleurs du drapeau affiché correspondent à celui de la Belgique.
    
    On trouve [sur ce site](http://ludowalsh.com/HTM/Liste_de_couleurs.htm) un nuancier de couleurs RVB qui pourra être utile (ou vous pouvez rechercher la couleur sur GIMP).
    
4. Modifier ce programme de sorte que le nombre de pixel soit désormais de 25 pixels de largeur et 20 en hauteurs.
5. Modifier la position du drapeau pour que son premier pixel commence au coordonnées (11, 9).
    
    → `image.putpixel((0, 0), bleuFonce )`
    
6. Modifier les autres pixels pour retrouver le drapeau en entier.

# II) Votre pixel art

1. Reproduisez le quadrillage suivant sur une feuille, et faites un dessin (une lettre, un smiley, etc.) en coloriant certaines cases. Votre dessin devra être composé d'au moins trois couleurs (en plus du blanc).
Ou vous pouvez vous inspirer des idées de ce site : [https://urls.fr/J21ae3](https://urls.fr/J21ae3) (ne viser pas trop grand !)
    
    ![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/matrice-vierge.png)
    
2. Dans votre dossier SNT, comme à la question I.1, créer un fichier .py puis enregistrez le en `dessin-NOM.py` (en remplaçant `NOM` par votre nom de famille).
3. Copier coller dans ce fichier, le code suivant :

```python
from PIL import Image

bleuFonce = (5, 20, 64)  
rouge = (255,0,0)
blanc = (255,255,255)

image = Image.new('RGB', (3, 2))

image.putpixel((0, 0), bleuFonce )

image.save("image.png")
image.show()
```

1. Modifiez le programme pour reproduire votre dessin, pixel par pixel.
Remarque :
Par défaut, toute votre image sera noire, sauf les pixels que vous dessinez. Si vous voulez une image sur fond d’une autre couleur, rajouter `, couleur)` , à la fin de la ligne qui crée votre image comme ci-dessous. 

```python
couleur = (255,255,255) # remplacer le code RVB par ce que vous voulez.
image = Image.new('RGB', (3, 2), couleur)
```

1. Il faudra rendre ce fichier `.py` sur Moodle.

---

## **III) Bonus : Structures de contrôle**

Plutôt que de définir les pixels un à un, il est possible d'utiliser des boucles. Voici quelques exemples.

### **Quelques bandes**

```python
**from** PIL **import** Image

*# On définit une image noire de 256 pixels par 256 pixels*
image **=** Image**.**new**(**"RGB"**,** **(256,** **256))**

*# Pour chaque valeur de x, colorier le pixel de coordonnées (x, 7)
# Cela colorie toute la ligne de rang 7.*
**for** x **in** range**(256):**
	image**.**putpixel**((**x**,** **7),** **(255,** **0,** **0))**
	
*# Pour chaque valeur de y, colorier le pixel de coordonnées (10, y)
# Cela colorie toute la ligne de rang 10.*
**for** y **in** range**(256):**
	image**.**putpixel**((10,** y**),** **(255,** **255,** **0))**

image**.**save**(**"image.png"**)**
```

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/bande1.png)

### **Encore plus de bandes**

```python
**from** PIL **import** Image

image **=** Image**.**new**(**"RGB"**,** **(256,** **256))
for** y **in** range**(26):
	for** x **in** range**(256):
		for** h **in** range**(5):**
			image**.**putpixel**((**x**,** **10***y**+**h**),** **(255,** **0,** **0))**
		
image**.**save**(**"image.png"**)**
```

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/bande2.png)

### **Entrelacs**

```python
**from** PIL **import** Image

image **=** Image**.**new**(**"RGB"**,** **(256,** **256))
for** y **in** range**(26):
	for** x **in** range**(256):
		for** h **in** range**(5):**
			image**.**putpixel**((**x**,** **10***y**+**h**),** **(255,** **0,** **0))
			
for** x **in** range**(26):
	for** y **in** range**(256):
		for** h **in** range**(5):**
			r**,** g**,** b **=** image**.**getpixel**((10***x**+**h**,** y**))**
			image**.**putpixel**((10***x**+**h**,** y**),** **(**r**,** **255,** **0))**
	
image**.**save**(**"image.png"**)**
```

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/entrelacs.png)

### **Opération sur les coordonnées**

Ici, la couleur de chaque pixel (la « quantité » de rouge, de vert, de bleu) est définie par une fonction de ses coordonnées *x* et *y*.

```python
**from** PIL **import** Image

image **=** Image**.**new**(**"RGB"**,** **(256,** **256))
for** x **in** range**(256):
	for** y **in** range**(256):**
		rouge **=** **(**x **+** y**)** **%** **256**
		vert **=** **(**y ***** x**)** **%** **256**
		bleu **=** round**(**x **/** **(**y **+** **1))** **%** **256**
		image**.**putpixel**((**x**,** y**),** **(**rouge**,** vert**,** bleu**))**
		
image**.**save**(**"image.png"**)**
```

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/fonction.png)

La « quantité » de rouge, vert et bleu doit être un nombre entier compris entre 0 et 255. Pour nous assurer cela :

- la fonction [`round()`](https://docs.python.org/fr/3/library/functions.html#round) permet d'arrondir le nombre à l'entier le plus proche ;
- le [modulo `%`](https://docs.python.org/fr/3/reference/expressions.html?highlight=modulo#binary-arithmetic-operations) permet de « ramener » dans l'intervalle [0;255] des nombres trop grands ou trop petits.

### **Hasard**

On peut aussi définir des coordonnées ou couleurs au hasard. Par exemple, **random.randint(0, 255)** donnera un nombre aléatoire entre 0 et 255.

Le programme suivant produit une « marche aléatoire » : un pixel se déplace aléatoirement sur le dessin, en laissant une trace colorée.

```python
**from** PIL **import** Image
**import** random

image **=** Image**.**new**(**"RGB"**,** **(256,** **256))**
x **=** round**(255** **/** **2)**
y **=** round**(255** **/** **2)**
rouge **=** round**(255** **/** **2)**
vert **=** round**(255** **/** **2)**
bleu **=** round**(255** **/** **2)
for** i **in** range**(1000):**
	direction **=** random**.**choice**([**"gauche"**,** "droite"**,** "haut"**,** "bas"**])
	if** direction **==** "gauche"**:**
		x **=** **(**x **-** **1)** **%** **256
	elif** direction **==** "droite"**:**
		x **=** **(**x **+** **1)** **%** **256
	elif** direction **==** "haut"**:**
		y **=** **(**y **-** **1)** **%** **256
	else:**
		y **=** **(**y **+** **1)** **%** **256**
		rouge **=** **(**rouge **+** **2)** **%** **256**
		vert **=** **(**vert **-** **1)** **%** **256
		if** random**.**randint**(0,** **1)** **==** **0:**
			bleu **=** **(**bleu **+** **3)** **%** **256
		else:**
			bleu **=** **(**bleu **-** **3)** **%** **256**
		image**.**putpixel**((**x**,** y**),** **(**rouge**,** vert**,** bleu**))**

image**.**save**(**"image.png"**)**
```

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixelart/random.png)

1. Faites une jolie image en utilisant différents outils.

2. Rendez le fichier `.py` sur Moodle.

[https://snt.ababsurdo.fr/tutoriels/installer-un-paquet-python-avec-thonny/](https://snt.ababsurdo.fr/tutoriels/installer-un-paquet-python-avec-thonny/)
