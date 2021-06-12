import heapq
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
        dist ={vertex: float('infinity') for vertex in self.graph}
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
                    print("Graph contains negative weight cycle")
                    return False
        return dist
G = Graph_Weight(4)
G.add_edge('1','2',-4)
G.add_edge('2','4',2)
G.add_edge('4','1',2)
G.add_edge('3','4',6)
G.add_edge('2','3',1)
print(G.Bellman_ford('1'))