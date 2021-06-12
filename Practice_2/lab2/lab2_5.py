"""
pseudocode:
Lab2.5(n):
    index <- 1
    arr = []
    while n!= 0:
        if n - index >= index or n - index == 0:
            arr.add(index)
            n <- n - index
        index <- index + 1
    reutrn len(arr)
"""
def Toi_da_giai_thuong(n):
    index=1
    arr=[]
    while n!=0:
        if n-index >= index+1 or n-index ==0:
            arr.append(index)
            n-=index
        index +=1
    print(len(arr))
    print(*arr)


n=int(input("Nhap n: "))
Toi_da_giai_thuong(n)