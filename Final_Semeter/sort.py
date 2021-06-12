def Bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>=arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def swap(a,b):
    return b,a
def Insertion(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i):
            if arr[j] >= arr[i]:
                arr[i],arr[j]=swap(arr[i], arr[j])
    return arr
def Selection(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] <arr[min]:
                min = j
        if min != i :
            arr[i],arr[min]=swap(arr[i], arr[min])
    return arr

def Merge(l_arr,r_arr):
    new =[]
    i,j=0,0
    while i<len(l_arr) and j<len(r_arr):
        if l_arr[i]<=r_arr[j]:
            new.append(l_arr[i])
            i+=1
        else:
            new.append(r_arr[j])
            j+=1
    if i <len(l_arr):
        new +=l_arr[i:]
    if j <len(r_arr):
        new+=r_arr[j:]
    return new
def MergeSort(arr,start=None,end=None):
    if start ==None and end == None:
        start,end = 0,len(arr)-1
    if start == end:
        return [arr[start]]
    else:
        mid = (start+end)//2
        left= MergeSort(arr,start,mid)
        right= MergeSort(arr,mid+1,end)
        return Merge(left, right)


def partition(arr,start,end):
    p,l,h = arr[start],start+1,end
    while True:
        while l<=h and arr[h]>=p:
            h-=1
        while l<=h and arr[l]<=p:
            l+=1
        if l<=h:
            arr[l],arr[h]=swap(arr[l], arr[h])
        else:
            break
    arr[start],arr[h]=swap(arr[start],arr[h])
    return h

def quicksort(arr,start=None,end=None):
    if start ==None and end == None:
        start,end = 0,len(arr)-1
    if start >= end:
        return
    p = partition(arr, start, end)
    quicksort(arr,start,p)
    quicksort(arr,p+1,end)

arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9]
print(Bubble(arr))
arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9]
print(Selection(arr))
arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9]
print(Insertion(arr))
arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9]
print(MergeSort(arr))
arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9]
quicksort(arr)
print(arr)