
def Toi_Da_Chien_loi_pham(W,values,weights):
    valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    A = [0]*len(weights) # 
    V = 0
    for i in range(len(valuePerWeight)):
        if W ==0 : 
            return round(V,4)
        a = min(valuePerWeight[i][1],W) #select number of item
        V = V+a*valuePerWeight[i][0]    #increate value
        valuePerWeight[i][1]=valuePerWeight[i][1]-a #decreate weights
        A[i] = A[i]+a   #increate count of item
        W = W-a #decreate MaxWeights
    return round(V,4)   
print("Nhap so vat phan va suc chua: ")
[n,W] =[int(i) for i in input().split(" ")]
value,weight=[],[]
for _ in range(n):
    print("Nhap v va w: ")
    [w,v]=[int(i) for i in input().split(" ")]
    value.append(v)
    weight.append(w)
print("Chien loi pham toi da: %0.4f"%Toi_Da_Chien_loi_pham(W,weight,value))