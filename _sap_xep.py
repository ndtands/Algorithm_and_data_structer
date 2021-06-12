arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9,-1000,20000]
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def bb_sort(arr):
    _arr = arr.copy()
    n= len(_arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if _arr[j]>_arr[j+1]:
                swap(_arr,j,j+1)
    print(*_arr)
bb_sort(arr)

def inser_sort(arr):
    _arr = arr.copy()
    n = len(_arr)
    for i in range(1,n):
        for j in range(i):
            if _arr[j]>_arr[i]:
                swap(_arr,i,j)
    print(*_arr)
inser_sort(arr)

def select_sort(arr):
    _arr = arr.copy()
    n = len(arr)
    for i in range(n-1):
        _min = i
        for j in range(i+1,n):
            if _arr[j]< _arr[_min]:
                _min=j
        if i!=_min:
            swap(_arr,_min,i)
    print(*_arr)
select_sort(arr)
def merger_sort(arr,low=None,high=None):
    if low==None:
        low,high=0,len(arr)-1
    if low==high:
        return [arr[low]]
    else:
        mid=low+(high-low)//2
        left    = merger_sort(arr,low,mid)
        right = merger_sort(arr,mid+1,high)
        return Merger(arr,left,right)

def Merger(arr,left,right):
    i,j,new=0,0,[]
    while i <len(left) and j <len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    if i<len(left):
        new+=left[i:]
    if j <len(right):
        new+=right[j:]
    return new
arr_ =arr.copy()
print(*merger_sort(arr_))   

def partition2(arr,low,high):
    p,l,h=arr[low],low+1,high
    while True:
        while l<=h and arr[h]>=p:
            h-=1
        while l<=h and arr[l]<=p:
            l+=1
        if l<=h:
            swap(arr,h,l)
        else:
            break
    swap(arr,low,h)
    return h

def quicksort2(arr,low=None,high=None):
    if low==None:
        low,high=0,len(arr)-1
    if low>=high:
        return 
    p=partition2(arr,low,high) #return index privot
    quicksort2(arr,low,p)
    quicksort2(arr,p+1,high)
arr_=arr.copy()
quicksort2(arr_)
print(*arr_)

def quicksort3(arr,low=None,high=None):
    if low ==None:
        low,high=0,len(arr)-1
    if low >=high:
        return
    m1,m2=partition3(arr,low,high)
    quicksort3(arr,low,m1-1)
    quicksort3(arr,m2+1,high)

def partition3(arr,low,high):
    p,m1,m2 =arr[low],low,high
    i=m1
    while i<=m2:
        if arr[i]<p:
            swap(arr,m1,i)
            m1+=1
        elif arr[i]>p:
            swap(arr,m2,i)
            m2-=1
            i-=1 #Giữ nguyên i trong trường hợp này để tránh đảo những số đã lớn rồi 
        i+=1
    return m1,m2
arr_=arr.copy()
quicksort3(arr_)
print(*arr_)
arr=[-1,3,1,2,4,2,3,100,12,4,5,33,2,45,32]
'''def count_sort(arr):
    _min = min(arr)
    _max = max(arr)
    k=_max-_min +1
    count=[0]*k

    for i in arr:
        count[i-_min]+=1
    result=[]
    for i in range(len(count)):
        while count[i]>0:
            result.append(i+_min)
            count[i]-=1
    return result'''
def count_sort(arr):
    _min,_max =min(arr),max(arr)
    count=[0]*(_max-_min+1)
    for i in arr:
        count[i-_min]+=1
    out=[]
    for i in range(len(count)):
        while count[i]>0:
            out.append(i+_min)
            count[i]-=1
        i+=1
    return out
print(*count_sort(arr))