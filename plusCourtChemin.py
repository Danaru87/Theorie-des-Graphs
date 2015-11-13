__author__ = 'danaru'

Matrice = [
    [0, 2, 4, 0],
    [2, 0, 1, 0],
    [4, 1, 0, 2],
    [0, 0, 2, 0]
]

def fermetureTransitive():
    for i in range(len(Matrice)):
        for k in range(len(Matrice[i])):
            for j in range(len(Matrice)):
                if Matrice[i][k] != 0 and Matrice[k][j] !=0 and i != j:
                    if (Matrice[i][j] > Matrice[i][k] + Matrice[k][j]) and Matrice[i][j] !=0:
                        Matrice[i][j] = Matrice[i][k] + Matrice[k][j]
                    elif(Matrice[i][j] == 0):
                        Matrice[i][j] = Matrice[i][k] + Matrice[k][j]

    print(Matrice)

def fermetureTransitiveArnaud(matrice):
    for n in range(len(matrice)):
        for i in range(len(matrice)):
            for k in range(len(matrice[i])):
                for j in range(len(matrice[i])):
                    if matrice[i][k] != 0 and matrice[k][j] != 0:
                        if matrice[i][j] == 0 and i != j:
                            matrice[i][j] = matrice[i][k] + matrice[k][j]
                        else:
                            if matrice[i][j] > matrice[i][k] + matrice[k][j]:
                                matrice[i][j] = matrice[i][k] + matrice[k][j]
    print(Matrice)

fermetureTransitive()
fermetureTransitiveArnaud(Matrice)