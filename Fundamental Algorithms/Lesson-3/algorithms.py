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

        
if __name__ == "__main__":
    #radix_sort_alpha(["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"])
    bucket_sort([.79,.13,.16,.64,.39,.20,.89,.53,.71,.43])