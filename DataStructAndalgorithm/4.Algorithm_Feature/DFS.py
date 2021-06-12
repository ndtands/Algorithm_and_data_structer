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
