# Programming language course, Spring 2017

## Recitation 1
***
**MISSING**
***
- lexer
- parser
- semantic analyzer
- intermediate code generator 
- **MISSING**

Regular Expressions 
- Tokens are the basic building blocks of a program. They are the shortest strings of characters with individual meaning. 
- Examples include keywords, identifiers, symbols, constants and numbers. 
- To specify tokens, we use the notation of regular expressions 
- Used in the phase 1 - lexical analysis (scanner) of the compiler. 
- Drawbacks
	- Nesting cannot be expressed (parenthesis, palindromes)

Regular expressions operations
- concatenation R1R2
- Alternation i.e. R1 | R2
- Kleene star (*) i.e. R1* which is E (empty epsilon) or a or aa or aaa... 
	
Context free grammar (CFG)
- More powerful than regular expressions
- By adding RECURSION, we can define many more sets of strings
- Recognized by parsers
- Every regular grammar is context free but not every context free grammar is regular
- Used in the Phase 2 - Syntactic analysis (Parser) of the compiler
- Examples
	- A ------> 0A1|E
		- Language of strings consisting of a number of 0s followed by an equal number of 1s
	- Give CFG for strings containing only 0s and 1s and contain equal number of 0s and 1s but in any order (01, 1100...)
	- Solution: S -----> 0S1S | 1S0S | E

