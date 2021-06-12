def search(arr,key,low=None,high=None):
    if low ==None:
        low = 0
    if high ==None:
        high = len(arr)-1
    if high<low:
        return -1
    if arr[low]==key:
        return low
    return search(arr,key,low+1,high)
#Arr=[1,3,51,2,5,3,7,5,21,2,52,5,9]
#print(search(Arr,7))

def BinarySearch(arr,key,low=None,high=None):
    if low ==None:
        low =0
    if high == None:
        high =len(arr)-1
    mid = int(low+(high-low)/2)
    if high <low:
        return -1
    if key ==arr[mid]:
        return mid
    elif key >arr[mid]:
        return BinarySearch(arr, key,mid+1,high)
    else:
        return BinarySearch(arr, key,low,mid-1)
#Arr.sort()
#print(Arr)
#print(BinarySearch(Arr,21))

def similarStrings(a,b):
    if a==b:
        return True
    elif len(a)==len(b) and len(a)%2==0:
        a1=a[0:len(a)//2]
        a2=a[len(a)//2:]
        b1=b[:len(b)//2]
        b2=b[len(b)//2:]
        return similarStrings(a1,b1) and similarStrings(a2,b2) or similarStrings(a1,b2) and similarStrings(a2,b1)
    else:
        return False

def Count(a,k,l=None,r=None):
    if l==None and r==None:
        l,r=0,len(a)-1
    if (l==r):
        if(a[l]==k):
            return 1
        else:
            return 0
    else:
        mid = (l+r)//2
        return Count(a,k,l,mid)+Count(a,k,mid+1,r)
arr=[1,2,1,1,2,2,1] 
def Count(arr,key,left=None,right=None):
    if left==None and right==None:
        left =0
        right=len(arr)-1
    if left==right:
        if key==arr[left]:
            return 1
        else:
            return 0
    else:
        mid =(left+right)//2
        return Count(arr,key,left,mid)+Count(arr,key,mid+1,right)
#print(Count(arr, 2))

'''
def countOccurrencePairs(arr,i=0,count=0):
    n= len(arr)
    if i == n-1:
        return count
    for j in range(i+1,n):
        a = Count(arr[0:i+1],arr[i])
        b = Count(arr[j:],arr[j])
        if(a>b):
            count+=1
    return countOccurrencePairs(arr,i+1,count)
print(countOccurrencePairs(arr))'''

'''def get_majority_element(a,left,right):
    if left ==right:
        return -1
    if left+1 ==right:
        return a[left]'''
    
def Search_Binary(arr,key,left=None,right=None):
    if left==None and right==None:
        left,right=0,len(arr)-1
    if high <low:
        return False
    mid =(left+right)//2
    if arr[mid]==key:
        return mid
    if key <arr[mid]:
        return BinarySearch(arr, key,left,mid)
    else:
        return BinarySearch(arr, key,mid+1,right)

