def Count(a,left,right,key):
    if(left==right):
        if(a[left]==key):
            return 1
        else:
            return 0
    else:
        mid =(left+right)//2
        return Count(a,left,mid,key)+Count(a,mid+1,right,key)
def Phan_tu_da_so(arr):
    out=0
    for i in arr:
        if(Count(arr,0,len(arr)-1,i)>len(arr)//2):
            out=1
            break
    return out
print("Nhap mang A: ")
A=[int(i) for i in input().split(" ")]
print(Phan_tu_da_so(A))