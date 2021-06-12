class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class DoubleLinked:
    def __init__(self):
        self.head = None
    
    def AtEnd(self,val):
        newNode = Node(val)
        newNode.next = None
        if(self.head is None):
            newNode.prev = None
            self.head = newNode
            return
        temp = self.head
        #After end Node
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def AtBegin(self,val):
        newNode = Node(val)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    def PrintLinkedPrev(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.prev
        
    def PrintLinkedNext(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next

    def Insert_by_index(self,index,val):
        if index ==0:
            self.AtBegin(val)
            return val
        if self.head is None:
            return 
        else:
            temp = self.head
            while temp is not None:
                if temp.data == index:
                    break
                temp = temp.next
            if temp is None:
                print("out of range")
            else:
                new_node = Node(val)
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next is not None:
                    temp.next.prev = new_node
                temp.next = new_node
    def Delete_at_end(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
    def Delete_at_start(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head  = self.head.next
        self.head.prev = None

    def Delete_By_index(self,index):
        if self.head is None:
            return
        if self.head.next is None:
            if self.head.data == index:
                self.head = None
            return
        if index ==0:
            self.Delete_at_start()
            return 
        temp= self.head
        for _ in range(index-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None or temp.next is None:
            return 
        if temp.next.prev is not None and temp.next.next is None:
            self.Delete_at_end()
            return
        curr_next = temp.next.next
        temp.next = curr_next
        curr_next.prev = temp

arr = [1,2,3,4,5,6]
double = DoubleLinked()
for i in arr:
    double.AtEnd(i)
double.PrintLinkedNext()
print(" ")
double.Delete_By_index(5)

double.PrintLinkedNext()
print(" ")