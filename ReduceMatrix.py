def ReduceMatrix (Adjacency, Levels):
    Matrix = []
    nlevel = 0
    
    for level in Levels: #level is the number of the start
        l = []
        for i in range(0, len(Levels)): #put all the values of l back to 0
            l.append(0)
        
        for place in level: #place is a place in level
            
            for nbr in Adjacency[place]: #nbr is a neighboor of place
                nbrlvl = 0
                
                while nbr not in Levels[nbrlvl] : #search the level of nbr
                    nbrlvl += 1

                if nbrlvl != nlevel:
                    l[nbrlvl] += 1
        
        Matrix.append(list(l))
        nlevel +=1
    return Matrix

