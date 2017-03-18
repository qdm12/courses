# Programming language course, Spring 2017

## Lesson 5: Call Stack, recursive thinking

- Storage mechanisms
- Stack frame (Activation record)
- Static links
- Dynamic links
- Closures
- Recursive thinking

### Storage mechanisms
- **Static objects** are given an absolute address retained throughout the program execution.
- **Stack objects** are allocated and deallocated in a stack style in conjunction with calls and returns.
- **Heap objects** may be allocated and deallocated at arbitrary times and require a more general and expensive storage management algorithm.

### Stack Frame *or* Activation record
- Each routine called is given a new **stack frame** at the **top** of the stack.
- When a subroutine returns, its frame is popped from the stack.

### Stack frame structure
```
SP (Stack Pointer) ->
                      ¦ LOCAL VARIABLES ¦
FP (Frame Pointer) -> ¦ DYNAMIC LINK    ¦
                      ¦ RETURN ADDRESS  ¦
                      ¦ STATIC LINK     ¦
                      ¦ PARAMETERS      ¦
```
- **Frame pointer** (FP) points to a fixed place within the frame.
- **Stack pointer** (SP) has the address of the top of the stack.
- **Return address** points to the place in the *code* of the calling procedure to return to.
- **Static link**
    - Points into the stack frame of the *defining* procedure.
    - It is used to support *static scoping* in a language supporting nested procedures. 
    - Static scoping objects that lie in surrounding subroutines (not local nor global) can  be found by maintaining a **static chain**.
    - Each stack frame contains a reference to the frame of the lexically surrounding subroutine and is called **static link**.
- **Dynamic link**
    - Points to the top of the stack frame of the calling procedure
    - The old value of the FP when the calling procedure was executing
    - The saved value of the FP which will be restored on subroutine return
- *Notes*:
    - Parameters and local variables are accessed using offsets from the FP, such as *[FP+]
    - For a recursive function, there are many stack frames, each for each call not returned yet
    - On Intel x86 CPUs, the stack grows **down** in memory (SP address is decremented with a push instruction).
    
### Call stack illustration 1
For the following code:
```ada
procedure A()
    x:integer;
    procedure B()
    begin
        x := 1;
    end;
    procedure C()
        x:integer;
    begin
        B()
    end;
begin
    C();
end;
```

We would have the following call stack:
[illustration stack 1][stack_1]

- Since *B* is defined in *A*, static scoping requires that the *x* referenced by *B* is the *x* declared in *A*.
- *B* must follow its static link one hop to get to *A*'s stack frame.
- To access *x*, *B* follows its static link one hop and then uses an offset to get the location of *x*. 


### Call stack illustration 2
For the following code:
```ada
procedure A()
    x:integer;
    procedure B()
        procedure C()
            procedure D()
            begin
                x := 1;
            end;
        begin
            ...
        end;
    begin
        ...
    end;
begin
    ...
end;
```

We would have the following call stack:
[illustration stack 2][stack_2]

- **Dynamic chain** is a sequence of dynamic links.
- There may be stack frames for other procedures between stack frames A, B, C, D
    - The *dynamic chain* cannot be used to access *x* in *A*.
- The compiler generates a code for *D* that follows *D*'s static chain for 3 hops to get to *A*'s stack frame. It then uses an offset to access *x*.
- **Number of hops** is the difference between the nesting level at which the variable is defined and the nesting level at which the variable is accessed.
- **NO** searching for variables in the stack frames along the static chain is required.

### Call stack illustration 3
For the following code:
```ada
procedure A()
    x:integer;
    procedure B(procedure D)
        x:integer;
        begin
            D();
        end;
    procedure C()
    begin
        x := 1;
    end;
begin
    B(C);
end;
```

We would have the following call stack:
[illustration stack 3][stack_3]

- When *A* calls *B*, it passes a **closure** to represent the procedure *C* being passed as the parameter.
- Functions passed as parameters ae passed using closures.
- A **closure** contains
    - Code pointer **CP**: Pointing to the code for the procedure passed
    - Environment pointer **EP**: static link to be used when the passed procedure is called.
- When *B* calls *D*, *B* copies the static link from the *EP* portion of the closure to *D*'s stack frame.
- *D* is executed by jumping to the code pointed by the **CP** portion of the closure.
- All closures go on **heap**

### Functional programming and recursive thinking
- Evaluation of functions analogous to mathematical functions.
- Use **declarations and expressions** rather than *statements and instructions*.
- *Variables* represent **values** and not *moemory locations*, so no **mutable data**.
- Heavy use of **recursion** instead of *loops*
- Functions are *first-class* values

### First Class Functions
- Necessity of functional languages
- Functions can be passed as arguments
- Return functions as output to other functions
- Assign them to variables to store them in any data structure

### Recursive thinking
1. Handle base case.
2. Assume the function works on input of size **n-1**.
3. Create the solution for size **n** under above assumption.

Examples: Fibonacci, Factorial, Append 2 lists, reverse, maximum...


[stack_1]: stack_1.jpg
[stack_2]: stack_2.jpg
[stack_3]: stack_3.jpg