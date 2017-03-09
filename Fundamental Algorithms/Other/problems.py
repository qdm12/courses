""" FACEBOOK GLASSDOOR """
# Dynammic programming is a method for solving a complex problem by breaking it 
# down into a collection of simpler subproblems, solving each of those 
# subproblems just once, and storing their solutions ideally, using a 
# memory-based data structure. The next time the same subproblem occurs, instead 
# of recomputing its solution, one simply looks up the previously computed solution, 
# thereby saving computation time at the expense of a (hopefully) modest 
# expenditure in storage space. (Each of the subproblem solutions is indexed in 
# some way, typically based on the values of its input parameters, so as to 
# facilitate its lookup.) The technique of storing solutions to subproblems 
# instead of recomputing them is called "memoization".

""" 
If your are given an Integer Singly linked list. Print it backwards. 
Constraints: 1. Do not manipulate the list. 
(example: do not make it a doubly linked list, do not add or delete elements, 
do not change any memory location of any element) 
2. O(n) < time < O(n^2) 3. O(1) < space < O(n) 
"""
class REVERSELINKEDLIST:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    
    # @param A : Head node
    # Complexity O(n) and space O(1)
    def print_reverse(self, A):
        if A is not None:
            self.print_reverse(A.next)
            print A.val,
            
    def run(self):
        A = self.ListNode(1)
        B = self.ListNode(2)
        C = self.ListNode(3)
        A.next = B
        B.next = C
        self.print_reverse(A)
        
""" 
Reverse a linked list dynamically (so delete the nodes)
"""
class REVERSELINKEDLISTDYNAMIC:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    
    # Complexity O(n) and space O(1)
    def reverse(self, A):
        # @param A : Head node
        if A.next is None:
            return A
        rest = self.reverse(A.next)
        A.next.next = A
        A.next = None
        return rest
            
    def print_list(self, A):
        while A is not None:
            print A.val
            A = A.next
    
    def run(self):
        A = self.ListNode(1)
        B = self.ListNode(2)
        C = self.ListNode(3)
        A.next = B
        B.next = C
        A = self.reverse(A)
        self.print_list(A) 
   
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        
    def __repr__(self):
        if self.imag == 0:
            return str(self.real)
        elif self.real == 0:
            return str(self.imag)
        else:
            return str(self.real) + " + i" + str(self.imag)
        
class SquareRoot:
    def __init__(self, precision = 0.000001):
        self.precision = precision
    
    # @param A : Integer or float
    def squareRoot(self, A):
        if A == 0:
            return ComplexNumber(real = 0)
        elif A < 0:
            A = -A
            return ComplexNumber(imag = self.test(A, A / 2.00))
        else:
            return ComplexNumber(real = self.test(A, A / 2.00))
    
    def test(self, A, g):
        if self.closeEnough(A/g, g):
            return g
        return self.test(A, self.betterGuess(A, g));
    
    def closeEnough(self, a, b):
        return abs(a - b) / max(abs(a), abs(b)) < self.precision

    def betterGuess(self, A, g):
        return (g + A/g) / 2
            
class FIBONACCI:
    # @param A : Positive Integer
    # Complexity O(2^n) and space O(1)
    def fib_recursive(self, A):
        if A < 3:
            return 1
        return self.fib_recursive(A-1) + self.fib_recursive(A-2)
    
    # @param A : Positive Integer
    # @param initial : Boolean, has to be true for first call
    # Complexity O(n) and space O(n)
    def fib_recursive_memoization(self, A, initial=False):
        if initial: #ran only once at first call
            self.mem = [None for _ in range(A)]
        if A < 3:
            self.mem[A-1] = 1
            return 1
        if self.mem[A-1 - 1] is None:
            self.fib_recursive_memoization(A - 1)
        if self.mem[A-1 - 2] is None:
            self.fib_recursive_memoization(A - 2)
        self.mem[A-1] = self.mem[A-1 - 1] + self.mem[A-1 - 2]
        return self.mem[A-1]
    
    # @param A : Positive Integer
    # Complexity O(n) and space O(1)
    def fib_iterative(self, A):
        x = 1
        y = 1
        for _ in range(2, A):
            x, y = y, x + y
        return y
    
    def run(self):
        print self.fib_recursive(6)
        print self.fib_iterative(6)
        print self.fib_recursive_memoization(6, initial=True)

"""
Use bit operations to write a function that will determine if a number is a power of 2
"""
class POWER2:
    def isPowerOf2(self, A):
        if A <= 0:
            return False
        return A & (A - 1)
    
"""
Max occurrence letter in a string. [Kept on adding constraints like ignore 
spaces, special characters, case insensitive..] Later asked about space and 
time complexities
"""
class MOSTCOMMONLETTER:
    # @param s : string
    def findMostCommonLetter(self, s):
        letters = dict() # at most 26 keys
        s.lower() # converts to lowercase
        for c in s: # Takes O(n) time
            if c.isalpha(): # c is a letter
                if c not in letters:
                    letters[c] = 0
                letters[c] += 1
        # Now we have a dictionary with at most 26 entries and their counts.
        maximum = -1
        most_common_c = None
        for c in letters: # Takes O(n)
            if letters[c] > maximum:
                maximum = letters[c]
                most_common_c = c
        return most_common_c


""" FACEBOOK CODELAB """
class NUM1BITS:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        if A > 0:
            n = self.numSetBits(A >> 1)
            if A % 2 != 0:
                return n + 1
            return n

class LISTCYCLE:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A == None:
            return None
        x1 = x2 = A
        while x1 and x2 and x2.next:
            x1 = x1.next
            x2 = x2.next.next            
            if x1 == x2:
                x1 = A
                while x1 != x2:
                    x1 = x1.next
                    x2 = x2.next
                return x1
        return None
    # OR JUST USE SETS
    
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
class REMDUPLNK:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        while A.next is not None:
            if A.val != A.next.val:
                A = A.next
            else:
                A.next = A.next.next
        return head
        
"""
N light bulbs are connected by a wire. Each bulb has a switch associated with it, 
however due to faulty wiring, a switch also changes the state of all the bulbs 
to the right of current bulb. Given an initial state of all bulbs, find the 
minimum number of switches you have to press to turn on all the bulbs. 
You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.
"""
class BUBLS:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        state = False
        switches = 0
        for a in A: #we can just go from left to right as ONLY one switch affects the RHS !
            if a == int(state):
                state = not state
                switches += 1                
        return switches

"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach's conjecture
Input : 4
Output: 2 + 2 = 4
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then
[a, b] < [c, d] 
If a < c OR a==c AND b < d. 
"""
class PRIMESUM:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for p1 in range(2, A/2 + 1):
            p2 = A - p1
            if self.isPrime(p1) and self.isPrime(p2):
                return [p1, p2]
    
    def isPrime(self, A):
        if A < 2:
            return False
        if A == 2:
            return True
        for i in range(2, int(A**0.5)+1):
            if A % i == 0:
                return False
        return True
    
"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
"""
from math import log
class POWER:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 0:
            return False
        if A == 1:
            return True
        log_A = log(A)
        for b in range(2, int(A**0.5) + 1):
            p = float(log_A)/log(b)
            if round(p,8).is_integer() and p > 1:
                return True
        return False
                    
"""
You are in an infinite 2D grid where you can move in any of the 8 directions :
(x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
"""
class ARRAY_BUG:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        steps = 0
        for i in range(1, len(X)):
            deltaX = abs(X[i] - X[i-1])
            deltaY = abs(Y[i] - Y[i-1])
            steps += max(deltaX, deltaY)
        return steps
        
class DIAGONAL:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        n = len(a)
        ret = []
        for i in range(n):
            anti_diagonal = [a[0][i]]
            for j in range(1, i+1):
                anti_diagonal.append(a[j][i - j])
            ret.append(anti_diagonal)
        for i in range(1, n):
            anti_diagonal = [a[i][n-1]]
            for j in range(1, n - i):
                anti_diagonal.append(a[i + j][n-1 - j])
            ret.append(anti_diagonal)
        return ret
    
"""
Given N and M find all stepping numbers in range N to M

The stepping number:

A number is called as a stepping number if the adjacent digits have a difference of 1.
e.g 123 is stepping number, but 358 is not a stepping number

Example:

N = 10, M = 20
all stepping numbers are 10 , 12 
Return the numbers in sorted order.
"""
class STEPNUM:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        ret = []
        for n in range(A, B+1):
            if self.is_step(n):
                ret.append(n)
        return ret
    
    def is_step(self, n):
        n_array = map(int, str(n))
        for i in range(len(n_array)-1):
            diff = n_array[i] - n_array[i+1]
            if diff != 1 and diff != -1:
                return False
        return True

# not efficient enough !

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
"""
class SINGLE:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        n = 0
        for a in A:
            n ^= a # Use XOR gate
        return n     

"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
"""
class GCD:
    def gcd(self, A, B):
        if A == 0:
            return B
        if B == 0:
            return A
        while A > 0 and B > 0:
            if A < B:
                A, B = B, A
            if A % B == 0:
                return B
            A -= B
    
    def gcd_recursive(self, A, B):
        if A == 0:
            return B
        return self.gcd_recursive(B % A, A)


"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.
"""
class LENGTHLAST:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        length = 0
        word_started = False
        for i in range(len(A) - 1, -1, -1):
            if A[i] != ' ':
                word_started = True
                length += 1
            elif word_started:
                return length
        return length

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2. 
"""
class MAJORITY:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        # Takes space O(n) but remove duplicates
        threshold = int(len(A)/2)
        counts = dict()
        for a in A: # O(n)
            if a not in counts: # O(1)
                counts[a] = 0
            counts[a] += 1
            if counts[a] > threshold:
                return a
            
"""

"""
class REVBITS:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        rev = 0
        for i in range(32):
            if A & (1 << i):
                rev = rev | 1 << ((32-1) - i)
        return rev
    
    def reverse_cheat(self, A):
        return int(str(bin(A))[2:].zfill(32)[::-1], 2)
