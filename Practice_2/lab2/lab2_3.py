def Toi_Da_doanh_thu(a,b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    sum=0
    for i in range(len(a)):
        sum+=a[i]*b[i]
    return sum

while (True):
    try:
        print("Nhap so phan tu")
        n=int(input())
        break
    except:
        print("Error")
print("Nhap a: ")
a=[int(i) for i in input().split(" ")]
print("Nhap b: ")
b=[int(i) for i in input().split(" ")]
print("Doanh thu toi da la: ",Toi_Da_doanh_thu(a,b))