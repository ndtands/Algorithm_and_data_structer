import heapq
class Graph_Weight():
    def __init__(self):
        self.graph = dict()
    
    def add_edge(self,u,v,w):
        if u not in self.graph :
            self.graph[u]={}
        self.graph[u][v]=w
        if v not in self.graph :
            self.graph[v]={}
        self.graph[v][u]=w

    def print_graph(self):
        print(self.graph)

    def Dijkstra(self,start_vertex):
        dist ={vertex: float('infinity') for vertex in self.graph}
        
        dist[start_vertex] = 0
        pq = [(0,start_vertex)]
        while len(pq) > 0:
            current_dist,current_vertex = heapq.heappop(pq)

            if current_dist > dist[current_vertex]:
                continue
            
            for neighbor,weight in self.graph[current_vertex].items():
                dist_ = current_dist +weight

                if dist_ <dist[neighbor]:
                    dist[neighbor] = dist_
                    heapq.heappush(pq,(dist_,neighbor))
        return dist
G = Graph_Weight()
G.add_edge('0','1',4)
G.add_edge('0','7',8)
G.add_edge('1','2',8)
G.add_edge('1','7',11)
G.add_edge('2','3',7)
G.add_edge('2','8',2)
G.add_edge('2','5',4)
G.add_edge('3','4',9)
G.add_edge('3','5',14)
G.add_edge('4','5',10)
G.add_edge('5','6',2)
G.add_edge('6','7',1)
G.add_edge('6','8',6)
G.add_edge('7','8',7)
print(G.Dijkstra('0'))

