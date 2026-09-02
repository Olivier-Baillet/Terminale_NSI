# Module Internet

# Simulation

Après la théorie, passons maintenant à la pratique. Il est un peu difficile de mettre en place un réseau pour effectuer quelques tests. À la place nous allons utiliser un simulateur de réseau.
Il existe différents types de simulateurs : du plus simple au plus "professionnel". Nous allons utiliser un simulateur relativement simple à prendre en main, mais suffisamment performant : [filius](https://www.lernsoftware-filius.de/Herunterladen) (la page web est en allemand, mais le logiciel est disponible en français).

> *Si « Filius » n’est pas installé sur votre ordinateur, téléchargez le grâce à la feuille annexe : aide_installation_logiciel_Filius*
> 

### Rappel

*Quelques rappels avant de travailler avec le logiciel de simulation Filius :*

**Un switch** est une sorte de « multiprise
intelligente » qui permet de relier entre eux tous les ordinateurs appartenant à un même réseau, que nous appellerons "local".

Pour ce faire, un switch est composé d’un nombre plus ou moins important de prises RJ45 femelles (un câble ethernet (souvent appelé « câble réseau ») possède 2 prises RJ45 mâles à ses 2 extrémités).

![image.png](Module%20Internet/image.png)

**Un routeur** permet de relier ensemble plusieurs réseaux, il est composé d’un nombre plus ou moins important d’interfaces réseau (cartes réseau).

Les routeurs les plus simples que l’on puisse rencontrer permettent de relier ensemble deux réseaux (ils possèdent alors 2 interfaces
réseau), mais il existe des routeurs capables de relier ensemble une dizaine de réseaux.

![image.png](Module%20Internet/image%201.png)

- La commande `ipconfig` permet de connaitre la configuration réseau de
la machine sur laquelle elle est exécutée.
- La commande `"ping"` permet d'envoyer des paquets de données d'une machine A vers une machine B.
Si la commande est exécutée sur la machine A, le "ping" devra être suivi par l'adresse IP de la machine B
→ par exemple, si l'adresse IP de B est "192.168.0.2", on aura "ping 192.168.0.2"

Autre chose à retenir, vous allez apercevoir dans les vidéos un "netmask" (masque de réseau en français), vous devez juste savoir que :

Pour une adresse IP qui se termine :

- Par /8, on a un netmask qui est "255.0.0.0"
- Par /16, on a un netmask qui est "255.255.0.0
- Par /24, on a un netmask qui est "255.255.255.0"

Vous pouvez maintenant visionner la vidéo : [cliquez ici pour visualiser la vidéo](https://www.youtube.com/watch?v=nzuRSOwdF5I)

---

## Mission I

En utilisant le logiciel Filius, créez un réseau de 4 machines (M1, M2, M3 et M4).
L'adresse IP de la machine M1 est "192.168.1.1/24", choisissez les adresses IP des machines M2, M3 et M4.

*Aides :
Tous les éléments d’un même réseau devront avoir les trois premiers nombres de leurs adresses IP identiques et uniques. Le quatrième nombre sera à définir.*

Faites des `« ipconfig »` pour vérifier les adresses IP des 4 machines.
Effectuez un `"ping"` de la machine M2 vers la machine M4, vérifiez que
les paquets transmis sont bien reçus.

<aside>
❓

*Faîtes des captures d’écran (Windows+Maj+S)* (prendre toute la fenêtre) *:*

- *Du schéma,*
- *Du résultat de `« l’ipconfig »` de la machine M4,*
- *Du résultat du `« ping »`.*

*Copier-coller dans un traitement de texte.*

</aside>

---

Dans la vidéo ci-dessous, nous allons utiliser la commande `"traceroute"` : la commande "traceroute" permet de suivre le chemin qu'un paquet de données va suivre pour aller d'une machine à l'autre.

[cliquez ici pour visualiser la vidéo](https://www.youtube.com/watch?v=xyK6ThdQeR0)

## Mission II

En utilisant le logiciel Filius, créez 3 réseaux de 2 machines chacun.
Ces 3 réseaux seront reliés par un routeur.

Effectuez toutes les opérations de configuration nécessaires.

Aides :

Dans l’onglet « Général » du routeur il faudra cocher « Routage
automatique ».

Tous les éléments d’un même réseau (les machines et l’interface du routeur reliée à ce réseau) devront avoir les trois premiers nombres de leurs adresses IP identiques et uniques. Le quatrième nombre sera à définir.

Exemple :

- Réseau 1 : 192.168.1.
- Réseau 2 : 192.168.2.
- Réseau 3 : 192.168.3.

**Pour chaque machine, il faudra indiquer dans « Passerelle » l’adresse IP de l’interface routeur utilisée.**

Dans notre routeur, il faudra modifier son adresse IP :

- Mettre le numéro correspondant à notre sous réseau sur le troisième nombre.
- Mettre 254 pour le définir comme passerelle routeur sur le quatrième nombre

![image.png](Module%20Internet/image%202.png)

Dans chacun de nos ordinateurs reliés au routeur par ce réseau :

- Définir dans la passerelle, l’adresse IP du routeur

![image.png](Module%20Internet/image%203.png)

*Ici `“Gateway”` sera `“passerelle”` chez vous.*

Effectuez un ping entre deux machines d’un même réseau, vérifiez que
les paquets transmis sont bien reçus.

Effectuez un ping entre deux machines de deux réseaux différents,
vérifiez que les paquets transmis sont bien reçus.

<aside>
❓

*Faîtes des captures d’écran :*

- *Du schéma,*
- *Du résultat des « ping ».*

*Copier-coller dans le traitement de texte*

</aside>

---

## Mission III

Nous allons maintenant travailler sur un réseau plus complexe :

![](https://cours-snt-informatique-lycee-snt-d06fddf61a3f63a0de27fba7d2d55c.forge.apps.education.fr/img/DiagRes.png)

À l'aide du logiciel Filius, ouvrez le fichier [snt_sim_res.fls](https://cours-snt-informatique-lycee-snt-d06fddf61a3f63a0de27fba7d2d55c.forge.apps.education.fr/asset/snt_sim_res.fls)

Aide :
La commande "traceroute", suivie de l’adresse IP de destination, permet de voir le chemin qu'un paquet de données va suivre pour aller d'une machine à l'autre.

Faites un "traceroute" entre l'ordinateur M14 et l'ordinateur M9

<aside>
❓

*Faîtes une capture d’écran :*

- *Du résultat du « traceroute »*

*La copier-coller dans le traitement de texte.
Indiquer, le chemin parcouru par le paquet de données.*

</aside>

### Panne

Nous allons maintenant simuler une panne.

Aide :

Pour un routeur qui a plusieurs câbles, vous pouvez supprimer un câble en
mode conception 🔨.
 Il faut faire un clic droit sur le routeur, choisir dans le menu « configurer », puis **“Gérer les connexions”** et avec les “ ➕ ❕” en bas de « Interfaces locales », vous pouvez supprimer le
dernier port du bas.

Il faudra éviter d’utiliser « supprimer tous les câbles » puis redessinez des câbles car les adresses IP seront mises automatiquement et ne seront pas celles voulues ?

Supprimez le câble réseau qui relie le routeur F au routeur E, refaites
un "traceroute" entre M14 et M9.

<aside>
❓

*Faîtes une capture d’écran :*

- *Du résultat du « traceroute »*

*La copier-coller dans le traitement de texte.
Indiquer, le chemin parcouru par le paquet de données.*

</aside>

ATTENTION : cela peut ne pas fonctionner du premier coup, car la mise à jour des tables de routage n'est pas immédiate : vous pouvez essayer de faire un ping entre M14 et M9, si cela ne fonctionne pas (timeout), attendez quelques secondes et recommencez. Une fois que le ping fonctionne, vous pouvez faire le traceroute.
