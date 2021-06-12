#bai toan do xang
"""
pesudocode:
Min(dist,L,gas_station):
    numRefills <- 0
    currentfills <- 0
    limit <- L
    n <- len(gas_station)
    while limit <=dist:
        if currentfills >=n or gas_station(currentfills)>limit:
            return -1
        while currentfills <n-1 and gas_station[currenfill+1] <=limit:
            currentfills <= currentlls+1
        numRefill <- Numrefill +1
        limit <- gas_station[numRefills]+L
        curRefill+=1
    return numRefill
"""
def MinRefill(dist,L,gas_station):
    numRefill,curStation,limit = 0,0,L
    max_station = len(gas_station)
    while limit <dist:
        if curStation >= max_station or gas_station[curStation]>limit:
            return -1
        while curStation <max_station-1 and gas_station[curStation+1] <= limit:
            curStation +=1
        numRefill+=1
        limit = gas_station[numRefill]+L
        curStation+=1
    return numRefill

def MinRefill_1(dist,L,gas_station):
    num_refill,cur_station,limit=0,0,L
    max_station = len(gas_station)
    while limit <dist:
        if cur_station>max_station and gas_station[cur_station+1] >limit:
            return False
        while cur_station<max_station-1 and gas_station[cur_station+1]<limit:
            cur_station+=1
        num_refill+=1
        limit =gas_station[cur_station]+L
        cur_station+=1
    return num_refill
gas_stations=[200,375,750,850]
dist =950
L=400

print(MinRefill(dist,L,gas_stations))

#bai toan mingroup 
def MinGroup(C,L):
    C.sort()
    R =[]
    n = len(C)
    i=0
    while i <n:
        [l,r]=[C[i],C[i]+L]
        R.append(l)
        i+=1
        while i<n and C[i]<=r:
            i+=1
    return len(R)   

def MinGroup(C,L):
    C.sort()
    R=[]
    n=len(C)
    i=0
    while i<n:
        [l,r]=[C[i],C[i]+L]
        R.append(l)
        i+=1
        while C[i]<=r and i<n:
            i+=1
    return len(R)
#print(MinGroup([1.1,1.2,1.5,2.6,2.8,3.9],1))

#Bai taon Xep tui 
def Knapsack_optimize(W,weight,value):
    if len(weight)!=len(value):
        return False
    data = sorted([[v/w,w] for w,v in zip(weight,value)],reverse=True)
    A = [0]*len(weight)
    values = 0
    for i in range(len(weight)): 
        if W==0:
            return values,A
        a = min(data[i][1],W)
        values += a*data[i][0]
        data[i][1]-=a
        A[i] +=a
        W-=a
    return values,A
#print(Knapsack_optimize(7,[4,2,2],[20,18,14]))

#Bai toan trong hoa
def All_flower(arr):
    max_day =0
    for day,hoa in enumerate(arr):
        b_day = (day+1)+hoa
        if b_day > max_day :
            max_day = b_day
    return max_day


#Mua duoc nhieu mon do choi nhat
def Toy(arr,coin):
    i=0
    arr.sort()
    A=[]
    while coin >= 0:
        if i>=len(arr):
            break
        if coin - arr[i]>=0:
            A.append(arr[i])
            coin -= arr[i]
        i+=1
    return A,len(A)
#print(Toy([73,88,68,88,41,33,11,46,49,17],300))

def meet(start,end):
    n = len(start)
    data = sorted([[e,s] for e,s in zip(end,start)])
    end = 0
    save =[]
    for i in range(n):
        if data[i][1]>=end:
            save.append([data[i][1],data[i][0]])
            end = data[i][0]
    return save,len(save)
print(meet([1,3,0,5,8,5],[2,4,6,7,9,9]))

