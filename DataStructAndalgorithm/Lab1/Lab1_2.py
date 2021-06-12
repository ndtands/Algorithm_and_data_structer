import time
def fib_last_digit(n):
    f1,f2=0,1
    for i in range(n-1):
        f1,f2=f2,f1+f2
    return f2%10
n = int(input())
start = time.time()
print(fib_last_digit(n))
print("Time implement: ",time.time()-start)