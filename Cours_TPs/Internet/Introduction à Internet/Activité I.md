# Activité I :

Dix élèves, possédant tous et toutes un ordinateur, se retrouvent pour jouer à un jeu vidéo en réseau, en connectant leurs ordinateurs les uns aux autres avec des câbles. Leurs contraintes sont :

- utiliser le moins de câbles possibles ;
- si un câble est coupé par accident, les ordinateurs peuvent toujours communiquer ensemble ;
- si un ordinateur cesse de fonctionner, les autres ordinateurs peuvent
toujours communiquer ensemble ;
- aucun joueur ou joueuse ne peut tricher en bloquant, en écoutant ou
en modifiant les communications qui passent par son ordinateur.

Dans toute la suite, on représente le réseau par un graphe, où les sommets sont les ordinateurs, et les arêtes les câbles.
On étudie différentes manières de connecter les ordinateurs entre eux.

1. Dans chacun des cas, on répondra aux questions suivantes.
    1. Représenter cette configuration par un graphe.
    2.  Combien de câbles sont nécessaires ?
    3. Si un câble ou un ordinateur cesse de fonctionner, les autres ordinateurs peuvent-ils continuer à communiquer ?
    4. Un ordinateur peut-il bloquer, espionner ou modifier les communications entre les autres ordinateurs ?
    
    <aside>
    💡
    
    1. **Réseau centré :** un ordinateur au centre est connecté par un câble à chacun des autres.
    2. **Réseau décentralisé :** un ordinateur est au centre, et trois ordinateurs sont connectés à lui. Deux autres ordinateurs sont connectés à chacun de ces trois ordinateurs.
    3. **Graphe complet :** chaque ordinateur est relié par un câble à chacun des autres ordinateurs.
    4. Réseau distribué : les ordinateurs sont placés au hasard dans la salle, et chacun est directement relié à trois ordinateurs parmi les plus proches.
    </aside>
    
2. Bilan
    1.  Les contraintes sont-elles compatibles ?
    2. Pour vérifier au mieux les trois conditions, quel semble être le meilleur réseau ?