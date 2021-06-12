"""
pesudocode:
b0<b1<b2<b3<...bn
Collect_sign(a,b):
    sort(b,a)
    count,end,arr = 0,0,[]
    for i from 0 to n-1:
        if a[i]>end:
            end =b[i]
            count +=1
            arr.add(end)
    return count,arr
"""
def Collect_sign(a,b):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            if (b[j]<b[i]):
                b[i],b[j]=b[j],b[i]
                a[i],a[j]=a[j],a[i]
    count =0
    end = 0 
    arr = []
    for i in range(n):
        if (a[i]>end):
            end = b[i]
            count +=1
            arr.append(end)
    print(count)
    print(*arr)

n = int(input("Nhap so phan tu: "))
A,B=[],[]
for _ in range(n):
    [a,b]=[int(i) for i in input("Nhap ai , bi : ").split(" ")]
    A.append(a)
    B.append(b)
Collect_sign(A,B)