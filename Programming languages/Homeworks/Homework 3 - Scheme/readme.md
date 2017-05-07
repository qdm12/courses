# Programming languages, Spring 2017

## Scheme programming assignment

### What is it?
It is a serie of small functions written in Scheme.

### Setup and run
1. Install [Racket](https://download.racket-lang.org/) for Scheme.
2. Copy the whole code and paste it into Racket.
3. You can then run these functions in the interpreter.

### Assignment description
Write the following functions:

1. `(find-min L)`, where `L` is a list of numbers, and returns the minimum element of `L`. 
Assume `L` is never empty. You need to have at most one recursive call to `find-min` in
your body. For example:
```scheme
> (find-min '(3 2 7 6 9 10))
2
```

2. `(find-min-rest L)`, where `L` is a list of numbers, and returns a list of:
  - The minimum element of L
  - A list of all the elements of L except its minimum previously found
For example:
```scheme
>> (find-min-rest '(3 2 7 2 9 10))
(2 (3 2 7 9 10))
```
Do not use `find-min` and only stick to `find-min-rest` (itself) and the built-in 
functions `null?`, `car`, `cdr`, `cadr`, and `list`. Assume `L` is never empty.
You might use a form of `let` to save the result of calling `find-min-rest` recursively.

3. `(sort L)`, where `L` is a list of numbers, and uses a selection sort to return a list 
containing the elements of L sorted in increasing order. You should use `find-min-rest`.
For example:
```scheme
> (sort '(3 4 1 2 6 9))
(1 2 3 4 6 9)
```

4. `(sum-list L)`, where L is a list containing numbers and nested lists of numbers, 
which adds up all the numbers in L at any depth of nesting. For example:
```scheme
> (sum-list '(8 3 (4 8) (1 (4 8)) 9))
45
```

5. `(map2 f L1 L2)`, where `f` is a function of two parameters and `L1` and `L2` are lists. 
`map2` should apply `f` to the corresponding elements of `L1` and `L2`, and return a list of
the results. For example:
```scheme
> (map2 (lambda (x y) (+ x y)) '(2 3 4 5 6) '(30 40 50 60 70))
(32 43 54 65 76)
```
Assume `L1` and `L2` are the same length. Do not use the built-in `map` function.

6. `(nums-from n m)`, where `n` and `m` are integers, and returns the list of all
integers from `n` to `m`, inclusive. For example:
```scheme
> (nums-from 7 12)
(7 8 9 10 11 12)
```

7. `(remove-mults n L)`, where `n` is an integer and `L` is a list of integers, and
returns the list of all elements of `L` that are not a multiple of `n`. For example:
```scheme
> (remove-mults 2 '(1 2 3 4 5 6 7 8 9))
(1 3 5 7 9)
> (remove-mults 3 '(1 2 3 4 5 6 7 8 9))
(1 2 4 5 7 8)
```
You might use the built-in `(modulo x y)`.

8. `(sieve L)`, where `L` is a list of integers, and returns the list of elements
of `L` that are not multiples of each other. For example:
```scheme
> (sieve '(4 5 6 7 8 9 10 11 12 13 14 15 16 17))
(4 5 6 7 9 11 13 17)
```
Assume that the elements of L are sorted in increasing order.
`sieve` should call `remove-mults`. 

9. `(primes n)`, where `n` is an integer, and returns the list of all the prime
numbers less than or equal to `n`. For example:
```scheme
(primes 20)
(2 3 5 7 11 13 17 19)
```
`primes` should not be recursive and should call sieve and nums-from.

10. `(gen-fn-list n)` which returns a list of `n` functions, such that the first
function in the list takes a parameter `x` and returns `x+1`, the second function 
takes a parameter `x` and returns `x+2`, etc. For example:
```scheme
> (define fs (gen-fn-list 3))
> ((car fs) 10)
11
> ((cadr fs) 10)
12
> (map (lambda (f) (f 10)) (gen-fn-list 6))
(11 12 13 14 15 16)
```