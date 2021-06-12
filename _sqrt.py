'''Pesudocode:
 check num
 low,high = 1,num/2
 while low <= high:
    mid = (low+high)/2
    if mid*mid ==num:
        return mid
    elif mid*mid <num:
        low = mid+1
        ans = mid
    else:
        high = mid-1
inc = 0.1
for _ in range(n):
    while ans*ans <= num:
        ans+=inc
    ans-=inc
    inc=inc/10
return ans
'''
def sqrt(num,percent):
    if num<0:
        return False
    if num <=1:
        return num
    low =1
    high =num//2
    while low <=high:
        mid = low+(high-low)//2
        if mid*mid ==num:
            return mid
        elif mid*mid >num:
            high = mid-1
        else:
            low = mid +1
            ans = mid
    inc = 0.1
    for _ in range(percent):
        while ans*ans <= num:
            ans+=inc
        ans-= inc
        inc=inc/10
    print(ans)
sqrt(10,10)
