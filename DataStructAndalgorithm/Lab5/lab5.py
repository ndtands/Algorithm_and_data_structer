import time
#Quick Sort with 2 partition
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
def quick_sort2(array, start, end):
    if start >= end:
        return
    p = partition2(array, start, end)
    quick_sort2(array, start, p-1)
    quick_sort2(array, p+1, end)
        
#arr=[-18,66,-51,-28,41,77,60,-2,30,-19,-9,-53,65,-26,-13,-12,-32,3,84,4,-18,-14,15,-46,45,-5,-11,27,-49,-7]
#quick_sort2(arr,0,len(arr)-1)
#print(arr)

def partition3(arr,start,end):
    pivot,m1,m2 =arr[start],start,end
    i=m1
    while i<=m2:
        if arr[i] < pivot:
            arr[m1],arr[i]=arr[i],arr[m1]
            m1+=1
        elif arr[i]>pivot:
            arr[m2],arr[i] =arr[i],arr[m2]
            m2-=1
            i-=1 #Giữ nguyên i trong trường hợp này để tránh đảo những số đã lớn rồi 
        i+=1
    return m1,m2

def quick_sort3(arr, start, end):
    if start >= end:
        return
    m1, m2 = partition3(arr,start, end)
    quick_sort3(arr, start, m1 - 1)
    quick_sort3(arr, m2 + 1, end)


arr=[-57,-41,-15,53,-15,-30,9,55,-19,15,-44,-55,-10,-9,20,13,66,-42,-15,88,46,-67,-37,4,-15,-48,-17,34,20,39,-47,-36,-17,-76,38,-42,11,78,2,-30,-31,39,14,-27,-6,-16,-41,66,-15,-38,8,-21,38,32,-1,8,-48,-9,35,17,-10,14,2,-52,41,55,4,16,60,29,5,17,-4,-11,42,38,-69,-88,-45,12,5,-5,40,7,21,-83,52,10,74,39,9,49]
start =time.time()
quick_sort2(arr,0,len(arr)-1)
print("Time for Quick Sort 2 is {} s".format(time.time()-start))
print(arr)
arr=[-57,-41,-15,53,-15,-30,9,55,-19,15,-44,-55,-10,-9,20,13,66,-42,-15,88,46,-67,-37,4,-15,-48,-17,34,20,39,-47,-36,-17,-76,38,-42,11,78,2,-30,-31,39,14,-27,-6,-16,-41,66,-15,-38,8,-21,38,32,-1,8,-48,-9,35,17,-10,14,2,-52,41,55,4,16,60,29,5,17,-4,-11,42,38,-69,-88,-45,12,5,-5,40,7,21,-83,52,10,74,39,9,49]
start =time.time()
quick_sort3(arr,0,len(arr)-1)
print("Time for Quick Sort 3 is {} s".format(time.time()-start))
print(arr)