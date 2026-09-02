# RPG

## 🎯 Objectif pédagogique

L’idée est qu’ils construisent **leur propre mini-moteur de RPG** :

un petit univers avec des **personnages** qui ont des **caractéristiques**, peuvent **interagir (combattre, se soigner, utiliser des objets)**, et où les classes (au sens POO) **représentent des entités du monde du jeu**.

---

## 🧩 Proposition de structure possible

Voici un **exemple d’organisation progressive**, de la base jusqu’à l’enrichissement possible selon le niveau des élèves.

---

### 🏗️ **Niveau 1 : Les bases — Deux classes reliées**

### Classe `Personnage`

| Élément | Exemple |
| --- | --- |
| **Attributs** | `nom`, `points_de_vie`, `attaque`, `defense`, `niveau` |
| **Méthodes** | • `afficher_statistiques()`
• `attaquer(autre_personnage)`
• `subir_degats(degats)`
• `est_vivant()` | |
|  |  |

### Classe `Arme`

| Élément | Exemple |
| --- | --- |
| **Attributs** | `nom`, `degats`, `rarete` |
| **Méthodes** | • `afficher_arme()`
• `ameliorer()` | |

→ **Lien entre les classes :**

Un `Personnage` **possède** une `Arme`.

C’est une **composition** classique.

---

### ⚔️ **Niveau 2 : Interaction entre objets**

Ajout d’une classe `Combat` qui fait interagir deux personnages.

### Classe `Combat`

| Élément | Exemple |
| --- | --- |
| **Attributs** | `joueur1`, `joueur2`, `tour_actuel` |
| **Méthodes** | • `demarrer_combat()`
• `effectuer_tour()`
• `verifier_vainqueur()` | |

→ Le `Combat` **utilise** les méthodes des `Personnage` (`attaquer`, `subir_degats`) pour simuler un affrontement.

---

### 🧙‍♂️ **Niveau 3 : Héritage et spécialisation**

Introduire des **sous-classes** de `Personnage` :

```python
class Guerrier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_de_vie=120, attaque=15, defense=10)
        self.arme = Arme("Épée", 10, "commune")

class Mage(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_de_vie=80, attaque=25, defense=5)
        self.mana = 50

    def lancer_sort(self, autre_personnage):
        degats = self.attaque + 10
        autre_personnage.subir_degats(degats)

```

→ Les élèves peuvent créer **leurs propres classes dérivées** selon leur imagination : `Voleur`, `Archer`, `Soigneur`, `Boss`, etc.

---

### 💎 **Niveau 4 : Classes complémentaires (optionnelles)**

| Classe | Rôle | Exemples de méthodes |
| --- | --- | --- |
| `Inventaire` | Contient les objets d’un personnage | `ajouter_objet()`, `utiliser_objet()` |
| `Objet` | Élément générique (potion, clé, artefact...) | `utiliser(cible)` |
| `Potion` | Hérite de `Objet` | `soigner(personnage)` |
| `Equipe` | Regroupe plusieurs personnages | `ajouter_membre()`, `moyenne_niveau()` |
| `Jeu` ou `Monde` | Gère l’ensemble des combats / personnages | `lancer_combat()`, `afficher_statistiques_globales()` |

---

## 💬 Quelques idées de **méthodes intéressantes et faciles à coder**

| Méthode | Description | Exemple de complexité |
| --- | --- | --- |
| `attaquer()` | Un personnage inflige des dégâts à un autre | `autre.points_de_vie -= self.attaque - autre.defense` |
| `soigner()` | Rend des PV à soi-même ou à un allié | `self.points_de_vie += 10` |
| `ameliorer_arme()` | Augmente les dégâts d’une arme | `self.degats += 2` |
| `gagner_experience()` | Fait monter le niveau après un combat | `self.niveau += 1` |
| `changer_arme()` | Associe une nouvelle arme à un personnage | `self.arme = nouvelle_arme` |
| `mort()` | Vérifie si les PV sont <= 0 | `return self.points_de_vie <= 0` |

---

## 🧭 Suggestions pour éviter qu’ils se perdent

- Encourage-les à **dessiner leur diagramme de classes** avant de coder.
- Imposes **un minimum de structure** (ex. au moins `Personnage` et une autre classe reliée).
- Donne-leur **un squelette de départ** s’ils bloquent :
    
    ```python
    class Personnage:
        def __init__(self, nom, pv, attaque):
            self.nom = nom
            self.pv = pv
            self.attaque = attaque
    
        def attaquer(self, autre):
            print(f"{self.nom} attaque {autre.nom} !")
            autre.pv -= self.attaque
    
    ```
    
- Les plus rapides peuvent ajouter :
    - une gestion de **tour par tour**
    - un peu d’**aléatoire** (avec `random.randint()`)
    - un système de **classes spécialisées** avec héritage

---

## 🎓 En résumé — Structure type conseillée

```
Personnage (classe de base)
│
├── Guerrier (héritée)
├── Mage (héritée)
│
├── Arme
│
└── Combat (fait interagir deux Personnage)

```

💡 Cette base est **suffisante pour 90 % des groupes**.

Les plus créatifs peuvent y ajouter : `Inventaire`, `Potion`, `Boss`, `Monde`, etc.

---

Souhaites-tu que je te fasse :

- 🧾 une **fiche d’aide élèves “aide à la conception RPG”** (avec tableau à remplir : classes / attributs / méthodes)
    
    ou
    
- 💻 un **squelette de code Python complet de base** (avec `Personnage`, `Arme`, `Combat`) à distribuer comme point de départ pour les plus bloqués ?

[Baptiste](RPG/Baptiste%2028b9d1894135803eb9cbd47e82c90f97.md)

[Juan](RPG/Juan%2028b9d189413580b4b437eaba2048ac68.md)