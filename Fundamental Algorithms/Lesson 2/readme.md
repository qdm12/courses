# Fundamental algorithms course, Spring 2017

## Lesson 2: Quicksort, countingsort, radix sort

### Quicksort

### Countingsort
Algorithm
```
input A[1..n] all 0 <= A[i] <= k
if k = O(n):
    input A[1..n]
    output B[1..n]
    auxiliary C[0..k]
    initialize C[i] <- 0 <= i <= k
    for i=1 to n:
        C[A[i]]++
    for s=1 to k:
        C[s] += C[s-1]
    for j=n to 1:
        value <- A[j]
        place <- C[value]
        B[place] <- value
        C[value]--
```
This takes time O(MAX(n,k))

### Radixsort
Algorithm
```
input A[1..n] all 0 <= A[i] < k^D integers written in base K with D digits
for j=D to 1:
    apply countingsort to jth digit
```
This takes time O(MAX(n,k))