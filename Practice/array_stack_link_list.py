class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in range(size)]
        self.top=0
        self.head=None
        self.tail=None
    def isEmpty(self):
        if self.top==0:
            return True
        else:
            return False
    def Push(self,value):
        if self.top==self.size:
            print("Stack Overflow !")
        else:
            newnode=Node(value)
            self.data[self.top]=newnode
            self.top+=1
            x=self.tail
            if self.head == None:
                self.head=newnode
                self.tail=newnode
            self.tail.next=newnode
            self.tail=newnode
    def Pop (self):
        if self.isEmpty():
            print("Stack Underflow !")
        else:
            p=self.head
            q=p.next
            while q.next != None:
                p=p.next
                q=q.next
            p.next=None
            x=self.data[self.top-1]
            self.top-=1
            self.data[self.top]=0
            return q.value
    def Check(self):
        if self.isempty:
            True
        else:
            False
    def Peek(self):
        x=self.head
        while x.next != None:
            x=x.next
        return x.value
    def Count(self):
        return self.top
    def Print(self):
        x=self.head
        while(x):
            print(x.value,end=" ")
            x=x.next
ob=ArrayStack(3)
ob.Push(7)
ob.Push(6)
ob.Push(5)
print(ob.Pop())
print(ob.Peek())
print(ob.Count())
ob.Print()