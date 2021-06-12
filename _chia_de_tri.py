def Search_binary(arr,left,right,key):
    if left >right:
        return -1
    mid = (left+right)//2
    if key ==arr[mid]:
        return mid
    elif key <arr[mid]:
        return Search_binary(arr,left,mid,key)
    elif key >arr[mid]:
        return Search_binary(arr,mid+1,right,key)
ar=[0,1,2,3,4,5,6]
print(Search_binary(ar,0,len(ar)-1,5))
def Search_binary(arr,key):
    left,right=0,len(arr)-1
    while left<=right:
        mid =(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            left = mid+1            
        else:
            right = mid-1
    return -1
ar=[0,1,2,3,4,5,6]
print(Search_binary(ar,5))     

def Count(arr,left,right,key):
    if left==right:
        if arr[left]==key:
            return 1
        else:
            return 0
    mid = (left+right)//2
    return Count(arr,left,mid,key)+Count(arr,mid+1,right,key)
