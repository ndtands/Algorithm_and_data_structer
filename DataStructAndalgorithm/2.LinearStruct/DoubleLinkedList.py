class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def listPrint(self):
        printval = self.start_node
        while printval is not None:
            print(printval.data, end=" ")
            printval = printval.next
    def insert_in_emptylist(self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self,data):
        if self.start_node is None:
            new_node= Node(data)
            self.start_node = new_node
            print("Node inserted")
            return 
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node 

    def insert_at_end(self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return 
        temp = self.start_node
        while temp.next is not None:
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node
        new_node.prev = temp
    
    def insert_after_item(self,x,data):
        if x==0:
            self.insert_at_start(data)
            return 

        if self.start_node is None:
            print("List is empty")
            return 
        else:
            temp = self.start_node
            while temp is not None:
                if temp.data == x:
                    break
                temp = temp.next
            if temp is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next is not None:
                    temp.next.prev = new_node
                temp.next = new_node
    
    def insert_before_item(self,x,data):
        if self.start_node is None:
            print("List is empty")
            return 
        else:
            temp = self.start_node
            while temp is not None:
                if temp.data ==x:
                    break
                temp = temp.next
            if temp is None:
                print("item not in the list")

            else:
                new_node = Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = new_node
                temp.prev = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return 
        self.start_node = self.start_node.next
        self.start_node.prev = None 

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        temp = self.start_node
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None   

    def delete_by_value(self,x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            if self.start_node.data == x:
                self.start_node = None
            else:
                print("Data not found")
            return 
        #delete the fist element
        if self.start_node.data ==x:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return

        temp = self.start_node
        while temp.next is not None:
            if temp.data ==x:
                break
            temp = temp.next
        if temp.next is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        else:
            #delete the last element
            if temp.data ==x:
                temp.prev.next = None
            else:
                print("Element not found")
    def delete_after_value(self,x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            if self.start_node.data == x:
                self.start_node = None
            else:
                print("Data not found")
            return 
        if x==0:
            self.delete_at_start()
            return 
        temp = self.start_node
        while temp.next is not None:
            if temp.data ==x:
                break
            temp = temp.next
        print(temp.data)
        if temp.next is not None:
            if temp.next.next is not None:
                A                   = temp.next.next
                temp.next           = A
                A.prev              = temp
            else:
                self.delete_at_end()
                return 
        else:
            #delete the last element
            if temp.data ==x:
                return 
            else:
                print("Element not found")
    def reverse_liked_link(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        temp = self.start_node
        temp_next = temp.next
        temp.next = None
        temp.prev = temp_next
        while temp_next is not None:
            temp_next.prev = temp_next.next
            temp_next.next = temp
            temp = temp_next
            temp_next = temp_next.prev
        self.start_node = temp
doubleLink = DoublyLinkedList()
arr=[1,2,3,4]
for i in arr :
    doubleLink.insert_at_end(i)
doubleLink.reverse_liked_link()
doubleLink.listPrint()