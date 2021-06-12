def RecursiveChange(money,coins):
    if money ==0:
        return 0
    MinNumCoins = 10000
    for i in range(len(coins)):
        if money >= coins[i]:
            Numcoins = RecursiveChange(money-coins[i],coins)
            if Numcoins+1 <MinNumCoins:
                MinNumCoins = Numcoins+1
    return MinNumCoins

#print(RecursiveChange(10,[6,5,1]))

"""
DChange(money,coins):
    MinNumCoins(0) <- 0
    for m from 1 to money:
        MinNumCoins(m) <- inf
        for i from 1 to |coins|:
            if m >= coins[i]:
                Numcoins <- MinNumCoins(m - coins[i])+1
                if Numcoins < MinNumCoins(m):
                    MinNumCoins(m) <- NumCoins
    return MinNumCoin
Dung truy xuat cac gia tri da luu truoc do 
O(Money*Num_of_Coin)
"""
def DChange(money,coins):
    MinNumCoins=[0]*(money+1)
    for m in range(1,money+1):
        MinNumCoins[m] = 10000
        for i in coins:
            if m >= i:
                NumCoins = MinNumCoins[m - i]+1
                print(m,i,NumCoins)
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

print(DChange(40,[5,10,15,20]))

def EditDistance(A,B):
    A="0"+A
    B="0"+B
    n = len(A)
    m = len(B)
    D = [[ 0 for i in range(m)] for j in range(n)]
    for j in range(m):
       for i in range(n):
            if i==0:
               D[i][j]=j
            elif j==0:
                D[i][j]=i
            else:
                D[i][j]=0
    for j in range(1,m):
        for i in range(1,n):
            insertion = D[i][j-1]+1
            deletion  = D[i-1][j]+1
            match     = D[i-1][j-1]
            mismatch  = D[i-1][j-1]+1
            if A[i] == B[j]:
                D[i][j]=min(insertion,deletion,match)
            else:
                D[i][j]=min(insertion,deletion,mismatch)
    return D

def OutPut(i,j):
    if i ==0 and j == 0: 
        return 
    if i>0 and D[i][j]==D[i-1][j]+1:
        OutPut(i-1,j)
        print(A[i],"_")
    elif j>0 and D[i][j]==D[i][j-1]+1:
        OutPut(i,j-1)
        print("_",B[j])
    else:
        OutPut(i-1,j-1)
        print(A[i],B[j])

'''A="0"+"break"
B="0"+"ready"
D=EditDistance(A,B)
print(D)
OutPut(len(A)-1,len(B)-1)'''

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
def DPKnapsack(weigh,val,W):
    n = len(weigh)
    value=[0]*(W+1)
    for w in range(1,W+1):
        value[w]=0
        for i in range(n):
            if weigh[i] <= w:
                v = value[w-weigh[i]]+val[i] #Value_curr = value_prev + val_postion => Find max => .update
                if v >value[w]:
                    value[w]=v
    return value[W]
'''import time
start = time.time()
print(DPKnapsack([6,3,4,2],[30,14,16,9],100))
print("EX: ",time.time()-start)'''
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
def Knapsack_2(weigh,value,W):
    weigh =[0]+weigh
    value =[0]+value
    V   = [[0 for _ in range(len(weigh))] for _ in range(W+1)]
     
    for i in range(1,len(weigh)):
        for w in range(1,W+1):
            V[w][i] = V[w][i-1]
            if weigh[i] <= w:
                val = V[w-weigh[i]][i-1]+weigh[i]
                if V[w][i] <val:
                    V[w][i] = val
    return V[W][len(weigh)-1]

#print(Knapsack_2([6,3,4,2],[30,14,16,9],10))
'''print(Knapsack_2([1,4,8],[30,14,16,9],10))'''
"""
Memoization

Knapsack(w):
    if w is in hash table:
        return value(w)
    value(w) <- 0 
    for i from 1 to n :
        if w[i] <= w:
            val <- Knapsack(w-w[i])+v[i]
            if val > value(w):
                value(w) <- val
    insert value(w) into hash table with key w
    return value(w)
"""
def Knapsack(W,w,v,Table):
    if W in Table:
        return value[W]
    value[W] = 0 
    for i in range(1,len(w)):
        if w[i] <= W:
            val = Knapsack(W-w[i],w,v,Table)+v[i]
            if val > value[W]:
                value[W] = val
    Table[W] = value[W]
    return value[W]
'''value = [0]*101
Table = {}
start = time.time()
print(Knapsack(100,[0,6,3,4,2],[0,30,14,16,9],Table))
print("EX2: ",time.time()-start)'''


