#Rabin-Karp

import random

class RabinKarp:
    def __init__(self,pattern,string):
        self.string  = string
        self.pattern = pattern
        self.p       = int(1e9)+7
        self.x       = random.randint(1,self.p-1)
        self.result  = []
    
    def AreEqual(self,start):
        return self.string[start:start+len(self.pattern)] ==self.pattern
    
    def polyHash(self,S):
        _hash=0
        for char in reversed(S):
            _hash =(_hash*self.x+ord(char))%self.p
        return _hash

    def PrecomputeHashes(self,lenP):
        lenT = len(self.string)
        H    = [0]*(lenT-lenP+1)
        S    = self.string[lenT-lenP:]
        H[lenT - lenP] = self.polyHash(S)
        y    = 1
        for _ in range(1,lenP+1):
            y=(y*self.x)%self.p
        for i in range(lenT-lenP-1,-1,-1):
            H[i]= ((self.x * H[i + 1] + ord(self.string[i]) - y * ord(self.string[i + lenP])) % self.p + self.p) % self.p
        return H
        
    def mainAlgorithm(self):
        result = []
        pHash  = self.polyHash(self.pattern)
        H      = self.PrecomputeHashes(len(self.pattern))
        for i in range(0,len(self.string)-len(self.pattern)+1):
            if pHash != H[i]:
                continue
            if self.AreEqual(i):
                result.append(i)
        print (*result)

#string = input("Input of String: ")
#pattern = input("Input of Pattetn: ")
#Lab = RabinKarp(string,pattern)
Lab = RabinKarp("aaaaa","baaaaaaa")
Lab.mainAlgorithm()


#Knuth-Morris-Pratt
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
    S=P+'@'+T
    pre = ComputePrefix(S)
    kq=[]
    for i in range(len(P)+1,len(S)):
        if pre[i]==len(P):
            kq.append(i-2*len(P))
    return kq

def CoputePrefix(P):
    s=[0]*len(P)
    border=0
    for i in range(1,len(P)):
        while border >0 and P[i] !=P[border]:
            border=s[border-1]

        if P[i]==P[border]:
            border+=1

        else:
            border=0
        s[i] = border
    return s 
print(CoputePrefix('abcabcb'))