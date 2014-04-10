preorder = {}
S = []
P = []
Assigned = []
Components = []
C = 0

def ConnectedComponents(Adjacency):
    n = len(Adjacency)

    for vertex in Adjacency:
        if vertex not in Assigned:
            PathBased(vertex, Assigned, Adjacency)

    return Components


def PathBased (v, Assigned, Adjacency):
    global C
    
    preorder[v] = C
    C+=1
    S.append(v)
    P.append(v)
    NewComp = []
    for w in Adjacency[v]: #w is a neighboor of v
        if w not in preorder: #If the preorder of w is not defined
            PathBased(w, Assigned, Adjacency)
        elif w not in Assigned:
            while preorder[P[len(P)-1]] > preorder[w]:
                P.pop()

    if P[len(P)-1] == v:
        while v in S:
            NewComp.append(S[len(S)-1])
            Assigned.append(S[len(S)-1])
            S.pop()
        P.pop()
        Components.append(NewComp)
