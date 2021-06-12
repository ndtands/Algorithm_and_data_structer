"""
kq = 0 
init Visited=[False]*len(adj)
for i in all Vertex:
    if not visted[i]:
        explore(i)
        kq +=1
return kq

"""
def number_of_components(adj):
    result = 0
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            explore(adj, i, visited)
            result += 1
    return result
"""
explore(v):
    visited[v] = True
    for (v,w) thuoc E:
        if not visited(w):
            explore(w)

"""
def explore(adj, x, visited):
    visited[x] = True
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj, adj[x][i], visited)

def add_edge(adj,a,b):
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


if __name__ == '__main__':
    V, E = map(int,input().split())
    adj = [[] for _ in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        add_edge(adj, a, b)		
        
    print(number_of_components(adj))