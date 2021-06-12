def Fibonacci(n):
    f1,f2=0,1
    for i in range(n-1):
        f1,f2=f2,f1+f2
    return f2
import time
n=int(input())
start = time.time()
print(Fibonacci(n))
print("Time Excutive: ",time.time()-start)