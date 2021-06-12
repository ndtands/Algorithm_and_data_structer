class MyQueue:
    def __init__(self):
        self.queue =[]
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size()>0

class Node:
    def __init__(self,infor):
        self.infor = infor
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.infor)

class BTS:
    def __init__(self):
        self.root = None
    
    def _insert(self,root,val):
        if root is None:
            root = Node(val)
        elif val <root.infor:
            root.left = self._insert(root.left,val)
        elif val > root.infor:
            root.right = self._insert(root.right,val)
        return root
    def insert(self,value):
        self.root = self._insert(self.root,value)
    
    def _inorder(self,root):
        if root == None:
            return 
        else:
            self._inorder(root.left)
            print(root.infor,end=" ")
            self._inorder(root.right)
    def inorder(self):
        self._inorder(self.root)
    
    def _preorder(self,root):
        if root == None:
            return 
        else:
            print(root.infor,en='')
            self._preorder(root.left)
            self._preorder(root.right)

    def _postorder(self,root):
        if root == None:
            return 
        else:               
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.infor,en='')
    
    def levelorder(self):
        if self.root is None:
            return 
        queue = MyQueue()
        queue.enqueue(self.root)
        while queue.isEmpty():
            node = queue.dequeue()
            print(node)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    
    def Search(self,key):
        if self.root is None:
            return 
        Queue = MyQueue()
        Queue.enqueue(self.root)
        while Queue.isEmpty():
            node = Queue.dequeue()
            if node.infor == key:
                return node
            if node.left:
                Queue.enqueue(node.left)
            if node.right:
                Queue.enqueue(node.right)
        return -1
    
    def minvalueNode(self,node):
        curr= node
        while curr.left is not None:
            curr= curr.left

        return curr
    
    def delete(self,root,key):
        if root is None:
            return root
        if key <root.infor:
            root.left = self.delete(root.left,key)
        elif key >root.infor:
            root.right = self.delete(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp =root.left
                root = None
                return temp
            min_node = self.minvalueNode(root.right)
            root = min_node
            root.right = self.delete(root.right,min_node)
        return root 