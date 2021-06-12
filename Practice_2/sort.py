"""
Bubble sort
    for i from 0 to n-2
        for j from 0 t0 n-2-i:
            if a[j]>a[j+1]:
                swap(a[j],a[j+1])
O(n^2)
"""
arr=[1,2,3,-12,4,-12,3,-2,0]

def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
#print(Bubble_Sort(arr))

"""
Insertion sort
    for i from 1 to n-1:
        for j from 0 to i:
            if a[i] <a[j]
                swap(a[i],a[j])
O(N^2)
"""
def Insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                 arr[j],arr[i]=arr[i],arr[j]
    return arr
#print(Insertion_sort(arr))

"""
selection sort:
    for i from 0 to n-2:
        min = i 
        for j from i+1,n-1:
            if a[j] <a[min]:
                min =j
        if min != i :
            swap(a[i],a[min])
    return a
O(N^2)  
"""
def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j 
        if i != min:
            arr[min],arr[i]=arr[i],arr[min]
    return arr
#print(selection_sort(arr))

"""
Mergesort(arr,left,right):
    if left==right:
        return [arr[left]]
    else:
        middle = (left+right)//2
        left_arr = Mergesort(arr,left,middle)
        right_arr = Mergesort(arr,middle+1,right)
        return Merge(left_arr,right_arr)

#Ghép 2 mảng lại với nhau mà đảm những phần từ nhỏ nằm về một bên
Merge(lef_arr,right_arr):
    new_arr =[]
    i=0
    j=0
    while i<len(left_arr) and j <len(right_arr):
        if left_arr[i]<right_arr[j]:
            new_arr.add(left_arr[i])
            i+=1
        else:
            new_arr.add(right_arr[j])
            j+=1
    if i<len(left_arr):
        new_arr+=left_arr[i:]
    if j <len(right_arr):
        new_arr += right_arr[j:]
    return new_arr
T(n)<= 2T(n/2)+O(n)
O(nlog(n))
Memory: O(n)
"""
def Merge(left_arr, right_arr):
    new_arr = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            new_arr.append(left_arr[i])
            i += 1
        else:
            new_arr.append(right_arr[j])
            j += 1
    #add các phần tử còn lại nếu có
    if i < len(left_arr):
        new_arr += left_arr[i:]
    # add các phần tử còn lại nếu có
    if j < len(right_arr):
        new_arr += right_arr[j:]
    return new_arr

def MergeSort(arr, start, end):
    if start == end: 
        return [arr[start]]
    else:
        middle = (start + end) // 2
        left_arr = MergeSort(arr, start, middle) 
        right_arr = MergeSort(arr, middle+1, end)
        return Merge(left_arr, right_arr)

#print(Merge([3,9,5,2], [1,11,10]))
#print(MergeSort(arr,0,len(arr)-1))

"""
Quick_sort 2 
Thay đổi mảng cho đúng yêu cầu 
A[k] <= x for all k from l+1 to j 
A[k] > x for all k from j+1 to i 

def partition2(arr,start,end):
    pivot,low,high = arr[start],start+1,end
    while True:
        #Check từ end vào có thỏa không
        while low <=high and arr[high]>=pivot:
            high = high-1
        #Check từ start lên có thỏa không
        while low <=high and arr[low] <=pivot:
            low=low+1
        #Ko thỏa thì tiến hành hoán đổi
        if low<=high:
            arr[low],arr[high]=arr[high],arr[low]
        else:
            break
    #Chuyen pivot vao dung vi tri , luu vao high
    arr[start],arr[high] =arr[high],arr[start]
    return high
"""