# Les protocoles TCP et IP

![internet](https://nsinfo.yo.fr/images/reseau_internet_terre.jpg)

Les informations circulant sur internet sont découpées en **paquets** de bits. Chaque paquet reçoit en en-tête les adresses **IP** de son émetteur et de son destinataire. Cette dernière est utilisée par les **routeurs** répartis sur tout le réseau qui se transmettent les paquets jusqu’à leur destinataire. C'est ce **protocole IP** qui assure l'envoi des paquets aux bons endroits.

Les paquets reçoivent aussi un en-tête **TCP**, un protocole qui assure leur transport et leur intégrité.

## **Le protocole IP**

Internet est défini par le **protocole IP (Internet Protocol)**, ensemble de normes qui permettent d’identifier et de nommer de façon uniforme tous les ordinateurs ou objets qui lui sont connectés.

Il uniformise l’accès à tous les ordinateurs, les téléphones et les objets connectés.

Lorsque vous tapez dans la barre d'adresse de votre navigateur «https://www.wikipedia.org/», votre ordinateur va chercher à entrer en communication avec un autre ordinateur se trouvant probablement à des milliers de kilomètres de chez vous. Pour pouvoir établir cette communication, il faut bien sûr que les 2 ordinateurs soient « reliés ». (en réseau >>> Internet).

Afin de pouvoir s'identifier, tout ordinateur possède une adresse sur un réseau : **son adresse IP**.

Une adresse IP est de la forme "74.125.133.94" (cette adresse IP correspond au serveur de google "google.fr")

Les adresses IP sont de la forme : "a.b.c.d", avec a, b, c et d compris entre 0 et 255.

N.B. Une autre norme est en train d'être déployée, la norme IPV6 (alors que les adresses IP vues ci-dessus appartiennent à la norme IPV4). Pourquoi cette nouvelle norme ? Parce qu' avec le système IPV4, nous allons manquer d'adresses IP disponibles sur internet dans les prochaines années en raison du trop grand nombre d'objet connecté (téléphone, enceinte, tv, PC, ...).

<aside>
💡

### **Exercice 1 :**

Nous allons utiliser un site basé en suisse ( http://en.dnstools.ch/) qui permet de lancer des requêtes simples sur Internet.

1. Connectez vous au site http://en.dnstools.ch/
2. Déterminer votre adresse IP en utilisant la fonction MY IP
3. Comparer avec vos voisins. Comment expliquez-vous cela?

### **Exercice 2 :**

En utilisant la fonction PING qui permet de lancer une requête Ping,

1. rechercher les adresses IP des 4 sites suivants :
    - wikipedia.org
    - elysee.fr
    - google.com
    - google.fr
2. Des paquets sont-ils perdus ?
3. Quel est le temps moyen de réponse obtenu pour ces sites?
Expliquer les différences entre les temps de traitement.

Il est possible de réaliser un ping avec l'invite de commandes cmd directement sur windows.

```python
ping wikipedia.org
```

</aside>

## **Le protocole TCP**

**l'IP** est accompagné de protocoles de transmission pour transférer l’information par paquets, le principal étant **TCP (Transmission Control Protocol)**.

Le protocole **TCP** permet le transfert de données en respectant les règles d'adressage, de transport et de contrôle d'intégrité des paquets.

Chaque paquet qui circule sur Internet à une en-tête avec des données supplémentaire ajouté par le **protocole IP** et le **protocole TCP**. Les paquets sont numérotés pour les rassembler dans l'ordre une fois transmis et vérifier leur arrivées à bon port.

![](https://nsinfo.yo.fr/images/tcp_ip.PNG)

<aside>
💡

### **Exercice 3 :**

Ordinateur A veut envoyer une photo à Ordinateur B. Cette photo est découpée en paquets de 1500 octets maximum.

| En_tête IP | En tête TCP | Données |
| --- | --- | --- |
| Emetteur : 107.191.220.153 | Envoie du N°1976 sur 2013 | 01110101010101010101010101 |
| Destinataire : 76.106.002.153 | réceptions du N°1976 sur 2013 | 01110101010101010101010101 |

![](https://nsinfo.yo.fr/images/TCP_IP_4.png)

1. Décrire le schéma ci-dessus qui explique le protocole TCP.
    
    Ecrire au minimum une ligne d’explication pour chacune de ces quatre étapes.
    
</aside>

## **A retenir :**

> **IP (Internet Protocol):**
Protocole réseau qui définit les échanges en donnant aux ordinateurs une adresse unique sur le réseau
> 
> 
> **IP :**
> Adresse d'une machine sur le réseau
> 
> **TCP(transmission Control Protocol):**
> Protocole qui gère la connexion et la transmission des données
> 
> **Paquet:**
> Unité de données
> 
> **Routeur:**
> Machine transmettant des données sur le réseau pour qu'elles atteignent leur destinataire
> 
> **Requête:**
> Demande d'information d'un client à un serveur
>
