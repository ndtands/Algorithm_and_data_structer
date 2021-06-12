class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def PrintList(self):
        temp =self.head
        if temp is None:
            return 
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("")
    
    def InserAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def InsertAtstart(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return 
        newNode.next = self.head
        self.head = newNode
    
    def InsertbyIndex(self,data,index):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        if index==0:
            self.InsertAtstart(data)
        temp = self.head
        for _ in range(index-1):
            temp =temp.next
        temp_next = temp.next
        temp.next = newNode
        newNode.next = temp_next

    def remove_by_index(self,index):
        if self.head is None:
            return 
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            return 
        curr_next = temp.next.next
        temp.next = curr_next