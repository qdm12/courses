# Programming language course, Spring 2017

## Lesson 13: Dynamic storage allocation

- Refers to the run-time allocation of storage for variables, structures, procedure calls, etc.
- Except Fortran, the amount of storage required for these objects can't be determined at compile time.

### Language features requiring DSA
- Recursion
- Pointers
- Explicit allocation
    - new
    - malloc
    - cons
- Dynamic data structures
    - lists
    - trees
    - graphs
    - dynamic arrays
- Higher order functions
    - lambdas
    - etc.

### Stack storage Allocation
- Mostly for imperative languages (C, Ada, ...)
- **Last-In-First-Out** allocation
    - For *activation records*
    - Why? Because local variables and parameters do not outlive the procedure calls
    - Procedure return -> its *activation record* removed from the **stack**
        - Local variables are automatically **deallocated**
        - This deallocation is **safe** for integers, ..., records and arrays.
    - This causes problem with **pointers**
        - Pointers are used for *aliasing*: multiple identifiers to refer to the same object
        - In OOP such as Java, all objects have **pointer semantics**
        - An object referenced by a pointer p can't be deallocated when p is returned for example.
    - An object outliving the function that created it is stored out of the function's stack frame.
- Such an object is stored in the **heap**
    - The lifetime, or **extent**, depends on execution and is thus called **dynamic extent**.
- The address space:
  ```
   __________________________
  |     Stack section        |
  |__________________________|
  |                          |
  |__________________________|
  |         Heap             |   Data
  |Globals, constants, etc.  |  Section
  |__________________________|
  |      Code section        |
  |__________________________|
  ```
  
- There are some unecessary heap-allocated objects that can be removed (otherwise the heap becomes full)
    - by the **user**, via calls to `free` or `delete` (C, Ada, C++)
    - by the **system** automaticaly, via **garbage collectors** (Scheme, ML, Java, Scala, Python)

### Heap storage Allocation
1. Free List
    - Available storage blocks are chained in a **linked list**
    - When a block is *required*, it is removed from the free list
    - When a block is *reclaimed*, it is inserted in the free list
    - Advantages and disadvantages
        - **Expensive allocation**
            - Search for a block of the **right size**
            - **Fragmented memory**
        - **Cheap reclamation**
2. Heap pointer
    - Available space is maintained in a **contiguous block** of bytes
    - The heap pointer points to the *next available byte*
      ```
       _____________________
      |        Free         |
      |        Space        |
      |_____________________| <- Heap pointer
      |=====================|
      |======= Used ========|
      |======= Space =======|
      |=====================|
      |=====================|
      |_____________________|
      ```
    - Advantages and disadvantages
        - **Cheap allocation**
        - **Expensive reclamation**
            - Requires **compaction** of live objects so that they are all adjacent
            
### Garbage collection
- A garbage collector:
    1. Finds each storage block by a **dead object** (*object which can't subsequently be referenced during execution*)
    2. Make that storage available for subsequent use
- Two categories
    1. Mark & Sweep collectors and Copying collectors
        - Determine all live objects through memory only **when the heap fills up**
        - The complement of this set (dead object) can be reclaimed
    2. Reference counting collectors
        - Determine when an object becomes dead **during execution** and its storage is then reclaimed.
        