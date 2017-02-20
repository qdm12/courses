# Programming language course, Spring 2017

## Lesson 4: Passing parameters

```ada
task Task 1;
task body Task 1 is:
begin
    ...
    Task2.E(6);
    ...

task Task2 is:
    entry E(x:integer);
end Task2;
task body Task2 is:
begin
    ...
    accept E(x:integer)
    do                -- scope
        ...            -- of
    end;            -- x
    ...
```

### Task type
```ada
task type MyTask is
    entry Go;
end
task body MyTask is
begin
    ...
end

T1: MyTask;
T2: MyTask;
A:array(1..50) of MyTask
T1.GO;
T2.GO;
```


### Math
```
f(x) = x^2 + 2  # Don't need to think about
Let y = 10        # how y is passed to x
f(y)
```
For paramater passing mechanisms:
1. Pass by value
    - The value of the actual parameter is copied to the formal parameter.
    - A new memory location is assigned for the formal parameter
2. Pass by reference
    - The **address** of the actual parameter is passed into the formal parameter.
    - Any reference to the formal parameter follows the address back to the actual parameter.    
    - In imperative languages, variables are **memory locations**.
    - Java's objects have *pointer semantics*
        - The **value** of an object is its address
3. Pass by value result "*copy in, copy out*"
    - Upon procedure call, copy the values at the actual params to the corresponding formal parameters
    - Upon procedure return, copy the values of the formal parameters back to the actual parameters.
4. Pass by name
    - The semantics of a function call is defined by **textual substitution**
    - The "Algo Copy Paste"
        1. Replace a function call with the body of the function definition, renaming variables at the call site to avoid name conflicts
        2. Replace all occurences of the formal parameters in the function body with the actual parameters, renaming local variables in the function body to avoid name conflicts
           ```ada
           procedure f(x:integer, y:integer)
           begin
               y = x * 2;
               y = y + 1;
           end;
           
           z:integer := 15;
           w:integer;
           begin
               z := z + 1;
               f(z+3, w) -- replace that by y = x * 2 => w = (z+3)*2
                         --                 y = y + 1    w = w + 1
               print(w);
           end;
    

    