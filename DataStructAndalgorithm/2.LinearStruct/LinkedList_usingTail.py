'''class Node:
    def __init__(self,node_data):
        self.data = node_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self,node_data):
        node = Node(node_data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data,end=" ")
        node = node.next
    print("")

'''
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

def mergeLists(h1, h2):
    if not h1 or not h2:
        return h1 or h2

    head, h1, h2 = (h1, h1.next, h2) if min([h1.data, h2.data]) == h1.data else (h2, h1, h2.next)
    curr = head
    while h1 or h2:

        if not h1 or not h2:
            curr.next = h1 or h2
            return head

        curr.next, h1, h2 = (h1, h1.next, h2) if min([h1.data, h2.data]) == h1.data else (h2, h1, h2.next)
        curr = curr.next
    return head


lst1 = LinkedList()
lst2 = LinkedList()
arr1 = [1,2,4,5,7]
arr2 = [1,3,6]
for i in arr1:
    lst1.insert_node(i)
for i in arr2:
    lst2.insert_node(i)
print_singly_linked_list(lst1.head)
print_singly_linked_list(lst2.head)
lst3 = mergeLists(lst1.head,lst2.head)

print_singly_linked_list(lst3)
