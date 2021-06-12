def LinearSearch(A,low,high,key):
    if high <low:
        return False
    if A[low]==key:
        return low
    return LinearSearch(A,low+1,high,key)
Arr=[1,3,51,2,5,3,7,5,21,2,52,5,9]
#print(LinearSearch(Arr,0,len(Arr)-1,7))

def BinarySearch(A,low,high,key):
    if high <low:
        return False
    mid = int(low+(high-low)/2)
    if key == A[mid]:
        return mid
    elif key > A[mid]:
        return BinarySearch(A,mid+1,high,key)
    else:
        return BinarySearch(A,low,mid-1,key)
'''Arr.sort()
print(Arr)
print(BinarySearch(Arr,0,len(Arr)-1,21))'''

def BinarySearchIt(A,low,high,key):
    while low <= high:
        mid = int(low+(high-low)/2)
        if key== A[mid]:
            return mid
        elif key <A[mid]:
            high = mid -1
        else:
            low = mid +1
    return low -1
'''Arr.sort()
print(Arr)
print(BinarySearchIt(Arr,0,len(Arr)-1,21))'''


def similarStrings(a,b):
    if a==b:
        return True
    elif len(a)==len(b)and len(a)%2==0:
        a1=a[0:len(a)//2]
        a2=a[len(a)//2:]
        b1=b[:len(b)//2]
        b2=b[len(b)//2:]
        return similarStrings(a1,b1) and similarStrings(a2,b2) or similarStrings(a1,b2) and similarStrings(a2,b1)
    else:
        return False
    
#print(similarStrings('aaba','abaa'))

def Count(a,left,right,key):

    if (left == right):
        if(a[left]==key):
            return 1
        else:
            return 0
    else:

        mid =(left+right)//2
        return Count(a,left,mid,key)+Count(a,mid+1,right,key)

arr =[1,2,1,1,2,2,1] 
#print(Count(arr,0,len(arr)-1,1))
'''def countOccurrencePairs(arr):
    count =0
    n= len(arr)
    for i in range(1,n-1):
        for j in range(i+1,n):
            a = Count(arr[1:i+1],0,len(arr[1:i+1])-1,arr[i])
            b = Count(arr[j:],0,len(arr[j:])-1,arr[j])
            if(a>b):
                print(i,j)
countOccurrencePairs(arr)'''
def countOccurrencePairs(arr,i=0,count=0):
    n= len(arr)
    if i == n-1:
        return count
    for j in range(i+1,n):
        a = Count(arr[0:i+1],0,len(arr[0:i+1])-1,arr[i])
        b = Count(arr[j:],0,len(arr[j:])-1,arr[j])
        if(a>b):
            count+=1
    return countOccurrencePairs(arr,i+1,count)
print(countOccurrencePairs(arr))