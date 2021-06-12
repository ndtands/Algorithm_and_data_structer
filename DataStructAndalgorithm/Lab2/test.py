a=[1,2,2,4,6]
b=[9,6,5,7,8]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(b[i]>b[j]):
            a[i],a[j]=a[j],a[i]
            b[i],b[j]=b[j],b[i]
        if(b[i]==b[j] and a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
            b[i],b[j]=b[j],b[i]
print(a)
print(b)
index =0
count=1
for i in range(1,len(a)):
    print(index)
    if(a[i]<=b[index]):
        pass
    else:
        index =i
        count+=1
print(count)