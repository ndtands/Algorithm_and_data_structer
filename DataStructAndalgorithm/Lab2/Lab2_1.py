import time
def Doi_tien(n):
  Xu=[1,5,10]
  Xu.sort(reverse=True)
  A  =[0]*len(Xu)
  index=0
  while (index<len(Xu)):
    if n==0:
        return sum(A)
    if (n>Xu[index]):
      n-=Xu[index]
      A[index]+=1
    else:
      index+=1
  return sum(A)
n=int(input())
start =time.time()
print(Doi_tien(n))
print("Time Excutive: ",time.time()-start)