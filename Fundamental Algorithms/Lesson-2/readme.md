# Lesson 2

- Quicksort
- Countingsort
- Radixsort

### Quicksort
It takes time O(n^2) at worst, and O(n log(n)) at average and best.

```python
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
```

### Countingsort
It takes time O(n+k)

Algorithm
```
input A[1..n] with all 0 <= A[i] <= k
output B[1..n]
auxiliary C[0..k]
initialize C[i] <- 0 <= i <= k
for i = 1 to n:
    C[A[i]]++
for s=1 to k:
    C[s] += C[s-1]
for j=n to 1:
    value <- A[j]
    place <- C[value]
    B[place] <- value
    C[value]--
```

In Python:
```python
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
```

### Radixsort
It takes time O(nk) where k is the base with D digits (0 <= A[i] < k^D)

Algorithm
```
input A[1..n] all 0 <= A[i] < k^D integers written in base K with D digits
for j=D to 1:
    apply countingsort to jth digit
```

In Python:
```python
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
```