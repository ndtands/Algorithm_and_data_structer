def computing(P):
    print(list(P))
    s= [0]*len(P)
    border = 0
    for i in range(1,len(P)):
        while (border >0) and P[i]!=P[border]:
            border = s[border-1]
        if P[i] == P[border]:
            border = border+1
        else:
            border = 0
        s[i] = border
    return s

print(computing("abcabcabca"))