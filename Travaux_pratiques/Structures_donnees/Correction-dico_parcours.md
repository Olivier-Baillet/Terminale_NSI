    

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
