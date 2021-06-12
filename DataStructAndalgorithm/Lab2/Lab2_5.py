def Toi_da_giai_thuong(n):
    index=1
    arr=[]
    while(n!=0):
        if(n-index>index+1 or n-index==0):
            arr.append(index)
            n-=index
            index+=1
            
        else:
            index+=1
    return len(arr),arr
print("Nhap n: ")
n=int(input())
print(Toi_da_giai_thuong(n))
# Dat cau hoi lab2_4 va lab2_5