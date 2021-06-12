class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def PrintLinked(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval,end =" ")
            printval = printval.nextval
    
    def InsertAtEnd(self,val):
        NewNode = Node(val)
        if self.head is None:
            self.head = NewNode
            return 
        temp = self.head
        while temp.nextval:
            temp= temp.nextval
        temp.nextval = NewNode
    
    def InsertbyIndex(self,index,val):
        NewNode = Node(val)
        if index == 0:
            NewNode.nextval = self.head
            self.head = NewNode
            return 
        if self.head is None:
            self.head = NewNode
            return 
        curr = self.head
        n = index -1
        while n >0 :
            curr = curr.nextval
            n-=1
        temp = curr.nextval 
        curr.nextval = NewNode # curr -> NewNode -> cur.next
        NewNode.nextval = temp

    def remove_Node_by_index(self,index):
        if self.head is None:
            return
        temp = self.head

        if index ==0:
            self.head = temp.nextval
            temp = None
            return 
        
        for _ in range(index -1 ):
            temp = temp.nextval
            if temp is None:
                break
        #Out of range and Node cuoi
        if temp is None or temp.nextval is None:
            return 
        curr_next = temp.nextval.nextval
        temp.nextval = curr_next

    def remove_Node_by_val(self,val):
        temp = self.head
        if temp is not None:
            if temp.dataval == val:
                self.head = temp.nextval
                temp = None
                return 
        while temp is not None:
            if temp.dataval == val:
                break
            prev = temp
            temp = temp.nextval
        if temp == None:
            return 
        prev.nextval = temp.nextval
        temp = None
    def Search(self,index):
        if self.head is None:
            return 
        if index ==0:
            return self.head.dataval
        temp = self.head
        for _ in range(index-1):
            temp = temp.nextval
        return temp.nextval.dataval
    
    def Replace(self,old,new):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            if temp.dataval == old:
                temp.dataval = new
            temp = temp.nextval

    def Select(self,index):
        value = None
        if self.head is None:
            return 
        temp = self.head

        if index ==0:
            value = temp.dataval
        else:
            for _ in range(index-1):
                temp = temp.nextval
            value = temp.nextval.dataval
            if value == None:
                return
            else:
                temp = self.head
                while temp != None:
                    if(temp.dataval>value):
                        self.remove_Node_by_val(temp.dataval)
                    temp= temp.nextval

ll = LinkedList()
arr = [1,2,3,3,2,1,2,3,4,8,9,5,4,6,8,9,5,45,66]
for i in arr:
    ll.InsertAtEnd(i)
ll.PrintLinked()
print("")
ll.Select(4)
ll.PrintLinked()