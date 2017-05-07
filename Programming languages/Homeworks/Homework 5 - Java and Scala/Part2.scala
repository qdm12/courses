/* 1. Define a class A that implements the Ordered trait. A should define the compare method required by Ordered
and should override the toString method so that it prints something sensible (identifying the object as a A
object). Each object of the A class should be instantiated with an integer parameter, e.g. by saying new A(6).
The result of comparing two A's should be based on the values of the integers they were created with. For
example, the expression (new A(5)).compare(new A(6)) should return ­1, because 5 is less than 6 (you can simply 
subtract the integer values that the objects were created with). This will allow two A objects to be compared 
using the usual < and > operators. (Note: Due to limitations of the type system, == will not be redefined to 
automatically work correctly. Use (x.compare(y) == 0) if you want to test equality between objects x and y). */
class A(a:Int) extends Ordered[A]{
  val a_string = a.toString
  var value:Int = a
  def compare(that:A):Int = {
    val diff = this.value - that.value
    if(diff < 0){
      return -1;
    }else if(diff > 0){
      return 1;
    }else{ //they are equal
      return 0;
    }
  }
  override def toString() =  "A<"+a_string+">"
}

/* 2. Define a class B that extends class A. Each object of the B class should be instantiated with two integer
parameters, e.g. by saying new B(6,7). The value to use in the compare() method is the sum of the two integers 
that the object was created with. For example, (new B(4,5) < new A(7)) would return false, because 4+5 is not 
less than 7. You don't need to override compare(). You can, for example, create a value field that is used in 
the comparison (and do the same in class A). Be sure that (new A(7) < new B(4,5)) would return true, given 
your definition of A and B.*/
class B(a:Int, b:Int) extends A(a){
  val b_string = b.toString
  value = this.a + this.b
  override def toString() =  "B<"+a_string+","+b_string+">"  
}

/* 3. Define a generic class C[T] with the following properties:
   		- Instances of C[T] are covariantly subtyped. For example, given the above classes A and B, anywhere 
   		  a C[A] is expected a C[B] can be used.
   		- Each instance of C[T] should be created with a function of type Int=>T. For example, if g is a 
   		  function of type Int=>A, then the following declaration would work: var c: C[A] = new C(g)
   		- C[T] has a method apply(), which takes an integer parameter x and returns the result of calling f(x),
		    where f was the function that the object was created with. For example, given the above definition of 
		    the c variable, the expression c.apply(3) would return the result of calling g(3). */
class C[+T](f:Int=>T) {
  def apply(x:Int) = f(x)
}

/* 4. Define an abstract generic class Tree[T] for implementing binary search trees, such that:
      - T must itself implement the Ordered trait, allowing two T's to be compared.
      - Any class derived from the Tree[T] must implement an insert method that takes a parameter of type T
				and returns a value of type Tree[T]. To do this, simply put the following (and nothing else) within the
				Tree[T] class definition: def insert(x:T):Tree[T] */
abstract class Tree[T <: Ordered[T]]{ // extends Ordered[Tree[T]]
  def insert(x:T):Tree[T]
}

/* 5. Define three case classes, Leaf[T], Node[T], and Empty[T] that extend the Tree[T] class, such that:
      - Leaf[T] should be parameterized by a T object representing the label at the leaf.
      - Node[T] should be parameterized by a T object representing the label at the node and by two Tree[T]'s
				representing the left and right subtrees.
		  - Empty[T] should take no parameters. For example, the following creates a Tree[A] object:
				val MyTree = Node(new A(3), Leaf(new A(2)), Node(new A(5),Leaf(new A(4)),Empty()))
		  - Each of the the above case classes should override the toString() method to have a sensible printout.
				For Empty[T], toString() can simply return the empty string. toString() for a Node[T] should be
				defined so that a tree is printed out in in­order fashion, which means for an interior node, the left 
				subtree should be printed, followed by the label at the node, followed by the right subtree.
		  - Each of the case classes should define an insert() method, override def insert(x:T): Tree[T] =  ...
		    that returns a new Tree[T] resulting from inserting a label x into the current tree in the appropriate 
		    place, so that the result is still a binary search tree. As you probably remember, a binary search tree 
		    is a binary tree with the property that the label at an interior node is greater than the label of its 
		    left child (if there is a left child) and not greater than the label of its right child (if there is one). 
		    For example, calling Empty[T]'s insert(x) should return a leaf whose label is x. Calling Leaf[T]'s insert(x) 
		    should return an interior node that has one leaf child and one empty child (depending on the relative 
		    values of x and the current leaf's label). Don't worry about keeping the search tree balanced in any way.
 */

case class Empty[T <: Ordered[T]]() extends Tree[T]{
  override def insert(x:T):Tree[T] = {
    return Leaf[T](x)
  }
  override def toString() = ""
}

case class Leaf[T <: Ordered[T]](label:T) extends Tree[T]{
  override def insert(x:T):Tree[T] = {
    if(x > label){
      return Node[T](label, Empty[T], Leaf[T](x))
    }else{ //x <= label
      return Node[T](label, Leaf[T](x), Empty[T])
    }
  }
  override def toString() = label.toString
}

case class Node[T <: Ordered[T]](label:T, left:Tree[T], right:Tree[T]) extends Tree[T]{
  override def insert(x:T):Tree[T] = {
    if(x > label){
      return Node(label, left, right.insert(x))
    }else{ //x <= label
      return Node(label, left.insert(x), right)
    }
  }
  override def toString() = "("+left.toString+","+label.toString+","+right.toString+")"
}


/* 6. In a singleton class named Part2, put the following.
      - A method applyTo10()that takes a parameter c of type C[A] and returns the result of calling c.apply(10).
      - A generic method found(), parameterized by a type parameter T, such that T implements the Ordered
				trait. found() should take a parameter y of type T and a parameter tr of type Tree[T] and return true if y
				is found in tr and false otherwise. Since tr is a binary search tree (above), searching for y is fast (linear
				in the depth of the tree). Do not use == to check for equality on objects of type T, rather write 
				(y.compare(x)==0) to determine if y equals x.
		  - A main() method that simply calls the test() method, below.
		  - The following test() method (shown below)
		  - The output should look like:
		    A<3>
            B<4,5>
            A<10>
            B<11,12>
            ((A<2>,A<3>,),A<4>,B<4,1>)
            A<3>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
            A<5>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
            B<2,1>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
            B<4,2>is not found in ((A<2>,A<3>,),A<4>,B<4,1>) */

object Part2{
  def applyTo10(c:C[A]) = c.apply(10)
  def found[T <: Ordered[T]](y:T, tr:Tree[T]):Boolean = {
    tr match {
      case Empty() => false
      case Leaf(label) => {
        if((label < y) || (label > y)){
          return false
        }else{ //label and y are equal
          return true
        }
      }
      case Node(label, left, right) => {
        if(y < label){
          return found(y, left)
        }else if(y > label){
          return found(y, right)
        }else{
          return true
        }
      }
    }
  }
  def test(){
    val c1 = new C((x:Int) => new A(x))
    println(c1.apply(3))
    
    val c2 = new C((x:Int) => new B(x+1, x+2))
    println(c2.apply(3))
    
    println(applyTo10(c1))
    println(applyTo10(c2)) //relies on covariant subtyping
    
    var t1:Tree[A] = Empty()
    t1 = t1.insert(new A(4))
    t1 = t1.insert(new A(3))
    t1 = t1.insert(new B(4,1))
    t1 = t1.insert(new A(2))
    println(t1)
    
    val a3 = new A(3)
    val a5 = new A(5)
    val b21 = new B(2,1)
    val b42 = new B(4,2)
    
    if (found(a3, t1))
      println(a3 + "is found in " + t1)
    else
      println(a3 + "is not found in " + t1)
           
    if (found(a5, t1))
      println(a5 + "is found in " + t1)
    else
      println(a5 + "is not found in " + t1)
      
    if (found(b21, t1))
      println(b21 + "is found in " + t1)
    else
      println(b21 + "is not found in " + t1)
      
    if (found(b42, t1))
      println(b42 + "is found in " + t1)
    else
      println(b42 + "is not found in " + t1)
  }
  def main(args:Array[String]):Unit = {
    test()
  }
}