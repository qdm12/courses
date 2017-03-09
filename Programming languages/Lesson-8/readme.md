# Programming language course, Spring 2017

## Lesson 8: The Lambda-Calculus

- Syntactic model of computation
- Based on transformations applied to expressions
- The syntax of expressions (we use **£** for **lambda**)
  ```
  exp -> c      constant
      | x       variable
      | exp exp
      | £ x exp     function that takes x as parameter and body is exp
  ```
- Constants: 3 + if =
- Examples of expressions in the £-calculus
  ```
  7 y       f x       £y. + y
  (£x.x)(£y.y)
  ```
  