/* Case classes and match clauses for pattern matching.
   An object of a case class can be created without the "new" keyword. */
abstract class Tree
case class Node(v:Int, l:Tree, r:Tree) extends Tree
case class Leaf(v:Int) extends Tree
case class Empty() extends Tree
object CaseClassTest{
    val myTree = Node(3,Leaf(4),Node(5,Leaf(6),Empty())) // no new !
    def printTree(t:Tree){
        t match {
            case Node(v,l,r) => print("(") 
                                printTree(l) 
                                print(v)
                                printTree(r)
                                print(")")
            case Leaf(v) => print(v)
            case Empty() => ()
        }
    }
    def main(args:Array[String]){printTree(myTree)} // (43(65))
}