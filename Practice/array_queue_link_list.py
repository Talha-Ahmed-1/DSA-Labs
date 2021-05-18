class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class ArrayQueue:
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in range(size)]
        self.f=-1
        self.r=0
        self.head=None
        self.tail=None
        self.a=None
    def enQueue(self,value):
        self.data[self.r]=value
        self.r=(self.r+1)%self.size
        newnode=Node(value)
        if self.head == None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.a=self.head
    def deQueue(self):
        self.f=(self.f+1)%self.size
        x=self.data[self.f]
        self.data[self.f]=0
        position=x
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
        self.a=self.head
        return x
    def isEmpty(self):
        if self.f==-1 and self.r==0:
            return True
        else:
            return False
    def Count(self):
        return len(self.data)
    def Print(self):
        print(self.Count())
ob=ArrayQueue(5)
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)
ob.enQueue(4)
ob.enQueue(5)
print(ob.deQueue())
ob.enQueue(6)
print(ob.data)
ob.Print()
print(ob.isEmpty())