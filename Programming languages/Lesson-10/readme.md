# Programming language course, Spring 2017

## Lesson 10: ML

- You can check the latex document in this directory
- You can check the SML file in this directory
- You can read the ML code below:
```sml
(* Basic types: int, real, string *)
- 5; (* val it = 5 : int *)
- 5.9; (* val it = 5.9 : real *)
- "hello"; (* val it = "hello" : string *)

(* Aggregate types: list, tuple *)
- [1,2,3]; (* IMPORTANT: The ";" is not part of the language *)
val it = [1,2,3] : int list
- [[3.4,6.7],[8.9]];
val it = [[3.4,6.7],[8.9]] : real list list

(* Lists are homogeneous: all the elements must be of the same type *)
- [1,2,3.4, "goodbye"] ; (* Gives an error: operator and operand don't agree *)

(* A tuple is like a record, where the fields are accessed by position *)
- (3, "one", 2.4) ;
val it = (3,"one",2.4) : int * string * real

(* Defining variables *)
- val x = 3 * 6; (* val x = 18 : int *)

(* Defining functions *)
- fun f x y = x + y; 
val f = fn : int -> int -> int
- fun f x = if x = 0 then 1 else x * f (x-1);
val f = fn : int -> int

(* ML functions are CURRIED:  No matter how many parameters are declared, 
   a function can be applied to a single argument, returning a function 
   taking the next argument, and so on *)
- fun g x y = x + y;  (* g takes a parameter x and returns a function taking 
                         a parameter y and evaluates x + y *)
val g = fn : int -> int -> int
- g 3 4;  (* both parameters at once *)
val it = 7 : int
- g 3; (* returns a function taking the next parameter *)
val it = fn : int -> int
- val h = g 3;  (* defining h to be the result of g 3 makes h a function *)
val h = fn : int -> int
- h 4; (* val it = 7 : int *)
- fun g x y z = x * (y+z);
val g = fn : int -> int -> int -> int

(* defining functions using PATTERN MATCHING *)
- fun fac 0 = 1
=  |  fac n = n * fac (n-1) ;
val fac = fn : int -> int

(* Going back to lists: cons is written :: and append is written @ *)
- 3 :: [4,56]; (* val it = [3,4,56] : int list *)
- 3.2 :: [4,5,6];  (* ERROR *)
- [1,2,3] @ [4,5,6]; (* val it = [1,2,3,4,5,6] : int list *)
(* cons and append are purely functional and don't change their arguments *)
- val l1 = [1,2,3];
- val l2 = [4,5,6];
- l1 @ l2; (* val it = [1,2,3,4,5,6] : int list *)
- l1 (* val it = [1,2,3] : int list *)

(* :: can be used as a pattern in a function definition *)
- fun f [] = 0
=  |  f (x::xs) = x + f xs; (* computes the sum of the elements of an int list *)
val f = fn : int list -> int
- f [3,4,5,6];
val it = 18 : int

- fun length [] = 0  (* what is the type of length? *)
=  |  length (y::rest) = 1 + length rest;
val length = fn : 'a list -> int
(* Note that it can take a list of any type. That is, for all types 'a ("alpha"),
   length is of type 'a list -> int. Any function with a type variable, 
   e.g. 'a, in its type is POLYMORPHIC *)
- length [[1,2],[3,4]]; (* val it = 2 : int *)

(* What is the type of this function? *)
- fun g (x::xs) = x;  
stdIn:40.5-40.18 Warning: match nonexhaustive
          x :: xs => ...
val g = fn : 'a list -> 'a

(* ML has higher order functions *)
- fun h f x = f (x+1) * 2;
val h = fn : (int -> int) -> int -> int
- fun h f x = f x * 2;  (* h is polymorphic *)
val h = fn : ('a -> int) -> 'a -> int

(* defining map (polymorphic) *)
- fun map f [] = []
=  |  map f (z::zs) = f z :: map f zs  ;
val map = fn : ('a -> 'b) -> 'a list -> 'b list

- (* What is the type of the compose function? *)
- fun compose f g x = f (g x)  ;
val compose = fn : ('a -> 'b) -> ('c -> 'a) -> 'c -> 'b

- (* LAMBDA expressions are written: fn <param> => <body> *)
- fn x => x + 1;
val it = fn : int -> int
- (fn x => x + 1) 7; (* val it = 8 : int *)
- fun f x = fn y => x + y;
val f = fn : int -> int -> int
- f 5 7; (* val it = 12 : int *)

(* Tuples can be used in patterns *)
- fun foo (y,z) = if y = 3 then z else "no"  ;
val foo = fn : int * string -> string
- val x = (3, "hello") ;
val x = (3,"hello") : int * string
- foo x; (* val it = "hello" : string *)

- []; (* Not a function, but is polymorphic *)
val it = [] : 'a list

(* The identity function is the only terminating function of type 'a -> 'a *)
- fun f x = x;

(* Non-terminating function of type 'a -> 'a *)
- fun g x = if true then g x else x ; 
val g = fn : 'a -> 'a

(* You can declare the types of parameters *)
- fun f (x:real) y = x + y ;
val f = fn : real -> real -> real

(* Patterns can be used in simultanenous variable definitions *)
- val (x,y) = (4, 3.5);
val x = 4 : int
val y = 3.5 : real
- val (x::xs) = [1,2,3,4]  ;
val x = 1 : int
val xs = [2,3,4] : int list

(* Defining nested variables and functions using a let *)
- fun g x =
=   let val y = x * 2
=       fun h z = z * y
=   in h x 
=   end;
val g = fn : int -> int

(* Use "and" for mutually recursive functions *)
- fun f x = if x = 0 then 1 else x * g (x-1)
= and 
=     g 0 = 1
=  |  g n = n * f (n-1);
val f = fn : int -> int
val g = fn : int -> int

(* Boolean operators "andalso" and "orelse" *)
- true andalso false; (* false *)
- true orelse false; (* true *)

(* Use "datatype" to define a new type, enumerating all the elements of the new type *)
- datatype stoplight = red | green | yellow;
- red; (* val it = red : stoplight *)
- (* These values can be used as patterns *)
- fun drive red = "stop"
=  |  drive green = "go"
=  |  drive yellow = "go faster"  ;
val drive = fn : stoplight -> string

(* Associating values with each alternative in a datatype declaration *)
- datatype vehicle = car of int | truck of bool | boat of int list;
- car 6; (* val it = car 6 : vehicle *)
- truck true; (* val it = truck true : vehicle *)
- boat [1,2,3]; (* val it = boat [1,2,3] : vehicle *)
(* These can also be used in patterns to define functions *)
- fun silly (car x) = x*2
=  |  silly (truck y) = if y then 3 else 4
=  |  silly (boat z) = length z;
val silly = fn : vehicle -> int
- silly (car 7); (* val it = 14 : int *)
- silly (boat [1,2,3,4]); (* val it = 4 : int *)

(* Datatypes can be recursive *)
- datatype tree = leaf of int | node of tree * tree;
- val mytree = node (node (leaf 3, leaf 4), leaf 5); (* Constructing a tree *)

(* fringe returns a list of the labels associated with the leaves of a tree *)
- fun fringe (leaf x) = [x]
=  |  fringe (node (left,right)) = fringe left @ fringe right;
val fringe = fn : tree -> int list
- fringe mytree; (* val it = [3,4,5] : int list *)

(* Datatypes can be polymorphic *)
- datatype 'a tree = leaf of 'a | node of 'a tree * 'a tree;
- leaf 5; (* val it = leaf 5 : int tree *)
- leaf ["hello"]; (* val it = leaf ["hello"] : string list tree*)

(* Now fringe would be polymorphic *)
- fun fringe (leaf x) = [x]
=  |  fringe (node (left,right)) = fringe left @ fringe right;
val fringe = fn : 'a tree -> 'a list

- (* Using infix operators as functions *)
- (op +)(3,4); (* val it = 7 : int *)
- fun f g = g(3,4);
val f = fn : (int * int -> 'a) -> 'a
- f (op +); (* val it = 7 : int *)
(* Declaring a parameter to a function as an infix symbol *)
- fun f (op <) x y = x < y;
val f = fn : ('a * 'b -> 'c) -> 'a -> 'b -> 'c
- f (op +) 4 5; (* val it = 9 : int *)
- f (fn (a,b) => a::b) 4 [5,6,7];
val it = [4,5,6,7] : int list
(* Defining your own infix operators *)
- infix =*=;
- fun x =*= y = (x*2)+y;
val =*= = fn : int * int -> int
- 3 =*= 4; (* val it = 10 : int *)
(* Using =*= with function syntax *)
- (op =*=)(3,4); (* val it = 10 : int *)
(* Passing =*= as a parameter *)
- f (op =*=) 3 4; (* val it = 10 : int *)
(* Another example *)
- infix ++;
- fun a ++ b = a + b;
val ++ = fn : int * int -> int
- fun (op ++)(a,b) = a + b;
```