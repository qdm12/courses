/* Contravariance */
class A(x:Integer){
    override def toString() = "A<"+x+">"
}
class B(x:Integer, y:Integer) extends A(x){
    override def toString() = "B<"+x+","+y+">"
}
class Contra[-T](){
    var v:List[Any] = List()
    def insert(x:T){v = x::v}
    override def toString() = {
        def elementsToString(l:List[Any]):String = l match {
            case List() => ""
            case (x::xs) => x.toString() + " " + elementsToString(xs)
        }
        "Contra[ " + elementsToString(v) + "]"
    }
}

object Test{
    def test(c:Contra[B], z:B){
        c.insert(z)
    }
    def main(args: Array[String]){
        val cA = new Contra[A]()
        val cB = new Contra[B]()
        
        test(cB, new B(3,4))
        println(cB)

        cA.insert(new A(5))
        test(cA, new B(3,4)) //uses contravariant subtyping in first argument
        println(cA)
    }
}



