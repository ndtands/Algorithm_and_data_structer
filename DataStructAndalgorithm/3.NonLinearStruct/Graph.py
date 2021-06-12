'''
def addEdge(graph,u,v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u]=[v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v]=[u]

def find_path(graph,start,end,path=[]):
    path = path +[start]
    if start ==end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_path(graph,node,end,path)
            if newpaths is not None:
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

def Check(graph,start,end):
    arr = find_path(graph,1,4)
    if arr == None or arr == []:
        return 0
    else:
        return 1
graph  = {}
[num_node,num_edge]=[int(i) for i in input("Nhap n node va m canh: ").split(" ")]
for _ in range(num_edge):
    [A,B]=[int(i) for i in input("Nhap 2 node: ").split(" ")]
    addEdge(graph,A,B)
print(Check(graph,1,num_node))

'''
class Graph:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
 
 
# Driver Code
if __name__ == "__main__":
 
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    print(g.adj)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
 
# This code is contributed by Abhishek Valsan