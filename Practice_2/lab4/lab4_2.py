"""
pesudocode:
- weigh: from 0 to n-1
- W
- value : nxW
- O(nxW)

Main:
    init value all = 0
    for i  from 0 to n-1:
        for m to 1 to W:
                         value[m][i-1]; m < weigh[i]   
            value[m][i]=
                         max{value[m][i-1],value[m-weight[i]][i-1]+weigh[i]}; m>=weigh[i]
    return value[W][n-1]
"""
def Get_max_god(weigh,W):
    weigh=[0]+weigh
    n = len(weigh)
    value = [[0 for _ in range(n)] for _ in range(W+1)]
    for i in range(1,len(weigh)):
        for w in range(1,W+1):
            value[w][i] = value[w][i-1]
            if weigh[i] <= w:
                val = value[w-weigh[i]][i-1]+weigh[i]
                if value[w][i] <val:
                    value[w][i] = val
    return value[W][len(weigh)-1]
W,n   = [int(i) for i in input("Nhap W,n: ").split(" ")]
weigh = [int(i) for i in input().split(" ")]
print(Get_max_god(weigh,W))
            
