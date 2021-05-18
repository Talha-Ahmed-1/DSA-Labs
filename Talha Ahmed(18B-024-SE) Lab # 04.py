import random
class Sorting:
    def __init__(self):
        self.data=[]
    def Print(self):
        print(self.data)
    def GenerateRandom(self,n):
        for i in range(n):
            x=random.randint(1,n)
            self.data.append(x)
    def BubbleSort(self):
        n=len(self.data)
        for i in range(1,n-1):
            for j in range(n-i):
                if self.data[j] > self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
        print(self.data)
    def InsertionSort(self):
        for i in range(len(self.data)):
            key=self.data[i]
            j=i-1
            while j>=0 and self.data[j]>key:
                self.data[j+1]=self.data[j]
                j=j-1
            self.data[j+1]=key
    def SelectionSort(self):
        n=len(self.data)
        for i in range(n):
            min = i
            for j in range(i+1,n):
                if self.data[j]<self.data[min] :
                    min = j
            if min != i:
                self.data[min],self.data[i]=self.data[i],self.data[min]
        print(data)
    def Search(self,x):
        i=1
        while i <= len(self.data) and x != self.data[i]:
            i += 1
        if i <= len(self.data):
            location=(self.data.index(i))+2
        else:
            location=0
        print("Position of",x,"is",location)
a=Sorting()
a.Print()
a.GenerateRandom(6)
a.Print()
a.BubbleSort()
b=Sorting()
b.GenerateRandom(6)
b.Print()
b.InsertionSort()
b.Print()
c=Sorting()
c.GenerateRandom(6)
c.Print()
c.InsertionSort()
c.Print()
c.Search(3)