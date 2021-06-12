class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.start_node = None

    def listQueue(self):
        printval =self.start_node
        while printval is not None:
            print(printval.data,end=" ")
            printval =printval.next

  
    def enqueue(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        temp = self.start_node
        while temp.next is not None:
            temp= temp.next
        temp.next = new_node
    def dequeue(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        print(self.start_node.data)
        self.start_node = self.start_node.next
 
  
    
lst1 = Queue()
arr = [1,3,2,23,452,3]
for i in arr:
    lst1.enqueue(i)
lst1.dequeue()
lst1.listQueue()