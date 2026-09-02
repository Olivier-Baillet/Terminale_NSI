# Equipe Rugby

---

## 🏉 Thème : Gestion d’équipes de Rugby

### 🎯 Objectif général

Créer un programme Python permettant de **gérer des équipes de rugby**, leurs **joueurs**, leurs **matchs**, et leurs **statistiques collectives** à travers une ou plusieurs classes interconnectées.

---

## 🧱 Classes principales

### 1. `Joueur`

**Attributs :**

- `nom` (str)
- `numero` (int)
- `poste` (str) — pilier, demi d’ouverture, arrière, etc.
- `essais` (int)
- `transformations` (int)
- `plaquages` (int)
- `cartons_jaunes` (int)
- `cartons_rouges` (int)

**Méthodes :**

- `marquer_essai()` → ajoute 1 essai (5 points)
- `reussir_transformation()` → ajoute 1 transformation (2 points)
- `effectuer_plaquage()` → ajoute 1 plaquage
- `recevoir_carton(couleur)` → ajoute un carton jaune ou rouge
- `afficher_stats()` → affiche les statistiques du joueur

---

### 2. `Equipe`

**Attributs :**

- `nom` (str)
- `ville` (str)
- `joueurs` (liste de `Joueur`)
- `points_marques` (int)
- `points_encaisses` (int)
- `victoires` (int)
- `defaites` (int)
- `matchs_nuls` (int)

**Méthodes :**

- `ajouter_joueur(joueur)`
- `supprimer_joueur(nom)`
- `afficher_effectif()`
- `mettre_a_jour_resultat(points_pour, points_contre)`
- `calculer_difference_points()`
- `afficher_statistiques()`

---

### 3. `Match`

**Attributs :**

- `equipe1`, `equipe2` (objets `Equipe`)
- `score_equipe1`, `score_equipe2`
- `meilleur_joueur` (objet `Joueur`)

**Méthodes :**

- `jouer_match()` → saisie ou génération aléatoire du score
- `attribuer_points()` → met à jour le classement (victoire = 4 pts, nul = 2 pts, bonus = 1 pt si défaite < 7 pts ou 4 essais)
- `afficher_resultat()`
- `selectionner_meilleur_joueur()`

---

### 4. `Championnat` *(optionnel mais intéressant pour les élèves rapides)*

**Attributs :**

- `nom`
- `equipes` (liste d’objets `Equipe`)
- `matchs` (liste d’objets `Match`)

**Méthodes :**

- `ajouter_equipe(equipe)`
- `generer_calendrier()`
- `afficher_classement()`
- `meilleure_attack()` / `meilleure_defense()`

---

## ⚙️ Fonctions possibles

- `creer_joueur()` → saisie d’un joueur depuis le clavier
- `creer_equipe()` → construit une équipe avec plusieurs joueurs
- `saisir_resultat_match()` → permet d’entrer le score manuellement
- `afficher_meilleur_marqueur(equipe)`
- `afficher_statistiques_generales(championnat)`
- `sauvegarder_donnees()` / `charger_donnees()`

---

## 💡 Extensions possibles

- Calcul des **bonus offensif** et **bonus défensif** (règle spécifique au rugby).
- Création d’un **tableau de classement** dynamique.
- Menu interactif :
    
    ```python
    1. Créer une équipe
    2. Ajouter un joueur
    3. Jouer un match
    4. Afficher le classement
    5. Quitter
    
    ```
    
- Enregistrement des matchs dans un fichier `.txt` ou `.json`.
- Génération aléatoire de scores ou de performances individuelles.
- Simulation d’un **Tournoi des 6 Nations** ou d’un **Top 14** miniature.

---

## 🧩 Niveau progressif

| Niveau | Idées adaptées |
| --- | --- |
| **Débutant** | Créer une équipe et gérer les statistiques des joueurs |
| **Intermédiaire** | Ajouter les matchs et le calcul des points du championnat |
| **Avancé** | Simuler une saison complète avec bonus et classement |

---

## 📄 Fiche consigne élève – *Projet Rugby POO*

### 🧭 Objectif

Concevoir un programme Python qui gère des **équipes de rugby** et leurs **matchs**, en appliquant les principes de la **programmation orientée objet** (classes, objets, méthodes, encapsulation).

---

### 🔧 Consignes

- Crée au moins **2 classes** (`Joueur`, `Equipe`).
- Chaque classe doit comporter des **attributs** et **méthodes cohérentes**.
- Le programme doit permettre :
    - d’ajouter et d’afficher les joueurs d’une équipe ;
    - de jouer au moins un match entre deux équipes ;
    - d’afficher le score final et les statistiques.
- Une **classe “Match”** ou “Championnat” est encouragée pour les groupes avancés.
- Le code doit être **commenté et lisible**.

---

### 💾 Rendu attendu

- Fichier `.py` documenté et fonctionnel.
- Au moins **5 méthodes** réparties entre les classes.
- Affichage clair en console.
- Une **présentation orale (2 à 3 minutes)** de votre projet pendant la séance 4.

---

### 🎯 Évaluation

| Critère | Points |
| --- | --- |
| Structure du code (classes, attributs, méthodes, cohérence) | /8 |
| Fonctionnalité du programme (ajout, match, stats) | /6 |
| Clarté du code et affichage | /3 |
| Créativité et présentation orale | /3 |
| **Total** | **/20** |

---

Souhaites-tu que je t’en fasse une **fiche distribuable aux élèves (PDF/Word)** avec en-tête, espaces à remplir (“Nom de l’équipe”, “Classes utilisées”, “Description du projet” etc.) ?

Je peux aussi y ajouter une **grille d’autoévaluation** (élève coche ses réussites).

[Sacha](Equipe%20Rugby/Sacha%2028b9d189413580589744da198e3788cb.md)