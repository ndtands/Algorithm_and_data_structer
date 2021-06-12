import heapq
class Graph_Weight():
    def __init__(self,vertex):
        self.vertex= vertex
        self.graph = dict()
    
    def add_edge(self,u,v,w):
        if u not in self.graph :
            self.graph[u]={}
        self.graph[u][v]=w

    def print_graph(self):
        print(self.graph)

    def Dijkstra(self,start_vertex,end):
        dist ={str(v): float('infinity') for v in range(1,self.vertex+1)}
        dist[start_vertex] = 0
        pq = [(0,start_vertex)]
        while len(pq) > 0:
            #get min
            current_dist,current_vertex = heapq.heappop(pq)
            if current_dist > dist[current_vertex]:
                continue
            if current_vertex in self.graph:
                for neighbor,weight in self.graph[current_vertex].items():
                    dist_ = current_dist + weight
                    #thường thì dist[neighbor là vô cùng]
                    if dist_ <dist[neighbor]:
                        dist[neighbor] = dist_
                        #Thêm vào queue và thay đổi ưu tiên
                        heapq.heappush(pq,(dist_,neighbor))
        if dist[end]==float('infinity'):
            return -1
        return dist[end]
'''G = Graph_Weight(5)
G.add_edge(1, 2, 4)
G.add_edge(1, 3, 2)
G.add_edge(2, 3, 2)
G.add_edge(3, 2, 1)
G.add_edge(2, 4, 2)
G.add_edge(3, 5, 4)
G.add_edge(5, 4, 1)
G.add_edge(2, 5, 3)
G.add_edge(3, 4, 4)
print(G.Dijkstra(1,5))'''

v,e = [i.strip() for i in input("Nhap so nut va so canh: ").strip().split(" ")]
MyGraph = Graph_Weight(int(v))
for _ in range(int(e)):
    u,v,w = [i.strip() for i in input("Nhap u,v,w: ").strip().split(" ")]
    MyGraph.add_edge(u, v, int(w))
s,end = [i.strip() for i in input("Nhap diem dau va dich: ").strip().split()]
print(MyGraph.Dijkstra(s,end))

