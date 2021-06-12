class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]

def isBalanced(string):
    myStack=[]
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    for i,char in enumerate(string):
        if char in ['(','[','{']:
            myStack.append(char)
        elif char in [']','}',')']:
            #check la ngoac nao
            pos = close_list.index(char)
            if ((len(myStack) > 0) and (open_list[pos] == myStack[len(myStack)-1])):
                myStack.pop()
            else:
                return i+1
    if len(myStack) == 0:
        return "Success"
    else:
        return len(string)

print(isBalanced("[]"))
print(isBalanced("{}[]"))
print(isBalanced("[()]"))
print(isBalanced("(())"))
print(isBalanced("{[]}()"))
print(isBalanced("{"))
print(isBalanced("{[}"))
print(isBalanced("foo(bar);"))
print(isBalanced("fo{}{}()}o(bar[}i);"))