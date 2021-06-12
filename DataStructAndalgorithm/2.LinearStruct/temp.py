#python3
n = 1000
def isPrime(t):
     if t < 2: return False
     for i in range(2, int(t**(1/2))+1):
          if t % i == 0: return False
     return True

a = []
for i in range(10):
     if isPrime(i):
          a.append(i)
print(a)
for j in a:
     for k in range(10):
          if isPrime(j*10 + k) and (j*10 + k) < n:
                print(j,k)
                a.append(j*10 + k)
print(*a)