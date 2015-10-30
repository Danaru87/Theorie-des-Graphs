__author__="arnaud.cueille"
__date__ ="$30 oct. 2015 7:42:56$"
ListeSommets = ['A','B','C','D']
Matrice = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]
#structure pour la gestion du resultat
def AjouterUnique(Element, Result):
    Trouve = False
    for i in range (len(Result)):
        if Result[i] == Element:
            Trouve = True
        if not Trouve:
            Result.append(Element)
    return Result

#initialisation du marquage des sommets
def InitMarquage(ListeSommets, ListeSommetsMarques):
    for i in range(len(ListeSommets)):
        ListeSommetsMarques.append([ListeSommets[i], ''])
    return ListeSommetsMarques

#retrouve l indice d un sommet
def IndiceSommet(Element):
    for i in range(len(ListeSommets)):
        if ListeSommetsMarques[i][0] == Element:
            return i

#controle du marquage d un sommet donne
def EstMarque(Element, ListeSommetsMarques):
    i = 0
    while i < len(ListeSommetsMarques):
        if ListeSommetsMarques[i][0] == Element:
            if ListeSommetsMarques[i][1] != '':
                return True
        else:
            return False
    i += 1

#controle le marquage de tous les sommets
def TousMarques(ListeSommetsMarques):
    i = 0
    Resultat = True
    while i < len(ListeSommetsMarques):
        if ListeSommetsMarques[i][1] == '':
            Resultat = False
    i += 1
    return Resultat

#marque un sommet donne
def Marquer(Element, ListeSommetsMarques):
    i = 0
    while i < len(ListeSommetsMarques):
        if ListeSommetsMarques[i][0] == Element:
            ListeSommetsMarques[i][1] = '*'
    i += 1
    return ListeSommetsMarques

def PL(SommetDeDepart):
    print "--- Parcours en largeur d abord ---"
    ListeSommetsMarquesPL = [] #liste a deux dimensions des sommets marques ou non indiques par une etoile *
    ListeSommetsMarquesPL = InitMarquage(ListeSommets, ListeSommetsMarquesPL)
    print "ListeSommetsMarquesPL", ListeSommetsMarquesPL
    Result = []
    Result = AjouterUnique(SommetDeDepart, Result)
    Indice = 0
    #on conditionne l arret sur l ensemble des sommets marques et non sur le nombre de sommets
    while not TousMarques(ListeSommetsMarquesPL):
        ListeSommetsMarquesPL = Marquer(Result[Indice], ListeSommetsMarquesPL)
        print "ListeSommetsMarquesPL: ", ListeSommetsMarquesPL
        print "Result: ", Result
        print "Indice: ", Indice
        #recherche les voisins dans la matrice
        for i in range(len(ListeSommets)):
            if Result[Indice] == ListeSommets[i]:
                for j in range(len(ListeSommets)):
                    if Matrice[i][j] == 1:
                        Result = AjouterUnique(ListeSommets[j], Result)
        Indice +=1
    print Result,

PL(ListeSommets[0])
print " --> Result (parcours en largeur) "