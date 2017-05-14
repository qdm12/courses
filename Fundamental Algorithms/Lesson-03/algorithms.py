from operator import itemgetter
from math import floor
             
def radix_sort_alpha(words):
    l = len(words[0])
    for w in words:
        if len(w) != l:
            raise Exception("All words should be of same length")
    for i in range(l, 0, -1):
        words = sorted(words, key=itemgetter(i - 1))
        words_str = str([''.join(w) for w in words])
        print "PASS "+str(l - i + 1)+": "+words_str
    return words_str
                
def bucket_sort(A):
    print "Initial input array A: "+str(A)
    n = len(A)
    for i in range(n):
        assert(A[i] >= 0 and A[i] < 1)
    B = [[] for _ in range(n)]
    print "Initial output buckets array B: "+str(B)
    for i in range(n):
        place = int(floor(A[i] * n))
        B[place].append(A[i])
    print "Output buckets array B with elements in buckets: "+str(B)
    for j in range(n):
        B[j].sort()
    print "Output buckets array B with elements sorted in buckets: "+str(B)
    B_final = []
    for bucket in B:
        B_final += bucket
    print "Final output array B: "+str(B_final)
    return B_final
    
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

        
if __name__ == "__main__":
    radix_sort_alpha(["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"])
    bucket_sort([.79,.13,.16,.64,.39,.20,.89,.53,.71,.43])
    m = MergeSort()
    m.run()