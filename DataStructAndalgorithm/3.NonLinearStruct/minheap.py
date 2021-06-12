# Python3 implementation of Min Heap
 
import sys
 
class MinHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
 
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
 
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
 
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
 
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
 
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
 
    # Function to heapify the node at pos
    def minHeapify(self, pos):
 
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
 
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
 
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
 
        current = self.size
 
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
 
    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
 
    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
 
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
 
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
 
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
 
# Driver Code
if __name__ == "__main__":
     
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
    print(minHeap.Heap)










'''
    class Maxheap:
    def __init__(self):
        self.heap=[]
        self.size = len(self.heap)
    
    def Parent(self,i):
        return int((i-1)/2)
    
    def LeftChild(self,i):
        return 2*i+1
    
    def RightChild(self,i):
        return 2*i+2
    
    #Check node i has a parent or not
    def hasParent(self,i):
        return self.Parent(i)<len(self.heap)
    
    def hasLeftChild(self,n,i):
        return self.LeftChild(i)<n
    
    def hasRightChild(self,n,i):
        return self.RightChild(i)<n
    
    def siftUp(self,i):
        while(self.hasParent(i) and self.heap[i]>self.heap[self.Parent(i)]):
            self.heap[i],self.heap[self.Parent(i)]=self.heap[self.Parent(i)],self.heap[i]
            i  = self.Parent(i)
    
    def printHeap(self):
        print(self.heap)
    
    def insert(self,value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)
    
    def getMax(self):
        return self.heap[0]
    
    def SiftDown(self,n,i):
        maxIndex = i
        if self.hasLeftChild(n,i) and self.heap[self.LeftChild(i)] <self.heap[maxIndex]:
            maxIndex=self.LeftChild(i)
        if self.hasRightChild(n,i) and self.heap[self.RightChild(i)]<self.heap[maxIndex]:
            maxIndex=self.RightChild(i)

        if  maxIndex != i:
            self.heap[i],self.heap[maxIndex]=  self.heap[maxIndex],self.heap[i]    
            self.SiftDown(n,maxIndex)     
    
    def ExtractMax(self):
        result = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap=self.heap[:-1]
        self.SiftDown(0)
        return result
    
    def Remove(self,i):
        self.heap[i] = float("inf")
        self.siftUp(i)
        self.ExtractMax()
    
    def ChangePriority(self,i,p):
        old_p = self.heap[i]
        self.heap[i] = p
        if p>old_p:
            self.siftUp(i)
        else:
            self.SiftDown(i)

    def BuldHeap(self,n):
        for i in range(int(n/ 2) - 1, -1, -1):
            self.SiftDown(n,i)

    def HeapSort(self):
        n=self.size
        self.BuldHeap(self.size)
        for i in range(n-1,-1,-1):
            self.heap[0],self.heap[i]=self.heap[i],self.heap[0]
            self.SiftDown(i,0)

Heap = Maxheap()
Heap.heap =[1,2,4,5,4,12,4,2] 
Heap.printHeap()
Heap.HeapSort()
Heap.printHeap()'''
