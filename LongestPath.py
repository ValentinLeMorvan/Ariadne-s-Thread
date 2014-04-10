def BellmanFord (AdjacencyMatrix, start, end):

    weight = {}
    pred = []
    AdjacencyList = {}
    level = 0
    longestPath = []

    #creation of the adjacency list for the given matrix
    for i in AdjacencyMatrix:
        l = []
        level +=1
        j = 0
        for val in i:
            j += 1
            if val != 0:
                l.append(j)
        AdjacencyList[level] = list(l)
        
    
    n = len(AdjacencyList)

    #Initialisation of weights at +infinity, except for the first node
    for i in range (1,n+1):
        pred.append(0)
        weight[i] = float('inf')
    weight[1] = 0

    #application  of the Bellman Ford algorithm
    for i in range(1,n+1):
        for i in AdjacencyList:
            for nbr in AdjacencyList[i]:
                pathW = AdjacencyMatrix[i-1][nbr-1]
                if (weight[i]- pathW) < weight[nbr]: #nbr is a neighbor of i. weight of e(i,nbr) = pathw
                    weight[nbr] = weight[i]- pathW
                    pred[nbr - 1] = i #indice in array pred start at 0, so the indice is nbr-1
                    
    for i in AdjacencyList:
        for nbr in AdjacencyList[i]:
            if (weight[i]- 1) < weight[nbr]:
                print "A cycle exist: the longest path is not computable"
                return []

    i = end
    while i != start:
        longestPath.append(i)
        i = pred[i-1]
    longestPath.append(start)
    longestPath.reverse()

    return longestPath
