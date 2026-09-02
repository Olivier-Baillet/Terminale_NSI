# TP Pixel

<aside>
💡

Vous pouvez faire ce travail à plusieurs, mais prenez garde à bien comprendre toutes les réponses (même celles apportées par vos camarade) et à ce que votre compte-rendu soit personnel car le rendu du TP est individuel.

*Lorsqu'une question est marquée d'un symbole 🔎, la réponse peut-être cherchée sur Internet.*

</aside markdown="1">

## **Pixels, Définition, Résolution**

Une photographie numérique (au format jpg, png, tiff, etc.) 
est composée de **pixels** : de petites cases colorées formant un tableau.

[Pixel-example](https://commons.wikimedia.org/wiki/File:Pixel-example.png), par [ed g2s](https://commons.wikimedia.org/wiki/User:Ed_g2s), publié sous licence [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/pixel-example.png)

**Définition d’un écran** : nombre de pixels en largeur × nombre de pixels en hauteur (généralement données sous la forme *1024×780*, signifiant « 1024 pixels de large, et 780 pixels de haut »).

[Cell Phone screen Pixels](https://commons.wikimedia.org/wiki/File:Cell_Phone_screen_Pixels.jpg), par Dinesh Dhankhar, publié sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/cell_phone_screen_pixels.jpg)

**Résolution d’un écran** : La *résolution* d'un écran (exprimée en *dpi* (*dots per inch*), *ppi* (*pixels per inch*), ou *ppp* (*pixels par pource*)) est le nombre de pixels disponibles sur une longueur d'un pouce (environ 2,54 cm). Plus ce nombre est élevé, plus la taille des pixels est petite, et plus l'image sera précise.

1. 🔎 Quelle est l'étymologie du mot ***pixel*** ?
2. 🔎 Quelles sont les résolution de ces écrans ***HD*, *Full HD*, et *4K* ?**
3. Quelle est la différence entre la résolution d’un écran (nombre total de pixels) et la densité de pixels (nombre de pixels par pouce) ?
4. *Écran de téléphone portable.*
Sur la fiche technique du téléphone portable [Fairphone 3](https://shop.fairphone.com/fr/) est écrit :
 *« 2160 x 1080 resolution ; 427 ppp pixel densité. »*
Quelle est la résolution en densité (ppp) de cet écran ?
5. *Écran de télévision 4K.* Une télévision *4K* a les caractéristiques techniques suivantes :
    
    > Taille de l'écran 55"
    Résolution : Longueur 3840 Pixels
    Résolution : Largeur 2160 Pixels
    Longueur du produit 123,06 cm
    Largeur du produit 79,26 cm
    Hauteur du produit 23,75 cm
    > 
    1. 🔎 Convertir la largeur de la télé en pouces (arrondir au dixième).
    2. La résolution est-elle plus grande ou plus petite que celle du téléphone portable étudié à la question précédente ? Comment expliquer cette différence ?

<aside markdown="1">
💡

- Je connais la définition/différence de *résolution* et *définition*.
- Je sais convertir les centimètres en pouces et inversement (exemple : *Combien mesure, en pouces, un écran de 5cm ?*).
- Je sais passer de la résolution à la définition, et inversement (exemple : *Un écran de 7cm a une résolution de 30ppp ; quelle est sa définition ?*).
</aside>

## **Couleurs**

Dans cette partie nous nous intéresserons à la manière dont sont codées les couleurs.

### **Souvenirs d'art plastique**

1. Quelles sont les trois couleurs primaires en peinture ?
2. Comment obtenir les couleurs suivantes à partir des trois couleurs primaires : orange, vert ?

### Le modèle RVB

En informatique, les couleurs ne sont pas décrites avec des mots (« bleu clair », « orange », « noir », etc.), mais par des **valeurs numériques**. 

Pour découvrir ce codage, on peut utiliser soit :

- un logiciel libre comme [GIMP](https://www.gimp.org/) (compatible GNU/Linux, Windows et MacOS),
- soit un [sélecteur de couleurs en ligne](https://mdn.github.io/css-examples/tools/color-picker/).

Vous pouvez faire cette partie, au choix, en utilisant le logiciel [GIMP](https://www.gimp.org/) (que vous pouvez télécharger et installer gratuitement, sous GNU/Linux, Windows ou MacOS), ou en allant sur [un site web en ligne](https://mdn.github.io/css-examples/tools/color-picker/).

---

### **Avec GIMP**

Ouvrir le logiciel GIMP, puis cliquer sur la couleur de premier plan (le carré noir dans le menu de gauche) pour afficher la palette des couleurs. Vous obtenez alors la fenêtre suivante.

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/gimp-palette.png)

Cliquer sur le bouton ‘0….255’ en haut de cet encart.

Dans cette partie, nous nous intéressons *uniquement* aux trois lignes R, G, B (qui ont, sur l'image, les valeurs 88,7, 21,3 et 94,2).

Vous pouvez alors :

- en sélectionnant une couleur dans la partie de gauche, voir quels nombres R, G, B codent cette couleur ;
- en écrivant les nombres R, G, B dans la partie de droite, voir à quelle couleur ils correspondent.

Nous voyons sur la capture d'écran que la couleur rose correspond aux nombres :
*R=88,7, G=21,3, B=94,2*.

### **Avec le site web**

Allez sur le site web [Sélecteur de couleurs CSS](https://mdn.github.io/css-examples/tools/color-picker/).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/mozilla-palette.png)

Dans cette partie, nous nous intéressons *uniquement* à la ligne contenant les trois nombres R, G, B (qui ont, sur l'image, les valeurs 255, 127 et 255).

Vous pouvez alors :

- en sélectionnant une couleur dans « l'arc en ciel » et la partie de gauche, voir quels nombres R, G, B codent cette couleur ;
- en écrivant les nombres R, G, B dans la partie de droite, voir à quelle couleur ils correspondent.

Nous voyons sur la capture d'écran que la couleur rose pâle correspond aux nombres *R=255, G=127, B=255*.

---

### **Questions**

1. 🔎 Que signifient les initiales RGB ?
2. Quelles sont les valeurs minimales et maximales que peuvent prendre les quantité de rouge, vert, bleu ?
    - Minimale :
    - Maximale :
3. En utilisant la palette (de Gimp ou du site web) utilisée à la question précédente, donner le code des couleurs suivantes (on notera `(x, y, z)` la couleur composée de `x` rouge, `y` vert et `z` bleu) :
    - Rouge : `(255, 0, 0)`
    - Vert : `(…, …, …)`
    - Bleu : `(…, …, …)`
    - Noir : `(…, …, …)`
    - Blanc : `(…, …, …)`
4. En utilisant le même outil, avec la même notation, donner les couleurs (en français) correspondant aux codes suivants (un seul mot par couleur) :
    - (0, 255, 255)
    - (255, 0, 255)
    - (255, 255, 0)
    - (255, 128, 0)
5. Combien de couleurs différentes est-il possible de coder en utilisant cette méthode ?

<aside markdown="1">
💡

- Je connais la signification des initiales RGB.
- Je connais la signification des trois nombres d'un code RGB (exemple : *Dans la couleur `(27, 150, 42)`, quelle est la « quantité » de vert, de rouge, de bleu ?*).
- Je connais le code RGB des couleurs suivantes : noir, blanc, rouge, vert, bleu.
- Je sais calculer le nombre de couleurs, c'est-à-dire, je sais expliquer d'où sort le nombre 16777216.
</aside>

---

## **Traitement d'image**

En manipulant les pixels d'une image, il est possible de la modifier, à plusieurs fins.

Lisez les quelques exemples, et répondez aux questions de la dernière partie.

### **Exemples de traitement d'image**

### **Ajout de personnes absentes de la photo originale**

[113th congress usa women version altered by office of House Minority Leader.jpg](https://en.wikipedia.org/wiki/File:113th_congress_usa_women_version_altered_by_office_of_House_Minority_Leader.jpg), original de *US Congress*, modifié par *Office of the House Minority Leader*, domaine public.

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/congress-women.jpg)

Quatre personnes, qui n'ont pu arriver à temps, ont été ajoutées après la prise de la photo.

### **Flou artificiel de l'arrière-plan**

[Faux-bokeh-comparison](https://commons.wikimedia.org/wiki/File:Faux-bokeh-comparison.jpg), par BenFrantzDale, retouché par [Cmglee](https://commons.wikimedia.org/wiki/User:Cmglee), publié sous licence [Creative Commons by-sa 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/flou.jpg)

La photo originale (1) a été altérée pour flouter l'arrière plan, en utilisant deux méthodes différentes (2 et 3).

### **Prise de vue en fourchette**

[Focus stacking Tachinid fly](https://commons.wikimedia.org/wiki/File:Focus_stacking_Tachinid_fly.jpg), par [Muhammad Mahdi Karim](https://en.wikipedia.org/wiki/User:Muhammad_Mahdi_Karim), publié sous licence [Creative Commons by-sa 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/focus-stacking.jpg)

Série d'images d'une mouche tachinaire montrant l'intérêt de la Prise de vue en fourchette. Les deux première images montrent les problèmes de profondeur de champ rencontrés, la troisième a été obtenue en combinant six clichés réalisés avec six mises au point différentes.

### **Assemblage de photos**

[Rochester NY](https://en.wikipedia.org/wiki/File:Rochester_NY.jpg), par [Noso1](https://en.wikipedia.org/wiki/User:Noso1). *The copyright holder of this file allows anyone to use it for any purpose, provided that the copyright holder is properly attributed. Redistribution, derivative work, commercial use, and all other use is permitted.*

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/panorama.jpg)

Plusieurs photos différentes sont assemblées pour donner l'illusion d'une seule photo panoramique.

### **Correction de la perspective**

[Panotools5618](https://commons.wikimedia.org/wiki/File:Panotools5618.jpg), par [Ashley Pomeroy](https://en.wikipedia.org/wiki/User:Ashley_Pomeroy), publié sous licence [Creative Commons by 3.0](https://creativecommons.org/licenses/by/3.0/deed.en).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/remap.jpg)

La photo prise avec une lentille *fisheye* (en haut) a été altérée pour corriger la perspective.

### **Fausse miniature**

[Jodhpur rooftops](https://commons.wikimedia.org/wiki/File:Jodhpur_rooftops.jpg), par [Paul Goyette](https://www.flickr.com/photos/65414509@N00), publié sous licence [Creative Commons by-sa 2.0](https://creativecommons.org/licenses/by-sa/2.0/deed.en).

![_primary](https://snt.ababsurdo.fr/la-photographie-numerique/pixels/tilt-shift.png)

En floutant numériquement la photo de gauche, la photo de droite donne l'impression d'une photo de modèle réduit.

### **Questions**

1. Classer les six exemples de manipulation d'image dans les trois catégories suivantes (plusieurs réponses sont possibles) :
    1. Algorithmes essayant de reproduire le plus fidèlement possible la réalité. 
    2. Algorithmes essayant d'imiter ou de créer un effet artistique. 
    3. Algorithmes produisant l'image d'une situation qui n'a jamais existé. 
2. Citez deux autres exemples de filtres (que vous utilisez peut-être), et :
    - décrivez-les (je ne les connais pas forcément) ;
    - classez-les dans les catégories de la question précédente.
    - Insérer une photo exemple d’un de ces deux filtres
3. Une photographie peut-elle être une preuve irréfutable (`oui` ou `non`) ? Pourquoi ?

<aside markdown="1">
💡

- Je sais donner et décrire quelques algorithmes de manipulation d'image.
</aside>

# Bonus :

## **Capteurs et Photosites**

Lire la page suivante, qui explique le fonctionnement d'un appareil photo numérique : [Capteur photo](https://pixees.fr/informatiquelycee/n_site/snt_photo_capteur.html).

Répondre aux questions suivantes (toutes les réponses se trouvent dans le document qui vient d'être lu).

1. Compléter la phrase suivante : *« Un photosite est un composant électronique ayant la capacité de capter un signal … pour le convertir en un signal … (grâce à l'effet photoélectrique), qui sera lui-même converti en un … (on parle de numérisation). »*
2. Comment fait-on pour qu'un photosite ne soit sensible qu'à une des trois couleurs (rouge, verte, bleue) ? 
3. Pourquoi y a-t-il deux fois plus de photosites verts que de photosites des autres couleurs ? 
4. Combien de photosites faut-il associer pour créer un seul pixel ?

<aside markdown="1">
💡

- Je suis capable de répondre aux quatre questions ci-dessus.
</aside>
