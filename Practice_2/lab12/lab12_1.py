def reachable(adj,x,y):
    visited =[False]*len(adj)
    return explore(adj, x, y, visited)

"""
explore(v,z):
    visited[v] = True
    if v = z:
        return 1
    for (v,w) thuoc E:
        if not visited(w):
            explore(w,z)
            if w = z:
                return 1
    return 0
"""
def explore(adj, x,y, visited):
    if (x==y):
        return 1
    visited[x] = True
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj, adj[x][i],y, visited)
            if (adj[x][i] == y ):
                return 1
    return 0

def add_edge(adj,a,b):
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


if __name__ == '__main__':
    V, E = map(int,input().split())
    adj = [[] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        add_edge(adj, a, b)		
    x, y = map(int, input().split())
    print(reachable(adj, x-1, y-1))