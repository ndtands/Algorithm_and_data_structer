"""
pseudocode:

Doi_tien(n,Coins):
    sorted(Coins) # reverse
    Count <- [0].len(Coins)
    index <- 0
    while index < |Coins|:
        if n == 0:
            return sum(Count)
        if n >= Coins(index):
            n <- n - Coins(index)
            Count(index) <- Count(index)+1
        else:
            index <- index +1
    return sum(Count)
"""
import time
def Doi_tien(n,Coin=None):
    if Coin == None:
        Coin = [2,5,10]
    Coin.sort(reverse=True)
    A   = [0]*len(Coin) 
    index = 0
    while index <len(Coin):
        if n == 0:
            return sum(A)
        if n>=Coin[index] :
            n-=Coin[index] 
            A[index] +=1 
        else:
            index +=1
    return sum(A)  

n=int(input())
start =time.time()
print("KQ: ",Doi_tien(n))
print("Time Excutive: ",time.time()-start)