class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class AssignmentOne:
    #________________A_________________
    
    def __init__(self,data):
        self.head=None
        self.tail=None
        for value in data:
            newnode=Node(value)
            x=self.tail
            if self.head == None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
                
    #________________B_________________
    def LReverse(self):
        whole = None
        now = self.head 
        while now != None: 
            agla = now.next
            now.next = whole 
            whole = now 
            now = agla
        self.head = whole
        x=self.head
        while x:
            print(x.value,end=" ")
            x=x.next
            
    #________________C_________________
    def Reverse(self,str):
        stack=[0 for i in range(len(str))]
        tap=0
        for value in str:
            stack[tap]=value
            tap+=1
        new=""
        while tap>=0:
            tap-=1
            new+=stack[tap]
        return new
    
    #________________D_________________
    def Evaluate(self,postfix):
        stack=[0 for i in range(len(postfix))]
        tap=0
        for exp in postfix:
            if exp.isdigit():
                stack[tap]=exp
                tap+=1
            else:
                var1=stack[tap-1]
                var2=stack[tap-2]
                tap-=2
                stack[tap]=str(eval(var2+exp+var1))
                tap+=1
        tap-=1
        return stack[tap]
    
    #________________E_________________
    def drawRecursive(self):
        self.__drawRecursive(5)
        
    #_________________Wrapper Function for E_______________
    
    def __drawRecursive(self,n):
        if n>0:
            self.__drawRecursive(n-1)
            print("*"*n)
a=AssignmentOne(data=[1,2,3,4,5,6,7,8,9])
a.LReverse()
print("\n",a.Reverse("Hello World !"))
print(a.Evaluate("39-"))
a.drawRecursive()