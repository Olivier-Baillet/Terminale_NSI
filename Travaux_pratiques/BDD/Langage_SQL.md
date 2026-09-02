# Langage SQL

Le langage SQL permet de communiquer avec le SGBD pour exploiter une base de données à l'aide de **requêtes**. Il comporte plusieurs parties, dont la partie *langage de définition des données* (LDD) et la partie *langage de manipulation des données* (LMD) qui sont au programme de NSI (plus ou moins explicitement...).

# La définition des données (LDD)

### Les types de données (Domaines)

<aside>
💡

**Non standardisation**

Les différents types de données peuvent varier d'un SGBD à l'autre...

Dans le tableau suivant, on donne les types les plus traditionnels (tels qu'on les manipulera avec SQLite et donnés dans les sujets de BAC).

</aside>

| **Classe de stockage** | **Type de donnée représentée** |
| --- | --- |
| `INTEGER` | Nombre entier (sur n bits, selon la taille) |
| `REAL` | Nombre flottant (8 bits, norme IEEE-754) |
| `DATE` | Format date, norme ISO AAAA-MM-JJ |
| `DATETIME` | Format date et heure, norme ISO AAAA-MM-JJ HH:MM:SS.SSS |
| `TEXT` | Chaîne de caractères codées selon l’encodage spécifié (UTF-8, ...) |
| `VARCHAR(n)` | Chaîne de caractères limitée à `n` caractères |
| `BLOB` | Données brutes, octets, images… stockées au format binaire. |

## CREATE TABLE

Le mot-clé `CREATE TABLE` permet de créer une table (étonnant, non?) en précisant son schéma.

```python
**Exemple de création d'une table**

CREATE TABLE livre (
    titre TEXT,
    editeur VARCHAR(45),
    annee INTEGER,
    isbn VARCHAR(17) PRIMARY KEY
);
```

<aside>
💡

**Syntaxe**

Si dans une requête SQL la casse n'est pas importante (on aurait très bien pu écrire `Create Table` ou `create table`), il ne faut pas oublier le « `;` » en fin de requête !

</aside>

### **Exercice 1**

1. Lancer DB Browser for SQLite et créer une nouvelle base de donnée `bibliotheque.db` (ne pas oublier l'extension). Fermer la fenêtre de création.
2. Dans l'onglet *Exécuter le SQL*, copier-coller le code précédent, puis exécuter le code (bouton ▶ ou F5).
3. Dans l'onglet *Structure de la Base de Données*, vérifier le schéma de cette table *livre*.
4. De la même façon, créer la table *usager* en reprenant le schéma du chapitre **T4.1**.

Pour définir une clé étrangère dans la création d'une table, on utilisera le mot-clé `REFERENCES` en indiquant la table et l'attribut auquel la clé fait référence. Par exemple, pour créer la table *emprunt*, on commencera par:

```python
CREATE TABLE emprunt (
    isbn VARCHAR(17) PRIMARY KEY REFERENCES livre(isbn),
    ...
);
```

### **Exercice 2**

Terminer la requête de création de la table *emprunt*.

## DROP TABLE

Le mot-clé `DROP TABLE` permet de supprimer une table.

```python
**Script SQL pour effacer la base de données**

DROP TABLE emprunt;
DROP TABLE usager;
DROP TABLE livre;
```

# La manipulation des données (LMD) : Requêtes de mise à jour

Commençons par créer la table *élève* suivante (je sais, il y a des erreurs):

| **id_eleve** | **prénom** | **nom** | **moyenne** | **maison** |
| --- | --- | --- | --- | --- |
| 1 | Harry | Potter | 17 | Gryffondor |
| 2 | Hermione | Granger | 9 | Gryffondor |
| 3 | Luna | Lovegood | 13 | Serdaigle |
| 4 | Drago | Malefoy | 15 | Poufsouffle |

## INSERT

Pour insérer dans une table une ligne (un enregistrement, une entité) sous la forme d'un n-uplet de valeurs, on utilise les mots-clés `INSERT INTO ... VALUES ...`.

```python
**Exemple d'insertion dans une table**

INSERT INTO eleve VALUES
    (1, 'Harry', 'Potter', 17, 'Gryffondor');
```

On peut également insérer plusieurs lignes à la fois, en séparant les n-uplets par des virgules:

```python
**Exemple d'insertion multiple dans une table**

INSERT INTO eleve VALUES
    (2, 'Hermione', 'Granger', 9, 'Gryffondor'),
    (3, 'Luna', 'Lovegood', 13, 'Serdaigle');
```

### **Exercice 3**

1. Dans une nouvelle base de données, créer la table *élève*.
2. Insérer les valeurs dans la table.
3. Ajouter la ligne `(4, 'Ron', 'Wisley', 16, 'Gryffondor')`. Que se passe-t-il? Pourquoi?
4. Ajouter la ligne en rectifiant.
- **Astuce hors-programme**
    
    On peut déléguer la gestion des clés primaires avec l'instruction `AUTOINCREMENT`.
    
    ```python
    CREATE TABLE eleve (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prenom VARCHAR(30),
        nom VARCHAR(30),
        moyenne REAL,
        maison VARCHAR(12)
    );
    
    INSERT INTO eleve (prenom, nom, moyenne, maison) VALUES
        ('Harry', 'Potter', 17, 'Gryffondor'),
        ('Hermione', 'Granger', 9, 'Gryffondor'),
        ('Luna', 'Lovegood', 13, 'Serdaigle'),
        ('Drago', 'Malefoy', 15, 'Poufsouffle');
    ```
    

### **Exercice 4**

1. Dans la base de données précédente, créer les tables **professeur** puis **maison** en suivant les schémas:
    - **professeur**(id_prof `Int`, nom `String`, cours `String`)
    - **maison**(nom `String`, dortoir `String`, #id_prof `Int`)
2. Insérer dans la table **professeur** les lignes `(1, 'Rogue', 'potion'), (2, 'Macgonagall', 'métamorphose'), (3, 'Flitwick', 'sortilège'), (4, 'Chourave', 'botanique')`.
3. Insérer dans la table **maison** les lignes `('Gryffondor', 'tour', 2), ('Poufsouffle', 'sous-sol', 4), ('Serpentard', 'cachot', 1)`.
4. Insérer dans la table **maison** la ligne `('Serdaigle', 'tour', 5)`. Que se passe-t-il? Pourquoi?

## UPDATE

Le mot-clé `UPDATE` permet d'actualiser une ou plusieurs valeurs d'une ligne (ou de plusieurs lignes).

```python
**Exemple de modification d'une valeur**

UPDATE eleve SET moyenne = 19
    WHERE nom = 'Granger';
```

<aside>
💡

**Remarques**

- On a précisé la ligne où la modification doit avoir lieu avec la clause `WHERE`. Sans cette clause, toutes les valeurs de l'attribut *moyenne* auraient été modifiées.
- On peut modifier plusieurs attributs en les séparant par une virgule après le mot-clé `SET`.
</aside>

### **Exercice 5**

1. Rectifier la maison de Drago Malefoy (Serpentard, pour les incultes).
2. En une seule requête, rectifier l'orthographe de Ron Weasley et augmenter sa moyenne de 0.5 point (on peut faire un calcul sur l'attribut).

## DELETE

À utiliser avec précaution, le mot-clé `DELETE` permet de supprimer une ou plusieurs lignes.

```python
**Exemple de suppression d'une ligne**

DELETE FROM eleve
    WHERE nom = 'Malefoy';
```

Sans la clause `WHERE`, toutes les lignes de la table auraient été supprimées par la requête `DELETE FROM eleve;` .

### **Exercice 6**

Supprimer tous les élèves qui ne sont pas de la maison Gryffondor.