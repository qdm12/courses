/* Anonymous functions (Lambda): ((parameters) => body) */
object lambdaExample{
  def higher(f: (Int) => Int) = f(f(3))  
  def main(args: Array[String]) = println(higher((x) => x+1)) // 5
}