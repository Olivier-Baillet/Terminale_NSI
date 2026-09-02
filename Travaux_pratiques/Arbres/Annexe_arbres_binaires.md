# Annexe : arbres binaires

```python
#-------------------------------------------------------------------------------
# TP Terminale NSI : arbres binaires
#-------------------------------------------------------------------------------
import copy
from random import randint,shuffle
from binarytree import Node

#------------------------------------------------------------------------------
# Classe Arbre : permet de construire un arbre binaire
#------------------------------------------------------------------------------
class Arbre():
	nom = None

    def __init__(self,nom):
    self.nom = nom
        """
        Constructeur de la classe Arbre
        @param nom: nom de la racine de l'arbre
        """
        pass

    def set_nom(self,nom):
        """
        renseigne le nom de la racine de l'arbre
        @param nom: nom de la racine de l'arbre
        @return:
        """
        pass

    def insere_fils_gauche(self, fils_gauche):
        """

        @param fils_gauche: sous-arbre gauche de type Arbre Ã  insÃ©rer
        @return:
        """
        pass

    def insere_fils_droit(self, fils_droit):
        """

        @param fils_droit: sous-arbre droit de type Arbre Ã  insÃ©rer
        @return:
        """
        pass

    def parcours_prefixe(self):
        """

        @return: le parcours prÃ©fixe : une liste de noeud dans l'ordre prÃ©fixe
        """
        parcours = []
        self.parcours_prefixe_recur(parcours)
        return parcours

    def parcours_prefixe_recur(self,parcours):
        """

        @param parcours:
        @return:
        """
        if self.nom != None:
            parcours.append(self.nom)
        if self.fils_gauche != None:
            self.fils_gauche.parcours_prefixe_recur(parcours)
        if self.fils_droit != None:
            self.fils_droit.parcours_prefixe_recur(parcours)

    def parcours_infixe(self):
        """

        @param parcours:
        @return: le parcours infixe : une liste de noeud dans l'ordre infixe
        """
        parcours = []
        self.parcours_infixe_recur(parcours)
        return parcours

    def parcours_infixe_recur(self,parcours):
        """

        @param parcours: le parcours infixe : une liste de noeud dans l'ordre infixe
        @return:
        """
        pass

    def parcours_postfixe(self):
        """

        @return: le parcours postfixe : une liste de noeud dans l'ordre infixe
        """
        parcours = []
        self.parcours_postfixe_recur(parcours)
        return parcours

    def parcours_postfixe_recur(self,parcours=[]):
        """

        @param parcours:
        @return:
        """
        pass

    def hauteur(self):
        """
        MÃ©thode rÃ©cursive qui calcule la hauteur d'un arbre binaire de type Arbre.
        @return: la hauteur de l'arbre (un entier)
        """
        # if self.fils_gauche != None:
        #     if self.fils_droit != None:
        #         return 1 + max(......, .......)
        #     else:
        #         return ........
        # elif self.fils_droit != None:
        #     return ..........
        # else:
        #     return .....

    def conversion_arbre_vers_dictionnaire(self):
        """
        Convertit un objet de la classe Arbre en un dictionnaire dont les clefs sont les noeuds et les valeurs la liste de fils d'un noeud
        @return: le dictionnaire en question
        """
        dico = {}
        self.conversion_vers_dictionnaire_recur(dico)
        return dico

    def conversion_arbre_vers_dictionnaire_recur(self,dico):
        """

        @param dico:
        @return:
        """
        pass

    def conversion_vers_arbre_binaire(self):
        """
        Convertit un objet de type Arbre vers un objet de type Node de la bibliothÃ¨que binarytree (pour afficher un arbre binaire)
        @return: arbre binaire de type Node
        """
        racine = Node(self.nom)
        self.conversion_vers_arbre_binaire_recur(racine,racine)
        return racine

    def conversion_vers_arbre_binaire_recur(self,racine,noeud):
        """

        @param racine: le noeud racine de l'arbre binaire de type Node
        @param noeud: un noeud courant(de type Node)
        @return: l'arbre binaire (de type Node) Ã  partir de sa racine
        """
        if self.fils_gauche != None:
            noeud.left = Node(self.fils_gauche.nom)
            self.fils_gauche.conversion_vers_arbre_binaire_recur(racine,noeud.left)
        if self.fils_droit != None:
            noeud.right = Node(self.fils_droit.nom)
            self.fils_droit.conversion_vers_arbre_binaire_recur(racine,noeud.right)
        return racine

    def affiche_arbre(self):
        """
        Affiche en mode texte un arbre binaire de type Arbre
        @return:
        """
        arbre_binaire = self.conversion_vers_arbre_binaire()
        print(arbre_binaire)

    def recherche_clef_abr(self,clef,nb_etapes=1):
        """
        MÃ©thode qui recherche une clef (un nombre) dans l'arbre binaire de recherche
        @param clef: la clef (un nombre) que l'on cherche dans l'arbre
        @param nb_etapes: le nombre d'Ã©tapes courante dans la recherche de la clef dans l'arbr
        @return: True,nb_etapes si la clef est prÃ©sente dans l'arbre et False,False sinon
        """
        pass

#---------------------------------------------------------------------------------------------
# Fin de la classe Arbre
#---------------------------------------------------------------------------------------------

def construit_arbre_exemple():
    """
    Construit l'arbre de type Arbre de l'exemple
    reprÃ©sentÃ© par ce dictionnaire
    dico_arbre = {10:[8,5],8:[3,15],3:[None,None],15:[20,None],20:[None,None],5:[4,None],4:[None,None]}
    @return:
    """
    pass

def genere_arbre_binaire_complet(hauteur):
    """
    GenÃ¨re un arbre binaire complet de type Arbre de hauteur donnÃ©e composÃ© des nombres compris entre 1 et 2^hauteur - 1
    @param hauteur: l hauteur de l'arbre
    @return: l'arbre de type Arbre
    """
    abc = Arbre(1)
    genere_arbre_binaire_complet_recur(hauteur,abc,abc)
    return abc

def genere_arbre_binaire_complet_recur(hauteur,racine,noeud_courant,h=1,no=1):
    """

    @param hauteur:
    @param racine:
    @param noeud_courant:
    @param h:
    @param no:
    @return:
    """
    if h < hauteur:
        fils_gauche = Arbre(2*no)
        fils_droit = Arbre(2 * no + 1)
        noeud_courant.insere_fils_gauche(fils_gauche)
        noeud_courant.insere_fils_droit(fils_droit)
        genere_arbre_binaire_complet_recur(hauteur,racine,fils_gauche, h+1, 2*no)
        genere_arbre_binaire_complet_recur(hauteur,racine, fils_droit,h+1, 2*no + 1)
```