def Start(matrice):
    n = len(matrice[0])
    
    for i in range(0,n-1):
        j = 0
        while matrice[j][i]==0 and j < n-1:
            j +=1
        if matrice[j][i] == 0:
            return (i + 1)

    return 0
