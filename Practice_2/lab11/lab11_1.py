class Lab11_1:
    def __init__(self,):
        self.memory={}
    
    def Add(self,number,name):
        self.memory[number]=name
    
    def Find(self,number):
        for num,name in self.memory.items():
            if num==number:
                print(name)
                return
        print("not found")
    
    def Delete(self,number):
        temp=None
        for num,name in self.memory.items():
            if num==number:
                temp=number
        if temp!=None:
            del self.memory[temp]
        else:
            return 
    
Lab = Lab11_1()
'''n= int(input("Nhap n: "))
control=[]
for _ in range(n):
    str=input("Nhap: ")
    control.append(str)'''
#control=['find 28', 'add 123 me', 'add 0 granny', 'find 0', 'find 123', 'del 0', 'del 0', 'find 0']
control=['add 911 police','add 76213 Mom','add 17239 Bob','find 76213','find 910','find 911','del 910','del 911','find 911','find 76213','add 76213 daddy','find 76213']
for str in control:
    str=str.split(" ")
    if str[0] == "add":
        Lab.Add(int(str[1]),str[2])
    elif str[0] == "find":
        Lab.Find(int(str[1]))
    elif str[0] =="del":
        Lab.Delete(int(str[1]))
    else:
        continue

