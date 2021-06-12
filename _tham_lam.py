def MinRefill(dist,gas_station,L):
    numRe,curRe,limit,n= 0,0,L,len(gas_station)
    while limit <dist:
        if curRe >=n or gas_station[curRe]>limit:
            return False
        while curRe < n-1 and gas_station[curRe+1] <= limit:
            curRe+=1
        numRe+=1
        limit = gas_station[curRe]+L
        curRe+=1
    return numRe
gas_stations=[200,375,750,850]
dist =950
L=400
print(MinRefill(dist,gas_stations,L))

def MinGroup(C,L):
    C.sort()
    i=0
    R=[]
    while i<len(C):
        [l,r]=[C[i],C[i]+L]
        R.append(l)
        i+=1
        while i<len(C) and r <=C[i]:
            i+=1
    return len(R)

print(MinGroup([1.1,1.2,1.5,2.6,2.8,3.9],1))

def Xep_tui(W,weigh,value):
    if len(weigh)!=len(value):
        return False
    data=sorted([[v/w,w] for w,v in zip(weigh,value)],reverse=True)
    A=[0]*len(weigh)
    values = 0 
    for i in range(len(weigh)):
        if W ==0:
            return A,values
        a = min(data[i][1],W)
        A[i]=a
        values+=a*data[i][0]
        W-=a
    return values,A
print(Xep_tui(7,[4,2,2],[20,18,14]))

def Toy(arr,coin):
    i,A=0,[]
    arr.sort()
    while coin >0:
        if i >=len(arr):
            break
        if coin -arr[i]>=0:
            A.append(arr[i])
            coin -=arr[i]
        i+=1
    return A,len(A)

def meet(start,end):
    save,end_,n=[],0,len(end)
    data = sorted([[e,s] for e,s in zip(end,start)])
    for i in range(n):
        if data[i][1]>=end_:
            save.append((data[i][1],data[i][0]))
            end_=data[i][0]
    return save,len(save)
print(meet([1,3,0,5,8,5],[2,4,6,7,9,9]))

def Doi_tien(n,arr):
    arr.sort(reverse=True)
    A=[0]*len(arr)
    index=0
    while index<len(arr):
        if n==0:
            return A,sum(A)
        if n>=arr[index]:
            n-=arr[index]
            A[index]+=1
        else:
            index+=1
    return A,sum(A)
print(Doi_tien(18,[2,5,10]))