from math import floor

class BinarySearch:
    def binarySearch(self, array, key):
        if not array:
            return -1
        mid = len(array) / 2
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            return self.binarySearch(array[:mid], key)
        else:
            return self.binarySearch(array[mid+1:], key)
        
    def run(self):
        array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        print self.binarySearch(array, 13)
        
class MergeSort(object):
    def merge(self, A, l, q, r):
        n1 = q - l + 1
        n2 = r - q
        L = [A[l + i] for i in range(n1)]
        R = [A[q + 1 + i] for i in range(n2)]
        i = j = 0 # Initial index of first and second subarrays
        k = l # Initial index of merged subarray
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        # Copy the remaining elements of L[], if there are any
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1
        # Copy the remaining elements of R[], if there are any
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, A, l, r):
        if l < r:
            q = (l+r)/2 # this does the floor
            self.mergeSort(A, l, q)
            self.mergeSort(A, q+1, r)
            self.merge(A, l, q, r)
            
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        self.mergeSort(A, 0, len(A) - 1)
        print A
        
class BucketSort:
    def bucketSort_percent(self, A):
        n = len(A)
        for i in range(n):
            assert(A[i] >= 0 and A[i] < 1)
        B = [[] for _ in range(n)]
        # Stores elements in buckets
        for i in range(n):
            place = int(floor(A[i] * n))
            B[place].append(A[i])
        # Sorts buckets
        for i in range(n):
            B[i].sort()
        # Concatenates
        B_final = []
        for bucket in B:
            B_final += bucket
        return B_final
    
    def bucketSort(self, A):
        maximum, sqrt_size = max(A), int((len(A)**0.5))
        buckets = [[] for _ in range(maximum)]
        for a in A:
            i = int(a / maximum * (sqrt_size - 1)) #hashing
            buckets[i].append(a) 
        for bucket in buckets:
            bucket.sort() #insertion sort        
        i = 0
        for bucket in buckets:
            for a in bucket:
                A[i] = a
                i += 1

    def run(self):
        A = [1, 2, 3.5, 6, 3.4, 2]
        self.bucket_sort(A)
        print A
        
        
        
m = MergeSort()
m.run()
        
        
        
        
        
        