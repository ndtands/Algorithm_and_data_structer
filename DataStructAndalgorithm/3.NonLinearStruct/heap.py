class Maxheap:
    def __init__(self):
        self.heap=[]
    
    def Parent(self,i):
        return int((i-1)/2)
    
    def LeftChild(self,i):
        return 2*i+1
    
    def RightChild(self,i):
        return 2*i+2
    
    def hasParent(self,i):
        return self.Parent(i)<len(self.heap)
    
    def hasLeftChild(self,n,i):
        return self.LeftChild(i)<n
    
    def hasRightChild(self,n,i):
        return self.RightChild(i)<n

    def printHeap(self):
        print(self.heap)

        def SiftDown(self,n,i):
            maxIndex = i
            if self.hasLeftChild(n,i) and self.heap[self.LeftChild(i)] >self.heap[maxIndex]:
                maxIndex=self.LeftChild(i)
            if self.hasRightChild(n,i) and self.heap[self.RightChild(i)]>self.heap[maxIndex]:
                maxIndex=self.RightChild(i)

            if  maxIndex != i:
                self.heap[i],self.heap[maxIndex]= self.heap[maxIndex],self.heap[i]
                self.SiftDown(n,maxIndex)     
        
        def siftUp(self,i):
            while(self.hasParent(i) and self.heap[self.Parent(i)] >self.heap[i]):
                self.heap[i],self.heap[self.Parent(i)] =self.heap[self.Parent(i)],self.heap[i]
                i=self.Parent(i)
                
        def HeapSort(self):
            n=len(self.heap)
            for i in range(int(n / 2) - 1, -1, -1):
                self.SiftDown(n,i)
            for i in range(n-1,-1,-1):
                self.heap[0],self.heap[i]=self.heap[i],self.heap[0]
                self.SiftDown(i,0)


Heap = Maxheap()
Heap.heap =[5,4,3,2,1]
Heap.siftUp(len(Heap.heap)-1)
Heap.HeapSort()
Heap.printHeap()