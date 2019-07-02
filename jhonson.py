#Rodrigo
import math
import heapq 

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


def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    heapq.heappush(queue, (0, s))

    while len(queue) > 0:
        g, u = heapq.heappop(queue)
        visited[u] = True

        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights 

def johnson(G,s):
    n = len(G)
    _, distances = bellmanford(G,s)
    counter = 0

    for u in range(n):
        counter = 0
        for v, w in G[u]:
            newDistance = w + distances[u] - distances[v]
            G[u][counter] = v, newDistance
            counter += 1

    print(dijkstra(G,s))

G = [[(1, 6), (3, 7)],
     [(2, 5), (3, 8), (4, -4)],
     [(1, -2), (4, 7)],
     [(2, -3), (4, 9)],
     [(0, 2)]]

johnson(G,1)

