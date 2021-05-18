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