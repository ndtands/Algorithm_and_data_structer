class MaxHeap:
    def __init__(self):
        self.heap =[]
    def Parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def hasLeft(self,n,i):
        return self.left(i)<n
    def hasRight(self,n,i):
        return self.right(i)<n
    def printHeap(self):
        print(self.heap)
    def SiftDown(self,n,i):
        maxIndex = i
        if self.hasLeft(n,i) and self.heap[self.left(i)]>self.heap[maxIndex]:
            maxIndex = self.left(i)
        if self.hasRight(n, i) and self.heap[self.right(i)]>self.heap[maxIndex]:
            maxIndex = self.right(i)
        
        if maxIndex != i:
            self.heap[i],self.heap[maxIndex]= self.heap[maxIndex],self.heap[i]
            self.SiftDown(n,maxIndex)
    def siftUp(self,i):
        while i > 1  and self.heap[self.Parent(i)]>self.heap[i]:
            self.heap[i],self.heap[self.Parent(i)] =self.heap[self.Parent(i)],self.heap[i]
            i = self.Parent(i)  
    def BuildHeap(self):
        n= len(self.heap)
        for i in range(int(n/2)-1,-1,-1):
            self.SiftDown(n,i)   
    def HeapSort(self):
        n= len(self.heap)
        self.BuildHeap()
        self.printHeap()
        print("Here")
        for i in range(n-1,-1,-1):
            self.heap[0],self.heap[i]= self.heap[i],self.heap[0]
            self.printHeap()
            self.SiftDown(i,0)
    

    def ExtractMax():
        result = self.heap[0]
        
MyHeap = MaxHeap()
MyHeap.heap = [-1,2,4,10,4,-10,24,2,6,4,2]
MyHeap.HeapSort()
