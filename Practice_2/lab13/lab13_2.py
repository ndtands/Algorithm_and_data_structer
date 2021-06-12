#Do den = 1 => trang = 0 
# Hai node cạnh nhau không được cùng màu gọi là lưỡng phân
def bipartite(adj):
    color_arr = [-1] * len(adj)
    color_arr[0] = 1
    queue = []
    queue.append(0)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            print(color_arr)
            if color_arr[v] == -1:
                queue.append(v)
                color_arr[v] = 1 - color_arr[u]
            elif color_arr[v] == color_arr[u]:
                print(u,v)
                return 0
    return 1
def add_edge(adj,a,b):
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        add_edge(adj, a, b)
    print(adj)
    print(bipartite(adj))    