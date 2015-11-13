ValeurSommet = {"A": 0, "B": 99999, "C": 99999,"D":99999,"E":99999}


SommetMarques = []

Matrice = {
    "A":
        {
            "B":10,
            "C":5,
            "E":7
        },
    "B":{
        "C":2,
        "D":2
    },
    "C": {
        "B":3,
        "D":9,
        "E":2
    },
    "D":
        {"E":4},
    "E":
        {"D":6}
}



def cheminOptimal():
    # On marque le premier sommet
    SommetMarques.append("A")

    #On boucle sur chaque sommet marque
    for sommet in SommetMarques:
        #On recupere les voisins du sommet
        lesVoisins = Matrice[sommet]
        #Pour chaque voisins
        ValuerVoisin(lesVoisins)

        #On recupere le plus petit voisin
        sommetVoisin = RechercherPlusPetitVoisin(lesVoisins)
        SommetMarques.append(sommetVoisin)
    print(ValeurSommet)
    print(SommetMarques)


def ValuerVoisin(lesVoisins):
    for voisin in lesVoisins:
            # Si le sommet n'est pas marque
            if not (estmarque(voisin)):
                # Si la valeur du sommet deja valuee est plus grande
                if (ValeurSommet[voisin] > lesVoisins[voisin]):
                    ValeurSommet[voisin] = lesVoisins[voisin]


def RechercherPlusPetitSommetNonMarque(lesVoisins): ##TODO: A corriger
    value = 99999
    sommetVoisin = "X"
    for voisin in lesVoisins:
        if (lesVoisins[voisin] < value):
            value = lesVoisins[voisin]
            sommetVoisin = voisin
    return sommetVoisin


def estmarque(element):
    for sommet in SommetMarques:
        if sommet == element:
            return True
    return False

cheminOptimal()