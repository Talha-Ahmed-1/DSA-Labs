#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1
def Write(n):
    if n>0:
        print(n)
        Write(n-1)
Write(5)


# In[71]:


# 2
def Factorial(n):
    if n>0:
        if n==1:
            print(n,end="=")
        if n!=1:
            print(n,end="x")
        n*=Factorial(n-1)
        return n
    else:
        return 1
n=5
print(str(n),end="!=")
print(Factorial(n))


# In[86]:


# 3
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
GCD(8,12)


# In[85]:


# 4
def BinSearch(a,lb,ub,x):
    mid=(lb+ub)//2
    if x==a[mid]:
        return mid+1
    elif x<a[mid]:
        return BinSearch(a,lb,mid-1,x)
    elif x>ub:
        return "Item not Found !"
    else:
        return BinSearch(a,mid+1,ub,x)
BinSearch([1,2,3,4,5,6,7,8],1,8,10)


# In[97]:


# 5
def QuickSort(a,p,r):
    if p<r:
        q=Partition(a,p,r)
        QuickSort(a,p,q-1)
        QuickSort(a,q+1,r)
def Partition(a,low,high):
    x=a[high]
    i=low-1
    for j in range(low,high):
        if a[j]<=x:
            i=i+1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
arr=[20,50,100,75,99]
QuickSort(arr,0,len(arr)-1)
print(arr)

