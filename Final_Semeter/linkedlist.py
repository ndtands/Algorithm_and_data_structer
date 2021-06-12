class Node:
    def __init__(self,data=None,next=None):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def listPrint(self):
        p = self.head
        while p is not None:
            print(p.data,end=" ")
            p = p.next
        
    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def delete_node(self,index):
        if self.head is None:
            return
        temp = self.head 
        if index ==0:
            self.head = temp.next
            temp = None
            return 
        for _ in range(index-1):
            temp = temp.next

        nextval = temp.next.next
        temp.next = None
        temp.next = nextval            