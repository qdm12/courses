# Programming language course, Spring 2017

## Recitation 2: Syntax, regular expressions and CFG

- Regular Expression
- CFG
- Derivations and Parse trees

### Phases of compiler
- lexer
- parser
- semantic analyzer
- intermediate code generator 
- Optimization (depends on system architecture)
- Target code generation

### Regular Expressions
- Tokens are the basic building blocks of a program. They are the shortest strings of characters with individual meaning. 
- Examples include keywords, identifiers, symbols, constants and numbers. 
- To specify tokens, we use the notation of regular expressions 
- Used in the phase 1 - lexical analysis (scanner) of the compiler. 
- Possibilities
	- Concatenation `R1R2` (*Two RE next to each other)
    - Alternation `R1 | R2` (*OR*)
    - Kleene star `*`: *i.e. R1* which is E (empty epsilon) or a or aa or aaa...*
- Drawbacks
    - Nesting cannot be expressed (parenthesis, palindromes)
- Other examples
    - `€` *epsilon* mathces a null string
    - `[a-z]` matches any character between *a* and *z*
    - `[A-Za-z]` for alphabet
    - `0|1|2|3|4|5|6|7|8|9` matches a digit
    - `digit digit*` for an integer
    - Alphabet(digit|Alphabet)*

	
### Context free grammar (CFG)
- More powerful than regular expressions
- By adding RECURSION, we can define many more sets of strings
- Recognized by parsers
- Every regular grammar is context free but not every context free grammar is regular
- Used in the Phase 2 - Syntactic analysis (Parser) of the compiler
- Consists of
    - Productions (**Rules** of the form *A -> B*)
    - Nonterminals (*Symbols on the left of the production*)
    - Terminals (*Symbols making up the string derived from grammar*)
    - Start symbol (*The nonterminal on the LHS of the first production*)
- Examples
	- A ------> 0A1|€
		- Language of strings consisting of a number of 0s followed by an equal number of 1s
	- CFG for strings containing only 0s and 1s and contain equal number of 0s and 1s but in any order (01, 1100...)
        - S -----> 0S1S | 1S0S | €
    - CFG for all strings ending with *a* and containing the set (*a*, *b*).
        - S ----> aS|bS|a
    - CFG for all strings containing the set (*a*,*b*) and has even number of *a*s
        - S ----> aSaS|bS|€
- Complex example: CFG of this code:
```
read X
read Y
prod=X*Y
write prod
```
    - Solution:
      ```
      Program ---> Stmt_List
      Stmt_List ---> Stmt Stmt_List|€
      Stmt ---> id=Expr|read id|write id
      Expr ---> Expr OP Expr | -Expr | (Expr) | id | num
      OP ---> +|-|*|/
      ```
- Conditional example (continued from previous)
```
Stmt ---> id=Expr|read id|write id|Cond
Cond ---> if BoolExpr then Stmt_List else Stmt_List end
BoolExpr ---> Expr relOp Expr | True | False
relOp ---> == | > | < | >= | <= | !=
```
      
### Parse tree
