"""
FIFO
    class name :  MyQueue
    Atribute: queue: Nơi lưu trữ queue
    Method: enqueue,dequeue,size,isEmpty
    Description: information and method with queue
""" 
class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
        
    def isEmpty(self):
        return self.size()>0

"""
class name :  Persion
    Atribute:ID,Name,DoB,Birthplace,left,right
    Method: __str__: show name of object
    Description: information of persion
"""
class Persion:
    def __init__(self,ID,Name,DoB,Birthplace):
        self.ID  = ID
        self.Name = Name 
        self.DoB  = DoB
        self.Birthplace = Birthplace
        self.left = None  
        self.right = None

    def __str__(self):
        return str(self.Name) 

"""
class name :  MyBSTree
Atribute: 
    + root: node đầu tiên của cây
    + idsave: nơi lưu trữ ID
Method: 
    + AddData , InOrderFunction
    + inOrder, levelOrder
    + Search, delete
Description: Stored information and method for Binary Tree
"""     
class MyBSTree:
    def __init__(self):
        self.root = None
        self.idsave=set()
    """
    AddData:
        if root is None:
            root = NewNode
        else:
            while True:
                current = self.root
                if value < current.val:
                    if current.left is None:
                        add Node
                        break
                    else:
                        current = current.left
                if value > current.val:
                    if current.right is None:
                        add Node
                        break
                    else:
                        current = current.right
    """
    def AddData(self,ID,Name,DoB,Birthplace):
        if self.root == None:
            self.idsave.add(ID)
            self.root = Persion(ID,Name,DoB,Birthplace)
        else:
            current = self.root
            while True:
                if ID < current.ID:
                    if current.left:
                        current = current.left
                    else:
                        self.idsave.add(ID)
                        current.left = Persion(ID,Name,DoB,Birthplace)
                        break
                elif ID > current.ID:
                    if current.right:
                        current = current.right
                    else:
                        self.idsave.add(ID)
                        current.right = Persion(ID,Name,DoB,Birthplace)
                        break
                else:
                    break   
    """
    #left -> root -> right
    inOrderFunction(root):
        root is None:
        if root:
            inOrderFuntion(root.left)
            print(root)
            inOrderFuntion(root.right)
    """
    def inOrderFunction(self,root):
        if root is None:
            return 
        if root:
            self.inOrderFunction(root.left)
            print("  ".join([str(root.ID),str(root.Name),str(root.DoB),str(root.Birthplace)]))
            self.inOrderFunction(root.right)
    
    def inOrder(self):
        self.inOrderFunction(self.root)
    """
    levelOrder(root):
        if root is None:
            return 
        Queue q
        q.Enqueue(root)
        while q.Empty():
            node = queue.Dequeue()
            print(node)
            if node.left is not None:
                q.Enqueue(node.left)
            if node.right is not None:
                q.Enqueue(node.right)  
    """
    def levelOrder(self):
        if self.root is None:
            return 
        queue = MyQueue()
        queue.enqueue(self.root)
        while queue.isEmpty():
            node  = queue.dequeue()
            print("  ".join([str(node.ID),str(node.Name),str(node.DoB),str(node.Birthplace)]))
            #print(node.ID,end=" ")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)   
    """
    Giống như levelOrder
    """
    def Search(self,key):
        queue = MyQueue()
        queue.enqueue(self.root)
        while queue :
            node = queue.dequeue()
            if node is None:
                break
            if node.ID == key:
                return node 
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return -1
    """
    find min value và nó nằm ở bên trái cuối cùng
    """
    def minValueNode(self,node):
        current = node 
        while (current.left is not None ):
            current = current.left
        return current
    
    """
    deletefunction(root,key):
        check None
        if key <root.val:
            root.left = deletefunction(root.left,key)
        elif key >root.val:
            root.right = deletefunction(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            minNode = getMin
            root = minNode
            delete(minNode)
    """
    def deletefunction(self,root,key,flagShow):
        if root is None:
            return root
        if key < root.ID:
            root.left = self.deletefunction(root.left,key,flagShow)
        elif key > root.ID:
            root.right = self.deletefunction(root.right,key,flagShow)
        else:
            if root.left is None:
                if flagShow:
                    print("ID | Name | Day of Birth | Birthplace")
                    print("  ".join([str(root.ID),str(root.Name),str(root.DoB),str(root.Birthplace)]))
                    flagShow = False
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                if flagShow:
                    print("ID | Name | Day of Birth | Birthplace")
                    print("  ".join([str(root.ID),str(root.Name),str(root.DoB),str(root.Birthplace)]))
                    flagShow = False
                temp = root.left
                root = None
                return temp
            if flagShow:
                print("ID | Name | Day of Birth | Birthplace")
                print("  ".join([str(root.ID),str(root.Name),str(root.DoB),str(root.Birthplace)]))
                flagShow = False
            min_node = self.minValueNode(root.right)
            root.ID = min_node.ID
            root.Name = min_node.Name
            root.Birthplace = min_node.Birthplace
            root.DoB = min_node.DoB
            root.right = self.deletefunction(root.right,min_node.ID,flagShow)
        return root
    """
    Delete:
        check key là root đầu tiên mà chỉ có một trong hai nhánh:
            giải quyết trường hợp cụ thể này
        else:
            deletefunction()
    """
    def delete(self,key):
        try:
            flagShow = True
            self.idsave.remove(key)
            current = self.root
            if current.ID == key and (current.left is None or current.right is None):
                if(current.left is None):
                    self.root = current.right 
                else:
                    self.root = current.left
                print("ID | Name | Day of Birth | Birthplace")
                print("  ".join([str(current.ID),str(current.Name),str(current.DoB),str(current.Birthplace)]))
            else:
                self.deletefunction(self.root,key,flagShow)
            print("Delete sussesful")
        except:
            print("The deleted ID is not valid")

