def siftDown(arr, n, i,save):
    min = i # Initialize min as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2
    if l < n and arr[l] < arr[min]:
        min = l
    if r < n and arr[r] < arr[min]:
        min = r
    if min != i:
        arr[i], arr[min] = arr[min], arr[i]
        save.append([i,min])
        siftDown(arr, n, min,save)
    return save   
  
def buildHeap(arr, n):
    startIdx = n // 2 - 1
    save=[]
    for i in range(startIdx, -1, -1):
        siftDown(arr, n, i,save)
    return save
if __name__ == '__main__':
    arr=[]
    n=int(input("Nhap n: "))
    for i in range(n,0,-1):
        arr.append(i)
    print("Original array: ",*arr)
    n = len(arr)
    temp= buildHeap(arr, n)
    print("Number of swap is: ",len(temp))
    for i in temp:
        print("position swap is: ",i[0],"and",i[1])
    print("After change: ",*arr)
      