/* Code typed in class */
(x:Int) => x + 1 //Lambda
((x:Int, y:Int) => x + y)(3,4) // gives 7

class A
class B extends A  // B is a subclass of A
def fa(g:A=>Int) = g(new A())
def fb(g:B=>Int) = g(new B())
def p(x:A) = 6 //p is of type A->Int
def q(x:B) = 6   // q is of type B->Int
fa(p) // passing an A->Int to a function expecting an A->Int
fa(q) // passing a B->Int to a function expecting an A->Int, ERROR !
fb(q) // passing a B->Int to a function expecting an B->Int
fb(p) // passing an A->Int to a function expecting a B->Int, works fine (contravariant subtyping)
def f(g:Int=>A) = g(5) // f expects a parameter of type Int->A
f((x:Int) => new B()) // passing an Int->B to a function expecting an Int->A, works fine (covariance)
def fac(x:Int): Int = x match { // Factorial
     | case 0 => 1
     | case n => n * fac(n-1)
     | }

class C[T]
new C[Int]
// By default, there is no subtyping among instances of a generic.
def f(x:C[A]) = 3
f(new C[B]) // passing a C[B] to a function expecting a C[A], ERROR !

class C[+T] // Covariantly subtyped generic class
val c: C[A] = new C[B]() // using a C[B] object where a C[A] is expected (covariance)
val d: C[B] = new C[A]() // trying to use a C[A] object where a C[B] is expected (contravariance)
/* The + seriously limits the types of methods you can write.  Essentially, in a
   covariantly subtyped generic, the type parameter can only appear as the return
   type to a method (not the input type). */

class D[+T] {       
     |   def f(x:T) = 0  // ERROR ! since f takes a T as an input
     | }
// error: covariant type T occurs in contravariant position in type T of value x

class D[+T](x:T){
     |   def f(y:Int):T = x  // this will work, since T is the return type.
     | }

class E[-T]   // E[] is contravariantly subtyped
val c: E[A] = new E[B]() // Using an E[B] where an E[A] is expected. ERROR ! (covariance).
val c: E[B] = new E[A]()  // Using an E[A] where an E[B] is expected. Works fine (contravariance)
/* The - is also seriously limiting. In a contravariantly subtyped generic 
   class, a method can have the type parameter as the input type, but not 
   as the return type. */
class E[-T](x:T){ // contravariantly subtyped generic class
     |   def f(y:Int):T = x // ERROR ! can't have the type parameter T as a return type
     | }
class E[-T] {  
     |   def f(x:T): Int = 3  // this method works, can have type parameter T as the input type.
     | }