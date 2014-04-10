def End(matrice):
    n = len(matrice)

    for i in range(0,n):
        j = 0
        while matrice[i][j]==0 and j < (n-1):
            j +=1
        if matrice[i][j]==0:
            return i + 1
            
    return 0
