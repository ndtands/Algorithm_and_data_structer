def fib(n):
    if n<=0:
        return False
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(20))

def fib(n):
    f0,f1=0,1
    for _ in range(n-1):
        f1,f0=f1+f0,f1
    return f1
print(fib(20))

def fib(n):
    memory = [0]*(n+1)
    memory[1]=1
    for i in range(2,n+1):
        memory[i]=memory[i-1]+memory[i-2]
    return memory[n]
print(fib(20))

def fib(n):
    a=(1+5**(1/2))/2
    b=(1-5**(1/5))/2
    c=1/(5**(1/2))
    return int(c*(a**n-b**n))
print(fib(20))


def isPrime(n):
    return all(list(n%i!=0 for i in range(2,n)) if n>1 else False)

print(isPrime(5))