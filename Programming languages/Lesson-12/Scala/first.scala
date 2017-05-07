/* Singleton class
   They are instantiated by a single object rather than by static members as in Java.
   They are declared using the "object" keyword. */

object Counter{
    var count = 0
    def increment{count = count + 1}
    def get() = count
    def useCount(f: (Int) => Unit) = f(count)
}

class F{
    val x = 12
    var y: Int = 20
    def f(z:Int):Int = x+y+z
    // Example of a method whose name is a symbol (no special syntax for that)
    def +(other:F):Int = y + other.y
    def set(w:Int){
        Counter.increment
        y = w
    }
}

object Bar{
    def printArg(x:Int){println("Got the value " + x)}
    def main(args: Array[String]){
        val f1 = new F()
        val f2 = new F()
        f1 set 17;  // same as f1.set(17)        
        f2.set(25)
        println(f1 + f2)  //same as f1.+(f2), prints 42
        println("Counter is now " + Counter.get()) // 2
        Counter.useCount(printArg) // Got the value 2
        Counter.useCount((x:Int) => println(x*1000)) // 2000
    }
}