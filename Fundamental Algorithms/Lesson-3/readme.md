# Lesson 3

- Bucketsort
- Growth of functions
- Mergesort
- Counting sort
- radix sort

### Bucketsort
Algorithm:
```
input array A[1..n] unsorted
assume 0 <= A[I] < 1 "Random"
output sorted array B[0..(n-1)] of linked lists
B is initially empty

for i=1 to n:
    place = floor(A[i] * n)
    insert A[i] in B[place]
for j=0 to n-1:
    sort B[j] by ANYSORT
```

### Growth of functions
See latex document

### Mergesort
Algorithm:
```
MERGE[A, p, q, r]
input A[p..r] sorted
      A[r-1..q] sorted
output A[p..q] sorted

create Aux
    L[1..r-p+2] with A[p..r] & "INFINITE"
    R[1..q-r+1] with A[r+1..q] & "INFINITE"
    Lpoint <- 1
    Rpoint <- 1
    for k=p to r:
        if L[Lpoint] <= R[Rpoint]:
            A[k] <- L[Lpoint]
            Lpoint++
        else:
            A[k] <- R[Rpoint]
            Rpoint++
```
and 
```
MERGESORT[A, p, r] (p<=r unsorted)
if p < r:
    q = floor((p+r)/2)
    MERGESORT[A, p, q]
    MERGESORT[A, q+1, r]
    MERGE[A, p, q, r]
```