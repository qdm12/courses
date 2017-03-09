# Programming language course, Spring 2017

## Lesson 7: More Scheme

- Access elements of a list
```scheme
(car '(1 2 3 4))
```
- Get the second element
```scheme
(car (cdr '(1 2 3 4)))
```
- Get the third element
```scheme
(car (cdr (cdr '(1 2 3 4))))
```
- This returns 2
```scheme
(cadar '((1 2 3 4) (5 6 7) (8 9 10)))
```
- Let's introduce a new scope and defines varaibles in that scope
```scheme
(define (f x)
    (let ((y (+ x 1)) (x (* x 2)))
        (+ y z)))
(f 4)
y ; y is undefined
```
Because the new variables introduced by a LET are only
visible in the BODY of the let, a new variable cannot be
used in the definition of a subsequent new variable
```scheme
(let ((x 3) (y (+ x 1)))
    (+ x y)
```



- *MISSING*


- Or you can use **LET\*\** which has the same effect as nesting a series of **LET**s
```scheme
(let* ((x 3) (y (+ x 1)) (z (* y 2)))
    (+ x y z)
```


Functions are *first class* objects, meaning they can be treated as values:
passed as parameters, returned as the results of function calls, placed into lists etc.

A simple *higher order* function, i.e *a function operating over functions*
```scheme
(define (foo f x)
    (f (* x 2)))
```
or
```scheme
(define (g y) (+ y 15))
```

### Built-in functions
- MAP
```scheme
(define (g y) (+ y 15))
(map g '(20 30 40 50))
; This results in (35 45 55 65)
```
or
```scheme
(map car '((1 2 3) (a b c) ("hello" "goodbye")))
; This results in (1 a "hello")
```
- Writing our own version of **MAP**:
```scheme
(define (myMap f L)
    (cond ((null? L) '())
          (else (cons (f (car L)) (myMap f (cdr L))))))
(myMap g '(2 3 4 5 6))
; This results in (17 18 19 20 21)
```
- Increment
```scheme
(define (increment x) (+ x 1))
(map incremnt '(1 2 3 4)) ; results in (2 3 4 5)
```

### Anonymous functions
Instead of defining named functions, we can define **anonymous** functions to do it with *LAMBDA*
```scheme
(lambda (x y) (+ x y0)) ; results in #<procedure>
```
- Using **map** with **lambda**:
```scheme
(map (lambda (x) (* x 2)) '(1 2 3 4 5))
; Results in (2 4 6 8 10)
```
- Note that
```scheme
(define (f x y) (+ x y))
```
is just a shorthand for
```scheme
(define f (lamda (x y) (+ x y)))
```
- Lambda to create a function in nested scope and return the function out of that scope
```scheme
(define (f x)
    (lambda (y) (+ x y))
(f 3) ; just results in #<procedure>
(define g (f 3))
(g 5) ; x is 3 and y is 5
```
- More weird things
```scheme
(define L (list (lambda (x) (+x 1)) (lamda (x) (+ x 2)) (lamda (x) (+ x 3))))
L ; This results in (#<procedure> #<procedure> #<procedure>)
((car L) 3) ; returns 3 + 1 = 4
((caddr L) 3) ; returns 3 + 3 = 6
```
- Defining recursive functions within an inner scope
```scheme
(let ((f (lambda (x) (if (= x 0) 1 (* x (f (- x 1)))))))
  (f 5)) ; that won't work, as there is a recursive definition
- Solution: **letrec**
```scheme
(letrec ((f (lambda (x) (if (= x 0) 1 (* x (f (- x 1)))))))
  (f 5))
```
**letrec** can be used to define mutually recursive functions
```scheme
(letrec ((f (lambda (x) (if (= x 0) 1 (* x (f (- x 1))))))
         (g (lambda (x) (if (= x 0) 1 (* x (f (- x 1)))))))
    (g 6)) ; returns 720
```

### Exam and assignment
Treat Scheme as being purely functional (although it's not true)
