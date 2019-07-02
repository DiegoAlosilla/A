import math
def floydWarshall(G):
    n = len(G)
    p = [[-1 for _ in range(n)]for _ in range(n)]
    c = [[math.inf for _ in range(n)]for _ in range(n)]
    for u in range(n):
        for v, w in G[u]:
            p[u][v] = u
            c[u][v] = w
    
    for i in range(n):
        for u in range(n):
            for v in range(n):
                if i == u or i == v or u == v:
                    continue
                f = c[u][i] + c[i][v]
                if f < c[u][v]:
                    c[u][v] = f
                    p[u][v] = i
    return p, c

#Rodrigo
def floydwarshallR(G):
    n = len(G)
    d = [[math.inf]*n for _ in range(n)]
    p = [[-1]*n for _ in range(n)]
    for u in range(n):
        d[u][u] = 0
        for v, w in G[u]:
            d[u][v] = w
            p[u][v] = u
            
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f = d[i][k] + d[k][j]
                if d[i][j] > f:
                    d[i][j] = f
                    p[i][j] = k
                    
    return p, d