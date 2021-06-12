class Graph:
    def __init__(self,numNode):
        self.V = numNode
        self.adj = [[] for i in range(self.V)]

    def addEdge(self,u,v):
       self.adj[u].append(v)
       self.adj[v].append(u)
    
    def DFSUtil(self,temp,v,visited):
        visited[v]=True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i]==False:
                temp = self.DFSUtil(temp, i, visited)
        return temp
    
    def connected(self):
        visited=[]
        cc=[]
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] ==False:
                temp =[]
                cc.append(self.DFSUtil(temp,v,visited))
        return cc
if __name__ == "__main__":
    [num_node,num_edge]=[int(i) for i in input("Nhap n node va m canh: ").split(" ")]
    g = Graph(num_node)
    for _ in range(num_edge):
        [A,B]=[int(i) for i in input("Nhap 2 node: ").split(" ")]
        g.addEdge(A, B)
    
    cc = g.connected()
    print(len(cc))
 
