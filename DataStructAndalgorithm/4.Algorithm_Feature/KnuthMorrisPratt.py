def computing(P):
    s= [0]*len(P)
    bdorder = 0
    for i in range(1,len(P)):
        while (border >0) and P[i]!=P[border]:
            border = s[border-1]
        if P[i] == P[border]:
            border = border+1
        else:
            border = 0
        s[i] = border
    return s
def KMP(P,T):
    S = P+'$'+T
    pre = computing(S)
    kq =[]
    for i in range(len(P)+1,len(S)):
        if pre[i] == len(P):
            kq.append(i-2*len(P))
    if kq == []:
        print("NULL")
    print(*kq)
KMP('ATAT','GATATATGCATATACTT')