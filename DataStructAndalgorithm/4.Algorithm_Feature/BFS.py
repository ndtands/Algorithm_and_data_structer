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