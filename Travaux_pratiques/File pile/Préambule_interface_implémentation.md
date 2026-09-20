# Préambule : interface ≠ implémentation

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/BO1.png)

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/BO2.png)

Les structures que nous allons voir peuvent s'envisager sous deux aspects :

• le côté utilisateur, qui utilisera une interface pour manipuler les données.
• le côté concepteur, qui aura choisi une implémentation pour construire la structure de données.

> 
> 
> 
> ### **Un exemple d'interface et d'implémentation**
> 
> • Le volant et les pédales d'une voiture constituent une partie de son **interface**.
> • L'**implémentation** va désigner tous les mécanismes techniques qui sont mis en œuvre pour que (par exemple) le mouvement de rotation du volant aboutisse à un changement de direction des roues.
> • La standardisation des interfaces fait qu'un utilisateur peut passer sans problème d'une voiture à une autre, même si l'implémentation est complètement différente.
> 
> ![image.png](Préambule_interface_implémentation/image.png)
> 

Nous avons déjà abordé ces deux aspects lors de la découverte de la Programmation Orientée Objet.
Le principe d'encapsulation fait que l'utilisateur n'a qu'à connaître l'existence des méthodes disponibles, et non pas le contenu technique de celle-ci. Cela permet notamment de modifier le contenu technique (l'implémentation) sans que les habitudes de l'utilisateur (l'interface) ne soient changées.

# **1. Structures de données linéaires**

## **1.1 À chaque donnée sa structure**

En informatique comme dans la vie courante, il est conseillé d'adapter sa manière de stocker et de traiter des données en fonction de la nature de celles-ci :

• Le serveur d'un café, chargé de transporter les boissons du comptoir aux tables des clients, n'utilisera pas un sac en plastique pour faire le transport : il préfèrera un plateau.
• Le chercheur de champignons, lui, n'utilisera pas un plateau pour stocker ses trouvailles : il préfèrera un panier.
• Pour stocker des chaussettes, on préfèrera les entasser dans un tiroir (après les avoir appairées), plutôt que de les suspendre à des cintres.

De même en informatique, pour chaque type de données, pour chaque utilisation prévue, une structure particulière de données se revèlera (peut-être) plus adaptée qu'une autre.

### **1.1.1 Données linéaires**

Intéressons nous par exemple aux **données linéaires**. Ce sont des données qui ne comportent pas de *hiérarchie* : toutes les données sont de la même nature et ont le même rôle. Par exemple, un relevé mensuel de températures, la liste des élèves d'une classe, un historique d'opérations bancaires...

Ces données sont «plates», n'ont pas de sous-domaines : la structure de **liste** paraît parfaitement adaptée.

Lorsque les données de cette liste sont en fait des couples (comme dans le cas d'une liste de noms/numéros de téléphone), alors la structure la plus adaptée est sans doute celle du **dictionnaire**.

Les listes et les dictionnaires sont donc des exemples de structures de **données linéaires**.

### **1.1.2 Données non-linéaires**

Même si ce n'est pas l'objet de ce cours, donnons des exemples de structures adaptées aux données non-linéaires :

Si une liste de courses est subdivisée en "rayon frais / bricolage / papeterie" et que le rayon frais est lui-même séparé en "laitages / viandes / fruits & légumes", alors une structure d'**arbre** sera plus adaptée pour la représenter. Les structures arborescentes seront vues plus tard en Terminale.

Enfin, si nos données à étudier sont les relations sur les réseaux sociaux des élèves d'une classe, alors la structure de **graphe** s'imposera d'elle-même. Cette structure sera elle-aussi étudiée plus tard cette année.

## **1.2 Comment seront traitées ces données linéaires ? Introduction des listes, des piles et des files**

La nature des données ne fait pas tout. Il faut aussi s'intéresser à la manière dont on voudra les traiter :

- À quelle position les faire entrer dans notre structure ?
- À quel moment devront-elles en éventuellement en sortir ?
- Veut-on pouvoir accéder rapidement à n'importe quel élément de la structure, ou simplement au premier ? ou au dernier ?

Lorsque ces problématiques d'entrée/sortie n'interviennent pas, la structure «classique» de liste est adaptée. Mais lorsque celle-ci est importante, il convient de différencier la structure de **pile** de celle de **file**.

### **1.2.1 Les piles (*stack*)**

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/assiettes2.png)

Une structure de **pile** (penser à une pile d'assiette) est associée à la méthode **LIFO** (Last In, First Out) :

les éléments sont empilés les uns au-dessus des autres, et on ne peut toujours dépiler que l'élément du haut de la pile. Le dernier élément à être arrivé est donc le premier à être sorti.

![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/gifpile.webp)

#### **Exemples de données stockées sous forme de pile**

- lors de l'exécution d'une fonction récursive, le processeur empile successivement les appels à traiter : seule l'instruction du haut de la pile peut être traitée.

![Fibonacci](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/pile_fibo.webp)

- dans un navigateur internet, la liste des pages parcourues est stockée sous forme de pile : la fonction «Back» permet de «dépiler» peu à peu les pages précédemment parcourues :
    
    ![](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/history.png)
    
- lors d'un Devoir Surveillé, la dernière copie remise sur le bureau du professeur est (souvent) la première corrigée.

### **1.2.2 Les files (*queue*)**

![image](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/queue.png)

Une structure de **file** (penser à une file d'attente) est associée à la méthode **FIFO** (First In, First Out) :

les éléments sont enfilés les uns à la suite des autres, et on ne peut toujours défiler que l'élément du haut de la file. Le premier élément à être arrivé est donc le premier à en sortir. Sinon ça râle dans la file d'attente.

![un bien joli gif](https://glassus.github.io/terminale_nsi/T1_Structures_de_donnees/1.1_Listes_Piles_Files/data/giffile.webp)

#### **Exemples de données stockées sous forme de file :**

- les documents envoyés à l'imprimante sont traitées dans une file d'impression.
- la «queue» à la cantine est (normalement) traitée sous forme de file.

### **1.2.3 Le problème du stockage : transformer les piles en files**

Dans les entrepôts de stockage, comme dans les rayons d'un supermarché, la structure naturelle est celle de la **pile** : les gens attrapent l'élément situé devant eux («en haut de la pile»). Si les employés du supermarché remettent en rayon les produits plus récents sur le dessus de la pile, les produits au bas de la pile ne seront jamais choisis et périmeront.

Ils doivent donc transformer la pile en file : lors de la mise en rayon de nouveaux produits, ceux-ci seront placés derrière («au bas de la file») afin que partent en priorité les produits à date de péremption plus courte. On passe donc du LIFO au FIFO.

Certains dispositifs permettent de le faire naturellement :Ci-dessous, une file... de piles (électriques). Le chargement par le haut du distributeur fait que celle qui sera sortie (en bas) sera celle qui aura été rentrée en premier (par le haut). Ce FIFO est donc provoqué naturellement par la gravité (et un peu d'astuce).

![image.png](Préambule_interface_implémentation/image%201.png)

*On notera que cette problématique est universelle : voir par exemple [ce site](https://www.mecalux.fr/blog/methode-lifo-fifo-peps).*

Après avoir présenté rapidement ces trois types de données linéaires, nous allons maintenant les étudier plus en détail, et proposer pour chacune d'elles une interface et plusieurs implémentations.
