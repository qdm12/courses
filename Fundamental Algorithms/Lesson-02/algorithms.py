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
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1
        
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