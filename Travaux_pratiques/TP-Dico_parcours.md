# TP : Dico et parcours

[https://pythontutor.com/render.html#mode=display](https://pythontutor.com/render.html#mode=display)

## Serie d’entrainement

### **Exercice 1**

Sans utiliser la fonction `max` de Python, écrire une fonction `maxDico` qui prend en argument un dictionnaire `d` non vide dont les valeurs sont des nombres et qui renvoie la valeur maximale de `d`.

Exemple:

```python
>>>d={"a":4,"b":5,"c":6}
>>>maxDico(d)
6

def maxDico(dico:{str:int})->int:
	#....
```

### **Exercice 2**

Ecrire une fonction `listeDeClesDeValeurs` qui prend en argument un dictionnaire `d` et une valeur `v` et qui renvoie la liste des clés de `d` de valeur égale à `v`.

Par exemple,

```python
>>>listeDeClesDeValeurs({'a':13,'b':16,'c':13},13)
['a','c']
>>>listeDeClesDeValeurs({'a':13,'b':16,'c':13},12)
[]

def listeDeClesDeValeurs(dico:{str:int})-> []:
	#....
```

### **Exercice 3**

Ecrire une fonction `Dicoccurrences` qui prend en argument une chaine de caractères `chaine` et qui renvoie un dictionnaire dont les clés sont les caractères de `chaine` et dont les valeurs sont les nombres d'apparitions de chaque caractère.

Par exemple,

```python
>>>Dicoccurrences('bonjour')
{'b':1,'o':2,'n':1,'j':1,'u':1,'r':1}

def Dicoccurrences(chaine:str) -> {}:
	#...
```

### **Exercice 4**

Ecrire une fonction `aUneMemeValeur` qui prend en argument deux dictionnaires et qui renvoie `True` si il existe une valeur commune à ces deux dictionnaires et `False` sinon.

Par exemple,

```python
>>>aUneMemeValeur({'adrien':13,'carla':16},{'aline':15,'celine':14,'benjamin':16})
True
```

puisque il y a une valeur commune qui est ici 16.

Par contre,

```python
>>>aUneMemeValeur({'adrien':13,'carla':16},{'aline':15,'celine':11,'benjamin':11})
False
```

puisqu'il n'y a aucune valeur commune entre les deux dictionnaires.

**Indication** : on pourra effectuer une double boucle sur chacun des deux dictionnaires

```python
def aUneMemeValeur(dico1:{str:int},dico2:{str,int})->bool:
	#....
```

## Problème I :

L’ARN contient le codage des protéines, composées de chaines d’acides aminés.

Le dictionnaire ci-dessous donne les correspondances entre les codons, des séquences d’ARN constitués de trois nucléotides, et les acides aminés.

La séquence AUG, par exemple, correspond à la méthionine, notée M.

```python
dico_gen ={
'UUU' : 'F', 'UUC' : 'F', 'UUG' : 'L', 'UUA' : 'L', 'UCU' : 'S',
'UCC' : 'S', 'UCG' : 'S', 'UCA' : 'S', 'UAU' : 'Y', 'UAC' : 'Y',
'UAG' : 'X', 'UAA' : 'X', 'UGU' : 'C', 'UGC' : 'C', 'UGG' : 'W',
'UGA' : 'X', 'CUU' : 'L', 'CUC' : 'L', 'CUG' : 'L', 'CUA' : 'L',
'CCU' : 'P', 'CCC' : 'P', 'CCG' : 'P', 'CCA' : 'P', 'CGU' : 'R',
'CGC' : 'R', 'CGG' : 'R', 'CGA' : 'R', 'CAU' : 'H', 'CAC' : 'H',
'CAG' : 'Q', 'CAA' : 'Q', 'ACU' : 'T', 'ACC' : 'T', 'ACG' : 'T',
'ACA' : 'T', 'AUG' : 'M', 'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I',
'AAU' : 'N', 'AAC' : 'N', 'AAG' : 'K', 'AAA' : 'K', 'AGU' : 'S',
'AGC' : 'S', 'AGG' : 'R', 'AGA' : 'R', 'GUU' : 'V', 'GUC' : 'V',
'GUG' : 'V', 'GUA' : 'V', 'GCU' : 'A', 'GCC' : 'A', 'GCG' : 'A',
'GCA' : 'A', 'GGU' : 'G', 'GGC' : 'G', 'GGG' : 'G', 'GGA' : 'G',
'GAU' : 'D', 'GAC' : 'D', 'GAG' : 'E', 'GAA' : 'E'}
```

---

Écrire une fonction `traduction` qui traduit une chaine d’ARN en protéine.
On suppose que la longueur de la chaine d’ARN est un multiple de trois. 

Ainsi, `traduction('UUCAGUGGG')` renverra `'FSG'`.

```python
def traduction(arn:str) -> str:
'''
traduit la chaîne arn en suite d'acides aminés.
'''

assert traduction('UUCAGUGGG') == 'FSG'
```

## Problème II :

Une ville souhaite gérer son parc de vélos en location partagée. L’ensemble de la flotte de vélos est stocké dans une table de données représentée en langage Python par un dictionnaire contenant des associations de type `id_velo : dict_velo` où `id_velo` est un nombre entier compris entre 1 et 199 qui correspond à l'identifiant unique du vélo et `dict_velo` est un dictionnaire dont les clés sont : `"type"`, `"etat"`, `"station"`. Les valeurs associées aux clés `"type"`, `"etat"`, `"station"` de `dict_velo` sont de type chaînes de caractères ou nombre entier :

- `"type"` : chaîne de caractères qui peut prendre la valeur `"electrique"` ou `"classique"`;
- `"état"` : nombre entier qui peut prendre la valeur 1 si le vélo est disponible, 0 si le vélo est en déplacement, -1 si le vélo est en panne;
- `"station"` : chaînes de caractères qui identifie la station où est garé le vélo.

Dans le cas où le vélo est en déplacement ou en panne, `"station"` correspond à celle où il a été dernièrement stationné. Voici un extrait de la table de données :

```python
flotte = {
    12 : {"type" : "electrique", "etat" : 1, "station" : "Prefecture"},
    80 : {"type" : "classique", "etat" : 0, "station" : "Saint-Leu"},
    45 : {"type" : "classique", "etat" : 1, "station" : "Baraban"},
    41 : {"type" : "classique", "etat" : -1, "station" : "Citadelle"},
    26 : {"type" : "classique", "etat" : 1, "station" : "Coliseum"},
    28 : {"type" : "electrique", "etat" : 0, "station" : "Coliseum"},
    74 : {"type" : "electrique", "etat" : 1, "station" : "Jacobins"},
    13 : {"type" : "classique", "etat" : 0, "station" : "Citadelle"},
    83 : {"type" : "classique", "etat" : -1, "station" : "Saint-Leu"},
    22 : {"type" : "electrique", "etat" : -1, "station" : "Joffre"}
}
```

`flotte` étant une variable globale du programme.

Toutes les questions de cet exercice se réfèrent à l'extrait de la table flotte fourni ci-dessus.

1. **a.** Que renvoie l'instruction `flotte[26]` ?
    
    **b.** Que renvoie l'instruction `flotte[80]["etat"]` ?
    
    **c.** Que renvoie l'instruction `flotte[99]["etat"]` ?
    
2. Voici le script d'une fonction :
    
    ```python
    def proposition(choix):
        for v in flotte:
            if flotte[v]["type"] == choix and flotte[v]["etat"] == 1:
                return flotte[v]["station"]
    ```
    
    **a.** Quelles sont les valeurs possibles de la variable `choix` ?
    
    **b.** Expliquer ce que renvoie la fonction lorsque l'on choisit comme paramètre l'une des valeurs possibles de la variable `choix`.
    
3. **a.** Écrire un script en langage Python qui affiche les identifiants `(id_velo)` de tous les vélos disponibles à la station`"Citadelle"`.
    
    **b.** Écrire un script en langage Python qui permet d'afficher l'identifiant `(id_velo)` et la station de tous les vélos électriques qui ne sont pas en panne.
    
4. On dispose d'une table de données des positions GPS de toutes les stations, dont un extrait est donné ci-dessous. Cette table est stockée sous forme d’un dictionnaire. Chaque élément du dictionnaire est du type: `'nom de la station' : (latitude, longitude)`:
    
    ```python
    stations = {
        'Prefecture' : (49.8905, 2.2967) ,
        'Saint-Leu' : (49.8982, 2.3017),
        'Coliseum' : (49.8942, 2.2874),
        'Jacobins' : (49.8912, 2.3016)
    }
    ```
    
    On **admet** que l'on dispose d'une fonction `distance` permettant de renvoyer la distance en mètres entre deux positions données par leurs coordonnées GPS (latitude et longitude).
    
    Cette fonction prend en paramètre deux tuples représentant les coordonnées des deux positions GPS et renvoie un nombre entier représentant cette distance en mètres.
    
    Par exemple, `distance((49.8905, 2.2967), (49.8912, 2.3016))` renvoie `9591`.
    
    Écrire une fonction qui prend en paramètre les coordonnées GPS de l'utilisateur sous forme d’un tuple et qui renvoie, pour chaque station située à moins de 800 mètres de l'utilisateur :
    
    - le nom de la station ;
    - la distance entre l'utilisateur et la station ;
    - les identifiants des vélos disponibles dans cette station.
    
    Une station où aucun vélo n’est disponible ne doit pas être affichée.
    

## Problème III :

La cryptographie est un ensemble de techniques permettant de chiffrer un message.

Une technique de cryptographie consiste à mélanger les lettres d'un alphabet et à réécrire le message avec ces permutations. En Python, on peut créer un dictionnaire dans lequel les clés sont les lettres de l'alphabet et les valeurs sont celles de l'alphabet mélangé.

**Exemple**

Par exemple, si l'alphabet contient les 4 lettres A, B, C et D, et si le dictionnaire de l'alphabet mélangé est

```python
alpha = {"A": "B", "B": "D", "C": "A", "D": "C"}
```

la chaine de caractères `"BAC"`

sera chiffrée `"DBA"`.

Un tel dictionnaire sera appelé **dictionnaire de chiffrement**.

1. On souhaite chiffrer un message écrit avec l'alphabet A, B, C, D, E, F, G à l'aide du dictionnaire
    
    ```python
    alpha ={"A": "B", "B": "D", "C": "A", "D": "C", "E": "F", "F": "G", "G": "E"}
    ```
    
    **a.** Quelle est la valeur associée à la clé `"D"` ? En Python, comment l'obtenir ?
    
    **b.** Chiffrer la chaine de caractères `"BAGAGE"` avec le dictionnaire `alpha`.
    
2. On considère qu'un mot est une chaine de caractères (un objet de type `str`) écrite uniquement avec les 26 lettres de l'alphabet en majuscule. Par exemple, `"ARBRE"` est un mot et `"L'ARBRE !"` n'est pas un mot à cause des caractères : `"'"`, `" "`(espace) et `"!"`.
    
    Écrire une fonction `chiffre` qui prend en paramètres `mot` un mot et `alpha` un dictionnaire de chiffrement, telle que `chiffre(mot, alpha)` renvoie `mot` sous forme de chaine chiffrée avec le dictionnaire de chiffrement `alpha`.
    
3. On souhaite déchiffrer un mot chiffré avec cette méthode.
    
    **a.** Si un mot est chiffré avec le dictionnaire de chiffrement :
    
    ```python
     alpha = {"A": "B", "B": "D", "C": "A", "D": "C", "E": "F", "F": "G", "G": "E"}
    ```
    
     Donner un dictionnaire permettant de le déchiffrer.
    
    **b.** Écrire une fonction en Python appelée `dico_dechiffrement` qui prend en paramètre `dico` un dictionnaire de chiffrement et qui renvoie un dictionnaire permettant le déchiffrement. On pourra s'inspirer du code incomplet ci-dessous ou proposer une autre solution :
    
    ```python
    def dico_dechiffrement(dico):
        nouveau = {}
        for lettre in dico:
            code = dico[...]
            nouveau[...] = ...
        return nouveau
    ```
    
    **c.** Écrire une fonction telle que `dechiffre(mot_chiffre, dico)` renvoie le mot décodé, quand `mot_chiffre` est chiffré par le dictionnaire de chiffrement `dico`. On utilisera les fonctions écrites dans les questions précédentes.
    
4. On souhaite à présent créer un dictionnaire de chiffrement. Écrire une fonction `dico_chiffrement` qui prend en paramètre `alphabet` un tableau de lettres et qui renvoie un dictionnaire de chiffrement dont les clés sont les lettres du tableau `alphabet` et les valeurs sont les lettres du tableau alphabet mélangées.
    
    On pourra utiliser la fonction `shuffle` du module `random` qui mélange en place un tableau. Par exemple, on a :
    
    ```python
    >>> tableau = ["A", "B", "C", "D"]
    >>> shuffle(tableau)
    >>> tableau
    ["B", "A", "D", "C"]
    ```
    

# Correction :

### P I

```python

proteine = ''
for i in range(0, len(arn), 3):
	codon = arn[i] + arn[i+1] + arn[i+2] # ou arn[i:i+3]
	acide = dico_gen[codon]
	proteine += acide
return proteine
```

[Evaluation__Terminale_NSI.pdf](TP%20Dico%20et%20parcours/Evaluation__Terminale_NSI.pdf)

### P II

1. **a.** L'instruction `flotte[26]` renvoie la valeur associée à la clé `26`, c'est-à-dire le dictionnaire `{'type': 'classique', 'etat': 1, 'station': 'Coliseum'}`.
    
    **b.** L'instruction `flotte[80]['etat']` renvoie `0` .
    
    **c.** L'instruction `flotte[99]['etat']` renvoie une erreur (`KeyError`), puisqu'il n'y a pas de clé égale à `99` dans le dictionnaire `flotte`.
    
2. **a.** Les valeurs possibles de la variable `choix` sont `classique` ou `electrique` .
    
    **b.** La fonction renvoie le nom des stations où des vélos du type `choix` sont disponibles.
    
3. **a.**
    
    ```python
    for v in flotte:
        if flotte[v]['station'] == 'Citadelle' and flotte[v]['etat'] == 1:
            print(v)
    ```
    
    ---
    
    **b.**
    
    ```python
    for v in flotte:
        if flotte[v]['type'] == 'electrique' and flotte[v]['etat'] != -1:
            print(v, flotte[v]['station'])
    ```
    
    ---
    
4. La liste en compréhension ligne 6 n'est pas obligatoire mais elle est bien pratique...
    
    ```python
    def info_velo(position:tuple) -> list:
        requete = []
        for station, coordonnees_GPS in stations.items():
            d = distance(position, coordonnees_GPS)
            if d < 800:
                velos_disponibles = [v for v in flotte if flotte[v]['station'] == station and flotte[v]['etat'] == 1]
                if velos_diponibles != []:
                    requete.append((station, d, velos_disponibles))
    ```
    
    ---
    

### P III

1. **a.** La valeur associée à la clé `'D'` est `'C'`, on l'obtient en Python avec `alpha['D']`.
    
    **b.** On obtient `'DBEBEF'`.
    
2. Il suffit d'utiliser une variable accumulatrice et de chiffrer en parcourant le paramètre `mot`:
    
    ```python
    def chiffre(mot:str, alpha:str) -> str:
        resultat = ''
        for c in mot:
            resultat = resultat + alpha[c]
        return resultat
    ```
    
    ---
    
3. **a.** Il suffit d'inverser clés et valeurs, donc on peut déchiffrer avec le dictionnaire:
    
    ```python
    {'A': 'C', 'B': 'A', 'C': 'D', 'D': 'B', 'E': 'G', 'F': 'E', 'G': 'F'}.
    ```
    
    **b.** On obtient:
    
    ```python
    def dico_dechiffrement(dico:dict) -> dict:
        nouveau = {}
        for lettre in dico:
            code = dico[lettre]
            nouveau[code] = lettre
        return nouveau
    ```
    
    ---
    
    **c.** À l'aide des deux dernières fonctions, cela va très vite:
    
    ```python
    def dechiffre(mot_chiffre:str , dico:dict) -> str:
        dico_inverse = dico_dechiffrement(dico)
        return chiffre(mot_chiffre, dico_inverse)
    ```
    
    ---
    
4. La difficulté tient dans le fait qu'il faut faire une [copie de la liste](https://cgouygou.github.io/1NSI/T02_TypesConstruits/T2.1_Listes/T2.1_Listes3/) contenant l'alphabet avant de mélanger.
    
    ```python
    import random
    
    def dico_chiffrement(alphabet:list) -> dict:
        alpha = alphabet.copy()
        random.shuffle(alpha)
        dico = {}
        for i in range(len(alphabet)):
            dico[alphabet[i]] = alpha[i]
        return dico
    ```
    
    ---