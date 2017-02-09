# Programming language course, Spring 2017

## Lesson 2: Syntax

### Semantics
- State semantics: Rules governing the user of types and the declaration of names
- Dynamic semantics: defines the execution behavior of each variable construct

### Compiler
- Translates from one PL to another
- Origin language: C++, C, Java, ...
- Target language: ASM, Machine code, Byte code

### Interpreter
- Executes the program, output is the result of the running program

### Phases of compilation
- lexical analysis called **lexer**
	- forms *words* (tokens) from sequences of characters
	- Examples
		- `for(` => "**for**" (*keyword*)
		- `xyz` => "**xyz** (*id*)
		- `1.629` => **1.629** (*num*)
- Parsing or *syntactic analysis* called **parser**
	- forms sentences from sequences of tokens
		- expressions
		- Statements
		- Declarations
		- Functions
		- Modules
		- Programs
- Type checking
	- ensures correct use of types and current declaration and use of names
- Code generator
	- Produces the target code
- Optimization
	- Improves the generated code

### Grammars used to define the syntax of PL
1. Regular expressions
	- Used to define the valid words in the PL
	- Regular Operators: `|`, `\*`
	- Notation: Regular expressions
	- Set
	- Correspondances notation to set
		- `R1 | R2` -> `R1 U R2`
		- `a` -> `{a}`
		- `ab` -> `{ab}`
		- `(a|b)b` -> `{ab, bb}`
		- `(a|b)\*` -> `{€, a, b, aa, ab, bb, aab, ...}`
		- *Note*: `€` (Epsilon) is the empty stems
	- `for|while|let|do`
	- digit -> `(0|1|2|3...|9)`  (Shortcut:* `[0-9]`)
	- `[0-9][0-9]\*.[0-9][0-9]\*`
	- Not use for syntactic relationships like brackets, not nesting as well
2. Context free grammar
    - Consists of
        - Non-terminal symbols
            - one of which is designated as the *start* non-terminal
        - Terminal symbols
            - Set of rules of the form `N` -> `s` where `N` is a 
            non-terminal and `s` a string of symbols (terminal and/or non-terminal)
    - Examples (Non-terminals `S`, `B`, and terminals `a`, `b`)
        - `S` -> `aSa`
        - `S` -> `B`
        - `B` -> `bBb`
        - `B` -> `€`
    - A CFG defines the set of all strings of non-terminals that can be 
    *derived* from the **start** non-terminal
    - Repeatedly applying the rules on the CFG, replacing a non-terminal 
    with a string by the right hand side of a corresponding rule
    - Derivation example 1
        - Given
            - `S` -> `aSa`
            - `S` -> `B`
            - `B` -> `bBb`
        - Derivation
            - `S` => `aSa` => `aaSaa` => `aaBaa` => `aabBbaa` => `aabbaa`
    - Derivation example 2
        - Given
            - `Exp` -> `exp+Exp`
            - `Exp` -> `Exp*Exp`
            - `Exp` -> `ID`
            - `Exp` -> `NUM`
            - also written as `Exp` -> `Exp+Exp|Expr*Exp|ID|NUM`
        - Derivation
            - `Exp` => `Exp*Exp` => `ID*Exp` => `ID*Exp+Exp` => `ID*NUM*Exp` => `ID*NUM*ID` => `ID*NUM+ID` => `X*3+Y`
    - Parse tree - Graphical representation of a derivation
    ```
    EXP----------*
       |---------EXP----------D
       |---------EXP----------+
                  |-----------EXP----------NUM
                  |-----------EXP----------ID
    ```
    - Ambiguous grammar
        - Allows to parse trees for the same string
        ```
        EXP----------+
           |---------EXP----------D
           |---------EXP----------*
                      |-----------EXP----------NUM
                      |-----------EXP----------ID
        ```
		
### Scope and blocks        
**Scope of a name**: Portion of the program in which the name is visible

**Block**: Syntactic construct that defines a scope (`{}` for example)

**Block structured language**
- Language where blocks can be nested, including nesting functions.
- A variable reference is resolved to the corresponding declaration 
the innermost surrounding block

```ada
x:integer;
procedure f()
begin
	x := x + 1;
end
procedure g()
	x:integer := 7;
begin
	f();
end
```