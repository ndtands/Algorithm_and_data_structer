class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class Doublelinked:
    def __init__(self):
        self.head = None
    
    def AddEnd(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev =temp
    
    def AddBegin(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return 
        temp = self.head
        self.head = newNode
        newNode.next = temp
        temp.prev = newNode

    def Insert_by_index(self,val,index):
        new = Node(val)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        if index ==0:
            self.AddBegin()
        for _ in range(index-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            return
        temp_next = temp.next
        temp.next = new
        new.next = temp_next
        new.prev = temp
        temp_next.prev = new
    def Delete(self,index):
        if self.head is None:
            return
        temp = self.head
        if index ==0:
            self.head = temp.next
            temp.next.prev = None
        for _ in range(index-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            return
        temp_next = temp.next.next
        temp.next = temp_next
        temp_next.prev = temp