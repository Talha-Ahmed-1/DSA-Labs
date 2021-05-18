# A
class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in range(size)]
        self.top=0
    def isEmpty(self):
        if self.top==0:
            return True
        else:
            return False
    def Push(self,value):
        if self.top==self.size:
            print("Stack Overflow !")
        else:
            self.data[self.top]=value
            self.top+=1
    def Pop (self):
        if self.isEmpty():
            print("Stack Underflow !")
        else:
            x=self.data[self.top-1]
            self.top-=1
            self.data[self.top]=0
            return x
    def Check(self):
        if self.isEmpty:
            True
        else:
            False
    def Peek(self):
        return self.data[self.top-1]
    def Count(self):
        return self.top
    def Printt(self):
        for i in self.data:
            print(i)
ob=ArrayStack(3)
ob.Push(7)
ob.Push(6)
ob.Push(5)
ob.Push(77)
#ob.Pop()
print(ob.Peek())
print(ob.Count())
ob.Printt()



# B
class ArrayQueue:
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in range(size)]
        self.f=-1
        self.r=0
    def enQueue(self,value):
        self.data[self.r]=value
        self.r=(self.r+1)%self.size
    def deQueue(self):
        self.f=(self.f+1)%self.size
        return self.data[self.f]
    def isEmpty(self):
        if self.f==-1 and self.r==0:
            return True
        else:
            False
    def Count(self):
        return len(self.data)
    def Printt(self):
        print(self.Count())
ob=ArrayQueue(4)
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)
ob.enQueue(4)
ob.enQueue(5)
print(ob.deQueue())
ob.Printt()





# A
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtFirst(self,value):
        newnode=Node(value)
        if self.head == None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertAtEnd(self,value):
        newnode=Node(value)
        x=self.tail
        if self.head == None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def insertAtAfter(self,position,value):
        newnode=Node(value)
        if self.tail == None:
            self.head=newnode
            self.tail=newnode
        else:
            temp=self.head
            while temp.value != position:
                temp=temp.next
            a=temp.next
            temp.next=newnode
            newnode.next=a
    def deleteAtFirst(self):
        x=self.head
        x=x.next
        self.head=x
    def deleteAtEnd(self):
        p=self.head
        q=p.next
        while q.next != None:
            p=p.next
            q=q.next
        p.next=None
    def deleteAtAfter(self,position):
        if self.tail == None:
            pass
        elif self.head.value==position:
            self.deleteAtFirst()
        else:
            p=self.head
            q=p.next
            while q.value != position:
                p=p.next
                q=q.next
            p.next=q.next            
    def Print(self):
        x=self.head
        while(x):
            print(x.value,end=" ")
            x=x.next
a=LinkedList()
a.insertAtFirst(5)
a.insertAtFirst(7)
a.insertAtEnd(2)
a.insertAtEnd(3)
a.deleteAtFirst()
a.deleteAtEnd()
a.insertAtAfter(5,8)
a.insertAtAfter(5,9)
a.deleteAtAfter(9)
a.insertAtAfter(2,4)
a.Print()