class QuickSort(object):
    def sort(self, A):
       self.quickSortHelper(A, 0, len(A)-1)

    def quickSortHelper(self, A, first, last):
       if first < last:
           splitpoint = self.partition(A, first, last)
           self.quickSortHelper(A, first, splitpoint-1)
           self.quickSortHelper(A, splitpoint+1, last)

    def partition(self, A, first, last):
        pivot = A[first]
        leftmark = first + 1
        rightmark = last
        while True:
            while A[leftmark] <= pivot and rightmark >= leftmark:
                leftmark += 1
            while A[rightmark] >= pivot and rightmark >= leftmark:
                rightmark -= 1
            if rightmark < leftmark:
                break # we are done
            A[leftmark], A[rightmark] = A[rightmark], A[leftmark]
        A[first], A[rightmark] = A[rightmark], A[first]
        return rightmark
        
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        self.sort(A)
        print A
        
class CountingSort(object):
    def sort(self, A, k=None):
        """
            Args:
                A (list): Unordered array
                k (int): Range of values = Number of buckets - 1
        """
        if k is None:
            k = max(A)
        n = len(A)
        B = [None for _ in range(n+1)] #n+1 so from 0 to n
        C = [0 for _ in range(k+1)] #counter
        for i in range(n):
            C[A[i]] += 1
        for s in range(1, k+1):
            C[s] += C[s-1]
        for j in range(n-1, -1, -1): #n to 0
            value = A[j]
            place = C[value]
            B[place] = value
            C[value] -= 1
        for i in range(n):
            A[i] = B[i+1] #we skip first one (Python thing)
        
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        self.sort(A)
        print A
        
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

qs = RadixSort()
qs.run()