Par groupes de 2 ou 3, vous allez construire un petit univers où des entités agissent les unes sur les autres. Le RPG est un thème possible, mais pas le seul.

## Ce que vous devez construire

Vous codez un **moteur de simulation** : un programme générique qui fait vivre des entités, quel que soit l'univers. Le thème n'est qu'un choix de données.

## Les classes de base

| Concept | Classe type | Rôle |
| --- | --- | --- |
| Une chose qui a un état | `Entite` | nom, caractéristiques numériques, `est_actif()` |
| Quelque chose qui agit | `Acteur` (ou la même classe) | choisit et exécute des actions |
| Quelque chose qu'on utilise | `Objet` | effet sur une entité, éventuellement à usage limité |
| Un endroit ou un conteneur | `Lieu` / `Inventaire` | contient des entités et des objets |
| Le chef d'orchestre | `Moteur` / `Jeu` | boucle de tours, conditions de fin |

Vous ne codez donc pas « un guerrier avec une épée », mais **une entité avec des caractéristiques, une action qui les modifie, un objet qui a un effet**. Le RPG devient un thème parmi d'autres.

## Choisissez votre thème

- **RPG classique** : combat, soin, potions.
- **Écosystème** : proies et prédateurs, énergie, reproduction, nourriture comme objet.
- **Gestion de ferme ou de jardin** : plantes qui poussent, arrosage, récolte, météo comme événement.
- **Restaurant ou cuisine** : clients avec patience, plats comme objets, cuisiniers qui agissent.
- **Station spatiale ou colonie** : oxygène, énergie, pannes, réparations.
- **Tournoi sportif** : équipes avec forme physique, matchs, blessures et soins.
- **Jeu de cartes** : cartes comme objets, joueurs comme entités.

Prenez un thème de cette liste, ou proposez le vôtre à votre professeur pour validation. Le squelette de classes reste le même quel que soit le thème.

## Les étapes du projet

Le projet avance par paliers. À la fin de chacun, montrez votre travail avant de passer au suivant.

1. **Conception sur papier** (1 séance) : listez vos classes, leurs attributs et leurs méthodes, avec un diagramme simple. Votre professeur le valide avant que vous codiez.
2. **Une entité** : écrivez une classe avec attributs, `__init__`, `__str__` et des méthodes qui modifient l'état (`subir`, `recuperer`). Protégez-vous des valeurs absurdes (points de vie négatifs).
3. **Interaction entre deux entités** : écrivez une méthode qui prend un autre objet en paramètre (attaque, soin, échange).
4. **Objets et inventaire** : créez une classe `Objet` et une liste d'objets dans l'entité, avec des objets d'usage unique.
5. **Le moteur** : codez la boucle de tours, le choix des actions (menu ou aléatoire) et la condition de fin.
6. **Extensions au choix** : sauvegarde en JSON, événements aléatoires, nouveau type d'entité, interface graphique simple.

## Ce que votre code doit respecter

Voici les critères de validation :

- Au moins 3 classes qui collaborent. Une classe en contient d'autres (**composition**) : par exemple, un `Lieu` contient une liste d'entités.
- Aucune variable globale pour l'état du jeu. Tout passe par les objets.
- L'aléatoire doit pouvoir être figé (`random.seed`), pour que vos tests soient reproductibles.
- Un petit jeu de tests (`assert`) par classe.
- Une documentation minimale : docstrings, plus un `README` qui décrit votre univers.

L'**héritage** et le polymorphisme sont en extension : si vous avez de l'avance, essayez par exemple une classe `Guerrier(Entite)`.

## Travailler en groupe

- Répartissez les rôles et faites-les tourner : une personne écrit les tests, une autre le moteur, la dernière les classes de contenu.
- Utilisez un fichier par classe pour limiter les conflits.
- À chaque palier, chaque membre doit pouvoir expliquer une classe qu'il n'a pas écrite.

## Comment vous serez évalués

- Respect du squelette et des contraintes (classes, composition, tests).
- Qualité de la conception : attributs cohérents, méthodes aux responsabilités claires.
- Fonctionnement du moteur.
- Lisibilité et documentation.
- Soutenance courte : vous expliquez une classe, vous faites une démonstration, vous répondez à une question du genre « comment ajouter un nouveau type d'objet ? ».

## Pour bien démarrer

Commencez petit : une seule classe qui fonctionne et que vous testez vaut mieux que cinq classes à moitié écrites.
