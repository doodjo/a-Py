def a_star(niz):
    found_end = False
    open_set = set()
    closed_set = set()
    g = {}
    prev_state = {}
    g[niz] = 0
    prev_state[niz] = None
    open_set.add(niz)
    while len(open_set) > 0 and (not found_end):
        node = None
        for next_node in open_set:
            if node is None or g[next_node] + h_function(next_node) < g[node] + h_function(node):
                node = next_node
        if kraj(node):
            found_end = True
            break
        for states in zamena_kuglica(node):
            print(states)
            if states not in open_set and states not in closed_set:
                open_set.add(states)
                prev_state[states] = node
                g[states] = g[node] + 1
            else:
                if g[states] > g[node] + 1:
                    g[states] = g[node] + 1
                    prev_state[states] = node
                    if states in closed_set:
                        closed_set.remove(states)
                        open_set.add(states)
        open_set.remove(node)
        closed_set.add(node)
    path = []
    if found_end:
        while prev_state[node] is not None:
            path.append(node)
            node = prev_state[node]
        path.append(niz)
        path.reverse()
    return path

def zamena_kuglica(niz):
    sve_zamene=[]
    n=len(niz)-1
    for x in range(0,n):
        i=list(niz)
        i[x], i[x+1] = i[x+1], i[x]
        sve_zamene.append(tuple(i))
    return sve_zamene


def h_function(node):
    s=0
    i1=node.index("G")
    i2=node.index("G",i1+1)
    i3=node.index("G",i2+1)
    i4=node.index("G",i3+1)
    s=s+i4+i3+i2-3*i1
    i1=node.index("R")
    i2=node.index("R",i1+1)
    i3=node.index("R",i2+1)
    i4=node.index("R",i3+1)
    s=s+i4+i3+i2-3*i1
    i1=node.index("B")
    i2=node.index("B",i1+1)
    i3=node.index("B",i2+1)
    i4=node.index("B",i3+1)
    s=s+i4+i3+i2-3*i1
    return s

def kraj(niz):
    if niz[0]==niz[1] and niz[2]==niz[3] and niz[0]==niz[3] and niz[8]==niz[9] and niz[10]==niz[11] and niz[8]==niz[11]:
        return True
    else:
        return False

a=a_star(("G","R","B","R","G","B","B","R","G","G","B","R"))
# a=a_star(("R","R","B","R","B","B","B","R","G","G","G","G"))
print(len(a))
for p in a:
    print(p)