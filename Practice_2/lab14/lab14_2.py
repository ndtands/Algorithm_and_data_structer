class Graph_Weight():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = dict()
    
    def add_edge(self,u,v,w):
        if u not in self.graph :
            self.graph[u]={}
        self.graph[u][v]=w

    def print_graph(self):
        print(self.graph)

    def Bellman_ford(self,src):
        # Step 1: fill the distance array and predecessor array
        dist ={str(vertex): float('infinity') for vertex in range(self.V+1)}
        # Mark the source vertex
        dist[src] = 0
        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V-1):
            for current_vertex in self.graph:
                for neighbor,weight in self.graph[current_vertex].items():
                    if dist[current_vertex] != float('infinity') and dist[current_vertex]+weight < dist[neighbor]:
                        dist[neighbor]=dist[current_vertex]+weight

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for current_vertex in self.graph:
            for neighbor,weight in self.graph[current_vertex].items():
                if dist[current_vertex] != float('infinity') and dist[current_vertex]+weight < dist[neighbor]:
                    #print("Graph contains negative weight cycle")
                    return False
        return dist
    def check(self):
        for key in self.graph:
            if self.Bellman_ford(key) == False:
                return False
        return True
v,e = [i.strip() for i in input("Nhap so nut va so canh: ").strip().split(" ")]
MyGraph = Graph_Weight(int(v))
for _ in range(int(e)):
    u,v,w = [i.strip() for i in input("Nhap u,v,w: ").strip().split(" ")]
    MyGraph.add_edge(u, v, int(w))
if MyGraph.check() == True:
    print('0')
else:
    print('1')