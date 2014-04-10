def Parse(fichier): 
    f = open(fichier,"r")
    matrice = []
    l=[]
    val = 0
    j=0
    AdjacencyList = {}


    strmatrice = f.readlines()

    for i in strmatrice:
        matrice.append(i.rstrip('\n'))
    n = int(matrice[0])


    for i in range(1,n+1):
        for c in matrice[i]:
            if c != ' ':
                j = j+1
                if int(c) == 1:
                    l.append(j)
        
        AdjacencyList[i] = l
        l=[]
        j = 0
                        
    return AdjacencyList

