"""
- Time complexity: O(V+E) 
- space complexity: O(V)
- Pseudocode:
DFS(G,u)
    u.visited =true
    for each v in G.Adj[u]
        if v.visited == false
            DFS(G,V)
"""

def DFS(graph,start,visted=None):
    if visted is None:
        visted=set()
    visted.add(start)
    print(start,graph[start],visted,graph[start]-visted)
    for next in graph[start]-visted:
        DFS(graph,next,visted)
    return visted

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3']),
         '5':set()}
DFS(graph,"0")

"""
-time complexity: O(V+E)
-space complexity: O(V)
-pseudocode:
    create a queue Q:
    mark v as visited and put v into Q
    while Q is non-empty:
        remove the head u of Q
        mark and enqueue all (unvisited) neighbours of u
"""
import collections
def BFS(graph,root):
    visited,queue =set(),collections.deque([root])
    visited.add(root)
    while queue:
        vertex =queue.popleft()
        print(str(vertex)+" ",end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
    print("Following is Breadth First Traversal: ")
    BFS(graph, '0')
    gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
    BFS(gdict, "a")



'''
DFG(G,u):
    u.visited = True
    for a in nebourhood of u:
        if a.visited == False:
            DFG(G,a)

#Tính toán:  O(V+E)
#Lưu trữ:  O(V)


BFG(G,u):
    create Queue
    enqueue u to Queue
    u.vistited = true
    while queue is not empty:
        node = dequeue
        for i in nebourhood of node:
            if node.vistited == False:
                enqueue i 
                i.vistited = true

#Tính toán : O(V+E)
#Lưu trữ : O(V)
'''


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