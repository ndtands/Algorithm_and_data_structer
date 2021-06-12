

'''def optimal(money,coins):
    sequence =[[]]*(money+1)
    min_coin = min(coins)
    sequence[min_coin]=[min_coin]
    for m in range(min_coin,money+1):
        for i in coins:
            if m==i:
                sequence[m]=[i]
                print("here")
            if m>i:
                _min=len(sequence[m-i])+1
                if sequence[m]==[]:
                    sequence[m]=sequence[m-i]+[i]
                elif _min < len(sequence[m]):
                    sequence[m]=sequence[m-i]+[i]
    print(sequence)
print(optimal(40,[1,2,7,5,20]))
'''


def optimal_coin(money,coins):
    sequence = [[]]*(money+1)
    for m in range(money+1):
        for i in coins:
            if m==i:
                sequence[i]=[i]
            elif m>i:
                temp = len(sequence[m-i])+1
                if sequence[m]==[]:
                    sequence[m]=sequence[m-i]+[i]
                elif temp <len(sequence[m]):
                    sequence[m]=sequence[m-i]+[i]
    return sequence
print(optimal_coin(40,[1,2,7,5,20]))

def caculator(n):
    if n==1:
        return [1]
    sequence =[[]]*(n+1)
    sequence[1]=[1]
    for m in range(2,n+1):
        _chia3=sequence[m//3]
        _chia2=sequence[m//2]
        _tru1 =sequence[m-1]
        if m%3==0:
            _min = min(len(_chia3)+1,len(_chia2)+1)
            if _min == len(_chia3)+1:
                sequence[m]=_chia3+[m]
            else:
                sequence[m]=_chia2+[m]
        elif m%2==0:
            _min = min(len(_tru1)+1,len(_chia2)+1)
            if _min == len(_chia3)+1:
                sequence[m]=_chia2+[m]
            else:
                sequence[m]=_tru1+[m]
        else:
            sequence[m]=sequence[m-1] + [m]
    return sequence[m],len(sequence[m])
print(caculator(1000000))

"""
Knapsack lap lai: Mot mon hang lay nhieu lan 
value(w) = max{value(w-wi)+vi}
knapsack(W):
    value(0) <- 0 
    for w from 1 to W:
        value(w) <- 0 
        for i from 1 to n :
            if w[i] <= w:
                val <- value(w-w[i])+v[i]
                if val > value(w):
                    value(w) <- val
    return value(W)
"""
"Xep tui lay duoc nhieu lan "
def Knapsack(weigh,val,W):
    n= len(weigh)
    value = [0]*(W+1)
    for w in range(1,W+1):
        value[w]=0
        for i in range(n):
            if weigh[i]<=w:
                v = value[w-weigh[i]]+val[i]
                if v >value[w]:
                    value[w]=v
    return value[w]
"""
Knapsack khong lap lai
- value(w,i) = max{value(w-wi,i-1)+vi,value(w,i-1)}
- w,v from 1 to n

Knapsack(W):
    initialize all value(0,j) <- 0 
    initialize all value(w,0) <- 0
    for i from 1 to n :
        for w from 1 to W:
            value(w,i) <- value (w,i-1)
            if wi <= w:
                val <- value (w-wi,i-1)+vi
                if value(w,i) <val:
                    value(w,i) <- val

    return  value(W,n)

O(n*W)
"""
def Knapsack(weigh,value,W):
    weigh =[0]+weigh
    value =[0]+value
    #weigh*W
    V   = [[0 for _ in range(len(weigh))] for _ in range(W+1)]
    for i in range(1,len(weigh)):
        for w in range(1,W+1):
            V[w][i]=V[w][i-1]
            if weigh[i] <=w:
                val = V[w-weigh[i]][i-1]+weigh[i]
                if V[w][i] <val:
                    V[w][i] = val
    return V[W][len(weigh)-1]