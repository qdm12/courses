# Programming language course, Spring 2017

## Lesson 6: Scheme
- It is a dialect of LISP
- Statistically scoped
- Dynamically typed

### Requirements    
- racket v6.6

### Basic types
```scheme
12 ; integer
13.356 ; float
'hello ; symbol where the only characteristic is its name.
"hello" ; string
;; The primary AGGREGATE TYPE is the list.
;;; Elements of a list can be of different types.
;;; Lists can be nested
'(34 (1 five) tom sally "hello")
```

### Expressions
- Atomic expressions
  ```scheme
  ;; Numeric literals
  34
  67.9
  ;; Symbol literals
  red
  green
  ;; Boolean literals
  #t
  #f
  ;; The empty list
  ()
  ;; Variable names
  x
  y
  z
  ```
- Combination expressions, which start with `(` and ends with `)`
  ```scheme
  ;; Defining variables
  (define x 6) ; declares a variable x whose value is 6
  #<procedure:>> ; XXX
  '(define y 7)
  y ;XXX
  (define y 7)
  y ;XXX
  ```
- Aritmetic expressions
  ```scheme
  (+ x y)
  + x y
  #<procedure:+>
  6
  7
  (quote x)
  'x
  ```
  
### Functions
```scheme
(define (f z y)(+ z (* 2 y))) ; define function f
(f 3 (+ x 5)) ; calls function first
```

### Conditionals
```scheme
;; (if <condition> <then-part> <else-part>
(if (= x y) 'yes (* x y))
;; (cond (<condition1> <result1>)
;;		 (<condition2> <result2>)
;;		 (else <result>)
(cond ((= x y) 'first)
	  ((< x y) 'second)
	  (else 'third))
```

### Example: *Hanoi* function
```scheme
;;; Towers of Hanoi in Scheme
(define (hanoi N from to temp)
	(cond ((= N 1) (display "Move fisk from ") (display from)
                   (display " to ") (display to) (newline))
        (else (hanoi (- N 1) from temp to)
			  (display "Move disk from ") (display from)
			  (display " to ") (display to) (newline)
			  (hanoi (- N 1) temp to from))))
(hanoi 1 'a 'b 'c)
(hanoi 4 'a 'b 'c)
```

### Lists
```
'(1 2 3 4) ; first way to create a list
(list 1 (+ 2 3) (* x y)) ;;; args are evaluated and put in a list
;;; (cons x L) where is a value and L is a list, creates a new list with x followed by L's elements
(define myList '(2 3 4 5))
(cons 1 myList)
;; myList is unmofidied though
;;; (append L1 L2)
(append '(1 2) '(3 4))
(cons '(1 2) '(3 4))

;;; ACCESSING THE ELEMENTS OF A LIST: CAR CDR
;; (car L) returns the first elements of the list L
(car '(2 4 6 8))
;; (cdr L) returns all except the first elements
(cdr '(2 4 6 8))
;; (car (cdr (cdr L))) to get the third element
(car (cdr (cdr '(1 2 3 4))))

'() ;; the empty list, which is also (cdr '(1))
(null? myList) ;; will return #f

(define (nth n L)
	(cond ((= n 1) (car L))
		(else (nth (- n 1) (cdr L)))))
(nth 5 '(2 4 6 8 10 12))

;;; Append can be written in Scheme
(define (myappend L1 L2)
	(cond ((null? L1) L2)
		(else (cons (car L1) (append (cdr L1) L2)))))
(myappend '(2 3 4) '(7 8 9))

;;; put an element at the end of a list
(define (atEnd x L) ;;; returns a list containing all the elements of L followed by x at the end
	(cond ((null? L) (list x))
		(else (cons (car L) (atEnd x (cdr L))))))

(atEnd 3 '(4 5 6 7 8))

(reverse '(1 2 3 4 5)

(define (myReverse L) ; Quadratic complexity
    (cond ((null? L) '())
          (else (append (myReverse (cdr L)) (list (car L))))))

(define (myRev from to) ; Linear complexity
    (cond ((null? from) to)
        (else (myRev (cdr from) (cons (car from) to)))))
        
(myRev '(1 2 3 4 5) '())

(let ((x 12) (y 3)) ;; define nested scopes (new var within expressions)
    (+ x y))
x
```