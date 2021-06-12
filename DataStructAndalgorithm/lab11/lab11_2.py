class Hash:
    def __init__(self,bucket):
        self.HashTable = [[] for _ in range(bucket)]
        self.bucket =bucket
        self.p = 1000000007
        self.x = 263
    
    def Hashing(self,S):
        s=0
        for i,val in enumerate(S):
            s+=ord(val)*self.x**i
        return s%self.p%self.bucket
    
    def printHashTable(self):
        print(self.HashTable)

    def Add_string(self,string):
        key = self.Hashing(string)
        if string not in self.HashTable[key]:
            self.HashTable[key].insert(0,string)
        else:
            return 

    def Del_string(self,string):
        key = self.Hashing(string)
        li = self.HashTable[key]
        if li == []:
            return 
        else:
            if string in li:
                i.remove(string)
                return
            else:
                return
    
    def Find_string(self,string):
        status ="no"
        for i in self.HashTable:
            if i == []:
                continue
            else:
                if string in i:
                    status="yes"
                    break
                else:
                    status="no"
        print(status)
    
    def check(self,i):
        print(*self.HashTable[i])
    
    def Select(self,array_select):
        for control in array_select:
            control = control.split(" ")
            if control[0] == "add":
                self.Add_string(control[1])
            elif control[0]=="check":
                self.check(int(control[1]))
            elif control[0]=="find":
                self.Find_string(control[1])
            elif control[0]=="del":
                self.Del_string(control[1])
            else:
                continue
bucket = int(input("Input Bucket for Hashing key: "))
#bucket=3
My_Hash = Hash(bucket)
n= int(input("Nhap n: "))
control=[]
for _ in range(n):
    str=input("Nhap: ")
    control.append(str)
#control =['add world','add HellO','check 4','find World','find world','del world','check 4','del HellO','add luck','add GooD','check 2','del good']
#control =["add test",'add test','find test','del test','find test','find Test','add Test','find Test']
#control = ["check 0",'find help','add help','add del','add add','find add','find del','del del','find del','check 0','check 1','check 2']
My_Hash.Select(control)