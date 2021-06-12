#sumarray
#Binh phuong tung element
def BinhPhuong(arr):
    return list(map(lambda x:x*x,tuple(arr)))
#insert to arr
def InserArr(arr,index,val):
    arr.append(0)#add one to last arr
    for i in range(len(arr)-1,index,-1):
        arr[i]=arr[i-1]
    arr[index]=val
    return arr

#Remove arr
def Remove_arr(arr,index):
    for i in range(index,len(arr)-1):
        arr[i]=arr[i+1]
    return arr[:-1]

#merger arr
def Megerarr(arr1,arr2):
    i,j=0
    arr=[]
    while i<len(arr1) and j<len(arr2):
        if (arr[i]<arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.appedn(arr2[j])
            j+=1
    if i <len(arr1):
        arr+=arr1[i:]
    if j <len(arr2):
        arr+=arr2[j:]
    return arr

#Sum matrix
def Sum_matrix(A):
    return sum(list(map(sum,A)))
#print(Sum_matrix([[1,2],[3,4]]))

