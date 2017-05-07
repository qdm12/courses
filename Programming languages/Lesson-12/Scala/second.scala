/* Inheritance 
   All class inherit from Object */

class A(x:Int, y:String){ //parameters are used as for a constructor.
    val value = x
    val name = y
    override def toString():String = value + name
}
class B(a:Int, b:String, c:Int) extends A(a,b){
    val age = c
    override def toString() = age + (value + name + name)
}

object Test{
    def f(a:A){println(a)}
    def main(args:Array[String]){
        val a = new A(1, "One")
        val b = new B(2, "Two", 36)
        println(a)       
        f(b); //Subtyping: pass a B to a method that expects an A
    }
}