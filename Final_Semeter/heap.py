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
    
    