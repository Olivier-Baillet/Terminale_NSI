# Serveur DNS (Domain Name System)

## Objectifs

| Contenus  | Capacités attendues |
| --- | --- |
| **Adresses symboliques et serveurs DNS**
 | Sur des exemples réels, retrouver une adresse IP à partir d’une adresse symbolique et inversement. |

Avec **Filius**, nous pouvons simuler et analyser les processus impliqués dans la communication entre un navigateur et un serveur distant.

---

# Adresses symboliques et serveur DNS

### Mise en place du réseau

Réaliser **2 réseaux de 3 machines chacun**, reliés par un **routeur**.

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image.png)

### Réseau de gauche :

Les trois machines du réseau de gauche
auront pour adresses IP :

- 192.168.0.1
- 192.168.0.2
- 192.168.0.3

### Réseau de droite :

Les trois machines du réseau de droite
auront pour adresses IP :

- 192.168.1.1
- 192.168.1.2
- 192.168.1.3

### Routeur :

Spécifier les adresses IP des interfaces du routeur, sans oublier de cocher “**Routage Automatique”.**

- Interface gauche : 192.168.0.254
- Interface droite : 192.168.1.254

### Passerelle :

Spécifier pour chaque machine d’un réseau, l’adresse IP de sa passerelle qui est l’adresse IP de son routeur référent.

### Test de connexion

Faites un `ping` :

- De la machine d’adresse    IP 192.168.0.1
- Vers la machine d’adresse IP 192.168.1.1
- Puis vérifier que cela fonctionne

---

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%201.png)

### Serveur Web ⬆️

Sur 192.168.1.1 :

- Installer serveur web (**Web Server)**
- Lancer l’application → bouton **Start**

### Navigateur Web ⬇️

Sur 192.168.0.1 :

- Installer **navigateur web** (**Web Browser)**
- Taper dans la barre d’adresse : [http://192.168.1.1](http://192.168.1.1/)

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%202.png)

> La connexion fonctionne, mais ce n’est pas ainsi qu’on identifie un serveur sur Internet.
> 

---

## Le rôle du serveur DNS

On contacte normalement un serveur via une **URL**, pas via une adresse IP.
Un **système de noms de domaine (ou DNS**) traduit l’URL en adresse IP.

<aside>
💡

### A1

**Appelez le professeur pour valider**

</aside>

---

# Ajout et configuration d’un serveur DNS

Nous allons maintenant ajouter un **serveur DNS** afin de permettre l’utilisation d’une **adresse web (URL)** au lieu d’une adresse IP.

---

### 1. Ajout du poste « Serveur DNS »

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%203.png)

1. Ajouter un **nouveau poste fixe** dans le réseau.
2. Nommer ce poste : **SERVEUR DNS**.
3. Configurer ses paramètres réseau :
    - **Adresse IP :** `192.168.3.100`
    - **Passerelle :** `192.168.3.254`

---

### 2. Ajout d’une troisième interface au routeur

Le routeur doit maintenant être relié à **trois réseaux**.

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%204.png)

1. Sélectionner le **routeur**.
2. Aller dans l’onglet **« Général »**.
3. Cliquer sur **« Gérer les Connexions »**.
4. Ajouter une nouvelle interface avec le bouton **« + »**.
5. Fermer avec **« Fermer»** pour enregistrer.
6. Renseigner l’adresse IP de cette nouvelle interface :
    - **Adresse IP :** `192.168.3.254`

---

### 3. Configuration des ordinateurs pour utiliser le DNS

Pour que tous les postes puissent utiliser le serveur DNS :

- Ajouter l’adresse IP du serveur DNS **`192.168.3.100`** dans la configuration réseau de **tous les ordinateurs** du réseau.

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%205.png)

---

### 4. Installation et paramétrage du serveur DNS

1. Sélectionner le poste **SERVEUR DNS**.
2. Installer l’application **« Serveur DNS »**.
3. Lancer l’application.
4. Créer une nouvelle association :
    - **Nom de domaine :** `www.snt.fr`
    - **Adresse IP associée :** `192.168.1.1`
5. Cliquer sur le bouton **« Ajouter»**.
6. Démarrer le serveur DNS avec le bouton **« Start »**.

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%206.png)

---

### 5. Test de la configuration DNS

Depuis le poste **192.168.0.1** :

1. Ouvrir l’application **Navigateur internet**.
2. Taper l’adresse suivante dans la barre d’adresse :  [http://www.snt.fr](http://www.snt.fr/)

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%207.png)

<aside>
💡

### A2

**Appelez le professeur pour valider**

</aside>

---

## Commande « host »

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%208.png)

Et pour finir, testons simplement la commande host [www.snt.fr](http://www.snt.fr/)
Nous voyons que le DNS fait son travail en nous fournissant l’adresse IP du serveur qui héberge la page internet.
[www.snt.fr](http://www.snt.fr/) → 192.168.1.1

<aside>
💡

### A3

**Appelez le professeur pour valider**

</aside>

---

# Synthèse DNS

Le serveur **DNS (Domain Name System)** permet de trouver l’adresse **numérique (adresse IP)** à partir d’une adresse **symbolique**.

Dans notre exemple, le serveur DNS a permis d’associer l’adresse
symbolique [www.snt.fr](http://www.snt.fr/) à l’adresse numérique 192.168.1.1

---

### Replacer les étapes d’une requête DNS :

- Requête : [http://172.217.18.195](http://172.217.18.195/)
- Réponse : Envoi de la page recherche Google
- Question : Quelle est l’adresse de [www.google.fr](http://www.google.fr/) ?
- Réponse : 172.217.18.195

Acteurs :

- Serveurs DNS
- Votre ordinateur
- Serveurs Google

Adresse symbolique de Google : __________________
Adresse numérique de Google : __________________

![image.png](Serveur%20DNS%20(Domain%20Name%20System)/image%209.png)

<aside>
💡

### A4

**Compléter le document**

</aside>

---
