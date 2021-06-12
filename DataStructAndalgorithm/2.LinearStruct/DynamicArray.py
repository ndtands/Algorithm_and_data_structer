class DynamicArray(object):
  def __init__(self):
    self.n = 0 #len
    self.capacity=1
    self.A = self.make_array(self.capacity) # create Array with capacity element
  def __len__(self):
    return self.n

  def __getitem__(self,index):
    if not 0<= index <self.n:
      return IndexError('K is out of bounds')
    return self.A[index]

  def __set__(self,index,val):
    if not 0<= index <self.n:
      return IndexError('K is out of bounds')
    self.A[index] = val
  
  #PushBack(val) - O(n)
  def append(self,val):
    #over capacity
    if self.n ==self.capacity:
      self._resize(2*self.capacity)
    self.A[self.n]=val
    self.n+=1

  def insertAt(self,val,index):
    if(index<0 or index >self.n):
      print("please enter approproate index....")
      return
    if self.n == self.capacity:
      self._resize(2*self.capacity)
    for i in range(self.n-1, index-1,-1):
      self.A[i+1]=self.A[i]
    self.A[index]=val
    self.n+=1

  def delete(self):
    if self.n ==0:
      print("Array is empty deletion not Possible")
      return 
    self.A[self.n-1]=0
    self.n -=1

  #Remove(i) - O(n)
  def removeAt(self,index):
    if self.n==0:
      print("Array is empty deletion not Possible")
      return 
    if index < 0 or index >self.n:
      return IndexError("Index out of bound ... deletion not Possible")
    if index ==self.n-1:
      self.A[index]=0
      self.n-=1
      return 
    for i in range(index,self.n-1):
      self.A[i]=self.A[i+1]
    self.A[self.n-1]=0
    self.n-=1

  def _resize(self,new_cap):
    B=self.make_array(new_cap)
    for k in range(self.n):
      B[k] =self.A[k]
    self.A=B
    self.capacity=new_cap
  
  def make_array(self,new_cap):
    return (new_cap*ctypes.py_object)()
  
  def print_arr(self):
    arr=[]
    for i in range(self.n):
      arr.append(self.A[i])
    print(*arr)


import ctypes
arr=DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.print_arr()
print(arr.removeAt(2))
arr.print_arr()
arr.delete()
arr.print_arr()

def dynamicArray(n, queries):    
    seq = [[] for _ in range(n)]
    last_ans = 0
    res = []

    for q in queries:
        index = (q[1] ^ last_ans) % n
        
        if q[0] == 1:
            seq[index].append(q[2])
        else:
            position = q[2] % len(seq[index])
            last_ans = seq[index][position]
            res.append(last_ans)
    return res
a=2
b=[[1, 0 ,5],[1, 1, 7],[1, 0, 3],[2, 1, 0],[2, 1, 1]]
print(dynamicArray(a,b))


def rotateLeft(d, arr):
    n=len(arr)
    brr=[]
    for i in range(n):
        b= (i+d)%n
        print(b)
        brr.append(arr[b])
    return brr

