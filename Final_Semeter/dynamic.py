#Bai toan doi tien 
def RecursiveChange(money,coins):
    if money ==0:
        return 0
    minNumCoins = float('inf')
    for i in range(len(coins)):
        if money >= coins[i]:
            Numcoins = RecursiveChange(money-coins[i], coins)
            if Numcoins+1<minNumCoins:
                minNumCoins=Numcoins+1
    return minNumCoins
#print(RecursiveChange(10,[6,5,1]))

def DChange(money,coins):
    MinNumCoins=[0]*(money+1)
    for m in range(1,money+1):
        MinNumCoins[m] = float('inf')
        for i in coins:
            if m >= i:
                NumCoins = MinNumCoins[m - i]+1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[m]
#print(DChange(40,[5,10,15,20]))

#baitoanmaytinh
def optimal_sequence(n):
    if n == 1:
        return [1]
    sequence =[[]]*(n+1)
    sequence[1]=[1]
    for m in range(2,n+1):
        if m%3 ==0:
            minNum = min(len(sequence[m//3])+1,len(sequence[m//2])+1)
            if minNum ==len(sequence[m//3])+1:
                sequence[m] =sequence[m//3]+[m]
            else:
                sequence[m] =sequence[m//2]+[m]
        elif m%2 == 0:
            minNum = min(len(sequence[m - 1]) + 1, len(sequence[m//2]) +1)
            if minNum == len(sequence[m//2]) + 1:
                sequence[m] = sequence[m//2] + [m]
            else:
                sequence[m] = sequence[m-1] + [m]
        else:
            sequence[m] = sequence[m-1] + [m]
    return sequence[m],len(sequence[m])
print(optimal_sequence(10))