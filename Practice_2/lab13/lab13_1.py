#Duyệt theo chiều rộng nên phù hợp với bài toán tìm đường đi ngắn nhất
"""
BFS(G,S):
    for all u thuoc V:
        dist[u] <- inf
    dist[S] <- 0
    Crete Queue
    enqueue(Q,S)
    while queue is not empty:
        u < - dequeue(Q)
        for all (u,v)  thuoc E:
            if dist[v] = inf:
                enqueue(Q,v)
                dist[v] <-dist[u]+1
    
    ## addition Code for function
    if dist[t] != inf:
        return dist[t]
    return -1 # Not reachable
"""
def distance(adj, s, t):
    dist = [float('infinity')] * len(adj)
    dist[s] = 0
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        #edge v_u
        for v in adj[u]:
            if dist[v] == float('infinity'):
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[t] != float('infinity'):
        return dist[t]
    return -1

def add_edge(adj,a,b):
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        add_edge(adj, a, b)
    s, t = map(int, input().split())
    print(distance(adj, s-1, t-1))
