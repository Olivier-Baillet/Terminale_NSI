# TP Arbres binaires (récursif)

<aside>
💡

## **Objectif**

Dans ce TP, il s'agit d'utiliser l'implémentation POO d'un arbre binaire et d'implémenter des fonctions:

- de calcul de taille
- de calcul de hauteur
- de parcours (largeur, préfixe, infixe, postfixe)
</aside>

Reprendre le fichier `arbre_binaire.py` et compléter au fur et à mesure la classe `AB`.

> **Stratégie :**
*Dès que possible, il s'agit d'exploiter le caractère **récursif** de la structure d'arbre pour écrire les méthodes suivantes...*
> 

### **Exercice 1 : Taille et hauteur**

1. Écrire une méthode renvoyant la taille d'un arbre binaire.
2. Écrire une méthode renvoyant la hauteur d'un arbre binaire.
    
    *Indice en bas de votre écran:* la fonction `max` est autorisée.
    

---

### **Exercice 3 : DFS**

Écrire les méthodes `prefixe`, `infixe` et `postfixe` parcourant l'arbre en profondeur d'abord selon les algorithmes correspondants (page précédente). Le traitement de la racine consistera en un affichage (`print`).

### **Exercice 4 : recherche d'une valeur**

Écrire une méthode permettant de déterminer si un arbre contient une valeur donnée. La méthode renverra un booléen selon le résultat de la recherche.