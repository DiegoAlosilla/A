import math
#pack rodrigo
def bellmanford(G, s):
    n = len(G)
    d = [math.inf]*n
    p = [None]*n
    d[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u
        
    for u in range(n):
        for v, w in G[u]:
            if d[v] > d[u] + w:
                print("Oh no!, ciclo negativo")
                return
    return p, d