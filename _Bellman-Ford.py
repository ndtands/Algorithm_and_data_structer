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

'''
Bellman_ford(src):
    all  dist of Node is inf
    dist[src]=0
    repeat(V-1):
        for node in all_node:
            for nebor,weight in node:
                if dist[node] != inf and dist[node]+weight <dist[nebor]:
                    dist[nebor]=dist[node]+weight
            
    for node in all_node:
        for nebor,weight  in node:
            if dist[node] !=inf and dist[node]+weight <dist[nebor]:
                #Error negative cycler
                return False
'''
#O(V*E)
#O(V)