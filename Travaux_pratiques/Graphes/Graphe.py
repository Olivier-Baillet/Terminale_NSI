class Graphe:
    def __init__(self, liste_sommets):
        self.liste_sommets = liste_sommets
        self.adjacents = {sommet : [] for sommet in liste_sommets}

    def ajoute_arete(self, sommetA, sommetB):
        self.adjacents[sommetA].append(sommetB)
        self.adjacents[sommetB].append(sommetA)

    def voisins(self, sommet):
        return self.adjacents[sommet]

    def sont_voisins(self, sommetA, sommetB):
        return sommetB in self.adjacents[sommetA]


