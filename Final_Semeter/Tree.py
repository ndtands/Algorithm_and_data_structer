key = [4,2,5,1,3]
left = [1,3,-1,-1,-1]
right =[2,4,-1,-1,-1]
def inorder(root=None,arr=None):
    if root==None:
        root,arr=0,[]
    if left[root] != -1:
        inorder(left[root],arr)
    arr.append(key[root])
    if right[root] !=-1:
        inorder(right[root],arr)
    return arr
print(inorder())
def preorder(root=None,arr=None):
    if root ==None:
        root,arr=0,[]
    arr.append(key[root])
    if left[root] !=-1:
        preorder(left[root],arr)
    if right[root] != -1:
        preorder(right[root],arr)
    return arr
print(preorder())
def postorder(root=None,arr=None):
    if root ==None:
        root,arr=0,[]
    if left[root] !=-1:
        postorder(left[root],arr)
    if right[root] != -1:
        postorder(right[root],arr)
    arr.append(key[root])
    return arr
print(postorder())
def BFS():
    arr=[]
    root = 0
    queue=[]
    queue.append(root)
    while len(queue)!=0:
        root = queue.pop(0)
        arr.append(key[root])
        if left[root] != -1:
            queue.append(left[root])
        if right[root] !=-1:
            queue.append(right[root])
    return arr
print(BFS())