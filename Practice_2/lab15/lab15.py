"""
ComputePreficFunction(P):
    s <- []*len(P)
    s[0] <- 0
    border <- 0
    for i from 0 to len(P)-2:
        #
        while(border>0) and (P[i] khac P[border]):
            border <- s[border-1]
        if P[i] == P[border]:
            border <- border +1
        else:
            border <- 0
        s[i] <- border
    return s
"""
#Lưu vào mảng chứa vị trí tương ứng đoạn border dài nhất có thể có
def ComputePrifix(P):
    s = [0]*len(P)
    border = 0
    for i in range(1,len(P)):
        while border >0 and P[i] != P[border]:
            #Check with pre border
            border = s[border-1]
        if P[i] == P[border]:
            border = border +1
        else:
            border = 0
        s[i] = border
    return s

'''
KMP:
    S <- P+'"'+T
    s <- computePrefixFunction(S) 
    result <- []
    for i in from |P|-1 to |S|-1:
        if s[i] == |P|
            append(i-2|P|)
    return result     
O(|P|+|T|)      
'''

def KMP(P,T):
    S = P+'$'+T
    pre = ComputePrifix(S)
    print(pre)
    kq =[]
    for i in range(len(P)+1,len(S)):
        if pre[i] == len(P):
            kq.append(i-2*len(P))
    if kq == []:
        print("NULL")
    print(*kq)
KMP('ATAT','GATATATGCATATACTT')

"""
def questionCorrection(s):
    s = s.lower()
    # Thay tat ca cac ky tu khong phai a-z, 0-9, white space, dau ',' bang ky tu " "
    s = re.sub("[^a-z0-9\\s,]", " ", s)
    # Xoa tat ca cac ky tu khong phai a-z, 0-9 dung truoc dau ','
    s = re.sub("[^a-z0-9]+,",",",s)
    # Thay tat ca ',' thanh ',' + ' '
    s = re.sub(",",", ",s)
    # Thay cac white space thanh " "
    s = re.sub("[\\s]+"," ",s)
    # Xoa cac ky tu khong phai la white space + , hoac ,+
    s = re.sub("^[\\s,]+","",s)
    # Xoa white space, ',' o cuoi dong
    s = re.sub("[\\s,]+$", "",s)
    # Viet hoa chu cai dau tien
    s = s.capitalize()
    # Them ? vao cuoi cau
    s = s + "?"
    
    return s
"""