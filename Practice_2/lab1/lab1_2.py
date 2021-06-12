import time
def fib_last_digit_v1(n):
    f1,f2=0,1
    for i in range(n-1):
        f1,f2=f2,f1+f2
    return f2%10
'''n = int(input())
start = time.time()
print(fib_last_digit_v1(n))
print("Time implement: ",time.time()-start)'''

import time
def fib_last_digit_v2(n):
    if n < 2: return n
    else:
        f1, f2 = 0, 1
        for i in range(1,n):
            f1, f2 = f2, (f1+f2) % 10
        return f2
'''n = int(input())
start = time.time()
print(fib_last_digit_v2(n))
print("Time implement: ",time.time()-start)'''


import time
def fib_last_digit_v3(n):
    return (
        [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
        [n % 60 - 1]
    )
n = int(input())
start = time.time()
print(fib_last_digit_v3(n))
print("Time implement: ",time.time()-start)