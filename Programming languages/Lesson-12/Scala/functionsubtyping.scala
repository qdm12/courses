class A
class B extends A

object Test{
    def fB(f:B=>String){
        val b:B = new B
        f(b)
    }
    def fA(f:A=>String){
        val a:A = new A
        f(a)
    }
    def gA(x:A) = x.toString()
    def gB(y:B) = y.toString()
    def main(args: Array[String]){
        fA(gA)
        /* fA(gB) */ /* Passing a function of type B->string to a function 
                        expecting an A->string gives a type error */
        fB(gA) /* Passing a function of type A->String to a function 
                  expecting a B->String works thanks to contravariance */
        fB(gB)        
    }
}