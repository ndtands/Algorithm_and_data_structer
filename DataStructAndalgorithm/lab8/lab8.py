class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        
    def __str__(self):
        return str(self.info) 

'''class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            if()'''

def preOrder(root):
    if root:
        print(str(root.info)+" ", end="") #print on same line
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.info)+" ", end="") #print on same line
def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(str(root.info)+" ", end="") #print on same line
        inOrder(root.right)
def height(root):
    if root is None:
        return -1
    return max(1 + height(root.left), 1 + height(root.right))
    
from collections import deque

def levelOrder(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.info, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()
def lca(root, a, b):
  node = root
  while node:
    if max(a, b) < node.info:
      node = node.left
    elif min(a, b) > node.info:
      node = node.right
    else:
      break
  return node

def topView(root):
    # Initialize the level
    this_level = [(root, 0)]
    scores = {}
    while this_level:
        # Basically iterate over the nodes on a single level
        for _ in range(len(this_level)):
            node, score = this_level.pop(0)
            # Skip empty nodes
            if not node:
                continue
            # Store the score if it's a new one!
            if score not in scores:
                scores[score] = node.info
            # Add the node children to the next level
            this_level.extend(
                [(node.left, score - 1),
                (node.right, score + 1)])

    # Sort the scores and print their values 
    # (By default the sort is on the tuple first element: the score)
    for _, value in sorted(list(scores.items())):
        print(value, end=' ')

def check_binary_search_tree_(root):
    tree = []
    
    def in_order(root):
        if root is None: return
        in_order(root.left)
        tree.append(root.data)
        in_order(root.right)
    
    in_order(root)
    return len(tree) == len(set(tree)) and tree == list(sorted(tree))

'''
A=BinarySearchTree()
arr=[4,-1,4,1]
arr.sort()
for i in arr:
    A.create(i)
print(height(A.root))
'''