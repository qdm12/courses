# Programming language course, Spring 2017

## Lesson 1: Introduction
### Programming language (PL)
- Aim
    - express algorithms to other people 
    - instruct computer to perform computations
- Necessary properties of a PL:
    - implementable
    - unambiguous 
    - Turing complete (sufficiently powerful to express only computable function)
- Desirable properties of a PL:
    - High level
    - System independent 
    - Concise (not APL) 
    - Readable
    - Strong math foundation 
    - Reusability
    - Efficiency
    - Exception handling 
    - Rich set of Operations

### Types of PL
- Low-level PL: constructs of the language reflect the computer hardware
    - Writing to memory locations 
    - Testing bits and jumping 
    - Perform arithmetic instructions
- High level PL: reflects a computational model other than the computer hardware 
    - Mathematical function 
    - logic languages (1st order logic)
    - Set theory
- Imperative language
    - Variables are memory locations 
    - Assignment statements write data to memory location
    - Loops != jumps for directing execution over assignment statements
- ML - functional language
    - Variables are not memory locations 
    - No assignment statements that overwrite locations 
    - No loops, only recursion
    ```sml
    fun fac 0 = 1
     | fac n = n * fac(n-1)
    ```

### Turing Machine
- A language is Turing complete if it is equivalent in power to a conversal Turing machine
- A TM that can emulate any other TM

### How to define a PL
- Syntax: rules governing the organization of symbols (letters, digits, spaces, etc) in a valid program
- Defined by grammars
- Semantics give meaning to valid expressions (sequence of symbols) such as `a = b + c`

### Grammars for defining syntax
- Regular expression
    - used for defining the words (names, keywords, numeric) 
- Context free grammar (**CFG**)
    - Used to define how words are composed to form expressions 
    - Expressions are composed to form statements and so on
