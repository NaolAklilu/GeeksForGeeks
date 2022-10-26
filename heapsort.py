class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = (2*i) + 2
        
        while (left <= n-1 and arr[left] > arr[largest]):
            largest = left
            
        while (right <= n-1 and arr[right] > arr[largest]):
            largest = right
            
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        firstparent = (n-2) // 2
        for i in reversed(range(firstparent+1)):
            self.heapify(arr, n, i)
            
        return arr
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        arr = self.buildHeap(arr, n)
        for i in reversed(range(n)):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
