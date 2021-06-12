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

    def isEmpty(self):
        return not self.size()>0
"""
pesudocode:
    Create empty Stack
    for char in string:
        if char in open_list:
            push char to stack
        else if char in close_list:
            pos = Vị trí của char trong chuỗi kí tự close
            if open_list[pos] == stack.top():
                stack,pop()
            else:
                return position of char in string
    if Stack is empty:
        reutrn Susscess
    else:
        return len(String)

"""
def isBalanced(string):
    myStack=Stack()
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    for i,char in enumerate(string):
        if char in open_list:
            myStack.push(char)
        elif char in close_list:
            #check la ngoac nao
            pos = close_list.index(char)
            if ((myStack.size() > 0) and (open_list[pos] == myStack.top())):
                myStack.pop()
            else:
                #Exit
                return i+1
    if  myStack.isEmpty() :
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
print(isBalanced("fo[{}{}()}o(bar[}i);"))