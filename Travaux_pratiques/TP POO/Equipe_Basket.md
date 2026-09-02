# Equipe Basket

---

Excellent choix 🏀 ! Le thème **“Équipe de basket”** se prête très bien à un projet orienté objet, tout en permettant aux élèves de manipuler les mêmes notions qu’avec le projet “Football” : classes, attributs, méthodes, listes, boucles, entrées utilisateur, etc.

Voici donc une **proposition complète** pour un **projet Python sur le thème “Basket”**, avec idées de classes, fonctions, extensions, et une fiche consigne possible à la fin.

---

## 🏀 Thème : Gestion d’équipes de basket

### 🎯 Objectif général

Créer un petit programme permettant de **gérer des équipes de basket**, leurs **joueurs**, leurs **matchs**, et leurs **statistiques individuelles et collectives**.

---

## 🧱 Classes principales

### 1. `Joueur`

**Attributs :**

- `nom` (str)
- `numero` (int)
- `poste` (str) — meneur, ailier, pivot, etc.
- `points` (int)
- `passes` (int)
- `rebonds` (int)
- `interceptions` (int)
- `contres` (int)

**Méthodes :**

- `marquer(nb_points)` → ajoute des points
- `donner_passe()` → ajoute une passe décisive
- `prendre_rebond()` → ajoute un rebond
- `afficher_stats()` → affiche les statistiques du joueur

---

### 2. `Equipe`

**Attributs :**

- `nom` (str)
- `ville` (str)
- `joueurs` (liste de `Joueur`)
- `victoires` (int)
- `defaites` (int)
- `points_marques` (int)
- `points_encaisses` (int)

**Méthodes :**

- `ajouter_joueur(joueur)`
- `supprimer_joueur(nom)`
- `afficher_effectif()`
- `moyenne_points_equipe()`
- `mettre_a_jour_resultat(points_pour, points_contre)`
- `ratio_victoire()`

---

### 3. `Match`

**Attributs :**

- `equipe1`, `equipe2` (objets `Equipe`)
- `score_equipe1`, `score_equipe2`
- `meilleur_joueur` (objet `Joueur`)

**Méthodes :**

- `jouer_match()` → saisie ou génération aléatoire du score
- `afficher_resultat()`
- `attribuer_victoire()` → mise à jour des stats d’équipes
- `nom_mvp()` → affiche le meilleur joueur du match

---

### 4. `Championnat`

*(facultatif mais motivant pour les groupes avancés)*

**Attributs :**

- `nom`
- `equipes` (liste de `Equipe`)
- `matchs` (liste de `Match`)

**Méthodes :**

- `ajouter_equipe(equipe)`
- `generer_calendrier()`
- `afficher_classement()`
- `simuler_saison()`

---

## ⚙️ Fonctions possibles

- `creer_joueur()` → saisie des infos d’un joueur
- `creer_equipe()` → crée une équipe avec plusieurs joueurs
- `saisir_resultat()` → entrée manuelle des scores
- `afficher_meilleur_marqueur(equipe)`
- `afficher_moyenne_points(championnat)`
- `sauvegarder_donnees()` / `charger_donnees()` → gestion de fichiers

---

## 💡 Extensions possibles

- Générer les scores de match **aléatoirement** (par exemple entre 60 et 120 points).
- Calculer le **MVP du championnat** (meilleur joueur global).
- Créer un **menu textuel** pour naviguer dans le programme :
    
    ```
    1. Créer une équipe
    2. Ajouter un joueur
    3. Jouer un match
    4. Afficher le classement
    5. Quitter
    
    ```
    
- Ajouter un **système de statistiques avancées** : efficacité, rebonds moyens, etc.
- Enregistrer les données dans un fichier `.txt` ou `.json`.
- Créer une **simulation automatique** de saison complète.

---

## 🧩 Niveau progressif

| Niveau | Idées adaptées |
| --- | --- |
| **Débutant** | Créer une équipe et afficher les stats des joueurs |
| **Intermédiaire** | Ajouter des matchs et mettre à jour les victoires/défaites |
| **Avancé** | Gestion d’un championnat complet avec classement et MVP |

---

## 📄 Fiche consigne élève (version courte)

### Projet Python : *Gestion d’équipes de Basket*

**Objectif :** concevoir un mini-programme de gestion d’équipes et de matchs de basket en utilisant les classes et méthodes.

---

### 💬 Consignes

- Crée au moins **2 classes** (`Joueur`, `Equipe`)
- Chaque classe doit comporter **des attributs** (informations) et **des méthodes** (actions).
- Tu peux ensuite ajouter une classe `Match` ou `Championnat` si tu veux aller plus loin.
- Le programme doit permettre :
    - d’ajouter des joueurs dans une équipe ;
    - de jouer un match et d’afficher le score ;
    - d’afficher les statistiques (joueurs et équipes).

---

### 💾 Rendu attendu

- Un fichier `.py` documenté.
- Au moins **5 méthodes** fonctionnelles.
- Un affichage clair en console (print, menus, etc.).
- Une **présentation orale (2 à 3 min)** en séance 4 : fonctionnement + choix de conception.

---

### 🎯 Évaluation

| Critère | Points |
| --- | --- |
| Fonctionnalité et structure du code (classes, méthodes, fonctions) | /8 |
| Respect du thème et clarté de l’affichage | /4 |
| Cohérence du projet et créativité | /4 |
| Présentation orale claire et structurée | /4 |
| **Total** | **/20** |

---

Souhaites-tu que je te fasse une **fiche élève complète** (prête à distribuer) au format du projet RPG/Foot, avec en-tête, barème détaillé et zone “Nom/Prénom/Équipe” ?

Je peux aussi te proposer une **version simplifiée (seconde)** ou une **version approfondie (première)** selon ta séquence.

[Pablo](Equipe%20Basket/Pablo%2028b9d189413580f382c5cccbc34b2a33.md)

[Marcus](Equipe%20Basket/Marcus%2028b9d18941358002b944e2864b2babd0.md)