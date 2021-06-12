class Stack:
    def __init__(self,max_size=None):
        self.stack=[]
        if max_size==None:
            self.max_size = 250
        self.max_size=max_size

    def isEmptry(self):
        return not self.size()>0
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()


def isBalance(string):
    stack = Stack()
    open_list = ["[","{","("]
    close_list = ["]","}",")"] 
    for index,char in enumerate(string):
        if char in open_list:
            stack.push(index)    
        elif char in close_list:
            pos = close_list.index(char)
        if stack.isEmptry() and open_list[pos]==stack.top():
            stack.pop()
        else:
            return index+1
    if stack.isEmptry():
        print("OKe")
        return 
    else:
        return len(string)


#Queu pop(0),insert(0,val)