class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class SlinkedList:
  def __init__(self):
    self.start_node = None

  def listPrint(self):
    printval =self.start_node
    while printval is not None:
      print(printval.data,end=" ")
      printval =printval.next

  def insert_at_start(self,data):
    new_node = Node(data)
    new_node.next = self.start_node
    self.start_node = new_node
  
  def insert_at_end(self, data):
      new_node = Node(data)
      if self.start_node is None:
          self.start_node = new_node
          return
      temp = self.start_node
      while temp.next is not None:
          temp= temp.next
      temp.next = new_node
  
  def insert_after_item(self,x,data):
    temp =self.start_node
    print(temp.next)
    while temp is not None:
      if temp.data == x:
        break
      temp = temp.next
    if temp is None:
      print("item not found")
    else:
      new_node = Node(data)
      new_node.next = temp.next
      temp.next = new_node

  def insert_before_item(self, x, data):
    if self.start_node is None:
        print("List has no element")
        return

    if x == self.start_node.data:
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node
        return

    n = self.start_node
    print(n.next)
    while n.next is not None:
        if n.next.data == x:
            break
        n = n.next
    if n.next is None:
        print("item not in the list")
    else:
        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node
  
def mergeLists(headA, headB):
    if headA is None and headB is None:
      return None
    
    if headA is None:
      return headB

    if headB is None:
      return headA
    
    if headA.data < headB.data:
      smallerNode = headA
      smallerNode.next = mergeLists(headA.next, headB)
    else:
      smallerNode = headB
      smallerNode.next = mergeLists(headA, headB.next)
    
    return smallerNode
lst1 = SlinkedList()
lst2 = SlinkedList()
arr = [1,2,3,4,5]
for i in arr:
    lst1.insert_at_start(i)
    lst2.insert_at_end(i)
lst1.listPrint()
print("\n")
lst2.listPrint()
#lst3 = mergeLists(lst1.start_node,lst2.start_node)
#print(lst3.next.data)
print(lst1)
