# Programming language course, Spring 2017

## Midterm

### What to know essentially
- Turing completeness
    - A **Turing complete** system is a system in which a program can be written 
      that will find an answer (no guarantees regarding runtime or memory).
    - A programing language is **Turing complete** if it can run any program 
      that a Turing machine can run given enough time and memory.
- Different [kind of languages](../Lesson-1#types-of-pl)

- [Syntax, semantics, compiler, interpreter](../Lesson-2#lesson-2-syntax) and no details of compiler will be asked.
- [Regular expressions](../Lesson-2#grammars-used-to-define-the-syntax-of-pl)
    - Sequence of characters that define a search pattern
    - Consist of **constants** (denote sets of strings) and **operator symbols** (denote operations over these sets)
- [CFGs](../Lesson-2#grammars-used-to-define-the-syntax-of-pl)
    - A set of **production rules** (simple replacements) that describe 
      all possible strings in a given formal language

- [Static and dynamic scoping](../Lesson-3#scoping)
- [Ada Module/Package interface (specification)](../Lesson-3#ada)
- Concurrency: Inability to know the order in which things happen
- Express modules and concurrency in Ada (Task, packages)
  ```ada
  TO DO
  ```

- [The 4 passing mechanisms](../Lesson-4)

- [Call Stack](../Lesson-5)

- Scheme [here](../Lesson-6) and [here](../Lesson-7)
- Treat Scheme as being purely functional (although it's not true)