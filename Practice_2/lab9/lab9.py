
class TreeOrders:
    def __init__(self,key,left,right):
        self.key =key
        self.left = left
        self.right = right

    # left -> root -> right
    def inOrder(self, root=None,arr=None):
        if arr==None:
            arr = []
        if root == None:
            root = 0
        if self.left[root] != -1:
            self.inOrder(self.left[root],arr)
        arr.append(self.key[root])
        if self.right[root] != -1:
            self.inOrder(self.right[root],arr)
        return arr

    #root -> left -> right
    def preOrder(self, root=None,arr=None):
        if arr == None:
            arr=[]
        if root == None:
            root = 0
        arr.append(self.key[root])
        if self.left[root] != -1:
            self.preOrder(self.left[root],arr)
        if self.right[root] != -1:
            self.preOrder(self.right[root],arr)
        return arr

    #left -> right -> root
    def postOrder(self, root = None,arr=None):
        if arr == None:
            arr = []
        if root == None:
            root =0
        if self.left[root] != -1:
            self.postOrder(self.left[root],arr)
        if self.right[root] != -1:
            self.postOrder(self.right[root],arr)
        arr.append(self.key[root])
        return arr


num_node = int(input("Nhap so Node: "))
key,left,right=[0]*num_node,[0]*num_node,[0]*num_node
for i in range(num_node):
    [a,b,c] =[int(m.strip()) for m in input("Nhap Node left right:").split()]
    key[i],left[i],right[i]=a,b,c
tree = TreeOrders(key,left,right)
print(" ".join(str(x) for x in tree.inOrder()))
print(" ".join(str(x) for x in tree.preOrder()))
print(" ".join(str(x) for x in tree.postOrder()))

