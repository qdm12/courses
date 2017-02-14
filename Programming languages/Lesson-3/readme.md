# Programming language course, Spring 2017

## Lesson 3: Scoping and Ada

### Scoping
- **Static scoping**
    - The body of a function is evaluated in the **environment** 
    in which the function is **defined**.
	- **Environment**: Mapping of names to values or memory locations
	```ada
	x:integer := 7; -- Static scoping
	procedure f()
	begin
		x := x + 1;
	end
	procedure g()
		x:integer := 20; -- dynamic scoping
	begin
		f();
	end
	```
- **Dynamic scoping**
    - The body of a function is evaluated in the **environment** 
    in which the function is **called**.
    ```ada
    x:integer := 8;
    procedure f(procedure h())
    begin
        h();
    end
    procedure g()
        x:integer := 20;
        procedure I()
        begin
            x := x + 1;
        end
    ```

### Ada
- Modularity (*packages*)
- Module
	- A collection of code
	- Has a resitrcted **interface** to code outside of the module
- Ada "*package*"
	- **Package specification** (*stack.ads*)
    
	```ada
	package stack is
        procedure push(x:integer);
        function pop return integer;
        stack_overflow, stack_underflow:exception;
	end stack;
	```
	- **Package body** (*stack.adb*)
    
    ```ada
    package body stack is
        subtype stack_index is integer range 1..20;
        the_stack: array (stack_index) of integer;
        index: integer:= 1;
        procedure push(x:integer) is
            begin
                if (index > 20) then
                    raise stack_overflow;
                else
                    the_stack(index) := x;
                    index := index + 1;
                end if;
            end;

        function pop return integer is
        begin
            if (index <= 1) then
                raise stack_underflow;
            else
                index := index - 1;
                return the_stack(index);
            end if;
       end;
    end stack;
	```
	- **Main procedure** (*main.adb*)
    
	```ada
	with text_io;
	with stack;
	
	procedure main is
        use text_io;
        package int_io is new integer_io(integer);
        use int_io;

        use stack;
        x,y,z:integer;
	  
	begin
        put("Enter number of pushes > ");
        get(x);
        put("Enter number of pops > ");
        get(y);
        for i in 1..x loop
            push(i);
        end loop;
        for i in 1..y loop
            z := pop;
            put(z);
        end loop;
	exception
        when stack_overflow =>
            put("Stack has overflowed"); new_line;
        when stack_underflow =>
            put("Stack has underflowed"); new_line;
	end main;
	```
- Concurrency (*The order in which events may happen is unknown*)
	- No assumption can be made about the order of events
	- Ada uses thread-based concurrency
		- A thread is a sequence of operations (instructions)
		- two threads are concurrent if no assumptions can be made 
		  about the order of operations in one thread relative to the other thread
		  A		W
		  B		X
		  C		Y
		  D		Z
	- Consumer/Producer problem