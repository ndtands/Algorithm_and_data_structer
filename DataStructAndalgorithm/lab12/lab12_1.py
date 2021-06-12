
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

