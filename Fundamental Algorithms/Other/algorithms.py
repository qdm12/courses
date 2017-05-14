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
        
class QuickSort(object):
    def sort(self, A):
        self.quickSortHelper(A, 0, len(A)-1)

    def quickSortHelper(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.quickSortHelper(A, p, q-1)
            self.quickSortHelper(A, q+1, r)

    def partition(self, A, p, r):
        pivot = A[r]
        i = p - 1
        for j in range(p, r+1):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        return i
        
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        self.sort(A)
        print A
        
class CountingSort(object):
    def sort(self, A, B, k=None):
        """
            Args:
                A (list): Unordered array
                B (list): Output sorted array
                k (int): Range of values = Number of buckets - 1
        """
        if k is None:
            k = max(A)
        n = len(A)
        C = [0 for _ in range(k+1)] #counter, k is the range of values
        for i in range(n):
            C[A[i]] += 1
        # C[i] contains the number of elements = i
        for i in range(1, k+1):
            C[i] += C[i-1] 
        # C[i] contains the number of elements <= i
        for i in range(n-1, -1, -1): #n to 0
            place = C[A[i]]
            B[place - 1] = A[i] # -1 for Python
            C[A[i]] -= 1
        
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        B = [None] * len(A)
        self.sort(A, B, max(A))
        print B
        
class RadixSort(object):
    def sort(self, A, RADIX=10):
        placement = 1
        tmp = A[0]
        while tmp > 0:
            buckets = [[] for _ in range(RADIX)]
            for i in range(len(A)):
                tmp = A[i] / placement
                buckets[tmp % RADIX].append(A[i])
            i = 0
            for bucket in buckets:
                for x in bucket:
                    A[i] = x
                    i += 1
            placement *= RADIX # move to next digit
        
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        self.sort(A)
        print A
        
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
            q = int(floor((l+r)/2))
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