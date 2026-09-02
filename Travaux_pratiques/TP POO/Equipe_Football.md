# Equipe Football

---

## ⚽ Thème : Gestion d’équipes de football

### 🎯 Objectif général

Créer un petit programme permettant de **gérer des équipes de football**, leurs **joueurs**, leurs **matchs**, et éventuellement leurs **statistiques**.

---

## 🧱 Classes possibles

### 1. `Joueur`

**Attributs :**

- `nom` (str)
- `poste` (str) — ex : gardien, défenseur, milieu, attaquant
- `numero` (int)
- `buts` (int)
- `passes` (int)
- `cartons_jaunes` (int)
- `cartons_rouges` (int)

**Méthodes :**

- `marquer(nb=1)` → ajoute un ou plusieurs buts
- `donner_passe()` → incrémente les passes décisives
- `recevoir_carton(couleur)` → met à jour les cartons
- `afficher_statistiques()` → affiche les infos du joueur

---

### 2. `Equipe`

**Attributs :**

- `nom` (str)
- `joueurs` (liste de `Joueur`)
- `buts_marques` (int)
- `buts_encaisses` (int)
- `points` (int)

**Méthodes :**

- `ajouter_joueur(joueur)`
- `supprimer_joueur(nom)`
- `afficher_effectif()`
- `calculer_difference_buts()`
- `mettre_a_jour_resultat(buts_pour, buts_contre)`
- `statistiques_equipe()` → renvoie les infos globales

---

### 3. `Match`

**Attributs :**

- `equipe1`, `equipe2` (objets `Equipe`)
- `score_equipe1`, `score_equipe2`
- `date`

**Méthodes :**

- `jouer_match()` → permet d’entrer le score ou de le générer aléatoirement
- `afficher_resultat()`
- `attribuer_points()` → 3 pts victoire, 1 nul, 0 défaite

---

### 4. `Championnat`

*(optionnel pour groupes avancés)*

**Attributs :**

- `nom`
- `equipes` (liste d’objets `Equipe`)
- `calendrier` (liste de `Match`)

**Méthodes :**

- `ajouter_equipe()`
- `generer_calendrier()`
- `afficher_classement()`
- `simuler_saison()`

---

## 🔢 Fonctions indépendantes possibles

- `creer_joueur()` → saisie par l’utilisateur
- `creer_equipe()` → ajoute plusieurs joueurs
- `sauvegarder_donnees()` / `charger_donnees()` → gestion de fichiers
- `trouver_meilleur_buteur(equipe)`
- `rechercher_joueur(nom)`

---

## 💡 Idées d’extensions possibles

- Générer un **classement automatique** selon les résultats.
- Créer une **interface console** avec un menu :
    
    ```
    1. Ajouter un joueur
    2. Afficher le classement
    3. Jouer un match
    4. Quitter
    
    ```
    
- Sauvegarde dans un **fichier texte ou JSON**.
- Simulation aléatoire de buts à partir de statistiques.
- Ajouter un **système de transfert** entre équipes.
- Générer un **MVP** (meilleur joueur du championnat).
- Créer une version simplifiée d’un **FIFA Manager**.

---

## 🧩 Niveau progressif

| Niveau | Idées adaptées |
| --- | --- |
| **Débutant** | Classes `Joueur` et `Equipe` avec affichage des stats |
| **Intermédiaire** | Ajout de `Match`, saisie de résultats, calcul des points |
| **Avancé** | Gestion complète d’un championnat, sauvegarde de données |

---

Souhaitez-tu que je te fasse une **fiche consigne élève** au même format que celle du RPG (avec objectifs, livrables, barème et consignes de rendu) pour ce projet “Football” ?

Cela permettra de l’intégrer directement dans la séance 3 ou 4.