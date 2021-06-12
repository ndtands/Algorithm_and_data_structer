def Search(arr,left,right,key):
    if(left>right):
        return -1
    mid =left+(right-left)//2
    if key ==arr[mid]:
        return mid
    elif key <arr[mid]:
        return Search(arr,left,mid-1,key)
    elif key >arr[mid]:
        return Search(arr,mid+1,right,key)
A=[int(i) for i in input("Nhap A: ").split(" ")]
B=[int(i) for i in input("Nhap B: ").split(" ")]
A=A[1:]
B=B[1:]
arr = []
for i in B:
    arr.append(Search(A,0,len(A)-1,i))
print(arr)