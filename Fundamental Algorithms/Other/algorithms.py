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
    def merge(self, L, R):
        C = []
        i, j = 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                C.append(L[i])
                i += 1
            else:
                C.append(R[j])
                j += 1
        while i < len(L):
            C.append(L[i])
            i += 1
        while j < len(R):
            C.append(R[j])
            j += 1
        return C

    def mergeSort(self, A):
        if len(A) < 2:
            return A
        else:
            middle = len(A) / 2
            L = self.mergeSort(A[:middle])
            R = self.mergeSort(A[middle:])
            return self.merge(L, R)
            
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        print self.mergeSort(A)
        
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
        
        
        
        
        
        
        
        
        
        