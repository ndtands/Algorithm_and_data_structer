"""
gas_station : maxtrix 
L: km with full
dist: distance

pesudocode:
MinRefill(dist,L,gas_station):
    numRefills   <- 0
    currentfills <- 0
    limit        <- L
    n <- len(gas_station)
    while limit <=dist:
        #Khong the tiep can dich hoac ga
        if currentfills >= n or gas_stations[currentfills]>limit:
            return -1
        # Tim gas station xa nhat co the tiep can 
        while currentfills <n-1 and gas_stations[currentfills+1] <= limit:
            currentfills < - currentfills
        numRefill <- numRefill
        limit = gas_stations[currentfills]+miles
        currentRefill <- currentfills+1
    return numRefills

Runing time : O(n)
"""
def MinRefill(dist,L,gas_stations):
    numRefill,curRefill,limit = 0,0,L
    n = len(gas_stations)
    while limit < dist:
        if curRefill>=n or gas_stations[curRefill]>limit:
            print("Can't reach !!")
            return -1
        while curRefill <n-1 and gas_stations[curRefill+1]<=limit:
            curRefill+=1
        numRefill+=1
        limit = gas_stations[curRefill]+L #update new limit
        curRefill+=1 #using for loop forever
    return numRefill
#gas_stations=[200,375,750,850]
#dist =950
#L=400
#print(MinRefill(dist,L,gas_stations))
#print(MinRefill(10, 3, [1, 2, 5, 9])) 

"""
C: arr
L: limit 

pesudocode 
MinGroup(C):
    sorted(C)
    R=[]
    i=0
    while i < n:
        [l,r] <- [C[i],C[i]+1]
        R <- R hop [l,r] => R.append(l) # add start group
        i <- i+1
        while i< n and C[i] <= r:
            i<- i+1 #find position of end group
    return len(R)


Time = O(Nlong(N)) +O(N)
"""
def MinGroups(C,L):
    C = sorted(C) 
    R = []
    n = len(C)
    i = 1
    while i < n:
        [l,r] =[C[i],C[i]+L]
        R.append(l)
        i+=1
        while i< n and C[i] <= r:
            i=i+1
    return len(R)

#print(MinGroups([1.1,1.2,1.5,2.6,2.8,3.9],1))

"""
W: weight max
w: matrix weight
v : matrix value

Pesudocode:
Knapsack(W,v,w):
    A <- [0]*n
    V <- 0
    repeat n times:
        if W = 0:
            reuturn V,A
        select i with wi >0 and max vi/wi
        a <- min(wi,W)
        V <- V+a*vi/wi
        wi <- wi - a
        A[i] <- A[i]+a
        W <- W -a
    return (V,A)
=> Time O(N^2)

KnapsackOptimize(W,w,v):
    A <- [0]*n
    V <- 0
    for i from 1 to n:
        if W =0 :
            return (V,A)
        a <- min(wi,W)
        V <- V +a.vi/wi
        wi <- wi-a
        A[i] <- A[i]+a
        W <- W-a
    return (V,A)

Time excutive: Sort()+O(N) = O(N*longN)
"""
def KnapSack(W,w,v):
    A = [0]*len(w)
    V = 0
    for _ in range(len(w)):
        if W ==0 :
            return (V,A)
        f = [v[i]/w[i] for i in range(len(w))]
        index = f.index(max(f))
        #Sau khi lay het thi no bang 0 => -1 => max chuyen sang min
        a = min(w[index],W)
        V = V+a*f[index]
        w[index] = w[index]-a
        A[index] = A[index]+a
        W        = W - a
        #Using for div zero
        if (w[index] == 0):
            w[index]  =-1
    return (V,A)
#print(KnapSack(7,[4,2,2],[20,18,14]))

def KnapsackOptimize(W,weights,values):
    valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    A = [0]*len(weights) # 
    V = 0
    for i in range(len(valuePerWeight)):
        if W ==0 : 
            return V,A
        a = min(valuePerWeight[i][1],W)
        V = V+a*valuePerWeight[i][0]
        valuePerWeight[i][1]=valuePerWeight[i][1]-a
        A[i] = A[i]+a
        W = W-a
    return V,A
#print(KnapsackOptimize(7,[4,2,2],[20,18,14]))

"""
Bài toán trồng hoa
pesudocode
All_flower(arr):
    max = 0
    for index, day in arr:
        day_find = index+1 +day
        if day-find >max
            max = day_find
    return max
"""
def All_flower(arr):
    max_day = 0
    for day,hoa in enumerate(arr):
        bloom_day = (day+1) + hoa
        if bloom_day >max_day:
            max_day = bloom_day
    return max_day
#print(All_flower([1,4, 3, 1]))

"""
Bài toán xếp gạch
"""
def Xep_gach(arr):
    n=len(arr)
    arr = sorted(arr,reverse=True)
    if arr[0]+1>n:
        return n
    else:
        return arr[0]+1
#print(Xep_gach([1,1,2,3,5,6,4,3,4,5,7,6,4,6,3,4,5,6,8,9,6,4,3,5,7,8,3,2,4,6,7]))


"""
Mua nhiều món đồ chơi nhất
TOY(arr,coin):
    num,i = 0,0
    A =[]
    arr.sort()
    while coin>=0:
        if i>= len(arr):
            break
        if coin - arr[i]>=0:
            num <- num + 1
            A.append(arr[i])
            coin <- coin - arr[i]
        i <- i+1
    return num ,A
        
"""
def  Toy(arr,Coin):
    num = 0 
    A = []
    arr.sort()
    i=0
    while(Coin>=0):
        if (i>=len(arr)):
            break
        if (Coin-arr[i] >= 0 and i<len(arr)):
            num+=1
            A.append(arr[i])
            Coin-=arr[i]
        i+=1
    return num,A
            
#print(Toy([73,88,68,88,41,33,11,46,49,17],300))

"""
Bài toán tổ chức cuộc họp 
"""
def meeting(s,e):
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            if (e[j]<e[i]):
                e[j],e[i] = e[i],e[j]
                s[j],s[i] = s[i],s[j]
    count = 0 
    end = 0 
    for i in range(n):
        if s[i]>=end:
            count +=1
            end = e[i]
    return count
#print(meeting([1,3,0,5,8,5],[2,4,6,7,9,9]))

"""
Tinh hieu lon nhat giua ca phan tu
"""
def maximizeSum(arr):
    sum =0
    arr.sort()
    n=len(arr)
    for i in range(1,n//2,2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    for i in range(n-1):
        sum=sum+arr[i]-arr[i+1] if (arr[i]>arr[i+1]) else sum+arr[i+1]-arr[i]
    sum=sum + arr[-1]-arr[0] if(arr[-1]>arr[0]) else sum+arr[0]-arr[-1]
    return sum
"""
Tim mang con lien tiep 
NumberofsubArr(arr):
    data ={}
    n = len(arr)
    maxAmount = 1
    for i from 1 to n :
        for j from 1 to  i-1:
            s =sum(arr[j:i]) 
            if s not in key(data):
                data[s] =[i-1,1]
            elif data[s][0]<j:
                data[s][1]+=1
                if data[s][1] >maxAmount:
                    maxAmount = data[s][1]
                data[s][0] = i-1
    return maxAmount

"""
def numberOfSubArray(arr):
    data = {}
    n = len(arr)
    maxAmount = 1
    for i in range(1, n + 1):
        for j in range(i):
            s = sum(arr[j:i])
            if s not in data:
                data[s] = [i - 1, 1]
            elif data[s][0] < j:
                data[s][1] += 1
                if data[s][1] > maxAmount: 
                    maxAmount = data[s][1]
                data[s][0] = i - 1
    return maxAmount