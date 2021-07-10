def Insert_MaxHeap(heap, elem):    # Insert new node
    heap.append(elem)  # Insert elemeent to the heap
    n = len(heap)    # Finding the length of the heap
    Heap_Increase_Key(heap,n,n-1)    # Heapify after insertion
    
def Extract_Heap_Max(heap):     # Remove any node
    n = len(heap)-1    # Finding the index of last element of heap
    heap[0] = heap[n]  # replacing the last with first
    Build_Max_Heap(heap,n,0)   # Heapify after removing node

def Build_Max_Heap(heap, n, i):    # Build heap when max node removed
    long = i     # index of root first after than it is incrementing
    l = 2 * i    # index of left one
    r = 2 * i + 1   # index of right one
    if l < n and heap[i] < heap[l]:  # if left one is less than root
        long = l    # replace long with the left one's index
    if r < n and heap[long] < heap[r]: # if right one is less than root
        long = r    # replace long with the right one's index
    if long != i:
        heap[i], heap[long] = heap[long], heap[i]   # swapping
        Build_Max_Heap(heap, n, long)  # heapify
        
def Max_Heapify(heap):      # Sorting
    n = len(heap)    # Finding the length of the heap
    for i in range(n,-1,-1):    # traversing heap from bottom to up
        Build_Max_Heap(heap,n,i)  # Heapify
    for j in range(n-1,0,-1):# traversing heap from bottom to up again
        heap[j],heap[0] = heap[0],heap[j]   # swapping
        Build_Max_Heap(heap,j,0)    # heapify
        
def Heap_Increase_Key(heap,n,_n):     # Increase to value stored at any node
    pat = (_n-1)//2     # Finding the parent index
    if heap[pat] > 0:   # if parent index in non zero and non negative
        if heap[_n] > heap[pat]:    # if previous element is greater than parent
            heap[_n], heap[pat] = heap[pat], heap[_n]    # swapping the elements
            Heap_Increase_Key(heap,n,pat)     #Heapify after insertion again


if __name__ == "__main__":
    heap = [25,16,14,13,10,8,12]
    print(f"Initializing Heap {heap}")
    Max_Heapify(heap)
    print(f"Max Heapify {heap}")
    key = 25
    Insert_MaxHeap(heap, key)
    print(f"Insert  Max Heap key = {key}\nAfter insertion Heap = {heap}")
    Extract_Heap_Max(heap)