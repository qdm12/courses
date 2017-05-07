/* COVARIANT TYPE PARAMETERS for generic classes */
class A{
    val x = 26
    override def toString() = "A: "+x
}
class B extends A{
    val y = 99
    override def toString() = "B: "+x+", "+y
}
class MyList[+T](lis:List[T]){
    val l: List[T] = lis
    def get = l
    def cons[SUPERT >: T](x:SUPERT): MyList[SUPERT] = new MyList[SUPERT](x::lis)
    /* Since cons can't have a T in contravariant position, it introduces 
       SUPERT that ranges over the supertypes of T. 
       The resulting list is a MyList[SUPERT] because a SUPERT is inserted. */
    // def cons(x:T):MyList[T] = new MyList[T](x::lis)
    // Fails because it contains a T in contravariant position
    def hd = l match {
        case (x::xs) => x
        case List() => throw new Exception()
    }
    def tl = l match {
        case (x::xs) => xs
        case List() => throw new Exception()
    }
    override def toString() = l + ""
}

object variant{  
    def foo(l:MyList[A]){
        println(l)
    }
    def main(args: Array[String]) {
        val lA = new MyList(List(new A()))
        val lB = new MyList(List(new B()))
        val hdA:A = lA.hd
        val hdB:A = lB.hd // expects A but receives B
        foo(lA) // expects MyList[A], prints List(A: 26)
        foo(lB) // expects MyList[A] and receives MyList[B], prints List(B: 26, 99)
        println(hdA) // A: 26
        println(hdB) // B: 26, 99
    }
}