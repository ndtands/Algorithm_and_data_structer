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

    def encode(self):
        out=""
        while(self.size()>0):
            temp = self.pop()
            count=1
            out+=temp
            while(self.size()>0):
                if self.top()==temp:
                    count+=1
                    self.pop()
                else:
                    print(self.top())
                    out+=str(count)
                    print(count)
                    break
        return out
    
arr="aaaacccsd"
arr=[i for i in arr]
print(arr)
AStack = Stack()
for i in arr:
    AStack.push(i)
print(AStack.stack)
print(AStack.encode())
                     
            