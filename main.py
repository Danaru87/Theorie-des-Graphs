ListSommetsMarques = []

Pile = []

Matrice = [
    ['A', [0, 0, 1, 0, 1, 0]],
    ['B', [0, 0, 0, 1, 0, 0]],
    ['C', [1, 0, 0, 1, 0, 0]],
    ['D', [0, 1, 1, 0, 0, 1]],
    ['E', [1, 0, 0, 0, 0, 0]],
    ['F', [0, 0, 0, 1, 0, 0]]
]

Successeurs = []

def ajouter(element):
    Pile.append(element)

def retirer():
    return Pile.pop()

def estmarque(element):
    for sommet in ListSommetsMarques:
        if sommet[0] == element and sommet[1] == "*":
            return True
    return False

def marquer(element):
    index = -1
    for i in range(0, len(ListSommetsMarques), 1):
        if ListSommetsMarques[i][0] == element:
            index = i

    if index == -1:
        ListSommetsMarques.append([element, "*"])
    else:
        ListSommetsMarques[index][1] = "*"

def rechercherSommets():
    for line in Matrice:
        Pile.append(line[0])
    print (Successeurs)

def rechercherSucesseurs(Element):
    for line in Matrice:
        if (line[0] == Element):
            listSuc = []
            for i in range(0, len(line[1]), 1):
                if line[1][i] == 1:
                    if i == 0:
                        listSuc.append('A')
                    elif i == 1:
                     listSuc.append('B')
                    elif i == 2:
                        listSuc.append('C')
                    elif i == 3:
                        listSuc.append('D')
                    elif i == 4:
                        listSuc.append('E')
                    elif i == 5:
                        listSuc.append('F')
    return listSuc

def parcourir():
    for som in Pile:
        if not estmarque(som):
            marquer(som)

    print("Parcour:" + str(ListSommetsMarques))



rechercherSommets()
ParcoursProfondeur = []
StackDejaTraite = []
ParcoursProfondeur.append('A')
StackDejaTraite.append('A')



'''
On commence a A    <------------------------------∏
On recupère a liste des successeurs de A          |
On stocke la longueur des successeurs de A        |
 On traite le premier successeur bla              |
 Si pas de successeurs à bla:                     |
  Retour à A            i+1 < longeurSucesseurs   |
 Sinon                                            |
    ajouter bla StackDejaTraité ------------------∏

succA = rechercherSucesseurs('A')
fsucc = succA[0]
StackDejaTraite.append(fsucc)






parcourir()

##rechercherSommets()
rechercherSucesseurs('A')
rechercherSucesseurs('B')
rechercherSucesseurs('C')
rechercherSucesseurs('D')

print(Successeurs)






'''
###################################
###################################
###################################
###################################
###################################
###################################
###################################
#    A ------------- B
#    |           -   |
#    |        -      |
#    |     -         |
#    |  -            |
#    C ------------- D
#
# LARGEUR
###################################
###################################
###################################
###################################
###################################
###################################
Pile = []
ajouter('A')
ajouter('B')
ajouter('C')
ajouter('D')
ajouter('E')
ajouter('F')

ParcoursLargeur =[]

ParcoursLargeur.append('A')
for sommet in ParcoursLargeur:
    existinp = False
    for parcours in ParcoursLargeur:
        if (sommet == parcours):
            existinp = True
    if not existinp:
        ParcoursLargeur.append(sommet)

    Success = rechercherSucesseurs(sommet)
    for succ in Success:
        existinp = False
        for parcours in ParcoursLargeur:
            if (succ == parcours):
                existinp = True
        if not existinp:
            ParcoursLargeur.append(succ)

print(ParcoursLargeur)