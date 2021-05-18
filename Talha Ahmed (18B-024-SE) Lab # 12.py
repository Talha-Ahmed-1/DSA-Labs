class StringOP:
    def __init__(self,data):
        self.data=data
    def StrLength(self,string):
        count=0
        for i in string:
            count+=1
        return count
    def StrConcat(self,string1,string2):
        return string1+string2
    def SubString(self,text,start,end):
        count=""
        for i in range(self.StrLength(text)):
            if i >= start-1:
                if i == end:
                    break
                count+=text[i]
        return count
    def InsertStr(self,text,pos):
        count=""
        for i in range(self.StrLength(self.data)):
            if i == pos-1:
                count+=text
            count+=self.data[i]
        return count
    def DeleteStr(self,pos,length):
        count=""
        for i in range(self.StrLength(self.data)):
            if i >= pos and i !=pos+length:
                None
            else:
                count+=self.data[i]
        return count
    def Naive(self,pattern):
        n=self.StrLength(self.data)
        m=self.StrLength(pattern)
        lst=[]
        for s in range(0,(n-m)+1):
            for i in range(m):
                if pattern[i]!=self.data[s+i]:
                    break
                if i == m-1:
                    lst.append(s+1)
        return lst
    def RabinKarp(self,pat,q): 
        txt=self.data
        lst=[]
        M = len(pat) 
        N = len(txt) 
        i = 0
        j = 0
        p = 0 
        t = 0 
        h = 1
        d=256
        for i in range(M-1): 
            h = (h*d)%q 
        for i in range(M): 
            p = (d*p + ord(pat[i]))%q 
            t = (d*t + ord(txt[i]))%q 
        for i in range(N-M+1):  
            if p==t: 
                for j in range(M): 
                    if txt[i+j] != pat[j]: 
                        break
                j+=1
                if j==M: 
                    lst.append(i)
                else:
                    lst.append(i)
            if i < N-M: 
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 
                if t < 0: 
                    t = t+q
        return lst
a=StringOP("talha Ahmed is hello is hello also")
print(a.StrLength("talha"))
print(a.SubString("talha Ahmed is also",7,11))
print(a.InsertStr("hellooooooooo ",1))
print(a.DeleteStr(2,2))
print(a.Naive("a"))
print(a.RabinKarp("hello",101))