## **Exercice 1**

On considère le contenu de mon dressing, représenté par un dictionnaire:

```python
dressing = {"pantalons": 3, "pulls": 4, "tee-shirts": 8}
```

1. J'ai oublié mes 5 chemises... Ajoutez-les au dictionnaire `dressing`.
2. Écrire une fonction (ou plutôt une *procédure*, pas de **return**) `ajout(habit)` qui prend en paramètre un type d'habit et qui augmente son nombre de 1 dans le dictionnaire.
3. Améliorer la fonction pour qu'elle crée une nouvelle entrée si le type d'habit n'existe pas comme clé.

## **Exercice 2**

On considère la liste suivante :

```python
lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']
```

Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?

## **Exercice 3**

On modélise des informations (nom, taille et poids) sur des Pokémons de la façon suivante:

```python
exemple_pokemons = {
    'Bulbizarre': (70, 7),
    'Herbizarre': (100, 13),
    'Abo': (200, 7),
    'Jungko': (170, 52)
    }
```

Par exemple, `Bulbizarre` est un pokémon qui mesure 70 cm et pèse 7 kg.

1. Ajouer le pokémon `Goupix` qui mesure 60 cm et pèse 10 kg.
2. Compléter la fonction `plus_grand` qui prend en paramètre un dictionnaire et qui renvoie un tuple contenant le nom du pokemon le plus grand et sa taille.

```python
def plus_grand(pokemons: dict) -> tuple:
    nom_plus_grand = ''
    taille_max = 0
    for  in pokemons. :
        if     > taille_max:
            nom_plus_grand =
            taille_max =
    return
```

## **Exercice 4**

Reprendre l'exercice «Le lion de Némée» (T2.1 exercice 7) et construire un dictionnaire dont les clés sont les noms des divinités et les valeurs leur «valeur» selon l'énoncé.

## **Exercice 5**

Voici un dictionnaire `dates` dont les clés sont des prénoms au format `str` et les valeurs des dates de naissance au format `tuple`.

```python
dates = {
    "Alan": (23, 6, 1912),
    "Grace": (9, 12, 1906),
    "Linus": (28, 12, 1969),
    "Guido": (31, 1, 1956),
    "Ada": (10, 12, 1815),
    "Tim": (8, 6, 1955),
    "Dennis": (9, 9, 1941),
    "Hedy": (9, 11, 1914),
    "Steve": (24, 2, 1955)
    }
```

Par exemple, Linus est né le 28 décembre 1969.

1. Ajouter les deux entrées suivantes: Margaret, née le 17 août 1936 et John, né le 28 décembre 1903.
2. Écrire une fonction `calendrier` qui prend en paramètre un dictionnaire constitué d'entrées `nom: (jour, mois, année)` comme `dates` et qui renvoie un dictionnaire dont les clés sont les mois de l'année et les valeurs les listes des noms nés ce mois-là. Par exemple, `calendrier(dates)` doit renvoyer un dictionnaire contenant l'entrée `"juin": ["Alan", "Tim"]`.
3. Écrire une fonction `plus_jeune` qui renvoie le nom de la personne la plus jeune du dictionnaire.

## **Exercice 6**

Voici un dictionnaire Python:

```python
dico = {'L': 'S', 'C': 'D', 'M': 'V', 'R': 'M', 'CA': 'T', 'GR': 'EP', 'HE': 'AD', 'CH': 'MOD'}
```

---

**À l'aide d'un parcours du dictionnaire**, créer le dictionnaire «inversé», c'est-à-dire en échangeant clés et valeurs.

## **Exercice 7**

Ci-dessous, un célèbre texte a été écrit en code morse. Décodez le!

```python
texte_morse = """
-- .- .. ... ...- --- ..- ... ... .- ...- . --.. -- --- .. .--- . -. .
-.-. .-. --- .. ... .--. .- ... --.- ..- .. .-.. -.-- .- .. - -.. . -... ---
-. -. . --- ..- -.. . -- .- ..- ...- .- .. ... . ... .. - ..- .-
- .. --- -. -- --- .. ... .. .--- . -.. . ...- .- .. ... .-. . ...
..- -- . .-. -- .- ...- .. . .- ..- .--- --- ..- .-. -.. .... ..- .. .-
...- . -.-. ...- --- ..- ... .--- . -.. .. .-. .- .. ... --.- ..- . -.-. .
... - -.. .- -... --- .-. -.. -.. . ... .-. . -. -.-. --- -. - .-. .
... -.. . ... --. . -. ... --.- ..- .. -- --- -. - - . -. -.. ..-
.-.. .- -- .- .. -. .--. . ..- - . - .-. . .- ..- -. -- --- --
. -. - --- ..- .--- . -. . .--. --- ..- ...- .- .. ... .--. .- ... ---
..- .--- . - .- .. ... ... . ..- .-.. -.-. .... . --.. -- --- .. . -
-.-. . ... - .- ... ... . --.. -.-. ..- .-. .. . ..- -..- -.. . ... .
-.. .. .-. . --.- ..- . .-.. . ... .... .- ... .- .-. -.. ... .-.. . ...
.-. . -. -.-. --- -. - .-. . ... ..-. --- .-. --. . -. - ..- -. .
-.. . ... - .. -. . . .--. .- .-. -.-. . --.- ..- . --.- ..- .- -.
-.. --- -. .- .-.. . --. --- ..- - -.. . .-.. .- -.-. .... --- ... . --.-
..- .- -. -.. --- -. .- .-.. . --. --- ..- - -.. . .-.. .- -.-. .... ---
... . -... .. . -. ..-. .- .. - . .-.. . -... . .- ..- --. . ...
- . .--. .- .-. ..-. --- .. ... --- -. -. . - .-. --- ..- ...- . .--.
.- ... .-.. .. -. - . .-. .-.. --- -.-. ..- - . ..- .-. . -. ..-. .-
-.-. . .--- . -.. .. .-. .- .. ... .-.. . -- .. .-. --- .. .-. --.- ..-
.. ...- --- ..- ... .- .. -.. . .- .- ...- .- -. -.-. . .-. .- .-.. ---
.-. ... -.-. . -. . ... - .--. .- ... -- --- -. -.-. .- ... -.-. --- --
-- . .--- . .-.. . -.. .. ... .- .. ... .-.. .- .--. ..- .. ... --.- ..-
. -- --- .. .- ..- -.-. --- -. - .-. .- .. .-. . .--- .- .. .--. ..-
. - .--- . -.. .. ... -- . .-. -.-. .. .- .-.. .- ...- .. . .--- .
.-.. ..- .. -.. .. ... -- . .-. -.-. .. .--- . -.-. .... .- -. - . .-..
.- ...- .. . .--- . -.. .- -. ... . .-.. .- ...- .. . .--- . -. .
... ..- .. ... --.- ..- .- -- --- ..- .-. . - ..-. .. -. .- .-.. . --
. -. - --.- ..- .- -. -.. -... . .- ..- -.-. --- ..- .--. -.. . --. .
-. ... .- ..- .--- --- ..- .-. -.. .... ..- .. -- . -.. .. ... . -. -
-- .- .. ... -.-. --- -- -- . -. - ..-. .- .. ... - ..- .--. --- ..-
.-. .- ...- --- .. .-. -.-. . - - . .... ..- -- .- -. .. - . .
.... -... .. . -. .--- . .-.. . ..- .-. .-. . .--. --- -. -.. ... - .-.
. ... ... .. -- .--. .-.. . -- . -. - .--- . .-.. . ..- .-. -.. ..
... --.- ..- . -.-. . ... - -.-. . --. --- ..- - -.. . .-.. .- -- ---
..- .-. -.-. . --. --- ..- - -.. --- -. -.-. --.- ..- .. -- .- .--. --- ..-
... ... . .- ..- .--- --- ..- .-. -.. .... ..- .. .- . -. - .-. . .--.
.-. . -. -.. .-. . ..- -. . -.-. --- -. ... - .-. ..- -.-. - .. ---
-. -- . -.-. .- -. .. --.- ..- . -- .- .. ... -.. . -- .- .. -.
--.- ..- .. ... .- .. - .--. . ..- - . - .-. . ... .. -- .--. .-..
. -- . -. - .- -- . -- . - - .-. . .- ..- ... . .-. ...-
.. -.-. . -.. . .-.. .- -.-. --- -- -- ..- -. .- ..- - . .- ..-. .-
.. .-. . .-.. . -.. --- -. .-.. . -.. --- -. -.. . ... --- ..
"""
```

---

## **Exercice 8**

L’ARN contient le codage des protéines, composées de chaines d’acides aminés.

Le dictionnaire ci-dessous donne les correspondances entre les codons, des séquences d’ARN constitués de trois nucléotides, et les acides aminés.

La séquence AUG, par exemple, correspond à la méthionine, notée M.

```python
dico_gen = {
    'UUU': 'F', 'UUC': 'F', 'UUG': 'L', 'UUA': 'L', 'UCU': 'S',
    'UCC': 'S', 'UCG': 'S', 'UCA': 'S', 'UAU': 'Y', 'UAC': 'Y',
    'UAG': 'X', 'UAA': 'X', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
    'UGA': 'X', 'CUU': 'L', 'CUC': 'L', 'CUG': 'L', 'CUA': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCG': 'P', 'CCA': 'P', 'CGU': 'R',
    'CGC': 'R', 'CGG': 'R', 'CGA': 'R', 'CAU': 'H', 'CAC': 'H',
    'CAG': 'Q', 'CAA': 'Q', 'ACU': 'T', 'ACC': 'T', 'ACG': 'T',
    'ACA': 'T', 'AUG': 'M', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AAU': 'N', 'AAC': 'N', 'AAG': 'K', 'AAA': 'K', 'AGU': 'S',
    'AGC': 'S', 'AGG': 'R', 'AGA': 'R', 'GUU': 'V', 'GUC': 'V',
    'GUG': 'V', 'GUA': 'V', 'GCU': 'A', 'GCC': 'A', 'GCG': 'A',
    'GCA': 'A', 'GGU': 'G', 'GGC': 'G', 'GGG': 'G', 'GGA': 'G',
    'GAU': 'D', 'GAC': 'D', 'GAG': 'E', 'GAA': 'E'
    }
```

---

Écrire une fonction `traduction` qui traduit une chaine d’ARN en protéine. On suppose que la longueur de la chaine d’ARN est un multiple de trois. Ainsi, `traduction('UUCAGUGGG')` renverra `'FSG'`.
